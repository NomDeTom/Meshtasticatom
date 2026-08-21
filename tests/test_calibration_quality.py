"""What the packaged fit's own observations can support, recomputed from them.

The Batumi link calibration is a ridge fit over 296 observed neighbour SNRs. Every feature it uses
correlates with those observations at |r| <= 0.1, so its geometric coefficients are fitting noise -
which is why the fitted model is non-monotone in distance inside its own envelope, and why
water_fraction and forest_fraction came out at exactly 0.0.

The preset records those diagnostics. This recomputes them, so the record cannot rot, and pins the
one structural fix that does not need a re-fit: transmit power and antenna gain are applied outside
the fitted surface, decibel for decibel.
"""

import math
import statistics
import unittest

from lib.clutter import clutter_obstruction_loss
from lib.config import Config
from lib.link_model import calculate_link_budget
from lib.phy import free_space_path_loss
from lib.point import Point
from lib.presets import (
    apply_preset_radio_calibration,
    load_preset_node_configs,
    load_preset_terrain_grid,
    preset_calibration_diagnostics,
    preset_calibration_observations,
    preset_clutter_grid,
    preset_origin,
)
from lib.terrain import terrain_ground_elevation, terrain_obstruction_loss


def scenario():
    conf = Config()
    conf.MODEM_PRESET = "LONG_FAST"
    configs = load_preset_node_configs("batumi", conf.PERIOD)
    conf.NR_NODES = len(configs)
    apply_preset_radio_calibration(conf, "batumi")
    conf.GEO_ORIGIN_LAT, conf.GEO_ORIGIN_LON = preset_origin("batumi")
    conf.TERRAIN_ENABLED = True
    conf.TERRAIN_GRID = load_preset_terrain_grid("batumi")
    conf.CLUTTER_ENABLED = True
    conf.CLUTTER_GRID_FILE = str(preset_clutter_grid("batumi"))
    return conf, {c.node_id: c for c in configs}


def pearson(xs, ys):
    n = len(xs)
    mx, my = statistics.mean(xs), statistics.mean(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return cov / (sx * sy)


class TheRecordedDiagnosticsAreTheObservationsOwn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conf, cls.nodes = scenario()
        cls.observed = [
            (o["from"], o["to"], float(o["snr"]))
            for o in preset_calibration_observations("batumi")
            if o.get("from") in cls.nodes and o.get("to") in cls.nodes
        ]
        cls.diagnostics = preset_calibration_diagnostics("batumi")

    def features(self):
        rows = []
        for i, j, snr in self.observed:
            a, b = self.nodes[i], self.nodes[j]
            distance = math.hypot(
                b.position.x - a.position.x, b.position.y - a.position.y
            )
            grounds = [
                terrain_ground_elevation(self.conf, a.position) or 0.0,
                terrain_ground_elevation(self.conf, b.position) or 0.0,
            ]
            rows.append({
                "snr": snr,
                "log10_distance_km": math.log10(max(distance, 1.0) / 1000.0),
                "terrain_loss_db": terrain_obstruction_loss(
                    self.conf, a.position, b.position, self.conf.FREQ
                ),
                "clutter_loss_db": clutter_obstruction_loss(
                    self.conf, a.position, b.position
                ),
                "max_ground_elevation_100m": max(grounds) / 100.0,
            })
        return rows

    def test_the_observation_count_and_range_are_as_recorded(self):
        self.assertEqual(len(self.observed), self.diagnostics["observations"])
        snrs = [snr for _, _, snr in self.observed]
        low, high = self.diagnostics["snr_range_db"]
        self.assertAlmostEqual(min(snrs), low, places=2)
        self.assertAlmostEqual(max(snrs), high, places=2)
        self.assertAlmostEqual(
            statistics.mean(snrs), self.diagnostics["snr_mean_db"], places=2
        )

    def test_no_feature_the_fit_uses_correlates_with_what_it_fits(self):
        rows = self.features()
        snrs = [r["snr"] for r in rows]
        for name, recorded in self.diagnostics["correlations_with_observed_snr"].items():
            with self.subTest(feature=name):
                measured = pearson([r[name] for r in rows], snrs)
                self.assertAlmostEqual(measured, recorded, places=2)
                # The point of recording them: none of these is a relationship.
                self.assertLess(abs(measured), 0.15)

    def test_the_observations_carry_no_distance_law(self):
        """A propagation model is 20-40 dB per decade. These are under one."""
        rows = self.features()
        xs = [r["log10_distance_km"] for r in rows]
        ys = [r["snr"] for r in rows]
        mx, my = statistics.mean(xs), statistics.mean(ys)
        slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum(
            (x - mx) ** 2 for x in xs
        )
        self.assertLess(abs(slope), 5.0)

    def test_every_observation_is_below_free_space(self):
        """Nothing here is physically impossible; there is simply no distance signal to fit."""
        above = 0
        for i, j, snr in self.observed:
            a, b = self.nodes[i], self.nodes[j]
            distance = max(
                1.0,
                math.hypot(b.position.x - a.position.x, b.position.y - a.position.y),
            )
            free_space_snr = (
                self.conf.PTX
                + a.antenna_gain
                + b.antenna_gain
                - free_space_path_loss(distance, self.conf.FREQ)
                - self.conf.NOISE_LEVEL
            )
            if snr > free_space_snr:
                above += 1
        self.assertEqual(above, self.diagnostics["observations_above_free_space"])

    def test_the_preset_says_it_is_not_a_propagation_model(self):
        self.assertTrue(self.diagnostics["is_level_match_not_propagation_model"])


class TransmitPowerIsTransparent(unittest.TestCase):
    """The fix that does not need a re-fit: EIRP is applied outside the fitted surface."""

    class Node:
        def __init__(self, x, y, gain=0.0):
            self.position = Point(x, y, 1.5)
            self.antenna_gain = gain
            self.antenna_height = 1.5

    def test_a_power_cut_arrives_decibel_for_decibel(self):
        conf, _ = scenario()
        tx, rx = self.Node(0.0, 0.0), self.Node(3000.0, 1000.0)
        full = calculate_link_budget(conf, tx, rx)
        for drop in (3, 6, 9, 12):
            with self.subTest(drop=drop):
                cut = calculate_link_budget(conf, tx, rx, tx_power_dbm=conf.PTX - drop)
                self.assertAlmostEqual(full.rssi_dbm - cut.rssi_dbm, drop, places=6)

    def test_antenna_gain_arrives_decibel_for_decibel(self):
        conf, _ = scenario()
        plain = calculate_link_budget(conf, self.Node(0.0, 0.0), self.Node(3000.0, 0.0))
        louder = calculate_link_budget(
            conf, self.Node(0.0, 0.0, gain=6.0), self.Node(3000.0, 0.0, gain=3.0)
        )
        self.assertAlmostEqual(louder.rssi_dbm - plain.rssi_dbm, 9.0, places=6)

    def test_the_packaged_preset_is_unchanged_at_its_own_power(self):
        """Every one of the 92 nodes has 0 dBi, which is the reference, so nothing moved."""
        conf, nodes = scenario()
        for node in nodes.values():
            self.assertEqual(node.antenna_gain, 0.0)
        self.assertEqual(conf.GL, 0)


if __name__ == "__main__":
    unittest.main()
