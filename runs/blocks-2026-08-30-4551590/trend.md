# Sweep blocks-2026-08-30-4551590

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** coastal
- **seed base** 4551590 · seeds 4551590
- **blocks** 87 run
- **compute** 12.1 h of simulator time across every cell
- **generated** 2026-08-30T11:15:11+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>117 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 4
- AD-badrouters: role-placement=random: decode_failures 48
- AD-badrouters: slower: 6.34 s per simulated hour against 2.42 over 9 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=local-typical: decode_failures 12
- AD-worst: role-placement=degree: decode_failures 54
- AD-worst: role-placement=inverse: decode_failures 78
- AD-worst: slower: 21 s per simulated hour against 3.62 over 9 prior run(s) - 5.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 28
- DB-hotstore: slower: 5.15 s per simulated hour against 2.57 over 9 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 36
- DB-hotstore-stress: max-num-nodes=120: decode_failures 1
- DB-hotstore-stress: max-num-nodes=250: decode_failures 48
- DB-platform: platform-mix=constrained: decode_failures 21
- DB-platform: slower: 5.35 s per simulated hour against 2.58 over 9 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: queue drops 27.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 112
- DB-warm: warm-num-nodes=25: queue drops 27.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 112
- DB-warm: warm-num-nodes=100: queue drops 27.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 112
- DB-warm: warm-num-nodes=2000: queue drops 27.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 112
- DG-burst: burst-loss=0.1: decode_failures 32
- DG-burst: burst-loss=0.2: decode_failures 20
- DG-burst: burst-loss=0.3: decode_failures 25
- DG-loss: extra-loss=0.2: decode_failures 24
- DG-loss: extra-loss=0.3: decode_failures 20
- DG-loss: slower: 5.01 s per simulated hour against 2.27 over 9 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.1: decode_failures 46
- DG-outage: burst-loss=0.2: decode_failures 32
- DG-outage: burst-loss=0.3: decode_failures 25
- DM-mode: dm-mode=flood-only: decode_failures 6
- DM-mode: dm-mode=m4-early-flood: decode_failures 8
- LD-chatty-hops: broadcast-interval-s=300: queue drops 23.2% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 16
- LD-chatty: broadcast-interval-s=900: decode_failures 9
- LD-chatty: broadcast-interval-s=300: queue drops 17.7% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 19
- LD-interval: broadcast-interval-s=900: decode_failures 9
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 27.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 112
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 38.0% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 95
- MS-density: nodes=40: decode_failures 14
- MS-density: nodes=120: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 3
- MS-hopscale: nodes=500: decode_failures 42
- MS-oversubscribed: nodes=250: decode_failures 1
- MS-oversubscribed: nodes=500: decode_failures 17
- MS-router-late: router-late-fraction=0.1: decode_failures 1
- MS-stretch: stretch=1.5: decode_failures 2
- PR-crladder: coding-rate-ladder=True: decode_failures 1
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 1
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 18
- RF-bw500: preset=LONG_TURBO: decode_failures 30
- RF-bw500: slower: 5.67 s per simulated hour against 1.43 over 9 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-noise: noise-profile=temporal: decode_failures 32
- RF-noise: noise-profile=periodic: decode_failures 11
- RF-preset: preset=LONG_MODERATE: decode_failures 56
- RF-preset: slower: 6.03 s per simulated hour against 2.94 over 9 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 18
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 30
- RF-preset-turbo: slower: 3.94 s per simulated hour against 1.59 over 5 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 6
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 11
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 6
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 2
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 46
- RF-stretch-duct: slower: 7.83 s per simulated hour against 1.72 over 9 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 6
- RF-txpower: tx-power=14: decode_failures 1
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-hopassign: hop-assign=random: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 16
- SF-bucket-mode: bucket-mode=time: misdecodes 40
- SF-bucket-mode: bucket-mode=window: misdecodes 11
- SF-bucket-time: time-bucket-s=600: misdecodes 116
- SF-bucket-time: time-bucket-s=1800: misdecodes 40
- SF-bucket-time: time-bucket-s=3600: misdecodes 10
- SF-cadence: trigger=interval: misdecodes 16
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 9
- SF-cadence: trigger=bucket+interval: misdecodes 23
- SF-capacity-local: capacity=4: decode_failures 99
- SF-capacity-local: capacity=8: decode_failures 83
- SF-capacity: capacity=4: decode_failures 99
- SF-capacity: capacity=8: decode_failures 83
- SF-capacity-window: capacity=8: misdecodes 5
- SF-capacity-window: capacity=8: decode_failures 48
- SF-capacity-window: capacity=16: misdecodes 22
- SF-capacity-window: capacity=32: misdecodes 11
- SF-catchup: catch-up-hours=: misdecodes 23
- SF-catchup: catch-up-hours=02-06: decode_failures 43
- SF-catchup: catch-up-hours=00-08: decode_failures 41
- SF-hops-spread: faster: 2.22 s per simulated hour against 4.81 over 9 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=random-clients: decode_failures 7
- SF-place-spread: place=random-clients: decode_failures 7
- SF-provide-transport: provide-transport=broadcast: decode_failures 4
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 4
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 9
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=5: misdecodes 1
- SF-servers-spread: servers=5: misdecodes 1
- SF-sr-retries: sr-retries=0: decode_failures 24
- SF-sr-retries: slower: 4.2 s per simulated hour against 1.7 over 9 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 124
- SF-window-size: window-size=16: misdecodes 65
- SF-window-size: window-size=32: misdecodes 11
- TH-congestion-input: congestion-input=hotstore: decode_failures 1
- TH-congestion-input: congestion-input=truesize: decode_failures 2
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 24.9% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 103

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 21 | 3.62 | 5.80x | 9 |
| `RF-stretch-duct` | 7.83 | 1.72 | 4.55x | 9 |
| `RF-bw500` | 5.67 | 1.43 | 3.95x | 9 |
| `AD-badrouters` | 6.34 | 2.42 | 2.62x | 9 |
| `RF-preset-turbo` | 3.94 | 1.59 | 2.48x | 5 |
| `SF-sr-retries` | 4.2 | 1.7 | 2.48x | 9 |
| `DG-loss` | 5.01 | 2.27 | 2.21x | 9 |
| `DB-platform` | 5.35 | 2.58 | 2.08x | 9 |
| `RF-preset` | 6.03 | 2.94 | 2.05x | 9 |
| `DB-hotstore` | 5.15 | 2.57 | 2.00x | 9 |
| `RF-pulse` | 3.04 | 1.6 | 1.89x | 9 |
| `AD-siting` | 2.27 | 1.25 | 1.81x | 9 |
| `SF-cadence` | 4.8 | 2.75 | 1.74x | 9 |
| `RF-noise` | 8.81 | 5.27 | 1.67x | 9 |
| `DG-burst` | 7.42 | 4.49 | 1.65x | 9 |
| `LD-interval` | 2.14 | 1.4 | 1.53x | 9 |
| `MS-router-late` | 2.67 | 1.76 | 1.52x | 9 |
| `SF-place-flat` | 2.2 | 3.47 | 0.63x | 9 |
| `SF-place-spread` | 2.11 | 3.33 | 0.63x | 9 |
| `BL-control` | 0.915 | 1.74 | 0.53x | 9 |
| `SF-hops-spread` | 2.22 | 4.81 | 0.46x | 9 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.988 | 0.988 | 0.929 → 0.938 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.987 | 0.987 | 0.926 → 0.938 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **text** | 0.096 → 0.940 | 0.844 | 0.096 → 0.934 | 5.8x sr_bytes | up | 5 |
| `AD-siting` | siting-mix | **text** | 0.052 → 0.886 | 0.834 | 0.052 → 0.879 | 11x sr_bytes | down | 3 |
| `RF-txpower` | tx-power | **text** | 0.112 → 0.940 | 0.828 | 0.111 → 0.934 | 5.3x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.166 → 0.940 | 0.774 | 0.164 → 0.934 | 3.3x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.171 → 0.933 | 0.761 | 0.165 → 0.881 | 88x sr_airtime | down | 4 |
| `RF-bw500` | preset | **text** | 0.196 → 0.874 | 0.678 | 0.194 → 0.870 | 3.6x sr_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.317 → 0.940 | 0.623 | 0.312 → 0.934 | 10x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.424 → 0.940 | 0.516 | 0.416 → 0.934 | 2.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.424 → 0.940 | 0.516 | 0.416 → 0.934 | 2.3x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **text** | 0.319 → 0.817 | 0.498 | 0.314 → 0.811 | 5.1x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.593 → 0.976 | 0.383 | 0.588 → 0.976 | 1.9x sr_bytes | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.592 → 0.964 | 0.372 | 0.587 → 0.961 | 16x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.604 → 0.947 | 0.343 | 0.570 → 0.945 | 3.2x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.611 → 0.940 | 0.329 | 0.592 → 0.934 | 2x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.504 → 0.833 | 0.329 | 0.312 → 0.520 | 6.1x sr_airtime | up | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.641 → 0.948 | 0.307 | 0.631 → 0.944 | 11x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.645 → 0.940 | 0.294 | 0.610 → 0.934 | 2.1x sr_bytes | down | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.733 → 0.974 | 0.241 | 0.723 → 0.971 | 4.4x sr_airtime | down | 2 |
| `RF-stretch-duct` | duct-per-hour | **held** | 0.594 → 0.831 | 0.237 | 0.571 → 0.766 | 2.7x sr_bytes | up | 2 |
| `MS-density` | nodes | **text** | 0.755 → 0.974 | 0.220 | 0.749 → 0.973 | 5.6x sr_airtime | up | 5 |
| `MS-size` | nodes | **text** | 0.758 → 0.940 | 0.182 | 0.750 → 0.934 | 4.5x sr_airtime | down | 5 |
| `RF-noise` | noise-profile | **held** | 0.833 → 0.987 | 0.154 | 0.785 → 0.934 | 1.3x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **held** | 0.856 → 0.987 | 0.131 | 0.809 → 0.934 | 1.3x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.845 → 0.960 | 0.115 | 0.822 → 0.958 | 1.8x sr_bytes | up | 4 |
| `DG-loss` | extra-loss | **held** | 0.877 → 0.987 | 0.110 | 0.823 → 0.934 | 1.3x sr_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.845 → 0.955 | 0.110 | 0.822 → 0.952 | 1.7x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.845 → 0.940 | 0.095 | 0.822 → 0.934 | 1.6x sr_bytes | up | 2 |
| `DB-platform` | platform-mix | **held** | 0.895 → 0.986 | 0.091 | 0.867 → 0.951 | 3x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.872 → 0.954 | 0.082 | 0.867 → 0.951 | 2.6x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.886 → 0.957 | 0.071 | 0.879 → 0.956 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.886 → 0.957 | 0.071 | 0.879 → 0.956 | 2.5x bytes_on_air | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.650 → 0.710 | 0.061 | 0.641 → 0.701 | 1.3x sr_airtime | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.900 → 0.958 | 0.058 | 0.891 → 0.955 | 5.1x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.930 → 0.987 | 0.057 | 0.934 → 0.938 | 28x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.930 → 0.987 | 0.057 | 0.920 → 0.934 | 13x advert_bytes | down | 4 |
| `MS-roles` | role-mix | **text** | 0.886 → 0.936 | 0.050 | 0.879 → 0.931 | 1.2x bytes_on_air | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.893 → 0.941 | 0.048 | 0.889 → 0.937 | 1.1x sr_airtime | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.944 → 0.989 | 0.045 | 0.929 → 0.936 | 1.2x sr_bytes | up | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.825 → 0.866 | 0.041 | 0.514 → 0.544 | 1.4x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.947 → 0.984 | 0.037 | 0.920 → 0.930 | 9.4x advert_bytes | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.940 → 0.969 | 0.030 | 0.934 → 0.968 | 1.5x bytes_on_air | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.910 → 0.940 | 0.029 | 0.902 → 0.934 | 1.6x sr_airtime | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.958 → 0.986 | 0.028 | 0.929 → 0.935 | 2.3x advert_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.940 → 0.961 | 0.022 | 0.934 → 0.958 | 1.4x bytes_on_air | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.940 → 0.958 | 0.019 | 0.934 → 0.958 | 3x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.946 → 0.963 | 0.017 | 0.876 → 0.889 | 1.2x sr_bytes | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.940 → 0.956 | 0.017 | 0.934 → 0.954 | 3.4x bytes_on_air | down | 2 |
| `AD-worst` | role-placement | **held** | 0.869 → 0.884 | 0.016 | 0.814 → 0.829 | 1.1x sr_airtime | up | 2 |
| `SF-hops-flat` | hops-apart | **text** | 0.927 → 0.942 | 0.015 | 0.927 → 0.934 | 2.6x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.927 → 0.942 | 0.015 | 0.927 → 0.934 | 2.6x sr_bytes | up | 5 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.973 → 0.987 | 0.014 | 0.919 → 0.934 | 5.4x advert_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.926 → 0.940 | 0.014 | 0.924 → 0.934 | 2.2x bytes_on_air | down | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.926 → 0.940 | 0.013 | 0.925 → 0.938 | 2.1x bytes_on_air | down | 4 |
| `SF-capacity` | capacity | **held** | 0.977 → 0.990 | 0.013 | 0.928 → 0.936 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.977 → 0.990 | 0.013 | 0.928 → 0.936 | 5.4x advert_bytes | up | 5 |
| `SF-place-flat` | place | **held** | 0.979 → 0.991 | 0.012 | 0.930 → 0.934 | 2.4x sr_bytes | down | 6 |
| `SF-place-spread` | place | **held** | 0.979 → 0.991 | 0.012 | 0.930 → 0.934 | 2.4x sr_bytes | down | 6 |
| `DM-mode` | dm-mode | **text** | 0.905 → 0.917 | 0.012 | 0.905 → 0.917 | 1.2x sr_airtime | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.976 → 0.987 | 0.012 | 0.930 → 0.941 | 1.3x bytes_on_air | down | 4 |
| `SF-width` | short-id-bits | **held** | 0.979 → 0.990 | 0.011 | 0.928 → 0.936 | 3.1x advert_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.929 → 0.940 | 0.010 | 0.920 → 0.934 | 1x sr_airtime | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.939 → 0.949 | 0.010 | 0.933 → 0.945 | 1.1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.968 → 0.978 | 0.010 | 0.916 → 0.917 | 1.1x sr_bytes | down | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.978 → 0.987 | 0.009 | 0.929 → 0.934 | 2.5x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.968 → 0.976 | 0.009 | 0.916 → 0.919 | 1.1x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.966 → 0.974 | 0.008 | 0.962 → 0.971 | 1.2x sr_airtime | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.936 → 0.943 | 0.007 | 0.931 → 0.939 | 1.3x sr_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.937 → 0.944 | 0.007 | 0.931 → 0.939 | 3.2x advert_bytes | down | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.987 → 0.994 | 0.007 | 0.933 → 0.939 | 1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.987 → 0.994 | 0.007 | 0.933 → 0.939 | 1x sr_bytes | down | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.978 → 0.985 | 0.007 | 0.929 → 0.932 | 1x sr_airtime | up | 2 |
| `FW-versions` | profile | **held** | 0.987 → 0.993 | 0.006 | 0.934 → 0.941 | 3.2x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **held** | 0.987 → 0.993 | 0.005 | 0.934 → 0.937 | 3.1x bytes_on_air | down | 2 |
| `SF-resolve` | resolve | **held** | 0.982 → 0.987 | 0.005 | 0.934 → 0.935 | 5.8x advert_bytes | = | 3 |
| `SF-servers-flat` | servers | **text** | 0.934 → 0.940 | 0.005 | 0.927 → 0.936 | 7x sr_bytes | down | 4 |
| `SF-servers-spread` | servers | **text** | 0.934 → 0.940 | 0.005 | 0.927 → 0.936 | 7x sr_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.986 → 0.990 | 0.004 | 0.930 → 0.931 | 2.6x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.936 → 0.940 | 0.003 | 0.931 → 0.934 | 1x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.940 → 0.942 | 0.003 | 0.934 → 0.938 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.974 → 0.976 | 0.003 | 0.971 → 0.974 | 1.1x bytes_on_air | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.987 → 0.990 | 0.002 | 0.934 → 0.935 | 3.1x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **text** | 0.935 → 0.937 | 0.002 | 0.928 → 0.931 | 5.9x advert_bytes | up | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.973 → 0.974 | 0.001 | 0.970 → 0.971 | 1x sr_bytes | down | 2 |

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
| none | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| sprinkled | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.972 | 0.972 | 0.786 | 1.24x | 21.9/29.0/30.4% | 1.8/5.8% | 3 |
| arms-race | 1 | 0.958 | 0.958 | 0.000 | - | - | 0.981 | 0.981 | 0.861 | 0.89x | 22.4/25.8/28.2% | 0.6/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario coastal`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.945 | 0.942 | 0.003 | - | - | 0.997 | 0.997 | 0.793 | 1.11x | 19.8/27.2/30.0% | 1.6/5.2% | 3 |
| 0.3 | 1 | 0.969 | 0.968 | 0.001 | - | - | 1.000 | 1.000 | 0.922 | 0.91x | 21.6/28.9/30.5% | 1.0/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario coastal`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.962 | 0.963 | 0.577 | 1.20x | 18.1/26.9/29.4% | 2.0/5.2% | 3 |
| inverse | 1 | 0.885 | 0.876 | 0.009 | - | - | 0.963 | 0.972 | 0.578 | 1.20x | 17.1/22.9/24.8% | 2.2/3.5% | 3 |
| random | 1 | 0.896 | 0.889 | 0.007 | - | - | 0.946 | 0.969 | 0.609 | 1.23x | 17.2/24.4/27.4% | 2.1/5.1% | 3 |

> role-placement=inverse: decode_failures 4

> role-placement=random: decode_failures 48

> slower: 6.34 s per simulated hour against 2.42 over 9 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario coastal`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.962 | 0.963 | 0.577 | 1.20x | 18.1/26.9/29.4% | 2.0/5.2% | 3 |
| all-routers | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.988 | 0.988 | 0.893 | 2.95x | 38.0/49.8/52.4% | 4.8/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario coastal`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.962 | 0.963 | 0.577 | 1.20x | 18.1/26.9/29.4% | 2.0/5.2% | 3 |
| no-mute | 1 | 0.923 | 0.918 | 0.004 | - | - | 0.984 | 0.985 | 0.667 | 1.36x | 19.7/25.4/29.3% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.988 | 0.988 | 0.893 | 2.95x | 38.0/49.8/52.4% | 4.8/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario coastal`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.962 | 0.963 | 0.577 | 1.20x | 18.1/26.9/29.4% | 2.0/5.2% | 3 |
| local-typical | 1 | 0.638 | 0.632 | 0.006 | - | - | 0.611 | 0.783 | 0.000 | 1.17x | 16.5/29.7/32.3% | 1.7/5.4% | 3 |
| basement-heavy | 1 | 0.052 | 0.052 | 0.000 | - | - | 0.134 | 0.136 | 0.000 | 0.55x | 0.8/8.8/12.4% | 0.3/3.1% | 3 |

> siting-mix=local-typical: decode_failures 12

### `AD-worst` - role-placement  `--scenario coastal`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.833 | 0.829 | 0.004 | - | - | 0.869 | 0.942 | 0.188 | 2.44x | 18.5/32.2/40.1% | 1.8/5.8% | 3 |
| inverse | 1 | 0.823 | 0.814 | 0.009 | - | - | 0.884 | 0.952 | 0.221 | 2.37x | 15.5/27.3/34.6% | 1.8/3.5% | 3 |

> role-placement=degree: decode_failures 54

> role-placement=inverse: decode_failures 78

> slower: 21 s per simulated hour against 3.62 over 9 prior run(s) - 5.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario coastal`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.938 | 0.938 | 0.000 | - | - | 0 | 0.000 | 0.694 | 1.30x | 18.9/26.7/27.2% | 1.8/5.1% | 3 |
| sr | 1 | 0.938 | 0.929 | 0.008 | - | - | 0.988 | 0.989 | 0.667 | 1.36x | 19.8/27.9/28.4% | 1.9/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario coastal`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.872 | 0.867 | 0.005 | - | - | 0.906 | 0.937 | 0.653 | 3.50x | 48.5/68.3/71.4% | 5.3/10.6% | 3 |
| 100 | 1 | 0.954 | 0.951 | 0.003 | - | - | 0.986 | 0.989 | 0.700 | 1.74x | 24.9/39.4/41.5% | 2.4/5.5% | 3 |
| 120 | 1 | 0.954 | 0.951 | 0.003 | - | - | 0.986 | 0.989 | 0.700 | 1.74x | 24.9/39.4/41.5% | 2.4/5.5% | 3 |
| 250 | 1 | 0.954 | 0.951 | 0.003 | - | - | 0.986 | 0.989 | 0.700 | 1.74x | 24.9/39.4/41.5% | 2.4/5.5% | 3 |

> max-num-nodes=10: decode_failures 28

> slower: 5.15 s per simulated hour against 2.57 over 9 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario coastal`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.320 | 0.312 | 0.007 | - | - | 0.504 | 0.525 | 0.147 | 11.50x | 42.0/56.1/66.3% | 4.0/10.8% | 3 |
| 120 | 1 | 0.524 | 0.514 | 0.010 | - | - | 0.825 | 0.826 | 0.254 | 4.34x | 15.9/24.9/31.1% | 1.4/5.7% | 3 |
| 250 | 1 | 0.530 | 0.520 | 0.010 | - | - | 0.833 | 0.838 | 0.239 | 4.21x | 15.4/24.2/29.9% | 1.4/5.6% | 3 |

> max-num-nodes=10: decode_failures 36

> max-num-nodes=120: decode_failures 1

> max-num-nodes=250: decode_failures 48

### `DB-platform` - platform-mix  `--scenario coastal`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.954 | 0.951 | 0.003 | - | - | 0.986 | 0.989 | 0.700 | 1.74x | 24.9/39.4/41.5% | 2.4/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.954 | 0.951 | 0.003 | - | - | 0.986 | 0.989 | 0.700 | 1.74x | 24.9/39.4/41.5% | 2.4/5.5% | 3 |
| constrained | 1 | 0.871 | 0.867 | 0.004 | - | - | 0.895 | 0.933 | 0.663 | 3.49x | 48.4/68.1/71.4% | 5.3/10.6% | 3 |

> platform-mix=constrained: decode_failures 21

> slower: 5.35 s per simulated hour against 2.58 over 9 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario coastal`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.710 | 0.701 | 0.009 | - | - | 0.782 | 0.832 | 0.541 | 5.47x | 59.5/77.5/80.7% | 4.1/12.5% | 3 |
| 25 | 1 | 0.710 | 0.701 | 0.009 | - | - | 0.782 | 0.832 | 0.541 | 5.47x | 59.5/77.5/80.7% | 4.1/12.5% | 3 |
| 100 | 1 | 0.710 | 0.701 | 0.009 | - | - | 0.782 | 0.832 | 0.541 | 5.47x | 59.5/77.5/80.7% | 4.1/12.5% | 3 |
| 2000 | 1 | 0.710 | 0.701 | 0.009 | - | - | 0.782 | 0.832 | 0.541 | 5.47x | 59.5/77.5/80.7% | 4.1/12.5% | 3 |

> warm-num-nodes=0: queue drops 27.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 112

> warm-num-nodes=25: queue drops 27.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 112

> warm-num-nodes=100: queue drops 27.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 112

> warm-num-nodes=2000: queue drops 27.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 112

### `DG-burst` - burst-loss  `--scenario coastal`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.841 | 0.826 | 0.015 | - | - | 0.940 | 0.970 | 0.639 | 1.29x | 19.2/27.1/27.6% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.751 | 0.724 | 0.027 | - | - | 0.888 | 0.949 | 0.535 | 1.22x | 18.4/26.1/26.7% | 1.8/4.7% | 3 |
| 0.3 | 1 | 0.645 | 0.610 | 0.036 | - | - | 0.812 | 0.911 | 0.399 | 1.12x | 17.4/25.0/25.6% | 1.6/4.2% | 3 |

> burst-loss=0.1: decode_failures 32

> burst-loss=0.2: decode_failures 20

> burst-loss=0.3: decode_failures 25

### `DG-loss` - extra-loss  `--scenario coastal`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.917 | 0.910 | 0.006 | - | - | 0.975 | 0.981 | 0.695 | 1.47x | 21.6/30.2/30.7% | 2.1/5.4% | 3 |
| 0.2 | 1 | 0.888 | 0.879 | 0.008 | - | - | 0.952 | 0.979 | 0.621 | 1.49x | 21.9/31.0/31.7% | 2.2/5.1% | 3 |
| 0.3 | 1 | 0.830 | 0.823 | 0.007 | - | - | 0.877 | 0.960 | 0.552 | 1.53x | 22.6/32.1/33.1% | 2.3/4.9% | 3 |

> extra-loss=0.2: decode_failures 24

> extra-loss=0.3: decode_failures 20

> slower: 5.01 s per simulated hour against 2.27 over 9 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario coastal`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.839 | 0.823 | 0.016 | - | - | 0.904 | 0.974 | 0.624 | 1.30x | 19.0/27.3/27.8% | 2.0/4.9% | 3 |
| 0.2 | 1 | 0.731 | 0.710 | 0.020 | - | - | 0.852 | 0.938 | 0.523 | 1.23x | 18.7/26.5/27.0% | 1.8/4.8% | 3 |
| 0.3 | 1 | 0.611 | 0.592 | 0.019 | - | - | 0.723 | 0.893 | 0.400 | 1.15x | 17.4/25.2/26.0% | 1.7/4.2% | 3 |

> burst-loss=0.1: decode_failures 46

> burst-loss=0.2: decode_failures 32

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario coastal`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.905 | 0.905 | 0.000 | - | - | 0.967 | 0.975 | 0.670 | 1.88x | 27.2/38.1/39.1% | 2.6/7.3% | 3 |
| directed-with-late-flood | 1 | 0.917 | 0.917 | 0.000 | - | - | 0.978 | 0.980 | 0.658 | 1.65x | 24.3/34.3/35.1% | 2.3/6.6% | 3 |
| m4-early-flood | 1 | 0.916 | 0.916 | 0.000 | - | - | 0.967 | 0.976 | 0.679 | 1.66x | 24.3/34.4/35.1% | 2.3/6.6% | 3 |

> dm-mode=flood-only: decode_failures 6

> dm-mode=m4-early-flood: decode_failures 8

### `FW-firmware` - profile  `--scenario coastal`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.942 | 0.937 | 0.004 | - | - | 0.993 | 0.993 | 0.804 | 0.79x | 10.6/13.2/13.7% | 1.3/2.0% | 3 |
| 2.8 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario coastal`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.940 | 0.938 | 0.002 | - | - | 0.995 | 0.996 | 0.797 | 1.24x | 18.2/25.7/28.4% | 1.8/5.0% | 3 |
| 0.5 | 1 | 0.929 | 0.928 | 0.002 | - | - | 0.984 | 0.984 | 0.701 | 1.08x | 15.4/21.4/24.3% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.926 | 0.925 | 0.001 | - | - | 0.994 | 0.994 | 0.466 | 0.91x | 13.4/17.4/19.3% | 1.4/3.7% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario coastal`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.933 | 0.930 | 0.003 | - | - | 0.991 | 0.992 | 0.798 | 1.25x | 18.7/25.8/28.5% | 1.7/5.1% | 3 |
| 0.5 | 1 | 0.928 | 0.927 | 0.002 | - | - | 0.983 | 0.983 | 0.699 | 1.05x | 15.2/21.4/24.0% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.926 | 0.924 | 0.002 | - | - | 0.996 | 0.997 | 0.454 | 0.89x | 13.4/17.2/19.0% | 1.3/3.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario coastal`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.956 | 0.954 | 0.002 | - | - | 0.995 | 0.995 | 0.743 | 0.70x | 10.7/15.4/15.9% | 1.0/3.1% | 3 |
| signing=true | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `FW-versions` - profile  `--scenario coastal`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.941 | 0.938 | 0.003 | - | - | 0.992 | 0.993 | 0.768 | 0.79x | 11.1/14.5/15.0% | 1.3/2.2% | 3 |
| 2.5 | 1 | 0.941 | 0.938 | 0.004 | - | - | 0.993 | 0.994 | 0.801 | 0.81x | 11.2/14.6/15.1% | 1.3/2.3% | 3 |
| 2.6 | 1 | 0.941 | 0.937 | 0.003 | - | - | 0.992 | 0.992 | 0.789 | 0.76x | 11.0/14.4/14.9% | 1.2/2.2% | 3 |
| 2.7 | 1 | 0.944 | 0.941 | 0.003 | - | - | 0.989 | 0.989 | 0.773 | 0.77x | 11.1/15.6/16.5% | 1.2/3.1% | 3 |
| 2.8 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.948 | 0.944 | 0.004 | - | - | 0.991 | 0.993 | 0.744 | 0.91x | 13.5/18.6/19.2% | 1.3/3.7% | 3 |
| 900 | 1 | 0.900 | 0.891 | 0.008 | - | - | 0.958 | 0.965 | 0.688 | 2.26x | 32.9/45.5/46.5% | 3.1/8.6% | 3 |
| 300 | 1 | 0.641 | 0.631 | 0.010 | - | - | 0.717 | 0.797 | 0.486 | 4.68x | 61.4/75.7/77.5% | 7.4/15.2% | 3 |

> broadcast-interval-s=900: decode_failures 9

> broadcast-interval-s=300: queue drops 17.7% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 19

### `LD-chatty-hops` - broadcast-interval-s  `--scenario coastal`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.964 | 0.961 | 0.003 | - | - | 0.994 | 0.996 | 0.756 | 0.97x | 14.0/19.1/19.9% | 1.4/3.7% | 3 |
| 900 | 1 | 0.932 | 0.929 | 0.003 | - | - | 0.970 | 0.973 | 0.747 | 2.50x | 35.3/48.0/48.9% | 3.6/9.0% | 3 |
| 300 | 1 | 0.592 | 0.587 | 0.004 | - | - | 0.634 | 0.692 | 0.409 | 5.10x | 64.4/75.7/78.9% | 8.1/15.7% | 3 |

> broadcast-interval-s=300: queue drops 23.2% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 16

### `LD-diurnal` - diurnal  `--scenario coastal`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.943 | 0.939 | 0.005 | - | - | 0.989 | 0.991 | 0.743 | 1.26x | 18.4/25.8/26.3% | 1.8/4.9% | 3 |
| sinusoid | 1 | 0.936 | 0.931 | 0.005 | - | - | 0.988 | 0.989 | 0.722 | 1.22x | 17.8/25.0/25.5% | 1.7/4.8% | 3 |
| commuter | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.900 | 0.891 | 0.008 | - | - | 0.958 | 0.965 | 0.688 | 2.26x | 32.9/45.5/46.5% | 3.1/8.6% | 3 |
| 3600 | 1 | 0.948 | 0.944 | 0.004 | - | - | 0.991 | 0.993 | 0.744 | 0.91x | 13.5/18.6/19.2% | 1.3/3.7% | 3 |
| 10800 | 1 | 0.958 | 0.955 | 0.003 | - | - | 0.998 | 0.999 | 0.769 | 0.62x | 9.1/12.5/13.1% | 0.9/2.5% | 3 |
| 43200 | 1 | 0.958 | 0.955 | 0.003 | - | - | 0.995 | 0.997 | 0.733 | 0.45x | 6.6/9.1/9.6% | 0.7/1.9% | 3 |

> broadcast-interval-s=900: decode_failures 9

### `LD-traceroute` - traceroute-per-hour  `--scenario coastal`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.936 | 0.930 | 0.005 | - | - | 0.990 | 0.991 | 0.719 | 1.47x | 21.4/30.2/30.7% | 2.1/5.7% | 3 |
| 1.0 | 1 | 0.931 | 0.925 | 0.006 | - | - | 0.984 | 0.985 | 0.735 | 1.58x | 23.3/32.9/33.7% | 2.2/6.3% | 3 |
| 4.0 | 1 | 0.910 | 0.902 | 0.008 | - | - | 0.973 | 0.976 | 0.713 | 2.03x | 30.2/42.3/43.8% | 2.9/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario coastal`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.710 | 0.701 | 0.009 | - | - | 0.782 | 0.832 | 0.541 | 5.47x | 59.5/77.5/80.7% | 4.1/12.5% | 3 |
| 1.0 | 1 | 0.650 | 0.641 | 0.008 | - | - | 0.726 | 0.787 | 0.482 | 5.86x | 62.4/77.7/80.8% | 4.4/13.1% | 3 |

> traceroute-per-hour=0.0: queue drops 27.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 112

> traceroute-per-hour=1.0: queue drops 38.0% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 95

### `MS-density` - nodes  `--scenario coastal`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.755 | 0.749 | 0.005 | - | - | 0.814 | 0.868 | 0.409 | 1.35x | 23.5/35.7/38.2% | 3.1/7.4% | 3 |
| 60 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 90 | 1 | 0.969 | 0.967 | 0.002 | - | - | 0.998 | 0.999 | 0.879 | 1.55x | 21.9/30.7/33.6% | 1.4/4.9% | 3 |
| 120 | 1 | 0.974 | 0.971 | 0.003 | - | - | 0.998 | 0.998 | 0.916 | 2.03x | 23.9/41.5/44.9% | 1.3/5.2% | 3 |
| 150 | 1 | 0.974 | 0.973 | 0.001 | - | - | 0.997 | 0.997 | 0.902 | 2.56x | 29.3/47.1/52.7% | 1.3/5.5% | 3 |

> nodes=40: decode_failures 14

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario coastal`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 120 | 1 | 0.816 | 0.810 | 0.006 | - | - | 0.970 | 0.970 | 0.428 | 2.13x | 15.2/25.1/30.8% | 1.5/5.2% | 3 |
| 250 | 1 | 0.531 | 0.522 | 0.010 | - | - | 0.833 | 0.835 | 0.258 | 4.55x | 16.7/26.3/32.8% | 1.5/6.0% | 3 |
| 500 | 1 | 0.317 | 0.312 | 0.005 | - | - | 0.531 | 0.536 | 0.109 | 9.81x | 19.4/29.5/41.7% | 1.7/7.0% | 3 |

> nodes=250: decode_failures 3

> nodes=500: decode_failures 42

### `MS-oversubscribed` - nodes  `--scenario coastal`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.966 | 0.967 | 0.429 | 1.96x | 13.9/23.2/28.6% | 1.4/4.9% | 3 |
| 250 | 1 | 0.524 | 0.514 | 0.010 | - | - | 0.825 | 0.826 | 0.254 | 4.34x | 15.9/24.9/31.1% | 1.4/5.7% | 3 |
| 500 | 1 | 0.319 | 0.314 | 0.005 | - | - | 0.523 | 0.525 | 0.113 | 9.25x | 18.2/27.1/38.3% | 1.6/6.4% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 17

### `MS-roles` - role-mix  `--scenario coastal`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.936 | 0.931 | 0.004 | - | - | 0.987 | 0.988 | 0.712 | 1.38x | 20.1/28.3/28.8% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.962 | 0.963 | 0.577 | 1.20x | 18.1/26.9/29.4% | 2.0/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario coastal`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.941 | 0.937 | 0.003 | - | - | 0.979 | 0.983 | 0.708 | 1.39x | 20.1/27.8/28.7% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.893 | 0.889 | 0.004 | - | - | 0.943 | 0.945 | 0.650 | 1.39x | 20.3/31.5/33.6% | 2.4/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario coastal`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.05 | 1 | 0.938 | 0.932 | 0.006 | - | - | 0.980 | 0.984 | 0.721 | 1.51x | 21.7/33.5/36.0% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.934 | 0.930 | 0.005 | - | - | 0.976 | 0.979 | 0.708 | 1.63x | 24.1/40.0/43.3% | 2.4/5.4% | 3 |
| 0.2 | 1 | 0.945 | 0.941 | 0.004 | - | - | 0.983 | 0.986 | 0.728 | 1.84x | 28.0/44.0/49.6% | 2.6/5.3% | 3 |

> router-late-fraction=0.1: decode_failures 1

### `MS-siting` - siting-mix  `--scenario coastal`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| local-typical | 1 | 0.782 | 0.778 | 0.004 | - | - | 0.906 | 0.906 | 0.000 | 1.56x | 19.2/33.1/37.0% | 2.3/5.5% | 3 |
| event | 1 | 0.593 | 0.588 | 0.005 | - | - | 0.798 | 0.798 | 0.000 | 1.63x | 11.0/23.0/30.1% | 2.6/5.0% | 3 |
| backbone | 1 | 0.976 | 0.976 | 0.000 | - | - | 1.000 | 1.000 | 0.789 | 1.12x | 32.6/40.1/41.3% | 1.2/5.5% | 3 |

### `MS-size` - nodes  `--scenario coastal`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.908 | 0.902 | 0.006 | - | - | 0.969 | 0.970 | 0.800 | 1.60x | 30.8/41.6/45.8% | 3.9/8.1% | 3 |
| 60 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 90 | 1 | 0.881 | 0.879 | 0.002 | - | - | 0.982 | 0.983 | 0.623 | 1.69x | 16.4/28.0/32.6% | 1.6/5.4% | 3 |
| 120 | 1 | 0.816 | 0.810 | 0.006 | - | - | 0.970 | 0.970 | 0.428 | 2.13x | 15.2/25.1/30.8% | 1.5/5.2% | 3 |
| 150 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.965 | 0.966 | 0.352 | 2.74x | 16.0/27.3/38.7% | 1.5/5.7% | 3 |

### `MS-stretch` - stretch  `--scenario coastal`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 1.25 | 1 | 0.794 | 0.785 | 0.009 | - | - | 0.953 | 0.955 | 0.168 | 1.46x | 14.4/22.2/26.3% | 2.2/5.1% | 3 |
| 1.5 | 1 | 0.574 | 0.571 | 0.002 | - | - | 0.594 | 0.818 | 0.066 | 1.36x | 10.8/22.0/24.3% | 2.0/5.1% | 3 |
| 2.0 | 1 | 0.166 | 0.164 | 0.002 | - | - | 0.398 | 0.401 | 0.000 | 1.03x | 4.3/13.0/18.6% | 1.3/4.7% | 3 |

> stretch=1.5: decode_failures 2

### `MS-topology` - topology  `--scenario coastal`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| clustered | 1 | 0.938 | 0.932 | 0.006 | - | - | 0.994 | 0.994 | 0.000 | 1.17x | 30.5/37.9/39.8% | 1.3/5.7% | 3 |
| corridor | 1 | 0.604 | 0.570 | 0.034 | - | - | 0.877 | 0.880 | 0.280 | 1.26x | 16.2/22.3/27.0% | 1.9/5.7% | 3 |
| hub | 1 | 0.947 | 0.945 | 0.001 | - | - | 0.986 | 0.986 | 0.719 | 1.12x | 28.7/36.1/37.4% | 1.3/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario coastal`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.917 | 0.917 | 0.000 | - | - | 0.978 | 0.980 | 0.658 | 1.65x | 24.3/34.3/35.1% | 2.3/6.6% | 3 |
| True | 1 | 0.916 | 0.916 | 0.000 | - | - | 0.968 | 0.978 | 0.690 | 1.68x | 24.7/34.8/35.5% | 2.3/6.7% | 3 |

> coding-rate-ladder=True: decode_failures 1

### `PR-dmmode-cr` - dm-mode  `--scenario coastal`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.916 | 0.916 | 0.000 | - | - | 0.968 | 0.978 | 0.690 | 1.68x | 24.7/34.8/35.5% | 2.3/6.7% | 3 |
| m4-early-flood | 1 | 0.919 | 0.919 | 0.000 | - | - | 0.976 | 0.980 | 0.660 | 1.70x | 25.0/35.3/36.0% | 2.3/6.8% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 1

### `PR-protocol` - protocol  `--scenario coastal`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.938 | 0.938 | 0.000 | - | - | 0 | 0.000 | 0.694 | 1.30x | 18.9/26.7/27.2% | 1.8/5.1% | 3 |
| chain | 1 | 0.927 | 0.926 | 0.000 | - | - | 0.919 | 0.989 | 0.694 | 1.60x | 23.3/32.3/33.2% | 2.3/6.1% | 3 |
| sr | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario coastal`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| True | 1 | 0.942 | 0.938 | 0.005 | - | - | 0.988 | 0.990 | 0.753 | 1.40x | 20.2/28.5/28.9% | 2.0/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario coastal`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.974 | 0.971 | 0.003 | - | - | 0.998 | 0.998 | 0.916 | 2.03x | 23.9/41.5/44.9% | 1.3/5.2% | 3 |
| True | 1 | 0.973 | 0.970 | 0.003 | - | - | 0.997 | 0.998 | 0.918 | 2.06x | 24.1/41.8/45.1% | 1.3/5.2% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario coastal`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.196 | 0.194 | 0.002 | - | - | 0.451 | 0.492 | 0.000 | 0.05x | 0.2/0.7/1.0% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.589 | 0.586 | 0.003 | - | - | 0.600 | 0.897 | 0.013 | 0.31x | 2.4/5.7/6.4% | 0.4/1.4% | 3 |
| LONG_TURBO | 1 | 0.874 | 0.870 | 0.004 | - | - | 0.893 | 0.969 | 0.369 | 1.37x | 15.2/23.5/24.8% | 2.0/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 18

> preset=LONG_TURBO: decode_failures 30

> slower: 5.67 s per simulated hour against 1.43 over 9 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-duct` - duct-per-hour  `--scenario coastal`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.943 | 0.937 | 0.006 | - | - | 0.992 | 0.992 | 0.738 | 1.31x | 20.7/28.3/28.7% | 1.8/5.4% | 3 |
| 1.0 | 1 | 0.961 | 0.958 | 0.003 | - | - | 0.993 | 0.993 | 0.836 | 1.02x | 25.1/30.8/31.4% | 1.3/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario coastal`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.424 | 0.416 | 0.007 | - | - | 0.783 | 0.789 | 0.041 | 0.16x | 1.1/2.3/3.0% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| LITE_FAST | 1 | 0.899 | 0.896 | 0.003 | - | - | 0.984 | 0.985 | 0.436 | 1.04x | 13.2/20.7/23.0% | 1.5/4.1% | 3 |
| NARROW_SLOW | 1 | 0.907 | 0.903 | 0.004 | - | - | 0.972 | 0.975 | 0.437 | 1.34x | 18.2/27.4/29.0% | 1.9/5.3% | 3 |

### `RF-noise` - noise-profile  `--scenario coastal`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| temporal | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.904 | 0.970 | 0.563 | 1.43x | 20.1/28.2/28.9% | 2.2/5.3% | 3 |
| transient | 1 | 0.936 | 0.930 | 0.006 | - | - | 0.986 | 0.987 | 0.726 | 1.38x | 20.1/28.1/28.6% | 2.0/5.4% | 3 |
| periodic | 1 | 0.792 | 0.785 | 0.006 | - | - | 0.833 | 0.848 | 0.604 | 1.27x | 18.8/26.3/26.8% | 1.8/4.6% | 3 |

> noise-profile=temporal: decode_failures 32

> noise-profile=periodic: decode_failures 11

### `RF-preset` - preset  `--scenario coastal`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.424 | 0.416 | 0.007 | - | - | 0.783 | 0.789 | 0.041 | 0.16x | 1.1/2.3/3.0% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| LONG_MODERATE | 1 | 0.860 | 0.856 | 0.004 | - | - | 0.905 | 0.933 | 0.735 | 3.63x | 57.4/70.5/72.6% | 5.2/13.0% | 3 |

> preset=LONG_MODERATE: decode_failures 56

> slower: 6.03 s per simulated hour against 2.94 over 9 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset-turbo` - preset  `--scenario coastal`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.096 | 0.096 | 0.000 | - | - | 0.275 | 0.275 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.1% | 3 |
| SHORT_TURBO | 1 | 0.196 | 0.194 | 0.002 | - | - | 0.451 | 0.492 | 0.000 | 0.05x | 0.2/0.7/1.0% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| LONG_TURBO | 1 | 0.874 | 0.870 | 0.004 | - | - | 0.893 | 0.969 | 0.369 | 1.37x | 15.2/23.5/24.8% | 2.0/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.920 | 0.916 | 0.004 | - | - | 0.976 | 0.977 | 0.739 | 1.95x | 26.8/38.1/40.1% | 2.9/7.1% | 3 |

> preset=SHORT_TURBO: decode_failures 18

> preset=LONG_TURBO: decode_failures 30

> slower: 3.94 s per simulated hour against 1.59 over 5 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario coastal`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.933 | 0.941 | 0.689 | 1.35x | 19.9/27.9/28.4% | 1.9/5.1% | 3 |
| 10000 | 1 | 0.792 | 0.785 | 0.006 | - | - | 0.833 | 0.848 | 0.604 | 1.27x | 18.8/26.3/26.8% | 1.8/4.6% | 3 |
| 4000 | 1 | 0.543 | 0.539 | 0.003 | - | - | 0.556 | 0.616 | 0.355 | 1.13x | 16.8/23.6/24.4% | 1.7/3.6% | 3 |
| 2000 | 1 | 0.165 | 0.165 | 0.000 | - | - | 0.171 | 0.239 | 0.072 | 0.79x | 12.2/18.1/19.2% | 1.2/2.1% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 6

> noise-pulse-interval-ms=10000: decode_failures 11

> noise-pulse-interval-ms=4000: decode_failures 6

### `RF-stretch-duct` - duct-per-hour  `--scenario coastal`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.574 | 0.571 | 0.002 | - | - | 0.594 | 0.818 | 0.066 | 1.36x | 10.8/22.0/24.3% | 2.0/5.1% | 3 |
| 1.0 | 1 | 0.786 | 0.766 | 0.020 | - | - | 0.831 | 0.914 | 0.471 | 1.18x | 19.1/28.2/30.2% | 1.6/5.3% | 3 |

> duct-per-hour=0.0: decode_failures 2

> duct-per-hour=1.0: decode_failures 46

> slower: 7.83 s per simulated hour against 1.72 over 9 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario coastal`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 22 | 1 | 0.551 | 0.548 | 0.004 | - | - | 0.616 | 0.811 | 0.042 | 1.36x | 10.0/20.9/24.3% | 2.0/5.1% | 3 |
| 17 | 1 | 0.192 | 0.190 | 0.002 | - | - | 0.427 | 0.431 | 0.000 | 1.13x | 4.4/14.3/21.2% | 1.4/4.9% | 3 |
| 14 | 1 | 0.112 | 0.111 | 0.001 | - | - | 0.261 | 0.276 | 0.000 | 0.82x | 3.4/8.9/13.7% | 1.0/3.6% | 3 |

> tx-power=22: decode_failures 6

> tx-power=14: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario coastal`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.974 | 0.971 | 0.003 | - | - | 0.998 | 0.998 | 0.916 | 2.03x | 23.9/41.5/44.9% | 1.3/5.2% | 3 |
| True | 1 | 0.966 | 0.962 | 0.004 | - | - | 0.996 | 0.996 | 0.892 | 2.36x | 27.3/46.5/50.0% | 1.5/5.8% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario coastal`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.939 | 0.933 | 0.006 | - | - | 0.985 | 0.986 | 0.727 | 1.49x | 21.5/31.7/34.0% | 2.1/5.4% | 3 |
| True | 1 | 0.949 | 0.945 | 0.005 | - | - | 0.984 | 0.985 | 0.736 | 1.59x | 22.9/32.9/34.8% | 2.2/5.5% | 3 |

### `RT-hopassign` - hop-assign  `--scenario coastal`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| random | 1 | 0.929 | 0.920 | 0.009 | - | - | 0.987 | 0.990 | 0.740 | 1.38x | 20.1/28.3/28.8% | 1.9/5.3% | 3 |

> hop-assign=random: decode_failures 2

### `RT-hoplimit` - hop-limit  `--scenario coastal`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.845 | 0.822 | 0.023 | - | - | 0.978 | 0.980 | 0.509 | 1.06x | 16.6/24.1/25.2% | 1.4/4.8% | 3 |
| 7 | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.986 | 0.989 | 0.784 | 1.51x | 21.9/29.8/30.8% | 2.1/5.7% | 3 |
| 15 | 1 | 0.957 | 0.954 | 0.003 | - | - | 0.987 | 0.988 | 0.774 | 1.50x | 21.6/29.4/30.5% | 2.1/5.6% | 3 |
| 32 | 1 | 0.960 | 0.958 | 0.002 | - | - | 0.990 | 0.992 | 0.771 | 1.50x | 21.4/29.3/30.3% | 2.1/5.6% | 3 |

### `RT-hopspread` - hop-limit  `--scenario coastal`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.845 | 0.822 | 0.023 | - | - | 0.978 | 0.980 | 0.509 | 1.06x | 16.6/24.1/25.2% | 1.4/4.8% | 3 |
| 5 | 1 | 0.940 | 0.935 | 0.005 | - | - | 0.986 | 0.988 | 0.774 | 1.37x | 20.3/28.3/28.8% | 1.9/5.5% | 3 |
| 7 | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.986 | 0.989 | 0.784 | 1.51x | 21.9/29.8/30.8% | 2.1/5.7% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario coastal`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.938 | 0.938 | 0.000 | - | - | 0.930 | 0.994 | 0.692 | 1.32x | 19.2/27.1/27.7% | 1.9/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario coastal`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.845 | 0.822 | 0.023 | - | - | 0.978 | 0.980 | 0.509 | 1.06x | 16.6/24.1/25.2% | 1.4/4.8% | 3 |
| True | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario coastal`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| BALANCED | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| STRICT | 1 | 0.809 | 0.809 | 0.000 | - | - | 0.856 | 0.860 | 0.597 | 1.51x | 21.8/30.2/30.9% | 2.2/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario coastal`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| dm | 1 | 0.940 | 0.935 | 0.005 | - | - | 0.990 | 0.992 | 0.731 | 1.33x | 19.7/27.8/28.2% | 1.9/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario coastal`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.944 | 0.939 | 0.005 | - | - | 0.990 | 0.995 | 0.726 | 1.37x | 20.0/28.2/28.6% | 1.9/5.3% | 3 |
| local | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| time | 1 | 0.939 | 0.934 | 0.005 | - | - | 0.987 | 0.992 | 0.737 | 1.41x | 20.6/28.9/29.5% | 2.0/5.5% | 3 |
| window | 1 | 0.937 | 0.931 | 0.006 | - | - | 0.986 | 0.988 | 0.729 | 1.36x | 19.9/28.0/28.5% | 1.9/5.3% | 3 |

> bucket-mode=global: misdecodes 16

> bucket-mode=time: misdecodes 40

> bucket-mode=window: misdecodes 11

### `SF-bucket-time` - time-bucket-s  `--scenario coastal`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.925 | 0.919 | 0.006 | - | - | 0.973 | 0.980 | 0.721 | 1.52x | 22.2/31.0/31.5% | 2.1/6.0% | 3 |
| 1800 | 1 | 0.939 | 0.934 | 0.005 | - | - | 0.987 | 0.992 | 0.737 | 1.41x | 20.6/28.9/29.5% | 2.0/5.5% | 3 |
| 3600 | 1 | 0.935 | 0.931 | 0.004 | - | - | 0.980 | 0.984 | 0.725 | 1.36x | 19.9/28.1/28.5% | 1.9/5.3% | 3 |

> time-bucket-s=600: misdecodes 116

> time-bucket-s=1800: misdecodes 40

> time-bucket-s=3600: misdecodes 10

### `SF-cadence` - trigger  `--scenario coastal`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| interval | 1 | 0.930 | 0.922 | 0.007 | - | - | 0.979 | 0.984 | 0.730 | 1.89x | 27.6/38.5/40.2% | 2.7/8.6% | 3 |
| aimd | 1 | 0.931 | 0.929 | 0.001 | - | - | 0.930 | 0.986 | 0.708 | 1.39x | 20.3/28.4/29.0% | 2.0/5.3% | 3 |
| bucket+interval | 1 | 0.928 | 0.920 | 0.008 | - | - | 0.984 | 0.984 | 0.721 | 1.92x | 28.0/39.1/40.8% | 2.8/8.7% | 3 |

> trigger=interval: misdecodes 16

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 9

> trigger=bucket+interval: misdecodes 23

### `SF-capacity` - capacity  `--scenario coastal`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.933 | 0.928 | 0.005 | - | - | 0.977 | 0.986 | 0.713 | 1.35x | 19.9/28.0/28.3% | 1.9/5.4% | 3 |
| 8 | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.981 | 0.991 | 0.723 | 1.38x | 20.3/28.5/28.9% | 1.9/5.5% | 3 |
| 16 | 1 | 0.941 | 0.936 | 0.005 | - | - | 0.990 | 0.991 | 0.733 | 1.37x | 20.1/28.2/28.6% | 1.9/5.4% | 3 |
| 32 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 50 | 1 | 0.937 | 0.932 | 0.005 | - | - | 0.986 | 0.986 | 0.713 | 1.38x | 20.1/28.2/28.7% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 99

> capacity=8: decode_failures 83

### `SF-capacity-local` - capacity  `--scenario coastal`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.933 | 0.928 | 0.005 | - | - | 0.977 | 0.986 | 0.713 | 1.35x | 19.9/28.0/28.3% | 1.9/5.4% | 3 |
| 8 | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.981 | 0.991 | 0.723 | 1.38x | 20.3/28.5/28.9% | 1.9/5.5% | 3 |
| 16 | 1 | 0.941 | 0.936 | 0.005 | - | - | 0.990 | 0.991 | 0.733 | 1.37x | 20.1/28.2/28.6% | 1.9/5.4% | 3 |
| 32 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 50 | 1 | 0.937 | 0.932 | 0.005 | - | - | 0.986 | 0.986 | 0.713 | 1.38x | 20.1/28.2/28.7% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 99

> capacity=8: decode_failures 83

### `SF-capacity-window` - capacity  `--scenario coastal`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.937 | 0.935 | 0.002 | - | - | 0.958 | 0.988 | 0.709 | 1.35x | 19.7/27.7/28.2% | 1.9/5.2% | 3 |
| 16 | 1 | 0.935 | 0.929 | 0.006 | - | - | 0.984 | 0.986 | 0.724 | 1.37x | 20.0/28.2/28.6% | 1.9/5.4% | 3 |
| 32 | 1 | 0.937 | 0.931 | 0.006 | - | - | 0.986 | 0.988 | 0.729 | 1.36x | 19.9/28.0/28.5% | 1.9/5.3% | 3 |

> capacity=8: misdecodes 5

> capacity=8: decode_failures 48

> capacity=16: misdecodes 22

> capacity=32: misdecodes 11

### `SF-catchup` - catch-up-hours  `--scenario coastal`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.928 | 0.920 | 0.008 | - | - | 0.984 | 0.984 | 0.721 | 1.92x | 28.0/39.1/40.8% | 2.8/8.7% | 3 |
| 02-06 | 1 | 0.930 | 0.927 | 0.003 | - | - | 0.947 | 0.984 | 0.715 | 1.41x | 20.6/29.0/29.4% | 2.0/5.6% | 3 |
| 00-08 | 1 | 0.933 | 0.930 | 0.004 | - | - | 0.954 | 0.988 | 0.720 | 1.49x | 21.8/30.5/31.3% | 2.1/6.1% | 3 |

> catch-up-hours=: misdecodes 23

> catch-up-hours=02-06: decode_failures 43

> catch-up-hours=00-08: decode_failures 41

### `SF-hops-flat` - hops-apart  `--scenario coastal`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.927 | 0.927 | 0.000 | - | - | 0.982 | 0.982 | 0.673 | 1.37x | 20.0/28.1/28.7% | 2.0/5.4% | 3 |
| 2 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 3 | 1 | 0.938 | 0.929 | 0.008 | - | - | 0.988 | 0.989 | 0.667 | 1.36x | 19.8/27.9/28.4% | 1.9/5.3% | 3 |
| 4 | 1 | 0.942 | 0.931 | 0.011 | - | - | 0.985 | 0.987 | 0.685 | 1.39x | 20.2/28.3/29.0% | 2.0/5.4% | 3 |

### `SF-hops-spread` - hops-apart  `--scenario coastal`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.927 | 0.927 | 0.000 | - | - | 0.982 | 0.982 | 0.673 | 1.37x | 20.0/28.1/28.7% | 2.0/5.4% | 3 |
| 2 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 3 | 1 | 0.938 | 0.929 | 0.008 | - | - | 0.988 | 0.989 | 0.667 | 1.36x | 19.8/27.9/28.4% | 1.9/5.3% | 3 |
| 4 | 1 | 0.942 | 0.931 | 0.011 | - | - | 0.985 | 0.987 | 0.685 | 1.39x | 20.2/28.3/29.0% | 2.0/5.4% | 3 |
| 5 | 1 | 0.942 | 0.931 | 0.011 | - | - | 0.985 | 0.987 | 0.685 | 1.39x | 20.2/28.3/29.0% | 2.0/5.4% | 3 |

> faster: 2.22 s per simulated hour against 4.81 over 9 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario coastal`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.945 | 0.939 | 0.005 | - | - | 0.994 | 0.995 | 0.737 | 1.36x | 19.8/27.9/28.3% | 1.9/5.3% | 3 |
| 30 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 120 | 1 | 0.943 | 0.938 | 0.004 | - | - | 0.991 | 0.992 | 0.741 | 1.38x | 20.3/28.5/28.9% | 1.9/5.4% | 3 |
| 600 | 1 | 0.938 | 0.933 | 0.005 | - | - | 0.989 | 0.989 | 0.748 | 1.37x | 19.9/28.1/28.6% | 1.9/5.3% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario coastal`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.945 | 0.939 | 0.005 | - | - | 0.994 | 0.995 | 0.737 | 1.36x | 19.8/27.9/28.3% | 1.9/5.3% | 3 |
| 30 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 120 | 1 | 0.943 | 0.938 | 0.004 | - | - | 0.991 | 0.992 | 0.741 | 1.38x | 20.3/28.5/28.9% | 1.9/5.4% | 3 |
| 600 | 1 | 0.938 | 0.933 | 0.005 | - | - | 0.989 | 0.989 | 0.748 | 1.37x | 19.9/28.1/28.6% | 1.9/5.3% | 3 |

### `SF-place-flat` - place  `--scenario coastal`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.943 | 0.933 | 0.010 | - | - | 0.991 | 0.992 | 0.691 | 1.38x | 20.1/28.1/28.8% | 1.9/5.3% | 3 |
| routers | 1 | 0.931 | 0.930 | 0.001 | - | - | 0.986 | 0.986 | 0.703 | 1.35x | 19.6/27.7/28.3% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.934 | 0.933 | 0.001 | - | - | 0.989 | 0.989 | 0.687 | 1.36x | 19.8/27.9/28.6% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.934 | 0.934 | 0.001 | - | - | 0.991 | 0.992 | 0.664 | 1.37x | 20.1/28.2/28.8% | 1.9/5.4% | 3 |
| random-clients | 1 | 0.939 | 0.933 | 0.006 | - | - | 0.979 | 0.990 | 0.698 | 1.39x | 20.1/28.3/29.0% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

> place=random-clients: decode_failures 7

### `SF-place-spread` - place  `--scenario coastal`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.943 | 0.933 | 0.010 | - | - | 0.991 | 0.992 | 0.691 | 1.38x | 20.1/28.1/28.8% | 1.9/5.3% | 3 |
| routers | 1 | 0.931 | 0.930 | 0.001 | - | - | 0.986 | 0.986 | 0.703 | 1.35x | 19.6/27.7/28.3% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.934 | 0.933 | 0.001 | - | - | 0.989 | 0.989 | 0.687 | 1.36x | 19.8/27.9/28.6% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.934 | 0.934 | 0.001 | - | - | 0.991 | 0.992 | 0.664 | 1.37x | 20.1/28.2/28.8% | 1.9/5.4% | 3 |
| random-clients | 1 | 0.939 | 0.933 | 0.006 | - | - | 0.979 | 0.990 | 0.698 | 1.39x | 20.1/28.3/29.0% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

> place=random-clients: decode_failures 7

### `SF-provide-transport` - provide-transport  `--scenario coastal`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| broadcast | 1 | 0.943 | 0.929 | 0.013 | - | - | 0.978 | 0.986 | 0.750 | 1.44x | 21.0/29.2/29.8% | 2.0/5.6% | 3 |

> provide-transport=broadcast: decode_failures 4

### `SF-replay-order` - replay-ordering  `--scenario coastal`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| heard | 1 | 0.936 | 0.931 | 0.005 | - | - | 0.986 | 0.987 | 0.733 | 1.38x | 20.3/28.5/28.9% | 1.9/5.4% | 3 |

> replay-ordering=heard: misdecodes 9

### `SF-replay-order-broadcast` - replay-ordering  `--scenario coastal`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.943 | 0.929 | 0.013 | - | - | 0.978 | 0.986 | 0.750 | 1.44x | 21.0/29.2/29.8% | 2.0/5.6% | 3 |
| heard | 1 | 0.944 | 0.932 | 0.013 | - | - | 0.985 | 0.987 | 0.764 | 1.45x | 21.1/29.5/30.0% | 2.0/5.6% | 3 |

> replay-ordering=tip: decode_failures 4

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario coastal`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| enum | 1 | 0.939 | 0.935 | 0.004 | - | - | 0.982 | 0.989 | 0.721 | 1.34x | 19.8/27.9/28.3% | 1.9/5.4% | 3 |
| hybrid | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario coastal`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.931 | 0.930 | 0.001 | - | - | 0.986 | 0.986 | 0.703 | 1.35x | 19.6/27.7/28.3% | 1.9/5.3% | 3 |
| 6 | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.990 | 0.991 | 0.694 | 1.37x | 20.0/28.3/28.9% | 1.9/5.5% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario coastal`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.937 | 0.936 | 0.001 | - | - | 0.992 | 0.992 | 0.693 | 1.36x | 19.8/27.8/28.4% | 1.9/5.3% | 2 |
| 3 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 5 | 1 | 0.936 | 0.931 | 0.006 | - | - | 0.991 | 0.991 | 0.721 | 1.37x | 20.0/28.2/28.7% | 1.9/5.4% | 5 |
| 8 | 1 | 0.934 | 0.927 | 0.007 | - | - | 0.987 | 0.988 | 0.725 | 1.43x | 20.9/29.3/29.7% | 2.0/5.6% | 8 |

> servers=5: misdecodes 1

### `SF-servers-spread` - servers  `--scenario coastal`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.937 | 0.936 | 0.001 | - | - | 0.992 | 0.992 | 0.693 | 1.36x | 19.8/27.8/28.4% | 1.9/5.3% | 2 |
| 3 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 5 | 1 | 0.936 | 0.931 | 0.006 | - | - | 0.991 | 0.991 | 0.721 | 1.37x | 20.0/28.2/28.7% | 1.9/5.4% | 5 |
| 8 | 1 | 0.934 | 0.927 | 0.007 | - | - | 0.987 | 0.988 | 0.725 | 1.43x | 20.9/29.3/29.7% | 2.0/5.6% | 8 |

> servers=5: misdecodes 1

### `SF-signed` - signed  `--scenario coastal`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| True | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario coastal`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.932 | 0.930 | 0.002 | - | - | 0.944 | 0.983 | 0.694 | 1.28x | 18.8/26.4/27.0% | 1.8/5.0% | 3 |
| 1 | 1 | 0.941 | 0.936 | 0.005 | - | - | 0.989 | 0.990 | 0.747 | 1.27x | 18.5/26.0/26.5% | 1.8/4.9% | 3 |
| 2 | 1 | 0.939 | 0.933 | 0.006 | - | - | 0.987 | 0.988 | 0.711 | 1.28x | 18.9/26.5/27.0% | 1.8/5.0% | 3 |
| 4 | 1 | 0.933 | 0.929 | 0.004 | - | - | 0.982 | 0.982 | 0.691 | 1.25x | 18.4/25.9/26.4% | 1.7/5.0% | 3 |

> sr-retries=0: decode_failures 24

> slower: 4.2 s per simulated hour against 1.7 over 9 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario coastal`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.939 | 0.933 | 0.006 | - | - | 0.985 | 0.989 | 0.736 | 1.35x | 19.9/28.1/28.5% | 1.9/5.3% | 3 |
| 24 | 1 | 0.941 | 0.936 | 0.005 | - | - | 0.990 | 0.991 | 0.737 | 1.37x | 20.0/28.1/28.5% | 1.9/5.3% | 3 |
| 32 | 1 | 0.940 | 0.934 | 0.005 | - | - | 0.987 | 0.988 | 0.736 | 1.38x | 20.2/28.4/28.9% | 1.9/5.4% | 3 |
| 64 | 1 | 0.932 | 0.928 | 0.004 | - | - | 0.979 | 0.982 | 0.722 | 1.39x | 20.3/28.5/29.1% | 1.9/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario coastal`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.935 | 0.928 | 0.008 | - | - | 0.984 | 0.990 | 0.731 | 1.47x | 21.5/30.0/30.6% | 2.1/5.7% | 3 |
| 16 | 1 | 0.936 | 0.929 | 0.006 | - | - | 0.986 | 0.988 | 0.749 | 1.39x | 20.3/28.5/29.0% | 1.9/5.5% | 3 |
| 32 | 1 | 0.937 | 0.931 | 0.006 | - | - | 0.986 | 0.988 | 0.729 | 1.36x | 19.9/28.0/28.5% | 1.9/5.3% | 3 |

> window-size=8: misdecodes 124

> window-size=16: misdecodes 65

> window-size=32: misdecodes 11

### `TH-congestion` - no-congestion-scaling  `--scenario coastal`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.974 | 0.971 | 0.003 | - | - | 0.998 | 0.998 | 0.916 | 2.03x | 23.9/41.5/44.9% | 1.3/5.2% | 3 |
| True | 1 | 0.733 | 0.723 | 0.010 | - | - | 0.808 | 0.853 | 0.570 | 5.37x | 58.9/77.2/80.3% | 4.0/12.5% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: queue drops 24.9% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 103

### `TH-congestion-input` - congestion-input  `--scenario coastal`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.524 | 0.514 | 0.010 | - | - | 0.825 | 0.826 | 0.254 | 4.34x | 15.9/24.9/31.1% | 1.4/5.7% | 3 |
| truesize | 1 | 0.554 | 0.544 | 0.010 | - | - | 0.866 | 0.867 | 0.252 | 3.32x | 11.8/19.8/24.7% | 1.1/4.8% | 3 |

> congestion-input=hotstore: decode_failures 1

> congestion-input=truesize: decode_failures 2

### `TH-congestion-mode` - congestion-mode  `--scenario coastal`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.976 | 0.974 | 0.002 | - | - | 0.998 | 0.998 | 0.931 | 1.85x | 21.7/38.0/41.1% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.974 | 0.971 | 0.003 | - | - | 0.998 | 0.998 | 0.916 | 2.03x | 23.9/41.5/44.9% | 1.3/5.2% | 3 |

> congestion-mode=adaptive: misdecodes 1

