import unittest

import lib.common

from lib.point import Point

class TestCommonFunctions(unittest.TestCase):

    def test_calc_dist(self):
        message = "sanity-checking our euclidean distance calculation"
        # Pythagorean triples, so the expected distance is exact: (3, 4, 5) here.
        p1 = (-1, -1)
        p2 = (2, 3)
        self.assertEqual(lib.common.calc_dist(p1[0], p2[0], p1[1], p2[1]), 5.0, message)

        # (5, 12, 13)
        p1 = (-1, -1)
        p2 = (4, 11)
        self.assertEqual(lib.common.calc_dist(p1[0], p2[0], p1[1], p2[1]), 13.0, message)

        # Pythagorean quadruples, the same trick in three dimensions: (1, 2, 2, 3).
        p1 = (-1, -1, -1)
        p2 = (0, 1, 1)
        self.assertEqual(lib.common.calc_dist(p1[0], p2[0], p1[1], p2[1], p1[2], p2[2]), 3.0, message)

        # (2, 3, 6, 7)
        p1 = (-1, -1, -1)
        p2 = (1, 2, 5)
        self.assertEqual(lib.common.calc_dist(p1[0], p2[0], p1[1], p2[1], p1[2], p2[2]), 7.0, message)

    def test_find_random_position(self):
        # A real Config rather than a mock: the function reads enough of one that
        # standing a fake up would just restate the class.
        from lib.config import CONFIG
        from lib.phy import estimate_path_loss

        # TODO: run this for every path-loss model and preset - each changes the range.
        conf = CONFIG

        class MyNode:
            def __init__(self, p):
                self.position = p

            def __repr__(self):
                return f"MyNode(p={self.position})"

        lower_bound_x = conf.OX - conf.XSIZE/2
        upper_bound_x = conf.OX + conf.XSIZE/2
        lower_bound_y = conf.OY - conf.YSIZE/2
        upper_bound_y = conf.OY + conf.YSIZE/2

        nodes = []
        # A position always comes back: in the area, in reach of one node, MINDIST from all.

        # first node case
        position = lib.common.find_random_position(conf, nodes)
        self.assertIsNotNone(position, "always return position")
        self.assertGreaterEqual(position[0], lower_bound_x, f"x within bounds {position=}")
        self.assertLessEqual(position[0], upper_bound_x, f"x within bounds {position=}")
        self.assertGreaterEqual(position[1], lower_bound_y, f"y within bounds {position=}")
        self.assertLessEqual(position[1], upper_bound_y, f"y within bounds {position=}")

        # second node case
        n = MyNode(Point(0, 0, 0))
        nodes = [n]
        position = lib.common.find_random_position(conf, nodes)
        self.assertIsNotNone(position, "always return position")
        self.assertGreaterEqual(position[0], lower_bound_x, f"x within bounds {position=}")
        self.assertLessEqual(position[0], upper_bound_x, f"x within bounds {position=}")
        self.assertGreaterEqual(position[1], lower_bound_y, f"y within bounds {position=}")
        self.assertLessEqual(position[1], upper_bound_y, f"y within bounds {position=}")

        distance = lib.common.calc_dist(n.position.x, position[0], n.position.y, position[1])
        self.assertGreaterEqual(distance, conf.MINDIST, f"{position=} not within MINDIST of {n=}")

        # TODO: this restates the function under test. A precomputed max distance for
        # these config parameters would be a real check rather than a mirror.
        pathLoss = estimate_path_loss(conf, distance, conf.FREQ)
        rssi = conf.PTX + 2*conf.GL - pathLoss
        self.assertGreaterEqual(rssi, conf.current_preset["sensitivity"], f"found {position=} is within radio range of {n=}")

if __name__ == '__main__':
    unittest.main()
