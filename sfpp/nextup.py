"""Which part of a sweep to run next, decided by what the archive already holds.

A rotation keyed on the date is stateless and even - and it marches on regardless. If a day's run
fails, or never fires, or dies half way, that part is simply missing until the cycle comes round again:
three days for the matrix, five for the cross. Nothing notices, because nothing looks.

So the schedule asks the archive instead. Each firing picks the part that has gone longest without a
digest - never-run first, then oldest - which means a failed part is retried by the *next* firing
rather than skipped, and a part that is already covered waits its turn. Self-healing, and still
stateless: there is no cursor to get out of step, only the record of what has actually run.

Two consequences worth knowing:

  * **An in-flight run has no digest yet.** Two firings close together could pick the same part. The
    workflows' concurrency groups already serialise runs of the same sweep, so the second waits, and by
    the time it plans, the first's digest exists and it picks the next part.
  * **A part that keeps failing keeps being chosen**, which is the intended behaviour - it is the
    part with no results - and it is visible as a run that fails repeatedly rather than as an absence.

Usage, from the tree root:
    python3 -m sfpp.nextup --surface matrix --archive runs --count 2
    python3 -m sfpp.nextup --surface design --archive runs
"""

import argparse
import glob
import json
import os
import sys


def coverage(archive_dir):
    """{block name: newest run_id that carried it}, from the digests in an archive.

    Digests, not raw JSONs, which are pruned; an unparseable one is skipped rather than fatal.
    """
    seen = {}
    if not archive_dir or not os.path.isdir(archive_dir):
        return seen
    for path in sorted(glob.glob(os.path.join(archive_dir, "*", "summary.json"))):
        try:
            with open(path) as f:
                digest = json.load(f)
        except (OSError, ValueError):
            continue
        # `generated` is when the digest was written; run_id is what names it on the page. Sorting on
        # generated rather than the id keeps this working if the id format ever changes.
        stamp = digest.get("generated") or ""
        for block in digest.get("blocks") or []:
            name = block.get("block")
            if not name:
                continue
            if name not in seen or stamp > seen[name][0]:
                seen[name] = (stamp, digest.get("run_id"))
    return {name: run for name, (_, run) in seen.items()}


def staleness(declared, archive_dir):
    """`declared`, ordered stalest first: never run, then longest since a digest.

    Ties break on name, so a retry picks the same part as the run it is retrying.
    """
    seen = {}
    for path in sorted(glob.glob(os.path.join(archive_dir or "", "*", "summary.json"))):
        try:
            with open(path) as f:
                digest = json.load(f)
        except (OSError, ValueError):
            continue
        stamp = digest.get("generated") or ""
        for block in digest.get("blocks") or []:
            name = block.get("block")
            if name and (name not in seen or stamp > seen[name]):
                seen[name] = stamp
    # "" sorts before any timestamp, so never-run parts come first.
    return sorted(declared, key=lambda name: (seen.get(name, ""), name))


def matrix_parts(archive_dir, count):
    """The `count` stalest matrix cells."""
    from .matrix import cells

    return staleness(sorted(cells()), archive_dir)[:count]


def design_parts(archive_dir, count=1):
    """The `count` stalest design meshes, judged by their own cells' coverage.

    A mesh, not a cell, is the unit a round is cut into; its staleness is its stalest cell's.
    """
    from .design import MESHES, cells

    known = cells()
    order = staleness(sorted(known), archive_dir)
    rank = {name: i for i, name in enumerate(order)}
    meshes = [m for m, _ in MESHES]
    return sorted(
        meshes,
        key=lambda mesh: min(
            (rank[c] for c, (m, _, _, _) in known.items() if m == mesh),
            default=-1,
        ),
    )[:count]


def main(argv=None):
    ap = argparse.ArgumentParser(description="which part of a sweep has gone longest without a digest")
    ap.add_argument("--surface", required=True, choices=("matrix", "design"))
    ap.add_argument("--archive", required=True, help="directory of run directories, each with summary.json")
    ap.add_argument("--count", type=int, default=1)
    opts = ap.parse_args(argv)
    if opts.count < 1:
        return ap.error("--count must be at least 1")
    parts = (
        matrix_parts(opts.archive, opts.count)
        if opts.surface == "matrix"
        else design_parts(opts.archive, opts.count)
    )
    if not parts:
        print("nothing declared", file=sys.stderr)
        return 1
    print(" ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
