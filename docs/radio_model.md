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
