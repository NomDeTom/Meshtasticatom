# Seventeen ways this simulator produced a confident wrong number

Companion to [README.md](README.md), which is the operating manual. This is the other half: not how
to run the thing, but how it has lied. All seventeen are fixed. They are written down because the
**shapes** recur, and because someone extending this tree can assert against them rather than
rediscover them one at a time.

Every entry ends with the check that would have caught it, and where that check lives now. Most are
enforced automatically on every scheduled run; the two that are not are marked.

## The defects

**1. A `Scenario` with no nodes was falsy.** `__len__` returned the node count, and a landform is
ground under a *generated* mesh - terrain rows, no points. So `if scenario:` was `False`, the run
came out flat, and the label still said `alpine`. No error, no warning, a plausible number, a wrong
label.

> **Assert** the run's `ground` block is non-null whenever `--scenario` was passed.
> **Enforced**: `collate.check_cell` - fatal, plus a warning when ground exists but no terrain was
> applied.

**2. Roles were parsed and thrown away.** `preset_scenario` read `isRouter` and `isClientMute` into
the Scenario; `build()` applied neither. Batumi ran as 92 CLIENT nodes, so `--place routers`
filtered for `role == ROUTER`, found none, and every placement experiment was answered by a mesh
with no routers in it.

> **Assert** the built role histogram matches the scenario's.
> **Not enforced.** The report carries `mesh.routers` but not the scenario's own histogram to
> compare it against, so the check needs a field that does not exist yet.

**3. The fitted link model was loaded and ignored.** Batumi ships 296 observed links and a ridge fit
over them. The transport computed the raw budget instead - which breaks the mesh into 15 components
where the observations show one. The report meanwhile claimed `link_calibration_applied: true`.

> **Assert** `link_calibration_applied` reflects what the link budget actually did.
> **Enforced by construction**: the field is now written `False` and the code says why - this
> transport layers its own per-node gains onto the raw budget, and the fit was trained against a
> budget without them. Saying "applied" because the coefficients parsed would be a lie in the one
> field a reader checks before trusting a link.

**4. The fit was extrapolated three times past its evidence.** Its ground-elevation terms are
positive and unbounded (+4.24 dB per 100 m of the lower endpoint) against a distance penalty of only
-4.68·log₁₀(km). Past the observed range two hilltop nodes gain more from elevation than distance
takes away, and the model invents a link. Mirroring exposed it: links to **60.6 km** on a snapshot
whose longest observation is **23.2 km**.

> **Assert** pairs stay inside `ground.calibration_envelope_m` whenever a fitted scenario is in play.
> **Enforced**: `collate.check_cell` warns with the count and the envelope in km. Expect it to fire
> on every `--mirror` run - seam-spanning pairs are outside the envelope by construction.

**5. A receiver counted the transmitters it collided with.** Channel utilisation charged every
audible transmission its full airtime, so overlapping signals billed a node twice or three times and
the figure ran to **184% of wall-clock**. A radio has one energy detector: overlapping signals are
one busy stretch, and on failure it learns that an Rx failed, not why or how many were talking.

> **Assert** `node_channel_util_percent.max <= 100`. Cheap, and a physical invariant rather than an
> opinion.
> **Enforced**: `collate.check_cell` - fatal.

**6. Role-bounded placements capped silently.** `routers` and `beside-router` cannot exceed the
mesh's router count - four, on Batumi - so a sweep over 2-6 servers produced three real rows and two
that repeated the fourth, indistinguishable once only the *requested* count was recorded.

> **Assert** `servers_placed == servers_requested`, or record both and group on the former.
> **Enforced**: both are recorded, `collate.check_cell` warns on a mismatch, and `sfpp/matrix.py`
> deliberately sweeps counts that straddle the cap so the capping is visible rather than hidden.

**7. The terrain index was slower than the sort it replaced.** Written for SRTM tiles, applied to a
42-point preset, where widening rings over sparse buckets costs more than scanning all 42. 1.48 s of
a 5.19 s build.

> **Assert** a block's runtime against its own history.
> **Enforced**: `collate.check_timing`, when `--history` points at the archive - which the scheduled
> runs now pass. Compared as **wall-clock seconds per simulated hour**, never as the raw `wall_seconds`
> sum: the sum moves whenever the seed count or `--hours` moves, so gating on it would have flagged
> every block in the archive the night the sweeps went from 2 h and 24 h to 72, and taught everyone to
> ignore the gate before it ever caught anything. Warn-only, at 2x, in **both** directions - a block
> that got four times faster has not been optimised, and a fragmented mesh or an arm that stopped being
> read both cost less to simulate.

**8. Tiling destroyed the clutter raster's regularity.** A reflection fixes the tile boundary, so
adjacent tiles each contribute the same column. Duplicate coordinates break
`ClutterGrid.is_regular`, and an irregular grid abandons its bisect to scan every sample on every
lookup. A 2×2 build ran 23 minutes before being killed; deduplicated it takes 41 s.

> **Assert** the clutter grid is regular after any scenario transform.
> **Not enforced.** The grid's regularity is not in the report, so the check would have to run
> inside the transform rather than over the output.

**9. The campaign sized per-node structures from `--nodes`.** Real geometry decides its own count
(Batumi is 92, the default is 60), so the first Batumi run died on `KeyError: 75`.

> **Caught by any run over a fixed-geometry scenario** - it crashes rather than lying, which is the
> good case. The digest additionally reads `nodes` from `ground` rather than from `--nodes`, because
> the requested figure describes a mesh that was never built.

**10. Aggregate demand was read as saturation.** `traffic.channel_utilisation` sums airtime demand
across the whole mesh and legitimately exceeds 1.0. It is **not** a utilisation, and for a spatially
extended mesh it is not even a proxy for one: nodes 30 km apart never contend, so demand grows with
mesh size while local utilisation does not. Measured: LONG_FAST at ×4 reads 9.55× demand with its
busiest node at 82.6% - and 82.4% at ×1, where demand was 2.45×. Reading demand as "saturated" led
to a whole analysis describing genuine comparisons as rankings of collapse.

> **Never gate or describe a run on demand.** Use `node_channel_util_percent` p90 and max, and name
> the two apart in any output: demand is a ratio, utilisation is a percentage.
> **Enforced**: the digest calls the field `demand` throughout, gates on `chutil` instead, and the
> explorer labels the columns `demand ×` and `chutil p90/max %`.
>
> One correction, recorded because the original entry overstated it: the naming distinction **was**
> documented, in [README.md](README.md) §7.1, complete with a warning that confusing the two
> overstates congestion because of spatial reuse. The trap was not reading the manual. The
> substantive half - a mesh-wide aggregate is not a local condition - stands.

## The shapes worth recognising

- **A default that silently substitutes.** 1, 2 and 3 all had a working fallback that produced a
  well-formed number. Nothing errored. Prefer failing loudly to defaulting quietly. This one recurs
  outside the simulator too: the firmware-discovery in `check_oracle.py` was written to fall back to
  a sibling checkout when `MESHTASTIC_FIRMWARE_ROOT` was wrong, which meant a typo produced 628
  passing checks against a tree the caller had not asked for.
- **A model asked outside its evidence.** 4 is the general case: a fit answers any input, including
  ones it has never seen, and linear extrapolation of a bounded physical quantity is unbounded.
  Anything fitted needs its envelope recorded and enforced.
- **An optimisation that changes an answer or a cost.** 7 and 8 were both performance work that
  either cost more than it saved or broke an invariant a downstream structure relied on.
- **Attributing knowledge to a node that no radio has.** 5 is [README.md](README.md) §1 rule 1
  broken directly. When adding anything node-side, the question is "how would the device learn
  this?"
- **A mesh-wide aggregate read as a local condition.** 10 fooled the analysis longest, because the
  number was correct and only its meaning was wrong.
- **A request and a result recorded as one number.** 6 and 9 are both a requested parameter and a
  derived one disagreeing, with only one written down.

## The two gates worth keeping permanently

Everything above is a check against a defect that has already happened. These two catch what nobody
predicted, and both run on every push in `.github/workflows/tests.yml`:

- **`node_channel_util_percent.max <= 100`** - a channel cannot be busy more than all the time.
- **A no-scenario run is byte-identical at a fixed seed.** Draws are hashed on
  `(seed, constant, window)` rather than pulled from a sequential stream, so this holds across
  adding and removing draws, and a paired before/after at one seed is a valid comparison. It has
  proved a change inert four separate times.

## 11. The inert-arm check was half a check

Found 2026-08-19, while confirming that the new per-run outputs had not disturbed the digest - which is
to say, by accident, like most of the entries above.

`_inert` compares every number in the reports and reports an arm whose cells are identical. `value` -
**the arm's own setting** - was not on the excluded list beside `opts`, and on an arm swept over numbers
`value` is itself a number. So it always distinguished the cells, and **no numeric-valued block could
ever be reported inert: 40 of the 87.** `E-capacity`, `E-width`, `G-servers`, `F-loss`, `F-hoplimit`,
`J-window` and thirty-four more.

It kept working for string-valued arms, which is why it survived: `D-cadence` was protected and
`E-capacity` was not, and nothing distinguishes those two in any output. README §8 calls this one of the
two checks worth keeping permanently, and §10.4's whole point is that a flag needing an enabler
produces well-formed identical rows - the failure this check exists to catch, unguarded for half the
sweep.

> **Assert** that an arm swept over numbers can still be reported inert, and that one with a real
> difference still is not.
> **Enforced**: `value` is in `NOT_A_MEASUREMENT`, with a test in each direction.

The shape is one already on the list - "a request and a result recorded as one number" - with the twist
that here the request was mistaken for the result *by the checker*. Worth asking of any comparison in
this tree: is anything on both sides of it?

## 12. A randomised placement did not carry the control's traffic

Found 2026-08-19, while testing whether a cell's archive arms could be split across CI jobs - so found
by asking whether a *different* thing was safe.

`random-any` and `random-clients` pick with `rng.sample`; the deliberate strategies sort by degree and
draw nothing. Both took their samples from `self.rng`, the run's shared stream. The traffic generator is
built before placement but *scheduled after it*, so consuming those draws shifted every later draw and
the generator produced a different schedule. At seed 4242, 25 nodes, 2 h:

| arm | text | position | telemetry | reach |
| --- | --: | --: | --: | --: |
| `off` (control) | 31 | 298 | 104 | 0.343 |
| `spread x2` | 31 | 298 | 104 | 0.343 |
| `beside-router x2` | 31 | 298 | 104 | 0.343 |
| **`random-any x2`** | 32 | 289 | 106 | **0.371** |
| **`random-any x6`** | 35 | 324 | 101 | **0.355** |

An 8% reach difference, the same order as the effects these sweeps exist to measure, between the control
and **the one arm whose whole job is to be the control** - `random-any` is described in `campaign.py` as
"the honest control for any claim that a deliberate arrangement beat chance", and it was the only arm
not carrying the control's traffic. `--servers` made it worse: more servers means more samples drawn, so
a count sweep confounded count with load.

> **Assert** that every placement and every server count reproduces the control's offered load.
> **Enforced**: `test_matrix.PlacementIsolation`, three tests. Placement now draws from
> `random.Random(seed ^ 0x504C4143)` - the pattern `_noise_field` and `_ducting` already used, and for
> the reason their comments give: "seeded off the run's seed but through its own constant, so the field
> is reproducible without being correlated with anything else the seed decides".

Two things worth carrying from this one. First, the shape: **a shared RNG is a shared mutable
dependency**, and "draws are hashed on (seed, constant, window) rather than pulled from a sequential
stream" was true of the physics and not of this. Second, the *reason it was found* - `design.py`'s header
warned against splitting the archive axis because "a cell's control comes from a different draw than the
arms it is subtracted from", and testing that warning is what exposed it. The warning was right, about a
defect that was already there without any splitting.

## 13. Every frame was 37-60% too long

Found 2026-08-20, in a review of the discrete-event simulator - the one defect here that was never
found by this tree's own checks, because every check compares runs against each other and all of
them were wrong the same way.

`lib.phy.airtime` is the Semtech payload-symbol formula, which multiplies by the coding-rate
**denominator** - 5 for 4/5, 8 for 4/8. The same formula is often written `(CR + 4)` with `CR` an
index 1..4, reaching the same number from the other side. The code used the second form against a
stored denominator, so it multiplied by 9 where the radio uses 5. LONG_FAST read 1042 ms at a
40-byte payload against a true 682 ms; the smallest error in the table was 37%.

Airtime is not one number among many. It sets how long a transmitter holds the channel, how much
two frames overlap, when a retransmission is due, and what channel utilisation reads - so contention,
collisions and every derived rate inherit the error. This transport calls the same function.

A second defect sat two lines below it: low data rate optimization was gated on `bw == 125e3 and sf
in (11, 12)` where the firmware gates it on symbol time, `(1 << sf) / bw >= 16`. VERY_LONG_SLOW -
SF12 at 62.5 kHz, the longest symbol of any preset - was the one setting running without it.

> **Assert** airtime against ground truth from outside this tree, not against itself.
> **Enforced**: `tests/test_phy_airtime.py` pins three published LoRaWAN vectors (SF7/BW125/4/5 at
> 13 B = 46.336 ms, SF12/BW125/4/5 at 13 B = 1155.072 ms and at 64 B = 2793.472 ms), locks all ten
> presets, and checks the LDRO boundary from both sides.

The shape is new to this list and worth naming: **a formula fed the wrong units of its own
parameter**. It cannot be caught by comparing runs, by determinism, or by any invariant internal to
the simulator - every number stays plausible, ordered correctly against every other number, and
wrong. Only an external vector catches it. Anything in this tree implementing a published formula
should be pinned to a published value.

## 14. Interference could not be turned off

Found 2026-08-20, in the same review.

`is_channel_active` - the CAD check every transmitter runs before keying up - drew
`random.randrange(10) <= INTERFERENCE_LEVEL * 10`. Both ends of that comparison are inclusive, so
the level was quantized to tenths *and floored at one*: 0.00 drew 10%, 0.05 drew 10%, 0.10 drew 20%,
0.50 drew 0.60. Measured over 200,000 samples, exactly those figures.

The floor is what makes it a trap rather than an inaccuracy. Nothing gates that draw, so every run
in this tree's history - including every run whose config set interference to zero to isolate
Meshtastic's own contention - deferred about a tenth of its transmissions to a channel nothing was
transmitting on.

> **Assert** a probability parameter at its endpoints, not in the middle. 0.0 must never fire and
> 1.0 must always fire; a bug that only shifts the middle is an inaccuracy, one that breaks an
> endpoint is a control that does not work.
> **Enforced**: `tests/test_interference.py` checks both endpoints and four intermediate levels, and
> `Config.INTERFERENCE_LEVEL` now rejects anything outside [0, 1] when set.

## 15. Reach counted overhearers against addressees

Found 2026-08-20, in the same review.

`nodeReach` was `nrUseful / (messageSeq * (N - 1))`. The denominator's `messageSeq` was one counter
incremented for application messages **and** for generated ACKs, so every unicast ACK added N-1
addressees to it. The numerator counted the first arrival of any packet at any node - including a
node that merely overheard a DM addressed to someone else.

Neither half counted the same population as the other, and nothing bounded the ratio. Measured on an
8-node DM run: 220% reach.

It agreed with the corrected figure exactly on a broadcast-only run, which is every default run, and
that is why it survived. The mixing only shows up where ACKs or DMs exist.

> **Assert** that a rate's numerator and denominator count the same population, and that a
> percentage cannot exceed 100.
> **Enforced**: `tests/test_metrics.py` counts the six populations apart - messages, ACKs, packet
> ids, transmissions, relays, receiver opportunities - and `docs/metrics.md` names each one.

## 16. Every macOS node ran out of node 0's state directory

Found 2026-08-20, by reading the review's report of it.

The macOS Docker path started each additional node with `-d /home/node{n0.nodeid}` - `n0`, the first
node, not `n`. Every meshtasticd process therefore shared one data directory, reading and writing
the others' identity and configuration. The Linux path, three lines below, was correct.

> **Assert** over the whole set of generated commands, not one of them: distinct data directories,
> ports and hardware ids.
> **Enforced**: `tests/test_interactive.py`, over commands built by one shared function so both
> platforms cannot drift apart again.

## 17. Files named a firmware version they did not implement

Found 2026-08-20, while checking what each part of the tree was pinned to.

`lib/mac.py` and `lib/phy.py` said "checked as of tag v2.7.15.567b8ea". The region table beside them
said nothing and was v2.7.15's data. The frequency calculation matched no version at all - it
omitted the half-bandwidth centre offset both versions have, putting US LongFast at 908.75 MHz
where a device sits at 906.875. And `lib/mac.py`'s router test was *2.8's* behaviour, CLIENT_BASE
having lost its early rebroadcast window after 2.7 - correct by accident, against a comment naming
the version where it was wrong.

Two more surfaces named no version at all: the interactive harness ran `meshtastic/meshtasticd`
untagged, so it tracked whatever `latest` resolved to on the day, driven by a 2.6.1 client; and
`lib/dcr.py` describes dynamic coding rate as "the firmware idea" when no released firmware has it.

> **Assert** the pin, do not just write it down. A version claim that cannot fail is decoration.
> **Enforced**: `tests/test_docs.py` checks the commit named in the docs is the one named in each
> pinned file and that the documented daemon image is the one that runs;
> `tests/test_region_frequency.py` checks the region set against the pinned tree, which is
> checkable because 2.8 removed `UA_868` and added the ITU ham regions.

## What is still open

An arm whose cells are identical in every number the report carries did nothing - it was accepted on
the command line, stored, and never read. That has happened twice, and both times the run produced a
well-formed table supporting the opposite of the truth. `collate.py` warns on it, comparing every
number in the report rather than a chosen few: the first version of that check compared only the
metrics the digest displays and called `E-signed` inert, when the arm moves `advert_bytes` by 43%
and nothing else. Some flags legitimately need a second flag before they do anything, which is why
this warns and names the arm rather than failing - [README.md](README.md) §10.4 lists them.
