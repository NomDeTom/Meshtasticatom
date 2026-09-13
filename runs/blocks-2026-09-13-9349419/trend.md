# Sweep blocks-2026-09-13-9349419

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 9349419 · seeds 9349419
- **blocks** 87 run
- **compute** 8.7 h of simulator time across every cell
- **generated** 2026-09-13T08:38:41+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>72 warnings</summary>

- AD-badrouters: role-placement=random: decode_failures 1
- AD-siting: siting-mix=local-typical: decode_failures 2
- AD-siting: siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count
- BL-control: protocol=sr: decode_failures 34
- BL-control: slower: 4.61 s per simulated hour against 1.7 over 23 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 55
- DB-warm: warm-num-nodes=0: decode_failures 51
- DB-warm: warm-num-nodes=25: decode_failures 51
- DB-warm: warm-num-nodes=100: decode_failures 51
- DB-warm: warm-num-nodes=2000: decode_failures 51
- DG-burst: burst-loss=0.2: decode_failures 2
- DG-burst: burst-loss=0.3: decode_failures 19
- DG-outage: burst-loss=0.1: decode_failures 27
- DG-outage: burst-loss=0.2: decode_failures 9
- DG-outage: burst-loss=0.3: decode_failures 14
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 2
- LD-chatty: broadcast-interval-s=300: decode_failures 3
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 51
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 108
- MS-density: nodes=90: misdecodes 1
- MS-hopscale: nodes=120: decode_failures 2
- MS-hopscale: nodes=500: decode_failures 124
- MS-oversubscribed: nodes=500: decode_failures 87
- MS-siting: siting-mix=event: decode_failures 9
- MS-size: nodes=120: decode_failures 2
- MS-stretch: stretch=2.0: decode_failures 10
- MS-topology: topology=clustered: misdecodes 1
- PR-dmmode-cr: faster: 1.21 s per simulated hour against 2.54 over 23 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 1
- RF-preset: faster: 1.28 s per simulated hour against 3.03 over 23 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- RF-stretch-duct: faster: 1.46 s per simulated hour against 2.97 over 23 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-bucket-mode: bucket-mode=global: misdecodes 34
- SF-bucket-mode: bucket-mode=time: misdecodes 48
- SF-bucket-mode: bucket-mode=window: misdecodes 22
- SF-bucket-mode: faster: 0.613 s per simulated hour against 1.63 over 23 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-bucket-time: time-bucket-s=600: misdecodes 135
- SF-bucket-time: time-bucket-s=1800: misdecodes 48
- SF-bucket-time: time-bucket-s=3600: misdecodes 24
- SF-cadence: trigger=interval: misdecodes 21
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 17
- SF-cadence: trigger=bucket+interval: misdecodes 21
- SF-capacity-local: capacity=4: decode_failures 52
- SF-capacity-local: capacity=8: decode_failures 7
- SF-capacity: capacity=4: decode_failures 52
- SF-capacity: capacity=8: decode_failures 7
- SF-capacity-window: capacity=8: misdecodes 20
- SF-capacity-window: capacity=8: decode_failures 12
- SF-capacity-window: capacity=16: misdecodes 2
- SF-capacity-window: capacity=32: misdecodes 22
- SF-catchup: catch-up-hours=: misdecodes 21
- SF-catchup: catch-up-hours=02-06: decode_failures 31
- SF-catchup: catch-up-hours=00-08: decode_failures 29
- SF-hops-flat: hops-apart=3: decode_failures 34
- SF-hops-flat: hops-apart=4: decode_failures 23
- SF-hops-spread: hops-apart=3: decode_failures 34
- SF-hops-spread: hops-apart=4: decode_failures 23
- SF-hops-spread: hops-apart=5: decode_failures 22
- SF-place-flat: place=spread: decode_failures 7
- SF-place-flat: place=random-clients: decode_failures 32
- SF-place-spread: place=spread: decode_failures 7
- SF-place-spread: place=random-clients: decode_failures 32
- SF-provide-transport: faster: 0.926 s per simulated hour against 1.91 over 23 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 10
- SF-replay-order: replay-ordering=heard: misdecodes 17
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-window-size: window-size=8: misdecodes 113
- SF-window-size: window-size=16: misdecodes 24
- SF-window-size: window-size=32: misdecodes 22
- TH-congestion: no-congestion-scaling=True: decode_failures 26
- TH-congestion: faster: 9.13 s per simulated hour against 18.7 over 23 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 4.61 | 1.7 | 2.71x | 23 |
| `DB-platform` | 1.74 | 2.6 | 0.67x | 23 |
| `SF-jitter-global` | 1.2 | 1.79 | 0.67x | 23 |
| `MS-stretch` | 1.6 | 2.4 | 0.67x | 23 |
| `SC-signing` | 1.25 | 1.87 | 0.67x | 23 |
| `SF-replay-order` | 1.12 | 1.69 | 0.67x | 23 |
| `RF-preset-turbo` | 1.02 | 1.59 | 0.64x | 19 |
| `RF-bw500` | 1.53 | 2.41 | 0.63x | 23 |
| `RT-rebroadcast` | 0.993 | 1.59 | 0.62x | 23 |
| `SF-capacity` | 1.06 | 1.7 | 0.62x | 23 |
| `LD-interval` | 0.871 | 1.4 | 0.62x | 23 |
| `LD-chatty-hops` | 2.66 | 4.32 | 0.62x | 23 |
| `SF-capacity-local` | 1.11 | 1.81 | 0.62x | 23 |
| `RF-txpower` | 0.975 | 1.61 | 0.61x | 23 |
| `LD-traceroute` | 1.27 | 2.1 | 0.60x | 23 |
| `DG-outage` | 4.2 | 6.97 | 0.60x | 23 |
| `PR-repeats` | 1.01 | 1.68 | 0.60x | 23 |
| `SF-window-size` | 0.863 | 1.44 | 0.60x | 23 |
| `SF-advert-transport` | 1.1 | 1.85 | 0.59x | 23 |
| `RF-eu-presets` | 1.2 | 2.03 | 0.59x | 23 |
| `DG-loss` | 1.31 | 2.22 | 0.59x | 23 |
| `DG-burst` | 2.85 | 4.9 | 0.58x | 23 |
| `RF-noise` | 3.05 | 5.27 | 0.58x | 23 |
| `SF-replay-order-broadcast` | 1.04 | 1.88 | 0.56x | 23 |
| `SF-jitter-local` | 1.03 | 1.88 | 0.55x | 23 |
| `DB-hotstore` | 1.39 | 2.54 | 0.55x | 23 |
| `PR-crladder` | 1.52 | 2.79 | 0.55x | 23 |
| `LD-chatty` | 2.74 | 5.04 | 0.54x | 23 |
| `DM-mode` | 1.64 | 3.06 | 0.53x | 23 |
| `RF-pulse` | 0.898 | 1.72 | 0.52x | 23 |
| `SF-bucket-time` | 0.869 | 1.71 | 0.51x | 23 |
| `RF-stretch-duct` | 1.46 | 2.97 | 0.49x | 23 |
| `TH-congestion` | 9.13 | 18.7 | 0.49x | 23 |
| `SF-provide-transport` | 0.926 | 1.91 | 0.48x | 23 |
| `PR-dmmode-cr` | 1.21 | 2.54 | 0.47x | 23 |
| `RF-preset` | 1.28 | 3.03 | 0.42x | 23 |
| `SF-bucket-mode` | 0.613 | 1.63 | 0.38x | 23 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.747 | 0.747 | 0.573 → 0.584 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.215 → 0.932 | 0.716 | 0.211 → 0.931 | 4.5x sr_airtime | up | 4 |
| `BL-control` | protocol | **held** | 0 → 0.646 | 0.646 | 0.577 → 0.584 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.136 → 0.747 | 0.611 | 0.053 → 0.589 | 6.2x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.076 → 0.670 | 0.594 | 0.063 → 0.521 | 1.1e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.181 → 0.747 | 0.566 | 0.077 → 0.582 | 4.5x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.057 → 0.593 | 0.536 | 0.061 → 0.441 | 66x sr_bytes | down | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.421 → 0.943 | 0.522 | 0.325 → 0.723 | 4.5x bytes_on_air | down | 3 |
| `MS-hopscale` | nodes | **held** | 0.421 → 0.939 | 0.517 | 0.326 → 0.712 | 11x sr_bytes | down | 4 |
| `MS-stretch` | stretch | **held** | 0.273 → 0.747 | 0.474 | 0.122 → 0.582 | 2.9x advert_bytes | down | 4 |
| `RF-preset` | preset | **text** | 0.227 → 0.670 | 0.442 | 0.222 → 0.658 | 2.9x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.506 → 0.947 | 0.441 | 0.502 → 0.945 | 5.8x sr_airtime | up | 5 |
| `RF-eu-presets` | preset | **text** | 0.227 → 0.589 | 0.361 | 0.222 → 0.582 | 1.9x sr_airtime | up | 4 |
| `RF-bw500` | preset | **text** | 0.150 → 0.497 | 0.347 | 0.149 → 0.488 | 1.8x advert_bytes | up | 3 |
| `MS-topology` | topology | **text** | 0.589 → 0.926 | 0.338 | 0.582 → 0.924 | 2.4x sr_bytes | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.589 → 0.914 | 0.325 | 0.582 → 0.888 | 2.5x sr_bytes | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.268 → 0.587 | 0.319 | 0.259 → 0.577 | 2.2x sr_airtime | up | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.589 → 0.893 | 0.304 | 0.582 → 0.887 | 1.3x advert_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.445 → 0.743 | 0.299 | 0.441 → 0.739 | 1.8x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.445 → 0.743 | 0.299 | 0.441 → 0.739 | 2x bytes_on_air | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.433 → 0.715 | 0.282 | 0.425 → 0.713 | 13x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.326 → 0.589 | 0.263 | 0.315 → 0.582 | 1.9x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.473 → 0.730 | 0.256 | 0.461 → 0.729 | 1.7x sr_bytes | up | 4 |
| `DG-burst` | burst-loss | **text** | 0.353 → 0.589 | 0.236 | 0.333 → 0.582 | 2.1x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.383 → 0.617 | 0.233 | 0.372 → 0.610 | 8.5x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.537 → 0.759 | 0.223 | 0.323 → 0.529 | 4.6x sr_airtime | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.473 → 0.691 | 0.218 | 0.461 → 0.688 | 1.4x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.720 → 0.926 | 0.206 | 0.707 → 0.923 | 3x sr_airtime | down | 2 |
| `FW-versions` | profile | **text** | 0.589 → 0.785 | 0.197 | 0.582 → 0.775 | 3.1x bytes_on_air | down | 5 |
| `MS-size` | nodes | **held** | 0.747 → 0.939 | 0.192 | 0.582 → 0.712 | 5.1x sr_bytes | up | 5 |
| `FW-mixed` | legacy-fraction | **text** | 0.589 → 0.778 | 0.190 | 0.582 → 0.772 | 2.2x bytes_on_air | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.589 → 0.777 | 0.188 | 0.582 → 0.773 | 1.4x sr_airtime | up | 3 |
| `FW-firmware` | profile | **text** | 0.589 → 0.774 | 0.185 | 0.582 → 0.760 | 3x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.589 → 0.769 | 0.181 | 0.582 → 0.760 | 2.3x bytes_on_air | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.646 → 0.822 | 0.176 | 0.577 → 0.586 | 4.3x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.646 → 0.822 | 0.176 | 0.577 → 0.586 | 4.3x sr_bytes | down | 5 |
| `SF-place-flat` | place | **held** | 0.572 → 0.747 | 0.175 | 0.574 → 0.584 | 2.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.572 → 0.747 | 0.175 | 0.574 → 0.584 | 2.6x sr_bytes | up | 6 |
| `RF-noise` | noise-profile | **held** | 0.572 → 0.747 | 0.175 | 0.444 → 0.582 | 1.6x sr_airtime | down | 4 |
| `MS-roles` | role-mix | **text** | 0.445 → 0.611 | 0.167 | 0.441 → 0.606 | 1.5x sr_airtime | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.589 → 0.755 | 0.166 | 0.463 → 0.620 | 1.7x sr_airtime | down | 2 |
| `RT-spread` | hop-spread | **text** | 0.473 → 0.589 | 0.115 | 0.461 → 0.582 | 1.4x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.478 → 0.589 | 0.110 | 0.467 → 0.582 | 1.5x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.566 → 0.673 | 0.107 | 0.561 → 0.669 | 2.1x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **text** | 0.445 → 0.550 | 0.106 | 0.441 → 0.538 | 1.5x sr_airtime | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.570 → 0.673 | 0.103 | 0.565 → 0.669 | 2.1x sr_airtime | up | 4 |
| `SC-signing` | signature-policy | **held** | 0.645 → 0.747 | 0.102 | 0.499 → 0.582 | 1.4x sr_bytes | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.537 → 0.636 | 0.100 | 0.529 → 0.632 | 6.5x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.634 → 0.719 | 0.084 | 0.623 → 0.704 | 1.4x sr_airtime | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.690 → 0.747 | 0.057 | 0.582 → 0.583 | 24x sr_airtime | down | 3 |
| `RT-hopassign` | hop-assign | **held** | 0.747 → 0.800 | 0.053 | 0.582 → 0.624 | 1.6x sr_bytes | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.545 → 0.589 | 0.044 | 0.540 → 0.582 | 1.4x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.589 → 0.629 | 0.040 | 0.582 → 0.624 | 3.4x bytes_on_air | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.564 → 0.600 | 0.036 | 0.557 → 0.596 | 9.2x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.589 → 0.625 | 0.036 | 0.582 → 0.620 | 1.3x bytes_on_air | up | 4 |
| `SF-capacity` | capacity | **held** | 0.725 → 0.760 | 0.035 | 0.574 → 0.590 | 4.9x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.725 → 0.760 | 0.035 | 0.574 → 0.590 | 4.9x advert_bytes | down | 5 |
| `SF-servers-flat` | servers | **held** | 0.717 → 0.751 | 0.035 | 0.578 → 0.583 | 8.1x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.717 → 0.751 | 0.035 | 0.578 → 0.583 | 8.1x sr_bytes | up | 4 |
| `SF-cadence` | trigger | **held** | 0.713 → 0.747 | 0.034 | 0.557 → 0.586 | 17x advert_bytes | down | 4 |
| `TH-congestion-input` | congestion-input | **text** | 0.528 → 0.557 | 0.029 | 0.521 → 0.550 | 1.4x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.721 → 0.750 | 0.028 | 0.573 → 0.591 | 1.3x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.721 → 0.750 | 0.028 | 0.573 → 0.591 | 1.3x sr_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.594 → 0.618 | 0.024 | 0.590 → 0.613 | 1.1x sr_bytes | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.589 → 0.612 | 0.023 | 0.582 → 0.583 | 2.7x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.778 → 0.799 | 0.021 | 0.768 → 0.794 | 1.1x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.721 → 0.741 | 0.020 | 0.573 → 0.582 | 3x advert_bytes | up | 3 |
| `SF-window-size` | window-size | **held** | 0.721 → 0.741 | 0.020 | 0.569 → 0.582 | 5.1x advert_bytes | up | 3 |
| `SF-servers-allrouters` | servers | **held** | 0.726 → 0.746 | 0.019 | 0.574 → 0.584 | 2.9x sr_bytes | up | 2 |
| `DM-mode` | dm-mode | **text** | 0.553 → 0.570 | 0.017 | 0.553 → 0.570 | 1.2x sr_airtime | up | 3 |
| `PR-repeats` | extra-repeats | **text** | 0.589 → 0.605 | 0.016 | 0.582 → 0.599 | 1x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.731 → 0.747 | 0.016 | 0.575 → 0.582 | 3.6x advert_bytes | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.732 → 0.747 | 0.015 | 0.579 → 0.585 | 3.1x advert_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.717 → 0.731 | 0.014 | 0.561 → 0.570 | 1.2x sr_bytes | up | 2 |
| `LD-diurnal` | diurnal | **text** | 0.589 → 0.600 | 0.011 | 0.582 → 0.594 | 1.2x sr_bytes | down | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.728 → 0.738 | 0.010 | 0.575 → 0.578 | 5x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.917 → 0.926 | 0.009 | 0.913 → 0.923 | 1.2x bytes_on_air | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.738 → 0.747 | 0.009 | 0.580 → 0.582 | 1x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.561 → 0.570 | 0.009 | 0.561 → 0.570 | 1.1x sr_airtime | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.720 → 0.727 | 0.008 | 0.575 → 0.578 | 1.1x sr_bytes | up | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.606 → 0.612 | 0.006 | 0.577 → 0.583 | 1x sr_bytes | down | 2 |
| `SF-resolve` | resolve | **held** | 0.747 → 0.752 | 0.005 | 0.582 → 0.586 | 5.7x advert_bytes | = | 3 |
| `SF-advert-transport` | advert-transport | **held** | 0.747 → 0.750 | 0.003 | 0.582 → 0.584 | 2.8x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.996 → 0.998 | 0.002 | 0.923 → 0.924 | 1x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.925 → 0.926 | 0.001 | 0.922 → 0.923 | 1.1x sr_bytes | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario alpine`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| sprinkled | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.860 | 0.863 | 0.500 | 1.31x | 14.7/22.5/26.9% | 2.0/4.9% | 3 |
| arms-race | 1 | 0.893 | 0.887 | 0.006 | - | - | 0.981 | 0.981 | 0.702 | 1.23x | 15.5/23.1/28.2% | 1.6/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.778 | 0.742 | 0.036 | - | - | 0.908 | 0.910 | 0.373 | 1.26x | 13.5/21.5/29.1% | 1.8/5.1% | 3 |
| 0.3 | 1 | 0.914 | 0.888 | 0.027 | - | - | 0.984 | 0.986 | 0.768 | 1.23x | 14.9/24.3/29.1% | 1.9/5.4% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.445 | 0.441 | 0.004 | - | - | 0.593 | 0.596 | 0.079 | 1.41x | 16.1/27.8/34.6% | 2.0/6.4% | 3 |
| inverse | 1 | 0.550 | 0.538 | 0.012 | - | - | 0.694 | 0.697 | 0.249 | 1.06x | 10.0/14.6/19.3% | 1.9/3.4% | 3 |
| random | 1 | 0.517 | 0.499 | 0.017 | - | - | 0.679 | 0.685 | 0.160 | 1.06x | 11.2/17.6/22.0% | 1.7/5.1% | 3 |

> role-placement=random: decode_failures 1

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.445 | 0.441 | 0.004 | - | - | 0.593 | 0.596 | 0.079 | 1.41x | 16.1/27.8/34.6% | 2.0/6.4% | 3 |
| all-routers | 1 | 0.743 | 0.739 | 0.005 | - | - | 0.867 | 0.868 | 0.457 | 2.49x | 22.7/32.9/39.8% | 4.0/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.445 | 0.441 | 0.004 | - | - | 0.593 | 0.596 | 0.079 | 1.41x | 16.1/27.8/34.6% | 2.0/6.4% | 3 |
| no-mute | 1 | 0.634 | 0.628 | 0.006 | - | - | 0.756 | 0.761 | 0.292 | 1.25x | 12.1/19.3/24.6% | 1.9/4.6% | 3 |
| all-routers | 1 | 0.743 | 0.739 | 0.005 | - | - | 0.867 | 0.868 | 0.457 | 2.49x | 22.7/32.9/39.8% | 4.0/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.445 | 0.441 | 0.004 | - | - | 0.593 | 0.596 | 0.079 | 1.41x | 16.1/27.8/34.6% | 2.0/6.4% | 3 |
| local-typical | 1 | 0.375 | 0.373 | 0.002 | - | - | 0.514 | 0.523 | 0.000 | 1.35x | 11.3/22.9/27.3% | 2.1/5.6% | 3 |
| basement-heavy | 1 | 0.061 | 0.061 | 0.000 | - | - | 0.057 | 0.114 | 0.000 | 0.55x | 1.5/7.3/9.9% | 0.6/3.0% | 2 |

> siting-mix=local-typical: decode_failures 2

> siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.799 | 0.794 | 0.005 | - | - | 0.954 | 0.954 | 0.000 | 2.46x | 16.8/29.6/37.5% | 1.9/5.5% | 3 |
| inverse | 1 | 0.778 | 0.768 | 0.010 | - | - | 0.951 | 0.952 | 0.000 | 2.33x | 14.7/24.2/31.5% | 1.8/3.6% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.584 | 0.584 | 0.000 | - | - | 0 | 0.000 | 0.272 | 1.20x | 12.1/19.0/24.6% | 1.9/4.7% | 3 |
| sr | 1 | 0.594 | 0.577 | 0.017 | - | - | 0.646 | 0.790 | 0.277 | 1.23x | 12.3/19.4/25.1% | 1.9/4.7% | 3 |

> protocol=sr: decode_failures 34

> slower: 4.61 s per simulated hour against 1.7 over 23 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.570 | 0.565 | 0.005 | - | - | 0.656 | 0.656 | 0.314 | 2.66x | 27.3/42.4/51.9% | 3.7/8.4% | 3 |
| 100 | 1 | 0.673 | 0.669 | 0.004 | - | - | 0.743 | 0.744 | 0.423 | 1.47x | 15.1/23.7/29.2% | 2.2/4.6% | 3 |
| 120 | 1 | 0.673 | 0.669 | 0.004 | - | - | 0.743 | 0.744 | 0.423 | 1.47x | 15.1/23.7/29.2% | 2.2/4.6% | 3 |
| 250 | 1 | 0.673 | 0.669 | 0.004 | - | - | 0.743 | 0.744 | 0.423 | 1.47x | 15.1/23.7/29.2% | 2.2/4.6% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.329 | 0.323 | 0.006 | - | - | 0.537 | 0.542 | 0.179 | 11.83x | 39.2/60.1/70.5% | 4.2/11.3% | 3 |
| 120 | 1 | 0.528 | 0.521 | 0.007 | - | - | 0.759 | 0.760 | 0.246 | 4.70x | 15.7/28.8/35.9% | 1.6/5.5% | 3 |
| 250 | 1 | 0.535 | 0.529 | 0.006 | - | - | 0.756 | 0.757 | 0.256 | 4.61x | 15.5/28.2/35.3% | 1.6/5.3% | 3 |

> max-num-nodes=10: decode_failures 55

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.673 | 0.669 | 0.004 | - | - | 0.743 | 0.744 | 0.423 | 1.47x | 15.1/23.7/29.2% | 2.2/4.6% | 3 |
| baymesh-2026-08 | 1 | 0.673 | 0.669 | 0.004 | - | - | 0.743 | 0.744 | 0.423 | 1.47x | 15.1/23.7/29.2% | 2.2/4.6% | 3 |
| constrained | 1 | 0.566 | 0.561 | 0.005 | - | - | 0.654 | 0.654 | 0.336 | 2.65x | 27.2/42.3/51.9% | 3.8/8.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.719 | 0.704 | 0.015 | - | - | 0.938 | 0.957 | 0.498 | 5.80x | 51.0/68.4/73.3% | 4.2/12.2% | 3 |
| 25 | 1 | 0.719 | 0.704 | 0.015 | - | - | 0.938 | 0.957 | 0.498 | 5.80x | 51.0/68.4/73.3% | 4.2/12.2% | 3 |
| 100 | 1 | 0.719 | 0.704 | 0.015 | - | - | 0.938 | 0.957 | 0.498 | 5.80x | 51.0/68.4/73.3% | 4.2/12.2% | 3 |
| 2000 | 1 | 0.719 | 0.704 | 0.015 | - | - | 0.938 | 0.957 | 0.498 | 5.80x | 51.0/68.4/73.3% | 4.2/12.2% | 3 |

> warm-num-nodes=0: decode_failures 51

> warm-num-nodes=25: decode_failures 51

> warm-num-nodes=100: decode_failures 51

> warm-num-nodes=2000: decode_failures 51

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.511 | 0.500 | 0.011 | - | - | 0.715 | 0.717 | 0.220 | 1.16x | 11.7/18.7/24.5% | 1.8/4.4% | 3 |
| 0.2 | 1 | 0.421 | 0.403 | 0.017 | - | - | 0.644 | 0.651 | 0.164 | 1.08x | 11.1/17.9/23.5% | 1.6/3.9% | 3 |
| 0.3 | 1 | 0.353 | 0.333 | 0.020 | - | - | 0.586 | 0.625 | 0.113 | 0.99x | 10.3/17.2/22.7% | 1.4/3.5% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 19

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.553 | 0.546 | 0.007 | - | - | 0.715 | 0.715 | 0.235 | 1.27x | 12.9/20.3/26.3% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.517 | 0.508 | 0.009 | - | - | 0.697 | 0.699 | 0.210 | 1.30x | 13.4/20.6/26.9% | 1.8/4.5% | 3 |
| 0.3 | 1 | 0.478 | 0.467 | 0.011 | - | - | 0.670 | 0.672 | 0.174 | 1.33x | 13.8/21.6/27.9% | 1.9/4.4% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.499 | 0.489 | 0.010 | - | - | 0.691 | 0.713 | 0.202 | 1.17x | 12.0/19.1/24.8% | 1.8/4.4% | 3 |
| 0.2 | 1 | 0.421 | 0.411 | 0.010 | - | - | 0.630 | 0.651 | 0.187 | 1.11x | 11.5/18.3/24.3% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.326 | 0.315 | 0.011 | - | - | 0.505 | 0.571 | 0.107 | 1.06x | 11.0/18.5/24.4% | 1.5/4.0% | 3 |

> burst-loss=0.1: decode_failures 27

> burst-loss=0.2: decode_failures 9

> burst-loss=0.3: decode_failures 14

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.553 | 0.553 | 0.000 | - | - | 0.713 | 0.714 | 0.266 | 1.47x | 15.3/24.3/31.0% | 2.2/5.9% | 3 |
| directed-with-late-flood | 1 | 0.570 | 0.570 | 0.000 | - | - | 0.723 | 0.724 | 0.264 | 1.40x | 14.2/23.0/29.7% | 2.1/5.7% | 3 |
| m4-early-flood | 1 | 0.565 | 0.565 | 0.000 | - | - | 0.722 | 0.723 | 0.261 | 1.39x | 14.2/22.7/29.3% | 2.1/5.6% | 3 |

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.774 | 0.760 | 0.014 | - | - | 0.931 | 0.936 | 0.442 | 0.73x | 7.8/10.6/13.0% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.673 | 0.667 | 0.006 | - | - | 0.838 | 0.840 | 0.360 | 1.17x | 11.9/20.6/23.9% | 1.6/4.4% | 3 |
| 0.5 | 1 | 0.778 | 0.772 | 0.006 | - | - | 0.919 | 0.920 | 0.407 | 1.04x | 10.7/15.8/18.4% | 1.6/3.9% | 3 |
| 0.75 | 1 | 0.648 | 0.638 | 0.009 | - | - | 0.860 | 0.861 | 0.348 | 0.81x | 8.3/13.6/16.0% | 1.2/3.3% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.680 | 0.675 | 0.006 | - | - | 0.842 | 0.845 | 0.375 | 1.15x | 11.8/20.4/23.8% | 1.5/4.4% | 3 |
| 0.5 | 1 | 0.769 | 0.760 | 0.009 | - | - | 0.912 | 0.912 | 0.406 | 1.03x | 10.7/15.9/18.8% | 1.6/3.9% | 3 |
| 0.75 | 1 | 0.618 | 0.608 | 0.010 | - | - | 0.835 | 0.837 | 0.317 | 0.78x | 7.9/13.6/16.5% | 1.1/3.3% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.629 | 0.624 | 0.005 | - | - | 0.777 | 0.777 | 0.317 | 0.65x | 6.7/11.0/14.5% | 1.0/2.7% | 3 |
| signing=true | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.783 | 0.773 | 0.010 | - | - | 0.936 | 0.941 | 0.449 | 0.73x | 8.1/11.4/14.3% | 1.1/2.7% | 3 |
| 2.5 | 1 | 0.773 | 0.760 | 0.013 | - | - | 0.925 | 0.930 | 0.437 | 0.75x | 8.2/11.3/14.3% | 1.2/2.7% | 3 |
| 2.6 | 1 | 0.785 | 0.775 | 0.010 | - | - | 0.933 | 0.938 | 0.469 | 0.71x | 7.9/11.4/14.3% | 1.1/2.7% | 3 |
| 2.7 | 1 | 0.779 | 0.771 | 0.008 | - | - | 0.931 | 0.935 | 0.453 | 0.73x | 8.4/12.6/16.1% | 1.1/2.9% | 3 |
| 2.8 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.617 | 0.610 | 0.006 | - | - | 0.776 | 0.776 | 0.284 | 0.82x | 8.4/13.3/17.2% | 1.3/3.2% | 3 |
| 900 | 1 | 0.537 | 0.529 | 0.008 | - | - | 0.696 | 0.696 | 0.263 | 1.95x | 19.3/30.9/39.5% | 3.0/7.6% | 3 |
| 300 | 1 | 0.383 | 0.372 | 0.011 | - | - | 0.554 | 0.562 | 0.161 | 4.58x | 42.6/64.7/75.8% | 7.2/15.6% | 3 |

> broadcast-interval-s=300: decode_failures 3

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.715 | 0.713 | 0.003 | - | - | 0.831 | 0.831 | 0.397 | 0.90x | 9.4/14.6/17.5% | 1.4/3.2% | 3 |
| 900 | 1 | 0.655 | 0.652 | 0.003 | - | - | 0.764 | 0.765 | 0.363 | 2.08x | 21.5/33.8/40.6% | 3.0/7.5% | 3 |
| 300 | 1 | 0.433 | 0.425 | 0.008 | - | - | 0.576 | 0.580 | 0.268 | 4.96x | 46.9/69.8/78.1% | 7.3/15.3% | 3 |

> broadcast-interval-s=300: decode_failures 2

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.598 | 0.593 | 0.005 | - | - | 0.751 | 0.753 | 0.292 | 1.15x | 11.5/18.3/23.7% | 1.8/4.5% | 3 |
| sinusoid | 1 | 0.600 | 0.594 | 0.006 | - | - | 0.756 | 0.756 | 0.305 | 1.09x | 11.0/17.3/22.5% | 1.7/4.2% | 3 |
| commuter | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.537 | 0.529 | 0.008 | - | - | 0.696 | 0.696 | 0.263 | 1.95x | 19.3/30.9/39.5% | 3.0/7.6% | 3 |
| 3600 | 1 | 0.617 | 0.610 | 0.006 | - | - | 0.776 | 0.776 | 0.284 | 0.82x | 8.4/13.3/17.2% | 1.3/3.2% | 3 |
| 10800 | 1 | 0.621 | 0.616 | 0.005 | - | - | 0.766 | 0.768 | 0.314 | 0.49x | 5.2/8.2/10.5% | 0.7/1.9% | 3 |
| 43200 | 1 | 0.636 | 0.632 | 0.004 | - | - | 0.786 | 0.788 | 0.317 | 0.33x | 3.5/5.4/7.1% | 0.4/1.3% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.582 | 0.576 | 0.006 | - | - | 0.735 | 0.735 | 0.282 | 1.26x | 12.7/20.2/26.2% | 2.0/4.9% | 3 |
| 1.0 | 1 | 0.574 | 0.569 | 0.005 | - | - | 0.733 | 0.733 | 0.264 | 1.36x | 13.9/22.2/28.6% | 2.1/5.4% | 3 |
| 4.0 | 1 | 0.545 | 0.540 | 0.006 | - | - | 0.705 | 0.705 | 0.246 | 1.64x | 16.7/27.1/35.4% | 2.5/6.7% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.719 | 0.704 | 0.015 | - | - | 0.938 | 0.957 | 0.498 | 5.80x | 51.0/68.4/73.3% | 4.2/12.2% | 3 |
| 1.0 | 1 | 0.634 | 0.623 | 0.011 | - | - | 0.858 | 0.908 | 0.417 | 6.69x | 56.8/71.7/76.6% | 4.9/13.9% | 3 |

> traceroute-per-hour=0.0: decode_failures 51

> traceroute-per-hour=1.0: decode_failures 108

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.506 | 0.502 | 0.003 | - | - | 0.730 | 0.734 | 0.027 | 0.99x | 11.9/20.1/23.0% | 2.4/5.1% | 3 |
| 60 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 90 | 1 | 0.902 | 0.898 | 0.005 | - | - | 0.987 | 0.987 | 0.733 | 1.66x | 16.9/22.5/28.4% | 1.7/4.8% | 3 |
| 120 | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.998 | 0.998 | 0.748 | 2.02x | 19.6/28.1/32.0% | 1.4/5.0% | 3 |
| 150 | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.998 | 0.999 | 0.746 | 2.62x | 25.1/35.7/40.6% | 1.3/5.5% | 3 |

> nodes=90: misdecodes 1

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 120 | 1 | 0.725 | 0.712 | 0.013 | - | - | 0.939 | 0.942 | 0.259 | 2.30x | 15.5/23.2/29.7% | 1.6/5.0% | 3 |
| 250 | 1 | 0.522 | 0.516 | 0.006 | - | - | 0.735 | 0.735 | 0.254 | 5.04x | 16.9/31.2/38.5% | 1.7/5.9% | 3 |
| 500 | 1 | 0.329 | 0.326 | 0.004 | - | - | 0.421 | 0.435 | 0.117 | 9.77x | 18.3/30.3/40.9% | 1.6/6.5% | 3 |

> nodes=120: decode_failures 2

> nodes=500: decode_failures 124

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.737 | 0.723 | 0.013 | - | - | 0.943 | 0.945 | 0.281 | 2.07x | 13.9/21.1/26.6% | 1.4/4.4% | 3 |
| 250 | 1 | 0.528 | 0.521 | 0.007 | - | - | 0.759 | 0.760 | 0.246 | 4.70x | 15.7/28.8/35.9% | 1.6/5.5% | 3 |
| 500 | 1 | 0.328 | 0.325 | 0.003 | - | - | 0.421 | 0.438 | 0.114 | 9.21x | 17.4/28.2/38.5% | 1.6/6.1% | 3 |

> nodes=500: decode_failures 87

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.611 | 0.606 | 0.005 | - | - | 0.756 | 0.759 | 0.261 | 1.25x | 12.6/19.6/25.5% | 2.0/4.8% | 3 |
| baymesh-2026-08 | 1 | 0.445 | 0.441 | 0.004 | - | - | 0.593 | 0.596 | 0.079 | 1.41x | 16.1/27.8/34.6% | 2.0/6.4% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.625 | 0.620 | 0.005 | - | - | 0.755 | 0.757 | 0.274 | 1.28x | 13.1/20.1/25.4% | 2.0/4.6% | 3 |
| baymesh-2026-08 | 1 | 0.466 | 0.463 | 0.002 | - | - | 0.589 | 0.591 | 0.094 | 1.69x | 19.7/32.8/40.2% | 3.0/6.4% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.05 | 1 | 0.590 | 0.585 | 0.005 | - | - | 0.720 | 0.722 | 0.287 | 1.32x | 13.1/22.5/27.9% | 2.1/4.7% | 3 |
| 0.1 | 1 | 0.625 | 0.620 | 0.005 | - | - | 0.733 | 0.733 | 0.321 | 1.42x | 13.9/24.5/30.7% | 2.0/4.5% | 3 |
| 0.2 | 1 | 0.622 | 0.618 | 0.004 | - | - | 0.723 | 0.724 | 0.328 | 1.59x | 15.6/28.0/35.9% | 2.3/4.7% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| local-typical | 1 | 0.370 | 0.367 | 0.003 | - | - | 0.485 | 0.486 | 0.000 | 1.74x | 12.8/25.5/32.6% | 2.5/6.0% | 3 |
| event | 1 | 0.215 | 0.211 | 0.004 | - | - | 0.367 | 0.396 | 0.000 | 1.52x | 7.9/14.5/25.0% | 2.3/5.1% | 3 |
| backbone | 1 | 0.932 | 0.931 | 0.001 | - | - | 0.968 | 0.969 | 0.814 | 1.20x | 20.5/29.4/31.8% | 1.7/5.3% | 3 |

> siting-mix=event: decode_failures 9

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.698 | 0.692 | 0.006 | - | - | 0.804 | 0.808 | 0.179 | 1.27x | 17.7/29.0/32.2% | 2.6/6.4% | 3 |
| 60 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 90 | 1 | 0.711 | 0.693 | 0.019 | - | - | 0.870 | 0.871 | 0.442 | 1.71x | 14.1/19.9/24.1% | 1.7/4.7% | 3 |
| 120 | 1 | 0.725 | 0.712 | 0.013 | - | - | 0.939 | 0.942 | 0.259 | 2.30x | 15.5/23.2/29.7% | 1.6/5.0% | 3 |
| 150 | 1 | 0.641 | 0.633 | 0.008 | - | - | 0.922 | 0.924 | 0.218 | 2.80x | 16.0/23.6/28.7% | 1.6/5.7% | 3 |

> nodes=120: decode_failures 2

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 1.25 | 1 | 0.301 | 0.297 | 0.004 | - | - | 0.493 | 0.494 | 0.000 | 1.23x | 7.8/19.7/23.2% | 1.8/5.4% | 3 |
| 1.5 | 1 | 0.268 | 0.259 | 0.008 | - | - | 0.498 | 0.503 | 0.000 | 1.38x | 8.3/21.9/25.0% | 2.0/6.2% | 3 |
| 2.0 | 1 | 0.125 | 0.122 | 0.003 | - | - | 0.273 | 0.307 | 0.000 | 0.89x | 4.1/9.9/13.6% | 1.4/3.9% | 3 |

> stretch=2.0: decode_failures 10

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| clustered | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.938 | 0.938 | 0.136 | 1.19x | 26.5/34.4/36.8% | 1.6/5.5% | 3 |
| corridor | 1 | 0.609 | 0.592 | 0.017 | - | - | 0.881 | 0.883 | 0.359 | 1.38x | 14.8/20.7/25.3% | 2.1/5.7% | 3 |
| hub | 1 | 0.926 | 0.924 | 0.003 | - | - | 0.980 | 0.981 | 0.721 | 1.20x | 27.9/36.4/38.9% | 1.8/5.8% | 3 |

> topology=clustered: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.570 | 0.570 | 0.000 | - | - | 0.723 | 0.724 | 0.264 | 1.40x | 14.2/23.0/29.7% | 2.1/5.7% | 3 |
| True | 1 | 0.561 | 0.561 | 0.000 | - | - | 0.717 | 0.718 | 0.278 | 1.40x | 14.4/23.0/29.6% | 2.1/5.6% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.561 | 0.561 | 0.000 | - | - | 0.717 | 0.718 | 0.278 | 1.40x | 14.4/23.0/29.6% | 2.1/5.6% | 3 |
| m4-early-flood | 1 | 0.570 | 0.570 | 0.000 | - | - | 0.731 | 0.732 | 0.274 | 1.40x | 14.4/23.0/29.6% | 2.1/5.7% | 3 |

> faster: 1.21 s per simulated hour against 2.54 over 23 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.584 | 0.584 | 0.000 | - | - | 0 | 0.000 | 0.272 | 1.20x | 12.1/19.0/24.6% | 1.9/4.7% | 3 |
| chain | 1 | 0.576 | 0.573 | 0.003 | - | - | 0.702 | 0.729 | 0.278 | 1.40x | 14.6/23.3/29.8% | 2.1/5.6% | 3 |
| sr | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| True | 1 | 0.605 | 0.599 | 0.006 | - | - | 0.748 | 0.750 | 0.312 | 1.24x | 12.4/19.8/25.4% | 2.0/4.8% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.998 | 0.998 | 0.748 | 2.02x | 19.6/28.1/32.0% | 1.4/5.0% | 3 |
| True | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.996 | 0.997 | 0.759 | 2.07x | 19.8/28.4/32.3% | 1.4/5.0% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.150 | 0.149 | 0.001 | - | - | 0.357 | 0.359 | 0.000 | 0.05x | 0.2/0.5/0.9% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.271 | 0.268 | 0.003 | - | - | 0.524 | 0.525 | 0.000 | 0.20x | 1.3/3.1/3.9% | 0.3/1.0% | 3 |
| LONG_TURBO | 1 | 0.497 | 0.488 | 0.009 | - | - | 0.649 | 0.651 | 0.168 | 1.18x | 9.3/17.0/22.1% | 1.6/4.7% | 3 |

> preset=MEDIUM_TURBO: decode_failures 1

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.644 | 0.639 | 0.005 | - | - | 0.775 | 0.775 | 0.381 | 1.06x | 12.7/19.4/24.8% | 1.5/4.7% | 3 |
| 1.0 | 1 | 0.777 | 0.773 | 0.004 | - | - | 0.870 | 0.871 | 0.614 | 0.91x | 15.5/21.8/26.2% | 1.2/4.8% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.227 | 0.222 | 0.005 | - | - | 0.473 | 0.473 | 0.000 | 0.11x | 0.6/1.7/2.3% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| LITE_FAST | 1 | 0.514 | 0.508 | 0.006 | - | - | 0.697 | 0.700 | 0.213 | 0.90x | 8.0/14.6/18.5% | 1.2/3.7% | 3 |
| NARROW_SLOW | 1 | 0.558 | 0.552 | 0.007 | - | - | 0.732 | 0.732 | 0.271 | 1.13x | 10.6/18.1/24.0% | 1.6/4.6% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| temporal | 1 | 0.487 | 0.481 | 0.006 | - | - | 0.667 | 0.668 | 0.160 | 1.23x | 11.7/20.1/26.3% | 1.8/4.8% | 3 |
| transient | 1 | 0.579 | 0.573 | 0.006 | - | - | 0.735 | 0.735 | 0.275 | 1.23x | 12.3/19.5/25.4% | 1.9/4.8% | 3 |
| periodic | 1 | 0.448 | 0.444 | 0.004 | - | - | 0.572 | 0.576 | 0.182 | 1.13x | 11.5/18.2/23.6% | 1.7/4.1% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.227 | 0.222 | 0.005 | - | - | 0.473 | 0.473 | 0.000 | 0.11x | 0.6/1.7/2.3% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| LONG_MODERATE | 1 | 0.670 | 0.658 | 0.012 | - | - | 0.768 | 0.771 | 0.424 | 3.43x | 38.4/56.5/61.8% | 5.2/12.1% | 3 |

> faster: 1.28 s per simulated hour against 3.03 over 23 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.054 | 0.053 | 0.002 | - | - | 0.136 | 0.145 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.150 | 0.149 | 0.001 | - | - | 0.357 | 0.359 | 0.000 | 0.05x | 0.2/0.5/0.9% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| LONG_TURBO | 1 | 0.497 | 0.488 | 0.009 | - | - | 0.649 | 0.651 | 0.168 | 1.18x | 9.3/17.0/22.1% | 1.6/4.7% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.598 | 0.589 | 0.009 | - | - | 0.747 | 0.749 | 0.319 | 1.72x | 16.5/25.6/32.6% | 2.6/6.4% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.526 | 0.521 | 0.004 | - | - | 0.670 | 0.673 | 0.225 | 1.19x | 12.3/19.5/25.1% | 1.8/4.6% | 3 |
| 10000 | 1 | 0.448 | 0.444 | 0.004 | - | - | 0.572 | 0.576 | 0.182 | 1.13x | 11.5/18.2/23.6% | 1.7/4.1% | 3 |
| 4000 | 1 | 0.256 | 0.253 | 0.003 | - | - | 0.335 | 0.366 | 0.072 | 1.02x | 10.5/17.2/22.0% | 1.5/3.4% | 3 |
| 2000 | 1 | 0.063 | 0.063 | 0.000 | - | - | 0.076 | 0.125 | 0.020 | 0.71x | 7.1/12.7/16.9% | 1.1/2.2% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.268 | 0.259 | 0.008 | - | - | 0.498 | 0.503 | 0.000 | 1.38x | 8.3/21.9/25.0% | 2.0/6.2% | 3 |
| 1.0 | 1 | 0.587 | 0.577 | 0.009 | - | - | 0.733 | 0.733 | 0.213 | 0.97x | 12.7/19.5/23.1% | 1.3/4.5% | 3 |

> faster: 1.46 s per simulated hour against 2.97 over 23 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 22 | 1 | 0.247 | 0.241 | 0.006 | - | - | 0.480 | 0.483 | 0.000 | 1.34x | 7.5/18.8/23.3% | 1.8/5.7% | 3 |
| 17 | 1 | 0.139 | 0.137 | 0.002 | - | - | 0.303 | 0.319 | 0.000 | 0.97x | 4.5/10.6/14.3% | 1.6/3.7% | 3 |
| 14 | 1 | 0.078 | 0.077 | 0.001 | - | - | 0.181 | 0.186 | 0.000 | 0.69x | 2.5/7.4/10.6% | 0.9/3.0% | 3 |

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.998 | 0.998 | 0.748 | 2.02x | 19.6/28.1/32.0% | 1.4/5.0% | 3 |
| True | 1 | 0.917 | 0.913 | 0.004 | - | - | 0.998 | 0.998 | 0.733 | 2.43x | 23.1/33.1/36.7% | 1.7/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.594 | 0.590 | 0.005 | - | - | 0.745 | 0.746 | 0.283 | 1.30x | 12.5/21.1/27.0% | 2.0/4.7% | 3 |
| True | 1 | 0.618 | 0.613 | 0.005 | - | - | 0.739 | 0.739 | 0.300 | 1.36x | 13.4/22.1/27.5% | 2.0/4.7% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| random | 1 | 0.633 | 0.624 | 0.009 | - | - | 0.800 | 0.801 | 0.239 | 1.32x | 13.8/22.0/27.2% | 1.9/5.0% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.473 | 0.461 | 0.013 | - | - | 0.664 | 0.667 | 0.196 | 1.25x | 12.7/22.6/29.1% | 1.8/5.6% | 3 |
| 7 | 1 | 0.691 | 0.688 | 0.004 | - | - | 0.799 | 0.800 | 0.406 | 1.32x | 13.7/21.2/25.9% | 2.0/4.7% | 3 |
| 15 | 1 | 0.730 | 0.729 | 0.000 | - | - | 0.798 | 0.799 | 0.470 | 1.34x | 13.8/21.6/26.1% | 2.0/4.7% | 3 |
| 32 | 1 | 0.726 | 0.725 | 0.000 | - | - | 0.789 | 0.790 | 0.451 | 1.34x | 13.9/21.5/26.0% | 2.0/4.8% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.473 | 0.461 | 0.013 | - | - | 0.664 | 0.667 | 0.196 | 1.25x | 12.7/22.6/29.1% | 1.8/5.6% | 3 |
| 5 | 1 | 0.606 | 0.598 | 0.007 | - | - | 0.747 | 0.750 | 0.323 | 1.26x | 13.3/20.9/26.2% | 1.8/4.9% | 3 |
| 7 | 1 | 0.691 | 0.688 | 0.004 | - | - | 0.799 | 0.800 | 0.406 | 1.32x | 13.7/21.2/25.9% | 2.0/4.7% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| KNOWN_ONLY | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.583 | 0.583 | 0.000 | - | - | 0.690 | 0.736 | 0.297 | 1.20x | 12.0/19.0/24.6% | 1.9/4.7% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.473 | 0.461 | 0.013 | - | - | 0.664 | 0.667 | 0.196 | 1.25x | 12.7/22.6/29.1% | 1.8/5.6% | 3 |
| True | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| BALANCED | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| STRICT | 1 | 0.499 | 0.499 | 0.000 | - | - | 0.645 | 0.647 | 0.203 | 1.36x | 14.1/22.4/28.5% | 2.0/5.3% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| dm | 1 | 0.591 | 0.584 | 0.007 | - | - | 0.750 | 0.752 | 0.275 | 1.22x | 12.2/19.2/25.2% | 1.9/4.7% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.583 | 0.575 | 0.007 | - | - | 0.738 | 0.738 | 0.269 | 1.23x | 12.4/19.8/25.6% | 1.9/4.8% | 3 |
| local | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| time | 1 | 0.581 | 0.575 | 0.006 | - | - | 0.731 | 0.733 | 0.287 | 1.26x | 12.7/20.3/26.2% | 2.0/4.9% | 3 |
| window | 1 | 0.588 | 0.582 | 0.006 | - | - | 0.741 | 0.742 | 0.278 | 1.23x | 12.3/19.5/25.2% | 1.9/4.7% | 3 |

> bucket-mode=global: misdecodes 34

> bucket-mode=time: misdecodes 48

> bucket-mode=window: misdecodes 22

> faster: 0.613 s per simulated hour against 1.63 over 23 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.581 | 0.576 | 0.004 | - | - | 0.728 | 0.729 | 0.278 | 1.37x | 14.1/22.2/28.3% | 2.0/5.4% | 3 |
| 1800 | 1 | 0.581 | 0.575 | 0.006 | - | - | 0.731 | 0.733 | 0.287 | 1.26x | 12.7/20.3/26.2% | 2.0/4.9% | 3 |
| 3600 | 1 | 0.582 | 0.578 | 0.004 | - | - | 0.738 | 0.741 | 0.280 | 1.22x | 12.2/19.5/25.3% | 1.9/4.8% | 3 |

> time-bucket-s=600: misdecodes 135

> time-bucket-s=1800: misdecodes 48

> time-bucket-s=3600: misdecodes 24

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| interval | 1 | 0.566 | 0.558 | 0.008 | - | - | 0.717 | 0.717 | 0.276 | 1.65x | 17.0/27.5/35.9% | 2.2/8.2% | 3 |
| aimd | 1 | 0.589 | 0.586 | 0.004 | - | - | 0.730 | 0.752 | 0.277 | 1.24x | 12.4/19.8/25.6% | 1.9/4.8% | 3 |
| bucket+interval | 1 | 0.564 | 0.557 | 0.007 | - | - | 0.713 | 0.714 | 0.279 | 1.68x | 17.5/27.9/36.5% | 2.3/8.3% | 3 |

> trigger=interval: misdecodes 21

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 17

> trigger=bucket+interval: misdecodes 21

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.596 | 0.590 | 0.007 | - | - | 0.760 | 0.760 | 0.288 | 1.23x | 12.3/19.7/25.8% | 1.9/4.8% | 3 |
| 8 | 1 | 0.591 | 0.586 | 0.006 | - | - | 0.744 | 0.746 | 0.298 | 1.22x | 12.2/19.3/25.2% | 1.9/4.7% | 3 |
| 16 | 1 | 0.593 | 0.587 | 0.006 | - | - | 0.745 | 0.745 | 0.300 | 1.23x | 12.3/19.3/25.2% | 1.9/4.7% | 3 |
| 32 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 50 | 1 | 0.579 | 0.574 | 0.005 | - | - | 0.725 | 0.727 | 0.285 | 1.24x | 12.4/19.8/25.6% | 1.9/4.8% | 3 |

> capacity=4: decode_failures 52

> capacity=8: decode_failures 7

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.596 | 0.590 | 0.007 | - | - | 0.760 | 0.760 | 0.288 | 1.23x | 12.3/19.7/25.8% | 1.9/4.8% | 3 |
| 8 | 1 | 0.591 | 0.586 | 0.006 | - | - | 0.744 | 0.746 | 0.298 | 1.22x | 12.2/19.3/25.2% | 1.9/4.7% | 3 |
| 16 | 1 | 0.593 | 0.587 | 0.006 | - | - | 0.745 | 0.745 | 0.300 | 1.23x | 12.3/19.3/25.2% | 1.9/4.7% | 3 |
| 32 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 50 | 1 | 0.579 | 0.574 | 0.005 | - | - | 0.725 | 0.727 | 0.285 | 1.24x | 12.4/19.8/25.6% | 1.9/4.8% | 3 |

> capacity=4: decode_failures 52

> capacity=8: decode_failures 7

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.578 | 0.573 | 0.005 | - | - | 0.721 | 0.727 | 0.286 | 1.21x | 12.1/19.4/25.1% | 1.9/4.7% | 3 |
| 16 | 1 | 0.586 | 0.580 | 0.006 | - | - | 0.741 | 0.741 | 0.269 | 1.22x | 12.2/19.4/25.2% | 1.9/4.8% | 3 |
| 32 | 1 | 0.588 | 0.582 | 0.006 | - | - | 0.741 | 0.742 | 0.278 | 1.23x | 12.3/19.5/25.2% | 1.9/4.7% | 3 |

> capacity=8: misdecodes 20

> capacity=8: decode_failures 12

> capacity=16: misdecodes 2

> capacity=32: misdecodes 22

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.564 | 0.557 | 0.007 | - | - | 0.713 | 0.714 | 0.279 | 1.68x | 17.5/27.9/36.5% | 2.3/8.3% | 3 |
| 02-06 | 1 | 0.592 | 0.587 | 0.004 | - | - | 0.729 | 0.747 | 0.291 | 1.26x | 12.7/20.3/26.3% | 2.0/4.9% | 3 |
| 00-08 | 1 | 0.600 | 0.596 | 0.004 | - | - | 0.743 | 0.760 | 0.291 | 1.31x | 13.2/21.2/27.6% | 2.0/5.3% | 3 |

> catch-up-hours=: misdecodes 21

> catch-up-hours=02-06: decode_failures 31

> catch-up-hours=00-08: decode_failures 29

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.583 | 0.581 | 0.002 | - | - | 0.724 | 0.725 | 0.275 | 1.21x | 12.2/19.4/24.9% | 1.9/4.8% | 3 |
| 2 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 3 | 1 | 0.594 | 0.577 | 0.017 | - | - | 0.646 | 0.790 | 0.277 | 1.23x | 12.3/19.4/25.1% | 1.9/4.7% | 3 |
| 4 | 1 | 0.631 | 0.586 | 0.044 | - | - | 0.822 | 0.891 | 0.287 | 1.24x | 12.7/19.8/25.4% | 1.9/4.9% | 3 |

> hops-apart=3: decode_failures 34

> hops-apart=4: decode_failures 23

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.583 | 0.581 | 0.002 | - | - | 0.724 | 0.725 | 0.275 | 1.21x | 12.2/19.4/24.9% | 1.9/4.8% | 3 |
| 2 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 3 | 1 | 0.594 | 0.577 | 0.017 | - | - | 0.646 | 0.790 | 0.277 | 1.23x | 12.3/19.4/25.1% | 1.9/4.7% | 3 |
| 4 | 1 | 0.631 | 0.586 | 0.044 | - | - | 0.822 | 0.891 | 0.287 | 1.24x | 12.7/19.8/25.4% | 1.9/4.9% | 3 |
| 5 | 1 | 0.609 | 0.580 | 0.029 | - | - | 0.660 | 0.932 | 0.269 | 1.22x | 12.4/19.4/25.0% | 1.9/4.8% | 3 |

> hops-apart=3: decode_failures 34

> hops-apart=4: decode_failures 23

> hops-apart=5: decode_failures 22

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.578 | 0.573 | 0.005 | - | - | 0.721 | 0.722 | 0.281 | 1.23x | 12.3/19.6/25.3% | 1.9/4.8% | 3 |
| 30 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 120 | 1 | 0.596 | 0.590 | 0.005 | - | - | 0.750 | 0.751 | 0.277 | 1.22x | 12.2/19.5/25.3% | 1.9/4.8% | 3 |
| 600 | 1 | 0.598 | 0.591 | 0.006 | - | - | 0.742 | 0.744 | 0.288 | 1.24x | 12.3/19.6/25.4% | 1.9/4.8% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.578 | 0.573 | 0.005 | - | - | 0.721 | 0.722 | 0.281 | 1.23x | 12.3/19.6/25.3% | 1.9/4.8% | 3 |
| 30 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 120 | 1 | 0.596 | 0.590 | 0.005 | - | - | 0.750 | 0.751 | 0.277 | 1.22x | 12.2/19.5/25.3% | 1.9/4.8% | 3 |
| 600 | 1 | 0.598 | 0.591 | 0.006 | - | - | 0.742 | 0.744 | 0.288 | 1.24x | 12.3/19.6/25.4% | 1.9/4.8% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.595 | 0.582 | 0.013 | - | - | 0.572 | 0.881 | 0.280 | 1.24x | 12.4/19.9/25.5% | 1.9/5.0% | 3 |
| routers | 1 | 0.578 | 0.574 | 0.003 | - | - | 0.726 | 0.727 | 0.276 | 1.22x | 12.2/19.6/25.1% | 1.9/4.8% | 3 |
| alternate-routers | 1 | 0.583 | 0.577 | 0.006 | - | - | 0.727 | 0.727 | 0.279 | 1.23x | 12.3/19.8/25.4% | 1.9/4.8% | 3 |
| beside-router | 1 | 0.595 | 0.578 | 0.017 | - | - | 0.743 | 0.745 | 0.284 | 1.23x | 12.3/19.9/25.6% | 2.0/5.0% | 3 |
| random-clients | 1 | 0.595 | 0.584 | 0.011 | - | - | 0.713 | 0.738 | 0.279 | 1.23x | 12.4/19.9/25.5% | 1.9/4.9% | 3 |
| hops-apart | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

> place=spread: decode_failures 7

> place=random-clients: decode_failures 32

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.595 | 0.582 | 0.013 | - | - | 0.572 | 0.881 | 0.280 | 1.24x | 12.4/19.9/25.5% | 1.9/5.0% | 3 |
| routers | 1 | 0.578 | 0.574 | 0.003 | - | - | 0.726 | 0.727 | 0.276 | 1.22x | 12.2/19.6/25.1% | 1.9/4.8% | 3 |
| alternate-routers | 1 | 0.583 | 0.577 | 0.006 | - | - | 0.727 | 0.727 | 0.279 | 1.23x | 12.3/19.8/25.4% | 1.9/4.8% | 3 |
| beside-router | 1 | 0.595 | 0.578 | 0.017 | - | - | 0.743 | 0.745 | 0.284 | 1.23x | 12.3/19.9/25.6% | 2.0/5.0% | 3 |
| random-clients | 1 | 0.595 | 0.584 | 0.011 | - | - | 0.713 | 0.738 | 0.279 | 1.23x | 12.4/19.9/25.5% | 1.9/4.9% | 3 |
| hops-apart | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

> place=spread: decode_failures 7

> place=random-clients: decode_failures 32

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| broadcast | 1 | 0.612 | 0.583 | 0.029 | - | - | 0.744 | 0.744 | 0.284 | 1.27x | 12.8/20.5/26.4% | 1.9/5.0% | 3 |

> faster: 0.926 s per simulated hour against 1.91 over 23 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| heard | 1 | 0.586 | 0.580 | 0.006 | - | - | 0.738 | 0.738 | 0.285 | 1.23x | 12.3/19.5/25.3% | 1.9/4.8% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.612 | 0.583 | 0.029 | - | - | 0.744 | 0.744 | 0.284 | 1.27x | 12.8/20.5/26.4% | 1.9/5.0% | 3 |
| heard | 1 | 0.606 | 0.577 | 0.029 | - | - | 0.740 | 0.740 | 0.288 | 1.27x | 12.9/20.6/26.5% | 1.9/5.0% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| enum | 1 | 0.592 | 0.586 | 0.006 | - | - | 0.752 | 0.752 | 0.271 | 1.22x | 12.0/19.3/25.3% | 1.9/4.7% | 3 |
| hybrid | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.578 | 0.574 | 0.003 | - | - | 0.726 | 0.727 | 0.276 | 1.22x | 12.2/19.6/25.1% | 1.9/4.8% | 3 |
| 6 | 1 | 0.591 | 0.584 | 0.007 | - | - | 0.746 | 0.746 | 0.290 | 1.24x | 12.4/20.3/25.9% | 1.9/5.1% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.582 | 0.578 | 0.005 | - | - | 0.717 | 0.717 | 0.270 | 1.21x | 12.1/19.3/24.9% | 1.9/4.7% | 2 |
| 3 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 5 | 1 | 0.586 | 0.578 | 0.008 | - | - | 0.737 | 0.738 | 0.298 | 1.25x | 12.6/20.0/25.9% | 1.9/4.8% | 5 |
| 8 | 1 | 0.597 | 0.583 | 0.014 | - | - | 0.751 | 0.755 | 0.272 | 1.30x | 13.2/20.8/27.0% | 1.9/5.1% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.582 | 0.578 | 0.005 | - | - | 0.717 | 0.717 | 0.270 | 1.21x | 12.1/19.3/24.9% | 1.9/4.7% | 2 |
| 3 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 5 | 1 | 0.586 | 0.578 | 0.008 | - | - | 0.737 | 0.738 | 0.298 | 1.25x | 12.6/20.0/25.9% | 1.9/4.8% | 5 |
| 8 | 1 | 0.597 | 0.583 | 0.014 | - | - | 0.751 | 0.755 | 0.272 | 1.30x | 13.2/20.8/27.0% | 1.9/5.1% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| True | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.583 | 0.576 | 0.007 | - | - | 0.720 | 0.721 | 0.282 | 1.16x | 11.5/18.0/23.4% | 1.9/4.4% | 3 |
| 1 | 1 | 0.583 | 0.575 | 0.007 | - | - | 0.727 | 0.729 | 0.286 | 1.17x | 11.6/18.3/23.8% | 1.8/4.5% | 3 |
| 2 | 1 | 0.584 | 0.578 | 0.005 | - | - | 0.727 | 0.730 | 0.291 | 1.16x | 11.6/18.1/23.3% | 1.8/4.4% | 3 |
| 4 | 1 | 0.584 | 0.578 | 0.005 | - | - | 0.727 | 0.730 | 0.291 | 1.16x | 11.6/18.1/23.3% | 1.8/4.4% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.588 | 0.582 | 0.006 | - | - | 0.738 | 0.738 | 0.299 | 1.23x | 12.2/19.6/25.3% | 1.9/4.8% | 3 |
| 24 | 1 | 0.590 | 0.585 | 0.005 | - | - | 0.745 | 0.746 | 0.279 | 1.24x | 12.5/19.8/25.6% | 2.0/4.8% | 3 |
| 32 | 1 | 0.589 | 0.582 | 0.007 | - | - | 0.747 | 0.748 | 0.286 | 1.23x | 12.4/19.6/25.5% | 2.0/4.8% | 3 |
| 64 | 1 | 0.584 | 0.579 | 0.005 | - | - | 0.732 | 0.733 | 0.288 | 1.24x | 12.4/19.6/25.3% | 1.9/4.8% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.575 | 0.569 | 0.006 | - | - | 0.731 | 0.732 | 0.275 | 1.28x | 13.0/20.8/26.6% | 1.9/5.0% | 3 |
| 16 | 1 | 0.577 | 0.571 | 0.006 | - | - | 0.721 | 0.722 | 0.272 | 1.23x | 12.3/19.5/25.3% | 1.9/4.8% | 3 |
| 32 | 1 | 0.588 | 0.582 | 0.006 | - | - | 0.741 | 0.742 | 0.278 | 1.23x | 12.3/19.5/25.2% | 1.9/4.7% | 3 |

> window-size=8: misdecodes 113

> window-size=16: misdecodes 24

> window-size=32: misdecodes 22

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.998 | 0.998 | 0.748 | 2.02x | 19.6/28.1/32.0% | 1.4/5.0% | 3 |
| True | 1 | 0.720 | 0.707 | 0.014 | - | - | 0.938 | 0.951 | 0.494 | 5.76x | 50.8/68.1/73.0% | 4.1/12.0% | 3 |

> no-congestion-scaling=True: decode_failures 26

> faster: 9.13 s per simulated hour against 18.7 over 23 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.528 | 0.521 | 0.007 | - | - | 0.759 | 0.760 | 0.246 | 4.70x | 15.7/28.8/35.9% | 1.6/5.5% | 3 |
| truesize | 1 | 0.557 | 0.550 | 0.007 | - | - | 0.784 | 0.785 | 0.269 | 3.61x | 11.8/22.7/29.3% | 1.2/4.6% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.998 | 0.998 | 0.742 | 1.96x | 18.7/27.1/30.4% | 1.3/4.7% | 3 |
| adaptive | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.998 | 0.998 | 0.748 | 2.02x | 19.6/28.1/32.0% | 1.4/5.0% | 3 |

