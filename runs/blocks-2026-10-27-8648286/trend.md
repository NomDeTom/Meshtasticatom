# Sweep blocks-2026-10-27-8648286

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 8648286 · seeds 8648286
- **blocks** 87 run
- **compute** 11.4 h of simulator time across every cell
- **generated** 2026-10-27T09:30:48+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>104 warnings</summary>

- AD-amplifiers: amplifier-mix=arms-race: misdecodes 1
- AD-siting: siting-mix=basement-heavy: decode_failures 5
- AD-worst: role-placement=inverse: decode_failures 99
- AD-worst: slower: 17.5 s per simulated hour against 3.41 over 67 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 6
- DB-hotstore-stress: max-num-nodes=10: decode_failures 61
- DB-hotstore-stress: max-num-nodes=120: decode_failures 16
- DB-hotstore-stress: max-num-nodes=250: decode_failures 9
- DB-platform: platform-mix=constrained: decode_failures 4
- DB-warm: warm-num-nodes=0: decode_failures 116
- DB-warm: warm-num-nodes=25: decode_failures 116
- DB-warm: warm-num-nodes=100: decode_failures 116
- DB-warm: warm-num-nodes=2000: decode_failures 116
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 25
- DG-burst: burst-loss=0.3: decode_failures 29
- DG-loss: extra-loss=0.2: decode_failures 35
- DG-loss: extra-loss=0.3: decode_failures 16
- DG-loss: slower: 5.31 s per simulated hour against 2.22 over 67 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.1: decode_failures 45
- DG-outage: burst-loss=0.2: decode_failures 30
- DG-outage: burst-loss=0.3: decode_failures 34
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 1
- DM-mode: dm-mode=m4-early-flood: decode_failures 11
- LD-chatty-hops: broadcast-interval-s=3600: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 42
- LD-chatty: broadcast-interval-s=300: decode_failures 30
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 1
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 116
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 15.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 100
- MS-hopscale: nodes=250: decode_failures 21
- MS-oversubscribed: nodes=250: decode_failures 16
- MS-size: nodes=90: decode_failures 66
- MS-size: nodes=150: decode_failures 3
- MS-stretch: stretch=1.25: decode_failures 3
- MS-stretch: stretch=1.5: decode_failures 28
- MS-stretch: stretch=2.0: decode_failures 3
- MS-stretch: slower: 4.26 s per simulated hour against 2.04 over 67 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-topology: topology=clustered: decode_failures 30
- MS-topology: slower: 4.2 s per simulated hour against 1.9 over 67 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-crladder: coding-rate-ladder=False: decode_failures 1
- PR-crladder: coding-rate-ladder=True: decode_failures 2
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 2
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 10
- RF-noise: noise-profile=temporal: decode_failures 2
- RF-noise: noise-profile=periodic: decode_failures 15
- RF-preset: preset=LONG_MODERATE: decode_failures 2
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 10
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 15
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 8
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 28
- RF-stretch-duct: slower: 5.74 s per simulated hour against 1.81 over 67 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 17
- RF-txpower: tx-power=17: decode_failures 5
- RF-txpower: tx-power=14: decode_failures 12
- RF-txpower: slower: 3.23 s per simulated hour against 1.57 over 67 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 7
- SC-signing: signature-policy=STRICT: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 40
- SF-bucket-mode: bucket-mode=time: misdecodes 20
- SF-bucket-mode: bucket-mode=window: misdecodes 22
- SF-bucket-time: time-bucket-s=600: misdecodes 99
- SF-bucket-time: time-bucket-s=1800: misdecodes 20
- SF-bucket-time: time-bucket-s=3600: misdecodes 6
- SF-bucket-time: time-bucket-s=3600: decode_failures 4
- SF-cadence: trigger=interval: misdecodes 12
- SF-cadence: trigger=interval: decode_failures 2
- SF-cadence: trigger=aimd: decode_failures 13
- SF-cadence: trigger=bucket+interval: misdecodes 10
- SF-capacity-local: capacity=4: decode_failures 102
- SF-capacity-local: capacity=8: decode_failures 65
- SF-capacity-local: capacity=16: decode_failures 67
- SF-capacity: capacity=4: decode_failures 102
- SF-capacity: capacity=8: decode_failures 65
- SF-capacity: capacity=16: decode_failures 67
- SF-capacity-window: capacity=8: misdecodes 9
- SF-capacity-window: capacity=8: decode_failures 95
- SF-capacity-window: capacity=16: misdecodes 18
- SF-capacity-window: capacity=16: decode_failures 13
- SF-capacity-window: capacity=32: misdecodes 22
- SF-catchup: catch-up-hours=: misdecodes 10
- SF-catchup: catch-up-hours=02-06: misdecodes 1
- SF-catchup: catch-up-hours=02-06: decode_failures 49
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 47
- SF-hops-flat: hops-apart=4: decode_failures 38
- SF-hops-spread: hops-apart=4: decode_failures 38
- SF-hops-spread: hops-apart=5: decode_failures 37
- SF-place-flat: place=spread: decode_failures 18
- SF-place-flat: place=random-clients: decode_failures 3
- SF-place-spread: place=spread: decode_failures 18
- SF-place-spread: place=random-clients: decode_failures 3
- SF-provide-transport: provide-transport=broadcast: decode_failures 5
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 5
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 6
- SF-replay-order: replay-ordering=heard: misdecodes 7
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-window-size: window-size=8: misdecodes 118
- SF-window-size: window-size=16: misdecodes 61
- SF-window-size: window-size=32: misdecodes 22
- TH-congestion-input: congestion-input=hotstore: decode_failures 16
- TH-congestion: no-congestion-scaling=True: decode_failures 108

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 17.5 | 3.41 | 5.14x | 67 |
| `RF-stretch-duct` | 5.74 | 1.81 | 3.16x | 67 |
| `DG-loss` | 5.31 | 2.22 | 2.39x | 67 |
| `MS-topology` | 4.2 | 1.9 | 2.22x | 67 |
| `MS-stretch` | 4.26 | 2.04 | 2.09x | 67 |
| `RF-txpower` | 3.23 | 1.57 | 2.06x | 67 |
| `SF-provide-transport` | 3.25 | 1.75 | 1.86x | 67 |
| `LD-chatty-hops` | 7.07 | 3.85 | 1.84x | 67 |
| `SF-replay-order-broadcast` | 3.01 | 1.68 | 1.79x | 67 |
| `SF-capacity-local` | 2.94 | 1.72 | 1.70x | 67 |
| `SF-capacity-window` | 2.45 | 1.59 | 1.54x | 67 |
| `AD-badrouters` | 1.21 | 1.86 | 0.65x | 67 |
| `SF-resolve` | 0.98 | 1.53 | 0.64x | 67 |
| `RT-spread` | 1.32 | 2.16 | 0.61x | 67 |
| `RT-hopspread` | 1.1 | 2.03 | 0.54x | 67 |
| `MS-hopscale` | 9.35 | 17.6 | 0.53x | 67 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.989 | 0.989 | 0.804 → 0.813 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.983 | 0.983 | 0.800 → 0.813 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.131 → 0.974 | 0.843 | 0.129 → 0.973 | 7.2x sr_airtime | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.137 → 0.927 | 0.790 | 0.108 → 0.751 | 1e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.101 → 0.825 | 0.725 | 0.099 → 0.813 | 4.8x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.271 → 0.983 | 0.712 | 0.116 → 0.813 | 4.6x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.201 → 0.911 | 0.709 | 0.093 → 0.744 | 4.6x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.215 → 0.825 | 0.610 | 0.208 → 0.813 | 1.8x sr_bytes | down | 4 |
| `MS-hopscale` | nodes | **held** | 0.403 → 0.983 | 0.580 | 0.317 → 0.813 | 7.8x bytes_on_air | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.330 → 0.825 | 0.496 | 0.324 → 0.813 | 2.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.330 → 0.825 | 0.496 | 0.324 → 0.813 | 2.8x sr_airtime | up | 3 |
| `RF-bw500` | preset | **text** | 0.242 → 0.727 | 0.485 | 0.239 → 0.715 | 1.8x sr_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.550 → 0.983 | 0.433 | 0.804 → 0.813 | 2.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.550 → 0.983 | 0.433 | 0.804 → 0.813 | 2.6x sr_bytes | up | 6 |
| `MS-oversubscribed` | nodes | **held** | 0.406 → 0.821 | 0.415 | 0.318 → 0.693 | 4.6x bytes_on_air | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.547 → 0.912 | 0.365 | 0.532 → 0.909 | 11x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.406 → 0.733 | 0.327 | 0.393 → 0.706 | 1.8x sr_bytes | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.536 → 0.851 | 0.315 | 0.523 → 0.844 | 11x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.512 → 0.825 | 0.313 | 0.488 → 0.813 | 1.9x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.532 → 0.825 | 0.293 | 0.492 → 0.813 | 1.8x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.658 → 0.939 | 0.281 | 0.647 → 0.938 | 2.5x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.539 → 0.799 | 0.259 | 0.315 → 0.504 | 5.2x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.676 → 0.915 | 0.239 | 0.634 → 0.912 | 2.3x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.676 → 0.879 | 0.203 | 0.634 → 0.872 | 1.9x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.745 → 0.947 | 0.202 | 0.739 → 0.945 | 4.6x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.675 → 0.865 | 0.190 | 0.655 → 0.851 | 5.2x sr_bytes | down | 5 |
| `MS-density` | nodes | **text** | 0.763 → 0.947 | 0.184 | 0.743 → 0.945 | 4.1x advert_bytes | up | 5 |
| `RF-noise` | noise-profile | **held** | 0.807 → 0.983 | 0.176 | 0.652 → 0.813 | 1.3x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.676 → 0.825 | 0.149 | 0.634 → 0.813 | 1.5x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.685 → 0.825 | 0.141 | 0.665 → 0.813 | 1.4x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.686 → 0.825 | 0.139 | 0.686 → 0.813 | 1.2x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.752 → 0.884 | 0.132 | 0.744 → 0.875 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.752 → 0.884 | 0.132 | 0.744 → 0.875 | 2.2x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.768 → 0.877 | 0.108 | 0.750 → 0.870 | 5.6x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.880 → 0.983 | 0.102 | 0.813 → 0.814 | 21x sr_airtime | down | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.891 → 0.989 | 0.098 | 0.798 → 0.813 | 3.9x sr_bytes | down | 5 |
| `RF-duct` | duct-per-hour | **text** | 0.825 → 0.919 | 0.094 | 0.813 → 0.912 | 1.4x bytes_on_air | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.825 → 0.915 | 0.090 | 0.813 → 0.914 | 1.9x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.784 → 0.871 | 0.087 | 0.762 → 0.861 | 2.3x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.785 → 0.871 | 0.086 | 0.761 → 0.861 | 2.2x sr_airtime | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.823 → 0.904 | 0.082 | 0.809 → 0.900 | 1.7x sr_bytes | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.649 → 0.727 | 0.079 | 0.645 → 0.722 | 1.5x sr_airtime | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.910 → 0.989 | 0.078 | 0.798 → 0.813 | 2.6x sr_bytes | down | 4 |
| `SF-cadence` | trigger | **held** | 0.907 → 0.983 | 0.076 | 0.777 → 0.813 | 13x advert_bytes | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.912 → 0.974 | 0.062 | 0.799 → 0.810 | 2.3x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.911 → 0.969 | 0.058 | 0.700 → 0.744 | 1.7x sr_bytes | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.825 → 0.880 | 0.055 | 0.813 → 0.871 | 2.1x bytes_on_air | up | 4 |
| `FW-versions` | profile | **text** | 0.825 → 0.880 | 0.055 | 0.813 → 0.872 | 3.5x bytes_on_air | down | 5 |
| `MS-roles` | role-mix | **text** | 0.752 → 0.805 | 0.053 | 0.744 → 0.789 | 1.3x sr_bytes | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.825 → 0.877 | 0.052 | 0.813 → 0.872 | 2.2x bytes_on_air | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.773 → 0.825 | 0.052 | 0.753 → 0.813 | 1.5x sr_airtime | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.935 → 0.983 | 0.047 | 0.791 → 0.813 | 1.1x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.825 → 0.866 | 0.041 | 0.813 → 0.858 | 3.3x bytes_on_air | down | 2 |
| `FW-firmware` | profile | **text** | 0.825 → 0.865 | 0.040 | 0.813 → 0.856 | 3.2x bytes_on_air | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.773 → 0.812 | 0.039 | 0.765 → 0.794 | 1.4x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.820 → 0.854 | 0.033 | 0.805 → 0.844 | 1.3x bytes_on_air | up | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.933 → 0.966 | 0.033 | 0.777 → 0.808 | 9.2x advert_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.825 → 0.856 | 0.031 | 0.802 → 0.813 | 3x sr_airtime | up | 2 |
| `SF-servers-flat` | servers | **held** | 0.965 → 0.994 | 0.030 | 0.799 → 0.813 | 8.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.965 → 0.994 | 0.030 | 0.799 → 0.813 | 8.4x sr_bytes | up | 4 |
| `TH-congestion-input` | congestion-input | **text** | 0.508 → 0.537 | 0.029 | 0.499 → 0.529 | 1.4x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.790 → 0.819 | 0.028 | 0.775 → 0.811 | 1.8x sr_bytes | down | 2 |
| `DM-mode` | dm-mode | **text** | 0.760 → 0.782 | 0.022 | 0.760 → 0.782 | 1.2x sr_airtime | up | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.823 → 0.842 | 0.019 | 0.812 → 0.831 | 1.2x sr_bytes | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.825 → 0.843 | 0.017 | 0.813 → 0.831 | 1.3x sr_bytes | down | 3 |
| `SF-servers-allrouters` | servers | **held** | 0.962 → 0.979 | 0.017 | 0.808 → 0.811 | 2.1x sr_airtime | up | 2 |
| `SF-capacity` | capacity | **held** | 0.968 → 0.983 | 0.014 | 0.800 → 0.813 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.968 → 0.983 | 0.014 | 0.800 → 0.813 | 5.3x advert_bytes | up | 5 |
| `SF-width` | short-id-bits | **held** | 0.972 → 0.983 | 0.011 | 0.803 → 0.816 | 3.2x advert_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.840 → 0.850 | 0.011 | 0.826 → 0.837 | 1.1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.958 → 0.967 | 0.009 | 0.776 → 0.778 | 1.2x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **held** | 0.973 → 0.983 | 0.009 | 0.806 → 0.813 | 5.8x advert_bytes | = | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.815 → 0.824 | 0.009 | 0.802 → 0.812 | 5.3x advert_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.817 → 0.825 | 0.009 | 0.801 → 0.813 | 2.5x advert_bytes | up | 4 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.947 → 0.954 | 0.007 | 0.945 → 0.953 | 1.1x bytes_on_air | down | 2 |
| `SF-window-size` | window-size | **held** | 0.974 → 0.980 | 0.006 | 0.805 → 0.808 | 4.3x advert_bytes | down | 3 |
| `SF-replay-order` | replay-ordering | **text** | 0.820 → 0.825 | 0.005 | 0.805 → 0.813 | 1x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.820 → 0.825 | 0.005 | 0.806 → 0.813 | 2.2x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.966 → 0.970 | 0.004 | 0.797 → 0.802 | 1.1x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.979 → 0.983 | 0.004 | 0.812 → 0.814 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.979 → 0.983 | 0.004 | 0.812 → 0.814 | 1.1x sr_airtime | up | 4 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.776 → 0.779 | 0.003 | 0.776 → 0.779 | 1x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.944 → 0.947 | 0.003 | 0.942 → 0.945 | 1.2x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.825 → 0.827 | 0.002 | 0.813 → 0.813 | 1x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.947 → 0.948 | 0.001 | 0.945 → 0.947 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| sprinkled | 1 | 0.899 | 0.899 | 0.001 | - | - | 0.974 | 0.974 | 0.400 | 1.21x | 17.4/25.8/28.8% | 1.7/5.4% | 3 |
| arms-race | 1 | 0.915 | 0.914 | 0.001 | - | - | 0.972 | 0.972 | 0.413 | 1.16x | 18.7/25.4/28.6% | 1.5/5.3% | 3 |

> amplifier-mix=arms-race: misdecodes 1

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.1 | 1 | 0.823 | 0.809 | 0.014 | - | - | 0.987 | 0.988 | 0.000 | 1.30x | 15.6/26.0/30.0% | 1.9/5.4% | 3 |
| 0.3 | 1 | 0.904 | 0.900 | 0.005 | - | - | 0.997 | 0.998 | 0.408 | 1.14x | 19.7/27.1/30.0% | 1.5/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.752 | 0.744 | 0.008 | - | - | 0.911 | 0.913 | 0.000 | 1.17x | 14.1/26.4/30.2% | 2.0/5.3% | 3 |
| inverse | 1 | 0.733 | 0.700 | 0.033 | - | - | 0.927 | 0.930 | 0.000 | 1.16x | 12.8/18.7/22.1% | 2.2/3.7% | 3 |
| random | 1 | 0.753 | 0.728 | 0.025 | - | - | 0.969 | 0.969 | 0.000 | 1.16x | 14.4/19.5/22.6% | 2.0/4.6% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.752 | 0.744 | 0.008 | - | - | 0.911 | 0.913 | 0.000 | 1.17x | 14.1/26.4/30.2% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.884 | 0.875 | 0.008 | - | - | 0.995 | 0.996 | 0.000 | 2.56x | 26.9/40.1/43.7% | 4.2/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.752 | 0.744 | 0.008 | - | - | 0.911 | 0.913 | 0.000 | 1.17x | 14.1/26.4/30.2% | 2.0/5.3% | 3 |
| no-mute | 1 | 0.806 | 0.795 | 0.010 | - | - | 0.946 | 0.948 | 0.000 | 1.31x | 14.1/23.4/27.5% | 2.1/5.2% | 3 |
| all-routers | 1 | 0.884 | 0.875 | 0.008 | - | - | 0.995 | 0.996 | 0.000 | 2.56x | 26.9/40.1/43.7% | 4.2/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.752 | 0.744 | 0.008 | - | - | 0.911 | 0.913 | 0.000 | 1.17x | 14.1/26.4/30.2% | 2.0/5.3% | 3 |
| local-typical | 1 | 0.694 | 0.677 | 0.017 | - | - | 0.861 | 0.864 | 0.000 | 1.31x | 13.5/24.4/33.5% | 2.3/5.6% | 3 |
| basement-heavy | 1 | 0.096 | 0.093 | 0.003 | - | - | 0.201 | 0.314 | 0.000 | 0.59x | 0.8/8.3/13.5% | 0.2/3.4% | 3 |

> siting-mix=basement-heavy: decode_failures 5

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.819 | 0.811 | 0.008 | - | - | 0.962 | 0.963 | 0.096 | 2.56x | 16.4/28.0/34.5% | 1.9/5.9% | 3 |
| inverse | 1 | 0.790 | 0.775 | 0.015 | - | - | 0.956 | 0.972 | 0.115 | 2.41x | 14.9/24.7/33.4% | 1.9/4.0% | 3 |

> role-placement=inverse: decode_failures 99

> slower: 17.5 s per simulated hour against 3.41 over 67 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.813 | 0.813 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.29x | 14.5/25.0/28.3% | 2.0/4.9% | 3 |
| sr | 1 | 0.825 | 0.804 | 0.021 | - | - | 0.989 | 0.990 | 0.000 | 1.34x | 15.2/25.9/29.3% | 2.1/5.2% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.784 | 0.762 | 0.021 | - | - | 0.925 | 0.943 | 0.000 | 3.03x | 33.7/55.7/61.5% | 4.4/9.4% | 3 |
| 100 | 1 | 0.871 | 0.861 | 0.011 | - | - | 0.972 | 0.973 | 0.000 | 1.57x | 18.0/30.8/34.5% | 2.4/5.1% | 3 |
| 120 | 1 | 0.871 | 0.861 | 0.011 | - | - | 0.972 | 0.973 | 0.000 | 1.57x | 18.0/30.8/34.5% | 2.4/5.1% | 3 |
| 250 | 1 | 0.871 | 0.861 | 0.011 | - | - | 0.972 | 0.973 | 0.000 | 1.57x | 18.0/30.8/34.5% | 2.4/5.1% | 3 |

> max-num-nodes=10: decode_failures 6

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.322 | 0.315 | 0.007 | - | - | 0.539 | 0.652 | 0.141 | 11.51x | 39.9/56.7/67.5% | 4.1/10.5% | 3 |
| 120 | 1 | 0.508 | 0.499 | 0.008 | - | - | 0.793 | 0.794 | 0.222 | 4.50x | 15.8/24.8/33.3% | 1.5/5.5% | 3 |
| 250 | 1 | 0.512 | 0.504 | 0.008 | - | - | 0.799 | 0.801 | 0.221 | 4.37x | 15.3/24.0/31.7% | 1.5/5.3% | 3 |

> max-num-nodes=10: decode_failures 61

> max-num-nodes=120: decode_failures 16

> max-num-nodes=250: decode_failures 9

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.871 | 0.861 | 0.011 | - | - | 0.972 | 0.973 | 0.000 | 1.57x | 18.0/30.8/34.5% | 2.4/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.871 | 0.861 | 0.011 | - | - | 0.972 | 0.973 | 0.000 | 1.57x | 18.0/30.8/34.5% | 2.4/5.1% | 3 |
| constrained | 1 | 0.785 | 0.761 | 0.024 | - | - | 0.936 | 0.944 | 0.000 | 3.03x | 33.7/55.8/61.7% | 4.5/9.4% | 3 |

> platform-mix=constrained: decode_failures 4

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.727 | 0.722 | 0.005 | - | - | 0.841 | 0.913 | 0.388 | 5.87x | 55.6/71.1/77.0% | 4.4/12.1% | 3 |
| 25 | 1 | 0.727 | 0.722 | 0.005 | - | - | 0.841 | 0.913 | 0.388 | 5.87x | 55.6/71.1/77.0% | 4.4/12.1% | 3 |
| 100 | 1 | 0.727 | 0.722 | 0.005 | - | - | 0.841 | 0.913 | 0.388 | 5.87x | 55.6/71.1/77.0% | 4.4/12.1% | 3 |
| 2000 | 1 | 0.727 | 0.722 | 0.005 | - | - | 0.841 | 0.913 | 0.388 | 5.87x | 55.6/71.1/77.0% | 4.4/12.1% | 3 |

> warm-num-nodes=0: decode_failures 116

> warm-num-nodes=25: decode_failures 116

> warm-num-nodes=100: decode_failures 116

> warm-num-nodes=2000: decode_failures 116

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.1 | 1 | 0.729 | 0.702 | 0.027 | - | - | 0.949 | 0.950 | 0.000 | 1.25x | 14.3/24.6/28.1% | 1.9/4.8% | 3 |
| 0.2 | 1 | 0.634 | 0.600 | 0.034 | - | - | 0.875 | 0.925 | 0.000 | 1.17x | 13.6/23.4/27.0% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.532 | 0.492 | 0.040 | - | - | 0.780 | 0.848 | 0.000 | 1.06x | 12.4/21.6/25.5% | 1.5/3.9% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 25

> burst-loss=0.3: decode_failures 29

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.1 | 1 | 0.790 | 0.776 | 0.015 | - | - | 0.971 | 0.975 | 0.000 | 1.39x | 15.7/27.0/30.6% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.744 | 0.727 | 0.018 | - | - | 0.938 | 0.957 | 0.000 | 1.41x | 16.1/27.4/31.6% | 2.1/5.0% | 3 |
| 0.3 | 1 | 0.685 | 0.665 | 0.019 | - | - | 0.893 | 0.926 | 0.000 | 1.39x | 16.0/26.8/31.3% | 2.1/4.7% | 3 |

> extra-loss=0.2: decode_failures 35

> extra-loss=0.3: decode_failures 16

> slower: 5.31 s per simulated hour against 2.22 over 67 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.1 | 1 | 0.728 | 0.710 | 0.018 | - | - | 0.938 | 0.967 | 0.000 | 1.27x | 14.3/25.0/28.5% | 1.9/5.0% | 3 |
| 0.2 | 1 | 0.617 | 0.597 | 0.021 | - | - | 0.824 | 0.929 | 0.000 | 1.18x | 13.6/23.8/27.2% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.512 | 0.488 | 0.024 | - | - | 0.763 | 0.869 | 0.000 | 1.10x | 12.9/21.8/25.7% | 1.7/4.0% | 3 |

> burst-loss=0.1: decode_failures 45

> burst-loss=0.2: decode_failures 30

> burst-loss=0.3: decode_failures 34

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.760 | 0.760 | 0.000 | - | - | 0.953 | 0.957 | 0.000 | 1.78x | 19.4/34.8/39.4% | 2.6/6.9% | 3 |
| directed-with-late-flood | 1 | 0.778 | 0.778 | 0.000 | - | - | 0.958 | 0.971 | 0.000 | 1.65x | 18.2/32.6/36.9% | 2.4/6.4% | 3 |
| m4-early-flood | 1 | 0.782 | 0.782 | 0.000 | - | - | 0.954 | 0.977 | 0.000 | 1.64x | 18.2/32.5/36.7% | 2.5/6.4% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 1

> dm-mode=m4-early-flood: decode_failures 11

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.985 | 0.986 | 0.000 | 0.74x | 8.8/11.7/13.3% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.25 | 1 | 0.876 | 0.871 | 0.006 | - | - | 0.989 | 0.991 | 0.000 | 1.24x | 15.6/22.3/25.8% | 1.9/4.7% | 3 |
| 0.5 | 1 | 0.880 | 0.869 | 0.012 | - | - | 0.983 | 0.984 | 0.347 | 1.08x | 13.0/20.0/22.9% | 1.6/4.3% | 3 |
| 0.75 | 1 | 0.838 | 0.833 | 0.005 | - | - | 0.954 | 0.954 | 0.000 | 0.89x | 11.3/15.2/17.5% | 1.4/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.25 | 1 | 0.877 | 0.872 | 0.005 | - | - | 0.988 | 0.990 | 0.000 | 1.20x | 15.3/21.5/25.5% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.876 | 0.865 | 0.011 | - | - | 0.976 | 0.981 | 0.405 | 1.05x | 12.8/19.7/23.0% | 1.7/4.4% | 3 |
| 0.75 | 1 | 0.848 | 0.843 | 0.004 | - | - | 0.965 | 0.965 | 0.000 | 0.86x | 11.1/15.3/17.8% | 1.4/3.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.866 | 0.858 | 0.008 | - | - | 0.990 | 0.990 | 0.000 | 0.72x | 8.3/15.1/17.0% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.864 | 0.855 | 0.009 | - | - | 0.975 | 0.976 | 0.000 | 0.71x | 9.2/12.5/14.1% | 1.1/2.5% | 3 |
| 2.5 | 1 | 0.872 | 0.865 | 0.007 | - | - | 0.980 | 0.980 | 0.000 | 0.73x | 9.1/12.6/14.1% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.874 | 0.864 | 0.010 | - | - | 0.988 | 0.988 | 0.000 | 0.69x | 9.1/12.5/14.1% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.880 | 0.872 | 0.008 | - | - | 0.984 | 0.984 | 0.000 | 0.73x | 10.2/14.6/16.5% | 1.0/3.1% | 3 |
| 2.8 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.851 | 0.844 | 0.008 | - | - | 0.985 | 0.986 | 0.000 | 0.90x | 9.9/17.9/20.1% | 1.3/3.6% | 3 |
| 900 | 1 | 0.768 | 0.750 | 0.019 | - | - | 0.953 | 0.957 | 0.000 | 2.13x | 23.9/40.9/45.9% | 3.2/8.1% | 3 |
| 300 | 1 | 0.536 | 0.523 | 0.013 | - | - | 0.758 | 0.892 | 0.000 | 4.60x | 47.0/71.2/79.3% | 7.2/15.2% | 3 |

> broadcast-interval-s=300: decode_failures 30

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.912 | 0.909 | 0.003 | - | - | 0.996 | 0.996 | 0.000 | 1.03x | 11.5/18.6/21.1% | 1.7/3.6% | 3 |
| 900 | 1 | 0.846 | 0.833 | 0.013 | - | - | 0.970 | 0.975 | 0.000 | 2.40x | 26.5/42.7/48.3% | 3.9/8.3% | 3 |
| 300 | 1 | 0.547 | 0.532 | 0.016 | - | - | 0.736 | 0.847 | 0.000 | 5.09x | 50.8/72.0/80.5% | 7.9/16.2% | 3 |

> broadcast-interval-s=3600: misdecodes 1

> broadcast-interval-s=300: decode_failures 42

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.843 | 0.831 | 0.011 | - | - | 0.983 | 0.984 | 0.000 | 1.26x | 14.0/24.7/27.7% | 1.9/5.0% | 3 |
| sinusoid | 1 | 0.833 | 0.820 | 0.013 | - | - | 0.972 | 0.976 | 0.000 | 1.23x | 13.6/23.9/27.0% | 1.9/4.7% | 3 |
| commuter | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.768 | 0.750 | 0.019 | - | - | 0.953 | 0.957 | 0.000 | 2.13x | 23.9/40.9/45.9% | 3.2/8.1% | 3 |
| 3600 | 1 | 0.851 | 0.844 | 0.008 | - | - | 0.985 | 0.986 | 0.000 | 0.90x | 9.9/17.9/20.1% | 1.3/3.6% | 3 |
| 10800 | 1 | 0.866 | 0.859 | 0.006 | - | - | 0.986 | 0.989 | 0.000 | 0.62x | 6.9/12.2/13.6% | 1.0/2.5% | 3 |
| 43200 | 1 | 0.877 | 0.870 | 0.007 | - | - | 0.992 | 0.996 | 0.000 | 0.45x | 5.0/9.1/10.2% | 0.7/1.9% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.25 | 1 | 0.819 | 0.806 | 0.014 | - | - | 0.983 | 0.983 | 0.000 | 1.42x | 15.7/27.7/31.2% | 2.2/5.5% | 3 |
| 1.0 | 1 | 0.803 | 0.789 | 0.014 | - | - | 0.977 | 0.977 | 0.000 | 1.54x | 17.2/30.4/34.4% | 2.3/6.0% | 3 |
| 4.0 | 1 | 0.773 | 0.753 | 0.021 | - | - | 0.961 | 0.963 | 0.000 | 1.90x | 21.6/38.2/42.8% | 2.8/7.4% | 3 |

> traceroute-per-hour=4.0: decode_failures 1

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.722 | 0.005 | - | - | 0.841 | 0.913 | 0.388 | 5.87x | 55.6/71.1/77.0% | 4.4/12.1% | 3 |
| 1.0 | 1 | 0.649 | 0.645 | 0.004 | - | - | 0.769 | 0.880 | 0.321 | 6.40x | 59.3/73.5/78.9% | 4.8/13.3% | 3 |

> traceroute-per-hour=0.0: decode_failures 116

> traceroute-per-hour=1.0: queue drops 15.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 100

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.763 | 0.743 | 0.021 | - | - | 0.916 | 0.921 | 0.390 | 1.46x | 19.4/26.6/28.8% | 3.4/7.2% | 3 |
| 60 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 90 | 1 | 0.913 | 0.912 | 0.002 | - | - | 0.990 | 0.990 | 0.687 | 1.58x | 16.9/25.5/30.9% | 1.5/4.9% | 3 |
| 120 | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.991 | 0.992 | 0.655 | 2.07x | 21.6/31.5/35.6% | 1.5/5.1% | 3 |
| 150 | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.994 | 0.994 | 0.685 | 2.52x | 23.3/36.4/43.2% | 1.3/5.4% | 3 |

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 120 | 1 | 0.707 | 0.696 | 0.011 | - | - | 0.829 | 0.832 | 0.165 | 2.18x | 15.0/24.2/31.7% | 1.5/5.2% | 3 |
| 250 | 1 | 0.508 | 0.499 | 0.009 | - | - | 0.793 | 0.795 | 0.216 | 4.79x | 16.9/26.2/35.6% | 1.6/6.0% | 3 |
| 500 | 1 | 0.319 | 0.317 | 0.002 | - | - | 0.403 | 0.403 | 0.110 | 10.12x | 18.5/30.7/42.0% | 1.7/5.8% | 3 |

> nodes=250: decode_failures 21

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.705 | 0.693 | 0.011 | - | - | 0.821 | 0.823 | 0.163 | 2.06x | 14.1/22.7/29.7% | 1.5/4.9% | 3 |
| 250 | 1 | 0.508 | 0.499 | 0.008 | - | - | 0.793 | 0.794 | 0.222 | 4.50x | 15.8/24.8/33.3% | 1.5/5.5% | 3 |
| 500 | 1 | 0.320 | 0.318 | 0.002 | - | - | 0.406 | 0.407 | 0.111 | 9.40x | 17.3/28.5/38.3% | 1.6/5.2% | 3 |

> nodes=250: decode_failures 16

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.805 | 0.789 | 0.017 | - | - | 0.928 | 0.929 | 0.000 | 1.37x | 15.5/26.4/29.7% | 2.1/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.752 | 0.744 | 0.008 | - | - | 0.911 | 0.913 | 0.000 | 1.17x | 14.1/26.4/30.2% | 2.0/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.812 | 0.794 | 0.018 | - | - | 0.933 | 0.934 | 0.000 | 1.41x | 15.9/26.7/30.3% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.773 | 0.765 | 0.007 | - | - | 0.903 | 0.904 | 0.000 | 1.33x | 15.8/29.1/33.5% | 2.3/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.05 | 1 | 0.820 | 0.805 | 0.015 | - | - | 0.966 | 0.967 | 0.000 | 1.45x | 15.6/30.2/34.4% | 2.2/5.1% | 3 |
| 0.1 | 1 | 0.854 | 0.844 | 0.010 | - | - | 0.984 | 0.984 | 0.000 | 1.54x | 17.4/31.7/36.6% | 2.2/5.0% | 3 |
| 0.2 | 1 | 0.843 | 0.832 | 0.011 | - | - | 0.965 | 0.967 | 0.000 | 1.75x | 19.2/39.8/44.0% | 2.3/5.0% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| local-typical | 1 | 0.750 | 0.737 | 0.013 | - | - | 0.902 | 0.902 | 0.000 | 1.50x | 15.5/25.3/34.0% | 2.3/5.5% | 3 |
| event | 1 | 0.131 | 0.129 | 0.002 | - | - | 0.188 | 0.191 | 0.000 | 0.88x | 4.4/8.9/12.6% | 1.4/3.1% | 3 |
| backbone | 1 | 0.974 | 0.973 | 0.001 | - | - | 0.997 | 0.998 | 0.893 | 1.10x | 25.9/30.6/33.3% | 1.1/5.6% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.865 | 0.851 | 0.014 | - | - | 0.972 | 0.973 | 0.586 | 1.45x | 23.8/34.1/38.8% | 3.1/7.6% | 3 |
| 60 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 90 | 1 | 0.799 | 0.790 | 0.009 | - | - | 0.867 | 0.946 | 0.260 | 1.74x | 14.5/23.0/28.7% | 1.6/5.0% | 3 |
| 120 | 1 | 0.707 | 0.696 | 0.011 | - | - | 0.829 | 0.832 | 0.165 | 2.18x | 15.0/24.2/31.7% | 1.5/5.2% | 3 |
| 150 | 1 | 0.675 | 0.655 | 0.020 | - | - | 0.962 | 0.964 | 0.000 | 2.80x | 14.9/25.2/33.7% | 1.6/5.8% | 3 |

> nodes=90: decode_failures 66

> nodes=150: decode_failures 3

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 1.25 | 1 | 0.629 | 0.614 | 0.015 | - | - | 0.931 | 0.939 | 0.000 | 1.34x | 11.6/21.0/26.6% | 1.9/5.1% | 3 |
| 1.5 | 1 | 0.406 | 0.393 | 0.013 | - | - | 0.782 | 0.806 | 0.000 | 1.36x | 10.0/19.5/27.7% | 2.0/5.4% | 3 |
| 2.0 | 1 | 0.215 | 0.208 | 0.007 | - | - | 0.562 | 0.571 | 0.000 | 1.03x | 4.8/13.1/16.5% | 1.4/5.0% | 3 |

> stretch=1.25: decode_failures 3

> stretch=1.5: decode_failures 28

> stretch=2.0: decode_failures 3

> slower: 4.26 s per simulated hour against 2.04 over 67 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| clustered | 1 | 0.829 | 0.823 | 0.006 | - | - | 0.873 | 0.919 | 0.000 | 1.15x | 28.5/37.4/39.7% | 1.5/5.7% | 3 |
| corridor | 1 | 0.658 | 0.647 | 0.011 | - | - | 0.726 | 0.730 | 0.365 | 1.16x | 15.3/18.7/22.3% | 1.5/5.5% | 3 |
| hub | 1 | 0.939 | 0.938 | 0.001 | - | - | 0.974 | 0.975 | 0.599 | 1.25x | 28.1/36.1/37.1% | 1.8/5.6% | 3 |

> topology=clustered: decode_failures 30

> slower: 4.2 s per simulated hour against 1.9 over 67 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.778 | 0.778 | 0.000 | - | - | 0.958 | 0.971 | 0.000 | 1.65x | 18.2/32.6/36.9% | 2.4/6.4% | 3 |
| True | 1 | 0.776 | 0.776 | 0.000 | - | - | 0.967 | 0.982 | 0.000 | 1.66x | 18.3/33.0/37.1% | 2.4/6.5% | 3 |

> coding-rate-ladder=False: decode_failures 1

> coding-rate-ladder=True: decode_failures 2

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.776 | 0.776 | 0.000 | - | - | 0.967 | 0.982 | 0.000 | 1.66x | 18.3/33.0/37.1% | 2.4/6.5% | 3 |
| m4-early-flood | 1 | 0.779 | 0.779 | 0.000 | - | - | 0.967 | 0.980 | 0.000 | 1.65x | 18.3/32.9/36.9% | 2.4/6.5% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 2

> dm-mode=m4-early-flood: decode_failures 1

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.813 | 0.813 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.29x | 14.5/25.0/28.3% | 2.0/4.9% | 3 |
| chain | 1 | 0.804 | 0.800 | 0.003 | - | - | 0.899 | 0.969 | 0.000 | 1.52x | 16.7/30.0/33.6% | 2.3/5.9% | 3 |
| sr | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| True | 1 | 0.827 | 0.813 | 0.014 | - | - | 0.984 | 0.985 | 0.000 | 1.38x | 15.3/26.8/30.1% | 2.1/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.991 | 0.992 | 0.655 | 2.07x | 21.6/31.5/35.6% | 1.5/5.1% | 3 |
| True | 1 | 0.948 | 0.947 | 0.002 | - | - | 0.992 | 0.993 | 0.667 | 2.08x | 21.6/31.6/35.7% | 1.5/5.1% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.242 | 0.239 | 0.002 | - | - | 0.535 | 0.623 | 0.000 | 0.05x | 0.2/0.7/0.9% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.361 | 0.353 | 0.009 | - | - | 0.721 | 0.725 | 0.000 | 0.22x | 1.4/3.9/5.3% | 0.3/1.2% | 3 |
| LONG_TURBO | 1 | 0.727 | 0.715 | 0.012 | - | - | 0.959 | 0.962 | 0.000 | 1.33x | 11.3/21.8/26.5% | 2.0/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 10

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 0.25 | 1 | 0.863 | 0.850 | 0.013 | - | - | 0.983 | 0.983 | 0.251 | 1.24x | 18.1/26.8/30.2% | 1.9/5.3% | 3 |
| 1.0 | 1 | 0.919 | 0.912 | 0.007 | - | - | 0.991 | 0.991 | 0.576 | 0.96x | 20.7/26.4/29.0% | 1.2/5.0% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.330 | 0.324 | 0.005 | - | - | 0.706 | 0.707 | 0.000 | 0.12x | 0.7/2.0/2.7% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| LITE_FAST | 1 | 0.754 | 0.743 | 0.011 | - | - | 0.972 | 0.974 | 0.000 | 1.04x | 9.5/19.5/22.5% | 1.5/4.0% | 3 |
| NARROW_SLOW | 1 | 0.770 | 0.758 | 0.012 | - | - | 0.969 | 0.971 | 0.000 | 1.28x | 13.2/22.1/27.1% | 1.9/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| temporal | 1 | 0.716 | 0.696 | 0.021 | - | - | 0.946 | 0.957 | 0.000 | 1.32x | 14.2/25.4/30.2% | 1.9/5.1% | 3 |
| transient | 1 | 0.812 | 0.796 | 0.015 | - | - | 0.976 | 0.977 | 0.000 | 1.35x | 15.0/26.1/29.4% | 2.0/5.3% | 3 |
| periodic | 1 | 0.664 | 0.652 | 0.012 | - | - | 0.807 | 0.821 | 0.000 | 1.24x | 14.1/24.0/27.3% | 1.8/4.6% | 3 |

> noise-profile=temporal: decode_failures 2

> noise-profile=periodic: decode_failures 15

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.330 | 0.324 | 0.005 | - | - | 0.706 | 0.707 | 0.000 | 0.12x | 0.7/2.0/2.7% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| LONG_MODERATE | 1 | 0.815 | 0.801 | 0.014 | - | - | 0.952 | 0.965 | 0.000 | 3.39x | 44.6/63.3/65.7% | 5.0/11.5% | 3 |

> preset=LONG_MODERATE: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.101 | 0.099 | 0.002 | - | - | 0.378 | 0.379 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.1% | 3 |
| SHORT_TURBO | 1 | 0.242 | 0.239 | 0.002 | - | - | 0.535 | 0.623 | 0.000 | 0.05x | 0.2/0.7/0.9% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| LONG_TURBO | 1 | 0.727 | 0.715 | 0.012 | - | - | 0.959 | 0.962 | 0.000 | 1.33x | 11.3/21.8/26.5% | 2.0/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.815 | 0.799 | 0.016 | - | - | 0.977 | 0.981 | 0.000 | 1.88x | 20.3/32.7/38.3% | 2.8/7.0% | 3 |

> preset=SHORT_TURBO: decode_failures 10

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.765 | 0.751 | 0.014 | - | - | 0.927 | 0.929 | 0.000 | 1.28x | 14.4/25.4/28.6% | 1.9/4.9% | 3 |
| 10000 | 1 | 0.664 | 0.652 | 0.012 | - | - | 0.807 | 0.821 | 0.000 | 1.24x | 14.1/24.0/27.3% | 1.8/4.6% | 3 |
| 4000 | 1 | 0.420 | 0.416 | 0.004 | - | - | 0.520 | 0.604 | 0.000 | 1.04x | 12.0/19.9/23.6% | 1.6/3.4% | 3 |
| 2000 | 1 | 0.108 | 0.108 | 0.000 | - | - | 0.137 | 0.232 | 0.000 | 0.72x | 8.4/14.0/17.6% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 15

> noise-pulse-interval-ms=4000: decode_failures 8

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.406 | 0.393 | 0.013 | - | - | 0.782 | 0.806 | 0.000 | 1.36x | 10.0/19.5/27.7% | 2.0/5.4% | 3 |
| 1.0 | 1 | 0.733 | 0.706 | 0.026 | - | - | 0.929 | 0.929 | 0.118 | 0.97x | 15.3/22.1/26.7% | 1.4/4.6% | 3 |

> duct-per-hour=0.0: decode_failures 28

> slower: 5.74 s per simulated hour against 1.81 over 67 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 22 | 1 | 0.349 | 0.346 | 0.003 | - | - | 0.594 | 0.700 | 0.000 | 1.31x | 8.7/19.6/26.7% | 1.9/5.9% | 3 |
| 17 | 1 | 0.223 | 0.222 | 0.001 | - | - | 0.281 | 0.565 | 0.000 | 1.03x | 4.6/14.1/19.0% | 1.3/5.0% | 3 |
| 14 | 1 | 0.118 | 0.116 | 0.002 | - | - | 0.271 | 0.431 | 0.000 | 0.60x | 1.6/8.4/11.0% | 0.6/3.7% | 3 |

> tx-power=22: decode_failures 17

> tx-power=17: decode_failures 5

> tx-power=14: decode_failures 12

> slower: 3.23 s per simulated hour against 1.57 over 67 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.991 | 0.992 | 0.655 | 2.07x | 21.6/31.5/35.6% | 1.5/5.1% | 3 |
| True | 1 | 0.944 | 0.942 | 0.002 | - | - | 0.993 | 0.993 | 0.627 | 2.44x | 24.9/35.7/39.8% | 1.7/5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.840 | 0.826 | 0.014 | - | - | 0.981 | 0.981 | 0.000 | 1.42x | 15.4/28.9/32.5% | 2.1/5.1% | 3 |
| True | 1 | 0.850 | 0.837 | 0.013 | - | - | 0.971 | 0.973 | 0.000 | 1.51x | 16.2/29.5/33.2% | 2.3/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| random | 1 | 0.808 | 0.791 | 0.017 | - | - | 0.935 | 0.936 | 0.000 | 1.35x | 15.3/26.3/29.4% | 2.1/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.676 | 0.634 | 0.043 | - | - | 0.954 | 0.960 | 0.000 | 1.05x | 11.8/23.1/25.7% | 1.5/4.8% | 3 |
| 7 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.983 | 0.987 | 0.000 | 1.54x | 17.2/28.1/31.6% | 2.5/5.4% | 3 |
| 15 | 1 | 0.915 | 0.912 | 0.004 | - | - | 0.991 | 0.992 | 0.000 | 1.57x | 17.5/27.9/31.7% | 2.6/5.4% | 3 |
| 32 | 1 | 0.914 | 0.910 | 0.005 | - | - | 0.992 | 0.993 | 0.000 | 1.56x | 17.4/28.0/31.7% | 2.6/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.676 | 0.634 | 0.043 | - | - | 0.954 | 0.960 | 0.000 | 1.05x | 11.8/23.1/25.7% | 1.5/4.8% | 3 |
| 5 | 1 | 0.826 | 0.810 | 0.016 | - | - | 0.978 | 0.981 | 0.000 | 1.39x | 15.8/26.8/30.0% | 2.2/5.3% | 3 |
| 7 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.983 | 0.987 | 0.000 | 1.54x | 17.2/28.1/31.6% | 2.5/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.814 | 0.814 | 0.000 | - | - | 0.880 | 0.983 | 0.000 | 1.31x | 14.8/25.3/28.6% | 2.0/5.0% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 7

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.676 | 0.634 | 0.043 | - | - | 0.954 | 0.960 | 0.000 | 1.05x | 11.8/23.1/25.7% | 1.5/4.8% | 3 |
| True | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| BALANCED | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| STRICT | 1 | 0.686 | 0.686 | 0.000 | - | - | 0.872 | 0.873 | 0.000 | 1.46x | 16.2/28.6/32.1% | 2.2/5.6% | 3 |

> signature-policy=STRICT: decode_failures 2

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| dm | 1 | 0.820 | 0.806 | 0.014 | - | - | 0.980 | 0.980 | 0.000 | 1.33x | 14.8/26.3/29.4% | 2.0/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.817 | 0.801 | 0.015 | - | - | 0.978 | 0.983 | 0.000 | 1.35x | 15.1/26.3/29.6% | 2.1/5.2% | 3 |
| local | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| time | 1 | 0.824 | 0.812 | 0.012 | - | - | 0.975 | 0.977 | 0.000 | 1.36x | 15.1/26.6/29.8% | 2.1/5.3% | 3 |
| window | 1 | 0.819 | 0.805 | 0.014 | - | - | 0.974 | 0.977 | 0.000 | 1.33x | 14.8/25.9/29.1% | 2.1/5.2% | 3 |

> bucket-mode=global: misdecodes 40

> bucket-mode=time: misdecodes 20

> bucket-mode=window: misdecodes 22

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.816 | 0.803 | 0.013 | - | - | 0.974 | 0.977 | 0.000 | 1.48x | 16.1/29.2/32.6% | 2.2/5.8% | 3 |
| 1800 | 1 | 0.824 | 0.812 | 0.012 | - | - | 0.975 | 0.977 | 0.000 | 1.36x | 15.1/26.6/29.8% | 2.1/5.3% | 3 |
| 3600 | 1 | 0.815 | 0.802 | 0.013 | - | - | 0.974 | 0.979 | 0.000 | 1.35x | 15.1/26.4/29.6% | 2.1/5.2% | 3 |

> time-bucket-s=600: misdecodes 99

> time-bucket-s=1800: misdecodes 20

> time-bucket-s=3600: misdecodes 6

> time-bucket-s=3600: decode_failures 4

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| interval | 1 | 0.802 | 0.787 | 0.015 | - | - | 0.959 | 0.973 | 0.000 | 1.76x | 18.9/36.2/39.6% | 2.5/7.5% | 3 |
| aimd | 1 | 0.810 | 0.805 | 0.005 | - | - | 0.907 | 0.983 | 0.000 | 1.35x | 15.1/26.4/29.6% | 2.1/5.2% | 3 |
| bucket+interval | 1 | 0.797 | 0.777 | 0.020 | - | - | 0.966 | 0.970 | 0.000 | 1.80x | 19.2/37.0/40.5% | 2.6/7.7% | 3 |

> trigger=interval: misdecodes 12

> trigger=interval: decode_failures 2

> trigger=aimd: decode_failures 13

> trigger=bucket+interval: misdecodes 10

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.820 | 0.805 | 0.015 | - | - | 0.975 | 0.983 | 0.000 | 1.33x | 14.8/26.4/29.7% | 2.0/5.3% | 3 |
| 8 | 1 | 0.815 | 0.800 | 0.015 | - | - | 0.968 | 0.972 | 0.000 | 1.35x | 15.0/26.7/29.9% | 2.0/5.3% | 3 |
| 16 | 1 | 0.820 | 0.806 | 0.014 | - | - | 0.974 | 0.981 | 0.000 | 1.34x | 15.0/26.5/29.7% | 2.0/5.3% | 3 |
| 32 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 50 | 1 | 0.815 | 0.801 | 0.014 | - | - | 0.982 | 0.983 | 0.000 | 1.33x | 14.9/26.1/29.3% | 2.1/5.2% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 65

> capacity=16: decode_failures 67

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.820 | 0.805 | 0.015 | - | - | 0.975 | 0.983 | 0.000 | 1.33x | 14.8/26.4/29.7% | 2.0/5.3% | 3 |
| 8 | 1 | 0.815 | 0.800 | 0.015 | - | - | 0.968 | 0.972 | 0.000 | 1.35x | 15.0/26.7/29.9% | 2.0/5.3% | 3 |
| 16 | 1 | 0.820 | 0.806 | 0.014 | - | - | 0.974 | 0.981 | 0.000 | 1.34x | 15.0/26.5/29.7% | 2.0/5.3% | 3 |
| 32 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 50 | 1 | 0.815 | 0.801 | 0.014 | - | - | 0.982 | 0.983 | 0.000 | 1.33x | 14.9/26.1/29.3% | 2.1/5.2% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 65

> capacity=16: decode_failures 67

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.807 | 0.799 | 0.008 | - | - | 0.912 | 0.983 | 0.000 | 1.33x | 15.0/25.9/29.2% | 2.1/5.1% | 3 |
| 16 | 1 | 0.823 | 0.810 | 0.013 | - | - | 0.968 | 0.983 | 0.000 | 1.34x | 15.0/26.1/29.4% | 2.1/5.2% | 3 |
| 32 | 1 | 0.819 | 0.805 | 0.014 | - | - | 0.974 | 0.977 | 0.000 | 1.33x | 14.8/25.9/29.1% | 2.1/5.2% | 3 |

> capacity=8: misdecodes 9

> capacity=8: decode_failures 95

> capacity=16: misdecodes 18

> capacity=16: decode_failures 13

> capacity=32: misdecodes 22

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.797 | 0.777 | 0.020 | - | - | 0.966 | 0.970 | 0.000 | 1.80x | 19.2/37.0/40.5% | 2.6/7.7% | 3 |
| 02-06 | 1 | 0.812 | 0.803 | 0.009 | - | - | 0.933 | 0.977 | 0.000 | 1.37x | 15.2/27.1/30.3% | 2.1/5.4% | 3 |
| 00-08 | 1 | 0.817 | 0.808 | 0.010 | - | - | 0.940 | 0.981 | 0.000 | 1.43x | 15.7/28.5/31.7% | 2.2/5.9% | 3 |

> catch-up-hours=: misdecodes 10

> catch-up-hours=02-06: misdecodes 1

> catch-up-hours=02-06: decode_failures 49

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 47

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.805 | 0.804 | 0.002 | - | - | 0.961 | 0.962 | 0.000 | 1.34x | 15.0/25.9/29.3% | 2.1/5.2% | 3 |
| 2 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 3 | 1 | 0.825 | 0.804 | 0.021 | - | - | 0.989 | 0.990 | 0.000 | 1.34x | 15.2/25.9/29.3% | 2.1/5.2% | 3 |
| 4 | 1 | 0.824 | 0.798 | 0.025 | - | - | 0.910 | 0.985 | 0.000 | 1.34x | 15.2/25.8/29.1% | 2.1/5.1% | 3 |

> hops-apart=4: decode_failures 38

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.805 | 0.804 | 0.002 | - | - | 0.961 | 0.962 | 0.000 | 1.34x | 15.0/25.9/29.3% | 2.1/5.2% | 3 |
| 2 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 3 | 1 | 0.825 | 0.804 | 0.021 | - | - | 0.989 | 0.990 | 0.000 | 1.34x | 15.2/25.9/29.3% | 2.1/5.2% | 3 |
| 4 | 1 | 0.824 | 0.798 | 0.025 | - | - | 0.910 | 0.985 | 0.000 | 1.34x | 15.2/25.8/29.1% | 2.1/5.1% | 3 |
| 5 | 1 | 0.834 | 0.802 | 0.032 | - | - | 0.891 | 0.985 | 0.000 | 1.36x | 15.3/26.0/29.4% | 2.1/5.2% | 3 |

> hops-apart=4: decode_failures 38

> hops-apart=5: decode_failures 37

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.826 | 0.814 | 0.012 | - | - | 0.980 | 0.982 | 0.000 | 1.36x | 15.1/26.5/29.8% | 2.1/5.3% | 3 |
| 30 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 120 | 1 | 0.826 | 0.813 | 0.013 | - | - | 0.979 | 0.979 | 0.000 | 1.33x | 14.9/26.2/29.4% | 2.1/5.2% | 3 |
| 600 | 1 | 0.825 | 0.812 | 0.013 | - | - | 0.981 | 0.983 | 0.000 | 1.35x | 15.1/26.5/29.8% | 2.1/5.3% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.826 | 0.814 | 0.012 | - | - | 0.980 | 0.982 | 0.000 | 1.36x | 15.1/26.5/29.8% | 2.1/5.3% | 3 |
| 30 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 120 | 1 | 0.826 | 0.813 | 0.013 | - | - | 0.979 | 0.979 | 0.000 | 1.33x | 14.9/26.2/29.4% | 2.1/5.2% | 3 |
| 600 | 1 | 0.825 | 0.812 | 0.013 | - | - | 0.981 | 0.983 | 0.000 | 1.35x | 15.1/26.5/29.8% | 2.1/5.3% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.816 | 0.808 | 0.008 | - | - | 0.550 | 0.925 | 0.000 | 1.33x | 15.2/25.6/28.9% | 2.1/5.0% | 3 |
| routers | 1 | 0.816 | 0.811 | 0.005 | - | - | 0.962 | 0.962 | 0.000 | 1.33x | 14.9/26.0/29.3% | 2.0/5.2% | 3 |
| alternate-routers | 1 | 0.811 | 0.807 | 0.005 | - | - | 0.956 | 0.956 | 0.000 | 1.34x | 15.0/26.2/29.5% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.805 | 0.804 | 0.001 | - | - | 0.956 | 0.956 | 0.000 | 1.34x | 14.9/25.9/29.3% | 2.1/5.1% | 3 |
| random-clients | 1 | 0.818 | 0.806 | 0.012 | - | - | 0.895 | 0.903 | 0.000 | 1.35x | 15.3/25.8/29.2% | 2.0/5.0% | 3 |
| hops-apart | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

> place=spread: decode_failures 18

> place=random-clients: decode_failures 3

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.816 | 0.808 | 0.008 | - | - | 0.550 | 0.925 | 0.000 | 1.33x | 15.2/25.6/28.9% | 2.1/5.0% | 3 |
| routers | 1 | 0.816 | 0.811 | 0.005 | - | - | 0.962 | 0.962 | 0.000 | 1.33x | 14.9/26.0/29.3% | 2.0/5.2% | 3 |
| alternate-routers | 1 | 0.811 | 0.807 | 0.005 | - | - | 0.956 | 0.956 | 0.000 | 1.34x | 15.0/26.2/29.5% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.805 | 0.804 | 0.001 | - | - | 0.956 | 0.956 | 0.000 | 1.34x | 14.9/25.9/29.3% | 2.1/5.1% | 3 |
| random-clients | 1 | 0.818 | 0.806 | 0.012 | - | - | 0.895 | 0.903 | 0.000 | 1.35x | 15.3/25.8/29.2% | 2.0/5.0% | 3 |
| hops-apart | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

> place=spread: decode_failures 18

> place=random-clients: decode_failures 3

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| broadcast | 1 | 0.856 | 0.802 | 0.054 | - | - | 0.966 | 0.977 | 0.000 | 1.43x | 15.8/27.7/31.2% | 2.2/5.4% | 3 |

> provide-transport=broadcast: decode_failures 5

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| heard | 1 | 0.820 | 0.805 | 0.015 | - | - | 0.984 | 0.985 | 0.000 | 1.35x | 15.0/26.3/29.7% | 2.1/5.3% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.856 | 0.802 | 0.054 | - | - | 0.966 | 0.977 | 0.000 | 1.43x | 15.8/27.7/31.2% | 2.2/5.4% | 3 |
| heard | 1 | 0.857 | 0.797 | 0.060 | - | - | 0.970 | 0.974 | 0.000 | 1.44x | 15.9/28.0/31.4% | 2.2/5.5% | 3 |

> replay-ordering=tip: decode_failures 5

> replay-ordering=heard: misdecodes 6

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| enum | 1 | 0.821 | 0.806 | 0.015 | - | - | 0.973 | 0.987 | 0.000 | 1.34x | 14.9/26.6/29.8% | 2.0/5.3% | 3 |
| hybrid | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.816 | 0.811 | 0.005 | - | - | 0.962 | 0.962 | 0.000 | 1.33x | 14.9/26.0/29.3% | 2.0/5.2% | 3 |
| 6 | 1 | 0.817 | 0.808 | 0.009 | - | - | 0.979 | 0.979 | 0.000 | 1.38x | 15.4/26.8/30.2% | 2.1/5.5% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.806 | 0.801 | 0.006 | - | - | 0.965 | 0.965 | 0.000 | 1.34x | 15.1/25.9/29.2% | 2.1/5.1% | 2 |
| 3 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 5 | 1 | 0.822 | 0.802 | 0.020 | - | - | 0.987 | 0.987 | 0.000 | 1.35x | 15.0/26.6/29.8% | 2.1/5.2% | 5 |
| 8 | 1 | 0.823 | 0.799 | 0.024 | - | - | 0.994 | 0.997 | 0.000 | 1.42x | 15.8/27.7/31.1% | 2.1/5.6% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.806 | 0.801 | 0.006 | - | - | 0.965 | 0.965 | 0.000 | 1.34x | 15.1/25.9/29.2% | 2.1/5.1% | 2 |
| 3 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 5 | 1 | 0.822 | 0.802 | 0.020 | - | - | 0.987 | 0.987 | 0.000 | 1.35x | 15.0/26.6/29.8% | 2.1/5.2% | 5 |
| 8 | 1 | 0.823 | 0.799 | 0.024 | - | - | 0.994 | 0.997 | 0.000 | 1.42x | 15.8/27.7/31.1% | 2.1/5.6% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| True | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.842 | 0.831 | 0.011 | - | - | 0.982 | 0.984 | 0.000 | 1.24x | 13.8/24.3/27.3% | 1.9/4.7% | 3 |
| 1 | 1 | 0.837 | 0.826 | 0.011 | - | - | 0.982 | 0.982 | 0.000 | 1.24x | 13.8/24.2/27.2% | 1.9/4.8% | 3 |
| 2 | 1 | 0.826 | 0.814 | 0.013 | - | - | 0.979 | 0.979 | 0.000 | 1.25x | 13.9/24.4/27.5% | 1.9/4.8% | 3 |
| 4 | 1 | 0.823 | 0.812 | 0.010 | - | - | 0.966 | 0.973 | 0.000 | 1.22x | 13.8/23.9/26.9% | 1.9/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.818 | 0.803 | 0.015 | - | - | 0.972 | 0.976 | 0.000 | 1.34x | 15.1/26.2/29.5% | 2.1/5.2% | 3 |
| 24 | 1 | 0.828 | 0.816 | 0.012 | - | - | 0.983 | 0.983 | 0.000 | 1.35x | 15.2/26.3/29.6% | 2.0/5.3% | 3 |
| 32 | 1 | 0.825 | 0.813 | 0.013 | - | - | 0.983 | 0.984 | 0.000 | 1.34x | 15.0/26.3/29.6% | 2.1/5.2% | 3 |
| 64 | 1 | 0.823 | 0.810 | 0.013 | - | - | 0.978 | 0.978 | 0.000 | 1.33x | 14.9/26.0/29.3% | 2.0/5.2% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.822 | 0.808 | 0.014 | - | - | 0.980 | 0.984 | 0.000 | 1.44x | 15.8/28.1/31.6% | 2.2/5.6% | 3 |
| 16 | 1 | 0.822 | 0.806 | 0.015 | - | - | 0.980 | 0.983 | 0.000 | 1.38x | 15.3/26.8/30.1% | 2.1/5.3% | 3 |
| 32 | 1 | 0.819 | 0.805 | 0.014 | - | - | 0.974 | 0.977 | 0.000 | 1.33x | 14.8/25.9/29.1% | 2.1/5.2% | 3 |

> window-size=8: misdecodes 118

> window-size=16: misdecodes 61

> window-size=32: misdecodes 22

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.991 | 0.992 | 0.655 | 2.07x | 21.6/31.5/35.6% | 1.5/5.1% | 3 |
| True | 1 | 0.745 | 0.739 | 0.006 | - | - | 0.865 | 0.924 | 0.408 | 5.70x | 54.0/70.8/76.5% | 4.3/11.6% | 3 |

> no-congestion-scaling=True: decode_failures 108

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.508 | 0.499 | 0.008 | - | - | 0.793 | 0.794 | 0.222 | 4.50x | 15.8/24.8/33.3% | 1.5/5.5% | 3 |
| truesize | 1 | 0.537 | 0.529 | 0.008 | - | - | 0.822 | 0.824 | 0.242 | 3.32x | 11.7/19.0/26.3% | 1.1/4.5% | 3 |

> congestion-input=hotstore: decode_failures 16

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.954 | 0.953 | 0.002 | - | - | 0.996 | 0.996 | 0.662 | 1.94x | 20.2/29.9/33.8% | 1.4/4.9% | 3 |
| adaptive | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.991 | 0.992 | 0.655 | 2.07x | 21.6/31.5/35.6% | 1.5/5.1% | 3 |

