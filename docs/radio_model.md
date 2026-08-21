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

`get_current_slot_time(conf)` is `RadioInterface::computeSlotTimeMsec`, unchanged between v2.7.15 and
2.8: CAD duration plus 0.2 ms propagation, 0.4 ms turnaround and 7 ms MAC processing, with the
2.4 GHz CAD term from AN1200.22 behind the region's `wide_lora` flag.

It takes the config rather than reading a module-level one. `lib/phy.py` used to bind
`lib.config.CONFIG` at import, so every MAC delay was scaled by a slot time belonging to whichever
config was bound last — and `sfpp.mesh.make_config` had to rebind that global to be heard at all,
which leaked a scenario's calibration into anything else running in the same process.

The 2.4 GHz CAD term is `(NUM_SYM_CAD_24GHZ + (2·SF + 3) / 32)`, and in the firmware that division
is **integer**: `sf` is a `uint8_t`, and `2·14 + 3` is 31, so the second term is 0 for every legal
spreading factor. Transcribed into Python it became true division, which made the 2.4 GHz slot time
13% long at SF7 and 21% at SF12.

## Interference

`INTERFERENCE_LEVEL` is the long-run share of time a foreign, non-Meshtastic transmitter holds a
node's channel. It is one occupancy seen from two ends, not two draws: `lib/interference.py` builds a
schedule of busy stretches per node — an alternating renewal process whose busy share is the level
exactly at every value including both endpoints, with a holding time defaulting to one full frame on
the configured preset.

The same schedule answers both questions a run asks of it. `is_channel_active` asks whether the band
is busy *now*, which is what CAD detects. A reception asks whether a busy stretch overlapped
*destructively* — landing on the preamble, or covering enough payload to exhaust the coding gain,
which are the two conditions the capture model already applies to a Meshtastic interferer. Charging
any overlap at all would make a millisecond of foreign air worth more than a full co-channel frame.

One schedule **per node**, because interference is local: the noise at a receiver is what destroys a
frame and the noise at a transmitter is what its CAD detects, and on a mesh spanning kilometres those
are different conditions.

Two defects preceded this. Until 2026-08 both call sites drew `random.randrange(10) <= level * 10`.
Both ends of that comparison are inclusive, so the level was quantized to tenths and floored at one:

| configured | drawn |
| --: | --: |
| 0.00 | 0.10 |
| 0.05 | 0.10 |
| 0.10 | 0.20 |
| 0.50 | 0.60 |

The floor is the part that mattered. `is_channel_active` is not gated by any flag, so every default
run — including every run configured with interference explicitly disabled — deferred about a tenth of
its transmissions to a channel that nothing was using.

Replacing that with a continuous draw fixed the endpoints and left a deeper problem: an independent
draw at each point of use is a probability with no holding time. A transmitter re-rolling its CAD
found the channel clear within a few attempts however high the level, so interference could delay a
transmission but never block one. And the two ends drew separately, so a transmitter could see clear
air while, in the same instant, its frame was destroyed at a receiver by interference that was not a
property of anything. The reception half was also behind a `COLLISION_DUE_TO_INTERFERENCE` flag,
off by default, so the shipped configuration had a channel busy enough to wait for and never busy
enough to break anything. That flag is gone: one occupancy, both ends.

The default level of 0.05 now costs what it says. A LONG_FAST frame is 682 ms, so a 5% duty cycle of
foreign traffic with comparable frames touches roughly a tenth of receptions.

The level is validated as a probability in [0, 1] when set, so a level outside that range fails at
configuration rather than silently saturating.

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

Two models, selected by `CAPTURE_COLLISION_MODEL_ENABLED`. The legacy one is the default: a timing
overlap on the same SF and frequency destroys the weaker packet unless the two are more than 6 dB
apart.

"Timing overlap" means the fresh packet's acquisition window does not clear the older packet's last
byte. That window is `preamble_lock_window_ms` — `NPREAM − 5` symbols, 90.1 ms on LONG_FAST — and it
is the same window the capture model uses. `timing_collision` used to compute it inline as
`2^SF / BW · (NPREAM − 5)`, which is **seconds** because `bw` is in Hz, and compare it against
`env.now` and `endTime`, which are milliseconds. The 90.1 ms window read as 0.09 ms, so the rule was
inert and every overlap counted as a collision — 9–13% of overlapping arrivals across the presets,
each of which also stopped being an interferer for later packets, because a collided packet is not
appended to `packetsAtN` in the legacy path.

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

Seven models, chosen by `MODEL` or by name through `--path-loss-model`. All take distance in metres
and frequency in MHz and return loss in dB. `lib.phy.PATH_LOSS_MODELS` is the mapping, and
`loraMesh.py --list-path-loss-models` prints it with the current default marked.

| name | `MODEL` | |
| --- | --- | --- |
| `log-distance` | 0 | |
| `hata-small-city` | 1 | Okumura-Hata, small and medium cities |
| `hata-metro` | 2 | Okumura-Hata, metropolitan |
| `hata-suburban` | 3 | Okumura-Hata, suburban |
| `hata-rural` | 4 | Okumura-Hata, rural |
| `3gpp-suburban` | 5 | **default** |
| `3gpp-urban` | 6 | |

A name resolves to exactly the integer the dispatch has always read, so naming one changes nothing
about what it computes. An unknown name raises rather than falling back to the default - a typo that
silently selected model 5 would turn a comparison arm into a duplicate of it.

Distance is floored at `PATH_LOSS_DISTANCE_FLOOR_M` before the logarithm. Randomized movement can
put two nodes on the same point, and a preset can raise the floor further as a near-field
calibration: the Hata and 3GPP formulas are not meaningful at apartment scale, and map positions are
coarse enough that two pins being close does not mean two antennas have 20 m of clear air.

**Free space is the floor under every model.** Each of the seven is an empirical fit with a validity
range — Okumura-Hata wants a base station 30–200 m up and a mobile 1–10 m up — and this simulator
passes antenna height above local ground for *both*, usually 1.5 m. Asked far enough outside that
range the 3GPP form's linear height terms dominate and it returns a negative loss, i.e. gain: 900 m of
antenna height on a 60 km path produced **+2173 dBm** of RSSI. `free_space_path_loss()` bounds it. The
bound is inert at the defaults, where every model is far above free space, and it catches the whole
class.

A consequence worth stating plainly: at `MODEL = 5` with 1.5 m antennas at both ends the exponent is
4.49, and the raw budget produces **no link past about a kilometre** on real geometry. That is why
the packaged Batumi scenario's fitted calibration is a replacement rather than a correction — see
[batumi_radio_calibration.md](batumi_radio_calibration.md).

## The noise floor, and the threshold derived from it

The thermal floor is theory. kTB plus a receiver's noise figure is what a band would be with nothing
in it — a lower bound, not a description — and a real receiver sits in whatever the band is doing.
So `NOISE_LEVEL` is a **median**, and `NOISE_SIGMA_DB` gives it spread, correlated over
`NOISE_TAU_MSEC` so the band drifts rather than flickering per packet, clamped below by kTB. Spread
is 0 by default. `lib/noise.py` hashes values on `(seed, bucket)` rather than drawing from a stream,
so a query cannot shift anything else in a run.

`NOISE_LEVEL` defaults to `thermal_noise_floor(bw)` for the preset in use, which is kTB + 6 dB. It
was one constant of −119.25 dBm for bandwidths spanning 15.6 kHz to 500 kHz — a 15 dB range in
thermal noise — and that constant implies a **0.8 dB noise figure** at 250 kHz, so it was a figure
back-derived from the sensitivity table rather than a band. A scenario that measured its own floor
sets it explicitly.

**A preset's sensitivity cannot outlive its noise floor.** Each entry in the preset table is kTB for
its bandwidth, plus the noise figure, plus the modem's required SNR — checked against the SX1262
per-spreading-factor table, and every row is internally consistent at a 6 dB noise figure. So the
sensitivity is a statement *about* a thermal floor, and keeping it while raising the floor says the
modem decodes below its own limit. `effective_sensitivity(conf, preset, noise_dbm)` takes whichever
threshold is harder — the datasheet figure, or the band the receiver is in plus
`required_snr_db(sf)` — and `effective_cad_threshold` keeps the preset table's own margin below it.

Under the packaged Batumi median of −110.5 dBm that tightens LONG_FAST from −131.5 to −128.0 dBm.
With spread configured, the same link is above threshold in a quiet band and below it in a noisy one,
instead of being decided once:

| the band | LONG_FAST threshold |
| --- | --: |
| quiet, −120 dBm | −131.5 — the datasheet figure binds |
| Batumi median, −110.5 dBm | −128.0 |
| noisy, −104 dBm | −121.5 |

## Payload loss

`PHY_LOSS_MODEL_ENABLED` adds a decode probability to a frame that was heard: a logistic curve in
SNR whose half-way point is `required_snr_db(sf) + PHY_LOSS_P50_OFFSET_DB_BY_CR[cr]`.

The offset is from the **modem's own demodulation limit**, not an absolute SNR. It was an absolute
figure per coding rate — −17.0 dB for 4/5 and so on — but a curve's position is set by the spreading
factor, which moves the limit 12.5 dB across the presets, while the coding rate only modulates it. So
the model sat 10 dB clear of the edge on SHORT_TURBO and right on it at LONG_FAST: nearly inert on
the fast presets, severe on the slow ones, and a preset sweep with `--phy-loss-model` measured that
rather than the presets. The offsets reproduce the old absolute figures exactly at LONG_FAST, which is
where they were tuned.

One draw per (packet, receiver) is taken at construction and reused when the coding rate or transmit
power changes, so a DCR or DTP comparison is paired rather than resampled.
