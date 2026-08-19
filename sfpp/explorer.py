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

from .collate import COST

# What the page shows per cell. The digest carries more (see collate.METRICS); these are the ones a
# person reads a trend through, and keeping the embedded payload to eight numbers a cell is what
# lets thirty runs of 87 blocks stay a file a browser opens instantly.
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
            entry["runs"].append(
                {
                    "run_id": run.get("run_id"),
                    "scenario": run.get("scenario_requested") or "flat",
                    "seed_base": run.get("seed_base"),
                    "cells": {c["value"]: c["metrics"] for c in b["cells"]},
                    "flags": b.get("flags", []),
                }
            )
    return blocks


def spread_of(run, key):
    """How far one metric travels across an arm within a single run, or None if it was not recorded."""
    values = [m.get(key) for m in run["cells"].values() if m.get(key) is not None]
    return max(values) - min(values) if len(values) > 1 else None


def leaderboard(blocks):
    """Blocks by how far they move a delivery measure, averaged over the runs that carry them.

    Averaged rather than pooled: a block present in thirty runs and one present in two would
    otherwise be ranked by how long they have been in the archive.

    The measure is whichever of the four the block moves most. They have different denominators and
    are not comparable, so one ranking column has to name one - and naming `held` for every block
    would rate an arm that halves DM success as having done nothing.
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
        if not spreads:
            continue
        rows.append(
            {
                "block": name,
                "arm": entry["arm"],
                "measure": measure,
                "spread": statistics.mean(spreads),
                # Whether the effect is stable run to run, or an artefact of one seed.
                "spread_sd": statistics.stdev(spreads) if len(spreads) > 1 else None,
                "cost": statistics.mean(costs) if costs else None,
                "runs": len(spreads),
            }
        )
    return sorted(rows, key=lambda r: r["spread"], reverse=True)


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
const q = document.getElementById('q');
const sc = document.getElementById('scenario');
function apply() {
  const needle = (q.value || '').toLowerCase();
  const scen = sc.value;
  for (const el of document.querySelectorAll('[data-block]')) {
    const hitText = !needle || el.dataset.block.toLowerCase().includes(needle)
                            || el.dataset.arm.toLowerCase().includes(needle);
    const hitScen = scen === 'all' || (el.dataset.scenarios || '').split('|').includes(scen);
    el.classList.toggle('hidden', !(hitText && hitScen));
  }
}
q.addEventListener('input', apply);
sc.addEventListener('change', apply);
"""


def render_html(runs, blocks, board, for_pages=False):
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

    # The three top actions, in the order the site requires them: back, theme, license. Only on the
    # published copy - the copy that lives on the results branch has no index.html to go back to,
    # and a link that 404s is worse than no link.
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
        '<a href="https://github.com/NomDeTom/Meshtasticator">NomDeTom/Meshtasticator</a>, '
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
        # The licence follows the code that produced the page rather than the site's usual one:
        # Meshtasticator is CC BY 4.0 and parts of its radio model descend from LoRaSim, so the
        # attribution chain has to reach back to both papers.
        "<p><b>Licence.</b> This page is output of "
        '<a href="https://github.com/NomDeTom/Meshtasticator">Meshtasticator</a> and is shared '
        "under the same terms: "
        '<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. '
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
        "</div>",
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
        "<h2>What moves a delivery measure</h2>",
        '<p class="sub">Mean spread of the measure each block moves most, averaged over the runs that '
        "carry it. The four measures have four denominators and are <b>not comparable to each other</b> - "
        "<code>measure</code> names which one this block travels in. A large <code>text spread</code> "
        "beside it means the block decides its measure by spending the mesh's own broadcast reach.</p>",
        '<div class="panel scroll"><table><thead><tr>'
        "<th>block</th><th>arm</th><th>measure</th><th>spread</th><th>run-to-run sd</th>"
        "<th>text spread</th><th>runs</th></tr></thead><tbody>",
    ]
    for row in board:
        out.append(
            f'<tr><td class="mono">{_esc(row["block"])}</td><td>{_esc(row["arm"])}</td>'
            f"<td><b>{_esc(row['measure'])}</b></td>"
            f"<td>{_fmt(row['spread'])}</td><td>{_fmt(row['spread_sd'])}</td>"
            f"<td>{_fmt(row['cost'])}</td><td>{row['runs']}</td></tr>"
        )
    out.append("</tbody></table></div>")

    out += [
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
        for f in {f for r in entry["runs"] for f in r["flags"]}:
            out.append(f'<p class="flag">{_esc(f)}</p>')
        out.append("</div>")

    out += [
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
        "<footer>Built by <code>sfpp.explorer</code> from the run digests in this branch. "
        "Nothing here is hand-edited; a scheduled job rewrites the page.</footer>",
        "</main>",
        f"<script>{JS}</script>",
    ]
    return "\n".join(out)


def render_markdown(runs, blocks, board):
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
        "",
        "## What moves a delivery measure",
        "",
        "| block | arm | measure | spread | run-to-run sd | text spread | runs |",
        "| --- | --- | --- | --: | --: | --: | --: |",
    ]
    for row in board:
        out.append(
            f"| `{row['block']}` | {row['arm']} | **{row['measure']}** | {_fmt(row['spread'])} | "
            f"{_fmt(row['spread_sd'])} | {_fmt(row['cost'])} | {row['runs']} |"
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
            f"| [`{r.get('run_id')}`]({r['_href']}/trend.md) | {r.get('scenario_requested') or 'flat'} | "
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
        "--for-pages",
        action="store_true",
        help="build the copy for the public site: adds the back-to-index action the site requires",
    )
    opts = ap.parse_args(argv)

    runs = load_archive(opts.archive, opts.window)
    if not runs:
        print(f"no run digests under {opts.archive} - nothing to roll up")
        return 1
    blocks = index_by_block(runs)
    board = leaderboard(blocks)

    os.makedirs(opts.out, exist_ok=True)
    # Links are written relative to the page, which does not sit in the archive: the page is at the
    # results root and the runs are a directory below it.
    for r in runs:
        if opts.link_base:
            r["_href"] = opts.link_base.rstrip("/") + "/" + r["_name"]
        else:
            r["_href"] = os.path.relpath(r["_dir"], opts.out).replace(os.sep, "/")
    with open(os.path.join(opts.out, opts.name), "w") as f:
        f.write(render_html(runs, blocks, board, for_pages=opts.for_pages))
    with open(os.path.join(opts.out, "INDEX.md"), "w") as f:
        f.write(render_markdown(runs, blocks, board) + "\n")
    print(
        f"rolled {len(runs)} run(s), {len(blocks)} block(s) -> {opts.out}/{opts.name}, {opts.out}/INDEX.md"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
