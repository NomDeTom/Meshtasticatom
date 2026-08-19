# Eleven ways this simulator produced a confident wrong number

Companion to [README.md](README.md), which is the operating manual. This is the other half: not how
to run the thing, but how it has lied. All ten are fixed. They are written down because the
**shapes** recur, and because someone extending this tree can assert against them rather than
rediscover them one at a time.

Every entry ends with the check that would have caught it, and where that check lives now. Nine are
enforced automatically on every scheduled run; two are not, and are marked.

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

## What is still open

An arm whose cells are identical in every number the report carries did nothing - it was accepted on
the command line, stored, and never read. That has happened twice, and both times the run produced a
well-formed table supporting the opposite of the truth. `collate.py` warns on it, comparing every
number in the report rather than a chosen few: the first version of that check compared only the
metrics the digest displays and called `E-signed` inert, when the arm moves `advert_bytes` by 43%
and nothing else. Some flags legitimately need a second flag before they do anything, which is why
this warns and names the arm rather than failing - [README.md](README.md) §10.4 lists them.
