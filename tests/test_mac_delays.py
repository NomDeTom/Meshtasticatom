"""Contention-window bounds, against the firmware's own draw.

Arduino `random(0, n)` is half-open, so a node can wait n-1 slots and never n. The bound matters at
both ends: the top slot is the one that decides who defers to whom.
"""

import random
import unittest
from unittest import mock

from lib.config import Config
from lib.mac import CWmax, CWmin, get_tx_delay_msec, get_tx_delay_msec_weighted
from lib.phy import get_current_slot_time


class FakeEnv:
    now = 1000.0


class FakeNode:
    def __init__(self, is_router=False, air_utilization=0.0):
        self.conf = Config()
        self.env = FakeEnv()
        self.nodeid = 0
        self.is_router = is_router
        self.airUtilization = air_utilization


def slots_drawn(node, delay, offset=0.0):
    return round((delay - offset) / get_current_slot_time(node.conf))


class TestWeightedDelayBounds(unittest.TestCase):
    """CWsize is 3..8 here, so a client draws 0..2^CWsize-1 slots past the router window."""

    def observed_slots(self, node, rssi, offset=0.0, draws=4000):
        random.seed(7)
        return {
            slots_drawn(node, get_tx_delay_msec_weighted(node, rssi), offset) for _ in range(draws)
        }

    def test_a_router_never_draws_its_top_slot(self):
        node = FakeNode(is_router=True)
        with mock.patch("lib.mac.estimate_snr", return_value=10):
            slots = self.observed_slots(node, rssi=-50)
        self.assertEqual(min(slots), 0)
        self.assertEqual(max(slots), 2 * CWmax - 1)

    def test_a_client_starts_past_the_whole_router_window(self):
        node = FakeNode()
        offset = 2 * CWmax * get_current_slot_time(node.conf)
        with mock.patch("lib.mac.estimate_snr", return_value=10):
            slots = self.observed_slots(node, rssi=-50, offset=offset)
        self.assertEqual(min(slots), 0)
        self.assertEqual(max(slots), 2**CWmax - 1)

    def test_the_router_window_and_the_client_window_do_not_overlap(self):
        router, client = FakeNode(is_router=True), FakeNode()
        with mock.patch("lib.mac.estimate_snr", return_value=10):
            random.seed(11)
            latest_router = max(get_tx_delay_msec_weighted(router, -50) for _ in range(4000))
            random.seed(11)
            earliest_client = min(get_tx_delay_msec_weighted(client, -50) for _ in range(4000))
        self.assertLess(latest_router, earliest_client)


class TestUnweightedDelayBounds(unittest.TestCase):
    def test_an_idle_channel_draws_the_smallest_window(self):
        node = FakeNode(air_utilization=0.0)
        random.seed(3)
        slots = {slots_drawn(node, get_tx_delay_msec(node)) for _ in range(4000)}
        self.assertEqual(min(slots), 0)
        self.assertEqual(max(slots), 2**CWmin - 1)

    def test_a_saturated_channel_draws_the_largest(self):
        node = FakeNode(air_utilization=FakeEnv.now)
        random.seed(3)
        slots = {slots_drawn(node, get_tx_delay_msec(node)) for _ in range(20000)}
        self.assertEqual(max(slots), 2**CWmax - 1)


if __name__ == "__main__":
    unittest.main()
