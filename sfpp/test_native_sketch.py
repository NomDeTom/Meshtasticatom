"""The two decoders are the same decoder, or the fast one is not usable.

`Sketch.decode` runs natively by default, so this is what stands behind that default. It is a
differential test rather than a property one: both implementations are asked the same questions and
their answers compared, which is the same shape as `check_oracle` and for the same reason - a
property test would pass on two implementations that were wrong in the same way, and would say
nothing at all about a wrapper whose contract is "identical".

Cheap on purpose. The costly half is Python's decode, so the plan here stops at capacity 8 and
leaves the deep end to `python3 -m sfpp.native_sketch --scale 1.0`, which the paired job runs: one
capacity-32 sketch held past its capacity is 21.6 s of Python by itself, and a suite nobody will sit
through is a suite that gets skipped.
"""

import unittest

from . import native_sketch, pinsketch

# Small capacities only. Enough of them to exercise decode success, decode failure and the
# misdecode path, without the seconds-per-case the large ones cost.
SUITE_PLAN = ((2, 40), (3, 25), (4, 15), (8, 4))


def native_available():
    """Whether this tree can build the decoder at all, and why not when it cannot."""
    try:
        native_sketch.start()
        return True, ""
    # SystemExit too: a failed compile is reported by check_oracle with sys.exit, which would
    # otherwise tear the suite down here rather than skipping this one test.
    except (Exception, SystemExit) as exc:
        return False, str(exc).strip().splitlines()[0] if str(exc).strip() else repr(exc)


class NativeDecoder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.available, cls.why_not = native_available()

    @classmethod
    def tearDownClass(cls):
        native_sketch.stop()

    def test_the_native_decoder_answers_what_the_transcription_answers(self):
        """Same sketches, both decoders, including sketches held past their capacity.

        Over-capacity is the half that matters. Such a sketch usually fails to decode but misdecodes
        to a wrong set at about 1/c!, and a wrapper agreeing only where decoding succeeds would pass
        a test that never reached the interesting case. Both sides must reach the *same* wrong
        answer, because a misdecode the firmware makes is one the simulator has to make too.
        """
        if not self.available:
            self.skipTest(f"no native decoder here: {self.why_not}")
        disagreed = native_sketch.verify(plan=SUITE_PLAN, report=lambda *a, **k: None)
        self.assertEqual(
            [],
            [(cap, members) for cap, members, _, _ in disagreed],
            f"{len(disagreed)} sketch(es) decoded differently: {disagreed[:3]}",
        )

    def test_a_decoder_that_cannot_be_built_is_a_named_fallback_not_a_crash(self):
        """A tree with no compiler still runs, and says which decoder it used.

        The two produce identical numbers, so falling back costs speed alone - but silently is the
        one way it must not happen, since a lost compiler would otherwise surface only as runs that
        gradually got slower.
        """
        import os
        import unittest.mock

        with unittest.mock.patch.dict(os.environ, {"SFPP_NATIVE_SKETCH": "0"}):
            self.assertEqual(native_sketch.activate(), "python (SFPP_NATIVE_SKETCH=0)")
        native_sketch.disable()

        with unittest.mock.patch.object(
            native_sketch, "start", side_effect=RuntimeError("g++ not found")
        ):
            with unittest.mock.patch.dict(os.environ, {}, clear=False):
                os.environ.pop("SFPP_NATIVE_SKETCH", None)
                said = native_sketch.activate()
        self.assertTrue(said.startswith("python (no native decoder:"), said)
        self.assertIn("g++ not found", said)

    def test_the_decoder_used_cannot_move_a_number(self):
        """fingerprint() drops `decoder`, so the two paths hash identically.

        Not decoration: the paired job compares a native run against a Python one by fingerprint, and
        a report that recorded which decoder ran would make those two differ for a reason that has
        nothing to do with the simulation.
        """
        from .test_series import fingerprint

        report = {"decoder": "native", "held": 0.9, "opts": {}}
        other = dict(report, decoder="python (SFPP_NATIVE_SKETCH=0)")
        self.assertEqual(fingerprint(report), fingerprint(other))


if __name__ == "__main__":
    unittest.main()
