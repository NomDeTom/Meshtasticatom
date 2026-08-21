import tempfile
import unittest
from pathlib import Path

from lib.clutter import ClutterGrid, clutter_obstruction_loss, clutter_path_features
from lib.config import Config
from lib.point import Point


class TestClutter(unittest.TestCase):
    def test_csv_grid_returns_nearest_regular_cell_class(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "clutter.csv"
            path.write_text(
                "x_m,y_m,clutter_class\n"
                "0,0,urban\n"
                "500,0,water\n",
                encoding="utf-8",
            )

            grid = ClutterGrid.from_csv(path)

        self.assertEqual(grid.class_at(20, 0), "urban")
        self.assertEqual(grid.class_at(480, 0), "water")

    def test_csv_grid_rejects_non_finite_samples(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "clutter.csv"
            path.write_text(
                "x_m,y_m,clutter_class\n"
                "0,nan,urban\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "row 2"):
                ClutterGrid.from_csv(path)

    def test_csv_grid_rejects_blank_clutter_class(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "clutter.csv"
            path.write_text(
                "x_m,y_m,clutter_class\n"
                "0,0,   \n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "clutter_class"):
                ClutterGrid.from_csv(path)

    def test_latlon_csv_grid_rejects_out_of_range_samples(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "clutter.csv"
            path.write_text(
                "lat,lon,clutter_class\n"
                "91,41,urban\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "latitude/longitude"):
                ClutterGrid.from_csv(path, origin_lat=41.0, origin_lon=41.0)

    def test_urban_clutter_adds_more_loss_than_coastal_open_path(self):
        conf = Config()
        conf.CLUTTER_ENABLED = True
        conf.CLUTTER_PROFILE_SAMPLES = 4

        with tempfile.TemporaryDirectory() as tmpdir:
            urban_path = Path(tmpdir) / "urban.csv"
            urban_path.write_text(
                "x_m,y_m,clutter_class\n"
                "0,0,urban\n"
                "500,0,urban\n"
                "1000,0,urban\n",
                encoding="utf-8",
            )
            conf.CLUTTER_GRID_FILE = str(urban_path)

            urban_loss = clutter_obstruction_loss(conf, Point(0, 0, 2), Point(1000, 0, 2))

            open_path = Path(tmpdir) / "open.csv"
            open_path.write_text(
                "x_m,y_m,clutter_class\n"
                "0,0,water\n"
                "500,0,water\n"
                "1000,0,water\n",
                encoding="utf-8",
            )
            conf._clutter_grid = None
            conf._clutter_loss_cache = {}
            conf.CLUTTER_GRID_FILE = str(open_path)

            open_loss = clutter_obstruction_loss(conf, Point(0, 0, 2), Point(1000, 0, 2))

        self.assertGreater(urban_loss, open_loss)

    def test_latlon_grid_cache_tracks_projection_origin(self):
        conf = Config()
        conf.CLUTTER_ENABLED = True
        conf.CLUTTER_PROFILE_SAMPLES = 1

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "clutter.csv"
            path.write_text(
                "lat,lon,clutter_class\n"
                "10.0,10.0,urban\n"
                "10.0,10.01,water\n",
                encoding="utf-8",
            )
            conf.CLUTTER_GRID_FILE = str(path)
            conf.GEO_ORIGIN_LAT = 10.0
            conf.GEO_ORIGIN_LON = 10.0

            first = clutter_path_features(conf, Point(0, 0, 1), Point(0, 0, 1))
            self.assertEqual(first["urban_fraction"], 1.0)

            # One CSV can be projected around a different origin, so the origin is part of
            # the cache key: otherwise a second scenario reuses the first one's cells.
            conf.GEO_ORIGIN_LON = 10.01
            second = clutter_path_features(conf, Point(0, 0, 1), Point(0, 0, 1))
            self.assertEqual(second["water_fraction"], 1.0)


if __name__ == "__main__":
    unittest.main()


class UnknownClassesAreRefused(unittest.TestCase):
    """A silent substitution produced a well-formed number for a raster nobody had checked."""

    def test_an_unrecognised_class_raises_rather_than_charging_the_open_rate(self):
        from lib.clutter import _class_loss_db_per_km

        conf = Config()
        for name in ("industrial", "agriculture", "grass", "Urban", ""):
            with self.subTest(clutter_class=name):
                with self.assertRaises(ValueError):
                    _class_loss_db_per_km(conf, name)

    def test_every_class_the_exporter_emits_is_known_to_the_loss_table(self):
        from lib.clutter import KNOWN_CLASSES
        from lib.osm_clutter import classify_osm_element

        emitted = {
            classify_osm_element(tags)
            for tags in (
                {"building": "yes"},
                {"landuse": "residential"},
                {"landuse": "forest"},
                {"natural": "water"},
                {"natural": "beach"},
                {"natural": "grassland"},
            )
        }
        self.assertTrue(emitted)
        self.assertLessEqual(emitted, KNOWN_CLASSES)

    def test_a_raster_naming_an_unknown_class_is_rejected_at_load(self):
        import tempfile
        from pathlib import Path

        from lib.clutter import ClutterGrid

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("x_m,y_m,clutter_class\n0,0,open\n500,0,industrial\n")
            with self.assertRaises(ValueError):
                ClutterGrid.from_csv(path)


class TheCoastalDiscountNeedsACoast(unittest.TestCase):
    def test_an_unmapped_inland_path_is_not_discounted_as_coastal(self):
        """`open` is the exporter's default for a cell it found nothing in, and 72% of the packaged
        Batumi raster is open, so this test used to fire on a quarter of all pairs."""
        from lib.clutter import clutter_obstruction_loss

        conf = Config()
        conf.CLUTTER_ENABLED = True
        conf.CLUTTER_GRID_FILE = self.write_grid(["open"] * 9)
        inland = clutter_obstruction_loss(conf, Point(0.0, 0.0, 2.0), Point(2000.0, 0.0, 2.0))

        conf._clutter_grid = None
        conf.CLUTTER_GRID_FILE = self.write_grid(["water"] * 9)
        coastal = clutter_obstruction_loss(conf, Point(0.0, 0.0, 2.0), Point(2000.0, 0.0, 2.0))

        # Water costs less per km than open ground, so the coastal path is cheaper - but the
        # inland one gets no 4x discount for being unmapped.
        self.assertGreater(inland, coastal)

    def write_grid(self, classes):
        import tempfile
        from pathlib import Path

        directory = tempfile.mkdtemp()
        path = Path(directory) / "grid.csv"
        rows = ["x_m,y_m,clutter_class"]
        index = 0
        for x in (-1000, 1000, 3000):
            for y in (-1000, 0, 1000):
                rows.append(f"{x},{y},{classes[index]}")
                index += 1
        path.write_text("\n".join(rows) + "\n")
        return str(path)
