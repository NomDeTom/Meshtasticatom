"""Region tables and frequency slots, pinned to firmware 2.8 (version.properties 2.8.0, 51eadb7).

The published default frequencies are the check that matters: a slot calculation can be wrong in
several ways and still produce a number inside the band.
"""

import unittest

from lib.config import Config, djb2_hash


class TestRegionTableMatchesItsPin(unittest.TestCase):
    """UA_868 was removed in 2.8 and the ITU ham regions were added; the set dates the table."""

    ADDED_IN_2_8 = (
        "EU_866",
        "EU_N_868",
        "ITU1_2M",
        "ITU1_70CM",
        "ITU2_125CM",
        "ITU2_2M",
        "ITU2_70CM",
        "ITU3_2M",
        "ITU3_70CM",
    )

    def test_the_regions_2_8_added_are_present(self):
        regions = Config().regions
        for name in self.ADDED_IN_2_8:
            self.assertIn(name, regions)

    def test_the_region_2_8_removed_is_absent(self):
        self.assertNotIn("UA_868", Config().regions)

    def test_every_region_names_a_profile_that_exists(self):
        conf = Config()
        for name, region in conf.regions.items():
            with self.subTest(region=name):
                self.assertIn(region["profile"], conf.REGION_PROFILES)

    def test_every_profile_lists_presets_that_exist(self):
        conf = Config()
        for name, profile in conf.REGION_PROFILES.items():
            for preset in profile["presets"]:
                with self.subTest(profile=name, preset=preset):
                    self.assertIn(preset, conf.MODEM_PRESETS)

    def test_every_region_defaults_to_a_preset_its_profile_allows(self):
        conf = Config()
        for name, region in conf.regions.items():
            with self.subTest(region=name):
                profile = conf.REGION_PROFILES[region["profile"]]
                self.assertIn(region["default_preset"], profile["presets"])


class TestPublishedDefaultFrequencies(unittest.TestCase):
    """External ground truth: the frequencies a device actually comes up on."""

    def frequency_mhz(self, region, preset):
        conf = Config()
        conf.REGION = conf.regions[region]
        conf.MODEM_PRESET = preset
        return conf.frequency() / 1e6

    def test_us_longfast(self):
        self.assertAlmostEqual(self.frequency_mhz("US", "LONG_FAST"), 906.875, places=3)

    def test_eu_868_longfast(self):
        self.assertAlmostEqual(self.frequency_mhz("EU_868", "LONG_FAST"), 869.525, places=3)

    def test_a_region_with_one_slot_has_one_slot(self):
        conf = Config()
        conf.REGION = conf.regions["EU_868"]
        self.assertEqual(conf.num_freq_slots(), 1)

    def test_the_centre_is_half_a_bandwidth_above_the_band_edge(self):
        """The offset the old calculation omitted, which put every region half a channel low."""
        conf = Config()
        conf.REGION = conf.regions["US"]
        self.assertAlmostEqual(
            conf.frequency(channel_num=1),
            conf.REGION["freq_start"] + conf.current_preset["bw"] / 2,
            places=3,
        )


class TestSlotSelection(unittest.TestCase):
    def test_an_override_slot_wins_over_the_hash(self):
        conf = Config()
        conf.REGION = conf.regions["EU_N_868"]
        conf.MODEM_PRESET = "NARROW_SLOW"
        self.assertEqual(conf.REGION["override_slot"], 1)
        self.assertEqual(conf.default_channel_num(), 0)

    def test_the_default_slot_is_the_hash_of_the_preset_display_name(self):
        conf = Config()
        conf.REGION = conf.regions["US"]
        self.assertEqual(
            conf.default_channel_num("LONG_FAST"),
            djb2_hash("LongFast") % conf.num_freq_slots("LONG_FAST"),
        )

    def test_djb2_matches_the_firmware(self):
        # hash("") is the seed; the rest is hash*33 + c, truncated to 32 bits.
        self.assertEqual(djb2_hash(""), 5381)
        self.assertEqual(djb2_hash("a"), 5381 * 33 + ord("a"))
        self.assertLess(djb2_hash("LongFast"), 1 << 32)


class TestConfigurationsThatDoNotFit(unittest.TestCase):
    def test_a_slot_past_the_end_of_the_band_is_rejected(self):
        conf = Config()
        conf.REGION = conf.regions["EU_868"]
        with self.assertRaises(ValueError):
            conf.frequency(channel_num=27)

    def test_a_preset_the_region_forbids_is_rejected(self):
        """EU_868 carries seven presets; SHORT_TURBO and LONG_TURBO are not among them."""
        conf = Config()
        conf.REGION = conf.regions["EU_868"]
        self.assertFalse(conf.supports_preset("SHORT_TURBO"))
        with self.assertRaises(ValueError):
            conf.frequency(preset="SHORT_TURBO")

    def test_the_last_legal_slot_is_accepted(self):
        conf = Config()
        conf.REGION = conf.regions["US"]
        slots = conf.num_freq_slots()
        self.assertLess(conf.frequency(channel_num=slots), conf.REGION["freq_end"])


if __name__ == "__main__":
    unittest.main()
