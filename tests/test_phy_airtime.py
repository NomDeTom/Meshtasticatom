"""Airtime vectors.

The three LoRaWAN cases are external ground truth - a published calculator, not this formula
rearranged - and the preset table locks every shipped Meshtastic setting against regression.
"""

import unittest

from lib.config import Config
from lib.phy import airtime


def lorawan_conf():
    """A config shaped like the published calculators: 8 preamble symbols, no extra header."""
    conf = Config()
    conf.NPREAM = 8
    conf.HEADERLENGTH = 0
    return conf


# Meshtastic presets at a 40-byte payload, 16 preamble symbols, 16 header bytes.
PRESET_AIRTIME_MS = {
    "SHORT_TURBO": 28.992,
    "SHORT_FAST": 57.984,
    "SHORT_SLOW": 105.728,
    "MEDIUM_FAST": 190.976,
    "MEDIUM_SLOW": 361.472,
    "LONG_TURBO": 476.160,
    "LONG_FAST": 681.984,
    "LONG_MODERATE": 2166.784,
    "LONG_SLOW": 4071.424,
    "VERY_LONG_SLOW": 8142.848,
}


class TestAirtimeAgainstPublishedVectors(unittest.TestCase):
    def test_sf7_bw125_cr45_13_bytes(self):
        # LoRaWAN reference: 46.336 ms.
        self.assertAlmostEqual(airtime(lorawan_conf(), 7, 5, 13, 125e3), 46.336, places=3)

    def test_sf12_bw125_cr45_13_bytes(self):
        # LoRaWAN reference: 1155.072 ms, low data rate optimization on.
        self.assertAlmostEqual(airtime(lorawan_conf(), 12, 5, 13, 125e3), 1155.072, places=3)

    def test_sf12_bw125_cr45_64_bytes(self):
        # LoRaWAN reference: a 51-byte application payload under a 13-byte header, 2793.472 ms.
        self.assertAlmostEqual(airtime(lorawan_conf(), 12, 5, 64, 125e3), 2793.472, places=3)


class TestCodingRateIsADenominator(unittest.TestCase):
    def test_payload_symbols_scale_with_the_denominator(self):
        conf = lorawan_conf()
        preamble = (conf.NPREAM + 4.25) * (2.0**7) / 125e3 * 1000
        symbol_ms = (2.0**7) / 125e3 * 1000

        # 4/8 sends eight symbols per block where 4/5 sends five, so the payload grows 8/5.
        slim = (airtime(conf, 7, 5, 13, 125e3) - preamble) / symbol_ms - 8
        robust = (airtime(conf, 7, 8, 13, 125e3) - preamble) / symbol_ms - 8
        self.assertAlmostEqual(robust / slim, 8 / 5, places=9)

    def test_every_denominator_is_accepted_and_ordered(self):
        conf = Config()
        times = [airtime(conf, 11, cr, 40, 250e3) for cr in (5, 6, 7, 8)]
        self.assertEqual(times, sorted(times))


class TestLowDataRateOptimization(unittest.TestCase):
    """RadioLibInterface.h gates LDRO on symbol time >= 16 ms, not on a bandwidth."""

    def test_enabled_where_the_symbol_is_long_enough(self):
        conf = Config()
        for sf, bw in ((11, 125e3), (12, 125e3), (12, 62.5e3), (12, 250e3)):
            with self.subTest(sf=sf, bw=bw):
                self.assertGreaterEqual((2.0**sf) / bw * 1000, 16)
                self.assertEqual(self.de_used(conf, sf, bw), 1)

    def test_disabled_where_it_is_not(self):
        conf = Config()
        for sf, bw in ((10, 125e3), (11, 250e3), (11, 500e3), (7, 125e3)):
            with self.subTest(sf=sf, bw=bw):
                self.assertLess((2.0**sf) / bw * 1000, 16)
                self.assertEqual(self.de_used(conf, sf, bw), 0)

    @staticmethod
    def de_used(conf, sf, bw):
        """Recover the DE the formula applied, by finding which value reproduces the airtime."""
        import math

        pl = 40 + conf.HEADERLENGTH
        Tsym = (2.0**sf) / bw
        measured = airtime(conf, sf, 5, 40, bw)
        for de in (0, 1):
            symbols = 8 + max(
                math.ceil((8.0 * pl - 4.0 * sf + 28 + 16) / (4.0 * (sf - 2 * de))) * 5, 0
            )
            expected = ((conf.NPREAM + 4.25) * Tsym + symbols * Tsym) * 1000
            if abs(expected - measured) < 1e-9:
                return de
        raise AssertionError("airtime matches neither DE=0 nor DE=1")


class TestShippedPresets(unittest.TestCase):
    def test_every_preset_matches_its_locked_airtime(self):
        conf = Config()
        self.assertEqual(set(conf.MODEM_PRESETS), set(PRESET_AIRTIME_MS))
        for name, preset in conf.MODEM_PRESETS.items():
            with self.subTest(preset=name):
                self.assertAlmostEqual(
                    airtime(conf, preset["sf"], preset["cr"], 40, preset["bw"]),
                    PRESET_AIRTIME_MS[name],
                    places=3,
                )


if __name__ == "__main__":
    unittest.main()
