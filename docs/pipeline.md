# The pipeline: what a run is assembled from, stage by stage

Every result this tree produces is a path through eight stages, numbered from zero because stage 0
usually happened before you arrived — and is the one you cannot redo from a flag. At each stage there
is a choice, and the choices are not equivalent: some are measurements, some are models, some are
theory, and one is a proposal no firmware ships. A number is only as good as the weakest stage behind it, so the point
of this document is to make the path explicit — what you picked, what it cost you, and what a reader
of the result must be told.

Read it as a decision tree. `docs/radio_model.md` and `docs/configuration.md` give the physics of
individual stages; `sfpp/README.md` §10 lists what no path can answer.

**Notation.** Flags are `sfpp.campaign`'s unless marked *(event sim)*, meaning `loraMesh.py` /
`batchSim.py`. The two simulators share stages 2–4 and diverge at stage 5.

---

## Stage 0 — Capturing a network in the first place

Stage 1a *uses* a captured mesh. This stage is how one comes to exist, and it matters because
"captured from a real mesh" is not one act. Batumi — the only real snapshot here — is **five separate
captures with five different evidential characters**, stored together in `presets/batumi.yaml` and
two CSVs beside it. Conflating them is how a result inherits confidence it has not earned.

`--scenario map --bbox …` performs 0a–0c live, at run time, for any footprint. The packaged preset is
those same steps run once and frozen, plus 0d and 0e, which have no live equivalent.

### 0a. Node positions and configuration — observed

92 nodes under `nodes:`, on 55 unique coordinates. Each carries `x`/`y` in metres from a stated
`origin` (41.6442879, 41.61536), `z` (almost all 1.5 m), `isRouter` / `isRepeater` / `isClientMute`,
`hopLimit`, `antennaGain`, `neighborInfo`.

Steps: read the public map or a device NodeDB → project lat/lon to local metres about the origin →
carry roles and hop limits **as configured by their operators**, which is why `--router-fraction` is
ignored for a preset.

Evidential character: **strong for geometry, and it is a snapshot.** 92 nodes on 55 coordinates means
many share a pin — a rooftop, a hackerspace, coarse map rounding. Positions are as accurate as
whatever each node reported.

### 0b. Ground elevation — measured, resampled

`presets/batumi_terrain.csv`: `x_m,y_m,lat,lon,elevation_m` on a regular grid.

Steps: `tools/`-side SRTM fetch over the bbox → sample onto the scenario's local grid → write the CSV
so a run needs no network. `--offline` forbids fetching entirely.

Evidential character: **strong.** SRTM is real survey data. The resampling step and the grid pitch
are the only modelling in it.

### 0c. Land cover — exported, and this one is flagged

`presets/batumi_clutter.csv`: `x_m,y_m,lat,lon,clutter_class` on a 500 m grid, 4320 cells.

Steps: OSM extract → `tools/osm_to_clutter_csv.py` → per-cell class.

Evidential character: **weakest of the five, and the preset says so itself.** `clutter_provenance`
records `exporter: "pre-coastline"` and **`regenerate_required: true`**, with a class histogram of
open 3101 / urban 1209 / forest 5 / water 5. Five water cells for a Black Sea coastal city is not
plausible, which is the point of recording it: `tests/test_presets.py` asserts the flag against the
histogram, so the caveat cannot quietly fall out of the file. The fitted model's `water_fraction` and
`forest_fraction` coefficients are both exactly `0.0` — those classes carried no signal to fit.

This is the residue of TRAPS 23: `open` was the exporter's word for "not mapped", and three separate
pieces of code read it as "mapped, and empty."

### 0d. Observed link reports — observed, and sparse

296 entries under `calibration_observations`, each `{from, to, snr}`. Lengths from under a metre
(co-located pins) to **23,225 m**, median 5.2 km, SNR −20.75 to +6.75 dB, mean −9.53.

Steps: collect per-pair SNR reports from the live mesh → keep the directed pairs → record the longest
observed link as the fit's envelope, **derived rather than declared**, so it cannot disagree with the
data.

Evidential character: **strong per observation, thin as a set.** 296 observations against 2190
audible pairs. `observations_above_free_space` is 0 — no physically impossible report got in.

### 0e. The fit — a level match, and the preset refuses to call it more

`radio_calibration.link_calibration_model`: ridge regression (λ=50) over the 296 positives plus
weighted background negatives, 17 coefficients across distance, terrain, clutter and elevation terms.
It also fixes three scalars used everywhere downstream: `noise_level: -110.5` dBm,
`path_loss_distance_floor_m: **780.0**`, and reported-SNR clamps of −21.25 / +8.25 dB.

The 780 m floor is not a typo. Map positions are coarse and many nodes share a pin, so the fit
declines to answer below that radius rather than extrapolating into a near field it never saw.

**What `calibration_diagnostics` records about its own quality** — every line asserted by
`tests/test_calibration_quality.py`, so none of it can rot:

| diagnostic | value | what it means |
| --- | --- | --- |
| `is_level_match_not_propagation_model` | `true` | it matches *levels*, it does not model propagation |
| `cause_settled` | `false` | no causal claim is made about why links behave this way |
| `correlations_with_observed_snr` | −0.094 log-distance, −0.011 terrain, 0.079 clutter | **no feature the fit uses correlates with what it fits** |
| `observed_links_reproduced` | 95 of 296 | it does not reproduce the graph it was fitted to |
| `unobserved_pairs_made_audible` | 2095 of 2190 audible | 96% of the links it asserts were never observed |
| `observed_pair_snr_error_rms_db` | 12.32 (mean −8.81) | error on its own training pairs |
| `background_effective_weight` | 161.5 | background rows are over a third of the fit |
| `log_distance_refit_rms_db` | 26.5–38.5 | what a plain log-distance law scores on the same data, i.e. why the fit exists |

Evidential character: **the strongest link model available here and still weak in absolute terms.**
It earns its place by being better than 2c on real geometry, not by being right. This is why
`--no-link-calibration` exists, why the envelope is enforced, and why stage 2a says *replacement,
not correction*.

### What Stage 0 means for reading a result

- A Batumi run is **not** uniformly "real". Its geometry and ground are measured, its land cover is
  flagged for regeneration, and its link model is an admitted level match that its own diagnostics
  say does not reproduce the graph it was trained on.
- The five captures are separable. `--no-terrain`, `--no-clutter` and `--no-link-calibration` each
  remove one, which is the only honest way to ask what that capture was contributing.
- **One place, one season, one band.** There is no second real snapshot to cross-check against, and
  `docs/batumi_radio_calibration.md` is the full account.

## Stage 1 — Where the nodes are

The geometry. Everything downstream is conditional on it, and it is the stage where "real" is
cheapest to obtain and most often skipped.

### 1a. Captured from a real mesh

| source | how | what you get |
| --- | --- | --- |
| packaged snapshot | `--scenario batumi` | 92 nodes on 55 unique coordinates, real roles and hop limits, **and the mesh decides its own node count** — `--nodes` is ignored |
| the public map | `--scenario map --bbox min_lat,min_lon,max_lat,max_lon` (+ `--scenario-limit`) | positions cut from the Meshtastic map, ground fetched under them |
| a live device | *(event sim)* `--from-nodedb` with `--nodedb-host` / `--nodedb-serial-port` | positions out of a device's own NodeDB over TCP or serial |
| a file | *(event sim)* `--from-file` | a YAML node list you control |

Steps: fetch or load the node list → resolve roles, hop limits and mute flags **from the snapshot**,
not from `--router-fraction` → establish the local metric origin → fetch ground under the footprint
(stage 2b) → optionally `--mirror N` to tile the geometry for a larger mesh of the same character.

What this buys: a node distribution no generator produces — clusters on ridgelines, nodes sharing a
rooftop, the long thin arm along a coast road. What it costs: **one place**. Batumi is the only real
snapshot here, its fitted budget rests on 296 observations reaching 23.2 km, and it must not be
extrapolated past that (`sfpp/README.md` §5.10).

### 1b. Generated from parameters

`--topology {uniform,clustered,corridor,hub,chain,mixed}` with `--nodes` and `--area`. A minimum
separation is enforced by `place_nodes` rather than exposed as a flag — 300 m, because two Meshtastic
nodes closer than that are one site.

Steps: draw positions for the chosen topology → assign roles by `--router-fraction`,
`--router-late-fraction`, `--client-base-fraction`, placed by `--role-placement
{degree,inverse,random}` → assign hop limits by `--hop-assign {centrality,random}` with
`--hop-spread` → apply the census mixes: `--role-mix`, `--platform-mix`, `--siting-mix`,
`--amplifier-mix` → optionally `--stretch` to scale distance as its own variable.

What this buys: a controlled variable and as many seeds as you want. What it costs: a mesh nobody
deployed. **Uniform placement understates congestion**, because spatial reuse means most
transmissions never overlap at any one receiver.

> A generated mesh can still stand on real ground — `--scenario ridge` puts a landform under it
> (stage 2b) without borrowing anyone's node positions. That combination is often the right default:
> controlled geometry, honest terrain.

---

## Stage 2 — How links are decided

Given positions, which pairs can hear each other and how well. Three sources of truth, in descending
order of evidential strength. They are **not** alternatives of equal standing.

### 2a. From real measurements — a fitted calibration

`--scenario batumi` carries it; `--no-link-calibration` refuses it.

Steps: load the scenario's fitted coefficients → compute the geometric budget → **replace** it with
the fit inside the fit's own observed envelope → refuse to answer outside that envelope rather than
extrapolating.

This is a *replacement*, not a correction, and the reason is stage 2c's failure: at
`3gpp-suburban` with 1.5 m antennas the exponent is 4.49 and the raw budget yields **no link past
about a kilometre** on real geometry. Details in `docs/batumi_radio_calibration.md`.

Strongest available. Also the narrowest: it is one mesh, one band, one season, and the envelope is
enforced precisely because a fit answers any input including ones it has never seen (TRAPS 4).

### 2b. From real terrain and modelled propagation

`--scenario {batumi,map,flat,rolling,ridge,valleys,coastal,alpine}`; disable parts with
`--no-terrain`, `--no-clutter`; `--offline` to forbid fetches.

Steps: obtain elevation — SRTM tiles for a real footprint, or a hashed synthetic grid for a landform
→ obtain land cover — OSM classes on an indexed grid → for each pair, sample the terrain profile →
knife-edge diffraction loss over the obstruction → clutter attenuation by class → add to the
modelled path loss from 2c → floor the total at free space.

What this buys: the largest real term most meshes actually face. On Batumi clutter is the larger of
the two. What it costs: the propagation *law* is still theory (2c); only the obstruction is measured.
Land cover has bitten twice — a cheapest-rate default for unrecognised classes (TRAPS 23) and a
tiling that destroyed the raster's regularity (TRAPS 8).

### 2c. From theory — a path-loss model alone

`--path-loss-model {log-distance,hata-small-city,hata-metro,hata-suburban,hata-rural,3gpp-suburban,3gpp-urban}`,
default `3gpp-suburban`. Seven models, tabulated in `docs/radio_model.md`.

Steps: distance and frequency, floored at `PATH_LOSS_DISTANCE_FLOOR_M` → the chosen empirical
formula → floor at free space → add reciprocal shadowing (`MODEL_SHADOWING_STDDEV`, 6 dB) and
per-radio asymmetry (`MODEL_RADIO_ASYMMETRY_STDDEV`, 2 dB) → compare against the receiver's
effective sensitivity.

What this costs, stated plainly: **every one of the seven is an empirical fit with a validity range
this simulator routinely violates.** Okumura-Hata wants a base station 30–200 m up and a mobile
1–10 m up; here both ends are usually 1.5 m above local ground. Asked far outside its range the 3GPP
form's linear height terms dominate and return *negative* loss — 900 m of antenna height on a 60 km
path once produced **+2173 dBm** of RSSI, which is why the free-space floor exists.

**A flat-world theory-only run is the default, and it is the weakest path through this stage.**

### The layer under all three: sensitivity

Effective sensitivity is `max(datasheet, noise floor + the spreading factor's required SNR)`. A
tabulated sensitivity cannot outlive the floor it was measured against — using one against a
different measured floor counts the floor twice (TRAPS 20).

---

## Stage 3 — What the channel is like

Conditions that are **real but unmeasured for your site**. This is a distinct category from stages 2
and 6: not speculative firmware, not a modelling shortcut, but a genuine phenomenon whose magnitude
you are choosing rather than observing. A result must say which of these were on.

| choice | flags | steps |
| --- | --- | --- |
| noise floor | `--noise-model {thermal,fixed}` | `thermal` derives kTB + 6 dB NF from the preset's bandwidth; `fixed` reproduces the single vendored constant. Both are set explicitly, because letting `fixed` default would make it identical to `thermal` and turn a comparison arm into a duplicate (TRAPS 14/21) |
| a floor that moves | `--noise-profile {none,temporal,transient,periodic,both,all}` + `--noise-sigma-db`, `--noise-tau-ms`, `--noise-transient-*` | correlated spatial spread, temporal drift, local excursions. Every threshold derives from the floor, so an excursion can **remove a link**, not merely dim it (TRAPS 19) |
| foreign occupancy | `--noise-pulse-interval-ms`, `--noise-pulse-ms` (`periodic`) | a non-Meshtastic transmitter holds the channel as a *state*, wiping whatever is in flight — a hard loss, not an SNR penalty |
| ducting | `--duct-per-hour`, `--duct-gain-db`, `--duct-ms` | tropospheric lift that admits new pairs *and* makes existing links louder. Interferers carry the same lift, so it is not free gain: receptions rise and so do collisions |
| blunt loss | `--extra-loss`, `--burst-loss`, `--burst-ms` | a flat or bursty probability, for when you want loss without claiming a cause |

---

## Stage 4 — What the radio is set to

`--preset` — 19 presets: the vendored table's 17, of which 7 were added here from the firmware's own
`modemPresetToParams`, plus 2 that are ours and not upstream. Then `--tx-power`
(the region limit is a ceiling an operator *may* use, not one they must), and the region's frequency
slots from `lib/config.py`, pinned to firmware 2.8.0.

**One preset per mesh.** Comparing presets is a between-run comparison, never within one. A preset
changes reception, not just airtime — sensitivity moves with spreading factor and bandwidth.

---

## Stage 5 — Whose behaviour runs on top

The stage where the two simulators part company, and the one where a proposal can be mistaken for
firmware.

### 5a. Modelled firmware — the transport (`sfpp/mesh.py`)

`--profile {2.4,2.5,2.6,2.7,2.8,legacy}`, cumulative, each named for a release series and carrying
that series' final release. `--old-profile` with `--legacy-fraction` for a mixed-version mesh;
`--profile-flag NAME=VALUE` to override one rule.

Steps per packet: originate → priority → enqueue and queue order → transmit delay and contention
window → listen-before-talk → on air → reception decided per receiver (stage 6) → duplicate
suppression → routing decision → acknowledgement or retry.

`legacy` is **not a firmware version**: four of its deviations were never any firmware's behaviour,
so it must not be read as "2.7 and earlier."

### 5b. Modelled firmware — the discrete-event sim *(event sim)*

`lib/mac.py`, `lib/node.py`, `lib/packet.py`, `lib/discrete_event_sim.py`, pinned to firmware 2.8.0
commit `51eadb7`. `--router-type` selects the router. Same idea, different implementation and a
different feature set — see `DISCRETE_EVENT_SIM.md` for what each part is pinned to.

### 5c. Real firmware — the interactive sim

`interactiveSim.py [nrNodes] [-p path | -d]` launches N `meshtasticd` instances over TCP from port
4403 and forwards frames between them by the stage-2 verdict. **Nothing here models the firmware —
it runs it.** Pinned to meshtasticd 2.7.26, recorded per run in `out/versions.yaml`.

This is the strongest evidence about firmware behaviour and the weakest about scale: one process per
node.

### 5d. Proposed features — no release ships these

`sfpp/mesh.py` `PROPOSALS` declares five, `lib/dcr.py` and `lib/dtp.py` add two more:

| flag | why it is a proposal |
| --- | --- |
| `--extra-repeats` | the `extra-repeats` branch's `RepeatScalingModule` |
| `--coding-rate-ladder` | on a branch |
| `early_flood_on_unverified` | M4, compiled out at `NEXTHOP_EARLY_FLOOD_ON_UNVERIFIED 0` |
| `exhaust_hops`, `event_relay_hop_limit` | off in every profile, no release path |
| `--dcr` *(event sim)* | dynamic coding rate |
| `--dtp` *(event sim)* | dynamic TX power |

A run with any engaged prints a banner and lists them under `proposals` in the report. **No reading
of such a run is a statement about firmware.**

---

## Stage 6 — How a reception is decided

For each transmission and each candidate receiver, in this order. Every gate is separately counted,
because the fix for one is not the fix for another.

1. **Audible?** RSSI ≥ this receiver's effective sensitivity *for this frame's band*. Fails to
   `lost_to_noise_floor` — no coding rate rescues a packet the receiver never attempted.
2. **Awake?** A node that is off hears nothing.
3. **Deaf?** Transmitting while this arrived → `lost_to_half_duplex`, counted separately from
   collision.
4. **Captured?** The interferer scan (bounded per preset — `sfpp/TRANSPORT.md`, *The overlap window*)
   finds overlaps, filters to those above this receiver's CAD floor, then applies the preamble lock:
   whichever preamble arrived first holds the receiver, and a later packet needs 6 dB to break it.
   Fails to `lost_to_collision`.
   *(event sim)* `--capture-collision-model` selects this; the default is the legacy binary rule.
5. **Wiped?** Periodic interference fired in flight → `wiped_by_periodic`.
6. **Decoded?** The empirical SNR-to-PER draw, coding-rate dependent and length-penalised
   *(event sim* `--phy-loss-model`; on by default in sfpp, off with `--no-phy-loss`*)*. Fails to
   `lost_to_phy`.

Channel-busy time is charged separately and is **not** the collision model: every packet a receiver
*could hear* counts, decoded or not, accumulated as the **union** of overlapping stretches, because a
radio has one energy detector. Charging each overlapping transmission its full airtime once took the
figure to 184% of wall-clock (TRAPS 5).

---

## Stage 7 — What the run is asked, and what it may be read as

### 7a. Offered load

`--diurnal {flat,sinusoid,commuter}` with `--start-hour`, per-class rates
(`--dm-per-hour`, `--traceroute-per-hour`, `--admin-probes-per-hour`, `--broadcast-interval-s`),
`--position-throttle` / `--telemetry-throttle`, and the firmware's own congestion throttle
(`--congestion-mode`, `--congestion-input`, `--congestion-pivot`, `--no-congestion-scaling`).

### 7b. The application under test

`--protocol {none,chain,sr}` — set reconciliation, the chain-walk incumbent it aims to replace, or
neither. Then the archive's own configuration: `--servers`, `--place`, `--bucket-mode`, `--capacity`,
`--trigger`, `--resolve`, `--advert-interval-s`.

### 7c. Measurement

`--out` writes the JSON; `--reception-bin-s` keeps a time series so a diurnal cycle is readable
rather than averaged away; `--mesh-map` draws the geometry; `--no-charts` skips pictures.

The report's `models` block names the resolved stage 2–4 stack and `proposals` names any stage 5d
behaviour, so a JSON says which path produced it.

### 7d. Comparability — the stage most often skipped

- **`sim_version`** answers "is this run comparable with that one?"; `transport_pin` answers "exactly
  which code produced it?" Both are recorded, because a commit does not order and does not survive a
  rebase.
- **Four success measures, four denominators, not comparable to each other**: broadcast reach, DM
  delivery at the addressed node, admin success per session, archive held fraction. Treating one as a
  proxy for another is the commonest misreading of this tool (`sfpp/README.md` §7.3).
- **Every arm names its own value.** An arm defined as "whatever the default is" becomes a duplicate
  of the control the moment the default moves (TRAPS 21).
- **`collate.py` warns on an inert arm** by comparing every number in the report, not a chosen few.

---

## Choosing a path

| you want to know | stage 0 leaned on | stage 1 | stage 2 | stage 5 |
| --- | --- | --- | --- | --- |
| does the firmware do what I think | none | any | any | 5c, real firmware |
| how a protocol scales | 0b ground only | 1b generated | 2b terrain under it | 5a transport |
| what happens on a real mesh | 0a–0e, all five | 1a Batumi | 2a fitted, inside its envelope | 5a at the matching profile |
| is this proposal worth shipping | 0b | 1b, many seeds | 2b | 5d, against the same run without it |
| a quick sanity check | none | 1b | 2c theory, flat | 5a |

The last row is the default, and the default is the weakest path in this document. That is fine for
a sanity check and not fine for a claim.
