# The models behind the settings

`lib/config.py` is a flat list of settings. Most are self-explanatory; the ones below are policies
or physical models whose reasoning does not fit on the line beside the value, and this is where it
lives so the config file can stay a list of values.

The first group is **on by default**, because each one is firmware behaviour the simulator was
missing rather than a proposal: leaving it off would model a device that does not exist. The second
group is **off by default**, and an unchanged config runs as though it were not there.

# On by default

## Reliable-send budgets (`RELIABLE_BROADCAST_ATTEMPTS`, `RELIABLE_UNICAST_ATTEMPTS`)

`NextHopRouter.h` carries two figures, not one: `NUM_RELIABLE_RETX` (3) for a reliable broadcast and
`NUM_RELIABLE_UNICAST_ATTEMPTS` (5) for an acknowledged unicast sent by the originator. Both count
the first send. `MeshPacket.reliable_attempts(conf, destId)` picks between them by destination, so a
broadcast gets two retries and a DM four - the simulator used to give both the same number, which
made DM delivery pessimistic and flood retransmission optimistic at the same time.

## The channel-utilisation transmit gate (`CHANNEL_UTIL_TX_*`)

`AirTime::isTxAllowedChannelUtil` refuses to originate periodic traffic when the 60-second channel
utilisation is over 40%, or over 25% for the polite callers - which is every role but TRACKER and
SENSOR. This is the mesh's main self-regulation, and without it a congestion sweep measures a
network that keeps offering the same load however busy the air gets.

The gate **defers, it does not drop.** `PositionModule` returns `RUNONCE_INTERVAL` before it
updates `lastGpsSend`, so the message it was about to send is still owed and is attempted again
`CHANNEL_UTIL_TX_RETRY_MSEC` (5000 ms) later. A node here waits in the same loop and only abandons
the message if the simulation ends first, which the results report separately as
`channelUtilDropped` alongside `channelUtilDeferred`. Relays and ACKs are not gated at all, because
the firmware puts the check in the modules that originate rather than in `Router`.

## Bounded duplicate suppression (`PACKET_HISTORY_MAX`)

`PacketHistory` is bounded by **capacity only** - `max(MAX_NUM_NODES * 2, 100)`, so 240 on the
nRF52840 and generic ESP32 builds - and it evicts the oldest slot when full. There is no time
expiry. The simulator kept an unbounded dict, so a node suppressed a duplicate of a message it had
heard an hour earlier where a device would long since have forgotten it.

## The noise floor and the thresholds derived from it (`NOISE_LEVEL`, `NOISE_SIGMA_DB`, `NOISE_TAU_MSEC`)

`NOISE_LEVEL` is a **median**, and by default it is derived from the preset's own bandwidth as
kTB + 6 dB noise figure rather than being one constant for every preset. See
[radio_model.md](radio_model.md) for why a single constant misstated SNR by up to 8 dB across the
preset range, and for how `effective_sensitivity` keeps a sensitivity and the floor it was measured
against from being combined into a link that could not exist.

`NOISE_SIGMA_DB` gives the floor the spread a real one has, correlated over `NOISE_TAU_MSEC` so the
band drifts across minutes instead of flickering per packet, and clamped below by kTB because
nothing sits under thermal noise. The default sigma is zero, which reproduces a constant floor
exactly, so no existing result moves until a scenario asks for the variation. `lib/noise.py` rejects
a `tau` under 10 s outright: a floor that decorrelates faster than a message exchange is not a
noise floor, it is per-packet noise wearing one's name.

## Foreign channel occupancy (`INTERFERENCE_LEVEL`, `INTERFERENCE_MEAN_BUSY_MS`)

One occupancy schedule per node, an alternating renewal process with `INTERFERENCE_LEVEL` as its
long-run busy share and `INTERFERENCE_MEAN_BUSY_MS` as the mean length of one busy stretch (`None`
derives it from a full frame on the configured preset, a foreign LoRa packet being the likeliest
occupant of a LoRa channel). The same schedule both defers this node's CAD and jams frames arriving
at it, because those are the same occupancy seen from the two ends. It used to be two independent
draws - an ungated one for CAD and `COLLISION_DUE_TO_INTERFERENCE` for reception - which described a
channel busy enough to wait for but never busy enough to break anything.

# Off by default

## Dynamic coding rate (`DCR_*`)

Off by default, so an unchanged config keeps the preset's coding rate for every packet. **No
released firmware has this** - it is a proposal this simulator exists to evaluate.

When enabled, a node picks a coding rate between 4/5 and 4/8 per packet immediately before
transmit, after queueing and listen-before-talk have settled, which is the last moment the decision
can be made on current channel conditions. With the default PHY model this is an
airtime-and-contention study; with `PHY_LOSS_MODEL_ENABLED` the chosen rate also moves the payload
decode probability near weak links.

`DCR_CR8_AIRTIME_LIMIT_PERCENT` caps non-urgent 4/8 traffic as a share of the node's own transmit
airtime. It is a mesh-behaviour rail, not a regulatory one: `_selected_region_duty_limit()` in
`lib/dcr.py` compares against a region's duty cycle only where that region has one.

The `DCR_*_UTIL_PERCENT` and `DCR_*_QUEUE_DEPTH` thresholds classify local channel pressure. They
are deliberately local observations, not regulatory limits.

### How a coding rate gets chosen

`lib/dcr.py` scores each packet and each moment, and the two together pick a rate:

- **First attempts stay compact.** Idle air is reserve, not permission to fatten every flood; in a
  dense public-mesh run that would just spend the quiet.
- **Retries are where robustness is spent.** A normal retry moves generic user traffic to 4/6, and
  a final retry after quiet loss can reach 4/8 when the airtime budget allows.
- **Header context counts.** A packet addressed directly and already relayed once is real
  header-level evidence of a link worth protecting, so it avoids the thinnest rate when local air
  is not busy.
- **ACKs are the only control class visible.** Simulated traffic carries no portnums or app
  priorities, so packet classification is coarser here than the firmware's would be.

## Dynamic transmit power (`DTP_*`)

Off by default, and also in no released firmware. It only ever *lowers* power: `PTX` stays the
ceiling, and DTP reduces individual relay and control packets to shrink their interference radius
in dense capture-collision experiments. It is not a way to exceed a region's limit.

## Terrain (`TERRAIN_*`)

Off by default. When enabled, `TERRAIN_GRID` holds a grid sampled from SRTM HGT tiles, and path loss
gains a diffraction term over the profile between two nodes.

`NODE_Z_REFERENCE` decides what a node's `z` means: `"ground"` is antenna height above local ground,
`"sea_level"` is absolute altitude with ground elevation already included.

`TERRAIN_EFFECTIVE_EARTH_RADIUS_MULTIPLIER` is the 4/3 earth-radius approximation from radio
planning, used as an earth-bulge term so long coastal and ridge links do not come out
unrealistically flat.

## Land-cover clutter (`CLUTTER_*`)

Off by default, and deliberately separate from terrain: a hill can be visible over open ground while
low urban fabric still blocks a balcony-to-balcony link at the same distance. The per-kilometre
figures are excess loss by land-cover class, with endpoint terms for the last few metres at each
end and discounts for high vantage points and coastal paths.

## Empirical payload loss (`PHY_LOSS_*`)

Off by default. RSSI against sensitivity still decides whether a packet can be heard at all; this
model only adds a smooth, coding-rate-dependent payload-success probability after that gate, so a
link at the edge stops being all-or-nothing. Each rate's curve is anchored to the
modem's own requirement: the midpoint is `required_snr_db(sf)` for the configured spreading factor
plus `PHY_LOSS_P50_OFFSET_DB_BY_CR[cr]`, the few tenths of a decibel the coding rate is worth. It
used to be an absolute SNR per coding rate, which meant the curve sat 12.5 dB from the demodulator
limit at SF7 and on top of it at SF12. The long-packet penalty widens it for frames longer than the
reference size.

## Link calibration (`LINK_CALIBRATION_*`, `REPORTED_SNR_*`, `PATH_LOSS_DISTANCE_FLOOR_M`)

All defaults preserve plain simulator behaviour. A packaged preset can tighten them to match
aggregate observations from a real mesh without changing generic runs - see
[batumi_radio_calibration.md](batumi_radio_calibration.md).

`LINK_CALIBRATION_MAX_M` is how far the fit has support. A linear model asked about a path three
times longer than anything it was fitted on answers confidently and wrongly, so past this distance
the raw link budget answers instead and `LinkBudget.calibration_applied` reports which of the two
did. `None` means no envelope is known, which is not the same as the fit being valid everywhere.

The calibration is also applied at a **reference EIRP** - `PTX + 2 * GL` - and the difference
between the actual EIRP and that reference is added back afterwards. A fit made at one power level
otherwise silently absorbed the power level, so changing `PTX` or an antenna gain moved nothing.

## Asymmetric links and movement

`MODEL_ASYMMETRIC_LINKS` splits link variation into the two things that cause it.
`MODEL_SHADOWING_STDDEV` is **shadowing**, a property of the path: one draw per unordered pair, the
same in both directions, because the buildings and trees between A and B do not rearrange
themselves depending on who is talking. `MODEL_RADIO_ASYMMETRY_STDDEV` is the **radio**, a property
of the endpoint: a per-node transmit offset and a per-node receive offset for its power amplifier,
antenna match and front end. The two together mean A hearing B does not imply B hearing A, while
the asymmetry stays a few decibels rather than the ~8.5 dB standard deviation two independent
per-direction draws produced.

Movement moves a configurable share of nodes at walking, cycling or driving speeds;
`APPROX_RATIO_NODES_MOVING` and the GPS ratio decide how many, and how many of those report
position. Each node's movement and traffic draws come from its own seeded generator
(`f"{SEED}:{nodeid}:move"`), so a run is reproducible independently of the order SimPy happens to
schedule nodes in.
