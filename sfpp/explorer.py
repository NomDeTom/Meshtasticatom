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
    ("dm", "DM", 3),
    ("admin", "admin", 3),
    ("held", "held", 3),
    ("union", "union", 3),
    ("text_worst", "worst", 3),
    # A multiple with no ceiling, and a percentage that cannot pass 100. Named apart on purpose:
    # reading the first as the second described genuine comparisons as rankings of collapse.
    ("demand", "demand x", 2),
    ("chutil_p90", "chutil p90 %", 1),
    ("chutil_max", "chutil max %", 1),
    ("airutil_max", "airutil max %", 1),
    ("sr_airtime", "SR air", 3),
    ("servers_placed", "placed", 0),
]
# The axis each metric belongs on. Bars side by side invite reading one height against another, and
# the note above is exactly why that has to be refused across units: `demand` has no ceiling and
# `chutil_p90` cannot pass 100, so one y axis for both ranks collapse instead of measuring it. A
# family is a promise that heights within it mean the same thing.
UNITS = {
    "text": "share",
    "dm": "share",
    "admin": "share",
    "held": "share",
    "union": "share",
    "text_worst": "share",
    "sr_airtime": "share",
    "demand": "multiple",
    "chutil_p90": "percent",
    "chutil_max": "percent",
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
}
# Fixed per metric, not per position in the selection, so a colour means the same thing in every
# panel and across a reload. Chosen to hold up on both themes and for red/green colour blindness.
SERIES_COLOURS = {
    "text": "#2E5E7E",
    "dm": "#B4472A",
    "admin": "#7A8C3F",
    "held": "#4E86A8",
    "union": "#8A5A9E",
    "text_worst": "#C08A2E",
    "sr_airtime": "#3F8A7A",
    "demand": "#2E5E7E",
    "chutil_p90": "#2E5E7E",
    "chutil_max": "#B4472A",
    "airutil_max": "#C08A2E",
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
@media (max-width: 768px) { .meta { gap: .35rem 1rem; } }
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
    const W = 640, LEFT = 132, RIGHT = 24, PLOT = W - LEFT - RIGHT;
    const rows = [];
    cells.forEach((cell) => {
      const classes = entry.nodes[cell].classes;
      Object.keys(classes).forEach((cls) => rows.push([cell, cls, classes[cls]]));
    });
    const H = 34 + rows.length * 16;
    const svg = el('svg', {viewBox: `0 0 ${W} ${H}`, width: '100%', height: H,
                           style: 'max-width:100%;height:auto;font-size:10.5px'});
    rows.forEach(([cell, cls, vector], i) => {
      const y = 14 + i * 16;
      const label = el('text', {x: LEFT - 8, y: y + 4, 'text-anchor': 'end',
                                style: 'fill:var(--muted)'});
      label.textContent = `${cell} · ${cls}`;
      svg.appendChild(label);
      svg.appendChild(el('line', {x1: LEFT, y1: y, x2: LEFT + PLOT, y2: y,
                                  style: 'stroke:var(--border)'}));
      vector.forEach((share, node) => {
        const dot = el('circle', {cx: LEFT + Math.max(0, Math.min(1, share)) * PLOT, cy: y, r: 2.1,
                                  style: 'fill:var(--accent);fill-opacity:.55'});
        const title = el('title', {});
        title.textContent = `node ${node}: ${share.toFixed(3)}`;
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
        title.textContent = `${c} · ${meta.labels[m] || m} = ${fmt(v, meta.places[m])}` +
          (seen.length > 1 ? ` (${entry.runs.length} runs: ${seen.join(', ')})` : '');
        bar.appendChild(title);
        svg.appendChild(bar);
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

  function draw(host, block, selected) {
    const entry = data[block];
    host.textContent = '';
    if (!entry) return;
    const nodes = selected.indexOf('__nodes') >= 0;
    const wantMap = selected.indexOf('__map') >= 0;
    const bars = selected.filter((m) => m !== '__nodes' && m !== '__map');
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
    families.forEach((fam) => {
      const got = drawFamily(entry, fam.metrics, fam.unit);
      if (!got) return;
      const cap = document.createElement('p');
      cap.className = 'axislabel';
      // Named from what was drawn, not what was ticked, so a metric this block has no numbers
      // for does not appear in the caption of a chart it is absent from.
      cap.textContent = (meta.axis[fam.unit] || fam.unit)
        + (got.live.length === 1 ? ' · ' + (meta.labels[got.live[0]] || got.live[0]) : '');
      host.appendChild(cap);
      host.appendChild(got.svg);
      drew++;
    });
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
        // Only fields this panel offers: `__nodes` exists where the digest carried the vectors.
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


def render_making():
    """What produced the runs on this page: two styles of question, three workflows asking them.

    Static prose, not derived from the archive. It is here because the page mixes producers - one
    block list holds both `<DD>-subject` and `batumi-...` cells - and nothing else on the page says
    why, or which of the two a row came from.
    """
    return [
        '<section class="tab-panel" data-tab="making" hidden>',
        "<h2>How these runs are made</h2>",
        '<p class="sub">Everything here is written by scheduled workflows into one archive branch, '
        "and this page is rebuilt from that archive. They ask <b>two different kinds of question</b>, "
        "which is why one block list holds two naming conventions: a synthetic mesh moving one flag "
        "at a time, and a real mesh over real ground.</p>",
        '<div class="panel">',
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
        '<div class="panel">',
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
        '<div class="panel">',
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
        "</section>",
    ]


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
        for value, metrics in cells.items():
            for key, label, _ in SHOWN:
                metrics[key] = [
                    (by_run.get(rid, {}).get("cells", {}).get(value) or {}).get(key)
                    for rid in run_ids
                ]
        # Per-node vectors, when the digest carried them: the latest run that has one for a cell,
        # since node order belongs to a single run and cannot be pooled across them.
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
            "runs": run_ids,
            "cells": cells,
        }
        if nodes:
            out[name]["nodes"] = nodes
        if maps:
            out[name]["maps"] = maps
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
        for f in {f for r in entry["runs"] for f in r["flags"]}:
            out.append(f'<p class="flag">{_esc(f)}</p>')
        out.append("</div>")

    out += ["</section>"]
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
