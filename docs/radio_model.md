# The radio model

What `lib/phy.py` computes, what firmware it is copied from, and the vectors that hold it in place.
Companion to [radio_physics_quickstart.md](radio_physics_quickstart.md), which is the operator's
view; this is the derivation.

## Time on air

`airtime(conf, sf, cr, pl, bw)` returns milliseconds for one frame, from the Semtech payload-symbol
formula:

```
Tsym       = 2^SF / BW
Tpreamble  = (NPREAM + 4.25) · Tsym
nPayload   = 8 + max(ceil((8·PL − 4·SF + 28 + 16·CRC − 20·IH) / (4·(SF − 2·DE))) · CR, 0)
airtime    = Tpreamble + nPayload · Tsym
```

### CR is a denominator, not an index

The multiplier `CR` in that formula is the coding-rate **denominator**: 5 for 4/5, 8 for 4/8. The
literature often writes the same expression as `(CR + 4)` with `CR` an index 1..4, which is the same
number reached from the other side. Mixing the two conventions inflates every airtime.

The simulator stores the denominator, because the firmware does:
`RadioLibInterface.h` builds `DataRate_t` with `.codingRate = cr` where `cr` is 5..8, and its
comment on a received frame — "Go from raw header value to denominator" — is explicit that
`calculateTimeOnAir()` multiplies by the denominator. So `airtime()` multiplies by `cr` directly.

Until 2026-08 it multiplied by `cr + 4` against that stored denominator, inflating every preset:

| preset | as it was | correct | error |
| --- | --: | --: | --: |
| SHORT_TURBO | 46.4 ms | 29.0 ms | +60% |
| SHORT_FAST | 92.8 ms | 58.0 ms | +60% |
| MEDIUM_FAST | 297.5 ms | 191.0 ms | +56% |
| LONG_FAST | 1042.4 ms | 682.0 ms | +53% |
| LONG_MODERATE | 3018.8 ms | 2166.8 ms | +39% |
| LONG_SLOW | 5644.3 ms | 4071.4 ms | +39% |

(40-byte payload, 16-byte header, 16 preamble symbols.)

### Low data rate optimization

LDRO is gated on **symbol time**, not on a bandwidth. `RadioLibInterface.h`:

```cpp
// We use auto LDRO, meaning it is enabled if the symbol time is >= 16msec
.ldrOptimize = (1 << sf) / bw >= 16
```

so `DE = 1` whenever `2^SF / BW ≥ 16 ms`. That covers SF11/BW125 (16.4 ms), SF12/BW125 (32.8 ms),
SF12/BW250 (16.4 ms) and SF12/BW62.5 (65.5 ms). The simulator previously tested `bw == 125e3 and sf
in (11, 12)`, which missed VERY_LONG_SLOW — SF12 at 62.5 kHz, the preset with by far the longest
symbol, was the one running without the optimization the radio would have applied.

### Reference vectors

`tests/test_phy_airtime.py` anchors the formula on published LoRaWAN airtimes, computed with 8
preamble symbols and no Meshtastic header so they can be compared against any external calculator:

| SF | BW | CR | payload | airtime |
| --: | --: | --: | --: | --: |
| 7 | 125 kHz | 4/5 | 13 B | 46.336 ms |
| 12 | 125 kHz | 4/5 | 13 B | 1155.072 ms |
| 12 | 125 kHz | 4/5 | 64 B | 2793.0 ms |

The same file locks all ten Meshtastic presets at a 40-byte payload, so a change to the formula has
to be deliberate. A full 237-byte payload is 14.3 s on LONG_SLOW and 28.6 s on VERY_LONG_SLOW.

## Slot time

`get_current_slot_time()` is `RadioInterface::computeSlotTimeMsec`, unchanged between v2.7.15 and
2.8: CAD duration plus 0.2 ms propagation, 0.4 ms turnaround and 7 ms MAC processing, with the
2.4 GHz CAD term from AN1200.22 behind the region's `wide_lora` flag.

## Interference

`INTERFERENCE_LEVEL` is the probability that the channel is already carrying non-Meshtastic traffic
at any instant. It is drawn continuously - `random.random() < level` - in two places: `is_channel_active`,
which is the CAD check every transmitter runs before it keys up, and `check_collision`, which is
gated behind `COLLISION_DUE_TO_INTERFERENCE` and off by default.

Until 2026-08 both drew `random.randrange(10) <= level * 10`. Both ends of that comparison are
inclusive, so the level was quantized to tenths and floored at one:

| configured | drawn |
| --: | --: |
| 0.00 | 0.10 |
| 0.05 | 0.10 |
| 0.10 | 0.20 |
| 0.50 | 0.60 |

The floor is the part that mattered. `is_channel_active` is not gated by any flag, so every default
run - including every run configured with interference explicitly disabled - deferred about a tenth
of its transmissions to a channel that nothing was using. The level is now validated as a
probability in [0, 1] when set, so a level outside that range fails at configuration rather than
silently saturating.

## Contention window

`set_transmit_delay` follows `RadioLibInterface::setTransmitDelay`: a node that heard the packet it
is rebroadcasting draws an SNR-weighted delay, and a node that did not draws on channel utilization
instead.

The draws are half-open, because the firmware's are. Arduino `random(0, n)` returns 0..n-1, so a
router waits at most `2·CWsize − 1` slots and a client at most `2^CWsize − 1` past the router
window. The window itself is `2 · CWmax · slotTime`, which is what keeps the two roles from
overlapping: the latest a router can transmit is strictly before the earliest a client can.

`CWmin = 3`, `CWmax = 8`, and `getCWsize` maps a reported SNR of -20..10 dB onto that range. Both
constants and the mapping are unchanged between v2.7.15 and 2.8.

## Regions and frequency slots

The region list, the region profiles and the modem preset table in `lib/config.py` are pinned to
firmware 2.8.0 (`version.properties`), commit `51eadb7`. That pin is checkable rather than
decorative: 2.8 removed `UA_868` and added `EU_866`, `EU_N_868` and seven ITU ham regions, so the
set of region names dates the table on its own.

A frequency comes out of four things, following `RadioInterface::applyModemConfig`:

```
slotWidth = spacing + 2·padding + bandwidth
slots     = round((freqEnd − freqStart + spacing) / slotWidth)
slot      = overrideSlot − 1, or hash(preset display name) mod slots
freq      = freqStart + bandwidth/2 + padding + slot · slotWidth
```

`CHANNEL_NUM` is 1-based, as the firmware's `loraConfig.channel_num` is, and 0 means "not set" -
which takes the region default rather than the bottom of the band. A slot past the end of the band
is rejected instead of silently landing outside it.

The half-bandwidth centre offset is what the previous calculation omitted. It put every region half
a channel low: US LongFast came out at 908.75 MHz where a real device sits at **906.875 MHz**, and
EU_868 at 876.15 MHz, which is outside its own 869.4-869.65 MHz band entirely.

Presets are region-scoped. A region's profile carries the list its firmware will accept, so
requesting SHORT_TURBO on EU_868 raises rather than simulating a configuration no device can hold.
2.8 also added seven presets the table did not have - MEDIUM_TURBO, the LITE pair, the NARROW pair
and the TINY pair - and two of those are region defaults: EU_866 comes up on LITE_FAST and EU_N_868
on NARROW_SLOW.

## Early rebroadcast

`lib/mac.py` gives the early window to ROUTER alone, which is 2.8's
`shouldRebroadcastEarlyLikeRouter`. At v2.7.15 a CLIENT_BASE node also took it, for traffic to or
from a favourited node; that was removed in 2.8. The code was already 2.8's behaviour while the
file's comment named the older tag - one reason the pin moved rather than the code.

## The collision model

Two models, selected by `CAPTURE_COLLISION_MODEL_ENABLED`. The legacy one is the default and is
preserved unchanged: any timing overlap on the same SF and frequency destroys the weaker packet
unless the two are more than 6 dB apart.

The capture-aware model encodes the two effects the binary one misses, and are what matter on a
crowded mesh:

- **Capture.** A packet at least `COLLISION_CAPTURE_THRESHOLD_DB` stronger than the interferer at
  that receiver survives, because the demodulator stays locked to it.
- **The lock window.** Overlap during the preamble and header destroys the packet regardless of
  margin - that is where acquisition happens. Overlap confined to a short tail of the payload,
  under `COLLISION_PAYLOAD_OVERLAP_LOSS_FRACTION`, is tolerated.

It is a compact model, not a chip-level demodulator.

A packet below the receiver's demodulation threshold still counts as interference energy - it can
jam a stronger packet - but is not counted as a *collision*, because it was never going to be
decoded. Counting it would inflate the collision rate with packets that failed for a different
reason.

Frequency separation is compared in kHz. Packet frequencies are stored in Hz here; the comparison
normalizes both Hz- and MHz-scale inputs so that the predicate does not depend on caller units.

## Path loss

Seven models, chosen by `MODEL`: log-distance (0), Okumura-Hata for four environment classes (1-4),
and 3GPP suburban and urban macro (5-6). All take distance in metres and frequency in MHz and
return loss in dB.

Distance is floored at `PATH_LOSS_DISTANCE_FLOOR_M` before the logarithm. Randomized movement can
put two nodes on the same point, and a preset can raise the floor further as a near-field
calibration: the Hata and 3GPP formulas are not meaningful at apartment scale, and map positions are
coarse enough that two pins being close does not mean two antennas have 20 m of clear air.
