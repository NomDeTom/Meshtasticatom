"""Hills, valleys, land cover and real node geometry, for the SF++ transport.

Everything in this file is an adapter onto code that already exists in `sim/meshtasticator/lib/` -
Komzpa's SRTM terrain, OSM land-cover clutter and the fitted link-calibration model from
Meshtasticator PR #77. None of it is reimplemented here. The vendored functions are called with the
vendored `Config` fields set the way the vendored simulator sets them, so a link budget computed
through this file and one computed by `loraMesh.py --preset batumi` differ only where this transport
deliberately differs (its own MAC, its own noise floor when `--noise-model thermal` is left on).

What this file adds is the three things that stood between that code and this simulator:

  * **a scenario**, so a run can take its node geometry from a real mesh instead of drawing points
    in a square. `batumi` is the packaged one; `map` pulls the public map and cuts a bounding box
    out of it, which is how Komzpa's original scenarios were built;
  * **a terrain source for a mesh that is not a real place.** A generated topology has no elevation
    to look up, and "3.2 km of reach in every direction" is the assumption a flat model makes.
    `synthetic` puts ridges and valleys under a generated mesh so the shape of the ground is a
    variable rather than a constant, and it is hashed rather than drawn so switching it on does not
    move the traffic schedule (the same discipline `NoiseField` follows, and for the same reason);
  * **an index**, because `TerrainGrid.elevation_at` sorts every sample on every call. That is fine
    for the packaged 78-point Batumi grid and unusable for an SRTM tile: a 60-node mesh asks for
    85 000 elevations before it has sent a packet. `IndexedTerrainGrid` answers the identical
    inverse-distance question over a bucketed candidate set, and `test_terrain_index_matches_vendored`
    holds it to the vendored answer.

The three loss terms stay separable on purpose, because they are three different claims and the
register has to be able to price them apart:

  | term                | flag                    | what it says                                          |
  | ------------------- | ----------------------- | ----------------------------------------------------- |
  | terrain             | `--terrain`             | a ridge is between these two nodes                    |
  | clutter             | `--clutter`             | the path crosses apartment blocks, forest, or water   |
  | link calibration    | `--link-calibration`    | a ridge fit against 296 observed Batumi links         |

`--scenario batumi` turns on all three, since that is the combination the coefficients were fitted
under and the only one where the calibration term means anything. Any of them can be turned off
again to ask what that term alone was worth.
"""

import csv
import heapq
import json
import math
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

# VENDOR_ROOT and CACHE_ROOT are re-exported: they were defined here before the transport had to
# work under two directory layouts, and other modules import them from this one.
from .vendor import CACHE_ROOT, PRESET_ROOT, VENDOR_ROOT, ensure_on_path  # noqa: F401

ensure_on_path()


# ---- the terrain index ----------------------------------------------------------------------


class IndexedTerrainGrid:
    """`TerrainGrid` with a spatial index. Same answers, without the per-call sort.

    A ring search over buckets, proven to cover the vendored nearest eight - MODEL.md.
    """

    NEAREST = 8

    # Below this the index is slower than the scan it replaces: 1.48 s of a 5.19 s Batumi
    # build went into ring widening. It earns its keep on an SRTM tile, not a preset.
    SCAN_BELOW = 512

    def __init__(self, samples):
        self.samples = list(samples)
        if not self.samples:
            raise ValueError("terrain grid has no samples")
        self.scan_only = len(self.samples) < self.SCAN_BELOW
        if self.scan_only:
            self._buckets = {}
            self._cache = {}
            self.cell = 1.0
            return
        xs = sorted({x for x, _, _ in self.samples})
        ys = sorted({y for _, y, _ in self.samples})
        # The grid's own spacing where it has one, sqrt(N) cells per axis where it does not:
        # either way a bucket holds O(1) samples, which is what bounds the ring search.
        self.cell = max(1.0, _median_spacing(xs, ys, len(self.samples)))
        self._buckets = {}
        for index, (x, y, elevation) in enumerate(self.samples):
            self._buckets.setdefault(
                (int(math.floor(x / self.cell)), int(math.floor(y / self.cell))), []
            ).append((x, y, elevation, index))
        # The occupied extent, so the ring knows when it has covered every sample: counting
        # cells against occupied buckets does not, since a square can be all empty cells.
        self._bx_min = min(bx for bx, _ in self._buckets)
        self._bx_max = max(bx for bx, _ in self._buckets)
        self._by_min = min(by for _, by in self._buckets)
        self._by_max = max(by for _, by in self._buckets)
        self._cache = {}

    @classmethod
    def from_rows(cls, rows):
        samples = []
        for row_number, row in enumerate(rows, start=1):
            try:
                x, y, elevation = row
            except (TypeError, ValueError) as err:
                raise ValueError(
                    f"terrain sample {row_number} must have x, y, and elevation"
                ) from err
            x, y, elevation = float(x), float(y), float(elevation)
            if not (
                math.isfinite(x) and math.isfinite(y) and math.isfinite(elevation)
            ):
                raise ValueError(f"terrain sample {row_number} values must be finite")
            samples.append((x, y, elevation))
        return cls(samples)

    def elevation_at(self, x, y):
        # Every pair sharing an endpoint walks the same coordinates, 24 per link. A decimetre
        # is below anything the model can see, and rounding to it removes most of the lookups.
        key = (round(x, 1), round(y, 1))
        hit = self._cache.get(key)
        if hit is not None:
            return hit
        value = self._compute(x, y)
        self._cache[key] = value
        return value

    def _compute(self, x, y):
        if self.scan_only:
            # Exactly the vendored calculation, and the parity tests hold both paths to it.
            weighted_sum = 0.0
            weight_total = 0.0
            for distance, elevation in heapq.nsmallest(
                self.NEAREST,
                (
                    (math.hypot(x - sx, y - sy), elevation)
                    for sx, sy, elevation in self.samples
                ),
                key=lambda item: item[0],
            ):
                if distance < 0.01:
                    return elevation
                weight = 1.0 / (distance * distance)
                weighted_sum += elevation * weight
                weight_total += weight
            return weighted_sum / weight_total

        cx = int(math.floor(x / self.cell))
        cy = int(math.floor(y / self.cell))

        found = []
        ring = 0
        while True:
            for bx in range(cx - ring, cx + ring + 1):
                for by in range(cy - ring, cy + ring + 1):
                    # Only the newly exposed shell of the square, not the whole square again.
                    if ring and max(abs(bx - cx), abs(by - cy)) != ring:
                        continue
                    for sx, sy, elevation, index in self._buckets.get((bx, by), ()):
                        found.append((math.hypot(x - sx, y - sy), index, elevation))
            found.sort()
            # Anything outside the examined square is at least `ring * cell` away, measured from
            # the nearest cell edge. Stop once the eighth candidate is closer than that.
            if len(found) >= self.NEAREST:
                guaranteed = ring * self.cell
                if found[self.NEAREST - 1][0] <= guaranteed:
                    break
            # Every occupied bucket is inside the examined square, so widening it further cannot
            # reach a sample that is not already in `found`.
            if (
                cx - ring <= self._bx_min
                and cx + ring >= self._bx_max
                and cy - ring <= self._by_min
                and cy + ring >= self._by_max
            ):
                break
            ring += 1

        weighted_sum = 0.0
        weight_total = 0.0
        for distance, _index, elevation in found[: self.NEAREST]:
            if distance < 0.01:
                return elevation
            weight = 1.0 / (distance * distance)
            weighted_sum += elevation * weight
            weight_total += weight
        return weighted_sum / weight_total


def _median_spacing(xs, ys, sample_count):
    """The grid's step where it is regular, and a bounding-box estimate where it is not."""
    steps = []
    for values in (xs, ys):
        gaps = sorted(b - a for a, b in zip(values, values[1:]) if b > a)
        if gaps:
            steps.append(gaps[len(gaps) // 2])
    if steps:
        return max(steps)
    span = max(
        (xs[-1] - xs[0]) if len(xs) > 1 else 0.0,
        (ys[-1] - ys[0]) if len(ys) > 1 else 0.0,
    )
    return span / max(1.0, math.sqrt(sample_count)) if span else 1.0


# ---- synthetic ground -----------------------------------------------------------------------


def _mix64(x):
    """SplitMix64's finaliser, as `mesh.NoiseField` uses it. Nothing is drawn from an RNG here."""
    x &= 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
    return (x ^ (x >> 31)) & 0xFFFFFFFFFFFFFFFF


def _unit(*key):
    h = 0x9E3779B97F4A7C15
    for k in key:
        h = _mix64(h ^ (int(k) & 0xFFFFFFFFFFFFFFFF))
    return h / 18446744073709551616.0


# Named ground shapes, none of them measured: they make the shape of the ground a variable
# rather than the constant zero. Field meanings in MODEL.md.
LANDFORMS = {
    # No relief at all. The control, and identical to running with terrain off except that the
    # elevation term is exercised, so it is also the test that terrain costs nothing on flat ground.
    "flat": {"relief_m": 0.0, "ridges": 1, "roughness": 0.0},
    # Gentle rolling country: nothing blocks a link outright, margins move by a few dB.
    "rolling": {"relief_m": 120.0, "ridges": 3, "roughness": 0.25},
    # One ridge across the middle, which is the case that splits a mesh in two.
    "ridge": {"relief_m": 400.0, "ridges": 1, "roughness": 0.15},
    # Steep valleys: most nodes are in a basin and hear their own basin.
    "valleys": {"relief_m": 500.0, "ridges": 4, "roughness": 0.35},
    # Mountains, where line of sight is the exception rather than the rule.
    "alpine": {"relief_m": 900.0, "ridges": 5, "roughness": 0.45},
    # A coastal shelf: flat and low on one side, rising hard on the other. Batumi's own shape, and
    # the reason a mesh there is not a disc.
    "coastal": {"relief_m": 600.0, "ridges": 2, "roughness": 0.2},
}


def synthetic_terrain_rows(landform, area, seed, step=None):
    """A regular elevation grid over `[-area, area]^2`, hashed from `seed`.

    Two ridge systems plus a lattice perturbation, so both wavelengths are present - MODEL.md.
    """
    shape = LANDFORMS[landform]
    relief = shape["relief_m"]
    ridges = shape["ridges"]
    roughness = shape["roughness"]
    span = area
    step = step or max(200.0, 2 * span / 48.0)

    phase_a = _unit(seed, 1) * 2 * math.pi
    phase_b = _unit(seed, 2) * 2 * math.pi
    tilt = _unit(seed, 3) * math.pi

    rows = []
    n = int(math.ceil(2 * span / step)) + 1
    for i in range(n):
        x = -span + i * step
        for j in range(n):
            y = -span + j * step
            u = (x * math.cos(tilt) + y * math.sin(tilt)) / span
            v = (-x * math.sin(tilt) + y * math.cos(tilt)) / span
            if landform == "coastal":
                # A shoreline along one axis: sea level on the low side, rising to the ridge line.
                base = 0.5 * (1.0 + math.tanh(2.2 * (u + 0.35)))
                base *= 0.5 * (1.0 + math.cos(math.pi * ridges * v + phase_b))
            else:
                base = 0.5 * (1.0 + math.cos(math.pi * ridges * u + phase_a))
                base *= 0.5 * (1.0 + math.cos(math.pi * ridges * v + phase_b))
            # Irwin-Hall over four hashed draws, so the perturbation is roughly normal and depends
            # on nothing but the lattice index.
            jitter = (
                _unit(seed, i, j, 0)
                + _unit(seed, i, j, 1)
                + _unit(seed, i, j, 2)
                + _unit(seed, i, j, 3)
            ) / 4.0 - 0.5
            elevation = relief * (base + roughness * jitter)
            rows.append((x, y, max(0.0, elevation)))
    return rows


# ---- the scenario ---------------------------------------------------------------------------


@dataclass
class Scenario:
    """A place: where the nodes are and what is under them.

    Local metres from `origin`, and `antenna_height` never becomes altitude - MODEL.md.
    """

    name: str
    points: list
    antenna_height: list
    origin: tuple = None
    absolute_altitude: list = field(default_factory=list)
    roles: list = field(default_factory=list)
    hop_limits: list = field(default_factory=list)
    antenna_gain: list = field(default_factory=list)
    terrain_rows: list = None
    clutter_file: Path = None
    calibration: dict = field(default_factory=dict)
    # Set when the geometry is a real mesh rather than points under a generated one. A run over real
    # geometry must not also be told a node count or an area; the place decides both.
    fixed_geometry: bool = False

    def __len__(self):
        return len(self.points)

    def __bool__(self):
        """A scenario is always a scenario, whatever `__len__` says.

        A landform has ground and no points, and falsiness silently dropped it - TRAPS 1.
        """
        return True

    @property
    def node_count(self):
        return len(self.points)

    def extent(self):
        """Half-width of the smallest square centred on the origin that holds every node."""
        if not self.points:
            return 0.0
        return max(max(abs(x), abs(y)) for x, y in self.points)

    def summary(self):
        """What went into the run, for the JSON. Every claim a result rests on, in one dict."""
        elevations = [z for _, _, z in (self.terrain_rows or [])]
        out = {
            "scenario": self.name,
            "nodes": self.node_count,
            "fixed_geometry": self.fixed_geometry,
            "origin": list(self.origin) if self.origin else None,
            "extent_m": round(self.extent(), 1),
            "terrain_samples": len(self.terrain_rows or []),
            "clutter": self.clutter_file.name if self.clutter_file else None,
            "link_calibration": bool(
                self.calibration.get("link_calibration_model", {}).get("coefficients")
            ),
        }
        if elevations:
            out["ground_elevation_m"] = {
                "min": round(min(elevations), 1),
                "max": round(max(elevations), 1),
                "mean": round(sum(elevations) / len(elevations), 1),
            }
        return out


def preset_scenario(name="batumi"):
    """The packaged real-mesh snapshot, geometry and ground together.

    Roles, hop limits and mute flags come from the snapshot, not from --router-fraction.
    """
    import yaml

    nodes_path = PRESET_ROOT / f"{name}.yaml"
    if not nodes_path.exists():
        raise ValueError(
            f"unknown scenario preset {name!r}; have "
            f"{', '.join(sorted(p.stem for p in PRESET_ROOT.glob('*.yaml')))}"
        )
    with nodes_path.open(encoding="utf-8") as fh:
        raw = yaml.safe_load(fh)

    origin = None
    if isinstance(raw.get("origin"), dict):
        origin = (float(raw["origin"]["lat"]), float(raw["origin"]["lon"]))

    points, heights, roles, hop_limits, gains, altitudes = [], [], [], [], [], []
    for _key, node in sorted(raw["nodes"].items(), key=lambda kv: int(kv[0])):
        points.append((float(node["x"]), float(node["y"])))
        heights.append(float(node.get("z", 1.5)))
        altitudes.append(node.get("absoluteAltitude"))
        gains.append(float(node.get("antennaGain", 0.0)))
        hop_limits.append(int(node.get("hopLimit", 3)))
        roles.append(_role_from_flags(node))

    terrain_path = PRESET_ROOT / f"{name}_terrain.csv"
    clutter_path = PRESET_ROOT / f"{name}_clutter.csv"
    calibration = dict(raw.get("radio_calibration", {}) or {})
    # How far the fit was actually trained, from its own observations: it extrapolates without
    # complaint, and past that range it invents links - TRAPS 4.
    observed = [
        math.dist(points[o["from"]], points[o["to"]])
        for o in raw.get("calibration_observations", []) or []
        if 0 <= o.get("from", -1) < len(points) and 0 <= o.get("to", -1) < len(points)
    ]
    if observed:
        calibration["max_observed_link_m"] = max(observed)
    return Scenario(
        name=name,
        points=points,
        antenna_height=heights,
        origin=origin,
        absolute_altitude=altitudes,
        roles=roles,
        hop_limits=hop_limits,
        antenna_gain=gains,
        terrain_rows=_terrain_rows_from_csv(terrain_path)
        if terrain_path.exists()
        else None,
        clutter_file=clutter_path if clutter_path.exists() else None,
        calibration=calibration,
        fixed_geometry=True,
    )


def _role_from_flags(node):
    if node.get("isRouter"):
        return "ROUTER"
    if node.get("isRepeater"):
        return "REPEATER"
    if node.get("isClientMute"):
        return "CLIENT_MUTE"
    return "CLIENT"


def _terrain_rows_from_csv(path):
    with Path(path).open(encoding="utf-8", newline="") as fh:
        return [
            (float(row["x_m"]), float(row["y_m"]), float(row["elevation_m"]))
            for row in csv.DictReader(fh)
        ]


def map_scenario(
    bbox,
    payload=None,
    limit=None,
    antenna_height=1.5,
    hop_limit=3,
    terrain_step_m=600.0,
    clutter_step_m=500.0,
    offline=False,
):
    """A mesh cut out of the public map, with SRTM ground and OSM land cover under it.

    `bbox` is (min_lat, min_lon, max_lat, max_lon); `offline` refuses the network rather than hanging.
    """
    from lib.map_input import (
        fetch_map_payload,
        filter_positioned_map_nodes,
        node_configs_from_positioned_rows,
        payload_nodes,
    )

    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    if payload is None:
        cached = CACHE_ROOT / "map_nodes.json"
        if cached.exists():
            payload = json.loads(cached.read_text(encoding="utf-8"))
        elif offline:
            raise RuntimeError(
                f"offline and no cached map payload at {cached}; fetch one first"
            )
        else:
            payload = fetch_map_payload()
            cached.write_text(json.dumps(payload), encoding="utf-8")
    elif isinstance(payload, (str, Path)):
        payload = json.loads(Path(payload).read_text(encoding="utf-8"))

    positioned = filter_positioned_map_nodes(payload_nodes(payload), bbox)
    if limit:
        positioned = positioned[:limit]
    if not positioned:
        raise ValueError("map payload produced no positioned nodes in that bounding box")

    configs, origin = node_configs_from_positioned_rows(
        positioned,
        period=0,
        antenna_height=antenna_height,
        hop_limit=hop_limit,
        return_origin=True,
    )

    points = [(c.position.x, c.position.y) for c in configs]
    return Scenario(
        name=f"map:{bbox[0]:.3f},{bbox[1]:.3f},{bbox[2]:.3f},{bbox[3]:.3f}",
        points=points,
        antenna_height=[c.antenna_height for c in configs],
        origin=origin,
        absolute_altitude=[c.absolute_altitude for c in configs],
        roles=[_role_from_config(c) for c in configs],
        hop_limits=[c.hop_limit for c in configs],
        antenna_gain=[c.antenna_gain for c in configs],
        terrain_rows=_srtm_rows(bbox, origin, terrain_step_m, offline),
        clutter_file=_osm_clutter(bbox, origin, clutter_step_m, offline),
        fixed_geometry=True,
    )


def _role_from_config(config):
    name = getattr(config.role, "name", str(config.role))
    return name if name in {"ROUTER", "REPEATER", "CLIENT_MUTE", "ROUTER_LATE"} else "CLIENT"


def _srtm_rows(bbox, origin, step_m, offline):
    """SRTM elevation over the bounding box, in the scenario's local metres.

    Through the same `latlon_to_xy` the node positions went through, so coordinates line up.
    """
    from lib.srtm import terrain_rows_from_srtm
    from lib.terrain import latlon_to_xy

    cached = CACHE_ROOT / f"terrain_{_bbox_slug(bbox)}_{int(step_m)}.csv"
    if cached.exists():
        return _terrain_rows_from_csv(cached)
    if offline:
        raise RuntimeError(f"offline and no cached terrain at {cached}")
    rows = [
        (
            *latlon_to_xy(float(row["lat"]), float(row["lon"]), origin[0], origin[1]),
            float(row["elevation_m"]),
        )
        for row in terrain_rows_from_srtm(bbox, step_m, str(CACHE_ROOT))
    ]
    with cached.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(("x_m", "y_m", "elevation_m"))
        writer.writerows(rows)
    return rows


def _osm_clutter(bbox, origin, step_m, offline):
    from lib.osm_clutter import fetch_overpass_payload, rasterize_clutter, write_clutter_csv

    cached = CACHE_ROOT / f"clutter_{_bbox_slug(bbox)}_{int(step_m)}.csv"
    if cached.exists():
        return cached
    if offline:
        return None
    rows = rasterize_clutter(
        fetch_overpass_payload(bbox), bbox, origin=origin, step_m=step_m
    )
    write_clutter_csv(rows, cached)
    return cached


def _bbox_slug(bbox):
    return "_".join(f"{v:.4f}" for v in bbox)


def tile_grid_for(copies):
    """The most square arrangement of `copies` tiles, wider than it is tall."""
    best = (1, copies)
    for gx in range(1, int(math.isqrt(copies)) + 1):
        if copies % gx == 0:
            best = (copies // gx, gx)
    return best


def mirror(scenario, copies, gap_m=1500.0):
    """Reflect a scenario into `copies` tiles, ground and all.

    Reflection, not translation, and it scales a place rather than a mesh - MODEL.md.
    """
    if copies <= 1:
        return scenario
    if not scenario.fixed_geometry:
        raise ValueError("mirror needs real geometry; a landform already covers its own area")

    gx, gy = tile_grid_for(copies)
    xs = [p[0] for p in scenario.points]
    ys = [p[1] for p in scenario.points]
    rows = _clutter_rows(scenario.clutter_file) if scenario.clutter_file else []
    for x, y, _ in scenario.terrain_rows or []:
        xs.append(x)
        ys.append(y)
    for x, y, _lat, _lon, _cls in rows:
        xs.append(x)
        ys.append(y)
    # The tile spans everything the scenario knows about, so no data is clipped, plus a margin -
    # without it the outermost nodes of two tiles would land on top of each other at the seam.
    x0, x1 = min(xs) - gap_m, max(xs) + gap_m
    y0, y1 = min(ys) - gap_m, max(ys) + gap_m
    w, h = x1 - x0, y1 - y0

    def place(x, y, i, j):
        u = x - x0
        v = y - y0
        return (
            x0 + i * w + (u if i % 2 == 0 else w - u),
            y0 + j * h + (v if j % 2 == 0 else h - v),
        )

    points, terrain, clutter = [], [], []
    seen_clutter = set()
    for i in range(gx):
        for j in range(gy):
            for x, y in scenario.points:
                points.append(place(x, y, i, j))
            for x, y, z in scenario.terrain_rows or []:
                terrain.append((*place(x, y, i, j), z))
            for x, y, lat, lon, cls in rows:
                px, py = place(x, y, i, j)
                # Adjacent reflected tiles share the boundary column, and a duplicate makes the
                # grid irregular - minutes per build rather than seconds. TRAPS 8.
                key = (round(px, 3), round(py, 3))
                if key in seen_clutter:
                    continue
                seen_clutter.add(key)
                clutter.append((px, py, lat, lon, cls))

    n = gx * gy
    path = scenario.clutter_file
    if clutter:
        CACHE_ROOT.mkdir(parents=True, exist_ok=True)
        path = CACHE_ROOT / f"{scenario.name}-mirror{gx}x{gy}-clutter.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["x_m", "y_m", "lat", "lon", "clutter_class"])
            for px, py, lat, lon, cls in clutter:
                writer.writerow([px, py, lat, lon, cls])

    def repeat(seq):
        return list(seq) * n if seq else list(seq)

    return Scenario(
        name=f"{scenario.name}-x{n}",
        points=points,
        antenna_height=repeat(scenario.antenna_height),
        origin=scenario.origin,
        absolute_altitude=repeat(scenario.absolute_altitude),
        roles=repeat(scenario.roles),
        hop_limits=repeat(scenario.hop_limits),
        antenna_gain=repeat(scenario.antenna_gain),
        terrain_rows=terrain,
        clutter_file=path,
        calibration=scenario.calibration,
        fixed_geometry=True,
    )


def _clutter_rows(path):
    """The raster as (x_m, y_m, lat, lon, class), for a transform that has to rewrite x and y."""
    out = []
    with Path(path).open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            out.append(
                (
                    float(row["x_m"]),
                    float(row["y_m"]),
                    row.get("lat", ""),
                    row.get("lon", ""),
                    row.get("clutter_class", "open"),
                )
            )
    return out


def synthetic_scenario(landform, area, seed, name=None):
    """Ground under a generated mesh. No geometry of its own - `build()` still places the nodes."""
    if landform not in LANDFORMS:
        raise ValueError(
            f"unknown landform {landform!r}; have {', '.join(sorted(LANDFORMS))}"
        )
    return Scenario(
        name=name or f"synthetic:{landform}",
        points=[],
        antenna_height=[],
        terrain_rows=synthetic_terrain_rows(landform, area, seed),
        fixed_geometry=False,
    )


def load(spec, area=8000.0, seed=0, bbox=None, limit=None, offline=False):
    """Resolve a `--scenario` string.

    A preset name is real geometry, a landform is ground under a generated mesh, `map` is a bbox.
    """
    if spec in (None, "", "none"):
        return None
    if spec in LANDFORMS:
        return synthetic_scenario(spec, area, seed)
    if spec == "map":
        if bbox is None:
            raise ValueError("--scenario map needs --bbox min_lat,min_lon,max_lat,max_lon")
        return map_scenario(bbox, limit=limit, offline=offline)
    return preset_scenario(spec)


def available():
    """Every scenario name `load` accepts, for the CLI's help and for `--list`."""
    return sorted(
        [p.stem for p in PRESET_ROOT.glob("*.yaml")] + list(LANDFORMS) + ["map"]
    )


# ---- applying it to the vendored Config ------------------------------------------------------


def apply(conf, scenario, terrain=True, clutter=True, link_calibration=True):
    """Set the vendored terrain, clutter and calibration fields from a scenario.

    Each is separately refusable because each is a separate claim - MODEL.md. Returns the grid.
    """
    grid = None
    if scenario is None:
        return None

    if scenario.origin:
        conf.GEO_ORIGIN_LAT, conf.GEO_ORIGIN_LON = scenario.origin

    if terrain and scenario.terrain_rows:
        grid = IndexedTerrainGrid.from_rows(scenario.terrain_rows)
        conf.TERRAIN_ENABLED = True
        conf.TERRAIN_GRID = grid
    else:
        conf.TERRAIN_ENABLED = False
        conf.TERRAIN_GRID = None

    if clutter and scenario.clutter_file:
        conf.CLUTTER_ENABLED = True
        conf.CLUTTER_GRID_FILE = str(scenario.clutter_file)
    else:
        conf.CLUTTER_ENABLED = False
        conf.CLUTTER_GRID_FILE = None

    calibration = scenario.calibration or {}
    # Measurements of the place, not of the link model, so they arrive with the scenario whatever
    # the calibration flag says. An explicit --noise-model still wins, being applied after.
    for source, target in (
        ("noise_level", "NOISE_LEVEL"),
        ("path_loss_distance_floor_m", "PATH_LOSS_DISTANCE_FLOOR_M"),
        ("reported_snr_min_db", "REPORTED_SNR_MIN_DB"),
        ("reported_snr_max_db", "REPORTED_SNR_MAX_DB"),
    ):
        if source in calibration:
            setattr(conf, target, float(calibration[source]))

    # The envelope the fit has support over. Beyond it the caller falls back to the raw budget,
    # because a linear model asked about a distance it never saw answers confidently and wrongly.
    conf.LINK_CALIBRATION_MAX_M = (
        float(calibration["max_observed_link_m"])
        if "max_observed_link_m" in calibration
        else None
    )

    model = calibration.get("link_calibration_model", {}) if link_calibration else {}
    conf.LINK_CALIBRATION_MODEL_ENABLED = bool(model.get("coefficients"))
    conf.LINK_CALIBRATION_COEFFICIENTS = {
        str(k): float(v) for k, v in model.get("coefficients", {}).items()
    }
    conf.LINK_CALIBRATION_SNR_MIN_DB = (
        float(model["snr_min_db"]) if "snr_min_db" in model else None
    )
    conf.LINK_CALIBRATION_SNR_MAX_DB = (
        float(model["snr_max_db"]) if "snr_max_db" in model else None
    )

    # Anything cached against the previous configuration is stale now.
    for attr in ("_terrain_loss_cache", "_clutter_loss_cache", "_clutter_grid"):
        if hasattr(conf, attr):
            setattr(conf, attr, None if attr == "_clutter_grid" else {})
    return grid


def ground_elevation(grid, x, y):
    """Ground height under a point, or 0 where there is no terrain."""
    return 0.0 if grid is None else grid.elevation_at(x, y)


class Point:
    """The x, y, z the vendored terrain and clutter code asks for.

    An adapter from this transport's flat node records, not a second position type.
    """

    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def euclidean_distance(self, other):
        return math.dist((self.x, self.y, self.z), (other.x, other.y, other.z))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
