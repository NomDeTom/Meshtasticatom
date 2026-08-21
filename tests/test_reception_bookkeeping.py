"""A reception holds a slot, and releases the one it took.

`isReceiving` was an append-only list of booleans. End of reception did
`self.isReceiving[self.isReceiving.index(True)] = False`, which clears whichever True it finds
first - so a packet that collided before the receiver locked on, and therefore never appended,
released a slot it never took. Measured over a ten-minute thirty-node run: 7786 appends against
8727 releases, 941 of which found nothing outstanding. Those were the harmless ones. The releases
that found a *live* reception cleared it, and `any(self.isReceiving)` is what stops the node
transmitting over a packet it is in the middle of receiving.
"""

import random
import unittest

import simpy

from lib.config import Config
from lib.discrete_event_sim import DiscreteEventSim
from lib.discrete_event_sim_components import SimulationDataTracking, SimulationState
from lib.node import MeshNode, NodeConfig, default_generate_node_list
from lib.point import Point


def stub_packet(collided):
    """A packet reduced to the fields the receive path reads.

    phyLostAtN is True so end-of-reception releases the slot and then stops, rather than going on
    into handle_received_packet, which wants a whole mesh behind it. The release is what is under
    test here.
    """
    return type("Packet", (), {
        "sensedByN": [True],
        "onAirToN": [True],
        "collidedAtN": [collided],
        "phyLostAtN": [True],
        "receivedAtN": [False],
        "rxStartedAtN": [False],
        "timeOnAir": 1.0,
        "seq": 1,
        "txNodeId": 7,
    })()


class ASlotIsReleasedByWhoeverTookIt(unittest.TestCase):
    def one_node(self):
        conf = Config()
        conf.NR_NODES = 1
        env = simpy.Environment()
        node = MeshNode(
            conf, SimulationState(conf, env), SimulationDataTracking(),
            NodeConfig(0, Point(0, 0, 1.5), conf.PERIOD),
        )
        return conf, env, node

    def test_a_collided_packet_does_not_release_a_slot_it_never_took(self):
        conf, env, node = self.one_node()
        pipe = simpy.Store(env)
        env.process(node.receive(pipe))

        live = stub_packet(collided=False)
        collided = stub_packet(collided=True)

        pipe.put(live)      # starts a reception: one slot taken
        env.run(until=0.001)
        self.assertEqual(node.receptionsInFlight, 1)

        pipe.put(collided)  # collided at the start: takes nothing
        env.run(until=0.002)
        self.assertEqual(node.receptionsInFlight, 1)

        pipe.put(collided)  # ...and so releases nothing
        env.run(until=0.003)
        self.assertEqual(node.receptionsInFlight, 1, "a collided packet released a live reception")

        pipe.put(live)      # the live one ends and releases its own slot
        env.run(until=0.004)
        self.assertEqual(node.receptionsInFlight, 0)

    def test_the_count_never_goes_negative(self):
        conf, env, node = self.one_node()
        node.release_reception(stub_packet(collided=False))
        self.assertEqual(node.receptionsInFlight, 0)


class TheDuplicateHistoryIsBounded(unittest.TestCase):
    """PacketHistory is a fixed-size table that evicts its oldest slot, with no time expiry."""

    def test_capacity_matches_mesh_pb_constants(self):
        # max(MAX_NUM_NODES * 2, 100), and MAX_NUM_NODES is 120 on nRF52840 and generic ESP32.
        self.assertEqual(Config().PACKET_HISTORY_MAX, 240)

    def test_the_history_stops_growing_and_forgets_the_oldest_first(self):
        conf = Config()
        conf.NR_NODES = 1
        conf.PACKET_HISTORY_MAX = 8
        env = simpy.Environment()
        node = MeshNode(
            conf, SimulationState(conf, env), SimulationDataTracking(),
            NodeConfig(0, Point(0, 0, 1.5), conf.PERIOD),
        )
        for seq in range(40):
            env.run(until=env.now + 1)
            node.was_seen_recently(stub_and_seq(seq))

        self.assertEqual(len(node.lastHeard), 8)
        self.assertEqual(len(node.timesReceived), 8)
        self.assertEqual(sorted(node.lastHeard), list(range(32, 40)))


def stub_and_seq(seq):
    return type("Packet", (), {"seq": seq, "isAck": False, "destId": 0xFFFFFFFF})()


class NoDecodedReceptionOverlapsItsOwnTransmission(unittest.TestCase):
    """A half-duplex radio cannot do it, and a stolen slot is how it used to become possible."""

    def test_a_dense_mesh_never_receives_while_transmitting(self):
        conf = Config()
        conf.NR_NODES = 25
        conf.SIMTIME = 4 * 60 * 1000
        conf.PERIOD = 5 * 1000
        conf.SEED = 44
        conf.MOVEMENT_ENABLED = False
        conf.XSIZE = conf.YSIZE = 4000
        random.seed(conf.SEED)
        sim = DiscreteEventSim(conf, default_generate_node_list(conf))
        sim.run_simulation()
        results = sim.get_results()

        sending = {n.nodeid: [] for n in sim.mutated_state.nodes}
        for packet in results["packets"]:
            if packet.endTime > 0:
                sending[packet.txNodeId].append((packet.startTime, packet.endTime))

        for packet in results["packets"]:
            if packet.endTime <= 0:
                continue
            for node in sim.mutated_state.nodes:
                if not packet.receivedAtN[node.nodeid]:
                    continue
                for start, end in sending[node.nodeid]:
                    self.assertFalse(
                        max(start, packet.startTime) < min(end, packet.endTime),
                        f"node {node.nodeid} decoded a packet it transmitted over",
                    )


if __name__ == "__main__":
    unittest.main()
