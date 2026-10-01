# Sweep blocks-2026-10-01-4233538

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 4233538 · seeds 4233538
- **blocks** 87 run
- **compute** 9.8 h of simulator time across every cell
- **generated** 2026-10-01T10:28:37+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>85 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 22
- AD-siting: siting-mix=basement-heavy: decode_failures 1
- BL-control: protocol=sr: decode_failures 4
- DB-hotstore-stress: max-num-nodes=10: decode_failures 52
- DB-hotstore-stress: max-num-nodes=120: decode_failures 51
- DB-hotstore-stress: max-num-nodes=250: decode_failures 58
- DB-warm: warm-num-nodes=0: queue drops 15.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 120
- DB-warm: warm-num-nodes=25: queue drops 15.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 120
- DB-warm: warm-num-nodes=100: queue drops 15.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 120
- DB-warm: warm-num-nodes=2000: queue drops 15.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 120
- DG-burst: burst-loss=0.2: decode_failures 2
- DG-burst: burst-loss=0.3: decode_failures 18
- DG-burst: faster: 2.38 s per simulated hour against 5.15 over 41 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DG-outage: burst-loss=0.1: decode_failures 6
- DG-outage: burst-loss=0.2: decode_failures 36
- DG-outage: burst-loss=0.3: decode_failures 28
- DM-mode: faster: 1.21 s per simulated hour against 3.31 over 41 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- FW-firmware: faster: 0.85 s per simulated hour against 1.78 over 41 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- FW-mixed: legacy-fraction=0.75: decode_failures 1
- LD-chatty: broadcast-interval-s=300: decode_failures 1
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 15.0% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 120
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 25.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 101
- MS-density: nodes=150: decode_failures 3
- MS-hopscale: nodes=250: decode_failures 120
- MS-hopscale: nodes=500: decode_failures 3
- MS-oversubscribed: nodes=250: decode_failures 51
- MS-siting: siting-mix=event: decode_failures 7
- MS-stretch: stretch=2.0: decode_failures 11
- RF-bw500: preset=SHORT_TURBO: decode_failures 6
- RF-eu-presets: preset=SHORT_FAST: decode_failures 2
- RF-preset: preset=SHORT_FAST: decode_failures 2
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 6
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 5
- RF-txpower: tx-power=17: decode_failures 3
- RF-txpower: tx-power=14: decode_failures 3
- RT-hoplimit: hop-limit=15: misdecodes 1
- RT-hoplimit: hop-limit=32: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 35
- SF-bucket-mode: bucket-mode=time: misdecodes 40
- SF-bucket-mode: bucket-mode=window: misdecodes 26
- SF-bucket-time: time-bucket-s=600: misdecodes 127
- SF-bucket-time: time-bucket-s=1800: misdecodes 40
- SF-bucket-time: time-bucket-s=3600: misdecodes 17
- SF-cadence: trigger=interval: misdecodes 23
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=aimd: decode_failures 6
- SF-cadence: trigger=bucket+interval: misdecodes 18
- SF-capacity-local: capacity=4: decode_failures 47
- SF-capacity-local: capacity=8: decode_failures 11
- SF-capacity: capacity=4: decode_failures 47
- SF-capacity: capacity=8: decode_failures 11
- SF-capacity-window: capacity=8: misdecodes 30
- SF-capacity-window: capacity=8: decode_failures 5
- SF-capacity-window: capacity=16: misdecodes 35
- SF-capacity-window: capacity=32: misdecodes 26
- SF-catchup: catch-up-hours=: misdecodes 18
- SF-catchup: catch-up-hours=02-06: decode_failures 31
- SF-catchup: catch-up-hours=00-08: misdecodes 2
- SF-catchup: catch-up-hours=00-08: decode_failures 28
- SF-hops-flat: hops-apart=3: decode_failures 4
- SF-hops-flat: hops-apart=4: decode_failures 7
- SF-hops-spread: hops-apart=3: decode_failures 4
- SF-hops-spread: hops-apart=4: decode_failures 7
- SF-hops-spread: faster: 1.92 s per simulated hour against 4.81 over 41 prior run(s) - 2.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=spread: decode_failures 3
- SF-place-spread: place=spread: decode_failures 3
- SF-place-spread: faster: 1.25 s per simulated hour against 2.79 over 41 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 13
- SF-replay-order: replay-ordering=heard: misdecodes 23
- SF-replay-order: faster: 0.785 s per simulated hour against 1.69 over 41 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-servers-flat: faster: 1.1 s per simulated hour against 2.54 over 41 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-window-size: window-size=8: misdecodes 139
- SF-window-size: window-size=16: misdecodes 54
- SF-window-size: window-size=32: misdecodes 26
- TH-congestion-input: congestion-input=hotstore: decode_failures 51
- TH-congestion-input: congestion-input=truesize: decode_failures 3
- TH-congestion-mode: congestion-mode=static: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 13.4% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 106

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 21.4 | 11.2 | 1.92x | 41 |
| `DB-hotstore-stress` | 36.6 | 22.6 | 1.62x | 41 |
| `SF-capacity-window` | 1.09 | 1.65 | 0.66x | 41 |
| `SF-hops-flat` | 2.54 | 3.88 | 0.66x | 41 |
| `PR-dmmode-cr` | 1.82 | 2.82 | 0.65x | 41 |
| `AD-nomute` | 1.47 | 2.35 | 0.63x | 41 |
| `PR-crladder` | 1.7 | 2.79 | 0.61x | 41 |
| `SC-signing` | 1.1 | 1.82 | 0.61x | 41 |
| `RF-preset` | 1.75 | 2.97 | 0.59x | 41 |
| `DG-loss` | 1.22 | 2.28 | 0.53x | 41 |
| `SF-place-flat` | 1.52 | 2.86 | 0.53x | 41 |
| `SF-catchup` | 4.94 | 9.48 | 0.52x | 41 |
| `LD-chatty` | 2.64 | 5.14 | 0.52x | 41 |
| `FW-firmware` | 0.85 | 1.78 | 0.48x | 41 |
| `SF-replay-order` | 0.785 | 1.69 | 0.46x | 41 |
| `DG-burst` | 2.38 | 5.15 | 0.46x | 41 |
| `SF-place-spread` | 1.25 | 2.79 | 0.45x | 41 |
| `SF-servers-flat` | 1.1 | 2.54 | 0.43x | 41 |
| `SF-hops-spread` | 1.92 | 4.81 | 0.40x | 41 |
| `DM-mode` | 1.21 | 3.31 | 0.36x | 41 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.892 | 0.892 | 0.799 → 0.814 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **text** | 0.074 → 0.817 | 0.743 | 0.073 → 0.811 | 5.2x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.099 → 0.834 | 0.735 | 0.093 → 0.753 | 1.4e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.092 → 0.823 | 0.731 | 0.091 → 0.810 | 4.2x advert_bytes | down | 3 |
| `RF-txpower` | tx-power | **text** | 0.097 → 0.817 | 0.720 | 0.094 → 0.811 | 4.9x advert_bytes | down | 4 |
| `MS-stretch` | stretch | **text** | 0.152 → 0.817 | 0.665 | 0.147 → 0.811 | 2.8x sr_airtime | down | 4 |
| `BL-control` | protocol | **held** | 0 → 0.648 | 0.648 | 0.814 → 0.814 | 1x bytes_on_air | up | 2 |
| `MS-hopscale` | nodes | **held** | 0.274 → 0.914 | 0.641 | 0.299 → 0.811 | 11x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.287 → 0.910 | 0.622 | 0.301 → 0.737 | 4.7x bytes_on_air | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.387 → 0.975 | 0.588 | 0.378 → 0.975 | 2.6x sr_bytes | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.248 → 0.817 | 0.569 | 0.245 → 0.811 | 2.9x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.248 → 0.817 | 0.569 | 0.245 → 0.811 | 4x sr_airtime | up | 3 |
| `RF-bw500` | preset | **text** | 0.166 → 0.733 | 0.567 | 0.162 → 0.724 | 2.2x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.347 → 0.783 | 0.436 | 0.342 → 0.777 | 2.6x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.590 → 0.967 | 0.377 | 0.576 → 0.966 | 1.9x sr_airtime | up | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.500 → 0.867 | 0.367 | 0.489 → 0.862 | 8.9x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.564 → 0.919 | 0.355 | 0.553 → 0.916 | 8.7x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.421 → 0.749 | 0.328 | 0.316 → 0.526 | 6.6x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.649 → 0.973 | 0.324 | 0.636 → 0.971 | 4.8x sr_airtime | up | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.648 → 0.948 | 0.300 | 0.807 → 0.818 | 2.7x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.648 → 0.948 | 0.300 | 0.807 → 0.818 | 2.7x sr_bytes | up | 5 |
| `DG-burst` | burst-loss | **text** | 0.532 → 0.817 | 0.284 | 0.497 → 0.811 | 2.8x sr_bytes | down | 4 |
| `DG-outage` | burst-loss | **text** | 0.537 → 0.817 | 0.280 | 0.514 → 0.811 | 2.9x sr_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.674 → 0.939 | 0.265 | 0.804 → 0.818 | 2.3x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.674 → 0.939 | 0.265 | 0.804 → 0.818 | 2.3x sr_bytes | up | 6 |
| `MS-size` | nodes | **text** | 0.646 → 0.856 | 0.210 | 0.637 → 0.850 | 5.7x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.746 → 0.955 | 0.209 | 0.740 → 0.953 | 4.5x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.725 → 0.912 | 0.188 | 0.703 → 0.910 | 2x sr_bytes | up | 4 |
| `SC-signing` | signature-policy | **held** | 0.715 → 0.892 | 0.177 | 0.650 → 0.811 | 1.3x sr_airtime | down | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.725 → 0.899 | 0.175 | 0.703 → 0.895 | 1.8x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.675 → 0.827 | 0.152 | 0.666 → 0.819 | 1.3x sr_airtime | down | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.817 → 0.964 | 0.147 | 0.811 → 0.962 | 1.4x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.817 → 0.956 | 0.139 | 0.811 → 0.951 | 1.3x sr_airtime | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.758 → 0.890 | 0.132 | 0.750 → 0.886 | 5.5x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.762 → 0.891 | 0.129 | 0.720 → 0.848 | 2.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.693 → 0.817 | 0.124 | 0.679 → 0.811 | 1.5x sr_bytes | down | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.732 → 0.851 | 0.120 | 0.724 → 0.848 | 2.3x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.817 → 0.919 | 0.103 | 0.811 → 0.916 | 1.4x sr_bytes | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.817 → 0.918 | 0.101 | 0.811 → 0.912 | 2.1x bytes_on_air | up | 4 |
| `AD-badrouters` | role-placement | **held** | 0.853 → 0.949 | 0.096 | 0.742 → 0.810 | 1.1x sr_bytes | down | 3 |
| `RT-spread` | hop-spread | **text** | 0.725 → 0.817 | 0.092 | 0.703 → 0.811 | 2x sr_bytes | up | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.817 → 0.908 | 0.091 | 0.811 → 0.903 | 2.1x bytes_on_air | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.748 → 0.837 | 0.089 | 0.640 → 0.723 | 1.5x sr_airtime | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.733 → 0.808 | 0.075 | 0.518 → 0.559 | 1.5x sr_airtime | up | 2 |
| `FW-firmware` | profile | **held** | 0.892 → 0.959 | 0.067 | 0.811 → 0.861 | 3.3x bytes_on_air | down | 2 |
| `FW-versions` | profile | **text** | 0.817 → 0.883 | 0.066 | 0.811 → 0.875 | 3.5x bytes_on_air | down | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.821 → 0.882 | 0.061 | 0.810 → 0.877 | 1.1x sr_bytes | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.817 → 0.875 | 0.058 | 0.811 → 0.872 | 3.3x bytes_on_air | down | 2 |
| `MS-roles` | role-mix | **text** | 0.823 → 0.874 | 0.051 | 0.810 → 0.867 | 1.1x sr_bytes | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.767 → 0.818 | 0.051 | 0.759 → 0.812 | 1.5x sr_airtime | down | 4 |
| `SF-servers-flat` | servers | **held** | 0.871 → 0.918 | 0.048 | 0.806 → 0.815 | 7.8x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.871 → 0.918 | 0.048 | 0.806 → 0.815 | 7.8x sr_bytes | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.846 → 0.892 | 0.046 | 0.811 → 0.813 | 25x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.851 → 0.892 | 0.041 | 0.779 → 0.821 | 15x advert_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.892 → 0.928 | 0.036 | 0.811 → 0.826 | 1.3x sr_bytes | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.794 → 0.829 | 0.034 | 0.786 → 0.823 | 9.3x advert_bytes | up | 3 |
| `AD-flooding` | role-mix | **held** | 0.916 → 0.949 | 0.033 | 0.810 → 0.849 | 2.3x bytes_on_air | down | 2 |
| `AD-nomute` | role-mix | **held** | 0.916 → 0.949 | 0.033 | 0.810 → 0.849 | 2.3x bytes_on_air | down | 3 |
| `LD-diurnal` | diurnal | **text** | 0.817 → 0.845 | 0.028 | 0.811 → 0.841 | 1.2x sr_bytes | down | 3 |
| `AD-worst` | role-placement | **text** | 0.882 → 0.905 | 0.023 | 0.872 → 0.897 | 1x bytes_on_air | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.817 → 0.839 | 0.022 | 0.811 → 0.831 | 1.3x bytes_on_air | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.878 → 0.895 | 0.017 | 0.801 → 0.813 | 2.6x advert_bytes | up | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.847 → 0.863 | 0.016 | 0.776 → 0.792 | 1.2x sr_airtime | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.828 → 0.844 | 0.016 | 0.823 → 0.841 | 1.3x sr_bytes | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.876 → 0.892 | 0.016 | 0.804 → 0.815 | 3.1x advert_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.847 → 0.861 | 0.015 | 0.776 → 0.785 | 1.1x sr_airtime | up | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.899 → 0.913 | 0.014 | 0.821 → 0.835 | 1.1x sr_airtime | down | 4 |
| `SF-window-size` | window-size | **held** | 0.881 → 0.895 | 0.014 | 0.802 → 0.811 | 5.6x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **text** | 0.778 → 0.792 | 0.014 | 0.778 → 0.792 | 1.3x sr_airtime | up | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.817 → 0.829 | 0.012 | 0.802 → 0.811 | 2.5x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.879 → 0.890 | 0.011 | 0.809 → 0.818 | 3x sr_bytes | up | 2 |
| `SF-capacity` | capacity | **text** | 0.812 → 0.822 | 0.010 | 0.806 → 0.815 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.812 → 0.822 | 0.010 | 0.806 → 0.815 | 5.3x advert_bytes | down | 5 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.883 → 0.892 | 0.009 | 0.807 → 0.813 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.883 → 0.892 | 0.009 | 0.807 → 0.813 | 1.1x sr_bytes | up | 4 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.814 → 0.822 | 0.008 | 0.806 → 0.814 | 3.2x advert_bytes | down | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.880 → 0.888 | 0.008 | 0.805 → 0.808 | 5.3x advert_bytes | up | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.879 → 0.886 | 0.007 | 0.802 → 0.802 | 1.1x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.817 → 0.823 | 0.006 | 0.811 → 0.816 | 3.1x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.949 → 0.955 | 0.006 | 0.947 → 0.953 | 1.2x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **held** | 0.886 → 0.892 | 0.006 | 0.809 → 0.811 | 5.7x advert_bytes | = | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.887 → 0.892 | 0.005 | 0.811 → 0.814 | 1.3x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.817 → 0.822 | 0.005 | 0.811 → 0.815 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.955 → 0.959 | 0.004 | 0.953 → 0.958 | 1.1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.955 → 0.956 | 0.001 | 0.953 → 0.954 | 1x bytes_on_air | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario ridge`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| sprinkled | 1 | 0.878 | 0.872 | 0.006 | - | - | 0.944 | 0.944 | 0.577 | 1.24x | 16.3/26.7/31.4% | 1.7/5.1% | 3 |
| arms-race | 1 | 0.956 | 0.951 | 0.006 | - | - | 0.989 | 0.990 | 0.857 | 1.03x | 20.5/25.4/30.2% | 1.2/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.920 | 0.914 | 0.006 | - | - | 0.993 | 0.994 | 0.756 | 1.11x | 17.6/23.9/26.7% | 1.5/5.2% | 3 |
| 0.3 | 1 | 0.964 | 0.962 | 0.002 | - | - | 0.994 | 0.994 | 0.898 | 0.96x | 22.9/27.2/30.5% | 1.1/5.1% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.823 | 0.810 | 0.012 | - | - | 0.949 | 0.949 | 0.226 | 1.16x | 14.9/25.4/29.5% | 1.7/4.9% | 3 |
| inverse | 1 | 0.810 | 0.796 | 0.014 | - | - | 0.939 | 0.942 | 0.074 | 1.09x | 12.9/18.6/23.1% | 1.9/3.8% | 3 |
| random | 1 | 0.754 | 0.742 | 0.012 | - | - | 0.853 | 0.856 | 0.204 | 1.12x | 14.1/21.2/25.3% | 1.7/4.9% | 3 |

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.823 | 0.810 | 0.012 | - | - | 0.949 | 0.949 | 0.226 | 1.16x | 14.9/25.4/29.5% | 1.7/4.9% | 3 |
| all-routers | 1 | 0.855 | 0.849 | 0.006 | - | - | 0.916 | 0.916 | 0.369 | 2.66x | 30.1/38.9/42.8% | 4.3/4.8% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.823 | 0.810 | 0.012 | - | - | 0.949 | 0.949 | 0.226 | 1.16x | 14.9/25.4/29.5% | 1.7/4.9% | 3 |
| no-mute | 1 | 0.843 | 0.834 | 0.009 | - | - | 0.947 | 0.948 | 0.208 | 1.25x | 15.1/21.7/26.9% | 1.8/5.0% | 3 |
| all-routers | 1 | 0.855 | 0.849 | 0.006 | - | - | 0.916 | 0.916 | 0.369 | 2.66x | 30.1/38.9/42.8% | 4.3/4.8% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.823 | 0.810 | 0.012 | - | - | 0.949 | 0.949 | 0.226 | 1.16x | 14.9/25.4/29.5% | 1.7/4.9% | 3 |
| local-typical | 1 | 0.526 | 0.510 | 0.015 | - | - | 0.680 | 0.742 | 0.000 | 1.18x | 12.5/25.4/31.8% | 1.9/5.4% | 3 |
| basement-heavy | 1 | 0.092 | 0.091 | 0.000 | - | - | 0.227 | 0.228 | 0.000 | 0.61x | 3.4/6.2/9.9% | 0.5/2.6% | 3 |

> siting-mix=local-typical: decode_failures 22

> siting-mix=basement-heavy: decode_failures 1

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.905 | 0.897 | 0.007 | - | - | 0.990 | 0.991 | 0.000 | 2.28x | 18.9/31.4/38.7% | 1.7/5.2% | 3 |
| inverse | 1 | 0.882 | 0.872 | 0.010 | - | - | 0.981 | 0.981 | 0.000 | 2.18x | 16.5/25.8/33.1% | 1.6/3.2% | 3 |

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.814 | 0.814 | 0.000 | - | - | 0 | 0.000 | 0.102 | 1.27x | 15.7/23.9/27.4% | 1.8/4.8% | 3 |
| sr | 1 | 0.820 | 0.814 | 0.006 | - | - | 0.648 | 0.888 | 0.101 | 1.29x | 15.7/24.4/27.8% | 1.8/4.9% | 3 |

> protocol=sr: decode_failures 4

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.732 | 0.724 | 0.007 | - | - | 0.773 | 0.775 | 0.125 | 3.04x | 35.6/56.0/61.8% | 4.6/9.1% | 3 |
| 100 | 1 | 0.851 | 0.848 | 0.003 | - | - | 0.891 | 0.892 | 0.087 | 1.58x | 18.4/31.0/34.9% | 2.2/4.9% | 3 |
| 120 | 1 | 0.851 | 0.848 | 0.003 | - | - | 0.891 | 0.892 | 0.087 | 1.58x | 18.4/31.0/34.9% | 2.2/4.9% | 3 |
| 250 | 1 | 0.851 | 0.848 | 0.003 | - | - | 0.891 | 0.892 | 0.087 | 1.58x | 18.4/31.0/34.9% | 2.2/4.9% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.323 | 0.316 | 0.007 | - | - | 0.421 | 0.497 | 0.000 | 11.47x | 39.7/62.3/76.5% | 4.2/11.2% | 3 |
| 120 | 1 | 0.529 | 0.518 | 0.012 | - | - | 0.733 | 0.745 | 0.000 | 4.79x | 16.4/33.3/45.7% | 1.6/5.8% | 3 |
| 250 | 1 | 0.538 | 0.526 | 0.011 | - | - | 0.749 | 0.763 | 0.000 | 4.67x | 16.1/32.4/43.9% | 1.6/5.7% | 3 |

> max-num-nodes=10: decode_failures 52

> max-num-nodes=120: decode_failures 51

> max-num-nodes=250: decode_failures 58

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.851 | 0.848 | 0.003 | - | - | 0.891 | 0.892 | 0.087 | 1.58x | 18.4/31.0/34.9% | 2.2/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.851 | 0.848 | 0.003 | - | - | 0.891 | 0.892 | 0.087 | 1.58x | 18.4/31.0/34.9% | 2.2/4.9% | 3 |
| constrained | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.762 | 0.762 | 0.118 | 3.05x | 35.5/55.9/61.9% | 4.6/9.0% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.731 | 0.723 | 0.008 | - | - | 0.837 | 0.896 | 0.521 | 5.99x | 60.8/72.3/77.2% | 4.3/13.9% | 3 |
| 25 | 1 | 0.731 | 0.723 | 0.008 | - | - | 0.837 | 0.896 | 0.521 | 5.99x | 60.8/72.3/77.2% | 4.3/13.9% | 3 |
| 100 | 1 | 0.731 | 0.723 | 0.008 | - | - | 0.837 | 0.896 | 0.521 | 5.99x | 60.8/72.3/77.2% | 4.3/13.9% | 3 |
| 2000 | 1 | 0.731 | 0.723 | 0.008 | - | - | 0.837 | 0.896 | 0.521 | 5.99x | 60.8/72.3/77.2% | 4.3/13.9% | 3 |

> warm-num-nodes=0: queue drops 15.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 120

> warm-num-nodes=25: queue drops 15.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 120

> warm-num-nodes=100: queue drops 15.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 120

> warm-num-nodes=2000: queue drops 15.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 120

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.730 | 0.712 | 0.018 | - | - | 0.878 | 0.880 | 0.149 | 1.22x | 15.1/23.4/26.8% | 1.7/4.5% | 3 |
| 0.2 | 1 | 0.638 | 0.606 | 0.031 | - | - | 0.837 | 0.841 | 0.162 | 1.13x | 14.2/22.0/25.6% | 1.6/4.0% | 3 |
| 0.3 | 1 | 0.532 | 0.497 | 0.035 | - | - | 0.759 | 0.781 | 0.152 | 1.04x | 13.2/20.6/24.3% | 1.5/3.7% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 18

> faster: 2.38 s per simulated hour against 5.15 over 41 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.796 | 0.789 | 0.007 | - | - | 0.881 | 0.883 | 0.154 | 1.33x | 16.5/24.9/28.7% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.752 | 0.741 | 0.011 | - | - | 0.865 | 0.869 | 0.136 | 1.41x | 17.3/26.5/30.3% | 2.0/4.7% | 3 |
| 0.3 | 1 | 0.693 | 0.679 | 0.013 | - | - | 0.809 | 0.814 | 0.181 | 1.41x | 17.5/27.2/30.9% | 2.1/4.5% | 3 |

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.703 | 0.688 | 0.016 | - | - | 0.835 | 0.854 | 0.180 | 1.23x | 15.2/23.3/26.9% | 1.8/4.5% | 3 |
| 0.2 | 1 | 0.590 | 0.573 | 0.018 | - | - | 0.766 | 0.802 | 0.118 | 1.14x | 14.2/22.2/25.9% | 1.6/4.3% | 3 |
| 0.3 | 1 | 0.537 | 0.514 | 0.023 | - | - | 0.738 | 0.820 | 0.164 | 1.10x | 13.8/21.7/25.2% | 1.6/4.0% | 3 |

> burst-loss=0.1: decode_failures 6

> burst-loss=0.2: decode_failures 36

> burst-loss=0.3: decode_failures 28

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.778 | 0.778 | 0.000 | - | - | 0.857 | 0.859 | 0.091 | 1.65x | 20.2/31.6/35.9% | 2.3/6.3% | 3 |
| directed-with-late-flood | 1 | 0.792 | 0.792 | 0.000 | - | - | 0.863 | 0.866 | 0.102 | 1.51x | 18.6/28.8/32.9% | 2.1/5.8% | 3 |
| m4-early-flood | 1 | 0.784 | 0.784 | 0.000 | - | - | 0.859 | 0.860 | 0.090 | 1.53x | 18.8/29.2/33.2% | 2.1/5.8% | 3 |

> faster: 1.21 s per simulated hour against 3.31 over 41 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.870 | 0.861 | 0.009 | - | - | 0.959 | 0.960 | 0.523 | 0.70x | 8.3/11.9/13.6% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

> faster: 0.85 s per simulated hour against 1.78 over 41 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.918 | 0.912 | 0.006 | - | - | 0.968 | 0.968 | 0.700 | 1.22x | 15.4/23.0/24.7% | 1.8/4.6% | 3 |
| 0.5 | 1 | 0.880 | 0.875 | 0.005 | - | - | 0.961 | 0.962 | 0.655 | 1.03x | 13.3/19.3/21.1% | 1.5/4.3% | 3 |
| 0.75 | 1 | 0.876 | 0.870 | 0.006 | - | - | 0.965 | 0.967 | 0.540 | 0.87x | 11.1/14.5/17.9% | 1.3/3.5% | 3 |

> legacy-fraction=0.75: decode_failures 1

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.908 | 0.903 | 0.004 | - | - | 0.962 | 0.963 | 0.674 | 1.22x | 15.2/23.1/24.7% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.885 | 0.880 | 0.005 | - | - | 0.961 | 0.962 | 0.659 | 1.01x | 13.1/19.0/21.1% | 1.5/4.3% | 3 |
| 0.75 | 1 | 0.872 | 0.867 | 0.005 | - | - | 0.959 | 0.962 | 0.511 | 0.85x | 10.9/14.3/18.1% | 1.3/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.875 | 0.872 | 0.003 | - | - | 0.942 | 0.942 | 0.128 | 0.70x | 8.9/13.6/16.0% | 0.9/2.8% | 3 |
| signing=true | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.860 | 0.851 | 0.009 | - | - | 0.949 | 0.949 | 0.500 | 0.70x | 8.6/12.4/15.3% | 1.1/2.3% | 3 |
| 2.5 | 1 | 0.857 | 0.846 | 0.011 | - | - | 0.955 | 0.956 | 0.447 | 0.70x | 8.5/12.2/15.1% | 1.0/2.2% | 3 |
| 2.6 | 1 | 0.864 | 0.853 | 0.011 | - | - | 0.956 | 0.958 | 0.499 | 0.67x | 8.4/11.9/15.0% | 1.0/2.3% | 3 |
| 2.7 | 1 | 0.883 | 0.875 | 0.008 | - | - | 0.958 | 0.960 | 0.478 | 0.71x | 8.9/14.7/17.4% | 1.0/3.1% | 3 |
| 2.8 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.867 | 0.862 | 0.005 | - | - | 0.932 | 0.932 | 0.140 | 0.86x | 10.6/16.2/18.5% | 1.2/3.3% | 3 |
| 900 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.837 | 0.837 | 0.146 | 2.06x | 24.9/38.3/43.5% | 2.9/7.7% | 3 |
| 300 | 1 | 0.500 | 0.489 | 0.010 | - | - | 0.591 | 0.597 | 0.092 | 4.29x | 49.5/69.5/77.2% | 6.3/14.5% | 3 |

> broadcast-interval-s=300: decode_failures 1

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.919 | 0.916 | 0.003 | - | - | 0.968 | 0.968 | 0.148 | 0.99x | 12.2/18.0/20.8% | 1.4/3.5% | 3 |
| 900 | 1 | 0.842 | 0.837 | 0.005 | - | - | 0.894 | 0.894 | 0.155 | 2.31x | 28.0/40.6/46.2% | 3.4/8.1% | 3 |
| 300 | 1 | 0.564 | 0.553 | 0.011 | - | - | 0.656 | 0.660 | 0.143 | 4.74x | 53.3/70.4/78.6% | 7.0/15.3% | 3 |

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.845 | 0.841 | 0.004 | - | - | 0.909 | 0.911 | 0.131 | 1.21x | 14.8/22.8/26.0% | 1.7/4.6% | 3 |
| sinusoid | 1 | 0.840 | 0.833 | 0.007 | - | - | 0.914 | 0.915 | 0.120 | 1.16x | 14.2/21.9/25.2% | 1.6/4.4% | 3 |
| commuter | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.837 | 0.837 | 0.146 | 2.06x | 24.9/38.3/43.5% | 2.9/7.7% | 3 |
| 3600 | 1 | 0.867 | 0.862 | 0.005 | - | - | 0.932 | 0.932 | 0.140 | 0.86x | 10.6/16.2/18.5% | 1.2/3.3% | 3 |
| 10800 | 1 | 0.883 | 0.879 | 0.004 | - | - | 0.949 | 0.949 | 0.115 | 0.60x | 7.3/11.1/12.7% | 0.9/2.2% | 3 |
| 43200 | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.955 | 0.955 | 0.129 | 0.41x | 5.1/7.8/8.9% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.818 | 0.812 | 0.006 | - | - | 0.887 | 0.888 | 0.139 | 1.36x | 16.7/25.6/29.2% | 1.9/5.1% | 3 |
| 1.0 | 1 | 0.797 | 0.790 | 0.007 | - | - | 0.860 | 0.862 | 0.149 | 1.49x | 18.3/28.2/32.2% | 2.1/5.7% | 3 |
| 4.0 | 1 | 0.767 | 0.759 | 0.008 | - | - | 0.850 | 0.851 | 0.121 | 1.85x | 23.0/35.6/40.6% | 2.6/7.1% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.731 | 0.723 | 0.008 | - | - | 0.837 | 0.896 | 0.521 | 5.99x | 60.8/72.3/77.2% | 4.3/13.9% | 3 |
| 1.0 | 1 | 0.645 | 0.640 | 0.006 | - | - | 0.748 | 0.830 | 0.462 | 6.56x | 63.9/74.2/78.6% | 4.8/14.9% | 3 |

> traceroute-per-hour=0.0: queue drops 15.0% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 120

> traceroute-per-hour=1.0: queue drops 25.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 101

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.649 | 0.636 | 0.012 | - | - | 0.819 | 0.820 | 0.268 | 1.22x | 17.0/29.2/34.2% | 2.6/7.0% | 3 |
| 60 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 90 | 1 | 0.921 | 0.915 | 0.006 | - | - | 0.990 | 0.990 | 0.779 | 1.51x | 17.8/27.5/29.9% | 1.4/4.7% | 3 |
| 120 | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.998 | 0.998 | 0.748 | 2.08x | 24.0/32.4/38.3% | 1.3/5.2% | 3 |
| 150 | 1 | 0.973 | 0.971 | 0.001 | - | - | 0.998 | 0.998 | 0.855 | 2.76x | 29.9/46.8/53.6% | 1.4/5.5% | 3 |

> nodes=150: decode_failures 3

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 120 | 1 | 0.742 | 0.727 | 0.016 | - | - | 0.914 | 0.916 | 0.245 | 2.17x | 14.7/23.2/30.3% | 1.5/5.6% | 3 |
| 250 | 1 | 0.529 | 0.516 | 0.013 | - | - | 0.733 | 0.753 | 0.000 | 5.19x | 17.8/36.3/49.4% | 1.8/6.4% | 3 |
| 500 | 1 | 0.301 | 0.299 | 0.002 | - | - | 0.274 | 0.274 | 0.000 | 9.88x | 18.8/30.5/46.0% | 1.7/5.4% | 3 |

> nodes=250: decode_failures 120

> nodes=500: decode_failures 3

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.751 | 0.737 | 0.013 | - | - | 0.910 | 0.913 | 0.235 | 2.00x | 13.8/21.3/27.6% | 1.5/5.0% | 3 |
| 250 | 1 | 0.529 | 0.518 | 0.012 | - | - | 0.733 | 0.745 | 0.000 | 4.79x | 16.4/33.3/45.7% | 1.6/5.8% | 3 |
| 500 | 1 | 0.303 | 0.301 | 0.002 | - | - | 0.287 | 0.288 | 0.000 | 9.31x | 17.5/28.5/43.4% | 1.6/5.1% | 3 |

> nodes=250: decode_failures 51

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.874 | 0.867 | 0.006 | - | - | 0.951 | 0.952 | 0.150 | 1.31x | 15.9/25.2/28.6% | 1.8/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.823 | 0.810 | 0.012 | - | - | 0.949 | 0.949 | 0.226 | 1.16x | 14.9/25.4/29.5% | 1.7/4.9% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.882 | 0.877 | 0.005 | - | - | 0.941 | 0.941 | 0.142 | 1.37x | 16.7/25.5/29.2% | 2.0/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.821 | 0.810 | 0.011 | - | - | 0.901 | 0.902 | 0.269 | 1.29x | 16.1/27.8/32.0% | 2.0/4.8% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.05 | 1 | 0.827 | 0.820 | 0.007 | - | - | 0.881 | 0.881 | 0.129 | 1.40x | 16.6/28.5/32.3% | 1.9/4.7% | 3 |
| 0.1 | 1 | 0.829 | 0.822 | 0.007 | - | - | 0.883 | 0.884 | 0.161 | 1.53x | 18.5/31.5/36.1% | 2.1/4.8% | 3 |
| 0.2 | 1 | 0.839 | 0.831 | 0.008 | - | - | 0.900 | 0.900 | 0.140 | 1.68x | 21.0/34.8/38.5% | 2.3/4.8% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| local-typical | 1 | 0.615 | 0.599 | 0.016 | - | - | 0.800 | 0.811 | 0.000 | 1.40x | 14.4/27.0/32.9% | 2.2/5.3% | 3 |
| event | 1 | 0.387 | 0.378 | 0.009 | - | - | 0.590 | 0.624 | 0.000 | 1.75x | 11.1/22.1/35.8% | 3.0/5.6% | 3 |
| backbone | 1 | 0.975 | 0.975 | 0.001 | - | - | 0.999 | 0.999 | 0.840 | 1.07x | 30.1/35.2/38.2% | 1.1/5.5% | 3 |

> siting-mix=event: decode_failures 7

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.856 | 0.850 | 0.006 | - | - | 0.921 | 0.924 | 0.728 | 1.45x | 26.1/34.3/37.1% | 3.4/7.6% | 3 |
| 60 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 90 | 1 | 0.779 | 0.767 | 0.012 | - | - | 0.976 | 0.977 | 0.326 | 1.66x | 14.0/24.1/27.8% | 1.6/5.0% | 3 |
| 120 | 1 | 0.742 | 0.727 | 0.016 | - | - | 0.914 | 0.916 | 0.245 | 2.17x | 14.7/23.2/30.3% | 1.5/5.6% | 3 |
| 150 | 1 | 0.646 | 0.637 | 0.009 | - | - | 0.849 | 0.850 | 0.151 | 2.83x | 14.9/29.8/39.4% | 1.6/5.3% | 3 |

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 1.25 | 1 | 0.600 | 0.592 | 0.008 | - | - | 0.735 | 0.737 | 0.000 | 1.33x | 12.1/18.6/24.8% | 1.9/4.5% | 3 |
| 1.5 | 1 | 0.347 | 0.342 | 0.005 | - | - | 0.525 | 0.528 | 0.000 | 1.55x | 11.2/18.5/23.6% | 2.3/5.5% | 3 |
| 2.0 | 1 | 0.152 | 0.147 | 0.005 | - | - | 0.395 | 0.406 | 0.000 | 0.90x | 3.9/10.0/13.3% | 1.2/3.6% | 3 |

> stretch=2.0: decode_failures 11

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| clustered | 1 | 0.888 | 0.884 | 0.004 | - | - | 0.951 | 0.951 | 0.000 | 1.15x | 28.2/37.2/39.2% | 1.3/5.5% | 3 |
| corridor | 1 | 0.590 | 0.576 | 0.014 | - | - | 0.767 | 0.769 | 0.277 | 1.42x | 16.8/29.0/32.4% | 2.1/5.3% | 3 |
| hub | 1 | 0.967 | 0.966 | 0.001 | - | - | 0.994 | 0.994 | 0.883 | 1.24x | 26.8/35.8/37.4% | 1.6/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.792 | 0.792 | 0.000 | - | - | 0.863 | 0.866 | 0.102 | 1.51x | 18.6/28.8/32.9% | 2.1/5.8% | 3 |
| True | 1 | 0.776 | 0.776 | 0.000 | - | - | 0.847 | 0.849 | 0.100 | 1.52x | 18.7/29.2/33.2% | 2.1/5.8% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.776 | 0.776 | 0.000 | - | - | 0.847 | 0.849 | 0.100 | 1.52x | 18.7/29.2/33.2% | 2.1/5.8% | 3 |
| m4-early-flood | 1 | 0.785 | 0.785 | 0.000 | - | - | 0.861 | 0.864 | 0.104 | 1.55x | 18.9/29.7/33.7% | 2.1/5.9% | 3 |

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.814 | 0.814 | 0.000 | - | - | 0 | 0.000 | 0.102 | 1.27x | 15.7/23.9/27.4% | 1.8/4.8% | 3 |
| chain | 1 | 0.802 | 0.799 | 0.003 | - | - | 0.847 | 0.872 | 0.132 | 1.49x | 18.0/28.0/32.2% | 2.1/5.6% | 3 |
| sr | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| True | 1 | 0.822 | 0.815 | 0.007 | - | - | 0.891 | 0.892 | 0.139 | 1.31x | 16.1/24.5/28.0% | 1.8/4.9% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.998 | 0.998 | 0.748 | 2.08x | 24.0/32.4/38.3% | 1.3/5.2% | 3 |
| True | 1 | 0.956 | 0.954 | 0.002 | - | - | 0.998 | 0.998 | 0.768 | 2.13x | 24.4/32.6/38.5% | 1.3/5.2% | 3 |

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.166 | 0.162 | 0.004 | - | - | 0.419 | 0.433 | 0.000 | 0.04x | 0.2/0.5/0.8% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.315 | 0.313 | 0.002 | - | - | 0.468 | 0.474 | 0.000 | 0.22x | 1.6/2.6/3.4% | 0.3/0.9% | 3 |
| LONG_TURBO | 1 | 0.733 | 0.724 | 0.009 | - | - | 0.795 | 0.797 | 0.000 | 1.26x | 11.9/18.8/24.3% | 1.8/4.4% | 3 |

> preset=SHORT_TURBO: decode_failures 6

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.846 | 0.840 | 0.005 | - | - | 0.899 | 0.899 | 0.271 | 1.22x | 18.6/26.5/29.6% | 1.7/5.0% | 3 |
| 1.0 | 1 | 0.919 | 0.916 | 0.004 | - | - | 0.950 | 0.950 | 0.697 | 0.95x | 27.7/34.2/35.3% | 1.2/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.248 | 0.245 | 0.003 | - | - | 0.450 | 0.484 | 0.000 | 0.11x | 0.6/1.5/2.2% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| LITE_FAST | 1 | 0.764 | 0.755 | 0.009 | - | - | 0.850 | 0.851 | 0.115 | 1.00x | 10.1/17.0/19.8% | 1.4/3.8% | 3 |
| NARROW_SLOW | 1 | 0.788 | 0.780 | 0.008 | - | - | 0.855 | 0.857 | 0.123 | 1.27x | 14.1/21.6/24.7% | 1.8/4.8% | 3 |

> preset=SHORT_FAST: decode_failures 2

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| temporal | 1 | 0.718 | 0.708 | 0.010 | - | - | 0.822 | 0.823 | 0.087 | 1.27x | 15.0/23.3/27.0% | 1.9/4.6% | 3 |
| transient | 1 | 0.827 | 0.819 | 0.008 | - | - | 0.904 | 0.905 | 0.133 | 1.30x | 15.9/24.4/27.9% | 1.8/4.9% | 3 |
| periodic | 1 | 0.675 | 0.666 | 0.009 | - | - | 0.752 | 0.755 | 0.120 | 1.20x | 14.9/22.8/26.5% | 1.7/4.3% | 3 |

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.248 | 0.245 | 0.003 | - | - | 0.450 | 0.484 | 0.000 | 0.11x | 0.6/1.5/2.2% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| LONG_MODERATE | 1 | 0.813 | 0.802 | 0.011 | - | - | 0.886 | 0.888 | 0.618 | 3.24x | 46.4/60.0/62.3% | 4.5/12.1% | 3 |

> preset=SHORT_FAST: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.074 | 0.073 | 0.001 | - | - | 0.173 | 0.174 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.166 | 0.162 | 0.004 | - | - | 0.419 | 0.433 | 0.000 | 0.04x | 0.2/0.5/0.8% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| LONG_TURBO | 1 | 0.733 | 0.724 | 0.009 | - | - | 0.795 | 0.797 | 0.000 | 1.26x | 11.9/18.8/24.3% | 1.8/4.4% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.808 | 0.801 | 0.007 | - | - | 0.879 | 0.880 | 0.186 | 1.80x | 20.5/30.8/34.3% | 2.7/6.5% | 3 |

> preset=SHORT_TURBO: decode_failures 6

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.759 | 0.753 | 0.006 | - | - | 0.834 | 0.837 | 0.131 | 1.27x | 15.7/24.1/27.6% | 1.8/4.7% | 3 |
| 10000 | 1 | 0.675 | 0.666 | 0.009 | - | - | 0.752 | 0.755 | 0.120 | 1.20x | 14.9/22.8/26.5% | 1.7/4.3% | 3 |
| 4000 | 1 | 0.428 | 0.424 | 0.004 | - | - | 0.487 | 0.542 | 0.093 | 1.02x | 12.5/19.5/22.7% | 1.4/3.2% | 3 |
| 2000 | 1 | 0.093 | 0.093 | 0.000 | - | - | 0.099 | 0.172 | 0.014 | 0.71x | 9.1/14.4/17.0% | 1.1/1.9% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 5

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.347 | 0.342 | 0.005 | - | - | 0.525 | 0.528 | 0.000 | 1.55x | 11.2/18.5/23.6% | 2.3/5.5% | 3 |
| 1.0 | 1 | 0.783 | 0.777 | 0.006 | - | - | 0.854 | 0.854 | 0.592 | 1.01x | 21.1/26.7/28.8% | 1.3/5.0% | 3 |

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 22 | 1 | 0.292 | 0.289 | 0.003 | - | - | 0.455 | 0.458 | 0.000 | 1.45x | 10.0/17.2/21.4% | 2.2/5.3% | 3 |
| 17 | 1 | 0.159 | 0.151 | 0.009 | - | - | 0.381 | 0.397 | 0.000 | 0.92x | 4.0/10.9/14.3% | 1.2/4.0% | 3 |
| 14 | 1 | 0.097 | 0.094 | 0.002 | - | - | 0.196 | 0.211 | 0.000 | 0.73x | 3.0/6.9/8.8% | 1.1/2.8% | 3 |

> tx-power=17: decode_failures 3

> tx-power=14: decode_failures 3

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.998 | 0.998 | 0.748 | 2.08x | 24.0/32.4/38.3% | 1.3/5.2% | 3 |
| True | 1 | 0.949 | 0.947 | 0.003 | - | - | 0.998 | 0.998 | 0.749 | 2.44x | 27.6/36.1/42.1% | 1.6/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.828 | 0.823 | 0.006 | - | - | 0.882 | 0.883 | 0.101 | 1.40x | 16.5/27.9/31.7% | 2.0/4.9% | 3 |
| True | 1 | 0.844 | 0.841 | 0.003 | - | - | 0.885 | 0.885 | 0.095 | 1.46x | 17.1/28.5/32.4% | 2.1/4.9% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| random | 1 | 0.837 | 0.826 | 0.011 | - | - | 0.928 | 0.929 | 0.153 | 1.28x | 15.6/24.3/27.8% | 1.8/4.9% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.725 | 0.703 | 0.021 | - | - | 0.915 | 0.915 | 0.201 | 0.99x | 12.4/20.0/23.2% | 1.3/4.2% | 3 |
| 7 | 1 | 0.899 | 0.895 | 0.004 | - | - | 0.947 | 0.947 | 0.162 | 1.45x | 17.9/25.9/29.9% | 2.1/5.1% | 3 |
| 15 | 1 | 0.912 | 0.910 | 0.002 | - | - | 0.953 | 0.953 | 0.142 | 1.44x | 17.8/25.8/29.6% | 2.0/5.1% | 3 |
| 32 | 1 | 0.912 | 0.910 | 0.002 | - | - | 0.953 | 0.953 | 0.142 | 1.44x | 17.8/25.8/29.6% | 2.0/5.1% | 3 |

> hop-limit=15: misdecodes 1

> hop-limit=32: misdecodes 1

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.725 | 0.703 | 0.021 | - | - | 0.915 | 0.915 | 0.201 | 0.99x | 12.4/20.0/23.2% | 1.3/4.2% | 3 |
| 5 | 1 | 0.852 | 0.844 | 0.008 | - | - | 0.934 | 0.936 | 0.160 | 1.32x | 16.1/24.6/28.1% | 1.9/4.9% | 3 |
| 7 | 1 | 0.899 | 0.895 | 0.004 | - | - | 0.947 | 0.947 | 0.162 | 1.45x | 17.9/25.9/29.9% | 2.1/5.1% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| KNOWN_ONLY | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.813 | 0.813 | 0.000 | - | - | 0.846 | 0.890 | 0.094 | 1.28x | 15.7/24.0/27.4% | 1.8/4.8% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.725 | 0.703 | 0.021 | - | - | 0.915 | 0.915 | 0.201 | 0.99x | 12.4/20.0/23.2% | 1.3/4.2% | 3 |
| True | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| BALANCED | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| STRICT | 1 | 0.650 | 0.650 | 0.000 | - | - | 0.715 | 0.715 | 0.043 | 1.40x | 17.2/26.3/30.1% | 2.0/5.3% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| dm | 1 | 0.823 | 0.816 | 0.007 | - | - | 0.887 | 0.889 | 0.149 | 1.30x | 15.9/24.5/28.1% | 1.8/4.9% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.822 | 0.814 | 0.008 | - | - | 0.893 | 0.895 | 0.159 | 1.29x | 15.9/24.2/27.6% | 1.8/4.8% | 3 |
| local | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| time | 1 | 0.814 | 0.806 | 0.007 | - | - | 0.888 | 0.889 | 0.136 | 1.34x | 16.3/25.3/28.8% | 1.9/5.0% | 3 |
| window | 1 | 0.818 | 0.811 | 0.007 | - | - | 0.895 | 0.896 | 0.135 | 1.31x | 16.0/24.6/28.1% | 1.9/4.9% | 3 |

> bucket-mode=global: misdecodes 35

> bucket-mode=time: misdecodes 40

> bucket-mode=window: misdecodes 26

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.811 | 0.805 | 0.006 | - | - | 0.880 | 0.881 | 0.140 | 1.47x | 17.7/27.8/31.5% | 2.1/5.6% | 3 |
| 1800 | 1 | 0.814 | 0.806 | 0.007 | - | - | 0.888 | 0.889 | 0.136 | 1.34x | 16.3/25.3/28.8% | 1.9/5.0% | 3 |
| 3600 | 1 | 0.814 | 0.808 | 0.006 | - | - | 0.883 | 0.883 | 0.143 | 1.32x | 16.1/24.9/28.4% | 1.9/5.0% | 3 |

> time-bucket-s=600: misdecodes 127

> time-bucket-s=1800: misdecodes 40

> time-bucket-s=3600: misdecodes 17

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| interval | 1 | 0.789 | 0.779 | 0.009 | - | - | 0.851 | 0.851 | 0.132 | 1.75x | 21.1/33.1/37.9% | 2.5/7.2% | 3 |
| aimd | 1 | 0.823 | 0.821 | 0.002 | - | - | 0.872 | 0.899 | 0.123 | 1.31x | 16.0/24.7/28.3% | 1.9/4.9% | 3 |
| bucket+interval | 1 | 0.794 | 0.786 | 0.008 | - | - | 0.870 | 0.870 | 0.129 | 1.76x | 21.4/33.5/38.2% | 2.5/7.0% | 3 |

> trigger=interval: misdecodes 23

> trigger=aimd: misdecodes 4

> trigger=aimd: decode_failures 6

> trigger=bucket+interval: misdecodes 18

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.822 | 0.815 | 0.007 | - | - | 0.890 | 0.892 | 0.148 | 1.30x | 15.9/24.4/27.9% | 1.8/4.9% | 3 |
| 8 | 1 | 0.818 | 0.811 | 0.006 | - | - | 0.884 | 0.885 | 0.124 | 1.30x | 15.9/24.5/27.9% | 1.9/4.9% | 3 |
| 16 | 1 | 0.820 | 0.814 | 0.007 | - | - | 0.892 | 0.892 | 0.138 | 1.29x | 15.8/24.4/27.8% | 1.8/4.9% | 3 |
| 32 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 50 | 1 | 0.812 | 0.806 | 0.005 | - | - | 0.886 | 0.887 | 0.144 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

> capacity=4: decode_failures 47

> capacity=8: decode_failures 11

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.822 | 0.815 | 0.007 | - | - | 0.890 | 0.892 | 0.148 | 1.30x | 15.9/24.4/27.9% | 1.8/4.9% | 3 |
| 8 | 1 | 0.818 | 0.811 | 0.006 | - | - | 0.884 | 0.885 | 0.124 | 1.30x | 15.9/24.5/27.9% | 1.9/4.9% | 3 |
| 16 | 1 | 0.820 | 0.814 | 0.007 | - | - | 0.892 | 0.892 | 0.138 | 1.29x | 15.8/24.4/27.8% | 1.8/4.9% | 3 |
| 32 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 50 | 1 | 0.812 | 0.806 | 0.005 | - | - | 0.886 | 0.887 | 0.144 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

> capacity=4: decode_failures 47

> capacity=8: decode_failures 11

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.808 | 0.801 | 0.006 | - | - | 0.878 | 0.881 | 0.142 | 1.28x | 15.7/23.9/27.4% | 1.8/4.8% | 3 |
| 16 | 1 | 0.819 | 0.813 | 0.006 | - | - | 0.888 | 0.889 | 0.140 | 1.30x | 15.9/24.3/27.8% | 1.8/4.9% | 3 |
| 32 | 1 | 0.818 | 0.811 | 0.007 | - | - | 0.895 | 0.896 | 0.135 | 1.31x | 16.0/24.6/28.1% | 1.9/4.9% | 3 |

> capacity=8: misdecodes 30

> capacity=8: decode_failures 5

> capacity=16: misdecodes 35

> capacity=32: misdecodes 26

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.794 | 0.786 | 0.008 | - | - | 0.870 | 0.870 | 0.129 | 1.76x | 21.4/33.5/38.2% | 2.5/7.0% | 3 |
| 02-06 | 1 | 0.829 | 0.823 | 0.005 | - | - | 0.889 | 0.906 | 0.121 | 1.36x | 16.7/25.6/29.4% | 1.9/5.1% | 3 |
| 00-08 | 1 | 0.821 | 0.815 | 0.006 | - | - | 0.885 | 0.900 | 0.131 | 1.42x | 17.1/26.7/30.7% | 2.0/5.5% | 3 |

> catch-up-hours=: misdecodes 18

> catch-up-hours=02-06: decode_failures 31

> catch-up-hours=00-08: misdecodes 2

> catch-up-hours=00-08: decode_failures 28

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.820 | 0.818 | 0.002 | - | - | 0.870 | 0.870 | 0.098 | 1.32x | 16.2/24.7/28.2% | 1.9/5.0% | 3 |
| 2 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 3 | 1 | 0.820 | 0.814 | 0.006 | - | - | 0.648 | 0.888 | 0.101 | 1.29x | 15.7/24.4/27.8% | 1.8/4.9% | 3 |
| 4 | 1 | 0.846 | 0.807 | 0.039 | - | - | 0.948 | 0.959 | 0.091 | 1.31x | 16.0/24.7/28.0% | 1.9/4.9% | 3 |

> hops-apart=3: decode_failures 4

> hops-apart=4: decode_failures 7

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.820 | 0.818 | 0.002 | - | - | 0.870 | 0.870 | 0.098 | 1.32x | 16.2/24.7/28.2% | 1.9/5.0% | 3 |
| 2 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 3 | 1 | 0.820 | 0.814 | 0.006 | - | - | 0.648 | 0.888 | 0.101 | 1.29x | 15.7/24.4/27.8% | 1.8/4.9% | 3 |
| 4 | 1 | 0.846 | 0.807 | 0.039 | - | - | 0.948 | 0.959 | 0.091 | 1.31x | 16.0/24.7/28.0% | 1.9/4.9% | 3 |
| 5 | 1 | 0.839 | 0.811 | 0.028 | - | - | 0.932 | 0.942 | 0.107 | 1.31x | 15.9/24.6/28.2% | 1.8/4.9% | 3 |

> hops-apart=3: decode_failures 4

> hops-apart=4: decode_failures 7

> faster: 1.92 s per simulated hour against 4.81 over 41 prior run(s) - 2.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.818 | 0.813 | 0.006 | - | - | 0.886 | 0.888 | 0.126 | 1.28x | 15.7/24.1/27.6% | 1.8/4.8% | 3 |
| 30 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 120 | 1 | 0.815 | 0.811 | 0.004 | - | - | 0.883 | 0.883 | 0.128 | 1.30x | 15.9/24.4/27.9% | 1.8/4.9% | 3 |
| 600 | 1 | 0.815 | 0.807 | 0.007 | - | - | 0.886 | 0.889 | 0.121 | 1.31x | 16.1/24.7/28.3% | 1.9/4.9% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.818 | 0.813 | 0.006 | - | - | 0.886 | 0.888 | 0.126 | 1.28x | 15.7/24.1/27.6% | 1.8/4.8% | 3 |
| 30 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 120 | 1 | 0.815 | 0.811 | 0.004 | - | - | 0.883 | 0.883 | 0.128 | 1.30x | 15.9/24.4/27.9% | 1.8/4.9% | 3 |
| 600 | 1 | 0.815 | 0.807 | 0.007 | - | - | 0.886 | 0.889 | 0.121 | 1.31x | 16.1/24.7/28.3% | 1.9/4.9% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.840 | 0.804 | 0.035 | - | - | 0.674 | 0.934 | 0.089 | 1.30x | 16.0/24.6/27.7% | 1.8/4.8% | 3 |
| routers | 1 | 0.821 | 0.818 | 0.003 | - | - | 0.879 | 0.879 | 0.087 | 1.30x | 15.9/24.5/28.0% | 1.8/4.9% | 3 |
| alternate-routers | 1 | 0.820 | 0.815 | 0.005 | - | - | 0.893 | 0.895 | 0.100 | 1.31x | 16.0/24.7/28.1% | 1.8/5.0% | 3 |
| beside-router | 1 | 0.810 | 0.807 | 0.004 | - | - | 0.879 | 0.879 | 0.100 | 1.31x | 15.9/24.7/28.2% | 1.8/4.9% | 3 |
| random-clients | 1 | 0.819 | 0.804 | 0.015 | - | - | 0.939 | 0.942 | 0.099 | 1.33x | 16.4/24.5/28.0% | 1.9/4.9% | 3 |
| hops-apart | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

> place=spread: decode_failures 3

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.840 | 0.804 | 0.035 | - | - | 0.674 | 0.934 | 0.089 | 1.30x | 16.0/24.6/27.7% | 1.8/4.8% | 3 |
| routers | 1 | 0.821 | 0.818 | 0.003 | - | - | 0.879 | 0.879 | 0.087 | 1.30x | 15.9/24.5/28.0% | 1.8/4.9% | 3 |
| alternate-routers | 1 | 0.820 | 0.815 | 0.005 | - | - | 0.893 | 0.895 | 0.100 | 1.31x | 16.0/24.7/28.1% | 1.8/5.0% | 3 |
| beside-router | 1 | 0.810 | 0.807 | 0.004 | - | - | 0.879 | 0.879 | 0.100 | 1.31x | 15.9/24.7/28.2% | 1.8/4.9% | 3 |
| random-clients | 1 | 0.819 | 0.804 | 0.015 | - | - | 0.939 | 0.942 | 0.099 | 1.33x | 16.4/24.5/28.0% | 1.9/4.9% | 3 |
| hops-apart | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

> place=spread: decode_failures 3

> faster: 1.25 s per simulated hour against 2.79 over 41 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| broadcast | 1 | 0.829 | 0.802 | 0.026 | - | - | 0.886 | 0.888 | 0.135 | 1.36x | 16.4/25.4/29.1% | 1.9/5.1% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| heard | 1 | 0.820 | 0.814 | 0.006 | - | - | 0.887 | 0.890 | 0.153 | 1.30x | 15.9/24.7/28.1% | 1.8/4.9% | 3 |

> replay-ordering=heard: misdecodes 23

> faster: 0.785 s per simulated hour against 1.69 over 41 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.829 | 0.802 | 0.026 | - | - | 0.886 | 0.888 | 0.135 | 1.36x | 16.4/25.4/29.1% | 1.9/5.1% | 3 |
| heard | 1 | 0.822 | 0.802 | 0.020 | - | - | 0.879 | 0.880 | 0.143 | 1.35x | 16.3/25.3/28.9% | 1.9/5.1% | 3 |

> replay-ordering=heard: misdecodes 13

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| enum | 1 | 0.817 | 0.809 | 0.008 | - | - | 0.886 | 0.888 | 0.137 | 1.29x | 15.8/24.2/27.8% | 1.8/4.8% | 3 |
| hybrid | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.821 | 0.818 | 0.003 | - | - | 0.879 | 0.879 | 0.087 | 1.30x | 15.9/24.5/28.0% | 1.8/4.9% | 3 |
| 6 | 1 | 0.817 | 0.809 | 0.008 | - | - | 0.890 | 0.891 | 0.092 | 1.33x | 16.3/25.5/29.0% | 1.9/5.2% | 6 |

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.818 | 0.815 | 0.003 | - | - | 0.871 | 0.871 | 0.105 | 1.28x | 15.7/24.2/27.6% | 1.8/4.8% | 2 |
| 3 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 5 | 1 | 0.814 | 0.807 | 0.007 | - | - | 0.880 | 0.881 | 0.140 | 1.33x | 16.1/25.0/28.4% | 1.9/5.0% | 5 |
| 8 | 1 | 0.834 | 0.806 | 0.027 | - | - | 0.918 | 0.920 | 0.184 | 1.37x | 16.5/25.8/29.4% | 1.9/5.2% | 8 |

> faster: 1.1 s per simulated hour against 2.54 over 41 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.818 | 0.815 | 0.003 | - | - | 0.871 | 0.871 | 0.105 | 1.28x | 15.7/24.2/27.6% | 1.8/4.8% | 2 |
| 3 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 5 | 1 | 0.814 | 0.807 | 0.007 | - | - | 0.880 | 0.881 | 0.140 | 1.33x | 16.1/25.0/28.4% | 1.9/5.0% | 5 |
| 8 | 1 | 0.834 | 0.806 | 0.027 | - | - | 0.918 | 0.920 | 0.184 | 1.37x | 16.5/25.8/29.4% | 1.9/5.2% | 8 |

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| True | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.843 | 0.835 | 0.008 | - | - | 0.913 | 0.913 | 0.114 | 1.20x | 14.6/22.7/26.1% | 1.7/4.5% | 3 |
| 1 | 1 | 0.832 | 0.823 | 0.009 | - | - | 0.899 | 0.899 | 0.146 | 1.22x | 14.9/22.9/26.3% | 1.7/4.6% | 3 |
| 2 | 1 | 0.830 | 0.821 | 0.009 | - | - | 0.902 | 0.902 | 0.118 | 1.23x | 15.2/23.3/26.6% | 1.7/4.6% | 3 |
| 4 | 1 | 0.840 | 0.833 | 0.007 | - | - | 0.909 | 0.909 | 0.128 | 1.24x | 15.2/23.2/26.5% | 1.8/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.820 | 0.815 | 0.005 | - | - | 0.887 | 0.887 | 0.153 | 1.30x | 15.8/24.2/27.8% | 1.8/4.9% | 3 |
| 24 | 1 | 0.813 | 0.806 | 0.007 | - | - | 0.881 | 0.882 | 0.127 | 1.31x | 16.1/24.6/28.2% | 1.9/4.9% | 3 |
| 32 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.892 | 0.893 | 0.128 | 1.31x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |
| 64 | 1 | 0.811 | 0.804 | 0.007 | - | - | 0.876 | 0.878 | 0.124 | 1.32x | 16.1/24.8/28.3% | 1.9/4.9% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.809 | 0.802 | 0.007 | - | - | 0.881 | 0.881 | 0.126 | 1.39x | 16.7/25.9/29.7% | 1.9/5.2% | 3 |
| 16 | 1 | 0.813 | 0.805 | 0.007 | - | - | 0.888 | 0.888 | 0.147 | 1.33x | 16.3/25.2/28.7% | 1.9/5.0% | 3 |
| 32 | 1 | 0.818 | 0.811 | 0.007 | - | - | 0.895 | 0.896 | 0.135 | 1.31x | 16.0/24.6/28.1% | 1.9/4.9% | 3 |

> window-size=8: misdecodes 139

> window-size=16: misdecodes 54

> window-size=32: misdecodes 26

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.998 | 0.998 | 0.748 | 2.08x | 24.0/32.4/38.3% | 1.3/5.2% | 3 |
| True | 1 | 0.746 | 0.740 | 0.007 | - | - | 0.841 | 0.907 | 0.526 | 5.88x | 60.3/72.2/77.0% | 4.2/13.7% | 3 |

> no-congestion-scaling=True: queue drops 13.4% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 106

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.529 | 0.518 | 0.012 | - | - | 0.733 | 0.745 | 0.000 | 4.79x | 16.4/33.3/45.7% | 1.6/5.8% | 3 |
| truesize | 1 | 0.572 | 0.559 | 0.012 | - | - | 0.808 | 0.810 | 0.000 | 3.50x | 11.9/26.3/36.3% | 1.1/4.9% | 3 |

> congestion-input=hotstore: decode_failures 51

> congestion-input=truesize: decode_failures 3

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.959 | 0.958 | 0.001 | - | - | 0.999 | 0.999 | 0.774 | 1.99x | 22.8/30.4/36.0% | 1.3/4.9% | 3 |
| adaptive | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.998 | 0.998 | 0.748 | 2.08x | 24.0/32.4/38.3% | 1.3/5.2% | 3 |

> congestion-mode=static: misdecodes 1

