"""The simulator's own version, stamped into every report, digest, figure and artifact name.

`transport_pin()` already records the commit that produced a run, and a commit is the precise answer.
It is a poor *label*: it does not order (is `b4a5ba4` before or after `feb8673`?), it does not survive a
rebase, and it says nothing about whether two runs are comparable. A result that has to be discarded is
almost never discarded because of one commit - it is discarded because a behaviour changed, and what a
reader needs is a number that says "these two runs measured the same thing".

So both are kept and they answer different questions:

  SIM_VERSION   is this run comparable with that one?
  transport     exactly which code produced it?

**Bump MINOR when a change makes existing results incomparable** - a fixed confound, a changed default,
a corrected measurement. Bump PATCH for anything that cannot move a number: a new output, a chart, a
doc, a test. The history below is the changelog, and it is the only place to look when a stored result
is suspect.
"""

# (version, what changed, and whether it invalidates earlier runs)
HISTORY = [
    (
        "1.0.0",
        "The baseline: everything up to and including the 2.8 fold-in, the sweeps, the cross and the "
        "digest, as it stood when versioning was introduced.",
        None,
    ),
    (
        "1.1.0",
        "Placement draws from its own stream. `random-any` and `random-clients` sampled from the run's "
        "shared RNG, which shifted the traffic generator's later draws - so a randomised placement "
        "carried a different offered load from the control it is subtracted from (measured: 31 texts "
        "and 298 positions against 32 and 289, reach 0.343 against 0.371). Also raises the matrix "
        "sweep from 2 simulated hours to 72 and the cross from 24, so a diurnal cycle is present.",
        "INVALIDATES every earlier result involving `random-any` or `random-clients`, and every "
        "matrix or design figure measured at the old durations.",
    ),
]

SIM_VERSION = HISTORY[-1][0]


def version_note():
    """One line naming this version and what it last changed, for a report header or a chart footer."""
    _, what, _ = HISTORY[-1]
    return f"sim {SIM_VERSION}: {what.split('.')[0]}."
