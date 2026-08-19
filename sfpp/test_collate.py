"""Tests for the scheduled run's digest and the rolling page built from it.

The reports here are hand-built rather than produced by a campaign run: a collator checked against
the simulator's own output only proves the two agree, and the cases that matter are the ones a real
run produces once a month - a silent loss, a block whose job never wrote a file, an arm that moved
nothing. Each is built directly.

The inert check has its own regression: the first version compared only the metrics the digest
displays and called `E-signed` inert, when that arm moves `advert_bytes` by 43% and nothing else.
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


def report(block="B-arm", arm="arm", value=1, seed=7, held=0.8, text=0.7, **overrides):
    """One cell report, shaped like the campaign's but only as deep as these tests read."""
    r = {
        "block": block,
        "arm": arm,
        "value": value,
        "seed": seed,
        "grid": [],
        "transport": "abc1234",
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
        # E-signed: held, text, airtime and every displayed metric identical; only the byte counters
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

    The cross shards a heavy cell one job per seed - the mirrored Batumi mesh is four times the
    nodes and a whole cell in one job runs past the runner's ceiling - and the artifacts merge into
    one directory, so the shards must be named apart on disk while carrying the same `block`. Read
    per file instead of per block, the digest would enter the same block three times and average
    nothing over seeds, which is the failure this guards.
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
        # Self-contained means it loads nothing over the network, not that it links nowhere: the
        # attribution block cites the repository and the licence, and a citation is a link the
        # reader may follow rather than a resource the page pulls in. What must not appear is any
        # construct that fetches - the page is served from a git branch and from a static site and
        # has to render identically opened from disk.
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

    Fatal means the run's other numbers cannot be trusted: a counter that falsifies the design, or a
    figure a radio cannot physically produce. Everything else warns and is still readable.
    """

    def _flags(self, **overrides):
        fatal, warn = C.check_cell(report(**overrides), "arm=1")
        return fatal, warn

    def test_a_node_cannot_exceed_100_percent_channel_utilisation(self):
        # A receiver charging itself for every transmitter it collided with ran this to 184%.
        fatal, _ = self._flags(
            traffic__node_channel_util_percent={"p90": 90.0, "max": 184.0}
        )
        self.assertTrue(any("physically impossible" in f for f in fatal))

    def test_demand_above_one_is_not_a_failure(self):
        # Aggregate demand legitimately exceeds 1.0 and says nothing about local headroom. Gating on
        # it would fail every spatially extended mesh.
        fatal, warn = self._flags(traffic__channel_utilisation=9.55)
        self.assertEqual(fatal, [])
        self.assertEqual(warn, [])

    def test_a_scenario_that_recorded_no_ground_is_fatal(self):
        # The Scenario with no nodes was falsy, so the run came out flat under an alpine label.
        fatal, _ = self._flags(opts={"scenario": "alpine"}, ground=None)
        self.assertTrue(any("recorded no ground" in f for f in fatal))

    def test_a_scenario_that_applied_no_terrain_warns(self):
        fatal, warn = self._flags(
            opts={"scenario": "alpine"},
            ground={"terrain_applied": False, "fixed_geometry": False},
        )
        self.assertEqual(fatal, [])
        self.assertTrue(any("applied no terrain" in w for w in warn))

    def test_the_at_rest_audit_disagreeing_is_fatal(self):
        fatal, _ = self._flags(sfpp__audit_checksum_agrees_sets_differ=2)
        self.assertTrue(any("at-rest audit" in f for f in fatal))

    def test_a_capped_placement_is_named(self):
        # `routers` and `beside-router` cap at the router count, so a sweep over 2-6 servers can
        # produce three real rows and two repeats of the fourth.
        _, warn = self._flags(sfpp__servers_requested=6, sfpp__servers_placed=4)
        self.assertTrue(any("6 archives requested, 4 placed" in w for w in warn))

    def test_pairs_outside_the_fit_envelope_are_named(self):
        _, warn = self._flags(
            ground={
                "link_calibration_loaded": True,
                "pairs_beyond_calibration": 812,
                "calibration_envelope_m": 23200,
                "terrain_applied": True,
            }
        )
        self.assertTrue(any("beyond the fit" in w for w in warn))

    def test_a_clean_cell_raises_nothing(self):
        fatal, warn = self._flags()
        self.assertEqual((fatal, warn), ([], []))


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

    One admin probe an hour over a two-hour run is two sessions. A single failed session then reads
    as a 50% swing, which is larger than any real effect in the archive numbers and would top a
    leaderboard built from them. The figure is still reported; it just cannot win.
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
        # D-resolve: enum advertises with a fifth of sketch's bytes and delivers the same.
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
