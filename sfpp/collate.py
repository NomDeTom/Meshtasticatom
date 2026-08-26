r"""One scheduled sweep, read as a whole: what moved, what did nothing, and what must never happen.

`sweep.py` writes one JSON per block and prints a table per block. A scheduled run that covers every
block produces 87 of those, which is more than anyone reads, so nothing in them is looked at until
something has already gone wrong. This module reduces a whole run to two artefacts: `summary.json`,
the machine-readable digest the explorer rolls up across runs, and `trend.md`, the page a person
actually opens.

**Four measures of success, four denominators, not comparable to each other** (README §7.3). A
broadcast figure is the share of *all* nodes that heard it; a DM figure is whether it reached *the
one* node addressed, with acknowledgements and retries; an admin figure is per session the operator
wanted; held is over objects originated. DM success reading higher than broadcast reach does not
mean DMs work better, and the commonest misreading of this tool is taking one as a proxy for
another. This module reports all four and ranks a block by whichever moved most, naming it.

**`channel_utilisation` is aggregate airtime demand, not a utilisation.** It sums demand across the
whole mesh, legitimately exceeds 1.0, and on a spatially extended mesh is not even a proxy for local
conditions - nodes 30 km apart never contend. It is called `demand` throughout this module and is
never gated on. What decides whether a mesh is busy is `node_channel_util_percent`, a percentage
that cannot pass 100. Reading one as the other cost an entire analysis once already.

The gates below each correspond to a defect that shipped; the traps they catch are listed against
them. A run failing a fatal gate is not a run with a bad number in it, it is a run whose other
numbers cannot be trusted.

Usage, from the tree root:
    python3 -m sfpp.collate --runs <dir>                     # trend.md and summary.json beside it
    python3 -m sfpp.collate --runs <dir> --out <dir> \
        --run-id 2026-08-19 --seed-base 4711 --scenario ridge
"""

import argparse
import datetime
import glob
import hashlib
import json
import os
import statistics

# Everything the digest carries per cell, by path into a campaign report. An absent metric
# becomes None rather than raising, so mixed vintages still collate.
METRICS = {
    # --- the four successes. Different denominators; see the module docstring and README §7.3 ---
    "text": ("baseline", "text_reception_mean"),
    "dm": ("dm", "reception"),
    "admin": (
        "admin",
        "_success_rate",
    ),  # derived below, across every hop distance probed
    "held": ("sfpp", "held_fraction_mean"),
    # --- what each success separates. A mean alone cannot say "would more hops help" ---
    "text_worst": ("baseline", "text_reception_min"),
    "reach_ceiling": ("baseline", "reach_ceiling_mean"),
    "missed_beyond_hops": ("baseline", "missed_beyond_hop_limit"),
    "missed_within_reach": ("baseline", "missed_within_reach"),
    "dm_composed": ("dm", "composed"),
    "admin_sessions": ("admin", "_sessions"),
    "dm_no_key": ("dm", "no_key"),
    "dm_no_peer": ("dm", "no_addressable_peer"),
    "held_min": ("sfpp", "held_fraction_min"),
    "union": ("sfpp", "union_fraction"),
    # --- load. `demand` is a multiple with no ceiling; the chutil pair is a percentage ---
    "demand": ("traffic", "channel_utilisation"),
    "chutil_p90": ("traffic", "node_channel_util_percent", "p90"),
    "chutil_max": ("traffic", "node_channel_util_percent", "max"),
    "airutil_p90": ("traffic", "node_air_util_tx_percent", "p90"),
    "airutil_max": ("traffic", "node_air_util_tx_percent", "max"),
    # --- what the archive cost and did ---
    "sr_airtime": ("sfpp", "sr_airtime_share"),
    "moved": ("sfpp", "objects_moved"),
    "adverts": ("sfpp", "adverts"),
    "advert_bytes": ("sfpp", "advert_bytes"),
    "sr_bytes": ("sfpp", "sr_bytes"),
    "bystander_pickups": ("sfpp", "bystander_pickups"),
    # --- request against result. Both, because only one written down has misled twice ---
    "servers_requested": ("sfpp", "servers_requested"),
    "servers_placed": ("sfpp", "servers_placed"),
    "nodes": ("_derived", "nodes"),
    # --- safety and integrity ---
    "silent_losses": ("sfpp", "silent_losses"),
    "audit_disagrees": ("sfpp", "audit_checksum_agrees_sets_differ"),
    "misdecodes": ("sfpp", "misdecodes"),
    "decode_failures": ("sfpp", "decode_failures"),
    # --- traffic and mesh shape ---
    "transmissions": ("traffic", "transmissions"),
    "queue_drops": ("traffic", "queue_drops"),
    "bytes_on_air": ("traffic", "bytes_on_air"),
    "degree": ("mesh", "mean_degree"),
    "pairs_beyond_calibration": ("ground", "pairs_beyond_calibration"),
}

# The measures a block is ranked by: whichever moves furthest decides, and the table says which.
# Ranking on `held` alone would rate an arm that halves DM success as inert. MODEL.md.
SUCCESSES = ("text", "dm", "admin", "held")

# What an arm costs, read beside whichever success it moved.
COST = "text"

# The arm a cell is a difference against, where a block declares one; first name present wins.
# A block sweep has no control cell and its arms are read against each other. MODEL.md.
CONTROL = ("control", "off")

# The price side of an arm, for the blocks that hold delivery flat and differ only in spend.
# Read as a ratio: these span orders of magnitude. MODEL.md.
COSTS = ("advert_bytes", "sr_bytes", "sr_airtime", "bytes_on_air")

# What a success needs before it may rank a block. Two admin sessions make one failure a 50%
# swing; below the floor a measure is still reported, it just cannot rank. MODEL.md.
MIN_OBSERVATIONS = {"dm": 20, "admin": 20}
DENOMINATOR = {"dm": "dm_composed", "admin": "admin_sessions"}

# Cells differing by less than this on every recorded number are the same cell. Relative, and
# over every number rather than the displayed few - MODEL.md.
INERT_EPSILON = 1e-9

# A run discarding more than this share of its rebroadcast attempts is measuring its own backoff cap.
QUEUE_DROP_WARN = 0.10

# Not measurements: they restate the arm, name the draw, or time this machine. `value` was
# missing, which disabled the inert check for 40 of the 87 blocks - TRAPS 11.
NOT_A_MEASUREMENT = ("opts", "seed", "wall_seconds", "value")

# How far a block's runtime may drift from its own history before the digest says so. TRAPS.md #7 is
# a terrain index that was slower than the sort it replaced, and its entry reads "the data to compare
# against a previous run exists; nothing compares it yet" - this is that comparison.
#
# Compared as **wall-clock seconds per simulated hour**, never as the raw `wall_seconds` sum. The sum
# moves whenever the seed count or `--hours` moves, so gating on it would fire on every block the
# next time either is retuned and teach everyone to ignore the gate. The rate is invariant to both.
#
# Warn, never fatal, and generously wide: a hosted runner is shared hardware and a 30-40% swing
# between two identical runs is ordinary. What this is for is the 4x kind - an optimisation that cost
# more than it saved - which a hard `timeout-minutes` only catches once it has grown enough to fail a
# job outright, long after the commit that caused it.
# Every kind of flag this module raises, as a vocabulary rather than a prose prefix. A flag is
# recorded twice over: as the sentence a reader wants (`flags`) and as its kind (`flag_kinds`), so the
# run-health page can group and count them without parsing the sentence back apart. Held to this set
# by test_collate, so a new check cannot invent a kind that nothing renders.
FLAG_KINDS = (
    "chutil-impossible",  # fatal: a node busier than all the time
    "no-ground",  # fatal: --scenario asked for, none recorded
    "silent-loss",  # fatal: a checksum closed over two unequal sets
    "audit-disagrees",  # fatal: the at-rest audit contradicts the checksum
    "no-terrain",  # ground recorded, no terrain applied
    "beyond-envelope",  # pairs outside the fitted budget, on the raw one instead
    "placement-capped",  # a role-bounded placement gave fewer archives than asked
    "queue-drops",  # airtime measured through a backoff cap
    "sketch-failures",  # misdecodes or decode failures
    "inert",  # every value of the arm produced identical numbers
    "slower",  # runtime drifted up against this block's own history
    "faster",  # runtime drifted down, which is not automatically good news
)

TIMING_DRIFT_FACTOR = 2.0
# Below this many prior observations there is no median worth the name, and a first run has none at
# all. A block new to the archive is silently ungated rather than compared against nothing.
TIMING_MIN_HISTORY = 2


def load_block(path):
    """Every cell report in one block file, as written by sweep.run_block."""
    with open(path) as f:
        data = json.load(f)
    return data if isinstance(data, list) else [data]


def admin_success_rate(admin):
    """One admin figure across every hop distance probed, weighted by sessions attempted.

    Averaging the rates would weight two sessions the same as fifty.
    """
    if not isinstance(admin, dict):
        return None
    sessions = admin_sessions(admin)
    completed = sum((v or {}).get("session_completed", 0) for v in admin.values())
    return round(completed / sessions, 4) if sessions else None


def admin_sessions(admin):
    """Sessions the operator wanted, across every hop distance - the admin measure's denominator."""
    if not isinstance(admin, dict):
        return None
    return sum((v or {}).get("sessions", 0) for v in admin.values()) or None


# campaign._dist's six. A mean alone hides the tail, and the tail is the point: on a stretched mesh
# the worst-served node is the one the archive exists for.
DIST_KEYS = ("min", "p10", "median", "mean", "p90", "max")


def distributions(report):
    """Every `_dist` block in a report, keyed by its dotted path.

    Found by shape, not by a list of paths. The six keys are `_dist`'s signature, and five of the
    twelve are `by_class.<class>.per_node_reception` - keyed by a class name, so any hand-written
    list would have to be reissued whenever a class or a report section was added. `metric()` reads
    single numbers and returns None for a dict, which is where these used to stop.
    """
    out = {}

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if all(k in node for k in DIST_KEYS):
            out[".".join(path)] = {k: node[k] for k in DIST_KEYS}
            return  # a distribution has no distributions inside it
        for key, value in node.items():
            walk(value, path + [key])

    walk(report, [])
    return out


def mean_distributions(reports):
    """One distribution per path, each statistic meaned over the seeds that carry it.

    Meaned the same way `metrics` is, and for the same reason: a cell is its seeds together. A path
    absent from some seeds is meaned over the ones that have it rather than being dropped.
    """
    seen = {}
    for report in reports:
        for path, dist in distributions(report).items():
            seen.setdefault(path, []).append(dist)
    out = {}
    for path, dists in seen.items():
        row = {}
        for key in DIST_KEYS:
            values = [d[key] for d in dists if d.get(key) is not None]
            if values:
                row[key] = round(sum(values) / len(values), 4)
        if row:
            out[path] = row
    return out


def derived(report):
    """Compute the figures that are not read straight out of the report.

    `nodes` comes from the mesh that was built, not from --nodes - TRAPS 9.
    """
    ground = report.get("ground") or {}
    mesh = report.get("mesh") or {}
    nodes = ground.get("nodes") if ground.get("fixed_geometry") else None
    return {"nodes": nodes or mesh.get("nodes")}


def metric(report, key):
    """One metric out of a report by its declared path, or None where the section does not exist."""
    path = METRICS[key]
    if path[0] == "_derived":
        return derived(report).get(path[1])
    if path == ("admin", "_success_rate"):
        return admin_success_rate(report.get("admin"))
    if path == ("admin", "_sessions"):
        return admin_sessions(report.get("admin"))
    node = report
    for step in path:
        if not isinstance(node, dict):
            return None
        node = node.get(step)
    return node if not isinstance(node, (dict, list)) else None


def _mean(values):
    present = [v for v in values if v is not None]
    return statistics.mean(present) if present else None


def _sd(values):
    present = [v for v in values if v is not None]
    return statistics.stdev(present) if len(present) > 1 else None


def group_by_value(reports):
    """{arm value: [report per seed]}, in the order the block declares its values."""
    grouped = {}
    for r in reports:
        grouped.setdefault(str(r.get("value", "-")), []).append(r)
    return grouped


def per_node_of(report):
    """Each class's per-node reach vector from one report, or nothing when it kept none.

    One seed's own node order, so it is taken from a single report and never averaged: node 7 of one
    seed is a different node from node 7 of the next, and a mean over them would be a fiction with a
    plausible shape.
    """
    out = {}
    for name, row in (report.get("by_class") or {}).items():
        vector = row.get("per_node")
        if vector:
            out[name] = vector
    return out


def map_of(report, registry):
    """This report's mesh map as a reference into `registry`, or nothing when it carried none.

    The geometry is entered once under the hash of its own contents, because a sweep changing what
    nodes *do* leaves the radio picture identical: across one Batumi batch 102 of 123 cells shared a
    single topology, so storing one per cell would be the same 17 kB written a hundred times.
    """
    got = report.get("mesh_map") or {}
    geometry, overlay = got.get("geometry"), got.get("overlay")
    if not geometry or not overlay:
        return None
    blob = json.dumps(geometry, separators=(",", ":"), sort_keys=True)
    key = hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]
    registry.setdefault(key, geometry)
    return {"geom": key, "overlay": overlay, "seed": report.get("seed")}


def cells_of(reports, per_node=False, maps=None):
    """One entry per arm value, averaged over whatever seeds the run drew for it.

    Grouped on the requested value; `placement_capped` records where the achieved one differs.
    """
    grouped = group_by_value(reports)
    cells = []
    for value, group in grouped.items():
        cell = {
            "value": value,
            "seeds": [g.get("seed") for g in group],
            "metrics": {k: _mean([metric(g, k) for g in group]) for k in METRICS},
            # The six-number distributions behind the single numbers above. The digest is the only
            # thing the rolling page reads, so a statistic that stops here is one nothing can ever
            # show - and unlike a figure it cannot be regenerated once the raw run is dropped.
            "dist": mean_distributions(group),
        }
        # Opt-in: one vector per class per cell is small for one run and 30 MB across a season of
        # them, and the scheduled page is rolled from these digests.
        if per_node:
            vectors = per_node_of(group[0])
            if vectors:
                cell["per_node"] = vectors
                cell["per_node_seed"] = group[0].get("seed")
        # One seed's geometry, for the same reason per_node takes one: node indices belong to a
        # single run, and a mean over two seeds' positions would draw a mesh that never existed.
        if maps is not None:
            reference = map_of(group[0], maps)
            if reference:
                cell["map"] = reference
        # Only when a value was run more than once - a single-seed run has no spread, and writing
        # 0.0 there would let the explorer average a fiction into a real one later.
        spread = {k: _sd([metric(g, k) for g in group]) for k in METRICS}
        cell["sd"] = {k: v for k, v in spread.items() if v is not None}
        cells.append(cell)
    return cells


def _ratio(cells, key):
    """How many times over the largest cell exceeds the smallest, or None if that cannot be read."""
    values = [c["metrics"].get(key) for c in cells]
    present = [v for v in values if v is not None and v > 0]
    if len(present) < 2 or len(present) != len(values):
        return None
    return max(present) / min(present)


def against_control(cells):
    """Each cell's difference from the block's control arm, where there is one.

    A difference, not a ratio: these are shares. The control keeps a row of its own reading zero.
    """
    control = next(
        (c for name in CONTROL for c in cells if c["value"] == name),
        None,
    )
    if control is None:
        return
    for cell in cells:
        cell["vs_control"] = {
            k: cell["metrics"][k] - control["metrics"][k]
            for k in SUCCESSES + (COST,)
            if cell["metrics"].get(k) is not None
            and control["metrics"].get(k) is not None
        }


def _effect(cells, key):
    """Spread of one metric across an arm: (low, high, high - low), or None if nothing was recorded."""
    values = [c["metrics"].get(key) for c in cells]
    present = [v for v in values if v is not None]
    if len(present) < 2:
        return None
    return min(present), max(present), max(present) - min(present)


def numeric_leaves(obj, prefix=""):
    """Every number anywhere in a report, keyed by its path. Bools are labels, not measurements."""
    found = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            found.update(numeric_leaves(v, f"{prefix}/{k}"))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            found.update(numeric_leaves(v, f"{prefix}[{i}]"))
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        found[prefix] = obj
    return found


def _inert(grouped):
    """Report whether no number anywhere in the reports distinguishes any two arm values.

    Compared through their means over seeds, so seed count does not change the verdict.
    """
    if len(grouped) < 2:
        return False
    per_value = []
    for reports in grouped.values():
        leaves = [
            numeric_leaves({k: v for k, v in r.items() if k not in NOT_A_MEASUREMENT})
            for r in reports
        ]
        keys = set().union(*leaves) if leaves else set()
        per_value.append({k: _mean([leaf.get(k) for leaf in leaves]) for k in keys})
    for key in set().union(*per_value):
        values = [v.get(key) for v in per_value]
        present = [v for v in values if v is not None]
        if len(present) < 2:
            # A number one arm value records and another does not is itself a difference.
            if len(present) != len(values):
                return False
            continue
        scale = max(abs(min(present)), abs(max(present)), 1.0)
        if (max(present) - min(present)) / scale > INERT_EPSILON:
            return False
    return True


def check_cell(report, where):
    """Apply the per-run gates, returning (fatal, warnings) as (kind, sentence) pairs.

    One per defect in TRAPS.md, each of which was found by accident the first time.
    """
    fatal, warn = [], []
    opts = report.get("opts") or {}
    sfpp = report.get("sfpp") or {}
    traffic = report.get("traffic") or {}
    ground = report.get("ground")

    # A radio has one energy detector, so overlapping signals are one busy stretch. Charging each
    # audible transmission its full airtime ran this to 184% of wall-clock. Physical invariant.
    chutil = (traffic.get("node_channel_util_percent") or {}).get("max")
    if chutil is not None and chutil > 100:
        fatal.append(
            (
                "chutil-impossible",
                f"{where}: node channel utilisation {chutil:.1f}% exceeds 100 - physically impossible",
            )
        )

    # A Scenario with no nodes was falsy, so `if scenario:` was False and the run came out flat
    # while the label said alpine. No error, a plausible number, a wrong label.
    if opts.get("scenario") and not ground:
        fatal.append(
            (
                "no-ground",
                f"{where}: --scenario {opts['scenario']} was asked for and the run recorded no ground",
            )
        )
    if (
        opts.get("scenario")
        and ground
        and not (ground.get("terrain_applied") or ground.get("fixed_geometry"))
    ):
        warn.append(
            (
                "no-terrain",
                f"{where}: --scenario {opts['scenario']} recorded ground but applied no terrain",
            )
        )

    # The design-falsifying counters. A run with a good reception figure and a non-zero silent-loss
    # count is not a good run.
    if sfpp.get("silent_losses"):
        fatal.append(
            (
                "silent-loss",
                f"{where}: SILENT LOSSES {sfpp['silent_losses']:g} - a checksum closed over two unequal sets",
            )
        )
    if sfpp.get("audit_checksum_agrees_sets_differ"):
        fatal.append(
            (
                "audit-disagrees",
                f"{where}: at-rest audit disagrees with the checksum in "
                f"{sfpp['audit_checksum_agrees_sets_differ']:g} case(s)",
            )
        )

    # A fit answers any input, including ones it has never seen. Its elevation terms are positive and
    # unbounded against a log-distance penalty, so past the observed range it invents links.
    if (
        ground
        and ground.get("link_calibration_loaded")
        and ground.get("pairs_beyond_calibration")
    ):
        envelope = ground.get("calibration_envelope_m")
        warn.append(
            (
                "beyond-envelope",
                f"{where}: {ground['pairs_beyond_calibration']} pair(s) beyond the fit's "
                f"{envelope / 1000:.1f} km envelope - those fell back to the raw budget"
                if envelope
                else f"{where}: {ground['pairs_beyond_calibration']} pair(s) beyond the fit's envelope",
            )
        )

    # Role-bounded placements cap at the mesh's router count and repeat above it, so two rows of a
    # --servers sweep can silently be the same run.
    req, placed = sfpp.get("servers_requested"), sfpp.get("servers_placed")
    if req is not None and placed is not None and req != placed:
        warn.append(
            (
                "placement-capped",
                f"{where}: {req} archives requested, {placed} placed - group on the placed count",
            )
        )

    # A backoff cap discarding rebroadcasts rescales every airtime figure in the run.
    tx, drops = traffic.get("transmissions"), traffic.get("queue_drops")
    if tx and drops and drops / tx > QUEUE_DROP_WARN:
        warn.append(
            (
                "queue-drops",
                f"{where}: queue drops {drops / tx:.1%} of transmissions - airtime here is measured through a cap",
            )
        )

    for counter in ("misdecodes", "decode_failures"):
        if sfpp.get(counter):
            warn.append(("sketch-failures", f"{where}: {counter} {sfpp[counter]:g}"))
    return fatal, warn


def _has_denominator(cells, key):
    """Whether a success was observed often enough for its spread to mean anything."""
    floor = MIN_OBSERVATIONS.get(key)
    if floor is None:
        return True
    counts = [c["metrics"].get(DENOMINATOR[key]) for c in cells]
    present = [c for c in counts if c is not None]
    return bool(present) and min(present) >= floor


def describe(block):
    """Return what this block changes, in one sentence, or None if no producer declares it.

    Three producers asked in turn, imported lazily so a digest collates from run JSONs alone.
    """
    try:
        from .sweep import DESCRIPTIONS

        if block in DESCRIPTIONS:
            return DESCRIPTIONS[block]
    except ImportError:
        pass
    for module in ("design", "matrix"):
        try:
            producer = __import__(f"{__package__}.{module}", fromlist=["describes"])
            found = producer.describes().get(block)
        except ImportError:
            continue
        if found:
            return found
    return None


def _sim_hours(reports):
    """Total simulated hours across these cells, or None if any cell does not say.

    Summed, not assumed constant: a block sweeping --hours would report every other arm as a regression.
    """
    total = 0.0
    for r in reports:
        hours = (r.get("opts") or {}).get("hours")
        if not hours:
            return None
        total += float(hours)
    return total or None


def _seconds_per_sim_hour(reports):
    """Wall-clock seconds spent per simulated hour - the one timing figure comparable across runs."""
    hours = _sim_hours(reports)
    if not hours:
        return None
    wall = sum(r.get("wall_seconds") or 0 for r in reports)
    return round(wall / hours, 4) if wall else None


# A block name arrives from a digest, and a digest arrives from a git branch that more than one
# person can write to. It is used two ways, and both are dangerous unescaped: as a path component
# (`figures/<block>.svg`, `reports/<block>.txt`, `<block>.json`) and as page content. Escaping covers
# the second - `_esc` on every display path, \u escapes inside the JSON blob - and this covers the
# first. Anything outside the set becomes a dash, so a hostile name is inert rather than rejected:
# the numbers in that block are still worth rolling up.
SAFE_NAME_CHARS = set(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_."
)
SAFE_NAME_MAX = 96
# Windows keeps these as device names whatever the extension, so `figures/CON.svg` is not a file
# there. Guarded even though the runners are Linux: a report directory gets copied about.
RESERVED_STEMS = (
    {"CON", "PRN", "AUX", "NUL"}
    | {f"COM{i}" for i in range(1, 10)}
    | {f"LPT{i}" for i in range(1, 10)}
)


def safe_name(name, fallback="block"):
    """`name` reduced to something that can only ever be one path component, and only ever its own.

    Separators, parent references, control characters and the rest become dashes, so a name like
    `../../etc/passwd` addresses a file called `-..-etc-passwd` inside the directory that was asked
    for and nothing outside it. Leading and trailing dots go too: `..` must not survive as a prefix,
    and Windows drops a trailing one, which would quietly merge two names into one file.

    Anything that had to be changed also carries a digest of the original, because cleaning alone is
    not injective: `a/b`, `a\\b` and a legitimate `a-b` all clean to `a-b`, and one block's report
    would then overwrite another's - or a hostile name could aim at a real block's figure on purpose.
    Truncation collides the same way and is covered by the same suffix.
    """
    raw = str(name)
    cleaned = "".join(c if c in SAFE_NAME_CHARS else "-" for c in raw)[:SAFE_NAME_MAX]
    cleaned = cleaned.strip(".")
    stem = cleaned or fallback
    if stem != raw or stem.upper() in RESERVED_STEMS:
        digest = hashlib.sha256(raw.encode("utf-8", "surrogatepass")).hexdigest()[:6]
        stem = f"{stem[: SAFE_NAME_MAX - 7]}-{digest}"
    return stem


def is_safe_name(name):
    """Whether `name` is already usable as a path component, for a caller that wants to say so."""
    return safe_name(name) == str(name)


def load_history(archive_dir, exclude_run_id=None):
    """{block name: [seconds_per_sim_hour, ...]} from every prior digest in the archive.

    Digests, not raw JSONs, which are pruned; an unparseable one is skipped rather than fatal.
    """
    history = {}
    if not archive_dir or not os.path.isdir(archive_dir):
        return history
    for path in sorted(glob.glob(os.path.join(archive_dir, "*", "summary.json"))):
        try:
            with open(path) as f:
                prior = json.load(f)
        except (OSError, ValueError):
            continue
        # A re-collate of the run in flight would otherwise compare it against itself and never drift.
        if exclude_run_id and prior.get("run_id") == exclude_run_id:
            continue
        for block in prior.get("blocks") or []:
            rate = block.get("seconds_per_sim_hour")
            if isinstance(rate, (int, float)) and rate > 0:
                history.setdefault(block.get("block"), []).append(float(rate))
    return history


def check_timing(blocks, history):
    """Flag a block whose seconds-per-simulated-hour has drifted from its own past. Warn only.

    Both directions: faster usually means less work was done, not that anything was optimised.
    """
    for block in blocks:
        rate = block.get("seconds_per_sim_hour")
        past = history.get(block["block"]) or []
        if not rate or len(past) < TIMING_MIN_HISTORY:
            continue
        median = statistics.median(past)
        if not median:
            continue
        block["timing"] = {
            "seconds_per_sim_hour": rate,
            "median": round(median, 4),
            "ratio": round(rate / median, 3),
            "runs_compared": len(past),
        }
        if rate > median * TIMING_DRIFT_FACTOR:
            add_flag(
                block,
                "slower",
                f"slower: {rate:.3g} s per simulated hour against {median:.3g} over "
                f"{len(past)} prior run(s) - {rate / median:.1f}x, and a runtime regression is "
                f"invisible to `timeout-minutes` until it fails a job outright",
            )
        elif rate * TIMING_DRIFT_FACTOR < median:
            add_flag(
                block,
                "faster",
                f"faster: {rate:.3g} s per simulated hour against {median:.3g} over "
                f"{len(past)} prior run(s) - {median / rate:.1f}x quicker, which is worth a look: "
                f"a fragmented mesh or an arm that stopped being read both cost less to simulate",
            )


def summarise_block(reports, per_node=False, maps=None):
    first = reports[0]
    cells = cells_of(reports, per_node=per_node, maps=maps)
    against_control(cells)
    block = {
        "block": first.get("block", "?"),
        "arm": first.get("arm", "?"),
        "grid": first.get("grid") or [],
        "transport": first.get("transport"),
        "sim_version": first.get("sim_version"),
        "cells": cells,
        "wall_seconds": sum(r.get("wall_seconds") or 0 for r in reports),
        # The comparable form of the above: wall_seconds sums over however many cells, seeds and
        # hours this block ran, so both have to be divided out. See TIMING_DRIFT_FACTOR.
        "runs": len(reports),
        "sim_hours": _sim_hours(reports),
        "seconds_per_sim_hour": _seconds_per_sim_hour(reports),
        "nodes": metric(first, "nodes"),
        "explains": describe(first.get("block", "?")),
        "scenario": (first.get("opts") or {}).get("scenario"),
        "mirror": (first.get("opts") or {}).get("mirror"),
        "effect": {},
        "moved": None,
        "cost": None,
        "flags": [],
        "fatal": [],
    }
    for key in SUCCESSES + (COST,):
        eff = _effect(cells, key)
        if eff:
            block["effect"][key] = {"low": eff[0], "high": eff[1], "spread": eff[2]}
    # What the arm costs, whatever it does to delivery. Reported for every block, because a flat
    # delivery row with a 5.7x byte ratio is a result rather than an absence of one.
    priced = [(k, _ratio(cells, k)) for k in COSTS]
    priced = [(k, r) for k, r in priced if r is not None and r > 1.0001]
    if priced:
        # Not `metric, ratio = ...`: that binds a local named `metric` for the whole function and
        # shadows the module-level metric() this function calls a few lines above.
        dearest = max(priced, key=lambda kv: kv[1])
        block["cost"] = {"metric": dearest[0], "ratio": dearest[1]}

    # Which success this arm actually moves, excluding any whose denominator is too small to
    # mean anything - or the leaderboard fills with two-session admin noise.
    block["thin"] = sorted(
        k for k in SUCCESSES if k in block["effect"] and not _has_denominator(cells, k)
    )
    # A spread of zero is not a movement: without this, identical cells reported
    # `moved: text, spread 0.000`, which reads as a finding and is the opposite of one.
    moved = [
        (k, v["spread"])
        for k, v in block["effect"].items()
        if k in SUCCESSES and k not in block["thin"] and v["spread"] > INERT_EPSILON
    ]
    if moved:
        block["moved"] = max(moved, key=lambda kv: kv[1])[0]

    if _inert(group_by_value(reports)):
        block["flags"].append(
            (
                "inert",
                f"inert: every value of `{block['arm']}` produced identical numbers - "
                "either the flag is not read, or it needs a second flag before it does anything "
                "(README §10.4)",
            )
        )
    for r in reports:
        fatal, warn = check_cell(r, f"{block['arm']}={r.get('value')}")
        block["fatal"] += fatal
        block["flags"] += warn
    _settle_flags(block)
    return block


def add_flag(block, kind, text):
    """Record one flag on an already-summarised block, keeping `flags` and `flag_kinds` in step.

    Needed because the timing check runs after summarise_block, once every block is known.
    """
    block.setdefault("flags", []).append(text)
    kinds = block.setdefault("flag_kinds", {})
    kinds[kind] = kinds.get(kind, 0) + 1
    block["flag_kinds"] = dict(sorted(kinds.items()))


def _settle_flags(block):
    """Turn the (kind, sentence) pairs collected above into what the digest publishes.

    Sentences stay sentences and the kinds go beside them, counted - MODEL.md.
    """
    for field in ("flags", "fatal"):
        kinds, sentences = [], []
        for entry in block[field]:
            if isinstance(entry, tuple):
                kind, text = entry
            else:
                kind, text = "unclassified", entry
            kinds.append(kind)
            sentences.append(text)
        block[field] = sentences
        counts = {}
        for kind in kinds:
            counts[kind] = counts.get(kind, 0) + 1
        block["fatal_kinds" if field == "fatal" else "flag_kinds"] = dict(
            sorted(counts.items())
        )


def collate(
    runs_dir,
    run_id=None,
    seed_base=None,
    scenario=None,
    expected=None,
    history_dir=None,
    per_node=False,
    maps=False,
):
    # On the `block` field, not one block per file: a sharded cell uploads a file per seed, and
    # reading per file would average nothing and enter the block three times.
    by_block = {}
    for path in sorted(glob.glob(os.path.join(runs_dir, "*.json"))):
        # summary.json is this module's own output; a re-collate must not read it back in as a block.
        if os.path.basename(path) == "summary.json":
            continue
        for report in load_block(path):
            if "block" in report:
                by_block.setdefault(report["block"], []).append(report)
    unsafe = sorted(name for name in by_block if not is_safe_name(name))
    if unsafe:
        # Not dropped: the measurements are still measurements. Named, because a block whose name
        # is a path is not something sweep.py or a batch runner produces.
        print(
            f"WARNING: {len(unsafe)} block name(s) are not usable as a path and will be "
            f"sanitised wherever one is needed: {', '.join(repr(n) for n in unsafe)}"
        )
    registry = {} if maps else None
    blocks = [
        summarise_block(reports, per_node=per_node, maps=registry)
        for reports in by_block.values()
    ]
    # Against this block's own past, not against a figure written into a comment once. Skipped
    # entirely when no archive is given, so a local collate of one run behaves exactly as before.
    check_timing(blocks, load_history(history_dir, exclude_run_id=run_id))

    present = {b["block"] for b in blocks}
    missing = sorted(set(expected) - present) if expected else []
    transports = sorted({b["transport"] for b in blocks if b.get("transport")})
    # More than one means the round straddles a behaviour change, and its blocks are not comparable
    # with each other. Named rather than averaged away - see sfpp/version.py.
    versions = sorted({b["sim_version"] for b in blocks if b.get("sim_version")})
    scenarios = sorted({b["scenario"] for b in blocks if b.get("scenario")})
    seeds = sorted(
        {s for b in blocks for c in b["cells"] for s in c["seeds"] if s is not None}
    )

    return {
        "run_id": run_id or datetime.date.today().isoformat(),
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(
            timespec="seconds"
        ),
        "seed_base": seed_base,
        "seeds": seeds,
        # What was asked for, and what the reports say happened. They differ when a block refuses a
        # scenario, and a digest that only recorded the request would hide that.
        "scenario_requested": scenario,
        "scenario_observed": scenarios,
        "transport": transports[0] if len(transports) == 1 else transports,
        "sim_version": versions[0] if len(versions) == 1 else versions,
        "blocks": sorted(blocks, key=lambda b: b["block"]),
        "missing_blocks": missing,
        "wall_seconds": sum(b["wall_seconds"] for b in blocks),
        "gate": gate(blocks, missing),
        # Deduplicated geometry, referenced by the cells that share it. Absent unless --maps, so a
        # digest that nobody draws a map from stays the size it was.
        **({"maps": registry} if registry else {}),
    }


def gate(blocks, missing):
    """Judge the run. Only the design-falsifying and physically impossible are fatal."""
    failures = [f"{b['block']}: {f}" for b in blocks for f in b["fatal"]]
    warnings = [f"{b['block']}: {f}" for b in blocks for f in b["flags"]]
    # Counted by kind and by how many blocks each touched: 400 envelope warnings and one inert
    # is not the same run as the reverse, though both are 401 sentences.
    by_kind = {}
    for b in blocks:
        for kind, count in (b.get("flag_kinds") or {}).items():
            entry = by_kind.setdefault(kind, {"flags": 0, "blocks": 0})
            entry["flags"] += count
            entry["blocks"] += 1
    # A round assembled from two behaviours is a round whose blocks cannot be read against each
    # other, and nothing else in the digest would say so.
    versions = sorted({b["sim_version"] for b in blocks if b.get("sim_version")})
    if len(versions) > 1:
        warnings.insert(
            0,
            f"mixed sim versions in one round: {', '.join(versions)} - blocks from different "
            f"versions are not comparable with each other (see sfpp/version.py)",
        )
    return {
        "ok": not failures,
        "failures": failures,
        "warnings": warnings,
        "warnings_by_kind": dict(sorted(by_kind.items())),
        "blocks_run": len(blocks),
        "blocks_missing": len(missing),
    }


def _fmt(v, places=3):
    if v is None:
        return "-"
    if isinstance(v, float) and abs(v) < 1000:
        return f"{v:.{places}f}"
    return f"{v:,.0f}"


def _arrow(cells, key):
    """Which end of the arm the metric prefers, read in the order the block declares its values."""
    values = [c["metrics"].get(key) for c in cells]
    present = [v for v in values if v is not None]
    if len(present) < 2:
        return " "
    if abs(present[-1] - present[0]) < INERT_EPSILON:
        return "="
    return "up" if present[-1] > present[0] else "down"


def _price(block):
    """Render the largest cost ratio across the arm, as `5.7x advert_bytes`, or a dash."""
    cost = block.get("cost")
    return f"{cost['ratio']:.2g}x {cost['metric']}" if cost else "-"


def markdown(summary):
    run_scenario = summary.get("scenario_requested") or "flat"
    gates = summary["gate"]
    out = [
        f"# Sweep {summary['run_id']}",
        "",
        f"- **sim version** `{summary.get('sim_version') or 'unversioned'}`",
        f"- **transport** `{summary['transport']}`",
        f"- **ground** {run_scenario}",
        f"- **seed base** {summary.get('seed_base') or 'drawn per block'}"
        + (
            f" · seeds {', '.join(str(s) for s in summary['seeds'][:8])}"
            if summary["seeds"]
            else ""
        ),
        f"- **blocks** {gates['blocks_run']} run"
        + (f", {gates['blocks_missing']} missing" if summary["missing_blocks"] else ""),
        f"- **compute** {summary['wall_seconds'] / 3600:.1f} h of simulator time across every cell",
        f"- **generated** {summary['generated']}",
        "",
        "## Gates" if not gates["ok"] else "## Gates - held",
        "",
    ]
    if gates["failures"]:
        out += [
            "**A fatal gate failed. Nothing else in this run should be read until it is explained** - "
            "these are the design-falsifying and physically impossible counters, not bad numbers.",
            "",
        ]
        out += [f"- FAIL {f}" for f in gates["failures"]]
        out.append("")
    else:
        out += [
            "- OK `silent_losses` and the at-rest audit are zero in every cell",
            "- OK no node reports channel utilisation above 100%",
            "- OK every run that asked for ground recorded some",
            "",
        ]
    if gates["warnings"]:
        out += [
            "<details><summary>" + f"{len(gates['warnings'])} warnings</summary>",
            "",
        ]
        out += [f"- {w}" for w in gates["warnings"]]
        out += ["", "</details>", ""]
    if summary["missing_blocks"]:
        out += [
            "Blocks that produced no JSON (their job failed, timed out, or was cancelled): "
            + ", ".join(f"`{b}`" for b in summary["missing_blocks"]),
            "",
        ]

    # Runtime against this block's own past, as a rate: a total moves whenever the seed count
    # or --hours does, and would read as a regression every time either is retuned.
    drifted = sorted(
        (b for b in summary["blocks"] if b.get("timing")),
        key=lambda b: b["timing"]["ratio"],
        reverse=True,
    )
    drifted = [b for b in drifted if b["timing"]["ratio"] >= 1.5 or b["timing"]["ratio"] <= 0.67]
    if drifted:
        out += [
            "## Runtime against this block's own history",
            "",
            "Wall-clock seconds per **simulated** hour, against the median of the same block's prior "
            "runs in this archive. Normalised because the raw total moves with the seed count and "
            "`--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise "
            f"and the flagged ones (past {TIMING_DRIFT_FACTOR:g}x either way) as worth a look.",
            "",
            "| block | s/sim-h | median | ratio | runs compared |",
            "| --- | --: | --: | --: | --: |",
        ]
        for b in drifted:
            t = b["timing"]
            out.append(
                f"| `{b['block']}` | {t['seconds_per_sim_hour']:.3g} | {t['median']:.3g} | "
                f"{t['ratio']:.2f}x | {t['runs_compared']} |"
            )
        out.append("")

    # The trend proper: which variables move a delivery measure at all, largest first. A reader who
    # stops after this table has the run's answer; everything below is the working.
    ranked = sorted(
        (b for b in summary["blocks"] if b["moved"]),
        key=lambda b: b["effect"][b["moved"]]["spread"],
        reverse=True,
    )
    out += [
        "## What moved a delivery measure",
        "",
        "Ranked by how far the arm moves whichever success it moves most. The four measures have "
        "four denominators and are **not comparable to each other** (README §7.3) - `moved` names "
        "which one this block travels in. `text` is the broadcast reach in the same cells, so an arm "
        "buying its measure while `text` falls is paying in the currency the mesh exists to spend.",
        "",
        "| block | arm | moved | low → high | spread | text | price | dir | cells |",
        "| --- | --- | --- | --- | --: | --- | --- | :-: | --: |",
    ]
    for b in ranked:
        eff = b["effect"][b["moved"]]
        cost = b["effect"].get(COST)
        out.append(
            f"| `{b['block']}` | {b['arm']} | **{b['moved']}** | "
            f"{_fmt(eff['low'])} → {_fmt(eff['high'])} | {_fmt(eff['spread'])} | "
            f"{_fmt(cost['low']) + ' → ' + _fmt(cost['high']) if cost else '-'} | "
            f"{_price(b)} | "
            f"{_arrow(b['cells'], b['moved'])} | {len(b['cells'])} |"
        )
    thin = sorted({m for b in summary["blocks"] for m in b.get("thin", [])})
    if thin:
        out += [
            "",
            f"Not ranked on for want of observations: {', '.join(f'`{m}`' for m in thin)} in some "
            f"blocks. A measure needs {min(MIN_OBSERVATIONS.values())} observations before an arm may "
            "be ranked on it; the figures are still in the per-block tables.",
        ]
    flat = [b for b in summary["blocks"] if not b["moved"]]
    if flat:
        out += [
            "",
            "### Moved no delivery measure",
            "",
            "Not the same as having done nothing: several arms hold delivery flat by design and "
            "differ in what they spend. Three ways of reconciling the same two sets had better "
            "agree on what is held; where they differ is the price.",
            "",
            "| block | arm | price | cells |",
            "| --- | --- | --- | --: |",
        ]
        for b in flat:
            out.append(
                f"| `{b['block']}` | {b['arm']} | {_price(b)} | {len(b['cells'])} |"
            )

    out += ["", "## Every block", ""]
    for b in summary["blocks"]:
        grid = " ".join(b["grid"])
        out += [
            f"### `{b['block']}` - {b['arm']}" + (f"  `{grid}`" if grid else ""),
            "",
        ]
        if b.get("explains"):
            out += [f"*{b['explains']}*", ""]
        out += [
            "| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |",
            "| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |",
        ]
        for c in b["cells"]:
            m = c["metrics"]
            out.append(
                f"| {c['value']} | {_fmt(m.get('text'))} | {_fmt(m.get('dm'))} | "
                f"{_fmt(m.get('admin'))} | {_fmt(m.get('held'))} | {_fmt(m.get('union'))} | "
                f"{_fmt(m.get('text_worst'))} | {_fmt(m.get('demand'), 2)}x | "
                f"{_fmt(m.get('chutil_p90'), 1)}/{_fmt(m.get('chutil_max'), 1)}% | "
                f"{_fmt(m.get('airutil_max'), 1)}% | {_fmt(m.get('servers_placed'), 0)} |"
            )
        for f in b["fatal"]:
            out.append(f"\n> FAIL {f}")
        for f in b["flags"]:
            out.append(f"\n> {f}")
        out.append("")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="reduce one scheduled sweep to a digest and a trend report"
    )
    ap.add_argument(
        "--runs", required=True, help="directory of block JSONs written by sfpp.sweep"
    )
    ap.add_argument(
        "--out", help="where to write summary.json and trend.md (default: --runs)"
    )
    ap.add_argument(
        "--run-id", help="names the run in the digest and the explorer; default today"
    )
    ap.add_argument("--seed-base", help="recorded so the run can be replayed exactly")
    ap.add_argument(
        "--scenario",
        help="the ground this run asked for, recorded alongside what it observed",
    )
    ap.add_argument(
        "--expect-all-blocks",
        action="store_true",
        help="treat sweep.BLOCKS as the expected set, so a block whose job failed is named rather than missed",
    )
    ap.add_argument(
        "--expect",
        help="space-separated block names this run asked for. Narrower than --expect-all-blocks, "
        "which would report every block a partial run never asked for as missing",
    )
    ap.add_argument(
        "--history",
        help="archive of prior run directories (each holding a summary.json), so a block's runtime "
        "is compared against its own past. Omit to skip the timing comparison entirely",
    )
    ap.add_argument(
        "--per-node",
        action="store_true",
        help="carry each class's per-node reach vector into the digest, for the meshes small enough "
        "to read node by node (the run keeps one up to 256 nodes). Off by default: a vector per "
        "class per cell is nothing for one run and tens of megabytes across a season of scheduled "
        "ones, and this digest is what the rolling page is built from",
    )
    ap.add_argument(
        "--maps",
        action="store_true",
        help="carry each cell's mesh as points and links, so the page can draw the map instead of "
        "linking an SVG that lives beside the block JSONs the archive is free to drop. Geometry is "
        "shared between cells that have the same one, which in practice is most of a batch",
    )
    ap.add_argument(
        "--fail-on-gate",
        action="store_true",
        help="exit non-zero when a fatal gate failed",
    )
    opts = ap.parse_args(argv)

    expected = set(opts.expect.split()) if opts.expect else None
    if expected is None and opts.expect_all_blocks:
        from .sweep import BLOCKS

        expected = set(BLOCKS)

    summary = collate(
        opts.runs,
        run_id=opts.run_id,
        seed_base=opts.seed_base,
        scenario=opts.scenario,
        expected=expected,
        history_dir=opts.history,
        per_node=opts.per_node,
        maps=opts.maps,
    )
    out_dir = opts.out or opts.runs
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1, sort_keys=True)
    with open(os.path.join(out_dir, "trend.md"), "w") as f:
        f.write(markdown(summary) + "\n")
    print(
        f"collated {summary['gate']['blocks_run']} blocks"
        + (
            f", {summary['gate']['blocks_missing']} missing"
            if summary["missing_blocks"]
            else ""
        )
        + f" -> {out_dir}/summary.json, {out_dir}/trend.md"
    )
    for f in summary["gate"]["failures"]:
        print(f"FAIL {f}")
    return 1 if opts.fail_on_gate and not summary["gate"]["ok"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
