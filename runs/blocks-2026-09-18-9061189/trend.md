# Sweep blocks-2026-09-18-9061189

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 9061189 · seeds 9061189
- **blocks** 87 run
- **compute** 10.4 h of simulator time across every cell
- **generated** 2026-09-18T08:38:23+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>80 warnings</summary>

- AD-amplifiers: amplifier-mix=sprinkled: decode_failures 34
- AD-amplifiers: slower: 4.72 s per simulated hour against 1.63 over 28 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-amplify-worst: amplify-worst=0.1: decode_failures 36
- AD-amplify-worst: slower: 3.76 s per simulated hour against 1.72 over 28 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=inverse: decode_failures 1
- BL-control: protocol=sr: decode_failures 33
- BL-control: slower: 4.65 s per simulated hour against 1.72 over 28 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 81
- DB-hotstore-stress: max-num-nodes=120: decode_failures 5
- DB-hotstore-stress: max-num-nodes=250: decode_failures 10
- DB-warm: warm-num-nodes=0: decode_failures 102
- DB-warm: warm-num-nodes=25: decode_failures 102
- DB-warm: warm-num-nodes=100: decode_failures 102
- DB-warm: warm-num-nodes=2000: decode_failures 102
- DG-burst: burst-loss=0.2: decode_failures 1
- DG-burst: burst-loss=0.3: decode_failures 13
- DG-outage: burst-loss=0.1: decode_failures 5
- DG-outage: burst-loss=0.2: decode_failures 31
- DG-outage: burst-loss=0.3: decode_failures 16
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 4
- LD-chatty: broadcast-interval-s=300: decode_failures 16
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 102
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 91
- MS-hopscale: nodes=120: decode_failures 1
- MS-hopscale: nodes=250: decode_failures 157
- MS-hopscale: nodes=500: decode_failures 43
- MS-oversubscribed: nodes=120: decode_failures 1
- MS-oversubscribed: nodes=250: decode_failures 5
- MS-oversubscribed: nodes=500: decode_failures 109
- MS-size: nodes=120: decode_failures 1
- MS-stretch: stretch=1.5: decode_failures 11
- MS-topology: topology=clustered: decode_failures 18
- RF-eu-presets: preset=SHORT_FAST: decode_failures 6
- RF-preset: preset=SHORT_FAST: decode_failures 6
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 11
- RF-txpower: tx-power=22: decode_failures 14
- RT-hoplimit: hop-limit=3: decode_failures 2
- RT-hopspread: hop-limit=3: decode_failures 2
- RT-spread: hop-spread=False: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 33
- SF-bucket-mode: bucket-mode=time: misdecodes 28
- SF-bucket-mode: bucket-mode=window: misdecodes 10
- SF-bucket-time: time-bucket-s=600: misdecodes 144
- SF-bucket-time: time-bucket-s=1800: misdecodes 28
- SF-bucket-time: time-bucket-s=3600: misdecodes 5
- SF-cadence: trigger=interval: misdecodes 25
- SF-cadence: trigger=aimd: misdecodes 5
- SF-cadence: trigger=aimd: decode_failures 4
- SF-cadence: trigger=bucket+interval: misdecodes 22
- SF-capacity-local: capacity=4: decode_failures 78
- SF-capacity-local: capacity=8: decode_failures 32
- SF-capacity: capacity=4: decode_failures 78
- SF-capacity: capacity=8: decode_failures 32
- SF-capacity-window: capacity=8: misdecodes 19
- SF-capacity-window: capacity=8: decode_failures 27
- SF-capacity-window: capacity=16: misdecodes 8
- SF-capacity-window: capacity=16: decode_failures 1
- SF-capacity-window: capacity=32: misdecodes 10
- SF-catchup: catch-up-hours=: misdecodes 22
- SF-catchup: catch-up-hours=02-06: decode_failures 22
- SF-catchup: catch-up-hours=00-08: decode_failures 22
- SF-hops-flat: hops-apart=3: decode_failures 33
- SF-hops-flat: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=3: decode_failures 33
- SF-hops-spread: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=5: decode_failures 22
- SF-place-flat: place=spread: decode_failures 16
- SF-place-flat: place=alternate-routers: decode_failures 6
- SF-place-flat: place=random-clients: decode_failures 19
- SF-place-spread: place=spread: decode_failures 16
- SF-place-spread: place=alternate-routers: decode_failures 6
- SF-place-spread: place=random-clients: decode_failures 19
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 13
- SF-replay-order: replay-ordering=heard: misdecodes 14
- SF-window-size: window-size=8: misdecodes 100
- SF-window-size: window-size=16: misdecodes 35
- SF-window-size: window-size=32: misdecodes 10
- TH-congestion-input: congestion-input=hotstore: decode_failures 5
- TH-congestion-input: congestion-input=truesize: decode_failures 1
- TH-congestion: no-congestion-scaling=True: decode_failures 93

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-amplifiers` | 4.72 | 1.63 | 2.90x | 28 |
| `BL-control` | 4.65 | 1.72 | 2.70x | 28 |
| `AD-amplify-worst` | 3.76 | 1.72 | 2.18x | 28 |
| `SF-hops-flat` | 5.57 | 3.45 | 1.62x | 28 |
| `MS-oversubscribed` | 29.7 | 19.6 | 1.52x | 28 |
| `SF-replay-order` | 1.12 | 1.68 | 0.67x | 28 |
| `RF-duct` | 1.17 | 1.76 | 0.67x | 28 |
| `SF-sr-retries` | 1.05 | 1.61 | 0.65x | 28 |
| `RF-preset` | 1.96 | 3.01 | 0.65x | 28 |
| `DG-burst` | 3.21 | 4.96 | 0.65x | 28 |
| `RF-noise` | 3.36 | 5.27 | 0.64x | 28 |
| `DG-outage` | 4.56 | 7.18 | 0.64x | 28 |
| `SF-jitter-local` | 1.12 | 1.78 | 0.63x | 28 |
| `FW-mixed` | 1.05 | 1.67 | 0.63x | 28 |
| `RF-preset-turbo` | 0.953 | 1.56 | 0.61x | 24 |
| `FW-signing-cost` | 0.971 | 1.6 | 0.61x | 28 |
| `PR-dmmode-cr` | 1.47 | 2.57 | 0.57x | 28 |
| `RF-pulse` | 0.919 | 1.67 | 0.55x | 28 |
| `LD-chatty-hops` | 2.39 | 4.41 | 0.54x | 28 |
| `RF-bw500` | 1 | 1.85 | 0.54x | 28 |
| `DM-mode` | 1.63 | 3.19 | 0.51x | 28 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.848 | 0.848 | 0.601 → 0.632 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.123 → 0.959 | 0.836 | 0.122 → 0.956 | 4.6x sr_airtime | up | 4 |
| `MS-stretch` | stretch | **held** | 0.039 → 0.848 | 0.809 | 0.076 → 0.632 | 1.2e+02x sr_airtime | down | 4 |
| `BL-control` | protocol | **held** | 0 → 0.744 | 0.744 | 0.613 → 0.616 | 1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.110 → 0.848 | 0.738 | 0.058 → 0.632 | 9x advert_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.158 → 0.848 | 0.690 | 0.051 → 0.632 | 6x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.092 → 0.764 | 0.672 | 0.068 → 0.565 | 1e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.152 → 0.722 | 0.570 | 0.042 → 0.465 | 6.4x sr_bytes | down | 3 |
| `RF-eu-presets` | preset | **held** | 0.302 → 0.848 | 0.545 | 0.153 → 0.632 | 2.9x advert_bytes | up | 4 |
| `RF-preset` | preset | **held** | 0.302 → 0.848 | 0.545 | 0.153 → 0.636 | 3.6x sr_airtime | up | 3 |
| `RF-bw500` | preset | **held** | 0.178 → 0.711 | 0.533 | 0.088 → 0.475 | 4.4x sr_bytes | up | 3 |
| `MS-topology` | topology | **held** | 0.513 → 0.967 | 0.455 | 0.514 → 0.897 | 2.8x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **held** | 0.454 → 0.880 | 0.427 | 0.315 → 0.666 | 12x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.440 → 0.866 | 0.425 | 0.316 → 0.667 | 4.5x bytes_on_air | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.250 → 0.637 | 0.387 | 0.244 → 0.620 | 2.9x sr_airtime | up | 2 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.485 → 0.849 | 0.364 | 0.362 → 0.720 | 12x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.425 → 0.757 | 0.332 | 0.390 → 0.754 | 2.8x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.514 → 0.842 | 0.328 | 0.313 → 0.496 | 6.3x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.634 → 0.945 | 0.311 | 0.627 → 0.943 | 5.3x sr_airtime | up | 5 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.551 → 0.862 | 0.311 | 0.348 → 0.667 | 9.3x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.349 → 0.647 | 0.297 | 0.328 → 0.632 | 2.2x sr_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.567 → 0.848 | 0.280 | 0.615 → 0.632 | 2.3x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.567 → 0.848 | 0.280 | 0.615 → 0.632 | 2.3x sr_bytes | up | 6 |
| `DG-burst` | burst-loss | **text** | 0.374 → 0.647 | 0.273 | 0.345 → 0.632 | 1.9x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.485 → 0.754 | 0.269 | 0.465 → 0.742 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.485 → 0.754 | 0.269 | 0.465 → 0.742 | 2.4x bytes_on_air | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.425 → 0.693 | 0.268 | 0.390 → 0.686 | 2.1x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.425 → 0.647 | 0.222 | 0.390 → 0.632 | 1.4x sr_bytes | up | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.647 → 0.865 | 0.218 | 0.632 → 0.861 | 2.2x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.706 → 0.922 | 0.216 | 0.690 → 0.918 | 3.6x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.758 → 0.968 | 0.210 | 0.632 → 0.830 | 2x sr_airtime | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.641 → 0.848 | 0.206 | 0.462 → 0.632 | 1.5x sr_airtime | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.653 → 0.848 | 0.195 | 0.615 → 0.632 | 5.9x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.653 → 0.848 | 0.195 | 0.615 → 0.632 | 5.9x sr_bytes | down | 5 |
| `RF-duct` | duct-per-hour | **text** | 0.647 → 0.822 | 0.175 | 0.632 → 0.813 | 1.3x bytes_on_air | up | 3 |
| `MS-roles` | role-mix | **text** | 0.485 → 0.646 | 0.161 | 0.465 → 0.636 | 1.3x bytes_on_air | down | 2 |
| `DG-loss` | extra-loss | **text** | 0.486 → 0.647 | 0.161 | 0.469 → 0.632 | 1.2x sr_airtime | down | 4 |
| `MS-roles-fav` | role-mix | **text** | 0.500 → 0.655 | 0.156 | 0.482 → 0.644 | 1.2x bytes_on_air | down | 2 |
| `AD-badrouters` | role-placement | **held** | 0.685 → 0.831 | 0.145 | 0.465 → 0.604 | 1.5x sr_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.647 → 0.784 | 0.138 | 0.632 → 0.778 | 3.4x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.647 → 0.782 | 0.135 | 0.632 → 0.774 | 3.4x bytes_on_air | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.582 → 0.713 | 0.131 | 0.565 → 0.706 | 6.8x sr_airtime | up | 4 |
| `MS-size` | nodes | **held** | 0.817 → 0.942 | 0.125 | 0.632 → 0.689 | 4.6x sr_bytes | up | 5 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.647 → 0.756 | 0.109 | 0.632 → 0.751 | 2.3x bytes_on_air | up | 4 |
| `SC-signing` | signature-policy | **text** | 0.542 → 0.647 | 0.105 | 0.542 → 0.632 | 1.3x sr_airtime | down | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.647 → 0.747 | 0.100 | 0.632 → 0.741 | 2.3x bytes_on_air | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.801 → 0.893 | 0.092 | 0.626 → 0.626 | 4.1x sr_bytes | up | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.784 → 0.874 | 0.090 | 0.609 → 0.691 | 1.2x bytes_on_air | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.607 → 0.684 | 0.076 | 0.593 → 0.673 | 1.9x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.607 → 0.684 | 0.076 | 0.593 → 0.673 | 1.9x sr_airtime | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.775 → 0.848 | 0.073 | 0.627 → 0.632 | 24x sr_airtime | down | 3 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.787 → 0.848 | 0.061 | 0.572 → 0.632 | 1.5x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.787 → 0.848 | 0.061 | 0.575 → 0.632 | 19x sr_bytes | down | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.653 → 0.712 | 0.058 | 0.640 → 0.698 | 1.4x sr_airtime | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.801 → 0.848 | 0.047 | 0.610 → 0.632 | 8.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.801 → 0.848 | 0.047 | 0.610 → 0.632 | 8.4x sr_bytes | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.647 → 0.687 | 0.040 | 0.632 → 0.677 | 3.4x bytes_on_air | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.810 → 0.848 | 0.038 | 0.605 → 0.632 | 3.9x advert_bytes | up | 4 |
| `AD-worst` | role-placement | **text** | 0.770 → 0.807 | 0.036 | 0.759 → 0.801 | 1.2x sr_bytes | down | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.813 → 0.848 | 0.035 | 0.610 → 0.632 | 2.3x sr_airtime | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.827 → 0.859 | 0.032 | 0.492 → 0.523 | 1.4x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.594 → 0.624 | 0.031 | 0.575 → 0.616 | 9.3x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.819 → 0.848 | 0.028 | 0.618 → 0.632 | 3.1x advert_bytes | down | 4 |
| `SF-capacity` | capacity | **held** | 0.820 → 0.848 | 0.028 | 0.615 → 0.632 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.820 → 0.848 | 0.028 | 0.615 → 0.632 | 5.3x advert_bytes | up | 5 |
| `RT-favourites` | favourite-routers | **text** | 0.627 → 0.651 | 0.024 | 0.612 → 0.637 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.825 → 0.848 | 0.023 | 0.617 → 0.632 | 1.1x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.811 → 0.833 | 0.022 | 0.606 → 0.623 | 2x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.625 → 0.647 | 0.021 | 0.611 → 0.632 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.625 → 0.647 | 0.021 | 0.611 → 0.632 | 1.1x sr_airtime | up | 4 |
| `DM-mode` | dm-mode | **held** | 0.793 → 0.814 | 0.021 | 0.590 → 0.607 | 1.1x sr_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.826 → 0.846 | 0.021 | 0.626 → 0.637 | 1.1x sr_bytes | = | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.815 → 0.834 | 0.019 | 0.605 → 0.609 | 1.1x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **held** | 0.829 → 0.848 | 0.018 | 0.619 → 0.632 | 5.9x advert_bytes | = | 3 |
| `RT-hopassign` | hop-assign | **held** | 0.831 → 0.848 | 0.017 | 0.625 → 0.632 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.831 → 0.848 | 0.016 | 0.617 → 0.632 | 2.9x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.619 → 0.635 | 0.015 | 0.605 → 0.622 | 5x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.833 → 0.848 | 0.015 | 0.629 → 0.632 | 1x advert_bytes | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.813 → 0.828 | 0.015 | 0.610 → 0.616 | 1.1x sr_bytes | up | 2 |
| `LD-diurnal` | diurnal | **held** | 0.845 → 0.860 | 0.015 | 0.632 → 0.646 | 1.3x sr_bytes | down | 3 |
| `SF-window-size` | window-size | **held** | 0.819 → 0.833 | 0.014 | 0.615 → 0.623 | 6x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.913 → 0.922 | 0.009 | 0.908 → 0.918 | 1.2x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.995 → 0.997 | 0.002 | 0.917 → 0.918 | 1.1x bytes_on_air | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.921 → 0.922 | 0.001 | 0.916 → 0.918 | 1x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.604 → 0.605 | 0.001 | 0.604 → 0.605 | 1.1x sr_airtime | up | 2 |

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
| none | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| sprinkled | 1 | 0.772 | 0.766 | 0.006 | - | - | 0.875 | 0.892 | 0.388 | 1.18x | 12.4/22.3/24.7% | 1.8/5.0% | 3 |
| arms-race | 1 | 0.865 | 0.861 | 0.004 | - | - | 0.916 | 0.916 | 0.580 | 1.17x | 16.6/24.5/27.6% | 1.8/4.9% | 3 |

> amplifier-mix=sprinkled: decode_failures 34

> slower: 4.72 s per simulated hour against 1.63 over 28 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.1 | 1 | 0.681 | 0.676 | 0.005 | - | - | 0.758 | 0.839 | 0.403 | 1.41x | 15.9/25.6/30.1% | 2.2/5.4% | 3 |
| 0.3 | 1 | 0.851 | 0.830 | 0.022 | - | - | 0.968 | 0.969 | 0.672 | 1.15x | 15.5/23.8/26.5% | 1.6/4.4% | 3 |

> amplify-worst=0.1: decode_failures 36

> slower: 3.76 s per simulated hour against 1.72 over 28 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.485 | 0.465 | 0.020 | - | - | 0.722 | 0.724 | 0.156 | 1.03x | 10.5/19.7/25.3% | 1.6/4.7% | 3 |
| inverse | 1 | 0.504 | 0.480 | 0.024 | - | - | 0.685 | 0.695 | 0.196 | 1.19x | 11.1/18.7/22.4% | 2.1/4.0% | 3 |
| random | 1 | 0.618 | 0.604 | 0.014 | - | - | 0.831 | 0.834 | 0.162 | 1.20x | 12.2/18.5/23.1% | 2.1/5.1% | 3 |

> role-placement=inverse: decode_failures 1

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.485 | 0.465 | 0.020 | - | - | 0.722 | 0.724 | 0.156 | 1.03x | 10.5/19.7/25.3% | 1.6/4.7% | 3 |
| all-routers | 1 | 0.754 | 0.742 | 0.013 | - | - | 0.906 | 0.908 | 0.533 | 2.50x | 22.0/37.4/41.6% | 4.0/5.5% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.485 | 0.465 | 0.020 | - | - | 0.722 | 0.724 | 0.156 | 1.03x | 10.5/19.7/25.3% | 1.6/4.7% | 3 |
| no-mute | 1 | 0.661 | 0.651 | 0.011 | - | - | 0.879 | 0.880 | 0.390 | 1.33x | 12.4/21.6/26.5% | 2.1/5.4% | 3 |
| all-routers | 1 | 0.754 | 0.742 | 0.013 | - | - | 0.906 | 0.908 | 0.533 | 2.50x | 22.0/37.4/41.6% | 4.0/5.5% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.485 | 0.465 | 0.020 | - | - | 0.722 | 0.724 | 0.156 | 1.03x | 10.5/19.7/25.3% | 1.6/4.7% | 3 |
| local-typical | 1 | 0.330 | 0.316 | 0.014 | - | - | 0.572 | 0.577 | 0.000 | 1.07x | 8.5/20.1/26.7% | 1.5/4.8% | 3 |
| basement-heavy | 1 | 0.043 | 0.042 | 0.001 | - | - | 0.152 | 0.161 | 0.000 | 0.42x | 0.8/5.8/10.8% | 0.3/2.6% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.807 | 0.801 | 0.006 | - | - | 0.966 | 0.966 | 0.148 | 2.49x | 14.9/26.8/34.9% | 1.8/5.5% | 3 |
| inverse | 1 | 0.770 | 0.759 | 0.011 | - | - | 0.967 | 0.967 | 0.154 | 2.32x | 13.0/21.5/29.5% | 1.8/3.1% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.613 | 0.613 | 0.000 | - | - | 0 | 0.000 | 0.348 | 1.33x | 12.8/22.9/27.5% | 2.0/5.3% | 3 |
| sr | 1 | 0.637 | 0.616 | 0.021 | - | - | 0.744 | 0.867 | 0.328 | 1.36x | 13.2/23.4/28.4% | 2.0/5.5% | 3 |

> protocol=sr: decode_failures 33

> slower: 4.65 s per simulated hour against 1.72 over 28 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.607 | 0.593 | 0.015 | - | - | 0.745 | 0.750 | 0.254 | 2.67x | 23.9/49.2/56.6% | 3.6/8.7% | 3 |
| 100 | 1 | 0.684 | 0.673 | 0.011 | - | - | 0.812 | 0.813 | 0.300 | 1.59x | 14.1/30.0/35.2% | 2.1/5.2% | 3 |
| 120 | 1 | 0.684 | 0.673 | 0.011 | - | - | 0.812 | 0.813 | 0.300 | 1.59x | 14.1/30.0/35.2% | 2.1/5.2% | 3 |
| 250 | 1 | 0.684 | 0.673 | 0.011 | - | - | 0.812 | 0.813 | 0.300 | 1.59x | 14.1/30.0/35.2% | 2.1/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.317 | 0.313 | 0.005 | - | - | 0.514 | 0.616 | 0.088 | 11.10x | 37.9/56.4/75.4% | 3.9/10.8% | 3 |
| 120 | 1 | 0.503 | 0.492 | 0.011 | - | - | 0.827 | 0.829 | 0.132 | 4.58x | 15.5/29.2/45.9% | 1.5/6.3% | 3 |
| 250 | 1 | 0.506 | 0.496 | 0.011 | - | - | 0.842 | 0.845 | 0.137 | 4.50x | 15.3/28.4/44.7% | 1.4/6.1% | 3 |

> max-num-nodes=10: decode_failures 81

> max-num-nodes=120: decode_failures 5

> max-num-nodes=250: decode_failures 10

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.684 | 0.673 | 0.011 | - | - | 0.812 | 0.813 | 0.300 | 1.59x | 14.1/30.0/35.2% | 2.1/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.684 | 0.673 | 0.011 | - | - | 0.812 | 0.813 | 0.300 | 1.59x | 14.1/30.0/35.2% | 2.1/5.2% | 3 |
| constrained | 1 | 0.607 | 0.593 | 0.015 | - | - | 0.745 | 0.750 | 0.254 | 2.67x | 23.9/49.2/56.6% | 3.6/8.7% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.712 | 0.698 | 0.013 | - | - | 0.897 | 0.951 | 0.281 | 5.48x | 49.7/66.5/74.3% | 3.7/12.5% | 3 |
| 25 | 1 | 0.712 | 0.698 | 0.013 | - | - | 0.897 | 0.951 | 0.281 | 5.48x | 49.7/66.5/74.3% | 3.7/12.5% | 3 |
| 100 | 1 | 0.712 | 0.698 | 0.013 | - | - | 0.897 | 0.951 | 0.281 | 5.48x | 49.7/66.5/74.3% | 3.7/12.5% | 3 |
| 2000 | 1 | 0.712 | 0.698 | 0.013 | - | - | 0.897 | 0.951 | 0.281 | 5.48x | 49.7/66.5/74.3% | 3.7/12.5% | 3 |

> warm-num-nodes=0: decode_failures 102

> warm-num-nodes=25: decode_failures 102

> warm-num-nodes=100: decode_failures 102

> warm-num-nodes=2000: decode_failures 102

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.1 | 1 | 0.541 | 0.522 | 0.019 | - | - | 0.782 | 0.784 | 0.289 | 1.26x | 12.1/22.2/26.8% | 1.8/5.1% | 3 |
| 0.2 | 1 | 0.441 | 0.419 | 0.022 | - | - | 0.710 | 0.713 | 0.193 | 1.15x | 11.2/20.1/24.8% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.374 | 0.345 | 0.029 | - | - | 0.655 | 0.679 | 0.167 | 1.02x | 10.3/18.3/22.7% | 1.5/4.0% | 3 |

> burst-loss=0.2: decode_failures 1

> burst-loss=0.3: decode_failures 13

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.1 | 1 | 0.589 | 0.574 | 0.015 | - | - | 0.797 | 0.798 | 0.326 | 1.37x | 13.3/23.4/28.3% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.545 | 0.529 | 0.016 | - | - | 0.784 | 0.785 | 0.285 | 1.38x | 13.5/23.8/28.8% | 2.0/5.1% | 3 |
| 0.3 | 1 | 0.486 | 0.469 | 0.017 | - | - | 0.729 | 0.734 | 0.238 | 1.36x | 13.6/23.6/28.8% | 2.0/4.8% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.1 | 1 | 0.530 | 0.512 | 0.018 | - | - | 0.762 | 0.772 | 0.253 | 1.26x | 12.1/22.3/27.0% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.426 | 0.405 | 0.022 | - | - | 0.672 | 0.720 | 0.194 | 1.14x | 11.3/20.0/24.8% | 1.6/4.7% | 3 |
| 0.3 | 1 | 0.349 | 0.328 | 0.021 | - | - | 0.581 | 0.652 | 0.158 | 1.04x | 10.4/18.5/22.9% | 1.6/3.9% | 3 |

> burst-loss=0.1: decode_failures 5

> burst-loss=0.2: decode_failures 31

> burst-loss=0.3: decode_failures 16

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.590 | 0.590 | 0.000 | - | - | 0.793 | 0.794 | 0.326 | 1.61x | 15.3/28.1/33.9% | 2.4/6.5% | 3 |
| directed-with-late-flood | 1 | 0.604 | 0.604 | 0.000 | - | - | 0.814 | 0.816 | 0.313 | 1.52x | 14.5/26.7/32.2% | 2.3/6.2% | 3 |
| m4-early-flood | 1 | 0.607 | 0.607 | 0.000 | - | - | 0.812 | 0.815 | 0.323 | 1.51x | 14.4/26.4/31.9% | 2.2/6.2% | 3 |

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.782 | 0.774 | 0.008 | - | - | 0.954 | 0.955 | 0.339 | 0.72x | 7.2/10.0/11.4% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.25 | 1 | 0.686 | 0.677 | 0.009 | - | - | 0.883 | 0.884 | 0.293 | 1.03x | 10.5/16.7/20.5% | 1.6/4.5% | 3 |
| 0.5 | 1 | 0.733 | 0.720 | 0.012 | - | - | 0.884 | 0.885 | 0.000 | 1.04x | 10.7/16.9/20.2% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.747 | 0.741 | 0.006 | - | - | 0.873 | 0.874 | 0.519 | 0.84x | 9.0/12.8/15.8% | 1.4/2.8% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.25 | 1 | 0.705 | 0.697 | 0.008 | - | - | 0.906 | 0.906 | 0.318 | 1.04x | 10.6/16.7/20.6% | 1.6/4.6% | 3 |
| 0.5 | 1 | 0.730 | 0.717 | 0.012 | - | - | 0.876 | 0.877 | 0.000 | 1.00x | 10.3/16.1/19.5% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.756 | 0.751 | 0.005 | - | - | 0.872 | 0.874 | 0.541 | 0.82x | 9.0/12.7/15.5% | 1.3/2.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.687 | 0.677 | 0.010 | - | - | 0.871 | 0.872 | 0.370 | 0.75x | 7.6/13.6/16.7% | 1.0/3.4% | 3 |
| signing=true | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.778 | 0.771 | 0.007 | - | - | 0.954 | 0.954 | 0.306 | 0.72x | 7.7/10.9/12.6% | 1.1/2.4% | 3 |
| 2.5 | 1 | 0.765 | 0.758 | 0.007 | - | - | 0.934 | 0.936 | 0.310 | 0.74x | 7.8/11.1/12.6% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.767 | 0.762 | 0.005 | - | - | 0.944 | 0.947 | 0.283 | 0.71x | 7.8/11.0/12.7% | 1.1/2.4% | 3 |
| 2.7 | 1 | 0.784 | 0.778 | 0.006 | - | - | 0.951 | 0.951 | 0.313 | 0.74x | 7.9/12.2/13.9% | 1.1/2.9% | 3 |
| 2.8 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.676 | 0.667 | 0.009 | - | - | 0.862 | 0.863 | 0.369 | 0.90x | 8.6/15.7/18.7% | 1.3/3.8% | 3 |
| 900 | 1 | 0.582 | 0.565 | 0.017 | - | - | 0.782 | 0.783 | 0.332 | 2.11x | 19.8/35.9/43.0% | 3.1/8.4% | 3 |
| 300 | 1 | 0.365 | 0.348 | 0.017 | - | - | 0.551 | 0.575 | 0.233 | 4.67x | 44.2/66.1/75.7% | 7.2/15.4% | 3 |

> broadcast-interval-s=300: decode_failures 16

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.725 | 0.720 | 0.005 | - | - | 0.849 | 0.849 | 0.335 | 0.95x | 9.4/15.0/18.0% | 1.4/3.5% | 3 |
| 900 | 1 | 0.631 | 0.622 | 0.009 | - | - | 0.746 | 0.747 | 0.289 | 2.24x | 22.2/35.1/42.1% | 3.3/8.0% | 3 |
| 300 | 1 | 0.374 | 0.362 | 0.012 | - | - | 0.485 | 0.489 | 0.207 | 4.85x | 45.9/67.3/75.9% | 7.7/15.4% | 3 |

> broadcast-interval-s=300: decode_failures 4

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.658 | 0.646 | 0.012 | - | - | 0.860 | 0.863 | 0.359 | 1.32x | 12.5/23.0/27.6% | 2.0/5.5% | 3 |
| sinusoid | 1 | 0.654 | 0.644 | 0.011 | - | - | 0.845 | 0.845 | 0.357 | 1.25x | 12.0/21.6/25.8% | 1.8/5.1% | 3 |
| commuter | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.582 | 0.565 | 0.017 | - | - | 0.782 | 0.783 | 0.332 | 2.11x | 19.8/35.9/43.0% | 3.1/8.4% | 3 |
| 3600 | 1 | 0.676 | 0.667 | 0.009 | - | - | 0.862 | 0.863 | 0.369 | 0.90x | 8.6/15.7/18.7% | 1.3/3.8% | 3 |
| 10800 | 1 | 0.691 | 0.680 | 0.011 | - | - | 0.865 | 0.865 | 0.373 | 0.54x | 5.3/9.4/11.3% | 0.8/2.3% | 3 |
| 43200 | 1 | 0.713 | 0.706 | 0.007 | - | - | 0.891 | 0.892 | 0.409 | 0.36x | 3.5/6.6/7.9% | 0.5/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.25 | 1 | 0.627 | 0.613 | 0.014 | - | - | 0.818 | 0.820 | 0.339 | 1.40x | 13.4/24.3/29.1% | 2.0/5.8% | 3 |
| 1.0 | 1 | 0.615 | 0.599 | 0.015 | - | - | 0.809 | 0.811 | 0.336 | 1.50x | 14.4/26.0/31.3% | 2.2/6.2% | 3 |
| 4.0 | 1 | 0.587 | 0.572 | 0.015 | - | - | 0.787 | 0.788 | 0.322 | 1.77x | 17.3/30.8/37.4% | 2.5/7.4% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.712 | 0.698 | 0.013 | - | - | 0.897 | 0.951 | 0.281 | 5.48x | 49.7/66.5/74.3% | 3.7/12.5% | 3 |
| 1.0 | 1 | 0.653 | 0.640 | 0.014 | - | - | 0.851 | 0.918 | 0.265 | 6.05x | 54.3/70.2/77.2% | 4.1/14.1% | 3 |

> traceroute-per-hour=0.0: decode_failures 102

> traceroute-per-hour=1.0: decode_failures 91

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.634 | 0.627 | 0.007 | - | - | 0.854 | 0.855 | 0.139 | 1.16x | 15.7/26.0/33.3% | 2.7/6.3% | 3 |
| 60 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 90 | 1 | 0.898 | 0.894 | 0.005 | - | - | 0.994 | 0.994 | 0.545 | 1.64x | 14.8/25.5/33.3% | 1.5/5.1% | 3 |
| 120 | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.997 | 0.998 | 0.385 | 1.91x | 18.2/27.5/33.4% | 1.2/5.3% | 3 |
| 150 | 1 | 0.945 | 0.943 | 0.003 | - | - | 0.999 | 0.999 | 0.738 | 2.54x | 24.0/35.3/41.1% | 1.3/5.5% | 3 |

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 120 | 1 | 0.676 | 0.666 | 0.011 | - | - | 0.880 | 0.882 | 0.194 | 2.15x | 13.3/24.7/31.7% | 1.5/5.4% | 3 |
| 250 | 1 | 0.489 | 0.478 | 0.011 | - | - | 0.802 | 0.811 | 0.129 | 4.94x | 16.6/31.0/49.7% | 1.6/7.2% | 3 |
| 500 | 1 | 0.321 | 0.315 | 0.005 | - | - | 0.454 | 0.455 | 0.087 | 9.79x | 18.6/28.2/36.3% | 1.7/6.4% | 3 |

> nodes=120: decode_failures 1

> nodes=250: decode_failures 157

> nodes=500: decode_failures 43

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.677 | 0.667 | 0.009 | - | - | 0.866 | 0.870 | 0.196 | 2.08x | 12.9/23.7/30.7% | 1.4/5.2% | 3 |
| 250 | 1 | 0.503 | 0.492 | 0.011 | - | - | 0.827 | 0.829 | 0.132 | 4.58x | 15.5/29.2/45.9% | 1.5/6.3% | 3 |
| 500 | 1 | 0.320 | 0.316 | 0.005 | - | - | 0.440 | 0.451 | 0.096 | 9.11x | 17.3/26.4/33.6% | 1.5/6.0% | 3 |

> nodes=120: decode_failures 1

> nodes=250: decode_failures 5

> nodes=500: decode_failures 109

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.646 | 0.636 | 0.010 | - | - | 0.848 | 0.849 | 0.322 | 1.37x | 13.0/24.0/28.6% | 2.0/5.6% | 3 |
| baymesh-2026-08 | 1 | 0.485 | 0.465 | 0.020 | - | - | 0.722 | 0.724 | 0.156 | 1.03x | 10.5/19.7/25.3% | 1.6/4.7% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.655 | 0.644 | 0.012 | - | - | 0.835 | 0.835 | 0.315 | 1.39x | 13.5/23.6/28.5% | 2.0/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.500 | 0.482 | 0.018 | - | - | 0.720 | 0.720 | 0.163 | 1.13x | 11.1/22.8/27.1% | 1.8/4.5% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.05 | 1 | 0.625 | 0.609 | 0.016 | - | - | 0.804 | 0.805 | 0.315 | 1.49x | 13.5/28.5/32.9% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.632 | 0.620 | 0.012 | - | - | 0.784 | 0.786 | 0.301 | 1.58x | 14.0/30.2/36.5% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.707 | 0.691 | 0.016 | - | - | 0.874 | 0.874 | 0.456 | 1.69x | 15.0/33.1/38.8% | 2.4/5.0% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| local-typical | 1 | 0.440 | 0.421 | 0.019 | - | - | 0.738 | 0.740 | 0.000 | 1.17x | 9.2/18.0/25.6% | 1.7/4.7% | 3 |
| event | 1 | 0.123 | 0.122 | 0.001 | - | - | 0.230 | 0.230 | 0.000 | 0.84x | 3.6/9.3/13.4% | 1.2/3.0% | 3 |
| backbone | 1 | 0.959 | 0.956 | 0.003 | - | - | 0.999 | 0.999 | 0.855 | 1.21x | 21.5/30.9/34.2% | 1.6/5.4% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.660 | 0.651 | 0.009 | - | - | 0.817 | 0.820 | 0.212 | 1.23x | 16.7/28.2/30.6% | 2.7/6.6% | 3 |
| 60 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 90 | 1 | 0.698 | 0.689 | 0.009 | - | - | 0.938 | 0.938 | 0.182 | 1.75x | 13.2/24.3/27.5% | 1.7/5.5% | 3 |
| 120 | 1 | 0.676 | 0.666 | 0.011 | - | - | 0.880 | 0.882 | 0.194 | 2.15x | 13.3/24.7/31.7% | 1.5/5.4% | 3 |
| 150 | 1 | 0.643 | 0.635 | 0.007 | - | - | 0.942 | 0.943 | 0.179 | 2.76x | 14.0/28.9/39.3% | 1.5/5.3% | 3 |

> nodes=120: decode_failures 1

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 1.25 | 1 | 0.479 | 0.463 | 0.015 | - | - | 0.672 | 0.677 | 0.000 | 1.28x | 10.5/17.3/24.4% | 2.0/4.6% | 3 |
| 1.5 | 1 | 0.250 | 0.244 | 0.005 | - | - | 0.323 | 0.388 | 0.000 | 1.17x | 6.8/13.5/20.1% | 1.9/3.5% | 3 |
| 2.0 | 1 | 0.076 | 0.076 | 0.000 | - | - | 0.039 | 0.085 | 0.000 | 0.60x | 2.9/4.4/7.5% | 1.1/2.3% | 3 |

> stretch=1.5: decode_failures 11

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| clustered | 1 | 0.712 | 0.690 | 0.021 | - | - | 0.862 | 0.996 | 0.236 | 0.92x | 19.8/28.8/30.5% | 1.2/4.5% | 3 |
| corridor | 1 | 0.517 | 0.514 | 0.003 | - | - | 0.513 | 0.517 | 0.311 | 1.53x | 16.9/24.3/31.4% | 2.4/4.9% | 3 |
| hub | 1 | 0.897 | 0.897 | 0.001 | - | - | 0.967 | 0.967 | 0.534 | 1.19x | 24.2/35.5/36.7% | 1.8/5.4% | 3 |

> topology=clustered: decode_failures 18

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.604 | 0.604 | 0.000 | - | - | 0.814 | 0.816 | 0.313 | 1.52x | 14.5/26.7/32.2% | 2.3/6.2% | 3 |
| True | 1 | 0.605 | 0.605 | 0.000 | - | - | 0.815 | 0.819 | 0.343 | 1.53x | 14.5/26.6/32.2% | 2.2/6.2% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.605 | 0.605 | 0.000 | - | - | 0.815 | 0.819 | 0.343 | 1.53x | 14.5/26.6/32.2% | 2.2/6.2% | 3 |
| m4-early-flood | 1 | 0.609 | 0.609 | 0.000 | - | - | 0.834 | 0.835 | 0.347 | 1.54x | 14.6/26.9/32.5% | 2.3/6.3% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.613 | 0.613 | 0.000 | - | - | 0 | 0.000 | 0.348 | 1.33x | 12.8/22.9/27.5% | 2.0/5.3% | 3 |
| chain | 1 | 0.609 | 0.601 | 0.008 | - | - | 0.774 | 0.811 | 0.331 | 1.54x | 14.5/26.9/32.2% | 2.2/6.4% | 3 |
| sr | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| True | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.833 | 0.833 | 0.361 | 1.38x | 13.2/23.8/28.5% | 2.0/5.6% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.997 | 0.998 | 0.385 | 1.91x | 18.2/27.5/33.4% | 1.2/5.3% | 3 |
| True | 1 | 0.921 | 0.916 | 0.004 | - | - | 0.998 | 0.998 | 0.405 | 1.94x | 18.3/27.4/33.4% | 1.3/5.3% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.088 | 0.088 | 0.000 | - | - | 0.178 | 0.179 | 0.000 | 0.03x | 0.1/0.3/0.6% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.214 | 0.208 | 0.006 | - | - | 0.441 | 0.444 | 0.000 | 0.17x | 0.8/2.8/3.7% | 0.2/0.8% | 3 |
| LONG_TURBO | 1 | 0.484 | 0.475 | 0.009 | - | - | 0.711 | 0.711 | 0.133 | 1.16x | 9.7/18.2/21.8% | 1.8/4.8% | 3 |

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 0.25 | 1 | 0.710 | 0.699 | 0.011 | - | - | 0.860 | 0.861 | 0.471 | 1.19x | 15.0/23.4/27.6% | 1.7/5.3% | 3 |
| 1.0 | 1 | 0.822 | 0.813 | 0.009 | - | - | 0.918 | 0.919 | 0.616 | 1.03x | 17.7/24.6/28.9% | 1.3/5.2% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.155 | 0.153 | 0.003 | - | - | 0.302 | 0.317 | 0.000 | 0.09x | 0.4/1.4/1.9% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| LITE_FAST | 1 | 0.544 | 0.537 | 0.007 | - | - | 0.773 | 0.775 | 0.225 | 0.90x | 7.7/15.9/18.5% | 1.3/3.7% | 3 |
| NARROW_SLOW | 1 | 0.571 | 0.562 | 0.009 | - | - | 0.786 | 0.788 | 0.223 | 1.19x | 10.5/20.0/25.0% | 1.6/4.8% | 3 |

> preset=SHORT_FAST: decode_failures 6

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| temporal | 1 | 0.490 | 0.473 | 0.017 | - | - | 0.742 | 0.744 | 0.128 | 1.32x | 12.9/22.6/27.6% | 1.9/5.3% | 3 |
| transient | 1 | 0.630 | 0.617 | 0.013 | - | - | 0.820 | 0.820 | 0.344 | 1.36x | 12.9/23.5/28.0% | 2.0/5.5% | 3 |
| periodic | 1 | 0.475 | 0.462 | 0.012 | - | - | 0.641 | 0.643 | 0.241 | 1.24x | 11.9/21.1/25.8% | 1.8/4.7% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.155 | 0.153 | 0.003 | - | - | 0.302 | 0.317 | 0.000 | 0.09x | 0.4/1.4/1.9% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| LONG_MODERATE | 1 | 0.650 | 0.636 | 0.014 | - | - | 0.753 | 0.755 | 0.405 | 3.29x | 35.0/56.8/64.7% | 5.1/11.3% | 3 |

> preset=SHORT_FAST: decode_failures 6

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.051 | 0.051 | 0.000 | - | - | 0.158 | 0.161 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.088 | 0.088 | 0.000 | - | - | 0.178 | 0.179 | 0.000 | 0.03x | 0.1/0.3/0.6% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| LONG_TURBO | 1 | 0.484 | 0.475 | 0.009 | - | - | 0.711 | 0.711 | 0.133 | 1.16x | 9.7/18.2/21.8% | 1.8/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.638 | 0.630 | 0.008 | - | - | 0.813 | 0.815 | 0.386 | 1.86x | 16.7/29.7/35.9% | 2.7/7.1% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.577 | 0.565 | 0.012 | - | - | 0.764 | 0.764 | 0.309 | 1.32x | 12.8/22.9/27.6% | 2.0/5.3% | 3 |
| 10000 | 1 | 0.475 | 0.462 | 0.012 | - | - | 0.641 | 0.643 | 0.241 | 1.24x | 11.9/21.1/25.8% | 1.8/4.7% | 3 |
| 4000 | 1 | 0.277 | 0.269 | 0.008 | - | - | 0.403 | 0.431 | 0.140 | 1.01x | 10.1/17.2/21.0% | 1.5/3.4% | 3 |
| 2000 | 1 | 0.068 | 0.068 | 0.000 | - | - | 0.092 | 0.150 | 0.029 | 0.67x | 6.5/11.7/15.2% | 1.1/2.0% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.250 | 0.244 | 0.005 | - | - | 0.323 | 0.388 | 0.000 | 1.17x | 6.8/13.5/20.1% | 1.9/3.5% | 3 |
| 1.0 | 1 | 0.637 | 0.620 | 0.017 | - | - | 0.710 | 0.712 | 0.468 | 1.05x | 12.9/20.3/23.5% | 1.5/4.0% | 3 |

> duct-per-hour=0.0: decode_failures 11

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 22 | 1 | 0.203 | 0.196 | 0.007 | - | - | 0.392 | 0.443 | 0.000 | 1.09x | 5.6/16.7/21.2% | 1.5/4.5% | 3 |
| 17 | 1 | 0.087 | 0.087 | 0.000 | - | - | 0.165 | 0.167 | 0.000 | 0.67x | 2.8/6.9/12.3% | 1.0/2.4% | 3 |
| 14 | 1 | 0.058 | 0.058 | 0.000 | - | - | 0.110 | 0.169 | 0.000 | 0.48x | 1.9/4.4/7.8% | 0.7/2.2% | 3 |

> tx-power=22: decode_failures 14

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.997 | 0.998 | 0.385 | 1.91x | 18.2/27.5/33.4% | 1.2/5.3% | 3 |
| True | 1 | 0.913 | 0.908 | 0.005 | - | - | 0.997 | 0.997 | 0.382 | 2.24x | 21.4/30.7/36.7% | 1.5/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.627 | 0.612 | 0.016 | - | - | 0.814 | 0.815 | 0.329 | 1.45x | 12.9/26.8/31.4% | 2.0/5.3% | 3 |
| True | 1 | 0.651 | 0.637 | 0.014 | - | - | 0.807 | 0.809 | 0.323 | 1.49x | 13.8/27.2/31.7% | 2.1/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| random | 1 | 0.640 | 0.625 | 0.015 | - | - | 0.831 | 0.831 | 0.274 | 1.31x | 13.3/21.9/26.1% | 1.9/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.425 | 0.390 | 0.035 | - | - | 0.628 | 0.628 | 0.191 | 1.09x | 10.8/19.3/23.6% | 1.5/4.9% | 3 |
| 7 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.813 | 0.814 | 0.340 | 1.44x | 14.2/22.8/27.3% | 2.1/5.3% | 3 |
| 15 | 1 | 0.754 | 0.752 | 0.002 | - | - | 0.809 | 0.809 | 0.392 | 1.44x | 14.2/22.6/26.8% | 2.1/5.1% | 3 |
| 32 | 1 | 0.757 | 0.754 | 0.002 | - | - | 0.811 | 0.812 | 0.427 | 1.44x | 14.1/22.5/26.7% | 2.1/5.0% | 3 |

> hop-limit=3: decode_failures 2

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.425 | 0.390 | 0.035 | - | - | 0.628 | 0.628 | 0.191 | 1.09x | 10.8/19.3/23.6% | 1.5/4.9% | 3 |
| 5 | 1 | 0.590 | 0.567 | 0.024 | - | - | 0.783 | 0.785 | 0.281 | 1.31x | 13.1/21.8/26.0% | 1.9/5.2% | 3 |
| 7 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.813 | 0.814 | 0.340 | 1.44x | 14.2/22.8/27.3% | 2.1/5.3% | 3 |

> hop-limit=3: decode_failures 2

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| KNOWN_ONLY | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.627 | 0.627 | 0.000 | - | - | 0.775 | 0.838 | 0.350 | 1.33x | 12.6/22.8/27.4% | 1.9/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.425 | 0.390 | 0.035 | - | - | 0.628 | 0.628 | 0.191 | 1.09x | 10.8/19.3/23.6% | 1.5/4.9% | 3 |
| True | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

> hop-spread=False: decode_failures 2

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| BALANCED | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| STRICT | 1 | 0.542 | 0.542 | 0.000 | - | - | 0.749 | 0.749 | 0.248 | 1.45x | 14.0/25.1/30.2% | 2.1/5.9% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| dm | 1 | 0.632 | 0.617 | 0.015 | - | - | 0.831 | 0.833 | 0.347 | 1.35x | 12.8/23.4/28.0% | 2.0/5.8% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.636 | 0.622 | 0.015 | - | - | 0.829 | 0.830 | 0.351 | 1.37x | 13.0/23.9/28.6% | 2.0/5.7% | 3 |
| local | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| time | 1 | 0.619 | 0.605 | 0.014 | - | - | 0.810 | 0.812 | 0.335 | 1.40x | 13.2/24.3/29.1% | 2.1/5.8% | 3 |
| window | 1 | 0.638 | 0.623 | 0.015 | - | - | 0.833 | 0.835 | 0.359 | 1.33x | 12.6/22.9/27.4% | 2.0/5.4% | 3 |

> bucket-mode=global: misdecodes 33

> bucket-mode=time: misdecodes 28

> bucket-mode=window: misdecodes 10

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.627 | 0.613 | 0.015 | - | - | 0.818 | 0.820 | 0.339 | 1.48x | 13.6/26.3/31.2% | 2.1/6.5% | 3 |
| 1800 | 1 | 0.619 | 0.605 | 0.014 | - | - | 0.810 | 0.812 | 0.335 | 1.40x | 13.2/24.3/29.1% | 2.1/5.8% | 3 |
| 3600 | 1 | 0.635 | 0.622 | 0.013 | - | - | 0.823 | 0.828 | 0.351 | 1.38x | 13.0/23.9/28.5% | 2.0/5.6% | 3 |

> time-bucket-s=600: misdecodes 144

> time-bucket-s=1800: misdecodes 28

> time-bucket-s=3600: misdecodes 5

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| interval | 1 | 0.603 | 0.583 | 0.020 | - | - | 0.787 | 0.792 | 0.293 | 1.78x | 16.2/33.0/41.2% | 2.5/11.3% | 3 |
| aimd | 1 | 0.626 | 0.620 | 0.005 | - | - | 0.792 | 0.830 | 0.343 | 1.39x | 13.1/24.1/28.8% | 2.1/5.7% | 3 |
| bucket+interval | 1 | 0.594 | 0.575 | 0.018 | - | - | 0.790 | 0.790 | 0.313 | 1.80x | 16.4/33.2/41.4% | 2.5/11.3% | 3 |

> trigger=interval: misdecodes 25

> trigger=aimd: misdecodes 5

> trigger=aimd: decode_failures 4

> trigger=bucket+interval: misdecodes 22

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.629 | 0.615 | 0.014 | - | - | 0.820 | 0.823 | 0.323 | 1.34x | 12.7/23.5/28.0% | 2.0/5.7% | 3 |
| 8 | 1 | 0.632 | 0.617 | 0.016 | - | - | 0.839 | 0.842 | 0.333 | 1.36x | 12.9/23.6/28.3% | 2.0/5.7% | 3 |
| 16 | 1 | 0.642 | 0.627 | 0.014 | - | - | 0.838 | 0.842 | 0.356 | 1.35x | 12.9/23.4/28.1% | 2.0/5.6% | 3 |
| 32 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 50 | 1 | 0.641 | 0.627 | 0.014 | - | - | 0.842 | 0.844 | 0.351 | 1.36x | 12.9/23.5/28.1% | 2.0/5.5% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 32

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.629 | 0.615 | 0.014 | - | - | 0.820 | 0.823 | 0.323 | 1.34x | 12.7/23.5/28.0% | 2.0/5.7% | 3 |
| 8 | 1 | 0.632 | 0.617 | 0.016 | - | - | 0.839 | 0.842 | 0.333 | 1.36x | 12.9/23.6/28.3% | 2.0/5.7% | 3 |
| 16 | 1 | 0.642 | 0.627 | 0.014 | - | - | 0.838 | 0.842 | 0.356 | 1.35x | 12.9/23.4/28.1% | 2.0/5.6% | 3 |
| 32 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 50 | 1 | 0.641 | 0.627 | 0.014 | - | - | 0.842 | 0.844 | 0.351 | 1.36x | 12.9/23.5/28.1% | 2.0/5.5% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 32

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.635 | 0.623 | 0.012 | - | - | 0.831 | 0.837 | 0.342 | 1.34x | 12.8/23.1/27.7% | 2.0/5.4% | 3 |
| 16 | 1 | 0.620 | 0.606 | 0.014 | - | - | 0.811 | 0.812 | 0.345 | 1.35x | 13.0/23.1/27.7% | 2.0/5.5% | 3 |
| 32 | 1 | 0.638 | 0.623 | 0.015 | - | - | 0.833 | 0.835 | 0.359 | 1.33x | 12.6/22.9/27.4% | 2.0/5.4% | 3 |

> capacity=8: misdecodes 19

> capacity=8: decode_failures 27

> capacity=16: misdecodes 8

> capacity=16: decode_failures 1

> capacity=32: misdecodes 10

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.594 | 0.575 | 0.018 | - | - | 0.790 | 0.790 | 0.313 | 1.80x | 16.4/33.2/41.4% | 2.5/11.3% | 3 |
| 02-06 | 1 | 0.619 | 0.611 | 0.008 | - | - | 0.792 | 0.820 | 0.329 | 1.41x | 13.3/24.6/29.5% | 2.1/6.1% | 3 |
| 00-08 | 1 | 0.624 | 0.616 | 0.008 | - | - | 0.798 | 0.825 | 0.328 | 1.46x | 13.7/26.1/31.1% | 2.1/6.8% | 3 |

> catch-up-hours=: misdecodes 22

> catch-up-hours=02-06: decode_failures 22

> catch-up-hours=00-08: decode_failures 22

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.624 | 0.621 | 0.003 | - | - | 0.774 | 0.775 | 0.328 | 1.35x | 12.8/23.4/28.1% | 1.9/5.4% | 3 |
| 2 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 3 | 1 | 0.637 | 0.616 | 0.021 | - | - | 0.744 | 0.867 | 0.328 | 1.36x | 13.2/23.4/28.4% | 2.0/5.5% | 3 |
| 4 | 1 | 0.641 | 0.615 | 0.027 | - | - | 0.653 | 0.854 | 0.337 | 1.36x | 12.8/23.7/28.2% | 2.0/5.5% | 3 |

> hops-apart=3: decode_failures 33

> hops-apart=4: decode_failures 28

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.624 | 0.621 | 0.003 | - | - | 0.774 | 0.775 | 0.328 | 1.35x | 12.8/23.4/28.1% | 1.9/5.4% | 3 |
| 2 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 3 | 1 | 0.637 | 0.616 | 0.021 | - | - | 0.744 | 0.867 | 0.328 | 1.36x | 13.2/23.4/28.4% | 2.0/5.5% | 3 |
| 4 | 1 | 0.641 | 0.615 | 0.027 | - | - | 0.653 | 0.854 | 0.337 | 1.36x | 12.8/23.7/28.2% | 2.0/5.5% | 3 |
| 5 | 1 | 0.669 | 0.623 | 0.046 | - | - | 0.744 | 0.971 | 0.338 | 1.37x | 13.3/23.5/28.3% | 2.0/5.5% | 3 |

> hops-apart=3: decode_failures 33

> hops-apart=4: decode_failures 28

> hops-apart=5: decode_failures 22

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.625 | 0.611 | 0.015 | - | - | 0.828 | 0.828 | 0.339 | 1.36x | 12.9/23.5/28.1% | 2.0/5.5% | 3 |
| 30 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 120 | 1 | 0.631 | 0.615 | 0.015 | - | - | 0.830 | 0.831 | 0.357 | 1.36x | 12.8/23.6/28.1% | 2.0/5.6% | 3 |
| 600 | 1 | 0.633 | 0.619 | 0.014 | - | - | 0.833 | 0.833 | 0.328 | 1.35x | 12.8/23.4/28.0% | 2.0/5.5% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.625 | 0.611 | 0.015 | - | - | 0.828 | 0.828 | 0.339 | 1.36x | 12.9/23.5/28.1% | 2.0/5.5% | 3 |
| 30 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 120 | 1 | 0.631 | 0.615 | 0.015 | - | - | 0.830 | 0.831 | 0.357 | 1.36x | 12.8/23.6/28.1% | 2.0/5.6% | 3 |
| 600 | 1 | 0.633 | 0.619 | 0.014 | - | - | 0.833 | 0.833 | 0.328 | 1.35x | 12.8/23.4/28.0% | 2.0/5.5% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.635 | 0.616 | 0.019 | - | - | 0.567 | 0.891 | 0.368 | 1.34x | 13.3/22.9/27.4% | 2.0/5.2% | 3 |
| routers | 1 | 0.632 | 0.626 | 0.006 | - | - | 0.801 | 0.802 | 0.332 | 1.36x | 12.9/23.7/28.2% | 2.0/5.5% | 3 |
| alternate-routers | 1 | 0.637 | 0.615 | 0.022 | - | - | 0.796 | 0.864 | 0.318 | 1.36x | 13.1/23.4/28.2% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.628 | 0.617 | 0.011 | - | - | 0.808 | 0.809 | 0.346 | 1.36x | 13.0/23.6/28.2% | 2.0/5.3% | 3 |
| random-clients | 1 | 0.630 | 0.619 | 0.011 | - | - | 0.663 | 0.804 | 0.335 | 1.37x | 13.1/23.3/28.1% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

> place=spread: decode_failures 16

> place=alternate-routers: decode_failures 6

> place=random-clients: decode_failures 19

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.635 | 0.616 | 0.019 | - | - | 0.567 | 0.891 | 0.368 | 1.34x | 13.3/22.9/27.4% | 2.0/5.2% | 3 |
| routers | 1 | 0.632 | 0.626 | 0.006 | - | - | 0.801 | 0.802 | 0.332 | 1.36x | 12.9/23.7/28.2% | 2.0/5.5% | 3 |
| alternate-routers | 1 | 0.637 | 0.615 | 0.022 | - | - | 0.796 | 0.864 | 0.318 | 1.36x | 13.1/23.4/28.2% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.628 | 0.617 | 0.011 | - | - | 0.808 | 0.809 | 0.346 | 1.36x | 13.0/23.6/28.2% | 2.0/5.3% | 3 |
| random-clients | 1 | 0.630 | 0.619 | 0.011 | - | - | 0.663 | 0.804 | 0.335 | 1.37x | 13.1/23.3/28.1% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

> place=spread: decode_failures 16

> place=alternate-routers: decode_failures 6

> place=random-clients: decode_failures 19

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| broadcast | 1 | 0.655 | 0.610 | 0.045 | - | - | 0.813 | 0.814 | 0.357 | 1.40x | 13.3/24.3/29.1% | 2.0/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| heard | 1 | 0.631 | 0.617 | 0.014 | - | - | 0.825 | 0.826 | 0.341 | 1.35x | 12.9/23.4/28.1% | 2.0/5.5% | 3 |

> replay-ordering=heard: misdecodes 14

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.655 | 0.610 | 0.045 | - | - | 0.813 | 0.814 | 0.357 | 1.40x | 13.3/24.3/29.1% | 2.0/5.6% | 3 |
| heard | 1 | 0.657 | 0.616 | 0.041 | - | - | 0.828 | 0.830 | 0.350 | 1.40x | 13.1/24.4/29.1% | 2.0/5.7% | 3 |

> replay-ordering=heard: misdecodes 13

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| enum | 1 | 0.633 | 0.619 | 0.014 | - | - | 0.829 | 0.830 | 0.335 | 1.38x | 13.1/24.0/28.7% | 2.0/5.9% | 3 |
| hybrid | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.632 | 0.626 | 0.006 | - | - | 0.801 | 0.802 | 0.332 | 1.36x | 12.9/23.7/28.2% | 2.0/5.5% | 3 |
| 6 | 1 | 0.672 | 0.626 | 0.046 | - | - | 0.893 | 0.901 | 0.347 | 1.39x | 13.3/24.1/29.0% | 2.0/5.9% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.625 | 0.616 | 0.010 | - | - | 0.801 | 0.802 | 0.335 | 1.36x | 12.7/23.5/28.1% | 2.0/5.5% | 2 |
| 3 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 5 | 1 | 0.638 | 0.612 | 0.026 | - | - | 0.827 | 0.828 | 0.357 | 1.39x | 13.0/24.1/28.8% | 2.0/5.6% | 5 |
| 8 | 1 | 0.635 | 0.610 | 0.025 | - | - | 0.834 | 0.837 | 0.344 | 1.41x | 13.2/24.8/29.5% | 2.1/5.7% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.625 | 0.616 | 0.010 | - | - | 0.801 | 0.802 | 0.335 | 1.36x | 12.7/23.5/28.1% | 2.0/5.5% | 2 |
| 3 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 5 | 1 | 0.638 | 0.612 | 0.026 | - | - | 0.827 | 0.828 | 0.357 | 1.39x | 13.0/24.1/28.8% | 2.0/5.6% | 5 |
| 8 | 1 | 0.635 | 0.610 | 0.025 | - | - | 0.834 | 0.837 | 0.344 | 1.41x | 13.2/24.8/29.5% | 2.1/5.7% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| True | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.639 | 0.626 | 0.013 | - | - | 0.834 | 0.837 | 0.341 | 1.29x | 12.3/22.3/26.7% | 1.9/5.2% | 3 |
| 1 | 1 | 0.648 | 0.637 | 0.012 | - | - | 0.846 | 0.847 | 0.364 | 1.29x | 12.3/22.2/26.7% | 1.9/5.2% | 3 |
| 2 | 1 | 0.638 | 0.629 | 0.009 | - | - | 0.826 | 0.826 | 0.338 | 1.29x | 12.4/22.3/26.7% | 1.9/5.2% | 3 |
| 4 | 1 | 0.640 | 0.629 | 0.011 | - | - | 0.834 | 0.835 | 0.335 | 1.28x | 12.3/22.2/26.7% | 1.9/5.2% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.640 | 0.627 | 0.013 | - | - | 0.836 | 0.839 | 0.359 | 1.36x | 12.8/23.5/28.2% | 2.0/5.6% | 3 |
| 24 | 1 | 0.631 | 0.618 | 0.013 | - | - | 0.819 | 0.820 | 0.349 | 1.36x | 13.1/23.5/28.3% | 2.0/5.6% | 3 |
| 32 | 1 | 0.647 | 0.632 | 0.015 | - | - | 0.848 | 0.848 | 0.348 | 1.36x | 12.9/23.5/28.2% | 2.0/5.6% | 3 |
| 64 | 1 | 0.635 | 0.621 | 0.013 | - | - | 0.828 | 0.828 | 0.352 | 1.38x | 13.0/23.8/28.5% | 2.0/5.6% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.631 | 0.617 | 0.014 | - | - | 0.823 | 0.823 | 0.364 | 1.43x | 13.4/24.9/29.7% | 2.1/5.9% | 3 |
| 16 | 1 | 0.629 | 0.615 | 0.014 | - | - | 0.819 | 0.820 | 0.329 | 1.36x | 12.8/23.5/28.1% | 2.0/5.5% | 3 |
| 32 | 1 | 0.638 | 0.623 | 0.015 | - | - | 0.833 | 0.835 | 0.359 | 1.33x | 12.6/22.9/27.4% | 2.0/5.4% | 3 |

> window-size=8: misdecodes 100

> window-size=16: misdecodes 35

> window-size=32: misdecodes 10

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.997 | 0.998 | 0.385 | 1.91x | 18.2/27.5/33.4% | 1.2/5.3% | 3 |
| True | 1 | 0.706 | 0.690 | 0.017 | - | - | 0.905 | 0.941 | 0.258 | 5.47x | 49.6/66.4/74.4% | 3.7/12.6% | 3 |

> no-congestion-scaling=True: decode_failures 93

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.503 | 0.492 | 0.011 | - | - | 0.827 | 0.829 | 0.132 | 4.58x | 15.5/29.2/45.9% | 1.5/6.3% | 3 |
| truesize | 1 | 0.532 | 0.523 | 0.009 | - | - | 0.859 | 0.861 | 0.140 | 3.40x | 11.1/23.4/37.2% | 1.1/5.1% | 3 |

> congestion-input=hotstore: decode_failures 5

> congestion-input=truesize: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.995 | 0.996 | 0.384 | 1.70x | 16.3/24.6/29.8% | 1.1/4.8% | 3 |
| adaptive | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.997 | 0.998 | 0.385 | 1.91x | 18.2/27.5/33.4% | 1.2/5.3% | 3 |

