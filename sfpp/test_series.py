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
    """Everything the simulation decided, with the series and the machine's own timings removed."""
    r = json.loads(json.dumps(report))
    for key in ("wall_seconds", "transport", "series"):
        r.pop(key, None)
    for key in ("out", "reception_bin_s", "mesh_map"):
        (r.get("opts") or {}).pop(key, None)
    return hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest()


def run(**flags):
    argv = ["--hours", "3", "--nodes", "20", "--seed", "77", "--no-charts"]
    for key, value in flags.items():
        argv += [f"--{key.replace('_', '-')}"] + ([] if value is True else [str(value)])
    return run_once(build_parser().parse_args(argv), 77)


class Inertness(unittest.TestCase):
    """The sampler must be an observer and nothing else."""

    def test_asking_for_the_series_does_not_change_the_run(self):
        """The whole guarantee. If this fails, every series run is a different experiment from the
        run it claims to describe, and the arms of a sweep would differ in the sampling as well as
        the arm."""
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


if __name__ == "__main__":
    unittest.main()
