"""Tests for archive-driven part selection.

The property that matters is the one a date-keyed rotation does not have: **a part whose run failed is
chosen again**, because it still has no digest. A calendar moves on and the gap goes unnoticed until the
cycle returns; this looks at what actually ran.

Run from the tree root:  python3 -m unittest sfpp.test_nextup -v
"""

import json
import os
import tempfile
import unittest

from . import nextup as N


class Archive(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = os.path.join(self.tmp.name, "runs")

    def digest(self, run_id, blocks, generated):
        d = os.path.join(self.root, run_id)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "summary.json"), "w") as f:
            json.dump(
                {
                    "run_id": run_id,
                    "generated": generated,
                    "blocks": [{"block": b} for b in blocks],
                },
                f,
            )


class Staleness(Archive):
    def test_a_part_that_never_ran_comes_first(self):
        self.digest("r1", ["a"], "2026-08-01T00:00:00Z")
        self.assertEqual(N.staleness(["a", "b"], self.root), ["b", "a"])

    def test_among_parts_that_ran_the_oldest_comes_first(self):
        self.digest("r1", ["a"], "2026-08-01T00:00:00Z")
        self.digest("r2", ["b"], "2026-08-09T00:00:00Z")
        self.assertEqual(N.staleness(["a", "b"], self.root), ["a", "b"])

    def test_the_newest_digest_for_a_part_is_the_one_that_counts(self):
        """A part run twice is as fresh as its latest run, not its first."""
        self.digest("r1", ["a", "b"], "2026-08-01T00:00:00Z")
        self.digest("r2", ["a"], "2026-08-09T00:00:00Z")
        self.assertEqual(N.staleness(["a", "b"], self.root), ["b", "a"])

    def test_the_order_is_deterministic(self):
        """Two never-run parts must not swap between two plan steps, or a retry could pick a different
        part than the run it is retrying."""
        for _ in range(5):
            self.assertEqual(N.staleness(["z", "a", "m"], self.root), ["a", "m", "z"])

    def test_an_unreadable_digest_does_not_stop_the_selection(self):
        self.digest("r1", ["a"], "2026-08-01T00:00:00Z")
        broken = os.path.join(self.root, "broken")
        os.makedirs(broken, exist_ok=True)
        with open(os.path.join(broken, "summary.json"), "w") as f:
            f.write("{not json")
        self.assertEqual(N.staleness(["a", "b"], self.root), ["b", "a"])

    def test_a_missing_archive_makes_everything_equally_never_run(self):
        """The state of a fresh repository, which is not an error."""
        self.assertEqual(
            N.staleness(["b", "a"], os.path.join(self.tmp.name, "nope")), ["a", "b"]
        )


class SelfHealing(Archive):
    """The property a calendar does not have."""

    def test_a_failed_part_is_chosen_again_rather_than_skipped(self):
        from .matrix import cells

        every = sorted(cells())
        # Two firings' worth of successful runs, then a part that produced nothing.
        first = N.matrix_parts(self.root, 2)
        self.digest("r1", first, "2026-08-01T00:00:00Z")
        second = N.matrix_parts(self.root, 2)
        self.assertNotEqual(set(second), set(first), "a covered part was picked again")
        # r2 fails: no digest written. The next firing must return to it, not move on.
        third = N.matrix_parts(self.root, 2)
        self.assertEqual(third, second, "the failed part was skipped")
        self.assertTrue(set(third) <= set(every))

    def test_coverage_advances_once_a_part_succeeds(self):
        seen = set()
        for day in range(3):
            picked = N.matrix_parts(self.root, 2)
            self.assertFalse(
                set(picked) & seen, f"day {day} repeated an already-covered part"
            )
            seen |= set(picked)
            self.digest(f"r{day}", picked, f"2026-08-0{day + 1}T00:00:00Z")
        from .matrix import cells

        self.assertEqual(seen, set(cells()), "three firings did not cover the grid")


class DesignMeshes(Archive):
    def test_a_mesh_with_one_missing_cell_outranks_a_merely_older_one(self):
        """Its staleness is that of its stalest cell, because the missing cell is the gap to close."""
        from .design import RIVALS, cells

        known = cells()
        covered = [c for c, (m, _, _, _) in known.items() if m == "batumi-short-fast"]
        partial = [c for c, (m, _, _, _) in known.items() if m == "batumi-legacy-25"][:-1]
        # short-fast fully covered but old; legacy-25 newer but one cell short.
        self.digest("r1", covered, "2026-08-01T00:00:00Z")
        self.digest("r2", partial, "2026-08-09T00:00:00Z")
        picked = N.design_parts(self.root, 5)
        self.assertLess(
            picked.index("batumi-legacy-25"),
            picked.index("batumi-short-fast"),
            "a fully covered mesh outranked one with a hole in it",
        )

    def test_it_returns_a_mesh_the_design_declares(self):
        from .design import MESHES

        self.assertIn(N.design_parts(self.root, 1)[0], [m for m, _ in MESHES])


class Cli(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def test_it_prints_space_separated_names_for_a_workflow_to_read(self):
        import contextlib
        import io

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = N.main(["--surface", "matrix", "--archive", self.tmp.name, "--count", "2"])
        self.assertEqual(code, 0)
        self.assertEqual(len(out.getvalue().split()), 2)

    def test_a_count_below_one_is_refused(self):
        with self.assertRaises(SystemExit):
            N.main(["--surface", "design", "--archive", self.tmp.name, "--count", "0"])


if __name__ == "__main__":
    unittest.main()
