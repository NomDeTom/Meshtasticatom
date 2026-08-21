"""Three numbers this simulator takes from the firmware, pinned against the firmware's own form.

Each was wrong in a way no comparison between runs could catch: the preamble window in the wrong
unit of its own parameter, a C integer division transcribed as true division, and one retransmission
budget where the firmware carries two.
"""

import unittest

from lib.config import Config
from lib.packet import NODENUM_BROADCAST, MeshPacket
from lib.phy import NUM_SYM_CAD_24GHZ, get_current_slot_time, preamble_lock_window_ms


class Packet:
    """The two fields the preamble window reads."""

    def __init__(self, sf, bw):
        self.sf = sf
        self.bw = bw


class PreambleLockWindow(unittest.TestCase):
    """`timing_collision` shares this window with the capture model, in milliseconds."""

    def test_window_is_milliseconds_not_seconds(self):
        conf = Config()  # LONG_FAST: SF11, BW250k, NPREAM 16
        window = preamble_lock_window_ms(conf, Packet(11, 250e3))
        # (16 - 5) symbols of 2**11 / 250e3 s = 90.112 ms. A tenth of a LONG_FAST frame, not a
        # ten-thousandth of one.
        self.assertAlmostEqual(window, 90.112, places=3)

    def test_window_is_a_real_share_of_a_frame(self):
        from lib.phy import airtime

        conf = Config()
        for preset in ("SHORT_TURBO", "LONG_FAST", "LONG_SLOW", "VERY_LONG_SLOW"):
            with self.subTest(preset=preset):
                c = Config()
                c.MODEM_PRESET = preset
                p = c.current_preset
                window = preamble_lock_window_ms(c, Packet(p["sf"], p["bw"]))
                frame = airtime(c, p["sf"], p["cr"], 40, p["bw"])
                # Between a twentieth and a quarter of a frame for every preset. A window that had
                # collapsed by 1000x would be far under this floor.
                self.assertGreater(window / frame, 0.05)
                self.assertLess(window / frame, 0.25)


class WideLoraCadTerm(unittest.TestCase):
    """`(2 * sf + 3) / 32` is integer division in RadioInterface::computeSlotTimeMsec."""

    def test_the_term_is_zero_for_every_legal_spreading_factor(self):
        for sf in range(6, 15):
            with self.subTest(sf=sf):
                self.assertEqual((2 * sf + 3) // 32, 0)

    def test_wide_lora_slot_time_is_the_bare_cad_symbols(self):
        conf = Config()
        conf.REGION = dict(conf.REGION)
        conf.REGION["wide_lora"] = True
        preset = conf.current_preset
        symbol_ms = (2.0 ** preset["sf"]) / (preset["bw"] / 1000)
        expected = NUM_SYM_CAD_24GHZ * symbol_ms + (0.2 + 0.4 + 7)
        self.assertAlmostEqual(get_current_slot_time(conf), expected, places=6)


class ReliableAttemptBudget(unittest.TestCase):
    """NextHopRouter.h: 3 for a reliable broadcast, 5 for an acknowledged unicast, first send in."""

    def test_broadcast_and_unicast_budgets_differ(self):
        conf = Config()
        self.assertEqual(conf.RELIABLE_BROADCAST_ATTEMPTS, 3)
        self.assertEqual(conf.RELIABLE_UNICAST_ATTEMPTS, 5)
        self.assertEqual(MeshPacket.reliable_attempts(conf, NODENUM_BROADCAST), 3)
        self.assertEqual(MeshPacket.reliable_attempts(conf, 7), 5)

    def test_retries_left_is_attempts_minus_the_first_send(self):
        conf = Config()
        self.assertEqual(
            MeshPacket.reliable_attempts(conf, NODENUM_BROADCAST) - 1,
            conf.RELIABLE_BROADCAST_ATTEMPTS - 1,
        )
        self.assertEqual(MeshPacket.reliable_attempts(conf, 7) - 1, 4)


if __name__ == "__main__":
    unittest.main()
