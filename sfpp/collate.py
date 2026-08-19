r"""One scheduled sweep, read as a whole: what moved, what did nothing, and what must never happen.

`sweep.py` writes one JSON per block and prints a table per block. A scheduled run that covers every
block produces 87 of those, which is more than anyone reads, so nothing in them is looked at until
something has already gone wrong. This module reduces a whole run to two artefacts: `summary.json`,
the machine-readable digest the explorer rolls up across runs, and `trend.md`, the page a person
actually opens.

**Four measures of success, four denominators, not comparable to each other** (README §7.2). A
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
import json
import os
import statistics

# Everything the digest carries per cell, by path into a campaign report. A metric absent from a
# report - an older transport, a section that only exists under some flags - becomes None rather
# than raising, so a run assembled from mixed vintages still collates.
METRICS = {
    # --- the four successes. Different denominators; see the module docstring and README §7.2 ---
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

# The measures a block is ranked by. Whichever of them moves furthest across an arm decides where
# the block sits in the trend table, and the table names which one it was - because ranking every
# block by `held` alone would rate an arm that halves DM success as having done nothing.
SUCCESSES = ("text", "dm", "admin", "held")

# What an arm costs, read beside whichever success it moved.
COST = "text"

# The arm a cell is a difference against, where a block declares one. `design.py` puts a control in
# every cell - the archive `off` arm, the mesh as the firmware runs it - so each later arm is a
# difference on the same mesh at the same seed; a block sweep has no such cell and its arms are read
# against each other instead. First name present wins, so a block may declare either.
CONTROL = ("control", "off")

# The price side of an arm. Several blocks - reconciliation strategy, signing, advert transport -
# deliberately hold delivery flat and differ only in what they spend, and ranking those on delivery
# alone reports them as having done nothing. `D-resolve` is the case that made this obvious: enum
# advertises with a fifth of sketch's advert bytes and then pays two thirds more in total traffic,
# while held moves by 0.004. Cost is read as a ratio rather than a difference because these span
# orders of magnitude and "5.7x" is the readable figure where "11877 bytes" is not.
COSTS = ("advert_bytes", "sr_bytes", "sr_airtime", "bytes_on_air")

# How many observations a success needs before an arm may be ranked on it. Broadcast reach is
# measured over every node of every broadcast and always clears this; DM and admin have their own
# small denominators, and one admin probe an hour over two hours is two sessions - where a single
# failed session reads as a 50% swing and tops a leaderboard built from real effects. A measure
# below the floor is still reported, it just cannot decide where the block ranks.
MIN_OBSERVATIONS = {"dm": 20, "admin": 20}
DENOMINATOR = {"dm": "dm_composed", "admin": "admin_sessions"}

# Cells differing by less than this on every recorded number are treated as the same cell, which is
# how an inert arm is detected. Relative, because the numbers compared span reception fractions and
# byte counters in the millions; a flag that moves a counter by one part in a billion has not moved
# it. The first version of this check compared only the metrics this module displays and called
# `E-signed` inert - the arm moves `advert_bytes` by 43%, which was not among them. Hence: every
# number in the report, not a chosen few.
INERT_EPSILON = 1e-9

# A run discarding more than this share of its rebroadcast attempts is measuring its own backoff cap.
QUEUE_DROP_WARN = 0.10

# Not measurements: `opts` restates the arm's own setting, `seed` names the draw, and `wall_seconds`
# is how long this machine took - it differs between two identical cells and would make every block
# look live.
NOT_A_MEASUREMENT = ("opts", "seed", "wall_seconds")


def load_block(path):
    """Every cell report in one block file, as written by sweep.run_block."""
    with open(path) as f:
        data = json.load(f)
    return data if isinstance(data, list) else [data]


def admin_success_rate(admin):
    """One admin figure across every hop distance probed, weighted by sessions attempted.

    `admin` is keyed by hop separation and each entry has its own denominator. Averaging the rates
    would weight a distance with two sessions the same as one with fifty.
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


def derived(report):
    """Compute the figures that are not read straight out of the report.

    `nodes` is the one that has already caused a wrong conclusion: a fixed-geometry scenario decides
    its own node count and overrides `--nodes`, so the requested figure describes a mesh that was
    never built. Batumi is 92 whatever `--nodes` says.
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


def cells_of(reports):
    """One entry per arm value, averaged over whatever seeds the run drew for it.

    Grouped on the arm's value, not on `servers_placed` - but see `placement_capped` below: a
    role-bounded placement caps at the mesh's router count, so two rows of a `--servers` sweep can be
    the same run. The digest records both figures so a reader can group on the achieved one.
    """
    grouped = group_by_value(reports)
    cells = []
    for value, group in grouped.items():
        cell = {
            "value": value,
            "seeds": [g.get("seed") for g in group],
            "metrics": {k: _mean([metric(g, k) for g in group]) for k in METRICS},
        }
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

    A difference rather than a ratio because these are shares: "+0.041 reach" is the sentence a
    reader wants, and a ratio of two reception fractions is not. The control keeps a row of its own
    reading zero, so the table shows what it was and not only what was subtracted.
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

    `grouped` is {arm value: [report per seed]}. Reports are compared through their means over
    seeds, so a block run with several seeds is judged on the same footing as one run with a single
    seed.
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
    """Apply the per-run gates, returning (fatal, warnings) already worded for a reader.

    Every one of these corresponds to a defect that shipped in this simulator and produced a
    confident wrong number rather than an error. They are cheap; the reason to run them on every
    cell of every night is that each was found by accident the first time.
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
            f"{where}: node channel utilisation {chutil:.1f}% exceeds 100 - physically impossible"
        )

    # A Scenario with no nodes was falsy, so `if scenario:` was False and the run came out flat
    # while the label said alpine. No error, a plausible number, a wrong label.
    if opts.get("scenario") and not ground:
        fatal.append(
            f"{where}: --scenario {opts['scenario']} was asked for and the run recorded no ground"
        )
    if (
        opts.get("scenario")
        and ground
        and not (ground.get("terrain_applied") or ground.get("fixed_geometry"))
    ):
        warn.append(
            f"{where}: --scenario {opts['scenario']} recorded ground but applied no terrain"
        )

    # The design-falsifying counters. A run with a good reception figure and a non-zero silent-loss
    # count is not a good run.
    if sfpp.get("silent_losses"):
        fatal.append(
            f"{where}: SILENT LOSSES {sfpp['silent_losses']:g} - a checksum closed over two unequal sets"
        )
    if sfpp.get("audit_checksum_agrees_sets_differ"):
        fatal.append(
            f"{where}: at-rest audit disagrees with the checksum in "
            f"{sfpp['audit_checksum_agrees_sets_differ']:g} case(s)"
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
            f"{where}: {ground['pairs_beyond_calibration']} pair(s) beyond the fit's "
            f"{envelope / 1000:.1f} km envelope - those fell back to the raw budget"
            if envelope
            else f"{where}: {ground['pairs_beyond_calibration']} pair(s) beyond the fit's envelope"
        )

    # Role-bounded placements cap at the mesh's router count and repeat above it, so two rows of a
    # --servers sweep can silently be the same run.
    req, placed = sfpp.get("servers_requested"), sfpp.get("servers_placed")
    if req is not None and placed is not None and req != placed:
        warn.append(
            f"{where}: {req} archives requested, {placed} placed - group on the placed count"
        )

    # A backoff cap discarding rebroadcasts rescales every airtime figure in the run.
    tx, drops = traffic.get("transmissions"), traffic.get("queue_drops")
    if tx and drops and drops / tx > QUEUE_DROP_WARN:
        warn.append(
            f"{where}: queue drops {drops / tx:.1%} of transmissions - airtime here is measured through a cap"
        )

    for counter in ("misdecodes", "decode_failures"):
        if sfpp.get(counter):
            warn.append(f"{where}: {counter} {sfpp[counter]:g}")
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
    """Return what this block changes, in one sentence, or None if the sweep does not declare it.

    Imported lazily: a digest can be collated from run JSONs alone, and a matrix run's cells are not
    in sweep.BLOCKS at all.
    """
    try:
        from .sweep import DESCRIPTIONS

        return DESCRIPTIONS.get(block)
    except ImportError:
        return None


def summarise_block(reports):
    first = reports[0]
    cells = cells_of(reports)
    against_control(cells)
    block = {
        "block": first.get("block", "?"),
        "arm": first.get("arm", "?"),
        "grid": first.get("grid") or [],
        "transport": first.get("transport"),
        "cells": cells,
        "wall_seconds": sum(r.get("wall_seconds") or 0 for r in reports),
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

    # Which success this arm actually moves. Ranking every block by `held` would rate an arm that
    # halves DM success as inert - but a measure whose denominator is too small to mean anything
    # must not win either, or the leaderboard fills with two-session admin noise.
    block["thin"] = sorted(
        k for k in SUCCESSES if k in block["effect"] and not _has_denominator(cells, k)
    )
    # A spread of zero is not a movement. Without this, a block whose cells are identical in every
    # delivery measure still reported `moved: text, spread 0.000` - which reads as a finding about
    # text and is the opposite of one. E-signed is that block: signing changes bytes and nothing
    # else, and it belongs under "moved no delivery measure" with its price beside it.
    moved = [
        (k, v["spread"])
        for k, v in block["effect"].items()
        if k in SUCCESSES and k not in block["thin"] and v["spread"] > INERT_EPSILON
    ]
    if moved:
        block["moved"] = max(moved, key=lambda kv: kv[1])[0]

    if _inert(group_by_value(reports)):
        block["flags"].append(
            f"inert: every value of `{block['arm']}` produced identical numbers - "
            "either the flag is not read, or it needs a second flag before it does anything (README §10.4)"
        )
    for r in reports:
        fatal, warn = check_cell(r, f"{block['arm']}={r.get('value')}")
        block["fatal"] += fatal
        block["flags"] += warn
    return block


def collate(runs_dir, run_id=None, seed_base=None, scenario=None, expected=None):
    blocks = []
    for path in sorted(glob.glob(os.path.join(runs_dir, "*.json"))):
        # summary.json is this module's own output; a re-collate must not read it back in as a block.
        if os.path.basename(path) == "summary.json":
            continue
        reports = load_block(path)
        if reports and "block" in reports[0]:
            blocks.append(summarise_block(reports))

    present = {b["block"] for b in blocks}
    missing = sorted(set(expected) - present) if expected else []
    transports = sorted({b["transport"] for b in blocks if b.get("transport")})
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
        "blocks": sorted(blocks, key=lambda b: b["block"]),
        "missing_blocks": missing,
        "wall_seconds": sum(b["wall_seconds"] for b in blocks),
        "gate": gate(blocks, missing),
    }


def gate(blocks, missing):
    """Judge the run. Only the design-falsifying and physically impossible are fatal."""
    failures = [f"{b['block']}: {f}" for b in blocks for f in b["fatal"]]
    warnings = [f"{b['block']}: {f}" for b in blocks for f in b["flags"]]
    return {
        "ok": not failures,
        "failures": failures,
        "warnings": warnings,
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
        "four denominators and are **not comparable to each other** (README §7.2) - `moved` names "
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
