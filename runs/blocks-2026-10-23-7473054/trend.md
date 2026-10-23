# Sweep blocks-2026-10-23-7473054

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 7473054 · seeds 7473054
- **blocks** 87 run
- **compute** 10.4 h of simulator time across every cell
- **generated** 2026-10-23T09:13:52+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>90 warnings</summary>

- AD-badrouters: faster: 0.944 s per simulated hour against 2 over 63 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-flooding: slower: 10.8 s per simulated hour against 2.5 over 63 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=basement-heavy: decode_failures 2
- AD-worst: role-placement=degree: decode_failures 93
- AD-worst: role-placement=inverse: decode_failures 89
- AD-worst: slower: 23.6 s per simulated hour against 3.37 over 63 prior run(s) - 7.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 78
- DB-hotstore-stress: max-num-nodes=120: decode_failures 11
- DB-platform: platform-mix=constrained: decode_failures 1
- DB-warm: warm-num-nodes=0: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 113
- DB-warm: warm-num-nodes=25: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 113
- DB-warm: warm-num-nodes=100: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 113
- DB-warm: warm-num-nodes=2000: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 113
- DG-burst: burst-loss=0.2: decode_failures 35
- DG-burst: burst-loss=0.3: decode_failures 22
- DG-loss: extra-loss=0.3: decode_failures 19
- DG-outage: burst-loss=0.1: decode_failures 5
- DG-outage: burst-loss=0.2: decode_failures 34
- DG-outage: burst-loss=0.3: decode_failures 29
- LD-chatty-hops: broadcast-interval-s=300: queue drops 10.8% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 28
- LD-chatty: broadcast-interval-s=300: decode_failures 26
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 19.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 113
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 28.3% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 102
- MS-density: nodes=120: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 23
- MS-hopscale: faster: 7.32 s per simulated hour against 17.3 over 63 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-oversubscribed: nodes=250: decode_failures 11
- MS-siting: faster: 0.908 s per simulated hour against 1.84 over 62 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-stretch: stretch=1.25: decode_failures 18
- MS-stretch: stretch=1.5: decode_failures 2
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 3
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 33
- RF-bw500: slower: 4.89 s per simulated hour against 1.95 over 63 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=SHORT_FAST: decode_failures 19
- RF-preset: preset=SHORT_FAST: decode_failures 19
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 3
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 11
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 2
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 1
- RF-txpower: tx-power=22: decode_failures 3
- RF-txpower: tx-power=17: decode_failures 3
- RF-txpower: tx-power=14: decode_failures 14
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-hoplimit: hop-limit=15: misdecodes 1
- RT-hoplimit: hop-limit=32: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 34
- SF-bucket-mode: bucket-mode=time: misdecodes 37
- SF-bucket-mode: bucket-mode=window: misdecodes 24
- SF-bucket-time: time-bucket-s=600: misdecodes 135
- SF-bucket-time: time-bucket-s=1800: misdecodes 37
- SF-bucket-time: time-bucket-s=3600: misdecodes 9
- SF-cadence: trigger=interval: misdecodes 22
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 2
- SF-cadence: trigger=bucket+interval: misdecodes 28
- SF-capacity-local: capacity=4: decode_failures 51
- SF-capacity-local: capacity=8: decode_failures 8
- SF-capacity: capacity=4: decode_failures 51
- SF-capacity: capacity=8: decode_failures 8
- SF-capacity-window: capacity=8: misdecodes 33
- SF-capacity-window: capacity=8: decode_failures 12
- SF-capacity-window: capacity=16: misdecodes 16
- SF-capacity-window: capacity=16: decode_failures 2
- SF-capacity-window: capacity=32: misdecodes 24
- SF-catchup: catch-up-hours=: misdecodes 28
- SF-catchup: catch-up-hours=02-06: decode_failures 39
- SF-catchup: catch-up-hours=00-08: decode_failures 39
- SF-hops-flat: faster: 1.09 s per simulated hour against 4.03 over 63 prior run(s) - 3.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: faster: 1.95 s per simulated hour against 4.52 over 63 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=spread: decode_failures 39
- SF-place-spread: place=spread: decode_failures 39
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 12
- SF-replay-order: replay-ordering=heard: misdecodes 20
- SF-window-size: window-size=8: misdecodes 140
- SF-window-size: window-size=16: misdecodes 35
- SF-window-size: window-size=32: misdecodes 24
- TH-congestion-input: congestion-input=hotstore: decode_failures 11
- TH-congestion-mode: congestion-mode=static: misdecodes 1
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 16.9% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 83

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 23.6 | 3.37 | 7.01x | 63 |
| `AD-flooding` | 10.8 | 2.5 | 4.34x | 63 |
| `RF-bw500` | 4.89 | 1.95 | 2.50x | 63 |
| `RF-stretch-duct` | 3.4 | 1.84 | 1.85x | 63 |
| `RF-txpower` | 2.53 | 1.58 | 1.60x | 63 |
| `RF-eu-presets` | 2.95 | 1.85 | 1.59x | 63 |
| `MS-stretch` | 3.14 | 2.04 | 1.54x | 63 |
| `SF-jitter-local` | 1.17 | 1.79 | 0.66x | 63 |
| `RT-adopt` | 2.52 | 3.87 | 0.65x | 63 |
| `AD-amplifiers` | 1.01 | 1.6 | 0.63x | 63 |
| `AD-nomute` | 1.44 | 2.28 | 0.63x | 63 |
| `RT-hoplimit` | 1.05 | 1.74 | 0.60x | 63 |
| `PR-dmmode-cr` | 1.56 | 2.6 | 0.60x | 63 |
| `MS-topology` | 1.12 | 1.9 | 0.59x | 63 |
| `SC-signing` | 1.05 | 1.79 | 0.59x | 63 |
| `FW-firmware` | 0.953 | 1.65 | 0.58x | 63 |
| `MS-size` | 1.92 | 3.39 | 0.56x | 63 |
| `SF-capacity-local` | 0.974 | 1.74 | 0.56x | 63 |
| `AD-siting` | 0.805 | 1.45 | 0.56x | 63 |
| `SF-width` | 0.912 | 1.66 | 0.55x | 63 |
| `FW-signing-cost` | 0.838 | 1.58 | 0.53x | 63 |
| `MS-siting` | 0.908 | 1.84 | 0.49x | 62 |
| `AD-badrouters` | 0.944 | 2 | 0.47x | 63 |
| `SF-hops-spread` | 1.95 | 4.52 | 0.43x | 63 |
| `MS-hopscale` | 7.32 | 17.3 | 0.42x | 63 |
| `SF-hops-flat` | 1.09 | 4.03 | 0.27x | 63 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.973 | 0.973 | 0.892 → 0.903 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.953 | 0.953 | 0.885 → 0.903 | 1.2x bytes_on_air | up | 3 |
| `MS-stretch` | stretch | **held** | 0.090 → 0.953 | 0.863 | 0.154 → 0.896 | 16x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.055 → 0.906 | 0.850 | 0.054 → 0.896 | 8.2x advert_bytes | up | 5 |
| `AD-siting` | siting-mix | **text** | 0.051 → 0.877 | 0.826 | 0.050 → 0.865 | 5.7x advert_bytes | down | 3 |
| `RF-txpower` | tx-power | **text** | 0.092 → 0.906 | 0.814 | 0.090 → 0.896 | 6.6x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.095 → 0.893 | 0.798 | 0.113 → 0.839 | 1.5e+02x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.249 → 0.915 | 0.665 | 0.205 → 0.835 | 5.3x sr_bytes | up | 3 |
| `RF-eu-presets` | preset | **held** | 0.361 → 0.964 | 0.603 | 0.399 → 0.896 | 4.7x sr_airtime | up | 4 |
| `MS-siting` | siting-mix | **text** | 0.386 → 0.981 | 0.595 | 0.372 → 0.981 | 2.1x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.361 → 0.953 | 0.592 | 0.399 → 0.896 | 5.6x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.368 → 0.955 | 0.587 | 0.320 → 0.896 | 10x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.375 → 0.948 | 0.572 | 0.324 → 0.795 | 4.8x bytes_on_air | down | 3 |
| `MS-topology` | topology | **held** | 0.588 → 0.990 | 0.402 | 0.558 → 0.956 | 3.1x sr_airtime | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.589 → 0.958 | 0.369 | 0.577 → 0.956 | 11x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.581 → 0.934 | 0.353 | 0.559 → 0.928 | 8.1x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.569 → 0.906 | 0.337 | 0.544 → 0.896 | 3x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.607 → 0.906 | 0.299 | 0.572 → 0.896 | 2.6x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.588 → 0.851 | 0.263 | 0.326 → 0.527 | 4.8x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.447 → 0.674 | 0.227 | 0.431 → 0.649 | 1.3x bytes_on_air | up | 2 |
| `MS-density` | nodes | **text** | 0.781 → 0.975 | 0.194 | 0.774 → 0.974 | 5.5x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.770 → 0.957 | 0.187 | 0.728 → 0.956 | 2.5x sr_bytes | up | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.798 → 0.975 | 0.177 | 0.785 → 0.974 | 3.9x sr_airtime | down | 2 |
| `RT-hopspread` | hop-limit | **text** | 0.770 → 0.946 | 0.176 | 0.728 → 0.944 | 2.4x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.798 → 0.961 | 0.163 | 0.743 → 0.901 | 1.6x sr_bytes | down | 4 |
| `MS-size` | nodes | **text** | 0.756 → 0.906 | 0.150 | 0.748 → 0.896 | 4.3x sr_airtime | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.770 → 0.906 | 0.136 | 0.728 → 0.896 | 2.1x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.794 → 0.906 | 0.112 | 0.794 → 0.896 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.804 → 0.906 | 0.102 | 0.785 → 0.896 | 1.8x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.837 → 0.931 | 0.094 | 0.820 → 0.927 | 2.4x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.840 → 0.931 | 0.091 | 0.824 → 0.927 | 2.4x sr_airtime | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.860 → 0.947 | 0.087 | 0.843 → 0.944 | 5x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.779 → 0.854 | 0.075 | 0.703 → 0.769 | 1.4x sr_airtime | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.877 → 0.944 | 0.067 | 0.865 → 0.937 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.877 → 0.944 | 0.067 | 0.865 → 0.937 | 2.5x bytes_on_air | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.906 → 0.969 | 0.064 | 0.896 → 0.966 | 1.5x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.906 → 0.967 | 0.061 | 0.896 → 0.965 | 2.2x sr_bytes | up | 3 |
| `AD-worst` | role-placement | **text** | 0.750 → 0.804 | 0.053 | 0.722 → 0.790 | 1.1x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **text** | 0.877 → 0.924 | 0.047 | 0.865 → 0.915 | 1.2x bytes_on_air | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.908 → 0.953 | 0.045 | 0.896 → 0.899 | 28x sr_airtime | down | 3 |
| `FW-versions` | profile | **text** | 0.906 → 0.951 | 0.045 | 0.896 → 0.947 | 3.4x bytes_on_air | down | 5 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.866 → 0.906 | 0.040 | 0.852 → 0.896 | 1.5x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.916 → 0.953 | 0.037 | 0.858 → 0.902 | 17x sr_bytes | down | 4 |
| `FW-firmware` | profile | **held** | 0.953 → 0.990 | 0.037 | 0.896 → 0.928 | 3.3x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **held** | 0.953 → 0.989 | 0.036 | 0.896 → 0.920 | 2.3x bytes_on_air | up | 4 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.953 → 0.989 | 0.036 | 0.896 → 0.919 | 2.3x bytes_on_air | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.906 → 0.941 | 0.036 | 0.896 → 0.937 | 3.4x bytes_on_air | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.903 → 0.937 | 0.035 | 0.900 → 0.931 | 1.2x sr_bytes | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.953 → 0.987 | 0.034 | 0.892 → 0.900 | 2.1x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.953 → 0.987 | 0.034 | 0.892 → 0.900 | 2.2x sr_bytes | up | 5 |
| `RF-duct` | duct-per-hour | **text** | 0.906 → 0.939 | 0.033 | 0.896 → 0.932 | 1.3x bytes_on_air | up | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.534 → 0.564 | 0.030 | 0.524 → 0.555 | 1.4x sr_airtime | up | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.953 → 0.982 | 0.029 | 0.896 → 0.923 | 1.3x bytes_on_air | up | 4 |
| `SF-place-flat` | place | **text** | 0.898 → 0.925 | 0.027 | 0.891 → 0.901 | 5.3x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.898 → 0.925 | 0.027 | 0.891 → 0.901 | 5.3x sr_bytes | down | 6 |
| `AD-badrouters` | role-placement | **text** | 0.852 → 0.877 | 0.024 | 0.838 → 0.865 | 1.3x sr_bytes | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.857 → 0.881 | 0.024 | 0.857 → 0.881 | 1.2x sr_airtime | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.950 → 0.973 | 0.023 | 0.889 → 0.899 | 6.3x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.950 → 0.973 | 0.023 | 0.889 → 0.899 | 6.3x sr_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.930 → 0.953 | 0.022 | 0.880 → 0.897 | 4.8x advert_bytes | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.906 → 0.927 | 0.021 | 0.896 → 0.919 | 1.1x advert_bytes | down | 3 |
| `SF-catchup` | catch-up-hours | **text** | 0.888 → 0.909 | 0.021 | 0.874 → 0.903 | 9.5x advert_bytes | up | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.930 → 0.949 | 0.019 | 0.870 → 0.881 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.953 → 0.969 | 0.016 | 0.885 → 0.896 | 1.2x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.944 → 0.959 | 0.015 | 0.890 → 0.900 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.944 → 0.959 | 0.015 | 0.890 → 0.900 | 1.1x sr_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.911 → 0.925 | 0.014 | 0.900 → 0.919 | 1.3x sr_bytes | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.906 → 0.919 | 0.014 | 0.896 → 0.897 | 2.3x sr_airtime | up | 2 |
| `SF-capacity` | capacity | **held** | 0.946 → 0.960 | 0.013 | 0.893 → 0.902 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.946 → 0.960 | 0.013 | 0.893 → 0.902 | 5.3x advert_bytes | down | 5 |
| `SF-sr-retries` | sr-retries | **held** | 0.955 → 0.966 | 0.011 | 0.893 → 0.908 | 1.3x sr_bytes | up | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.944 → 0.955 | 0.011 | 0.891 → 0.897 | 1.1x sr_bytes | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.901 → 0.908 | 0.007 | 0.889 → 0.896 | 5.6x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.952 → 0.959 | 0.007 | 0.893 → 0.900 | 3x advert_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.953 → 0.958 | 0.005 | 0.896 → 0.897 | 2.7x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.952 → 0.957 | 0.005 | 0.893 → 0.897 | 2.8x advert_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **text** | 0.893 → 0.898 | 0.005 | 0.890 → 0.896 | 2.5x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.949 → 0.953 | 0.004 | 0.895 → 0.898 | 2.1x advert_bytes | down | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.972 → 0.975 | 0.003 | 0.970 → 0.974 | 1.2x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.930 → 0.932 | 0.002 | 0.870 → 0.870 | 1x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.906 → 0.908 | 0.002 | 0.896 → 0.898 | 1.2x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.906 → 0.908 | 0.002 | 0.896 → 0.898 | 1x bytes_on_air | up | 2 |
| `SF-resolve` | resolve | **text** | 0.906 → 0.907 | 0.001 | 0.896 → 0.897 | 5.7x advert_bytes | = | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.975 → 0.976 | 0.001 | 0.974 → 0.974 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.999 → 1.000 | 0.000 | 0.974 → 0.974 | 1.1x sr_bytes | up | 2 |

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
| none | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| sprinkled | 1 | 0.936 | 0.933 | 0.003 | - | - | 0.985 | 0.987 | 0.825 | 1.20x | 18.7/26.2/28.2% | 1.8/5.2% | 3 |
| arms-race | 1 | 0.969 | 0.966 | 0.003 | - | - | 0.995 | 0.996 | 0.912 | 0.93x | 22.1/28.0/29.1% | 1.1/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.941 | 0.927 | 0.015 | - | - | 0.990 | 0.991 | 0.855 | 1.13x | 18.6/25.9/30.5% | 1.7/4.6% | 3 |
| 0.3 | 1 | 0.967 | 0.965 | 0.001 | - | - | 0.997 | 0.997 | 0.916 | 0.90x | 21.5/26.1/30.8% | 1.1/5.1% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.877 | 0.865 | 0.011 | - | - | 0.950 | 0.951 | 0.626 | 1.17x | 16.0/25.5/30.1% | 1.8/5.3% | 3 |
| inverse | 1 | 0.852 | 0.840 | 0.013 | - | - | 0.956 | 0.959 | 0.639 | 1.18x | 16.6/21.4/26.6% | 2.1/3.9% | 3 |
| random | 1 | 0.854 | 0.838 | 0.017 | - | - | 0.970 | 0.972 | 0.661 | 1.19x | 15.6/22.0/27.1% | 2.1/4.9% | 3 |

> faster: 0.944 s per simulated hour against 2 over 63 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.877 | 0.865 | 0.011 | - | - | 0.950 | 0.951 | 0.626 | 1.17x | 16.0/25.5/30.1% | 1.8/5.3% | 3 |
| all-routers | 1 | 0.944 | 0.937 | 0.007 | - | - | 0.987 | 0.988 | 0.808 | 2.92x | 35.2/44.4/48.3% | 4.7/5.5% | 3 |

> slower: 10.8 s per simulated hour against 2.5 over 63 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.877 | 0.865 | 0.011 | - | - | 0.950 | 0.951 | 0.626 | 1.17x | 16.0/25.5/30.1% | 1.8/5.3% | 3 |
| no-mute | 1 | 0.915 | 0.904 | 0.011 | - | - | 0.976 | 0.977 | 0.774 | 1.32x | 16.9/25.7/31.0% | 2.0/5.5% | 3 |
| all-routers | 1 | 0.944 | 0.937 | 0.007 | - | - | 0.987 | 0.988 | 0.808 | 2.92x | 35.2/44.4/48.3% | 4.7/5.5% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.877 | 0.865 | 0.011 | - | - | 0.950 | 0.951 | 0.626 | 1.17x | 16.0/25.5/30.1% | 1.8/5.3% | 3 |
| local-typical | 1 | 0.766 | 0.761 | 0.005 | - | - | 0.928 | 0.931 | 0.000 | 1.31x | 17.3/26.8/33.4% | 2.1/5.6% | 3 |
| basement-heavy | 1 | 0.051 | 0.050 | 0.001 | - | - | 0.169 | 0.209 | 0.000 | 0.40x | 0.9/4.7/8.1% | 0.2/2.2% | 3 |

> siting-mix=basement-heavy: decode_failures 2

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.804 | 0.790 | 0.013 | - | - | 0.937 | 0.960 | 0.000 | 2.53x | 15.9/27.4/37.9% | 1.9/5.7% | 3 |
| inverse | 1 | 0.750 | 0.722 | 0.029 | - | - | 0.917 | 0.962 | 0.000 | 2.36x | 14.2/22.5/34.2% | 1.9/3.2% | 3 |

> role-placement=degree: decode_failures 93

> role-placement=inverse: decode_failures 89

> slower: 23.6 s per simulated hour against 3.37 over 63 prior run(s) - 7.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.903 | 0.903 | 0.000 | - | - | 0 | 0.000 | 0.741 | 1.35x | 17.7/27.5/32.0% | 1.9/5.0% | 3 |
| sr | 1 | 0.912 | 0.892 | 0.021 | - | - | 0.973 | 0.976 | 0.743 | 1.40x | 18.5/28.5/33.1% | 2.0/5.5% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.840 | 0.824 | 0.016 | - | - | 0.893 | 0.896 | 0.617 | 3.28x | 41.3/62.8/69.7% | 4.5/10.3% | 3 |
| 100 | 1 | 0.931 | 0.927 | 0.004 | - | - | 0.959 | 0.959 | 0.763 | 1.61x | 20.7/33.7/38.5% | 2.1/5.2% | 3 |
| 120 | 1 | 0.931 | 0.927 | 0.004 | - | - | 0.959 | 0.959 | 0.763 | 1.61x | 20.7/33.7/38.5% | 2.1/5.2% | 3 |
| 250 | 1 | 0.931 | 0.927 | 0.004 | - | - | 0.959 | 0.959 | 0.763 | 1.61x | 20.7/33.7/38.5% | 2.1/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.336 | 0.326 | 0.010 | - | - | 0.588 | 0.610 | 0.168 | 11.12x | 40.3/59.4/65.4% | 3.9/11.0% | 3 |
| 120 | 1 | 0.534 | 0.524 | 0.010 | - | - | 0.847 | 0.847 | 0.221 | 4.26x | 15.8/27.2/33.8% | 1.4/5.7% | 3 |
| 250 | 1 | 0.537 | 0.527 | 0.009 | - | - | 0.851 | 0.853 | 0.217 | 4.17x | 15.5/26.5/32.9% | 1.4/5.6% | 3 |

> max-num-nodes=10: decode_failures 78

> max-num-nodes=120: decode_failures 11

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.931 | 0.927 | 0.004 | - | - | 0.959 | 0.959 | 0.763 | 1.61x | 20.7/33.7/38.5% | 2.1/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.931 | 0.927 | 0.004 | - | - | 0.959 | 0.959 | 0.763 | 1.61x | 20.7/33.7/38.5% | 2.1/5.2% | 3 |
| constrained | 1 | 0.837 | 0.820 | 0.017 | - | - | 0.889 | 0.889 | 0.624 | 3.27x | 41.1/62.7/69.6% | 4.5/10.2% | 3 |

> platform-mix=constrained: decode_failures 1

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.782 | 0.769 | 0.013 | - | - | 0.854 | 0.920 | 0.619 | 5.47x | 60.9/74.6/77.2% | 3.7/13.9% | 3 |
| 25 | 1 | 0.782 | 0.769 | 0.013 | - | - | 0.854 | 0.920 | 0.619 | 5.47x | 60.9/74.6/77.2% | 3.7/13.9% | 3 |
| 100 | 1 | 0.782 | 0.769 | 0.013 | - | - | 0.854 | 0.920 | 0.619 | 5.47x | 60.9/74.6/77.2% | 3.7/13.9% | 3 |
| 2000 | 1 | 0.782 | 0.769 | 0.013 | - | - | 0.854 | 0.920 | 0.619 | 5.47x | 60.9/74.6/77.2% | 3.7/13.9% | 3 |

> warm-num-nodes=0: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 113

> warm-num-nodes=25: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 113

> warm-num-nodes=100: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 113

> warm-num-nodes=2000: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 113

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.807 | 0.787 | 0.020 | - | - | 0.923 | 0.928 | 0.622 | 1.30x | 17.4/27.1/31.8% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.719 | 0.688 | 0.031 | - | - | 0.875 | 0.905 | 0.552 | 1.23x | 16.6/26.0/30.5% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.607 | 0.572 | 0.035 | - | - | 0.780 | 0.845 | 0.436 | 1.12x | 15.1/24.0/28.4% | 1.6/4.0% | 3 |

> burst-loss=0.2: decode_failures 35

> burst-loss=0.3: decode_failures 22

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.886 | 0.873 | 0.013 | - | - | 0.946 | 0.946 | 0.689 | 1.43x | 18.8/29.2/34.0% | 2.0/5.2% | 3 |
| 0.2 | 1 | 0.854 | 0.838 | 0.015 | - | - | 0.927 | 0.930 | 0.643 | 1.48x | 19.9/30.0/34.6% | 2.1/5.2% | 3 |
| 0.3 | 1 | 0.804 | 0.785 | 0.018 | - | - | 0.896 | 0.916 | 0.577 | 1.53x | 20.4/30.8/35.7% | 2.2/5.1% | 3 |

> extra-loss=0.3: decode_failures 19

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.813 | 0.796 | 0.017 | - | - | 0.943 | 0.946 | 0.628 | 1.31x | 17.5/27.4/32.0% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.685 | 0.662 | 0.023 | - | - | 0.818 | 0.896 | 0.499 | 1.22x | 16.6/25.7/30.3% | 1.7/4.8% | 3 |
| 0.3 | 1 | 0.569 | 0.544 | 0.025 | - | - | 0.722 | 0.852 | 0.430 | 1.14x | 15.6/23.4/27.9% | 1.6/4.1% | 3 |

> burst-loss=0.1: decode_failures 5

> burst-loss=0.2: decode_failures 34

> burst-loss=0.3: decode_failures 29

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.857 | 0.857 | 0.000 | - | - | 0.926 | 0.929 | 0.655 | 1.83x | 24.1/37.6/43.4% | 2.5/7.0% | 3 |
| directed-with-late-flood | 1 | 0.881 | 0.881 | 0.000 | - | - | 0.949 | 0.951 | 0.695 | 1.65x | 21.8/34.2/39.6% | 2.3/6.3% | 3 |
| m4-early-flood | 1 | 0.875 | 0.875 | 0.000 | - | - | 0.947 | 0.949 | 0.678 | 1.65x | 21.9/34.5/40.0% | 2.2/6.4% | 3 |

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.933 | 0.928 | 0.004 | - | - | 0.990 | 0.991 | 0.758 | 0.74x | 10.1/12.2/13.7% | 1.2/1.8% | 3 |
| 2.8 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.924 | 0.918 | 0.005 | - | - | 0.975 | 0.975 | 0.758 | 1.17x | 16.4/22.0/25.6% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.918 | 0.911 | 0.007 | - | - | 0.989 | 0.989 | 0.731 | 1.01x | 14.6/18.0/19.2% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.923 | 0.920 | 0.004 | - | - | 0.988 | 0.988 | 0.613 | 0.84x | 11.9/16.4/17.3% | 1.3/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.921 | 0.916 | 0.005 | - | - | 0.966 | 0.966 | 0.757 | 1.16x | 16.6/22.0/25.7% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.911 | 0.907 | 0.004 | - | - | 0.978 | 0.981 | 0.723 | 0.99x | 14.5/17.7/19.2% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.925 | 0.919 | 0.006 | - | - | 0.989 | 0.989 | 0.680 | 0.85x | 12.1/16.6/17.7% | 1.3/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.941 | 0.937 | 0.005 | - | - | 0.979 | 0.980 | 0.827 | 0.71x | 9.6/15.6/18.9% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.938 | 0.934 | 0.003 | - | - | 0.990 | 0.992 | 0.798 | 0.75x | 10.7/13.6/15.2% | 1.1/2.3% | 3 |
| 2.5 | 1 | 0.932 | 0.929 | 0.003 | - | - | 0.987 | 0.989 | 0.790 | 0.75x | 10.5/13.6/15.1% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.937 | 0.934 | 0.003 | - | - | 0.986 | 0.988 | 0.795 | 0.72x | 10.5/13.5/15.2% | 1.1/2.3% | 3 |
| 2.7 | 1 | 0.951 | 0.947 | 0.003 | - | - | 0.989 | 0.991 | 0.868 | 0.76x | 10.8/14.9/16.0% | 1.2/3.1% | 3 |
| 2.8 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.934 | 0.928 | 0.006 | - | - | 0.972 | 0.973 | 0.778 | 0.92x | 12.2/18.9/22.3% | 1.3/3.6% | 3 |
| 900 | 1 | 0.860 | 0.843 | 0.017 | - | - | 0.919 | 0.921 | 0.657 | 2.21x | 29.0/44.9/51.6% | 3.0/8.4% | 3 |
| 300 | 1 | 0.581 | 0.559 | 0.021 | - | - | 0.623 | 0.700 | 0.317 | 4.57x | 56.0/73.2/80.5% | 7.0/16.1% | 3 |

> broadcast-interval-s=300: decode_failures 26

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.958 | 0.956 | 0.002 | - | - | 0.984 | 0.985 | 0.900 | 0.99x | 13.2/19.4/22.9% | 1.4/3.6% | 3 |
| 900 | 1 | 0.911 | 0.905 | 0.006 | - | - | 0.954 | 0.954 | 0.836 | 2.49x | 32.7/48.0/55.0% | 3.5/8.7% | 3 |
| 300 | 1 | 0.589 | 0.577 | 0.012 | - | - | 0.662 | 0.725 | 0.471 | 5.01x | 59.6/74.1/80.7% | 8.0/16.7% | 3 |

> broadcast-interval-s=300: queue drops 10.8% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 28

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.927 | 0.919 | 0.008 | - | - | 0.970 | 0.970 | 0.772 | 1.27x | 16.9/26.4/30.8% | 1.7/5.0% | 3 |
| sinusoid | 1 | 0.916 | 0.906 | 0.010 | - | - | 0.965 | 0.966 | 0.756 | 1.27x | 17.0/26.3/30.8% | 1.7/4.9% | 3 |
| commuter | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.860 | 0.843 | 0.017 | - | - | 0.919 | 0.921 | 0.657 | 2.21x | 29.0/44.9/51.6% | 3.0/8.4% | 3 |
| 3600 | 1 | 0.934 | 0.928 | 0.006 | - | - | 0.972 | 0.973 | 0.778 | 0.92x | 12.2/18.9/22.3% | 1.3/3.6% | 3 |
| 10800 | 1 | 0.940 | 0.935 | 0.005 | - | - | 0.979 | 0.979 | 0.815 | 0.62x | 8.3/12.5/14.9% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.947 | 0.944 | 0.003 | - | - | 0.984 | 0.985 | 0.819 | 0.48x | 6.3/9.7/11.5% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.902 | 0.891 | 0.011 | - | - | 0.951 | 0.952 | 0.719 | 1.47x | 19.5/30.2/35.1% | 2.1/5.7% | 3 |
| 1.0 | 1 | 0.892 | 0.879 | 0.013 | - | - | 0.941 | 0.942 | 0.709 | 1.62x | 21.4/33.6/38.8% | 2.2/6.3% | 3 |
| 4.0 | 1 | 0.866 | 0.852 | 0.014 | - | - | 0.923 | 0.924 | 0.672 | 2.01x | 26.8/41.9/48.4% | 2.8/7.6% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.782 | 0.769 | 0.013 | - | - | 0.854 | 0.920 | 0.619 | 5.47x | 60.9/74.6/77.2% | 3.7/13.9% | 3 |
| 1.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.779 | 0.875 | 0.556 | 5.89x | 64.1/76.5/78.8% | 4.0/14.8% | 3 |

> traceroute-per-hour=0.0: queue drops 19.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 113

> traceroute-per-hour=1.0: queue drops 28.3% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 102

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.781 | 0.774 | 0.007 | - | - | 0.902 | 0.902 | 0.559 | 1.44x | 22.2/29.6/34.2% | 3.4/7.0% | 3 |
| 60 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 90 | 1 | 0.958 | 0.953 | 0.005 | - | - | 0.992 | 0.992 | 0.884 | 1.60x | 18.9/33.4/37.5% | 1.5/4.8% | 3 |
| 120 | 1 | 0.975 | 0.974 | 0.002 | - | - | 1.000 | 1.000 | 0.883 | 1.84x | 22.8/32.6/35.8% | 1.2/5.1% | 3 |
| 150 | 1 | 0.972 | 0.970 | 0.002 | - | - | 0.999 | 0.999 | 0.845 | 2.63x | 31.5/46.0/51.2% | 1.3/5.9% | 3 |

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 120 | 1 | 0.803 | 0.792 | 0.010 | - | - | 0.955 | 0.955 | 0.409 | 2.17x | 16.6/25.5/31.7% | 1.6/5.5% | 3 |
| 250 | 1 | 0.524 | 0.513 | 0.011 | - | - | 0.826 | 0.827 | 0.230 | 4.78x | 17.7/30.9/38.0% | 1.5/6.5% | 3 |
| 500 | 1 | 0.322 | 0.320 | 0.002 | - | - | 0.368 | 0.368 | 0.103 | 10.28x | 19.6/32.3/48.7% | 1.7/6.0% | 3 |

> nodes=250: decode_failures 23

> faster: 7.32 s per simulated hour against 17.3 over 63 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.948 | 0.948 | 0.397 | 1.99x | 15.5/23.3/28.9% | 1.5/4.9% | 3 |
| 250 | 1 | 0.534 | 0.524 | 0.010 | - | - | 0.847 | 0.847 | 0.221 | 4.26x | 15.8/27.2/33.8% | 1.4/5.7% | 3 |
| 500 | 1 | 0.326 | 0.324 | 0.002 | - | - | 0.375 | 0.375 | 0.111 | 9.47x | 18.1/29.8/44.8% | 1.6/5.5% | 3 |

> nodes=250: decode_failures 11

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.924 | 0.915 | 0.009 | - | - | 0.966 | 0.968 | 0.778 | 1.40x | 18.4/28.6/33.3% | 1.9/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.877 | 0.865 | 0.011 | - | - | 0.950 | 0.951 | 0.626 | 1.17x | 16.0/25.5/30.1% | 1.8/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.937 | 0.931 | 0.006 | - | - | 0.972 | 0.972 | 0.819 | 1.45x | 19.1/29.2/34.2% | 2.0/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.903 | 0.900 | 0.003 | - | - | 0.949 | 0.949 | 0.717 | 1.33x | 18.2/28.6/34.1% | 2.3/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.05 | 1 | 0.914 | 0.905 | 0.009 | - | - | 0.964 | 0.964 | 0.699 | 1.50x | 19.7/30.8/35.9% | 2.0/5.5% | 3 |
| 0.1 | 1 | 0.914 | 0.904 | 0.010 | - | - | 0.964 | 0.965 | 0.695 | 1.53x | 20.2/32.9/38.5% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.933 | 0.923 | 0.010 | - | - | 0.982 | 0.984 | 0.782 | 1.76x | 22.8/37.5/44.0% | 2.3/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| local-typical | 1 | 0.713 | 0.709 | 0.004 | - | - | 0.848 | 0.848 | 0.000 | 1.51x | 17.3/27.4/34.7% | 2.2/5.6% | 3 |
| event | 1 | 0.386 | 0.372 | 0.015 | - | - | 0.615 | 0.620 | 0.000 | 1.51x | 7.8/15.0/26.3% | 2.4/5.4% | 3 |
| backbone | 1 | 0.981 | 0.981 | 0.000 | - | - | 1.000 | 1.000 | 0.908 | 1.03x | 28.8/39.0/40.2% | 1.2/5.6% | 3 |

> faster: 0.908 s per simulated hour against 1.84 over 62 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.873 | 0.865 | 0.007 | - | - | 0.944 | 0.950 | 0.687 | 1.48x | 28.6/38.4/42.0% | 3.1/8.1% | 3 |
| 60 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 90 | 1 | 0.846 | 0.839 | 0.007 | - | - | 0.981 | 0.981 | 0.573 | 1.58x | 15.2/22.4/25.1% | 1.4/5.1% | 3 |
| 120 | 1 | 0.803 | 0.792 | 0.010 | - | - | 0.955 | 0.955 | 0.409 | 2.17x | 16.6/25.5/31.7% | 1.6/5.5% | 3 |
| 150 | 1 | 0.756 | 0.748 | 0.008 | - | - | 0.975 | 0.976 | 0.433 | 2.72x | 16.5/26.5/31.3% | 1.5/5.5% | 3 |

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 1.25 | 1 | 0.706 | 0.690 | 0.016 | - | - | 0.812 | 0.837 | 0.363 | 1.34x | 12.7/20.5/25.6% | 2.0/5.1% | 3 |
| 1.5 | 1 | 0.447 | 0.431 | 0.016 | - | - | 0.856 | 0.859 | 0.062 | 1.32x | 9.4/15.6/18.4% | 2.0/5.5% | 3 |
| 2.0 | 1 | 0.154 | 0.154 | 0.001 | - | - | 0.090 | 0.100 | 0.000 | 1.01x | 5.1/9.2/12.2% | 1.7/3.4% | 3 |

> stretch=1.25: decode_failures 18

> stretch=1.5: decode_failures 2

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| clustered | 1 | 0.952 | 0.949 | 0.002 | - | - | 0.986 | 0.986 | 0.634 | 1.14x | 24.2/33.3/34.9% | 1.4/5.4% | 3 |
| corridor | 1 | 0.562 | 0.558 | 0.004 | - | - | 0.588 | 0.590 | 0.403 | 1.37x | 17.4/21.6/25.2% | 2.0/5.4% | 3 |
| hub | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.990 | 0.991 | 0.824 | 1.22x | 30.8/38.4/39.5% | 1.8/5.7% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.881 | 0.881 | 0.000 | - | - | 0.949 | 0.951 | 0.695 | 1.65x | 21.8/34.2/39.6% | 2.3/6.3% | 3 |
| True | 1 | 0.870 | 0.870 | 0.000 | - | - | 0.930 | 0.932 | 0.676 | 1.64x | 21.7/34.4/39.7% | 2.2/6.4% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.870 | 0.870 | 0.000 | - | - | 0.930 | 0.932 | 0.676 | 1.64x | 21.7/34.4/39.7% | 2.2/6.4% | 3 |
| m4-early-flood | 1 | 0.870 | 0.870 | 0.000 | - | - | 0.932 | 0.932 | 0.682 | 1.65x | 21.8/34.5/40.0% | 2.2/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.903 | 0.903 | 0.000 | - | - | 0 | 0.000 | 0.741 | 1.35x | 17.7/27.5/32.0% | 1.9/5.0% | 3 |
| chain | 1 | 0.886 | 0.885 | 0.001 | - | - | 0.896 | 0.949 | 0.719 | 1.58x | 20.9/32.4/38.1% | 2.1/6.0% | 3 |
| sr | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| True | 1 | 0.908 | 0.898 | 0.010 | - | - | 0.954 | 0.955 | 0.739 | 1.39x | 18.4/28.5/33.3% | 1.9/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.975 | 0.974 | 0.002 | - | - | 1.000 | 1.000 | 0.883 | 1.84x | 22.8/32.6/35.8% | 1.2/5.1% | 3 |
| True | 1 | 0.976 | 0.974 | 0.002 | - | - | 1.000 | 1.000 | 0.900 | 1.89x | 23.3/33.0/36.3% | 1.2/5.2% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.207 | 0.205 | 0.002 | - | - | 0.249 | 0.431 | 0.000 | 0.06x | 0.3/0.6/0.7% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.551 | 0.516 | 0.035 | - | - | 0.731 | 0.762 | 0.256 | 0.31x | 2.3/3.9/4.5% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.846 | 0.835 | 0.010 | - | - | 0.915 | 0.917 | 0.528 | 1.30x | 14.3/20.7/25.3% | 1.9/4.8% | 3 |

> preset=SHORT_TURBO: decode_failures 3

> preset=MEDIUM_TURBO: decode_failures 33

> slower: 4.89 s per simulated hour against 1.95 over 63 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.911 | 0.902 | 0.010 | - | - | 0.953 | 0.954 | 0.749 | 1.34x | 19.1/29.0/33.4% | 1.9/5.4% | 3 |
| 1.0 | 1 | 0.939 | 0.932 | 0.007 | - | - | 0.972 | 0.973 | 0.810 | 1.09x | 24.2/32.0/34.9% | 1.4/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.403 | 0.399 | 0.004 | - | - | 0.361 | 0.383 | 0.023 | 0.18x | 1.2/1.8/2.4% | 0.3/0.6% | 3 |
| LONG_FAST | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| LITE_FAST | 1 | 0.855 | 0.845 | 0.010 | - | - | 0.931 | 0.931 | 0.528 | 1.05x | 11.9/18.9/23.0% | 1.5/4.0% | 3 |
| NARROW_SLOW | 1 | 0.894 | 0.881 | 0.013 | - | - | 0.964 | 0.965 | 0.552 | 1.30x | 15.4/22.6/26.8% | 1.8/5.1% | 3 |

> preset=SHORT_FAST: decode_failures 19

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| temporal | 1 | 0.836 | 0.817 | 0.019 | - | - | 0.910 | 0.910 | 0.549 | 1.40x | 17.6/27.6/32.7% | 2.0/5.3% | 3 |
| transient | 1 | 0.911 | 0.901 | 0.010 | - | - | 0.961 | 0.961 | 0.739 | 1.38x | 18.1/28.1/32.9% | 1.9/5.3% | 3 |
| periodic | 1 | 0.751 | 0.743 | 0.008 | - | - | 0.798 | 0.799 | 0.590 | 1.25x | 16.6/25.7/29.7% | 1.7/4.6% | 3 |

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.403 | 0.399 | 0.004 | - | - | 0.361 | 0.383 | 0.023 | 0.18x | 1.2/1.8/2.4% | 0.3/0.6% | 3 |
| LONG_FAST | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| LONG_MODERATE | 1 | 0.852 | 0.837 | 0.015 | - | - | 0.919 | 0.919 | 0.719 | 3.32x | 49.6/65.3/69.8% | 4.8/11.9% | 3 |

> preset=SHORT_FAST: decode_failures 19

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.055 | 0.054 | 0.001 | - | - | 0.118 | 0.120 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.207 | 0.205 | 0.002 | - | - | 0.249 | 0.431 | 0.000 | 0.06x | 0.3/0.6/0.7% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| LONG_TURBO | 1 | 0.846 | 0.835 | 0.010 | - | - | 0.915 | 0.917 | 0.528 | 1.30x | 14.3/20.7/25.3% | 1.9/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.879 | 0.866 | 0.013 | - | - | 0.940 | 0.941 | 0.618 | 1.93x | 24.1/34.9/42.0% | 2.7/6.9% | 3 |

> preset=SHORT_TURBO: decode_failures 3

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.850 | 0.839 | 0.010 | - | - | 0.893 | 0.894 | 0.669 | 1.34x | 17.9/28.0/32.4% | 1.8/5.2% | 3 |
| 10000 | 1 | 0.751 | 0.743 | 0.008 | - | - | 0.798 | 0.799 | 0.590 | 1.25x | 16.6/25.7/29.7% | 1.7/4.6% | 3 |
| 4000 | 1 | 0.473 | 0.468 | 0.005 | - | - | 0.501 | 0.534 | 0.346 | 1.11x | 15.2/22.6/26.3% | 1.6/3.6% | 3 |
| 2000 | 1 | 0.113 | 0.113 | 0.000 | - | - | 0.095 | 0.157 | 0.051 | 0.75x | 10.1/15.0/18.4% | 1.2/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 11

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.447 | 0.431 | 0.016 | - | - | 0.856 | 0.859 | 0.062 | 1.32x | 9.4/15.6/18.4% | 2.0/5.5% | 3 |
| 1.0 | 1 | 0.674 | 0.649 | 0.025 | - | - | 0.916 | 0.919 | 0.390 | 1.04x | 14.6/20.3/21.9% | 1.4/5.0% | 3 |

> duct-per-hour=0.0: decode_failures 2

> duct-per-hour=1.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 22 | 1 | 0.519 | 0.478 | 0.041 | - | - | 0.714 | 0.723 | 0.244 | 1.41x | 10.6/16.1/17.5% | 2.1/5.0% | 3 |
| 17 | 1 | 0.189 | 0.186 | 0.003 | - | - | 0.211 | 0.367 | 0.000 | 1.18x | 6.6/11.4/13.7% | 2.1/3.8% | 3 |
| 14 | 1 | 0.092 | 0.090 | 0.002 | - | - | 0.150 | 0.151 | 0.000 | 0.73x | 3.4/5.5/8.3% | 1.2/2.4% | 3 |

> tx-power=22: decode_failures 3

> tx-power=17: decode_failures 3

> tx-power=14: decode_failures 14

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.975 | 0.974 | 0.002 | - | - | 1.000 | 1.000 | 0.883 | 1.84x | 22.8/32.6/35.8% | 1.2/5.1% | 3 |
| True | 1 | 0.972 | 0.970 | 0.002 | - | - | 0.999 | 0.999 | 0.889 | 2.22x | 27.1/36.9/40.5% | 1.4/5.8% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.911 | 0.900 | 0.010 | - | - | 0.958 | 0.958 | 0.704 | 1.44x | 19.1/29.8/34.5% | 1.9/5.4% | 3 |
| True | 1 | 0.925 | 0.919 | 0.006 | - | - | 0.958 | 0.958 | 0.779 | 1.53x | 20.2/30.7/35.9% | 2.0/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| random | 1 | 0.896 | 0.885 | 0.011 | - | - | 0.969 | 0.971 | 0.759 | 1.32x | 17.4/27.6/32.3% | 1.7/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.770 | 0.728 | 0.042 | - | - | 0.922 | 0.927 | 0.478 | 1.01x | 13.5/23.6/27.6% | 1.3/4.8% | 3 |
| 7 | 1 | 0.946 | 0.944 | 0.002 | - | - | 0.979 | 0.979 | 0.887 | 1.50x | 20.1/29.6/34.8% | 2.1/5.4% | 3 |
| 15 | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.982 | 0.982 | 0.899 | 1.54x | 20.6/30.0/35.5% | 2.2/5.4% | 3 |
| 32 | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.982 | 0.982 | 0.899 | 1.54x | 20.6/30.0/35.5% | 2.2/5.4% | 3 |

> hop-limit=15: misdecodes 1

> hop-limit=32: misdecodes 1

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.770 | 0.728 | 0.042 | - | - | 0.922 | 0.927 | 0.478 | 1.01x | 13.5/23.6/27.6% | 1.3/4.8% | 3 |
| 5 | 1 | 0.905 | 0.894 | 0.011 | - | - | 0.965 | 0.965 | 0.789 | 1.40x | 18.5/28.8/33.5% | 1.9/5.4% | 3 |
| 7 | 1 | 0.946 | 0.944 | 0.002 | - | - | 0.979 | 0.979 | 0.887 | 1.50x | 20.1/29.6/34.8% | 2.1/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.899 | 0.899 | 0.000 | - | - | 0.908 | 0.960 | 0.749 | 1.34x | 17.8/27.6/32.0% | 1.9/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.770 | 0.728 | 0.042 | - | - | 0.922 | 0.927 | 0.478 | 1.01x | 13.5/23.6/27.6% | 1.3/4.8% | 3 |
| True | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| BALANCED | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| STRICT | 1 | 0.794 | 0.794 | 0.000 | - | - | 0.851 | 0.855 | 0.627 | 1.46x | 19.4/29.6/34.6% | 2.1/5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| dm | 1 | 0.909 | 0.897 | 0.012 | - | - | 0.958 | 0.959 | 0.731 | 1.37x | 18.1/28.2/33.0% | 1.9/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.908 | 0.897 | 0.011 | - | - | 0.956 | 0.956 | 0.729 | 1.39x | 18.3/28.3/33.1% | 1.9/5.3% | 3 |
| local | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| time | 1 | 0.904 | 0.893 | 0.011 | - | - | 0.957 | 0.957 | 0.734 | 1.43x | 18.9/29.3/34.2% | 1.9/5.6% | 3 |
| window | 1 | 0.906 | 0.897 | 0.009 | - | - | 0.952 | 0.953 | 0.725 | 1.36x | 18.0/27.8/32.3% | 1.9/5.2% | 3 |

> bucket-mode=global: misdecodes 34

> bucket-mode=time: misdecodes 37

> bucket-mode=window: misdecodes 24

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.901 | 0.889 | 0.012 | - | - | 0.953 | 0.953 | 0.725 | 1.55x | 20.3/31.8/37.2% | 2.1/6.2% | 3 |
| 1800 | 1 | 0.904 | 0.893 | 0.011 | - | - | 0.957 | 0.957 | 0.734 | 1.43x | 18.9/29.3/34.2% | 1.9/5.6% | 3 |
| 3600 | 1 | 0.908 | 0.896 | 0.012 | - | - | 0.956 | 0.956 | 0.715 | 1.38x | 18.2/28.4/32.8% | 1.9/5.3% | 3 |

> time-bucket-s=600: misdecodes 135

> time-bucket-s=1800: misdecodes 37

> time-bucket-s=3600: misdecodes 9

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| interval | 1 | 0.873 | 0.858 | 0.015 | - | - | 0.916 | 0.918 | 0.665 | 1.91x | 25.2/40.4/47.2% | 2.5/8.8% | 3 |
| aimd | 1 | 0.905 | 0.902 | 0.003 | - | - | 0.921 | 0.959 | 0.743 | 1.38x | 18.2/28.3/32.9% | 1.9/5.3% | 3 |
| bucket+interval | 1 | 0.888 | 0.874 | 0.015 | - | - | 0.936 | 0.936 | 0.675 | 1.97x | 26.2/41.6/48.6% | 2.6/9.3% | 3 |

> trigger=interval: misdecodes 22

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 2

> trigger=bucket+interval: misdecodes 28

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.907 | 0.899 | 0.007 | - | - | 0.948 | 0.954 | 0.753 | 1.37x | 18.1/28.2/32.8% | 1.9/5.3% | 3 |
| 8 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.948 | 0.949 | 0.756 | 1.38x | 18.2/28.3/33.0% | 1.9/5.4% | 3 |
| 16 | 1 | 0.912 | 0.902 | 0.010 | - | - | 0.960 | 0.960 | 0.745 | 1.39x | 18.4/28.7/33.2% | 2.0/5.4% | 3 |
| 32 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 50 | 1 | 0.904 | 0.893 | 0.010 | - | - | 0.946 | 0.948 | 0.709 | 1.38x | 18.3/28.2/32.8% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 51

> capacity=8: decode_failures 8

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.907 | 0.899 | 0.007 | - | - | 0.948 | 0.954 | 0.753 | 1.37x | 18.1/28.2/32.8% | 1.9/5.3% | 3 |
| 8 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.948 | 0.949 | 0.756 | 1.38x | 18.2/28.3/33.0% | 1.9/5.4% | 3 |
| 16 | 1 | 0.912 | 0.902 | 0.010 | - | - | 0.960 | 0.960 | 0.745 | 1.39x | 18.4/28.7/33.2% | 2.0/5.4% | 3 |
| 32 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 50 | 1 | 0.904 | 0.893 | 0.010 | - | - | 0.946 | 0.948 | 0.709 | 1.38x | 18.3/28.2/32.8% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 51

> capacity=8: decode_failures 8

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.907 | 0.898 | 0.009 | - | - | 0.953 | 0.958 | 0.741 | 1.36x | 17.9/27.9/32.5% | 1.9/5.2% | 3 |
| 16 | 1 | 0.903 | 0.895 | 0.009 | - | - | 0.949 | 0.952 | 0.718 | 1.37x | 18.0/28.1/32.6% | 1.9/5.2% | 3 |
| 32 | 1 | 0.906 | 0.897 | 0.009 | - | - | 0.952 | 0.953 | 0.725 | 1.36x | 18.0/27.8/32.3% | 1.9/5.2% | 3 |

> capacity=8: misdecodes 33

> capacity=8: decode_failures 12

> capacity=16: misdecodes 16

> capacity=16: decode_failures 2

> capacity=32: misdecodes 24

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.888 | 0.874 | 0.015 | - | - | 0.936 | 0.936 | 0.675 | 1.97x | 26.2/41.6/48.6% | 2.6/9.3% | 3 |
| 02-06 | 1 | 0.904 | 0.899 | 0.006 | - | - | 0.932 | 0.955 | 0.727 | 1.44x | 19.1/29.5/34.9% | 2.0/5.7% | 3 |
| 00-08 | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.938 | 0.960 | 0.721 | 1.49x | 19.4/30.8/36.4% | 2.1/6.1% | 3 |

> catch-up-hours=: misdecodes 28

> catch-up-hours=02-06: decode_failures 39

> catch-up-hours=00-08: decode_failures 39

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.898 | 0.898 | 0.001 | - | - | 0.955 | 0.955 | 0.730 | 1.40x | 18.4/28.6/33.1% | 1.9/5.3% | 3 |
| 2 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 3 | 1 | 0.912 | 0.892 | 0.021 | - | - | 0.973 | 0.976 | 0.743 | 1.40x | 18.5/28.5/33.1% | 2.0/5.5% | 3 |
| 4 | 1 | 0.918 | 0.900 | 0.018 | - | - | 0.987 | 0.990 | 0.755 | 1.39x | 18.4/28.5/33.0% | 1.9/5.4% | 3 |

> faster: 1.09 s per simulated hour against 4.03 over 63 prior run(s) - 3.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.898 | 0.898 | 0.001 | - | - | 0.955 | 0.955 | 0.730 | 1.40x | 18.4/28.6/33.1% | 1.9/5.3% | 3 |
| 2 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 3 | 1 | 0.912 | 0.892 | 0.021 | - | - | 0.973 | 0.976 | 0.743 | 1.40x | 18.5/28.5/33.1% | 2.0/5.5% | 3 |
| 4 | 1 | 0.918 | 0.900 | 0.018 | - | - | 0.987 | 0.990 | 0.755 | 1.39x | 18.4/28.5/33.0% | 1.9/5.4% | 3 |
| 5 | 1 | 0.915 | 0.895 | 0.020 | - | - | 0.981 | 0.984 | 0.732 | 1.39x | 18.6/28.6/32.9% | 1.9/5.4% | 3 |

> faster: 1.95 s per simulated hour against 4.52 over 63 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.900 | 0.890 | 0.010 | - | - | 0.944 | 0.944 | 0.734 | 1.40x | 18.5/28.7/33.4% | 1.9/5.4% | 3 |
| 30 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 120 | 1 | 0.911 | 0.900 | 0.010 | - | - | 0.959 | 0.959 | 0.715 | 1.40x | 18.5/28.7/33.4% | 2.0/5.4% | 3 |
| 600 | 1 | 0.903 | 0.893 | 0.010 | - | - | 0.953 | 0.954 | 0.737 | 1.39x | 18.4/28.5/33.2% | 1.9/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.900 | 0.890 | 0.010 | - | - | 0.944 | 0.944 | 0.734 | 1.40x | 18.5/28.7/33.4% | 1.9/5.4% | 3 |
| 30 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 120 | 1 | 0.911 | 0.900 | 0.010 | - | - | 0.959 | 0.959 | 0.715 | 1.40x | 18.5/28.7/33.4% | 2.0/5.4% | 3 |
| 600 | 1 | 0.903 | 0.893 | 0.010 | - | - | 0.953 | 0.954 | 0.737 | 1.39x | 18.4/28.5/33.2% | 1.9/5.4% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.925 | 0.898 | 0.027 | - | - | 0.949 | 0.983 | 0.756 | 1.41x | 19.0/28.6/33.0% | 1.9/5.2% | 3 |
| routers | 1 | 0.898 | 0.896 | 0.002 | - | - | 0.956 | 0.957 | 0.717 | 1.38x | 18.3/28.3/32.8% | 1.9/5.2% | 3 |
| alternate-routers | 1 | 0.902 | 0.901 | 0.001 | - | - | 0.957 | 0.957 | 0.756 | 1.38x | 18.1/28.1/32.6% | 1.9/5.2% | 3 |
| beside-router | 1 | 0.901 | 0.891 | 0.009 | - | - | 0.964 | 0.965 | 0.746 | 1.37x | 18.1/28.2/32.8% | 1.9/5.3% | 3 |
| random-clients | 1 | 0.908 | 0.899 | 0.010 | - | - | 0.963 | 0.964 | 0.720 | 1.39x | 18.4/28.5/32.8% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

> place=spread: decode_failures 39

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.925 | 0.898 | 0.027 | - | - | 0.949 | 0.983 | 0.756 | 1.41x | 19.0/28.6/33.0% | 1.9/5.2% | 3 |
| routers | 1 | 0.898 | 0.896 | 0.002 | - | - | 0.956 | 0.957 | 0.717 | 1.38x | 18.3/28.3/32.8% | 1.9/5.2% | 3 |
| alternate-routers | 1 | 0.902 | 0.901 | 0.001 | - | - | 0.957 | 0.957 | 0.756 | 1.38x | 18.1/28.1/32.6% | 1.9/5.2% | 3 |
| beside-router | 1 | 0.901 | 0.891 | 0.009 | - | - | 0.964 | 0.965 | 0.746 | 1.37x | 18.1/28.2/32.8% | 1.9/5.3% | 3 |
| random-clients | 1 | 0.908 | 0.899 | 0.010 | - | - | 0.963 | 0.964 | 0.720 | 1.39x | 18.4/28.5/32.8% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

> place=spread: decode_failures 39

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| broadcast | 1 | 0.919 | 0.897 | 0.022 | - | - | 0.955 | 0.957 | 0.809 | 1.44x | 19.0/29.4/34.1% | 2.0/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| heard | 1 | 0.908 | 0.898 | 0.010 | - | - | 0.954 | 0.955 | 0.743 | 1.37x | 18.1/28.2/32.5% | 1.9/5.3% | 3 |

> replay-ordering=heard: misdecodes 20

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.919 | 0.897 | 0.022 | - | - | 0.955 | 0.957 | 0.809 | 1.44x | 19.0/29.4/34.1% | 2.0/5.4% | 3 |
| heard | 1 | 0.913 | 0.891 | 0.022 | - | - | 0.944 | 0.945 | 0.799 | 1.41x | 18.5/28.8/33.5% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 12

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| enum | 1 | 0.907 | 0.897 | 0.010 | - | - | 0.952 | 0.954 | 0.746 | 1.39x | 18.3/28.5/33.5% | 1.9/5.5% | 3 |
| hybrid | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.898 | 0.896 | 0.002 | - | - | 0.956 | 0.957 | 0.717 | 1.38x | 18.3/28.3/32.8% | 1.9/5.2% | 3 |
| 6 | 1 | 0.893 | 0.890 | 0.003 | - | - | 0.960 | 0.960 | 0.723 | 1.41x | 18.5/29.0/33.5% | 1.9/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.908 | 0.899 | 0.009 | - | - | 0.950 | 0.953 | 0.734 | 1.38x | 18.1/28.1/32.8% | 1.9/5.3% | 2 |
| 3 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 5 | 1 | 0.904 | 0.889 | 0.015 | - | - | 0.964 | 0.964 | 0.749 | 1.42x | 18.7/28.9/33.8% | 1.9/5.4% | 5 |
| 8 | 1 | 0.908 | 0.891 | 0.016 | - | - | 0.973 | 0.974 | 0.716 | 1.47x | 19.3/29.9/35.0% | 2.0/5.6% | 8 |

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.908 | 0.899 | 0.009 | - | - | 0.950 | 0.953 | 0.734 | 1.38x | 18.1/28.1/32.8% | 1.9/5.3% | 2 |
| 3 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 5 | 1 | 0.904 | 0.889 | 0.015 | - | - | 0.964 | 0.964 | 0.749 | 1.42x | 18.7/28.9/33.8% | 1.9/5.4% | 5 |
| 8 | 1 | 0.908 | 0.891 | 0.016 | - | - | 0.973 | 0.974 | 0.716 | 1.47x | 19.3/29.9/35.0% | 2.0/5.6% | 8 |

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| True | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.913 | 0.904 | 0.009 | - | - | 0.955 | 0.960 | 0.770 | 1.28x | 17.1/26.3/30.6% | 1.7/4.9% | 3 |
| 1 | 1 | 0.907 | 0.893 | 0.013 | - | - | 0.958 | 0.958 | 0.754 | 1.30x | 17.1/26.6/30.9% | 1.8/5.0% | 3 |
| 2 | 1 | 0.911 | 0.904 | 0.007 | - | - | 0.964 | 0.965 | 0.773 | 1.30x | 17.2/26.6/31.1% | 1.8/4.9% | 3 |
| 4 | 1 | 0.917 | 0.908 | 0.009 | - | - | 0.966 | 0.966 | 0.765 | 1.34x | 17.8/27.7/32.1% | 1.9/5.2% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.907 | 0.893 | 0.014 | - | - | 0.959 | 0.959 | 0.719 | 1.38x | 18.3/28.5/33.0% | 1.9/5.4% | 3 |
| 24 | 1 | 0.908 | 0.900 | 0.009 | - | - | 0.953 | 0.954 | 0.732 | 1.37x | 18.1/28.2/32.7% | 1.9/5.3% | 3 |
| 32 | 1 | 0.906 | 0.896 | 0.009 | - | - | 0.953 | 0.953 | 0.735 | 1.38x | 18.3/28.4/33.0% | 1.9/5.3% | 3 |
| 64 | 1 | 0.907 | 0.898 | 0.009 | - | - | 0.952 | 0.953 | 0.716 | 1.40x | 18.4/28.6/33.4% | 1.9/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.890 | 0.880 | 0.010 | - | - | 0.930 | 0.932 | 0.715 | 1.46x | 19.2/29.7/34.7% | 2.0/5.6% | 3 |
| 16 | 1 | 0.904 | 0.895 | 0.009 | - | - | 0.953 | 0.954 | 0.741 | 1.40x | 18.5/28.8/33.6% | 1.9/5.4% | 3 |
| 32 | 1 | 0.906 | 0.897 | 0.009 | - | - | 0.952 | 0.953 | 0.725 | 1.36x | 18.0/27.8/32.3% | 1.9/5.2% | 3 |

> window-size=8: misdecodes 140

> window-size=16: misdecodes 35

> window-size=32: misdecodes 24

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.975 | 0.974 | 0.002 | - | - | 1.000 | 1.000 | 0.883 | 1.84x | 22.8/32.6/35.8% | 1.2/5.1% | 3 |
| True | 1 | 0.798 | 0.785 | 0.013 | - | - | 0.874 | 0.934 | 0.632 | 5.38x | 60.4/74.3/77.0% | 3.7/13.8% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: queue drops 16.9% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 83

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.534 | 0.524 | 0.010 | - | - | 0.847 | 0.847 | 0.221 | 4.26x | 15.8/27.2/33.8% | 1.4/5.7% | 3 |
| truesize | 1 | 0.564 | 0.555 | 0.009 | - | - | 0.872 | 0.874 | 0.226 | 3.22x | 11.6/22.2/28.4% | 1.0/5.1% | 3 |

> congestion-input=hotstore: decode_failures 11

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.976 | 0.974 | 0.002 | - | - | 0.999 | 1.000 | 0.887 | 1.78x | 21.9/31.1/34.2% | 1.1/4.9% | 3 |
| adaptive | 1 | 0.975 | 0.974 | 0.002 | - | - | 1.000 | 1.000 | 0.883 | 1.84x | 22.8/32.6/35.8% | 1.2/5.1% | 3 |

> congestion-mode=static: misdecodes 1

> congestion-mode=adaptive: misdecodes 1

