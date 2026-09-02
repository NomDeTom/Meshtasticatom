# Sweep blocks-2026-09-02-2602309

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 2602309 · seeds 2602309
- **blocks** 87 run
- **compute** 10.3 h of simulator time across every cell
- **generated** 2026-09-02T08:49:14+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>91 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 27
- AD-siting: siting-mix=basement-heavy: decode_failures 1
- AD-siting: slower: 3.03 s per simulated hour against 1.27 over 12 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 1
- DB-hotstore: max-num-nodes=10: decode_failures 10
- DB-hotstore-stress: max-num-nodes=10: decode_failures 60
- DB-warm: warm-num-nodes=0: decode_failures 113
- DB-warm: warm-num-nodes=25: decode_failures 113
- DB-warm: warm-num-nodes=100: decode_failures 113
- DB-warm: warm-num-nodes=2000: decode_failures 113
- DG-burst: burst-loss=0.2: decode_failures 3
- DG-burst: burst-loss=0.3: decode_failures 32
- DG-outage: burst-loss=0.1: decode_failures 28
- DG-outage: burst-loss=0.2: decode_failures 19
- DG-outage: burst-loss=0.3: decode_failures 18
- FW-versions: profile=2.4: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 31
- LD-chatty: broadcast-interval-s=300: decode_failures 32
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 113
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 12.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 120
- MS-density: nodes=90: misdecodes 1
- MS-density: nodes=120: misdecodes 1
- MS-siting: siting-mix=local-typical: decode_failures 39
- MS-siting: siting-mix=event: decode_failures 15
- MS-siting: slower: 4.4 s per simulated hour against 1.57 over 12 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.5: decode_failures 29
- MS-stretch: stretch=2.0: decode_failures 4
- MS-stretch: slower: 3.62 s per simulated hour against 1.77 over 12 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 10
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 1
- RF-eu-presets: preset=SHORT_FAST: decode_failures 3
- RF-eu-presets: preset=NARROW_SLOW: misdecodes 1
- RF-preset: preset=SHORT_FAST: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 40
- RF-preset: slower: 5.97 s per simulated hour against 2.85 over 12 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 1
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 10
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 7
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 29
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 1
- RF-stretch-duct: slower: 4.47 s per simulated hour against 1.87 over 12 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 1
- RF-txpower: tx-power=17: decode_failures 9
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-hoplimit: hop-limit=3: decode_failures 1
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SC-signing: signature-policy=STRICT: decode_failures 51
- SC-signing: slower: 4.32 s per simulated hour against 1.85 over 12 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 44
- SF-bucket-mode: bucket-mode=time: misdecodes 23
- SF-bucket-mode: bucket-mode=window: misdecodes 23
- SF-bucket-time: time-bucket-s=600: misdecodes 149
- SF-bucket-time: time-bucket-s=1800: misdecodes 23
- SF-bucket-time: time-bucket-s=3600: misdecodes 10
- SF-cadence: trigger=interval: misdecodes 14
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 7
- SF-cadence: trigger=bucket+interval: misdecodes 16
- SF-capacity-local: capacity=4: decode_failures 78
- SF-capacity-local: capacity=8: decode_failures 24
- SF-capacity: capacity=4: decode_failures 78
- SF-capacity: capacity=8: decode_failures 24
- SF-capacity-window: capacity=8: misdecodes 28
- SF-capacity-window: capacity=8: decode_failures 21
- SF-capacity-window: capacity=16: misdecodes 20
- SF-capacity-window: capacity=32: misdecodes 23
- SF-catchup: catch-up-hours=: misdecodes 16
- SF-catchup: catch-up-hours=02-06: decode_failures 37
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 36
- SF-hops-flat: hops-apart=3: decode_failures 1
- SF-hops-flat: hops-apart=4: decode_failures 35
- SF-hops-spread: hops-apart=3: decode_failures 1
- SF-hops-spread: hops-apart=4: decode_failures 35
- SF-hops-spread: hops-apart=5: decode_failures 29
- SF-place-flat: place=spread: decode_failures 23
- SF-place-flat: place=random-clients: decode_failures 1
- SF-place-spread: place=spread: decode_failures 23
- SF-place-spread: place=random-clients: decode_failures 1
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 11
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-window-size: window-size=8: misdecodes 175
- SF-window-size: window-size=16: misdecodes 76
- SF-window-size: window-size=32: misdecodes 23
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: decode_failures 119

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `MS-siting` | 4.4 | 1.57 | 2.81x | 12 |
| `RF-stretch-duct` | 4.47 | 1.87 | 2.40x | 12 |
| `AD-siting` | 3.03 | 1.27 | 2.38x | 12 |
| `SC-signing` | 4.32 | 1.85 | 2.34x | 12 |
| `RF-preset` | 5.97 | 2.85 | 2.10x | 12 |
| `MS-stretch` | 3.62 | 1.77 | 2.04x | 12 |
| `TH-congestion-input` | 7.79 | 11.7 | 0.67x | 12 |
| `FW-versions` | 1.12 | 1.69 | 0.66x | 12 |
| `MS-roles-fav` | 1.13 | 1.76 | 0.65x | 12 |
| `MS-density` | 2.18 | 3.62 | 0.60x | 12 |
| `MS-oversubscribed` | 11 | 19 | 0.58x | 12 |
| `MS-hopscale` | 9.6 | 18.6 | 0.52x | 12 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.975 | 0.975 | 0.859 → 0.864 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.959 | 0.959 | 0.846 → 0.859 | 1.1x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.155 → 0.959 | 0.804 | 0.102 → 0.852 | 9.2x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.081 → 0.882 | 0.801 | 0.029 → 0.779 | 17x sr_bytes | down | 3 |
| `RF-preset-turbo` | preset | **text** | 0.071 → 0.861 | 0.789 | 0.070 → 0.852 | 5.7x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.128 → 0.902 | 0.774 | 0.112 → 0.795 | 94x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.226 → 0.959 | 0.733 | 0.145 → 0.852 | 7.4x sr_bytes | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.345 → 0.972 | 0.627 | 0.336 → 0.970 | 3.4x sr_bytes | up | 4 |
| `RF-bw500` | preset | **held** | 0.311 → 0.937 | 0.626 | 0.176 → 0.757 | 3x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.379 → 0.959 | 0.580 | 0.322 → 0.852 | 8.5x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.371 → 0.924 | 0.553 | 0.324 → 0.728 | 4.7x bytes_on_air | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.346 → 0.861 | 0.514 | 0.339 → 0.852 | 2.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.346 → 0.861 | 0.514 | 0.339 → 0.852 | 2.5x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.563 → 0.926 | 0.364 | 0.556 → 0.925 | 2.5x sr_airtime | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.527 → 0.861 | 0.333 | 0.510 → 0.852 | 1.9x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.587 → 0.919 | 0.332 | 0.578 → 0.913 | 13x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.556 → 0.861 | 0.304 | 0.526 → 0.852 | 2.1x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.586 → 0.888 | 0.303 | 0.574 → 0.884 | 8.7x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.386 → 0.685 | 0.299 | 0.364 → 0.651 | 2.3x sr_bytes | up | 2 |
| `MS-density` | nodes | **text** | 0.669 → 0.967 | 0.298 | 0.652 → 0.965 | 5.1x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.645 → 0.929 | 0.284 | 0.618 → 0.929 | 2.9x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.505 → 0.788 | 0.283 | 0.318 → 0.521 | 5.4x sr_airtime | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.645 → 0.899 | 0.254 | 0.618 → 0.893 | 1.9x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.645 → 0.861 | 0.216 | 0.618 → 0.852 | 1.6x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.776 → 0.956 | 0.180 | 0.771 → 0.955 | 4.2x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **held** | 0.790 → 0.965 | 0.175 | 0.686 → 0.857 | 1.6x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.829 → 0.975 | 0.146 | 0.851 → 0.864 | 2x sr_bytes | down | 5 |
| `SC-signing` | signature-policy | **held** | 0.819 → 0.959 | 0.141 | 0.730 → 0.852 | 1.4x sr_airtime | down | 3 |
| `MS-size` | nodes | **text** | 0.733 → 0.861 | 0.128 | 0.724 → 0.852 | 6.3x sr_bytes | down | 5 |
| `AD-flooding` | role-mix | **text** | 0.786 → 0.913 | 0.127 | 0.779 → 0.905 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.786 → 0.913 | 0.127 | 0.779 → 0.905 | 2.4x bytes_on_air | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.737 → 0.861 | 0.124 | 0.723 → 0.852 | 1.4x sr_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.861 → 0.978 | 0.118 | 0.852 → 0.863 | 5.1x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.861 → 0.978 | 0.118 | 0.852 → 0.863 | 5.1x sr_bytes | up | 6 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.873 → 0.979 | 0.106 | 0.852 → 0.945 | 1.5x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.861 → 0.958 | 0.097 | 0.852 → 0.953 | 1.4x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.882 → 0.966 | 0.084 | 0.779 → 0.779 | 1.8x sr_bytes | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.678 → 0.761 | 0.083 | 0.674 → 0.756 | 1.6x sr_airtime | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.831 → 0.907 | 0.075 | 0.819 → 0.903 | 4.9x sr_airtime | up | 4 |
| `MS-roles` | role-mix | **text** | 0.786 → 0.861 | 0.075 | 0.779 → 0.851 | 1.1x sr_bytes | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.889 → 0.959 | 0.070 | 0.788 → 0.852 | 1.1x sr_airtime | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.833 → 0.901 | 0.069 | 0.822 → 0.899 | 2.2x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.833 → 0.901 | 0.068 | 0.826 → 0.899 | 2.3x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.861 → 0.920 | 0.059 | 0.852 → 0.916 | 1.5x sr_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.816 → 0.874 | 0.058 | 0.813 → 0.869 | 1.2x sr_bytes | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.821 → 0.867 | 0.046 | 0.811 → 0.859 | 1.6x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.915 → 0.959 | 0.044 | 0.834 → 0.865 | 14x advert_bytes | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.861 → 0.904 | 0.044 | 0.852 → 0.900 | 3.3x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.778 → 0.820 | 0.042 | 0.511 → 0.545 | 1.5x sr_airtime | up | 2 |
| `FW-versions` | profile | **text** | 0.861 → 0.898 | 0.038 | 0.852 → 0.889 | 3.2x bytes_on_air | down | 5 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.922 → 0.959 | 0.037 | 0.852 → 0.862 | 14x sr_airtime | down | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.862 → 0.895 | 0.033 | 0.857 → 0.892 | 1.2x sr_bytes | up | 2 |
| `SF-hops-flat` | hops-apart | **text** | 0.854 → 0.886 | 0.033 | 0.851 → 0.864 | 2x sr_bytes | up | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.959 → 0.991 | 0.032 | 0.851 → 0.862 | 2x bytes_on_air | up | 4 |
| `FW-firmware` | profile | **text** | 0.861 → 0.891 | 0.030 | 0.852 → 0.879 | 3.1x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.856 → 0.885 | 0.029 | 0.841 → 0.866 | 2.1x bytes_on_air | down | 4 |
| `SF-servers-flat` | servers | **held** | 0.959 → 0.986 | 0.027 | 0.852 → 0.863 | 8x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.959 → 0.986 | 0.027 | 0.852 → 0.863 | 8x sr_bytes | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.844 → 0.871 | 0.027 | 0.834 → 0.867 | 9.3x advert_bytes | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.861 → 0.886 | 0.026 | 0.852 → 0.881 | 1.2x sr_bytes | down | 3 |
| `AD-worst` | role-placement | **text** | 0.785 → 0.808 | 0.024 | 0.775 → 0.804 | 1.3x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.952 → 0.971 | 0.019 | 0.862 → 0.869 | 2.3x advert_bytes | up | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.861 → 0.877 | 0.016 | 0.852 → 0.852 | 2.5x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **text** | 0.825 → 0.840 | 0.015 | 0.825 → 0.840 | 1.2x sr_airtime | up | 3 |
| `SF-window-size` | window-size | **held** | 0.955 → 0.968 | 0.012 | 0.859 → 0.862 | 5.4x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.956 → 0.968 | 0.012 | 0.852 → 0.862 | 2.9x advert_bytes | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.957 → 0.969 | 0.011 | 0.852 → 0.862 | 3.1x advert_bytes | down | 4 |
| `SF-capacity` | capacity | **text** | 0.861 → 0.872 | 0.011 | 0.852 → 0.866 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **text** | 0.861 → 0.872 | 0.011 | 0.852 → 0.866 | 5.3x advert_bytes | up | 5 |
| `SF-sr-retries` | sr-retries | **text** | 0.870 → 0.881 | 0.011 | 0.863 → 0.875 | 1.2x sr_bytes | down | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.861 → 0.871 | 0.011 | 0.852 → 0.863 | 1.4x bytes_on_air | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.861 → 0.870 | 0.009 | 0.852 → 0.863 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.959 → 0.968 | 0.008 | 0.855 → 0.863 | 5.2x advert_bytes | down | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.954 → 0.962 | 0.008 | 0.852 → 0.861 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.954 → 0.962 | 0.008 | 0.852 → 0.861 | 1.1x sr_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.836 → 0.844 | 0.008 | 0.836 → 0.844 | 1.1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.948 → 0.956 | 0.008 | 0.947 → 0.955 | 1.2x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.975 → 0.982 | 0.007 | 0.856 → 0.860 | 3.3x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.861 → 0.866 | 0.005 | 0.852 → 0.858 | 1x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.836 → 0.840 | 0.004 | 0.836 → 0.840 | 1.1x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.956 → 0.960 | 0.004 | 0.955 → 0.959 | 1x sr_bytes | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.955 → 0.958 | 0.003 | 0.849 → 0.852 | 1.1x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.861 → 0.863 | 0.003 | 0.852 → 0.857 | 2.7x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.956 → 0.958 | 0.001 | 0.955 → 0.956 | 1x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **held** | 0.958 → 0.959 | 0.001 | 0.852 → 0.853 | 5.7x advert_bytes | = | 3 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario valleys`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| sprinkled | 1 | 0.918 | 0.896 | 0.022 | - | - | 0.983 | 0.989 | 0.715 | 1.11x | 15.9/21.3/22.8% | 1.6/5.0% | 3 |
| arms-race | 1 | 0.958 | 0.953 | 0.004 | - | - | 0.998 | 0.998 | 0.864 | 1.02x | 18.5/23.6/26.9% | 1.3/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.1 | 1 | 0.898 | 0.892 | 0.006 | - | - | 0.873 | 0.875 | 0.713 | 1.25x | 18.2/24.1/28.7% | 1.8/5.3% | 3 |
| 0.3 | 1 | 0.950 | 0.945 | 0.005 | - | - | 0.979 | 0.979 | 0.887 | 1.06x | 20.8/25.5/30.9% | 1.3/5.1% | 3 |

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.786 | 0.779 | 0.007 | - | - | 0.882 | 0.884 | 0.145 | 1.13x | 15.6/23.0/27.5% | 1.7/5.3% | 3 |
| inverse | 1 | 0.811 | 0.779 | 0.031 | - | - | 0.948 | 0.951 | 0.508 | 1.08x | 12.8/18.1/20.3% | 1.9/3.3% | 3 |
| random | 1 | 0.802 | 0.779 | 0.023 | - | - | 0.966 | 0.968 | 0.367 | 1.08x | 13.9/18.6/22.1% | 1.8/5.0% | 3 |

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.786 | 0.779 | 0.007 | - | - | 0.882 | 0.884 | 0.145 | 1.13x | 15.6/23.0/27.5% | 1.7/5.3% | 3 |
| all-routers | 1 | 0.913 | 0.905 | 0.008 | - | - | 0.979 | 0.982 | 0.678 | 2.77x | 32.7/40.3/45.7% | 4.5/5.5% | 3 |

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.786 | 0.779 | 0.007 | - | - | 0.882 | 0.884 | 0.145 | 1.13x | 15.6/23.0/27.5% | 1.7/5.3% | 3 |
| no-mute | 1 | 0.846 | 0.838 | 0.008 | - | - | 0.937 | 0.940 | 0.497 | 1.25x | 15.7/22.1/26.1% | 1.9/5.4% | 3 |
| all-routers | 1 | 0.913 | 0.905 | 0.008 | - | - | 0.979 | 0.982 | 0.678 | 2.77x | 32.7/40.3/45.7% | 4.5/5.5% | 3 |

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.786 | 0.779 | 0.007 | - | - | 0.882 | 0.884 | 0.145 | 1.13x | 15.6/23.0/27.5% | 1.7/5.3% | 3 |
| local-typical | 1 | 0.709 | 0.693 | 0.016 | - | - | 0.802 | 0.865 | 0.149 | 1.27x | 12.8/24.4/29.6% | 1.9/5.3% | 3 |
| basement-heavy | 1 | 0.029 | 0.029 | 0.000 | - | - | 0.081 | 0.089 | 0.000 | 0.36x | 0.9/3.3/5.1% | 0.3/1.9% | 3 |

> siting-mix=local-typical: decode_failures 27

> siting-mix=basement-heavy: decode_failures 1

> slower: 3.03 s per simulated hour against 1.27 over 12 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.808 | 0.804 | 0.004 | - | - | 0.935 | 0.935 | 0.073 | 2.47x | 16.2/27.0/33.8% | 2.0/5.3% | 3 |
| inverse | 1 | 0.785 | 0.775 | 0.010 | - | - | 0.935 | 0.938 | 0.084 | 2.36x | 14.5/22.3/29.5% | 1.9/3.2% | 3 |

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.859 | 0.859 | 0.000 | - | - | 0 | 0.000 | 0.492 | 1.24x | 15.6/22.8/28.0% | 1.7/5.3% | 3 |
| sr | 1 | 0.881 | 0.864 | 0.017 | - | - | 0.975 | 0.987 | 0.501 | 1.26x | 15.7/23.0/28.4% | 1.7/5.4% | 3 |

> protocol=sr: decode_failures 1

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.833 | 0.826 | 0.007 | - | - | 0.922 | 0.936 | 0.468 | 3.19x | 40.0/56.4/63.2% | 4.7/11.1% | 3 |
| 100 | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.972 | 0.973 | 0.571 | 1.56x | 19.9/29.3/33.6% | 2.2/5.4% | 3 |
| 120 | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.972 | 0.973 | 0.571 | 1.56x | 19.9/29.3/33.6% | 2.2/5.4% | 3 |
| 250 | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.972 | 0.973 | 0.571 | 1.56x | 19.9/29.3/33.6% | 2.2/5.4% | 3 |

> max-num-nodes=10: decode_failures 10

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.322 | 0.318 | 0.004 | - | - | 0.505 | 0.517 | 0.142 | 11.36x | 38.1/62.8/72.6% | 4.0/11.1% | 3 |
| 120 | 1 | 0.518 | 0.511 | 0.007 | - | - | 0.778 | 0.780 | 0.193 | 4.38x | 14.5/30.3/39.4% | 1.4/4.9% | 3 |
| 250 | 1 | 0.528 | 0.521 | 0.007 | - | - | 0.788 | 0.789 | 0.205 | 4.34x | 14.4/30.1/39.0% | 1.4/4.8% | 3 |

> max-num-nodes=10: decode_failures 60

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.972 | 0.973 | 0.571 | 1.56x | 19.9/29.3/33.6% | 2.2/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.972 | 0.973 | 0.571 | 1.56x | 19.9/29.3/33.6% | 2.2/5.4% | 3 |
| constrained | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.932 | 0.933 | 0.456 | 3.18x | 40.1/56.3/63.0% | 4.8/11.1% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.761 | 0.756 | 0.005 | - | - | 0.919 | 0.944 | 0.552 | 5.58x | 57.9/68.9/73.3% | 3.7/12.5% | 3 |
| 25 | 1 | 0.761 | 0.756 | 0.005 | - | - | 0.919 | 0.944 | 0.552 | 5.58x | 57.9/68.9/73.3% | 3.7/12.5% | 3 |
| 100 | 1 | 0.761 | 0.756 | 0.005 | - | - | 0.919 | 0.944 | 0.552 | 5.58x | 57.9/68.9/73.3% | 3.7/12.5% | 3 |
| 2000 | 1 | 0.761 | 0.756 | 0.005 | - | - | 0.919 | 0.944 | 0.552 | 5.58x | 57.9/68.9/73.3% | 3.7/12.5% | 3 |

> warm-num-nodes=0: decode_failures 113

> warm-num-nodes=25: decode_failures 113

> warm-num-nodes=100: decode_failures 113

> warm-num-nodes=2000: decode_failures 113

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.1 | 1 | 0.761 | 0.746 | 0.015 | - | - | 0.932 | 0.935 | 0.432 | 1.17x | 14.9/22.1/27.3% | 1.6/4.8% | 3 |
| 0.2 | 1 | 0.657 | 0.635 | 0.022 | - | - | 0.864 | 0.882 | 0.347 | 1.10x | 14.5/21.4/26.4% | 1.5/4.4% | 3 |
| 0.3 | 1 | 0.556 | 0.526 | 0.030 | - | - | 0.794 | 0.842 | 0.272 | 1.02x | 13.7/20.0/25.2% | 1.4/3.9% | 3 |

> burst-loss=0.2: decode_failures 3

> burst-loss=0.3: decode_failures 32

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.1 | 1 | 0.845 | 0.838 | 0.007 | - | - | 0.957 | 0.958 | 0.483 | 1.31x | 16.8/24.5/29.9% | 1.8/5.2% | 3 |
| 0.2 | 1 | 0.793 | 0.782 | 0.011 | - | - | 0.930 | 0.935 | 0.396 | 1.40x | 17.8/26.0/31.5% | 2.0/5.1% | 3 |
| 0.3 | 1 | 0.737 | 0.723 | 0.014 | - | - | 0.902 | 0.904 | 0.327 | 1.41x | 18.4/26.6/32.5% | 2.0/5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.1 | 1 | 0.750 | 0.740 | 0.010 | - | - | 0.913 | 0.944 | 0.394 | 1.20x | 15.6/22.8/28.0% | 1.6/5.1% | 3 |
| 0.2 | 1 | 0.641 | 0.622 | 0.019 | - | - | 0.846 | 0.875 | 0.335 | 1.11x | 14.6/21.5/26.9% | 1.5/4.5% | 3 |
| 0.3 | 1 | 0.527 | 0.510 | 0.017 | - | - | 0.739 | 0.797 | 0.251 | 1.05x | 14.1/20.2/25.4% | 1.6/4.1% | 3 |

> burst-loss=0.1: decode_failures 28

> burst-loss=0.2: decode_failures 19

> burst-loss=0.3: decode_failures 18

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.825 | 0.825 | 0.000 | - | - | 0.940 | 0.943 | 0.472 | 1.64x | 21.3/31.1/37.8% | 2.2/7.2% | 3 |
| directed-with-late-flood | 1 | 0.840 | 0.840 | 0.000 | - | - | 0.947 | 0.950 | 0.488 | 1.46x | 18.9/27.8/33.9% | 2.0/6.3% | 3 |
| m4-early-flood | 1 | 0.840 | 0.840 | 0.000 | - | - | 0.947 | 0.952 | 0.511 | 1.46x | 18.9/27.9/34.2% | 2.0/6.4% | 3 |

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.891 | 0.879 | 0.011 | - | - | 0.966 | 0.968 | 0.667 | 0.72x | 8.7/11.5/12.3% | 1.1/2.1% | 3 |
| 2.8 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.25 | 1 | 0.878 | 0.861 | 0.018 | - | - | 0.976 | 0.976 | 0.513 | 1.10x | 14.2/20.0/24.5% | 1.6/4.9% | 3 |
| 0.5 | 1 | 0.870 | 0.862 | 0.008 | - | - | 0.982 | 0.983 | 0.626 | 1.00x | 12.4/16.9/20.2% | 1.5/4.3% | 3 |
| 0.75 | 1 | 0.864 | 0.851 | 0.013 | - | - | 0.991 | 0.991 | 0.587 | 0.83x | 10.3/14.9/16.9% | 1.2/3.5% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.25 | 1 | 0.885 | 0.866 | 0.020 | - | - | 0.985 | 0.987 | 0.543 | 1.11x | 14.6/20.7/25.3% | 1.7/4.9% | 3 |
| 0.5 | 1 | 0.868 | 0.859 | 0.009 | - | - | 0.981 | 0.982 | 0.597 | 0.99x | 12.7/16.6/20.1% | 1.5/4.3% | 3 |
| 0.75 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.977 | 0.980 | 0.591 | 0.80x | 9.9/14.8/16.6% | 1.2/3.4% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.904 | 0.900 | 0.004 | - | - | 0.983 | 0.984 | 0.587 | 0.65x | 8.7/13.0/16.2% | 0.9/3.1% | 3 |
| signing=true | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.895 | 0.882 | 0.012 | - | - | 0.972 | 0.974 | 0.677 | 0.71x | 9.4/12.7/13.7% | 1.0/2.6% | 3 |
| 2.5 | 1 | 0.886 | 0.875 | 0.011 | - | - | 0.965 | 0.965 | 0.671 | 0.73x | 9.7/12.7/13.9% | 1.1/2.6% | 3 |
| 2.6 | 1 | 0.882 | 0.871 | 0.011 | - | - | 0.958 | 0.959 | 0.663 | 0.69x | 9.4/12.6/13.6% | 1.0/2.6% | 3 |
| 2.7 | 1 | 0.898 | 0.889 | 0.009 | - | - | 0.971 | 0.972 | 0.647 | 0.70x | 9.4/12.8/14.4% | 1.0/3.0% | 3 |
| 2.8 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

> profile=2.4: misdecodes 1

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.888 | 0.884 | 0.004 | - | - | 0.983 | 0.983 | 0.556 | 0.85x | 11.1/15.9/19.5% | 1.2/3.7% | 3 |
| 900 | 1 | 0.831 | 0.819 | 0.013 | - | - | 0.946 | 0.947 | 0.452 | 1.97x | 24.6/36.5/44.0% | 2.6/8.4% | 3 |
| 300 | 1 | 0.586 | 0.574 | 0.011 | - | - | 0.721 | 0.792 | 0.297 | 4.38x | 51.5/70.1/77.8% | 6.5/16.7% | 3 |

> broadcast-interval-s=300: decode_failures 32

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.919 | 0.913 | 0.005 | - | - | 0.968 | 0.968 | 0.744 | 0.89x | 11.2/15.4/19.0% | 1.4/3.5% | 3 |
| 900 | 1 | 0.858 | 0.850 | 0.008 | - | - | 0.911 | 0.912 | 0.620 | 2.26x | 27.8/38.7/46.8% | 3.4/8.7% | 3 |
| 300 | 1 | 0.587 | 0.578 | 0.009 | - | - | 0.652 | 0.718 | 0.376 | 4.89x | 56.5/72.3/79.5% | 7.9/17.4% | 3 |

> broadcast-interval-s=300: decode_failures 31

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.886 | 0.881 | 0.005 | - | - | 0.979 | 0.980 | 0.533 | 1.20x | 15.6/22.3/27.3% | 1.7/5.1% | 3 |
| sinusoid | 1 | 0.884 | 0.876 | 0.008 | - | - | 0.978 | 0.979 | 0.556 | 1.13x | 14.5/21.2/25.9% | 1.5/4.9% | 3 |
| commuter | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.831 | 0.819 | 0.013 | - | - | 0.946 | 0.947 | 0.452 | 1.97x | 24.6/36.5/44.0% | 2.6/8.4% | 3 |
| 3600 | 1 | 0.888 | 0.884 | 0.004 | - | - | 0.983 | 0.983 | 0.556 | 0.85x | 11.1/15.9/19.5% | 1.2/3.7% | 3 |
| 10800 | 1 | 0.907 | 0.903 | 0.003 | - | - | 0.986 | 0.986 | 0.584 | 0.57x | 7.5/10.5/12.8% | 0.8/2.5% | 3 |
| 43200 | 1 | 0.906 | 0.903 | 0.003 | - | - | 0.986 | 0.986 | 0.575 | 0.40x | 5.2/7.3/9.0% | 0.6/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.25 | 1 | 0.867 | 0.859 | 0.008 | - | - | 0.962 | 0.963 | 0.524 | 1.32x | 16.9/24.5/30.0% | 1.8/5.6% | 3 |
| 1.0 | 1 | 0.857 | 0.849 | 0.008 | - | - | 0.960 | 0.962 | 0.490 | 1.42x | 18.1/26.8/32.8% | 1.9/6.2% | 3 |
| 4.0 | 1 | 0.821 | 0.811 | 0.010 | - | - | 0.924 | 0.926 | 0.486 | 1.74x | 22.0/33.5/40.9% | 2.2/7.9% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.761 | 0.756 | 0.005 | - | - | 0.919 | 0.944 | 0.552 | 5.58x | 57.9/68.9/73.3% | 3.7/12.5% | 3 |
| 1.0 | 1 | 0.678 | 0.674 | 0.004 | - | - | 0.848 | 0.900 | 0.479 | 6.29x | 61.9/72.5/76.3% | 4.2/13.9% | 3 |

> traceroute-per-hour=0.0: decode_failures 113

> traceroute-per-hour=1.0: queue drops 12.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 120

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.669 | 0.652 | 0.017 | - | - | 0.868 | 0.869 | 0.232 | 1.32x | 17.5/24.5/26.2% | 3.1/6.6% | 3 |
| 60 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 90 | 1 | 0.941 | 0.939 | 0.002 | - | - | 0.997 | 0.997 | 0.796 | 1.61x | 19.2/28.2/31.8% | 1.5/5.1% | 3 |
| 120 | 1 | 0.956 | 0.955 | 0.002 | - | - | 0.999 | 0.999 | 0.811 | 1.94x | 21.7/28.5/31.6% | 1.2/5.1% | 3 |
| 150 | 1 | 0.967 | 0.965 | 0.003 | - | - | 0.997 | 0.998 | 0.841 | 2.58x | 28.4/44.5/49.4% | 1.3/5.7% | 3 |

> nodes=90: misdecodes 1

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 120 | 1 | 0.741 | 0.724 | 0.017 | - | - | 0.918 | 0.918 | 0.377 | 2.13x | 14.6/22.9/28.9% | 1.5/5.6% | 3 |
| 250 | 1 | 0.521 | 0.514 | 0.007 | - | - | 0.778 | 0.779 | 0.187 | 4.69x | 15.5/33.0/42.5% | 1.5/5.4% | 3 |
| 500 | 1 | 0.327 | 0.322 | 0.005 | - | - | 0.379 | 0.380 | 0.076 | 10.21x | 19.0/32.6/51.7% | 1.7/5.5% | 3 |

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.745 | 0.728 | 0.018 | - | - | 0.924 | 0.926 | 0.389 | 2.01x | 14.0/21.6/27.1% | 1.4/5.2% | 3 |
| 250 | 1 | 0.518 | 0.511 | 0.007 | - | - | 0.778 | 0.780 | 0.193 | 4.38x | 14.5/30.3/39.4% | 1.4/4.9% | 3 |
| 500 | 1 | 0.328 | 0.324 | 0.004 | - | - | 0.371 | 0.372 | 0.084 | 9.41x | 17.7/29.9/47.5% | 1.5/5.1% | 3 |

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.861 | 0.851 | 0.010 | - | - | 0.949 | 0.950 | 0.506 | 1.25x | 15.9/23.4/28.4% | 1.7/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.786 | 0.779 | 0.007 | - | - | 0.882 | 0.884 | 0.145 | 1.13x | 15.6/23.0/27.5% | 1.7/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.874 | 0.869 | 0.005 | - | - | 0.939 | 0.940 | 0.558 | 1.34x | 16.8/23.7/28.8% | 1.8/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.816 | 0.813 | 0.003 | - | - | 0.889 | 0.890 | 0.195 | 1.28x | 17.8/25.9/29.7% | 2.2/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.05 | 1 | 0.867 | 0.861 | 0.006 | - | - | 0.959 | 0.959 | 0.511 | 1.38x | 18.2/26.9/31.8% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.869 | 0.863 | 0.006 | - | - | 0.962 | 0.963 | 0.519 | 1.51x | 20.6/30.1/34.0% | 2.1/5.4% | 3 |
| 0.2 | 1 | 0.871 | 0.862 | 0.009 | - | - | 0.966 | 0.970 | 0.485 | 1.70x | 24.5/32.7/35.5% | 2.4/5.5% | 3 |

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| local-typical | 1 | 0.750 | 0.735 | 0.014 | - | - | 0.781 | 0.921 | 0.134 | 1.47x | 13.7/24.1/27.9% | 2.2/5.6% | 3 |
| event | 1 | 0.345 | 0.336 | 0.009 | - | - | 0.569 | 0.665 | 0.000 | 1.46x | 7.9/20.2/26.8% | 2.4/5.7% | 3 |
| backbone | 1 | 0.972 | 0.970 | 0.002 | - | - | 0.997 | 0.997 | 0.903 | 1.06x | 23.0/31.9/34.6% | 1.3/5.4% | 3 |

> siting-mix=local-typical: decode_failures 39

> siting-mix=event: decode_failures 15

> slower: 4.4 s per simulated hour against 1.57 over 12 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.810 | 0.795 | 0.015 | - | - | 0.893 | 0.897 | 0.669 | 1.33x | 22.2/27.5/32.8% | 2.7/7.2% | 3 |
| 60 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 90 | 1 | 0.836 | 0.829 | 0.007 | - | - | 0.978 | 0.979 | 0.562 | 1.64x | 14.9/25.5/29.1% | 1.5/4.9% | 3 |
| 120 | 1 | 0.741 | 0.724 | 0.017 | - | - | 0.918 | 0.918 | 0.377 | 2.13x | 14.6/22.9/28.9% | 1.5/5.6% | 3 |
| 150 | 1 | 0.733 | 0.726 | 0.007 | - | - | 0.971 | 0.972 | 0.292 | 2.87x | 15.6/29.2/36.7% | 1.6/6.1% | 3 |

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 1.25 | 1 | 0.596 | 0.584 | 0.013 | - | - | 0.885 | 0.899 | 0.146 | 1.41x | 13.5/18.5/21.3% | 2.1/5.2% | 3 |
| 1.5 | 1 | 0.386 | 0.364 | 0.022 | - | - | 0.681 | 0.750 | 0.042 | 1.48x | 11.8/18.1/21.3% | 2.3/5.0% | 3 |
| 2.0 | 1 | 0.147 | 0.145 | 0.001 | - | - | 0.226 | 0.268 | 0.000 | 0.89x | 5.3/9.0/12.4% | 1.2/3.2% | 3 |

> stretch=1.5: decode_failures 29

> stretch=2.0: decode_failures 4

> slower: 3.62 s per simulated hour against 1.77 over 12 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| clustered | 1 | 0.790 | 0.787 | 0.003 | - | - | 0.882 | 0.882 | 0.440 | 1.16x | 19.4/31.5/32.9% | 1.7/5.0% | 3 |
| corridor | 1 | 0.563 | 0.556 | 0.006 | - | - | 0.606 | 0.611 | 0.358 | 1.33x | 16.3/20.5/24.7% | 1.9/5.1% | 3 |
| hub | 1 | 0.926 | 0.925 | 0.002 | - | - | 0.958 | 0.960 | 0.803 | 1.24x | 26.9/35.7/37.2% | 2.0/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.840 | 0.840 | 0.000 | - | - | 0.947 | 0.950 | 0.488 | 1.46x | 18.9/27.8/33.9% | 2.0/6.3% | 3 |
| True | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.943 | 0.948 | 0.477 | 1.47x | 19.2/28.1/34.3% | 2.0/6.4% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.943 | 0.948 | 0.477 | 1.47x | 19.2/28.1/34.3% | 2.0/6.4% | 3 |
| m4-early-flood | 1 | 0.844 | 0.844 | 0.000 | - | - | 0.950 | 0.956 | 0.486 | 1.47x | 19.0/28.1/34.3% | 2.0/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.859 | 0.859 | 0.000 | - | - | 0 | 0.000 | 0.492 | 1.24x | 15.6/22.8/28.0% | 1.7/5.3% | 3 |
| chain | 1 | 0.848 | 0.846 | 0.002 | - | - | 0.897 | 0.956 | 0.505 | 1.41x | 18.3/26.7/32.2% | 2.0/6.1% | 3 |
| sr | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| True | 1 | 0.870 | 0.863 | 0.006 | - | - | 0.962 | 0.963 | 0.542 | 1.27x | 16.1/23.3/28.5% | 1.8/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.955 | 0.002 | - | - | 0.999 | 0.999 | 0.811 | 1.94x | 21.7/28.5/31.6% | 1.2/5.1% | 3 |
| True | 1 | 0.958 | 0.956 | 0.001 | - | - | 0.998 | 0.998 | 0.808 | 1.94x | 21.6/28.2/31.5% | 1.2/5.1% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.178 | 0.176 | 0.003 | - | - | 0.311 | 0.341 | 0.000 | 0.04x | 0.2/0.5/0.6% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.491 | 0.471 | 0.020 | - | - | 0.794 | 0.796 | 0.107 | 0.28x | 2.4/3.8/4.7% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.769 | 0.757 | 0.012 | - | - | 0.937 | 0.939 | 0.266 | 1.17x | 13.4/16.5/21.2% | 1.7/4.8% | 3 |

> preset=SHORT_TURBO: decode_failures 10

> preset=MEDIUM_TURBO: decode_failures 1

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 0.25 | 1 | 0.881 | 0.873 | 0.008 | - | - | 0.977 | 0.977 | 0.565 | 1.23x | 17.0/24.4/29.7% | 1.7/5.4% | 3 |
| 1.0 | 1 | 0.920 | 0.916 | 0.004 | - | - | 0.977 | 0.977 | 0.740 | 1.05x | 21.6/27.8/32.2% | 1.5/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.346 | 0.339 | 0.007 | - | - | 0.541 | 0.557 | 0.000 | 0.15x | 1.0/1.8/2.4% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| LITE_FAST | 1 | 0.786 | 0.772 | 0.013 | - | - | 0.949 | 0.950 | 0.354 | 0.93x | 11.4/17.0/18.9% | 1.4/4.2% | 3 |
| NARROW_SLOW | 1 | 0.818 | 0.808 | 0.010 | - | - | 0.965 | 0.966 | 0.377 | 1.19x | 14.3/20.9/23.3% | 1.6/5.4% | 3 |

> preset=SHORT_FAST: decode_failures 3

> preset=NARROW_SLOW: misdecodes 1

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| temporal | 1 | 0.804 | 0.789 | 0.015 | - | - | 0.953 | 0.955 | 0.338 | 1.30x | 16.3/24.1/29.1% | 1.8/5.3% | 3 |
| transient | 1 | 0.866 | 0.857 | 0.008 | - | - | 0.965 | 0.969 | 0.508 | 1.24x | 15.9/23.3/28.4% | 1.7/5.3% | 3 |
| periodic | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.790 | 0.800 | 0.354 | 1.16x | 14.7/21.5/26.4% | 1.5/4.6% | 3 |

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.346 | 0.339 | 0.007 | - | - | 0.541 | 0.557 | 0.000 | 0.15x | 1.0/1.8/2.4% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| LONG_MODERATE | 1 | 0.823 | 0.811 | 0.012 | - | - | 0.890 | 0.971 | 0.663 | 3.28x | 44.3/61.0/68.1% | 4.5/12.6% | 3 |

> preset=SHORT_FAST: decode_failures 3

> preset=LONG_MODERATE: decode_failures 40

> slower: 5.97 s per simulated hour against 2.85 over 12 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.071 | 0.070 | 0.002 | - | - | 0.178 | 0.180 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.178 | 0.176 | 0.003 | - | - | 0.311 | 0.341 | 0.000 | 0.04x | 0.2/0.5/0.6% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| LONG_TURBO | 1 | 0.769 | 0.757 | 0.012 | - | - | 0.937 | 0.939 | 0.266 | 1.17x | 13.4/16.5/21.2% | 1.7/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.837 | 0.831 | 0.006 | - | - | 0.944 | 0.949 | 0.557 | 1.75x | 21.2/29.6/32.4% | 2.4/7.3% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 1

> preset=SHORT_TURBO: decode_failures 10

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.801 | 0.795 | 0.005 | - | - | 0.902 | 0.903 | 0.455 | 1.21x | 15.6/22.9/27.9% | 1.6/5.1% | 3 |
| 10000 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.790 | 0.800 | 0.354 | 1.16x | 14.7/21.5/26.4% | 1.5/4.6% | 3 |
| 4000 | 1 | 0.453 | 0.451 | 0.003 | - | - | 0.521 | 0.568 | 0.207 | 1.04x | 13.3/19.7/24.3% | 1.5/3.6% | 3 |
| 2000 | 1 | 0.112 | 0.112 | 0.000 | - | - | 0.128 | 0.199 | 0.043 | 0.72x | 9.5/14.0/17.9% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 7

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.386 | 0.364 | 0.022 | - | - | 0.681 | 0.750 | 0.042 | 1.48x | 11.8/18.1/21.3% | 2.3/5.0% | 3 |
| 1.0 | 1 | 0.685 | 0.651 | 0.033 | - | - | 0.870 | 0.873 | 0.447 | 1.02x | 14.1/18.9/21.8% | 1.4/4.5% | 3 |

> duct-per-hour=0.0: decode_failures 29

> duct-per-hour=1.0: decode_failures 1

> slower: 4.47 s per simulated hour against 1.87 over 12 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 22 | 1 | 0.458 | 0.438 | 0.020 | - | - | 0.748 | 0.757 | 0.125 | 1.44x | 11.7/17.4/20.0% | 2.1/4.8% | 3 |
| 17 | 1 | 0.179 | 0.175 | 0.004 | - | - | 0.267 | 0.329 | 0.000 | 1.02x | 5.4/9.8/13.5% | 1.4/3.5% | 3 |
| 14 | 1 | 0.102 | 0.102 | 0.000 | - | - | 0.155 | 0.157 | 0.000 | 0.78x | 3.7/6.8/8.7% | 1.3/2.3% | 3 |

> tx-power=22: decode_failures 1

> tx-power=17: decode_failures 9

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.955 | 0.002 | - | - | 0.999 | 0.999 | 0.811 | 1.94x | 21.7/28.5/31.6% | 1.2/5.1% | 3 |
| True | 1 | 0.948 | 0.947 | 0.001 | - | - | 0.997 | 0.998 | 0.784 | 2.34x | 25.4/32.3/35.7% | 1.5/5.7% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.862 | 0.857 | 0.005 | - | - | 0.965 | 0.967 | 0.487 | 1.33x | 17.1/25.9/31.0% | 1.8/5.5% | 3 |
| True | 1 | 0.895 | 0.892 | 0.003 | - | - | 0.969 | 0.970 | 0.578 | 1.43x | 18.2/26.2/31.3% | 1.9/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| random | 1 | 0.801 | 0.788 | 0.013 | - | - | 0.889 | 0.891 | 0.463 | 1.20x | 15.0/22.6/27.0% | 1.7/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.645 | 0.618 | 0.027 | - | - | 0.775 | 0.780 | 0.289 | 0.96x | 12.1/19.8/23.9% | 1.3/4.8% | 3 |
| 7 | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.946 | 0.947 | 0.713 | 1.32x | 16.6/23.3/28.5% | 2.0/5.3% | 3 |
| 15 | 1 | 0.918 | 0.917 | 0.001 | - | - | 0.957 | 0.957 | 0.796 | 1.37x | 17.3/23.9/29.3% | 2.1/5.4% | 3 |
| 32 | 1 | 0.929 | 0.929 | 0.000 | - | - | 0.967 | 0.967 | 0.799 | 1.37x | 17.3/24.1/29.2% | 2.1/5.4% | 3 |

> hop-limit=3: decode_failures 1

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.645 | 0.618 | 0.027 | - | - | 0.775 | 0.780 | 0.289 | 0.96x | 12.1/19.8/23.9% | 1.3/4.8% | 3 |
| 5 | 1 | 0.823 | 0.807 | 0.016 | - | - | 0.890 | 0.893 | 0.517 | 1.22x | 15.3/22.6/27.5% | 1.7/5.2% | 3 |
| 7 | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.946 | 0.947 | 0.713 | 1.32x | 16.6/23.3/28.5% | 2.0/5.3% | 3 |

> hop-limit=3: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.862 | 0.862 | 0.001 | - | - | 0.922 | 0.977 | 0.493 | 1.23x | 15.7/22.8/27.9% | 1.7/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.645 | 0.618 | 0.027 | - | - | 0.775 | 0.780 | 0.289 | 0.96x | 12.1/19.8/23.9% | 1.3/4.8% | 3 |
| True | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

> hop-spread=False: decode_failures 1

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| BALANCED | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| STRICT | 1 | 0.730 | 0.730 | 0.000 | - | - | 0.819 | 0.836 | 0.401 | 1.35x | 17.3/24.7/30.4% | 1.9/5.6% | 3 |

> signature-policy=STRICT: decode_failures 51

> slower: 4.32 s per simulated hour against 1.85 over 12 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| dm | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.959 | 0.959 | 0.516 | 1.23x | 15.7/22.9/27.9% | 1.7/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.864 | 0.858 | 0.007 | - | - | 0.956 | 0.961 | 0.535 | 1.25x | 15.9/23.1/28.3% | 1.7/5.3% | 3 |
| local | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| time | 1 | 0.863 | 0.856 | 0.007 | - | - | 0.959 | 0.963 | 0.533 | 1.29x | 16.6/24.1/29.3% | 1.8/5.5% | 3 |
| window | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.968 | 0.973 | 0.499 | 1.24x | 15.8/23.0/28.2% | 1.7/5.3% | 3 |

> bucket-mode=global: misdecodes 44

> bucket-mode=time: misdecodes 23

> bucket-mode=window: misdecodes 23

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.863 | 0.855 | 0.007 | - | - | 0.968 | 0.969 | 0.500 | 1.38x | 18.0/26.2/31.4% | 1.9/6.0% | 3 |
| 1800 | 1 | 0.863 | 0.856 | 0.007 | - | - | 0.959 | 0.963 | 0.533 | 1.29x | 16.6/24.1/29.3% | 1.8/5.5% | 3 |
| 3600 | 1 | 0.869 | 0.863 | 0.006 | - | - | 0.961 | 0.966 | 0.515 | 1.25x | 15.9/23.3/28.3% | 1.7/5.3% | 3 |

> time-bucket-s=600: misdecodes 149

> time-bucket-s=1800: misdecodes 23

> time-bucket-s=3600: misdecodes 10

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| interval | 1 | 0.852 | 0.844 | 0.009 | - | - | 0.951 | 0.961 | 0.468 | 1.67x | 22.5/32.2/37.9% | 2.3/7.5% | 3 |
| aimd | 1 | 0.866 | 0.865 | 0.001 | - | - | 0.915 | 0.966 | 0.517 | 1.24x | 16.0/23.3/28.3% | 1.7/5.3% | 3 |
| bucket+interval | 1 | 0.844 | 0.834 | 0.010 | - | - | 0.942 | 0.946 | 0.503 | 1.69x | 22.9/32.8/38.2% | 2.3/7.7% | 3 |

> trigger=interval: misdecodes 14

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 7

> trigger=bucket+interval: misdecodes 16

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.864 | 0.857 | 0.007 | - | - | 0.956 | 0.960 | 0.492 | 1.24x | 15.9/23.1/28.2% | 1.7/5.3% | 3 |
| 8 | 1 | 0.866 | 0.860 | 0.006 | - | - | 0.961 | 0.962 | 0.523 | 1.24x | 15.8/23.0/28.1% | 1.7/5.2% | 3 |
| 16 | 1 | 0.871 | 0.864 | 0.007 | - | - | 0.967 | 0.968 | 0.545 | 1.24x | 15.7/23.0/28.1% | 1.7/5.3% | 3 |
| 32 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 50 | 1 | 0.872 | 0.866 | 0.006 | - | - | 0.966 | 0.968 | 0.519 | 1.27x | 16.3/23.8/29.0% | 1.7/5.4% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 24

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.864 | 0.857 | 0.007 | - | - | 0.956 | 0.960 | 0.492 | 1.24x | 15.9/23.1/28.2% | 1.7/5.3% | 3 |
| 8 | 1 | 0.866 | 0.860 | 0.006 | - | - | 0.961 | 0.962 | 0.523 | 1.24x | 15.8/23.0/28.1% | 1.7/5.2% | 3 |
| 16 | 1 | 0.871 | 0.864 | 0.007 | - | - | 0.967 | 0.968 | 0.545 | 1.24x | 15.7/23.0/28.1% | 1.7/5.3% | 3 |
| 32 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 50 | 1 | 0.872 | 0.866 | 0.006 | - | - | 0.966 | 0.968 | 0.519 | 1.27x | 16.3/23.8/29.0% | 1.7/5.4% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 24

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.870 | 0.865 | 0.004 | - | - | 0.952 | 0.966 | 0.512 | 1.25x | 15.8/23.1/28.2% | 1.7/5.3% | 3 |
| 16 | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.971 | 0.974 | 0.515 | 1.24x | 15.8/23.1/28.2% | 1.7/5.3% | 3 |
| 32 | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.968 | 0.973 | 0.499 | 1.24x | 15.8/23.0/28.2% | 1.7/5.3% | 3 |

> capacity=8: misdecodes 28

> capacity=8: decode_failures 21

> capacity=16: misdecodes 20

> capacity=32: misdecodes 23

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.844 | 0.834 | 0.010 | - | - | 0.942 | 0.946 | 0.503 | 1.69x | 22.9/32.8/38.2% | 2.3/7.7% | 3 |
| 02-06 | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.927 | 0.961 | 0.531 | 1.27x | 16.3/23.8/29.0% | 1.7/5.4% | 3 |
| 00-08 | 1 | 0.871 | 0.867 | 0.004 | - | - | 0.943 | 0.970 | 0.518 | 1.34x | 17.4/25.5/30.6% | 1.8/5.9% | 3 |

> catch-up-hours=: misdecodes 16

> catch-up-hours=02-06: decode_failures 37

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 36

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.948 | 0.950 | 0.487 | 1.27x | 16.0/23.4/28.7% | 1.7/5.4% | 3 |
| 2 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 3 | 1 | 0.881 | 0.864 | 0.017 | - | - | 0.975 | 0.987 | 0.501 | 1.26x | 15.7/23.0/28.4% | 1.7/5.4% | 3 |
| 4 | 1 | 0.886 | 0.859 | 0.028 | - | - | 0.945 | 0.990 | 0.494 | 1.27x | 15.8/23.1/28.5% | 1.8/5.4% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 35

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.948 | 0.950 | 0.487 | 1.27x | 16.0/23.4/28.7% | 1.7/5.4% | 3 |
| 2 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 3 | 1 | 0.881 | 0.864 | 0.017 | - | - | 0.975 | 0.987 | 0.501 | 1.26x | 15.7/23.0/28.4% | 1.7/5.4% | 3 |
| 4 | 1 | 0.886 | 0.859 | 0.028 | - | - | 0.945 | 0.990 | 0.494 | 1.27x | 15.8/23.1/28.5% | 1.8/5.4% | 3 |
| 5 | 1 | 0.869 | 0.857 | 0.012 | - | - | 0.829 | 0.988 | 0.502 | 1.24x | 15.5/22.8/27.9% | 1.8/5.3% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 35

> hops-apart=5: decode_failures 29

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.957 | 0.959 | 0.519 | 1.26x | 16.1/23.4/28.7% | 1.7/5.3% | 3 |
| 30 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 120 | 1 | 0.867 | 0.860 | 0.007 | - | - | 0.962 | 0.964 | 0.517 | 1.26x | 16.1/23.4/28.7% | 1.7/5.4% | 3 |
| 600 | 1 | 0.867 | 0.861 | 0.006 | - | - | 0.954 | 0.955 | 0.517 | 1.24x | 15.8/23.0/28.1% | 1.7/5.3% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.957 | 0.959 | 0.519 | 1.26x | 16.1/23.4/28.7% | 1.7/5.3% | 3 |
| 30 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 120 | 1 | 0.867 | 0.860 | 0.007 | - | - | 0.962 | 0.964 | 0.517 | 1.26x | 16.1/23.4/28.7% | 1.7/5.4% | 3 |
| 600 | 1 | 0.867 | 0.861 | 0.006 | - | - | 0.954 | 0.955 | 0.517 | 1.24x | 15.8/23.0/28.1% | 1.7/5.3% | 3 |

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.890 | 0.863 | 0.027 | - | - | 0.861 | 0.954 | 0.527 | 1.29x | 16.4/23.8/28.9% | 1.9/5.4% | 3 |
| routers | 1 | 0.862 | 0.860 | 0.001 | - | - | 0.975 | 0.976 | 0.495 | 1.27x | 16.1/23.4/28.8% | 1.7/5.4% | 3 |
| alternate-routers | 1 | 0.862 | 0.860 | 0.003 | - | - | 0.978 | 0.978 | 0.523 | 1.25x | 15.8/22.9/28.2% | 1.7/5.4% | 3 |
| beside-router | 1 | 0.864 | 0.859 | 0.004 | - | - | 0.978 | 0.978 | 0.496 | 1.28x | 16.0/23.5/28.8% | 1.7/5.5% | 3 |
| random-clients | 1 | 0.883 | 0.857 | 0.026 | - | - | 0.978 | 0.981 | 0.521 | 1.29x | 16.2/23.6/28.9% | 1.7/5.5% | 3 |
| hops-apart | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

> place=spread: decode_failures 23

> place=random-clients: decode_failures 1

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.890 | 0.863 | 0.027 | - | - | 0.861 | 0.954 | 0.527 | 1.29x | 16.4/23.8/28.9% | 1.9/5.4% | 3 |
| routers | 1 | 0.862 | 0.860 | 0.001 | - | - | 0.975 | 0.976 | 0.495 | 1.27x | 16.1/23.4/28.8% | 1.7/5.4% | 3 |
| alternate-routers | 1 | 0.862 | 0.860 | 0.003 | - | - | 0.978 | 0.978 | 0.523 | 1.25x | 15.8/22.9/28.2% | 1.7/5.4% | 3 |
| beside-router | 1 | 0.864 | 0.859 | 0.004 | - | - | 0.978 | 0.978 | 0.496 | 1.28x | 16.0/23.5/28.8% | 1.7/5.5% | 3 |
| random-clients | 1 | 0.883 | 0.857 | 0.026 | - | - | 0.978 | 0.981 | 0.521 | 1.29x | 16.2/23.6/28.9% | 1.7/5.5% | 3 |
| hops-apart | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

> place=spread: decode_failures 23

> place=random-clients: decode_failures 1

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| broadcast | 1 | 0.877 | 0.852 | 0.025 | - | - | 0.958 | 0.959 | 0.528 | 1.32x | 17.0/24.7/30.0% | 1.8/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| heard | 1 | 0.866 | 0.858 | 0.008 | - | - | 0.964 | 0.965 | 0.509 | 1.25x | 16.0/23.4/28.6% | 1.7/5.3% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.877 | 0.852 | 0.025 | - | - | 0.958 | 0.959 | 0.528 | 1.32x | 17.0/24.7/30.0% | 1.8/5.6% | 3 |
| heard | 1 | 0.875 | 0.849 | 0.025 | - | - | 0.955 | 0.957 | 0.510 | 1.31x | 16.9/24.5/29.8% | 1.8/5.6% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| enum | 1 | 0.861 | 0.853 | 0.008 | - | - | 0.958 | 0.959 | 0.519 | 1.24x | 15.9/23.2/28.2% | 1.7/5.3% | 3 |
| hybrid | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.862 | 0.860 | 0.001 | - | - | 0.975 | 0.976 | 0.495 | 1.27x | 16.1/23.4/28.8% | 1.7/5.4% | 3 |
| 6 | 1 | 0.866 | 0.856 | 0.009 | - | - | 0.982 | 0.983 | 0.511 | 1.28x | 16.0/23.7/29.0% | 1.7/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.862 | 0.858 | 0.003 | - | - | 0.961 | 0.963 | 0.517 | 1.22x | 15.4/22.6/27.7% | 1.7/5.2% | 2 |
| 3 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 5 | 1 | 0.870 | 0.863 | 0.007 | - | - | 0.966 | 0.967 | 0.511 | 1.28x | 16.4/23.9/29.1% | 1.8/5.5% | 5 |
| 8 | 1 | 0.869 | 0.853 | 0.016 | - | - | 0.986 | 0.989 | 0.496 | 1.33x | 16.9/24.8/29.6% | 1.8/5.8% | 8 |

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.862 | 0.858 | 0.003 | - | - | 0.961 | 0.963 | 0.517 | 1.22x | 15.4/22.6/27.7% | 1.7/5.2% | 2 |
| 3 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 5 | 1 | 0.870 | 0.863 | 0.007 | - | - | 0.966 | 0.967 | 0.511 | 1.28x | 16.4/23.9/29.1% | 1.8/5.5% | 5 |
| 8 | 1 | 0.869 | 0.853 | 0.016 | - | - | 0.986 | 0.989 | 0.496 | 1.33x | 16.9/24.8/29.6% | 1.8/5.8% | 8 |

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| True | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.877 | 0.870 | 0.007 | - | - | 0.973 | 0.982 | 0.509 | 1.16x | 14.8/21.5/26.3% | 1.6/4.9% | 3 |
| 1 | 1 | 0.870 | 0.863 | 0.007 | - | - | 0.965 | 0.969 | 0.517 | 1.16x | 14.8/21.5/26.4% | 1.6/4.9% | 3 |
| 2 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.976 | 0.980 | 0.530 | 1.15x | 14.8/21.5/26.2% | 1.5/4.9% | 3 |
| 4 | 1 | 0.874 | 0.869 | 0.005 | - | - | 0.966 | 0.969 | 0.523 | 1.15x | 14.7/21.3/26.2% | 1.6/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.869 | 0.862 | 0.008 | - | - | 0.969 | 0.971 | 0.535 | 1.25x | 15.9/23.4/28.4% | 1.7/5.3% | 3 |
| 24 | 1 | 0.865 | 0.859 | 0.005 | - | - | 0.957 | 0.958 | 0.505 | 1.24x | 15.8/23.1/28.2% | 1.7/5.3% | 3 |
| 32 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.959 | 0.961 | 0.496 | 1.24x | 15.8/23.1/28.3% | 1.7/5.3% | 3 |
| 64 | 1 | 0.864 | 0.858 | 0.006 | - | - | 0.963 | 0.965 | 0.503 | 1.28x | 16.4/23.9/29.1% | 1.8/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.867 | 0.860 | 0.007 | - | - | 0.955 | 0.956 | 0.499 | 1.34x | 17.2/25.1/30.4% | 1.9/5.7% | 3 |
| 16 | 1 | 0.866 | 0.859 | 0.007 | - | - | 0.963 | 0.965 | 0.516 | 1.28x | 16.3/23.7/28.9% | 1.8/5.4% | 3 |
| 32 | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.968 | 0.973 | 0.499 | 1.24x | 15.8/23.0/28.2% | 1.7/5.3% | 3 |

> window-size=8: misdecodes 175

> window-size=16: misdecodes 76

> window-size=32: misdecodes 23

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.955 | 0.002 | - | - | 0.999 | 0.999 | 0.811 | 1.94x | 21.7/28.5/31.6% | 1.2/5.1% | 3 |
| True | 1 | 0.776 | 0.771 | 0.005 | - | - | 0.934 | 0.956 | 0.557 | 5.53x | 57.5/68.8/73.1% | 3.7/12.4% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: decode_failures 119

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.518 | 0.511 | 0.007 | - | - | 0.778 | 0.780 | 0.193 | 4.38x | 14.5/30.3/39.4% | 1.4/4.9% | 3 |
| truesize | 1 | 0.552 | 0.545 | 0.007 | - | - | 0.820 | 0.821 | 0.212 | 3.30x | 10.6/24.5/32.4% | 1.0/4.0% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.999 | 1.000 | 0.824 | 1.86x | 20.6/26.5/29.5% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.956 | 0.955 | 0.002 | - | - | 0.999 | 0.999 | 0.811 | 1.94x | 21.7/28.5/31.6% | 1.2/5.1% | 3 |

> congestion-mode=adaptive: misdecodes 1

