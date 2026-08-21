"""One channel-utilisation figure, bounded by the fact that a channel cannot be busy twice.

AirTime keeps two windows and the simulator now keeps the same two: 60 s of audible air, ours and
everyone else's, for channel utilisation; an hour of our own transmissions for the TX figure a duty
cycle binds against. The contention window is sized from the first, as
RadioInterface::getTxDelayMsec does.

Before this, the contention window read `airUtilization / env.now` - a lifetime mean that charged
every overlapping reception its full airtime, measured at 117.5% of wall-clock, and unclamped on its
way into 2**CWsize.
"""

import random
import unittest

from lib.config import Config
from lib.discrete_event_sim import DiscreteEventSim
from lib.node import default_generate_node_list


class FakeEnv:
    def __init__(self, now=0.0):
        self.now = now


class Bare:
    """A node reduced to the two rings and the clock they are keyed to."""

    _ring_add = None  # filled in below from MeshNode

    def __init__(self):
        from lib.node import MeshNode

        self.conf = Config()
        self.env = FakeEnv()
        self.channelUtilization = [0.0] * self.conf.CHANNEL_UTILIZATION_PERIODS
        self.channelUtilizationIndex = 0
        self.channelUtilizationEpoch = 0.0
        self.senseUntil = 0.0
        self.utilizationTx = [0.0] * self.conf.UTILIZATION_TX_PERIODS
        self.utilizationTxIndex = 0
        self.utilizationTxEpoch = 0.0
        for name in ("_ring_add", "sense_busy", "log_tx_airtime",
                     "channel_utilization_percent", "utilization_tx_percent"):
            setattr(self, name, getattr(MeshNode, name).__get__(self, Bare))


class OneEnergyDetector(unittest.TestCase):
    def test_overlapping_transmissions_are_one_busy_stretch(self):
        node = Bare()
        self.assertEqual(node.sense_busy(0.0, 600.0), 600.0)
        # Wholly inside the stretch already charged: a second transmitter, not a second channel.
        self.assertEqual(node.sense_busy(100.0, 500.0), 0.0)
        # Overlapping the tail: only the part past the end of the first is new.
        self.assertEqual(node.sense_busy(400.0, 900.0), 300.0)
        node.env.now = 900.0
        self.assertAlmostEqual(node.channel_utilization_percent(), 900.0 / 60000.0 * 100.0)

    def test_a_quiet_window_decays_to_nothing(self):
        node = Bare()
        node.sense_busy(0.0, 5000.0)
        node.env.now = 5000.0
        self.assertGreater(node.channel_utilization_percent(), 0.0)
        # Past the whole 60 s window, every bucket the ring holds has been crossed.
        node.env.now = 200000.0
        self.assertEqual(node.channel_utilization_percent(), 0.0)

    def test_the_two_windows_measure_different_things(self):
        node = Bare()
        node.sense_busy(0.0, 6000.0)       # someone else's transmission, audible here
        node.log_tx_airtime(6000.0, 600.0)  # a tenth of it was ours
        node.env.now = 6000.0
        self.assertAlmostEqual(node.channel_utilization_percent(), 10.0)
        self.assertAlmostEqual(node.utilization_tx_percent(), 600.0 / 3600000.0 * 100.0)


class ChannelCannotBeBusyMoreThanAllTheTime(unittest.TestCase):
    """The invariant sfpp gates on fatally, on the configurations that used to break it."""

    def run_mesh(self, nodes, period_s, area_m, minutes=4, seed=44):
        conf = Config()
        conf.NR_NODES = nodes
        conf.SIMTIME = int(minutes * 60 * 1000)
        conf.PERIOD = period_s * 1000
        conf.SEED = seed
        conf.MOVEMENT_ENABLED = False
        conf.XSIZE = conf.YSIZE = area_m
        random.seed(seed)
        sim = DiscreteEventSim(conf, default_generate_node_list(conf))
        sim.run_simulation()
        return sim.get_results()

    def test_dense_meshes_stay_under_one_hundred_percent(self):
        # 25 nodes on a 5 s period in a 4 km box read 117.5% under the old figure.
        for nodes, period_s, area_m in ((25, 5, 4000), (20, 10, 6000)):
            with self.subTest(nodes=nodes, period_s=period_s):
                results = self.run_mesh(nodes, period_s, area_m)
                util = results["nodeChannelUtilPercent"]
                self.assertLessEqual(util["max"], 100.0)
                self.assertGreaterEqual(util["mean"], 0.0)
                self.assertLessEqual(util["mean"], util["max"])
                # A busy mesh should read busy: this is not a figure stuck near zero.
                self.assertGreater(util["max"], 10.0)

    def test_own_transmit_share_is_far_below_the_channel_share(self):
        """The old chutil was this quantity, which is why the 25% polite gate never fired."""
        results = self.run_mesh(20, 10, 6000)
        self.assertLess(
            results["nodeUtilizationTxPercent"]["max"],
            results["nodeChannelUtilPercent"]["max"],
        )


if __name__ == "__main__":
    unittest.main()
