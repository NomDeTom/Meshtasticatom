"""Tests for the place-and-radio matrix's grid and its sharding.

This module had no tests, and then acquired the one thing that most needs them: the cells are sharded
one job per seed, so several jobs now write into a directory that is merged into one. `--tag` is what
keeps them apart, and a regression there does not fail - it silently keeps whichever shard the
download happened to write last, under the whole cell's name. That is the failure `TRAPS.md` catalogues
six variants of, so it gets a test rather than a comment.

Run from the tree root:  python3 -m unittest sfpp.test_matrix -v
"""

import contextlib
import io
import json
import os
import tempfile
import unittest
from unittest import mock

from . import collate as C
from . import matrix as M
from .campaign import build_parser


def quietly(fn, *args, **kwargs):
    """Run something without its progress lines landing in the test output."""
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*args, **kwargs)


def stub_report(opts, seed):
    """What run_once would have returned, without the ten minutes of simulation.

    Stubbed deliberately: what these tests are about is matrix.py's own bookkeeping - which file a
    shard lands in and what `block` it claims - and running the transport to check a filename would
    make the test both slow and a test of something else.
    """
    return {
        "seed": seed,
        "wall_seconds": 351.7,
        "opts": {"hours": opts.hours, "nodes": 92, "scenario": opts.scenario},
        "baseline": {"text_reception_mean": 0.888},
        "sfpp": {
            "held_fraction_mean": 0.469,
            "silent_losses": 0,
            "servers_placed": opts.servers if not opts.baseline else None,
        },
    }


class TestGrid(unittest.TestCase):
    def test_every_cell_is_one_preset_and_one_scale(self):
        for name, (preset, mirror) in M.cells().items():
            self.assertIn(preset, M.PRESETS, name)
            self.assertIn(mirror, M.MIRRORS, name)

    def test_cell_names_are_unique(self):
        self.assertEqual(len(M.cells()), len(M.PRESETS) * len(M.MIRRORS))

    def test_every_combination_parses(self):
        parser = build_parser()
        for preset, mirror in M.cells().values():
            parser.parse_args(M.cell_argv(preset, mirror, baseline=True))
            for place in M.PLACES:
                for servers in M.SERVERS:
                    parser.parse_args(M.cell_argv(preset, mirror, place, servers))

    def test_the_baseline_arm_asks_for_no_archive(self):
        opts = build_parser().parse_args(M.cell_argv("LONG_FAST", 1, baseline=True))
        self.assertTrue(opts.baseline)

    def test_the_server_counts_straddle_the_router_cap(self):
        """Batumi has four routers, and this grid exists to make the capping visible rather than hide
        it - a role-bounded placement above the cap silently repeats the capped row (TRAPS.md #6)."""
        self.assertLess(min(M.SERVERS), 4)
        self.assertGreater(max(M.SERVERS), 4)

    def test_random_any_is_among_the_placements(self):
        """The control. A deliberate arrangement that cannot beat nodes picked at random has not
        earned its complexity."""
        self.assertIn("random-any", M.PLACES)


class TestDescriptions(unittest.TestCase):
    """Every cell says what it covers, and the saying is enforced rather than hoped for.

    Mirrors the four checks `test_mesh` holds `sweep.DESCRIPTIONS` to. The failure this prevents is
    quiet: `collate.describe()` returns None for a cell no producer declares, so a missing sentence
    does not fail anything - it renders as a blank row in the digest and on the page, which reads as
    "this cell does nothing interesting" rather than "nobody wrote it down".
    """

    def test_every_cell_has_an_explanation(self):
        self.assertEqual(sorted(set(M.cells()) - set(M.describes())), [])

    def test_no_explanation_outlives_its_cell(self):
        self.assertEqual(sorted(set(M.describes()) - set(M.cells())), [])

    def test_an_explanation_is_a_sentence(self):
        for name, text in M.describes().items():
            self.assertTrue(text.endswith("."), f"{name}: not a sentence")
            self.assertGreater(len(text), 30, f"{name}: too short to explain anything")

    def test_sibling_cells_do_not_share_an_explanation(self):
        """Cells differ in exactly two coordinates, and both have to reach the sentence.

        Composing the text from the preset and the scale is what makes this hold; writing six
        sentences by hand is what would eventually break it.
        """
        seen = {}
        for name, text in M.describes().items():
            self.assertNotIn(text, seen, f"{name} and {seen.get(text)} share an explanation")
            seen[text] = name

    def test_every_preset_and_scale_in_the_grid_has_a_note(self):
        """The composition's own inputs, so adding a preset to PRESETS fails here rather than with a
        KeyError halfway through a scheduled round."""
        self.assertEqual(sorted(set(M.PRESETS) - set(M.PRESET_NOTES)), [])
        self.assertEqual(sorted(set(M.MIRRORS) - set(M.MIRROR_NOTES)), [])

    def test_the_digest_finds_a_matrix_cell_by_name(self):
        """The end the explanation exists for. Matrix cells reached collate nameless before this."""
        for name in M.cells():
            self.assertIsNotNone(C.describe(name), name)


class TestDuration(unittest.TestCase):
    def test_the_matrix_runs_long_enough_for_a_diurnal_cycle(self):
        """Three passes of the 24-hour curve, not one.

        This was two hours, which samples two hours of a 17:1 peak-to-trough curve - so a time-of-day
        effect and an artefact of wherever --start-hour landed were the same reading. A regression here
        would not fail anything; it would quietly make every figure in the matrix a figure about one
        arbitrary evening again.
        """
        opts = build_parser().parse_args(M.cell_argv("LONG_FAST", 1, "random-any", 2))
        self.assertGreaterEqual(opts.hours, 72)

    def test_the_duration_is_the_same_for_every_cell(self):
        """Duration is held fixed, not crossed - it is not one of the matrix's axes."""
        parser = build_parser()
        hours = {
            parser.parse_args(M.cell_argv(preset, mirror, place, servers)).hours
            for preset, mirror in M.cells().values()
            for place in M.PLACES
            for servers in M.SERVERS
        }
        self.assertEqual(len(hours), 1)


class TestSharding(unittest.TestCase):
    """One cell over several jobs, and the filename discipline that keeps them apart."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def shard(self, out_dir, seed, tag):
        """One shard of one cell, with the transport stubbed out."""
        with mock.patch.object(M, "run_once", stub_report):
            return quietly(
                M.run_cell, "batumi-x1-LONG_FAST", "LONG_FAST", 1, [seed], out_dir, tag
            )

    def test_a_tag_is_accepted_on_the_command_line(self):
        """The flags the sharded workflow actually issues. --list short-circuits before any run."""
        self.assertEqual(quietly(M.main, ["--list", "--seeds", "7", "--tag", "s7"]), 0)

    def test_two_shards_of_one_cell_do_not_overwrite_each_other(self):
        """The whole point of --tag, exercised through run_cell rather than asserted about strings.

        Without it both shards write `batumi-x1-LONG_FAST.json` into the directory the collate job
        merges every artifact into, and one seed's data silently wears the whole cell's name.
        """
        out = os.path.join(self.tmp.name, "shards")
        first = self.shard(out, 7, "s7")
        second = self.shard(out, 11, "s11")
        self.assertNotEqual(first, second)
        # Both shards' JSON, side by side. Counted rather than merely named, because the failure this
        # guards is one file where there should be two. (`figures/` is beside them either way -
        # run_cell has always asked autochart for a chart, which no-ops without matplotlib.)
        self.assertEqual(
            sorted(f for f in os.listdir(out) if f.endswith(".json")),
            ["batumi-x1-LONG_FAST.s11.json", "batumi-x1-LONG_FAST.s7.json"],
        )
        for path, seed in ((first, 7), (second, 11)):
            with open(path) as f:
                self.assertEqual({r["seed"] for r in json.load(f)}, {seed})

    def test_without_a_tag_the_filename_is_unchanged(self):
        """An unsharded local run must behave exactly as it did before --tag existed."""
        out = os.path.join(self.tmp.name, "untagged")
        path = self.shard(out, 7, None)
        self.assertEqual(os.path.basename(path), "batumi-x1-LONG_FAST.json")

    def test_a_shard_still_carries_the_cell_name_as_its_block(self):
        """Only the filename differs between shards; `block` is what the digest groups on."""
        out = os.path.join(self.tmp.name, "blockname")
        with open(self.shard(out, 7, "s7")) as f:
            self.assertEqual({r["block"] for r in json.load(f)}, {"batumi-x1-LONG_FAST"})

    def test_the_digest_reads_the_shards_of_a_cell_as_one_block(self):
        """A shard is not a block. All of a cell's shards carry the same `block`, so the digest must
        group them rather than enter the cell once per seed - and must not report it missing."""
        run = os.path.join(self.tmp.name, "run")
        os.makedirs(run, exist_ok=True)
        for seed in (7, 11):
            reports = [
                {
                    "block": "batumi-x1-LONG_FAST",
                    "arm": "placement",
                    "value": label,
                    "seed": seed,
                    "wall_seconds": 351.7,
                    "opts": {"hours": 72.0, "nodes": 92, "scenario": "batumi"},
                    "baseline": {"text_reception_mean": 0.888},
                    "sfpp": {"held_fraction_mean": 0.469, "silent_losses": 0},
                }
                for label in ("baseline", "random-any x2")
            ]
            with open(os.path.join(run, f"batumi-x1-LONG_FAST.s{seed}.json"), "w") as f:
                json.dump(reports, f)

        summary = C.collate(run, expected={"batumi-x1-LONG_FAST"})
        self.assertEqual(len(summary["blocks"]), 1)
        self.assertEqual(summary["missing_blocks"], [])
        # Both seeds reached the digest rather than one shard overwriting the other.
        self.assertEqual(summary["seeds"], [7, 11])


if __name__ == "__main__":
    unittest.main()
