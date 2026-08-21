# Radio Physics Quickstart

This guide is for comparing Meshtastic radio-policy experiments in the
discrete-event simulator without reading the simulator internals first.

## Find Runnable Scenarios

Packaged presets are the easiest starting point because they already carry
node locations and any matching terrain, clutter, and calibration data:

```bash
./loraMesh.py --list-presets
```

Modem presets can also be listed from the same CLI:

```bash
./loraMesh.py --list-modem-presets
```

The `batumi` preset is a sanitized Batumi/Georgia-area scenario. It includes
node geometry, terrain, land-cover clutter, and a fitted link-calibration model.
The preset does not include node names, source IDs, collection endpoints, or
per-link runtime corrections.

## Minimal Useful Runs

Use `--no-gui` for repeatable command-line comparisons:

```bash
./loraMesh.py --preset batumi --no-gui --simtime-seconds 60 --period-seconds 5
```

## One-Command Policy Comparison

The easiest way to compare policy experiments is the wrapper tool:

```bash
python3 tools/radio_policy_compare.py --policies static,dcr,dtp --simtime-seconds 60 --period-seconds 5
```

It runs the same preset and traffic load for:

- `static`: static coding rate with packet-loss and capture-collision physics.
- `dcr`: Dynamic Coding Rate on top of the same physics flags.
- `dtp`: Dynamic TX Power on top of the same physics flags.

The output is one table with reach, useful traffic, airtime, collisions, PHY
loss, and placeholders for future policy counters.

For CI, write durable artifacts:

```bash
python3 tools/radio_policy_compare.py \
  --simtime-seconds 120 \
  --period-seconds 5 \
  --json-output out/radio_policy_compare.json \
  --markdown-output out/radio_policy_compare.md
```

Threshold flags such as `--max-reach-drop-pp` compare every non-baseline policy
against the first policy in `--policies`; they require at least two policies.
This lets CI fail when `dcr` or `dtp` loses too much reach/useful traffic or
spends too much extra TX airtime. The JSON file is intended for machines; the
Markdown file is intended for CI summaries, uploaded artifacts, or PR comments.

Extra `loraMesh.py` flags can be applied to every run after `--`:

```bash
python3 tools/radio_policy_compare.py --policies static,dcr,dtp -- --no-clutter
```

Enable packet-level loss and capture-aware collisions when testing radio
physics. Those two flags make weak links and overlapping transmissions matter:

```bash
./loraMesh.py --preset batumi --no-gui --simtime-seconds 60 --period-seconds 5 \
  --phy-loss-model --capture-collision-model
```

Keep `--simtime-seconds`, `--period-seconds`, preset, and model flags identical
when comparing policies. Otherwise the result moves because the traffic load or
radio physics changed, not because the policy improved.

## Reading The Result

`radio_policy_compare.py` prints one row per policy: `reach%`, `useful%`,
`tx_air%`, `msgs`, `sent`, `rx`, `coll`, `phy_loss`, the CR mix, the DTP power
mix, and mean CAD-detected/decodable receivers per transmission. Start with
`reach%` and `useful%`, and read `coll`, `phy_loss` and `tx_air%` as the cost.

A single `loraMesh.py` run prints more, and these are the lines worth reading
first:

- `Percentage of addressed receivers reached`: deliveries over the receivers
  those messages actually addressed - N−1 for a broadcast, 1 for a DM. See
  [metrics.md](metrics.md); it is not "percentage of nodes".
- `Percentage of received packets containing new message`: how much received
  traffic was useful instead of a duplicate.
- `Average Tx air utilization`: the run-long share of time this mesh's nodes
  spent transmitting.
- `Channel utilization (60 s window)`: what the air sounded like to each node,
  own transmissions included. This is the figure the transmit gate reads.
- `Own-TX utilization (1 hr window)`: the node's own transmissions only, which
  is what a region's duty cycle binds against.
- `Sends deferred by the channel-utilization gate`: how often a node held a
  periodic message back because the channel was over 25%, and for how long.
- `Number of collisions`: overlap pressure before packet-level PHY loss.

Good policy changes should improve reach or useful traffic without causing a
large airtime or collision regression. A policy that only makes every packet
more robust or louder is usually not a useful mesh policy.

**Read reach and deferral together.** The transmit gate means a congested mesh
offers less load rather than dropping more of it, so a policy that makes the air
busier can show unchanged reach while the deferral count and mean wait climb.
That is a real cost paid in latency, and it only appears in those two fields.

## Importing Map Locations

Map imports are useful for quick local experiments:

```bash
./loraMesh.py --from-map 'https://meshtastic.liamcottle.net/api/v1/nodes' \
  --map-bbox 41.50,41.50,41.82,41.86 \
  --map-limit 100 \
  --no-gui
```

Map-imported scenarios do not automatically gain the Batumi preset's terrain,
clutter, or fitted radio calibration. Use packaged presets for calibrated
benchmarks, and map imports for exploratory placement checks.

## Common Pitfalls

- `--preset batumi` automatically uses its bundled terrain, clutter, and link
  calibration. Add `--no-clutter` only when intentionally comparing against a
  no-clutter run.
- `--phy-loss-model` and `--capture-collision-model` are separate from terrain
  and clutter. Use them for packet-policy comparisons once more policy flags are
  available.
- Short runs are noisy. Use longer runs or repeated runs before claiming that a
  policy is better.
- Treat CI thresholds as guardrails, not proof of RF truth. A failed threshold
  means "inspect this change"; a passed threshold means "no regression in this
  fixed simulator scenario".
- The `batumi` calibration is fitted, and `LINK_CALIBRATION_MAX_M` bounds where
  it applies. Past that distance the raw link budget answers instead, so a run
  whose interesting links are long is not being answered by the fit. See
  [batumi_radio_calibration.md](batumi_radio_calibration.md) for what the fit
  does and does not reproduce.
- Reach and airtime are not comparable across modem presets unless the noise
  floor moved with the bandwidth. It does by default now (`NOISE_LEVEL` is
  derived per preset); a scenario that pins its own floor is comparing presets
  against one band and should say so.
