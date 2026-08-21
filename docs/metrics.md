# What a run counts

Nine counters over populations that are deliberately not interchangeable. A report that mixes any
two of them produces a rate with no stable meaning - which is what "reach" and "usefulness" used to
be.

| key | population | counts |
| --- | --- | --- |
| `appMessages` | application messages | distinct packet ids that are not ACKs |
| `ackMessages` | ACKs | distinct packet ids that are |
| `uniquePacketIds` | mesh packet ids | both of the above |
| `transmissions` | physical transmissions | every frame put on the air, `sent` |
| `rebroadcasts` | relayed copies | transmissions whose sender is not the origin |
| `retransmissions` | repeats by the origin | the origin sending an id it already sent |
| `receiverOpportunities` | addressed receivers | per transmission: N−1 broadcast, 1 unicast |
| `appReceiverOpportunities` | addressed receivers, messages only | the same, once per message, ACKs excluded |
| `uniqueAppDeliveries` | successful deliveries | first arrival of a message at a node it addressed |

## Reach

```
nodeReach = uniqueAppDeliveries / appReceiverOpportunities
```

Both halves are application traffic addressed to a specific set of nodes. A broadcast addresses
every other node, a DM addresses one, and an ACK addresses nobody the statistic cares about.

It used to be `nrUseful / (messageSeq · (N−1))`, where `nrUseful` counted the first arrival of *any*
packet including ACKs, and `messageSeq` was a shared counter incremented for messages and generated
ACKs alike. So an ACK - unicast, one addressee - added `N−1` to the denominator, and the numerator
counted every node that happened to overhear it.

On a broadcast-only run the two definitions agree exactly, which is why the default scenario did
not move when this changed. They diverge as soon as ACKs or DMs exist, and the old one is not
bounded: measured on an 8-node DM run, the old expression gives 51.65% and the corrected one 46.3%,
and a numerator counting overheard unicasts can exceed its denominator outright.

## Usefulness

```
usefulness = nrUseful / nrReceived
```

The fraction of receptions that carried something the receiver had not already seen. This one is a
ratio of two like things - receptions - so it keeps counting every packet, ACKs included.

## Packet ids

`packetIdSeq` allocates ids for messages and ACKs from one sequence, because a reply is matched to
its request by id and those have to be unique across the run. `packetIdsIssued` reports its final
value. It is an allocator, not a message count: `appMessages` is the message count.

## Channel occupancy

Two figures, because `AirTime` keeps two windows and they answer different questions.

| key | window | measures |
| --- | --- | --- |
| `nodeChannelUtilPercent` | 6 × 10 s = 60 s | all air this node could hear, its own transmissions included |
| `nodeUtilizationTxPercent` | 60 × 1 min = 1 hour | only this node's own transmissions, which is what a duty cycle binds |

`nodeChannelUtilPercent` reports `mean`, `p90` and `max` across nodes; `nodeUtilizationTxPercent`
reports `mean` and `max`. Both are per-node observations aggregated at the end of the run, not a
mesh-wide average of air time - two nodes out of earshot of each other genuinely see different
channels, and collapsing them to one number hides exactly the contention a congestion study is
looking for.

A channel cannot be busy more than all the time. Reporting these makes that invariant assertable,
which matters because the figure that used to drive the contention window reached 117.5%: it charged
each overlapping reception separately instead of charging the union of the busy intervals.

## What the transmit gate did

| key | counts |
| --- | --- |
| `channelUtilDeferred` | messages that waited for the gate at least once before going out |
| `channelUtilDeferralMsec` | total time spent waiting, summed over all of them |
| `meanChannelUtilDeferralMsec` | the quotient of the two, or 0 when nothing deferred |
| `channelUtilDropped` | messages whose channel never cleared before the run ended |

The headline figure is the **deferral**, not the drop, because the firmware defers: `PositionModule`
returns `RUNONCE_INTERVAL` without updating `lastGpsSend`, so the send is still owed. `channelUtilDropped`
is an artefact of a finite run - a message still waiting when `SIMTIME` arrives has to be counted
somewhere - and a run where it is a large share of offered load is a run that is too short for the
congestion it created, not a mesh that lost those messages.
