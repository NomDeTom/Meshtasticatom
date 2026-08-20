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

# Presets differing in both sensitivity and airtime, placements spanning deliberate to random,
# and counts that straddle the router cap so the capping is visible rather than hidden.
PRESETS = ["SHORT_FAST", "LITE_FAST", "LONG_FAST"]
MIRRORS = [1, 4]
PLACES = ["random-any", "beside-router", "routers"]
SERVERS = [2, 4, 8]

# Everything held fixed across the matrix, at campaign.py's own 72-hour default: a 2 h run samples
# two hours of a 17:1 diurnal curve, and sharding per seed is what keeps a job inside its ceiling.
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


# One sentence per cell, composed from the preset and the scale rather than hand-written, since
# those two coordinates are the whole content of a cell name. test_matrix holds every cell to one.
PRESET_NOTES = {
    "SHORT_FAST": "SHORT_FAST, the fast end of what deployed meshes run: least airtime per packet "
    "and the least range per hop, so the mesh is quiet but sparser",
    "LITE_FAST": "LITE_FAST, the EU_866 default - a narrower 125 kHz channel that buys sensitivity "
    "back at four times LONG_FAST's airtime",
    "LONG_FAST": "LONG_FAST, the shipped default and the middle of the deployed range",
}

MIRROR_NOTES = {
    1: "the 92-node Batumi snapshot on its own ground",
    4: "Batumi mirrored into four reflected copies - 368 nodes over the same terrain, so size moves "
    "and the ground does not. Three-quarters of the resulting pairs fall outside the fitted link "
    "budget, so read pairs_beyond_calibration before anything else here",
}


def describes():
    """{cell name: one sentence}, composed from the scale and the preset it crosses."""
    return {
        f"batumi-x{mirror}-{preset}": (
            f"{MIRROR_NOTES[mirror]}, on {PRESET_NOTES[preset]}. Crossed against the archive off "
            f"and at every placement and count, so the capping of the role-bounded placements is "
            f"visible rather than hidden."
        )
        for preset, mirror in itertools.product(PRESETS, MIRRORS)
    }


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


# How many jobs a cell's arms are split across, by scale. Measured on a GitHub runner rather than
# guessed: an x1 cell's ten arms at 72 h took 110 minutes, and x4 is 3.15x that per run - about 346
# minutes, past this workflow's ceiling and close to the platform's own 360-minute hard limit, which
# no timeout can raise. Split three ways it is ~115 minutes, the same size as an x1 job.
#
# Splitting the arms is only sound because placement draws from its own stream (see
# Campaign._place_servers): every arm carries the control's offered load whichever job it lands in, so
# a cell reassembled from three shards is the same cell. Before that fix this split would have been
# the confound it warns about.
SHARDS_BY_MIRROR = {1: 1, 4: 3}


def arms():
    """Every (label, place, servers) this matrix runs, baseline first."""
    return [("baseline", None, None)] + [
        (f"{place} x{servers}", place, servers)
        for place, servers in itertools.product(PLACES, SERVERS)
    ]


def shard_of(all_arms, index, total):
    """The `index`-th of `total` contiguous slices of the arm list.

    Contiguous, not strided, so a half-finished round reads as a partial with its control in it.
    """
    if total <= 1:
        return list(all_arms)
    size = -(-len(all_arms) // total)  # ceiling, so the last shard is the short one
    return list(all_arms)[index * size : (index + 1) * size]


def run_cell(name, preset, mirror, seeds, out_dir, tag=None, shard=None):
    """Every placement and count at one preset and one scale, plus the baseline control per seed.

    `tag` names a shard's file; without it merged artifacts overwrite and one seed wears the cell.
    """
    parser = build_parser()
    results = []
    chosen = arms()
    if shard:
        index, total = shard
        chosen = shard_of(chosen, index, total)
    for label, place, servers in chosen:
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
    ap.add_argument(
        "--shard",
        help="run only part of a cell's arms, as i/n - e.g. 0/3 for the first third. Every shard "
        "keeps the cell's name, so the digest reads them as one block. See SHARDS_BY_MIRROR",
    )
    opts = ap.parse_args(argv)
    shard = None
    if opts.shard:
        try:
            index, total = (int(part) for part in opts.shard.split("/", 1))
        except ValueError:
            return ap.error(f"--shard wants i/n, got {opts.shard!r}")
        if not 0 <= index < total:
            return ap.error(f"--shard {opts.shard} is out of range")
        shard = (index, total)

    known = cells()
    if opts.list:
        notes = describes()
        for name, (preset, mirror) in known.items():
            shards = SHARDS_BY_MIRROR.get(mirror, 1)
            per_shard = len(shard_of(arms(), 0, shards)) * len(opts.seeds)
            runs = len(arms()) * len(opts.seeds)
            print(
                f"{name:28} {preset} x{mirror}  {runs} runs, "
                f"{shards} shard(s) of up to {per_shard}"
            )
            print(f"{'':28} {notes[name]}")
        print(f"\n{len(known)} cells, {len(opts.seeds)} seeds each")
        return 0
    if not opts.cell:
        return ap.error("give --cell or --list")
    if opts.cell not in known:
        return ap.error(f"unknown cell {opts.cell!r}; --list prints them")
    preset, mirror = known[opts.cell]
    run_cell(opts.cell, preset, mirror, opts.seeds, opts.out, opts.tag, shard)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
