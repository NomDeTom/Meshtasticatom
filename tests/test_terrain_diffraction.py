"""Diffraction loss is continuous in clearance, and grazing costs 6 dB.

TERRAIN_FRESNEL_CLEARANCE was added into the obstruction height and then used to compute the
knife-edge parameter from it. The first Fresnel radius is exactly the reciprocal of v's own scaling,
so that offset v by a constant 0.6*sqrt(2) = 0.849: a grazing path was charged 12.91 dB against a
true 6.03, and the loss stepped from 0 to 6.03 dB across an arbitrarily small change in geometry -
right where marginal links sit.
"""

import math
import unittest

from lib.config import Config
from lib.terrain import TerrainGrid, knife_edge_loss_db, terrain_obstruction_loss
from lib.point import Point


class KnifeEdgeCurve(unittest.TestCase):
    def loss_at(self, clearance_in_fresnel_radii):
        """The ITU curve at a clearance expressed in first-Fresnel-zone radii."""
        return knife_edge_loss_db(-clearance_in_fresnel_radii * math.sqrt(2.0))

    def test_grazing_costs_six_decibels(self):
        self.assertAlmostEqual(self.loss_at(0.0), 6.03, places=2)

    def test_a_cleared_path_costs_nothing(self):
        for clearance in (0.6, 0.8, 1.0, 2.0):
            with self.subTest(clearance=clearance):
                self.assertEqual(self.loss_at(clearance), 0.0)

    def test_the_curve_is_continuous_across_the_clearance_threshold(self):
        """No step at 0.6*F1: the ITU approximation is already zero there."""
        just_clear = self.loss_at(0.601)
        just_short = self.loss_at(0.599)
        self.assertEqual(just_clear, 0.0)
        self.assertLess(abs(just_short - just_clear), 0.01)

    def test_loss_rises_as_clearance_falls(self):
        previous = 0.0
        for clearance in (0.4, 0.2, 0.0, -0.2, -0.5, -1.0):
            loss = self.loss_at(clearance)
            self.assertGreaterEqual(loss, previous)
            previous = loss


class OverARealProfile(unittest.TestCase):
    def conf_with_ridge(self, ridge_height_m):
        """A 10 km path with one hill at the midpoint, on a grid coarse enough to be flat elsewhere."""
        conf = Config()
        conf.TERRAIN_ENABLED = True
        conf.GEO_ORIGIN_LAT, conf.GEO_ORIGIN_LON = 0.0, 0.0
        rows = []
        for x in range(-12000, 12001, 1000):
            for y in (-1000, 0, 1000):
                elevation = ridge_height_m if x == 0 else 0.0
                rows.append((float(x), float(y), elevation))
        conf.TERRAIN_GRID = TerrainGrid.from_rows(rows)
        return conf

    def test_a_clear_path_over_flat_ground_costs_nothing(self):
        conf = self.conf_with_ridge(0.0)
        tx = Point(-5000.0, 0.0, 400.0)
        rx = Point(5000.0, 0.0, 400.0)
        self.assertEqual(terrain_obstruction_loss(conf, tx, rx, conf.FREQ), 0.0)

    def test_a_ridge_through_the_path_costs_more_than_one_grazing_it(self):
        blocking = self.conf_with_ridge(600.0)
        grazing = self.conf_with_ridge(0.0)
        tx = Point(-5000.0, 0.0, 300.0)
        rx = Point(5000.0, 0.0, 300.0)
        blocked_loss = terrain_obstruction_loss(blocking, tx, rx, blocking.FREQ)
        clear_loss = terrain_obstruction_loss(grazing, tx, rx, grazing.FREQ)
        self.assertGreater(blocked_loss, clear_loss)
        self.assertGreater(blocked_loss, 6.0)

    def test_loss_is_capped(self):
        conf = self.conf_with_ridge(5000.0)
        tx = Point(-5000.0, 0.0, 10.0)
        rx = Point(5000.0, 0.0, 10.0)
        self.assertLessEqual(
            terrain_obstruction_loss(conf, tx, rx, conf.FREQ), conf.TERRAIN_MAX_LOSS_DB
        )


if __name__ == "__main__":
    unittest.main()
