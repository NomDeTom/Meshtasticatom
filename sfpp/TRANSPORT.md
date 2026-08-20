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
