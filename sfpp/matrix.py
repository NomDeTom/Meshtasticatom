"""The place-and-radio matrix: real geometry, several presets, several placements, paired controls.

`sweep.py` moves one arm at a time against a fixed synthetic mesh, which is the right shape for
asking what a mechanism does. It cannot ask the questions that only real ground poses - whether a
preset ordering survives scaling, whether a deliberate archive placement beats picking nodes at
random, whether an archive count is a constant or a proportion. Those need a grid over a snapshot,
and they need controls.

Three controls are built in, because each has already been the difference between a finding and an
artefact:

  * **`--baseline`, once per seed per scale.** No archive at all. Every claim about what an archive
    costs is a difference against this, and without it the cost is measured against nothing.
  * **`random-any` among the placements.** A deliberate arrangement that cannot beat nodes picked at
    random has not earned its complexity.
  * **`servers_placed` recorded beside `servers_requested`.** Role-bounded placements cap at the
    mesh's router count and silently repeat above it, so two rows of a `--servers` sweep can be the
    same run. The digest groups on what was achieved, not what was asked.

Output is deliberately the same shape `sweep.py` writes - one JSON per cell group, each report
carrying `block`, `arm` and `value` - so `collate.py` and `explorer.py` read a matrix run and a block
run through the same path and the rolling page carries both.

Usage, from the tree root:
    python3 -m sfpp.matrix --list
    python3 -m sfpp.matrix --cell batumi-x1-LONG_FAST --seeds 7 11 13 --out runs/
"""

import argparse
import itertools
import json
import os
import time

from . import autochart as AC
from .campaign import build_parser, run_once

# The suggested first matrix, as the handover ranks it. Presets that differ in both sensitivity and
# airtime; placements spanning deliberate, adjacent and random; archive counts spanning the router
# cap so the capping itself is visible.
PRESETS = ["SHORT_FAST", "LITE_FAST", "LONG_FAST"]
MIRRORS = [1, 4]
PLACES = ["random-any", "beside-router", "routers"]
SERVERS = [2, 4, 8]

# Everything held fixed across the matrix. Seventy-two hours, which is `campaign.py`'s own default.
#
# This was two, on the reasoning that two is "long enough for adverts to have spread and for a bucket
# to have sealed, and short enough that the x4 cells stay inside a CI job". The first half was true of
# the archive and false of everything around it: `--diurnal commuter` is a 17:1 peak-to-trough curve
# and a 2 h run samples two hours of it, so every figure here was quietly a figure about one arbitrary
# stretch of one evening. The second half was solved the right way instead - the cells are now sharded
# one job per seed (see sim_sweep_matrix.yml), so a job holds ten runs rather than fifty and the x4
# cells stay inside a CI job at 72 h too.
BASE = [
    "--hours",
    "72",
    "--scenario",
    "batumi",
    "--protocol",
    "sr",
    # Charts are the transport's only heavy dependency and a matrix job has no one watching it.
    "--no-charts",
    # An addressed measure and an operator measure, so a cell reports all four successes rather than
    # broadcast reach alone.
    "--dm-per-hour",
    "6",
    "--admin-probes-per-hour",
    "6",
]


def cells():
    """{name: (preset, mirror)} - one job's worth of work per entry."""
    return {
        f"batumi-x{mirror}-{preset}": (preset, mirror)
        for preset, mirror in itertools.product(PRESETS, MIRRORS)
    }


def cell_argv(preset, mirror, place=None, servers=None, baseline=False):
    argv = BASE + ["--preset", preset, "--mirror", str(mirror)]
    if baseline:
        # No servers at all. The paired control the archive's cost is measured against.
        return argv + ["--baseline"]
    return argv + ["--place", place, "--servers", str(servers)]


def run_cell(name, preset, mirror, seeds, out_dir, tag=None):
    """Every placement and count at one preset and one scale, plus the baseline control per seed.

    `tag` distinguishes the file when a cell is sharded across jobs, exactly as `design.run_cell` uses
    it: every shard keeps the same `block`, which is what the digest groups on, and only the filename
    differs. It is not optional once the cells are sharded - the shards' artifacts are downloaded into
    one directory with `merge-multiple: true`, so without a tag every seed of a cell writes
    `{cell}.json` and each silently overwrites the last, leaving one seed's data wearing the whole
    cell's name.
    """
    parser = build_parser()
    results = []
    arms = [("baseline", None, None)] + [
        (f"{place} x{servers}", place, servers)
        for place, servers in itertools.product(PLACES, SERVERS)
    ]
    for label, place, servers in arms:
        for seed in seeds:
            argv = cell_argv(preset, mirror, place, servers, baseline=place is None)
            opts = parser.parse_args(argv)
            started = time.time()
            report = run_once(opts, seed)
            report["block"] = name
            report["arm"] = "placement"
            report["value"] = label
            report["grid"] = ["--preset", preset, "--mirror", str(mirror)]
            results.append(report)
            placed = (report.get("sfpp") or {}).get("servers_placed")
            print(
                f"  {name} {label} seed={seed} {time.time() - started:.0f}s"
                + (f" (placed {placed})" if placed is not None else ""),
                flush=True,
            )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{name}.{tag}.json" if tag else f"{name}.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"wrote {path}")
    chart = AC.auto(results, path, kind="block")
    if chart:
        print(f"wrote {chart}")
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="the place-and-radio matrix over real geometry"
    )
    ap.add_argument("--cell", help="one entry from --list; a job's worth of work")
    ap.add_argument(
        "--list", action="store_true", help="print the cell names and what each covers"
    )
    ap.add_argument("--seeds", nargs="+", type=int, default=[7, 11, 13, 17, 23])
    ap.add_argument("--out", default="runs")
    ap.add_argument(
        "--tag",
        help="suffix this shard's filename. For splitting one cell over several jobs; the cell "
        "keeps its name in the reports, so the digest still reads the shards as one block",
    )
    opts = ap.parse_args(argv)

    known = cells()
    if opts.list:
        for name, (preset, mirror) in known.items():
            runs = (len(PLACES) * len(SERVERS) + 1) * len(opts.seeds)
            print(f"{name:28} {preset} x{mirror}  {runs} runs per invocation")
        print(f"\n{len(known)} cells, {len(opts.seeds)} seeds each")
        return 0
    if not opts.cell:
        return ap.error("give --cell or --list")
    if opts.cell not in known:
        return ap.error(f"unknown cell {opts.cell!r}; --list prints them")
    preset, mirror = known[opts.cell]
    run_cell(opts.cell, preset, mirror, opts.seeds, opts.out, opts.tag)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
