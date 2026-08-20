"""The populations a run counts, which are not interchangeable.

One message can become many transmissions; one transmission reaches many receivers; an ACK is
neither a message nor a broadcast. Collapsing any of those gives a number with no stable meaning.
"""

import unittest

from lib.config import Config
from lib.discrete_event_sim import BROADCAST_DEST_ID, count_populations


class Packet:
    def __init__(self, seq, tx=0, orig=0, dest=BROADCAST_DEST_ID, is_ack=False):
        self.seq = seq
        self.txNodeId = tx
        self.origTxNodeId = orig
        self.destId = dest
        self.isAck = is_ack


def conf_with(nodes):
    conf = Config()
    conf.NR_NODES = nodes
    return conf


class TestPopulationsAreSeparate(unittest.TestCase):
    def test_a_rebroadcast_is_a_transmission_and_not_a_message(self):
        packets = [Packet(1)] + [Packet(1, tx=n, orig=0) for n in (1, 2, 3)]
        counts = count_populations(conf_with(5), packets)
        self.assertEqual(counts["appMessages"], 1)
        self.assertEqual(counts["transmissions"], 4)
        self.assertEqual(counts["rebroadcasts"], 3)
        self.assertEqual(counts["retransmissions"], 0)

    def test_a_retransmission_is_the_origin_sending_again(self):
        packets = [Packet(1), Packet(1), Packet(1, tx=2, orig=0)]
        counts = count_populations(conf_with(4), packets)
        self.assertEqual(counts["appMessages"], 1)
        self.assertEqual(counts["retransmissions"], 1)
        self.assertEqual(counts["rebroadcasts"], 1)

    def test_acks_are_counted_apart_from_messages(self):
        packets = [Packet(1), Packet(2, dest=3, is_ack=True)]
        counts = count_populations(conf_with(5), packets)
        self.assertEqual(counts["appMessages"], 1)
        self.assertEqual(counts["ackMessages"], 1)
        self.assertEqual(counts["uniquePacketIds"], 2)


class TestReceiverOpportunities(unittest.TestCase):
    """The denominator the old reach figure got wrong: a unicast does not address the whole mesh."""

    def test_a_broadcast_addresses_every_other_node(self):
        counts = count_populations(conf_with(10), [Packet(1)])
        self.assertEqual(counts["receiverOpportunities"], 9)
        self.assertEqual(counts["appReceiverOpportunities"], 9)

    def test_a_unicast_addresses_one(self):
        counts = count_populations(conf_with(10), [Packet(1, dest=4)])
        self.assertEqual(counts["receiverOpportunities"], 1)
        self.assertEqual(counts["appReceiverOpportunities"], 1)

    def test_an_ack_contributes_no_message_opportunities(self):
        packets = [Packet(1), Packet(2, dest=3, is_ack=True)]
        counts = count_populations(conf_with(10), packets)
        self.assertEqual(counts["appReceiverOpportunities"], 9)
        self.assertEqual(counts["receiverOpportunities"], 10)

    def test_rebroadcasts_do_not_inflate_the_reach_denominator(self):
        """Each message is counted once however many nodes relay it."""
        packets = [Packet(1)] + [Packet(1, tx=n, orig=0) for n in (1, 2, 3)]
        counts = count_populations(conf_with(5), packets)
        self.assertEqual(counts["appReceiverOpportunities"], 4)
        self.assertEqual(counts["receiverOpportunities"], 16)


class TestEmptyRun(unittest.TestCase):
    def test_no_packets_counts_nothing_rather_than_failing(self):
        counts = count_populations(conf_with(5), [])
        self.assertEqual(set(counts.values()), {0})


if __name__ == "__main__":
    unittest.main()
