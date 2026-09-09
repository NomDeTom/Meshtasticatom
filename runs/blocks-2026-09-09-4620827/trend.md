# Sweep blocks-2026-09-09-4620827

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** coastal
- **seed base** 4620827 · seeds 4620827
- **blocks** 87 run
- **compute** 11.0 h of simulator time across every cell
- **generated** 2026-09-09T09:14:03+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>93 warnings</summary>

- AD-amplifiers: amplifier-mix=arms-race: misdecodes 1
- AD-siting: siting-mix=local-typical: decode_failures 10
- AD-siting: siting-mix=basement-heavy: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 34
- DB-hotstore-stress: max-num-nodes=250: decode_failures 2
- DB-platform: platform-mix=constrained: decode_failures 2
- DB-warm: warm-num-nodes=0: queue drops 15.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 118
- DB-warm: warm-num-nodes=25: queue drops 15.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 118
- DB-warm: warm-num-nodes=100: queue drops 15.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 118
- DB-warm: warm-num-nodes=2000: queue drops 15.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 118
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 10
- DG-burst: burst-loss=0.3: decode_failures 39
- DG-loss: extra-loss=0.3: decode_failures 2
- DG-outage: burst-loss=0.1: decode_failures 23
- DG-outage: burst-loss=0.2: decode_failures 30
- DG-outage: burst-loss=0.3: decode_failures 25
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 37
- DM-mode: dm-mode=m4-early-flood: decode_failures 3
- DM-mode: slower: 7.09 s per simulated hour against 3.06 over 19 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.25: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: queue drops 18.4% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 20
- LD-chatty: broadcast-interval-s=300: queue drops 13.2% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 24
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 15.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 118
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 26.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 103
- MS-density: nodes=150: misdecodes 2
- MS-oversubscribed: nodes=500: decode_failures 4
- MS-siting: siting-mix=local-typical: decode_failures 10
- MS-siting: siting-mix=event: decode_failures 17
- MS-size: nodes=150: decode_failures 2
- MS-stretch: stretch=2.0: decode_failures 2
- PR-crladder: coding-rate-ladder=False: decode_failures 37
- PR-crladder: coding-rate-ladder=True: decode_failures 5
- PR-crladder: slower: 8.25 s per simulated hour against 2.79 over 19 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 5
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 29
- RF-eu-presets: preset=SHORT_FAST: decode_failures 25
- RF-preset: preset=SHORT_FAST: decode_failures 25
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 29
- RF-preset-turbo: slower: 3.12 s per simulated hour against 1.54 over 15 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 4
- RF-txpower: tx-power=17: decode_failures 11
- RF-txpower: tx-power=14: decode_failures 4
- RT-hoplimit: hop-limit=15: misdecodes 1
- RT-hoplimit: hop-limit=32: misdecodes 1
- SC-signing: signature-policy=STRICT: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 42
- SF-bucket-mode: bucket-mode=time: misdecodes 21
- SF-bucket-mode: bucket-mode=window: misdecodes 24
- SF-bucket-time: time-bucket-s=600: misdecodes 110
- SF-bucket-time: time-bucket-s=1800: misdecodes 21
- SF-bucket-time: time-bucket-s=3600: misdecodes 9
- SF-bucket-time: time-bucket-s=3600: decode_failures 1
- SF-cadence: trigger=interval: misdecodes 11
- SF-cadence: trigger=interval: decode_failures 12
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=aimd: decode_failures 5
- SF-cadence: trigger=bucket+interval: misdecodes 18
- SF-capacity-local: capacity=4: decode_failures 101
- SF-capacity-local: capacity=8: decode_failures 40
- SF-capacity: capacity=4: decode_failures 101
- SF-capacity: capacity=8: decode_failures 40
- SF-capacity-window: capacity=8: misdecodes 27
- SF-capacity-window: capacity=8: decode_failures 37
- SF-capacity-window: capacity=16: misdecodes 17
- SF-capacity-window: capacity=16: decode_failures 1
- SF-capacity-window: capacity=32: misdecodes 24
- SF-catchup: catch-up-hours=: misdecodes 18
- SF-catchup: catch-up-hours=02-06: misdecodes 1
- SF-catchup: catch-up-hours=02-06: decode_failures 39
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 35
- SF-hops-flat: faster: 1.8 s per simulated hour against 3.8 over 19 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: faster: 1.88 s per simulated hour against 4.81 over 19 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 14
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 137
- SF-window-size: window-size=16: misdecodes 51
- SF-window-size: window-size=32: misdecodes 24
- TH-congestion: no-congestion-scaling=True: queue drops 14.8% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 113

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `PR-crladder` | 8.25 | 2.79 | 2.96x | 19 |
| `DM-mode` | 7.09 | 3.06 | 2.31x | 19 |
| `RF-preset-turbo` | 3.12 | 1.54 | 2.03x | 15 |
| `RF-eu-presets` | 3.77 | 2.03 | 1.85x | 19 |
| `RF-bw500` | 4.47 | 2.41 | 1.85x | 19 |
| `PR-dmmode-cr` | 4.26 | 2.54 | 1.68x | 19 |
| `AD-siting` | 2.42 | 1.53 | 1.58x | 19 |
| `RF-txpower` | 2.47 | 1.59 | 1.55x | 19 |
| `MS-siting` | 3.04 | 2.02 | 1.51x | 19 |
| `MS-hopscale` | 11.6 | 18.1 | 0.64x | 19 |
| `BL-control` | 1.11 | 1.75 | 0.63x | 19 |
| `SF-place-flat` | 1.47 | 2.86 | 0.51x | 19 |
| `SF-place-spread` | 1.44 | 2.86 | 0.50x | 19 |
| `SF-hops-flat` | 1.8 | 3.8 | 0.47x | 19 |
| `SF-hops-spread` | 1.88 | 4.81 | 0.39x | 19 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.992 | 0.992 | 0.896 → 0.911 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.988 | 0.988 | 0.911 → 0.911 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.094 → 0.992 | 0.898 | 0.077 → 0.910 | 12x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.149 → 0.992 | 0.843 | 0.111 → 0.910 | 8x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.064 → 0.901 | 0.837 | 0.062 → 0.890 | 5.3x advert_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.136 → 0.939 | 0.803 | 0.126 → 0.861 | 1.2e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.217 → 0.918 | 0.701 | 0.212 → 0.910 | 3.5x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.272 → 0.973 | 0.701 | 0.264 → 0.973 | 2.9x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.335 → 0.918 | 0.584 | 0.331 → 0.910 | 8.1x bytes_on_air | down | 4 |
| `RF-bw500` | preset | **text** | 0.304 → 0.878 | 0.574 | 0.292 → 0.859 | 1.9x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.480 → 0.979 | 0.499 | 0.335 → 0.807 | 5x bytes_on_air | down | 3 |
| `MS-topology` | topology | **held** | 0.580 → 0.995 | 0.415 | 0.616 → 0.967 | 2.4x sr_airtime | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.511 → 0.918 | 0.408 | 0.492 → 0.910 | 2.8x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.511 → 0.918 | 0.408 | 0.492 → 0.910 | 2.4x sr_bytes | up | 3 |
| `DG-outage` | burst-loss | **text** | 0.593 → 0.918 | 0.326 | 0.572 → 0.910 | 2x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.615 → 0.939 | 0.324 | 0.594 → 0.934 | 6.7x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.632 → 0.952 | 0.320 | 0.615 → 0.949 | 8.5x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.634 → 0.918 | 0.284 | 0.597 → 0.910 | 2.2x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.510 → 0.753 | 0.244 | 0.321 → 0.536 | 5.3x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.569 → 0.807 | 0.237 | 0.553 → 0.790 | 1.6x sr_bytes | up | 2 |
| `MS-density` | nodes | **text** | 0.753 → 0.971 | 0.218 | 0.739 → 0.969 | 5.6x sr_airtime | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.765 → 0.971 | 0.206 | 0.755 → 0.969 | 4.3x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.739 → 0.918 | 0.179 | 0.727 → 0.910 | 5.9x sr_airtime | down | 5 |
| `RF-noise` | noise-profile | **text** | 0.769 → 0.918 | 0.149 | 0.759 → 0.910 | 1.3x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.809 → 0.949 | 0.139 | 0.777 → 0.947 | 2.3x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.809 → 0.945 | 0.136 | 0.777 → 0.942 | 2.3x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.809 → 0.918 | 0.109 | 0.777 → 0.910 | 1.7x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.820 → 0.918 | 0.098 | 0.800 → 0.910 | 1.5x sr_bytes | down | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.902 → 0.992 | 0.090 | 0.910 → 0.913 | 31x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.758 → 0.833 | 0.075 | 0.667 → 0.742 | 1.4x sr_airtime | down | 2 |
| `SC-signing` | signature-policy | **text** | 0.845 → 0.918 | 0.074 | 0.845 → 0.910 | 1.2x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.873 → 0.940 | 0.067 | 0.864 → 0.937 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.873 → 0.940 | 0.066 | 0.865 → 0.937 | 2.2x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.926 → 0.992 | 0.066 | 0.888 → 0.910 | 13x advert_bytes | down | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.885 → 0.943 | 0.058 | 0.869 → 0.939 | 5.2x sr_airtime | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.918 → 0.974 | 0.056 | 0.910 → 0.972 | 1.8x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.918 → 0.972 | 0.053 | 0.910 → 0.969 | 1.9x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.901 → 0.952 | 0.051 | 0.890 → 0.949 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.901 → 0.952 | 0.051 | 0.890 → 0.949 | 2.4x bytes_on_air | up | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.946 → 0.989 | 0.042 | 0.888 → 0.915 | 9.3x advert_bytes | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.918 → 0.957 | 0.038 | 0.910 → 0.950 | 1.3x sr_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.536 → 0.571 | 0.035 | 0.525 → 0.562 | 1.4x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.885 → 0.918 | 0.034 | 0.869 → 0.910 | 1.6x sr_airtime | down | 4 |
| `FW-versions` | profile | **text** | 0.918 → 0.946 | 0.028 | 0.910 → 0.943 | 3.3x bytes_on_air | down | 5 |
| `MS-roles` | role-mix | **text** | 0.901 → 0.927 | 0.026 | 0.890 → 0.918 | 1.3x sr_bytes | down | 2 |
| `FW-firmware` | profile | **text** | 0.918 → 0.942 | 0.024 | 0.910 → 0.939 | 3.1x bytes_on_air | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.918 → 0.941 | 0.023 | 0.910 → 0.937 | 3.4x bytes_on_air | down | 2 |
| `SF-place-flat` | place | **text** | 0.908 → 0.930 | 0.022 | 0.905 → 0.913 | 2.5x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.908 → 0.930 | 0.022 | 0.905 → 0.913 | 2.5x sr_bytes | down | 6 |
| `DM-mode` | dm-mode | **held** | 0.956 → 0.978 | 0.021 | 0.880 → 0.883 | 1.1x sr_airtime | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.918 → 0.940 | 0.021 | 0.901 → 0.910 | 3x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.777 → 0.798 | 0.021 | 0.765 → 0.792 | 1.1x sr_bytes | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.903 → 0.921 | 0.018 | 0.900 → 0.915 | 2.1x bytes_on_air | down | 4 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.956 → 0.974 | 0.018 | 0.883 → 0.888 | 1.1x sr_airtime | up | 2 |
| `FW-mixed` | legacy-fraction | **held** | 0.978 → 0.995 | 0.017 | 0.900 → 0.913 | 2.1x bytes_on_air | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.918 → 0.935 | 0.016 | 0.910 → 0.928 | 1.3x sr_bytes | down | 3 |
| `AD-badrouters` | role-placement | **text** | 0.896 → 0.907 | 0.011 | 0.879 → 0.893 | 1.3x sr_bytes | down | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.909 → 0.919 | 0.010 | 0.900 → 0.910 | 5.3x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.918 → 0.929 | 0.010 | 0.910 → 0.924 | 1.3x bytes_on_air | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.929 → 0.939 | 0.009 | 0.925 → 0.937 | 1.1x sr_bytes | up | 2 |
| `SF-hops-flat` | hops-apart | **text** | 0.913 → 0.922 | 0.009 | 0.903 → 0.912 | 2.3x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.913 → 0.922 | 0.009 | 0.903 → 0.912 | 2.3x sr_bytes | up | 5 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.962 → 0.971 | 0.009 | 0.960 → 0.969 | 1.2x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.977 → 0.986 | 0.009 | 0.906 → 0.910 | 2.4x sr_bytes | up | 2 |
| `SF-capacity-window` | capacity | **text** | 0.916 → 0.925 | 0.008 | 0.906 → 0.918 | 2.5x advert_bytes | down | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.974 → 0.982 | 0.008 | 0.888 → 0.889 | 1x sr_bytes | up | 2 |
| `SF-capacity` | capacity | **text** | 0.917 → 0.925 | 0.008 | 0.908 → 0.917 | 5.4x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.917 → 0.925 | 0.008 | 0.908 → 0.917 | 5.4x advert_bytes | down | 5 |
| `RT-hopassign` | hop-assign | **text** | 0.918 → 0.926 | 0.008 | 0.910 → 0.919 | 1.1x advert_bytes | up | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.914 → 0.921 | 0.007 | 0.904 → 0.912 | 1.1x sr_bytes | down | 4 |
| `SF-window-size` | window-size | **held** | 0.986 → 0.992 | 0.007 | 0.905 → 0.908 | 4x advert_bytes | down | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.991 → 0.997 | 0.006 | 0.931 → 0.936 | 1.2x sr_bytes | down | 2 |
| `SF-resolve` | resolve | **text** | 0.918 → 0.924 | 0.006 | 0.910 → 0.915 | 5.8x advert_bytes | = | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.934 → 0.940 | 0.006 | 0.898 → 0.901 | 1x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.986 → 0.992 | 0.006 | 0.908 → 0.916 | 2.4x advert_bytes | up | 4 |
| `SF-servers-flat` | servers | **text** | 0.918 → 0.924 | 0.005 | 0.904 → 0.913 | 6.6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **text** | 0.918 → 0.924 | 0.005 | 0.904 → 0.913 | 6.6x sr_bytes | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.988 → 0.993 | 0.005 | 0.910 → 0.913 | 3.1x advert_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.917 → 0.921 | 0.004 | 0.907 → 0.912 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.917 → 0.921 | 0.004 | 0.907 → 0.912 | 1.1x sr_airtime | up | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.988 → 0.992 | 0.004 | 0.904 → 0.910 | 2.8x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.918 → 0.922 | 0.003 | 0.910 → 0.912 | 1x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.918 → 0.922 | 0.003 | 0.910 → 0.911 | 1x bytes_on_air | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.970 → 0.971 | 0.001 | 0.968 → 0.969 | 1.1x sr_bytes | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.970 → 0.971 | 0.001 | 0.968 → 0.969 | 1.1x sr_bytes | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario coastal`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| sprinkled | 1 | 0.948 | 0.946 | 0.002 | - | - | 0.986 | 0.986 | 0.742 | 1.11x | 19.5/26.0/27.9% | 1.5/5.2% | 3 |
| arms-race | 1 | 0.972 | 0.969 | 0.003 | - | - | 0.998 | 0.998 | 0.851 | 0.99x | 23.5/28.8/31.8% | 1.3/5.4% | 3 |

> amplifier-mix=arms-race: misdecodes 1

### `AD-amplify-worst` - amplify-worst  `--scenario coastal`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.941 | 0.935 | 0.006 | - | - | 0.994 | 0.995 | 0.877 | 1.16x | 19.8/24.5/26.8% | 1.6/5.0% | 3 |
| 0.3 | 1 | 0.974 | 0.972 | 0.002 | - | - | 0.999 | 1.000 | 0.921 | 0.81x | 21.7/25.7/27.9% | 0.9/5.1% | 3 |

### `AD-badrouters` - role-placement  `--scenario coastal`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.901 | 0.890 | 0.011 | - | - | 0.980 | 0.981 | 0.436 | 1.20x | 17.8/24.5/28.6% | 1.9/5.5% | 3 |
| inverse | 1 | 0.907 | 0.893 | 0.013 | - | - | 0.987 | 0.989 | 0.675 | 1.15x | 16.1/21.0/24.5% | 2.0/4.2% | 3 |
| random | 1 | 0.896 | 0.879 | 0.017 | - | - | 0.990 | 0.992 | 0.280 | 1.10x | 15.8/20.6/26.6% | 1.7/5.2% | 3 |

### `AD-flooding` - role-mix  `--scenario coastal`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.901 | 0.890 | 0.011 | - | - | 0.980 | 0.981 | 0.436 | 1.20x | 17.8/24.5/28.6% | 1.9/5.5% | 3 |
| all-routers | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.993 | 0.994 | 0.891 | 2.94x | 36.6/45.6/50.2% | 4.8/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario coastal`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.901 | 0.890 | 0.011 | - | - | 0.980 | 0.981 | 0.436 | 1.20x | 17.8/24.5/28.6% | 1.9/5.5% | 3 |
| no-mute | 1 | 0.926 | 0.918 | 0.007 | - | - | 0.993 | 0.993 | 0.639 | 1.32x | 18.7/24.2/29.3% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.993 | 0.994 | 0.891 | 2.94x | 36.6/45.6/50.2% | 4.8/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario coastal`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.901 | 0.890 | 0.011 | - | - | 0.980 | 0.981 | 0.436 | 1.20x | 17.8/24.5/28.6% | 1.9/5.5% | 3 |
| local-typical | 1 | 0.693 | 0.689 | 0.004 | - | - | 0.739 | 0.866 | 0.000 | 1.24x | 16.2/23.5/31.5% | 2.1/5.3% | 3 |
| basement-heavy | 1 | 0.064 | 0.062 | 0.002 | - | - | 0.195 | 0.200 | 0.000 | 0.48x | 0.5/5.7/9.1% | 0.2/2.6% | 3 |

> siting-mix=local-typical: decode_failures 10

> siting-mix=basement-heavy: decode_failures 1

### `AD-worst` - role-placement  `--scenario coastal`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.798 | 0.792 | 0.006 | - | - | 0.930 | 0.931 | 0.000 | 2.52x | 16.4/32.2/38.1% | 1.9/5.6% | 3 |
| inverse | 1 | 0.777 | 0.765 | 0.012 | - | - | 0.935 | 0.935 | 0.000 | 2.40x | 14.3/27.4/33.5% | 1.9/3.8% | 3 |

### `BL-control` - protocol  `--scenario coastal`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.911 | 0.911 | 0.000 | - | - | 0 | 0.000 | 0.572 | 1.27x | 18.1/24.1/28.4% | 1.9/5.0% | 3 |
| sr | 1 | 0.922 | 0.911 | 0.011 | - | - | 0.988 | 0.989 | 0.559 | 1.31x | 18.7/24.9/29.3% | 2.0/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario coastal`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.873 | 0.864 | 0.009 | - | - | 0.964 | 0.965 | 0.604 | 3.19x | 45.0/55.7/63.8% | 4.4/10.7% | 3 |
| 100 | 1 | 0.940 | 0.937 | 0.003 | - | - | 0.988 | 0.989 | 0.640 | 1.52x | 22.5/28.7/34.2% | 2.0/5.3% | 3 |
| 120 | 1 | 0.940 | 0.937 | 0.003 | - | - | 0.988 | 0.989 | 0.640 | 1.52x | 22.5/28.7/34.2% | 2.0/5.3% | 3 |
| 250 | 1 | 0.940 | 0.937 | 0.003 | - | - | 0.988 | 0.989 | 0.640 | 1.52x | 22.5/28.7/34.2% | 2.0/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario coastal`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.328 | 0.321 | 0.007 | - | - | 0.510 | 0.529 | 0.169 | 11.74x | 43.8/58.4/67.0% | 4.0/11.9% | 3 |
| 120 | 1 | 0.536 | 0.525 | 0.011 | - | - | 0.749 | 0.750 | 0.252 | 4.41x | 17.4/25.7/31.1% | 1.5/5.4% | 3 |
| 250 | 1 | 0.547 | 0.536 | 0.010 | - | - | 0.753 | 0.754 | 0.258 | 4.22x | 16.5/24.7/29.5% | 1.4/5.2% | 3 |

> max-num-nodes=10: decode_failures 34

> max-num-nodes=250: decode_failures 2

### `DB-platform` - platform-mix  `--scenario coastal`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.940 | 0.937 | 0.003 | - | - | 0.988 | 0.989 | 0.640 | 1.52x | 22.5/28.7/34.2% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.940 | 0.937 | 0.003 | - | - | 0.988 | 0.989 | 0.640 | 1.52x | 22.5/28.7/34.2% | 2.0/5.3% | 3 |
| constrained | 1 | 0.873 | 0.865 | 0.009 | - | - | 0.968 | 0.969 | 0.633 | 3.19x | 44.9/55.6/63.9% | 4.4/10.6% | 3 |

> platform-mix=constrained: decode_failures 2

### `DB-warm` - warm-num-nodes  `--scenario coastal`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.751 | 0.742 | 0.010 | - | - | 0.833 | 0.885 | 0.592 | 5.50x | 60.7/74.2/78.1% | 4.0/11.8% | 3 |
| 25 | 1 | 0.751 | 0.742 | 0.010 | - | - | 0.833 | 0.885 | 0.592 | 5.50x | 60.7/74.2/78.1% | 4.0/11.8% | 3 |
| 100 | 1 | 0.751 | 0.742 | 0.010 | - | - | 0.833 | 0.885 | 0.592 | 5.50x | 60.7/74.2/78.1% | 4.0/11.8% | 3 |
| 2000 | 1 | 0.751 | 0.742 | 0.010 | - | - | 0.833 | 0.885 | 0.592 | 5.50x | 60.7/74.2/78.1% | 4.0/11.8% | 3 |

> warm-num-nodes=0: queue drops 15.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 118

> warm-num-nodes=25: queue drops 15.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 118

> warm-num-nodes=100: queue drops 15.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 118

> warm-num-nodes=2000: queue drops 15.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 118

### `DG-burst` - burst-loss  `--scenario coastal`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.830 | 0.809 | 0.021 | - | - | 0.971 | 0.976 | 0.581 | 1.26x | 18.2/24.5/28.9% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.743 | 0.711 | 0.032 | - | - | 0.927 | 0.951 | 0.518 | 1.19x | 17.4/23.2/27.8% | 1.8/4.4% | 3 |
| 0.3 | 1 | 0.634 | 0.597 | 0.037 | - | - | 0.793 | 0.883 | 0.409 | 1.09x | 16.2/21.9/26.5% | 1.7/4.0% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 10

> burst-loss=0.3: decode_failures 39

### `DG-loss` - extra-loss  `--scenario coastal`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.895 | 0.884 | 0.011 | - | - | 0.980 | 0.984 | 0.569 | 1.40x | 20.0/26.6/31.2% | 2.2/5.3% | 3 |
| 0.2 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.968 | 0.975 | 0.549 | 1.46x | 20.9/27.5/32.7% | 2.2/5.2% | 3 |
| 0.3 | 1 | 0.820 | 0.800 | 0.021 | - | - | 0.946 | 0.964 | 0.499 | 1.52x | 21.9/28.8/34.3% | 2.4/5.1% | 3 |

> extra-loss=0.3: decode_failures 2

### `DG-outage` - burst-loss  `--scenario coastal`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.815 | 0.798 | 0.017 | - | - | 0.936 | 0.976 | 0.526 | 1.27x | 18.4/24.3/28.8% | 1.9/4.9% | 3 |
| 0.2 | 1 | 0.718 | 0.695 | 0.024 | - | - | 0.894 | 0.967 | 0.432 | 1.21x | 17.6/23.9/28.4% | 1.8/4.9% | 3 |
| 0.3 | 1 | 0.593 | 0.572 | 0.020 | - | - | 0.683 | 0.862 | 0.384 | 1.12x | 16.6/22.0/26.9% | 1.7/4.0% | 3 |

> burst-loss=0.1: decode_failures 23

> burst-loss=0.2: decode_failures 30

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario coastal`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.880 | 0.880 | 0.000 | - | - | 0.978 | 0.984 | 0.529 | 1.82x | 25.7/34.2/39.9% | 2.7/7.0% | 3 |
| directed-with-late-flood | 1 | 0.883 | 0.883 | 0.000 | - | - | 0.956 | 0.984 | 0.529 | 1.64x | 23.5/31.4/36.8% | 2.4/6.4% | 3 |
| m4-early-flood | 1 | 0.880 | 0.880 | 0.000 | - | - | 0.973 | 0.987 | 0.540 | 1.65x | 23.5/31.5/37.0% | 2.4/6.6% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 37

> dm-mode=m4-early-flood: decode_failures 3

> slower: 7.09 s per simulated hour against 3.06 over 19 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario coastal`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.942 | 0.939 | 0.004 | - | - | 0.996 | 0.996 | 0.708 | 0.75x | 10.0/12.8/14.3% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario coastal`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.906 | 0.902 | 0.004 | - | - | 0.978 | 0.979 | 0.738 | 1.19x | 16.1/21.9/25.0% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.918 | 0.913 | 0.006 | - | - | 0.995 | 0.995 | 0.522 | 1.08x | 15.2/20.7/22.6% | 1.6/4.4% | 3 |
| 0.75 | 1 | 0.902 | 0.900 | 0.003 | - | - | 0.983 | 0.984 | 0.277 | 0.86x | 12.3/14.6/17.6% | 1.4/3.0% | 3 |

> legacy-fraction=0.25: misdecodes 1

### `FW-mixed-26` - legacy-fraction  `--scenario coastal`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.907 | 0.903 | 0.004 | - | - | 0.986 | 0.986 | 0.735 | 1.17x | 15.9/21.0/24.4% | 1.8/4.6% | 3 |
| 0.5 | 1 | 0.921 | 0.915 | 0.005 | - | - | 0.996 | 0.996 | 0.547 | 1.04x | 14.8/20.5/22.3% | 1.6/4.4% | 3 |
| 0.75 | 1 | 0.903 | 0.900 | 0.002 | - | - | 0.981 | 0.981 | 0.272 | 0.84x | 12.4/14.8/18.0% | 1.3/3.0% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario coastal`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.941 | 0.937 | 0.004 | - | - | 0.996 | 0.997 | 0.618 | 0.69x | 10.2/13.7/16.6% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `FW-versions` - profile  `--scenario coastal`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.997 | 0.997 | 0.700 | 0.74x | 10.9/13.3/16.1% | 1.1/2.5% | 3 |
| 2.5 | 1 | 0.943 | 0.939 | 0.003 | - | - | 0.995 | 0.997 | 0.744 | 0.74x | 10.7/13.2/15.7% | 1.1/2.5% | 3 |
| 2.6 | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.999 | 1.000 | 0.712 | 0.71x | 10.6/13.0/15.8% | 1.0/2.5% | 3 |
| 2.7 | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.996 | 0.996 | 0.692 | 0.72x | 11.0/13.8/16.7% | 0.9/3.1% | 3 |
| 2.8 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.939 | 0.934 | 0.005 | - | - | 0.993 | 0.996 | 0.619 | 0.87x | 12.5/16.6/19.6% | 1.3/3.6% | 3 |
| 900 | 1 | 0.885 | 0.869 | 0.016 | - | - | 0.982 | 0.982 | 0.580 | 2.15x | 30.4/40.4/47.1% | 3.2/8.6% | 3 |
| 300 | 1 | 0.615 | 0.594 | 0.021 | - | - | 0.800 | 0.875 | 0.454 | 4.72x | 61.2/73.0/79.4% | 7.2/16.4% | 3 |

> broadcast-interval-s=300: queue drops 13.2% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 24

### `LD-chatty-hops` - broadcast-interval-s  `--scenario coastal`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.952 | 0.949 | 0.002 | - | - | 0.991 | 0.991 | 0.627 | 0.96x | 13.4/17.6/20.6% | 1.4/3.6% | 3 |
| 900 | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.977 | 0.978 | 0.582 | 2.31x | 32.2/42.4/49.0% | 3.4/8.8% | 3 |
| 300 | 1 | 0.632 | 0.615 | 0.017 | - | - | 0.775 | 0.821 | 0.349 | 5.17x | 64.9/74.9/80.1% | 8.2/16.9% | 3 |

> broadcast-interval-s=300: queue drops 18.4% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 20

### `LD-diurnal` - diurnal  `--scenario coastal`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.935 | 0.928 | 0.007 | - | - | 0.996 | 0.996 | 0.622 | 1.20x | 17.5/23.4/27.6% | 1.8/5.0% | 3 |
| sinusoid | 1 | 0.929 | 0.922 | 0.007 | - | - | 0.994 | 0.996 | 0.606 | 1.19x | 16.9/22.5/26.5% | 1.8/4.8% | 3 |
| commuter | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.885 | 0.869 | 0.016 | - | - | 0.982 | 0.982 | 0.580 | 2.15x | 30.4/40.4/47.1% | 3.2/8.6% | 3 |
| 3600 | 1 | 0.939 | 0.934 | 0.005 | - | - | 0.993 | 0.996 | 0.619 | 0.87x | 12.5/16.6/19.6% | 1.3/3.6% | 3 |
| 10800 | 1 | 0.941 | 0.937 | 0.004 | - | - | 0.994 | 0.996 | 0.615 | 0.60x | 8.4/11.0/13.2% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.997 | 0.998 | 0.627 | 0.44x | 6.3/8.2/9.7% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario coastal`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.917 | 0.906 | 0.011 | - | - | 0.990 | 0.991 | 0.594 | 1.39x | 19.9/26.7/31.2% | 2.1/5.7% | 3 |
| 1.0 | 1 | 0.908 | 0.897 | 0.011 | - | - | 0.990 | 0.990 | 0.617 | 1.56x | 22.2/29.8/35.1% | 2.3/6.3% | 3 |
| 4.0 | 1 | 0.885 | 0.869 | 0.015 | - | - | 0.979 | 0.984 | 0.556 | 1.97x | 28.4/38.5/45.3% | 2.9/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario coastal`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.751 | 0.742 | 0.010 | - | - | 0.833 | 0.885 | 0.592 | 5.50x | 60.7/74.2/78.1% | 4.0/11.8% | 3 |
| 1.0 | 1 | 0.677 | 0.667 | 0.009 | - | - | 0.758 | 0.817 | 0.522 | 6.05x | 64.5/76.3/79.5% | 4.5/13.0% | 3 |

> traceroute-per-hour=0.0: queue drops 15.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 118

> traceroute-per-hour=1.0: queue drops 26.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 103

### `MS-density` - nodes  `--scenario coastal`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.753 | 0.739 | 0.014 | - | - | 0.859 | 0.864 | 0.384 | 1.54x | 23.5/29.1/37.2% | 3.6/7.2% | 3 |
| 60 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 90 | 1 | 0.959 | 0.955 | 0.004 | - | - | 0.996 | 0.996 | 0.775 | 1.65x | 20.7/29.7/33.6% | 1.5/5.1% | 3 |
| 120 | 1 | 0.971 | 0.969 | 0.002 | - | - | 0.999 | 0.999 | 0.906 | 1.92x | 23.4/34.6/38.4% | 1.3/4.9% | 3 |
| 150 | 1 | 0.971 | 0.969 | 0.002 | - | - | 1.000 | 1.000 | 0.882 | 2.50x | 28.8/40.9/45.9% | 1.2/5.6% | 3 |

> nodes=150: misdecodes 2

### `MS-hopscale` - nodes  `--scenario coastal`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 120 | 1 | 0.812 | 0.803 | 0.010 | - | - | 0.980 | 0.981 | 0.565 | 2.08x | 15.0/21.5/26.7% | 1.5/5.0% | 3 |
| 250 | 1 | 0.540 | 0.529 | 0.011 | - | - | 0.743 | 0.744 | 0.254 | 4.79x | 18.9/27.4/33.6% | 1.6/5.7% | 3 |
| 500 | 1 | 0.335 | 0.331 | 0.004 | - | - | 0.473 | 0.474 | 0.094 | 10.39x | 20.2/30.9/47.5% | 1.8/6.6% | 3 |

### `MS-oversubscribed` - nodes  `--scenario coastal`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.817 | 0.807 | 0.010 | - | - | 0.979 | 0.981 | 0.562 | 1.92x | 13.9/19.7/24.6% | 1.4/4.5% | 3 |
| 250 | 1 | 0.536 | 0.525 | 0.011 | - | - | 0.749 | 0.750 | 0.252 | 4.41x | 17.4/25.7/31.1% | 1.5/5.4% | 3 |
| 500 | 1 | 0.339 | 0.335 | 0.004 | - | - | 0.480 | 0.482 | 0.099 | 9.51x | 18.5/28.5/43.6% | 1.6/6.0% | 3 |

> nodes=500: decode_failures 4

### `MS-roles` - role-mix  `--scenario coastal`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.927 | 0.918 | 0.009 | - | - | 0.995 | 0.995 | 0.609 | 1.34x | 19.1/25.6/29.9% | 2.0/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.901 | 0.890 | 0.011 | - | - | 0.980 | 0.981 | 0.436 | 1.20x | 17.8/24.5/28.6% | 1.9/5.5% | 3 |

### `MS-roles-fav` - role-mix  `--scenario coastal`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.942 | 0.936 | 0.006 | - | - | 0.997 | 0.998 | 0.619 | 1.36x | 19.4/25.3/29.9% | 2.1/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.936 | 0.931 | 0.005 | - | - | 0.991 | 0.992 | 0.534 | 1.40x | 20.6/27.5/33.3% | 2.4/5.5% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario coastal`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.05 | 1 | 0.927 | 0.922 | 0.004 | - | - | 0.987 | 0.987 | 0.670 | 1.43x | 21.0/27.0/32.5% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.928 | 0.923 | 0.005 | - | - | 0.992 | 0.992 | 0.648 | 1.54x | 23.7/30.4/36.9% | 2.3/5.2% | 3 |
| 0.2 | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.988 | 0.989 | 0.651 | 1.78x | 26.8/39.2/46.9% | 2.4/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario coastal`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| local-typical | 1 | 0.677 | 0.670 | 0.006 | - | - | 0.727 | 0.861 | 0.000 | 1.48x | 18.2/27.9/34.5% | 2.3/5.4% | 3 |
| event | 1 | 0.272 | 0.264 | 0.008 | - | - | 0.453 | 0.470 | 0.000 | 1.61x | 9.3/16.1/20.9% | 2.6/4.8% | 3 |
| backbone | 1 | 0.973 | 0.973 | 0.001 | - | - | 0.999 | 1.000 | 0.618 | 1.00x | 28.7/34.1/36.1% | 1.1/5.4% | 3 |

> siting-mix=local-typical: decode_failures 10

> siting-mix=event: decode_failures 17

### `MS-size` - nodes  `--scenario coastal`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.884 | 0.877 | 0.007 | - | - | 0.961 | 0.966 | 0.374 | 1.50x | 26.3/34.7/38.1% | 3.4/7.9% | 3 |
| 60 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 90 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.982 | 0.983 | 0.674 | 1.58x | 15.3/21.7/26.0% | 1.5/4.9% | 3 |
| 120 | 1 | 0.812 | 0.803 | 0.010 | - | - | 0.980 | 0.981 | 0.565 | 2.08x | 15.0/21.5/26.7% | 1.5/5.0% | 3 |
| 150 | 1 | 0.739 | 0.727 | 0.012 | - | - | 0.947 | 0.950 | 0.422 | 2.79x | 17.3/26.2/34.3% | 1.5/5.3% | 3 |

> nodes=150: decode_failures 2

### `MS-stretch` - stretch  `--scenario coastal`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 1.25 | 1 | 0.793 | 0.775 | 0.018 | - | - | 0.913 | 0.915 | 0.370 | 1.36x | 14.9/21.7/24.8% | 2.1/4.9% | 3 |
| 1.5 | 1 | 0.569 | 0.553 | 0.017 | - | - | 0.804 | 0.805 | 0.218 | 1.45x | 11.2/19.5/22.6% | 2.2/5.2% | 3 |
| 2.0 | 1 | 0.217 | 0.212 | 0.005 | - | - | 0.463 | 0.478 | 0.000 | 1.30x | 7.1/14.5/17.0% | 2.1/5.0% | 3 |

> stretch=2.0: decode_failures 2

### `MS-topology` - topology  `--scenario coastal`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| clustered | 1 | 0.941 | 0.941 | 0.000 | - | - | 0.969 | 0.970 | 0.656 | 1.07x | 30.0/35.8/36.8% | 1.3/5.5% | 3 |
| corridor | 1 | 0.628 | 0.616 | 0.012 | - | - | 0.580 | 0.582 | 0.344 | 1.29x | 16.7/21.3/24.7% | 1.9/4.7% | 3 |
| hub | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.995 | 0.995 | 0.815 | 1.20x | 29.3/37.1/38.3% | 1.5/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario coastal`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.883 | 0.883 | 0.000 | - | - | 0.956 | 0.984 | 0.529 | 1.64x | 23.5/31.4/36.8% | 2.4/6.4% | 3 |
| True | 1 | 0.888 | 0.888 | 0.000 | - | - | 0.974 | 0.987 | 0.507 | 1.67x | 23.9/31.9/37.4% | 2.5/6.6% | 3 |

> coding-rate-ladder=False: decode_failures 37

> coding-rate-ladder=True: decode_failures 5

> slower: 8.25 s per simulated hour against 2.79 over 19 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario coastal`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.888 | 0.888 | 0.000 | - | - | 0.974 | 0.987 | 0.507 | 1.67x | 23.9/31.9/37.4% | 2.5/6.6% | 3 |
| m4-early-flood | 1 | 0.889 | 0.889 | 0.000 | - | - | 0.982 | 0.992 | 0.512 | 1.65x | 23.5/31.6/36.9% | 2.4/6.5% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 5

> dm-mode=m4-early-flood: decode_failures 1

### `PR-protocol` - protocol  `--scenario coastal`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.911 | 0.911 | 0.000 | - | - | 0 | 0.000 | 0.572 | 1.27x | 18.1/24.1/28.4% | 1.9/5.0% | 3 |
| chain | 1 | 0.899 | 0.896 | 0.002 | - | - | 0.910 | 0.991 | 0.549 | 1.55x | 22.0/29.1/34.0% | 2.4/6.0% | 3 |
| sr | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario coastal`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| True | 1 | 0.922 | 0.911 | 0.010 | - | - | 0.992 | 0.993 | 0.632 | 1.33x | 18.9/25.1/29.4% | 2.0/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario coastal`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.971 | 0.969 | 0.002 | - | - | 0.999 | 0.999 | 0.906 | 1.92x | 23.4/34.6/38.4% | 1.3/4.9% | 3 |
| True | 1 | 0.970 | 0.968 | 0.002 | - | - | 0.998 | 0.998 | 0.916 | 1.96x | 23.7/34.9/38.8% | 1.3/5.0% | 3 |

### `RF-bw500` - preset  `--scenario coastal`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.304 | 0.292 | 0.012 | - | - | 0.544 | 0.599 | 0.000 | 0.07x | 0.4/1.0/1.2% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.618 | 0.608 | 0.009 | - | - | 0.888 | 0.889 | 0.188 | 0.33x | 2.9/4.9/5.8% | 0.5/1.4% | 3 |
| LONG_TURBO | 1 | 0.878 | 0.859 | 0.019 | - | - | 0.970 | 0.971 | 0.443 | 1.30x | 14.7/21.9/24.6% | 1.9/4.8% | 3 |

> preset=SHORT_TURBO: decode_failures 29

### `RF-duct` - duct-per-hour  `--scenario coastal`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.926 | 0.915 | 0.011 | - | - | 0.993 | 0.994 | 0.660 | 1.22x | 20.5/26.6/30.5% | 1.8/5.4% | 3 |
| 1.0 | 1 | 0.957 | 0.950 | 0.007 | - | - | 0.994 | 0.995 | 0.811 | 1.00x | 25.9/31.2/33.8% | 1.4/5.6% | 3 |

### `RF-eu-presets` - preset  `--scenario coastal`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.511 | 0.492 | 0.019 | - | - | 0.715 | 0.770 | 0.000 | 0.19x | 1.4/2.5/3.0% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| LITE_FAST | 1 | 0.883 | 0.876 | 0.007 | - | - | 0.980 | 0.982 | 0.405 | 0.99x | 13.0/17.4/22.3% | 1.5/4.0% | 3 |
| NARROW_SLOW | 1 | 0.901 | 0.888 | 0.013 | - | - | 0.987 | 0.987 | 0.391 | 1.27x | 17.6/22.5/28.6% | 2.0/5.1% | 3 |

> preset=SHORT_FAST: decode_failures 25

### `RF-noise` - noise-profile  `--scenario coastal`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| temporal | 1 | 0.859 | 0.843 | 0.015 | - | - | 0.967 | 0.970 | 0.490 | 1.34x | 18.6/24.5/29.1% | 2.0/5.3% | 3 |
| transient | 1 | 0.910 | 0.900 | 0.011 | - | - | 0.987 | 0.988 | 0.594 | 1.33x | 18.8/24.9/29.3% | 2.0/5.4% | 3 |
| periodic | 1 | 0.769 | 0.759 | 0.010 | - | - | 0.843 | 0.849 | 0.483 | 1.25x | 17.9/23.6/28.0% | 1.9/4.7% | 3 |

### `RF-preset` - preset  `--scenario coastal`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.511 | 0.492 | 0.019 | - | - | 0.715 | 0.770 | 0.000 | 0.19x | 1.4/2.5/3.0% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| LONG_MODERATE | 1 | 0.865 | 0.853 | 0.012 | - | - | 0.951 | 0.955 | 0.651 | 3.37x | 52.4/65.9/68.4% | 4.8/12.6% | 3 |

> preset=SHORT_FAST: decode_failures 25

### `RF-preset-turbo` - preset  `--scenario coastal`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.077 | 0.077 | 0.001 | - | - | 0.094 | 0.121 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.304 | 0.292 | 0.012 | - | - | 0.544 | 0.599 | 0.000 | 0.07x | 0.4/1.0/1.2% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| LONG_TURBO | 1 | 0.878 | 0.859 | 0.019 | - | - | 0.970 | 0.971 | 0.443 | 1.30x | 14.7/21.9/24.6% | 1.9/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.905 | 0.895 | 0.011 | - | - | 0.981 | 0.982 | 0.617 | 1.82x | 24.4/31.2/36.6% | 2.7/6.8% | 3 |

> preset=SHORT_TURBO: decode_failures 29

> slower: 3.12 s per simulated hour against 1.54 over 15 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario coastal`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.870 | 0.861 | 0.009 | - | - | 0.939 | 0.942 | 0.545 | 1.25x | 18.1/24.0/28.2% | 1.9/5.0% | 3 |
| 10000 | 1 | 0.769 | 0.759 | 0.010 | - | - | 0.843 | 0.849 | 0.483 | 1.25x | 17.9/23.6/28.0% | 1.9/4.7% | 3 |
| 4000 | 1 | 0.510 | 0.505 | 0.006 | - | - | 0.541 | 0.597 | 0.290 | 1.09x | 15.9/20.7/25.0% | 1.7/3.5% | 3 |
| 2000 | 1 | 0.126 | 0.126 | 0.000 | - | - | 0.136 | 0.210 | 0.059 | 0.75x | 11.3/14.8/18.5% | 1.2/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 4

### `RF-stretch-duct` - duct-per-hour  `--scenario coastal`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.569 | 0.553 | 0.017 | - | - | 0.804 | 0.805 | 0.218 | 1.45x | 11.2/19.5/22.6% | 2.2/5.2% | 3 |
| 1.0 | 1 | 0.807 | 0.790 | 0.017 | - | - | 0.911 | 0.914 | 0.597 | 1.07x | 19.0/24.9/26.5% | 1.5/5.1% | 3 |

### `RF-txpower` - tx-power  `--scenario coastal`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 22 | 1 | 0.560 | 0.545 | 0.015 | - | - | 0.801 | 0.805 | 0.233 | 1.39x | 11.8/16.0/19.7% | 2.1/5.3% | 3 |
| 17 | 1 | 0.255 | 0.245 | 0.010 | - | - | 0.461 | 0.504 | 0.000 | 1.38x | 7.7/16.0/18.5% | 2.2/5.4% | 3 |
| 14 | 1 | 0.112 | 0.111 | 0.001 | - | - | 0.149 | 0.162 | 0.000 | 0.89x | 4.4/7.3/10.4% | 1.5/3.0% | 3 |

> tx-power=17: decode_failures 11

> tx-power=14: decode_failures 4

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario coastal`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.971 | 0.969 | 0.002 | - | - | 0.999 | 0.999 | 0.906 | 1.92x | 23.4/34.6/38.4% | 1.3/4.9% | 3 |
| True | 1 | 0.962 | 0.960 | 0.003 | - | - | 0.995 | 0.996 | 0.891 | 2.31x | 27.6/39.7/43.7% | 1.6/5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario coastal`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.929 | 0.925 | 0.005 | - | - | 0.993 | 0.994 | 0.607 | 1.36x | 19.9/25.3/30.8% | 1.8/5.2% | 3 |
| True | 1 | 0.939 | 0.937 | 0.002 | - | - | 0.990 | 0.990 | 0.610 | 1.46x | 21.2/26.7/32.3% | 2.0/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario coastal`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| random | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.993 | 0.994 | 0.578 | 1.27x | 18.2/24.5/28.8% | 2.0/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario coastal`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.809 | 0.777 | 0.032 | - | - | 0.978 | 0.984 | 0.498 | 0.99x | 14.7/20.5/24.6% | 1.5/4.5% | 3 |
| 7 | 1 | 0.945 | 0.942 | 0.003 | - | - | 0.986 | 0.988 | 0.610 | 1.47x | 20.4/27.0/31.4% | 2.2/5.7% | 3 |
| 15 | 1 | 0.949 | 0.947 | 0.001 | - | - | 0.984 | 0.985 | 0.638 | 1.46x | 20.2/26.8/31.2% | 2.2/5.5% | 3 |
| 32 | 1 | 0.949 | 0.947 | 0.001 | - | - | 0.984 | 0.985 | 0.638 | 1.46x | 20.2/26.8/31.2% | 2.2/5.5% | 3 |

> hop-limit=15: misdecodes 1

> hop-limit=32: misdecodes 1

### `RT-hopspread` - hop-limit  `--scenario coastal`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.809 | 0.777 | 0.032 | - | - | 0.978 | 0.984 | 0.498 | 0.99x | 14.7/20.5/24.6% | 1.5/4.5% | 3 |
| 5 | 1 | 0.919 | 0.913 | 0.007 | - | - | 0.987 | 0.989 | 0.573 | 1.35x | 19.2/25.5/30.0% | 2.0/5.4% | 3 |
| 7 | 1 | 0.945 | 0.942 | 0.003 | - | - | 0.986 | 0.988 | 0.610 | 1.47x | 20.4/27.0/31.4% | 2.2/5.7% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario coastal`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.913 | 0.913 | 0.000 | - | - | 0.902 | 0.991 | 0.558 | 1.25x | 18.0/23.9/28.1% | 1.9/5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario coastal`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.809 | 0.777 | 0.032 | - | - | 0.978 | 0.984 | 0.498 | 0.99x | 14.7/20.5/24.6% | 1.5/4.5% | 3 |
| True | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario coastal`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| BALANCED | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| STRICT | 1 | 0.845 | 0.845 | 0.000 | - | - | 0.930 | 0.931 | 0.449 | 1.46x | 20.8/27.5/32.1% | 2.2/5.8% | 3 |

> signature-policy=STRICT: decode_failures 1

### `SF-advert-transport` - advert-transport  `--scenario coastal`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| dm | 1 | 0.916 | 0.904 | 0.012 | - | - | 0.988 | 0.989 | 0.598 | 1.29x | 18.4/24.6/29.0% | 2.0/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario coastal`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.923 | 0.916 | 0.007 | - | - | 0.986 | 0.989 | 0.624 | 1.31x | 18.7/24.8/29.0% | 2.0/5.2% | 3 |
| local | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| time | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.987 | 0.991 | 0.597 | 1.36x | 19.4/25.9/30.3% | 2.1/5.5% | 3 |
| window | 1 | 0.917 | 0.908 | 0.009 | - | - | 0.987 | 0.989 | 0.591 | 1.31x | 18.7/25.0/29.3% | 2.0/5.3% | 3 |

> bucket-mode=global: misdecodes 42

> bucket-mode=time: misdecodes 21

> bucket-mode=window: misdecodes 24

### `SF-bucket-time` - time-bucket-s  `--scenario coastal`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.909 | 0.900 | 0.009 | - | - | 0.987 | 0.989 | 0.595 | 1.49x | 21.1/27.9/32.5% | 2.3/6.0% | 3 |
| 1800 | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.987 | 0.991 | 0.597 | 1.36x | 19.4/25.9/30.3% | 2.1/5.5% | 3 |
| 3600 | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.983 | 0.992 | 0.593 | 1.32x | 18.8/25.1/29.5% | 2.0/5.3% | 3 |

> time-bucket-s=600: misdecodes 110

> time-bucket-s=1800: misdecodes 21

> time-bucket-s=3600: misdecodes 9

> time-bucket-s=3600: decode_failures 1

### `SF-cadence` - trigger  `--scenario coastal`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| interval | 1 | 0.904 | 0.892 | 0.012 | - | - | 0.977 | 0.990 | 0.610 | 1.82x | 25.5/33.3/39.0% | 2.8/7.6% | 3 |
| aimd | 1 | 0.911 | 0.909 | 0.003 | - | - | 0.926 | 0.989 | 0.588 | 1.32x | 18.8/25.0/29.3% | 2.0/5.2% | 3 |
| bucket+interval | 1 | 0.902 | 0.888 | 0.014 | - | - | 0.989 | 0.989 | 0.589 | 1.84x | 25.9/34.1/39.5% | 2.9/7.7% | 3 |

> trigger=interval: misdecodes 11

> trigger=interval: decode_failures 12

> trigger=aimd: misdecodes 4

> trigger=aimd: decode_failures 5

> trigger=bucket+interval: misdecodes 18

### `SF-capacity` - capacity  `--scenario coastal`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.986 | 0.991 | 0.610 | 1.31x | 18.7/24.9/29.4% | 2.0/5.4% | 3 |
| 8 | 1 | 0.925 | 0.917 | 0.009 | - | - | 0.989 | 0.991 | 0.638 | 1.31x | 18.8/25.0/29.5% | 2.0/5.3% | 3 |
| 16 | 1 | 0.919 | 0.909 | 0.010 | - | - | 0.989 | 0.989 | 0.588 | 1.31x | 18.7/24.9/29.3% | 2.0/5.3% | 3 |
| 32 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 50 | 1 | 0.917 | 0.908 | 0.009 | - | - | 0.989 | 0.989 | 0.615 | 1.32x | 18.9/25.1/29.5% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 101

> capacity=8: decode_failures 40

### `SF-capacity-local` - capacity  `--scenario coastal`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.986 | 0.991 | 0.610 | 1.31x | 18.7/24.9/29.4% | 2.0/5.4% | 3 |
| 8 | 1 | 0.925 | 0.917 | 0.009 | - | - | 0.989 | 0.991 | 0.638 | 1.31x | 18.8/25.0/29.5% | 2.0/5.3% | 3 |
| 16 | 1 | 0.919 | 0.909 | 0.010 | - | - | 0.989 | 0.989 | 0.588 | 1.31x | 18.7/24.9/29.3% | 2.0/5.3% | 3 |
| 32 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 50 | 1 | 0.917 | 0.908 | 0.009 | - | - | 0.989 | 0.989 | 0.615 | 1.32x | 18.9/25.1/29.5% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 101

> capacity=8: decode_failures 40

### `SF-capacity-window` - capacity  `--scenario coastal`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.925 | 0.918 | 0.007 | - | - | 0.980 | 0.995 | 0.621 | 1.29x | 18.4/24.6/28.9% | 2.0/5.2% | 3 |
| 16 | 1 | 0.916 | 0.906 | 0.011 | - | - | 0.987 | 0.989 | 0.602 | 1.30x | 18.6/24.8/29.1% | 2.0/5.2% | 3 |
| 32 | 1 | 0.917 | 0.908 | 0.009 | - | - | 0.987 | 0.989 | 0.591 | 1.31x | 18.7/25.0/29.3% | 2.0/5.3% | 3 |

> capacity=8: misdecodes 27

> capacity=8: decode_failures 37

> capacity=16: misdecodes 17

> capacity=16: decode_failures 1

> capacity=32: misdecodes 24

### `SF-catchup` - catch-up-hours  `--scenario coastal`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.902 | 0.888 | 0.014 | - | - | 0.989 | 0.989 | 0.589 | 1.84x | 25.9/34.1/39.5% | 2.9/7.7% | 3 |
| 02-06 | 1 | 0.916 | 0.912 | 0.004 | - | - | 0.946 | 0.990 | 0.617 | 1.34x | 19.1/25.4/29.8% | 2.1/5.4% | 3 |
| 00-08 | 1 | 0.919 | 0.915 | 0.004 | - | - | 0.955 | 0.994 | 0.603 | 1.39x | 19.8/26.4/30.9% | 2.2/5.8% | 3 |

> catch-up-hours=: misdecodes 18

> catch-up-hours=02-06: misdecodes 1

> catch-up-hours=02-06: decode_failures 39

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 35

### `SF-hops-flat` - hops-apart  `--scenario coastal`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.913 | 0.912 | 0.001 | - | - | 0.989 | 0.989 | 0.556 | 1.30x | 18.5/24.7/29.0% | 1.9/5.1% | 3 |
| 2 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 3 | 1 | 0.922 | 0.911 | 0.011 | - | - | 0.988 | 0.989 | 0.559 | 1.31x | 18.7/24.9/29.3% | 2.0/5.3% | 3 |
| 4 | 1 | 0.917 | 0.903 | 0.013 | - | - | 0.989 | 0.990 | 0.539 | 1.32x | 18.9/25.0/29.4% | 2.0/5.4% | 3 |

> faster: 1.8 s per simulated hour against 3.8 over 19 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario coastal`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.913 | 0.912 | 0.001 | - | - | 0.989 | 0.989 | 0.556 | 1.30x | 18.5/24.7/29.0% | 1.9/5.1% | 3 |
| 2 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 3 | 1 | 0.922 | 0.911 | 0.011 | - | - | 0.988 | 0.989 | 0.559 | 1.31x | 18.7/24.9/29.3% | 2.0/5.3% | 3 |
| 4 | 1 | 0.917 | 0.903 | 0.013 | - | - | 0.989 | 0.990 | 0.539 | 1.32x | 18.9/25.0/29.4% | 2.0/5.4% | 3 |
| 5 | 1 | 0.917 | 0.903 | 0.013 | - | - | 0.989 | 0.990 | 0.539 | 1.32x | 18.9/25.0/29.4% | 2.0/5.4% | 3 |

> faster: 1.88 s per simulated hour against 4.81 over 19 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario coastal`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.917 | 0.907 | 0.010 | - | - | 0.989 | 0.991 | 0.588 | 1.33x | 19.0/25.3/29.7% | 2.0/5.4% | 3 |
| 30 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 120 | 1 | 0.919 | 0.909 | 0.010 | - | - | 0.992 | 0.993 | 0.620 | 1.34x | 19.0/25.3/29.7% | 2.0/5.4% | 3 |
| 600 | 1 | 0.921 | 0.912 | 0.009 | - | - | 0.992 | 0.992 | 0.625 | 1.30x | 18.6/24.9/29.1% | 2.0/5.3% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario coastal`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.917 | 0.907 | 0.010 | - | - | 0.989 | 0.991 | 0.588 | 1.33x | 19.0/25.3/29.7% | 2.0/5.4% | 3 |
| 30 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 120 | 1 | 0.919 | 0.909 | 0.010 | - | - | 0.992 | 0.993 | 0.620 | 1.34x | 19.0/25.3/29.7% | 2.0/5.4% | 3 |
| 600 | 1 | 0.921 | 0.912 | 0.009 | - | - | 0.992 | 0.992 | 0.625 | 1.30x | 18.6/24.9/29.1% | 2.0/5.3% | 3 |

### `SF-place-flat` - place  `--scenario coastal`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.930 | 0.911 | 0.019 | - | - | 0.991 | 0.992 | 0.551 | 1.34x | 19.0/25.5/29.8% | 2.0/5.6% | 3 |
| routers | 1 | 0.909 | 0.906 | 0.002 | - | - | 0.977 | 0.978 | 0.548 | 1.28x | 18.3/24.5/28.7% | 1.9/5.1% | 3 |
| alternate-routers | 1 | 0.908 | 0.907 | 0.002 | - | - | 0.982 | 0.982 | 0.553 | 1.32x | 19.0/25.4/29.7% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.908 | 0.905 | 0.003 | - | - | 0.988 | 0.988 | 0.552 | 1.30x | 18.7/24.9/29.3% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.924 | 0.913 | 0.011 | - | - | 0.993 | 0.995 | 0.548 | 1.32x | 18.7/24.8/29.2% | 2.0/5.1% | 3 |
| hops-apart | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `SF-place-spread` - place  `--scenario coastal`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.930 | 0.911 | 0.019 | - | - | 0.991 | 0.992 | 0.551 | 1.34x | 19.0/25.5/29.8% | 2.0/5.6% | 3 |
| routers | 1 | 0.909 | 0.906 | 0.002 | - | - | 0.977 | 0.978 | 0.548 | 1.28x | 18.3/24.5/28.7% | 1.9/5.1% | 3 |
| alternate-routers | 1 | 0.908 | 0.907 | 0.002 | - | - | 0.982 | 0.982 | 0.553 | 1.32x | 19.0/25.4/29.7% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.908 | 0.905 | 0.003 | - | - | 0.988 | 0.988 | 0.552 | 1.30x | 18.7/24.9/29.3% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.924 | 0.913 | 0.011 | - | - | 0.993 | 0.995 | 0.548 | 1.32x | 18.7/24.8/29.2% | 2.0/5.1% | 3 |
| hops-apart | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `SF-provide-transport` - provide-transport  `--scenario coastal`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| broadcast | 1 | 0.940 | 0.901 | 0.038 | - | - | 0.985 | 0.989 | 0.627 | 1.41x | 20.0/26.5/31.0% | 2.1/5.5% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario coastal`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| heard | 1 | 0.922 | 0.912 | 0.010 | - | - | 0.989 | 0.991 | 0.599 | 1.32x | 18.8/25.0/29.4% | 2.0/5.3% | 3 |

> replay-ordering=heard: misdecodes 14

### `SF-replay-order-broadcast` - replay-ordering  `--scenario coastal`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.940 | 0.901 | 0.038 | - | - | 0.985 | 0.989 | 0.627 | 1.41x | 20.0/26.5/31.0% | 2.1/5.5% | 3 |
| heard | 1 | 0.934 | 0.898 | 0.036 | - | - | 0.985 | 0.987 | 0.628 | 1.42x | 20.1/26.7/31.1% | 2.1/5.5% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario coastal`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| enum | 1 | 0.924 | 0.915 | 0.009 | - | - | 0.986 | 0.992 | 0.634 | 1.29x | 18.4/24.6/29.0% | 2.0/5.3% | 3 |
| hybrid | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario coastal`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.909 | 0.906 | 0.002 | - | - | 0.977 | 0.978 | 0.548 | 1.28x | 18.3/24.5/28.7% | 1.9/5.1% | 3 |
| 6 | 1 | 0.914 | 0.910 | 0.004 | - | - | 0.986 | 0.986 | 0.549 | 1.34x | 19.2/25.7/30.1% | 2.0/5.4% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario coastal`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.920 | 0.913 | 0.007 | - | - | 0.992 | 0.994 | 0.598 | 1.30x | 18.6/24.8/29.0% | 2.0/5.2% | 2 |
| 3 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 5 | 1 | 0.919 | 0.904 | 0.015 | - | - | 0.991 | 0.992 | 0.611 | 1.34x | 19.0/25.3/29.7% | 2.0/5.6% | 5 |
| 8 | 1 | 0.924 | 0.908 | 0.015 | - | - | 0.994 | 0.995 | 0.625 | 1.39x | 19.7/26.3/30.7% | 2.1/5.8% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario coastal`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.920 | 0.913 | 0.007 | - | - | 0.992 | 0.994 | 0.598 | 1.30x | 18.6/24.8/29.0% | 2.0/5.2% | 2 |
| 3 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 5 | 1 | 0.919 | 0.904 | 0.015 | - | - | 0.991 | 0.992 | 0.611 | 1.34x | 19.0/25.3/29.7% | 2.0/5.6% | 5 |
| 8 | 1 | 0.924 | 0.908 | 0.015 | - | - | 0.994 | 0.995 | 0.625 | 1.39x | 19.7/26.3/30.7% | 2.1/5.8% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario coastal`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| True | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario coastal`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.918 | 0.911 | 0.007 | - | - | 0.984 | 0.990 | 0.609 | 1.23x | 17.6/23.5/27.5% | 1.9/5.0% | 3 |
| 1 | 1 | 0.921 | 0.912 | 0.008 | - | - | 0.988 | 0.989 | 0.623 | 1.24x | 17.5/23.6/27.7% | 1.8/5.0% | 3 |
| 2 | 1 | 0.914 | 0.904 | 0.009 | - | - | 0.987 | 0.989 | 0.591 | 1.24x | 17.6/23.7/27.7% | 1.8/5.1% | 3 |
| 4 | 1 | 0.917 | 0.906 | 0.011 | - | - | 0.989 | 0.989 | 0.609 | 1.22x | 17.3/23.4/27.3% | 1.8/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario coastal`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.988 | 0.990 | 0.593 | 1.31x | 18.7/25.0/29.3% | 2.0/5.3% | 3 |
| 24 | 1 | 0.922 | 0.913 | 0.009 | - | - | 0.993 | 0.995 | 0.633 | 1.31x | 18.8/25.0/29.4% | 2.0/5.3% | 3 |
| 32 | 1 | 0.918 | 0.910 | 0.009 | - | - | 0.992 | 0.992 | 0.603 | 1.32x | 19.0/25.3/29.6% | 2.0/5.4% | 3 |
| 64 | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.990 | 0.991 | 0.591 | 1.34x | 19.0/25.4/29.9% | 2.0/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario coastal`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.919 | 0.908 | 0.011 | - | - | 0.992 | 0.993 | 0.608 | 1.40x | 19.8/26.4/30.9% | 2.1/5.6% | 3 |
| 16 | 1 | 0.915 | 0.905 | 0.010 | - | - | 0.986 | 0.987 | 0.599 | 1.36x | 19.5/26.0/30.3% | 2.1/5.5% | 3 |
| 32 | 1 | 0.917 | 0.908 | 0.009 | - | - | 0.987 | 0.989 | 0.591 | 1.31x | 18.7/25.0/29.3% | 2.0/5.3% | 3 |

> window-size=8: misdecodes 137

> window-size=16: misdecodes 51

> window-size=32: misdecodes 24

### `TH-congestion` - no-congestion-scaling  `--scenario coastal`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.971 | 0.969 | 0.002 | - | - | 0.999 | 0.999 | 0.906 | 1.92x | 23.4/34.6/38.4% | 1.3/4.9% | 3 |
| True | 1 | 0.765 | 0.755 | 0.010 | - | - | 0.859 | 0.895 | 0.610 | 5.49x | 60.5/74.1/78.0% | 3.9/11.7% | 3 |

> no-congestion-scaling=True: queue drops 14.8% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 113

### `TH-congestion-input` - congestion-input  `--scenario coastal`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.536 | 0.525 | 0.011 | - | - | 0.749 | 0.750 | 0.252 | 4.41x | 17.4/25.7/31.1% | 1.5/5.4% | 3 |
| truesize | 1 | 0.571 | 0.562 | 0.010 | - | - | 0.779 | 0.780 | 0.270 | 3.33x | 13.2/19.7/24.0% | 1.1/4.0% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario coastal`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.970 | 0.968 | 0.002 | - | - | 0.998 | 0.999 | 0.911 | 1.82x | 22.2/32.8/36.4% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.971 | 0.969 | 0.002 | - | - | 0.999 | 0.999 | 0.906 | 1.92x | 23.4/34.6/38.4% | 1.3/4.9% | 3 |

