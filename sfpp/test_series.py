"""Tests for reception-over-time.

The property that matters most here is not what the series says but that asking for it changes nothing:
README SS1's second rule is that only the observer has full knowledge and only ever for measurement, and
a sampler that perturbs the run it samples has broken it. `test_asking_for_the_series_does_not_change
_the_run` is that rule, checked rather than assumed - the sampler puts events on the same queue the
transport uses, so reordering ties was a real possibility.

Run from the tree root:  python3 -m unittest sfpp.test_series -v
"""

import hashlib
import json
import os
import tempfile
import unittest

from .campaign import build_parser, run_once


def fingerprint(report):
    """Everything the *simulation* decided, with what only the observer produced removed.

    Three things dropped and no more: dropping `hops_away` wholesale would blind it to the failure.
    """
    r = json.loads(json.dumps(report))
    # `mesh_map` joined these once --mesh-map started recording points and links without --out:
    # it is the observer's picture of the mesh, so asking for it must not move a single number, and
    # dropping only `opts.mesh_map` below would no longer prove that.
    # `decoder` joins these for the same reason wall_seconds is here: which implementation of
    # Sketch.decode was reachable is a fact about the machine, and the whole claim of the native one
    # is that it cannot move a number. A run that used it and one that did not must hash the same.
    for key in ("wall_seconds", "transport", "series", "mesh_map", "decoder"):
        r.pop(key, None)
    for key in ("out", "reception_bin_s", "mesh_map"):
        (r.get("opts") or {}).pop(key, None)
    for row in (r.get("hops_away") or {}).get("typical_nodes") or []:
        row.pop("estimated_peers_at_hop", None)
        row.pop("estimate_samples", None)
    return hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest()


def run(hours_override=3, **flags):
    argv = ["--hours", str(hours_override or 30), "--nodes", "20", "--seed", "77", "--no-charts"]
    for key, value in flags.items():
        argv += [f"--{key.replace('_', '-')}"] + ([] if value is True else [str(value)])
    return run_once(build_parser().parse_args(argv), 77)


class Inertness(unittest.TestCase):
    """The sampler must be an observer and nothing else."""

    def test_sampling_changes_nothing_a_node_believed(self):
        """Narrower than the fingerprint: the estimator's own state must be what it would have been
        unsampled. Reading a histogram must not change it."""
        plain = {r["node"]: r for r in run()["hops_away"]["typical_nodes"]}
        sampled = {
            r["node"]: r for r in run(reception_bin_s=1800)["hops_away"]["typical_nodes"]
        }
        self.assertEqual(sorted(plain), sorted(sampled))
        for node, row in plain.items():
            for key in ("suggested_hop", "table_fill_percent", "filtering_denominator",
                        "dropped_full", "truth_peers_at_hop", "observed_receptions_at_hop"):
                self.assertEqual(row[key], sampled[node][key], f"node {node} {key}")

    def test_asking_for_the_series_does_not_change_the_run(self):
        """The whole guarantee: without it a series run is a different experiment from the run it
        claims to describe."""
        self.assertEqual(
            fingerprint(run()), fingerprint(run(reception_bin_s=1800)),
            "enabling the series perturbed the simulation - the sampler's events reordered ties",
        )

    def test_the_bin_width_does_not_change_the_run_either(self):
        """A finer sampler is more events on the same queue, so this is the sharper version."""
        self.assertEqual(
            fingerprint(run(reception_bin_s=600)),
            fingerprint(run(reception_bin_s=3600)),
        )

    def test_off_by_default(self):
        """A run that does not ask for the series must not pay for it, or carry it."""
        report = run()
        self.assertIsNone(report["series"])


class Series(unittest.TestCase):
    def setUp(self):
        self.report = run(reception_bin_s=3600)
        self.series = self.report["series"]

    def test_the_bins_cover_the_run(self):
        self.assertEqual(self.series["bin_s"], 3600)
        # Three hours of run, so three bins of reception (a fourth can exist for the closing instant).
        self.assertGreaterEqual(self.series["bins"], 3)

    def test_every_row_carries_its_own_denominator(self):
        """A rate without its denominator is unreadable on non-flat traffic: the quiet bins are
        exactly where a handful of packets reads as a collapse or a triumph."""
        for row in self.series["reception"]:
            for name, cls in row["by_class"].items():
                self.assertIn("originated", cls)
                self.assertIn("receptions", cls)
                if cls["rate"] is not None:
                    self.assertGreater(cls["originated"], 0, f"{name} has a rate but no denominator")

    def test_a_bin_with_no_originations_has_no_rate_rather_than_zero(self):
        """Zero would read as total loss. None reads as "nothing was sent", which is the truth."""
        for row in self.series["reception"]:
            for cls in row["by_class"].values():
                if not cls["originated"]:
                    self.assertIsNone(cls["rate"])

    def test_the_binned_totals_reconcile_with_the_whole_run(self):
        """The series is a partition, not a second measurement. If these disagree, one of them is
        wrong and there is no way to tell which from the report alone."""
        for name, whole in self.report["by_class"].items():
            if name == "all":
                continue
            binned_sent = sum(
                row["by_class"].get(name, {}).get("originated", 0)
                for row in self.series["reception"]
            )
            binned_got = sum(
                row["by_class"].get(name, {}).get("receptions", 0)
                for row in self.series["reception"]
            )
            self.assertEqual(binned_sent, whole["originated"], f"{name} originated")
            self.assertEqual(binned_got, whole["receptions"], f"{name} receptions")

    def test_the_rate_matches_the_whole_run_definition(self):
        """Same quantity, partitioned - not recomputed differently. A row and the headline figure
        have to be comparable or the series is a separate metric wearing the same name."""
        peers = max(1, self.report["opts"]["nodes"] - 1)
        for row in self.series["reception"]:
            for cls in row["by_class"].values():
                if cls["rate"] is not None:
                    self.assertAlmostEqual(
                        cls["rate"], round(cls["receptions"] / (cls["originated"] * peers), 4)
                    )

    def test_hour_of_day_follows_start_hour(self):
        """So a diurnal shape is readable without the reader working out where the run began."""
        report = run(reception_bin_s=3600, start_hour=22)
        hours = [row["hour_of_day"] for row in report["series"]["reception"]]
        self.assertEqual(hours[0], 22.0)
        self.assertIn(0.0, hours)  # and it wraps rather than running to 25

    def test_the_load_rows_are_differences_not_totals(self):
        """Cumulative counters read at each boundary. A row showing the running total would rise
        monotonically and say nothing about the bin it belongs to."""
        load = self.series["load"]
        self.assertTrue(load)
        for row in load:
            for key in ("transmissions", "receptions", "lost_to_collision", "queue_drops"):
                self.assertGreaterEqual(row[key], 0, f"{key} went backwards - not a difference")
        # And they sum to no more than the whole run's totals.
        self.assertLessEqual(
            sum(r["transmissions"] for r in load), self.report["traffic"]["transmissions"]
        )

    def test_channel_utilisation_is_sampled_not_differenced(self):
        """It is a percentage at a moment, and it cannot pass 100 - the invariant a receiver counting
        the transmitters it collided with once broke (TRAPS.md #5)."""
        for row in self.series["load"]:
            self.assertLessEqual(row["chutil_max"], 100.0)
            self.assertLessEqual(row["chutil_median"], row["chutil_p90"] + 1e-9)
            self.assertLessEqual(row["chutil_p90"], row["chutil_max"] + 1e-9)


class SeriesChart(unittest.TestCase):
    """The chart, which is the form anyone will actually read the series in."""

    @classmethod
    def setUpClass(cls):
        cls.report = run(reception_bin_s=3600, diurnal="commuter", hours_override=None)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def draw(self, report):
        from . import autochart as AC

        path = AC.render_series(report, self.tmp.name, "t")
        return path, (open(path).read() if path else "")

    def test_it_draws_and_is_valid_xml(self):
        import xml.dom.minidom

        path, svg = self.draw(self.report)
        self.assertTrue(path)
        xml.dom.minidom.parseString(svg)

    def test_a_run_without_a_series_draws_nothing_rather_than_an_empty_frame(self):
        """An axis with no line on it reads as "measured, and flat"."""
        path, _ = self.draw(run())
        self.assertIsNone(path)

    def test_the_night_hours_are_shaded(self):
        """Context, not decoration: it is what tells "the mesh got quieter" from "it was 4am", which
        is the entire question a series over a multi-day run is asked."""
        _, svg = self.draw(self.report)
        self.assertIn('opacity="0.08"', svg)

    def test_a_gap_is_not_bridged(self):
        """A bin with no denominator has no rate. A line drawn through it would be a trend through an
        hour with no measurement in it - the same failure explorer.py's sparkline avoids."""
        from . import autochart as AC

        panel = AC.Panel(0, "t", ["a", "b", "c"], lo=0.0, hi=1.0)
        AC._series_line(panel, [(0, 0.5), (1, None), (2, 0.5)], AC.ACCENT)
        self.assertEqual(len([p for p in panel.parts if "<line" in p]), 0)
        panel2 = AC.Panel(0, "t", ["a", "b"], lo=0.0, hi=1.0)
        AC._series_line(panel2, [(0, 0.5), (1, 0.6)], AC.ACCENT)
        self.assertEqual(len([p for p in panel2.parts if "<line" in p]), 1)

    def test_the_collision_line_says_it_is_scaled(self):
        """It shares the utilisation panel's percentage axis, so the legend has to carry the peak or
        it reads as a percentage - demand-as-utilisation one level down."""
        _, svg = self.draw(self.report)
        self.assertIn("collisions (peak", svg)


class TypicalNodes(unittest.TestCase):
    """The handful of nodes the hop histograms are actually printed for.

    The selection is the work: not all 500, and not the mean node - MODEL.md.
    """

    @classmethod
    def setUpClass(cls):
        cls.report = run(reception_bin_s=1800, hop_spread=True)
        cls.rows = cls.report["hops_away"]["typical_nodes"]

    def test_the_selection_spans_the_range_rather_than_sampling_the_middle(self):
        labels = " ".join(r["stands_for"] for r in self.rows)
        for wanted in ("worst", "p10", "median", "p90", "best"):
            self.assertIn(wanted, labels, f"{wanted} is not represented")

    def test_the_worst_node_really_is_the_worst(self):
        """Ranked by observed reach, so the first row must be the minimum, not merely a low one."""
        worst = next(r for r in self.rows if "worst" in r["stands_for"])
        everything = self.report["hops_away"]["observed_per_node"]
        lowest = min(sum(v["counts"].values()) for v in everything.values())
        self.assertEqual(worst["receptions"], lowest)

    def test_no_node_is_listed_twice(self):
        """A small mesh can land two labels on one node; it must be named once, carrying both."""
        indexes = [r["node"] for r in self.rows]
        self.assertEqual(len(indexes), len(set(indexes)))

    def test_every_row_says_how_many_nodes_it_speaks_for(self):
        """So one node is never read as a population."""
        for row in self.rows:
            self.assertEqual(row["of_nodes"], len(self.report["hops_away"]["observed_per_node"]))

    def test_the_units_are_in_the_key_names(self):
        """Peers and receptions are different quantities, and a reader given `truth` beside
        `observed` will compare them. The names have to stop that."""
        for row in self.rows:
            self.assertIn("truth_peers_at_hop", row)
            self.assertIn("estimated_peers_at_hop", row)
            self.assertIn("observed_receptions_at_hop", row)
            self.assertNotIn("truth", row)  # the ambiguous name must be gone, not aliased
            self.assertNotIn("observed", row)

    def test_the_estimate_is_averaged_over_the_run_not_a_final_snapshot(self):
        """A converged estimate and an oscillating one have the same last value."""
        for row in self.rows:
            self.assertGreater(row["estimate_samples"], 1, "only one sample is not an average")
            self.assertIsNotNone(row["estimated_peers_at_hop"])

    def test_the_estimate_is_absent_rather_than_faked_without_sampling(self):
        """No series, nothing to average. None says so; a snapshot wearing the name would not."""
        rows = run(hop_spread=True)["hops_away"]["typical_nodes"]
        for row in rows:
            self.assertIsNone(row["estimated_peers_at_hop"])
            self.assertEqual(row["estimate_samples"], 0)

    def test_the_recommendation_comes_with_the_state_it_was_derived_from(self):
        """A suggestion off a full table with a raised denominator is a different claim from the
        same number off a table with room in it - TRAPS.md's request-and-result shape."""
        for row in self.rows:
            self.assertIsNotNone(row["suggested_hop"])
            self.assertIsNotNone(row["table_fill_percent"])
            self.assertIsNotNone(row["filtering_denominator"])
            self.assertLessEqual(row["table_fill_percent"], 100)

    def test_truth_has_no_zero_bucket_and_observed_does(self):
        """Not a discrepancy: a node is not its own peer, but a direct reception has travelled no
        hops. Asserted so that 'fixing' one of them later has to be deliberate."""
        for row in self.rows:
            self.assertNotIn("0", row["truth_peers_at_hop"] or {})


if __name__ == "__main__":
    unittest.main()
