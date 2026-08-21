"""A preset's sensitivity is a datasheet figure, and it cannot outlive its own noise floor.

Each preset's sensitivity is kTB for its bandwidth, plus the receiver noise figure, plus the modem's
required SNR - so it is a statement about a *thermal* noise floor. Combining it with a measured or
fitted `NOISE_LEVEL` double-counts: raising the floor by 9.5 dB and keeping the sensitivity says the
modem decodes 9.5 dB below its own limit. On the packaged Batumi calibration that made LONG_FAST's
weakest audible link sit 3.5 dB under what SF11 can demodulate, and LONG_SLOW's 6.5 dB under.
"""

import math
import unittest

from lib.config import Config
from lib.phy import (
    REQUIRED_SNR_DB,
    effective_cad_threshold,
    effective_sensitivity,
    required_snr_db,
    thermal_noise_floor,
)


class ThePresetTableIsBuiltFromPublishedNumbers(unittest.TestCase):
    def test_thermal_noise_follows_bandwidth(self):
        # kTB at 290 K is -174 dBm/Hz; doubling the bandwidth costs 3 dB.
        self.assertAlmostEqual(thermal_noise_floor(125e3, 0.0), -174 + 10 * math.log10(125e3), places=6)
        self.assertAlmostEqual(
            thermal_noise_floor(250e3, 0.0) - thermal_noise_floor(125e3, 0.0), 3.01, places=2
        )

    def test_each_preset_sensitivity_is_thermal_plus_noise_figure_plus_required_snr(self):
        """The consistency this exposes: the table is internally coherent at a thermal floor."""
        for name in ("SHORT_TURBO", "SHORT_FAST", "MEDIUM_FAST", "LONG_FAST", "LONG_SLOW"):
            with self.subTest(preset=name):
                conf = Config()
                conf.MODEM_PRESET = name
                preset = conf.current_preset
                implied = (
                    thermal_noise_floor(preset["bw"]) + required_snr_db(preset["sf"])
                )
                # Within a decibel of the datasheet figure the preset table carries.
                self.assertLess(abs(implied - preset["sensitivity"]), 1.0)

    def test_every_preset_spreading_factor_has_a_published_floor(self):
        conf = Config()
        for name, preset in conf.MODEM_PRESETS.items():
            with self.subTest(preset=name):
                self.assertIn(preset["sf"], REQUIRED_SNR_DB)


class AnElevatedNoiseFloorRaisesTheThreshold(unittest.TestCase):
    def test_the_default_configuration_does_not_move(self):
        """Inert where it should be: every deployed preset keeps its datasheet figure."""
        for name in ("SHORT_TURBO", "SHORT_FAST", "SHORT_SLOW", "MEDIUM_FAST", "MEDIUM_SLOW",
                     "LONG_TURBO", "LONG_FAST", "LONG_MODERATE", "LONG_SLOW"):
            with self.subTest(preset=name):
                conf = Config()
                conf.MODEM_PRESET = name
                self.assertEqual(
                    effective_sensitivity(conf), conf.current_preset["sensitivity"]
                )

    def test_the_batumi_noise_floor_tightens_it(self):
        conf = Config()
        conf.MODEM_PRESET = "LONG_FAST"
        conf.NOISE_LEVEL = -110.5
        # -110.5 dBm of ambient noise, SF11 needing -17.5 dB: -128.0 dBm, not -131.5.
        self.assertAlmostEqual(effective_sensitivity(conf), -128.0, places=6)
        self.assertGreater(effective_sensitivity(conf), conf.current_preset["sensitivity"])

    def test_a_quieter_than_thermal_floor_cannot_help(self):
        """The receiver's own noise dominates below thermal, so the datasheet figure holds."""
        conf = Config()
        conf.MODEM_PRESET = "LONG_FAST"
        conf.NOISE_LEVEL = -140.0
        self.assertEqual(effective_sensitivity(conf), conf.current_preset["sensitivity"])

    def test_no_audible_link_is_below_the_modems_own_limit(self):
        """The invariant this exists for, over every preset and both noise floors."""
        for noise in (None, -110.5, -105.0, -120.0):
            for name in ("SHORT_TURBO", "MEDIUM_FAST", "LONG_FAST", "LONG_SLOW"):
                with self.subTest(preset=name, noise=noise):
                    conf = Config()
                    conf.MODEM_PRESET = name
                    if noise is not None:
                        conf.NOISE_LEVEL = noise
                    weakest_snr = effective_sensitivity(conf) - conf.NOISE_LEVEL
                    self.assertGreaterEqual(
                        weakest_snr, required_snr_db(conf.current_preset["sf"]) - 1e-9,
                        "the simulator admitted a link the modem cannot demodulate",
                    )

    def test_the_cad_floor_keeps_its_margin(self):
        conf = Config()
        conf.MODEM_PRESET = "LONG_FAST"
        preset = conf.current_preset
        margin = preset["sensitivity"] - preset["cad_threshold"]
        self.assertAlmostEqual(
            effective_sensitivity(conf) - effective_cad_threshold(conf), margin, places=6
        )
        conf.NOISE_LEVEL = -110.5
        self.assertAlmostEqual(
            effective_sensitivity(conf) - effective_cad_threshold(conf), margin, places=6
        )


if __name__ == "__main__":
    unittest.main()
