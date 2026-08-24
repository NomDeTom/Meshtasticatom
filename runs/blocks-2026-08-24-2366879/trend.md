# Sweep blocks-2026-08-24-2366879

- **sim version** `1.4.0`
- **transport** `591429c`
- **ground** ridge
- **seed base** 2366879 · seeds 2366879
- **blocks** 86 run, 1 missing
- **compute** 12.1 h of simulator time across every cell
- **generated** 2026-08-24T05:01:12+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>90 warnings</summary>

- D-cadence: trigger=interval: misdecodes 21
- D-cadence: trigger=aimd: misdecodes 2
- D-cadence: trigger=aimd: decode_failures 2
- D-cadence: trigger=bucket+interval: misdecodes 22
- E-capacity: capacity=4: decode_failures 92
- E-capacity: capacity=8: decode_failures 52
- F-burst: burst-loss=0.2: decode_failures 2
- F-burst: burst-loss=0.3: decode_failures 34
- F-loss: extra-loss=0.3: decode_failures 1
- F-outage: burst-loss=0.1: decode_failures 35
- F-outage: burst-loss=0.2: decode_failures 7
- F-outage: burst-loss=0.3: decode_failures 41
- F-txpower: faster: 1.06 s per simulated hour against 2.33 over 3 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- G-hops: hops-apart=4: decode_failures 19
- G-place: place=spread: decode_failures 13
- J-bucketmode: bucket-mode=global: misdecodes 39
- J-bucketmode: bucket-mode=time: misdecodes 26
- J-bucketmode: bucket-mode=window: misdecodes 28
- J-timewin: time-bucket-s=600: misdecodes 124
- J-timewin: time-bucket-s=1800: misdecodes 26
- J-timewin: time-bucket-s=3600: misdecodes 6
- J-wincap: capacity=8: misdecodes 24
- J-wincap: capacity=8: decode_failures 44
- J-wincap: capacity=16: misdecodes 16
- J-wincap: capacity=16: decode_failures 2
- J-wincap: capacity=32: misdecodes 28
- J-window: window-size=8: misdecodes 92
- J-window: window-size=16: misdecodes 64
- J-window: window-size=32: misdecodes 28
- M-capacity: capacity=4: decode_failures 92
- M-capacity: capacity=8: decode_failures 52
- M-combined: replay-ordering=heard: misdecodes 10
- M-replayorder: replay-ordering=heard: misdecodes 21
- N-hops: hops-apart=4: decode_failures 19
- N-hops: hops-apart=5: decode_failures 19
- N-place: place=spread: decode_failures 13
- P-bw500: preset=MEDIUM_TURBO: decode_failures 1
- P-catchup: catch-up-hours=: misdecodes 22
- P-catchup: catch-up-hours=02-06: decode_failures 31
- P-catchup: catch-up-hours=00-08: misdecodes 1
- P-catchup: catch-up-hours=00-08: decode_failures 32
- P-congestion: no-congestion-scaling=True: queue drops 16.4% of transmissions - airtime here is measured through a cap
- P-congestion: no-congestion-scaling=True: decode_failures 100
- P-preset: preset=LONG_MODERATE: decode_failures 9
- Q-topology: topology=hub: misdecodes 1
- R-congestion-input: congestion-input=hotstore: decode_failures 18
- R-congestion-input: congestion-input=truesize: decode_failures 8
- R-firmware: profile=legacy: decode_failures 37
- R-firmware: slower: 7.35 s per simulated hour against 1.93 over 3 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- R-hopscale: nodes=250: decode_failures 113
- R-hopscale: nodes=500: decode_failures 101
- R-hotstore-stress: max-num-nodes=10: decode_failures 38
- R-hotstore-stress: max-num-nodes=120: decode_failures 18
- R-hotstore-stress: max-num-nodes=250: decode_failures 73
- R-mixed-26: legacy-fraction=0.5: decode_failures 23
- R-mixed-26: slower: 3.62 s per simulated hour against 1.71 over 3 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- R-mixed: legacy-fraction=0.5: decode_failures 3
- R-oversubscribed: nodes=250: decode_failures 18
- R-oversubscribed: nodes=500: decode_failures 4
- R-platform: platform-mix=constrained: decode_failures 1
- R-signing: signature-policy=STRICT: decode_failures 2
- R-traceroute-small: traceroute-per-hour=0.0: queue drops 19.0% of transmissions - airtime here is measured through a cap
- R-traceroute-small: traceroute-per-hour=0.0: decode_failures 81
- R-traceroute-small: traceroute-per-hour=1.0: queue drops 26.7% of transmissions - airtime here is measured through a cap
- R-traceroute-small: traceroute-per-hour=1.0: decode_failures 57
- R-versions: profile=2.4: decode_failures 46
- R-versions: profile=2.5: decode_failures 44
- R-versions: profile=2.6: decode_failures 40
- R-versions: profile=2.7: decode_failures 39
- R-versions: slower: 11.4 s per simulated hour against 1.92 over 3 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- R-warm: warm-num-nodes=0: queue drops 19.0% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=0: decode_failures 81
- R-warm: warm-num-nodes=25: queue drops 19.0% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=25: decode_failures 81
- R-warm: warm-num-nodes=100: queue drops 19.0% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=100: decode_failures 81
- R-warm: warm-num-nodes=2000: queue drops 19.0% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=2000: decode_failures 81
- X-badrouters: role-placement=inverse: decode_failures 3
- X-badrouters: role-placement=random: decode_failures 2
- X-chatty-hops: broadcast-interval-s=300: decode_failures 3
- X-chatty: broadcast-interval-s=300: decode_failures 4
- X-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- X-stretch-duct: duct-per-hour=0.0: decode_failures 1
- X-stretch-duct: duct-per-hour=1.0: decode_failures 30
- X-stretch: stretch=1.25: decode_failures 13
- X-stretch: stretch=1.5: decode_failures 1
- X-worst: role-placement=degree: decode_failures 60
- X-worst: role-placement=inverse: decode_failures 43
- X-worst: slower: 18.1 s per simulated hour against 3.33 over 3 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

</details>

Blocks that produced no JSON (their job failed, timed out, or was cancelled): `F-preset-turbo`

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `R-versions` | 11.4 | 1.92 | 5.96x | 3 |
| `X-worst` | 18.1 | 3.33 | 5.45x | 3 |
| `R-firmware` | 7.35 | 1.93 | 3.80x | 3 |
| `R-mixed-26` | 3.62 | 1.71 | 2.12x | 3 |
| `R-hotstore` | 3.38 | 1.99 | 1.70x | 3 |
| `R-srretries` | 2.16 | 1.29 | 1.68x | 3 |
| `P-diurnal` | 2.3 | 1.47 | 1.57x | 3 |
| `X-chatty` | 3 | 4.58 | 0.66x | 3 |
| `K-hopspread` | 1.44 | 2.31 | 0.62x | 3 |
| `G-place` | 2.06 | 3.47 | 0.59x | 3 |
| `X-stretch` | 2 | 3.48 | 0.57x | 3 |
| `P-bw500` | 1.43 | 2.64 | 0.54x | 3 |
| `J-window` | 1.06 | 2.03 | 0.52x | 3 |
| `F-txpower` | 1.06 | 2.33 | 0.46x | 3 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `Q-control` | protocol | **held** | 0 → 0.981 | 0.981 | 0.850 → 0.872 | 1x bytes_on_air | up | 2 |
| `Q-protocol` | protocol | **held** | 0 → 0.961 | 0.961 | 0.833 → 0.861 | 1.2x bytes_on_air | up | 3 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.129 → 0.903 | 0.774 | 0.107 → 0.793 | 1e+02x sr_airtime | down | 4 |
| `F-txpower` | tx-power | **text** | 0.104 → 0.861 | 0.756 | 0.104 → 0.861 | 7.2x sr_airtime | down | 4 |
| `X-stretch` | stretch | **text** | 0.129 → 0.861 | 0.732 | 0.129 → 0.861 | 7.3x sr_airtime | down | 4 |
| `R-siting` | siting-mix | **text** | 0.255 → 0.980 | 0.725 | 0.255 → 0.980 | 4.5x sr_airtime | up | 4 |
| `X-siting` | siting-mix | **text** | 0.089 → 0.793 | 0.704 | 0.089 → 0.793 | 2.9x advert_bytes | down | 3 |
| `P-preset` | preset | **held** | 0.312 → 0.980 | 0.668 | 0.226 → 0.861 | 7.5x sr_airtime | up | 3 |
| `P-bw500` | preset | **held** | 0.312 → 0.967 | 0.655 | 0.163 → 0.773 | 7.5x sr_bytes | up | 3 |
| `P-eu-presets` | preset | **held** | 0.312 → 0.961 | 0.648 | 0.226 → 0.861 | 4.9x sr_airtime | up | 4 |
| `R-hopscale` | nodes | **text** | 0.310 → 0.861 | 0.551 | 0.310 → 0.861 | 10x sr_bytes | down | 4 |
| `X-stretch-duct` | duct-per-hour | **held** | 0.339 → 0.835 | 0.496 | 0.276 → 0.733 | 14x sr_airtime | up | 2 |
| `R-oversubscribed` | nodes | **held** | 0.510 → 0.952 | 0.442 | 0.316 → 0.738 | 4.5x bytes_on_air | down | 3 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.567 → 0.930 | 0.364 | 0.567 → 0.930 | 11x sr_airtime | down | 3 |
| `X-chatty` | broadcast-interval-s | **text** | 0.517 → 0.877 | 0.360 | 0.517 → 0.877 | 11x sr_airtime | down | 3 |
| `Q-topology` | topology | **text** | 0.610 → 0.963 | 0.353 | 0.610 → 0.963 | 1.7x sr_bytes | up | 4 |
| `F-outage` | burst-loss | **text** | 0.518 → 0.861 | 0.343 | 0.518 → 0.861 | 2.1x sr_bytes | down | 4 |
| `F-burst` | burst-loss | **text** | 0.552 → 0.861 | 0.309 | 0.552 → 0.861 | 2.5x sr_bytes | down | 4 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.419 → 0.698 | 0.279 | 0.320 → 0.524 | 7x sr_airtime | up | 3 |
| `P-congestion` | no-congestion-scaling | **text** | 0.747 → 0.968 | 0.221 | 0.747 → 0.968 | 3.3x sr_airtime | down | 2 |
| `F-hoplimit` | hop-limit | **text** | 0.711 → 0.930 | 0.219 | 0.711 → 0.930 | 1.6x sr_bytes | up | 4 |
| `K-density` | nodes | **text** | 0.767 → 0.969 | 0.202 | 0.767 → 0.969 | 5.2x sr_airtime | up | 5 |
| `K-hopspread` | hop-limit | **text** | 0.711 → 0.913 | 0.202 | 0.711 → 0.913 | 1.5x bytes_on_air | up | 3 |
| `X-noise` | noise-profile | **text** | 0.679 → 0.861 | 0.181 | 0.679 → 0.861 | 1.3x sr_airtime | down | 4 |
| `K-size` | nodes | **text** | 0.719 → 0.882 | 0.164 | 0.719 → 0.882 | 4.9x sr_bytes | down | 5 |
| `K-spread` | hop-spread | **text** | 0.711 → 0.861 | 0.150 | 0.711 → 0.861 | 1.3x bytes_on_air | up | 2 |
| `F-loss` | extra-loss | **text** | 0.719 → 0.861 | 0.141 | 0.719 → 0.861 | 1.5x sr_bytes | down | 4 |
| `R-signing` | signature-policy | **text** | 0.729 → 0.861 | 0.131 | 0.729 → 0.861 | 1.3x sr_airtime | down | 3 |
| `R-hotstore` | max-num-nodes | **text** | 0.745 → 0.876 | 0.131 | 0.745 → 0.876 | 2.2x sr_airtime | up | 4 |
| `R-platform` | platform-mix | **text** | 0.761 → 0.876 | 0.115 | 0.761 → 0.876 | 2.2x sr_airtime | down | 3 |
| `Q-interval` | broadcast-interval-s | **text** | 0.786 → 0.901 | 0.115 | 0.786 → 0.901 | 6.1x sr_airtime | up | 4 |
| `F-flooding` | role-mix | **text** | 0.793 → 0.892 | 0.099 | 0.793 → 0.892 | 2.4x bytes_on_air | up | 2 |
| `X-nomute` | role-mix | **text** | 0.793 → 0.892 | 0.099 | 0.793 → 0.892 | 2.4x bytes_on_air | up | 3 |
| `X-amplify-worst` | amplify-worst | **text** | 0.861 → 0.960 | 0.099 | 0.861 → 0.960 | 1.7x sr_bytes | up | 3 |
| `X-amplifiers` | amplifier-mix | **text** | 0.861 → 0.953 | 0.092 | 0.861 → 0.953 | 1.5x sr_bytes | up | 3 |
| `X-badrouters` | role-placement | **text** | 0.709 → 0.793 | 0.085 | 0.709 → 0.793 | 1.6x sr_bytes | down | 3 |
| `G-place` | place | **held** | 0.915 → 0.988 | 0.074 | 0.854 → 0.877 | 2.3x sr_bytes | up | 6 |
| `N-place` | place | **held** | 0.915 → 0.988 | 0.074 | 0.854 → 0.877 | 2.3x sr_bytes | up | 6 |
| `D-cadence` | trigger | **held** | 0.889 → 0.961 | 0.072 | 0.821 → 0.861 | 14x advert_bytes | down | 4 |
| `R-traceroute-small` | traceroute-per-hour | **held** | 0.770 → 0.841 | 0.070 | 0.661 → 0.726 | 1.2x sr_airtime | down | 2 |
| `X-duct` | duct-per-hour | **text** | 0.861 → 0.930 | 0.069 | 0.861 → 0.930 | 1.5x bytes_on_air | up | 3 |
| `G-hops` | hops-apart | **held** | 0.912 → 0.981 | 0.069 | 0.853 → 0.882 | 2.8x sr_bytes | up | 4 |
| `N-hops` | hops-apart | **held** | 0.912 → 0.981 | 0.069 | 0.853 → 0.882 | 2.8x sr_bytes | up | 5 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.793 → 0.861 | 0.068 | 0.793 → 0.861 | 1.6x sr_airtime | down | 4 |
| `R-roles` | role-mix | **text** | 0.793 → 0.853 | 0.060 | 0.793 → 0.853 | 1.2x bytes_on_air | down | 2 |
| `R-mixed-26` | legacy-fraction | **held** | 0.941 → 0.992 | 0.051 | 0.845 → 0.886 | 2.2x bytes_on_air | up | 4 |
| `R-mixed` | legacy-fraction | **text** | 0.845 → 0.890 | 0.045 | 0.845 → 0.890 | 2.1x bytes_on_air | up | 4 |
| `R-congestion-input` | congestion-input | **held** | 0.698 → 0.742 | 0.045 | 0.521 → 0.554 | 1.5x sr_airtime | up | 2 |
| `R-versions` | profile | **held** | 0.922 → 0.961 | 0.039 | 0.841 → 0.861 | 3.1x bytes_on_air | up | 5 |
| `R-roles-fav` | role-mix | **text** | 0.815 → 0.853 | 0.038 | 0.815 → 0.853 | 1.1x bytes_on_air | down | 2 |
| `G-servers` | servers | **held** | 0.950 → 0.988 | 0.037 | 0.851 → 0.862 | 8.3x sr_bytes | up | 4 |
| `N-servers` | servers | **held** | 0.950 → 0.988 | 0.037 | 0.851 → 0.862 | 8.3x sr_bytes | up | 4 |
| `P-catchup` | catch-up-hours | **text** | 0.821 → 0.854 | 0.033 | 0.821 → 0.854 | 9.2x advert_bytes | up | 3 |
| `R-signing-cost` | profile-flag | **text** | 0.861 → 0.892 | 0.031 | 0.861 → 0.892 | 3.3x bytes_on_air | down | 2 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.930 → 0.961 | 0.031 | 0.861 → 0.861 | 10x sr_airtime | down | 3 |
| `R-dmmode` | dm-mode | **text** | 0.786 → 0.812 | 0.026 | 0.786 → 0.812 | 1.1x sr_airtime | up | 3 |
| `R-firmware` | profile | **held** | 0.935 → 0.961 | 0.026 | 0.842 → 0.861 | 3.1x bytes_on_air | up | 2 |
| `X-worst` | role-placement | **text** | 0.743 → 0.768 | 0.025 | 0.743 → 0.768 | 1.1x sr_bytes | down | 2 |
| `E-capacity` | capacity | **held** | 0.946 → 0.967 | 0.021 | 0.845 → 0.861 | 5.3x advert_bytes | up | 5 |
| `M-capacity` | capacity | **held** | 0.946 → 0.967 | 0.021 | 0.845 → 0.861 | 5.3x advert_bytes | up | 5 |
| `P-diurnal` | diurnal | **text** | 0.855 → 0.875 | 0.020 | 0.855 → 0.875 | 1.2x advert_bytes | down | 3 |
| `J-wincap` | capacity | **held** | 0.937 → 0.957 | 0.020 | 0.854 → 0.859 | 2.2x advert_bytes | up | 3 |
| `D-resolve` | resolve | **held** | 0.941 → 0.961 | 0.020 | 0.844 → 0.861 | 5.9x advert_bytes | = | 3 |
| `J-timewin` | time-bucket-s | **held** | 0.943 → 0.961 | 0.019 | 0.838 → 0.849 | 5.3x advert_bytes | up | 3 |
| `L-provide` | provide-transport | **text** | 0.861 → 0.878 | 0.017 | 0.861 → 0.878 | 3.1x sr_airtime | up | 2 |
| `R-favourites` | favourite-routers | **text** | 0.850 → 0.867 | 0.017 | 0.850 → 0.867 | 1.1x sr_bytes | up | 2 |
| `R-srretries` | sr-retries | **held** | 0.949 → 0.966 | 0.017 | 0.853 → 0.860 | 1.1x sr_bytes | down | 4 |
| `R-routerlate` | router-late-fraction | **held** | 0.952 → 0.968 | 0.015 | 0.853 → 0.865 | 1.3x bytes_on_air | down | 4 |
| `R-dmmode-cr` | dm-mode | **text** | 0.800 → 0.813 | 0.014 | 0.800 → 0.813 | 1.1x sr_bytes | up | 2 |
| `J-window` | window-size | **held** | 0.948 → 0.961 | 0.013 | 0.848 → 0.859 | 4.8x advert_bytes | up | 3 |
| `J-bucketmode` | bucket-mode | **text** | 0.848 → 0.861 | 0.013 | 0.848 → 0.861 | 3x advert_bytes | up | 4 |
| `Q-hopassign` | hop-assign | **held** | 0.948 → 0.961 | 0.013 | 0.852 → 0.861 | 1.1x advert_bytes | down | 2 |
| `M-replayorder` | replay-ordering | **text** | 0.848 → 0.861 | 0.013 | 0.848 → 0.861 | 1.2x sr_bytes | down | 2 |
| `E-width` | short-id-bits | **held** | 0.949 → 0.961 | 0.012 | 0.851 → 0.861 | 3.1x advert_bytes | up | 4 |
| `D-jitter` | advert-jitter-s | **text** | 0.852 → 0.861 | 0.009 | 0.852 → 0.861 | 1.1x sr_airtime | down | 4 |
| `M-jitter` | advert-jitter-s | **text** | 0.852 → 0.861 | 0.009 | 0.852 → 0.861 | 1.1x sr_airtime | down | 4 |
| `R-crladder` | coding-rate-ladder | **text** | 0.800 → 0.807 | 0.008 | 0.800 → 0.807 | 1.2x sr_airtime | down | 2 |
| `R-adopt` | no-adopt-hop-recommendation | **text** | 0.961 → 0.968 | 0.007 | 0.961 → 0.968 | 1.1x bytes_on_air | down | 2 |
| `G-allrouters` | servers | **text** | 0.854 → 0.859 | 0.005 | 0.854 → 0.859 | 2.6x sr_bytes | up | 2 |
| `L-advert` | advert-transport | **text** | 0.856 → 0.861 | 0.005 | 0.856 → 0.861 | 3.5x sr_airtime | down | 2 |
| `R-repeats` | extra-repeats | **held** | 0.961 → 0.966 | 0.005 | 0.861 → 0.861 | 1.1x sr_airtime | up | 2 |
| `M-combined` | replay-ordering | **held** | 0.946 → 0.951 | 0.004 | 0.877 → 0.878 | 1x sr_bytes | up | 2 |
| `R-congestion-mode` | congestion-mode | **text** | 0.968 → 0.970 | 0.002 | 0.968 → 0.970 | 1.1x sr_airtime | down | 2 |
| `R-repeats-busy` | extra-repeats | **text** | 0.968 → 0.968 | 0.000 | 0.968 → 0.968 | 1x sr_bytes | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `E-signed` | signed | 1.4x advert_bytes | 2 |
| `R-warm` | warm-num-nodes | - | 4 |

## Every block

### `D-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| interval | 0.830 | - | - | 0.937 | 0.937 | 0.594 | 1.71x | 30.4/35.5% | 6.6% | 3 |
| aimd | 0.843 | - | - | 0.889 | 0.954 | 0.609 | 1.25x | 23.6/27.0% | 4.8% | 3 |
| bucket+interval | 0.821 | - | - | 0.936 | 0.938 | 0.572 | 1.74x | 31.0/36.2% | 6.9% | 3 |

> trigger=interval: misdecodes 21

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 2

> trigger=bucket+interval: misdecodes 22

### `D-jitter` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.854 | - | - | 0.958 | 0.960 | 0.615 | 1.27x | 23.9/27.7% | 4.9% | 3 |
| 30 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 120 | 0.853 | - | - | 0.954 | 0.955 | 0.603 | 1.26x | 23.7/27.4% | 4.9% | 3 |
| 600 | 0.852 | - | - | 0.952 | 0.952 | 0.613 | 1.27x | 24.0/27.6% | 4.9% | 3 |

### `D-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| enum | 0.844 | - | - | 0.941 | 0.947 | 0.605 | 1.24x | 23.5/27.1% | 4.8% | 3 |
| hybrid | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

### `E-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.850 | - | - | 0.946 | 0.949 | 0.615 | 1.25x | 23.6/27.1% | 4.8% | 3 |
| 8 | 0.856 | - | - | 0.956 | 0.959 | 0.630 | 1.25x | 23.8/27.1% | 4.8% | 3 |
| 16 | 0.855 | - | - | 0.967 | 0.970 | 0.616 | 1.25x | 23.6/27.1% | 4.8% | 3 |
| 32 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 50 | 0.845 | - | - | 0.951 | 0.952 | 0.620 | 1.26x | 23.9/27.4% | 4.9% | 3 |

> capacity=4: decode_failures 92

> capacity=8: decode_failures 52

### `E-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| True | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

### `E-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 0.851 | - | - | 0.949 | 0.949 | 0.607 | 1.26x | 23.8/27.3% | 4.9% | 3 |
| 24 | 0.856 | - | - | 0.960 | 0.962 | 0.609 | 1.26x | 23.7/27.3% | 4.8% | 3 |
| 32 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 64 | 0.851 | - | - | 0.954 | 0.955 | 0.619 | 1.26x | 24.0/27.4% | 4.9% | 3 |

### `F-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.1 | 0.755 | - | - | 0.939 | 0.945 | 0.480 | 1.19x | 22.5/25.7% | 4.4% | 3 |
| 0.2 | 0.651 | - | - | 0.882 | 0.891 | 0.373 | 1.08x | 20.6/23.2% | 4.0% | 3 |
| 0.3 | 0.552 | - | - | 0.780 | 0.835 | 0.263 | 1.01x | 19.2/22.0% | 3.4% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 34

### `F-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.793 | - | - | 0.911 | 0.912 | 0.597 | 1.11x | 23.9/26.0% | 4.9% | 3 |
| all-routers | 0.892 | - | - | 0.976 | 0.976 | 0.800 | 2.62x | 39.8/43.3% | 5.0% | 3 |

### `F-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.711 | - | - | 0.918 | 0.919 | 0.309 | 0.97x | 18.7/21.7% | 4.1% | 3 |
| 7 | 0.913 | - | - | 0.975 | 0.975 | 0.746 | 1.42x | 25.8/28.8% | 5.1% | 3 |
| 15 | 0.930 | - | - | 0.977 | 0.978 | 0.785 | 1.40x | 25.5/28.3% | 5.0% | 3 |
| 32 | 0.929 | - | - | 0.970 | 0.971 | 0.791 | 1.43x | 26.1/28.9% | 5.1% | 3 |

### `F-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.1 | 0.820 | - | - | 0.949 | 0.949 | 0.562 | 1.32x | 24.6/27.6% | 4.7% | 3 |
| 0.2 | 0.773 | - | - | 0.928 | 0.932 | 0.425 | 1.31x | 24.5/27.4% | 4.4% | 3 |
| 0.3 | 0.719 | - | - | 0.904 | 0.912 | 0.346 | 1.36x | 25.0/28.0% | 4.3% | 3 |

> extra-loss=0.3: decode_failures 1

### `F-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.1 | 0.740 | - | - | 0.908 | 0.930 | 0.444 | 1.18x | 22.2/25.2% | 4.3% | 3 |
| 0.2 | 0.632 | - | - | 0.820 | 0.866 | 0.336 | 1.12x | 21.1/24.3% | 4.1% | 3 |
| 0.3 | 0.518 | - | - | 0.751 | 0.827 | 0.262 | 1.02x | 19.3/22.6% | 3.7% | 3 |

> burst-loss=0.1: decode_failures 35

> burst-loss=0.2: decode_failures 7

> burst-loss=0.3: decode_failures 41

### `F-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 22 | 0.285 | - | - | 0.340 | 0.738 | 0.055 | 1.32x | 15.9/19.5% | 4.4% | 3 |
| 17 | 0.161 | - | - | 0.302 | 0.304 | 0.000 | 0.95x | 10.9/14.7% | 3.9% | 3 |
| 14 | 0.104 | - | - | 0.235 | 0.250 | 0.000 | 0.68x | 7.1/9.0% | 2.8% | 3 |

> faster: 1.06 s per simulated hour against 2.33 over 3 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `G-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.854 | - | - | 0.983 | 0.986 | 0.596 | 1.27x | 24.3/27.8% | 5.0% | 3 |
| 6 | 0.859 | - | - | 0.983 | 0.984 | 0.612 | 1.29x | 24.8/28.3% | 5.1% | 6 |

### `G-hops` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.853 | - | - | 0.912 | 0.913 | 0.618 | 1.25x | 23.7/27.3% | 4.9% | 3 |
| 2 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 3 | 0.872 | - | - | 0.981 | 0.984 | 0.598 | 1.25x | 23.9/27.3% | 4.8% | 3 |
| 4 | 0.882 | - | - | 0.968 | 0.986 | 0.618 | 1.26x | 24.2/27.5% | 4.9% | 3 |

> hops-apart=4: decode_failures 19

### `G-place` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.877 | - | - | 0.915 | 0.981 | 0.595 | 1.26x | 24.1/27.6% | 4.8% | 3 |
| routers | 0.854 | - | - | 0.983 | 0.986 | 0.596 | 1.27x | 24.3/27.8% | 5.0% | 3 |
| alternate-routers | 0.864 | - | - | 0.988 | 0.989 | 0.605 | 1.26x | 24.0/27.5% | 4.9% | 3 |
| beside-router | 0.858 | - | - | 0.981 | 0.983 | 0.629 | 1.26x | 24.0/27.6% | 4.9% | 3 |
| random-clients | 0.873 | - | - | 0.977 | 0.980 | 0.607 | 1.29x | 24.7/28.3% | 5.1% | 3 |
| hops-apart | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

> place=spread: decode_failures 13

### `G-servers` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.851 | - | - | 0.950 | 0.951 | 0.613 | 1.25x | 23.7/27.1% | 4.8% | 2 |
| 3 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 5 | 0.857 | - | - | 0.987 | 0.990 | 0.621 | 1.30x | 24.7/28.1% | 4.9% | 5 |
| 8 | 0.862 | - | - | 0.988 | 0.990 | 0.595 | 1.34x | 25.0/28.6% | 5.1% | 8 |

### `J-bucketmode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 0.848 | - | - | 0.953 | 0.956 | 0.610 | 1.25x | 23.6/26.9% | 4.8% | 3 |
| local | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| time | 0.848 | - | - | 0.961 | 0.963 | 0.587 | 1.29x | 24.1/27.7% | 4.9% | 3 |
| window | 0.859 | - | - | 0.957 | 0.959 | 0.617 | 1.25x | 23.8/27.3% | 4.9% | 3 |

> bucket-mode=global: misdecodes 39

> bucket-mode=time: misdecodes 26

> bucket-mode=window: misdecodes 28

### `J-timewin` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 0.838 | - | - | 0.943 | 0.946 | 0.599 | 1.40x | 25.8/29.9% | 5.3% | 3 |
| 1800 | 0.848 | - | - | 0.961 | 0.963 | 0.587 | 1.29x | 24.1/27.7% | 4.9% | 3 |
| 3600 | 0.849 | - | - | 0.954 | 0.959 | 0.623 | 1.25x | 23.6/27.2% | 4.8% | 3 |

> time-bucket-s=600: misdecodes 124

> time-bucket-s=1800: misdecodes 26

> time-bucket-s=3600: misdecodes 6

### `J-wincap` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.855 | - | - | 0.937 | 0.960 | 0.619 | 1.25x | 23.7/27.3% | 4.9% | 3 |
| 16 | 0.854 | - | - | 0.957 | 0.957 | 0.621 | 1.24x | 23.5/27.1% | 4.8% | 3 |
| 32 | 0.859 | - | - | 0.957 | 0.959 | 0.617 | 1.25x | 23.8/27.3% | 4.9% | 3 |

> capacity=8: misdecodes 24

> capacity=8: decode_failures 44

> capacity=16: misdecodes 16

> capacity=16: decode_failures 2

> capacity=32: misdecodes 28

### `J-window` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.848 | - | - | 0.948 | 0.950 | 0.607 | 1.31x | 24.5/27.9% | 5.0% | 3 |
| 16 | 0.853 | - | - | 0.961 | 0.962 | 0.603 | 1.28x | 24.0/27.6% | 4.9% | 3 |
| 32 | 0.859 | - | - | 0.957 | 0.959 | 0.617 | 1.25x | 23.8/27.3% | 4.9% | 3 |

> window-size=8: misdecodes 92

> window-size=16: misdecodes 64

> window-size=32: misdecodes 28

### `K-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.767 | - | - | 0.910 | 0.930 | 0.524 | 1.32x | 23.4/26.9% | 6.2% | 3 |
| 60 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 90 | 0.939 | - | - | 0.991 | 0.991 | 0.732 | 1.60x | 31.0/33.2% | 4.8% | 3 |
| 120 | 0.968 | - | - | 1.000 | 1.000 | 0.601 | 2.11x | 43.9/47.3% | 5.2% | 3 |
| 150 | 0.969 | - | - | 0.999 | 0.999 | 0.910 | 2.54x | 41.0/47.4% | 5.6% | 3 |

### `K-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.711 | - | - | 0.918 | 0.919 | 0.309 | 0.97x | 18.7/21.7% | 4.1% | 3 |
| 5 | 0.860 | - | - | 0.961 | 0.963 | 0.603 | 1.31x | 24.2/27.4% | 4.9% | 3 |
| 7 | 0.913 | - | - | 0.975 | 0.975 | 0.746 | 1.42x | 25.8/28.8% | 5.1% | 3 |

### `K-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.882 | - | - | 0.985 | 0.991 | 0.615 | 1.37x | 31.2/33.4% | 7.5% | 3 |
| 60 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 90 | 0.800 | - | - | 0.938 | 0.940 | 0.468 | 1.60x | 21.9/26.8% | 4.6% | 3 |
| 120 | 0.740 | - | - | 0.954 | 0.956 | 0.287 | 2.20x | 29.0/35.1% | 5.0% | 3 |
| 150 | 0.719 | - | - | 0.932 | 0.934 | 0.399 | 2.79x | 27.0/32.5% | 4.9% | 3 |

### `K-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.711 | - | - | 0.918 | 0.919 | 0.309 | 0.97x | 18.7/21.7% | 4.1% | 3 |
| True | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

### `L-advert` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| dm | 0.856 | - | - | 0.960 | 0.962 | 0.630 | 1.23x | 23.3/26.6% | 4.7% | 3 |

### `L-provide` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| broadcast | 0.878 | - | - | 0.946 | 0.946 | 0.630 | 1.34x | 24.8/28.4% | 5.0% | 3 |

### `M-capacity` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.850 | - | - | 0.946 | 0.949 | 0.615 | 1.25x | 23.6/27.1% | 4.8% | 3 |
| 8 | 0.856 | - | - | 0.956 | 0.959 | 0.630 | 1.25x | 23.8/27.1% | 4.8% | 3 |
| 16 | 0.855 | - | - | 0.967 | 0.970 | 0.616 | 1.25x | 23.6/27.1% | 4.8% | 3 |
| 32 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 50 | 0.845 | - | - | 0.951 | 0.952 | 0.620 | 1.26x | 23.9/27.4% | 4.9% | 3 |

> capacity=4: decode_failures 92

> capacity=8: decode_failures 52

### `M-combined` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.878 | - | - | 0.946 | 0.946 | 0.630 | 1.34x | 24.8/28.4% | 5.0% | 3 |
| heard | 0.877 | - | - | 0.951 | 0.953 | 0.634 | 1.35x | 25.1/29.0% | 5.1% | 3 |

> replay-ordering=heard: misdecodes 10

### `M-jitter` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.854 | - | - | 0.958 | 0.960 | 0.615 | 1.27x | 23.9/27.7% | 4.9% | 3 |
| 30 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 120 | 0.853 | - | - | 0.954 | 0.955 | 0.603 | 1.26x | 23.7/27.4% | 4.9% | 3 |
| 600 | 0.852 | - | - | 0.952 | 0.952 | 0.613 | 1.27x | 24.0/27.6% | 4.9% | 3 |

### `M-replayorder` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| heard | 0.848 | - | - | 0.959 | 0.960 | 0.606 | 1.26x | 23.8/27.4% | 4.9% | 3 |

> replay-ordering=heard: misdecodes 21

### `N-hops` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.853 | - | - | 0.912 | 0.913 | 0.618 | 1.25x | 23.7/27.3% | 4.9% | 3 |
| 2 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 3 | 0.872 | - | - | 0.981 | 0.984 | 0.598 | 1.25x | 23.9/27.3% | 4.8% | 3 |
| 4 | 0.882 | - | - | 0.968 | 0.986 | 0.618 | 1.26x | 24.2/27.5% | 4.9% | 3 |
| 5 | 0.882 | - | - | 0.968 | 0.986 | 0.618 | 1.26x | 24.2/27.5% | 4.9% | 3 |

> hops-apart=4: decode_failures 19

> hops-apart=5: decode_failures 19

### `N-place` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.877 | - | - | 0.915 | 0.981 | 0.595 | 1.26x | 24.1/27.6% | 4.8% | 3 |
| routers | 0.854 | - | - | 0.983 | 0.986 | 0.596 | 1.27x | 24.3/27.8% | 5.0% | 3 |
| alternate-routers | 0.864 | - | - | 0.988 | 0.989 | 0.605 | 1.26x | 24.0/27.5% | 4.9% | 3 |
| beside-router | 0.858 | - | - | 0.981 | 0.983 | 0.629 | 1.26x | 24.0/27.6% | 4.9% | 3 |
| random-clients | 0.873 | - | - | 0.977 | 0.980 | 0.607 | 1.29x | 24.7/28.3% | 5.1% | 3 |
| hops-apart | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

> place=spread: decode_failures 13

### `N-servers` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.851 | - | - | 0.950 | 0.951 | 0.613 | 1.25x | 23.7/27.1% | 4.8% | 2 |
| 3 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 5 | 0.857 | - | - | 0.987 | 0.990 | 0.621 | 1.30x | 24.7/28.1% | 4.9% | 5 |
| 8 | 0.862 | - | - | 0.988 | 0.990 | 0.595 | 1.34x | 25.0/28.6% | 5.1% | 8 |

### `P-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 0.163 | - | - | 0.312 | 0.312 | 0.000 | 0.04x | 0.5/0.7% | 0.2% | 3 |
| MEDIUM_TURBO | 0.298 | - | - | 0.335 | 0.770 | 0.065 | 0.21x | 2.7/3.6% | 0.7% | 3 |
| LONG_TURBO | 0.773 | - | - | 0.967 | 0.971 | 0.465 | 1.21x | 17.7/19.0% | 4.6% | 3 |

> preset=MEDIUM_TURBO: decode_failures 1

### `P-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 0.821 | - | - | 0.936 | 0.938 | 0.572 | 1.74x | 31.0/36.2% | 6.9% | 3 |
| 02-06 | 0.854 | - | - | 0.924 | 0.967 | 0.629 | 1.31x | 24.6/28.3% | 5.0% | 3 |
| 00-08 | 0.849 | - | - | 0.919 | 0.952 | 0.622 | 1.34x | 24.9/28.7% | 5.2% | 3 |

> catch-up-hours=: misdecodes 22

> catch-up-hours=02-06: decode_failures 31

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 32

### `P-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.968 | - | - | 1.000 | 1.000 | 0.601 | 2.11x | 43.9/47.3% | 5.2% | 3 |
| True | 0.747 | - | - | 0.849 | 0.866 | 0.421 | 5.38x | 77.1/80.3% | 12.2% | 3 |

> no-congestion-scaling=True: queue drops 16.4% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 100

### `P-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 0.875 | - | - | 0.964 | 0.965 | 0.658 | 1.23x | 23.1/26.3% | 4.7% | 3 |
| sinusoid | 0.855 | - | - | 0.947 | 0.951 | 0.638 | 1.15x | 21.6/24.9% | 4.4% | 3 |
| commuter | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

### `P-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.226 | - | - | 0.312 | 0.313 | 0.000 | 0.11x | 1.4/1.8% | 0.4% | 3 |
| LONG_FAST | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| LITE_FAST | 0.805 | - | - | 0.949 | 0.950 | 0.485 | 0.92x | 15.0/17.8% | 3.8% | 3 |
| NARROW_SLOW | 0.801 | - | - | 0.922 | 0.922 | 0.573 | 1.21x | 21.0/24.1% | 4.5% | 3 |

### `P-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.226 | - | - | 0.312 | 0.313 | 0.000 | 0.11x | 1.4/1.8% | 0.4% | 3 |
| LONG_FAST | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| LONG_MODERATE | 0.833 | - | - | 0.980 | 0.983 | 0.582 | 3.04x | 58.2/63.4% | 12.0% | 3 |

> preset=LONG_MODERATE: decode_failures 9

### `Q-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.850 | - | - | 0 | 0.000 | 0.613 | 1.23x | 23.5/26.8% | 4.8% | 3 |
| sr | 0.872 | - | - | 0.981 | 0.984 | 0.598 | 1.25x | 23.9/27.3% | 4.8% | 3 |

### `Q-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| random | 0.852 | - | - | 0.948 | 0.950 | 0.645 | 1.31x | 24.4/27.4% | 4.9% | 3 |

### `Q-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 0.786 | - | - | 0.902 | 0.904 | 0.569 | 2.01x | 37.1/41.8% | 7.4% | 3 |
| 3600 | 0.877 | - | - | 0.963 | 0.963 | 0.652 | 0.87x | 16.3/18.7% | 3.3% | 3 |
| 10800 | 0.896 | - | - | 0.979 | 0.980 | 0.674 | 0.59x | 11.1/12.8% | 2.2% | 3 |
| 43200 | 0.901 | - | - | 0.982 | 0.982 | 0.692 | 0.45x | 8.3/9.6% | 1.7% | 3 |

### `Q-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.850 | - | - | 0 | 0.000 | 0.613 | 1.23x | 23.5/26.8% | 4.8% | 3 |
| chain | 0.833 | - | - | 0.904 | 0.955 | 0.593 | 1.47x | 27.2/31.3% | 5.5% | 3 |
| sr | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

### `Q-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| clustered | 0.866 | - | - | 0.959 | 0.960 | 0.153 | 1.11x | 31.4/33.5% | 5.4% | 3 |
| corridor | 0.610 | - | - | 0.893 | 0.894 | 0.188 | 1.25x | 21.0/23.0% | 5.3% | 3 |
| hub | 0.963 | - | - | 0.990 | 0.990 | 0.869 | 1.17x | 38.6/39.4% | 5.7% | 3 |

> topology=hub: misdecodes 1

### `R-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.968 | - | - | 1.000 | 1.000 | 0.601 | 2.11x | 43.9/47.3% | 5.2% | 3 |
| True | 0.961 | - | - | 0.999 | 0.999 | 0.617 | 2.44x | 48.9/52.6% | 5.7% | 3 |

### `R-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 0.521 | - | - | 0.698 | 0.701 | 0.115 | 4.45x | 27.3/32.9% | 4.9% | 3 |
| truesize | 0.554 | - | - | 0.742 | 0.747 | 0.115 | 3.27x | 20.4/25.6% | 3.7% | 3 |

> congestion-input=hotstore: decode_failures 18

> congestion-input=truesize: decode_failures 8

### `R-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 0.970 | - | - | 0.999 | 0.999 | 0.607 | 1.97x | 41.0/44.2% | 4.8% | 3 |
| adaptive | 0.968 | - | - | 1.000 | 1.000 | 0.601 | 2.11x | 43.9/47.3% | 5.2% | 3 |

### `R-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.807 | - | - | 0.930 | 0.933 | 0.556 | 1.58x | 29.4/33.6% | 5.9% | 3 |
| True | 0.800 | - | - | 0.928 | 0.931 | 0.590 | 1.58x | 29.4/33.6% | 5.9% | 3 |

### `R-dmmode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 0.786 | - | - | 0.922 | 0.922 | 0.567 | 1.73x | 31.6/36.2% | 6.4% | 3 |
| directed-with-late-flood | 0.807 | - | - | 0.930 | 0.933 | 0.556 | 1.58x | 29.4/33.6% | 5.9% | 3 |
| m4-early-flood | 0.812 | - | - | 0.928 | 0.929 | 0.551 | 1.58x | 29.4/33.5% | 5.9% | 3 |

### `R-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 0.800 | - | - | 0.928 | 0.931 | 0.590 | 1.58x | 29.4/33.6% | 5.9% | 3 |
| m4-early-flood | 0.813 | - | - | 0.935 | 0.940 | 0.575 | 1.59x | 29.3/33.6% | 5.9% | 3 |

### `R-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.850 | - | - | 0.956 | 0.958 | 0.692 | 1.34x | 27.7/30.7% | 4.8% | 3 |
| True | 0.867 | - | - | 0.951 | 0.952 | 0.733 | 1.38x | 28.1/31.1% | 4.7% | 3 |

### `R-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 0.842 | - | - | 0.935 | 0.979 | 0.440 | 0.73x | 11.1/12.4% | 2.0% | 3 |
| 2.8 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

> profile=legacy: decode_failures 37

> slower: 7.35 s per simulated hour against 1.93 over 3 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `R-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 120 | 0.740 | - | - | 0.954 | 0.956 | 0.287 | 2.20x | 29.0/35.1% | 5.0% | 3 |
| 250 | 0.518 | - | - | 0.676 | 0.691 | 0.107 | 4.74x | 29.2/35.2% | 5.2% | 3 |
| 500 | 0.310 | - | - | 0.497 | 0.498 | 0.049 | 10.28x | 32.5/59.4% | 6.5% | 3 |

> nodes=250: decode_failures 113

> nodes=500: decode_failures 101

### `R-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.745 | - | - | 0.889 | 0.889 | 0.621 | 2.83x | 55.7/61.8% | 9.1% | 3 |
| 100 | 0.876 | - | - | 0.958 | 0.961 | 0.699 | 1.50x | 31.9/36.1% | 4.9% | 3 |
| 120 | 0.876 | - | - | 0.958 | 0.961 | 0.699 | 1.50x | 31.9/36.1% | 4.9% | 3 |
| 250 | 0.876 | - | - | 0.958 | 0.961 | 0.699 | 1.50x | 31.9/36.1% | 4.9% | 3 |

### `R-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.320 | - | - | 0.419 | 0.465 | 0.072 | 11.58x | 59.9/69.4% | 11.1% | 3 |
| 120 | 0.521 | - | - | 0.698 | 0.701 | 0.115 | 4.45x | 27.3/32.9% | 4.9% | 3 |
| 250 | 0.524 | - | - | 0.696 | 0.711 | 0.106 | 4.30x | 26.0/32.7% | 4.8% | 3 |

> max-num-nodes=10: decode_failures 38

> max-num-nodes=120: decode_failures 18

> max-num-nodes=250: decode_failures 73

### `R-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.25 | 0.848 | - | - | 0.972 | 0.973 | 0.522 | 1.14x | 19.5/21.8% | 4.4% | 3 |
| 0.5 | 0.845 | - | - | 0.952 | 0.986 | 0.476 | 0.96x | 16.5/19.3% | 4.0% | 3 |
| 0.75 | 0.890 | - | - | 0.994 | 0.996 | 0.665 | 0.83x | 14.5/16.1% | 3.2% | 3 |

> legacy-fraction=0.5: decode_failures 3

### `R-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.25 | 0.845 | - | - | 0.967 | 0.972 | 0.527 | 1.12x | 19.4/21.8% | 4.4% | 3 |
| 0.5 | 0.846 | - | - | 0.941 | 0.986 | 0.503 | 0.94x | 16.4/19.0% | 3.9% | 3 |
| 0.75 | 0.886 | - | - | 0.992 | 0.995 | 0.671 | 0.79x | 14.2/15.7% | 3.1% | 3 |

> legacy-fraction=0.5: decode_failures 23

> slower: 3.62 s per simulated hour against 1.71 over 3 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `R-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 0.738 | - | - | 0.952 | 0.955 | 0.303 | 2.15x | 28.3/34.0% | 4.8% | 3 |
| 250 | 0.521 | - | - | 0.698 | 0.701 | 0.115 | 4.45x | 27.3/32.9% | 4.9% | 3 |
| 500 | 0.316 | - | - | 0.510 | 0.511 | 0.043 | 9.53x | 30.6/55.7% | 5.9% | 3 |

> nodes=250: decode_failures 18

> nodes=500: decode_failures 4

### `R-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.876 | - | - | 0.958 | 0.961 | 0.699 | 1.50x | 31.9/36.1% | 4.9% | 3 |
| baymesh-2026-08 | 0.876 | - | - | 0.958 | 0.961 | 0.699 | 1.50x | 31.9/36.1% | 4.9% | 3 |
| constrained | 0.761 | - | - | 0.895 | 0.900 | 0.627 | 2.84x | 55.9/62.0% | 9.1% | 3 |

> platform-mix=constrained: decode_failures 1

### `R-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| KNOWN_ONLY | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| CORE_PORTNUMS_ONLY | 0.861 | - | - | 0.930 | 0.965 | 0.625 | 1.20x | 22.8/26.2% | 4.7% | 3 |

### `R-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| True | 0.861 | - | - | 0.966 | 0.966 | 0.611 | 1.27x | 24.1/27.5% | 4.9% | 3 |

### `R-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.968 | - | - | 1.000 | 1.000 | 0.601 | 2.11x | 43.9/47.3% | 5.2% | 3 |
| True | 0.968 | - | - | 1.000 | 1.000 | 0.627 | 2.11x | 43.7/47.0% | 5.1% | 3 |

### `R-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.853 | - | - | 0.945 | 0.948 | 0.655 | 1.31x | 24.9/28.2% | 5.0% | 3 |
| baymesh-2026-08 | 0.793 | - | - | 0.911 | 0.912 | 0.597 | 1.11x | 23.9/26.0% | 4.9% | 3 |

### `R-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.853 | - | - | 0.941 | 0.942 | 0.678 | 1.33x | 25.1/28.4% | 5.0% | 3 |
| baymesh-2026-08 | 0.815 | - | - | 0.927 | 0.932 | 0.637 | 1.23x | 27.2/30.3% | 4.9% | 3 |

### `R-routerlate` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.05 | 0.860 | - | - | 0.968 | 0.971 | 0.687 | 1.35x | 28.2/32.1% | 4.6% | 3 |
| 0.1 | 0.853 | - | - | 0.956 | 0.957 | 0.692 | 1.47x | 32.0/36.1% | 4.8% | 3 |
| 0.2 | 0.865 | - | - | 0.952 | 0.955 | 0.705 | 1.65x | 33.0/38.1% | 4.6% | 3 |

### `R-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| BALANCED | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| STRICT | 0.729 | - | - | 0.850 | 0.852 | 0.496 | 1.36x | 25.5/29.4% | 5.1% | 3 |

> signature-policy=STRICT: decode_failures 2

### `R-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 0.892 | - | - | 0.976 | 0.976 | 0.643 | 0.67x | 13.1/15.2% | 2.7% | 3 |
| signing=true | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

### `R-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| local-typical | 0.621 | - | - | 0.763 | 0.770 | 0.000 | 1.43x | 22.0/28.0% | 4.8% | 3 |
| event | 0.255 | - | - | 0.461 | 0.461 | 0.000 | 1.52x | 26.1/33.2% | 6.1% | 3 |
| backbone | 0.980 | - | - | 0.999 | 1.000 | 0.873 | 0.99x | 34.1/36.7% | 5.5% | 3 |

### `R-srretries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.854 | - | - | 0.959 | 0.960 | 0.629 | 1.22x | 22.9/26.1% | 4.6% | 3 |
| 1 | 0.860 | - | - | 0.966 | 0.969 | 0.607 | 1.22x | 22.7/26.3% | 4.6% | 3 |
| 2 | 0.853 | - | - | 0.949 | 0.950 | 0.624 | 1.22x | 22.8/26.3% | 4.6% | 3 |
| 4 | 0.853 | - | - | 0.949 | 0.950 | 0.624 | 1.22x | 22.8/26.3% | 4.6% | 3 |

### `R-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.25 | 0.842 | - | - | 0.945 | 0.946 | 0.602 | 1.34x | 25.2/28.8% | 5.1% | 3 |
| 1.0 | 0.833 | - | - | 0.941 | 0.945 | 0.584 | 1.51x | 28.4/32.4% | 5.7% | 3 |
| 4.0 | 0.793 | - | - | 0.913 | 0.917 | 0.545 | 1.86x | 35.5/39.9% | 7.1% | 3 |

### `R-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.726 | - | - | 0.841 | 0.850 | 0.417 | 5.53x | 77.5/80.6% | 12.4% | 3 |
| 1.0 | 0.661 | - | - | 0.770 | 0.787 | 0.371 | 5.92x | 77.4/80.6% | 13.4% | 3 |

> traceroute-per-hour=0.0: queue drops 19.0% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 81

> traceroute-per-hour=1.0: queue drops 26.7% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 57

### `R-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 0.841 | - | - | 0.922 | 0.977 | 0.404 | 0.74x | 12.1/13.3% | 2.4% | 3 |
| 2.5 | 0.841 | - | - | 0.929 | 0.977 | 0.395 | 0.75x | 12.0/13.3% | 2.4% | 3 |
| 2.6 | 0.843 | - | - | 0.948 | 0.984 | 0.367 | 0.72x | 12.1/13.2% | 2.4% | 3 |
| 2.7 | 0.852 | - | - | 0.936 | 0.977 | 0.374 | 0.75x | 13.1/13.8% | 3.1% | 3 |
| 2.8 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |

> profile=2.4: decode_failures 46

> profile=2.5: decode_failures 44

> profile=2.6: decode_failures 40

> profile=2.7: decode_failures 39

> slower: 11.4 s per simulated hour against 1.92 over 3 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `R-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.726 | - | - | 0.841 | 0.850 | 0.417 | 5.53x | 77.5/80.6% | 12.4% | 3 |
| 25 | 0.726 | - | - | 0.841 | 0.850 | 0.417 | 5.53x | 77.5/80.6% | 12.4% | 3 |
| 100 | 0.726 | - | - | 0.841 | 0.850 | 0.417 | 5.53x | 77.5/80.6% | 12.4% | 3 |
| 2000 | 0.726 | - | - | 0.841 | 0.850 | 0.417 | 5.53x | 77.5/80.6% | 12.4% | 3 |

> warm-num-nodes=0: queue drops 19.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 81

> warm-num-nodes=25: queue drops 19.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 81

> warm-num-nodes=100: queue drops 19.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 81

> warm-num-nodes=2000: queue drops 19.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 81

### `X-amplifiers` - amplifier-mix  `--scenario ridge`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| sprinkled | 0.890 | - | - | 0.987 | 0.990 | 0.606 | 1.22x | 22.9/26.0% | 5.0% | 3 |
| arms-race | 0.953 | - | - | 0.992 | 0.993 | 0.785 | 1.01x | 24.9/28.8% | 5.5% | 3 |

### `X-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.1 | 0.869 | - | - | 0.937 | 0.939 | 0.739 | 1.07x | 22.2/24.3% | 4.6% | 3 |
| 0.3 | 0.960 | - | - | 0.995 | 0.995 | 0.821 | 0.91x | 26.9/29.9% | 4.9% | 3 |

### `X-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.793 | - | - | 0.911 | 0.912 | 0.597 | 1.11x | 23.9/26.0% | 4.9% | 3 |
| inverse | 0.709 | - | - | 0.871 | 0.878 | 0.308 | 1.06x | 17.2/19.4% | 3.8% | 3 |
| random | 0.781 | - | - | 0.931 | 0.942 | 0.568 | 1.05x | 18.7/24.0% | 4.6% | 3 |

> role-placement=inverse: decode_failures 3

> role-placement=random: decode_failures 2

### `X-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.877 | - | - | 0.963 | 0.963 | 0.652 | 0.87x | 16.3/18.7% | 3.3% | 3 |
| 900 | 0.786 | - | - | 0.902 | 0.904 | 0.569 | 2.01x | 37.1/41.8% | 7.4% | 3 |
| 300 | 0.517 | - | - | 0.724 | 0.732 | 0.332 | 4.19x | 68.2/73.2% | 13.9% | 3 |

> broadcast-interval-s=300: decode_failures 4

### `X-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.930 | - | - | 0.984 | 0.984 | 0.770 | 0.95x | 17.3/19.0% | 3.4% | 3 |
| 900 | 0.868 | - | - | 0.945 | 0.946 | 0.689 | 2.29x | 40.6/44.9% | 8.0% | 3 |
| 300 | 0.567 | - | - | 0.756 | 0.766 | 0.394 | 4.69x | 71.2/75.1% | 15.5% | 3 |

> broadcast-interval-s=300: decode_failures 3

### `X-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 0.25 | 0.867 | - | - | 0.955 | 0.956 | 0.678 | 1.18x | 26.0/28.8% | 5.0% | 3 |
| 1.0 | 0.930 | - | - | 0.979 | 0.979 | 0.810 | 0.85x | 26.6/28.1% | 4.7% | 3 |

### `X-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| temporal | 0.757 | - | - | 0.897 | 0.898 | 0.512 | 1.26x | 22.9/25.7% | 4.5% | 3 |
| transient | 0.848 | - | - | 0.956 | 0.957 | 0.616 | 1.25x | 23.4/26.9% | 4.8% | 3 |
| periodic | 0.679 | - | - | 0.792 | 0.799 | 0.401 | 1.15x | 21.9/24.6% | 4.2% | 3 |

### `X-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.793 | - | - | 0.911 | 0.912 | 0.597 | 1.11x | 23.9/26.0% | 4.9% | 3 |
| no-mute | 0.847 | - | - | 0.950 | 0.950 | 0.696 | 1.24x | 21.2/24.6% | 5.0% | 3 |
| all-routers | 0.892 | - | - | 0.976 | 0.976 | 0.800 | 2.62x | 39.8/43.3% | 5.0% | 3 |

### `X-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 0.793 | - | - | 0.903 | 0.905 | 0.548 | 1.23x | 23.4/26.6% | 4.6% | 3 |
| 10000 | 0.679 | - | - | 0.792 | 0.799 | 0.401 | 1.15x | 21.9/24.6% | 4.2% | 3 |
| 4000 | 0.425 | - | - | 0.493 | 0.556 | 0.173 | 1.00x | 18.7/20.9% | 3.2% | 3 |
| 2000 | 0.107 | - | - | 0.129 | 0.195 | 0.040 | 0.72x | 13.7/15.4% | 2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 3

### `X-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.793 | - | - | 0.911 | 0.912 | 0.597 | 1.11x | 23.9/26.0% | 4.9% | 3 |
| local-typical | 0.562 | - | - | 0.752 | 0.753 | 0.000 | 1.24x | 22.1/29.7% | 5.1% | 3 |
| basement-heavy | 0.089 | - | - | 0.316 | 0.317 | 0.000 | 0.62x | 8.4/13.3% | 3.4% | 3 |

### `X-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 0.861 | - | - | 0.961 | 0.963 | 0.630 | 1.26x | 23.8/27.3% | 4.8% | 3 |
| 1.25 | 0.585 | - | - | 0.773 | 0.814 | 0.325 | 1.24x | 17.5/18.4% | 4.3% | 3 |
| 1.5 | 0.276 | - | - | 0.339 | 0.738 | 0.000 | 1.29x | 15.9/19.5% | 4.6% | 3 |
| 2.0 | 0.129 | - | - | 0.290 | 0.302 | 0.000 | 0.80x | 9.8/12.6% | 3.6% | 3 |

> stretch=1.25: decode_failures 13

> stretch=1.5: decode_failures 1

### `X-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.276 | - | - | 0.339 | 0.738 | 0.000 | 1.29x | 15.9/19.5% | 4.6% | 3 |
| 1.0 | 0.733 | - | - | 0.835 | 0.887 | 0.479 | 0.83x | 20.4/22.1% | 4.5% | 3 |

> duct-per-hour=0.0: decode_failures 1

> duct-per-hour=1.0: decode_failures 30

### `X-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.768 | - | - | 0.838 | 0.898 | 0.000 | 2.25x | 27.0/37.3% | 5.3% | 3 |
| inverse | 0.743 | - | - | 0.846 | 0.905 | 0.000 | 2.24x | 23.9/31.2% | 3.3% | 3 |

> role-placement=degree: decode_failures 60

> role-placement=inverse: decode_failures 43

> slower: 18.1 s per simulated hour against 3.33 over 3 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

