"""The interference level is a probability and has to behave like one at both ends."""

import random
import unittest

from lib.config import Config
from lib.phy import is_channel_active


class FakeNode:
    """The two attributes is_channel_active reads, with no packets to sense."""

    def __init__(self, conf):
        self.conf = conf
        self.nodeid = 0
        self.packets = []


class FakeEnv:
    now = 0.0


class TestChannelBusyDraw(unittest.TestCase):
    DRAWS = 200_000

    def busy_fraction(self, level):
        conf = Config()
        conf.INTERFERENCE_LEVEL = level
        node, env = FakeNode(conf), FakeEnv()
        random.seed(1)
        return sum(is_channel_active(node, env) for _ in range(self.DRAWS)) / self.DRAWS

    def test_zero_is_never_busy(self):
        """The defect this replaces: a level of 0.00 still reported busy about a tenth of the time."""
        self.assertEqual(self.busy_fraction(0.0), 0.0)

    def test_one_is_always_busy(self):
        self.assertEqual(self.busy_fraction(1.0), 1.0)

    def test_intermediate_levels_land_on_the_level(self):
        for level in (0.05, 0.1, 0.5, 0.9):
            with self.subTest(level=level):
                self.assertAlmostEqual(self.busy_fraction(level), level, places=2)


class TestLevelValidation(unittest.TestCase):
    def test_a_probability_outside_the_unit_interval_is_rejected(self):
        conf = Config()
        for bad in (-0.01, 1.01, 10):
            with self.subTest(value=bad):
                with self.assertRaises(ValueError):
                    conf.INTERFERENCE_LEVEL = bad

    def test_the_endpoints_are_accepted(self):
        conf = Config()
        for good in (0, 0.5, 1):
            conf.INTERFERENCE_LEVEL = good
            self.assertEqual(conf.INTERFERENCE_LEVEL, float(good))


if __name__ == "__main__":
    unittest.main()
