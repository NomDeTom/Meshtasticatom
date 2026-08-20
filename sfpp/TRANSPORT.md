# The transport

What `sfpp/mesh.py` models and where each rule comes from. [README.md](README.md) is the operating
manual, [MODEL.md](MODEL.md) the arithmetic, [TRAPS.md](TRAPS.md) the defects; this is the firmware
behaviour the simulation reproduces.

Everything here is read off the firmware in this tree unless a release is named. `VERSIONS` runs
2.4 to 2.8, each profile carrying the rules of that series' **final** release - 2.4 = v2.4.3,
2.5 = v2.5.23, 2.6 = v2.6.13, 2.7 = v2.7.21, 2.8 = this tree - so a mechanism that arrived
mid-series is present in that series' profile. `FEATURE_TAG` records the release each one shipped
in.

`legacy` is **not a firmware version**. It is the rule set this transport carried before the 2.8
fold-in, kept so earlier runs still reproduce. Four of its deviations were never any firmware's
behaviour - no router offset, a continuous slot draw, a clamped contention window, a 400-backoff
discard - so it must not be read as "2.7 and earlier". It reproduces distributions rather than
streams: the TX queue replaced a recursive retry closure, so a seed does not reproduce a
pre-fold-in run packet for packet.

## Roles

- **ROUTER** rebroadcasts early, drawing from the bottom of the contention window while everyone
  else waits behind a fixed router offset.
- **ROUTER_LATE** is the mirror image: it relays like a router but is pushed to the back of the
  window the moment it hears someone else do the job.
- **CLIENT_BASE** behaves as a router for traffic to or from its favourites and as a client for
  everything else.
- **CLIENT_MUTE** never rebroadcasts at all.

Who skips the router offset - `RadioInterface::shouldRebroadcastEarlyLikeRouter` and the inline
role test that preceded it - moved across releases: ROUTER and REPEATER up to 2.6, plus CLIENT_BASE
on favourite traffic in 2.7, and ROUTER alone in 2.8 once REPEATER and CLIENT_BASE were taken back
out.

Role shares come from a real census of 1769 nodes. TRACKER, CLIENT_HIDDEN, TAK and SENSOR together
are about 1% and fold into CLIENT: none of them changes a rebroadcast decision, which is all a role
is read for here. The `no-mute` mix is adversarial rather than a census - CLIENT_MUTE is what keeps
a real mesh quiet, a fifth of Baymesh does not rebroadcast at all, so removing it is the cruellest
realistic change to a role mix.

## Contention

The contention window is sized from SNR so that distant nodes - the ones whose rebroadcast actually
extends coverage - transmit first (`RadioInterface.h`). Both bounds moved: 2.5 lowered CWmax to 7,
2.6 raised CWmin to 3 and put CWmax back, and 2.6 also narrowed the top of the SNR range from 15 dB
to 10, which shifts every rebroadcast delay on a strong link.

Slot draws are integer and half-open, matching Arduino `random(0, n)`. Under `legacy` the draw stays
continuous, which removes a class of collision the firmware produces routinely: two nodes can only
pick the same slot if slots are discrete.

## The queue

`MeshPacketQueue::CompareMeshPacketFunc`. 2.4 orders a max-heap by priority alone, ties to the
lower id. 2.5 replaced it with a sorted insert that puts the late-transmit group last and, at equal
priority, prefers a packet already on the mesh over one of ours.

The queue is finite and overflow is its only drop: `setTransmitDelay` reschedules a blocked packet
indefinitely, so congestion appears as a full queue and as latency rather than as a packet that
evaporates. On overflow the firmware chooses what to lose - `replaceLowerPriorityPacket`.

## Routing

`TraceRouteModule::updateNextHops` (v2.7.13): a traceroute reply teaches a next hop for every node
beyond the learner in the route, not just the neighbour. The corroboration guard - refusing to learn
unless the byte the route names is the one that actually relayed the reply - is only in this tree.
2.7 learns from the unauthenticated payload unconditionally, so it learns more, and some of what it
learns is wrong.

## The node database

`MAX_NUM_NODES` is the hot store. Up to 2.5 the cap was a flat 100 for every board; 2.6 introduced
the platform split with nRF52 at 80 and the ESP32-S3 flash tiers; this tree raised the compile-time
default to 120 and dropped the separate nRF52 branch. The `nrf52840` key stands for "nRF52840 and
generic ESP32", which 2.6 and 2.7 do not treat alike.

Board sizes are derived from this tree's own variants: each `platformio.ini` declares
`custom_meshtastic_hw_model_slug`, `custom_meshtastic_architecture` and
`custom_meshtastic_partition_scheme`, and `mesh-pb-constants.h` turns those into `MAX_NUM_NODES`.
Regenerate after a firmware bump. HELTEC_V3 is an 8 MB ESP32-S3 and so gets 200 slots, not the 120
of the compile-time default.

No declared hardware model maps to the 10-slot STM32WL tier - the stm32 variants here do not declare
a slug, so they cannot be named in a census by one. The `constrained` mix reaches that tier
directly, as a stress test rather than a deployment.

`WARM_NODE_COUNT` keys on memory class rather than flash, so the flash-derived platform names here
do not line up exactly: STM32WL is `MEM_CLASS_TINY` and has no warm tier at all, nRF52840 is a named
case at 100, and a non-PSRAM ESP32-S3 takes the 150 of `MEM_CLASS_MEDIUM`. The 16 MB tier is taken
as the PSRAM-equipped S3 that `MEM_CLASS_LARGE` describes - an assumption about the boards in that
tier rather than something flash size determines, and `warm_num_nodes` overrides it.

`TRAFFIC_MANAGEMENT_CACHE_SIZE` is the cold tier. A key seen on the wire is cached there and can
answer the inbound-decrypt path, but it is never authoritative: nothing routes, resolves or
attributes identity from it.

## Signing

An XEdDSA signature is 64 bytes and the protobuf field carrying it costs two more
(`CryptoEngine.h`, `RadioInterface.h`). A frame is 255 bytes with a 16-byte header, so a Data
payload signs only while it stays under 173 bytes - the gate `signedDataFits()` applies with the
real encoder.

## Repeat scaling

From the `extra-repeats` branch's `RepeatScalingModule`. Cancelling a queued rebroadcast on the
first heard copy costs delivery on the one class with no ACK behind it, so text tolerates a second
copy first. The suppression thresholds are the module's own, and none of the three is validated.

## The overlap window

`MAX_AIRTIME_MS` bounds how far back the interferer scan looks. It was once a flat 20 s, justified
by a claim that a full LONG_SLOW payload was "about 6 s". It is 14.3 s, and 6 s is roughly what a
45-byte payload costs. Even 20 s sat under VERY_LONG_SLOW's 28.6 s, and a transmission still in
flight past the window was dropped from the scan entirely: measured over 8 h at 30 nodes,
VERY_LONG_SLOW put 130 of 5669 transmissions past it - the longest ones, and so the likeliest to
overlap something.

## Arduino arithmetic

`arduino_map()` reproduces Arduino's `map()`, and two details decide the answer where Python's
defaults would not. The parameters are `long`, so a float SNR or utilisation truncates toward zero
on the way in - −5.7 dB enters as −5. C integer division also truncates toward zero where Python's
`//` floors, and the two disagree for every negative numerator: `getCWsize(-25)` is 0 in the
firmware and −1 under `//`.

`getCWsize()` takes the result as a `uint8_t` without constraining it, so an SNR outside
[SNR_MIN, SNR_MAX] extrapolates off the end of the window rather than saturating at it.

## Packet fields

`relay_index` is **not on the wire**. `relay_node` is one ambiguous byte; the index is the sending
node's, kept for instrumentation so a cancellation can be attributed. Nothing in the transport
reads it and no decision may - resolving a relay to a node is exactly the ambiguity
`resolve_unique_last_byte` exists to model.

`RouteDiscovery` carries two arrays, not one: `route` accumulates outbound and `route_back` on the
way home (mesh.proto tags 1 and 3, `TraceRouteModule.cpp:377`). Conflating them meant that on an
asymmetric mesh - which this transport models - a reply that did not retrace its request had its
return-leg relays learned as forward hops.

`highest_hop_limit` on a `SeenRecord` is what the upgrade path turns on: hearing the same packet
again with more hops left than the copy already queued means an earlier relay took a shorter route,
and 2.8 throws away the queued copy for the better one.

Everything routing can do is bounded by a `NodeRecord` existing. A peer evicted from the hot store
cannot be resolved from a relay byte, cannot hold a next hop, and does not count as online.

A `QueueEntry`'s `tx_after` is an absolute deadline, not a delay: `MeshPacketQueue` sorts every
deferred packet behind every ready one, and the late-rebroadcast window is nothing more than
setting it.

## Ambiguity and route health

`NodeDB::resolveUniqueLastByte`. Before this tree a last-byte lookup took the first node it matched
and nothing asked whether a second shared the byte, so hop preservation and next-hop emission were
ambiguity-blind and got it wrong silently on a dense mesh.

`RouteHealth` is RAM-only in the firmware too: the route lives in `NodeDB`, and this is the metadata
that lets `getNextHop()` decay a dead hop back to flooding rather than spend a DM discovering it.

## Hop scaling

`HopScalingModule` is a sampled, capped, hash-collided estimate of how far the mesh reaches, and it
emits a hop-limit recommendation from it. Every property costs accuracy against an exhaustive count,
and each is why modelling it is worth anything:

- identity is a 16-bit hash, so two nodes can share an entry
- 128 entries of 4 bytes each, and it fills
- only one node in `sampling_denominator` is admitted, chosen by hash
- buckets are scaled by `filtering_denominator` before the recommendation walk
- recency is a 13-bit hourly bitmap, not a count
- on overflow it raises the denominator and drops nodes, warning that the answer may be skewed

So the module's per-hop counts are an estimate and the transport can compute the truth; reporting
both is what says how far apart they are.

The recommendation is the first hop that reaches `target_affected_nodes` after scaling - 40 in the
firmware - plus one more hop when the nodes it would add still leave the total inside a budget
running from that target to `max_target_nodes`, scaled by how politely the mesh is behaving. Both
figures are literals in the module and instance attributes here, so a run can ask what the mesh
would do if the firmware aimed at more or fewer nodes. The ceiling follows the target unless set
outright, keeping the firmware's 40:80 ratio.

A node lowering its own hop limit on routine broadcasts is the module's whole purpose, and
unconditional in the firmware wherever the module exists. It is separable here only so a sweep can
hold the feedback loop open.

## The warm tier

A `WarmNodeEntry` is 40 bytes: node number, `last_heard`, and a Curve25519 public key. The role, a
protected category and an XEdDSA-signed flag are packed into the low seven bits of `last_heard`,
which is why warm recency is quantised to 128 seconds. That coarseness is load-bearing: the tier is
LRU-ordered by that field, so two nodes heard inside one 128-second window are indistinguishable to
eviction.

`TrafficManagementModule`'s overflow cache of next-hop hints is much larger than the hot store and
not bounded by it, so it can hold a route for a node the NodeDB has evicted or never admitted.

`RepeatScalingModule` keeps a ring of eight `(sender, id)` duplicate counts, replaced round-robin -
small enough to thrash on a busy mesh, which is why its size is modelled rather than a dict.

## Sensing

`sense_until` is the end of the last stretch this radio sensed the channel occupied, separate from
`busy_until`, which is only our own transmission. It is what the energy detector saw, ours and
everyone else's, and it exists so overlapping signals are charged once (TRAPS 5).

## Identity on the wire

`NodeDB::getLastByteOfNodeNum` puts all of a node number that fits in `relay_node`. A low byte of
zero is sent as 0xFF, because 0 is the `NO_RELAY_NODE` sentinel - so one node number in 256 is not
identified by its own last byte, and 0xFF answers for twice as many nodes as any other value.

## The three tiers

**Hot.** `NodeDB::updateFrom` notes that a peer was heard and how far away it is. `hops_away` stays
`None` until a packet arrives with a usable hop count, matching `has_hops_away`: "never established"
is a different answer from "zero hops", and next-hop resolution turns on the difference.

`demoteOldestHotNodesToWarm` demotes the stalest unprotected record on overflow - protection
outranks recency, and within a class the most-recently-heard survives. This is how a learned route
dies without any expiry being involved.

**Warm.** `WarmNodeStore::absorb` keeps an evicted node's identity, key and role in 40 bytes. The
key is what the tier exists for - expensive to re-learn where the rest rebuilds from traffic in
seconds - so a keyless candidate never displaces a keyed entry, and eviction takes the oldest
keyless entry first. Routing does not survive demotion: `next_hop` and `hops_away` are hot-store
fields, so a re-admitted node is flooded to until its route is learned again. A node lives in hot or
warm, never both.

**Cold.** A cache for the inbound-decrypt path, never authoritative. It can answer "do we hold a
key for this node" and cannot be used to claim a node's identity.

`copyPublicKey` reads hot then warm, both authoritative. A node's own record is in the hot store
with its own key, so it can always verify a signature of its own - which is what it hears when its
relay comes back.

`NodeDB::getNumOnlineMeshNodes` is bounded by the store *and* by a two-hour window. The transport
does not read it; the congestion coefficient does, which is what makes that coefficient bounded by
the store rather than by mesh size.

## Position

`position3` is absolute altitude, not height above ground. Without terrain the ground is zero, so
it is the flat position plus an antenna height, and 1.5 m over a kilometre is nothing a path-loss
model can see. With terrain it is the number that matters: two nodes 3 km apart with 400 m of ridge
between them are further apart than the map says.

`direct_neighbours` stands in for `HopScalingModule::getLastPerHopCounts().perHop[0]` - the exact
figure that sampled, capped estimator is trying to approximate.

## Channel busy time

A receiver has one energy detector and one channel. Two overlapping signals are one busy stretch to
it, not two: it cannot count transmitters, and when a packet fails it learns only that an Rx
failed - not why, and not how many were talking. Charging each overlapping transmission its full
airtime attributes knowledge no radio has and lets the figure exceed 100% of wall-clock, which a
channel cannot do (TRAPS 5).

So only the part of a stretch not already covered is charged, and the ring accumulates the union.
Callers charge at a transmission's *end*, which is the order deliveries fire in, so a running
high-water mark is exactly the union rather than an approximation.

`AirTime`'s second ring is our own transmissions only, per minute over the last hour - a different
structure over a different window from channel utilisation, and the one the duty cycle is enforced
against.

## Placement

`place_nodes` is Poisson-disc-ish: uniform, rejecting anything too close to an existing node, so
stacked nodes cannot make the mesh look better connected than a real deployment.

- **clustered** - towns with a thin scatter between them, which is what most regional meshes look
  like: dense pockets joined by a handful of long links. Nine in ten nodes belong to a town; the
  rest hold the mesh together.
- **hub** - a dense core with radial arms. The core hears everything and the spoke ends hear almost
  nothing, so archives placed among the well-connected nodes are maximally redundant with each
  other.
- **chain** - towns strung out in a line: a valley, a rail line, a coast road. The point is a mesh
  that is *long and connected*. Stretching a uniform field far enough to exceed seven hops
  eventually fragments it - at 20 km with 60 nodes a fifth are isolated, and the measured diameter
  becomes a surviving fragment's - where a chain stretches without breaking, because consecutive
  towns sit inside each other's range.
- **mixed** draws the generator from the same seed, so a sweep samples across mesh shapes rather
  than across draws of one shape, and a placement rule that only holds on uniform points shows up
  as an artefact of the generator.

`stretch_points` scales every distance about the mesh's centroid. A stretch is not a bigger area:
`--area` redraws the placement, so an 8 km and a 16 km mesh at one seed are two different meshes.
Scaling points already drawn keeps node *k* the same node with the same neighbours in the same
arrangement and changes only how far apart they are. About the centroid rather than the origin so
the mesh grows in place, and it consumes no randomness, so a stretch sweep is paired.

## Noise

`NoiseField` is hashed, not drawn, for two reasons learned from `--amplify-worst`: it consumes no
randomness, so switching a profile on does not shift the stream the traffic generator shares; and
it is order-independent, where a stateful AR(1) would hand out a different field depending on what
the traffic happened to do, and a run would not reproduce.

**Temporal** is a smooth field with a coherence time, sampled across the packet's own airtime and
judged on the **worst** excursion it spans - a frame is decoded as one unit, so a single deep fade
anywhere inside it corrupts enough coded symbols to fail it. A 14.3 s LONG_SLOW packet at τ=500 ms
spans twenty-eight independent excursions and is judged on the deepest; a 100 ms SHORT_TURBO packet
spans less than one. The length penalty that falls out is superlinear, which the vendored curve's
flat 0.8 dB per 100 bytes is not.

**Transient** is episodic and spatial: a window of raised floor over part of the map, standing in
for an interferer switching on, a neighbour's non-LoRa gear, weather. Nothing extra is needed to
make it bite the stretched links first - a fixed dB excursion removes the least margin first, so the
marginal population is exactly who pays. Transient excursions are one-directional: the floor rises,
and a quieter-than-nominal band is left to the temporal field, which can fall below zero on its own.

**Periodic** is not a probability or an SNR penalty but a hard loss: a switching supply, a radar
sweep, a pager transmitter. It does not degrade a link, it removes whatever was in the air. The
length effect falls out of the geometry with no coefficient - the chance of being caught is
`(airtime + pulse) / interval`, so at a 10 s interval a 175 ms SHORT_TURBO frame is hit under 4% of
the time and an 11.7 s LONG_MODERATE frame cannot avoid it at all. That is a far harder length
penalty than the PER curve's, and the one that decides whether a preset is usable near an
interferer. It is mesh-wide, which is the simplification: one emitter every receiver hears, where a
real one has a location and a radius - which the transient profile already models, and the two
compose. Perfectly regular, with no jitter, because that is the adversarial case: a mesh cannot
average it away, and a packet length that resonates with the interval fails every time.

## Ducting

Tropospheric ducting is kept apart from `NoiseField` because it is the propagation path improving,
not the floor moving. Over water, under an inversion, on a still evening, signal that normally
disappears into the ground arrives 10 to 30 dB stronger than the path loss says, and operators watch
their node lists fill with names from a hundred kilometres away.

**It is not a gift.** A duct hands the mesh far more audible neighbours, so more transmissions
collide and contend; links that appear, get learned, get written into a NodeDB and a `next_hop`, and
then vanish when the duct closes, leaving routes pointing at nodes that cannot be heard; and an
apparent densification the congestion machinery reacts to, scaling intervals for a node count that
is not really there. So the interesting result from a ducting run is rarely the extra reach - it is
what the mesh does afterwards.

The lift is one figure for the whole mesh: a duct is a property of the atmosphere over the region,
not of a pair of nodes. A real duct has a geometry and favours paths along it, often over water;
the uniform lift is the conservative direction here, because it densifies everywhere at once.

## Siting and amplifiers

**Not from the firmware, and not measured.** The firmware has no concept of siting - it knows
`tx_power` and a GPS position, and `antenna_gain` appears nowhere in `src/` or the protobufs. Even
the vendored simulator's antenna gain is a single global `Config.GL`, not per node.

`SITINGS` is a gain offset in dB on every link a node takes part in, for the deployments people
describe having: a roof node clears local clutter and gets height, a desk node is indoors with a
window, a pocket node pays body loss and gets no height, a basement node is below grade. The spread
is larger than most parameters this simulator sweeps - roof to basement is 26 dB, more than the
whole span from SHORT_FAST to VERY_LONG_SLOW sensitivity - so these round numbers want replacing
with measurements rather than defending.

`AMPLIFIERS` is a (transmit, receive) pair on top of siting, shaped like the modules people fit: a
PA gives 8 to 15 dB out, and the receive path is at best unchanged and often slightly worse, since
the amplifier's insertion loss sits ahead of the LNA and few boards switch cleanly. The asymmetry is
the whole point: a node heard far further than it hears relays into places whose replies cannot
reach it, and its rebroadcast cancels copies queued by nodes that could have carried the packet
further. `cancelled_by_weaker_relay` is the counter that shows it.

## The noise floor

The vendored `NOISE_LEVEL` is one constant for every preset, and the sensitivity table beside it is
not: those figures are kTB + 6 dB NF, each landing exactly on its spreading factor's demodulator
limit (SF7 −7.5 dB, SF11 −17.5, SF12 −20.0). A fixed floor therefore misstates SNR by
10·log₁₀(bw/anchor) - about 5 dB optimistic at 250 kHz and 8 at 500 kHz.

That matters more than a few dB sounds, because the PER curve's p50 sits at −17.0 dB (CR5) to
−19.4 (CR8), right on those limits. Under the fixed floor a LONG_FAST link at sensitivity computes
SNR −12.25 and decodes 96% of the time; under a thermal floor it computes −17.5 and decodes 39%.
The fixed floor is why this model had no marginal link at all: it puts every link the graph will use
5 dB into the flat top of the curve.

`EXTRA_PRESETS` are not upstream and in no firmware build, and their sensitivity is **extrapolated**
rather than derived: the vendored figures fall about 2.5 dB per spreading factor across the 500 kHz
rows, and these continue that slope one step past each end. Treat them as indicative of a direction,
not as a link budget. SF5 and SF6 also need an SX126x or SX128x, so `EXTRA_SHORT_TURBO` is not a
setting every board could take even if the firmware offered it.

## Loss knobs

`extra_loss` is a flat loss floor on every reception, standing in for what the model does not carry
- interference from outside the mesh, fading, a receiver busy elsewhere.

`burst_loss` is bursty deafness: a node periodically unable to receive for a stretch, standing in
for a blocked antenna, a neighbour keying up nearby, or a radio busy elsewhere. The two are
different problems for a sketch: flat loss spreads divergence evenly across buckets, and a burst
puts a whole bucket's worth into one.

A noise excursion is attributed both ways off one draw - lost where the static floor would have
delivered, and delivered through a quieter-than-nominal band where the static floor would have
dropped - so neither attribution costs an extra random number.

## Links

Per-pair asymmetry is drawn **once** for the life of a mesh and kept. A rebuild - after an amplifier
is fitted, or to price a stretch - then draws nothing and moves nothing it was not asked to move.
Redrawing re-randomised every link, including every pair with no amplifier near it, and advanced the
RNG the traffic generator shares, so the before and after of any such comparison were two different
meshes carrying two different schedules.

Siting moves both directions together - a basement is a bad place to transmit from *and* to receive
in - so it is carried separately from amplification, which does not. Both must arrive with the
constructor, because links are computed once.

Terrain is a grid rather than a per-node height, because the link budget asks what is *between* two
nodes and a node's own elevation answers half of that. Lifting nodes onto it is a no-op without a
grid: the nodes keep their sea-level default, every obstruction term returns 0.0, and a flat run
computes exactly the budget it always did. With terrain there are two numbers - `ground_m` from the
grid, and `antenna_height_m` above it, never absolute altitude.

## The link budget

Three loss terms, three separate claims, kept apart so a result can price them apart: distance is
geometry, terrain is a public elevation model, clutter is a land-cover raster. Both obstruction
functions return 0.0 with their grid disabled, which is what makes a no-terrain run bit-identical to
every run made before the ground existed.

The path is measured between antennas, not between map pins. Without terrain every altitude is zero
and the 3-D distance is the 2-D one; with terrain, two nodes 3 km apart with 400 m of ridge between
them are further apart than the map says, and the obstruction terms price the ridge itself.

`rssi[i][j]` is *i* transmitting and *j* receiving, so it takes i's transmit gain and j's receive
gain - separate numbers per node, not one siting figure used both ways. The per-pair Gaussian skew
sits on top, for the asymmetry that is a property of the pair rather than of either end.

**Calibration.** Where a scenario ships fitted coefficients it has measured what its links actually
do, and that beats this budget: on Batumi the fit is trained on 296 observed links, and the raw
budget disagrees with them badly enough to break the mesh into 15 pieces the observations show as
one. The vendored function is called rather than reimplemented, so the number is exactly the one the
preset was fitted to produce. Per-node gains go in as the endpoints' antenna gain, where the fit
expects them - `raw_snr` is one of its features - and the snapshot's own gains are all zero, so a
default run reproduces the preset and an `--amplifier-mix` run asks what an amplifier would do to a
mesh measured without one.

These coefficients are one city, 296 links and one window. They are not a better link model in
general: taking them elsewhere transports Batumi's ridges and rooftops to a place that does not have
them.

**The envelope.** A fit answers any distance asked of it. Batumi's was trained on links reaching
23.2 km - three past 20 km, none past 30 - with ground-elevation terms that are positive and
unbounded against a log-distance penalty that grows far more slowly. Mirrored past one tile it stops
being an approximation: at four tiles a tenth of the links run beyond 42 km and the longest reaches
60.6 km. Past the envelope the raw budget answers instead - only a physical path loss, but a
physical path loss everywhere (TRAPS 4).

## Link quality

Every directed link is graded twice.

**By margin** - `comfortable` (≥10 dB), `adequate` (5-10), `fragile` (<5, so a little fading removes
it). These are geometry and do not depend on the noise floor at all. `near_miss` counts the other
side of the cliff: pairs within 6 dB below sensitivity, which a real radio would sometimes hear and
this one never does.

**By what it delivers**, which is the grading that answers "how many links here are genuinely
marginal". Under a fixed noise floor the answer was none: the threshold sat 5 dB into the flat top
of the PER curve, so every link the mesh would use delivered 96%+ and everything worse was not a
link. Under the thermal floor the threshold lands on the knee - a LONG_FAST link at sensitivity
delivers 39% - and a marginal band exists to measure. That band is the population every retry,
coding-rate and repeat mechanism in this design exists to serve.

**The denominator matters.** Quoting either grading against the live link count alone is a trap: a
stretched mesh loses its worst links off the bottom of the graph, so the share of *surviving* links
that are bad can improve while the mesh gets worse. Every share is reported twice - against live
links, and per thousand ordered pairs, which is fixed whatever the stretch does. Read the second
across a stretch sweep, with `sub_sensitivity` beside it for what fell off the cliff.

Delivery probability is zero below sensitivity, because `neighbours` is thresholded there and such a
pair is never offered a packet at all.

Duct reach is precomputed from the widest lift any configured duct can produce, so a delivery
filters a candidate set rather than scanning all *n* receivers per transmission.

## Reception

A radio cannot hear while it is keying up. A router relays everything it hears, so it spends a
large share of the time deaf, and the node beside it - same traffic, fewer relays - is the better
listener.

`AirTime` charges every packet a receiver *could* hear against its channel utilisation, decoded or
not, and that figure sizes the contention window for our own traffic. Under a duct it rises for
everyone, which is how an operator's mesh gets slower on the evening it appears to get bigger.

One duct lift applies to a whole transmission, taken at its start - a duct does not open or close
inside a frame. Above zero it does two things at once: it brings pairs that are not links into
range, and it makes every existing link louder, which is what turns extra reach into extra
contention rather than a free gain. Interferers are lifted too; leaving them unlifted would have
ducting deliver distant packets into a channel that had gone magically quiet.

A noise excursion arrives as a penalty on RSSI rather than as a change to the floor, because the
PER curve reads only their difference - 4 dB more noise and 4 dB less signal are the same packet.
That keeps the vendored `radio_loss` a clean copy, and it is why the excursion is applied per
reception: the floor a packet met is a property of when and where it was heard, not of the
configuration. Exactly one random number is drawn whatever the profile, so turning a profile on does
not move the stream.

## Failure

`take_down` is not a deletion. Every other node keeps its NodeDB record and keeps believing what it
last learned, including a next hop pointing through the dead node. Failure is not broadcast, so the
gap between what the mesh believes and what is true has to be modelled. `bring_up` restores a node
with everything it knew - a node merely out of range loses nothing, where a reboot loses far more,
and `wipe` covers that case.

Partitioning scans both directions, because links are not reciprocal: `_build_links` gives each pair
an asymmetry draw, so A can hear B without B hearing A, and scanning only outward would leave every
inbound-only link intact and the mesh connected through them.

## The queue's order

`MeshPacketQueue::enqueue`. From 2.5 this is an upper-bound insert into a sorted list: the deferred
group always sorts behind the ready one, the ready group is priority order, and at equal priority a
packet already on the mesh sorts ahead of one we originated; within the deferred group it is
deadline order. Keeping the groups apart is what makes the late-rebroadcast window work - a clamped
packet goes to the back and stays there until its time comes.

2.4 has no late group and no relayed-first tie-break: a max-heap ordered by priority alone, ties to
the lower packet id. Pop order under that comparator is a total order, so a sorted insert reproduces
the sequence the heap dequeues.

`setTransmitDelay` tells a relayed packet from a composed one by the RSSI and SNR it arrived with: a
locally generated packet has both at zero, and the radio's noise floor offset guarantees a received
one never does.

`clampToLateRebroadcastWindow` is what ROUTER_LATE does when it hears someone else relay: it will
not cancel - that is the role's point - but it moves to the back of the window, so it only speaks if
the mesh still needs it.

## Resolving a relay byte

`NodeDB::resolveLastByte` returns UNIQUE, AMBIGUOUS or NONE. `relay_node` and `next_hop` are one
byte of a 32-bit node number, so on a mesh of any size they collide. Callers treat anything but
UNIQUE as the safe branch - decrement the hop limit, flood instead of unicasting, learn nothing -
and the two failures are kept apart because they say different things: AMBIGUOUS is a dense mesh,
NONE is a mesh this node has not learned.

Two gates decide the candidate set, and both shrink it well below "every node with this byte". The
**candidate** gate is the hot store, minus ourselves and any ignored node: an evicted or never-heard
peer is not a candidate. The **relevance** gate asks whether the peer is a plausible relay for this
question - on the send path a direct neighbour heard within two hours, otherwise a direct
neighbour, a favourite or a router-like node.

So a smaller store makes the byte *less* ambiguous rather than more, which is the opposite of a
birthday bound over the whole mesh. A large mesh costs knowledge, not resolution.

Only this tree scans for a second candidate. Under 2.6 and 2.7 the lookup takes the first node it
matches and the caller is never told it guessed.

## Hops and routes

`Router::shouldDecrementHopLimit`: a hop between two favourited routers costs nothing, so a spine of
them does not eat the sender's hop budget, and the first hop always pays. The two implementations
identify the previous relay differently - this tree resolves the byte and preserves the hop only
when exactly one node answers, so ambiguity charges the hop; 2.7 walks its own store for favourited
router-like nodes and preserves on the first byte match, which on a dense mesh gives a free hop to a
node that merely shares a byte with a favourite.

`FloodingRouter::roleAllowsCancelingDupe`: a ROUTER never drops a relay it has queued, however many
other stations it hears do the job. The role exists to be the copy that goes out regardless.

`NextHopRouter::getNextHop` returns None for flood. A stored route decays - unconfirmed for half an
hour, or three failed directed deliveries in a row, and it is cleared rather than trusted for one
more DM. A packet is never handed back to the node that just relayed it, and a byte that no longer
resolves to a single reachable neighbour is never emitted.

Decay needs a health record still matching the stored byte, and `route_health` is capped with LRU
eviction, so a destination whose record was evicted keeps its `next_hop` with no TTL and no failure
count to age it. That is the firmware's behaviour, not a shortcut: `NextHopRouter.cpp:297` guards the
same way on the same cap of 32, with a comment saying a next hop set by another path "is left
authoritative". On a mesh holding more than 32 live routes a dead hop can be trusted until something
routes around it - worth knowing when reading a large-mesh result.

The route lives in the destination's own hot-store record, as `NodeInfoLite.next_hop` does, so
evicting a peer forgets the way to it - a cost separate from the relay byte's ambiguity. The
overflow cache covers exactly that case: a node past the store's capacity whose route traceroute or
an ACK taught, and whose record has since gone. A stale hint there is cleared rather than tried.

`noteRouteLearned` refreshes a route without forgiving it: the failure count clears only when the
hop itself changes, so an asymmetric reverse path that keeps re-teaching a dead forward hop still
ages that hop out.

A traceroute reply is what teaches anything - a node finding itself in the returned route learns a
next hop for every node beyond it, not just its neighbour.

## Signature policy

`Router::checkXeddsaReceivePolicy`. COMPATIBLE takes anything, STRICT only what it can verify, and
BALANCED accepts unsigned traffic in general but drops an unsigned broadcast from a node it has
already seen sign, when that payload would have fitted a signature.

The size test is the sharp edge. It mirrors the sender's gate, so a payload big enough to push a
signature over the frame is exempt from the downgrade rule - which is what an attacker inflates to
evade it, and what would make an honest unsigned broadcast get dropped if a signable type grew past
the budget.

`verifyFirstContactNodeInfo` is how a mesh bootstraps under STRICT at all: a signed NodeInfo carries
the sender's own key and the node number is a CRC32 of that key, so the packet verifies against
itself and nobody can claim another node's number with it. Without it, the NodeInfo that would teach
the key is dropped for want of the key.

A policy rejection deliberately does not cancel a queued rebroadcast of the same packet: it is
attacker-controlled input, and letting it cancel would hand anyone a way to silence a relay.

## Repeat scaling

`meshTooBusyForExtraRepeats` is three unvalidated constants, any one of which forces a single copy:
channel utilisation over 10%, our own transmit share of the last hour over 4%, or more than ten
direct neighbours. That neighbour count is `HopScalingModule`'s zero-hop bucket - a sampled,
hourly-rolled estimate rather than the exact count - so on a mesh whose sampling denominator has
climbed the threshold reads low and extra repeats stay on longer than the exact count would allow.

`getDupeCancelThreshold`: text tolerates one heard copy and nothing else does. An undecodable packet
is classified from the plaintext header instead - flooded traffic as text-like, directed traffic as
not.

`perhapsHandleUpgradedPacket`: a copy with more hops left than the one queued reached us by a
shorter route, so it is swapped in. Relaying the copy with fewer hops left would strand everything
beyond our own horizon.

## Traceroute

`alterReceivedProtobuf`: a relay writes itself into the route before passing it on, and
`TraceRouteModule` picks the array by direction - `route` while the request travels out,
`route_back` once the destination has answered - so a reply coming home by a different path cannot
append onto the outbound leg. `request_id` marks a packet as the reply.

`updateNextHops` on a returning reply: if the route is A→B→C→D then B learns C as the next hop for
C *and* for D, and C learns D for D. A node that is the original sender takes the first entry; a
node last in the route takes the responder itself.

The guard is the part worth having. The route array is unauthenticated payload, so this tree refuses
to learn from it unless the node it names as our next hop is the one that actually relayed the
reply, and treats a missing relay byte - an MQTT-sourced packet with no RF corroboration - as
unlearnable. 2.7 has the learning without the guard, so a forged reply could point any node's
`next_hop` anywhere.

`maybeSetNextHop` mirrors a traceroute hint into the overflow cache even for a target the hot store
has no room for: a full known route is the highest-confidence source there is.

## Replies and ACKs

`RoutingModule::getHopLimitForResponse`: a reply needs the hops the request used plus a margin,
because the way back may differ - not the sender's whole budget. A request that arrived with a
`hop_start` of zero is answered directly and not relayed at all.

`ReliableRouter::sendAckNak`: only the addressee answers, and only for a request. A packet that is
itself a response gets a hop-limited ACK, so the far end stops retransmitting without the ACK
flooding.

`NextHopRouter::sniffReceived` learns a route from a delivery that demonstrably worked, under two
gates: only a relayer that also carried the original teaches anything, and only when its byte
resolves to one node. Without the first the learned hop need never have touched this path; without
the second every future DM aims at whichever node shares a last byte.

## Hop policy on our own packets

`Router.cpp:483` and the Portduino zero-hop list. The hop recommendation reaches routine device
broadcasts and nothing else - position, telemetry, nodeinfo, neighbourinfo - and can only lower the
limit, never raise it above what the operator configured. A text message is untouched, which bounds
how far the feedback loop can reach.

A zero-hop portnum is capped afterwards. Both paths reduce `hop_start` by the same amount as
`hop_limit`, so `hops_away` computed downstream stays honest - changing only the limit would
silently corrupt the very histogram the recommendation came from.

The hop-scaling module runs `RUNS_PER_HOUR` times an hour and rolls once, so the recommendation
moves on an hourly cadence however busy the mesh is. Each node's roll is offset, since nothing
synchronises boot times.

## Retry ladders

Two candidate mechanisms, neither in a release. The **coding-rate ladder** (branch `CRCRRCRRR`)
sends a retry that already failed at a slower rate - base, then one step slower, then 4/8 - keyed by
`(from, id)` so every copy of the same retransmission picks the same rate. **M4** starts flooding
one retry sooner when a route is not proven healthy, trading airtime for recovery latency and
leaving a fresh, never-failed route on the unchanged path.

## Building a mesh

**Boards, sitings and roles are drawn, not striped.** A mesh whose one STM32WL or one basement node
sits on the only bridge is a case striping would never produce.

Router-like roles go to the head of the placement order; CLIENT_MUTE is drawn at random from the
rest, because muting a node is a decision about power or noise rather than siting, and handing it to
the worst-connected nodes would make it look free.

`--router-placement` chooses what a router is: `degree` is what an operator does - the repeater goes
on the hill; `inverse` is the adversarial control, the router in the basement with three neighbours,
which is what happens when someone flashes ROUTER onto the node they already own; `random` separates
the role's own effect from the siting that usually comes with it.

`--amplify-worst` is the field pathology: the node nobody can hear gets an amplifier bolted on,
which fixes its outbound reach and nothing else. It is now heard by everyone and still hears almost
nobody, so it relays into a mesh it cannot receive replies from and its rebroadcasts cancel copies
queued by nodes that could have carried them further. Fitted after the links exist, because "hears
worst" is a property of the mesh rather than of the node.

**Hop limits.** Operators do not all set the same one: a node in a dense middle reaches what it needs
at 3 or 4 and leaves the default alone, while one on the edge raises it until the rest of the mesh
answers, and field guidance tops out at 7. `centrality` reproduces that correlation and therefore
confounds hop limit with position - a table of receptions by hop limit then measures siting under a
hop-limit label. `random` breaks the correlation as a control, and is not how operators behave.

Hop preservation only fires between nodes that have favourited each other, which in the field means
one operator running both ends of a spine. Every router-like node favouriting every other is the
upper bound on how much relaying can be free.

**A scenario overrides all of it.** Real geometry decides where the nodes are and therefore how many
there are: the place is the input, not a shape to fit a requested count into. Stretching it is
refused rather than silently ignored - moving Batumi's nodes apart makes it somewhere else, and a
result labelled `batumi` would no longer be about Batumi. Recorded roles beat anything derived from
degree, and measured antenna heights beat any generated mix: a real snapshot knows which nodes are
on a mast and which are on a windowsill, and that difference decides more links than the mixes do.

## Reading adaptive behaviour

Every adaptive quantity is in a feedback loop - the hop recommendation feeds what gets sent, which
feeds the histogram it came from; the congestion coefficient feeds how often a node sends, which
feeds how many peers everyone hears. An end-state mean cannot tell a value that settled from one
still swinging between two, so sampling per node over time is a prerequisite for reading any of
these results rather than a follow-up to them.

`hop_report` puts three things side by side for one node: `truth`, the topological distance to every
reachable node, which no device can know; `observed`, every hop count this node actually saw,
exhaustive and exact; and `estimated`, what the firmware's own structure would report - sampled,
capped, hashed into collisions and scaled back up. All three are indexed by `hops_away`, where a
direct neighbour is zero, because `getHopsAway` is `hop_start − hop_limit`; a BFS distance counts
that neighbour as 1, so truth is shifted down to match rather than reported in units nothing else
uses.

The overlap window is derived per preset - one maximum-length frame plus a fifth - because the span
across presets is two orders of magnitude, 0.175 s at SHORT_TURBO against 28.6 s at VERY_LONG_SLOW,
and one number cannot be both correct at the slow end and cheap at the fast end.
