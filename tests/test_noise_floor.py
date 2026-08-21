"""The noise floor moves, and the thresholds derived from it move with it.

kTB plus a noise figure is what a band would be with nothing in it - a lower bound, not a
description. A real receiver sits in whatever the band is doing, so the floor is a distribution with
a median well above thermal and several decibels of spread. Collapsing it to one constant and using
it as a hard cut turns a link that is up at 3 a.m. and down at 6 p.m. into a link that either exists
or does not, which removes exactly the marginal connectivity that decides whether a mesh holds
together.

Default spread is zero, so nothing moves until a scenario asks for it.
"""

import math
import statistics
import unittest

from lib.config import Config
from lib.noise import NoiseFloor, build as noise_floor_for
from lib.phy import effective_cad_threshold, effective_sensitivity, thermal_noise_floor


class AConstantFloorIsExactlyConstant(unittest.TestCase):
    def test_zero_spread_never_varies(self):
        floor = noise_floor_for(Config(), 3)
        levels = {round(floor.level_at(t), 9) for t in range(0, 600_000, 977)}
        self.assertEqual(len(levels), 1)

    def test_the_default_configuration_keeps_its_own_noise_level(self):
        """The clamp is kTB, not kTB+NF: the noise figure is already inside the sensitivity table."""
        conf = Config()
        self.assertEqual(noise_floor_for(conf, 0).level_at(0.0), conf.NOISE_LEVEL)

    def test_nothing_can_be_quieter_than_thermal(self):
        conf = Config()
        conf.NOISE_LEVEL = -150.0  # far below kTB for any bandwidth
        floor = noise_floor_for(conf, 0)
        kTB = thermal_noise_floor(conf.current_preset["bw"], noise_figure_db=0.0)
        self.assertAlmostEqual(floor.level_at(0.0), kTB, places=6)


class SpreadIsTheSpreadYouAskedFor(unittest.TestCase):
    def test_the_realised_deviation_matches_sigma(self):
        # Median far above thermal so the clamp does not truncate the distribution.
        floor = NoiseFloor(-100.0, 4.0, 60_000.0, -130.0, 11)
        levels = [floor.level_at(t) for t in range(0, 7_200_000, 500)]
        self.assertAlmostEqual(statistics.mean(levels), -100.0, delta=0.5)
        self.assertAlmostEqual(statistics.stdev(levels), 4.0, delta=0.4)

    def test_the_band_drifts_rather_than_flickering(self):
        """Correlated over tau: two instants a second apart are in almost the same band."""
        floor = NoiseFloor(-100.0, 4.0, 60_000.0, -130.0, 11)
        near = [abs(floor.level_at(t) - floor.level_at(t + 1000)) for t in range(0, 600_000, 5000)]
        far = [abs(floor.level_at(t) - floor.level_at(t + 300_000)) for t in range(0, 600_000, 5000)]
        self.assertLess(statistics.mean(near), statistics.mean(far))

    def test_two_nodes_do_not_share_one_band(self):
        conf = Config()
        conf.NOISE_SIGMA_DB = 4.0
        first, second = noise_floor_for(conf, 0), noise_floor_for(conf, 1)
        samples = [(first.level_at(t), second.level_at(t)) for t in range(0, 600_000, 7000)]
        self.assertTrue(any(abs(a - b) > 1.0 for a, b in samples))

    def test_it_is_reproducible_and_stream_free(self):
        """Hashed on (seed, bucket), so a query cannot shift anything else in the run."""
        conf = Config()
        conf.NOISE_SIGMA_DB = 4.0
        a = noise_floor_for(conf, 5)
        b = noise_floor_for(conf, 5)
        self.assertEqual(
            [a.level_at(t) for t in range(0, 100_000, 3000)],
            [b.level_at(t) for t in range(0, 100_000, 3000)],
        )
        # Out of order, and interleaved with other queries: same answers.
        self.assertEqual(a.level_at(50_000.0), b.level_at(50_000.0))


class TheThresholdFollowsTheBand(unittest.TestCase):
    def test_a_quiet_moment_reaches_the_datasheet_figure(self):
        conf = Config()
        conf.MODEM_PRESET = "LONG_FAST"
        conf.NOISE_LEVEL = -110.5  # the packaged Batumi median
        datasheet = conf.current_preset["sensitivity"]

        at_median = effective_sensitivity(conf)
        quiet = effective_sensitivity(conf, noise_dbm=-120.0)
        noisy = effective_sensitivity(conf, noise_dbm=-104.0)

        self.assertAlmostEqual(at_median, -128.0, places=6)
        self.assertEqual(quiet, datasheet)
        self.assertAlmostEqual(noisy, -121.5, places=6)
        self.assertGreater(noisy, at_median)

    def test_a_marginal_link_is_up_in_a_quiet_band_and_down_in_a_noisy_one(self):
        """The point of all of it: marginal links flicker instead of being decided once."""
        conf = Config()
        conf.MODEM_PRESET = "LONG_FAST"
        conf.NOISE_LEVEL = -110.5
        rssi = -129.0  # between the datasheet figure and the median-floor threshold

        self.assertLess(rssi, effective_sensitivity(conf))                    # down at the median
        self.assertGreaterEqual(rssi, effective_sensitivity(conf, noise_dbm=-116.0))  # up when quiet

    def test_the_cad_floor_keeps_its_margin_as_the_band_moves(self):
        conf = Config()
        preset = conf.current_preset
        margin = preset["sensitivity"] - preset["cad_threshold"]
        for noise in (-104.0, -110.5, -120.0):
            with self.subTest(noise=noise):
                self.assertAlmostEqual(
                    effective_sensitivity(conf, noise_dbm=noise)
                    - effective_cad_threshold(conf, noise_dbm=noise),
                    margin,
                    places=6,
                )


class ItChangesLinkExistenceInARun(unittest.TestCase):
    def test_a_noisy_band_costs_a_mesh_some_of_its_links(self):
        import random

        from lib.discrete_event_sim import DiscreteEventSim
        from lib.node import default_generate_node_list

        def links(sigma):
            conf = Config()
            conf.NR_NODES = 15
            conf.SIMTIME = 3 * 60 * 1000
            conf.SEED = 44
            conf.MOVEMENT_ENABLED = False
            conf.NOISE_SIGMA_DB = sigma
            random.seed(conf.SEED)
            sim = DiscreteEventSim(conf, default_generate_node_list(conf))
            sim.run_simulation()
            return sim.get_results()

        steady = links(0.0)
        moving = links(6.0)
        # The same geometry, and a different number of receptions, because the band moved.
        self.assertNotEqual(steady["nrReceived"], moving["nrReceived"])


if __name__ == "__main__":
    unittest.main()
