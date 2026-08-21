"""No module-level config, so nothing can answer for a config the caller did not pass.

`lib/phy.py` used to bind `lib.config.CONFIG` at import and read it from `get_current_slot_time`
and the range helpers. `sfpp.mesh.make_config` had to rebind both to be heard, which left the
process-global carrying whichever scenario ran last - and `python3 -m unittest` from the repo root
failed because sfpp's terrain tests leaked the Batumi calibration into the discrete-event tests.
"""

import unittest

import lib.config
import lib.phy as phy
from lib.config import Config


class NoModuleLevelConfig(unittest.TestCase):
    def test_phy_exposes_no_default_config(self):
        for name in ("conf", "CONFIG", "MAXRANGE"):
            self.assertFalse(
                hasattr(phy, name),
                f"lib.phy.{name} would answer for a config no caller passed",
            )

    def test_slot_time_requires_a_config(self):
        with self.assertRaises(TypeError):
            phy.get_current_slot_time()


class SlotTimeFollowsItsOwnConfig(unittest.TestCase):
    def test_two_presets_give_two_slot_times(self):
        fast, slow = Config(), Config()
        fast.MODEM_PRESET = "SHORT_TURBO"
        slow.MODEM_PRESET = "LONG_SLOW"
        # SF7/BW500 against SF12/BW125: four doublings of SF and two of bandwidth apart.
        self.assertLess(phy.get_current_slot_time(fast), phy.get_current_slot_time(slow))

    def test_max_range_counts_a_gain_at_each_end(self):
        conf = Config()
        plain = phy.estimate_max_range(conf)
        both_ends = phy.estimate_max_range(conf, 3.0, 3.0)
        one_end = phy.estimate_max_range(conf, 3.0)
        self.assertGreater(one_end, plain)
        self.assertGreater(both_ends, one_end)


class SfppDoesNotRebindTheGlobal(unittest.TestCase):
    def test_make_config_leaves_the_shared_config_alone(self):
        from sfpp.mesh import make_config

        before = dict(vars(lib.config.CONFIG))
        conf = make_config(preset="LONG_MODERATE", noise_model="thermal")
        after = dict(vars(lib.config.CONFIG))

        self.assertIsNot(conf, lib.config.CONFIG)
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
