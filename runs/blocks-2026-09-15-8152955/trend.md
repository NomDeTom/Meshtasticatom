# Sweep blocks-2026-09-15-8152955

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 8152955 · seeds 8152955
- **blocks** 87 run
- **compute** 11.1 h of simulator time across every cell
- **generated** 2026-09-15T08:56:32+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>99 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 25
- AD-siting: siting-mix=local-typical: decode_failures 3
- AD-worst: role-placement=degree: decode_failures 56
- AD-worst: role-placement=inverse: decode_failures 46
- AD-worst: slower: 17.7 s per simulated hour against 3.48 over 25 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 43
- DB-hotstore-stress: max-num-nodes=120: decode_failures 41
- DB-hotstore-stress: max-num-nodes=250: decode_failures 20
- DB-platform: platform-mix=constrained: decode_failures 3
- DB-warm: warm-num-nodes=0: queue drops 11.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 82
- DB-warm: warm-num-nodes=25: queue drops 11.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 82
- DB-warm: warm-num-nodes=100: queue drops 11.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 82
- DB-warm: warm-num-nodes=2000: queue drops 11.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 82
- DG-burst: burst-loss=0.2: decode_failures 17
- DG-burst: burst-loss=0.3: decode_failures 26
- DG-loss: extra-loss=0.2: decode_failures 2
- DG-loss: extra-loss=0.3: decode_failures 18
- DG-outage: burst-loss=0.1: decode_failures 35
- DG-outage: burst-loss=0.2: decode_failures 33
- DG-outage: burst-loss=0.3: decode_failures 25
- DM-mode: dm-mode=flood-only: decode_failures 24
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 23
- DM-mode: dm-mode=m4-early-flood: decode_failures 6
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 27
- LD-chatty: broadcast-interval-s=300: decode_failures 10
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 11.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 82
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 19.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 88
- MS-hopscale: nodes=250: decode_failures 141
- MS-hopscale: nodes=500: decode_failures 189
- MS-oversubscribed: nodes=250: decode_failures 41
- MS-oversubscribed: nodes=500: decode_failures 126
- MS-siting: siting-mix=local-typical: decode_failures 10
- MS-stretch: stretch=1.25: decode_failures 20
- MS-topology: topology=corridor: decode_failures 4
- PR-crladder: coding-rate-ladder=False: decode_failures 23
- PR-crladder: coding-rate-ladder=True: decode_failures 23
- PR-crladder: slower: 6.74 s per simulated hour against 2.79 over 25 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 23
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 22
- PR-dmmode-cr: slower: 8.63 s per simulated hour against 2.54 over 25 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=LONG_TURBO: decode_failures 1
- RF-noise: noise-profile=temporal: decode_failures 10
- RF-preset: preset=LONG_MODERATE: decode_failures 15
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 5
- RF-txpower: tx-power=14: 3 archives requested, 2 placed - group on the placed count
- SF-bucket-mode: bucket-mode=global: misdecodes 18
- SF-bucket-mode: bucket-mode=time: misdecodes 28
- SF-bucket-mode: bucket-mode=window: misdecodes 27
- SF-bucket-time: time-bucket-s=600: misdecodes 102
- SF-bucket-time: time-bucket-s=1800: misdecodes 28
- SF-bucket-time: time-bucket-s=3600: misdecodes 14
- SF-cadence: trigger=interval: misdecodes 14
- SF-cadence: trigger=aimd: misdecodes 5
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 21
- SF-capacity-local: capacity=4: decode_failures 83
- SF-capacity-local: capacity=8: decode_failures 18
- SF-capacity: capacity=4: decode_failures 83
- SF-capacity: capacity=8: decode_failures 18
- SF-capacity-window: capacity=8: misdecodes 18
- SF-capacity-window: capacity=8: decode_failures 35
- SF-capacity-window: capacity=16: misdecodes 19
- SF-capacity-window: capacity=16: decode_failures 2
- SF-capacity-window: capacity=32: misdecodes 27
- SF-catchup: catch-up-hours=: misdecodes 21
- SF-catchup: catch-up-hours=02-06: decode_failures 43
- SF-catchup: catch-up-hours=00-08: decode_failures 43
- SF-hops-flat: hops-apart=4: decode_failures 3
- SF-hops-flat: faster: 1.81 s per simulated hour against 3.65 over 25 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: hops-apart=4: decode_failures 3
- SF-hops-spread: hops-apart=5: decode_failures 3
- SF-hops-spread: faster: 2.15 s per simulated hour against 4.81 over 25 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=spread: decode_failures 20
- SF-place-spread: place=spread: decode_failures 20
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 9
- SF-servers-allrouters: servers=6: misdecodes 3
- SF-servers-flat: servers=5: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 2
- SF-servers-spread: servers=5: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 2
- SF-width: short-id-bits=64: misdecodes 1
- SF-window-size: window-size=8: misdecodes 102
- SF-window-size: window-size=16: misdecodes 60
- SF-window-size: window-size=32: misdecodes 27
- TH-congestion-input: congestion-input=hotstore: decode_failures 41
- TH-congestion-input: congestion-input=truesize: decode_failures 45
- TH-congestion-input: slower: 28.7 s per simulated hour against 10.3 over 25 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion-mode: congestion-mode=static: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 10.6% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 77

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 17.7 | 3.48 | 5.08x | 25 |
| `PR-dmmode-cr` | 8.63 | 2.54 | 3.40x | 25 |
| `TH-congestion-input` | 28.7 | 10.3 | 2.79x | 25 |
| `PR-crladder` | 6.74 | 2.79 | 2.42x | 25 |
| `DM-mode` | 5.95 | 3.06 | 1.94x | 25 |
| `AD-badrouters` | 3.92 | 2.1 | 1.87x | 25 |
| `MS-oversubscribed` | 32.7 | 19.4 | 1.68x | 25 |
| `LD-chatty` | 3.31 | 5.04 | 0.66x | 25 |
| `FW-versions` | 1.07 | 1.66 | 0.64x | 25 |
| `LD-traceroute` | 1.27 | 2.1 | 0.60x | 25 |
| `SF-capacity-local` | 1.09 | 1.81 | 0.60x | 25 |
| `RF-txpower` | 0.931 | 1.61 | 0.58x | 25 |
| `RF-stretch-duct` | 1.5 | 2.62 | 0.57x | 25 |
| `FW-signing-cost` | 0.903 | 1.61 | 0.56x | 25 |
| `RT-rebroadcast` | 0.842 | 1.59 | 0.53x | 25 |
| `SF-hops-flat` | 1.81 | 3.65 | 0.49x | 25 |
| `SF-hops-spread` | 2.15 | 4.81 | 0.45x | 25 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.984 | 0.984 | 0.878 → 0.880 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.977 | 0.977 | 0.868 → 0.880 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.045 → 0.977 | 0.932 | 0.062 → 0.880 | 1.4e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.075 → 0.977 | 0.902 | 0.037 → 0.880 | 17x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.089 → 0.908 | 0.819 | 0.086 → 0.812 | 1.3e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.188 → 0.977 | 0.789 | 0.100 → 0.880 | 7.4x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.213 → 0.973 | 0.760 | 0.210 → 0.972 | 4.9x sr_airtime | up | 4 |
| `AD-siting` | siting-mix | **text** | 0.056 → 0.806 | 0.751 | 0.054 → 0.797 | 4x sr_bytes | down | 3 |
| `RF-bw500` | preset | **held** | 0.241 → 0.958 | 0.717 | 0.122 → 0.810 | 4.1x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.309 → 0.887 | 0.579 | 0.303 → 0.880 | 16x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.321 → 0.887 | 0.567 | 0.319 → 0.880 | 2.5x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.321 → 0.887 | 0.567 | 0.319 → 0.880 | 3.8x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **text** | 0.311 → 0.790 | 0.479 | 0.305 → 0.770 | 4.8x sr_bytes | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.538 → 0.887 | 0.349 | 0.512 → 0.880 | 2.5x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.605 → 0.952 | 0.347 | 0.581 → 0.951 | 2x sr_bytes | up | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.575 → 0.917 | 0.343 | 0.560 → 0.913 | 9.3x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.605 → 0.937 | 0.332 | 0.589 → 0.935 | 7.9x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.410 → 0.738 | 0.328 | 0.399 → 0.723 | 2x sr_airtime | up | 2 |
| `DG-burst` | burst-loss | **text** | 0.560 → 0.887 | 0.327 | 0.526 → 0.880 | 2.4x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.444 → 0.748 | 0.304 | 0.291 → 0.486 | 5.9x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.684 → 0.940 | 0.256 | 0.640 → 0.939 | 2.8x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.727 → 0.968 | 0.241 | 0.717 → 0.965 | 5.4x sr_airtime | up | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.684 → 0.922 | 0.238 | 0.640 → 0.919 | 2.4x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.749 → 0.957 | 0.208 | 0.743 → 0.956 | 5.1x sr_airtime | down | 2 |
| `RT-spread` | hop-spread | **text** | 0.684 → 0.887 | 0.203 | 0.640 → 0.880 | 1.8x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **text** | 0.704 → 0.887 | 0.183 | 0.696 → 0.880 | 1.3x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.718 → 0.887 | 0.169 | 0.718 → 0.880 | 1.4x sr_airtime | down | 3 |
| `MS-size` | nodes | **text** | 0.727 → 0.887 | 0.160 | 0.712 → 0.880 | 6.4x sr_bytes | down | 5 |
| `DG-loss` | extra-loss | **text** | 0.746 → 0.887 | 0.142 | 0.731 → 0.880 | 1.9x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.806 → 0.921 | 0.114 | 0.797 → 0.915 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.806 → 0.921 | 0.114 | 0.797 → 0.915 | 2.2x bytes_on_air | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.816 → 0.922 | 0.106 | 0.804 → 0.919 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.816 → 0.922 | 0.106 | 0.806 → 0.919 | 2.2x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.839 → 0.930 | 0.091 | 0.827 → 0.927 | 4.6x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.895 → 0.977 | 0.081 | 0.878 → 0.880 | 28x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.887 → 0.963 | 0.075 | 0.880 → 0.962 | 2x sr_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.916 → 0.985 | 0.069 | 0.880 → 0.883 | 4x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.916 → 0.985 | 0.069 | 0.880 → 0.883 | 4x sr_bytes | up | 6 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.807 → 0.875 | 0.068 | 0.658 → 0.721 | 1.8x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.887 → 0.953 | 0.065 | 0.880 → 0.950 | 1.4x bytes_on_air | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.894 → 0.956 | 0.062 | 0.751 → 0.797 | 2x sr_bytes | up | 3 |
| `MS-roles` | role-mix | **text** | 0.806 → 0.866 | 0.059 | 0.797 → 0.860 | 1.3x sr_bytes | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.887 → 0.945 | 0.058 | 0.880 → 0.939 | 1.5x bytes_on_air | up | 3 |
| `SF-cadence` | trigger | **held** | 0.919 → 0.977 | 0.058 | 0.857 → 0.880 | 14x advert_bytes | down | 4 |
| `MS-roles-fav` | role-mix | **text** | 0.843 → 0.899 | 0.056 | 0.837 → 0.895 | 1.2x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.736 → 0.787 | 0.051 | 0.482 → 0.517 | 1.5x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.840 → 0.887 | 0.047 | 0.831 → 0.880 | 1.6x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.887 → 0.923 | 0.035 | 0.880 → 0.920 | 3.4x bytes_on_air | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.951 → 0.982 | 0.031 | 0.879 → 0.890 | 2.6x advert_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.880 → 0.910 | 0.029 | 0.878 → 0.909 | 3.5x bytes_on_air | up | 5 |
| `FW-mixed` | legacy-fraction | **text** | 0.868 → 0.897 | 0.029 | 0.865 → 0.890 | 2.3x bytes_on_air | down | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.869 → 0.897 | 0.028 | 0.867 → 0.889 | 2.3x bytes_on_air | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.887 → 0.915 | 0.028 | 0.880 → 0.911 | 1.2x sr_bytes | down | 3 |
| `SF-hops-flat` | hops-apart | **text** | 0.882 → 0.906 | 0.024 | 0.878 → 0.881 | 2.8x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.882 → 0.906 | 0.024 | 0.878 → 0.881 | 2.8x sr_bytes | up | 5 |
| `MS-router-late` | router-late-fraction | **held** | 0.953 → 0.977 | 0.023 | 0.877 → 0.885 | 1.3x bytes_on_air | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.954 → 0.977 | 0.023 | 0.861 → 0.880 | 1.4x sr_airtime | down | 2 |
| `DM-mode` | dm-mode | **held** | 0.925 → 0.947 | 0.022 | 0.851 → 0.867 | 1.4x sr_airtime | up | 3 |
| `AD-worst` | role-placement | **text** | 0.810 → 0.832 | 0.022 | 0.787 → 0.824 | 1.1x sr_bytes | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.892 → 0.913 | 0.021 | 0.886 → 0.908 | 1.1x sr_bytes | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.940 → 0.959 | 0.019 | 0.857 → 0.879 | 9.3x advert_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.887 → 0.904 | 0.017 | 0.869 → 0.880 | 3.4x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.924 → 0.941 | 0.016 | 0.861 → 0.861 | 1.1x sr_bytes | down | 2 |
| `SF-capacity` | capacity | **held** | 0.968 → 0.977 | 0.009 | 0.874 → 0.880 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.968 → 0.977 | 0.009 | 0.874 → 0.880 | 5.3x advert_bytes | down | 5 |
| `SF-window-size` | window-size | **text** | 0.877 → 0.886 | 0.009 | 0.869 → 0.879 | 4.9x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.973 → 0.982 | 0.008 | 0.884 → 0.890 | 1.3x sr_bytes | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.977 → 0.984 | 0.007 | 0.880 → 0.889 | 7.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.977 → 0.984 | 0.007 | 0.880 → 0.889 | 7.4x sr_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.970 → 0.977 | 0.007 | 0.877 → 0.880 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.970 → 0.977 | 0.007 | 0.877 → 0.880 | 1.2x sr_airtime | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.882 → 0.888 | 0.007 | 0.876 → 0.883 | 5.2x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **text** | 0.881 → 0.887 | 0.007 | 0.875 → 0.881 | 3.1x advert_bytes | down | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.861 → 0.867 | 0.006 | 0.861 → 0.867 | 1.2x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.882 → 0.888 | 0.006 | 0.875 → 0.882 | 2.7x advert_bytes | up | 4 |
| `SF-resolve` | resolve | **text** | 0.887 → 0.893 | 0.006 | 0.880 → 0.887 | 5.7x advert_bytes | = | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.952 → 0.957 | 0.005 | 0.950 → 0.956 | 1.2x sr_airtime | down | 2 |
| `FW-firmware` | profile | **text** | 0.887 → 0.893 | 0.005 | 0.880 → 0.890 | 3.5x bytes_on_air | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.879 → 0.884 | 0.005 | 0.875 → 0.883 | 3.5x sr_bytes | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.970 → 0.975 | 0.005 | 0.869 → 0.875 | 1.1x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.957 → 0.960 | 0.003 | 0.956 → 0.959 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.885 → 0.887 | 0.003 | 0.876 → 0.880 | 1.2x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.997 → 0.998 | 0.002 | 0.956 → 0.957 | 1x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.887 → 0.889 | 0.001 | 0.880 → 0.882 | 1x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.976 → 0.977 | 0.001 | 0.880 → 0.880 | 2.2x sr_airtime | down | 2 |

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
| none | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| sprinkled | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.995 | 0.995 | 0.794 | 1.27x | 17.2/23.4/26.1% | 1.9/5.1% | 3 |
| arms-race | 1 | 0.963 | 0.962 | 0.001 | - | - | 0.997 | 0.997 | 0.784 | 1.05x | 21.2/28.0/29.7% | 1.4/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.1 | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.991 | 0.991 | 0.815 | 1.14x | 17.8/23.8/26.3% | 1.6/5.0% | 3 |
| 0.3 | 1 | 0.953 | 0.950 | 0.003 | - | - | 0.998 | 0.999 | 0.899 | 1.05x | 20.4/27.1/29.8% | 1.4/4.8% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.806 | 0.797 | 0.009 | - | - | 0.934 | 0.936 | 0.457 | 1.26x | 15.0/26.3/30.2% | 1.9/5.4% | 3 |
| inverse | 1 | 0.769 | 0.751 | 0.018 | - | - | 0.894 | 0.932 | 0.389 | 1.17x | 14.7/20.2/22.0% | 2.1/4.3% | 3 |
| random | 1 | 0.776 | 0.765 | 0.011 | - | - | 0.956 | 0.961 | 0.440 | 1.20x | 14.4/22.7/26.4% | 2.1/5.1% | 3 |

> role-placement=inverse: decode_failures 25

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.806 | 0.797 | 0.009 | - | - | 0.934 | 0.936 | 0.457 | 1.26x | 15.0/26.3/30.2% | 1.9/5.4% | 3 |
| all-routers | 1 | 0.921 | 0.915 | 0.006 | - | - | 0.985 | 0.986 | 0.784 | 2.77x | 28.5/41.1/45.3% | 4.5/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.806 | 0.797 | 0.009 | - | - | 0.934 | 0.936 | 0.457 | 1.26x | 15.0/26.3/30.2% | 1.9/5.4% | 3 |
| no-mute | 1 | 0.854 | 0.846 | 0.008 | - | - | 0.969 | 0.973 | 0.654 | 1.36x | 16.4/22.5/26.6% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.921 | 0.915 | 0.006 | - | - | 0.985 | 0.986 | 0.784 | 2.77x | 28.5/41.1/45.3% | 4.5/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.806 | 0.797 | 0.009 | - | - | 0.934 | 0.936 | 0.457 | 1.26x | 15.0/26.3/30.2% | 1.9/5.4% | 3 |
| local-typical | 1 | 0.472 | 0.468 | 0.004 | - | - | 0.647 | 0.651 | 0.000 | 1.14x | 11.4/26.6/30.6% | 1.7/5.5% | 3 |
| basement-heavy | 1 | 0.056 | 0.054 | 0.001 | - | - | 0.269 | 0.271 | 0.000 | 0.44x | 0.2/6.0/11.1% | 0.2/2.7% | 3 |

> siting-mix=local-typical: decode_failures 3

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.832 | 0.824 | 0.009 | - | - | 0.933 | 0.946 | 0.000 | 2.26x | 15.2/28.1/33.9% | 1.7/5.6% | 3 |
| inverse | 1 | 0.810 | 0.787 | 0.023 | - | - | 0.931 | 0.944 | 0.000 | 2.16x | 14.6/24.1/30.7% | 1.7/3.0% | 3 |

> role-placement=degree: decode_failures 56

> role-placement=inverse: decode_failures 46

> slower: 17.7 s per simulated hour against 3.48 over 25 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.880 | 0.880 | 0.000 | - | - | 0 | 0.000 | 0.728 | 1.41x | 17.1/26.0/29.7% | 2.1/5.1% | 3 |
| sr | 1 | 0.890 | 0.878 | 0.013 | - | - | 0.984 | 0.985 | 0.724 | 1.46x | 17.7/26.9/30.7% | 2.1/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.816 | 0.804 | 0.012 | - | - | 0.911 | 0.912 | 0.647 | 3.33x | 38.6/59.5/65.4% | 4.8/10.1% | 3 |
| 100 | 1 | 0.922 | 0.919 | 0.004 | - | - | 0.976 | 0.977 | 0.825 | 1.68x | 19.6/32.1/35.9% | 2.4/5.4% | 3 |
| 120 | 1 | 0.922 | 0.919 | 0.004 | - | - | 0.976 | 0.977 | 0.825 | 1.68x | 19.6/32.1/35.9% | 2.4/5.4% | 3 |
| 250 | 1 | 0.922 | 0.919 | 0.004 | - | - | 0.976 | 0.977 | 0.825 | 1.68x | 19.6/32.1/35.9% | 2.4/5.4% | 3 |

> max-num-nodes=10: decode_failures 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.299 | 0.291 | 0.007 | - | - | 0.444 | 0.525 | 0.148 | 10.88x | 38.0/53.8/64.2% | 3.7/10.5% | 3 |
| 120 | 1 | 0.492 | 0.482 | 0.010 | - | - | 0.736 | 0.758 | 0.214 | 4.19x | 14.5/23.8/29.4% | 1.4/5.3% | 3 |
| 250 | 1 | 0.495 | 0.486 | 0.009 | - | - | 0.748 | 0.757 | 0.222 | 4.07x | 14.2/22.8/28.2% | 1.3/5.0% | 3 |

> max-num-nodes=10: decode_failures 43

> max-num-nodes=120: decode_failures 41

> max-num-nodes=250: decode_failures 20

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.922 | 0.919 | 0.004 | - | - | 0.976 | 0.977 | 0.825 | 1.68x | 19.6/32.1/35.9% | 2.4/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.922 | 0.919 | 0.004 | - | - | 0.976 | 0.977 | 0.825 | 1.68x | 19.6/32.1/35.9% | 2.4/5.4% | 3 |
| constrained | 1 | 0.816 | 0.806 | 0.010 | - | - | 0.906 | 0.914 | 0.652 | 3.33x | 38.5/59.5/65.5% | 4.8/10.1% | 3 |

> platform-mix=constrained: decode_failures 3

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.875 | 0.912 | 0.554 | 5.46x | 59.3/73.0/76.5% | 3.6/13.4% | 3 |
| 25 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.875 | 0.912 | 0.554 | 5.46x | 59.3/73.0/76.5% | 3.6/13.4% | 3 |
| 100 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.875 | 0.912 | 0.554 | 5.46x | 59.3/73.0/76.5% | 3.6/13.4% | 3 |
| 2000 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.875 | 0.912 | 0.554 | 5.46x | 59.3/73.0/76.5% | 3.6/13.4% | 3 |

> warm-num-nodes=0: queue drops 11.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 82

> warm-num-nodes=25: queue drops 11.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 82

> warm-num-nodes=100: queue drops 11.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 82

> warm-num-nodes=2000: queue drops 11.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 82

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.1 | 1 | 0.780 | 0.760 | 0.020 | - | - | 0.948 | 0.953 | 0.594 | 1.36x | 16.4/25.5/29.6% | 2.0/5.1% | 3 |
| 0.2 | 1 | 0.673 | 0.643 | 0.030 | - | - | 0.876 | 0.918 | 0.482 | 1.24x | 15.2/23.7/28.0% | 1.8/4.6% | 3 |
| 0.3 | 1 | 0.560 | 0.526 | 0.034 | - | - | 0.766 | 0.862 | 0.355 | 1.12x | 14.0/21.7/26.0% | 1.7/4.2% | 3 |

> burst-loss=0.2: decode_failures 17

> burst-loss=0.3: decode_failures 26

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.1 | 1 | 0.846 | 0.837 | 0.009 | - | - | 0.964 | 0.964 | 0.655 | 1.50x | 18.1/27.5/31.8% | 2.2/5.4% | 3 |
| 0.2 | 1 | 0.798 | 0.784 | 0.014 | - | - | 0.941 | 0.944 | 0.560 | 1.54x | 18.8/28.0/32.6% | 2.3/5.3% | 3 |
| 0.3 | 1 | 0.746 | 0.731 | 0.015 | - | - | 0.882 | 0.925 | 0.507 | 1.53x | 18.7/28.2/33.0% | 2.3/5.1% | 3 |

> extra-loss=0.2: decode_failures 2

> extra-loss=0.3: decode_failures 18

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.1 | 1 | 0.772 | 0.757 | 0.015 | - | - | 0.917 | 0.952 | 0.589 | 1.35x | 16.3/25.3/29.6% | 2.0/5.2% | 3 |
| 0.2 | 1 | 0.669 | 0.649 | 0.019 | - | - | 0.870 | 0.929 | 0.489 | 1.27x | 15.6/23.8/28.2% | 1.9/4.7% | 3 |
| 0.3 | 1 | 0.538 | 0.512 | 0.026 | - | - | 0.693 | 0.833 | 0.295 | 1.16x | 14.6/22.3/26.3% | 1.7/4.1% | 3 |

> burst-loss=0.1: decode_failures 35

> burst-loss=0.2: decode_failures 33

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.851 | 0.851 | 0.000 | - | - | 0.925 | 0.959 | 0.690 | 1.89x | 22.6/34.9/40.0% | 2.7/7.0% | 3 |
| directed-with-late-flood | 1 | 0.867 | 0.867 | 0.000 | - | - | 0.935 | 0.980 | 0.691 | 1.72x | 20.7/32.1/36.6% | 2.5/6.4% | 3 |
| m4-early-flood | 1 | 0.851 | 0.851 | 0.000 | - | - | 0.947 | 0.960 | 0.683 | 1.76x | 21.1/33.1/37.8% | 2.6/6.6% | 3 |

> dm-mode=flood-only: decode_failures 24

> dm-mode=directed-with-late-flood: decode_failures 23

> dm-mode=m4-early-flood: decode_failures 6

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.893 | 0.890 | 0.003 | - | - | 0.977 | 0.977 | 0.701 | 0.75x | 8.7/12.4/15.1% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.25 | 1 | 0.897 | 0.890 | 0.007 | - | - | 0.990 | 0.991 | 0.722 | 1.23x | 13.6/23.1/26.1% | 1.8/4.9% | 3 |
| 0.5 | 1 | 0.885 | 0.868 | 0.017 | - | - | 0.976 | 0.980 | 0.495 | 1.05x | 13.4/17.3/20.6% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.868 | 0.865 | 0.003 | - | - | 0.980 | 0.981 | 0.558 | 0.89x | 10.5/15.0/17.6% | 1.4/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.25 | 1 | 0.897 | 0.889 | 0.008 | - | - | 0.989 | 0.989 | 0.700 | 1.22x | 13.4/22.7/25.8% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.897 | 0.879 | 0.019 | - | - | 0.989 | 0.989 | 0.517 | 1.03x | 13.2/17.3/20.5% | 1.7/3.9% | 3 |
| 0.75 | 1 | 0.869 | 0.867 | 0.003 | - | - | 0.976 | 0.977 | 0.571 | 0.88x | 10.5/15.4/17.9% | 1.4/3.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.923 | 0.920 | 0.003 | - | - | 0.988 | 0.989 | 0.759 | 0.76x | 9.4/14.8/17.3% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.887 | 0.885 | 0.002 | - | - | 0.976 | 0.976 | 0.679 | 0.76x | 9.2/13.4/16.9% | 1.2/2.4% | 3 |
| 2.5 | 1 | 0.884 | 0.882 | 0.002 | - | - | 0.973 | 0.974 | 0.696 | 0.76x | 9.1/13.2/16.5% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.970 | 0.970 | 0.669 | 0.74x | 9.0/13.2/16.8% | 1.1/2.3% | 3 |
| 2.7 | 1 | 0.910 | 0.909 | 0.001 | - | - | 0.983 | 0.983 | 0.708 | 0.78x | 9.3/14.7/18.0% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.917 | 0.913 | 0.004 | - | - | 0.986 | 0.986 | 0.784 | 0.96x | 11.6/17.7/20.3% | 1.5/3.7% | 3 |
| 900 | 1 | 0.839 | 0.827 | 0.012 | - | - | 0.949 | 0.950 | 0.654 | 2.29x | 27.5/41.7/47.5% | 3.4/8.4% | 3 |
| 300 | 1 | 0.575 | 0.560 | 0.015 | - | - | 0.711 | 0.793 | 0.382 | 4.93x | 56.0/72.7/79.3% | 7.6/16.6% | 3 |

> broadcast-interval-s=300: decode_failures 10

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.937 | 0.935 | 0.002 | - | - | 0.988 | 0.988 | 0.835 | 1.02x | 12.3/18.0/20.6% | 1.6/3.6% | 3 |
| 900 | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.959 | 0.960 | 0.758 | 2.57x | 30.5/43.9/49.8% | 4.0/8.7% | 3 |
| 300 | 1 | 0.605 | 0.589 | 0.016 | - | - | 0.797 | 0.830 | 0.424 | 5.38x | 59.3/73.5/79.8% | 8.4/16.9% | 3 |

> broadcast-interval-s=300: decode_failures 27

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.915 | 0.911 | 0.004 | - | - | 0.987 | 0.988 | 0.755 | 1.32x | 16.0/24.7/28.3% | 1.9/5.1% | 3 |
| sinusoid | 1 | 0.898 | 0.892 | 0.006 | - | - | 0.976 | 0.976 | 0.749 | 1.31x | 15.7/23.9/27.5% | 1.9/4.8% | 3 |
| commuter | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.839 | 0.827 | 0.012 | - | - | 0.949 | 0.950 | 0.654 | 2.29x | 27.5/41.7/47.5% | 3.4/8.4% | 3 |
| 3600 | 1 | 0.917 | 0.913 | 0.004 | - | - | 0.986 | 0.986 | 0.784 | 0.96x | 11.6/17.7/20.3% | 1.5/3.7% | 3 |
| 10800 | 1 | 0.927 | 0.923 | 0.004 | - | - | 0.993 | 0.994 | 0.792 | 0.68x | 8.1/12.2/14.1% | 1.0/2.6% | 3 |
| 43200 | 1 | 0.930 | 0.927 | 0.002 | - | - | 0.990 | 0.990 | 0.805 | 0.47x | 5.6/8.4/9.7% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.25 | 1 | 0.883 | 0.877 | 0.006 | - | - | 0.977 | 0.978 | 0.691 | 1.54x | 18.5/28.5/32.7% | 2.3/5.8% | 3 |
| 1.0 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.976 | 0.977 | 0.690 | 1.70x | 20.6/31.7/36.2% | 2.5/6.4% | 3 |
| 4.0 | 1 | 0.840 | 0.831 | 0.009 | - | - | 0.945 | 0.946 | 0.666 | 2.06x | 25.0/38.8/44.6% | 3.1/7.8% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.875 | 0.912 | 0.554 | 5.46x | 59.3/73.0/76.5% | 3.6/13.4% | 3 |
| 1.0 | 1 | 0.662 | 0.658 | 0.004 | - | - | 0.807 | 0.879 | 0.509 | 5.95x | 62.5/75.2/78.6% | 4.0/14.6% | 3 |

> traceroute-per-hour=0.0: queue drops 11.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 82

> traceroute-per-hour=1.0: queue drops 19.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 88

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.727 | 0.717 | 0.009 | - | - | 0.845 | 0.848 | 0.499 | 1.35x | 18.2/26.6/29.1% | 3.1/6.9% | 3 |
| 60 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 90 | 1 | 0.951 | 0.951 | 0.001 | - | - | 0.995 | 0.995 | 0.833 | 1.63x | 19.2/30.0/34.2% | 1.5/4.9% | 3 |
| 120 | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.997 | 0.997 | 0.868 | 1.89x | 22.6/32.1/34.7% | 1.2/5.0% | 3 |
| 150 | 1 | 0.968 | 0.965 | 0.003 | - | - | 0.997 | 0.997 | 0.866 | 2.39x | 27.2/41.1/46.5% | 1.1/5.4% | 3 |

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 120 | 1 | 0.785 | 0.765 | 0.020 | - | - | 0.952 | 0.954 | 0.379 | 2.19x | 15.2/24.3/29.0% | 1.5/5.5% | 3 |
| 250 | 1 | 0.494 | 0.484 | 0.010 | - | - | 0.733 | 0.756 | 0.219 | 4.51x | 15.8/25.7/31.4% | 1.4/5.9% | 3 |
| 500 | 1 | 0.309 | 0.303 | 0.006 | - | - | 0.517 | 0.528 | 0.147 | 9.97x | 18.5/28.2/42.5% | 1.7/6.6% | 3 |

> nodes=250: decode_failures 141

> nodes=500: decode_failures 189

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.790 | 0.770 | 0.020 | - | - | 0.960 | 0.961 | 0.375 | 2.01x | 14.0/22.2/26.4% | 1.4/4.8% | 3 |
| 250 | 1 | 0.492 | 0.482 | 0.010 | - | - | 0.736 | 0.758 | 0.214 | 4.19x | 14.5/23.8/29.4% | 1.4/5.3% | 3 |
| 500 | 1 | 0.311 | 0.305 | 0.006 | - | - | 0.526 | 0.540 | 0.141 | 9.16x | 16.9/26.1/39.4% | 1.6/5.9% | 3 |

> nodes=250: decode_failures 41

> nodes=500: decode_failures 126

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.866 | 0.860 | 0.005 | - | - | 0.964 | 0.968 | 0.675 | 1.43x | 17.2/26.7/30.4% | 2.1/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.806 | 0.797 | 0.009 | - | - | 0.934 | 0.936 | 0.457 | 1.26x | 15.0/26.3/30.2% | 1.9/5.4% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.899 | 0.895 | 0.004 | - | - | 0.976 | 0.976 | 0.724 | 1.51x | 18.2/27.3/30.9% | 2.3/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.843 | 0.837 | 0.006 | - | - | 0.923 | 0.923 | 0.541 | 1.44x | 17.4/29.9/33.7% | 2.6/5.3% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.05 | 1 | 0.890 | 0.884 | 0.006 | - | - | 0.972 | 0.973 | 0.718 | 1.57x | 18.4/32.0/36.8% | 2.3/5.4% | 3 |
| 0.1 | 1 | 0.892 | 0.885 | 0.006 | - | - | 0.974 | 0.976 | 0.714 | 1.66x | 19.5/33.7/37.6% | 2.3/5.4% | 3 |
| 0.2 | 1 | 0.884 | 0.877 | 0.007 | - | - | 0.953 | 0.955 | 0.714 | 1.86x | 21.7/38.0/42.9% | 2.5/5.1% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| local-typical | 1 | 0.515 | 0.512 | 0.003 | - | - | 0.699 | 0.710 | 0.000 | 1.40x | 12.8/30.0/33.6% | 2.1/5.5% | 3 |
| event | 1 | 0.213 | 0.210 | 0.003 | - | - | 0.365 | 0.372 | 0.000 | 1.46x | 8.2/15.4/26.8% | 2.3/5.2% | 3 |
| backbone | 1 | 0.973 | 0.972 | 0.001 | - | - | 0.996 | 0.997 | 0.886 | 1.23x | 27.8/38.9/39.9% | 1.5/5.5% | 3 |

> siting-mix=local-typical: decode_failures 10

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.847 | 0.840 | 0.006 | - | - | 0.930 | 0.932 | 0.545 | 1.50x | 29.2/37.0/38.0% | 3.5/7.7% | 3 |
| 60 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 90 | 1 | 0.845 | 0.838 | 0.007 | - | - | 0.983 | 0.985 | 0.532 | 1.70x | 15.6/22.6/25.8% | 1.6/5.1% | 3 |
| 120 | 1 | 0.785 | 0.765 | 0.020 | - | - | 0.952 | 0.954 | 0.379 | 2.19x | 15.2/24.3/29.0% | 1.5/5.5% | 3 |
| 150 | 1 | 0.727 | 0.712 | 0.015 | - | - | 0.917 | 0.918 | 0.379 | 2.82x | 15.3/26.5/32.7% | 1.6/5.3% | 3 |

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 1.25 | 1 | 0.704 | 0.697 | 0.007 | - | - | 0.884 | 0.905 | 0.462 | 1.49x | 11.8/21.5/25.2% | 2.4/5.1% | 3 |
| 1.5 | 1 | 0.410 | 0.399 | 0.011 | - | - | 0.663 | 0.666 | 0.000 | 1.42x | 9.2/16.5/20.6% | 2.2/4.9% | 3 |
| 2.0 | 1 | 0.101 | 0.100 | 0.001 | - | - | 0.188 | 0.192 | 0.000 | 0.83x | 2.9/9.1/13.9% | 1.1/3.4% | 3 |

> stretch=1.25: decode_failures 20

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| clustered | 1 | 0.934 | 0.933 | 0.001 | - | - | 0.969 | 0.969 | 0.663 | 1.10x | 24.8/32.8/35.2% | 1.3/5.3% | 3 |
| corridor | 1 | 0.605 | 0.581 | 0.024 | - | - | 0.825 | 0.832 | 0.277 | 1.26x | 13.5/23.7/26.8% | 1.9/4.9% | 3 |
| hub | 1 | 0.952 | 0.951 | 0.001 | - | - | 0.982 | 0.983 | 0.747 | 1.20x | 26.7/35.1/36.8% | 1.7/5.6% | 3 |

> topology=corridor: decode_failures 4

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.867 | 0.867 | 0.000 | - | - | 0.935 | 0.980 | 0.691 | 1.72x | 20.7/32.1/36.6% | 2.5/6.4% | 3 |
| True | 1 | 0.861 | 0.861 | 0.000 | - | - | 0.941 | 0.976 | 0.687 | 1.73x | 20.8/32.6/37.2% | 2.5/6.5% | 3 |

> coding-rate-ladder=False: decode_failures 23

> coding-rate-ladder=True: decode_failures 23

> slower: 6.74 s per simulated hour against 2.79 over 25 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.861 | 0.861 | 0.000 | - | - | 0.941 | 0.976 | 0.687 | 1.73x | 20.8/32.6/37.2% | 2.5/6.5% | 3 |
| m4-early-flood | 1 | 0.861 | 0.861 | 0.000 | - | - | 0.924 | 0.968 | 0.673 | 1.72x | 20.6/32.0/36.5% | 2.5/6.4% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 23

> dm-mode=m4-early-flood: decode_failures 22

> slower: 8.63 s per simulated hour against 2.54 over 25 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.880 | 0.880 | 0.000 | - | - | 0 | 0.000 | 0.728 | 1.41x | 17.1/26.0/29.7% | 2.1/5.1% | 3 |
| chain | 1 | 0.871 | 0.868 | 0.003 | - | - | 0.920 | 0.967 | 0.699 | 1.67x | 19.9/31.0/35.6% | 2.5/6.3% | 3 |
| sr | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| True | 1 | 0.889 | 0.882 | 0.007 | - | - | 0.976 | 0.977 | 0.732 | 1.46x | 17.6/26.9/30.8% | 2.2/5.5% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.997 | 0.997 | 0.868 | 1.89x | 22.6/32.1/34.7% | 1.2/5.0% | 3 |
| True | 1 | 0.959 | 0.957 | 0.002 | - | - | 0.998 | 0.998 | 0.875 | 1.95x | 23.2/32.8/35.5% | 1.3/5.1% | 3 |

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.123 | 0.122 | 0.001 | - | - | 0.241 | 0.244 | 0.000 | 0.04x | 0.1/0.5/0.7% | 0.0/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.427 | 0.422 | 0.005 | - | - | 0.726 | 0.728 | 0.067 | 0.27x | 1.8/3.6/5.1% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.821 | 0.810 | 0.011 | - | - | 0.958 | 0.962 | 0.599 | 1.40x | 13.1/21.5/25.4% | 2.1/5.2% | 3 |

> preset=LONG_TURBO: decode_failures 1

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 0.25 | 1 | 0.891 | 0.885 | 0.006 | - | - | 0.969 | 0.970 | 0.740 | 1.36x | 19.3/28.3/31.6% | 2.0/5.5% | 3 |
| 1.0 | 1 | 0.945 | 0.939 | 0.006 | - | - | 0.987 | 0.989 | 0.857 | 0.98x | 25.5/31.2/33.6% | 1.3/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.321 | 0.319 | 0.002 | - | - | 0.640 | 0.641 | 0.000 | 0.15x | 0.7/2.1/3.4% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| LITE_FAST | 1 | 0.847 | 0.835 | 0.011 | - | - | 0.974 | 0.975 | 0.613 | 1.14x | 11.7/18.7/22.3% | 1.6/4.2% | 3 |
| NARROW_SLOW | 1 | 0.858 | 0.847 | 0.011 | - | - | 0.973 | 0.975 | 0.625 | 1.46x | 15.5/24.5/28.4% | 2.1/5.4% | 3 |

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| temporal | 1 | 0.816 | 0.805 | 0.010 | - | - | 0.937 | 0.961 | 0.573 | 1.45x | 17.2/25.6/29.7% | 2.1/5.3% | 3 |
| transient | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.972 | 0.973 | 0.729 | 1.44x | 17.3/26.7/30.6% | 2.1/5.5% | 3 |
| periodic | 1 | 0.704 | 0.696 | 0.008 | - | - | 0.798 | 0.799 | 0.549 | 1.32x | 16.0/24.2/28.1% | 2.0/4.7% | 3 |

> noise-profile=temporal: decode_failures 10

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.321 | 0.319 | 0.002 | - | - | 0.640 | 0.641 | 0.000 | 0.15x | 0.7/2.1/3.4% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| LONG_MODERATE | 1 | 0.832 | 0.824 | 0.008 | - | - | 0.946 | 0.949 | 0.699 | 3.51x | 47.6/68.5/70.7% | 5.1/11.4% | 3 |

> preset=LONG_MODERATE: decode_failures 15

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.037 | 0.037 | 0.000 | - | - | 0.075 | 0.079 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.123 | 0.122 | 0.001 | - | - | 0.241 | 0.244 | 0.000 | 0.04x | 0.1/0.5/0.7% | 0.0/0.2% | 3 |
| LONG_FAST | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| LONG_TURBO | 1 | 0.821 | 0.810 | 0.011 | - | - | 0.958 | 0.962 | 0.599 | 1.40x | 13.1/21.5/25.4% | 2.1/5.2% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.861 | 0.849 | 0.012 | - | - | 0.963 | 0.963 | 0.645 | 1.97x | 22.4/33.5/39.2% | 3.0/7.1% | 3 |

> preset=LONG_TURBO: decode_failures 1

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.819 | 0.812 | 0.007 | - | - | 0.908 | 0.909 | 0.649 | 1.41x | 17.1/26.3/30.2% | 2.1/5.2% | 3 |
| 10000 | 1 | 0.704 | 0.696 | 0.008 | - | - | 0.798 | 0.799 | 0.549 | 1.32x | 16.0/24.2/28.1% | 2.0/4.7% | 3 |
| 4000 | 1 | 0.433 | 0.430 | 0.003 | - | - | 0.471 | 0.555 | 0.286 | 1.12x | 14.0/20.5/24.3% | 1.7/3.5% | 3 |
| 2000 | 1 | 0.086 | 0.086 | 0.000 | - | - | 0.089 | 0.165 | 0.042 | 0.74x | 9.3/13.8/16.7% | 1.2/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 5

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.410 | 0.399 | 0.011 | - | - | 0.663 | 0.666 | 0.000 | 1.42x | 9.2/16.5/20.6% | 2.2/4.9% | 3 |
| 1.0 | 1 | 0.738 | 0.723 | 0.015 | - | - | 0.856 | 0.856 | 0.540 | 1.01x | 18.3/25.9/27.8% | 1.4/4.7% | 3 |

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 22 | 1 | 0.404 | 0.394 | 0.010 | - | - | 0.676 | 0.681 | 0.072 | 1.37x | 8.7/15.9/21.0% | 2.1/4.8% | 3 |
| 17 | 1 | 0.117 | 0.116 | 0.001 | - | - | 0.228 | 0.228 | 0.000 | 0.92x | 3.2/10.5/18.2% | 1.3/3.6% | 3 |
| 14 | 1 | 0.062 | 0.062 | 0.000 | - | - | 0.045 | 0.089 | 0.000 | 0.57x | 2.2/4.5/6.2% | 1.0/2.0% | 2 |

> tx-power=14: 3 archives requested, 2 placed - group on the placed count

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.997 | 0.997 | 0.868 | 1.89x | 22.6/32.1/34.7% | 1.2/5.0% | 3 |
| True | 1 | 0.952 | 0.950 | 0.002 | - | - | 0.998 | 0.998 | 0.860 | 2.28x | 27.0/37.6/40.1% | 1.5/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.892 | 0.886 | 0.006 | - | - | 0.974 | 0.977 | 0.748 | 1.52x | 17.7/31.1/34.8% | 2.2/5.4% | 3 |
| True | 1 | 0.913 | 0.908 | 0.004 | - | - | 0.974 | 0.974 | 0.813 | 1.60x | 18.7/31.4/35.0% | 2.3/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| random | 1 | 0.874 | 0.861 | 0.012 | - | - | 0.954 | 0.955 | 0.684 | 1.42x | 17.3/26.0/29.8% | 2.1/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.684 | 0.640 | 0.044 | - | - | 0.915 | 0.922 | 0.350 | 1.06x | 13.2/20.7/25.3% | 1.5/4.6% | 3 |
| 7 | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.984 | 0.984 | 0.829 | 1.56x | 18.7/27.4/31.3% | 2.4/5.5% | 3 |
| 15 | 1 | 0.940 | 0.939 | 0.001 | - | - | 0.982 | 0.982 | 0.841 | 1.59x | 19.0/27.7/31.6% | 2.5/5.5% | 3 |
| 32 | 1 | 0.940 | 0.939 | 0.001 | - | - | 0.982 | 0.982 | 0.841 | 1.59x | 19.0/27.7/31.6% | 2.5/5.5% | 3 |

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.684 | 0.640 | 0.044 | - | - | 0.915 | 0.922 | 0.350 | 1.06x | 13.2/20.7/25.3% | 1.5/4.6% | 3 |
| 5 | 1 | 0.858 | 0.846 | 0.011 | - | - | 0.972 | 0.972 | 0.670 | 1.44x | 17.5/26.4/30.4% | 2.2/5.4% | 3 |
| 7 | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.984 | 0.984 | 0.829 | 1.56x | 18.7/27.4/31.3% | 2.4/5.5% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| KNOWN_ONLY | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.878 | 0.878 | 0.000 | - | - | 0.895 | 0.976 | 0.724 | 1.44x | 17.4/26.7/30.5% | 2.1/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.684 | 0.640 | 0.044 | - | - | 0.915 | 0.922 | 0.350 | 1.06x | 13.2/20.7/25.3% | 1.5/4.6% | 3 |
| True | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| BALANCED | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| STRICT | 1 | 0.718 | 0.718 | 0.000 | - | - | 0.807 | 0.812 | 0.550 | 1.56x | 18.8/28.3/32.4% | 2.3/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| dm | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.976 | 0.977 | 0.718 | 1.44x | 17.4/26.6/30.8% | 2.1/5.6% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.882 | 0.875 | 0.007 | - | - | 0.974 | 0.975 | 0.699 | 1.45x | 17.5/27.0/31.0% | 2.1/5.5% | 3 |
| local | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| time | 1 | 0.888 | 0.882 | 0.007 | - | - | 0.971 | 0.977 | 0.721 | 1.47x | 17.6/27.3/31.3% | 2.1/5.6% | 3 |
| window | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.974 | 0.975 | 0.715 | 1.43x | 17.2/26.5/30.4% | 2.1/5.4% | 3 |

> bucket-mode=global: misdecodes 18

> bucket-mode=time: misdecodes 28

> bucket-mode=window: misdecodes 27

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.970 | 0.974 | 0.724 | 1.59x | 18.9/29.3/33.7% | 2.3/6.1% | 3 |
| 1800 | 1 | 0.888 | 0.882 | 0.007 | - | - | 0.971 | 0.977 | 0.721 | 1.47x | 17.6/27.3/31.3% | 2.1/5.6% | 3 |
| 3600 | 1 | 0.888 | 0.883 | 0.005 | - | - | 0.966 | 0.974 | 0.731 | 1.45x | 17.4/26.8/30.7% | 2.1/5.5% | 3 |

> time-bucket-s=600: misdecodes 102

> time-bucket-s=1800: misdecodes 28

> time-bucket-s=3600: misdecodes 14

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| interval | 1 | 0.868 | 0.857 | 0.011 | - | - | 0.962 | 0.969 | 0.690 | 1.87x | 21.6/34.8/40.3% | 2.6/7.7% | 3 |
| aimd | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.919 | 0.970 | 0.711 | 1.47x | 17.7/27.2/31.1% | 2.2/5.4% | 3 |
| bucket+interval | 1 | 0.865 | 0.857 | 0.008 | - | - | 0.959 | 0.960 | 0.691 | 1.93x | 22.2/35.8/41.7% | 2.8/8.0% | 3 |

> trigger=interval: misdecodes 14

> trigger=aimd: misdecodes 5

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 21

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.972 | 0.975 | 0.715 | 1.44x | 17.3/26.7/30.8% | 2.1/5.6% | 3 |
| 8 | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.968 | 0.968 | 0.710 | 1.44x | 17.4/26.6/30.5% | 2.1/5.5% | 3 |
| 16 | 1 | 0.884 | 0.877 | 0.007 | - | - | 0.973 | 0.974 | 0.709 | 1.45x | 17.4/26.8/30.8% | 2.1/5.5% | 3 |
| 32 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 50 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.971 | 0.974 | 0.719 | 1.44x | 17.4/26.9/30.8% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 83

> capacity=8: decode_failures 18

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.972 | 0.975 | 0.715 | 1.44x | 17.3/26.7/30.8% | 2.1/5.6% | 3 |
| 8 | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.968 | 0.968 | 0.710 | 1.44x | 17.4/26.6/30.5% | 2.1/5.5% | 3 |
| 16 | 1 | 0.884 | 0.877 | 0.007 | - | - | 0.973 | 0.974 | 0.709 | 1.45x | 17.4/26.8/30.8% | 2.1/5.5% | 3 |
| 32 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 50 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.971 | 0.974 | 0.719 | 1.44x | 17.4/26.9/30.8% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 83

> capacity=8: decode_failures 18

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.892 | 0.890 | 0.003 | - | - | 0.951 | 0.981 | 0.713 | 1.42x | 17.1/26.3/30.1% | 2.1/5.3% | 3 |
| 16 | 1 | 0.892 | 0.885 | 0.007 | - | - | 0.982 | 0.987 | 0.718 | 1.44x | 17.3/26.6/30.5% | 2.1/5.4% | 3 |
| 32 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.974 | 0.975 | 0.715 | 1.43x | 17.2/26.5/30.4% | 2.1/5.4% | 3 |

> capacity=8: misdecodes 18

> capacity=8: decode_failures 35

> capacity=16: misdecodes 19

> capacity=16: decode_failures 2

> capacity=32: misdecodes 27

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.865 | 0.857 | 0.008 | - | - | 0.959 | 0.960 | 0.691 | 1.93x | 22.2/35.8/41.7% | 2.8/8.0% | 3 |
| 02-06 | 1 | 0.882 | 0.879 | 0.003 | - | - | 0.941 | 0.975 | 0.730 | 1.50x | 18.0/28.0/32.2% | 2.2/5.8% | 3 |
| 00-08 | 1 | 0.880 | 0.876 | 0.004 | - | - | 0.940 | 0.974 | 0.725 | 1.56x | 18.5/29.0/33.6% | 2.3/6.2% | 3 |

> catch-up-hours=: misdecodes 21

> catch-up-hours=02-06: decode_failures 43

> catch-up-hours=00-08: decode_failures 43

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.882 | 0.881 | 0.001 | - | - | 0.976 | 0.976 | 0.720 | 1.43x | 17.2/26.3/30.0% | 2.1/5.2% | 3 |
| 2 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 3 | 1 | 0.890 | 0.878 | 0.013 | - | - | 0.984 | 0.985 | 0.724 | 1.46x | 17.7/26.9/30.7% | 2.1/5.4% | 3 |
| 4 | 1 | 0.906 | 0.878 | 0.028 | - | - | 0.974 | 0.989 | 0.745 | 1.46x | 17.7/26.9/30.7% | 2.2/5.4% | 3 |

> hops-apart=4: decode_failures 3

> faster: 1.81 s per simulated hour against 3.65 over 25 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.882 | 0.881 | 0.001 | - | - | 0.976 | 0.976 | 0.720 | 1.43x | 17.2/26.3/30.0% | 2.1/5.2% | 3 |
| 2 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 3 | 1 | 0.890 | 0.878 | 0.013 | - | - | 0.984 | 0.985 | 0.724 | 1.46x | 17.7/26.9/30.7% | 2.1/5.4% | 3 |
| 4 | 1 | 0.906 | 0.878 | 0.028 | - | - | 0.974 | 0.989 | 0.745 | 1.46x | 17.7/26.9/30.7% | 2.2/5.4% | 3 |
| 5 | 1 | 0.906 | 0.878 | 0.028 | - | - | 0.974 | 0.989 | 0.745 | 1.46x | 17.7/26.9/30.7% | 2.2/5.4% | 3 |

> hops-apart=4: decode_failures 3

> hops-apart=5: decode_failures 3

> faster: 2.15 s per simulated hour against 4.81 over 25 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.883 | 0.877 | 0.007 | - | - | 0.970 | 0.974 | 0.725 | 1.46x | 17.6/27.2/31.3% | 2.1/5.5% | 3 |
| 30 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 120 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.974 | 0.974 | 0.738 | 1.46x | 17.6/27.1/30.9% | 2.1/5.5% | 3 |
| 600 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.978 | 0.723 | 1.46x | 17.5/26.9/30.9% | 2.1/5.5% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.883 | 0.877 | 0.007 | - | - | 0.970 | 0.974 | 0.725 | 1.46x | 17.6/27.2/31.3% | 2.1/5.5% | 3 |
| 30 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 120 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.974 | 0.974 | 0.738 | 1.46x | 17.6/27.1/30.9% | 2.1/5.5% | 3 |
| 600 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.978 | 0.723 | 1.46x | 17.5/26.9/30.9% | 2.1/5.5% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.903 | 0.881 | 0.022 | - | - | 0.916 | 0.972 | 0.717 | 1.45x | 17.6/26.7/30.7% | 2.1/5.4% | 3 |
| routers | 1 | 0.884 | 0.883 | 0.001 | - | - | 0.979 | 0.980 | 0.714 | 1.47x | 17.7/27.1/31.0% | 2.2/5.4% | 3 |
| alternate-routers | 1 | 0.884 | 0.880 | 0.004 | - | - | 0.981 | 0.981 | 0.724 | 1.44x | 17.4/26.8/30.6% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.885 | 0.882 | 0.003 | - | - | 0.973 | 0.974 | 0.737 | 1.45x | 17.6/27.0/30.7% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.985 | 0.988 | 0.717 | 1.47x | 17.6/27.1/31.1% | 2.1/5.5% | 3 |
| hops-apart | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

> place=spread: decode_failures 20

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.903 | 0.881 | 0.022 | - | - | 0.916 | 0.972 | 0.717 | 1.45x | 17.6/26.7/30.7% | 2.1/5.4% | 3 |
| routers | 1 | 0.884 | 0.883 | 0.001 | - | - | 0.979 | 0.980 | 0.714 | 1.47x | 17.7/27.1/31.0% | 2.2/5.4% | 3 |
| alternate-routers | 1 | 0.884 | 0.880 | 0.004 | - | - | 0.981 | 0.981 | 0.724 | 1.44x | 17.4/26.8/30.6% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.885 | 0.882 | 0.003 | - | - | 0.973 | 0.974 | 0.737 | 1.45x | 17.6/27.0/30.7% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.985 | 0.988 | 0.717 | 1.47x | 17.6/27.1/31.1% | 2.1/5.5% | 3 |
| hops-apart | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

> place=spread: decode_failures 20

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| broadcast | 1 | 0.904 | 0.869 | 0.036 | - | - | 0.970 | 0.971 | 0.751 | 1.54x | 18.4/28.6/32.5% | 2.2/5.7% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| heard | 1 | 0.885 | 0.876 | 0.009 | - | - | 0.976 | 0.976 | 0.714 | 1.44x | 17.3/26.6/30.5% | 2.1/5.4% | 3 |

> replay-ordering=heard: misdecodes 9

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.904 | 0.869 | 0.036 | - | - | 0.970 | 0.971 | 0.751 | 1.54x | 18.4/28.6/32.5% | 2.2/5.7% | 3 |
| heard | 1 | 0.908 | 0.875 | 0.033 | - | - | 0.975 | 0.976 | 0.738 | 1.51x | 18.1/28.0/31.9% | 2.2/5.6% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| enum | 1 | 0.893 | 0.887 | 0.006 | - | - | 0.979 | 0.984 | 0.746 | 1.46x | 17.5/27.1/31.3% | 2.2/5.7% | 3 |
| hybrid | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.884 | 0.883 | 0.001 | - | - | 0.979 | 0.980 | 0.714 | 1.47x | 17.7/27.1/31.0% | 2.2/5.4% | 3 |
| 6 | 1 | 0.879 | 0.875 | 0.003 | - | - | 0.975 | 0.976 | 0.706 | 1.49x | 17.9/27.7/31.6% | 2.1/5.6% | 6 |

> servers=6: misdecodes 3

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.890 | 0.889 | 0.002 | - | - | 0.980 | 0.980 | 0.731 | 1.44x | 17.5/26.6/30.4% | 2.1/5.3% | 2 |
| 3 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 5 | 1 | 0.892 | 0.880 | 0.012 | - | - | 0.984 | 0.985 | 0.725 | 1.48x | 17.8/27.6/31.4% | 2.2/5.6% | 5 |
| 8 | 1 | 0.892 | 0.881 | 0.012 | - | - | 0.984 | 0.987 | 0.730 | 1.52x | 18.3/28.1/32.1% | 2.2/5.6% | 8 |

> servers=5: misdecodes 1

> servers=8: misdecodes 2

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.890 | 0.889 | 0.002 | - | - | 0.980 | 0.980 | 0.731 | 1.44x | 17.5/26.6/30.4% | 2.1/5.3% | 2 |
| 3 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 5 | 1 | 0.892 | 0.880 | 0.012 | - | - | 0.984 | 0.985 | 0.725 | 1.48x | 17.8/27.6/31.4% | 2.2/5.6% | 5 |
| 8 | 1 | 0.892 | 0.881 | 0.012 | - | - | 0.984 | 0.987 | 0.730 | 1.52x | 18.3/28.1/32.1% | 2.2/5.6% | 8 |

> servers=5: misdecodes 1

> servers=8: misdecodes 2

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| True | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.895 | 0.890 | 0.006 | - | - | 0.973 | 0.980 | 0.738 | 1.37x | 16.5/25.4/29.1% | 2.0/5.2% | 3 |
| 1 | 1 | 0.891 | 0.884 | 0.006 | - | - | 0.976 | 0.980 | 0.723 | 1.36x | 16.4/25.2/28.8% | 2.0/5.1% | 3 |
| 2 | 1 | 0.892 | 0.885 | 0.007 | - | - | 0.982 | 0.984 | 0.720 | 1.38x | 16.6/25.6/29.3% | 2.0/5.2% | 3 |
| 4 | 1 | 0.895 | 0.888 | 0.008 | - | - | 0.976 | 0.980 | 0.739 | 1.34x | 16.2/24.9/28.5% | 1.9/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.978 | 0.979 | 0.716 | 1.43x | 17.4/26.6/30.4% | 2.1/5.4% | 3 |
| 24 | 1 | 0.887 | 0.881 | 0.007 | - | - | 0.978 | 0.980 | 0.711 | 1.45x | 17.5/26.8/30.9% | 2.1/5.5% | 3 |
| 32 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.705 | 1.47x | 17.6/27.0/31.0% | 2.2/5.5% | 3 |
| 64 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.972 | 0.974 | 0.710 | 1.45x | 17.5/26.9/30.9% | 2.1/5.5% | 3 |

> short-id-bits=64: misdecodes 1

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.877 | 0.869 | 0.008 | - | - | 0.969 | 0.972 | 0.709 | 1.54x | 18.4/28.6/32.6% | 2.2/5.8% | 3 |
| 16 | 1 | 0.882 | 0.874 | 0.008 | - | - | 0.975 | 0.977 | 0.715 | 1.49x | 18.0/27.6/31.6% | 2.2/5.6% | 3 |
| 32 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.974 | 0.975 | 0.715 | 1.43x | 17.2/26.5/30.4% | 2.1/5.4% | 3 |

> window-size=8: misdecodes 102

> window-size=16: misdecodes 60

> window-size=32: misdecodes 27

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.997 | 0.997 | 0.868 | 1.89x | 22.6/32.1/34.7% | 1.2/5.0% | 3 |
| True | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.897 | 0.931 | 0.580 | 5.43x | 59.0/73.0/76.3% | 3.5/13.3% | 3 |

> no-congestion-scaling=True: queue drops 10.6% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 77

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.492 | 0.482 | 0.010 | - | - | 0.736 | 0.758 | 0.214 | 4.19x | 14.5/23.8/29.4% | 1.4/5.3% | 3 |
| truesize | 1 | 0.527 | 0.517 | 0.010 | - | - | 0.787 | 0.794 | 0.218 | 3.19x | 11.0/19.2/24.0% | 1.0/4.6% | 3 |

> congestion-input=hotstore: decode_failures 41

> congestion-input=truesize: decode_failures 45

> slower: 28.7 s per simulated hour against 10.3 over 25 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.998 | 0.998 | 0.877 | 1.81x | 21.8/30.5/32.9% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.997 | 0.997 | 0.868 | 1.89x | 22.6/32.1/34.7% | 1.2/5.0% | 3 |

> congestion-mode=static: misdecodes 1

