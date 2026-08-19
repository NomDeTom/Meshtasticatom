"""One substrate, many arms, every one measured against the same control.

`sweep.py` moves one flag at a time with the archive switched on in every cell, because `--protocol`
is not in its BASE and the campaign default is `sr`. That answers "what does this variable do to a
mesh" and cannot answer "what is the archive worth", which is the question the design exists to
settle. A topology sweep run that way reports that a corridor delivers less than a hub - true, and a
statement about mesh physics rather than about anything proposed here.

So this module inverts the arrangement. A **substrate** - seed, topology, node count, area, hours,
preset - is pinned and shared. Every cell begins with a **control** arm that sites the archives and
leaves them silent, so each later arm is a difference against the same mesh carrying the same
traffic at the same seed rather than a comparison between two runs that differ in ways nobody wrote
down. Two families of arm sit on it:

  * **archive** - the archive's own design parameters, where it goes and how many of it there are.
    Crossed, because placement and count interact: a count above the router cap is the same run
    twice under a role-bounded placement.
  * **rivals** - one arm per mechanism that could be spent *instead of* the archive. An extra relay
    of every text, favouriting routers, the coding-rate ladder, early flooding. Each is measured
    against the same control the archive is, which is the only way to say whether the archive earns
    its complexity against something simpler.

**Adding a future idea is adding one line to RIVALS.** It then runs on the same seeds, the same
topologies and against the same control as everything already measured, which is what makes a result
from today and an idea tried in six months comparable at all.

Output is the shape `sweep.py` writes - each report carrying `block`, `arm` and `value` - so
`collate.py` and `explorer.py` read these runs through the same path as the block sweeps.

Usage, from the tree root:
    python3 -m sfpp.design --list
    python3 -m sfpp.design --cell archive-corridor --seeds 7 11 13 --out runs/
"""

import argparse
import itertools
import json
import os
import time

from . import autochart as AC
from .campaign import build_parser, run_once

# The substrate. Everything here is held fixed across every cell and every arm in this module, and
# changing any of it invalidates comparison with every result already stored - which is why it is one
# list with a name rather than defaults scattered over the arms.
#
# 24 hours because the diurnal cycle has to close; 60 nodes and 8 km because that is the mesh the
# block sweeps were measured on and their results should remain readable beside these; LONG_FAST
# because it is the default a deployed mesh runs. DMs and traceroutes are on so the addressed
# measures have a denominator and the DM-dependent rivals are not inert.
SUBSTRATE = [
    "--hours",
    "24",
    "--nodes",
    "60",
    "--area",
    "8000",
    "--preset",
    "LONG_FAST",
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

# The shapes every family is run over. A result that holds in one and not another is the finding;
# a result measured in only one is a result about that shape.
TOPOLOGIES = ["uniform", "clustered", "corridor", "hub"]

# Where the archive can go, and how much of it there is. Crossed rather than swept separately
# because the two interact: `routers` caps at the mesh's router count and repeats above it, so a
# count arm read without its placement is two identical rows and a wrong conclusion.
PLACES = ["random-any", "spread", "beside-router"]
SERVERS = [2, 3, 6]

# What could be spent instead of the archive. Each entry is (label, extra flags) and runs with the
# protocol off, so it is the mechanism on its own against the same control - not stacked on top of
# a running archive, which is what the block sweeps measure and why R-repeats could not answer the
# question its own comment poses.
#
# To add an idea: append one line. It inherits the substrate, the seeds, the topologies and the
# control, and becomes comparable with everything already here.
RIVALS = [
    ("control", ["--protocol", "none"]),
    ("archive", ["--protocol", "sr"]),
    ("extra-repeats", ["--protocol", "none", "--extra-repeats"]),
    ("favourite-routers", ["--protocol", "none", "--favourite-routers"]),
    ("coding-rate-ladder", ["--protocol", "none", "--coding-rate-ladder"]),
    ("m4-early-flood", ["--protocol", "none", "--dm-mode", "m4-early-flood"]),
    ("hop-limit-7", ["--protocol", "none", "--no-hop-spread", "--hop-limit", "7"]),
]


def cells():
    """{name: (family, topology)} - one job's worth of work per entry."""
    out = {}
    for topology in TOPOLOGIES:
        out[f"archive-{topology}"] = ("archive", topology)
        out[f"rivals-{topology}"] = ("rivals", topology)
    return out


def arms(family):
    """(label, flags) for each arm of a family, control first."""
    if family == "rivals":
        return list(RIVALS)
    # The archive family: the same silent control, then every placement at every count.
    return [("control", ["--protocol", "none"])] + [
        (
            f"{place} x{servers}",
            ["--protocol", "sr", "--place", place, "--servers", str(servers)],
        )
        for place, servers in itertools.product(PLACES, SERVERS)
    ]


def run_cell(name, family, topology, seeds, out_dir):
    """Every arm of one family on one topology, at each seed, against the same control."""
    parser = build_parser()
    results = []
    for label, flags in arms(family):
        for seed in seeds:
            opts = parser.parse_args(SUBSTRATE + ["--topology", topology] + flags)
            started = time.time()
            report = run_once(opts, seed)
            report["block"] = name
            report["arm"] = family
            report["value"] = label
            report["grid"] = ["--topology", topology]
            results.append(report)
            reach = (report.get("baseline") or {}).get("text_reception_mean")
            print(
                f"  {name} {label} seed={seed} {time.time() - started:.0f}s"
                + (f" reach {reach:.3f}" if reach is not None else ""),
                flush=True,
            )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{name}.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"wrote {path}")
    chart = AC.auto(results, path, kind="block")
    if chart:
        print(f"wrote {chart}")
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="one substrate, every arm against the same control"
    )
    ap.add_argument("--cell", help="one entry from --list; a job's worth of work")
    ap.add_argument(
        "--list", action="store_true", help="print the cells and what each covers"
    )
    ap.add_argument("--seeds", nargs="+", type=int, default=[7, 11, 13])
    ap.add_argument("--out", default="runs")
    opts = ap.parse_args(argv)

    known = cells()
    if opts.list:
        for name, (family, topology) in known.items():
            n = len(arms(family)) * len(opts.seeds)
            print(f"{name:22} {family:8} {topology:10} {n:3} runs per invocation")
        print(f"\n{len(known)} cells, {len(opts.seeds)} seeds each")
        print(f"substrate: {' '.join(SUBSTRATE)}")
        return 0
    if not opts.cell:
        return ap.error("give --cell or --list")
    if opts.cell not in known:
        return ap.error(f"unknown cell {opts.cell!r}; --list prints them")
    family, topology = known[opts.cell]
    run_cell(opts.cell, family, topology, opts.seeds, opts.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
