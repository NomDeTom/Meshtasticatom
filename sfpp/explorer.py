"""The rolling view: every scheduled sweep so far, in one page.

A single run answers "what did this seed and this ground say". The question that matters is whether
it says the same thing as the last thirty, and no single run can answer that - which is the whole
reason a nightly sweep is worth running at all. This module reads the digests `collate.py` left
behind, one per run, and renders them as a page whose rows are blocks and whose columns are runs.

Only the digests are read, never the block JSONs, so the archive can drop the raw runs without the
explorer losing its history. The page is a single self-contained file: no CDN, no fonts, no fetch,
because it is served from a git branch and has to work as a local file too.

Usage, from sim/:
    python3 -m sfpp.explorer --archive <dir of run dirs> --out <dir>
    python3 -m sfpp.explorer --archive runs --out . --window 30
"""

import argparse
import glob
import html
import json
import os
import statistics
import urllib.parse

from .collate import COST, safe_name
from .version import SIM_VERSION

# What the page shows per cell; the digest carries more. Eight numbers a cell is what keeps
# thirty runs of 87 blocks a file a browser opens instantly.
SHOWN = [
    ("text", "text", 3),
    # The same texts by how they arrived. `text` is what a node holds; `text_on_air` is what the
    # broadcast delivered, and the difference is an archive's replay rather than a better mesh.
    ("text_on_air", "text on air", 3),
    ("text_overheard", "text overheard", 3),
    ("dm", "DM", 3),
    ("admin", "admin", 3),
    ("held", "held", 3),
    ("union", "union", 3),
    ("text_worst", "worst", 3),
    # A multiple with no ceiling, and a percentage that cannot pass 100. Named apart on purpose:
    # reading the first as the second described genuine comparisons as rankings of collapse.
    ("demand", "demand x", 2),
    # Both utilisations across their own distribution. A max alone cannot tell a mesh with one
    # saturated node from one that is uniformly half busy, and those are different problems.
    ("chutil_p10", "chutil p10 %", 1),
    ("chutil_median", "chutil p50 %", 1),
    ("chutil_p90", "chutil p90 %", 1),
    ("chutil_max", "chutil max %", 1),
    ("airutil_p10", "airutil p10 %", 1),
    ("airutil_median", "airutil p50 %", 1),
    ("airutil_p90", "airutil p90 %", 1),
    ("airutil_max", "airutil max %", 1),
    ("sr_airtime", "SR air", 3),
    # Sketch failures, chartable rather than only listed as warnings. The share is the comparable
    # one - a raw count ranks whichever cell ran the most exchanges.
    # Overhead against catch-up: what the protocol said, and what got carried because it said it.
    ("sr_messages", "protocol messages", 0),
    ("objects_moved", "objects carried", 0),
    ("messages_per_object", "messages per object", 2),
    ("bytes_per_object", "bytes per object", 0),
    ("adverts", "adverts", 0),
    ("item_requests", "item requests", 0),
    ("provides", "provides", 0),
    ("chain_round_trips", "chain round trips", 0),
    ("sr_bytes", "protocol bytes", 0),
    ("decode_fail_share", "decode fail rate", 3),
    ("decode_failures", "decode failures", 0),
    ("misdecodes", "misdecodes", 0),
    ("exchanges", "exchanges", 0),
    ("servers_placed", "placed", 0),
]
# The axis each metric belongs on. Bars side by side invite reading one height against another, and
# the note above is exactly why that has to be refused across units: `demand` has no ceiling and
# `chutil_p90` cannot pass 100, so one y axis for both ranks collapse instead of measuring it. A
# family is a promise that heights within it mean the same thing.
UNITS = {
    "text": "share",
    "text_on_air": "share",
    "text_overheard": "share",
    "dm": "share",
    "admin": "share",
    "held": "share",
    "union": "share",
    "text_worst": "share",
    "sr_airtime": "share",
    "decode_fail_share": "share",
    "sr_messages": "events",
    "objects_moved": "events",
    "adverts": "events",
    "item_requests": "events",
    "provides": "events",
    "chain_round_trips": "events",
    "messages_per_object": "per-object",
    "bytes_per_object": "bytes",
    "sr_bytes": "bytes",
    "decode_failures": "events",
    "misdecodes": "events",
    "exchanges": "events",
    "demand": "multiple",
    "chutil_p10": "percent",
    "chutil_median": "percent",
    "chutil_p90": "percent",
    "chutil_max": "percent",
    "airutil_p10": "percent",
    "airutil_median": "percent",
    "airutil_p90": "percent",
    "airutil_max": "percent",
    "servers_placed": "count",
}
# The map's role marks, as the drawn map has them. Duplicated rather than imported: this module is
# built to read an archive with nothing else present, and a page that cannot draw a legend because
# meshmap is absent would be worse than one whose two copies can drift. test_collate pins them equal.
MAP_MARKS = [
    ["ROUTER", "square", "#2E5E7E"],
    ["ROUTER_LATE", "square-open", "#4E86A8"],
    ["CLIENT_BASE", "diamond", "#7FB0CB"],
    ["CLIENT", "circle", "#B5D2E2"],
    ["CLIENT_MUTE", "circle-open", "#DCE9F1"],
    ["unmodelled", "circle", "#F0F0F0"],
]
MAP_FRAGILE = "#B4472A"
MAP_LINK = "#9fb4c7"
UNIT_AXIS = {
    "share": "share of offered traffic (0-1)",
    "multiple": "multiple of the unscaled interval (x)",
    "percent": "channel/air utilisation (%)",
    "count": "nodes",
    "events": "count over the run",
    "bytes": "bytes over the run",
    "per-object": "protocol messages per object carried",
}
# Fixed per metric, not per position in the selection, so a colour means the same thing in every
# panel and across a reload. Chosen to hold up on both themes and for red/green colour blindness.
SERIES_COLOURS = {
    "text": "#2E5E7E",
    "text_on_air": "#1F7A5A",
    "text_overheard": "#B8860B",
    "dm": "#B4472A",
    "admin": "#7A8C3F",
    "held": "#4E86A8",
    "union": "#8A5A9E",
    "text_worst": "#C08A2E",
    "sr_airtime": "#3F8A7A",
    "sr_messages": "#8A5A9E",
    "objects_moved": "#4E86A8",
    "messages_per_object": "#8A5A9E",
    "bytes_per_object": "#7A8C3F",
    "adverts": "#A57BB8",
    "item_requests": "#C08A2E",
    "provides": "#3F8A7A",
    "chain_round_trips": "#B4472A",
    "sr_bytes": "#7A8C3F",
    "decode_fail_share": "#B4472A",
    "decode_failures": "#B4472A",
    "misdecodes": "#8C2F16",
    "exchanges": "#7FA8C0",
    "demand": "#2E5E7E",
    # One ramp per utilisation, darkening towards the tail, so the four read as one distribution
    # rather than as four unrelated series - and the two types stay apart by hue.
    "chutil_p10": "#9CC0D6",
    "chutil_median": "#6296B8",
    "chutil_p90": "#2E5E7E",
    "chutil_max": "#1B3A50",
    "airutil_p10": "#E0BE7E",
    "airutil_median": "#C08A2E",
    "airutil_p90": "#8F6413",
    "airutil_max": "#5E4109",
    "servers_placed": "#4E86A8",
}


def load_archive(archive_dir, window=None):
    """Every run digest under `archive_dir`, oldest first, optionally only the most recent `window`."""
    runs = []
    for path in sorted(glob.glob(os.path.join(archive_dir, "*", "summary.json"))):
        try:
            with open(path) as f:
                summary = json.load(f)
        except (OSError, json.JSONDecodeError):
            # A run whose digest is unreadable is a run that failed midway; the rolling view is
            # exactly the wrong place to stop for it.
            continue
        summary["_dir"] = os.path.dirname(path)
        summary["_name"] = os.path.basename(summary["_dir"])
        runs.append(summary)
    runs.sort(key=lambda r: (r.get("run_id") or "", r.get("generated") or ""))
    return runs[-window:] if window else runs


def comparable_series(version):
    """The MAJOR.MINOR a run has to carry to be readable against `version`.

    version.py bumps MINOR when a change makes existing results incomparable and PATCH when nothing
    can move a number, so the patch component is exactly what may differ.
    """
    parts = str(version or "").split(".")
    return ".".join(parts[:2]) if len(parts) >= 2 else str(version or "")


def comparable_runs(runs, version=SIM_VERSION):
    """Split the archive into runs measured under `version` and runs superseded by it.

    A superseded run is not wrong, it answered a different question: an airtime correction or a
    changed default moves every metric it carries. Pooling the two into one mean or one trend line
    is the shape TRAPS.md keeps recording - a well-formed number nothing marks as incomparable.
    Returns (comparable, superseded), both oldest first.
    """
    want = comparable_series(version)
    current, stale = [], []
    for run in runs:
        got = run.get("sim_version")
        # A digest predating versioning, or one straddling a bump, cannot claim to be comparable.
        series = comparable_series(got) if isinstance(got, str) else None
        (current if series == want else stale).append(run)
    return current, stale


def index_by_block(runs):
    """{block: {"arm", "runs": [{run_id, scenario, cells: {value: metrics}}]}} across the archive."""
    blocks = {}
    for run in runs:
        for b in run.get("blocks", []):
            entry = blocks.setdefault(
                b["block"], {"arm": b["arm"], "runs": [], "moved": None}
            )
            entry["arm"] = b["arm"]
            # The measure this block travels in, decided per run by collate. Later runs win, so the
            # page follows the current transport rather than whatever the first night happened to say.
            entry["moved"] = b.get("moved") or entry["moved"]
            entry["explains"] = b.get("explains") or entry.get("explains")
            entry["runs"].append(
                {
                    "run_id": run.get("run_id"),
                    "scenario": run.get("scenario_requested") or "flat",
                    "seed_base": run.get("seed_base"),
                    "cells": {c["value"]: c["metrics"] for c in b["cells"]},
                    # Seed-to-seed standard deviation per metric, where the cell was run more than
                    # once. Collated since the digest existed and never rendered, so three seeds
                    # were reported as one number and a difference smaller than the draw read
                    # exactly like a difference larger than it.
                    "sd": {
                        c["value"]: c["sd"] for c in b["cells"] if c.get("sd")
                    },
                    # The six-number distributions behind the single numbers, where the digest was
                    # collated recently enough to carry them. Older digests have none, so every
                    # reader of this has to treat it as absent rather than empty.
                    "dist": {
                        c["value"]: c["dist"] for c in b["cells"] if c.get("dist")
                    },
                    # Only present when the digest was collated with --per-node.
                    "per_node": {
                        c["value"]: c["per_node"] for c in b["cells"] if c.get("per_node")
                    },
                    # Only present when the digest was collated with --maps. The geometry itself
                    # lives once per run, in `run["maps"]`, and this holds the key into it.
                    "maps": {
                        c["value"]: c["map"] for c in b["cells"] if c.get("map")
                    },
                    "cost": b.get("cost"),
                    "flags": b.get("flags", []),
                    "flag_kinds": b.get("flag_kinds") or {},
                    "timing": b.get("timing"),
                    "seconds_per_sim_hour": b.get("seconds_per_sim_hour"),
                    "wall_seconds": b.get("wall_seconds"),
                }
            )
    return blocks


def declared_surfaces():
    """{surface: {cell name: sentence}} for every sweep this tree declares, run or not.

    The one place this module reaches past the digests; guarded, so an archive stays readable alone.
    """
    surfaces = {}
    try:
        from .sweep import BLOCKS, DESCRIPTIONS

        surfaces["blocks"] = {name: DESCRIPTIONS.get(name, "") for name in BLOCKS}
    except ImportError:
        pass
    for module, label in (("matrix", "matrix"), ("design", "design")):
        try:
            producer = __import__(f"{__package__}.{module}", fromlist=["describes"])
            surfaces[label] = dict(producer.describes())
        except ImportError:
            continue
    return surfaces


def schedule(runs, surfaces=None):
    """Every declared cell against what the archive holds for it.

    `runs` and `last_run` both recorded: nightly and weekly surfaces mean different things by "due".
    """
    surfaces = declared_surfaces() if surfaces is None else surfaces
    seen = {}
    for run in runs:
        for b in run.get("blocks", []):
            entry = seen.setdefault(b["block"], {"runs": 0, "last": None})
            entry["runs"] += 1
            entry["last"] = run.get("run_id") or entry["last"]
    latest = (runs[-1].get("run_id") if runs else None) or None
    in_latest = {
        b["block"] for b in (runs[-1].get("blocks", []) if runs else [])
    }

    out = []
    for surface, cells in sorted(surfaces.items()):
        rows = []
        for name, sentence in sorted(cells.items()):
            got = seen.get(name)
            rows.append(
                {
                    "cell": name,
                    "explains": sentence,
                    "runs": got["runs"] if got else 0,
                    "last_run": got["last"] if got else None,
                    "in_latest": name in in_latest,
                }
            )
        out.append(
            {
                "surface": surface,
                "declared": len(cells),
                "ever_run": sum(1 for r in rows if r["runs"]),
                "never_run": sum(1 for r in rows if not r["runs"]),
                "in_latest": sum(1 for r in rows if r["in_latest"]),
                "rows": rows,
            }
        )
    # Anything the archive holds that nothing declares - a renamed or retired cell whose old results
    # are still in the branch. Not an error, but it is why a "done" count can exceed the declared one.
    declared = {name for cells in surfaces.values() for name in cells}
    undeclared = sorted(set(seen) - declared)
    return {"surfaces": out, "undeclared": undeclared, "latest_run": latest}


def run_health(runs):
    """Per run: what it cost, what it flagged, and whether its runtime drifted.

    Duration both ways: the total decides whether a job fits, the rate is what compares.
    """
    out = []
    for run in runs:
        gate = run.get("gate", {})
        blocks = run.get("blocks", [])
        rates = [
            b["seconds_per_sim_hour"]
            for b in blocks
            if isinstance(b.get("seconds_per_sim_hour"), (int, float))
        ]
        drifted = [b for b in blocks if b.get("timing")]
        slowest = max(
            (b for b in blocks if isinstance(b.get("wall_seconds"), (int, float))),
            key=lambda b: b["wall_seconds"],
            default=None,
        )
        out.append(
            {
                "run_id": run.get("run_id") or run.get("_name"),
                "href": run.get("_href"),
                "generated": run.get("generated"),
                "scenario": run.get("scenario_requested") or "flat",
                "seed_base": run.get("seed_base"),
                "wall_seconds": run.get("wall_seconds") or 0,
                "blocks_run": gate.get("blocks_run", 0),
                "blocks_missing": gate.get("blocks_missing", 0),
                "ok": gate.get("ok", True),
                "failures": len(gate.get("failures", [])),
                "warnings": len(gate.get("warnings", [])),
                "by_kind": gate.get("warnings_by_kind") or {},
                "median_rate": statistics.median(rates) if rates else None,
                "slowest_block": slowest["block"] if slowest else None,
                "slowest_seconds": slowest["wall_seconds"] if slowest else None,
                "drifted": sorted(
                    (
                        {
                            "block": b["block"],
                            "ratio": b["timing"]["ratio"],
                            "rate": b["timing"]["seconds_per_sim_hour"],
                            "median": b["timing"]["median"],
                        }
                        for b in drifted
                    ),
                    key=lambda d: -d["ratio"],
                ),
            }
        )
    return out


def spread_of(run, key):
    """How far one metric travels across an arm within a single run, or None if it was not recorded."""
    values = [m.get(key) for m in run["cells"].values() if m.get(key) is not None]
    return max(values) - min(values) if len(values) > 1 else None


def leaderboard(blocks):
    """Blocks by how far they move a delivery measure, averaged over the runs that carry them.

    Averaged, not pooled, or age in the archive becomes the ranking. Measure named per block.
    """
    rows = []
    for name, entry in blocks.items():
        measure = entry.get("moved") or "held"
        spreads = [
            s for s in (spread_of(r, measure) for r in entry["runs"]) if s is not None
        ]
        costs = [
            s for s in (spread_of(r, COST) for r in entry["runs"]) if s is not None
        ]
        price = next(
            (r["cost"] for r in reversed(entry["runs"]) if r.get("cost")), None
        )
        if not spreads and not price:
            continue
        rows.append(
            {
                "block": name,
                "arm": entry["arm"],
                "measure": measure,
                "spread": statistics.mean(spreads) if spreads else None,
                # Whether the effect is stable run to run, or an artefact of one seed.
                "spread_sd": statistics.stdev(spreads) if len(spreads) > 1 else None,
                "cost": statistics.mean(costs) if costs else None,
                # The price side, from the most recent run that priced it. A block that holds
                # delivery flat and moves a byte counter fivefold is a result, not an absence.
                "price": next(
                    (r["cost"] for r in reversed(entry["runs"]) if r.get("cost")), None
                ),
                "runs": len(spreads),
            }
        )
    return sorted(
        rows, key=lambda r: (r["spread"] is not None, r["spread"] or 0), reverse=True
    )


def series(entry, key):
    """{arm value: [metric per run, None where that run did not have the value]} for one block."""
    values = []
    for run in entry["runs"]:
        for v in run["cells"]:
            if v not in values:
                values.append(v)
    return {
        v: [run["cells"].get(v, {}).get(key) for run in entry["runs"]] for v in values
    }


def sparkline(points, width=90, height=18):
    """Inline SVG, no library. Gaps in the series break the line rather than interpolating a lie."""
    present = [p for p in points if p is not None]
    if len(present) < 2:
        return ""
    lo, hi = min(present), max(present)
    span = (hi - lo) or 1.0
    step = width / max(1, len(points) - 1)
    segments, current = [], []
    for i, p in enumerate(points):
        if p is None:
            if len(current) > 1:
                segments.append(current)
            current = []
            continue
        current.append(
            f"{i * step:.1f},{height - (p - lo) / span * (height - 2) - 1:.1f}"
        )
    if len(current) > 1:
        segments.append(current)
    paths = "".join(f'<polyline points="{" ".join(s)}" />' for s in segments)
    return (
        f'<svg class="spark" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
        f'aria-hidden="true">{paths}</svg>'
    )


def _fmt(v, places=3):
    if v is None:
        return "·"
    if places == 0:
        return f"{v:,.0f}"
    return f"{v:.{places}f}"


def _price(row):
    """Render the largest cost ratio across the arm, as `5.7x advert_bytes`, or a dash."""
    cost = row.get("price")
    return f"{cost['ratio']:.2g}x {cost['metric']}" if cost else "·"


def _esc(v):
    return html.escape(str(v))


CSS = """
/* The variable names, both theme mechanisms and the .action-btn pattern are the house style of the
   site this page is published to (its AGENTS.md). Auto follows the viewer's system setting; the
   toggle stamps data-theme and wins in either direction. Every colour is defined on bare :root, so
   nothing depends on a media query having matched. */
:root {
  --page-bg: #f7f7f2;
  --panel-bg: #ffffff;
  --field-bg: #ffffff;
  --text: #1f2520;
  --muted: #5c645d;
  --disabled: #888a88;
  --border: #d9ddd4;
  --accent: #1d6b43;
  --accent-soft: #eef6ef;
  --warn: #8a6d1a;
  --bad: #a01f1f;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --page-bg: #111713;
    --panel-bg: #1a241d;
    --field-bg: #131b15;
    --text: #e5efe6;
    --muted: #b2beb4;
    --disabled: #7a827b;
    --border: #3a4d40;
    --accent: #81d39d;
    --accent-soft: #23362a;
    --warn: #d4b155;
    --bad: #e57373;
  }
}
:root[data-theme="dark"] {
  --page-bg: #111713;
  --panel-bg: #1a241d;
  --field-bg: #131b15;
  --text: #e5efe6;
  --muted: #b2beb4;
  --disabled: #7a827b;
  --border: #3a4d40;
  --accent: #81d39d;
  --accent-soft: #23362a;
  --warn: #d4b155;
  --bad: #e57373;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--page-bg); color: var(--text);
  font: 15px/1.55 ui-sans-serif, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
main { width: min(100%, 96rem); margin: 0 auto; padding: 2rem 1rem 3rem; }
.top-actions { display: flex; flex-wrap: wrap; gap: .5rem; margin-bottom: 1.5rem; }
.action-btn {
  border: 1px solid var(--border); background: var(--panel-bg); color: var(--text);
  padding: .45rem .75rem; cursor: pointer; font: inherit;
}
.action-btn:hover { border-color: var(--accent); color: var(--accent); }
a.action-btn { text-decoration: none; display: inline-block; }
a:not(.action-btn) { color: var(--accent); text-decoration: none; }
a:not(.action-btn):hover { text-decoration: underline; }
h1 { font-size: 1.5rem; margin: 0 0 .25rem; letter-spacing: -0.01em; }
h2 { font-size: 1.05rem; margin: 2.5rem 0 .75rem; }
h3 { font-size: .95rem; margin: 0; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
p.sub { color: var(--muted); margin: 0 0 1.5rem; }
.meta { display: flex; flex-wrap: wrap; gap: .5rem 1.5rem; color: var(--muted); font-size: .85rem; margin-bottom: 1.5rem; }
.meta b { color: var(--text); font-weight: 600; }
.panel { background: var(--panel-bg); border: 1px solid var(--border); border-radius: 10px; padding: 1rem 1.1rem; margin-bottom: 1rem; }
.scroll { overflow-x: auto; }
/* Collapsed by default: a reader scanning thirty blocks wants the tables, and opens the one chart
   that the numbers sent them to. */
.figure { margin: .75rem 0 .25rem; }
.figure > summary { cursor: pointer; color: var(--muted); font-size: .8rem; width: max-content; }
.figure > summary:hover { color: var(--text); }
.chartbar { margin: .5rem 0 .25rem; }
/* Wraps rather than scrolls: on a narrow screen a reader needs to see every field on offer at once
   to decide, and a hidden checkbox reads as a metric the digest does not carry. */
.chartpick { display: flex; flex-wrap: wrap; gap: .15rem .9rem; font-size: .8rem; color: var(--muted); }
.chartpick label { display: inline-flex; align-items: center; gap: .3rem; cursor: pointer; }
.chartpick label:hover { color: var(--text); }
.chartpick input { margin: 0; cursor: pointer; }
.chartpick .wide { flex-basis: 100%; }
/* One group per unit family, and the family is what the chart splits on, so a group is one chart's
   worth of ticks. The rule keeps the boundary visible when the row wraps mid-group. */
.chartgroup { display: inline-flex; flex-wrap: wrap; align-items: center; gap: .15rem .9rem;
  padding: .1rem .55rem .1rem .5rem; border-left: 2px solid var(--border); }
.chartgroup .unit { font-weight: 600; color: var(--text); font-size: .95em; }
.chart { min-height: 2rem; }
.chart .axislabel { font-size: .75rem; color: var(--muted); margin: .5rem 0 -.2rem; }
.figure svg { background: #FCFCFA; border: 1px solid var(--border); border-radius: 6px; margin-top: .4rem; }
/* Tabs. Progressive enhancement: with no JS every panel stays visible and the nav is inert, so the
   page remains one long readable document - which is also what printing and grepping it want. */
.tabs { display: flex; flex-wrap: wrap; gap: .25rem; border-bottom: 1px solid var(--border); margin: 1.5rem 0 0; }
.tabs button {
  border: 1px solid transparent; border-bottom: none; background: none; color: var(--muted);
  padding: .5rem .9rem; cursor: pointer; font: inherit; border-radius: 8px 8px 0 0;
}
.tabs button:hover { color: var(--accent); }
.tabs button[aria-selected="true"] {
  color: var(--text); background: var(--panel-bg);
  border-color: var(--border); margin-bottom: -1px; font-weight: 600;
}
.tabs .count { color: var(--muted); font-weight: 400; font-size: .8em; }
/* The `hidden` attribute is in the markup so the first paint shows one panel rather than flashing
   all five. That means overriding the UA's own [hidden] rule for the no-JS case, or the panels stay
   hidden with nothing able to reveal them - the nav only becomes live once the script adds .tabbed. */
.tab-panel[hidden] { display: block; }
body.tabbed .tab-panel[hidden] { display: none; }
.tab-panel > h2:first-child { margin-top: 1.5rem; }
/* A kind of flag, counted. Neutral by default - `beyond-envelope` on a mirrored cell is expected,
   and colouring every warning red teaches people to stop reading them. */
.kind { display: inline-flex; gap: .35rem; align-items: baseline; border: 1px solid var(--border);
        border-radius: 999px; padding: .1rem .5rem; font-size: .78rem; margin: .15rem .25rem .15rem 0; }
.kind b { font-weight: 600; }
.kind.warnish { border-color: var(--warn); color: var(--warn); }
.drift-up { color: var(--warn); font-weight: 600; }
.drift-down { color: var(--accent); font-weight: 600; }
.never { color: var(--muted); }
.tick { color: var(--accent); font-weight: 600; }
table { border-collapse: collapse; width: 100%; font-size: .85rem; }
th, td { text-align: right; padding: .35rem .5rem; border-bottom: 1px solid var(--border); white-space: nowrap; }
th:first-child, td:first-child { text-align: left; }
th { color: var(--muted); font-weight: 600; font-size: .78rem; text-transform: uppercase; letter-spacing: .04em; }
tbody tr:last-child td { border-bottom: 0; }
code, .mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .95em; }
.spark polyline { fill: none; stroke: var(--accent); stroke-width: 1.5; stroke-linejoin: round; }
.flag { color: var(--warn); font-size: .82rem; margin: .5rem 0 0; }
.flags { margin-top: .6rem; }
.flags > summary {
  cursor: pointer; color: var(--warn); font-size: .82rem; list-style: none;
  display: inline-block; border: 1px solid var(--border); border-radius: 999px;
  padding: .1rem .6rem;
}
.flags > summary::-webkit-details-marker { display: none; }
.flags > summary::before { content: "▸ "; }
.flags[open] > summary::before { content: "▾ "; }
.flags > summary:hover { border-color: var(--warn); }
.flag.bad { color: var(--bad); }
.pill { display: inline-block; padding: .1rem .5rem; border: 1px solid var(--border); border-radius: 999px; font-size: .75rem; color: var(--muted); }
.controls { display: flex; flex-wrap: wrap; gap: .6rem; margin: 1rem 0 1.5rem; }
input[type=search], select {
  background: var(--field-bg); color: var(--text); border: 1px solid var(--border);
  border-radius: 8px; padding: .4rem .6rem; font: inherit; font-size: .85rem;
}
input:focus, select:focus { outline: 2px solid var(--accent); outline-offset: 2px; border-color: var(--accent); }
.blockhead { display: flex; align-items: baseline; gap: .6rem; flex-wrap: wrap; margin-bottom: .6rem; }
.blockhead .arm { color: var(--muted); font-size: .85rem; }
.attribution-block { background: var(--accent-soft); border: 1px solid var(--border); border-radius: 10px; padding: 1rem 1.1rem; margin-bottom: 1rem; font-size: .85rem; }
.attribution-block[hidden] { display: none; }
.hidden { display: none; }
footer { color: var(--muted); font-size: .8rem; margin-top: 3rem; }
/* The making page reads as a manual rather than as a result, so it gets a manual's furniture:
   an index that stays put while the prose scrolls past it. */
.making { display: grid; grid-template-columns: 12.5rem minmax(0, 1fr); gap: 1.4rem; align-items: start; }
.making-nav { position: sticky; top: 1rem; font-size: .85rem; }
.making-nav ol { list-style: none; margin: 0; padding: 0; counter-reset: makingnav; }
.making-nav li { counter-increment: makingnav; margin: 0 0 .1rem; }
.making-nav a {
  display: block; padding: .3rem .5rem; border-left: 2px solid var(--border);
  color: var(--muted); text-decoration: none;
}
.making-nav a::before { content: counter(makingnav) ". "; color: var(--disabled); }
.making-nav a:hover { border-left-color: var(--accent); color: var(--accent); text-decoration: none; }
/* Two columns, never more: `auto-fit` fitted four across a 96rem page and shrank a 640-wide chart
   to 60%, which makes 11px axis text unreadable. A multi-series family takes the width back - its
   bars are meant to be read against each other across the whole axis - and `dense` lets a later
   narrow chart backfill the gap a wide one leaves, so the narrow pair ends up side by side. */
.chartgrid {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
  grid-auto-flow: row dense; gap: .4rem 1.2rem; align-items: end;
}
.chartcell { min-width: 0; }
.chartcell.wide { grid-column: 1 / -1; }
/* The cross-block page. One row per block, stacked, sharing a left gutter and one scale. */
.stackbar { display: flex; align-items: center; gap: .8rem; flex-wrap: wrap; margin-bottom: .6rem; }
.stacklabel { font-size: .78rem; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); font-weight: 600; }
.stackmetrics { border-bottom: 1px solid var(--border); padding-bottom: .6rem; }
.stackblocks { display: flex; flex-wrap: wrap; gap: .3rem 1rem; font-size: .85rem; color: var(--muted); margin-bottom: .8rem; }
.stackblocks label { display: flex; align-items: center; gap: .3rem; }
.stackrow { border-top: 1px solid var(--border); padding: .5rem 0 .2rem; }
.stackrow:first-child { border-top: 0; }
/* The campaign panel: the recipe as a table beside the mesh it made. */
.recipe { border-top: 1px solid var(--border); padding-top: .8rem; margin-top: .8rem; }
.recipe:first-of-type { border-top: 0; padding-top: 0; margin-top: 0; }
.recipename { font-size: .95rem; margin: 0 0 .2rem; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.recipebody { display: grid; grid-template-columns: minmax(0, 21rem) minmax(0, 1fr); gap: 1rem 1.4rem; align-items: start; }
.recipebody > * { min-width: 0; }
/* Its own rules rather than the glossary's: that table fixes a 10rem term column and a 13rem
   denominator column, which together overflow this narrower track and run under the map. */
.recipetable { table-layout: fixed; width: 100%; }
.recipetable td {
  font-size: .8rem; padding: .18rem .5rem; text-align: left; white-space: normal;
  overflow-wrap: break-word; vertical-align: top;
}
.recipetable td:first-child { width: 8.5rem; color: var(--muted); }
.campaignmap { min-width: 0; overflow: hidden; }
.campaignmap svg { display: block; width: 100%; height: auto; }
/* Three cells to a row, not `auto-fit`: a 96rem page fitted eight of them at 11rem and each pie
   came out smaller than its own legend. Each cell holds a pair, so a row is six pies. */
.piegrid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .8rem 1.4rem; }
.piecell { min-width: 0; }
.piepair { display: grid; grid-template-columns: 1fr 1fr; gap: .4rem; }
@media (max-width: 1100px) { .piegrid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 700px) { .piegrid { grid-template-columns: minmax(0, 1fr); } }
@media (max-width: 900px) { .recipebody { grid-template-columns: minmax(0, 1fr); } }
.swatch { display: inline-block; width: .62rem; height: .62rem; border-radius: 2px; margin-right: .3rem; vertical-align: baseline; }
@media (max-width: 1100px) { .chartgrid { grid-template-columns: minmax(0, 1fr); } }
/* This table holds prose, not numbers, so it has to undo the numeric defaults above: those set
   `text-align: right` and `white-space: nowrap`, which between them right-align a sentence and
   then refuse to wrap it. Fixed layout keeps the prose column taking the slack. */
.glossary { table-layout: fixed; width: 100%; }
.glossary th, .glossary td {
  text-align: left; white-space: normal; overflow-wrap: break-word;
  vertical-align: top; line-height: 1.45;
}
.glossary th:first-child, .glossary td:first-child { width: 10rem; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.glossary th:last-child, .glossary td:last-child { width: 13rem; color: var(--muted); }
.glossary tr.head td { vertical-align: middle; }
@media (max-width: 640px) {
  .glossary th:first-child, .glossary td:first-child { width: 6.5rem; }
  .glossary th:last-child, .glossary td:last-child { width: 7.5rem; }
}
.glossary tr.head td { font-weight: 600; color: var(--muted); background: var(--field-bg); }
@media (max-width: 768px) {
  .meta { gap: .35rem 1rem; }
  .making { grid-template-columns: minmax(0, 1fr); }
  .making-nav { position: static; }
}
"""

JS = """
// Every panel's chart, drawn from the digest numbers embedded below rather than from an image.
// Bars per cell for the latest run, and a line per cell when there is more than one run to trace.
(function () {
  const data = JSON.parse(document.getElementById('chartdata').textContent);
  const meta = JSON.parse(document.getElementById('chartmeta').textContent);
  document.querySelectorAll('.nojs').forEach((p) => p.remove());
  const NS = 'http://www.w3.org/2000/svg';
  const el = (name, attrs) => {
    const node = document.createElementNS(NS, name);
    for (const k in attrs) node.setAttribute(k, attrs[k]);
    return node;
  };

  // One dot per node per class: a mesh small enough to read node by node, read that way. The
  // classes share an x axis, so a node that is deaf to everything lines up down the chart and a
  // class that alone fails does not hide inside a median.
  function drawNodes(host, entry) {
    const cells = Object.keys(entry.nodes || {});
    host.textContent = '';
    if (!cells.length) return;
    // Two marks per node on a text row - one on the baseline, one half a row up - so the row is
    // twice the height a single track of dots needs. Anything tighter and the lifted marks of one
    // row sit on the dots of the row above.
    const W = 640, LEFT = 132, RIGHT = 24, PLOT = W - LEFT - RIGHT, ROW = 32;
    const rows = [];
    cells.forEach((cell) => {
      const classes = entry.nodes[cell].classes;
      // A class either kept the bare on-air vector or, where a second delivery path exists, the
      // two apart. Both shapes are in the archive, so both are read here.
      Object.keys(classes).forEach((cls) => {
        const v = classes[cls];
        rows.push(Array.isArray(v)
          ? [cell, cls, v, null]
          : [cell, cls, v.on_air || [], v.overheard || null]);
      });
    });
    const H = 34 + rows.length * ROW;
    const svg = el('svg', {viewBox: `0 0 ${W} ${H}`, width: '100%', height: H,
                           style: 'max-width:100%;height:auto;font-size:10.5px'});
    rows.forEach(([cell, cls, vector, overheard], i) => {
      const y = 14 + i * ROW;
      const label = el('text', {x: LEFT - 8, y: y + 4, 'text-anchor': 'end',
                                style: 'fill:var(--muted)'});
      label.textContent = `${cell} · ${cls}`;
      svg.appendChild(label);
      svg.appendChild(el('line', {x1: LEFT, y1: y, x2: LEFT + PLOT, y2: y,
                                  style: 'stroke:var(--border)'}));
      const at = (v) => LEFT + Math.max(0, Math.min(1, v)) * PLOT;
      // Half a row up, on a track of its own: drawn through the dots it crossed them, and a
      // segment that starts inside a filled circle cannot show where it started.
      const lift = y - ROW / 2;
      vector.forEach((share, node) => {
        const extra = overheard ? (overheard[node] || 0) : 0;
        if (extra > 0) {
          // Joins this node's two points: the dot where the broadcast left it, and the mark half a
          // row up where the archive's replays left it. The line is the measurement - one node
          // going from what it heard to what it holds - and the lift is only so it clears the dots.
          // Faint: with twenty nodes to a row the connectors are the densest thing on the chart,
          // and they are there to say which two points belong together, not to be read off.
          const reachLine = el('line', {x1: at(share), y1: y, x2: at(share + extra), y2: lift,
                                        style: 'stroke:var(--warn);stroke-width:1;opacity:.32'});
          const reachTitle = el('title', {});
          reachTitle.textContent =
            `node ${node}: ${share.toFixed(3)} on air -> ${(share + extra).toFixed(3)} held ` +
            `(+${extra.toFixed(3)} overheard)`;
          reachLine.appendChild(reachTitle);
          svg.appendChild(reachLine);
          const held = el('circle', {cx: at(share + extra), cy: lift, r: 2.1,
                                     style: 'fill:var(--warn);fill-opacity:.85'});
          held.appendChild(el('title', {})).textContent =
            `node ${node}: ${(share + extra).toFixed(3)} held`;
          svg.appendChild(held);
        }
        const dot = el('circle', {cx: at(share), cy: y, r: 2.1,
                                  style: 'fill:var(--accent);fill-opacity:.55'});
        const title = el('title', {});
        title.textContent = extra > 0
          ? `node ${node}: ${share.toFixed(3)} on air, ${(share + extra).toFixed(3)} held`
          : `node ${node}: ${share.toFixed(3)}`;
        dot.appendChild(title);
        svg.appendChild(dot);
      });
    });
    [0, 0.5, 1].forEach((t) => {
      const tick = el('text', {x: LEFT + t * PLOT, y: H - 4, 'text-anchor': 'middle',
                               style: 'fill:var(--muted)'});
      tick.textContent = t.toFixed(1);
      svg.appendChild(tick);
    });
    host.appendChild(svg);
  }

  // Text delivery per cell as two stacked layers: what the broadcast carried, and what an
  // archive replayed on top of it. Stacked because they sum to the reach the run reports, and
  // separated because only the first says the mesh itself got better.
  function drawDelivery(host, entry) {
    const cells = Object.keys(entry.cells);
    const onAir = latestOf(entry, 'text_on_air');
    const total = latestOf(entry, 'text');
    const live = cells.filter((c) => onAir[c] != null || total[c] != null);
    host.textContent = '';
    if (!live.length) return 0;
    const W = 640, LEFT = 132, RIGHT = 24, PLOT = W - LEFT - RIGHT;
    const H = 30 + live.length * 26;
    const svg = el('svg', {viewBox: `0 0 ${W} ${H}`, width: '100%', height: H,
                           style: 'max-width:100%;height:auto;font-size:10.5px'});
    const top = Math.max(1e-9, Math.max.apply(null, live.map(
      (c) => Math.max(total[c] == null ? 0 : total[c], onAir[c] == null ? 0 : onAir[c]))) * 1.1);
    live.forEach((cell, i) => {
      const y = 12 + i * 26;
      const label = el('text', {x: LEFT - 8, y: y + 12, 'text-anchor': 'end',
                                style: 'fill:var(--muted)'});
      label.textContent = cell;
      svg.appendChild(label);
      const air = onAir[cell] == null ? total[cell] : onAir[cell];
      const held = total[cell] == null ? air : total[cell];
      const extra = Math.max(0, held - air);
      const wAir = (air / top) * PLOT, wExtra = (extra / top) * PLOT;
      const first = el('rect', {x: LEFT, y: y + 2, width: Math.max(0, wAir), height: 15,
                                style: 'fill:var(--accent);fill-opacity:.75'});
      first.appendChild(el('title', {})).textContent = `${cell}: ${air.toFixed(3)} on air`;
      svg.appendChild(first);
      if (extra > 0) {
        const second = el('rect', {x: LEFT + wAir, y: y + 2, width: wExtra, height: 15,
                                   style: 'fill:var(--warn);fill-opacity:.85'});
        second.appendChild(el('title', {})).textContent =
          `${cell}: +${extra.toFixed(3)} overheard replay, ${held.toFixed(3)} held`;
        svg.appendChild(second);
      }
      const value = el('text', {x: LEFT + wAir + wExtra + 6, y: y + 13,
                                style: 'fill:var(--muted)'});
      value.textContent = extra > 0
        ? `${air.toFixed(3)} + ${extra.toFixed(3)}` : air.toFixed(3);
      svg.appendChild(value);
    });
    host.appendChild(svg);
    return 1;
  }

  function latestOf(entry, metric) {
    // The last run that has a number for a cell is the one the bars show; a cell missing from the
    // latest run keeps its most recent value rather than vanishing.
    const out = {};
    Object.keys(entry.cells).forEach((c) => {
      const s = entry.cells[c][metric] || [];
      for (let i = s.length - 1; i >= 0; i--) if (s[i] !== null) { out[c] = s[i]; break; }
    });
    return out;
  }

  const fmt = (v, places) =>
    Math.abs(v) >= 100 ? v.toFixed(0) : v.toFixed(places === undefined ? 3 : places);

  // One group per cell, one bar per selected metric, sharing a y axis. Only ever called with
  // metrics of a single unit family, because heights side by side are a claim that they compare.
  function drawFamily(entry, metrics, unit) {
    const cells = Object.keys(entry.cells);
    if (!cells.length) return null;
    const latest = {};
    metrics.forEach((m) => { latest[m] = latestOf(entry, m); });
    const has = (m, c) => latest[m][c] !== undefined && latest[m][c] !== null;
    // A metric this block has no number for is dropped, not drawn flat at zero: an absent
    // measurement and a measured zero are different findings.
    const live = metrics.filter((m) => cells.some((c) => has(m, c)));
    if (!live.length) return null;
    const values = [];
    cells.forEach((c) => live.forEach((m) => { if (has(m, c)) values.push(latest[m][c]); }));
    if (!values.length) return null;

    const turn = cells.some((c) => c.length > 7) || cells.length > 5;
    const W = 640, padL = 54, padR = 14;
    const padT = live.length > 1 ? 32 : 14, padB = turn ? 74 : 32;
    const H = padT + 180 + padB;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    let hi = Math.max(...values, 0), lo = Math.min(...values, 0);
    // A share is read against its ceiling; letting the tallest bar fill the panel turns 0.31 into
    // a full-height bar and reads as success.
    if (unit === 'share') hi = Math.max(hi, 1);
    if (hi === lo) hi = lo + 1;
    const span = hi - lo;
    const yOf = (v) => padT + plotH - (v - lo) / span * plotH;
    const places = meta.places[live[0]];

    const svg = el('svg', {viewBox: `0 0 ${W} ${H}`, width: '100%', height: H,
                           style: 'max-width:100%;height:auto;font-size:11px'});
    for (let t = 0; t <= 4; t++) {
      const v = lo + (span * t) / 4, y = yOf(v);
      svg.appendChild(el('line', {x1: padL, y1: y, x2: padL + plotW, y2: y,
                                  style: 'stroke:var(--border)' + (v === 0 ? '' : ';opacity:.45')}));
      const lab = el('text', {x: padL - 7, y: y + 3.5, 'text-anchor': 'end',
                              style: 'fill:var(--muted)'});
      lab.textContent = fmt(v, places);
      svg.appendChild(lab);
    }
    if (live.length > 1) {
      let lx = padL;
      live.forEach((m) => {
        svg.appendChild(el('rect', {x: lx, y: 6, width: 9, height: 9, rx: 1.5,
                                    style: 'fill:' + (meta.colours[m] || 'var(--accent)')}));
        const lab = el('text', {x: lx + 13, y: 14.5, style: 'fill:var(--muted)'});
        lab.textContent = meta.labels[m] || m;
        svg.appendChild(lab);
        lx += 26 + 6.4 * (meta.labels[m] || m).length;
      });
    }
    const gw = plotW / cells.length;
    const barW = Math.max(2.5, (gw * 0.76) / live.length);
    const naming = cells.length * live.length <= 8;
    cells.forEach((c, i) => {
      const mid = padL + i * gw + gw / 2;
      const base = mid - (barW * live.length) / 2;
      live.forEach((m, k) => {
        if (!has(m, c)) return;
        const v = latest[m][c], top = yOf(v), zero = yOf(Math.max(lo, 0));
        const bar = el('rect', {x: base + k * barW + 0.5, y: Math.min(top, zero),
                                width: Math.max(1, barW - 1), height: Math.abs(zero - top) || 1,
                                rx: 1.5, style: 'fill:' + (meta.colours[m] || 'var(--accent)')});
        const title = el('title', {});
        const run = entry.cells[c][m] || [];
        const seen = run.filter((n) => n !== null);
        const sd = ((entry.sd || {})[c] || {})[m];
        title.textContent = `${c} · ${meta.labels[m] || m} = ${fmt(v, meta.places[m])}` +
          (sd ? ` ± ${fmt(sd, meta.places[m])} across seeds` : '') +
          (seen.length > 1 ? ` (${entry.runs.length} runs: ${seen.join(', ')})` : '');
        bar.appendChild(title);
        svg.appendChild(bar);
        // One standard deviation across the seeds of this cell. A bar without it invites reading
        // a gap the draw could have produced as a result the arm produced.
        if (sd) {
          const cx = base + k * barW + barW / 2;
          const hiY = yOf(v + sd), loY = yOf(v - sd);
          const cap = Math.max(2, Math.min(4, barW / 3));
          const stroke = 'stroke:var(--text);stroke-width:1;opacity:.55';
          svg.appendChild(el('line', {x1: cx, y1: hiY, x2: cx, y2: loY, style: stroke}));
          [hiY, loY].forEach((yy) => svg.appendChild(
            el('line', {x1: cx - cap, y1: yy, x2: cx + cap, y2: yy, style: stroke})));
        }
        if (naming) {
          const num = el('text', {x: base + k * barW + barW / 2, y: Math.min(top, zero) - 4,
                                  'text-anchor': 'middle', style: 'fill:var(--text)'});
          num.textContent = fmt(v, meta.places[m]);
          svg.appendChild(num);
        }
      });
      // Rotated only when the names would otherwise collide, so a two-cell block stays level.
      const name = c.length > 22 ? c.slice(0, 21) + '…' : c;
      const tick = turn
        ? el('text', {x: mid, y: padT + plotH + 8, 'text-anchor': 'end',
                      transform: `rotate(-34 ${mid} ${padT + plotH + 8})`,
                      style: 'fill:var(--muted)'})
        : el('text', {x: mid, y: padT + plotH + 14, 'text-anchor': 'middle',
                      style: 'fill:var(--muted)'});
      tick.textContent = name;
      svg.appendChild(tick);
    });
    svg.appendChild(el('line', {x1: padL, y1: yOf(Math.max(lo, 0)), x2: padL + plotW,
                                y2: yOf(Math.max(lo, 0)), style: 'stroke:var(--border)'}));
    return {svg: svg, live: live};
  }

  // A mark per role, ordered by how much the node relays: a filled square relays everything, a
  // hollow dot relays nothing. Same shapes meshmap.py draws, so the two pictures read alike.
  function roleMark(shape, cx, cy, r, fill) {
    if (shape === 'square') {
      return el('rect', {x: cx - r, y: cy - r, width: 2 * r, height: 2 * r,
                         style: `fill:${fill};stroke:var(--muted);stroke-width:.9`});
    }
    if (shape === 'square-open') {
      return el('rect', {x: cx - r, y: cy - r, width: 2 * r, height: 2 * r,
                         style: `fill:none;stroke:${fill};stroke-width:1.6`});
    }
    if (shape === 'diamond') {
      return el('polygon', {points: `${cx},${cy - r} ${cx + r},${cy} ${cx},${cy + r} ${cx - r},${cy}`,
                            style: `fill:${fill};stroke:var(--muted);stroke-width:.9`});
    }
    if (shape === 'circle-open') {
      return el('circle', {cx: cx, cy: cy, r: r, style: `fill:none;stroke:${fill};stroke-width:1.6`});
    }
    return el('circle', {cx: cx, cy: cy, r: r,
                         style: `fill:${fill};stroke:var(--muted);stroke-width:.9`});
  }

  // Nodes sharing a position, fanned onto a small circle around it. Batumi is 92 nodes on 55
  // coordinates, so drawn literally a third of the mesh is invisible; the tooltip says so.
  function fanOut(pts, n) {
    const groups = {}, place = [], stack = [];
    for (let i = 0; i < n; i++) {
      const key = pts[2 * i] + ',' + pts[2 * i + 1];
      (groups[key] = groups[key] || []).push(i);
    }
    Object.keys(groups).forEach((key) => {
      const members = groups[key], count = members.length;
      members.forEach((i, k) => {
        stack[i] = count;
        if (count === 1) { place[i] = [0, 0]; return; }
        const angle = (2 * Math.PI * k) / count, spread = 7 * (count > 8 ? 1.55 : 1);
        place[i] = [spread * Math.cos(angle), spread * Math.sin(angle)];
      });
    });
    return {place: place, stack: stack};
  }

  function drawMap(host, entry) {
    const cells = Object.keys(entry.maps || {});
    host.textContent = '';
    cells.forEach((cell) => {
      const ref = entry.maps[cell];
      const geo = meta.maps[ref.geom];
      if (!geo) return;                 // a digest referencing a geometry it did not carry
      const over = ref.overlay || {};
      const n = geo.n, pts = geo.pts, links = geo.links || [];
      const W = 640, padL = 14, padR = 14, padT = 34, padB = 46;
      const H = 470;
      let mx = 1, my = 1;
      for (let i = 0; i < n; i++) { mx = Math.max(mx, pts[2 * i]); my = Math.max(my, pts[2 * i + 1]); }
      // One scale for both axes, so the picture is not a stretched version of the geometry.
      const scale = Math.min((W - padL - padR) / mx, (H - padT - padB) / my);
      const ox = padL + ((W - padL - padR) - mx * scale) / 2;
      const oy = padT + ((H - padT - padB) - my * scale) / 2;
      const fan = fanOut(pts, n);
      // SVG y grows downward; the mesh's does not.
      const at = (i) => [ox + pts[2 * i] * scale + fan.place[i][0],
                         oy + (my - pts[2 * i + 1]) * scale + fan.place[i][1]];

      const svg = el('svg', {viewBox: `0 0 ${W} ${H}`, width: '100%', height: H,
                             style: 'max-width:100%;height:auto;font-size:10.5px'});
      const head = el('text', {x: 14, y: 16, style: 'fill:var(--text)'});
      head.textContent = `${cell} · ${n} nodes, ${geo.links_total} link(s)`
        + ((over.servers || []).length ? `, ${over.servers.length} archive(s)` : '');
      svg.appendChild(head);
      const sub = el('text', {x: 14, y: 29, style: 'fill:var(--muted)'});
      sub.textContent = `${geo.preset} · sensitivity ${geo.sensitivity} dBm · `
        + `${geo.extent_km[0]} x ${geo.extent_km[1]} km · a link is drawn where the budget closes;`
        + ` red is under ${geo.fragile_db} dB of margin`;
      svg.appendChild(sub);

      // Two passes - every link faint, the fragile over the top - since 2000 equal links smear.
      const weak = [];
      for (let k = 0; k < links.length; k += 3) {
        const a = at(links[k]), b = at(links[k + 1]), margin = links[k + 2];
        if (margin < geo.fragile_db) {
          weak.push(el('line', {x1: a[0], y1: a[1], x2: b[0], y2: b[1],
                                style: `stroke:${meta.mapcolours.fragile};stroke-width:.8;opacity:.45`}));
        } else {
          const alpha = (0.06 + 0.16 * Math.min(1, margin / 25)).toFixed(2);
          svg.appendChild(el('line', {x1: a[0], y1: a[1], x2: b[0], y2: b[1],
                                      style: `stroke:${meta.mapcolours.link};stroke-width:.7;opacity:${alpha}`}));
        }
      }
      weak.forEach((l) => svg.appendChild(l));

      const servers = over.servers || [], designated = over.designated || [];
      const seen = {};
      for (let i = 0; i < n; i++) {
        const p = at(i);
        const idx = (over.role_of || [])[i];
        const mark = meta.rolemarks[idx === undefined ? meta.rolemarks.length - 1 : idx]
                     || meta.rolemarks[meta.rolemarks.length - 1];
        seen[mark[0]] = (seen[mark[0]] || 0) + 1;
        // A designated-but-archiveless node is the `--protocol none` control: ringed, not filled.
        if (designated.indexOf(i) >= 0 && servers.indexOf(i) < 0) {
          svg.appendChild(el('circle', {cx: p[0], cy: p[1], r: 10,
                                        style: `fill:none;stroke:${meta.mapcolours.fragile};stroke-width:1.4;stroke-dasharray:3 2`}));
        }
        if (servers.indexOf(i) >= 0) {
          // Outside the role mark rather than replacing it: an archive on a router and one on a
          // muted client are different deployments, and one ring cannot tell them apart.
          svg.appendChild(el('circle', {cx: p[0], cy: p[1], r: 10.5,
                                        style: `fill:none;stroke:${meta.mapcolours.fragile};stroke-width:2.2`}));
        }
        const node = roleMark(mark[1], p[0], p[1], 5, mark[2]);
        const title = el('title', {});
        title.textContent = `node ${i} · ${mark[0]}`
          + (servers.indexOf(i) >= 0 ? ' · archive' : '')
          + (fan.stack[i] > 1
              ? ` · shares a position with ${fan.stack[i] - 1} other(s), fanned out to be visible`
              : '');
        node.appendChild(title);
        svg.appendChild(node);
      }

      let lx = 14;
      meta.rolemarks.forEach((mark) => {
        if (!seen[mark[0]]) return;     // only the roles this mesh has
        svg.appendChild(roleMark(mark[1], lx + 5, H - 20, 5, mark[2]));
        const lab = el('text', {x: lx + 15, y: H - 16, style: 'fill:var(--muted)'});
        lab.textContent = `${mark[0]} ${seen[mark[0]]}`;
        svg.appendChild(lab);
        lx += 30 + 6.4 * (mark[0].length + String(seen[mark[0]]).length);
      });
      if (geo.links_dropped) {
        const note = el('text', {x: W - 14, y: H - 6, 'text-anchor': 'end', style: 'fill:var(--muted)'});
        note.textContent = `${geo.links_dropped} link(s) not stored (over the cap)`;
        svg.appendChild(note);
      }
      const cap = document.createElement('p');
      cap.className = 'axislabel';
      cap.textContent = `mesh map · ${cell}` + (ref.run ? ` · ${ref.run}` : '')
        + (ref.seed !== undefined && ref.seed !== null ? ` · seed ${ref.seed}` : '');
      host.appendChild(cap);
      host.appendChild(svg);
    });
  }

  // One metric, every block that has it, on ONE scale. The per-block panels each scale to their
  // own numbers, which is right when reading a block and wrong when comparing two: a 0.09 bar and
  // a 0.87 bar both reach the top of their own chart. Here they cannot.
  // One or more measures, every block that has them, one scale per unit. Ticking several puts
  // their bars beside each other within a cell, which is the comparison a single-choice picker
  // could not make: two measures on two charts have two scales and no shared row.
  function drawAcross(host, metrics, wanted) {
    host.textContent = '';
    // The compositions come first and are drawn per block rather than as bars: a pie has no scale
    // to share, so it is stacked down the page the way the bar families are.
    const pies = metrics.filter((m) => m === '__pies' || m === '__srpies');
    metrics = metrics.filter((m) => m.indexOf('__') !== 0 || m === '__delivery');
    if (pies.length) {
      const names = Object.keys(data).filter(
        (n) => !wanted.length || wanted.indexOf(n) >= 0).sort();
      pies.forEach((which) => {
        const cap = document.createElement('p');
        cap.className = 'axislabel';
        cap.textContent = which === '__pies'
          ? 'all traffic by message type · packets against bytes on the air'
          : "the archive's own messages by type · count against bytes";
        host.appendChild(cap);
        names.forEach((name) => {
          const row = document.createElement('div');
          row.className = 'stackrow';
          const head = document.createElement('p');
          head.className = 'axislabel';
          head.textContent = name;
          row.appendChild(head);
          const box = document.createElement('div');
          row.appendChild(box);
          host.appendChild(row);
          drawPies(box, data[name],
                   which === '__pies' ? meta.trafficTypes : meta.messageTypes);
        });
      });
    }
    if (!metrics.length) {
      if (!pies.length) {
        host.appendChild(document.createTextNode('tick a measure to draw it'));
      }
      return pies.length;
    }
    const names = Object.keys(data).filter(
      (n) => !wanted.length || wanted.indexOf(n) >= 0).sort();
    // `__delivery` is a composition rather than a measure: its bar is the two halves of text
    // reach stacked, and it lives on the share axis with everything else measured 0-1.
    const partsOf = (m) => (m === '__delivery' ? ['text_on_air', 'text_overheard'] : [m]);
    const unitOf = (m) => (m === '__delivery' ? 'share' : (meta.units[m] || 'other'));
    const labelOf = (m) => (m === '__delivery' ? 'on air + overheard' : (meta.labels[m] || m));
    const placesOf = (m) => (m === '__delivery' ? meta.places.text : meta.places[m]);

    // Split by unit for the same reason the per-block charts do: a share and a percentage on one
    // axis rank collapse instead of measuring it.
    const families = [];
    metrics.forEach((m) => {
      const unit = unitOf(m);
      let fam = families.filter((f) => f.unit === unit)[0];
      if (!fam) { fam = {unit: unit, metrics: []}; families.push(fam); }
      fam.metrics.push(m);
    });

    let drew = 0;
    families.forEach((fam) => {
      const rows = [];
      let hi = 0, lo = 0;
      names.forEach((name) => {
        const entry = data[name];
        const values = {};
        fam.metrics.forEach((m) => partsOf(m).forEach((part) => {
          if (!values[part]) values[part] = latestOf(entry, part);
        }));
        const totals = {};
        const cells = Object.keys(entry.cells);
        const live = [];
        cells.forEach((c) => {
          const per = {};
          let any = false;
          fam.metrics.forEach((m) => {
            const sum = partsOf(m).reduce((acc, part) => {
              const v = values[part][c];
              return v === undefined || v === null ? acc : acc + v;
            }, null);
            if (sum !== null) { per[m] = sum; any = true; hi = Math.max(hi, sum); lo = Math.min(lo, sum); }
          });
          if (any) { totals[c] = per; live.push(c); }
        });
        if (live.length) {
          rows.push({name: name, arm: entry.arm, cells: live, parts: values,
                     totals: totals, sd: entry.sd || {}});
        }
      });
      if (!rows.length) return;
      if (fam.unit === 'share') hi = Math.max(hi, 1);
      if (hi === lo) hi = lo + 1;

      const cap = document.createElement('p');
      cap.className = 'axislabel';
      cap.textContent = (meta.axis[fam.unit] || fam.unit) + ' · ' + rows.length
        + ' block(s), one scale to ' + fmt(hi, placesOf(fam.metrics[0]));
      host.appendChild(cap);
      const key = document.createElement('p');
      key.className = 'sub';
      key.style.margin = '0 0 .4rem';
      key.innerHTML = fam.metrics.map((m) => partsOf(m).map((part) =>
        `<span class="swatch" style="background:${meta.colours[part] || 'var(--accent)'}"></span>` +
        (m === '__delivery' ? (meta.labels[part] || part) : labelOf(m))).join(' ')).join(' &nbsp; ');
      host.appendChild(key);

      rows.forEach((row) => {
        const W = 640, LEFT = 150, RIGHT = 46, PLOT = W - LEFT - RIGHT;
        const BAR = 11, GAP = 2, PAD = 5;
        const group = fam.metrics.length * (BAR + GAP) + PAD;
        const H = 22 + row.cells.length * group + 6;
        const svg = el('svg', {viewBox: `0 0 ${W} ${H}`, width: '100%', height: H,
                               style: 'max-width:100%;height:auto;font-size:10.5px'});
        const head = el('text', {x: 0, y: 10, style: 'fill:var(--text);font-weight:600'});
        head.textContent = row.name;
        svg.appendChild(head);
        const arm = el('text', {x: W, y: 10, 'text-anchor': 'end', style: 'fill:var(--muted)'});
        arm.textContent = row.arm;
        svg.appendChild(arm);
        const at = (v) => LEFT + ((v - lo) / (hi - lo)) * PLOT;
        const zero = at(Math.max(lo, 0));
        row.cells.forEach((c, i) => {
          const top = 22 + i * group;
          const label = el('text', {x: LEFT - 8, y: top + BAR - 1, 'text-anchor': 'end',
                                    style: 'fill:var(--muted)'});
          label.textContent = c.length > 20 ? c.slice(0, 19) + '…' : c;
          svg.appendChild(label);
          fam.metrics.forEach((m, k) => {
            const total = row.totals[c][m];
            if (total === undefined) return;
            const y = top + k * (BAR + GAP);
            let cursor = Math.max(lo, 0);
            partsOf(m).forEach((part) => {
              const seg = row.parts[part][c];
              if (seg === undefined || seg === null) return;
              const from = at(cursor), to = at(cursor + seg);
              const bar = el('rect', {x: Math.min(from, to), y: y, rx: 1.5,
                                      width: Math.max(1, Math.abs(to - from)), height: BAR,
                                      style: 'fill:' + (meta.colours[part] || 'var(--accent)')
                                             + ';fill-opacity:.85'});
              const segSd = (row.sd[c] || {})[part];
              bar.appendChild(el('title', {})).textContent =
                `${row.name} · ${c} · ${meta.labels[part] || part} = ${fmt(seg, placesOf(m))}` +
                (segSd ? ` ± ${fmt(segSd, placesOf(m))} across seeds` : '') +
                (partsOf(m).length > 1 ? `, ${fmt(total, placesOf(m))} together` : '');
              svg.appendChild(bar);
              cursor += seg;
            });
            const sd = (row.sd[c] || {})[m === '__delivery' ? 'text' : m];
            if (sd) {
              const mid = y + BAR / 2;
              const stroke = 'stroke:var(--text);stroke-width:1;opacity:.5';
              svg.appendChild(el('line', {x1: at(total - sd), y1: mid, x2: at(total + sd), y2: mid,
                                          style: stroke}));
              [at(total - sd), at(total + sd)].forEach((x) => svg.appendChild(
                el('line', {x1: x, y1: mid - 2.5, x2: x, y2: mid + 2.5, style: stroke})));
            }
            const num = el('text', {x: Math.max(at(total), zero) + 5, y: y + BAR - 1,
                                    style: 'fill:var(--text)'});
            num.textContent = fmt(total, placesOf(m));
            svg.appendChild(num);
          });
        });
        svg.appendChild(el('line', {x1: zero, y1: 18, x2: zero, y2: H - 4,
                                    style: 'stroke:var(--border)'}));
        const box = document.createElement('div');
        box.className = 'stackrow';
        box.appendChild(svg);
        host.appendChild(box);
      });
      drew += rows.length;
    });
    if (!drew) {
      host.appendChild(document.createTextNode('no block on this page records that measure'));
    }
    return drew;
  }


  // The protocol's traffic by message type, as two pies per cell: how many messages, and how many
  // bytes. Counts and bytes rank the types differently, which is the reason both are drawn.
  function drawPies(host, entry, types) {
    const cells = Object.keys(entry.cells);
    host.textContent = '';
    let drew = 0;
    const grid = document.createElement('div');
    grid.className = 'piegrid';
    cells.forEach((cell) => {
      const counts = types.map((t) => (latestOf(entry, t.count) || {})[cell] || 0);
      const bytes = types.map((t) => (latestOf(entry, t.bytes) || {})[cell] || 0);
      const totalCount = counts.reduce((a, b) => a + b, 0);
      const totalBytes = bytes.reduce((a, b) => a + b, 0);
      if (!totalCount && !totalBytes) return;
      drew++;
      const box = document.createElement('div');
      box.className = 'piecell';
      const title = document.createElement('p');
      title.className = 'axislabel';
      title.textContent = cell;
      box.appendChild(title);
      const pair = document.createElement('div');
      pair.className = 'piepair';
      [[counts, totalCount, 'messages', 0], [bytes, totalBytes, 'bytes', 0]].forEach(
        ([values, total, what]) => {
          const R = 46, W = 150, H = 128;
          const svg = el('svg', {viewBox: `0 0 ${W} ${H}`, width: '100%', height: H,
                                 style: 'max-width:100%;height:auto;font-size:9.5px'});
          const cx = W / 2, cy = 56;
          if (!total) {
            svg.appendChild(el('circle', {cx: cx, cy: cy, r: R,
                                          style: 'fill:none;stroke:var(--border)'}));
          } else {
            let from = -Math.PI / 2;
            values.forEach((v, i) => {
              if (!v) return;
              const sweep = (v / total) * Math.PI * 2;
              const to = from + sweep;
              // A full circle cannot be an arc - its two endpoints are the same point, and the
              // path degenerates to nothing. One type accounting for everything is not rare here.
              const node = sweep >= Math.PI * 2 - 1e-9
                ? el('circle', {cx: cx, cy: cy, r: R, style: `fill:${types[i].colour}`})
                : el('path', {d: `M ${cx} ${cy} L ${cx + R * Math.cos(from)} `
                                 + `${cy + R * Math.sin(from)} A ${R} ${R} 0 `
                                 + `${sweep > Math.PI ? 1 : 0} 1 `
                                 + `${cx + R * Math.cos(to)} ${cy + R * Math.sin(to)} Z`,
                              style: `fill:${types[i].colour};stroke:var(--panel-bg);stroke-width:.8`});
              node.appendChild(el('title', {})).textContent =
                `${cell} · ${types[i].label} ${what}: ${fmt(v, 0)} (${(100 * v / total).toFixed(1)}%)`;
              svg.appendChild(node);
              from = to;
            });
          }
          const cap = el('text', {x: cx, y: H - 8, 'text-anchor': 'middle',
                                  style: 'fill:var(--muted)'});
          cap.textContent = `${what} · ${fmt(total, 0)}`;
          svg.appendChild(cap);
          pair.appendChild(svg);
        });
      box.appendChild(pair);
      grid.appendChild(box);
    });
    if (!drew) {
      host.appendChild(document.createTextNode('this block records no protocol messages'));
      return 0;
    }
    const key = document.createElement('p');
    key.className = 'sub';
    key.style.margin = '0 0 .5rem';
    key.innerHTML = types.map((t) =>
      `<span class="swatch" style="background:${t.colour}"></span>${t.label}`).join(' &nbsp; ');
    host.appendChild(key);
    host.appendChild(grid);
    return drew;
  }

  // The campaign panel's maps: one per recipe, drawn from the geometry a cell of it carried.
  (function () {
    const hosts = Array.from(document.querySelectorAll('.campaignmap'));
    if (!hosts.length) return;
    hosts.forEach((host) => {
      const ref = (meta.recipeMaps || {})[host.dataset.recipe];
      if (!ref) {
        host.appendChild(document.createTextNode(
          'no mesh map in this digest - collate with --maps to draw one'));
        return;
      }
      // drawMap takes an entry keyed by cell name; the campaign has one picture per recipe, so
      // the key is the recipe's own label rather than a cell's.
      drawMap(host, {maps: {'the mesh': ref}});
    });
  })();

  // The cross-block page: any number of measures, over any number of blocks.
  (function () {
    const host = document.getElementById('stackchart');
    if (!host) return;
    const metricPicks = Array.from(document.querySelectorAll('input.stackmetric'));
    const blockPicks = Array.from(document.querySelectorAll('input.stackblock'));
    if (!metricPicks.length) return;
    const render = () => {
      // DOM order, not tick order, so the bars within a cell keep one order however they were
      // chosen - and that order is the one the tables use.
      const metrics = metricPicks.filter((b) => b.checked).map((b) => b.value);
      const wanted = blockPicks.filter((b) => b.checked).map((b) => b.value);
      drawAcross(host, metrics, wanted);
      try {
        localStorage.setItem('sfpp-stack', JSON.stringify(metrics));
      } catch (e) { /* a page in a sandbox may refuse storage; the chart does not depend on it */ }
    };
    try {
      const last = JSON.parse(localStorage.getItem('sfpp-stack') || 'null');
      if (Array.isArray(last) && last.length) {
        metricPicks.forEach((b) => { b.checked = last.indexOf(b.value) >= 0; });
      }
    } catch (e) { /* as above */ }
    metricPicks.forEach((b) => b.addEventListener('change', render));
    blockPicks.forEach((b) => b.addEventListener('change', render));
    const toggle = (picks, button) => {
      if (!button) return;
      button.addEventListener('click', () => {
        const turnOn = picks.some((b) => !b.checked);
        picks.forEach((b) => { b.checked = turnOn; });
        render();
      });
    };
    toggle(blockPicks, document.getElementById('stackall'));
    toggle(metricPicks, document.getElementById('stackallmetrics'));
    render();
  })();

  function draw(host, block, selected) {
    const entry = data[block];
    host.textContent = '';
    if (!entry) return;
    const nodes = selected.indexOf('__nodes') >= 0;
    const wantMap = selected.indexOf('__map') >= 0;
    const wantDelivery = selected.indexOf('__delivery') >= 0;
    const wantPies = selected.indexOf('__pies') >= 0;
    const bars = selected.filter((m) => m.indexOf('__') !== 0);
    // Split by unit, in the order the fields are offered: a selection mixing a share with a
    // percentage draws two charts rather than one chart nobody can read a height off.
    const families = [];
    bars.forEach((m) => {
      const unit = meta.units[m] || 'other';
      let fam = families.filter((f) => f.unit === unit)[0];
      if (!fam) { fam = {unit: unit, metrics: []}; families.push(fam); }
      fam.metrics.push(m);
    });
    let drew = 0;
    // A one-metric family is a single column of bars and does not need the width of a page. They
    // share a row where two will fit; a family carrying several series keeps the full width,
    // because its bars have to be comparable by eye across the whole axis.
    const grid = document.createElement('div');
    grid.className = 'chartgrid';
    families.forEach((fam) => {
      const got = drawFamily(entry, fam.metrics, fam.unit);
      if (!got) return;
      const box = document.createElement('div');
      box.className = got.live.length > 1 ? 'chartcell wide' : 'chartcell';
      const cap = document.createElement('p');
      cap.className = 'axislabel';
      // Named from what was drawn, not what was ticked, so a metric this block has no numbers
      // for does not appear in the caption of a chart it is absent from.
      cap.textContent = (meta.axis[fam.unit] || fam.unit)
        + (got.live.length === 1 ? ' · ' + (meta.labels[got.live[0]] || got.live[0]) : '');
      box.appendChild(cap);
      box.appendChild(got.svg);
      grid.appendChild(box);
      drew++;
    });
    if (grid.childNodes.length) host.appendChild(grid);
    if (wantDelivery) {
      const box = document.createElement('div');
      const cap = document.createElement('p');
      cap.className = 'axislabel';
      cap.textContent = 'text delivery · first chance on air, then overheard replay';
      host.appendChild(cap);
      host.appendChild(box);
      drew += drawDelivery(box, entry);
    }
    if (wantPies) {
      const box = document.createElement('div');
      const cap = document.createElement('p');
      cap.className = 'axislabel';
      cap.textContent = 'all traffic by message type · packets against bytes on the air';
      host.appendChild(cap);
      host.appendChild(box);
      drew += drawPies(box, entry, meta.trafficTypes);
    }
    if (selected.indexOf('__srpies') >= 0) {
      const box = document.createElement('div');
      const cap = document.createElement('p');
      cap.className = 'axislabel';
      cap.textContent = "the archive's own messages by type · count against bytes";
      host.appendChild(cap);
      host.appendChild(box);
      drew += drawPies(box, entry, meta.messageTypes);
    }
    if (nodes) {
      const box = document.createElement('div');
      host.appendChild(box);
      drawNodes(box, entry);
      drew++;
    }
    if (wantMap && entry.maps) {
      const box = document.createElement('div');
      host.appendChild(box);
      drawMap(box, entry);
      drew++;
    }
    if (!drew) {
      host.appendChild(document.createTextNode(
        selected.length ? 'no numbers recorded for this block' : 'tick a field to draw it'));
    }
  }

  // The last set ticked becomes the default for the next panel opened: with fifty blocks on one
  // page, re-ticking the same three fields per panel is the entire cost of the control.
  let sticky = null;
  document.querySelectorAll('details[data-chart]').forEach((box) => {
    const block = box.getAttribute('data-chart');
    const host = box.querySelector('.chart');
    const picks = Array.from(box.querySelectorAll('input.metric'));
    const chosen = () => picks.filter((b) => b.checked).map((b) => b.value);
    let drawn = false;
    box.addEventListener('toggle', () => {
      if (!box.open || drawn) return;
      if (sticky) {
        // Only fields this panel offers: `__nodes` and `__delivery` exist where the digest
        // carried the vectors and the split respectively.
        const offered = picks.map((b) => b.value);
        const want = sticky.filter((v) => offered.indexOf(v) >= 0);
        if (want.length) picks.forEach((b) => { b.checked = want.indexOf(b.value) >= 0; });
      }
      draw(host, block, chosen());
      drawn = true;
    });
    picks.forEach((b) => b.addEventListener('change', () => {
      sticky = chosen();
      if (box.open) draw(host, block, chosen());
    }));
  });
})();
// Auto -> Light -> Dark, stamped on the root element. Auto removes the attribute and lets
// prefers-color-scheme decide. aria-pressed stays "false" per the site's convention.
(function () {
  const btn = document.getElementById('toggle-theme-btn');
  if (!btn) return;
  const modes = ['Auto', 'Light', 'Dark'];
  let i = 0;
  btn.addEventListener('click', () => {
    i = (i + 1) % modes.length;
    const mode = modes[i];
    if (mode === 'Auto') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', mode.toLowerCase());
    btn.textContent = 'Theme: ' + mode;
  });
})();
(function () {
  const btn = document.getElementById('toggle-license-btn');
  const block = document.getElementById('attribution');
  if (!btn || !block) return;
  btn.addEventListener('click', () => {
    const shown = !block.hidden;
    block.hidden = shown;
    btn.setAttribute('aria-expanded', String(!shown));
    btn.textContent = (shown ? 'Show' : 'Hide') + ' license';
  });
})();
// Tabs. The body only gets `tabbed` once this runs, so a browser with JS off never hides a panel.
(function () {
  const nav = document.querySelector('.tabs');
  const panels = Array.from(document.querySelectorAll('.tab-panel'));
  if (!nav || !panels.length) return;
  const buttons = Array.from(nav.querySelectorAll('button[data-tab]'));
  document.body.classList.add('tabbed');
  function show(name) {
    for (const p of panels) p.hidden = p.dataset.tab !== name;
    for (const b of buttons) b.setAttribute('aria-selected', String(b.dataset.tab === name));
    if (location.hash.slice(1) !== name) history.replaceState(null, '', '#' + name);
  }
  for (const b of buttons) b.addEventListener('click', () => show(b.dataset.tab));
  const wanted = location.hash.slice(1);
  show(buttons.some((b) => b.dataset.tab === wanted) ? wanted : buttons[0].dataset.tab);
})();
const q = document.getElementById('q');
const sc = document.getElementById('scenario');
function apply() {
  if (!q || !sc) return;
  const needle = (q.value || '').toLowerCase();
  const scen = sc.value;
  for (const el of document.querySelectorAll('[data-block]')) {
    const hitText = !needle || el.dataset.block.toLowerCase().includes(needle)
                            || el.dataset.arm.toLowerCase().includes(needle);
    const hitScen = scen === 'all' || (el.dataset.scenarios || '').split('|').includes(scen);
    el.classList.toggle('hidden', !(hitText && hitScen));
  }
}
if (q) q.addEventListener('input', apply);
if (sc) sc.addEventListener('change', apply);
"""


def render_distributions(run):
    """The six-number distributions for one run's cells, as a range per cell.

    Six columns per statistic would be forty-odd columns a reader has to scan; a range with the
    median marked is the same information in the shape the question is asked in - how far apart are
    the best and worst served node, and where does the middle sit between them. min and max are the
    ends, p10 and p90 the inner ticks, and the mean is given as a number because a mean that sits
    off the median is the finding.
    """
    cells = run.get("dist") or {}
    if not cells:
        return []
    paths = sorted({p for row in cells.values() for p in row})
    out = [
        '<p class="sub" style="margin:.75rem 0 .35rem;font-size:.8rem">'
        "distributions, same run - min <span class=\"mono\">|</span> p10 &middot; median "
        "&middot; p90 <span class=\"mono\">|</span> max, mean in brackets</p>",
        '<div class="scroll"><table><thead><tr><th>value</th>',
    ]
    out += [f'<th>{_esc(p.split(".")[-1])}<br><span class="sub">{_esc(p)}</span></th>' for p in paths]
    out.append("</tr></thead><tbody>")
    for value, row in cells.items():
        out.append(f'<tr><td class="mono">{_esc(value)}</td>')
        for path in paths:
            d = row.get(path)
            if not d:
                out.append('<td class="never">-</td>')
                continue
            out.append(
                '<td class="mono" style="white-space:nowrap">'
                f'{_fmt(d.get("min"), 3)} <span class="sub">|</span> {_fmt(d.get("p10"), 3)} '
                f'&middot; <b>{_fmt(d.get("median"), 3)}</b> &middot; {_fmt(d.get("p90"), 3)} '
                f'<span class="sub">|</span> {_fmt(d.get("max"), 3)} '
                f'<span class="sub">({_fmt(d.get("mean"), 3)})</span></td>'
            )
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return out


# What every column on this page counts, and against what. Four columns rather than two, because
# the denominator is the half that gets misread: `text` and `dm` are both "did it arrive" and they
# divide by different things, so a reader comparing the two numbers is comparing nothing.
GLOSSARY = [
    (
        "delivery - what arrived, and by which route",
        [
            (
                "text",
                "share of broadcast texts a node <b>holds</b>, however it got there - the "
                "on-air and overheard columns below sum to this",
                "every node, every broadcast text",
            ),
            (
                "on air",
                "of those, what the <b>broadcast itself</b> delivered. First chance. This is the "
                "one to quote when asking whether the mesh got better, and it is what an arm is "
                "priced against",
                "every node, every broadcast text",
            ),
            (
                "overheard",
                "of those, what was filed from an <b>overheard replay</b> - a bystander keeping an "
                "archived object it was never sent, because the replay header sits outside the "
                "encryption wrapper. Zero for a protocol that puts no replay on the air",
                "every node, every broadcast text",
            ),
            (
                "worst node",
                "the least-served node's text reach. <b>Prefer it to the mean</b>: the mean is "
                "carried by the middle of a mesh, and the archive argument is about the edge",
                "one node, every broadcast text",
            ),
            (
                "DM",
                "did the direct message reach <b>the one node it was addressed to</b>? A bystander "
                "hearing it relayed it; that is not delivery",
                "DMs that reached the air",
            ),
            (
                "admin",
                "did the operator's change take, within the attempts they made? Both legs - the "
                "request and the reply - must land inside the firmware's 300 s window",
                "sessions the operator wanted",
            ),
        ],
    ),
    (
        "inventory - what an archive has",
        [
            (
                "held",
                "what one archive <b>holds</b>, averaged over the archives. <b>Not a delivery "
                "measure</b>: there is no client hydration path, so nothing here models a user "
                "asking a server for what they missed",
                "objects originated",
            ),
            (
                "union",
                "what <b>all archives together</b> hold - the ceiling reconciliation is working "
                "towards. A high union beside a low held means the copies have diverged",
                "objects originated",
            ),
        ],
    ),
    (
        "cost - what it spent to get there",
        [
            (
                "demand",
                "every node's transmit time summed over elapsed time - <b>aggregate demand, not a "
                "busy fraction</b>. Unbounded: above 1.0 is normal, because spatial reuse means "
                "most transmissions never overlap at any one receiver",
                "elapsed time (1.0 = one channel-second asked for per second)",
            ),
            (
                "chutil p90/max",
                "<code>AirTime::channelUtilizationPercent</code> per node - what a real device "
                "reports and what sizes its contention window. <b>Quote this one when asking "
                "whether a mesh is busy</b>",
                "wall-clock, per node (0-100%)",
            ),
            (
                "airutil max",
                "<code>node_air_util_tx_percent</code>: what the busiest node would have to "
                "declare as its own transmit duty",
                "wall-clock, per node (0-100%)",
            ),
            (
                "SR air",
                "reconciliation's share of all channel airtime - the archive's bill, separated "
                "from the traffic it is carried alongside",
                "total airtime on the mesh",
            ),
            (
                "price",
                "on the ranking table: how much more of something an arm spent across its cells, "
                "as a ratio - bytes on air, advert bytes or SR bytes, whichever moved furthest",
                "the arm's own lowest cell",
            ),
        ],
    ),
    (
        "the run itself",
        [
            (
                "placed",
                "archives actually sited against the number asked for. A role-bounded placement "
                "quietly returning fewer is how &ldquo;6 servers&rdquo; and &ldquo;4 servers&rdquo; "
                "become one row",
                "archives requested",
            ),
            (
                "moved",
                "on the ranking table: which delivery measure this block travels in. The four have "
                "four denominators and <b>are not comparable to each other</b>",
                "-",
            ),
            (
                "spread",
                "the distance between the arm's lowest and highest cell on whichever measure it "
                "moved - how much the variable is worth at all",
                "-",
            ),
            (
                "cells",
                "how many values of the arm this block ran. A block with two cells states a "
                "difference; one with six states a shape",
                "-",
            ),
        ],
    ),
]


def render_glossary():
    """Every column on this page, what it counts and what it counts against.

    The denominator column is the point: `text` and `dm` are both shares and neither divides by
    what the other does, so the commonest misreading of this tool is treating one as a proxy for
    the other. README §7.3 is the same statement at length.
    """
    out = [
        '<div class="panel" id="making-terms">',
        '<div class="blockhead"><h3>What each term means</h3>'
        '<span class="arm">every column on this page</span>'
        '<span class="pill">four denominators</span></div>',
        "<p>Four questions, four denominators, and <b>they are not comparable to each other</b>. A "
        "DM figure higher than a text figure does not mean DMs work better - a DM needs to reach one "
        "node and gets retries, while text reach is the share of <i>all</i> nodes that heard it.</p>",
        # No `scroll` wrapper: this is prose in a table, and prose wraps. A horizontal scrollbar
        # on a glossary hides the half of every row that says what the term is counted against.
        '<table class="glossary"><thead><tr>'
        "<th>column</th><th>what it counts</th><th>out of</th></tr></thead><tbody>",
    ]
    for heading, rows in GLOSSARY:
        out.append(f'<tr class="head"><td colspan="3">{_esc(heading)}</td></tr>')
        for term, meaning, denominator in rows:
            out.append(
                f"<tr><td>{_esc(term)}</td><td>{meaning}</td><td>{denominator}</td></tr>"
            )
    out += [
        "</tbody></table>",
        '<p class="sub" style="margin:.8rem 0 0">Every per-node quantity on this page is reported as '
        "min / p10 / median / mean / p90 / max. The mean alone cannot say whether a mesh serves its "
        "worst node, which is the question the archive exists to answer.</p>",
        "</div>",
    ]
    return out


def render_making():
    """What produced the runs on this page: two styles of question, three workflows asking them.

    Static prose, not derived from the archive. It is here because the page mixes producers - one
    block list holds both `<DD>-subject` and `batumi-...` cells - and nothing else on the page says
    why, or which of the two a row came from.
    """
    # (anchor, nav label, panel html). The index below is built from this list rather than written
    # beside it, so a section cannot be added without appearing in the index or renamed out of it.
    sections = [
        (
            "making-sweep",
            "The mechanism sweep",
            [
                '<div class="panel" id="making-sweep">',
        "<div class=\"blockhead\"><h3>1. The mechanism sweep</h3>"
        '<span class="arm">synthetic mesh</span><span class="pill">nightly 02:10 UTC</span>'
        '<span class="pill">runs/blocks-&lt;date&gt;-&lt;seed&gt;</span></div>',
        "<p><b>What does this one variable do to a mesh?</b> Every block <code>sfpp.sweep</code> "
        "declares - 87 of them - against a generated mesh, with one landform and one seed base drawn "
        "for the whole night so every block that night saw the same draw. One arm moves per block; "
        "everything else is held. Each block is its own job, because a single job running all 87 in "
        "sequence is about six hours of simulator time and one slow block would take the night down "
        "with it.</p>",
        "<p>Cells are named <code class=\"mono\">&lt;DD&gt;-subject</code> - a two-letter domain and a "
        "kebab tail, <code>RF-preset-turbo</code>, <code>SF-capacity</code>, <code>DG-outage</code>. "
        "The archive is switched <b>on in every cell</b>, so this style can say what a variable does "
        "and can never say what the archive itself is worth.</p>",
                "</div>",
            ],
        ),
        (
            "making-ground",
            "Real ground",
            [
                '<div class="panel" id="making-ground">',
        "<div class=\"blockhead\"><h3>2. Real ground</h3>"
        '<span class="arm">Batumi, real geometry and terrain</span>'
        '<span class="pill">two workflows</span>'
        '<span class="pill">runs/matrix-&lt;date&gt;, runs/design-&lt;date&gt;-&lt;seed&gt;</span></div>',
        "<p>Both run over a real node snapshot with matching terrain, so their cells are named for the "
        "ground rather than a domain: <code class=\"mono\">batumi-x1-LONG_FAST</code>, "
        "<code class=\"mono\">batumi-coding-rate-ladder</code> - scenario, mirror count, then the thing "
        "being varied. They predate the domain scheme and are not governed by it.</p>",
        "<p>They are heavier than the mechanism sweep: the link build is O(n&sup2;) with a terrain "
        "profile and a clutter walk per pair, so a mirrored cell spends most of its time before the "
        "simulation starts. Neither runs its whole grid nightly - each night takes the stalest cells "
        "it has not covered recently, so a full pass completes over roughly a week.</p>",
        '<p class="sub" style="margin:.8rem 0 .3rem"><b>Sim Sweep (matrix)</b> &middot; 03:40 UTC &middot; '
        "three presets, two scales, three placements, three archive counts, five seeds, with a "
        "no-archive baseline per seed per scale. Asks whether a preset ordering survives scaling, and "
        "whether any deliberate placement beats picking nodes at random.</p>",
        '<p class="sub" style="margin:.3rem 0 0"><b>Sim Design (cross)</b> &middot; 04:40 UTC &middot; a '
        "three-axis cross: what the archive is configured as, against what could be deployed instead "
        "of it, on each mesh in the round. This is the one that <b>can</b> answer what the archive is "
        "worth, because the archive sits on an axis rather than being on everywhere.</p>",
                "</div>",
            ],
        ),
        (
            "making-joins",
            "What joins them up",
            [
                '<div class="panel" id="making-joins">',
        "<div class=\"blockhead\"><h3>What joins them up</h3></div>",
        "<p><b>Sim Collate</b> is called by all three rather than scheduled. It reduces a run to the "
        "two files this page reads - <code>summary.json</code> and <code>trend.md</code> - and applies "
        "the standing gates, so a run that produced an impossible number is caught where it was made.</p>",
        "<p><b>Sim Results Explorer</b> rebuilds this page at 06:20 UTC, after all three producers have "
        "finished. It reads <b>only the digests, never the raw block JSONs</b>, so the archive can drop "
        "raw runs without the page losing its history - and a figure that lives beside a dropped JSON "
        "can never be shown here at all, which is why the charts are drawn in the browser from numbers "
        "embedded in the page.</p>",
                "</div>",
            ],
        ),
        ("making-terms", "What each term means", render_glossary()),
    ]

    index = ["<nav class=\"making-nav\" aria-label=\"sections\"><ol>"]
    for anchor, label, _ in sections:
        index.append(f'<li><a href="#{anchor}">{_esc(label)}</a></li>')
    index.append("</ol></nav>")

    body = []
    for _, _, parts in sections:
        body += parts

    return (
        [
            '<section class="tab-panel" data-tab="making" hidden>',
            "<h2>How these runs are made</h2>",
            '<p class="sub">Everything here is written by scheduled workflows into one archive branch, '
            "and this page is rebuilt from that archive. They ask <b>two different kinds of question</b>, "
            "which is why one block list holds two naming conventions: a synthetic mesh moving one flag "
            "at a time, and a real mesh over real ground. The last section is the glossary: what every "
            "column on this page actually counts, and what it is counted against.</p>",
            '<div class="making">',
        ]
        + index
        + ["<div>"]
        + body
        + ["</div>", "</div>", "</section>"]
    )


# The protocol's own traffic split by message type: one pie of counts, one of bytes. The pair is
# the point - an advert is tiny and frequent, a provide is large and rare, so the two pictures of
# the same run look nothing alike and a reader who has seen only one has the wrong idea of where
# the airtime went.
# All traffic by type, with everything the archive sends folded into one slice. This is the pie
# that answers "what share of the channel is the archive" - the SF++ internal split below answers
# a different question and the two are not substitutes.
TRAFFIC_TYPES = (
    ("mix_position_count", "mix_position_bytes", "position", "#7FB0CB"),
    ("mix_telemetry_count", "mix_telemetry_bytes", "telemetry", "#7A8C3F"),
    ("mix_nodeinfo_count", "mix_nodeinfo_bytes", "nodeinfo", "#C08A2E"),
    ("mix_text_count", "mix_text_bytes", "text", "#2E5E7E"),
    ("mix_dm_count", "mix_dm_bytes", "DM", "#B4472A"),
    ("mix_sfpp_count", "mix_sfpp_bytes", "SF++", "#8A5A9E"),
)

MESSAGE_TYPES = (
    ("adverts", "advert_bytes", "advert", "#A57BB8"),
    ("item_requests", "item_request_bytes", "item request", "#C08A2E"),
    ("provides", "provide_bytes", "provide", "#3F8A7A"),
    ("enum_requests", "enum_request_bytes", "enum request", "#B4472A"),
    ("enum_provides", "enum_provide_bytes", "enum provide", "#4E86A8"),
)


# Which recipe fields make the sentence, and how each reads. Anything not named here still shows in
# the table below the sentence, so a field added to collate is never silently dropped.
RECIPE_PROSE = (
    ("topology", "{} topology"),
    ("nodes", "{} nodes"),
    ("scenario", "over {}"),
    ("preset", "{}"),
    ("hop_limit", "hop limit {}"),
    ("servers", "{} archives"),
    ("place", "placed {}"),
    ("hours", "{} h per run"),
)


def _ordinal(n):
    """3 -> 3rd. English, because the sentence it lands in is English."""
    n = int(n)
    if 10 <= n % 100 <= 20:
        return f"{n}th"
    return f"{n}{ {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th') }"


def recipe_sentence(recipe):
    """One line naming how a mesh was made, from the fields that decided it."""
    parts = []
    for key, shape in RECIPE_PROSE:
        value = recipe.get(key)
        if value is None:
            continue
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        if key == "place":
            # The strided placement carries its step, and "placed every-nth" says nothing without it.
            stride = recipe.get("place_stride")
            parts.append(
                f"on every {_ordinal(stride)} node" if value == "every-nth" and stride
                else shape.format(value)
            )
            continue
        parts.append(shape.format(value))
    if recipe.get("no_link_shadowing"):
        parts.append("links by distance alone")
    if recipe.get("hop_spread"):
        parts.append("per-node hop limits 3-7")
    return " · ".join(str(p) for p in parts)


def render_campaign(runs, blocks):
    """What every block on this page was run on: the mesh, and the method that made it.

    First on the page because it is the thing every other number is conditional on. A digest that
    carries a hundred cells and no statement of the mesh underneath them is a hundred numbers
    nobody can place.
    """
    recipes, seen = {}, {}
    for run in runs:
        for key, recipe in (run.get("recipes") or {}).items():
            recipes.setdefault(key, recipe)
    if not recipes:
        return []
    # A representative cell per recipe, for the map and for naming who uses it.
    for run in runs:
        for block in run.get("blocks") or []:
            for cell in block.get("cells") or []:
                key = cell.get("recipe")
                if key is None:
                    continue
                entry = seen.setdefault(key, {"blocks": set(), "map": None})
                entry["blocks"].add(block.get("block"))
                if entry["map"] is None and cell.get("map"):
                    entry["map"] = cell["map"]

    out = [
        '<div class="panel" id="campaign">',
        '<div class="blockhead"><h3>Campaign</h3>'
        f'<span class="arm">{len(recipes)} mesh recipe(s)</span>'
        f'<span class="pill">{sum(len(v["blocks"]) for v in seen.values())} block(s)</span></div>',
        '<p class="sub">The mesh every block below was run on, and how it was made. Every number '
        "on this page is conditional on this: a reach figure is a statement about <i>this</i> mesh "
        "at <i>this</i> hop limit, and two recipes are two experiments rather than two cells.</p>",
    ]
    for key, recipe in sorted(recipes.items()):
        used = sorted(b for b in (seen.get(key) or {}).get("blocks", set()) if b)
        out += [
            '<div class="recipe">',
            f'<h4 class="recipename">{_esc(recipe_sentence(recipe)) or "mesh " + key[:6]}</h4>',
            '<p class="sub">'
            + (f"used by {', '.join(f'<code>{_esc(b)}</code>' for b in used)}" if used
               else "carried by this digest")
            + "</p>",
            '<div class="recipebody">',
            '<table class="recipetable"><tbody>',
        ]
        for field, value in sorted(recipe.items()):
            shown = int(value) if isinstance(value, float) and value.is_integer() else value
            out.append(
                f"<tr><td>{_esc(field.replace('_', ' '))}</td>"
                f"<td>{_esc(shown)}</td></tr>"
            )
        out += [
            "</tbody></table>",
            f'<div class="campaignmap" data-recipe="{_esc(key)}" role="img"></div>',
            "</div>",
            "</div>",
        ]
    out.append("</div>")
    return out


def render_stack(blocks):
    """The cross-block page: one measure, every block, one scale.

    The per-block charts answer "what did this arm do"; this one answers "which arm did the most",
    which no amount of switching between panels can, because each of those scales to itself.
    """
    if not blocks:
        return []
    out = [
        '<section class="tab-panel" data-tab="charts" hidden>',
        "<h2>Chart explorer</h2>",
        '<p class="sub">Any number of measures, drawn for every block that records them, <b>on a single '
        "scale</b>. The per-block charts each scale to their own numbers - right for reading one "
        "block, wrong for comparing two, since a 0.09 bar and a 0.87 bar both reach the top of "
        "their own chart. Whiskers are one standard deviation across the seeds of that cell: where "
        "two of them overlap, the arm has not moved the measure by more than the draw did.</p>",
        '<div class="panel">',
        '<div class="stackbar"><span class="stacklabel">measures</span>'
        '<button class="action-btn" id="stackallmetrics" type="button">all / none</button></div>',
        '<div class="stackblocks stackmetrics">',
        # First and ticked: the composition, which is the one comparison the per-block panels
        # cannot make across blocks.
        '<label><input type="checkbox" class="stackmetric" checked value="__delivery"> '
        "text delivery: on air + overheard</label>",
        '<label><input type="checkbox" class="stackmetric" value="__pies"> '
        "all traffic by type: packets and bytes</label>",
        '<label><input type="checkbox" class="stackmetric" value="__srpies"> '
        "the archive's own messages by type</label>",
    ]
    for key, label, _ in SHOWN:
        out.append(
            '<label><input type="checkbox" class="stackmetric" '
            f'value="{key}"> {_esc(label)}</label>'
        )
    out += [
        "</div>",
        '<div class="stackbar"><span class="stacklabel">blocks</span>'
        '<button class="action-btn" id="stackall" type="button">all / none</button></div>',
        '<div class="stackblocks">',
    ]
    for name in sorted(blocks):
        out.append(
            '<label><input type="checkbox" class="stackblock" checked '
            f'value="{_esc(name)}"> {_esc(name)}</label>'
        )
    out += [
        "</div>",
        '<div id="stackchart" class="chart" role="img"></div>',
        '<p class="sub nojs" style="font-size:.8rem">This page draws from the same digest numbers '
        "as the tables; it needs JavaScript.</p>",
        "</div>",
        "</section>",
    ]
    return out


def render_schedule(sched):
    """The declared test matrix against what the archive holds - what is done, and what is not."""
    out = [
        '<section class="tab-panel" data-tab="schedule" hidden>',
        "<h2>Schedule</h2>",
        '<p class="sub">Every cell the tree declares, against the runs in this archive. '
        "<b>Two different readings of &ldquo;still to do&rdquo;</b> and they disagree by design: the "
        "block sweep runs nightly and touches all 87 every night, while the matrix and the cross run "
        "weekly and touch a cell once a week - so <i>not in the latest run</i> means something for the "
        "first and nothing for the other two. <code>runs</code> counts every run a cell appears in; "
        "<code>never</code> is the column that means work outstanding.</p>",
    ]
    if not sched["surfaces"]:
        out += [
            '<div class="panel"><p class="sub">No sweep definitions are importable here, so only the '
            "run side is knowable. This is the expected state for an archive read on a machine "
            "without the simulator.</p></div>",
            "</section>",
        ]
        return out

    out.append('<div class="panel scroll"><table><thead><tr><th>surface</th><th>declared</th>'
               "<th>ever run</th><th>never run</th><th>in latest</th></tr></thead><tbody>")
    for su in sched["surfaces"]:
        outstanding = (
            '<span class="never">0</span>' if not su["never_run"] else str(su["never_run"])
        )
        out.append(
            f'<tr><td class="mono">{_esc(su["surface"])}</td><td>{su["declared"]}</td>'
            f'<td class="tick">{su["ever_run"]}</td>'
            f"<td>{outstanding}</td>"
            f'<td>{su["in_latest"]}</td></tr>'
        )
    out.append("</tbody></table></div>")

    if sched["undeclared"]:
        out.append(
            '<p class="flag">In the archive but declared by nothing - a renamed or retired cell whose '
            "results are still in the branch: "
            + ", ".join(f"<code>{_esc(n)}</code>" for n in sched["undeclared"])
            + "</p>"
        )

    for su in sched["surfaces"]:
        out += [
            f'<div class="panel"><h3>{_esc(su["surface"])}</h3>',
            '<div class="scroll"><table><thead><tr><th>cell</th><th>runs</th><th>last run</th>'
            "<th>latest</th><th>covers</th></tr></thead><tbody>",
        ]
        latest_yes = '<span class="tick">yes</span>'
        latest_no = '<span class="never">no</span>'
        for row in su["rows"]:
            counted = (
                '<td><span class="never">never</span></td><td class="never">-</td>'
                if not row["runs"]
                else f'<td>{row["runs"]}</td><td class="mono">{_esc(row["last_run"] or "-")}</td>'
            )
            out.append(
                f'<tr><td class="mono">{_esc(row["cell"])}</td>'
                + counted
                + f"<td>{latest_yes if row['in_latest'] else latest_no}</td>"
                + f'<td class="left sub">{_esc(row["explains"] or "")}</td></tr>'
            )
        out += ["</tbody></table></div></div>"]
    out.append("</section>")
    return out


def render_health(health):
    """Per run: duration both ways, flags grouped by kind, and any runtime drift."""
    out = [
        '<section class="tab-panel" data-tab="health" hidden>',
        "<h2>Run health</h2>",
        '<p class="sub">What each run cost and what it flagged. <b>Duration is given both ways on '
        "purpose.</b> <code>compute h</code> is what the run actually spent, which is what decides "
        "whether a job fits its ceiling; <code>s/sim-h</code> is wall-clock seconds per <i>simulated</i> "
        "hour, the only form comparable between runs of different length - and the form the digest "
        "gates on, because the total moves whenever <code>--hours</code> or the seed count does. "
        "Flag kinds are counted, not ranked: <code>beyond-envelope</code> on a mirrored cell is "
        "expected by construction, and colouring every warning red would train everyone to skip "
        "them.</p>",
    ]
    if not health:
        out += ['<div class="panel"><p class="sub">No runs in this archive yet.</p></div>', "</section>"]
        return out

    out.append(
        '<div class="panel scroll"><table><thead><tr><th>run</th><th>ground</th><th>compute h</th>'
        "<th>s/sim-h median</th><th>slowest block</th><th>blocks</th><th>missing</th>"
        "<th>fatal</th><th>warnings</th><th>drifted</th></tr></thead><tbody>"
    )
    for h in reversed(health):
        out.append(
            f'<tr><td class="mono">{_esc(h["run_id"])}</td><td>{_esc(h["scenario"])}</td>'
            f'<td>{h["wall_seconds"] / 3600:.1f}</td>'
            f'<td>{_fmt(h["median_rate"], 2)}</td>'
            + (
                f'<td class="left mono">{_esc(h["slowest_block"])} '
                f'<span class="sub">{h["slowest_seconds"] / 60:.0f}m</span></td>'
                if h["slowest_block"]
                else '<td class="never">-</td>'
            )
            + f'<td>{h["blocks_run"]}</td>'
            f'<td>{h["blocks_missing"] or "-"}</td>'
            + (
                f'<td class="bad">{h["failures"]}</td>'
                if h["failures"]
                else '<td class="never">0</td>'
            )
            + f'<td>{h["warnings"] or "-"}</td>'
            f'<td>{len(h["drifted"]) or "-"}</td></tr>'
        )
    out.append("</tbody></table></div>")

    # Flag kinds, newest run first. Grouped per run rather than pooled: a kind that appeared once and
    # then every night after is a different story from one that fired once a month ago.
    for h in reversed(health):
        if not h["by_kind"] and not h["drifted"]:
            continue
        out.append(f'<div class="panel"><h3>{_esc(h["run_id"])}</h3>')
        if h["by_kind"]:
            out.append("<p>")
            for kind, counts in h["by_kind"].items():
                warnish = " warnish" if kind in ("slower", "inert", "queue-drops") else ""
                out.append(
                    f'<span class="kind{warnish}"><b>{_esc(kind)}</b> {counts["flags"]} '
                    f'<span class="sub">in {counts["blocks"]} block(s)</span></span>'
                )
            out.append("</p>")
        if h["drifted"]:
            out.append(
                '<div class="scroll"><table><thead><tr><th>block</th><th>s/sim-h</th>'
                "<th>median</th><th>ratio</th></tr></thead><tbody>"
            )
            for d in h["drifted"]:
                cls = (
                    "drift-up"
                    if d["ratio"] >= 1.5
                    else "drift-down"
                    if d["ratio"] <= 0.67
                    else ""
                )
                out.append(
                    f'<tr><td class="mono">{_esc(d["block"])}</td>'
                    f'<td>{_fmt(d["rate"], 2)}</td><td>{_fmt(d["median"], 2)}</td>'
                    f'<td class="{cls}">{d["ratio"]:.2f}x</td></tr>'
                )
            out.append("</tbody></table></div>")
        out.append("</div>")
    out.append("</section>")
    return out


# A chart is inlined, never linked: the page is opened from a git branch or a local directory and a
# relative link to a figure that did not travel renders as a broken image. The cap is a runaway
# guard, not a policy - it sits above every figure autochart produces, so nothing a block asks to
# show is refused. A per-node mesh map is the one figure that can pass it, and it has its own page.
FIGURE_CAP_BYTES = 400_000


def block_figure(figures_dir, name):
    """`<block>.svg` from a figures directory, inlined, or nothing at all.

    The layout is autochart's own: `figures/<block>.svg` beside the block JSON, which is where both
    sweep.run_block and a local batch put it.
    """
    if not figures_dir:
        return ""
    # The name comes from a digest, which comes from a branch someone else can write to. Sanitised
    # so it can only ever address a file inside the directory that was asked for: without this a
    # block called `../../id_rsa` would be read and inlined into a published page.
    stem = safe_name(name)
    path = os.path.join(figures_dir, f"{stem}.svg")
    try:
        size = os.path.getsize(path)
    except OSError:
        return ""
    if size > FIGURE_CAP_BYTES:
        return (
            f'<p class="sub" style="font-size:.8rem">chart is {size // 1024} kB, over the '
            f"{FIGURE_CAP_BYTES // 1024} kB inline cap - open {_esc(path)}</p>"
        )
    figures = [(None, path)]
    # A block may need more than one chart. `<block>--<label>.svg` beside it is rendered under the
    # same disclosure, labelled by whatever the producer put after the dashes.
    for extra in sorted(glob.glob(os.path.join(figures_dir, f"{stem}--*.svg"))):
        if os.path.getsize(extra) <= FIGURE_CAP_BYTES:
            label = os.path.basename(extra)[len(stem) + 2 : -4]
            figures.append((label, extra))
    parts = []
    for label, each in figures:
        with open(each) as f:
            svg = f.read()
        # The figure carries its own width and height; this makes it shrink with the panel instead
        # of forcing the page to scroll sideways.
        svg = svg.replace("<svg ", '<svg style="max-width:100%;height:auto" ', 1)
        if label:
            parts.append(f'<p class="sub" style="font-size:.8rem">{_esc(label)}</p>')
        parts.append(f'<div class="scroll">{svg}</div>')
    plural = "" if len(figures) == 1 else f" ({len(figures)})"
    return (
        f"<details class=\"figure\"><summary>chart{plural}</summary>"
        + "".join(parts)
        + "</details>"
    )


def _md(text):
    """A name safe to drop into a markdown cell or code span.

    `_esc` guards the HTML page; this guards the file beside it. A pipe ends a table cell and a
    backtick ends a code span, so a block named ``a|b`` silently reshapes the table it is listed in.
    """
    return str(text).replace("\\", "").replace("|", "\\|").replace("`", "'")


def _md_link(href):
    """A link target that cannot end early: a bracket or a space in a run directory's name would
    close the markdown link and leave whatever follows as clickable text of its own."""
    return urllib.parse.quote(str(href), safe="/:._-~")


def chart_data(blocks, runs):
    """The numbers each block panel draws, as one JSON blob for the page to render live.

    Drawn in the browser rather than shipped as an image, because the digests are all this page is
    promised: figures live beside the block JSONs, which the archive is free to drop and the results
    branch never carries. A chart built from the same numbers as the tables cannot go stale against
    them either.
    """
    run_ids = [r.get("run_id") or r["_dir"] for r in runs]
    out = {}
    for name, entry in blocks.items():
        by_run = {r.get("run_id"): r for r in entry["runs"]}
        cells = {}
        for run in entry["runs"]:
            for value in run["cells"]:
                cells.setdefault(str(value), {})
        # SHOWN is what the picker offers; the pies need the per-type counters too, and those are
        # deliberately not in the picker - ten more checkboxes for a split that is only readable as
        # a composition. Carried here or `latestOf` finds nothing and every byte slice reads zero.
        carried = list(
            dict.fromkeys(
                [k for k, _, _ in SHOWN]
                + [t[0] for t in MESSAGE_TYPES + TRAFFIC_TYPES]
                + [t[1] for t in MESSAGE_TYPES + TRAFFIC_TYPES]
            )
        )
        for value, metrics in cells.items():
            for key in carried:
                metrics[key] = [
                    (by_run.get(rid, {}).get("cells", {}).get(value) or {}).get(key)
                    for rid in run_ids
                ]
        # Per-node vectors, when the digest carried them: the latest run that has one for a cell,
        # since node order belongs to a single run and cannot be pooled across them.
        # The latest run that recorded a spread for a cell, for the same reason the metrics take
        # the latest value: an older run's seed count is not this one's.
        spread = {}
        for run in entry["runs"]:
            for value, per_metric in (run.get("sd") or {}).items():
                spread[str(value)] = per_metric
        nodes = {}
        for run in entry["runs"]:
            for value, vectors in (run.get("per_node") or {}).items():
                nodes[str(value)] = {"run": run.get("run_id"), "classes": vectors}
        # Same rule for maps: the latest run that has one for a cell wins, since a geometry and the
        # node indices its overlay points at belong together.
        maps = {}
        for run in entry["runs"]:
            for value, reference in (run.get("maps") or {}).items():
                maps[str(value)] = dict(reference, run=run.get("run_id"))
        out[name] = {
            "arm": entry["arm"],
            "measure": entry.get("moved") or "held",
            "sd": spread,
            "runs": run_ids,
            "cells": cells,
        }
        if nodes:
            out[name]["nodes"] = nodes
        if maps:
            out[name]["maps"] = maps
    return out


def recipe_maps(runs):
    """{recipe key: one cell's map reference}, for the campaign panel's picture.

    First cell wins: every cell sharing a recipe was run on the same geometry, and where a run
    carried no map the recipe simply has no picture rather than the wrong one.
    """
    out = {}
    for run in runs:
        for block in run.get("blocks") or []:
            for cell in block.get("cells") or []:
                key, reference = cell.get("recipe"), cell.get("map")
                if key and reference and key not in out:
                    out[key] = reference
    return out


def map_registry(runs):
    """Every geometry any run carried, keyed by content hash - collate's registries, merged.

    Identical geometry across two runs hashes the same, so a scenario measured every night enters
    the page once however many nights are in the window.
    """
    out = {}
    for run in runs:
        for key, geometry in (run.get("maps") or {}).items():
            out.setdefault(key, geometry)
    return out


def render_html(runs, blocks, board, for_pages=False, superseded=(), figures_dir=None):
    scenarios = sorted({r.get("scenario_requested") or "flat" for r in runs})
    transports = sorted(
        {
            t
            for r in runs
            for t in (
                [r["transport"]]
                if isinstance(r.get("transport"), str)
                else r.get("transport") or []
            )
        }
    )
    run_ids = [r.get("run_id") or r["_dir"] for r in runs]
    failures = [
        (r.get("run_id"), f)
        for r in runs
        for f in r.get("gate", {}).get("failures", [])
    ]

    # Back, theme, license, in the order the site requires. Only on the published copy: the
    # results-branch copy has no index.html, and a link that 404s is worse than none.
    actions = [
        '<div class="top-actions">',
        (
            '<a class="action-btn" href="index.html">Back to index</a>'
            if for_pages
            else ""
        ),
        '<button id="toggle-theme-btn" class="action-btn" aria-pressed="false">Theme: Auto</button>',
        '<button id="toggle-license-btn" class="action-btn" aria-expanded="false">Show license</button>',
        "</div>",
        '<div class="attribution-block" id="attribution" hidden>',
        "<p><b>What this is.</b> Output of the SF++ set-reconciliation simulator in "
        '<a href="https://github.com/NomDeTom/Meshtasticatom">NomDeTom/Meshtasticatom</a>, '
        "built from the run digests on its <code>sim-results</code> branch by a scheduled job. "
        "Nothing on this page is hand-written or hand-edited.</p>",
        "<p><b>What it is not.</b> Not a measurement of a real network. The radio model, terrain and "
        "clutter come from Meshtasticator and Komzpa's terrain stack; the mesh, traffic and archive "
        "behaviour are simulated. <code>held</code> and <code>union</code> are what an archive holds, "
        "not what a user receives.</p>",
        "<p><b>Reading it.</b> The four delivery measures have four different denominators and are "
        "not comparable to each other. <code>demand</code> is aggregate airtime demand across the "
        "whole mesh, a multiple with no ceiling; <code>chutil</code> is what a device reports and "
        "cannot exceed 100%.</p>",
        # The licence follows the code that produced the page, not the site's usual one: the
        # attribution chain reaches back through Meshtasticator to LoRaSim.
        "<p><b>Licence.</b> This page is output of the simulator in "
        '<a href="https://github.com/NomDeTom/Meshtasticatom">NomDeTom/Meshtasticatom</a>, which is '
        'distributed under <a href="https://www.gnu.org/licenses/gpl-3.0.html">GPL-3.0</a> because '
        "parts of it are transcribed from Meshtastic firmware. A program's output is not the "
        "program: this page describes a simulation and is free to read and quote. The simulator's "
        'Meshtasticator half remains <a href="https://creativecommons.org/licenses/by/4.0/">CC BY '
        "4.0</a>, attribution preserved. "
        "Part of that simulator's source is based on Spinsante, Gioacchini and Scalise, "
        "<i>A novel experimental-based tool for the design of LoRa networks</i> (MetroInd4.0&amp;IoT, "
        "2019), which stems from Bor, Roedig, Voigt and Alonso, <i>Do LoRa Low-Power Wide-Area "
        "Networks Scale?</i> (MSWiM '16) and the LoRaSim library. Terrain, clutter and the capture-"
        "aware physics are from Komzpa's Meshtasticator branch.</p>",
        "</div>",
    ]
    out = [
        # A page that has to survive being copied to a laptop and opened from disk. Without the
        # doctype a browser renders it in quirks mode; without the charset one opened over file://
        # has no header to read and guesses, which turns every `·`, `±` and `→` into mojibake.
        "<!doctype html>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>SF++ sweep explorer</title>",
        f"<style>{CSS}</style>",
        "<main>",
        *[a for a in actions if a],
        "<h1>SF++ sweep explorer</h1>",
        f'<p class="sub">{len(runs)} scheduled run(s), {len(blocks)} block(s), rolling. '
        "Each column is one run: one random seed base over one landform.</p>",
        '<div class="meta">',
        f"<span><b>{len(runs)}</b> runs</span>",
        f"<span>first <b>{_esc(run_ids[0]) if run_ids else '-'}</b></span>",
        f"<span>latest <b>{_esc(run_ids[-1]) if run_ids else '-'}</b></span>",
        f"<span>ground <b>{_esc(', '.join(scenarios))}</b></span>",
        f"<span>transport <b class='mono'>{_esc(', '.join(transports) or '-')}</b></span>",
        f"<span>sim <b class='mono'>{_esc(SIM_VERSION)}</b></span>",
        "</div>",
    ]
    if superseded:
        # Named, not silently dropped: a reader who remembers a number that is no longer on the
        # page needs to know it was superseded rather than lost.
        out.append(
            f'<p class="sub">{len(superseded)} earlier run(s) are excluded from every metric '
            f"below: they were measured before sim {_esc(SIM_VERSION)}, which changed what the "
            "numbers mean. They still appear under run health, whose costs remain comparable.</p>"
        )

    sched = schedule(runs)
    health = run_health(list(runs) + list(superseded))
    pending = sum(su["never_run"] for su in sched["surfaces"])
    flagged = sum(h["warnings"] for h in health)
    out += [
        '<nav class="tabs" role="tablist">',
        '<button data-tab="trend" role="tab" aria-selected="true">Trend</button>',
        '<button data-tab="blocks" role="tab" aria-selected="false">Every block</button>',
        # Only where there is something to draw: render_stack emits nothing for an empty archive,
        # and a button pointing at a panel that does not exist shows a blank page.
        *(
            ['<button data-tab="charts" role="tab" aria-selected="false">Chart explorer</button>']
            if blocks
            else []
        ),
        f'<button data-tab="schedule" role="tab" aria-selected="false">Schedule'
        + (f' <span class="count">{pending} to do</span>' if pending else "")
        + "</button>",
        f'<button data-tab="health" role="tab" aria-selected="false">Run health'
        + (f' <span class="count">{flagged} flags</span>' if flagged else "")
        + "</button>",
        '<button data-tab="runs" role="tab" aria-selected="false">Runs</button>',
        '<button data-tab="making" role="tab" aria-selected="false">How runs are made</button>',
        "</nav>",
    ]

    if failures:
        out.append('<div class="panel">')
        out.append(
            '<p class="flag bad"><b>The standing gate failed in one or more runs.</b></p>'
        )
        for run_id, f in failures:
            out.append(f'<p class="flag bad">{_esc(run_id)}: {_esc(f)}</p>')
        out.append("</div>")

    out += [
        '<section class="tab-panel" data-tab="trend">',
        *render_campaign(runs, blocks),
        "<h2>What moves a delivery measure</h2>",
        '<p class="sub">Mean spread of the measure each block moves most, averaged over the runs that '
        "carry it. The four measures have four denominators and are <b>not comparable to each other</b> - "
        "<code>measure</code> names which one this block travels in. A large <code>text spread</code> "
        "beside it means the block decides its measure by spending the mesh's own broadcast reach.</p>",
        '<div class="panel scroll"><table><thead><tr>'
        "<th>block</th><th>arm</th><th>measure</th><th>spread</th><th>run-to-run sd</th>"
        "<th>text spread</th><th>price</th><th>runs</th></tr></thead><tbody>",
    ]
    for row in board:
        out.append(
            f'<tr><td class="mono">{_esc(row["block"])}</td><td>{_esc(row["arm"])}</td>'
            f"<td><b>{_esc(row['measure'])}</b></td>"
            f"<td>{_fmt(row['spread'])}</td><td>{_fmt(row['spread_sd'])}</td>"
            f"<td>{_fmt(row['cost'])}</td><td>{_price(row)}</td><td>{row['runs']}</td></tr>"
        )
    out.append("</tbody></table></div>")

    out += [
        "</section>",
        '<section class="tab-panel" data-tab="blocks" hidden>',
        "<h2>Every block, run by run</h2>",
        '<div class="controls">',
        '<input type="search" id="q" placeholder="filter by block or arm…" />',
        '<select id="scenario"><option value="all">every landform</option>'
        + "".join(f'<option value="{_esc(s)}">{_esc(s)}</option>' for s in scenarios)
        + "</select>",
        "</div>",
    ]

    for name in sorted(blocks):
        entry = blocks[name]
        block_scenarios = sorted({r["scenario"] for r in entry["runs"]})
        measure = entry.get("moved") or "held"
        tracked = series(entry, measure)
        out.append(
            f'<div class="panel" data-block="{_esc(name)}" data-arm="{_esc(entry["arm"])}" '
            f'data-scenarios="{_esc("|".join(block_scenarios))}">'
        )
        out.append(
            f'<div class="blockhead"><h3>{_esc(name)}</h3>'
            f'<span class="arm">{_esc(entry["arm"])}</span>'
            + "".join(f'<span class="pill">{_esc(s)}</span>' for s in block_scenarios)
            + f'<span class="pill">{len(entry["runs"])} run(s)</span>'
            + f'<span class="pill">tracking {_esc(measure)}</span></div>'
        )
        if entry.get("explains"):
            out.append(
                f'<p class="sub" style="margin:-.2rem 0 .8rem;font-size:.85rem">'
                f"{_esc(entry['explains'])}</p>"
            )
        out.append("")
        out.append('<div class="scroll"><table><thead><tr><th>value</th><th>trend</th>')
        out += [f"<th>{_esc(r['run_id'])}</th>" for r in entry["runs"]]
        out.append("<th>mean</th></tr></thead><tbody>")
        for value, points in tracked.items():
            present = [p for p in points if p is not None]
            out.append(
                f'<tr><td class="mono">{_esc(value)}</td><td>{sparkline(points)}</td>'
                + "".join(f"<td>{_fmt(p)}</td>" for p in points)
                + f"<td><b>{_fmt(statistics.mean(present)) if present else '·'}</b></td></tr>"
            )
        out.append("</tbody></table></div>")

        # One checkbox per metric, because the question a reader arrives with is nearly always
        # comparative - did DM hold up where text did not - and a control that shows one metric at a
        # time answers it only by memory of the previous click.
        #
        # Grouped by unit and ticked on arrival, so the control removes rather than adds. A reader
        # who does not know the metric names cannot add what they cannot name, and one metric ticked
        # by default made the other eleven invisible unless guessed at. The unit is the grouping
        # because it is already the one the chart must obey: a family is a promise that heights
        # within it mean the same thing, so a group is exactly one chart's worth of ticks.
        picks = []
        for unit in dict.fromkeys(UNITS.get(k, "other") for k, _, _ in SHOWN):
            members = [
                f'<label><input type="checkbox" class="metric" value="{k}" checked> '
                f"{_esc(label)}</label>"
                for k, label, _ in SHOWN
                if UNITS.get(k, "other") == unit
            ]
            picks.append(
                f'<span class="chartgroup"><b class="unit">{_esc(unit)}</b>'
                f'{"".join(members)}</span>'
            )
        # Offered only where the digest carried the vectors, so the control cannot promise a chart
        # the page has no numbers for.
        if any(r.get("per_node") for r in entry["runs"]):
            picks.append(
                '<label class="wide"><input type="checkbox" class="metric" value="__nodes">'
                " every node, by class</label>"
            )
        if any(
            (r.get("cells") or {}).get(value, {}).get("text_on_air") is not None
            for r in entry["runs"]
            for value in (r.get("cells") or {})
        ):
            picks.append(
                '<label class="wide"><input type="checkbox" class="metric" value="__delivery" '
                "checked> text delivery: on air vs overheard</label>"
            )
        if any(
            (r.get("cells") or {}).get(value, {}).get("adverts") is not None
            for r in entry["runs"]
            for value in (r.get("cells") or {})
        ):
            picks.append(
                '<label class="wide"><input type="checkbox" class="metric" value="__pies" '
                "checked> all traffic by type: packets and bytes</label>"
            )
            picks.append(
                '<label class="wide"><input type="checkbox" class="metric" value="__srpies" '
                "checked> the archive's own messages by type</label>"
            )
        if any(r.get("maps") for r in entry["runs"]):
            picks.append(
                '<label class="wide"><input type="checkbox" class="metric" value="__map">'
                " mesh map</label>"
            )
        out.append(
            f'<details class="figure" data-chart="{_esc(name)}">'
            f"<summary>chart</summary>"
            f'<div class="chartbar chartpick">{"".join(picks)}</div>'
            f'<div class="chart" role="img"></div>'
            f'<p class="sub nojs" style="font-size:.8rem">This chart draws from the same digest '
            f"numbers as the tables above; it needs JavaScript.</p></details>"
        )
        # A figure rendered beside the block JSON, when the raw runs are still there to have one.
        # Additional to the live chart, never instead of it.
        figure = block_figure(figures_dir, name)
        if figure:
            out.append(figure)

        # The latest run in full: the sparkline row above carries `held` only, and a reader who has
        # spotted a moving block needs the currency it moved in without opening the run's own report.
        latest = entry["runs"][-1]
        out.append(
            f'<p class="sub" style="margin:.75rem 0 .35rem;font-size:.8rem">'
            f"latest run {_esc(latest['run_id'])}, every metric</p>"
        )
        out.append('<div class="scroll"><table><thead><tr><th>value</th>')
        out += [f"<th>{_esc(label)}</th>" for _, label, _ in SHOWN]
        out.append("</tr></thead><tbody>")
        for value, metrics in latest["cells"].items():
            out.append(
                f'<tr><td class="mono">{_esc(value)}</td>'
                + "".join(
                    f"<td>{_fmt(metrics.get(key), places)}</td>"
                    for key, _, places in SHOWN
                )
                + "</tr>"
            )
        out.append("</tbody></table></div>")
        out += render_distributions(latest)
        # Folded away: a block with a dozen queue-drop and decode-failure lines buries its own
        # tables under them, and the counts they report are on the charts now. The summary still
        # states how many there are, so a folded warning is not a hidden one.
        flags = sorted({f for r in entry["runs"] for f in r["flags"]})
        if flags:
            out.append(
                '<details class="flags"><summary>'
                f'{len(flags)} warning{"" if len(flags) == 1 else "s"}</summary>'
            )
            out += [f'<p class="flag">{_esc(f)}</p>' for f in flags]
            out.append("</details>")
        out.append("</div>")

    out += ["</section>"]
    out += render_stack(blocks)
    out += render_schedule(sched)
    out += render_health(health)
    out += render_making()
    out += [
        '<section class="tab-panel" data-tab="runs" hidden>',
        "<h2>Runs</h2>",
        '<div class="panel scroll"><table><thead><tr><th>run</th><th>ground</th><th>seed base</th>'
        "<th>blocks</th><th>missing</th><th>warnings</th><th>compute h</th><th>report</th>"
        "</tr></thead><tbody>",
    ]
    for r in reversed(runs):
        gate = r.get("gate", {})
        # A run that asked for ground and got none is a run whose landform column is a label rather
        # than a fact - the same failure as an inert arm, one level up.
        asked = r.get("scenario_requested") or ""
        ignored = asked and asked not in (r.get("scenario_observed") or [])
        out.append(
            f'<tr><td class="mono">{_esc(r.get("run_id"))}</td>'
            f'<td>{_esc(asked or "flat")}'
            + (
                ' <span class="pill" title="the blocks in this run recorded no scenario">not applied</span>'
                if ignored
                else ""
            )
            + "</td>"
            f'<td class="mono">{_esc(r.get("seed_base") or "-")}</td>'
            f'<td>{gate.get("blocks_run", 0)}</td><td>{gate.get("blocks_missing", 0)}</td>'
            f'<td>{len(gate.get("warnings", []))}</td>'
            f'<td>{(r.get("wall_seconds") or 0) / 3600:.1f}</td>'
            f'<td><a href="{_esc(r["_href"])}/trend.md">trend.md</a></td></tr>'
        )
    out += [
        "</tbody></table></div>",
        "</section>",
        "<footer>Built by <code>sfpp.explorer</code> from the run digests in this branch. "
        "Nothing here is hand-edited; a scheduled job rewrites the page.</footer>",
        "</main>",
        # A block name reaches this blob, and a name holding `</script>` would close the element
        # and everything after it would be markup. Escaped as \u ..., which is still valid JSON.
        '<script type="application/json" id="chartmeta">'
        + json.dumps(
            {
                "units": UNITS,
                "axis": UNIT_AXIS,
                "colours": SERIES_COLOURS,
                "labels": {k: label for k, label, _ in SHOWN},
                "places": {k: places for k, _, places in SHOWN},
                # Shared by every cell that has this geometry, which is why it travels here and
                # not inside a block: one Batumi topology served 102 of 123 cells.
                "maps": map_registry(runs),
                # One map reference per recipe, so the campaign panel draws the mesh a recipe
                # made without having to know which cell happened to carry the geometry.
                "recipeMaps": recipe_maps(runs),
                # The message-type split the pies draw, as (count, bytes, label, colour).
                "messageTypes": [
                    {"count": c, "bytes": b, "label": label, "colour": colour}
                    for c, b, label, colour in MESSAGE_TYPES
                ],
                "trafficTypes": [
                    {"count": c, "bytes": b, "label": label, "colour": colour}
                    for c, b, label, colour in TRAFFIC_TYPES
                ],
                "rolemarks": MAP_MARKS,
                "mapcolours": {"fragile": MAP_FRAGILE, "link": MAP_LINK},
            },
            separators=(",", ":"),
        )
        + "</script>",
        '<script type="application/json" id="chartdata">'
        + (
            json.dumps(chart_data(blocks, runs), separators=(",", ":"))
            .replace("<", "\\u003c")
            .replace(">", "\\u003e")
            .replace("&", "\\u0026")
        )
        + "</script>",
        f"<script>{JS}</script>",
    ]
    return "\n".join(out)


def render_markdown(runs, blocks, board, superseded=()):
    latest = runs[-1] if runs else {}
    out = [
        "# SF++ sweep explorer",
        "",
        f"{len(runs)} scheduled run(s) rolled up, {len(blocks)} block(s). "
        "Open `index.html` for the filterable page; this file is the same data in a diff-readable form.",
        "",
        f"- **latest** `{latest.get('run_id', '-')}` on {latest.get('scenario_requested') or 'flat'} "
        f"ground, seed base `{latest.get('seed_base', '-')}`",
        f"- **transport** `{latest.get('transport', '-')}`",
        f"- **sim version** `{SIM_VERSION}`"
        + (
            f", excluding {len(superseded)} superseded run(s) from every metric below"
            if superseded
            else ""
        ),
        "",
        "## What moves a delivery measure",
        "",
        "| block | arm | measure | spread | run-to-run sd | text spread | price | runs |",
        "| --- | --- | --- | --: | --: | --: | --- | --: |",
    ]
    for row in board:
        out.append(
            f"| `{_md(row['block'])}` | {_md(row['arm'])} | **{_md(row['measure'])}** | "
            f"{_fmt(row['spread'])} | "
            f"{_fmt(row['spread_sd'])} | {_fmt(row['cost'])} | {_price(row)} | {row['runs']} |"
        )
    out += [
        "",
        "## Runs",
        "",
        "| run | ground | seed base | blocks | missing | warnings |",
        "| --- | --- | --- | --: | --: | --: |",
    ]
    for r in reversed(runs):
        gate = r.get("gate", {})
        out.append(
            f"| [`{_md(r.get('run_id'))}`]({_md_link(r['_href'])}/trend.md) | "
            f"{_md(r.get('scenario_requested') or 'flat')} | "
            f"`{r.get('seed_base', '-')}` | {gate.get('blocks_run', 0)} | {gate.get('blocks_missing', 0)} | "
            f"{len(gate.get('warnings', []))} |"
        )
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="roll every collated sweep into one page")
    ap.add_argument(
        "--archive", required=True, help="directory holding one subdirectory per run"
    )
    ap.add_argument(
        "--out", default=".", help="where the page and INDEX.md are written"
    )
    ap.add_argument("--window", type=int, help="use only the most recent N runs")
    ap.add_argument(
        "--name",
        default="index.html",
        help="filename for the page. The published copy is not called index.html - it is one page "
        "on a site that has its own index",
    )
    ap.add_argument(
        "--link-base",
        help="prefix for the per-run report links. The archive is a git branch, so a page published "
        "anywhere else has to point at it absolutely or every report link 404s",
    )
    ap.add_argument(
        "--figures",
        help="directory of autochart block figures (`figures/<block>.svg`, as sweep.run_block and "
        "the local batches write them). Each block's chart is inlined under its tables when one "
        "exists. Off by default: the scheduled page is rolled from digests alone, and the figures "
        "live in a run's artifact rather than on the results branch",
    )
    ap.add_argument(
        "--for-pages",
        action="store_true",
        help="build the copy for the public site: adds the back-to-index action the site requires",
    )
    opts = ap.parse_args(argv)

    archive = load_archive(opts.archive, opts.window)
    if not archive:
        print(f"no run digests under {opts.archive} - nothing to roll up")
        return 1
    # Metrics come from the runs measured under this sim version; run health reads the whole
    # archive, because seconds per simulated hour does not care what the airtime was.
    runs, superseded = comparable_runs(archive)
    blocks = index_by_block(runs)
    board = leaderboard(blocks)
    if superseded:
        print(
            f"{len(superseded)} run(s) superseded by sim {SIM_VERSION} and excluded from the "
            f"metrics: {', '.join(r.get('run_id') or r['_name'] for r in superseded)}"
        )
    if not runs:
        print(f"no run digests at sim {SIM_VERSION} yet - the trend and block views will be empty")

    os.makedirs(opts.out, exist_ok=True)
    # Links are written relative to the page, which does not sit in the archive: the page is at the
    # results root and the runs are a directory below it.
    for r in archive:
        if opts.link_base:
            r["_href"] = opts.link_base.rstrip("/") + "/" + r["_name"]
        else:
            r["_href"] = os.path.relpath(r["_dir"], opts.out).replace(os.sep, "/")
    with open(os.path.join(opts.out, opts.name), "w") as f:
        f.write(
            render_html(runs, blocks, board, opts.for_pages, superseded, opts.figures)
        )
    with open(os.path.join(opts.out, "INDEX.md"), "w") as f:
        f.write(render_markdown(runs, blocks, board, superseded) + "\n")
    print(
        f"rolled {len(runs)} run(s), {len(blocks)} block(s) -> {opts.out}/{opts.name}, {opts.out}/INDEX.md"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
