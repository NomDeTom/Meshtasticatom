"""Shared link-budget calculation for generated radio pairs.

Packet construction, asymmetric-link reporting, and the interactive helper all
need the same answer: what RSSI/SNR does this TX/RX pair get after distance,
terrain, clutter, antenna gains, optional asymmetry, and optional field
calibration? Keeping that in one helper prevents calibration code from becoming
a hidden side path in only one simulator mode.
"""

import math
from dataclasses import dataclass

from lib.clutter import clutter_obstruction_loss, clutter_path_features
from lib.phy import estimate_path_loss
from lib.radio_loss import apply_link_calibration, estimate_snr
from lib.terrain import terrain_ground_elevation, terrain_obstruction_loss


@dataclass(frozen=True)
class LinkBudget:
    distance_m: float
    base_path_loss_db: float
    terrain_loss_db: float
    clutter_loss_db: float
    offset_db: float
    raw_rssi_dbm: float
    rssi_dbm: float
    snr_db: float
    features: dict

    @property
    def calibration_applied(self):
        """Whether the fitted transform answered for this pair, or the raw budget did."""
        return self.rssi_dbm != self.raw_rssi_dbm

    @property
    def path_loss_db(self):
        return self.base_path_loss_db + self.terrain_loss_db + self.clutter_loss_db + self.offset_db

    @property
    def calibrated_path_loss_db(self):
        return self.path_loss_db + self.raw_rssi_dbm - self.rssi_dbm


def _antenna_gain(node):
    """Accept both MeshNode.antennaGain and NodeConfig.antenna_gain."""
    return getattr(node, "antennaGain", getattr(node, "antenna_gain", 0.0))


def _antenna_height(node):
    """Accept runtime and config antenna height above local ground."""
    return getattr(node, "antennaHeight", getattr(node, "antenna_height", node.position.z))


def _link_calibration_features(conf, tx_point, rx_point, raw_snr, terrain_loss, clutter_loss):
    """Build the reusable feature vector a fitted calibration consumes.

    Path-shape features, not pair identities, so a fit carries to meshes with no observed links.
    """
    horizontal_distance_m = max(1.0, math.hypot(rx_point.x - tx_point.x, rx_point.y - tx_point.y))
    log_distance_km = math.log10(horizontal_distance_m / 1000.0)

    tx_ground = terrain_ground_elevation(conf, tx_point)
    rx_ground = terrain_ground_elevation(conf, rx_point)
    grounds = [ground for ground in (tx_ground, rx_ground) if ground is not None]
    max_ground_m = max(grounds) if grounds else 0.0
    min_ground_m = min(grounds) if grounds else 0.0
    ground_delta_m = abs((tx_ground or 0.0) - (rx_ground or 0.0)) if len(grounds) == 2 else 0.0
    high_vantage = 1.0 if max_ground_m >= conf.CLUTTER_HIGH_VANTAGE_ELEVATION_M else 0.0

    clutter_features = clutter_path_features(conf, tx_point, rx_point)
    urban_fraction = clutter_features["urban_fraction"]

    features = {
        "raw_snr_clip": max(-120.0, min(10.0, raw_snr)),
        "log_distance_km": log_distance_km,
        "log_distance_km_sq": log_distance_km * log_distance_km,
        "terrain_loss_db": terrain_loss,
        "clutter_loss_db": clutter_loss,
        "terrain_high_vantage_loss_db": terrain_loss * high_vantage,
        "clutter_urban_loss_db": clutter_loss * urban_fraction,
        "max_ground_elevation_100m": max_ground_m / 100.0,
        "min_ground_elevation_100m": min_ground_m / 100.0,
        "ground_delta_100m": ground_delta_m / 100.0,
        "high_vantage": high_vantage,
        **clutter_features,
    }
    return features


def calculate_link_budget(conf, tx_node, rx_node, offset_db=0.0, tx_power_dbm=None):
    """Calculate raw and calibrated radio budget for one directed pair."""
    tx_point = tx_node.position
    rx_point = rx_node.position
    distance_m = tx_point.euclidean_distance(rx_point)
    base_loss = estimate_path_loss(conf, distance_m, conf.FREQ, _antenna_height(tx_node), _antenna_height(rx_node))
    terrain_loss = terrain_obstruction_loss(conf, tx_point, rx_point, conf.FREQ)
    clutter_loss = clutter_obstruction_loss(conf, tx_point, rx_point)

    raw_path_loss = base_loss + terrain_loss + clutter_loss + offset_db

    # Delivery and the link summary share one budget: an antenna gain at each end, with
    # terrain, clutter and calibration layered on the path between them.
    tx_power = conf.PTX if tx_power_dbm is None else tx_power_dbm
    raw_rssi = tx_power + _antenna_gain(tx_node) + _antenna_gain(rx_node) - raw_path_loss
    raw_snr = raw_rssi - conf.NOISE_LEVEL
    features = _link_calibration_features(conf, tx_point, rx_point, raw_snr, terrain_loss, clutter_loss)
    # Only inside the distances the fit was trained over. A ridge fit extrapolates without
    # complaint, and this one's ground-elevation terms are large, positive and unbounded, so past
    # its evidence two high nodes gain more from elevation than distance takes away and it invents
    # a link. sfpp guarded this from the start; the vendored path did not, so `loraMesh.py --preset
    # batumi` and an sfpp scenario over the same preset were two different link models.
    envelope = getattr(conf, "LINK_CALIBRATION_MAX_M", None)
    if envelope is not None and distance_m > envelope:
        rssi = raw_rssi
    else:
        rssi = apply_link_calibration(conf, raw_rssi, features)

    return LinkBudget(
        distance_m=distance_m,
        base_path_loss_db=base_loss,
        terrain_loss_db=terrain_loss,
        clutter_loss_db=clutter_loss,
        offset_db=offset_db,
        raw_rssi_dbm=raw_rssi,
        rssi_dbm=rssi,
        snr_db=estimate_snr(conf, rssi),
        features=features,
    )
