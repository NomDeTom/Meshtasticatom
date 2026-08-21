import unittest

from lib.config import Config
import lib.phy

class TestPhy(unittest.TestCase):

    def test_path_loss_estimator(self):
        # make sure we reject invalid model selection integers
        from lib.config import CONFIG
        conf = CONFIG

        model = -1 # invalid model
        self.assertRaises(ValueError, lib.phy.estimate_path_loss, conf, 50, 915, 3, 3, model)
        model = 7 # invalid model
        self.assertRaises(ValueError, lib.phy.estimate_path_loss, conf, 50, 915, 3, 3, model)
        model = 10 # invalid model
        self.assertRaises(ValueError, lib.phy.estimate_path_loss, conf, 50, 915, 3, 3, model)
        model = -10 # invalid model
        self.assertRaises(ValueError, lib.phy.estimate_path_loss, conf, 50, 915, 3, 3, model)

        # TODO: pin expected values per path-loss model, once each is verified against
        # something outside this tree - the way test_phy_airtime.py pins airtime.

    def test_rootFinder(self):
        # double-check we can find the roots of some polynomials
        message = "sanity-check Newton-Raphson root-finding implementation"
        tolerance = 0.0000001

        def poly1(x):
            ''' roots at x=-3, 0, 2.5 '''
            return (x+3)*(x-2.5)*x

        # should find -3
        res = lib.phy.rootFinder(poly1, -3.5, tol=tolerance)
        diff = abs(res - -3)
        self.assertLess(diff, tolerance, message)

        # should find 0
        res = lib.phy.rootFinder(poly1, -1, tol=tolerance)
        diff = abs(res - 0)
        self.assertLess(diff, tolerance, message)

        # should find 2.5
        res = lib.phy.rootFinder(poly1, 3, tol=tolerance)
        diff = abs(res - 2.5)
        self.assertLess(diff, tolerance, message)

    def test_path_loss_distance_floor_keeps_near_field_calibrated(self):
        conf = Config()
        conf.PATH_LOSS_DISTANCE_FLOOR_M = 780.0

        below_floor = lib.phy.estimate_path_loss(conf, 10.0, conf.FREQ)
        at_floor = lib.phy.estimate_path_loss(conf, 780.0, conf.FREQ)

        self.assertAlmostEqual(below_floor, at_floor)

    def test_estimate_path_loss_accepts_explicit_model(self):
        conf = Config()
        dist = 1500
        freq = conf.FREQ

        explicit = lib.phy.estimate_path_loss(conf, dist, freq, model=0)

        self.assertEqual(conf.MODEL, 5, "explicit model must not mutate config")
        conf.MODEL = 0
        implicit = lib.phy.estimate_path_loss(conf, dist, freq)
        self.assertAlmostEqual(explicit, implicit)

    def test_estimate_path_loss_rejects_unsupported_model(self):
        conf = Config()

        with self.assertRaisesRegex(ValueError, "unsupported path loss model"):
            lib.phy.estimate_path_loss(conf, 1500, conf.FREQ, model=99)


if __name__ == '__main__':
    unittest.main()


class FreeSpaceIsTheFloor(unittest.TestCase):
    """No empirical propagation model may beat free space, however far outside its range it is asked."""

    def test_the_published_friis_constant(self):
        from lib.phy import free_space_path_loss

        # 1 km at 900 MHz: 20log10(1000) + 20log10(900e6) - 147.552 = 91.5 dB.
        self.assertAlmostEqual(free_space_path_loss(1000.0, 900e6), 91.53, places=2)
        # Doubling the distance costs 6 dB, as it must.
        self.assertAlmostEqual(
            free_space_path_loss(2000.0, 900e6) - free_space_path_loss(1000.0, 900e6), 6.02, places=2
        )

    def test_an_absurd_antenna_height_cannot_produce_gain(self):
        from lib.phy import estimate_path_loss, free_space_path_loss

        conf = Config()
        # 900 m passed as an antenna height above ground is far outside the 3GPP form's validity,
        # and its linear height terms used to dominate and return a negative loss: 900 m produced
        # +2173 dBm of RSSI on a 60 km path.
        loss = estimate_path_loss(conf, 60000.0, conf.FREQ, 900.0, 900.0)
        self.assertGreater(loss, 0.0)
        self.assertGreaterEqual(loss, free_space_path_loss(60000.0, conf.FREQ) - 1e-9)

    def test_the_floor_is_inert_at_the_defaults(self):
        """It guards the absurd cases without moving any number a normal run produces."""
        from lib.phy import estimate_path_loss, free_space_path_loss

        conf = Config()
        for distance in (100.0, 1000.0, 5000.0, 20000.0):
            with self.subTest(distance=distance):
                self.assertGreater(
                    estimate_path_loss(conf, distance, conf.FREQ),
                    free_space_path_loss(distance, conf.FREQ),
                )
