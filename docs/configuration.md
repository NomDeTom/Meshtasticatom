# The optional models

`lib/config.py` is a flat list of settings. Most are self-explanatory; the ones below are policies
or physical models that are off by default, and this is where their reasoning lives so the config
file can stay a list of values.

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
link at the edge stops being all-or-nothing. `PHY_LOSS_SNR_P50_BY_CR` is where each rate's curve
sits; the long-packet penalty widens it for frames longer than the reference size.

## Link calibration (`LINK_CALIBRATION_*`, `REPORTED_SNR_*`, `PATH_LOSS_DISTANCE_FLOOR_M`)

All defaults preserve plain simulator behaviour. A packaged preset can tighten them to match
aggregate observations from a real mesh without changing generic runs - see
[batumi_radio_calibration.md](batumi_radio_calibration.md).

## Asymmetric links and movement

`MODEL_ASYMMETRIC_LINKS` adds a random offset to each direction of each link, so A hearing B does
not imply B hearing A. Movement moves a configurable share of nodes at walking, cycling or driving
speeds; `APPROX_RATIO_NODES_MOVING` and the GPS ratio decide how many, and how many of those report
position.
