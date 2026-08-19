"""Tests for the mesh map.

A map is the one output nobody checks by reading it: a wrong number in a report looks wrong, while a
wrong picture just looks like a picture. So the things asserted here are the ones that would produce a
plausible-looking map of the wrong mesh - a role silently dropped, co-located nodes drawn as fewer
nodes than there are, a stretched aspect ratio, an archive indistinguishable from what it sits on.

Run from the tree root:  python3 -m unittest sfpp.test_meshmap -v
"""

import os
import tempfile
import unittest
import xml.dom.minidom

from . import meshmap as MM


class FakeNode:
    def __init__(self, x, y, role="CLIENT"):
        self.x, self.y, self.role = x, y, role


class FakeConf:
    MODEM_PRESET = "LONG_FAST"
    current_preset = {"sensitivity": -131.5}


class FakeOpts:
    scenario = None
    mirror = 1


class FakeMesh:
    def __init__(self, nodes, neighbours, rssi):
        self.nodes, self.neighbours, self.rssi = nodes, neighbours, rssi


class FakeCampaign:
    def __init__(self, nodes, neighbours=None, rssi=None, servers=(), designated=()):
        n = len(nodes)
        neighbours = neighbours if neighbours is not None else [set() for _ in range(n)]
        rssi = rssi if rssi is not None else [[-100.0] * n for _ in range(n)]
        self.mesh = FakeMesh(nodes, neighbours, rssi)
        self.conf = FakeConf()
        self.opts = FakeOpts()
        self.servers = {i: None for i in servers}
        self.designated = list(designated)


class MapOutput(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = os.path.join(self.tmp.name, "mesh.svg")

    def draw(self, campaign, **kw):
        stats = MM.mesh_svg(campaign, self.path, **kw)
        with open(self.path) as f:
            return stats, f.read()

    def test_the_output_is_valid_xml(self):
        """Hand-written SVG, so nothing else checks the syntax."""
        _, svg = self.draw(FakeCampaign([FakeNode(0, 0), FakeNode(1000, 1000)]))
        xml.dom.minidom.parseString(svg)

    def test_every_node_is_drawn_even_when_co_located(self):
        """Batumi is 92 nodes on 55 coordinates, the largest stack holding 14. Drawn literally that
        is a third of the mesh invisible with nothing saying so."""
        nodes = [FakeNode(500, 500) for _ in range(14)] + [FakeNode(0, 0)]
        stats, svg = self.draw(FakeCampaign(nodes))
        self.assertEqual(stats["nodes"], 15)
        self.assertEqual(stats["stacked_nodes"], 14)
        # And the map says it moved them, because their drawn positions are not their real ones.
        self.assertIn("share a position", svg)

    def test_co_located_nodes_get_distinct_positions(self):
        stacked = [FakeNode(500, 500) for _ in range(6)]
        offsets = {MM._fan(6, k) for k in range(6)}
        self.assertEqual(len(offsets), 6)
        # A lone node is never displaced - only a stack is.
        self.assertEqual(MM._fan(1, 0), (0.0, 0.0))
        self.draw(FakeCampaign(stacked))

    def test_a_role_the_mesh_has_reaches_the_legend_with_its_count(self):
        nodes = [FakeNode(0, 0, "ROUTER"), FakeNode(900, 0, "CLIENT_MUTE"), FakeNode(0, 900, "CLIENT_MUTE")]
        stats, svg = self.draw(FakeCampaign(nodes))
        self.assertEqual(stats["roles"], {"CLIENT_MUTE": 2, "ROUTER": 1})
        self.assertIn("ROUTER 1", svg)
        self.assertIn("CLIENT_MUTE 2", svg)

    def test_a_role_the_mesh_lacks_is_not_in_the_legend(self):
        """A uniform mesh should not carry five legend entries for roles it has none of."""
        _, svg = self.draw(FakeCampaign([FakeNode(0, 0), FakeNode(900, 900)]))
        self.assertNotIn("ROUTER_LATE", svg)
        self.assertNotIn("CLIENT_BASE", svg)

    def test_an_unmodelled_role_still_draws(self):
        """Better a mark with a caveat than a KeyError halfway through a scheduled round."""
        stats, _ = self.draw(FakeCampaign([FakeNode(0, 0, "TRACKER"), FakeNode(900, 900)]))
        self.assertEqual(stats["roles"]["TRACKER"], 1)

    def test_an_archive_keeps_the_role_mark_of_what_it_sits_on(self):
        """An archive on a router and an archive on a muted client are different deployments, and a
        map drawing both as the same red dot cannot say which one it is."""
        nodes = [FakeNode(0, 0, "ROUTER"), FakeNode(900, 900, "CLIENT_MUTE")]
        _, both = self.draw(FakeCampaign(nodes, servers=(0,)))
        # The router-shaped archive is a rect in the archive colour; a circle-shaped one would not be.
        self.assertIn(f'fill="{MM.SERVER}"', both)
        self.assertIn("<rect", both)

    def test_the_designated_control_is_marked_apart_from_an_archive(self):
        """--protocol none sites the nodes and runs no archive. The control has to look like one."""
        nodes = [FakeNode(0, 0), FakeNode(900, 900)]
        _, svg = self.draw(FakeCampaign(nodes, designated=(0,)))
        self.assertIn("stroke-dasharray", svg)

    def test_fragile_links_are_drawn_apart_from_sound_ones(self):
        nodes = [FakeNode(0, 0), FakeNode(900, 0), FakeNode(0, 900)]
        rssi = [[-100.0] * 3 for _ in range(3)]
        rssi[0][1] = rssi[1][0] = -129.0  # 2.5 dB of margin: fragile
        rssi[0][2] = rssi[2][0] = -110.0  # 21.5 dB: comfortable
        neighbours = [{1, 2}, {0}, {0}]
        stats, svg = self.draw(FakeCampaign(nodes, neighbours, rssi))
        self.assertEqual(stats["links_drawn"], 2)
        self.assertEqual(stats["fragile_drawn"], 1)
        self.assertIn(MM.FRAGILE, svg)

    def test_a_link_is_drawn_once_not_once_per_direction(self):
        nodes = [FakeNode(0, 0), FakeNode(900, 900)]
        stats, _ = self.draw(FakeCampaign(nodes, [{1}, {0}]))
        self.assertEqual(stats["links_drawn"], 1)

    def test_the_link_cap_is_reported_rather_than_silent(self):
        """A truncated picture that does not say so reads as a sparser mesh than it is."""
        nodes = [FakeNode(i * 100, 0) for i in range(12)]
        neighbours = [set(range(12)) - {i} for i in range(12)]
        stats, svg = self.draw(FakeCampaign(nodes, neighbours), max_links=5)
        self.assertEqual(stats["links_drawn"], 5)
        self.assertGreater(stats["links_skipped"], 0)
        self.assertIn("not drawn", svg)

    def test_the_geometry_is_not_stretched_to_fill_the_frame(self):
        """One scale for both axes. A corridor mesh scaled per-axis is a picture of a different
        shape, and shape is what this map is for."""
        wide = FakeCampaign([FakeNode(0, 0), FakeNode(10000, 0), FakeNode(10000, 500)])
        stats, _ = self.draw(wide)
        self.assertEqual(stats["extent_km"], [10.0, 0.5])

    def test_a_degenerate_extent_does_not_divide_by_zero(self):
        """Every node on one point, which a one-node mesh or a bad scenario can produce."""
        stats, svg = self.draw(FakeCampaign([FakeNode(700, 700), FakeNode(700, 700)]))
        xml.dom.minidom.parseString(svg)
        self.assertEqual(stats["nodes"], 2)


if __name__ == "__main__":
    unittest.main()
