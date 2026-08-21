"""A seed sweep has to resample what a run does, and a paired comparison has to be paired.

Two defects with one shape. Per-node streams were `random.Random(self.nodeid)` - no run seed in them
at all - so the mobility assignment and each node's message gaps were byte-identical at every seed,
and a hundred repetitions averaged over placement and contention while replaying one realisation of
the traffic. And batchSim derived its seed as `rt_i * 10000 + rep`, so two router types were compared
on the same node coordinates and a different link graph.
"""

import random
import unittest

from lib.common import find_random_position, setup_asymmetric_links
from lib.config import Config
from lib.discrete_event_sim import DiscreteEventSim
from lib.node import default_generate_node_list
from lib.point import Point


def mobility_at(seed, nodes=20):
    conf = Config()
    conf.NR_NODES = nodes
    conf.SIMTIME = 60 * 1000
    conf.SEED = seed
    conf.MOVEMENT_ENABLED = True
    random.seed(seed)
    sim = DiscreteEventSim(conf, default_generate_node_list(conf))
    sim.run_simulation()
    return [
        (n.nodeid, n.isMoving, n.gpsEnabled, getattr(n, "movementStepSize", None))
        for n in sim.mutated_state.nodes
    ]


def first_gaps(seed, node_id=3, count=4):
    conf = Config()
    conf.SEED = seed
    rng = random.Random(f"{conf.SEED}:{node_id}:traffic")
    return [round(rng.expovariate(1.0 / conf.PERIOD), 3) for _ in range(count)]


class ASeedResamplesTheRun(unittest.TestCase):
    def test_mobility_differs_between_seeds(self):
        self.assertNotEqual(mobility_at(44), mobility_at(7))
        self.assertNotEqual(mobility_at(7), mobility_at(101))

    def test_mobility_is_reproducible_at_one_seed(self):
        self.assertEqual(mobility_at(44), mobility_at(44))

    def test_the_message_schedule_differs_between_seeds(self):
        self.assertNotEqual(first_gaps(44), first_gaps(7))
        self.assertEqual(first_gaps(44), first_gaps(44))

    def test_two_nodes_at_one_seed_still_differ_from_each_other(self):
        self.assertNotEqual(first_gaps(44, node_id=3), first_gaps(44, node_id=7))


class ShadowingIsOnThePathAndAsymmetryIsInTheRadio(unittest.TestCase):
    class Node:
        def __init__(self, x):
            self.position = Point(float(x), 0.0, 1.5)
            self.antenna_gain = 0.0
            self.antenna_height = 1.5

    def offsets(self, conf):
        nodes = [self.Node(i * 500) for i in range(6)]
        conf.NR_NODES = len(nodes)
        setup_asymmetric_links(conf, nodes)
        return conf.LINK_OFFSET

    def test_the_two_directions_share_their_shadowing(self):
        """The channel between two antennas is the same channel either way."""
        conf = Config()
        conf.MODEL_RADIO_ASYMMETRY_STDDEV = 0.0  # leave only the path term
        offsets = self.offsets(conf)
        for i in range(6):
            for j in range(i + 1, 6):
                self.assertAlmostEqual(offsets[(i, j)], offsets[(j, i)])

    def test_the_radios_are_what_make_a_link_one_way(self):
        conf = Config()
        conf.MODEL_SHADOWING_STDDEV = 0.0  # leave only the radio term
        offsets = self.offsets(conf)
        differences = [
            abs(offsets[(i, j)] - offsets[(j, i)]) for i in range(6) for j in range(i + 1, 6)
        ]
        self.assertGreater(max(differences), 0.0)

    def test_turning_asymmetry_off_leaves_no_offset_at_all(self):
        conf = Config()
        conf.MODEL_ASYMMETRIC_LINKS = False
        offsets = self.offsets(conf)
        self.assertEqual(set(offsets.values()), {0.0})

    def test_shadowing_is_wide_enough_to_move_a_marginal_link(self):
        """At 2 dB the mesh graph was a near-perfect disc graph."""
        self.assertGreaterEqual(Config().MODEL_SHADOWING_STDDEV, 5.0)


class PlacementDoesNotPoisonItsOwnSearch(unittest.TestCase):
    def test_a_dense_configuration_places_every_node(self):
        """One MINDIST rejection used to set a flag that no later candidate could clear."""
        conf = Config()
        conf.XSIZE = conf.YSIZE = 1500
        conf.MINDIST = 120

        class Placed:
            def __init__(self, x, y):
                self.position = Point(x, y, conf.HM)

        random.seed(4)
        placed = []
        for _ in range(8):
            x, y = find_random_position(conf, placed)
            placed.append(Placed(x, y))
        self.assertEqual(len(placed), 8)
        for i, a in enumerate(placed):
            for b in placed[i + 1:]:
                self.assertGreaterEqual(a.position.euclidean_distance(b.position), conf.MINDIST)

    def test_an_impossible_configuration_raises_instead_of_returning_none(self):
        conf = Config()
        conf.XSIZE = conf.YSIZE = 10
        conf.MINDIST = 500

        class Placed:
            def __init__(self):
                self.position = Point(0.0, 0.0, conf.HM)

        random.seed(4)
        with self.assertRaises(RuntimeError):
            find_random_position(conf, [Placed()])


if __name__ == "__main__":
    unittest.main()
