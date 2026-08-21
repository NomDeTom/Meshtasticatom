"""The interference level is a duty cycle, and has to behave like one at both ends.

It was an independent draw per point of use, which made it a probability with no holding time: a
transmitter re-rolling its CAD found the channel clear within a few attempts however high the level,
and a receiver drew separately, so the two ends could disagree about the same instant.
"""

import unittest

from lib.config import Config
from lib.interference import ExternalInterference, build as interference_for
from lib.phy import is_channel_active


class FakeNode:
    """What is_channel_active reads, with no packets to sense."""

    def __init__(self, conf):
        self.conf = conf
        self.nodeid = 0
        self.packets = []
        self.interference = interference_for(conf, conf.SEED, self.nodeid)


class FakeEnv:
    def __init__(self, now=0.0):
        self.now = now


class TestChannelBusyShare(unittest.TestCase):
    SAMPLES = 20_000

    def busy_fraction(self, level):
        """Sampled across the run, because a duty cycle is a share of time, not of draws."""
        conf = Config()
        conf.INTERFERENCE_LEVEL = level
        node = FakeNode(conf)
        env = FakeEnv()
        busy = 0
        for i in range(self.SAMPLES):
            env.now = conf.SIMTIME * i / self.SAMPLES
            busy += is_channel_active(node, env)
        return busy / self.SAMPLES

    def test_zero_is_never_busy(self):
        """A level of 0.00 used to report busy about a tenth of the time; then, briefly, 0%
        of draws but with no channel behind it at all."""
        self.assertEqual(self.busy_fraction(0.0), 0.0)

    def test_one_is_always_busy(self):
        self.assertEqual(self.busy_fraction(1.0), 1.0)

    def test_intermediate_levels_land_on_the_level(self):
        for level in (0.05, 0.1, 0.5, 0.9):
            with self.subTest(level=level):
                self.assertAlmostEqual(self.busy_fraction(level), level, delta=0.02)


class TestBusyStretchesHaveALength(unittest.TestCase):
    def test_a_busy_channel_stays_busy_for_a_while(self):
        """The point of a holding time: a busy instant is part of a stretch, not an isolated draw."""
        field = ExternalInterference(0.5, 600_000, 682.0, 3)
        self.assertGreater(len(field._starts), 0)
        lengths = [end - start for start, end in zip(field._starts, field._ends)]
        self.assertAlmostEqual(sum(lengths) / len(lengths), 682.0, delta=120.0)

    def test_the_same_stretch_is_seen_by_cad_and_by_a_reception(self):
        field = ExternalInterference(0.5, 600_000, 682.0, 3)
        start = field._starts[0]
        end = field._ends[0]
        midpoint = (start + end) / 2
        self.assertTrue(field.is_busy(midpoint))
        self.assertTrue(field.overlaps(midpoint, midpoint + 1.0))
        # And a frame wholly inside a gap is not jammed.
        gap_start = end + 1.0
        if len(field._starts) > 1:
            self.assertFalse(field.is_busy(gap_start))
            self.assertFalse(field.overlaps(gap_start, min(gap_start + 1.0, field._starts[1])))

    def test_two_nodes_do_not_share_one_channel_condition(self):
        conf = Config()
        conf.INTERFERENCE_LEVEL = 0.3
        first = interference_for(conf, conf.SEED, 0)
        second = interference_for(conf, conf.SEED, 1)
        self.assertNotEqual(first._starts[:5], second._starts[:5])


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
