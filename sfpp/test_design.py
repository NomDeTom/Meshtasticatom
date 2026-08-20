"""Tests for the three-axis cross - that it is wired the way its docstring claims.

None of these run a simulation. They check the grid itself: that every cell's flags are flags the
campaign accepts, that the arm the digest reads as a control is the arm the design writes, and that
the two arms which restate a firmware constant still restate it. That last one is the reason the
file exists. `hop-scaling-40` and `congestion-40` are in the grid to reproduce `none` cell for cell,
which they only do while the firmware's literals are 40; if either constant moves and the arm does
not, the cross silently gains a second baseline that disagrees with the first, and every difference
read against it is wrong by that amount. A grid that cannot reproduce its own baseline is worth
catching here rather than a month of runs later.

Run from the tree root:  python3 -m unittest sfpp.test_design -v
"""

import unittest

from . import collate as C
from . import design as D
from . import mesh as M
from . import traffic as T
from .campaign import build_parser


class TestGrid(unittest.TestCase):
    def test_every_cell_is_one_mesh_and_one_rival(self):
        cells = D.cells()
        self.assertEqual(len(cells), len(D.MESHES) * len(D.RIVALS))
        for name, (mesh, mesh_flags, rival, rival_flags) in cells.items():
            self.assertEqual(name, f"{mesh}-{rival}")
            self.assertIn((mesh, mesh_flags), D.MESHES)
            self.assertIn((rival, rival_flags), D.RIVALS)

    def test_cell_names_are_unique(self):
        # `batumi` + `x4-none` and `batumi-x4` + `none` would collide into one filename, and the
        # second job written would overwrite the first without either failing.
        names = [f"{m}-{r}" for m, _ in D.MESHES for r, _ in D.RIVALS]
        self.assertEqual(len(names), len(set(names)))

    def test_every_combination_parses(self):
        parser = build_parser()
        for _, mesh_flags in D.MESHES:
            for _, rival_flags in D.RIVALS:
                for _, archive_flags in D.archives():
                    parser.parse_args(D.TRAFFIC + mesh_flags + rival_flags + archive_flags)

    def test_the_archive_axis_starts_switched_off(self):
        # The `off` arm has to be first and has to be the only one without the archive: it is the
        # cell every other cell in the mesh is a difference against.
        label, flags = D.archives()[0]
        self.assertEqual(label, "off")
        self.assertEqual(flags, ["--protocol", "none"])
        self.assertEqual(len(D.archives()), 1 + len(D.PLACES) * len(D.SERVERS))

    def test_the_digest_reads_the_off_arm_as_the_control(self):
        # `against_control` finds the control by label. If the design renames the arm and the
        # digest is not told, every cell quietly loses its `vs_control` row instead of failing.
        self.assertIn(D.archives()[0][0], C.CONTROL)

    def test_rivals_change_one_thing_each(self):
        labels = [label for label, _ in D.RIVALS]
        self.assertEqual(labels[0], "none")
        self.assertEqual(D.RIVALS[0][1], [])
        self.assertEqual(len(labels), len(set(labels)))

    def test_the_mesh_axis_is_batumi_throughout(self):
        # Round one holds the geometry and varies the condition. A synthetic mesh in here would be
        # varying both at once, and the round would not answer what it was run to answer.
        for _, flags in D.MESHES:
            self.assertEqual(flags[:2], ["--scenario", "batumi"])


class TestReportFields(unittest.TestCase):
    """The coordinates a cell writes onto each report, checked against what the campaign writes."""

    def test_the_mesh_name_does_not_overwrite_the_mesh_statistics(self):
        # The campaign writes `mesh` as a dict of the run's node count, mean degree and
        # connectedness, and both the digest and the chart read it as one. An earlier draft of the
        # cross stored the mesh's *name* under the same key, which replaced that dict with a string
        # and would have taken the node count out of every cell in the round.
        import inspect

        source = inspect.getsource(D.run_cell)
        self.assertIn('report["mesh_label"] = mesh', source)
        self.assertNotIn('report["mesh"] =', source)


class TestReproducesBaseline(unittest.TestCase):
    """The two arms that restate a firmware constant, and the constants they restate."""

    def flags_for(self, label):
        return dict(D.RIVALS)[label]

    def test_both_named_arms_are_in_the_grid(self):
        for label in D.REPRODUCES_BASELINE:
            self.assertIn(label, dict(D.RIVALS))

    def test_hop_scaling_40_is_the_firmware_default(self):
        self.assertEqual(self.flags_for("hop-scaling-40"), ["--hop-target-nodes", "40"])
        self.assertEqual(M.HopScaling().target_affected_nodes, 40)
        self.assertEqual(M.HopScaling(target_nodes=40).target_affected_nodes, 40)
        # The ceiling follows the target, so restating the target restates both halves.
        self.assertEqual(M.HopScaling().max_target_nodes, M.HopScaling(target_nodes=40).max_target_nodes)

    def test_congestion_40_is_the_firmware_default(self):
        self.assertEqual(self.flags_for("congestion-40"), ["--congestion-pivot", "40"])
        self.assertEqual(T.CONGESTION_PIVOT, 40)

    def test_the_scalings_are_not_the_same_setting(self):
        # These get conflated. Hop scaling moves how far a broadcast is told to travel; congestion
        # scaling moves how often the periodic ones are sent. Nothing here would notice if one flag
        # were wired to the other's target, so this asserts they land in different places.
        hop_flag = self.flags_for("hop-scaling-80")[0]
        congestion_flag = self.flags_for("congestion-80")[0]
        self.assertNotEqual(hop_flag, congestion_flag)
        parser = build_parser()
        hop = parser.parse_args(D.TRAFFIC + self.flags_for("hop-scaling-80"))
        congestion = parser.parse_args(D.TRAFFIC + self.flags_for("congestion-80"))
        # Moving one arm must leave the other at its firmware default, or the cross is measuring
        # two changes and attributing them to one.
        self.assertEqual(hop.hop_target_nodes, 80)
        self.assertEqual(hop.congestion_pivot, T.CONGESTION_PIVOT)
        self.assertEqual(congestion.congestion_pivot, 80)
        self.assertEqual(congestion.hop_target_nodes, M.HopScaling.TARGET_AFFECTED_NODES)

    def test_the_scalings_move_what_they_claim_to_move(self):
        # Hop scaling reaches further as its target rises; congestion scaling stretches intervals
        # harder as its pivot falls. Both are monotone, and an arm wired backwards would not be.
        targets = [M.HopScaling(target_nodes=n).target_affected_nodes for n in (40, 60, 80)]
        self.assertEqual(targets, sorted(targets))
        # LONG_FAST: SF11 at 250 kHz, the preset every mesh on this axis but one runs.
        at = [T.congestion_coefficient(60, 11, 250_000, pivot=p) for p in (40, 60, 80)]
        self.assertEqual(at, sorted(at, reverse=True))
        self.assertEqual(at[-1], 1.0)


if __name__ == "__main__":
    unittest.main()


class ArchiveSharding(unittest.TestCase):
    """Splitting a cell's archive configurations, which this module's header used to warn against.

    The warning was right until placement got its own RNG stream: with the archive arms drawing from
    the run's shared stream, a randomised placement shifted the traffic generator's later draws, so the
    control and the arms carried different offered load. `test_matrix.PlacementIsolation` pins the fix;
    without it none of this is sound.
    """

    def test_the_shards_of_a_cell_cover_every_configuration_exactly_once(self):
        for total in (1, 2, 3, 4, 10):
            rebuilt = [a for i in range(total) for a in D.shard_of(D.archives(), i, total)]
            self.assertEqual(rebuilt, D.archives(), f"{total} shards do not reassemble the cell")

    def test_the_off_control_lands_in_the_first_shard(self):
        self.assertEqual(D.shard_of(D.archives(), 0, 3)[0][0], "off")

    def test_only_the_mirrored_mesh_is_split(self):
        """It is the only one past the platform's hard limit; splitting the others buys nothing and
        costs a checkout each."""
        self.assertGreater(D.shards_for("batumi-x4"), 1)
        for mesh, _ in D.MESHES:
            if mesh != "batumi-x4":
                self.assertEqual(D.shards_for(mesh), 1, mesh)

    def test_every_sharded_mesh_is_a_mesh_the_design_declares(self):
        """A shard count for a mesh that no longer exists is a silent no-op."""
        self.assertEqual(
            sorted(set(D.SHARDS_BY_MESH) - {m for m, _ in D.MESHES}), []
        )

    def test_no_shard_is_empty(self):
        for total in (2, 3, 4):
            for index in range(total):
                self.assertTrue(D.shard_of(D.archives(), index, total), f"{index}/{total}")
