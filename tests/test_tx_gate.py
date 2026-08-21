"""A device declines to originate when the channel is busy, and that is what stops a collapse.

AirTime::isTxAllowedChannelUtil gates every periodic module in the firmware - position, telemetry,
nodeinfo, neighbourinfo, store-and-forward, range test - at 40%, or 25% for the polite roles. The
simulator had no such gate anywhere, so its congestion curves described a mesh that keeps offering
the same load however busy the air gets.
"""

import random
import unittest

from lib.config import Config
from lib.discrete_event_sim import DiscreteEventSim
from lib.node import default_generate_node_list


def run(nodes, period_s, area_m, minutes=6, gate=True, polite=True, seed=44):
    conf = Config()
    conf.NR_NODES = nodes
    conf.SIMTIME = int(minutes * 60 * 1000)
    conf.PERIOD = period_s * 1000
    conf.SEED = seed
    conf.MOVEMENT_ENABLED = False
    conf.XSIZE = conf.YSIZE = area_m
    conf.CHANNEL_UTIL_TX_GATE_ENABLED = gate
    conf.CHANNEL_UTIL_TX_GATE_POLITE = polite
    random.seed(seed)
    sim = DiscreteEventSim(conf, default_generate_node_list(conf))
    sim.run_simulation()
    return sim.get_results()


class TheThresholdIsTheFirmwareEsts(unittest.TestCase):
    def test_thresholds_match_airtime_h(self):
        conf = Config()
        self.assertEqual(conf.CHANNEL_UTIL_TX_LIMIT_PERCENT, 40)
        self.assertEqual(conf.CHANNEL_UTIL_POLITE_TX_LIMIT_PERCENT, 25)

    def test_the_gate_reads_the_channel_and_not_our_own_transmissions(self):
        from lib.node import MeshNode

        class Bare:
            conf = Config()
            _util = 0.0

            def channel_utilization_percent(self):
                return self._util

        node = Bare()
        node.is_tx_allowed_channel_util = MeshNode.is_tx_allowed_channel_util.__get__(node, Bare)

        node._util = 24.9
        self.assertTrue(node.is_tx_allowed_channel_util())
        node._util = 25.0
        self.assertFalse(node.is_tx_allowed_channel_util())
        # The impolite limit is the one NodeInfoModule uses.
        node.conf.CHANNEL_UTIL_TX_GATE_POLITE = False
        self.assertTrue(node.is_tx_allowed_channel_util())
        node._util = 40.0
        self.assertFalse(node.is_tx_allowed_channel_util())

    def test_the_gate_can_be_turned_off_and_then_declines_nothing(self):
        results = run(10, 100, 15000, gate=False)
        self.assertEqual(results["channelUtilDropped"], 0)


class AGatedMeshDoesNotDrown(unittest.TestCase):
    """The finding this exists for: without the gate, an offered load past capacity collapses."""

    def test_a_saturated_mesh_sheds_load_instead_of_collapsing(self):
        ungated = run(25, 5, 4000, gate=False)
        gated = run(25, 5, 4000, gate=True)

        self.assertEqual(ungated["channelUtilDropped"], 0)
        self.assertGreater(gated["channelUtilDropped"], 0)
        # It stops originating, so it originates far less...
        self.assertLess(gated["appMessages"], ungated["appMessages"])
        # ...and what it does originate actually arrives.
        self.assertGreater(gated["nodeReach"], ungated["nodeReach"])
        self.assertLess(gated["nodeChannelUtilPercent"]["mean"],
                        ungated["nodeChannelUtilPercent"]["mean"])

    def test_a_quiet_mesh_is_barely_gated(self):
        """The gate must be off the critical path when the channel is not busy.

        Barely, not never: a five-node mesh can still put two nodes close enough that one of them
        sees a busy 60-second window, which is a real condition rather than a threshold artefact.
        """
        results = run(5, 100, 15000)
        offered = results["appMessages"] + results["channelUtilDropped"]
        self.assertLess(results["channelUtilDropped"] / max(1, offered), 0.15)


if __name__ == "__main__":
    unittest.main()
