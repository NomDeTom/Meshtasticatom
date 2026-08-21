# Batumi Radio Calibration

This report documents the reusable radio calibration used by the packaged `batumi` preset. It is
intentionally aggregate-only: no node names, source node IDs, or collection endpoint details are
required for reproducing simulator behavior.

**Read the status section first.** The fit is a level-matching surface, not a propagation model, and
it does not reproduce the link graph it was trained on. Every figure below was recomputed against
the current tree; `tests/test_calibration_quality.py` and `tests/test_presets.py` recompute the ones
recorded in `presets/batumi.yaml` on every run, so those cannot go stale unnoticed.

## Data Window

The reference data is a 30-day Batumi/Georgia-area neighbor-SNR snapshot. Nodes were filtered to the
preset bounding box:

```text
lat: 41.50..41.82
lon: 41.50..41.86
```

Reference sample shape:

```text
nodes in bbox:                      92
current neighbor edges:             85
30-day distinct directed edges:     296
30-day neighbor samples:            14361
generated directed pairs:           8372
OSM clutter cells:                  4320
OSM clutter cells by class:         open=3101 urban=1209 forest=5 water=5
```

Observed median SNR across the 296 directed calibration edges:

```text
min:  -20.75 dB
p05:  -19.06 dB
p25:  -17.50 dB
p50:  -10.88 dB
mean:  -9.53 dB
p75:   -3.75 dB
p95:    5.81 dB
max:    6.75 dB
```

Observed link lengths run from under a metre (co-located pins) to 23.2 km, with a median of 5.2 km.

## Calibration Shape

The calibration is not a node-pair replay table. The runtime simulator never asks "was this exact
directed pair observed?" and never lifts one specific link because it appeared in the calibration
data.

Instead, the preset stores a reusable feature transform:

```text
calibrated_snr = intercept
               + raw_snr_clip * a
               + log_distance_km * b
               + log_distance_km_sq * c
               + terrain/clutter/vantage/land-cover feature terms
```

The model is trained from two kinds of examples:

```text
positive targets: 296 observed directed links with median observed SNR
background targets: all other generated directed pairs, weakly weighted at 0.02
background target SNR: min(raw_model_snr, -22 dB)
ridge lambda: 50
```

The applied coefficient set lives in `presets/batumi.yaml` under
`radio_calibration.link_calibration_model.coefficients`. Runtime packet logic uses only those
coefficients and path features, so the same model can be applied to new generated points that have
no ground-truth links.

### Where the transform applies, and where it stops

Two things are deliberately outside the fitted surface.

**EIRP.** The transform is evaluated at a *reference* EIRP of `PTX + 2 * GL`, and the difference
between a packet's actual EIRP and that reference is added back afterwards, decibel for decibel. A
fit made at one power level otherwise absorbs the power level, and changing `PTX` or an antenna gain
moves nothing - which would make every transmit-power experiment on this preset a no-op.
`tests/test_calibration_quality.py::TransmitPowerIsTransparent` pins this.

**Distance beyond the fit's support.** `LINK_CALIBRATION_MAX_M` is derived from the observation list
itself - the longest observed link, **23,225 m** - rather than declared, so it cannot disagree with
the data beside it. Past that distance the raw link budget answers instead, and
`LinkBudget.calibration_applied` reports which of the two answered. This affects 26 of the 8372
generated pairs on the packaged geometry; it matters much more for a `--from-map` scenario over a
wider bbox, where a quadratic in `log10(distance)` fitted inside 23 km is asked about 60 km and
answers confidently.

## Scalar Baseline

The scalar baseline includes the preset noise floor, path-loss distance floor, terrain, and
OSM-derived clutter, but not the fitted feature transform:

```yaml
radio_calibration:
  noise_level: -110.5
  path_loss_distance_floor_m: 780.0
  reported_snr_min_db: -21.25
  reported_snr_max_db: 8.25
```

`noise_level: -110.5` is a **measured** floor, 3.5 dB above kTB + 6 dB NF at 250 kHz
(−114.02 dBm), which is plausible for a coastal city. It is also why the decodability threshold on
this preset cannot be read from a table. `effective_sensitivity` takes
`max(datasheet_sensitivity, noise + required_snr_db(sf))`:

```text
datasheet sensitivity, LONG_FAST:              -131.5 dBm
measured floor + SF11 requirement (-17.5 dB):  -128.0 dBm
effective sensitivity:                         -128.0 dBm
```

The measured floor binds, by 3.5 dB. Using the datasheet figure against this preset's own measured
floor would have declared audible a band of links 3.5 dB below anything the measured noise permits -
a sensitivity and the noise floor it was measured against are not independent numbers, and the
datasheet figure is itself kTB + 6 dB NF + the SF11 requirement (−131.52 dBm), so pairing it with a
different floor double-counts the band.

`reported_snr_min_db: -21.25` is a **reporting** clamp, matched to the archive's own floor (its
minimum observation is −20.75 dB). It is not a decodability threshold, and it sits 3.75 dB *below*
the SF11 demodulator requirement of −17.5 dB: a pair whose reported SNR is at the clamp is not a
marginal link, it is an inaudible one. Decodability is decided by RSSI against
`effective_sensitivity`, never by this number.

On the 296 observed directed edges, scalar-only reachability is poor:

```text
observed directed links reproduced by scalar model:  28 / 296
scalar-only audible directed links, all pairs:      760 / 8372
```

Scalar model RSSI margin to the effective sensitivity on observed pairs:

```text
min: -103.02 dB
p05:  -90.17 dB
p25:  -62.97 dB
p50:  -45.55 dB
mean: -43.13 dB
p75:  -24.05 dB
p95:    9.86 dB
max:   18.61 dB
```

Pairwise residual, `observed_median_snr - scalar_model_snr`, on the reported (clamped) scale:

```text
min:  -19.86 dB
p05:    0.50 dB
p25:    3.50 dB
p50:    9.25 dB
mean:  10.27 dB
p75:   16.75 dB
p95:   26.75 dB
max:   28.00 dB
```

The residual is bounded above by 28 dB only because the reported SNR is clamped at −21.25; on the
unclamped scale the scalar model is tens of decibels pessimistic on most observed pairs. Coarse map
pins, balcony/roof placement, antenna orientation, coastal corridors, and reflections are not
represented by distance, terrain, and OSM land-cover alone.

## Fitted Feature Model

After applying the reusable feature transform:

```text
observed directed links reproduced by fitted model:  95 / 296
fitted-model audible directed links, all pairs:    2190 / 8372
```

Reported model SNR for the 296 observed calibration links:

```text
min: -21.25 dB
p05: -21.25 dB
p25: -21.25 dB
p50: -20.48 dB
mean: -18.34 dB
p75: -16.60 dB
p95:  -6.08 dB
max:  -1.57 dB
```

Residual after feature calibration, `observed_median_snr - fitted_model_snr`:

```text
min: -16.88 dB
p05:  -4.74 dB
p25:   2.55 dB
p50:   7.75 dB
mean:  8.81 dB
p75:  14.83 dB
p95:  26.50 dB
max:  28.00 dB
```

Reported SNR across all generated directed pairs after feature calibration:

```text
min: -21.25 dB
p05: -21.25 dB
p25: -21.25 dB
p50: -21.25 dB
mean: -18.78 dB
p75: -17.31 dB
p95:  -9.85 dB
max:   8.25 dB
```

The transform is worth roughly 67 recovered observed links and 1430 extra audible pairs over the
scalar baseline. It is still 8.8 dB pessimistic in the mean on the links it was trained on.

## Status Of The Fit

This is the part a reader needs before using the coefficients for anything. The figures here are
recomputed by `tests/test_calibration_quality.py` and mirrored in `presets/batumi.yaml` under
`calibration_diagnostics`.

**The observations carry no distance law.** Every feature the ridge fit uses correlates with the
observed SNR at |r| ≤ 0.1:

```text
log10_distance_km:          -0.094
terrain_loss_db:            -0.011
clutter_loss_db:             0.079
max_ground_elevation_100m:   0.099
```

A least-squares refit of observed SNR on `log10(distance)` alone gives a slope of **0.94 dB per
decade**, where any propagation model is 20 to 40. A 10-25 km link reads *better* on average
(−8.5 dB) than a 2-5 km one (−12.1 dB). Refitting at any fixed path-loss exponent leaves 26.5 to
38.5 dB RMS. So the geometric coefficients are fitting noise, which is why the model is non-monotone
in distance inside its own envelope, and why `water_fraction` and `forest_fraction` came out at
exactly 0.0.

**The fit does not reproduce the graph it was fitted to.** 95 of 296 observed links are audible in
the model; 2095 pairs that were never observed are. So it is neither a propagation model nor a
proven-link interpolator, and it should not be described as either.

**Nothing here is physically impossible.** All 296 observations lie below free space - the check
matters, because a fit trying to reach observations above free space would be fitting an error
rather than a channel. `estimate_path_loss` now floors at free space, so the model cannot answer
below it either.

**Three hypotheses, and no settled cause.** An earlier version of this document named censoring as
the likely cause. That was premature; it is now the second of three, and the first needs no fault in
the measurements at all.

1. **A moving noise floor.** A real floor is a distribution with a median well above kTB and several
   decibels of spread. The observations scatter by 8.11 dB, and on this geometry the *path* only
   varies by 10-20 dB across the whole 0-23 km range under any plausible exponent - so a band with
   5-8 dB of spread, sampled once per pair over an unknown window, is enough to bury the distance
   signal with nothing wrong with the data. Testable, and only with timestamps: it predicts that
   observations taken close in time agree better than ones taken far apart. `NOISE_SIGMA_DB` and
   `NOISE_TAU_MSEC` exist so a scenario can model this band; see
   [radio_model.md](radio_model.md).
2. **Censoring.** Every row is a link that worked. There are no non-detections, and the sample stops
   near the modem's own floor (min −20.75 dB). Selecting on success destroys distance dependence.
3. **The background weight.** `training_background_weight: 0.02` applies to every unobserved pair,
   and there are 8076 of them - a total weight of **161.5** against the observations' 296, so the
   synthetic −22 dB rows carry 35% of the fit's weight. That matches the measured −8.8 dB pessimism
   on observed links, and unlike the other two it would make the fit recoverable **without new
   measurements**: re-fitting at a weight that leaves the background a stated minority is a
   re-derivation, not a new field campaign.

Distinguishing (1) from (2) needs per-observation timestamps, which the packaged aggregate does not
carry. The question list for the mesh's modellers (kept in the
`notes-sync` companion repository, alongside this fix series) asks for them.

**What the coefficients are used as.** A level-matching surface that reproduces the existing
archive's *levels*, and not a propagation model. Transmit power and antenna gain are applied outside
it, decibel for decibel, so a power experiment on this preset is physical even though the surface is
not.

## The Clutter Raster

The land-cover clutter grid is derived from public OpenStreetMap building, landuse, natural, and
water polygons fetched with Overpass. The packaged CSV is a coarse 500 m raster over
`[41.500396, 41.501032, 41.819656, 41.856051]`. It does not include raw OSM feature IDs or names.
Attribution: OpenStreetMap contributors.

It was exported **before** `lib/osm_clutter.py` queried relations or `natural=coastline`, and open
sea is neither a closed way nor tagged `natural=water` - it comes from coastline processing. So the
Black Sea, west of a Black Sea coastal city, is classified `open`: five water cells in 4320. Every
consequence follows from that:

- `water_fraction` has no variance over the mesh, which is why the fit's coefficient for it is
  exactly 0.0.
- `CLUTTER_WATER_LOSS_DB_PER_KM` is unreachable on this preset.
- The coastal discount was firing on roughly a quarter of all pairs as an "over half this path is
  unmapped" test, until it was made to require actual water samples.

Regenerating it needs Overpass access, which the environment these fixes were made in does not have:

```bash
python3 tools/osm_to_clutter_csv.py \
  --bbox 41.500396,41.501032,41.819656,41.856051 \
  --origin 41.6442879,41.61536 --step-meters 500 \
  --output presets/batumi_clutter.csv
```

and then re-deriving the link calibration against the new raster, since the fit's clutter terms were
trained on this one. `presets/batumi.yaml` records the class histogram under `clutter_provenance`,
and `tests/test_presets.py` asserts it against the CSV, so a regenerated raster will fail that test
until the record is updated with it.

The terrain grid's resolution is a deliberate choice by the preset's author and is not on this list.

## Why Not Pairwise Correction

The runtime model deliberately does not carry a lookup table of observed directed links and does not
boost one exact node pair just because that pair appeared in the calibration sample. A pair-specific
correction can make the calibration set look perfect while adding nothing for a new generated point
with no ground truth.

The packaged observations are training/evaluation records only. The simulator applies one fitted
transform to every generated TX/RX pair. That is less flattering to the calibration set, but much
more useful for testing new placements and other nearby meshes.

## Known Limitations

This calibration target is neighbor-SNR history, not a packet-level PER trace. Neighbor tables are
biased toward nodes that report neighbor info, and a 30-day observed edge does not prove the link is
continuously available - or that it was available at the same time as any other edge in the set.

The fitted coefficients are local to the packaged Batumi preset. They do not change random or
default simulations and should not be treated as universal LoRa propagation constants. Given the
status section above, they should not be treated as propagation constants for Batumi either. The
useful part to reuse elsewhere is the workflow: compute physical path features, fit coefficients
against local observations, evaluate generated pairs without runtime per-link priors - and then
check, as this document now does, whether the result reproduces the graph it was fitted to.
