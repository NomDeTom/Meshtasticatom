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

    These tests are about matrix.py's bookkeeping, not about the transport.
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

    A missing sentence fails nothing: it renders as a blank row, which reads as "nothing here".
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

        Composing the text from those two is what holds; six hand-written sentences would drift.
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

        Without it one seed's data silently wears the whole cell's name.
        """
        out = os.path.join(self.tmp.name, "shards")
        first = self.shard(out, 7, "s7")
        second = self.shard(out, 11, "s11")
        self.assertNotEqual(first, second)
        # Counted, not merely named: the failure this guards is one file where there should be
        # two. `figures/` sits beside them either way and no-ops without matplotlib.
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


class PlacementIsolation(unittest.TestCase):
    """The placement stream, and why it has to be its own.

    An 8% reach gap between the control and the arm whose job is to be the control - TRAPS 12.
    """

    def offered_load(self, *flags):
        from .campaign import build_parser, run_once

        report = run_once(
            build_parser().parse_args(
                ["--hours", "2", "--nodes", "25", "--no-charts", "--hop-spread", *flags]
            ),
            4242,
        )
        by = report["by_class"]
        return (
            by["text"]["originated"],
            by["position"]["originated"],
            by["telemetry"]["originated"],
        )

    def test_a_randomised_placement_carries_the_controls_traffic(self):
        control = self.offered_load("--protocol", "none")
        for place in ("random-any", "random-clients"):
            self.assertEqual(
                self.offered_load("--protocol", "sr", "--place", place, "--servers", "2"),
                control,
                f"{place} does not carry the control's offered load",
            )

    def test_the_server_count_does_not_move_the_traffic_either(self):
        """More servers means more samples drawn, so a shared stream would make a --servers sweep
        confound count with offered load."""
        control = self.offered_load("--protocol", "none")
        for count in ("2", "4", "8"):
            self.assertEqual(
                self.offered_load(
                    "--protocol", "sr", "--place", "random-any", "--servers", count
                ),
                control,
                f"--servers {count} moved the offered load",
            )

    def test_a_deliberate_placement_still_carries_it(self):
        control = self.offered_load("--protocol", "none")
        for place in ("spread", "beside-router", "routers"):
            self.assertEqual(
                self.offered_load("--protocol", "sr", "--place", place, "--servers", "2"),
                control,
                place,
            )


class ArmSharding(unittest.TestCase):
    """Splitting a cell's arms across jobs, which is what keeps a mirrored cell inside a runner."""

    def test_the_shards_of_a_cell_cover_every_arm_exactly_once(self):
        """A dropped arm is a missing row nobody would notice, and a duplicated one is a seed counted
        twice in the digest's mean."""
        for total in (1, 2, 3, 4, 11):
            rebuilt = [a for i in range(total) for a in M.shard_of(M.arms(), i, total)]
            self.assertEqual(rebuilt, M.arms(), f"{total} shards do not reassemble the cell")

    def test_the_baseline_lands_in_the_first_shard(self):
        """Contiguous, not strided, so reading shard 0 alone gives the control plus the first
        placements rather than every third arm."""
        first = M.shard_of(M.arms(), 0, 3)
        self.assertEqual(first[0][0], "baseline")

    def test_no_shard_is_empty(self):
        for total in (2, 3, 4):
            for index in range(total):
                self.assertTrue(M.shard_of(M.arms(), index, total), f"{index}/{total} is empty")

    def test_only_the_mirrored_cells_are_split(self):
        """An x1 cell already fits; splitting it would triple the checkout and setup for nothing."""
        self.assertEqual(M.SHARDS_BY_MIRROR[1], 1)
        self.assertGreater(M.SHARDS_BY_MIRROR[4], 1)

    def test_every_scale_in_the_grid_has_a_shard_count(self):
        self.assertEqual(sorted(set(M.MIRRORS) - set(M.SHARDS_BY_MIRROR)), [])

    def test_a_bad_shard_argument_is_refused_rather_than_guessed(self):
        for bad in ("3/3", "4/3", "-1/3", "nonsense", "1"):
            with self.assertRaises(SystemExit, msg=bad):
                quietly(M.main, ["--cell", "batumi-x1-LONG_FAST", "--shard", bad, "--out", "/tmp/x"])

    def test_a_sharded_run_writes_only_its_own_arms(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        with mock.patch.object(M, "run_once", stub_report):
            path = quietly(
                M.run_cell, "batumi-x4-LONG_FAST", "LONG_FAST", 4, [7], tmp.name, "s7-1", (1, 3)
            )
        with open(path) as f:
            values = [r["value"] for r in json.load(f)]
        self.assertEqual(values, [a[0] for a in M.shard_of(M.arms(), 1, 3)])
        self.assertNotIn("baseline", values)  # that one is shard 0's
