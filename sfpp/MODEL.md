# The model behind the numbers

Derivations and mechanisms the code assumes. [README.md](README.md) is the operating manual and
[TRAPS.md](TRAPS.md) is the list of ways this tree has produced a confident wrong number; this is
the third: why the arithmetic is what it is.

## Airtime

`sfpp/analytic/radio.py` computes LoRa time on air, and `validate.py` checks it against three
independent sources. The reference calculator's stated formula, implemented in `validate.py` from
the description alone rather than from `radio.py`:

```
T_sym           = 2^SF / BW_kHz
payload_bits    = 8·PL − 4·SF + 8 + 16·CRC + 20·explicit_header
bits_per_symbol = SF − 2 when LDRO else SF
payload_symbols = ceil(payload_bits / 4 / bits_per_symbol) · CR_denominator + 8
airtime          = (preamble + 4.25)·T_sym + payload_symbols·T_sym
```

`CR_denominator` is 5..8. Feeding it a coding-rate *index* instead inflates every airtime, which is
the shape of TRAPS 13 in the discrete-event simulator and of the 1-vs-5 error caught in this file's
first draft.

Two anchors worth keeping in mind when a figure looks wrong: LongFast's preamble is
`16 · 2048/250 = 131 ms`, and a full 233-byte LongFast frame is a little over two seconds. A figure
far from those is a preset or coding-rate mistake, not a rounding one.

Low data rate optimisation is on when a symbol lasts strictly longer than 16 ms. Nothing in the
Meshtastic preset table lands exactly on the boundary, so the comparison's strictness is academic -
but it matches the reference calculator, and two sources should not disagree on a case either could
hit.

## Bytes per hour

Channel occupancy is per *frame*, not per byte. A stream of 43-byte adverts buys far fewer payload
bytes per second than the same airtime spent on full frames, so any bytes-per-hour figure is only
meaningful beside the frame size that produced it.

## Advertising against blind repetition

The question the analytic model exists to answer: is reconciling cheaper than just sending things
more than once?

Costs per hour, with `λ` messages an hour, `k` copies each, `N` nodes in earshot, `f` adverts per
node per hour:

- **Repetition**: `λ·k·OBJECT`. One broadcast serves every listener, so `N` does not appear - which
  is exactly why blind repetition is hard to beat on a small mesh.
- **Reconciliation**: `λ·OBJECT + N·f·ADVERT + recovery`, counting the original transmission on both
  sides. Leaving it out of one side compares `k` copies against `k−1`, a whole copy of every
  message.

Solving for break-even, advertising is affordable while

```
f/λ  <  (k − 1 − recovery_fraction) · OBJECT / (N · ADVERT)
```

with `k−1` because one copy is the original either way, and the recovery fraction subtracted
because reconciliation still has to push whatever someone missed.

### Why earshot decides it

`recovery_fraction = 1 − (1 − miss_rate)^N`. A push is a broadcast, so what matters is whether
*anyone* in earshot missed the object, not how many did. That saturates: at 20 nodes and a 15% miss
rate almost every message needs a push, while at 2 nodes only a quarter do. Advertising cost has no
such ceiling - it grows with `N` - so earshot size decides the comparison, and 20 nodes is the
worst case for advertising rather than a neutral default.

Charging a per-node miss rate instead of the saturating one understated push cost by 6.4× at 20
nodes.

Push also has no requester to address, so duplicate suppression carries more weight than in the
pull case. That is the risk push trades the second round trip for.

### What the sketch buys

Repetition only ever reaches nodes that were listening at the time. Reconciliation recovers long
after the fact, at a cost that does not grow with the recovery window - which is the property that
earns the sketch its place, independent of the cost comparison above.

## Misdecode rate

An over-capacity sketch difference decodes to a wrong set that reproduces the same syndromes at
roughly `1/c!` for capacity `c`. `test_pinsketch` asserts this empirically at `c = 2`, where it
misdecodes on more than a fifth of over-capacity trials. Since the simulation uses the same `1/c!`
model, agreement at `c = 2` is by construction; what matters is that it decays fast enough that the
capacities actually in use are safe.

## Chains

A chain is per-server with local counters, exactly as in the set-reconciliation work - there is no
official counter anywhere. What a chain adds is a parent link per object, so order is recoverable
by walking, which is what makes catch-up serial.

## Adaptive sketch capacity

A full-capacity sketch on every advert is what makes the steady state expensive, and the steady
state is almost always `d = 0`. So a routine advert carries capacity 4 and the member count. When
two sketches do not resolve, the count difference is a lower bound on the divergence, so one
directed request buys a sketch sized to it. Capacity truncation is exact - the small sketch is a
prefix of the large one - so nothing already sent is wasted.

## What advertising costs against what it saves

SF++ already broadcasts `CANON_ANNOUNCE` on a cadence whether or not anything changed. An advert
carrying a sketch is roughly four times that size, so in a steady state where nothing is ever
missed this design is strictly worse. It pays for itself the moment a node has to catch up; the
break-even is how often that has to happen.

Against "just send it again" on the same axes: if `d` objects are missed per hour at a
per-transmission miss rate `q`, the underlying message rate is `d/q`, so the extra copies cost
`(k−1)·(d/q)·object`. Only the extra copies count, since the first transmission happens under every
strategy. That comparison flatters repetition, and the charts say so: `k` copies leave `q^k` of
messages unrecovered for good, where every other curve converges. It is a cheaper mechanism for a
weaker guarantee.

Fifty per cent channel utilisation is roughly thirty times the top of these curves, so it only
appears on a log axis. That is the point: none of these strategies saturates the channel, and the
differences between them are ratios rather than absolute bytes.

## Enumeration against sketching

Enumeration scales with what a node holds; a sketch scales with what two nodes differ by. At the
frozen bucket size of 32 the two are nearly tied, which makes bucket size the parameter that
decides whether the sketch is worth having at all.

## Ground

### The indexed grid

`IndexedTerrainGrid` gives the vendored `TerrainGrid`'s answers without its per-call sort. The
vendored grid sorts all N samples by distance on every lookup and keeps the nearest eight for an
inverse-square weighting. The index buckets samples on a cell of the grid's own spacing and widens
a ring until no unexamined bucket could hold a closer sample than the eighth it already has - so
the candidate set is a superset of the vendored nearest eight, and the same weighting is applied to
the same eight points. Ties break on sample order, as a stable sort does.

The bucket side is the grid's own spacing where it has one, and the bounding box cut into roughly
√N cells per axis where it does not, so a bucket holds O(1) samples and the ring terminates
quickly. The ring stops against the occupied extent, not against a count of occupied buckets:
buckets are sparse, and a square can cover many empty cells while every sample sits outside it.

Below `SCAN_BELOW` samples the index is *slower* than the scan it replaces. The packaged Batumi
grid is 42 points about 4 km apart, so the ring widens two or three times - re-sorting candidates
each pass - where `heapq` over all 42 answers in one. Profiling a 92-node Batumi build put 1.48 s
of 5.19 s in the ring search alone (TRAPS 7). The index earns its keep on an SRTM tile, not on a
preset.

Profile lookups round to a decimetre before caching: every pair sharing an endpoint walks the same
coordinates, the knife-edge loop asks for 24 per link, and a decimetre is below anything the model
can see.

### Landforms

`relief_m` is peak-to-trough elevation range and `ridges` the number of ridge lines across the
area, with `roughness` adding a shorter wavelength so a valley floor is not perfectly flat. None of
these are measured. They exist to make the shape of the ground a variable rather than the constant
zero. `synthetic_terrain_rows` lays down two sinusoidal ridge systems at an angle plus a hashed
lattice perturbation, so the field has both a long wavelength a link can be blocked by and a short
one that moves a margin; `coastal` replaces one system with a monotone rise, which is what a
shoreline is.

### Scenarios

A `Scenario` is where the nodes are and what is under them. Points are local metres from the
origin, matching the vendored projection exactly, so node *i* here and node *i* under
`loraMesh.py --preset batumi` are the same node in the same spot. `antenna_height` stays height
above local ground and never becomes altitude - the path-loss models take an antenna-height term,
and metres above sea level would silently make every node a mountaintop.

A scenario is always truthy. `__len__` counts nodes, and a landform is ground under a *generated*
mesh - terrain rows and no points - so `if scenario:` would read false and silently drop the
ground. That is TRAPS 1.

`apply()` sets terrain, clutter and calibration separately, because each is a separate claim:
terrain is geometry anyone can check, clutter is a land-cover raster, and the calibration is a
ridge fit over 296 observed links in one city. A run that keeps the first and drops the third is
asking what the ground alone does.

The noise floor and the near-field distance floor arrive with the scenario whatever the calibration
flag says, because they are measurements of the *place*, not of the link model. The per-preset
thermal floor is the better answer for a generated mesh and the wrong one for a mesh whose observed
SNRs were fitted against a measured floor. An explicit `--noise-model` still wins, being applied
afterwards.

### The fit's envelope

`preset_scenario` records how far the fit was actually trained from the observations themselves. A
ridge fit extrapolates without complaint, and this one's ground-elevation terms are large, positive
and unbounded - +4.24 dB per 100 m of the lower endpoint against a distance penalty of only
−4.68·log₁₀(km). Past the observed range two high nodes gain more from elevation than distance
takes away and the model invents a link (TRAPS 4).

### Mirroring

`mirror()` reflects a scenario into tiles rather than translating it, and the difference is the
whole point. `IndexedTerrainGrid` interpolates rather than refusing, so a translated copy lands on
ground the grid never surveyed and gets a featureless plateau - the packaged Batumi grid returns
the same 460 m at any distance outside its box. A reflected copy sits on terrain samples as real as
the original's, because they *are* the original's, and every seam meets its own mirror image so the
ground stays continuous across it.

It scales a place, not a mesh: the result is a plausible larger version of somewhere with this
terrain, not a claim about anywhere. On a fitted scenario, pairs spanning a seam are outside the
distance range the coefficients were fitted over.

A reflection also fixes the tile boundary, so adjacent tiles would each contribute the same column.
Duplicates break `ClutterGrid.is_regular`, and an irregular grid scans every sample on every lookup
- minutes per build rather than seconds (TRAPS 8). Dropping the repeated column loses nothing.

## Offered load

### The congestion throttle

The firmware scales every periodic broadcast interval by `congestionScalingCoefficient`
(`Default.h`), starting at `numOnlineNodes > 40`. `CONGESTION_PIVOT` exposes that 40 as a knob
rather than a constant, because "should the throttle start sooner or later" is deployment advice
and answering it needs the pivot moved, not described.

Three models, one per firmware era; a mesh takes the one its own default profile carries, so a 2.5
mesh gets the per-preset table and its small-mesh speedup rather than 2.8's SF/BW curve.

Device-originated broadcasts stretch with mesh size. User-typed text does not - nothing in the
firmware throttles a person deciding to send a message.

**When the coefficient is computed.** `adaptive` recomputes it per node from that node's own online
count at the moment it would send, which is what `Default::getConfiguredOrDefaultMsScaled` does on
every interval. `static` computes one mesh-wide coefficient up front, which is what earlier runs
were measured under.

**What feeds it** - `--congestion-input`, the arm round four exists to price:

- `hotstore` is what the firmware does. `getNumOnlineMeshNodes()` walks the hot store, so the input
  is bounded twice - by `MAX_NUM_NODES` and by the two-hour `NUM_ONLINE_SECS` window - and
  saturates on a mesh larger than the store, which is exactly where the throttle is most needed.
  The node counts itself, as the firmware does by iterating a table containing its own record.
- `truesize` is the unbounded ideal: the mesh as it really is, which no device can see. The upper
  bound on what a corrected input could buy.
- `utilisation` drops the node count and scales on measured channel busy-ness, which is what the
  throttle actually cares about and the one input memory cannot bound. No firmware has this mode.
  Busy share maps onto the same 40-node pivot so the three are comparable: 40% busy reads as the 40
  nodes at which throttling begins. That mapping is a stated assumption, not a reconstruction.

**The three coefficient models**, where `pivot` is the node count below which nothing throttles:

- `flat` (2.4): 1.0 up to the pivot, then 0.075 per extra node whatever the preset.
- `preset` (2.5, 2.6): a per-preset factor, no throttle at all on SHORT_FAST or SHORT_TURBO, and a
  coefficient *below* 1.0 up to 30 nodes - a small mesh is deliberately made chattier.
- `sf_bw` (2.7, 2.8): `2^SF / (BW_kHz · divisor)`, which on LONG_FAST is 0.08192 per node, so a
  150-node mesh stretches its intervals tenfold. The divisor is 100, or 25 in event mode.

`observed_senders` reports distinct senders heard recently - what the mesh can see of its own size,
bounded by packet history rather than by `MAX_NUM_NODES`, so it keeps rising after the hot-store
count has saturated. It sits beside the coefficient in the output so saturation is visible rather
than inferred. The sender comes from the `PacketHistory` record; counting packet ids would count
packets, since every packet carries its own.

### Emission

A Poisson process per class per node - exponential gaps rather than a fixed period, because
synchronised senders understate collisions and every node in a real mesh has its own phase.

Time-of-day weighting uses thinning: generate at the peak rate and keep each candidate with
probability `weight(t)/peak`. Simpler than integrating the rate curve, and it produces the right
arrival process rather than a rescaled uniform one.

Under `adaptive` the coefficient is unknown until the moment of sending, so candidates are laid
down at the most permissive rate the model allows and thinned at emit time against each node's own
view - a candidate survives with probability `floor/coefficient`. The floor is taken across every
profile present, not just node zero's: on a mixed mesh a node whose model is more permissive than
the sampled floor can never be thinned, while its candidates were generated at the stricter rate,
so it silently sends less than its own model calls for. That is the `--legacy-fraction` arm.

A class with no rate draws **nothing**, not even its emitter set. `rng.sample()` would advance the
shared stream and shift every schedule after it, so a run asking for no DMs would stop matching the
same run made before DMs existed.

### Direct messages

The DM pool is every node that is not router-like. A router is infrastructure on a mast: people do
not chat from it and nobody DMs it, and field traffic addressed to one is an admin session, modelled
separately. `CLIENT_MUTE` is in the pool at both ends - a muted node does not rebroadcast, which is
not the same as not having a user.

Peers are drawn fresh each time rather than as persistent pairings, which would make the result
depend on which pairs the draw happened to place near each other. Uniform keeps the airtime honest
without claiming to model who talks to whom.

The draw is restricted to peers whose keys the node holds, because the firmware's DM UI lists
exactly those: a target it cannot encrypt to is one the user could not have picked. Drawing from
the whole mesh instead made the measurement mostly about key availability - 91% of attempts failed
that way on a 2-hour Batumi run - rather than about delivery.

DM outcomes are resolved against whether the target ever saw the message, so success is measured at
the intended recipient rather than inferred from the flood.

## The digest

`collate.py` turns a night's run JSONs into one report. What it counts and how it ranks is
deliberate.

**Missing metrics become `None`, not errors.** A run assembled from mixed vintages - an older
transport, a section that only exists under some flags - still collates.

**Ranking.** A block is ranked by whichever of `text`, `dm`, `admin` and `held` moves furthest, and
the table names which one it was. Ranking everything on `held` would rate an arm that halves DM
success as having done nothing. A measure needs `MIN_OBSERVATIONS` before it may decide the ranking:
one admin probe an hour over two hours is two sessions, where a single failure reads as a 50% swing
and tops a leaderboard built from real effects. Below the floor it is still reported, it just cannot
rank.

A spread of zero is not a movement. Without that guard a block whose cells are identical in every
delivery measure still reported `moved: text, spread 0.000`, which reads as a finding and is the
opposite of one.

**Cost is a ratio, not a difference.** Several blocks - reconciliation strategy, signing, advert
transport - deliberately hold delivery flat and differ only in what they spend. `D-resolve` is the
clear case: enum advertises with a fifth of sketch's advert bytes then pays two thirds more in
total traffic, while `held` moves by 0.004. These span orders of magnitude, so "5.7×" is the
readable figure where "11877 bytes" is not.

**Deltas are differences, not ratios.** Reach figures are shares: "+0.041 reach" is the sentence a
reader wants, and a ratio of two reception fractions is not. The control keeps a row of its own
reading zero, so the table shows what it was rather than only what was subtracted.

**Controls.** `design.py` puts a control in every cell - the archive `off` arm, the mesh as the
firmware runs it - so each later arm is a difference on the same mesh at the same seed. A block
sweep has no such cell and its arms are read against each other.

**Inert detection.** Cells differing by less than `INERT_EPSILON` on *every* recorded number are
the same cell. Relative, because the numbers span reception fractions and byte counters in the
millions. Two mistakes are recorded here: comparing only the displayed metrics called `E-signed`
inert when it moves `advert_bytes` by 43% (hence: every number, not a chosen few), and leaving
`value` out of `NOT_A_MEASUREMENT`, which disabled the check for 40 of the 87 blocks (TRAPS 11).

**Weighted rates.** `admin_success_rate` weights by sessions attempted, because averaging the rates
would weight a distance with two sessions the same as one with fifty.

**Derived figures.** `nodes` comes from the built mesh, not from `--nodes`: a fixed-geometry
scenario decides its own count, and Batumi is 92 whatever was requested (TRAPS 9).

**Grouping.** Cells group on the arm's value; a block does not have to arrive in one file, since a
heavy cross cell is sharded one job per seed and each shard uploads under its own name. Reading one
block per file would average nothing over seeds and enter the same block three times.

**Timing.** Runtime is compared as seconds per simulated hour against the block's own history, never
as raw `wall_seconds` - the total moves whenever the seed count or `--hours` moves. Both directions
warn: slower is TRAPS 7, and faster is the subtler one, since a fragmented mesh, an unread arm or
traffic that stopped generating all make a run cheaper by doing less work. History comes from prior
digests rather than raw block JSONs, because the archive prunes the raw data and keeps the digests.

**Flags carry a kind.** The run-health page groups and counts them, and recognising a flag by
re-reading its prose would break the first time one was reworded. A run with 400 `beyond-envelope`
warnings from one mirrored cell and one `inert` is not the same run as the reverse, and a flat list
of 401 sentences reads identically either way.

## The campaign

### The replay header

One field outside the encryption wrapper: `heard_ago`, in 64-second ticks, two bytes. A node that
merely overhears a replay can then file it where it belongs in its own history rather than showing
it as having arrived now.

No separate "replayed" flag is needed, because the field's *presence* is the flag: fresh traffic
carries no `heard_ago` and a replay does. In protobuf terms that is an optional field, so absence
costs nothing and cannot be confused with zero-seconds-ago.

64-second ticks because fine resolution is worthless here - the measured spread between two
archives' accounts of the same message is single-digit seconds - and a full 16 bits of ticks buys 48
days, comfortably past any retention window.

### Admin sessions

`AdminModule.h:109`, `kOutstandingAdminRequestMs = 300 s`, "the same window as the session
passkey". The whole round trip has to land inside it or the firmware stops accepting the response:
the request's slot has expired and the reply is no longer vouched for by anything.

The retry count is an assumption about the operator, not a firmware constant - the firmware has no
retry loop here at all - so it is stated as one and adjustable with `--admin-attempts`. Three is what
a person does when a change does not take: presses it again, twice, then stops.

The key half of the model is not an assumption. Admin authorisation lives in
`config.security.admin_key[3]`, separate from NodeDB and immune to its eviction, so a session's
outcome is decided by timing rather than by key availability.

### Short IDs

PinSketch here is GF(2^32) because it is a transcription of the firmware's, so the arithmetic cannot
be re-fielded without breaking the oracle. A narrower short ID is modelled by masking the ID to `b`
bits before it enters the sketch, which reproduces exactly what `b` controls - the collision rate -
while airtime is charged at the real `c × b/8`. Widths above 32 are charged their real airtime and
modelled as collision-free, which they effectively are.

### Where an archive goes

`beside-router` is a plain client one hop from each router: it hears most of what the router hears
without competing with it for the channel.

`random-any` is the odd one out and deliberately so. Every other strategy answers "where should an
operator put one" and every one is bounded by something - `routers` and `beside-router` cannot
exceed the mesh's router count, four on Batumi, so asking either for six gets four and no complaint.
`random-any` is bounded only by the node count, which makes it the strategy for asking how the
archive *scales* rather than where it goes, and the honest control for any claim that a deliberate
arrangement beat chance.

### Buckets and windows

Bucket membership is per server. The firmware assigns a chain counter as `chain_end.counter + 1`
when it ingests a message that arrived without an official one
(`StoreForwardPlusPlus.cpp:1366`), so two servers hearing the same broadcast off the air number it
differently. `SketchIndex.h` describes a count boundary as one both sides derive from the data
itself; it is derived from local arrival order instead, which is what the bucket-mode arm measures.

A sliding window needs no agreement at all. Two servers' windows overlap because they heard mostly
the same recent traffic, not because they negotiated a boundary - the XOR of two sketches is the
symmetric difference of whatever sets they were built over.

Membership is checked against the whole store rather than the window, which is load-bearing in
window mode: a short ID in the decoded difference may be something the peer holds and has simply
aged out, and checking the window would request it back.

A server keeps two records for provenance: `(rx_time_ms, bucket)` for objects heard directly, so a
replay carrying `heard_ago` can be binary-searched into the bucket it would have been in; and
`message_hash -> (first_heard_ms, [claims])`, holding both the directly-heard copy and every
replay's claim, which is what makes drift measurable and would catch a peer lying about `heard_ago`.

### Mesh size against density

150 nodes in the same 8 × 8 km as 60 is two and a half times the density, so a size sweep holding
area fixed measures density and calls it size. Scaling the side by `sqrt(n/60)` keeps nodes per
square kilometre constant and lets the two be separated.

Every field that draws randomness is seeded off the run's seed through its own constant, so it is
reproducible without being correlated with anything else the seed decides - and `NoiseField` draws
no randomness at all, so switching a profile on leaves every other draw exactly where it was.

### Setting a run up

The ground is resolved before the mesh is built, because it decides the config the link budget is
computed against and, for a real snapshot, the geometry and node count too. It is applied outside
`build()` so an explicit `--noise-model` still beats the floor a calibrated scenario carries.

A `--nodes` that disagrees with a fixed-geometry scenario is a mistake, not a preference, and
`opts.nodes` is overwritten rather than ignored: every per-node structure is sized from it, and the
report records `opts` as the description of the run, so leaving 60 there while 92 nodes transmit
would be a lie in the one place a reader checks.

Who has a user is assigned at random rather than by degree - whether a node has an owner typing on
it is a fact about the owner, not about how well sited it is, and choosing the worst-connected nodes
would make an unattended mesh look cheaper than it is.

### The paired baseline

`none` is a cell of the protocol arm rather than a separate run: same seed, same topology, same
traffic schedule, no archive. That turns every other cell into a *difference* instead of a
comparison.

The same nodes are designated whatever the protocol, including under `none`, where they run no
archive and behave as ordinary nodes. That separates two things this campaign had been conflating:
what being a server *costs* a node in its own reception - a server transmits more, so contention and
half duplex charge it - and what reconciliation then *adds* on top. Without it, "held 0.966" cannot
be split into "heard anyway" and "recovered".

Observers are intermediate nodes wired for telemetry only. They run no archive and change no
behaviour; they record what an ordinary node in the middle of the mesh ends up with, split by how it
got there. Without them the bystander benefit of a broadcast replay is invisible.

Placement draws from `random.Random(seed ^ 0x504C4143)` rather than the run's stream. Taking those
samples from the shared RNG shifted every later draw, so a randomised placement produced a different
traffic schedule from a deliberate one - an 8% reach difference between the control and the one arm
that exists to *be* the control (TRAPS 12).

`--servers` below 1 is read as a share of the mesh rather than a count, so a scaling sweep can hold
archive density fixed while the node count moves. Zero servers is legitimate and means `--baseline`.

What was asked for and what the mesh could offer are both recorded: a role-bounded strategy
returning a shorter list silently is how "6 servers" and "4 servers" become the same row (TRAPS 6).

### Counting a reception

A DM counts as received only at the node it was addressed to. Every other node that heard it relayed
it, and counting the flood reaching a bystander as delivery is how an addressed protocol gets
credited with a broadcast's reach.

Every class is counted, not just the archived one: position, telemetry and nodeinfo are generated,
flooded and charged airtime, so any airtime share quoted against them needs their receptions
measured too.

Time bins are keyed by *reception* time rather than origination. Over a bin far wider than the
latency - an hour against seconds - the two agree except for packets straddling a boundary, and
tracking an origin time per packet would mean a slot on `Packet` and a live dict of every id in the
run. The first and last bins are the ones to distrust, which is why the denominator is recorded per
bin rather than assumed flat. `--reception-bin-s 0` is off and leaves a run byte-identical to one
made before the series existed.

A 72-hour run reported as one mean is still a single number. The sweeps run three diurnal cycles
because the cycle is visible, and it is only visible if something samples inside it.

Hop histograms are summed rather than kept per sample - a per-bin array per node is O(nodes × bins)
and only ever read as a mean, so O(nodes) does. `hops_away` is kept as a histogram rather than a
mean because the interesting nodes are the ones whose traffic all arrives at 4+ hops, and it mirrors
`NodeInfoLite.hops_away` rather than being an invented metric.

A replayed object is useful to whoever hears it, not only to whoever asked: a server files it in its
store and any other node records it for its own history, so both paths run.
