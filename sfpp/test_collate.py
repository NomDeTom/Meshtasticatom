"""Tests for the scheduled run's digest and the rolling page built from it.

The reports here are hand-built rather than produced by a campaign run: a collator checked against
the simulator's own output only proves the two agree, and the cases that matter are the ones a real
run produces once a month - a silent loss, a block whose job never wrote a file, an arm that moved
nothing. Each is built directly.

The inert check has its own regression: the first version compared only the metrics the digest
displays and called `SF-signed` inert, when that arm moves `advert_bytes` by 43% and nothing else.
`test_inert_sees_a_metric_it_does_not_display` is that case.

Run from `sim/`:  python3 -m unittest sfpp.test_collate -v
"""

import contextlib
import io
import json
import os
import tempfile
import unittest

from . import collate as C
from . import explorer as E
from . import version as V


def report(block="B-arm", arm="arm", value=1, seed=7, held=0.8, text=0.7, **overrides):
    """One cell report, shaped like the campaign's but only as deep as these tests read."""
    r = {
        "block": block,
        "arm": arm,
        "value": value,
        "seed": seed,
        "grid": [],
        "transport": "abc1234",
        "sim_version": V.SIM_VERSION,
        "wall_seconds": 68.6,
        "opts": {"nodes": 60, "scenario": None, "signed": bool(value)},
        "mesh": {"nodes": 60, "mean_degree": 9.5, "connected": True},
        "baseline": {
            "text_reception_mean": text,
            "text_reception_min": text - 0.2,
            "reach_ceiling_mean": 0.94,
        },
        "traffic": {
            "transmissions": 10000,
            "queue_drops": 100,
            # Aggregate demand, a multiple with no ceiling. Never a utilisation.
            "channel_utilisation": 1.7,
            "node_channel_util_percent": {"p90": 33.5, "max": 40.8},
            "node_air_util_tx_percent": {"p90": 7.1, "max": 7.7},
            "bytes_on_air": 500000,
        },
        "ground": None,
        "dm": {
            "reception": 0.966,
            "composed": 120,
            "no_key": 0,
            "no_addressable_peer": 0,
        },
        "admin": {"1": {"sessions": 40, "session_completed": 32}},
        "sfpp": {
            "held_fraction_mean": held,
            "held_fraction_min": held - 0.1,
            "union_fraction": held + 0.02,
            "sr_airtime_share": 0.026,
            "objects_moved": 229,
            "adverts": 81,
            "advert_bytes": 12555,
            "sr_bytes": 36212,
            "escalations": 0,
            "decode_failures": 0,
            "misdecodes": 0,
            "silent_losses": 0,
            "audit_checksum_agrees_sets_differ": 0,
            "servers_requested": 3,
            "servers_placed": 3,
            "held_per_server": [0.79, 0.80, 0.81],
        },
    }
    for path, v in overrides.items():
        section, _, field = path.partition("__")
        if field:
            r[section][field] = v
        else:
            r[section] = v
    return r


def quietly(main, argv):
    """Run a module's main() without its progress lines landing in the test output."""
    with contextlib.redirect_stdout(io.StringIO()):
        return main(argv)


def write_run(directory, blocks):
    """{block name: [reports]} on disk, the way sweep.py leaves a run."""
    os.makedirs(directory, exist_ok=True)
    for name, reports in blocks.items():
        with open(os.path.join(directory, f"{name}.json"), "w") as f:
            json.dump(reports, f)
    return directory


class SafeNames(unittest.TestCase):
    """A block name arrives from a digest on a shared branch and is used to build paths."""

    def test_a_name_can_only_ever_be_one_path_component(self):
        for hostile in ("../../etc/passwd", "/etc/passwd", "..", "a/b", "a\\b", "x\x00y", "..."):
            cleaned = C.safe_name(hostile)
            self.assertNotIn("/", cleaned)
            self.assertNotIn("\\", cleaned)
            self.assertNotEqual(cleaned, "..")
            self.assertFalse(cleaned.startswith("."), cleaned)
            self.assertEqual(cleaned, os.path.basename(cleaned))

    def test_an_ordinary_block_name_is_left_alone(self):
        for name in ("RT-adopt", "DB-hotstore-stress", "SF-archive-sr", "SF-signed"):
            self.assertEqual(C.safe_name(name), name)
            self.assertTrue(C.is_safe_name(name))

    def test_an_empty_or_dotted_name_falls_back(self):
        for name in ("", "...", "."):
            self.assertTrue(C.safe_name(name).startswith("block-"), C.safe_name(name))

    def test_two_names_never_land_on_one_file(self):
        # Cleaning alone is not injective: `a/b`, `a\\b` and a real `a-b` all clean to `a-b`, so one
        # block's report would overwrite another's - or a hostile name could aim at a real one.
        names = ["a/b", "a\\b", "a-b", "a b", "x" * 200 + "A", "x" * 200 + "B", "..", ".", ""]
        stems = [C.safe_name(n) for n in names]
        self.assertEqual(len(set(stems)), len(stems), stems)

    def test_a_windows_device_name_is_not_left_as_one(self):
        # CON.svg is the console on Windows whatever the extension, and a report directory travels.
        for device in ("CON", "nul", "COM1", "LPT9"):
            self.assertNotEqual(C.safe_name(device).upper(), device.upper())

    def test_a_name_already_usable_is_untouched(self):
        # The suffix appears only where something had to change, so ordinary block names - which is
        # all of them - keep addressing the files they always did.
        self.assertEqual(C.safe_name("B-congestion-scaling"), "B-congestion-scaling")

    def test_the_page_cannot_be_walked_out_of_the_figures_directory(self):
        # Without sanitising, a block named ../secret would inline a file from outside the figures
        # directory into a page that gets published.
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        figures = os.path.join(tmp.name, "figures")
        os.makedirs(figures)
        secret = os.path.join(tmp.name, "secret.svg")
        with open(secret, "w") as f:
            f.write("<svg>PRIVATE</svg>")
        self.assertEqual(E.block_figure(figures, "../secret"), "")

    def test_a_name_cannot_reshape_the_markdown_beside_the_page(self):
        # _esc guards the HTML and does nothing for the file next to it: a pipe ends a table cell,
        # a backtick ends a code span, and a bracket or a space ends a link target.
        self.assertEqual(E._md("a|b`c"), "a\\|b'c")
        self.assertEqual(E._md_link("../run 1/x)y"), "../run%201/x%29y")

    def test_a_hostile_run_directory_cannot_end_a_markdown_link(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        archive = os.path.join(tmp.name, "archive")
        runs = write_run(os.path.join(tmp.name, "runs"), {"B-arm": [report()]})
        quietly(
            C.main,
            ["--runs", runs, "--out", os.path.join(archive, "r1) [x](y"), "--run-id", "r1"],
        )
        out = os.path.join(tmp.name, "page")
        quietly(E.main, ["--archive", archive, "--out", out])
        with open(os.path.join(out, "INDEX.md")) as f:
            index = f.read()
        self.assertNotIn("r1) [x](y/trend.md", index)
        self.assertIn("%29%20%5Bx%5D%28y/trend.md", index)

    def test_collate_says_when_a_digest_carries_one(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        runs = write_run(os.path.join(tmp.name, "runs"), {"hostile": [report(block="../../x")]})
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            C.collate(runs, run_id="r1")
        self.assertIn("not usable as a path", buffer.getvalue())


class PerNodeDetail(unittest.TestCase):
    """The vectors behind the distributions: stored by the run, carried only when asked."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.runs = write_run(
            os.path.join(self.tmp.name, "runs"),
            {
                "B-arm": [
                    report(value=0, by_class={"text": {"per_node": [0.9, 0.1, 0.5]}}),
                    report(value=1, by_class={"text": {"per_node": [0.8, 0.2, 0.4]}}),
                ]
            },
        )

    def _cells(self, **kw):
        digest = C.collate(self.runs, run_id="r1", **kw)
        return {c["value"]: c for c in digest["blocks"][0]["cells"]}

    def test_the_digest_leaves_them_out_by_default(self):
        # This digest is what the rolling page is built from, and a season of them is not the place
        # for a vector per class per cell.
        for cell in self._cells().values():
            self.assertNotIn("per_node", cell)

    def test_per_node_carries_the_vectors_and_names_the_seed(self):
        # Values are grouped as strings, the way every other cell in a digest is keyed.
        cells = self._cells(per_node=True)
        self.assertEqual(cells["0"]["per_node"]["text"], [0.9, 0.1, 0.5])
        self.assertEqual(cells["1"]["per_node"]["text"], [0.8, 0.2, 0.4])
        # Node order belongs to one run, so the digest says which seed the vector came from.
        self.assertEqual(cells["0"]["per_node_seed"], 7)

    def test_the_page_only_offers_the_chart_when_it_has_the_numbers(self):
        archive = os.path.join(self.tmp.name, "archive")
        quietly(C.main, ["--runs", self.runs, "--out", os.path.join(archive, "r1"),
                         "--run-id", "r1"])
        out = os.path.join(self.tmp.name, "plain")
        quietly(E.main, ["--archive", archive, "--out", out])
        with open(os.path.join(out, "index.html")) as f:
            self.assertNotIn("every node, by class", f.read())

        quietly(C.main, ["--runs", self.runs, "--out", os.path.join(archive, "r1"),
                         "--run-id", "r1", "--per-node"])
        out = os.path.join(self.tmp.name, "rich")
        quietly(E.main, ["--archive", archive, "--out", out])
        with open(os.path.join(out, "index.html")) as f:
            page = f.read()
        self.assertIn("every node, by class", page)
        self.assertIn("0.9", page)


class NumericLeaves(unittest.TestCase):
    def test_walks_dicts_and_lists(self):
        leaves = C.numeric_leaves({"a": {"b": 1}, "c": [2, {"d": 3.5}]})
        self.assertEqual(leaves["/a/b"], 1)
        self.assertEqual(leaves["/c[0]"], 2)
        self.assertEqual(leaves["/c[1]/d"], 3.5)

    def test_bools_are_not_measurements(self):
        # `connected` flipping is a different mesh, not a different measurement of one, and a bool
        # compared as 0/1 would put every fragmented run's block on the leaderboard.
        self.assertEqual(
            C.numeric_leaves({"connected": True, "nodes": 60}), {"/nodes": 60}
        )


class Inert(unittest.TestCase):
    def test_identical_cells_are_inert(self):
        grouped = {"False": [report(value=False)], "True": [report(value=True)]}
        self.assertTrue(C._inert(grouped))

    def test_inert_sees_a_metric_it_does_not_display(self):
        # SF-signed: held, text, airtime and every displayed metric identical; only the byte counters
        # move. The arm is live and must not be reported as inert.
        grouped = {
            "False": [report(value=False)],
            "True": [report(value=True, sfpp__advert_bytes=17901)],
        }
        self.assertFalse(C._inert(grouped))

    def test_a_difference_inside_a_list_counts(self):
        grouped = {
            "a": [report(value="a")],
            "b": [report(value="b", sfpp__held_per_server=[0.79, 0.80, 0.99])],
        }
        self.assertFalse(C._inert(grouped))

    def test_timing_and_seed_are_not_evidence(self):
        # Two identical cells always differ in wall_seconds, and the seed is the draw rather than a
        # measurement of it. Neither may rescue an inert arm.
        grouped = {
            "False": [report(value=False, wall_seconds=68.6, seed=1)],
            "True": [report(value=True, wall_seconds=71.2, seed=1)],
        }
        self.assertTrue(C._inert(grouped))

    def test_a_numeric_arm_can_be_reported_inert(self):
        """The blind spot that disabled this check for 40 of the 87 blocks - TRAPS 11.

        It kept working for string-valued arms, which is why nobody noticed.
        """
        self.assertTrue(C._inert({1: [report(value=1)], 2: [report(value=2)]}))

    def test_a_numeric_arm_with_a_real_difference_is_still_not_inert(self):
        """The other direction, or the fix above would just switch the check off."""
        self.assertFalse(
            C._inert({1: [report(value=1, held=0.80)], 2: [report(value=2, held=0.50)]})
        )

    def test_the_arms_own_value_is_not_evidence_that_it_did_something(self):
        self.assertIn("value", C.NOT_A_MEASUREMENT)

    def test_a_single_value_is_never_inert(self):
        self.assertFalse(C._inert({"only": [report()]}))


class Cells(unittest.TestCase):
    def test_seeds_are_averaged_and_spread_recorded(self):
        cells = C.cells_of([report(seed=1, held=0.7), report(seed=2, held=0.9)])
        self.assertEqual(len(cells), 1)
        self.assertAlmostEqual(cells[0]["metrics"]["held"], 0.8)
        self.assertEqual(cells[0]["seeds"], [1, 2])
        self.assertIn("held", cells[0]["sd"])

    def test_one_seed_records_no_spread(self):
        # A nightly run draws one seed per cell. Writing 0.0 as its spread would let the explorer
        # average a fiction into the runs that do have several.
        cells = C.cells_of([report(seed=1)])
        self.assertEqual(cells[0]["sd"], {})

    def test_values_keep_the_order_the_block_declares(self):
        reports = [report(value=v) for v in ("bucket", "interval", "aimd")]
        self.assertEqual(
            [c["value"] for c in C.cells_of(reports)], ["bucket", "interval", "aimd"]
        )


class ShardedBlocks(unittest.TestCase):
    """A block that arrives in several files is one block, not several.

    Shards are named apart on disk and carry the same `block` - MODEL.md.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def shards(self, directory):
        os.makedirs(directory, exist_ok=True)
        for seed, text in ((7, 0.6), (11, 0.7), (13, 0.8)):
            reports = [
                report(block="X-arm", value="off", seed=seed, text=text, held=0.0),
                report(block="X-arm", value="spread x3", seed=seed, text=text, held=0.5),
            ]
            with open(os.path.join(directory, f"X-arm.s{seed}.json"), "w") as f:
                json.dump(reports, f)
        return directory

    def test_three_shards_are_one_block(self):
        summary = C.collate(self.shards(os.path.join(self.tmp.name, "sharded")))
        self.assertEqual([b["block"] for b in summary["blocks"]], ["X-arm"])

    def test_the_seeds_are_averaged_across_the_shards(self):
        summary = C.collate(self.shards(os.path.join(self.tmp.name, "avg")))
        cells = {c["value"]: c for c in summary["blocks"][0]["cells"]}
        self.assertEqual(sorted(cells["off"]["seeds"]), [7, 11, 13])
        # (0.6 + 0.7 + 0.8) / 3, which only exists if all three files reached one cell.
        self.assertAlmostEqual(cells["off"]["metrics"]["text"], 0.7, places=6)
        self.assertIn("text", cells["off"]["sd"])

    def test_a_sharded_block_is_not_reported_missing(self):
        summary = C.collate(
            self.shards(os.path.join(self.tmp.name, "expect")), expected=["X-arm"]
        )
        self.assertEqual(summary["missing_blocks"], [])


class Gate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def test_a_silent_loss_fails_the_run(self):
        run = write_run(
            os.path.join(self.tmp.name, "r1"),
            {
                "B-arm": [
                    report(value=1),
                    report(value=2, sfpp__silent_losses=3, held=0.9),
                ]
            },
        )
        summary = C.collate(run)
        self.assertFalse(summary["gate"]["ok"])
        self.assertIn("SILENT LOSSES", summary["gate"]["failures"][0])

    def test_queue_drops_are_a_warning_not_a_failure(self):
        run = write_run(
            os.path.join(self.tmp.name, "r2"),
            {
                "B-arm": [
                    report(value=1),
                    report(value=2, traffic__queue_drops=9000, held=0.9),
                ]
            },
        )
        summary = C.collate(run)
        self.assertTrue(summary["gate"]["ok"])
        self.assertTrue(any("queue drops" in w for w in summary["gate"]["warnings"]))

    def test_a_block_that_never_ran_is_named(self):
        run = write_run(os.path.join(self.tmp.name, "r3"), {"B-arm": [report()]})
        summary = C.collate(run, expected={"B-arm", "B-missing"})
        self.assertEqual(summary["missing_blocks"], ["B-missing"])
        self.assertEqual(summary["gate"]["blocks_missing"], 1)

    def test_its_own_digest_is_not_read_back_as_a_block(self):
        run = write_run(os.path.join(self.tmp.name, "r4"), {"B-arm": [report()]})
        quietly(C.main, ["--runs", run])
        again = C.collate(run)
        self.assertEqual([b["block"] for b in again["blocks"]], ["B-arm"])


class Timing(unittest.TestCase):
    """The runtime comparison. TRAPS.md #7's missing check: `wall_seconds` was recorded and summed,
    and nothing compared it against a previous run."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def archive(self, rates, block="B-arm"):
        """A digest per prior run, each carrying one block at a given seconds-per-simulated-hour."""
        root = os.path.join(self.tmp.name, "archive")
        for i, rate in enumerate(rates):
            run = os.path.join(root, f"run-{i}")
            os.makedirs(run, exist_ok=True)
            with open(os.path.join(run, "summary.json"), "w") as f:
                json.dump(
                    {
                        "run_id": f"run-{i}",
                        "blocks": [{"block": block, "seconds_per_sim_hour": rate}],
                    },
                    f,
                )
        return root

    def run_at(self, seconds, hours, name="timing"):
        """One block whose cells each took `seconds` of wall-clock for `hours` of simulated time."""
        return write_run(
            os.path.join(self.tmp.name, name),
            {
                "B-arm": [
                    report(value=v, wall_seconds=seconds, opts={"nodes": 60, "hours": hours})
                    for v in (1, 2)
                ]
            },
        )

    def rate_of(self, summary, block="B-arm"):
        return next(b for b in summary["blocks"] if b["block"] == block)["seconds_per_sim_hour"]

    def drift(self, summary):
        """Only the timing kinds: these fixtures are two identical cells and legitimately inert too,
        so asserting on the whole warning list would fail for the wrong reason."""
        return {
            kind: counts
            for kind, counts in (summary["gate"]["warnings_by_kind"] or {}).items()
            if kind in ("slower", "faster")
        }

    def test_the_rate_is_wall_clock_over_simulated_hours(self):
        summary = C.collate(self.run_at(120.0, 24))
        # Two cells, 120 s each over 24 simulated hours each: 240 / 48.
        self.assertAlmostEqual(self.rate_of(summary), 5.0)

    def test_a_block_that_got_much_slower_is_flagged(self):
        summary = C.collate(
            self.run_at(1200.0, 24, name="slow"), history_dir=self.archive([5.0, 5.2, 4.9])
        )
        self.assertTrue(any("slower" in w for w in summary["gate"]["warnings"]))

    def test_a_slowdown_is_a_warning_not_a_failure(self):
        summary = C.collate(
            self.run_at(1200.0, 24, name="warnonly"), history_dir=self.archive([5.0, 5.2, 4.9])
        )
        self.assertTrue(summary["gate"]["ok"])
        self.assertEqual(summary["gate"]["failures"], [])

    def test_a_block_that_got_much_faster_is_also_flagged(self):
        # A fragmented mesh or an arm that stopped being read both cost less to simulate.
        summary = C.collate(
            self.run_at(12.0, 24, name="fast"), history_dir=self.archive([5.0, 5.2, 4.9])
        )
        self.assertTrue(any("faster" in w for w in summary["gate"]["warnings"]))

    def test_ordinary_runner_noise_is_not_flagged(self):
        summary = C.collate(
            self.run_at(150.0, 24, name="noise"), history_dir=self.archive([5.0, 5.2, 4.9])
        )
        self.assertEqual(self.drift(summary), {})

    def test_changing_hours_alone_does_not_read_as_a_regression(self):
        """The interaction that would have made this gate useless.

        Gating on raw wall_seconds would have flagged every block the night --hours was raised.
        """
        history = self.archive([5.0, 5.2, 4.9])
        # Three times the simulated hours, three times the wall clock: the same machine, same speed.
        summary = C.collate(self.run_at(360.0, 72, name="longer"), history_dir=history)
        self.assertAlmostEqual(self.rate_of(summary), 5.0)
        self.assertEqual(self.drift(summary), {})

    def test_a_block_new_to_the_archive_is_not_compared(self):
        summary = C.collate(
            self.run_at(9000.0, 24, name="new"), history_dir=self.archive([5.0], block="B-other")
        )
        self.assertEqual(self.drift(summary), {})

    def test_one_prior_run_is_not_enough_history(self):
        summary = C.collate(
            self.run_at(9000.0, 24, name="thin"), history_dir=self.archive([5.0])
        )
        self.assertEqual(self.drift(summary), {})

    def test_a_run_is_not_compared_against_itself(self):
        """A re-collate of the run in flight would otherwise find its own digest and never drift."""
        root = self.archive([5.0, 5.2, 4.9])
        mine = os.path.join(root, "mine")
        os.makedirs(mine, exist_ok=True)
        with open(os.path.join(mine, "summary.json"), "w") as f:
            json.dump(
                {"run_id": "mine", "blocks": [{"block": "B-arm", "seconds_per_sim_hour": 500.0}]}, f
            )
        summary = C.collate(
            self.run_at(1200.0, 24, name="self"), run_id="mine", history_dir=root
        )
        # Its own 500.0 excluded, the median is the archive's ~5 and the slowdown still shows.
        self.assertTrue(any("slower" in w for w in summary["gate"]["warnings"]))

    def test_a_cell_that_does_not_record_hours_is_not_rated(self):
        run = write_run(
            os.path.join(self.tmp.name, "nohours"),
            {"B-arm": [report(value=v, wall_seconds=99.0) for v in (1, 2)]},
        )
        summary = C.collate(run, history_dir=self.archive([5.0, 5.2, 4.9]))
        self.assertIsNone(self.rate_of(summary))
        self.assertEqual(self.drift(summary), {})

    def test_no_archive_means_no_comparison(self):
        summary = C.collate(self.run_at(9000.0, 24, name="noarchive"))
        self.assertEqual(self.drift(summary), {})

    def test_an_unreadable_digest_does_not_stop_the_comparison(self):
        root = self.archive([5.0, 5.2, 4.9])
        broken = os.path.join(root, "broken")
        os.makedirs(broken, exist_ok=True)
        with open(os.path.join(broken, "summary.json"), "w") as f:
            f.write("{not json")
        summary = C.collate(self.run_at(1200.0, 24, name="broken"), history_dir=root)
        self.assertTrue(any("slower" in w for w in summary["gate"]["warnings"]))

    def test_a_drift_flag_is_a_sentence_not_a_pair(self):
        """The bug the page build died on, and it died in integration rather than here.

        Every flag must be a plain string by the time it reaches the digest.
        """
        summary = C.collate(
            self.run_at(1200.0, 24, name="strflag"), history_dir=self.archive([5.0, 5.2, 4.9])
        )
        for block in summary["blocks"]:
            for flag in block["flags"]:
                self.assertIsInstance(flag, str, flag)
        # And it survives the JSON round trip the archive actually does.
        for block in json.loads(json.dumps(summary))["blocks"]:
            self.assertTrue(all(isinstance(f, str) for f in block["flags"]))

    def test_a_drift_flag_is_counted_in_the_kinds(self):
        """The other half of the same bug: the kind never reached `flag_kinds`, so the gate added to
        catch a runtime regression was itself invisible to the page that groups by kind."""
        summary = C.collate(
            self.run_at(1200.0, 24, name="kindflag"), history_dir=self.archive([5.0, 5.2, 4.9])
        )
        self.assertIn("slower", summary["gate"]["warnings_by_kind"])
        self.assertEqual(
            summary["gate"]["warnings_by_kind"]["slower"], {"flags": 1, "blocks": 1}
        )

    def test_the_trend_report_names_a_drifted_block(self):
        md = C.markdown(
            C.collate(self.run_at(1200.0, 24, name="md"), history_dir=self.archive([5.0, 5.2, 4.9]))
        )
        self.assertIn("Runtime against this block's own history", md)
        self.assertIn("B-arm", md)


class Trend(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def test_blocks_rank_by_how_far_held_travels(self):
        run = write_run(
            os.path.join(self.tmp.name, "r"),
            {
                "A-small": [
                    report(block="A-small", value=1, held=0.80),
                    report(block="A-small", value=2, held=0.81),
                ],
                "B-large": [
                    report(block="B-large", value=1, held=0.50),
                    report(block="B-large", value=2, held=0.90),
                ],
            },
        )
        md = C.markdown(C.collate(run))
        self.assertLess(md.index("`B-large`"), md.index("`A-small`"))

    def test_the_report_names_the_run_and_its_ground(self):
        run = write_run(os.path.join(self.tmp.name, "r"), {"B-arm": [report()]})
        md = C.markdown(
            C.collate(run, run_id="2026-08-19-4711", seed_base="4711", scenario="ridge")
        )
        self.assertIn("2026-08-19-4711", md)
        self.assertIn("ridge", md)
        self.assertIn("4711", md)

    def test_main_writes_both_artefacts(self):
        run = write_run(os.path.join(self.tmp.name, "r"), {"B-arm": [report()]})
        self.assertEqual(quietly(C.main, ["--runs", run, "--run-id", "x"]), 0)
        self.assertTrue(os.path.exists(os.path.join(run, "summary.json")))
        self.assertTrue(os.path.exists(os.path.join(run, "trend.md")))

    def test_fail_on_gate_is_the_only_non_zero_exit(self):
        run = write_run(
            os.path.join(self.tmp.name, "r"),
            {
                "B-arm": [
                    report(value=1),
                    report(value=2, sfpp__silent_losses=1, held=0.9),
                ]
            },
        )
        self.assertEqual(quietly(C.main, ["--runs", run]), 0)
        self.assertEqual(quietly(C.main, ["--runs", run, "--fail-on-gate"]), 1)


class Explorer(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.archive = os.path.join(self.tmp.name, "runs")
        for run_id, held in (("2026-08-19-1", 0.80), ("2026-08-20-2", 0.84)):
            run = write_run(
                os.path.join(self.archive, run_id),
                {
                    "B-arm": [
                        report(value=1, held=held),
                        report(value=2, held=held + 0.05),
                    ]
                },
            )
            quietly(
                C.main,
                [
                    "--runs",
                    run,
                    "--run-id",
                    run_id,
                    "--seed-base",
                    run_id.split("-")[-1],
                    "--scenario",
                    "ridge",
                ],
            )

    def test_runs_load_oldest_first(self):
        runs = E.load_archive(self.archive)
        self.assertEqual([r["run_id"] for r in runs], ["2026-08-19-1", "2026-08-20-2"])

    def test_window_keeps_the_most_recent(self):
        runs = E.load_archive(self.archive, window=1)
        self.assertEqual([r["run_id"] for r in runs], ["2026-08-20-2"])

    def test_an_unreadable_digest_does_not_stop_the_rollup(self):
        broken = os.path.join(self.archive, "2026-08-21-3")
        os.makedirs(broken)
        with open(os.path.join(broken, "summary.json"), "w") as f:
            f.write("{ this is not json")
        self.assertEqual(len(E.load_archive(self.archive)), 2)

    def test_a_block_is_indexed_across_every_run_that_has_it(self):
        blocks = E.index_by_block(E.load_archive(self.archive))
        self.assertEqual(len(blocks["B-arm"]["runs"]), 2)

    def test_leaderboard_averages_rather_than_pools(self):
        # Both runs spread held by 0.05, so the average spread is 0.05 however many runs there are.
        board = E.leaderboard(E.index_by_block(E.load_archive(self.archive)))
        self.assertAlmostEqual(board[0]["spread"], 0.05, places=6)
        self.assertEqual(board[0]["runs"], 2)

    def test_a_gap_breaks_the_sparkline_rather_than_bridging_it(self):
        # A block missing from one run must not draw a straight line through the run it missed.
        svg = E.sparkline([0.1, None, 0.9, 0.95])
        self.assertEqual(svg.count("<polyline"), 1)
        self.assertIn("polyline", E.sparkline([0.1, 0.2, None, 0.8, 0.9]))

    def test_series_holds_a_place_for_a_value_a_run_lacks(self):
        blocks = E.index_by_block(E.load_archive(self.archive))
        blocks["B-arm"]["runs"][0]["cells"].pop("2")
        self.assertEqual(E.series(blocks["B-arm"], "held")["2"][0], None)

    def test_the_page_is_self_contained_and_names_every_run(self):
        runs = E.load_archive(self.archive)
        for r in runs:
            r["_href"] = os.path.join("runs", r["_name"])
        page = E.render_html(
            runs, E.index_by_block(runs), E.leaderboard(E.index_by_block(runs))
        )
        self.assertIn("2026-08-19-1", page)
        self.assertIn("2026-08-20-2", page)
        # Self-contained means it fetches nothing, not that it links nowhere: a citation is a
        # link the reader may follow. The page has to render identically opened from disk.
        for loader in (
            "<script src",
            '<link rel="stylesheet"',
            "@import",
            "url(http",
            "fetch(",
            "XMLHttpRequest",
            "fonts.googleapis",
        ):
            self.assertNotIn(
                loader, page, f"the page pulls in something external: {loader}"
            )

    def test_every_shown_metric_has_an_axis_and_a_colour(self):
        """A register invariant: a metric added to SHOWN and nowhere else draws on an axis whose
        heights mean nothing, silently pooled into a family called "other"."""
        for key, label, _ in E.SHOWN:
            self.assertIn(key, E.UNITS, f"{key} is charted with no unit family")
            self.assertIn(E.UNITS[key], E.UNIT_AXIS, f"{key}'s family has no axis label")
            self.assertIn(key, E.SERIES_COLOURS, f"{key} has no series colour")

    def test_the_chart_offers_a_checkbox_per_field_and_opens_on_what_moved(self):
        runs = E.load_archive(self.archive)
        for r in runs:
            r["_href"] = "runs/" + r["_name"]
        blocks = E.index_by_block(runs)
        page = E.render_html(runs, blocks, [])
        # One box per field, so a reader picks the comparison rather than clicking through it.
        for key, label, _ in E.SHOWN:
            self.assertIn(f'type="checkbox" class="metric" value="{key}"', page)
        self.assertNotIn('select class="metric"', page)
        # Ticked on arrival: the measure collate says the block moves in.
        moved = blocks["B-arm"].get("moved") or "held"
        self.assertIn(f'value="{moved}" checked', page)
        # The renderer needs the units to refuse a shared axis across families.
        self.assertIn('id="chartmeta"', page)
        self.assertIn("channel/air utilisation", page)

    def test_the_pages_role_marks_match_the_drawn_maps(self):
        """explorer.MAP_MARKS duplicates meshmap.ROLE_MARKS so the page can draw a legend with
        meshmap absent. Pinned equal here, because two pictures of one mesh disagreeing on what a
        square means is worse than either alone."""
        from . import meshmap as MM

        self.assertEqual(
            [[role, shape, colour] for role, (shape, colour, _) in MM.ROLE_MARKS.items()],
            E.MAP_MARKS[:-1],
        )
        # The last entry is meshmap's UNKNOWN_ROLE, which mesh_data indexes as len(ROLE_MARKS).
        self.assertEqual(E.MAP_MARKS[-1][1:], list(MM.UNKNOWN_ROLE[:2]))
        self.assertEqual(E.MAP_FRAGILE, MM.FRAGILE)
        self.assertEqual(E.MAP_LINK, MM.LINK)

    def test_a_block_name_cannot_inject_markup(self):
        runs = E.load_archive(self.archive)
        runs[0]["blocks"][0]["block"] = "<script>alert(1)</script>"
        for r in runs:
            r["_href"] = "runs/" + r["_name"]
        page = E.render_html(runs, E.index_by_block(runs), [])
        self.assertNotIn("<script>alert(1)</script>", page)
        self.assertIn("&lt;script&gt;", page)

    def test_main_writes_a_page_and_a_digest(self):
        out = os.path.join(self.tmp.name, "site")
        self.assertEqual(quietly(E.main, ["--archive", self.archive, "--out", out]), 0)
        self.assertTrue(os.path.exists(os.path.join(out, "index.html")))
        with open(os.path.join(out, "INDEX.md")) as f:
            self.assertIn("2026-08-20-2", f.read())

    def test_links_are_relative_to_the_page_not_the_archive(self):
        out = os.path.join(self.tmp.name, "site2")
        quietly(E.main, ["--archive", self.archive, "--out", out])
        with open(os.path.join(out, "index.html")) as f:
            page = f.read()
        # The page sits beside `runs/`, so a run's report is one directory down from it.
        self.assertIn("runs/2026-08-20-2/trend.md", page.replace("../", ""))

    def test_an_empty_archive_says_so_rather_than_writing_a_blank_page(self):
        self.assertEqual(
            quietly(
                E.main,
                [
                    "--archive",
                    os.path.join(self.tmp.name, "nothing"),
                    "--out",
                    self.tmp.name,
                ],
            ),
            1,
        )


if __name__ == "__main__":
    unittest.main()


class Tabs(unittest.TestCase):
    """The schedule and run-health panels, and the tab shell around them."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def archive(self, runs):
        """{run_id: digest} on disk, the way collate leaves an archive."""
        root = os.path.join(self.tmp.name, "arch")
        for rid, digest in runs.items():
            d = os.path.join(root, rid)
            os.makedirs(d, exist_ok=True)
            digest.setdefault("run_id", rid)
            with open(os.path.join(d, "summary.json"), "w") as f:
                json.dump(digest, f)
        runs = E.load_archive(root)
        # `_href` is stamped by main(), not by load_archive - the link base differs between the copy
        # on the data branch and the published one. Mirrored here so render_html is exercised the way
        # it is actually called.
        for r in runs:
            r["_href"] = r["_name"]
        return runs

    def digest(self, block="B-arm", **over):
        d = {
            "blocks": [
                {
                    "block": block,
                    "arm": "arm",
                    "cells": [],
                    "wall_seconds": 120.0,
                    "seconds_per_sim_hour": 5.0,
                    "flags": [],
                    "flag_kinds": {},
                }
            ],
            "gate": {"ok": True, "blocks_run": 1, "blocks_missing": 0, "warnings": []},
            "wall_seconds": 120.0,
        }
        d.update(over)
        return d

    def test_the_schedule_separates_never_run_from_not_in_the_latest_run(self):
        """The distinction the tab exists for. A weekly cell absent from tonight's run is not
        outstanding work; a cell that has never run once is."""
        runs = self.archive({"r1": self.digest("A"), "r2": self.digest("B")})
        sched = E.schedule(runs, {"surface": {"A": "ran once.", "B": "ran once.", "C": "never."}})
        rows = {r["cell"]: r for r in sched["surfaces"][0]["rows"]}
        self.assertEqual(rows["A"]["runs"], 1)
        self.assertFalse(rows["A"]["in_latest"])  # ran, but not in the latest run
        self.assertTrue(rows["B"]["in_latest"])
        self.assertEqual(rows["C"]["runs"], 0)  # the one that is actually outstanding
        self.assertEqual(sched["surfaces"][0]["never_run"], 1)
        self.assertEqual(sched["surfaces"][0]["ever_run"], 2)

    def test_a_cell_in_the_archive_that_nothing_declares_is_named(self):
        """A renamed or retired cell whose results are still in the branch. Not an error - but it is
        why an ever-run count can exceed the declared one, and silence there reads as a miscount."""
        runs = self.archive({"r1": self.digest("retired-cell")})
        sched = E.schedule(runs, {"surface": {"current": "declared."}})
        self.assertEqual(sched["undeclared"], ["retired-cell"])

    def test_the_declared_side_survives_having_no_producers(self):
        """An archive read on a machine without the simulator. The honest answer is no declared side,
        not a traceback - which is how collate.describe() already guards the same import."""
        sched = E.schedule(self.archive({"r1": self.digest()}), {})
        self.assertEqual(sched["surfaces"], [])

    def test_every_declared_surface_is_reachable(self):
        """The real producers, so a renamed module shows up here rather than as an empty tab."""
        self.assertEqual(sorted(E.declared_surfaces()), ["blocks", "design", "matrix"])

    def test_run_health_reports_duration_both_ways(self):
        """A total and a rate. The total decides whether a job fits its ceiling; only the rate is
        comparable between runs of different length."""
        health = E.run_health(self.archive({"r1": self.digest()}))
        self.assertEqual(health[0]["wall_seconds"], 120.0)
        self.assertEqual(health[0]["median_rate"], 5.0)

    def test_run_health_carries_the_flag_kinds_and_the_drift(self):
        digest = self.digest()
        digest["blocks"][0]["flag_kinds"] = {"inert": 1}
        digest["blocks"][0]["timing"] = {
            "seconds_per_sim_hour": 30.0,
            "median": 5.0,
            "ratio": 6.0,
            "runs_compared": 3,
        }
        digest["gate"]["warnings_by_kind"] = {"inert": {"flags": 1, "blocks": 1}}
        health = E.run_health(self.archive({"r1": digest}))
        self.assertEqual(health[0]["by_kind"], {"inert": {"flags": 1, "blocks": 1}})
        self.assertEqual(health[0]["drifted"][0]["ratio"], 6.0)

    def test_the_page_has_a_panel_for_every_tab(self):
        runs = self.archive({"r1": self.digest()})
        html = E.render_html(runs, E.index_by_block(runs), E.leaderboard(E.index_by_block(runs)))
        for tab in ("trend", "blocks", "schedule", "health", "runs"):
            self.assertIn(f'data-tab="{tab}" role="tab"', html, tab)
            self.assertIn(f'class="tab-panel" data-tab="{tab}"', html, tab)
        self.assertEqual(html.count('<section class="tab-panel"'), html.count("</section>"))

    def test_the_page_stays_readable_without_javascript(self):
        """The panels carry `hidden` so the first paint shows one tab, so the UA's own [hidden]
        rule has to be overridden - or the page is four hidden panels and an inert nav."""
        runs = self.archive({"r1": self.digest()})
        html = E.render_html(runs, E.index_by_block(runs), E.leaderboard(E.index_by_block(runs)))
        override = html.find(".tab-panel[hidden] { display: block; }")
        gated = html.find("body.tabbed .tab-panel[hidden] { display: none; }")
        self.assertGreater(override, 0)
        self.assertLess(override, gated, "the gated rule must come after the override")
        # And nothing but the script may add the class that does the hiding.
        self.assertIn("classList.add('tabbed')", html)

    def test_the_page_is_still_self_contained(self):
        """No CDN, no fetch, no external script - it is served from a git branch and read as a file."""
        runs = self.archive({"r1": self.digest()})
        html = E.render_html(runs, E.index_by_block(runs), E.leaderboard(E.index_by_block(runs)))
        self.assertNotIn("fetch(", html)
        self.assertNotIn("<script src", html)
        self.assertNotIn("<link rel=\"stylesheet\"", html)


class ScenarioTruth(unittest.TestCase):
    """A landform the run asked for but no block recorded must be visible as such."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _page(self, observed):
        archive = os.path.join(self.tmp.name, "runs")
        run = write_run(
            os.path.join(archive, "2026-08-19-1"),
            {
                "B-arm": [
                    report(value=1, opts={"scenario": observed}),
                    report(value=2, held=0.9, opts={"scenario": observed}),
                ]
            },
        )
        quietly(
            C.main, ["--runs", run, "--run-id", "2026-08-19-1", "--scenario", "ridge"]
        )
        runs = E.load_archive(archive)
        for r in runs:
            r["_href"] = "runs/" + r["_name"]
        return E.render_html(runs, E.index_by_block(runs), [])

    def test_ground_that_reached_the_blocks_is_not_flagged(self):
        self.assertNotIn("not applied", self._page("ridge"))

    def test_ground_that_never_reached_the_blocks_is_flagged(self):
        self.assertIn("not applied", self._page(None))


class NewGates(unittest.TestCase):
    """The gates the handover names, each against the defect it caught.

    Fatal means the run's other numbers cannot be trusted; everything else warns.
    """

    def _flags(self, **overrides):
        """(fatal, warn) as (kind, sentence) pairs, which is check_cell's contract."""
        return C.check_cell(report(**overrides), "arm=1")

    def kinds(self, entries):
        return [kind for kind, _ in entries]

    def sentences(self, entries):
        return [text for _, text in entries]

    def test_a_node_cannot_exceed_100_percent_channel_utilisation(self):
        # A receiver charging itself for every transmitter it collided with ran this to 184%.
        fatal, _ = self._flags(
            traffic__node_channel_util_percent={"p90": 90.0, "max": 184.0}
        )
        self.assertEqual(self.kinds(fatal), ["chutil-impossible"])
        self.assertTrue(any("physically impossible" in f for f in self.sentences(fatal)))

    def test_demand_above_one_is_not_a_failure(self):
        # Aggregate demand legitimately exceeds 1.0 and says nothing about local headroom. Gating on
        # it would fail every spatially extended mesh.
        fatal, warn = self._flags(traffic__channel_utilisation=9.55)
        self.assertEqual(fatal, [])
        self.assertEqual(warn, [])

    def test_a_scenario_that_recorded_no_ground_is_fatal(self):
        # The Scenario with no nodes was falsy, so the run came out flat under an alpine label.
        fatal, _ = self._flags(opts={"scenario": "alpine"}, ground=None)
        self.assertEqual(self.kinds(fatal), ["no-ground"])
        self.assertTrue(any("recorded no ground" in f for f in self.sentences(fatal)))

    def test_a_scenario_that_applied_no_terrain_warns(self):
        fatal, warn = self._flags(
            opts={"scenario": "alpine"},
            ground={"terrain_applied": False, "fixed_geometry": False},
        )
        self.assertEqual(fatal, [])
        self.assertEqual(self.kinds(warn), ["no-terrain"])
        self.assertTrue(any("applied no terrain" in w for w in self.sentences(warn)))

    def test_the_at_rest_audit_disagreeing_is_fatal(self):
        fatal, _ = self._flags(sfpp__audit_checksum_agrees_sets_differ=2)
        self.assertEqual(self.kinds(fatal), ["audit-disagrees"])
        self.assertTrue(any("at-rest audit" in f for f in self.sentences(fatal)))

    def test_a_capped_placement_is_named(self):
        # `routers` and `beside-router` cap at the router count, so a sweep over 2-6 servers can
        # produce three real rows and two repeats of the fourth.
        _, warn = self._flags(sfpp__servers_requested=6, sfpp__servers_placed=4)
        self.assertEqual(self.kinds(warn), ["placement-capped"])
        self.assertTrue(
            any("6 archives requested, 4 placed" in w for w in self.sentences(warn))
        )

    def test_pairs_outside_the_fit_envelope_are_named(self):
        _, warn = self._flags(
            ground={
                "link_calibration_loaded": True,
                "pairs_beyond_calibration": 812,
                "calibration_envelope_m": 23200,
                "terrain_applied": True,
            }
        )
        self.assertEqual(self.kinds(warn), ["beyond-envelope"])
        self.assertTrue(any("beyond the fit" in w for w in self.sentences(warn)))

    def test_a_clean_cell_raises_nothing(self):
        fatal, warn = self._flags()
        self.assertEqual((fatal, warn), ([], []))

    def test_every_kind_this_module_can_raise_is_in_the_vocabulary(self):
        """A check that invents a kind is a flag the run-health page silently will not group.

        Exercised through the reports that trigger each gate, not by reading the source.
        """
        triggers = [
            {"traffic__node_channel_util_percent": {"p90": 9.0, "max": 184.0}},
            {"opts": {"scenario": "alpine"}, "ground": None},
            {
                "opts": {"scenario": "alpine"},
                "ground": {"terrain_applied": False, "fixed_geometry": False},
            },
            {"sfpp__silent_losses": 3},
            {"sfpp__audit_checksum_agrees_sets_differ": 2},
            {
                "ground": {
                    "link_calibration_loaded": True,
                    "pairs_beyond_calibration": 812,
                    "calibration_envelope_m": 23200,
                    "terrain_applied": True,
                }
            },
            {"sfpp__servers_requested": 6, "sfpp__servers_placed": 4},
            {"traffic__transmissions": 100, "traffic__queue_drops": 40},
            {"sfpp__misdecodes": 2},
            {"sfpp__decode_failures": 5},
        ]
        raised = set()
        for override in triggers:
            fatal, warn = self._flags(**override)
            raised.update(self.kinds(fatal) + self.kinds(warn))
        self.assertEqual(sorted(raised - set(C.FLAG_KINDS)), [])
        # And every one of those gates actually fired, or the assertion above proves nothing.
        self.assertGreaterEqual(len(raised), 9)


class FourSuccesses(unittest.TestCase):
    def test_admin_is_weighted_by_sessions_not_averaged_over_hops(self):
        # Two hop distances, one with fifty sessions and one with two. Averaging the rates would
        # weight them equally: (1.0 + 0.0) / 2 = 0.5, against the true 50/52.
        rate = C.admin_success_rate(
            {
                "1": {"sessions": 50, "session_completed": 50},
                "5": {"sessions": 2, "session_completed": 0},
            }
        )
        self.assertAlmostEqual(rate, round(50 / 52, 4))

    def test_node_count_comes_from_a_fixed_geometry_scenario(self):
        # Batumi is 92 nodes whatever --nodes said, and recording the request instead has already
        # produced a wrong conclusion here.
        r = report(ground={"fixed_geometry": True, "nodes": 92}, mesh={"nodes": 60})
        self.assertEqual(C.metric(r, "nodes"), 92)

    def test_node_count_falls_back_to_the_built_mesh(self):
        self.assertEqual(C.metric(report(), "nodes"), 60)

    def test_the_block_names_which_measure_it_moved(self):
        # held is flat, DM success is not: the block moved DM and must be ranked and labelled on it.
        block = C.summarise_block(
            [
                report(
                    value=1,
                    dm={
                        "reception": 0.99,
                        "composed": 120,
                        "no_key": 0,
                        "no_addressable_peer": 0,
                    },
                ),
                report(
                    value=2,
                    dm={
                        "reception": 0.42,
                        "composed": 120,
                        "no_key": 0,
                        "no_addressable_peer": 0,
                    },
                ),
            ]
        )
        self.assertEqual(block["moved"], "dm")
        self.assertAlmostEqual(block["effect"]["dm"]["spread"], 0.57, places=6)

    def test_a_missing_measure_does_not_rank_the_block(self):
        # No DM traffic in the run at all: `dm` is null and must not be read as zero.
        block = C.summarise_block(
            [report(value=1, dm=None), report(value=2, dm=None, held=0.9)]
        )
        self.assertEqual(block["moved"], "held")
        self.assertNotIn("dm", block["effect"])


class ThinDenominators(unittest.TestCase):
    """A measure with almost no observations must not decide where a block ranks.

    Two sessions make one failure a 50% swing. Still reported, but it cannot win. MODEL.md.
    """

    def test_two_sessions_cannot_rank_a_block(self):
        block = C.summarise_block(
            [
                report(
                    value=1,
                    admin={"1": {"sessions": 2, "session_completed": 2}},
                    held=0.80,
                ),
                report(
                    value=2,
                    admin={"1": {"sessions": 2, "session_completed": 1}},
                    held=0.81,
                ),
            ]
        )
        self.assertIn("admin", block["thin"])
        self.assertEqual(block["moved"], "held")

    def test_a_real_denominator_can(self):
        block = C.summarise_block(
            [
                report(
                    value=1,
                    admin={"1": {"sessions": 60, "session_completed": 60}},
                    held=0.80,
                ),
                report(
                    value=2,
                    admin={"1": {"sessions": 60, "session_completed": 30}},
                    held=0.81,
                ),
            ]
        )
        self.assertEqual(block["thin"], [])
        self.assertEqual(block["moved"], "admin")

    def test_broadcast_reach_never_needs_a_denominator(self):
        # text is measured over every node of every broadcast; there is no small-sample case.
        block = C.summarise_block(
            [report(value=1, text=0.5), report(value=2, text=0.9)]
        )
        self.assertNotIn("text", block["thin"])


class PublishedCopy(unittest.TestCase):
    """The copy that goes to the public site differs from the one on the data branch in two ways."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.archive = os.path.join(self.tmp.name, "runs")
        run = write_run(
            os.path.join(self.archive, "2026-08-19-1"), {"B-arm": [report()]}
        )
        quietly(C.main, ["--runs", run, "--run-id", "2026-08-19-1"])

    def _build(self, *extra):
        out = os.path.join(self.tmp.name, "site" + str(len(extra)))
        quietly(E.main, ["--archive", self.archive, "--out", out, *extra])
        return out

    def test_it_is_not_called_index(self):
        # The site has its own index and this is one page on it.
        out = self._build("--name", "meshtasticatom-explorer.html")
        self.assertTrue(
            os.path.exists(os.path.join(out, "meshtasticatom-explorer.html"))
        )
        self.assertFalse(os.path.exists(os.path.join(out, "index.html")))

    def test_report_links_point_at_the_archive_absolutely(self):
        # `runs/` exists on the data branch, not on the site. A relative link would 404 there.
        base = "https://github.com/NomDeTom/Meshtasticatom/blob/sim-results/runs"
        out = self._build("--name", "e.html", "--link-base", base)
        with open(os.path.join(out, "e.html")) as f:
            page = f.read()
        self.assertIn(f"{base}/2026-08-19-1/trend.md", page)

    def test_the_back_link_is_only_on_the_published_copy(self):
        with open(os.path.join(self._build("--name", "a.html"), "a.html")) as f:
            self.assertNotIn('href="index.html"', f.read())
        with open(
            os.path.join(self._build("--name", "b.html", "--for-pages"), "b.html")
        ) as f:
            page = f.read()
        self.assertIn('<a class="action-btn" href="index.html">Back to index</a>', page)

    def test_the_house_top_action_order_is_kept(self):
        # Back, theme, license - the site requires exactly this order.
        with open(
            os.path.join(self._build("--name", "c.html", "--for-pages"), "c.html")
        ) as f:
            page = f.read()
        self.assertLess(page.index('href="index.html"'), page.index("toggle-theme-btn"))
        self.assertLess(
            page.index("toggle-theme-btn"), page.index("toggle-license-btn")
        )

    def test_the_licence_is_the_simulator_s_own(self):
        # Meshtasticator is CC BY 4.0 and its radio model descends from LoRaSim; the page carries
        # that chain rather than the site's usual licence.
        with open(
            os.path.join(self._build("--name", "d.html", "--for-pages"), "d.html")
        ) as f:
            page = f.read()
        self.assertIn("CC BY 4.0", page)
        self.assertIn("creativecommons.org/licenses/by/4.0/", page)
        self.assertIn("LoRaSim", page)

    def test_no_local_paths_leak_into_the_published_page(self):
        # The site forbids local filesystem paths in anything published, and the archive is read
        # from an absolute path on whatever machine built it.
        with open(
            os.path.join(self._build("--name", "f.html", "--for-pages"), "f.html")
        ) as f:
            page = f.read()
        self.assertNotIn(self.tmp.name, page)
        self.assertNotIn("/home/", page)


class LicenceOnThePage(unittest.TestCase):
    """The page states the licence of the code that produced it, not the site's usual one."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        archive = os.path.join(self.tmp.name, "runs")
        run = write_run(os.path.join(archive, "r1"), {"B-arm": [report()]})
        quietly(C.main, ["--runs", run, "--run-id", "r1"])
        out = os.path.join(self.tmp.name, "site")
        quietly(
            E.main,
            ["--archive", archive, "--out", out, "--name", "p.html", "--for-pages"],
        )
        with open(os.path.join(out, "p.html")) as f:
            self.page = f.read()

    def test_it_names_both_licences(self):
        # GPL-3.0 for the simulator, because parts of it are transcribed from the firmware; CC BY
        # 4.0 for the Meshtasticator half, whose attribution has to survive either way.
        self.assertIn("GPL-3.0", self.page)
        self.assertIn("CC BY 4.0", self.page)

    def test_it_says_output_is_not_the_program(self):
        # A GPL program's output is not covered by the GPL, and a reader quoting a figure from this
        # page should not have to work that out for themselves.
        self.assertIn("output is not the", self.page)

    def test_the_upstream_chain_survives(self):
        self.assertIn("LoRaSim", self.page)


class PriceOfAnArm(unittest.TestCase):
    """An arm that holds delivery flat and moves what it spends has done something."""

    def _block(self, **second):
        return C.summarise_block([report(value="a"), report(value="b", **second)])

    def test_a_flat_arm_that_moves_bytes_is_priced(self):
        # SF-resolve: enum advertises with a fifth of sketch's bytes and delivers the same.
        block = self._block(sfpp__advert_bytes=2538)
        self.assertIsNone(block["moved"])
        self.assertEqual(block["cost"]["metric"], "advert_bytes")
        self.assertAlmostEqual(block["cost"]["ratio"], 12555 / 2538, places=6)

    def test_the_largest_ratio_wins(self):
        block = self._block(sfpp__advert_bytes=12555 * 2, sfpp__sr_bytes=36212 * 5)
        self.assertEqual(block["cost"]["metric"], "sr_bytes")

    def test_an_arm_that_costs_nothing_extra_is_not_priced(self):
        self.assertIsNone(self._block()["cost"])

    def test_a_zero_counter_is_not_a_ratio(self):
        # Dividing by a cell that spent nothing would report an infinite price.
        self.assertIsNone(self._block(sfpp__advert_bytes=0)["cost"])

    def test_the_report_says_what_a_flat_block_moved(self):
        run = write_run(
            os.path.join(tempfile.mkdtemp(), "r"),
            {"B-arm": [report(value="a"), report(value="b", sfpp__advert_bytes=2538)]},
        )
        md = C.markdown(C.collate(run))
        self.assertIn("Moved no delivery measure", md)
        self.assertIn("advert_bytes", md)
        self.assertNotIn("moved no delivery measure: `B-arm`.", md)


class AgainstControl(unittest.TestCase):
    """A cell that names a control is read as a difference from it, not as a bare number."""

    def _cells(self, *values):
        return C.cells_of([report(value=v, text=t, held=h) for v, t, h in values])

    def test_each_arm_is_differenced_against_the_control(self):
        cells = self._cells(("control", 0.700, 0.000), ("archive", 0.742, 0.860))
        C.against_control(cells)
        arm = next(c for c in cells if c["value"] == "archive")
        self.assertAlmostEqual(arm["vs_control"]["text"], 0.042, places=6)
        self.assertAlmostEqual(arm["vs_control"]["held"], 0.860, places=6)

    def test_the_control_keeps_a_row_reading_zero(self):
        # It has to stay visible: a table of differences with the thing differenced away is a table
        # nobody can check.
        cells = self._cells(("control", 0.700, 0.0), ("archive", 0.742, 0.86))
        C.against_control(cells)
        control = next(c for c in cells if c["value"] == "control")
        self.assertEqual(control["vs_control"]["text"], 0.0)

    def test_a_block_without_a_control_is_left_alone(self):
        # The block sweeps have no control arm; their arms are read against each other.
        cells = self._cells(("sketch", 0.7, 0.85), ("enum", 0.7, 0.86))
        C.against_control(cells)
        self.assertNotIn("vs_control", cells[0])

    def test_a_measure_the_control_never_recorded_is_not_differenced(self):
        # A DM figure needs DM traffic; subtracting from a null reads as a loss of the whole value.
        cells = C.cells_of(
            [
                report(value="control", dm=None),
                report(value="archive", dm={"reception": 0.9, "composed": 100}),
            ]
        )
        C.against_control(cells)
        arm = next(c for c in cells if c["value"] == "archive")
        self.assertNotIn("dm", arm["vs_control"])
        self.assertIn("text", arm["vs_control"])


class SupersededRuns(unittest.TestCase):
    """A version bump means earlier runs answered a different question - see sfpp/version.py."""

    @staticmethod
    def _run(version, run_id="2026-08-01"):
        return {"run_id": run_id, "sim_version": version, "_name": run_id, "blocks": []}

    def test_a_patch_bump_stays_comparable(self):
        # PATCH cannot move a number, so 1.2.0 and 1.2.7 measured the same thing.
        current, stale = E.comparable_runs(
            [self._run("1.2.0"), self._run("1.2.7")], version="1.2.0"
        )
        self.assertEqual(len(current), 2)
        self.assertEqual(stale, [])

    def test_a_minor_bump_supersedes(self):
        current, stale = E.comparable_runs(
            [self._run("1.1.0", "old"), self._run("1.2.0", "new")], version="1.2.0"
        )
        self.assertEqual([r["run_id"] for r in current], ["new"])
        self.assertEqual([r["run_id"] for r in stale], ["old"])

    def test_a_run_from_before_versioning_is_not_comparable(self):
        # No version is not "the current one": it is a digest that cannot claim to be comparable.
        current, stale = E.comparable_runs([self._run(None)], version="1.2.0")
        self.assertEqual(current, [])
        self.assertEqual(len(stale), 1)

    def test_a_run_straddling_a_bump_is_not_comparable(self):
        # collate writes a list when one round's blocks disagree, which is exactly not one version.
        current, stale = E.comparable_runs(
            [self._run(["1.1.0", "1.2.0"])], version="1.2.0"
        )
        self.assertEqual(current, [])
        self.assertEqual(len(stale), 1)

    def test_superseded_runs_reach_neither_the_leaderboard_nor_the_trend(self):
        old = write_run(
            os.path.join(self.tmp.name, "runs", "2026-08-01"),
            {"B-arm": [report(value=1, held=0.1), report(value=2, held=0.9)]},
        )
        quietly(C.main, ["--runs", old, "--run-id", "2026-08-01"])
        new = write_run(
            os.path.join(self.tmp.name, "runs", "2026-08-20"),
            {"B-arm": [report(value=1, held=0.5), report(value=2, held=0.5)]},
        )
        quietly(C.main, ["--runs", new, "--run-id", "2026-08-20"])
        self._age_run("2026-08-01", "1.1.0")

        archive = E.load_archive(os.path.join(self.tmp.name, "runs"))
        self.assertEqual(len(archive), 2)
        current, stale = E.comparable_runs(archive)
        self.assertEqual([r["run_id"] for r in current], ["2026-08-20"])

        # The old run's spread is 0.8 and the new one's is 0.0. Pooled they average to 0.4, which
        # is a number describing neither run.
        board = E.leaderboard(E.index_by_block(current))
        self.assertEqual(len(board), 1)
        self.assertAlmostEqual(board[0]["spread"], 0.0, places=6)
        self.assertEqual(board[0]["runs"], 1)

    def test_run_health_still_carries_the_superseded_runs(self):
        # Seconds per simulated hour does not care what the airtime was, so the cost history stays.
        self.test_superseded_runs_reach_neither_the_leaderboard_nor_the_trend()
        archive = E.load_archive(os.path.join(self.tmp.name, "runs"))
        current, stale = E.comparable_runs(archive)
        health = E.run_health(list(current) + list(stale))
        self.assertEqual(len(health), 2)

    def test_the_page_says_what_it_excluded(self):
        self.test_superseded_runs_reach_neither_the_leaderboard_nor_the_trend()
        archive = E.load_archive(os.path.join(self.tmp.name, "runs"))
        current, stale = E.comparable_runs(archive)
        for r in archive:
            r["_href"] = os.path.join("runs", r["_name"])
        page = E.render_html(current, E.index_by_block(current), [], superseded=stale)
        self.assertIn("1 earlier run(s) are excluded", page)
        self.assertIn(V.SIM_VERSION, page)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _age_run(self, run_id, version):
        """Rewrite one digest as though an older sim had produced it."""
        path = os.path.join(self.tmp.name, "runs", run_id, "summary.json")
        with open(path) as f:
            summary = json.load(f)
        summary["sim_version"] = version
        with open(path, "w") as f:
            json.dump(summary, f)
