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
