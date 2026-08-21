"""The fit answers only inside the distances it was trained on, whichever entry point asks.

sfpp derives LINK_CALIBRATION_MAX_M from the preset's own observations and falls back to the raw
budget beyond it. lib/presets.py never set the field and lib/link_model.py had no envelope test at
all, so `loraMesh.py --preset batumi` applied the fit at any distance - reproducing the defect
TRAPS 4 records as mitigated, on the same coefficients, from the other door.
"""

import unittest

from lib.config import Config
from lib.link_model import calculate_link_budget
from lib.presets import (
    apply_preset_radio_calibration,
    load_preset_node_configs,
    preset_calibration_envelope_m,
    preset_clutter_grid,
    preset_origin,
    load_preset_terrain_grid,
)
from lib.point import Point


class Node:
    """A transmitter or receiver reduced to what the link budget reads."""

    def __init__(self, x, y, z=1.5, gain=0.0, height=1.5):
        self.position = Point(x, y, z)
        self.antenna_gain = gain
        self.antenna_height = height


def batumi_config(with_terrain=True):
    conf = Config()
    conf.MODEM_PRESET = "LONG_FAST"
    configs = load_preset_node_configs("batumi", conf.PERIOD)
    conf.NR_NODES = len(configs)
    apply_preset_radio_calibration(conf, "batumi")
    conf.GEO_ORIGIN_LAT, conf.GEO_ORIGIN_LON = preset_origin("batumi")
    if with_terrain:
        conf.TERRAIN_ENABLED = True
        conf.TERRAIN_GRID = load_preset_terrain_grid("batumi")
        conf.CLUTTER_ENABLED = True
        conf.CLUTTER_GRID_FILE = str(preset_clutter_grid("batumi"))
    return conf, configs


class TheEnvelopeIsDerivedFromTheObservations(unittest.TestCase):
    def test_it_is_the_longest_observed_link(self):
        envelope = preset_calibration_envelope_m("batumi")
        self.assertIsNotNone(envelope)
        # 296 observations, longest 23.22 km.
        self.assertAlmostEqual(envelope / 1000.0, 23.22, places=2)

    def test_applying_the_preset_sets_it(self):
        conf, _ = batumi_config(with_terrain=False)
        self.assertAlmostEqual(
            conf.LINK_CALIBRATION_MAX_M, preset_calibration_envelope_m("batumi")
        )

    def test_a_plain_config_declares_no_envelope(self):
        """None means "no envelope known", which is not the same as "valid everywhere"."""
        self.assertIsNone(Config().LINK_CALIBRATION_MAX_M)


class BeyondTheEnvelopeTheRawBudgetAnswers(unittest.TestCase):
    def test_a_pair_past_the_envelope_gets_the_raw_budget(self):
        conf, _ = batumi_config(with_terrain=False)
        envelope = conf.LINK_CALIBRATION_MAX_M

        inside = calculate_link_budget(conf, Node(0.0, 0.0), Node(envelope * 0.9, 0.0))
        outside = calculate_link_budget(conf, Node(0.0, 0.0), Node(envelope * 1.1, 0.0))

        self.assertTrue(inside.calibration_applied)
        self.assertFalse(outside.calibration_applied)
        self.assertEqual(outside.rssi_dbm, outside.raw_rssi_dbm)
        # And the fit was holding the link up: the raw budget at that range is far weaker.
        self.assertLess(outside.rssi_dbm, inside.rssi_dbm - 20.0)

    def test_the_fit_no_longer_answers_at_sixty_kilometres(self):
        """TRAPS 4's own example: links to 60.6 km on a snapshot whose longest observation is 23.2."""
        conf, _ = batumi_config(with_terrain=False)
        far = calculate_link_budget(
            conf, Node(0.0, 0.0, 900.0), Node(60000.0, 0.0, 900.0)
        )
        self.assertFalse(far.calibration_applied)
        self.assertEqual(far.rssi_dbm, far.raw_rssi_dbm)


class BothEntryPointsAgree(unittest.TestCase):
    """The check the fix exists for: one preset, one link model, whichever code asks."""

    def test_the_vendored_budget_matches_sfpps_for_the_packaged_preset(self):
        import random

        from sfpp import mesh as M
        from sfpp import terrain as T

        conf = M.make_config()
        scenario = T.load("batumi")
        grid = T.apply(conf, scenario, terrain=True)
        mesh = M.build(conf, len(scenario.points), 8000.0, random.Random(5),
                       scenario=scenario, terrain=grid)

        self.assertIsNotNone(getattr(conf, "LINK_CALIBRATION_MAX_M", None))
        envelope = conf.LINK_CALIBRATION_MAX_M

        # sfpp's own switch and the vendored one are now the same rule, so a pair the transport
        # treats as beyond the fit is one the vendored budget also refuses to calibrate.
        checked = 0
        for i in range(len(mesh.nodes)):
            for j in range(i + 1, len(mesh.nodes)):
                a, b = mesh.nodes[i], mesh.nodes[j]
                distance = ((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.altitude - b.altitude) ** 2) ** 0.5
                budget = calculate_link_budget(
                    conf,
                    Node(a.x, a.y, a.altitude, height=a.antenna_height_m or conf.HM),
                    Node(b.x, b.y, b.altitude, height=b.antenna_height_m or conf.HM),
                )
                self.assertEqual(budget.calibration_applied, distance <= envelope,
                                 f"pair {i},{j} at {distance:.0f} m disagrees about the envelope")
                checked += 1
        self.assertGreater(checked, 100)


if __name__ == "__main__":
    unittest.main()
