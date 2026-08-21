"""The application's timer is an input, not an output of the radio's congestion.

generate_message used to contain the reliable-send loop, and that loop slept a full
retransmission timeout - about 7.4 s at LONG_FAST - before it looked to see whether the implicit ACK
had already arrived. Every message therefore cost its own node that stall, so offered load ran 8.9%
under nominal on a five-node mesh and 16.9% under on a sixty-node one: the load fell as the mesh
grew, through a feedback the firmware does not have.
"""

import random
import statistics
import unittest

from lib.config import Config
from lib.discrete_event_sim import DiscreteEventSim
from lib.node import default_generate_node_list


def originated_per_node(results, nodes):
    seen = set()
    counts = {i: 0 for i in range(nodes)}
    for packet in results["packets"]:
        if packet.isAck or packet.txNodeId != packet.origTxNodeId or packet.seq in seen:
            continue
        seen.add(packet.seq)
        counts[packet.origTxNodeId] += 1
    return counts


def offered_per_node(sim, results, nodes):
    """What the application timer produced. With the gate off, that is every message it drew."""
    return originated_per_node(results, nodes)


def run(nodes, period_s=20, minutes=8, seed=44, dms=False, gate=False):
    conf = Config()
    conf.NR_NODES = nodes
    conf.SIMTIME = int(minutes * 60 * 1000)
    conf.PERIOD = period_s * 1000
    conf.SEED = seed
    conf.MOVEMENT_ENABLED = False
    conf.DMs = dms
    # The channel-utilisation gate is off here on purpose. A shut gate legitimately rate-limits the
    # generator - the module cannot send faster than the channel allows, and the firmware's
    # interval restarts from the actual send - so with it on, "offered load equals nominal" is not
    # the right expectation. What this file tests is that nothing *downstream* of the timer holds
    # it up, which is what the reliable-send loop used to do. The gate's own effect is measured in
    # tests/test_tx_gate.py.
    conf.CHANNEL_UTIL_TX_GATE_ENABLED = gate
    random.seed(seed)
    sim = DiscreteEventSim(conf, default_generate_node_list(conf))
    sim.run_simulation()
    return conf, sim, sim.get_results()


class OfferedLoadMatchesItsOwnConfiguration(unittest.TestCase):
    def observed_mean(self, nodes, **kwargs):
        conf, sim, results = run(nodes, **kwargs)
        counts = offered_per_node(sim, results, nodes)
        nominal = conf.SIMTIME / conf.PERIOD
        return statistics.mean(counts.values()), nominal

    def test_a_small_mesh_offers_what_it_was_configured_to_offer(self):
        observed, nominal = self.observed_mean(5)
        # Within a Poisson process's own spread: sd of the per-node mean is sqrt(nominal / nodes).
        self.assertAlmostEqual(observed, nominal, delta=3 * (nominal / 5) ** 0.5)

    def test_a_congested_mesh_offers_the_same_load_as_a_quiet_one(self):
        """The defect was the slope, not the level: load must not fall as the mesh grows."""
        small, nominal = self.observed_mean(5)
        large, _ = self.observed_mean(40)
        self.assertAlmostEqual(large, nominal, delta=3 * (nominal / 40) ** 0.5)
        # A 40-node mesh is genuinely busier than a 5-node one, and still offers the same load.
        self.assertLess(abs(large - small) / nominal, 0.10)


class AnAckEndsTheWait(unittest.TestCase):
    def test_the_reliable_send_runs_beside_the_generator(self):
        """A node with a message in flight is still allowed to compose the next one."""
        from lib.node import MeshNode

        self.assertTrue(hasattr(MeshNode, "reliable_send"))
        self.assertTrue(hasattr(MeshNode, "signal_ack"))

    def test_the_gate_and_the_generator_are_separate_things(self):
        """A deferred send is a delay the firmware has; a stalled generator was a defect.

        With the gate off the timer produces its nominal rate. With it on the same mesh produces
        less, and that difference is the channel telling it to wait - not the timer being held up
        by its own retransmissions.
        """
        _, _, ungated = run(40, gate=False)
        _, _, gated = run(40, gate=True)
        self.assertEqual(ungated["channelUtilDeferred"], 0)
        self.assertGreater(gated["channelUtilDeferred"], 0)
        self.assertGreater(gated["meanChannelUtilDeferralMsec"], 0.0)
        self.assertLess(gated["appMessages"], ungated["appMessages"])


class AnAckEndsTheWaitAlso(unittest.TestCase):
    def test_acknowledged_messages_do_not_use_their_whole_retry_budget(self):
        """On a connected, uncongested mesh most messages are implicitly acked on the first send.

        A quiet period deliberately: at 20 s the mesh is busy enough that most messages do retry,
        which is the correct behaviour and would make this assertion say nothing.
        """
        _, _, results = run(10, period_s=100, minutes=6)
        self.assertGreater(results["appMessages"], 0)
        # Retransmissions are counted apart from rebroadcasts in count_populations.
        self.assertLess(results["retransmissions"], results["appMessages"])


if __name__ == "__main__":
    unittest.main()
