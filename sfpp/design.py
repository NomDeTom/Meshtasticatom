"""Three axes crossed: how the archive is configured, what else could be spent instead, and where.

`sweep.py` moves one flag at a time with the archive switched on in every cell, because `--protocol`
is not in its BASE and the campaign default is `sr`. That answers "what does this variable do to a
mesh" and cannot answer "what is the archive worth", which is the question the design exists to
settle. A topology sweep run that way reports that a corridor delivers less than a hub - true, and a
statement about mesh physics rather than about anything proposed here.

So this module crosses three axes and pins everything else:

  * **archive** - `off`, and every placement at every count. Crossed rather than swept because
    placement and count interact: a count above the router cap is the same run twice under a
    role-bounded placement.
  * **rivals** - the routing and throttle settings that could be changed *instead of*, or as well
    as, deploying an archive. An extra relay of every text, favouriting routers, the coding-rate
    ladder, early flooding, raised hop limits, and both of the firmware's scaling constants.
  * **mesh** - Batumi, and Batumi under the conditions a deployed mesh actually meets: scaled up,
    part-way through a firmware upgrade, on a faster preset.

The mesh axis is what makes the other two mean anything. A cross on one mesh says "0.489 held here";
the same cross on the same geometry scaled up and part-upgraded is what turns it into advice that
names its conditions. Traffic is not on any axis - every cell carries the same load, because
changing it changes every cell equally.

Within each mesh, the cell at `rival=none, archive=off` is the reference every other cell in that
mesh is a difference against. `hop-scaling-40` and `congestion-40` restate firmware constants, so
each must reproduce `none` cell for cell; they are kept as arms because a cross that cannot
reproduce its own baseline is wired wrong and this is the cheapest way to notice.

Output is the shape `sweep.py` writes - each report carrying `block`, `arm` and `value` - so
`collate.py` and `explorer.py` read these runs through the same path as the block sweeps. Each
report also carries `mesh`, `rival` and `archive` as their own fields, so the cross can be
re-tabulated along any axis without re-running anything.

Usage, from the tree root:
    python3 -m sfpp.design --list
    python3 -m sfpp.design --cell batumi-hop-limit-15 --seeds 7 11 13 --out runs/
"""

import argparse
import itertools
import json
import os
import time

from . import autochart as AC
from .campaign import build_parser, run_once

# --- axis three: the mesh the cross is run on ----------------------------------------------------
#
# Batumi is in every round: it is the only real geometry here, and everything else on this axis is
# a condition applied to it, so that a finding can be advice rather than an observation.
MESHES = [
    ("batumi", ["--scenario", "batumi"]),
    # The same place tiled into reflected copies, so size moves and the ground does not. Read
    # pairs_beyond_calibration first: seam-spanning pairs are outside the fitted budget.
    ("batumi-x4", ["--scenario", "batumi", "--mirror", "4"]),
    # A mesh part-way through upgrading, which is every real mesh.
    ("batumi-legacy-25", ["--scenario", "batumi", "--legacy-fraction", "0.25", "--old-profile", "2.6"]),
    ("batumi-legacy-50", ["--scenario", "batumi", "--legacy-fraction", "0.5", "--old-profile", "2.6"]),
    # The fast end of the presets a deployed mesh runs, against the default the others use.
    ("batumi-short-fast", ["--scenario", "batumi", "--preset", "SHORT_FAST"]),
]

# Traffic every cell carries, so the addressed measures have denominators. 72 hours because one
# pass of a diurnal curve cannot separate a time-of-day effect from where --start-hour landed.
TRAFFIC = [
    "--hours",
    "72",
    "--hop-spread",
    "--dm-per-hour",
    "6",
    "--dm-transport",
    "transport",
    "--traceroute-per-hour",
    "1",
    "--admin-probes-per-hour",
    "6",
    "--no-charts",
]

# --- axis one: the archive ----------------------------------------------------------------------
PLACES = ["random-any", "spread", "beside-router"]
SERVERS = [2, 3, 6]

# --- axis two: what else could be changed --------------------------------------------------------
#
# (label, flags), one change each and never combined - combining is a later question that would
# square an already square grid. Appending a line crosses it against everything already measured.
RIVALS = [
    ("none", []),
    ("extra-repeats", ["--extra-repeats"]),
    ("favourite-routers", ["--favourite-routers"]),
    ("coding-rate-ladder", ["--coding-rate-ladder"]),
    ("m4-early-flood", ["--dm-mode", "m4-early-flood"]),
    # Hop limits. The mesh runs per-node 3-7 by centrality; these put everyone on one ceiling, so
    # each is "everyone at N" rather than "N more hops than before".
    ("hop-limit-7", ["--no-hop-spread", "--hop-limit", "7"]),
    ("hop-limit-15", ["--no-hop-spread", "--hop-limit", "15"]),
    # Two different scalings, often confused. This one sets how many nodes the hop recommendation
    # aims to reach - HopScalingModule's literal 40 - so it scales the hop limit.
    ("hop-scaling-40", ["--hop-target-nodes", "40"]),
    ("hop-scaling-60", ["--hop-target-nodes", "60"]),
    ("hop-scaling-80", ["--hop-target-nodes", "80"]),
    # And this one sets the node count above which the firmware starts stretching broadcast
    # intervals - Default.h's literal 40 - so it scales the traffic rather than the reach.
    ("congestion-40", ["--congestion-pivot", "40"]),
    ("congestion-60", ["--congestion-pivot", "60"]),
    ("congestion-80", ["--congestion-pivot", "80"]),
]

# The two arms that restate a firmware default. Each must reproduce `none` cell for cell; a cross
# that cannot reproduce its own baseline is wired wrong, and this is the cheapest way to notice.
REPRODUCES_BASELINE = ("hop-scaling-40", "congestion-40")

# One sentence per coordinate, in a reader's terms rather than a flag's: the digest composes a
# cell's sentence from its mesh and its rival. sweep.DESCRIPTIONS is the same idea.
MESH_NOTES = {
    "batumi": "the 92-node Batumi snapshot on its own ground, at the shipped defaults",
    "batumi-x4": "Batumi mirrored into four reflected copies - four times the nodes over the same "
    "terrain, so size moves and the ground does not. Seam-spanning pairs sit outside the fitted "
    "link budget; read pairs_beyond_calibration before anything else",
    "batumi-legacy-25": "Batumi with a quarter of the mesh still on 2.6, as a mesh part-way through "
    "an upgrade",
    "batumi-legacy-50": "Batumi with half the mesh still on 2.6 - the upgrade stalled halfway",
    "batumi-short-fast": "Batumi on SHORT_FAST instead of LONG_FAST: more airtime per second and "
    "less range per hop",
}

RIVAL_NOTES = {
    "none": "nothing changed - the mesh as the firmware ships it",
    "extra-repeats": "a node tolerates a second heard copy before cancelling its own rebroadcast, "
    "so a text is relayed more often. Not in any release",
    "favourite-routers": "router-like nodes favourite each other, so a relay between two of them "
    "keeps its hop limit instead of spending one",
    "coding-rate-ladder": "each retransmission goes out at a higher coding rate - more redundancy "
    "and more airtime per attempt. Not in any release",
    "m4-early-flood": "an addressed message floods sooner instead of waiting out the directed "
    "attempts",
    "hop-limit-7": "every node at 7 hops instead of the per-node 3-7 by centrality. Also removes "
    "the centrality assignment, so it is two changes and reads as one",
    "hop-limit-15": "every node at 15 hops - a ceiling far past anything this mesh can use, which "
    "is the point: it shows what the limit was costing when it bound",
    "hop-scaling-40": "the hop recommendation still aims at 40 nodes, the firmware's own constant. "
    "This arm must reproduce the unchanged mesh exactly",
    "hop-scaling-60": "the hop recommendation aims at 60 nodes, so it suggests further travel",
    "hop-scaling-80": "the hop recommendation aims at 80 nodes - most of this mesh, and about as "
    "far as the suggestion can reach",
    "congestion-40": "broadcast intervals still start stretching above 40 nodes, the firmware's own "
    "constant. This arm must reproduce the unchanged mesh exactly",
    "congestion-60": "broadcast intervals hold their shipped cadence up to 60 nodes before "
    "stretching, so the mesh stays chattier for longer",
    "congestion-80": "broadcast intervals hold their shipped cadence up to 80 nodes - on a mesh "
    "this size, almost no throttling at all",
}


def describes():
    """{cell name: one sentence}, composed from the mesh and the rival it crosses."""
    return {
        f"{mesh}-{rival}": f"{MESH_NOTES[mesh]}; {RIVAL_NOTES[rival]}. Crossed against the archive "
        f"off and at every placement and count."
        for mesh, _ in MESHES
        for rival, _ in RIVALS
    }


def archives():
    """(label, flags) for each archive configuration, `off` first."""
    return [("off", ["--protocol", "none"])] + [
        (
            f"{place} x{servers}",
            ["--protocol", "sr", "--place", place, "--servers", str(servers)],
        )
        for place, servers in itertools.product(PLACES, SERVERS)
    ]


def cells():
    """One job per (mesh, rival): that pair crossed against every archive configuration.

    Mesh is the outer coordinate, so a round runs mesh by mesh without disturbing what is measured.
    """
    return {
        f"{mesh}-{rival}": (mesh, mesh_flags, rival, rival_flags)
        for mesh, mesh_flags in MESHES
        for rival, rival_flags in RIVALS
    }


# Measured, not guessed: the mirrored mesh at 72 h is ~444 minutes in one job, past the platform's
# 360-minute hard limit. Sound only because placement draws from its own stream - TRAPS 12.
SHARDS_BY_MESH = {"batumi-x4": 3}
DEFAULT_SHARDS = 1


def shards_for(mesh):
    return SHARDS_BY_MESH.get(mesh, DEFAULT_SHARDS)


def shard_of(items, index, total):
    """The `index`-th of `total` contiguous slices, so the `off` control lands in the first shard."""
    if total <= 1:
        return list(items)
    size = -(-len(items) // total)
    return list(items)[index * size : (index + 1) * size]


def run_cell(name, mesh, mesh_flags, rival, rival_flags, seeds, out_dir, tag=None, shard=None):
    """One (mesh, rival) pair against every archive configuration, at each seed.

    `tag` names a shard's file; every shard keeps the same `block`, which the digest groups on.
    """
    parser = build_parser()
    results = []
    chosen = archives()
    if shard:
        index, total = shard
        chosen = shard_of(chosen, index, total)
    for archive, archive_flags in chosen:
        for seed in seeds:
            opts = parser.parse_args(TRAFFIC + mesh_flags + rival_flags + archive_flags)
            started = time.time()
            report = run_once(opts, seed)
            report["block"] = name
            report["arm"] = "archive"
            report["value"] = archive
            # All three coordinates, so the cross re-tabulates along any axis later. `mesh_label`
            # because `mesh` is already the run's mesh statistics, and the digest reads its count.
            report["mesh_label"] = mesh
            report["rival"] = rival
            report["archive"] = archive
            report["grid"] = mesh_flags + rival_flags
            results.append(report)
            reach = (report.get("baseline") or {}).get("text_reception_mean")
            print(
                f"  {name} {archive} seed={seed} {time.time() - started:.0f}s"
                + (f" reach {reach:.3f}" if reach is not None else ""),
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
    ap = argparse.ArgumentParser(description="the archive crossed against what else could be spent")
    ap.add_argument("--cell", help="one cell from --list; a job's worth of work")
    ap.add_argument("--list", action="store_true", help="print the cells and what a round costs")
    ap.add_argument("--mesh", help="with --list, print only this mesh's cells")
    ap.add_argument("--seeds", nargs="+", type=int, default=[7, 11, 13])
    ap.add_argument("--out", default="runs")
    ap.add_argument(
        "--tag",
        help="suffix this shard's filename. For splitting one cell over several jobs; the cell "
        "keeps its name in the reports, so the digest still reads the shards as one block",
    )
    ap.add_argument(
        "--shard",
        help="run only part of a cell's archive configurations, as i/n - e.g. 0/3 for the first "
        "third. Every shard keeps the cell's name, so the digest reads them as one block. See "
        "SHARDS_BY_MESH",
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
        per_cell = len(archives()) * len(opts.seeds)
        shown = [
            label for label, (mesh, _, _, _) in known.items() if opts.mesh in (None, mesh)
        ]
        if not shown:
            return ap.error(f"unknown mesh {opts.mesh!r}; one of {', '.join(m for m, _ in MESHES)}")
        for label in shown:
            mesh = known[label][0]
            n = shards_for(mesh)
            print(
                f"{label:34} {per_cell:3} runs, {n} shard(s) of up to "
                f"{len(shard_of(archives(), 0, n)) * len(opts.seeds)}"
            )
        print(
            f"\n{len(MESHES)} meshes x {len(RIVALS)} rivals = {len(known)} cells,"
            f" each x {len(archives())} archive configurations x {len(opts.seeds)} seeds"
        )
        print(f"= {len(shown) * per_cell} runs for what is listed above")
        return 0
    if not opts.cell:
        return ap.error("give --cell or --list")
    if opts.cell not in known:
        return ap.error(f"unknown cell {opts.cell!r}; --list prints them")
    run_cell(opts.cell, *known[opts.cell], opts.seeds, opts.out, opts.tag, shard)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
