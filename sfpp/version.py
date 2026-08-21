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
    (
        "1.2.0",
        "Airtime and channel-busy corrections in `lib.phy`, which this transport calls for every "
        "frame. Time on air multiplied by the coding-rate denominator plus four rather than the "
        "denominator, inflating every preset by 37-60% (LONG_FAST 1042 ms against 682 ms at a "
        "40-byte payload), and low data rate optimization was gated on bandwidth rather than "
        "symbol time, so VERY_LONG_SLOW ran without it. The channel-busy draw was quantized and "
        "floored at 10%, so a level of 0.00 still deferred a tenth of all transmissions.",
        "INVALIDATES every earlier result: airtime sets contention, collision overlap, "
        "retransmission timing and channel utilisation, and no run in the archive was measured "
        "with the corrected figures.",
    ),
    (
        "1.3.0",
        "The vendored physics review, which this transport calls for every link. Terrain "
        "diffraction added TERRAIN_FRESNEL_CLEARANCE into the obstruction height and then computed "
        "the knife-edge parameter from it, offsetting v by a constant 0.849 - a grazing path cost "
        "12.91 dB against a true 6.03, and the loss stepped from 0 to 6.03 dB across the clearance "
        "threshold. The clutter model charged its cheapest rate for any class it did not recognise, "
        "resolved a 500 m cell by a fixed order so one pond made a city block read as water, and "
        "applied a 4x coastal discount on a test that `open` - the exporter's default for an "
        "unmapped cell - satisfied on a quarter of all pairs. Link asymmetry was one antisymmetric "
        "draw with no shadowing at all, so link existence was a near-deterministic function of "
        "geometry; shadowing is now a reciprocal 6 dB term on the path, with radio asymmetry kept "
        "separate at 2 dB. The fitted link calibration is now refused beyond its own observed "
        "envelope in the vendored budget as well as here.",
        "INVALIDATES every earlier result over a scenario with terrain or clutter, which is every "
        "matrix and design cell: Batumi's directed link count moves 5033 -> 4813 at seed 7. Flat "
        "generated meshes move too, through the shadowing term.",
    ),
    (
        "1.4.0",
        "The second half of the same physics review, and the corrections it needed. A threshold "
        "derived from a sensitivity table can no longer outlive the noise floor it was measured "
        "against: `effective_sensitivity` is max(datasheet, floor + the spreading factor's required "
        "SNR), so Batumi's -110.5 dBm median raises LONG_FAST's threshold from -131.5 to -128.0. "
        "The floor itself moves - a median with correlated spread, clamped below by kTB - and every "
        "threshold derived from it moves with it: delivery, the CAD floor, the capture audience and "
        "the ducted audience each read the receiver's own band for the frame, where a NoiseField "
        "excursion previously arrived only as an RSSI penalty inside the PER curve and so could "
        "fail a packet but never take a link down (measured: 19 directed links differ in existence "
        "between two instants at 6 dB of spread, where none could before). `NOISE_LEVEL` derives "
        "from the preset's bandwidth instead of being one constant across a 15 dB range of thermal "
        "noise, and the payload curve is anchored to the modem's own requirement rather than to an "
        "absolute SNR per coding rate. `--noise-model fixed` names the old constant explicitly, "
        "since the vendored default is no longer it. Path loss is floored at free space. On the "
        "vendored side, the channel-utilisation transmit gate defers instead of dropping, reliable "
        "broadcast and unicast carry their two separate firmware budgets, duplicate suppression is "
        "capacity-bounded at 240, and channel-busy time is charged as the union of overlapping "
        "receptions rather than per reception.",
        "INVALIDATES every 1.3.0 result. Batumi's directed link count moves 4813 -> 3754 at seed "
        "7, on the sensitivity correction alone; any run with a noise profile moves again, because "
        "an excursion can now remove a link and not merely dim it.",
    ),
]

SIM_VERSION = HISTORY[-1][0]


def version_note():
    """One line naming this version and what it last changed, for a report header or a chart footer."""
    _, what, _ = HISTORY[-1]
    return f"sim {SIM_VERSION}: {what.split('.')[0]}."
