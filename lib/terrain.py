"""Optional terrain obstruction model for radio links.

The simulator's default coordinates are local meters with `Point.z` acting like
antenna height. Terrain-aware input loaders can lift points to absolute antenna
altitude (`ground elevation + antenna height`) so the existing 3D distance path
already reflects terrain before any extra RF obstruction loss is applied.

The loss model is intentionally conservative and dependency-free: sample the
path, find the worst Fresnel/line-of-sight obstruction, then apply the standard
single knife-edge diffraction approximation for that obstruction. It is not a
full ray tracer, but it captures the important Batumi-mesh case where hills and
ridges matter more than flat-earth distance alone.
"""

import heapq
import itertools
import math


EARTH_RADIUS_M = 6371000.0
NODE_Z_REFERENCE_GROUND = "ground"
NODE_Z_REFERENCE_SEA_LEVEL = "sea_level"
MAX_REASONABLE_STRUCTURE_HEIGHT_M = 850.0


def normalize_longitude_delta(lon, origin_lon):
    """Return shortest signed longitude delta in degrees."""
    return ((lon - origin_lon + 180.0) % 360.0) - 180.0


def normalize_longitude(lon):
    """Normalize longitude to the conventional [-180, 180] range."""
    return ((lon + 180.0) % 360.0) - 180.0


def latlon_to_xy(lat, lon, origin_lat, origin_lon):
    """Project WGS84 lat/lon to local x/y meters with an equirectangular map."""
    origin_lat_rad = math.radians(origin_lat)
    lon_delta = normalize_longitude_delta(lon, origin_lon)
    x = math.radians(lon_delta) * EARTH_RADIUS_M * math.cos(origin_lat_rad)
    y = math.radians(lat - origin_lat) * EARTH_RADIUS_M
    return x, y


def xy_to_latlon(x, y, origin_lat, origin_lon):
    """Inverse of latlon_to_xy for small local simulation areas."""
    origin_lat_rad = math.radians(origin_lat)
    origin_cos = math.cos(origin_lat_rad)
    if abs(origin_cos) < 1e-9:
        raise ValueError("origin latitude is too close to a pole for local x/y projection")

    lat = origin_lat + math.degrees(y / EARTH_RADIUS_M)
    lon = normalize_longitude(origin_lon + math.degrees(x / (EARTH_RADIUS_M * origin_cos)))
    return lat, lon


class TerrainGrid:
    """Small scattered terrain sample grid with inverse-distance interpolation."""

    # The cache key identifies a grid by this token, not by id(): a recycled address
    # would otherwise revive entries computed against an earlier grid.
    _cache_token_counter = itertools.count(1)

    def __init__(self, samples):
        self.samples = samples
        self.cache_token = next(TerrainGrid._cache_token_counter)

    @classmethod
    def from_rows(cls, rows):
        """Build a terrain grid from `(x_m, y_m, elevation_m)` samples."""
        samples = []
        for row_number, row in enumerate(rows, start=1):
            try:
                x, y, elevation = row
            except (TypeError, ValueError) as err:
                raise ValueError(f"terrain sample {row_number} must have x, y, and elevation") from err
            x = float(x)
            y = float(y)
            elevation = float(elevation)
            if not math.isfinite(x) or not math.isfinite(y) or not math.isfinite(elevation):
                raise ValueError(f"terrain sample {row_number} values must be finite")
            samples.append((x, y, elevation))

        if not samples:
            raise ValueError("terrain grid has no samples")
        return cls(samples)

    # Value equality, so a config holding a grid can be compared - a deepcopy of a grid
    # describes the same ground, and identity comparison would call it a different one.
    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.samples == other.samples

    def __hash__(self):
        return hash((len(self.samples), self.samples[0], self.samples[-1]))

    def elevation_at(self, x, y):
        weighted_sum = 0.0
        weight_total = 0.0

        nearest = heapq.nsmallest(
            8,
            ((math.hypot(x - sx, y - sy), elevation) for sx, sy, elevation in self.samples),
            key=lambda item: item[0],
        )

        for distance, elevation in nearest:
            if distance < 0.01:
                return elevation
            weight = 1.0 / (distance * distance)
            weighted_sum += elevation * weight
            weight_total += weight

        return weighted_sum / weight_total


def _terrain_grid(conf):
    """Return the configured in-memory terrain grid when terrain is enabled."""
    if not conf.TERRAIN_ENABLED:
        return None
    return getattr(conf, "TERRAIN_GRID", None)


def terrain_ground_elevation(conf, point):
    """Return terrain elevation at a point, or None when terrain is unavailable."""
    grid = _terrain_grid(conf)
    if grid is None:
        return None
    return grid.elevation_at(point.x, point.y)


def map_altitude_if_plausible(node, ground):
    """Return per-node map altitude when SRTM says it is physically plausible."""
    altitude = getattr(node, "absolute_altitude", None)
    if altitude is None:
        return None
    altitude = float(altitude)
    if not math.isfinite(altitude):
        return None
    if altitude <= ground:
        return None
    if altitude > ground + MAX_REASONABLE_STRUCTURE_HEIGHT_M:
        return None
    return altitude


def node_antenna_height(node):
    """Return node antenna height above ground for config and live node types."""
    return getattr(
        node,
        "antenna_height",
        getattr(node, "antennaHeight", node.position.z),
    )


def apply_terrain_altitude(terrain_grid, node):
    """Lift one node's z to absolute antenna altitude from terrain.

    `antenna_height` stays height above local ground, which is what the path-loss terms want.
    """
    ground = terrain_grid.elevation_at(node.position.x, node.position.y)
    map_altitude = map_altitude_if_plausible(node, ground)
    if map_altitude is None:
        node.position.z = ground + node_antenna_height(node)
    else:
        node.position.z = map_altitude


def apply_terrain_altitudes(terrain_grid, node_config):
    """Lift node z coordinates to absolute antenna altitude from terrain."""
    for node in node_config:
        apply_terrain_altitude(terrain_grid, node)


def terrain_antenna_altitude(conf, grid, point):
    """Return absolute antenna altitude for a terrain-backed point."""
    ground = grid.elevation_at(point.x, point.y)
    min_altitude = ground + conf.TERRAIN_MIN_ANTENNA_HEIGHT_M
    if getattr(conf, "NODE_Z_REFERENCE", NODE_Z_REFERENCE_GROUND) == NODE_Z_REFERENCE_SEA_LEVEL:
        return max(point.z, min_altitude)
    return ground + max(point.z, conf.TERRAIN_MIN_ANTENNA_HEIGHT_M)


def knife_edge_loss_db(v):
    """ITU-R single knife-edge diffraction loss approximation."""
    if v <= -0.78:
        return 0.0
    return 6.9 + 20.0 * math.log10(math.sqrt((v - 0.1) ** 2 + 1.0) + v - 0.1)


def terrain_obstruction_loss(conf, tx_point, rx_point, freq):
    """Estimate extra terrain obstruction loss in dB for a TX/RX path."""
    grid = _terrain_grid(conf)
    if grid is None:
        return 0.0

    # In a static topology the terrain term is a pure function of the two endpoints,
    # and every packet asks for every receiver, so it is cached on the Config.
    cache = getattr(conf, "_terrain_loss_cache", None)
    if cache is None:
        cache = {}
        conf._terrain_loss_cache = cache

    cache_key = (
        round(tx_point.x, 2),
        round(tx_point.y, 2),
        round(tx_point.z, 2),
        round(rx_point.x, 2),
        round(rx_point.y, 2),
        round(rx_point.z, 2),
        round(freq, 0),
        getattr(grid, "cache_token", id(grid)),
        conf.GEO_ORIGIN_LAT,
        conf.GEO_ORIGIN_LON,
        conf.TERRAIN_PROFILE_SAMPLES,
        conf.TERRAIN_FRESNEL_CLEARANCE,
        conf.TERRAIN_EFFECTIVE_EARTH_RADIUS_MULTIPLIER,
        conf.TERRAIN_MIN_ANTENNA_HEIGHT_M,
        conf.TERRAIN_MAX_LOSS_DB,
    )
    if cache_key in cache:
        return cache[cache_key]

    horizontal_distance = math.hypot(rx_point.x - tx_point.x, rx_point.y - tx_point.y)
    if horizontal_distance <= 0:
        return 0.0

    wavelength = 299792458.0 / freq
    tx_height = terrain_antenna_altitude(conf, grid, tx_point)
    rx_height = terrain_antenna_altitude(conf, grid, rx_point)
    effective_earth_radius = EARTH_RADIUS_M * conf.TERRAIN_EFFECTIVE_EARTH_RADIUS_MULTIPLIER
    curvature_scale = (horizontal_distance * horizontal_distance) / (2.0 * effective_earth_radius)

    worst_loss = 0.0
    for i in range(1, conf.TERRAIN_PROFILE_SAMPLES):
        fraction = i / conf.TERRAIN_PROFILE_SAMPLES
        x = tx_point.x + (rx_point.x - tx_point.x) * fraction
        y = tx_point.y + (rx_point.y - tx_point.y) * fraction
        ground = grid.elevation_at(x, y)
        los_height = tx_height + (rx_height - tx_height) * fraction
        d1 = horizontal_distance * fraction
        d2 = horizontal_distance - d1

        fresnel_radius = math.sqrt(wavelength * d1 * d2 / horizontal_distance)
        # A flat projection makes long links look too clear, so each sample gets the
        # 4/3 earth bulge before clearance is measured against the antenna line.
        earth_bulge = curvature_scale * fraction * (1.0 - fraction)
        # Metres of clearance between the antenna line and the ground: positive when the path is
        # clear over this sample, negative when the terrain rises through it.
        clearance = los_height - (ground + earth_bulge)

        # TERRAIN_FRESNEL_CLEARANCE is a clearance *requirement*, not a height to add to the
        # obstruction. Adding it in offset v by a constant 0.6*sqrt(2) = 0.849, because the first
        # Fresnel radius is exactly the reciprocal of v's own scaling - so a grazing path was
        # charged 12.9 dB against a true 6.0, a path with 0.2*F1 of clearance 10.8 dB against
        # 3.7, and the loss jumped from 0 to 6.03 dB across the threshold. The requirement now
        # only decides when to stop looking, and at 0.6*F1 the ITU curve is already zero, so the
        # model is continuous in clearance.
        if clearance >= conf.TERRAIN_FRESNEL_CLEARANCE * fresnel_radius:
            continue

        v = -clearance * math.sqrt(2.0 * horizontal_distance / (wavelength * d1 * d2))
        worst_loss = max(worst_loss, knife_edge_loss_db(v))

    loss = min(worst_loss, conf.TERRAIN_MAX_LOSS_DB)
    cache[cache_key] = loss
    return loss
