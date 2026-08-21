"""Packaged real-mesh scenario presets.

Presets keep small, reproducible field snapshots in the tree so PHY and
collision-model changes can be compared without depending on live map services
or other runtime inputs.
"""

import csv
import math
from pathlib import Path

import yaml

from lib.node import node_configs_from_yaml, origin_from_yaml
from lib.terrain import TerrainGrid


PRESET_ROOT = Path(__file__).resolve().parents[1] / "presets"

PRESETS = {
    "batumi": {
        # Real Batumi node geometry with matching terrain, which loraMesh.py enables
        # automatically so path-loss experiments carry the local ridge and sea shape.
        "nodes": PRESET_ROOT / "batumi.yaml",
        "terrain": PRESET_ROOT / "batumi_terrain.csv",
        "clutter": PRESET_ROOT / "batumi_clutter.csv",
    },
}

RADIO_CALIBRATION_FIELDS = (
    "NOISE_LEVEL",
    "PATH_LOSS_DISTANCE_FLOOR_M",
    "REPORTED_SNR_MIN_DB",
    "REPORTED_SNR_MAX_DB",
    "LINK_CALIBRATION_MODEL_ENABLED",
    "LINK_CALIBRATION_COEFFICIENTS",
    "LINK_CALIBRATION_SNR_MIN_DB",
    "LINK_CALIBRATION_SNR_MAX_DB",
    "LINK_CALIBRATION_MAX_M",
)


def available_presets():
    return sorted(PRESETS.keys())


def preset_paths(name):
    try:
        return PRESETS[name]
    except KeyError as err:
        raise ValueError(f"unknown preset: {name}") from err


def load_preset_raw(name):
    paths = preset_paths(name)
    with paths["nodes"].open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_preset_node_configs(name, period):
    return node_configs_from_yaml(load_preset_raw(name), period)


def preset_radio_calibration(name):
    raw = load_preset_raw(name)
    return raw.get("radio_calibration", {}) if isinstance(raw, dict) else {}


def preset_calibration_observations(name):
    raw = load_preset_raw(name)
    return raw.get("calibration_observations", []) if isinstance(raw, dict) else []


def snapshot_radio_calibration(conf):
    """Capture caller-default radio calibration so reusable CLI parses reset cleanly."""
    snapshot = {}
    for field in RADIO_CALIBRATION_FIELDS:
        value = getattr(conf, field)
        snapshot[field] = value.copy() if isinstance(value, dict) else value
    return snapshot


def restore_radio_calibration(conf, snapshot):
    for field, value in snapshot.items():
        setattr(conf, field, value.copy() if isinstance(value, dict) else value)


def apply_preset_radio_calibration(conf, name):
    """Apply the aggregate radio calibration packaged with a preset.

    It lives with presets so it cannot change a generic run. See docs/batumi_radio_calibration.md.
    """
    calibration = preset_radio_calibration(name)

    fields = {
        "noise_level": "NOISE_LEVEL",
        "path_loss_distance_floor_m": "PATH_LOSS_DISTANCE_FLOOR_M",
        "reported_snr_min_db": "REPORTED_SNR_MIN_DB",
        "reported_snr_max_db": "REPORTED_SNR_MAX_DB",
    }
    if calibration:
        for source_name, config_name in fields.items():
            if source_name in calibration:
                setattr(conf, config_name, float(calibration[source_name]))

    # The envelope comes from the observations, not from the coefficient block: a fit's support is
    # a property of the data it saw.
    conf.LINK_CALIBRATION_MAX_M = preset_calibration_envelope_m(name)

    link_model = calibration.get("link_calibration_model", {}) if calibration else {}
    conf.LINK_CALIBRATION_MODEL_ENABLED = bool(link_model)
    conf.LINK_CALIBRATION_COEFFICIENTS = {
        str(key): float(value)
        for key, value in link_model.get("coefficients", {}).items()
    }
    conf.LINK_CALIBRATION_SNR_MIN_DB = None
    conf.LINK_CALIBRATION_SNR_MAX_DB = None
    if "snr_min_db" in link_model:
        conf.LINK_CALIBRATION_SNR_MIN_DB = float(link_model["snr_min_db"])
    if "snr_max_db" in link_model:
        conf.LINK_CALIBRATION_SNR_MAX_DB = float(link_model["snr_max_db"])


def preset_calibration_envelope_m(name):
    """The longest link the fit was actually trained on, from its own observations.

    Derived rather than declared, so it cannot disagree with the observation list beside it.
    """
    raw = load_preset_raw(name)
    if not isinstance(raw, dict):
        return None
    nodes = raw.get("nodes") or {}
    points = {}
    for index, node in enumerate(nodes.values()):
        points[index] = (float(node["x"]), float(node["y"]))

    lengths = []
    for observation in raw.get("calibration_observations") or []:
        source, target = observation.get("from"), observation.get("to")
        if source in points and target in points:
            (x0, y0), (x1, y1) = points[source], points[target]
            lengths.append(math.dist((x0, y0), (x1, y1)))
    return max(lengths) if lengths else None


def preset_origin(name):
    return origin_from_yaml(load_preset_raw(name))


def preset_terrain_grid(name):
    terrain_path = preset_paths(name).get("terrain")
    if terrain_path and terrain_path.exists():
        return terrain_path
    return None


def load_preset_terrain_grid(name):
    terrain_path = preset_terrain_grid(name)
    if terrain_path is None:
        return None
    with terrain_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return TerrainGrid.from_rows(
            (
                row["x_m"],
                row["y_m"],
                row["elevation_m"],
            )
            for row in reader
        )


def preset_calibration_diagnostics(name):
    """What the packaged fit's own observations can support, measured from them.

    A reader deciding whether to trust a link set needs to know the fit is a level-matching surface
    over features that do not correlate with the observations, not a propagation model.
    """
    raw = load_preset_raw(name)
    return raw.get("calibration_diagnostics", {}) if isinstance(raw, dict) else {}


def preset_clutter_provenance(name):
    """What the packaged clutter raster is, and what is known to be wrong with it.

    Recorded rather than assumed: the raster cannot be regenerated without Overpass, and a reader
    comparing water_fraction coefficients needs to know the class never varies.
    """
    raw = load_preset_raw(name)
    return raw.get("clutter_provenance", {}) if isinstance(raw, dict) else {}


def preset_clutter_grid(name):
    clutter_path = preset_paths(name).get("clutter")
    if clutter_path and clutter_path.exists():
        return clutter_path
    return None
