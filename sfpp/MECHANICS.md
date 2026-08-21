# How this simulator works, from first principles

Companion to three other documents, and the one to read first. [README.md](README.md) is the
operating manual - what to type and what the output means. [MODEL.md](MODEL.md) says what the
physical and traffic models claim. [TRANSPORT.md](TRANSPORT.md) is the firmware reference: for every
mechanism, the C++ it came from and the decision it makes. [TRAPS.md](TRAPS.md) is how all of it has
lied.

This document is the **mechanism**: what a node is, what a link is, how time advances, what happens
between a `send()` and a delivery, and where a collision is and is not possible. It repeats a little
of the others where a mechanism cannot be explained without it, and points at them for the rest.

Every mechanism below names the firmware release its behaviour is pinned to. Three answers appear:

| pin | meaning |
| --- | --- |
| **a release series** (2.4 - 2.8) | `Profile` selects it, and `FEATURE_TAG` in `mesh.py` names the exact release tag it shipped in |
| **this tree** | written from firmware source but not in any release - a branch, a compiled-out flag, or a proposal |
| **no firmware** | a modelling decision. `legacy` is the largest of these and is **not a firmware version** |

`sfpp/version.py` carries the simulator's own version and the changelog of behaviour changes. Two
runs are comparable when their `SIM_VERSION` agrees on MAJOR.MINOR.

---

## 1. Three objects, and nothing else

The whole simulation is three kinds of object plus a clock.

**A `Node`** is a radio and the state a device carries. It has a position, a role, a firmware
`Profile`, a board (`platform`), and about thirty slots of state - a NodeDB in three tiers, a packet
history, a transmit queue, two airtime rings, a route-health table, a hop-scaling module. It is a
plain object with no thread and no process of its own: nothing in it runs, it is only read and
written by the mesh.

**A `Packet`** is a frame: origin, destination, portnum, hop limit, `next_hop` byte, `relay_node`
byte, length, coding rate, and - once heard - the `rx_rssi` and `rx_snr` of the copy that arrived.
`copy()` is used constantly, because a relay is a new frame carrying the old payload, and the
distinction between a packet and a copy of it is where several firmware behaviours live.

**A `Transmission`** is a packet occupying the air: `(packet, tx_node, start, end, sender_role)`.
This is the only object with a duration. Every collision question is a question about the overlap of
two `Transmission` intervals and about the RSSI each one arrives at.

**The `Mesh`** owns all of them, plus the clock, plus the link matrix. There is no separate scheduler
object and no per-node process. Every state change in the simulation happens inside one of the
mesh's methods, called from the event queue.

The consequence worth stating: **there is no concurrency**. A firmware race between two interrupt
contexts cannot be reproduced here, and nothing in this tree claims to. What is reproduced is the
*ordering* the firmware's own single-threaded main loop imposes, plus the timing of the radio.

---

## 2. The net of nodes

### 2.1 Positions

Nodes get positions one of two ways.

**Generated.** `place(topology, count, area, rng, min_dist)` draws points into a square of side
`area` under one of five topologies - `uniform`, `clustered`, `corridor`, `hub`, `chain` (README
§5.1). Every draw enforces `min_dist` between nodes, defaulting to 300 m, because two Meshtastic
nodes ten metres apart are one node for every purpose this simulator measures.

**From a scenario.** `sfpp/terrain.py` loads a real place: `batumi` is the packaged 92-node snapshot,
`map` pulls the public map inside a bounding box. A scenario with `fixed_geometry` decides its own
node count, roles and hop limits, and the campaign overwrites `--nodes` from it rather than
ignoring the mismatch (TRAPS 9).

`stretch_points(points, factor)` scales every distance about the centroid **after** the draw, and
consumes no randomness. That is the only way to vary distance while holding the arrangement and the
traffic schedule fixed; changing `--area` redraws the mesh and changes both.

### 2.2 Height, and why it is two numbers

With no terrain grid a node sits at `ground_m = 0.0` with `antenna_height_m = None`, which defers to
the path-loss model's own default. That is exactly what every run made before terrain existed
assumed without saying so, which is why a no-terrain run is bit-identical to those.

With a grid, `_lift_to_terrain()` fills both: `ground_m` from the grid under the node, and
`antenna_height_m` above it. **Antenna height never becomes altitude.** The link budget asks what is
*between* two nodes, and a node's own elevation answers only half of that - which is why terrain is a
grid and not a per-node number.

### 2.3 Roles

Six roles, from `config.device.role`:

| role | what it changes |
| --- | --- |
| `CLIENT` | the default; relays everything, waits out the router offset first |
| `ROUTER` | skips the router offset, so its relay goes out first; never cancels a queued relay on hearing someone else's |
| `ROUTER_LATE` | relays where everyone else has given up - on hearing a duplicate it moves to the back of its own window instead of cancelling |
| `CLIENT_BASE` | 2.7+; behaves like a router for its operator's *favourites* only |
| `CLIENT_MUTE` | never relays anything |
| `REPEATER` | relays, and skips the offset in every series but 2.8 |

`ROUTER_LIKE = (ROUTER, ROUTER_LATE, CLIENT_BASE)` is the set that hop preservation and
role-aware cancellation test against.

**Which roles skip the router offset moved every series**, and it is one of the largest behaviour
differences between releases: `Profile.early_rebroadcast` is `router_repeater` up to 2.6,
`router_repeater_favourite_base` in 2.7, and **`router` alone in 2.8** - so a repeater that went
first in 2.7 waits its turn in 2.8.

Roles are assigned by degree by default (`--role-placement`), because that is what a deployment
does: the operator puts a router where it can hear the most.

### 2.4 Rebroadcast mode

`config.device.rebroadcast_mode`, orthogonal to role, six values. `ALL` is the default;
`CORE_PORTNUMS_ONLY` (2.5+) relays only portnums 1, 3, 4, 5, 67 and 70 - nothing the SR protocol
invents is among them, so under that mode no node relays an advert or a replay. `KNOWN_ONLY` and
`LOCAL_ONLY` require the originator to be in this node's NodeDB, which makes them **subject to
eviction**: forgetting a node stops relaying for it until it is heard again. `NONE` relays nothing.

### 2.5 Platform

`--platform-mix` gives each node a board, and the board decides how much of the mesh it can hold:
`PLATFORM_HOT_STORE`, `PLATFORM_WARM_STORE` and `PLATFORM_COLD_CACHE`. An `stm32wl` has no warm tier
and no cold cache at all; an `esp32s3_16mb` holds 2000 warm entries. This is not decoration - the
NodeDB bound is load-bearing (§7), and a mesh of small boards forgets things a mesh of large ones
does not.

---

## 3. The matrix of link-pairs

`_build_links()` computes, once, an `n × n` matrix `rssi[i][j]`: the received signal level in dBm
when *i* transmits and *j* receives. Everything about propagation is decided here and never
recomputed per packet.

### 3.1 What goes into one cell

For each **unordered** pair, once:

```
loss        = phy.estimate_path_loss(conf, distance, freq, height_i, height_j)
terrain_db  = terrain_obstruction_loss(conf, point_i, point_j, freq)
clutter_db  = clutter_obstruction_loss(conf, point_i, point_j)
base        = PTX + 2*GL - loss - terrain_db - clutter_db
shadow      = gauss(0, MODEL_SHADOWING_STDDEV)        # 6 dB
skew        = gauss(0, MODEL_RADIO_ASYMMETRY_STDDEV)  # 2 dB
```

and then for each **direction**:

```
rssi[i][j] = base + tx_gain[i] + rx_gain[j] + skew - shadow
rssi[j][i] = base + tx_gain[j] + rx_gain[i] - skew - shadow
```

Four kinds of term, and the symmetry of each is the point:

| term | symmetry | why |
| --- | --- | --- |
| path loss, terrain, clutter | **symmetric** | properties of the path between two points |
| `shadow` | **symmetric** | shadowing is buildings and trees on the path, which do not rearrange themselves depending on who is talking |
| `skew` | **antisymmetric** | the radios: power amplifier, antenna match, front end |
| `tx_gain[i]`, `rx_gain[j]` | **per node, per direction** | siting and amplifiers - a basement is a bad place to transmit *and* to receive; a PA gives 8-15 dB out and nothing back |

Link variation used to be one antisymmetric draw with no shadowing at all, which made link existence
a near-deterministic function of geometry while simultaneously overstating asymmetry (TRAPS 24).

Path loss is **floored at free space**: no environment attenuates less than empty space does, and a
log-distance model with a small exponent otherwise answers below it at short range.

### 3.2 Fitted scenarios

Where a scenario ships fitted coefficients it has measured what its links actually do, and that beats
the generic budget - on Batumi the raw budget disagrees with the 296 observations badly enough to
break the mesh into 15 pieces the observations show as one. The vendored `calculate_link_budget` is
**called rather than reimplemented**, so the number is exactly the one the preset was fitted to
produce.

Two guards on that, both of which exist because a fit answers any input:

- **The envelope.** Past `LINK_CALIBRATION_MAX_M` - derived from the observation list, 23,225 m on
  Batumi - the raw budget answers instead, and `loss_terms["beyond_calibration"]` counts how often.
  Expect it to be most of a `--mirror` run, whose seam-spanning pairs are outside by construction
  (TRAPS 4).
- **EIRP is outside the surface.** The fit is evaluated at a reference EIRP and the difference from
  the actual EIRP is added afterwards, decibel for decibel. Otherwise the fit silently absorbs the
  power level and every `--tx-power` or `--amplifier-mix` sweep is a no-op.

Read `docs/batumi_radio_calibration.md` before leaning on a fitted scenario's *geometry*. The Batumi
fit is a level-matching surface, not a propagation model: its distance slope is 0.94 dB per decade
where a propagation model is 20 to 40.

### 3.3 From the matrix to the graph

```
neighbours[i] = [j for j in all if rssi[i][j] >= effective_sensitivity(conf)]
duct_reach[i] = [j for j in all if sensitivity - duct_headroom <= rssi[i][j] < sensitivity]
```

`neighbours` is the link graph, and it is **directed**: `j in neighbours[i]` does not imply the
reverse. Partitioning, articulation-node analysis and mesh-breaking all scan both directions for
that reason - scanning outward only would leave every inbound-only link intact and the mesh connected
through links that cannot carry a reply.

`effective_sensitivity` is `max(datasheet_sensitivity, noise_floor + required_snr_db(sf))`. A
sensitivity figure is a noise floor plus what the demodulator needs above it, so taking one from a
table while the scenario supplies its own measured floor counts the band twice, in the optimistic
direction (TRAPS 20). On Batumi's measured −110.5 dBm that correction removed 1059 of 4813 directed
links.

`duct_reach` is the candidate set for tropospheric ducting: pairs that are not links but would be
under the widest lift any configured duct can produce. Building it at construction is what lets a
delivery filter a small candidate set instead of rescanning every receiver.

### 3.4 The matrix is drawn once, and rebuilding draws nothing

`_shadow` and `_skew` are drawn once for the life of the mesh and stored per pair. `_build_links()`
can then be called again - after an amplifier is fitted, to price a stretch - and it **moves nothing
it was not asked to move and consumes no randomness**. Redrawing re-randomised every link including
every pair nowhere near the amplifier, and advanced the RNG the traffic generator shares, so the
before and after of any such comparison were two different meshes carrying two different schedules
(TRAPS 12 is the same shape). Two tests pin it: a rebuild moves no unaffected pair, and a rebuild
leaves `rng.getstate()` unchanged.

### 3.5 What the matrix does not model

- **No frequency dimension.** One channel, so every transmission contends with every other audible
  one. A real mesh on two channel presets in one place does not.
- **No fast fading.** `rssi[i][j]` does not vary per packet from multipath. The moving noise floor
  (§5) varies the *threshold* instead, which reaches the same decisions by the opposite route but is
  not the same thing physically.
- **No mobility.** Positions are fixed for the run.
- **No antenna pattern.** Gain is one scalar per node per direction, not a function of bearing.

---

## 4. Time: how the event loop steps

The loop is thirteen lines.

```python
def at(self, time, fn):
    self._seq += 1
    token = [False]
    heapq.heappush(self._queue, (time, self._seq, fn, token))
    return token

def run(self, until):
    while self._queue and self._queue[0][0] <= until:
        time, _, fn, token = heapq.heappop(self._queue)
        self.now = time
        if not token[0]:
            fn()
    self.now = until
```

Five properties follow, and each one matters somewhere:

**Time is continuous and advances in jumps.** `now` is a float in milliseconds and takes exactly the
values events are scheduled at. There is no tick, no timestep, and no quantisation of time itself.
Nothing is evaluated between two events, so nothing needs to be: state changes only inside `fn()`.

**Ordering is total and deterministic.** The heap key is `(time, seq)`, and `seq` is a monotonic
counter. Two events at the identical timestamp fire in the order they were *scheduled*, never in an
arbitrary order - so a run is reproducible to the bit at a fixed seed, and a paired before/after at
one seed is a valid comparison. Without the sequence number, heap tie-breaking would fall through to
comparing the functions themselves.

**Cancellation is a flag, not a removal.** `cancel(token)` sets `token[0] = True` and leaves the
entry in the heap, to be popped and skipped. This is deliberate: it is O(1), and it matches the
firmware, where a timer that has already been overwritten does not have its old callback extracted
from anywhere - it simply no longer does anything. `Node.tx_token` is exactly the firmware's
`txTimerOverwrite`: one pending transmit timer per radio, replaced on each call.

**There is no event for "nothing happened".** A quiet mesh costs nothing. Runs of many simulated
hours are cheap because the loop is driven by traffic, not by wall-clock granularity.

**The loop is single-threaded and reentrant-by-scheduling.** An `fn()` may schedule more events,
including at the current `now`, and they queue behind whatever is already at that timestamp. Nothing
runs *inside* anything else.

### 4.1 The events the mesh schedules

`sfpp/mesh.py` has exactly six scheduling sites:

| scheduled by | at | does |
| --- | --- | --- |
| `_arm(node, when)` | the transmit delay's expiry | `_service_queue(node)` - send the front packet, or wait some more |
| `_start_send` | `tx.end` | `_deliver(tx)` - the whole reception pass for one transmission |
| `_start_retransmission` | `now + retransmission_msec` | `_do_retransmission` - one more attempt, or give up |
| `_do_retransmission` | the same interval again | itself, until the budget runs out |
| `start_hop_scaling` | an hourly cadence | `HopScaling.roll_hour()` on each node with the module, then `required_hop = max(suggested, role_floor)` |
| `start_adaptive_trace` | every 30 minutes | one row per node of every adaptive quantity, kept as a series |

Everything else inside the mesh - a rebroadcast decision, a route being learned, a NodeDB update, an
ACK - is a plain function call from one of those six, and happens at the same `now`.

**The campaign layered on top schedules its own**, through the same `mesh.at`: advert emissions,
replay ticks, chain ticks, probes, admin session legs, bucket sampling, and every originated packet
from the traffic generator. That is deliberate - one clock, one ordering, so nothing in the protocol
under study can run in a different time base from the mesh carrying it.

---

## 5. From `originate()` to the air

Seven stages, each pinned to firmware.

### 5.0 Origination - `Router::send`

`originate(node, portnum, length, ...)` injects a packet from a node's application layer, as if the
device had composed it. Everything the campaign's traffic model does goes through here, and six
things happen before the packet reaches the queue:

1. **An offline radio composes nothing.** Returning a packet anyway would let the caller register a
   message that never existed; `sends_while_offline` counts the attempt.
2. **A PKI DM needs the destination's key.** Without it the message never reaches the air at all, and
   `dm_blocked_no_key` counts it - which is why that figure is reported separately from `lost`.
3. **Signing** (2.8): an unencrypted broadcast from a keyed node is signed if the payload still fits a
   frame with 66 more bytes on it, and the length *grows* by those bytes. Over the limit,
   `packets_too_large_to_sign`.
4. **The hop limit** comes from this node's own configuration - operators do not all set 3 - then
   `_apply_hop_policy` may lower it for the portnums that scale.
5. **A next hop** is looked up now, so a first send is directed when a route is known and floods when
   it is not.
6. **Our own packet enters our own history**, with our relay byte noted, so overhearing someone
   relaying it does not make us relay it back.

`want_ack` arms the retransmission timer here, with the budget the destination implies (§9.4).

Packet ids are **random on a real mesh, not sequential** - which is exactly why a receiver cannot
detect a gap, and therefore the reason set reconciliation exists at all. `new_packet_id` is a counter
here because nothing in the transport reads an id's ordering; the *protocol* under study is the thing
that must not.

### 5.0a Priority

`meshtastic_MeshPacket_Priority`, and only the values the queue order actually distinguishes:

| priority | value | what carries it |
| --- | --- | --- |
| `BACKGROUND` | 10 | bulk, deferrable traffic |
| `DEFAULT` | 64 | ordinary application traffic |
| `RELIABLE` | 70 | anything with `want_ack` |
| `ACK` | 120 | the acknowledgement itself |

A packet's default is `RELIABLE` when `want_ack` is set and `DEFAULT` otherwise; an ACK is
constructed at `ACK` explicitly. Priority decides queue position and which packet is sacrificed when
the queue is full. It does **not** change airtime, contention window, or anything on the air.

### 5.1 Enqueue - `MeshPacketQueue::enqueue`

`QUEUE_DEPTH` is 16. The ordering rule **changed at 2.5**, and `Profile.queue_late_first` selects:

- **2.4**: a priority max-heap, ties broken by packet id.
- **2.5+**: a sorted insert that puts deferred (`tx_after`) packets last, and, at equal priority,
  prefers a **relayed** packet over one this node composed itself. Someone else's packet is already
  in flight through the mesh; ours has not started.

**Overflow is the queue's only drop.** `setTransmitDelay` reschedules indefinitely, so congestion
here is a full queue and latency rather than an evaporated packet.

On a full queue, `replaceLowerPriorityPacket` makes room in three passes from the back forward: the
back if it is ready and worth less; otherwise the last *ready* packet past the deferred tail, because
a deferred packet is not necessarily the cheapest thing to lose; otherwise the back if its deadline
has already passed. `queue_drops` counts it either way - something is dropped, and only which packet
is in question.

### 5.2 The transmit delay - `RadioLibInterface::setTransmitDelay`

**A relayed packet is told from a composed one by the RSSI and SNR it arrived with.** That is the
actual firmware test, and it is why `_receive` attaches `rx_rssi` and `rx_snr` to its copy.

| case | delay |
| --- | --- |
| composed here (`rx_snr == 0 and rx_rssi == 0`) | `getTxDelayMsec` |
| relaying someone else's | `getTxDelayMsecWeighted(rx_snr)` |
| already deferred | re-armed, capped at `2 * getTxDelayMsecWeightedWorst` |

`getTxDelayMsec` sizes its window from **channel utilisation**: `cw = map(util, 0..100, CWmin..CWmax)`
and the delay is `random(0, 2^cw) * slotTime`. A busy mesh backs off harder, which is a feedback loop
and one of the few places where the mesh regulates itself. `Profile.util_backoff` is on for every
firmware series; `legacy` draws `uniform(1, 4) * slotTime` instead, with no reference to how busy the
channel is.

`getTxDelayMsecWeighted` sizes its window from **SNR**: `cw = map(snr, SNR_MIN..SNR_MAX,
CWmin..CWmax)`. A loud packet means a close sender and therefore a large window, so distant nodes -
which have more to contribute to a flood - go first. Nodes that do not `shouldRebroadcastEarlyLikeRouter`
add `2 * CWmax * slotTime` first, so a router's copy is out before a client's window even opens.

Two firmware details are reproduced rather than cleaned up:

- **`arduino_map` is integer arithmetic with no clamp.** An SNR outside the mapped range produces a
  `cw` outside `[CWmin, CWmax]`, and the firmware does not clamp it. `Profile.clamp_cw` exists to
  ask what clamping would do; no release turns it on.
- **`random(0, bound)` is integer and half-open**, so `bound` itself never comes out and the slot
  count is discrete. `legacy` draws continuously instead, which removes collisions only discrete
  slots can produce.

`CWmin`/`CWmax` and the SNR range **both moved across 2.5 and 2.6** (`CW_BOUNDS`, `SNR_BOUNDS`),
which shifts every rebroadcast delay on a strong link.

### 5.3 Slot time - `RadioInterface::computeSlotTimeMsec`

```
symbol_ms = 2^sf / (bw_khz)
slot      = max(2.25, 2 + 0.5) * symbol_ms + 7.6         # sub-GHz
slot      = (4 + (2*sf + 3) // 32) * symbol_ms + 7.6     # wideLora, per AN1200.22
```

The 7.6 ms is propagation, turnaround and MAC processing. `wideLora` is a property of the configured
**region**, not of the bandwidth - selecting on bandwidth would put the LONG_FAST slot at 40.4 ms
rather than 28.1. The CAD term is integer division, as in the C++.

### 5.4 Listen before talk

`_service_queue` refuses to transmit when `_channel_busy(node)` or when the radio is still keying up
(`busy_until > now`). Each refusal is a `deferral`, and re-arms the delay.

`_channel_busy` is the CAD check: is any transmission still on air whose RSSI at this node clears
this node's energy-detection floor? The floor is `effective_cad_threshold` against **the band this
node is in now**, so a node cannot hear a channel as clear and then fail to decode what was on it.

`Profile.max_backoffs` reproduces a pre-fold-in defect faithfully: past the cap the packet is
*dropped*, counted as `dropped_to_backoff_cap`. No firmware does this - `setTransmitDelay` reschedules
indefinitely - so it is `None` for every firmware series and 400 under `legacy`, because the runs
measured under that profile had it.

### 5.5 On the air - `_start_send`

```
duration       = airtime_ms(length, coding_rate)
busy_until     = now + duration          # a radio transmits one packet at a time
log_tx_airtime(now, duration)            # AirTime's TX ring
packet.relay_node = radio.relay_byte     # our last byte goes on the wire here
transmissions.append(Transmission(...))
at(tx.end, lambda: _deliver(tx))
```

Air-util-TX is charged at **start** because a radio never overlaps itself. Channel utilisation is
charged in `_deliver` instead, with the receivers, so every busy interval reaches `sense_busy()` in
*end* order and the union is exact (§6.4).

`relay_node` is `NodeDB::getLastByteOfNodeNum` - all of our 32-bit node number that fits in one byte.
A zero low byte goes out as `0xFF`, so that value answers for twice as many nodes as any other, and
ambiguity resolution has to cope with it.

### 5.6 Airtime

`lib.phy.airtime` is the Semtech formula, called for every frame. Two corrections in its history are
worth knowing because they invalidated everything before them: time on air was multiplied by the
coding-rate denominator plus four rather than the denominator (inflating every preset by 37-60%), and
low-data-rate optimization was gated on bandwidth rather than symbol time (TRAPS 13). Airtime sets
contention, collision overlap, retransmission timing and channel utilisation, so nothing survives an
error in it.

---

## 6. Reception, collisions, and where a collision cannot happen

`_deliver(tx)` runs once per transmission, at its end, and is the whole reception pass. This is the
densest mechanism in the tree, so it is worth following in order.

### 6.1 Who is in the audience

```
audience = neighbours[tx.tx_node]
if lift:  audience += [j in duct_reach[tx] if rssi + lift >= sensitivity_at(j)]
```

The static link graph, plus - only while a duct is open - the sub-sensitivity pairs the lift reaches.
**One lift figure for the whole transmission, taken at its start**: a duct does not open or close
inside a frame.

### 6.2 The six ways a reception fails

In order, and the order matters because each is charged separately:

| # | test | counter | mechanism |
| --- | --- | --- | --- |
| 1 | `rssi < _sensitivity_at(rx, start, end)` | `lost_to_noise_floor` | the band this receiver is in has taken the link away for this frame |
| 2 | `not nodes[rx].online` | - | the node is off |
| 3 | `rx in transmitting` | `lost_to_half_duplex` | it was transmitting while this arrived |
| 4 | `not _survives_capture(...)` | `lost_to_collision` | something else held the receiver |
| 5 | `noise.wiped(start, end)` | `wiped_by_periodic` | a periodic emitter fired while this was in flight |
| 6 | `_deaf(rx)` or `_lost_to_phy(...)` or `extra_loss` | `lost_to_phy` | a loss burst, or the SNR-to-PER draw |

Each of those is **per reception opportunity**, not per packet: one broadcast heard by fifty nodes
can produce fifty collision losses. The counters are for the *ratio* between them, never as rates -
`lost_to_collision` far exceeding `lost_to_phy` says the mesh is contention-limited rather than
range-limited, which is a different problem with a different fix.

### 6.3 The collision model

Two transmissions overlap when `o.start < tx.end and o.end > tx.start`. That predicate is the whole
collision criterion. `_overlapping(tx)` applies it while scanning backwards through `transmissions`,
bounded by `max_airtime_ms` - the airtime of a maximum-length frame at this preset
(`MAX_PAYLOAD_BYTES`, 237) plus a fifth. The bound decides only when the scan may stop, so it is a
guard on that early exit and not a physical quantity: no decision reads it, and being generous costs
nothing but time. It is **derived per preset** rather than constant, because the span is two orders of
magnitude: a flat 20 s sat under VERY_LONG_SLOW's 28.6 s full payload, and anything still in flight
past the window left the interferer scan - 130 of 5669 transmissions, the longest ones.

The scan is bounded by *start* time and does not stop at the first transmission that has already
ended: starts are monotonic, ends are not, because a long frame started earlier can still be on air
after a short one that started later has finished.

An overlapping transmission only matters if the receiver can hear it:

```python
audible = [o for o in interferers
           if o.tx_node != rx and rssi[o.tx_node][rx] + lift >= cad_floor]
```

`cad_floor` is **this receiver's own** energy-detection threshold for this frame, band included. It
used to be a mesh-wide constant of sensitivity minus three.

Then the capture rule, which is a **preamble lock**:

```python
if not audible:              return True     # nothing to collide with
earliest = min(audible, key=start)
if earliest.start < tx.start:
    return rssi >= rssi[earliest.tx_node][rx] + lift + CAPTURE_DB
return all(rssi >= rssi[o.tx_node][rx] + lift + CAPTURE_DB for o in audible)
```

Whichever preamble arrived **first** holds the receiver. A packet arriving into an already-locked
receiver needs `CAPTURE_DB` (6 dB) over the incumbent to break the lock. A packet that arrived first
keeps the receiver unless something much louder arrives. Interferers carry the same duct lift, so the
margin comparison is unchanged by ducting - and leaving them unlifted would have a duct deliver
distant packets into a channel that had gone magically quiet.

### 6.4 Channel-busy time, which is not the collision model

Every packet a receiver **could hear**, decoded or not, is charged against its channel utilisation,
because that is what `AirTime` does and it is what sizes the contention window for this node's own
traffic. Under a duct it rises for everyone, which is how an operator's mesh gets slower on the
evening it appears to get bigger.

A receiver has **one energy detector and one channel**. Two overlapping signals are one busy stretch
to it, not two: it cannot count transmitters, and when a packet fails it learns only that an Rx
failed - not why, and not how many were talking. So `sense_busy(start, end)` charges only the part of
a stretch not already covered, and the ring accumulates the *union*. Charging each overlapping
transmission its full airtime attributes knowledge no radio has and took the figure to 184% of
wall-clock (TRAPS 5). `node_channel_util_percent.max <= 100` is asserted on every scheduled run for
exactly this reason.

### 6.5 Where a collision is *not* possible

This is the part most easily got wrong, because several of these look like collisions and are not.

**Between two frames from the same transmitter.** `busy_until` makes a radio transmit one packet at a
time, so a node's own transmissions never overlap. This is why air-util-TX can be charged at start.

**At the transmitter itself.** `_survives_capture` filters `o.tx_node != rx`, and the half-duplex
test removes `rx in transmitting` before capture is even consulted. A node that was transmitting
loses the packet to **half duplex**, not to collision, and the two are counted separately - the fix
for one is not the fix for the other.

**With anything the receiver cannot hear.** An overlapping transmission below this receiver's CAD
floor is not an interferer at all. Two distant nodes transmitting simultaneously do not collide *at a
third node that hears only one of them* - spatial reuse is real here, and it is why a mesh-wide
aggregate is not a local condition (TRAPS 10).

**Outside the overlap.** Frames that merely follow one another do not interact, however tightly
packed. There is no inter-frame guard time modelled beyond the slot time's 7.6 ms.

**After capture succeeds.** Once a frame wins the capture test, remaining interference has no further
effect on it. There is no partial corruption: a frame either holds the receiver for its whole
duration or it does not. The PER draw that follows is about *link quality*, not about interference,
and giving the same energy two chances to kill one packet would double-count it.

**Between the copies of one flood at different receivers.** Each `(tx, rx)` pair is judged
independently. A flood that collides at node A can be received cleanly at node B in the same instant,
which is the whole reason flooding works.

**On a different channel.** There is no different channel. One frequency, so this exclusion is
vacuous here - and worth stating precisely because it is a real mesh's most common escape from
contention and this model does not have it.

### 6.6 The payload draw

`_lost_to_phy` is the empirical SNR-to-PER curve from `lib/radio_loss.py`: more redundancy survives a
worse link. **Exactly one random number is drawn whatever the noise profile**, so turning a profile on
does not shift the stream, and the same draw judged against the calm-band probability says for free
whether the band is what decided this packet (`lost_to_noise_excursion` / `saved_by_quiet_band`).

The curve is anchored to the modem's own requirement - `required_snr_db(sf)` plus a per-coding-rate
offset of a few tenths of a decibel - rather than to an absolute SNR per coding rate. An absolute
figure sat 12.5 dB from the demodulator limit at SF7 and on top of it at SF12, so a preset sweep was
confounded by which preset the curve happened to suit.

The curve is floored at 2% and capped at 99.5%, and **how much of that range a run actually visits
depends on the noise floor**, which is the single largest thing `--noise-model` decides:

| | success at sensitivity, `fixed` | `thermal` |
| --- | --- | --- |
| `LONG_FAST` | 0.964 | **0.388** |
| `LONG_TURBO` | 0.995 | **0.386** |
| `EXTRA_LONG_TURBO` | 0.974 | **0.095** |

Under the historical fixed floor the threshold landed 5 dB into the curve's flat top, so the whole
probabilistic band was 0.96 to 0.995 and **a link that worked a third of the time could not exist**.
Under the thermal floor - the default - the threshold lands on the curve's knee instead, which is
where such links come from. Everything measured before `--noise-model` existed is optimistic about
weak-link delivery by that margin, and the turbo presets are the worst affected (README §5.6).

The limitation that remains: delivery probability is **zero below sensitivity**, because `neighbours`
is thresholded there and such a pair is never offered a packet. So this model degrades a link until it
reaches sensitivity and then deletes it, and most of what stretching a mesh costs is invisible to the
delivery curve - `lost_to_cliff` dominates `marginal_now` in the stretch census. `link_quality.fragile`
(margin under 5 dB) and `near_miss` (within 6 dB *below* sensitivity) size what the threshold hides:
207 against 342 on a stock 60-node mesh. Letting sub-sensitivity pairs deliver probabilistically is
the fix, and it is a change to the vendored physics.

---

## 7. The modelled NodeDB

Three tiers, because the firmware has three, and the boundaries between them are where several
behaviours live.

### 7.1 The hot store - `NodeDB`, `meshtastic_NodeInfoLite`

`node.nodedb` maps peer index to `NodeRecord`: `last_heard`, `hops_away`, `has_key`, `next_hop`,
`is_favourite`, and whether it is protected. Bounded by `max_num_nodes`, which comes from the
platform - `PLATFORM_HOT_STORE`: 10 on an `stm32wl`, 120 on an nRF52840 or generic ESP32 (the
compile-time default), and 100, 200 or 250 on ESP32-S3 by flash size. Every board before 2.6 got a
flat 100; `PLATFORM_HOT_STORE_BY_VERSION` carries the earlier tables, because 2.6 and 2.7 do not
treat an nRF52 and a generic ESP32 alike where this tree does.

**The bound is load-bearing.** It caps what can be resolved, routed to, or counted as online.
`trim_nodedb()` sorts on `(is_protected, last_heard)`, so the stalest **unprotected** record goes
first and a protected one is only sacrificed when nothing else is left. Eviction is not a deletion in
the reader's sense: it **demotes** the record to the warm tier, keeping the peer's identity, key and
role while discarding its routing. That is how a learned route dies here with no expiry involved.

The consequences are worth holding in mind while reading a large-mesh result: `KNOWN_ONLY` and
`LOCAL_ONLY` rebroadcast modes stop relaying for a peer they have forgotten, a next hop cannot be
emitted for a destination no longer in the store, and `getNumOnlineMeshNodes` - the congestion
throttle's input - is bounded by the store as well as by the two-hour window.

`update_from(peer, now, hops_away)` is `NodeDB::updateFrom`. `hops_away` comes from
`hop_start - hop_limit`, so **a packet that has not been relayed yet is what tells us a peer is a
direct neighbour** - there is no neighbour discovery separate from ordinary traffic.

Two **two-hour** windows narrow what a record can be used for, and they are the same two hours by
coincidence of the firmware rather than by one constant: `NUM_ONLINE_SECS` decides whether a peer
counts as online for congestion scaling, and `NEXTHOP_NEIGHBOR_FRESH_MSEC` decides whether it is a
usable next hop. A peer in the store but not heard inside the window is neither.

### 7.2 The warm tier - `WarmNodeStore.h`, this tree's 2.8

`node.warm` holds peers evicted from the hot store, in far less memory. A node is in one tier or the
other, **never both** - `warm_take()` on re-admission empties the warm slot, and routing does not come
back with it. Size is `PLATFORM_WARM_STORE`, a different table from the hot store's and keyed on
memory class rather than flash: zero on `stm32wl`, 100 on nRF52840, 150 on the 4 MB and 8 MB ESP32-S3
and 2000 on the 16 MB.

**The key is what the tier exists for**, so its own eviction policy is about keys rather than age: a
keyless entry goes first, and a keyless candidate cannot displace a keyed one - it is simply not kept.
`copyPublicKey` reads hot then warm, and both are authoritative.

The compression is modelled exactly, because it is lossy in a way that matters: the low
`WARM_META_BITS` (7) of `last_heard` carry the role, the protected category and the XEdDSA-signed
flag, so **the timestamp left in the high bits has a 128-second resolution**. `warm_quantise()`
reproduces that rounding. A warm entry's age is therefore known only to the nearest two minutes,
which is enough to matter for a freshness comparison.

### 7.3 The cold tier - `TRAFFIC_MANAGEMENT_CACHE_SIZE`

`node.cold_keys` is public keys seen on the wire. It can answer the inbound-decrypt path and is
**never authoritative**: nothing routes or resolves from it. A NodeInfo packet sets `has_key` on the
hot record *and* caches the key cold, so an evicted peer's traffic can still be read.

### 7.4 The route cache - `TrafficManagementModule`

`node.route_cache` holds next-hop hints outside the hot store's bound, so it can carry a route for a
node the NodeDB evicted or never admitted. 2.8 only.

### 7.5 Packet history - `PacketHistory`

`node.history` maps packet id to a `SeenRecord`: the sender, the **highest hop limit anyone has shown
us**, the `next_hop` on the copy we first saw, the receive time, and up to `MAX_RELAYERS` (3) relay
bytes of everyone we have seen relay it.

Bounded by capacity only - `PACKETHISTORY_MAX`, which is `max(max_num_nodes * 2, 100)`, so 240 on the
default board - and it evicts the oldest slot. **There is no time expiry.** A node suppressing a duplicate is
suppressing it because the record is still in the ring, not because a timer has not fired, and on a
busy mesh the ring turns over fast.

The three fields are each read by a different later decision: `highest_hop_limit` drives hop upgrade,
the relayer list drives next-hop learning, and `next_hop` tells a node whether it was the intended
relay for a copy it is now seeing again.

### 7.6 Ambiguity - `NodeDB::resolveUniqueLastByte`

A relay byte is one byte of a 32-bit node number, so two nodes in a mesh can share it, and `0xFF`
answers for every number with a zero low byte. `resolve_last_byte` returns a *status*, not just a
peer: unique, ambiguous, or unknown. Before 2.8 a last-byte lookup took the first match, so hop
preservation and next-hop emission were **ambiguity-blind** - which is why node numbers here are real
32-bit values rather than small integers. Routing detects the collision instead of being safe against
it by construction, and a detection cannot be exercised without the collision.

---

## 8. Per-node hop histograms

Three histograms per node, in **two different units**, which is easy to misread and produces a
confident wrong answer.

| histogram | held in | unit | what it is |
| --- | --- | --- | --- |
| `truth` | computed from the graph | **nodes** | shortest-path distance to every other node, whether or not anything arrived |
| `estimated` | `node.hop_scaling` | **nodes** | what the firmware's own module believes, its scaled histogram |
| `observed` | `node.observed_hops` | **receptions** | receptions that arrived having travelled that many hops |

The first two are comparable - belief against truth, in nodes, which is the comparison the hop
recommendation actually rests on. The third is a different quantity: a busy neighbour contributes many
receptions at one hop, so it must not be read as a third column of the same table. The report's keys
carry the unit for this reason (`truth_peers_at_hop`, `estimated_peers_at_hop`,
`observed_receptions_at_hop`).

### 8.1 The module - `HopScalingModule`, 2.8

`HopScaling` is a **sampled, capped, hash-collided** estimate of how far the mesh is, and every one of
those three words is a way the estimate can be wrong while looking fine.

- **Sampled.** `sample(node_num, hops)` is called for every packet heard over the air, but only for
  peers whose hash passes `passes_filter(hash, sampling_denominator)`. Subsampling happens in *hash
  space* rather than by node number, so which nodes are sampled is stable as the mesh changes.
- **Capped.** `CAPACITY` is 128 entries. At 80% full, `trim_if_needed()` drops everything unseen for
  13 hours and then **halves the sample rate** if it is still full. Past `DENOM_MAX` there is nothing
  left to halve, and further peers are simply dropped - `dropped_full` counts them, and from then on
  the recommendation is skewed.
- **Hash-collided.** The key is a 16-bit Knuth multiplicative hash. Two peers that collide are one
  entry.

Each entry is `[hops_away, seen_bitmap]`, the bitmap covering 13 hours one bit per hour.
`roll_hour()` runs hourly: it summarises the surviving entries into a per-hop histogram, decides how
*generous* the recommendation may be from how fast the mesh is turning over, walks the histogram for
a suggested hop limit, scales the buckets by the filtering denominator, then shifts every bitmap
along by one hour.

The walk is "the first hop that reaches enough nodes, plus one if the next hop is cheap", where both
"enough" and "cheap" are scaled. The politeness numerator - 1, 2 or 4 - comes from comparing recent
hourly counts against older ones.

Two details are reproduced because they change the answer:

- **The filtering denominator is held for 13 rolls** after it rises, so buckets scaled under one
  denominator are not reinterpreted under another.
- **A negative hop count is clamped to zero rather than rejected**, following `NodeDB.cpp` - the
  conservative direction for a recommendation.

`hop_report(index)` prints truth, observation and estimate side by side for one node, plus the state
the estimate came from: entry count, both denominators, roll count and `dropped_full`. A
recommendation from a full table with a raised denominator is a different claim from the same number
off a table with room in it, so the state is reported beside it.

The nodes printed are chosen by *observed reach* at the tenth percentile, the median and the
ninetieth, plus the outright worst and best - never the mean node - and each row says how many nodes
sit in its neighbourhood, so one node is never mistaken for a population.

**`adopt_hop_recommendation`** closes the loop: `required_hop` becomes
`max(suggested_hop, role_floor)` - the floor is 2 for a tracker and 1 for a sensor - and the node's own
hop limit follows it. Until the module has rolled at least once with something in its table,
`required_hop` stays at `HOP_MAX`, so a fresh mesh is not throttled by an empty histogram. Adoption is
unconditional in the firmware wherever it exists, and separable here only so a sweep can hold the
feedback loop open and measure the module's belief without letting it act.

**`start_adaptive_trace`** samples every adaptive quantity per node every 30 minutes - `required_hop`,
the live hop limit, neighbour count, NodeDB size, `num_online`, channel utilisation, the module's
suggestion and denominators, and the congestion coefficient - and keeps the series. It is a
prerequisite for reading any adaptive result rather than a follow-up to one: a whole-run total cannot
distinguish a mesh that settled from one that oscillated.

---

## 9. Routing

### 9.1 Flooding - `FloodingRouter`, every series

`perhaps_rebroadcast(rx, packet)` queues a relay copy unless any of these hold: we are the
destination, we are the origin, the hop limit is spent, `is_rebroadcaster` says no (role or
rebroadcast mode), or the packet's `next_hop` names someone else.

Duplicate suppression is the packet history, so a second copy of a packet already in the ring reaches
`_handle_dupe` instead.

### 9.2 Hop limits

**Decrementing is not automatic.** `should_decrement_hop_limit` (2.7+, `preserve_hops`) makes a hop
free when *all* of: the packet has already been relayed at least once (the first hop always pays), we
are router-like, and the previous relayer resolves **uniquely** to a favourited router-like peer.
Before `resolve_ambiguity` (2.8) the resolution took the first match, so an ambiguous relay byte
could make a hop free through a node the operator never favourited.

**Hop upgrade** (2.7+): a duplicate arriving with a *higher* hop limit than the record's best means
the mesh has a better path than the one we relayed on, and the copy is worth relaying again.

**`hop_limit_for_response`** decides what a reply gets. `VARIABLE_HOP_PORTNUMS` - position, nodeinfo,
telemetry, neighborinfo - are the ones whose responses scale.

**`nohop_portnums`** is Portduino's `nohop_ports`: named portnums relayed at hop limit 0. Operator
configuration rather than a release feature, so no series turns it on.

### 9.3 Next-hop routing - `NextHopRouter`, 2.6+

A directed packet carries a `next_hop` byte. `NO_NEXT_HOP_PREFERENCE` (0) means flood. A node relays
a directed packet only if the byte is zero or names it.

**Learning** (2.7+, `next_hop_learning`) comes from the packet history's relayer list: seeing who
relayed a packet toward a destination is what teaches a next hop for it. **Traceroute learning**
(v2.7.13) is the other source - a reply teaches a next hop for every node beyond the learner in the
returned route. `traceroute_corroboration` (this tree) guards against learning from a single reply.

**Route health** (2.8, `RouteHealth`): a learned route not confirmed within `ROUTE_TTL_MSEC`
(30 minutes), or failing `ROUTE_FAILURE_THRESHOLD` (3) directed deliveries in a row, decays back to
flooding rather than being trusted on the next DM. `ROUTE_HEALTH_MAX` (32) bounds the table.

### 9.4 Reliable delivery - `NextHopRouter.h`

**Two budgets, not one**, both counting the first send:

| | attempts | from |
| --- | --- | --- |
| reliable broadcast | `NUM_RELIABLE_RETX` = 3 | every series |
| directed unicast | `NUM_RELIABLE_UNICAST_ATTEMPTS` = 5 | 2.8; earlier series use 3 |

`retransmission_msec` is `RadioInterface::getRetransmissionMsec`: twice the airtime, plus the worst
contention window, plus a responder's window at the midpoint of the CW range, plus
`PROCESSING_TIME_MSEC` (4500 ms) for constructing, processing and reconstructing a packet.

**On the last directed attempt the route is abandoned.** `_fall_back_to_flooding` records the failure,
clears the next hop in the packet *and* in the hot store *and* in the health table, and floods -
which is the only thing left that can still deliver.

Two behaviours behind flags no release sets: `early_flood_on_unverified` (M4, written and compiled
out at `NEXTHOP_EARLY_FLOOD_ON_UNVERIFIED 0`) starts flooding one retry sooner when the route was
never verified, and `coding_rate_ladder` (a branch) sends each retry at a higher coding rate, keyed by
`(from, id)` so every copy of one retransmission picks the same rate.

### 9.5 Duplicate cancellation

Hearing someone else relay a packet we have queued is a reason to drop ours - and **which nodes are
allowed to** changed at 2.7 (`role_aware_cancel`): a `ROUTER` or `ROUTER_LATE` never drops a queued
relay, because the role exists to be the copy that goes out, and a `CLIENT_BASE` keeps its copy only
for favourite traffic.

`ROUTER_LATE` does something different again:
`clamp_to_late_rebroadcast_window` (2.5+, v2.5.18) moves the queued copy to the **back** of its own
window rather than cancelling it. That is the whole definition of "late" - it relays where everyone
else has given up.

`RepeatScalingModule` (a branch, not a release) adds a *tolerance*: text tolerates one heard copy
before cancelling, other traffic none. `meshTooBusyForExtraRepeats` forces the tolerance to 1 on
three unvalidated constants - channel utilisation over 10%, own-TX over 4%, or more than 10 direct
active nodes - any one of which is enough.

### 9.6 Acknowledgement - `ReliableRouter::sendAckNak`

**Only the addressee answers.** `_perhaps_ack` fires at a packet's destination, never at a relay, and
the ACK is an ordinary packet on `ROUTING_PORTNUM` at `PRIORITY_ACK` with `request_id` set to the id
it acknowledges. A *response* - anything already carrying a `request_id` or `reply_id` - gets an ACK
at hop limit **0**, so an acknowledgement of an acknowledgement cannot flood.

`_sniff_ack_or_reply` is `NextHopRouter::sniffReceived`, and it does three different things depending
on where the ACK is seen:

- **At a relay that carried the original**, it *learns a route*, because a delivery that demonstrably
  worked names a working next hop. Two gates: the ACK must have carried the original (`request_id`
  matches a record in our history) and we must either have relayed it while its returning relayer
  also did, or be the sole relayer of a packet that arrived unrelayed. The relay byte must then
  resolve to exactly one node.
- **At the origin**, it refreshes the route's health, counts the delivery, and **stops the
  retransmission**. That is the point of having asked - and it is often already stopped, because
  overhearing our own packet relayed is an implicit ACK and usually beats the real one back.
- **At anyone else**, it cancels a queued relay of the acknowledged packet and stops any
  retransmission of it: the packet has arrived, so nothing more needs to carry it.

### 9.7 Traceroute - `TraceRouteModule`

`send_traceroute(src, dst)` starts a route discovery on `TRACEROUTE_PORTNUM`, whose payload is a
`RouteDiscovery`. Each relay appends itself (`_record_traceroute_hop`), and the destination replies.

**The reply is what teaches.** `updateNextHops` (v2.7.13) has every node in the returned route learn a
next hop for every node *beyond* it - one reply is worth a whole table of routes, which is why
traceroute is a route-learning mechanism and not only a diagnostic. A request on its way *out* teaches
nobody.

`traceroute_corroboration` (2.8, this tree only) requires the byte the reply arrived on to **be** the
next hop the route claims. Without it, a node adopts a route from a reply whose relay byte says the
packet came from somewhere else - the route is a claim about the path, and the relay byte is the only
evidence that the claim describes the copy in hand. `traceroute_uncorroborated` counts the refusals.

`_maybe_set_next_hop` writes to the hot store when it holds the target, and to the overflow route
cache (2.8) always - a full known route is the best source there is, so it is kept even for a node the
NodeDB has no record of.

### 9.8 Opaque relay - 2.8

A packet this node cannot decrypt never enters history, the NodeDB, or the app layer. The only thing
2.8 does with it is relay the outer header and let hop exhaustion bound it.

### 9.9 Signing - `config.security.packet_signature_policy`, 2.8

An XEdDSA signature is 64 bytes plus two for the protobuf field, so a Data payload signs only under
173 bytes - the gate `signed_data_fits()` applies. The policy is `COMPATIBLE`, `BALANCED` or `STRICT`
and **only affects what a node accepts, never what it sends**: a node signs whatever it can whichever
policy it runs.

A packet the policy refuses is neither delivered nor relayed - and deliberately **does not cancel a
queued rebroadcast** either. Cancelling would hand an attacker a way to silence a relay by sending an
unsigned copy.

---

## 10. Offered load, and the throttle the firmware puts on it

Traffic is not an input to the mesh - it is a schedule computed before the run and handed to it.
`sfpp/traffic.py`'s `Generator` draws **Poisson per class per node**, because synchronised senders
would understate collisions: a mesh where every node's position packet lands on the minute collides
far less than one where they drift.

`--diurnal` multiplies the rate by an hourly weight (the `commuter` shape is 17:1 peak to trough),
which is why a whole-run rate is a poor summary and the per-bin series exists.

### 10.1 The congestion throttle - `Default.h congestionScalingCoefficient`

This is the firmware's own answer to a crowded mesh: a **multiplier on every periodic broadcast
interval**, applied per node. Below the pivot - Default.h's literal `numOnlineNodes > 40` - every era
leaves the interval alone. Above it, three models, one per era, and `Profile.congestion_model` selects:

| model | series | coefficient above the pivot |
| --- | --- | --- |
| `flat` | 2.4 | `1 + (n - 40) * 0.075`, whatever the preset |
| `preset` | 2.5, 2.6 | a per-preset factor: 0.04 MEDIUM_SLOW down to 0.01 SHORT_SLOW, and **off entirely** for SHORT_FAST and SHORT_TURBO |
| `sf_bw` | 2.7, 2.8 | `1 + (n - 40) * 2^sf / (bw_khz * divisor)`, the divisor 100 normally and 25 in event mode |

Two details that change the answer and are reproduced rather than tidied:

- **2.5 through v2.7.16 *shorten* intervals on a small mesh** rather than leaving them alone - 0.6 at
  ten nodes or fewer, 0.7 at twenty, 0.8 at thirty. Removed in v2.7.17, so the `2.7` profile (which
  is v2.7.21) does not have it, and the `2.6` profile does.
- **`n` is what the node believes, not what is true.** `--congestion-input` selects it:

| input | `n` is | in firmware? |
| --- | --- | --- |
| `hotstore` (default) | `getNumOnlineMeshNodes()` - peers heard within `NUM_ONLINE_SECS` **and still in the hot store** | yes, this is what the firmware does |
| `truesize` | the mesh's actual node count | no - the unbounded ideal, as a comparison |
| `utilisation` | measured channel busy-ness, mapped onto the same 40-node pivot | **no** - a stated assumption, not a transcription |

  The difference between the first two is the point: a node whose NodeDB has saturated throttles as
  though the mesh were the size of its own memory. `congestion_pivot` is a knob rather than a constant
  because moving it is how the firmware's advice gets tested - `congestion-40` reproduces the baseline
  by construction, which is what makes the 60 and 80 cells readable.

`--congestion-mode` decides *when* the coefficient is computed: `adaptive` (the default, and what the
firmware does) recomputes it per node from that node's own online count at the moment it sends;
`static` applies one mesh-wide coefficient for the whole run. `congestion_clamp` (2.8) bounds the
result, and `--no-congestion-scaling` turns the whole thing off - the arm that says how much of a
large mesh's behaviour is the throttle rather than the radio.

## 11. Degradation: how a mesh is broken

Because what a mesh does when it breaks is the question, and a model that can only run intact meshes
cannot answer it.

**`take_down(index)` is not a deletion.** The node stops transmitting and stops hearing. Every other
node keeps its NodeDB record and keeps believing what it last learned, **including a next hop
pointing through the dead node**. Failure is not broadcast, so the gap between what the mesh believes
and what is true is exactly the thing being modelled.

**`bring_up` restores everything the node knew** - a node merely out of range loses nothing - and
**`wipe` covers the reboot case**, which loses far more.

**`sever(a, b)`** removes one link in both directions. **`partition(group)`** cuts a set off.
**`articulation_nodes()`** finds the nodes whose removal disconnects the mesh, and `break_mesh(mode)`
applies a named degradation. All of them scan **both directions**, because links are not reciprocal
and scanning outward only would leave every inbound-only link intact.

Two loss knobs stand in for what the model does not carry. `extra_loss` is a flat loss floor on every
reception - interference from outside the mesh, fading, a receiver busy elsewhere. `burst_loss` with
`burst_ms` is bursty deafness: a node periodically unable to receive for a stretch, standing in for a
blocked antenna, a neighbour keying up nearby, or a radio busy elsewhere. It is **redrawn once per
burst window, not per packet**, which is the whole difference between the two: flat loss spreads
divergence evenly across a set sketch's buckets, and a burst puts a whole bucket's worth into one.

---

## 12. What decides whether two runs are comparable

Five things, and getting any of them wrong produces a well-formed table supporting a conclusion that
is not there.

**`SIM_VERSION` on MAJOR.MINOR.** A MINOR bump means a behaviour changed and earlier results measure
something else. `explorer.comparable_runs` splits the archive on it, and the page names what it
excluded rather than silently dropping it (TRAPS 18).

**The seed, and only the seed.** Every hashed draw is keyed on `(seed, constant, window)` rather than
pulled from a sequential stream, so adding or removing a draw does not shift anything else, and a
paired before/after at one seed is a valid comparison. A no-scenario run being byte-identical at a
fixed seed is asserted on every push, and has proved a change inert four separate times.

**That both arms actually differ.** An arm whose cells are identical in every number the report
carries did nothing. That has happened twice, and both times the run produced a well-formed table
supporting the opposite of the truth - so `collate.py` compares *every* number in the report rather
than the ones the digest displays. `--noise-model fixed` became a copy of `thermal` this way when the
default it inherited moved (TRAPS 21).

**That the arm was defined at a parameter, not at a default.** Which is the same failure stated
before it happens.

**That the geometry is named.** `ground` is null on a flat run, which is the honest label for one:
every figure rests on the geometry, so a report that does not say which geometry cannot be compared
with one that does.

---

## 13. What is not here

Stated plainly, because the absence of a mechanism is a property of a result.

**No concurrency**, so no firmware race between interrupt contexts (§1).

**No second channel**, so no escape from contention by frequency, and no cross-preset mesh (§3.5).

**No mobility and no fast fading** (§3.5). The moving noise floor varies the threshold instead, which
is not the same thing.

**No link below sensitivity, at all.** Such a pair is not in `neighbours` and is never offered a
packet, so this model degrades a link and then deletes it rather than letting it deliver a third of the
time. Under the thermal floor a link *at* sensitivity does deliver 39% of the time, which is where the
marginal band comes from - but the cliff below it is absolute (§6.6).

**No client hydration path.** `held` and `union` are what an archive *has*. Nothing measures a user
asking a server for what they missed, so the only measured end-user gain from the archive is bystander
pickup. Every other metric is a delivery measurement; that one is inventory.

**No partial frame corruption.** A frame either holds the receiver for its whole duration or it does
not (§6.5).

**No `legacy` firmware.** The `legacy` profile is a *modelling* baseline, not a release. Five of its
behaviours were never any firmware's: no router offset, a continuous slot draw, a clamped contention
window, a router pinned to the bottom of its window, and a 400-backoff discard. It exists so runs
measured before the 2.8 fold-in still reproduce, and to price those mechanisms one at a time - not to
imitate anything shipped, and it must not be read as "2.7 and earlier". It reproduces *distributions*
rather than streams: the TX queue replaced a recursive retry closure, so a seed does not reproduce a
pre-fold-in run packet for packet.

**No ordering guarantee across a `SIM_VERSION` boundary.** Two runs at different MINOR versions
measured different things, and averaging across the boundary is the failure TRAPS 18 exists for.
