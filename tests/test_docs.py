import re
import unittest
from pathlib import Path

from lib.config import Config


class TestDocumentation(unittest.TestCase):
    def test_modem_table_matches_config_base_settings(self):
        docs = Path("DISCRETE_EVENT_SIM.md").read_text(encoding="utf-8")
        rows = [
            row
            for row in docs.splitlines()
            if re.match(r"^\| \d+ \|", row)
        ]

        conf = Config()
        self.assertEqual(len(rows), len(conf.MODEM_PRESETS))

        for row, (preset_name, preset) in zip(rows, conf.MODEM_PRESETS.items()):
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            _, display_name, bandwidth_khz, coding_rate, spreading_factor, _ = cells

            self.assertEqual(display_name.upper().replace(" ", "_"), preset_name)
            self.assertEqual(float(bandwidth_khz), preset["bw"] / 1000)
            self.assertEqual(coding_rate, f"4/{preset['cr']}")
            self.assertEqual(int(spreading_factor), preset["sf"])


class TestVersionPins(unittest.TestCase):
    """A pin comment a reader trusts has to be checkable against the code beside it."""

    def test_the_documented_pin_matches_the_one_in_the_code(self):
        pin = "51eadb7"
        docs = Path("DISCRETE_EVENT_SIM.md").read_text(encoding="utf-8")
        self.assertIn(pin, docs)
        for source in ("lib/mac.py", "lib/phy.py", "lib/config.py"):
            with self.subTest(source=source):
                self.assertIn(pin, Path(source).read_text(encoding="utf-8"))

    def test_the_documented_daemon_image_is_the_one_that_runs(self):
        # Read rather than import: lib.interactive pulls in lib.gui, which forces a Tk backend.
        source = Path("lib/interactive.py").read_text(encoding="utf-8")
        tag = re.search(r'MESHTASTICD_IMAGE_TAG = "([^"]+)"', source).group(1)
        self.assertIn(tag, Path("DISCRETE_EVENT_SIM.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
