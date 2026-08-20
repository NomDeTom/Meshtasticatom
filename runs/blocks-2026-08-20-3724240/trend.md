# Sweep blocks-2026-08-20-3724240

- **transport** `adb0188`
- **ground** ridge
- **seed base** 3724240 · seeds 3724240
- **blocks** 87 run
- **compute** 12.3 h of simulator time across every cell
- **generated** 2026-08-20T04:38:32+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>110 warnings</summary>

- D-cadence: trigger=interval: misdecodes 18
- D-cadence: trigger=aimd: misdecodes 2
- D-cadence: trigger=aimd: decode_failures 2
- D-cadence: trigger=bucket+interval: misdecodes 14
- E-capacity: capacity=4: decode_failures 85
- E-capacity: capacity=8: decode_failures 45
- E-capacity: capacity=16: decode_failures 5
- F-burst: burst-loss=0.2: decode_failures 8
- F-burst: burst-loss=0.3: decode_failures 20
- F-loss: extra-loss=0.1: decode_failures 1
- F-outage: burst-loss=0.1: decode_failures 28
- F-outage: burst-loss=0.2: decode_failures 32
- F-outage: burst-loss=0.3: decode_failures 22
- F-preset-turbo: preset=LONG_TURBO: decode_failures 1
- F-txpower: tx-power=22: decode_failures 9
- F-txpower: tx-power=17: decode_failures 2
- G-allrouters: servers=3: decode_failures 2
- G-allrouters: servers=6: misdecodes 1
- G-allrouters: servers=6: decode_failures 2
- G-hops: hops-apart=3: decode_failures 32
- G-hops: hops-apart=4: decode_failures 32
- G-place: place=spread: decode_failures 23
- G-place: place=routers: decode_failures 2
- G-place: place=beside-router: decode_failures 25
- G-place: place=random-clients: decode_failures 1
- J-bucketmode: bucket-mode=global: misdecodes 41
- J-bucketmode: bucket-mode=time: misdecodes 26
- J-bucketmode: bucket-mode=window: misdecodes 7
- J-timewin: time-bucket-s=600: misdecodes 124
- J-timewin: time-bucket-s=1800: misdecodes 26
- J-timewin: time-bucket-s=3600: misdecodes 7
- J-wincap: capacity=8: misdecodes 14
- J-wincap: capacity=8: decode_failures 37
- J-wincap: capacity=16: misdecodes 24
- J-wincap: capacity=16: decode_failures 2
- J-wincap: capacity=32: misdecodes 7
- J-window: window-size=8: misdecodes 143
- J-window: window-size=16: misdecodes 59
- J-window: window-size=32: misdecodes 7
- K-density: nodes=120: decode_failures 75
- K-density: nodes=150: decode_failures 64
- K-size: nodes=120: decode_failures 15
- M-capacity: capacity=4: decode_failures 85
- M-capacity: capacity=8: decode_failures 45
- M-capacity: capacity=16: decode_failures 5
- M-combined: replay-ordering=heard: misdecodes 5
- M-replayorder: replay-ordering=heard: misdecodes 11
- N-hops: hops-apart=3: decode_failures 32
- N-hops: hops-apart=4: decode_failures 32
- N-hops: hops-apart=5: decode_failures 24
- N-place: place=spread: decode_failures 23
- N-place: place=routers: decode_failures 2
- N-place: place=beside-router: decode_failures 25
- N-place: place=random-clients: decode_failures 1
- P-bw500: preset=LONG_TURBO: decode_failures 1
- P-catchup: catch-up-hours=: misdecodes 14
- P-catchup: catch-up-hours=02-06: decode_failures 26
- P-catchup: catch-up-hours=00-08: decode_failures 22
- P-congestion: no-congestion-scaling=False: decode_failures 75
- P-congestion: no-congestion-scaling=True: queue drops 31.3% of transmissions - airtime here is measured through a cap
- P-congestion: no-congestion-scaling=True: decode_failures 45
- P-eu-presets: preset=LITE_FAST: decode_failures 1
- P-eu-presets: preset=NARROW_SLOW: decode_failures 1
- P-preset: preset=LONG_MODERATE: queue drops 11.2% of transmissions - airtime here is measured through a cap
- P-preset: preset=LONG_MODERATE: decode_failures 5
- Q-control: protocol=sr: decode_failures 32
- R-adopt: no-adopt-hop-recommendation=False: decode_failures 75
- R-adopt: no-adopt-hop-recommendation=True: decode_failures 61
- R-congestion-input: congestion-input=hotstore: decode_failures 14
- R-congestion-input: congestion-input=truesize: decode_failures 21
- R-congestion-mode: congestion-mode=static: decode_failures 9
- R-congestion-mode: congestion-mode=adaptive: decode_failures 75
- R-hopscale: nodes=120: decode_failures 15
- R-hopscale: nodes=250: decode_failures 32
- R-hopscale: nodes=500: decode_failures 172
- R-hotstore-stress: max-num-nodes=10: decode_failures 52
- R-hotstore-stress: max-num-nodes=120: decode_failures 14
- R-hotstore-stress: max-num-nodes=250: decode_failures 17
- R-oversubscribed: nodes=120: decode_failures 2
- R-oversubscribed: nodes=250: decode_failures 14
- R-oversubscribed: nodes=500: decode_failures 82
- R-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 3
- R-repeats-busy: extra-repeats=False: decode_failures 75
- R-repeats-busy: extra-repeats=True: decode_failures 82
- R-siting: siting-mix=local-typical: decode_failures 18
- R-siting: siting-mix=backbone: misdecodes 1
- R-traceroute-small: traceroute-per-hour=0.0: queue drops 33.3% of transmissions - airtime here is measured through a cap
- R-traceroute-small: traceroute-per-hour=0.0: decode_failures 44
- R-traceroute-small: traceroute-per-hour=1.0: queue drops 38.7% of transmissions - airtime here is measured through a cap
- R-traceroute-small: traceroute-per-hour=1.0: decode_failures 48
- R-warm: warm-num-nodes=0: queue drops 33.3% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=0: decode_failures 44
- R-warm: warm-num-nodes=25: queue drops 33.3% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=25: decode_failures 44
- R-warm: warm-num-nodes=100: queue drops 33.3% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=100: decode_failures 44
- R-warm: warm-num-nodes=2000: queue drops 33.3% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=2000: decode_failures 44
- X-amplify-worst: amplify-worst=0.3: misdecodes 1
- X-chatty-hops: broadcast-interval-s=300: queue drops 18.4% of transmissions - airtime here is measured through a cap
- X-chatty-hops: broadcast-interval-s=300: decode_failures 23
- X-chatty: broadcast-interval-s=300: queue drops 23.9% of transmissions - airtime here is measured through a cap
- X-chatty: broadcast-interval-s=300: decode_failures 14
- X-pulse: noise-pulse-interval-ms=30000: decode_failures 5
- X-siting: siting-mix=local-typical: decode_failures 4
- X-stretch-duct: duct-per-hour=0.0: decode_failures 3
- X-stretch: stretch=1.5: decode_failures 3
- X-stretch: stretch=2.0: decode_failures 7
- X-worst: role-placement=degree: decode_failures 49
- X-worst: role-placement=inverse: decode_failures 38

</details>

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.2) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `F-preset-turbo` | preset | **held** | 0.000 → 0.880 | 0.880 | 0.018 → 0.696 | 4.7x bytes_on_air | up | 5 |
| `Q-protocol` | protocol | **held** | 0 → 0.880 | 0.880 | 0.670 → 0.696 | 1.1x bytes_on_air | up | 3 |
| `R-siting` | siting-mix | **held** | 0.140 → 0.986 | 0.846 | 0.127 → 0.949 | 30x sr_bytes | up | 4 |
| `F-txpower` | tx-power | **held** | 0.040 → 0.880 | 0.840 | 0.027 → 0.696 | 90x sr_bytes | down | 4 |
| `Q-control` | protocol | **held** | 0 → 0.791 | 0.791 | 0.687 → 0.699 | 1.1x bytes_on_air | up | 2 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.001 → 0.779 | 0.778 | 0.002 → 0.612 | 5.3x bytes_on_air | down | 4 |
| `X-stretch` | stretch | **held** | 0.118 → 0.880 | 0.762 | 0.070 → 0.696 | 8x advert_bytes | down | 4 |
| `X-siting` | siting-mix | **held** | 0.220 → 0.859 | 0.639 | 0.035 → 0.649 | 4.1x sr_bytes | down | 3 |
| `R-hopscale` | nodes | **held** | 0.290 → 0.880 | 0.590 | 0.175 → 0.696 | 8.5x sr_bytes | down | 4 |
| `P-bw500` | preset | **held** | 0.210 → 0.796 | 0.586 | 0.122 → 0.598 | 10x sr_bytes | up | 3 |
| `X-chatty` | broadcast-interval-s | **held** | 0.416 → 0.926 | 0.510 | 0.295 → 0.745 | 25x sr_airtime | down | 3 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.332 → 0.832 | 0.500 | 0.332 → 0.832 | 18x sr_airtime | down | 3 |
| `P-eu-presets` | preset | **text** | 0.238 → 0.724 | 0.486 | 0.238 → 0.724 | 2.5x sr_bytes | up | 4 |
| `P-preset` | preset | **text** | 0.238 → 0.696 | 0.458 | 0.238 → 0.696 | 2.4x sr_airtime | up | 3 |
| `Q-topology` | topology | **text** | 0.489 → 0.919 | 0.431 | 0.489 → 0.919 | 2.2x sr_bytes | up | 4 |
| `X-stretch-duct` | duct-per-hour | **text** | 0.213 → 0.619 | 0.406 | 0.213 → 0.619 | 2.5x sr_airtime | up | 2 |
| `P-congestion` | no-congestion-scaling | **held** | 0.550 → 0.941 | 0.391 | 0.451 → 0.836 | 6.6x sr_airtime | down | 2 |
| `R-oversubscribed` | nodes | **held** | 0.293 → 0.660 | 0.367 | 0.175 → 0.467 | 4x bytes_on_air | down | 3 |
| `F-hoplimit` | hop-limit | **text** | 0.491 → 0.845 | 0.353 | 0.491 → 0.845 | 2.9x sr_bytes | up | 4 |
| `K-density` | nodes | **held** | 0.647 → 0.978 | 0.331 | 0.547 → 0.846 | 6x advert_bytes | up | 5 |
| `F-outage` | burst-loss | **text** | 0.367 → 0.696 | 0.329 | 0.367 → 0.696 | 1.9x sr_bytes | down | 4 |
| `K-hopspread` | hop-limit | **text** | 0.491 → 0.785 | 0.294 | 0.491 → 0.785 | 2.2x sr_bytes | up | 3 |
| `F-burst` | burst-loss | **text** | 0.417 → 0.696 | 0.279 | 0.417 → 0.696 | 1.8x sr_bytes | down | 4 |
| `K-size` | nodes | **text** | 0.420 → 0.696 | 0.276 | 0.420 → 0.696 | 4.3x sr_bytes | down | 5 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.307 → 0.567 | 0.260 | 0.186 → 0.300 | 5.5x sr_airtime | up | 3 |
| `X-noise` | noise-profile | **held** | 0.624 → 0.880 | 0.256 | 0.466 → 0.696 | 1.6x sr_airtime | down | 4 |
| `K-spread` | hop-spread | **text** | 0.491 → 0.696 | 0.205 | 0.491 → 0.696 | 1.7x sr_bytes | up | 2 |
| `N-hops` | hops-apart | **held** | 0.686 → 0.880 | 0.193 | 0.682 → 0.707 | 2.6x sr_bytes | down | 5 |
| `X-amplify-worst` | amplify-worst | **text** | 0.696 → 0.888 | 0.192 | 0.696 → 0.888 | 1.4x sr_airtime | up | 3 |
| `X-amplifiers` | amplifier-mix | **text** | 0.696 → 0.885 | 0.189 | 0.696 → 0.885 | 1.5x sr_bytes | up | 3 |
| `G-place` | place | **held** | 0.700 → 0.880 | 0.180 | 0.688 → 0.700 | 2.1x sr_bytes | up | 6 |
| `N-place` | place | **held** | 0.700 → 0.880 | 0.180 | 0.688 → 0.700 | 2.1x sr_bytes | up | 6 |
| `G-allrouters` | servers | **held** | 0.767 → 0.944 | 0.177 | 0.696 → 0.751 | 4.9x sr_bytes | up | 2 |
| `G-hops` | hops-apart | **held** | 0.703 → 0.880 | 0.177 | 0.682 → 0.707 | 2.6x sr_bytes | down | 4 |
| `X-duct` | duct-per-hour | **text** | 0.696 → 0.862 | 0.166 | 0.696 → 0.862 | 1.5x bytes_on_air | up | 3 |
| `Q-interval` | broadcast-interval-s | **text** | 0.625 → 0.787 | 0.163 | 0.625 → 0.787 | 6x sr_airtime | up | 4 |
| `F-loss` | extra-loss | **text** | 0.538 → 0.696 | 0.158 | 0.538 → 0.696 | 1.3x sr_bytes | down | 4 |
| `R-hotstore` | max-num-nodes | **text** | 0.622 → 0.752 | 0.130 | 0.622 → 0.752 | 2.1x sr_airtime | up | 4 |
| `R-platform` | platform-mix | **text** | 0.622 → 0.752 | 0.130 | 0.622 → 0.752 | 2.1x sr_airtime | down | 3 |
| `R-mixed` | legacy-fraction | **text** | 0.684 → 0.777 | 0.093 | 0.684 → 0.777 | 1.9x bytes_on_air | up | 4 |
| `R-signing` | signature-policy | **text** | 0.605 → 0.696 | 0.091 | 0.605 → 0.696 | 1.2x sr_airtime | down | 3 |
| `F-flooding` | role-mix | **text** | 0.649 → 0.739 | 0.089 | 0.649 → 0.739 | 2.4x bytes_on_air | up | 2 |
| `X-nomute` | role-mix | **text** | 0.649 → 0.739 | 0.089 | 0.649 → 0.739 | 2.4x bytes_on_air | up | 3 |
| `R-mixed-26` | legacy-fraction | **text** | 0.684 → 0.770 | 0.086 | 0.684 → 0.770 | 1.9x bytes_on_air | up | 4 |
| `R-firmware` | profile | **text** | 0.696 → 0.778 | 0.082 | 0.696 → 0.778 | 3.2x bytes_on_air | down | 2 |
| `R-versions` | profile | **text** | 0.696 → 0.777 | 0.081 | 0.696 → 0.777 | 3.3x bytes_on_air | down | 5 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.811 → 0.880 | 0.069 | 0.695 → 0.696 | 13x sr_airtime | down | 3 |
| `R-signing-cost` | profile-flag | **text** | 0.696 → 0.764 | 0.068 | 0.696 → 0.764 | 3.3x bytes_on_air | down | 2 |
| `R-congestion-input` | congestion-input | **held** | 0.566 → 0.632 | 0.065 | 0.298 → 0.335 | 2.2x sr_airtime | up | 2 |
| `D-cadence` | trigger | **held** | 0.819 → 0.880 | 0.061 | 0.651 → 0.696 | 14x advert_bytes | down | 4 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.640 → 0.696 | 0.056 | 0.640 → 0.696 | 1.4x sr_airtime | down | 4 |
| `R-favourites` | favourite-routers | **text** | 0.695 → 0.750 | 0.056 | 0.695 → 0.750 | 1.1x sr_bytes | up | 2 |
| `R-roles-fav` | role-mix | **held** | 0.839 → 0.894 | 0.055 | 0.699 → 0.714 | 1.3x sr_bytes | down | 2 |
| `G-servers` | servers | **held** | 0.854 → 0.909 | 0.055 | 0.691 → 0.712 | 9.8x sr_bytes | up | 4 |
| `N-servers` | servers | **held** | 0.854 → 0.909 | 0.055 | 0.691 → 0.712 | 9.8x sr_bytes | up | 4 |
| `Q-hopassign` | hop-assign | **text** | 0.652 → 0.696 | 0.044 | 0.652 → 0.696 | 1.6x sr_airtime | down | 2 |
| `R-traceroute-small` | traceroute-per-hour | **held** | 0.489 → 0.532 | 0.042 | 0.401 → 0.436 | 1.1x sr_bytes | down | 2 |
| `R-roles` | role-mix | **held** | 0.859 → 0.894 | 0.035 | 0.649 → 0.682 | 1.1x sr_bytes | down | 2 |
| `P-catchup` | catch-up-hours | **text** | 0.655 → 0.689 | 0.034 | 0.655 → 0.689 | 9.2x advert_bytes | up | 3 |
| `R-congestion-mode` | congestion-mode | **held** | 0.941 → 0.975 | 0.033 | 0.836 → 0.849 | 1.2x sr_airtime | down | 2 |
| `E-capacity` | capacity | **held** | 0.848 → 0.880 | 0.032 | 0.680 → 0.701 | 5.4x advert_bytes | up | 5 |
| `M-capacity` | capacity | **held** | 0.848 → 0.880 | 0.032 | 0.680 → 0.701 | 5.4x advert_bytes | up | 5 |
| `L-provide` | provide-transport | **text** | 0.696 → 0.726 | 0.030 | 0.696 → 0.726 | 3.1x sr_airtime | up | 2 |
| `P-diurnal` | diurnal | **text** | 0.696 → 0.726 | 0.030 | 0.696 → 0.726 | 1.2x advert_bytes | down | 3 |
| `J-timewin` | time-bucket-s | **held** | 0.850 → 0.879 | 0.029 | 0.675 → 0.696 | 5.1x advert_bytes | up | 3 |
| `R-srretries` | sr-retries | **held** | 0.855 → 0.883 | 0.028 | 0.688 → 0.701 | 1.2x sr_bytes | down | 4 |
| `R-dmmode-cr` | dm-mode | **held** | 0.840 → 0.863 | 0.023 | 0.653 → 0.655 | 1.2x sr_airtime | up | 2 |
| `X-badrouters` | role-placement | **held** | 0.849 → 0.871 | 0.022 | 0.629 → 0.649 | 1.3x sr_bytes | down | 3 |
| `D-jitter` | advert-jitter-s | **held** | 0.869 → 0.889 | 0.020 | 0.691 → 0.703 | 1.1x sr_bytes | down | 4 |
| `M-jitter` | advert-jitter-s | **held** | 0.869 → 0.889 | 0.020 | 0.691 → 0.703 | 1.1x sr_bytes | down | 4 |
| `R-routerlate` | router-late-fraction | **held** | 0.861 → 0.880 | 0.019 | 0.695 → 0.706 | 1.3x bytes_on_air | down | 4 |
| `R-dmmode` | dm-mode | **held** | 0.834 → 0.852 | 0.018 | 0.641 → 0.655 | 1.2x sr_airtime | up | 3 |
| `X-worst` | role-placement | **held** | 0.867 → 0.881 | 0.014 | 0.709 → 0.723 | 1.1x sr_airtime | up | 2 |
| `R-adopt` | no-adopt-hop-recommendation | **held** | 0.927 → 0.941 | 0.014 | 0.823 → 0.836 | 1.1x sr_airtime | down | 2 |
| `J-wincap` | capacity | **held** | 0.862 → 0.873 | 0.011 | 0.690 → 0.696 | 1.8x advert_bytes | up | 3 |
| `R-crladder` | coding-rate-ladder | **text** | 0.645 → 0.653 | 0.008 | 0.645 → 0.653 | 1.1x sr_bytes | up | 2 |
| `D-resolve` | resolve | **held** | 0.872 → 0.880 | 0.008 | 0.690 → 0.696 | 5.7x advert_bytes | = | 3 |
| `E-width` | short-id-bits | **held** | 0.873 → 0.880 | 0.007 | 0.690 → 0.696 | 3.1x advert_bytes | up | 4 |
| `J-bucketmode` | bucket-mode | **held** | 0.873 → 0.880 | 0.007 | 0.690 → 0.696 | 3.9x advert_bytes | down | 4 |
| `R-repeats` | extra-repeats | **held** | 0.873 → 0.880 | 0.007 | 0.693 → 0.696 | 1x sr_airtime | down | 2 |
| `R-repeats-busy` | extra-repeats | **text** | 0.829 → 0.836 | 0.006 | 0.829 → 0.836 | 1.1x sr_bytes | down | 2 |
| `J-window` | window-size | **text** | 0.690 → 0.696 | 0.006 | 0.690 → 0.696 | 6.6x advert_bytes | up | 3 |
| `L-advert` | advert-transport | **text** | 0.696 → 0.700 | 0.004 | 0.696 → 0.700 | 2x advert_bytes | up | 2 |
| `M-replayorder` | replay-ordering | **held** | 0.877 → 0.880 | 0.003 | 0.696 → 0.699 | 1.1x sr_bytes | down | 2 |
| `M-combined` | replay-ordering | **held** | 0.871 → 0.874 | 0.003 | 0.724 → 0.726 | 1x sr_airtime | up | 2 |

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
| bucket | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| interval | 0.651 | - | - | 0.819 | 0.825 | 0.364 | 2.32x | 46.1/54.8% | 12.1% | 3 |
| aimd | 0.690 | - | - | 0.829 | 0.884 | 0.344 | 1.79x | 32.3/38.4% | 8.2% | 3 |
| bucket+interval | 0.655 | - | - | 0.834 | 0.835 | 0.348 | 2.33x | 46.0/54.4% | 11.8% | 3 |

> trigger=interval: misdecodes 18

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 2

> trigger=bucket+interval: misdecodes 14

### `D-jitter` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.703 | - | - | 0.889 | 0.889 | 0.347 | 1.75x | 31.9/37.8% | 8.1% | 3 |
| 30 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 120 | 0.691 | - | - | 0.870 | 0.872 | 0.350 | 1.75x | 31.5/37.5% | 8.0% | 3 |
| 600 | 0.695 | - | - | 0.869 | 0.869 | 0.364 | 1.77x | 31.8/37.7% | 8.1% | 3 |

### `D-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| enum | 0.690 | - | - | 0.872 | 0.876 | 0.358 | 1.78x | 32.6/38.6% | 8.0% | 3 |
| hybrid | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `E-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.680 | - | - | 0.848 | 0.854 | 0.341 | 1.76x | 32.4/38.2% | 8.0% | 3 |
| 8 | 0.701 | - | - | 0.877 | 0.879 | 0.367 | 1.76x | 31.9/37.9% | 8.1% | 3 |
| 16 | 0.699 | - | - | 0.879 | 0.880 | 0.364 | 1.75x | 31.7/37.7% | 8.1% | 3 |
| 32 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 50 | 0.697 | - | - | 0.877 | 0.878 | 0.348 | 1.77x | 32.0/37.9% | 8.1% | 3 |

> capacity=4: decode_failures 85

> capacity=8: decode_failures 45

> capacity=16: decode_failures 5

### `E-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| True | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `E-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 0.694 | - | - | 0.873 | 0.877 | 0.353 | 1.77x | 32.1/38.2% | 8.2% | 3 |
| 24 | 0.690 | - | - | 0.875 | 0.877 | 0.355 | 1.75x | 31.7/37.7% | 8.1% | 3 |
| 32 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 64 | 0.690 | - | - | 0.873 | 0.874 | 0.356 | 1.78x | 32.0/38.0% | 8.2% | 3 |

### `F-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.1 | 0.601 | - | - | 0.832 | 0.835 | 0.272 | 1.66x | 30.3/36.1% | 7.4% | 3 |
| 0.2 | 0.515 | - | - | 0.784 | 0.798 | 0.206 | 1.58x | 29.1/34.9% | 6.5% | 3 |
| 0.3 | 0.417 | - | - | 0.675 | 0.721 | 0.155 | 1.47x | 27.3/32.7% | 5.7% | 3 |

> burst-loss=0.2: decode_failures 8

> burst-loss=0.3: decode_failures 20

### `F-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.649 | - | - | 0.859 | 0.860 | 0.256 | 1.64x | 30.8/37.4% | 7.4% | 3 |
| all-routers | 0.739 | - | - | 0.918 | 0.918 | 0.451 | 3.93x | 59.1/65.1% | 8.5% | 3 |

### `F-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.491 | - | - | 0.791 | 0.792 | 0.149 | 1.53x | 28.4/34.8% | 7.4% | 3 |
| 7 | 0.785 | - | - | 0.873 | 0.873 | 0.567 | 1.91x | 31.9/37.7% | 7.9% | 3 |
| 15 | 0.829 | - | - | 0.872 | 0.873 | 0.673 | 2.02x | 32.8/38.5% | 8.1% | 3 |
| 32 | 0.845 | - | - | 0.887 | 0.888 | 0.697 | 2.00x | 32.3/37.9% | 7.9% | 3 |

### `F-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.1 | 0.641 | - | - | 0.834 | 0.835 | 0.298 | 1.86x | 33.3/39.1% | 7.8% | 3 |
| 0.2 | 0.601 | - | - | 0.803 | 0.809 | 0.229 | 1.94x | 34.3/40.2% | 7.5% | 3 |
| 0.3 | 0.538 | - | - | 0.762 | 0.772 | 0.175 | 2.00x | 35.5/41.4% | 7.1% | 3 |

> extra-loss=0.1: decode_failures 1

### `F-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.1 | 0.589 | - | - | 0.805 | 0.835 | 0.290 | 1.66x | 30.6/36.6% | 7.6% | 3 |
| 0.2 | 0.492 | - | - | 0.705 | 0.769 | 0.196 | 1.59x | 29.8/35.0% | 7.2% | 3 |
| 0.3 | 0.367 | - | - | 0.554 | 0.678 | 0.148 | 1.47x | 26.6/31.7% | 5.7% | 3 |

> burst-loss=0.1: decode_failures 28

> burst-loss=0.2: decode_failures 32

> burst-loss=0.3: decode_failures 22

### `F-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 0.018 | - | - | 0.000 | 0.000 | 0.000 | 0.01x | 0.1/0.1% | 0.0% | 3 |
| SHORT_TURBO | 0.122 | - | - | 0.210 | 0.212 | 0.000 | 0.06x | 0.6/0.8% | 0.2% | 3 |
| LONG_FAST | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| LONG_TURBO | 0.598 | - | - | 0.796 | 0.817 | 0.217 | 1.54x | 21.8/26.3% | 6.4% | 3 |
| EXTRA_LONG_TURBO | 0.634 | - | - | 0.828 | 0.831 | 0.374 | 2.26x | 38.7/45.6% | 9.5% | 3 |

> preset=LONG_TURBO: decode_failures 1

### `F-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 22 | 0.249 | - | - | 0.388 | 0.442 | 0.000 | 1.93x | 18.8/21.6% | 6.6% | 3 |
| 17 | 0.081 | - | - | 0.147 | 0.181 | 0.000 | 1.05x | 10.6/13.8% | 4.0% | 3 |
| 14 | 0.027 | - | - | 0.040 | 0.106 | 0.000 | 0.57x | 4.4/8.7% | 2.7% | 3 |

> tx-power=22: decode_failures 9

> tx-power=17: decode_failures 2

### `G-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.696 | - | - | 0.767 | 0.934 | 0.363 | 1.75x | 31.0/37.1% | 8.0% | 3 |
| 6 | 0.751 | - | - | 0.944 | 0.953 | 0.343 | 1.85x | 33.5/39.6% | 8.9% | 6 |

> servers=3: decode_failures 2

> servers=6: misdecodes 1

> servers=6: decode_failures 2

### `G-hops` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.682 | - | - | 0.820 | 0.823 | 0.355 | 1.73x | 31.0/36.8% | 8.0% | 3 |
| 2 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 3 | 0.699 | - | - | 0.791 | 0.939 | 0.354 | 1.80x | 32.3/38.4% | 8.1% | 3 |
| 4 | 0.707 | - | - | 0.703 | 0.943 | 0.375 | 1.78x | 31.7/37.5% | 8.3% | 3 |

> hops-apart=3: decode_failures 32

> hops-apart=4: decode_failures 32

### `G-place` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.700 | - | - | 0.700 | 0.965 | 0.355 | 1.80x | 31.5/37.5% | 8.1% | 3 |
| routers | 0.696 | - | - | 0.767 | 0.934 | 0.363 | 1.75x | 31.0/37.1% | 8.0% | 3 |
| alternate-routers | 0.692 | - | - | 0.865 | 0.867 | 0.346 | 1.77x | 32.0/38.0% | 8.4% | 3 |
| beside-router | 0.688 | - | - | 0.795 | 0.930 | 0.313 | 1.76x | 31.5/37.7% | 8.0% | 3 |
| random-clients | 0.699 | - | - | 0.769 | 0.772 | 0.336 | 1.75x | 30.9/37.0% | 8.0% | 3 |
| hops-apart | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

> place=spread: decode_failures 23

> place=routers: decode_failures 2

> place=beside-router: decode_failures 25

> place=random-clients: decode_failures 1

### `G-servers` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.691 | - | - | 0.854 | 0.856 | 0.363 | 1.76x | 31.4/37.5% | 8.2% | 2 |
| 3 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 5 | 0.712 | - | - | 0.883 | 0.887 | 0.367 | 1.81x | 32.8/38.7% | 8.2% | 5 |
| 8 | 0.699 | - | - | 0.909 | 0.911 | 0.362 | 1.85x | 33.5/39.8% | 8.2% | 8 |

### `J-bucketmode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 0.690 | - | - | 0.873 | 0.873 | 0.366 | 1.78x | 32.5/38.3% | 8.1% | 3 |
| local | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| time | 0.694 | - | - | 0.879 | 0.882 | 0.374 | 1.79x | 32.9/38.8% | 8.3% | 3 |
| window | 0.696 | - | - | 0.873 | 0.877 | 0.348 | 1.74x | 31.3/37.3% | 8.0% | 3 |

> bucket-mode=global: misdecodes 41

> bucket-mode=time: misdecodes 26

> bucket-mode=window: misdecodes 7

### `J-timewin` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 0.675 | - | - | 0.850 | 0.852 | 0.360 | 1.93x | 36.0/42.0% | 8.8% | 3 |
| 1800 | 0.694 | - | - | 0.879 | 0.882 | 0.374 | 1.79x | 32.9/38.8% | 8.3% | 3 |
| 3600 | 0.696 | - | - | 0.877 | 0.878 | 0.364 | 1.78x | 32.2/38.2% | 8.2% | 3 |

> time-bucket-s=600: misdecodes 124

> time-bucket-s=1800: misdecodes 26

> time-bucket-s=3600: misdecodes 7

### `J-wincap` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.694 | - | - | 0.862 | 0.880 | 0.350 | 1.73x | 31.3/37.4% | 8.0% | 3 |
| 16 | 0.690 | - | - | 0.865 | 0.867 | 0.344 | 1.75x | 31.4/37.3% | 7.9% | 3 |
| 32 | 0.696 | - | - | 0.873 | 0.877 | 0.348 | 1.74x | 31.3/37.3% | 8.0% | 3 |

> capacity=8: misdecodes 14

> capacity=8: decode_failures 37

> capacity=16: misdecodes 24

> capacity=16: decode_failures 2

> capacity=32: misdecodes 7

### `J-window` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.690 | - | - | 0.874 | 0.877 | 0.341 | 1.85x | 34.1/40.0% | 8.6% | 3 |
| 16 | 0.694 | - | - | 0.872 | 0.874 | 0.352 | 1.78x | 32.5/38.4% | 8.2% | 3 |
| 32 | 0.696 | - | - | 0.873 | 0.877 | 0.348 | 1.74x | 31.3/37.3% | 8.0% | 3 |

> window-size=8: misdecodes 143

> window-size=16: misdecodes 59

> window-size=32: misdecodes 7

### `K-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.547 | - | - | 0.647 | 0.648 | 0.333 | 1.69x | 34.6/37.6% | 9.1% | 3 |
| 60 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 90 | 0.777 | - | - | 0.946 | 0.947 | 0.585 | 2.24x | 39.4/43.6% | 8.3% | 3 |
| 120 | 0.836 | - | - | 0.941 | 0.973 | 0.552 | 2.90x | 55.7/61.8% | 7.6% | 3 |
| 150 | 0.846 | - | - | 0.978 | 0.983 | 0.629 | 3.65x | 59.1/64.6% | 8.9% | 3 |

> nodes=120: decode_failures 75

> nodes=150: decode_failures 64

### `K-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.491 | - | - | 0.791 | 0.792 | 0.149 | 1.53x | 28.4/34.8% | 7.4% | 3 |
| 5 | 0.687 | - | - | 0.858 | 0.861 | 0.446 | 1.70x | 30.6/36.7% | 7.9% | 3 |
| 7 | 0.785 | - | - | 0.873 | 0.873 | 0.567 | 1.91x | 31.9/37.7% | 7.9% | 3 |

### `K-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.685 | - | - | 0.781 | 0.789 | 0.485 | 1.86x | 46.3/49.3% | 10.5% | 3 |
| 60 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 90 | 0.582 | - | - | 0.851 | 0.852 | 0.374 | 2.45x | 34.4/43.8% | 6.9% | 3 |
| 120 | 0.471 | - | - | 0.682 | 0.690 | 0.200 | 3.28x | 35.6/48.2% | 6.8% | 3 |
| 150 | 0.420 | - | - | 0.751 | 0.752 | 0.140 | 4.43x | 45.5/57.5% | 8.2% | 3 |

> nodes=120: decode_failures 15

### `K-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.491 | - | - | 0.791 | 0.792 | 0.149 | 1.53x | 28.4/34.8% | 7.4% | 3 |
| True | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `L-advert` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| dm | 0.700 | - | - | 0.879 | 0.882 | 0.364 | 1.74x | 31.5/37.5% | 7.8% | 3 |

### `L-provide` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| broadcast | 0.726 | - | - | 0.871 | 0.874 | 0.366 | 1.85x | 33.7/39.6% | 8.6% | 3 |

### `M-capacity` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.680 | - | - | 0.848 | 0.854 | 0.341 | 1.76x | 32.4/38.2% | 8.0% | 3 |
| 8 | 0.701 | - | - | 0.877 | 0.879 | 0.367 | 1.76x | 31.9/37.9% | 8.1% | 3 |
| 16 | 0.699 | - | - | 0.879 | 0.880 | 0.364 | 1.75x | 31.7/37.7% | 8.1% | 3 |
| 32 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 50 | 0.697 | - | - | 0.877 | 0.878 | 0.348 | 1.77x | 32.0/37.9% | 8.1% | 3 |

> capacity=4: decode_failures 85

> capacity=8: decode_failures 45

> capacity=16: decode_failures 5

### `M-combined` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.726 | - | - | 0.871 | 0.874 | 0.366 | 1.85x | 33.7/39.6% | 8.6% | 3 |
| heard | 0.724 | - | - | 0.874 | 0.876 | 0.378 | 1.86x | 33.6/39.6% | 8.6% | 3 |

> replay-ordering=heard: misdecodes 5

### `M-jitter` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.703 | - | - | 0.889 | 0.889 | 0.347 | 1.75x | 31.9/37.8% | 8.1% | 3 |
| 30 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 120 | 0.691 | - | - | 0.870 | 0.872 | 0.350 | 1.75x | 31.5/37.5% | 8.0% | 3 |
| 600 | 0.695 | - | - | 0.869 | 0.869 | 0.364 | 1.77x | 31.8/37.7% | 8.1% | 3 |

### `M-replayorder` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| heard | 0.699 | - | - | 0.877 | 0.877 | 0.358 | 1.75x | 31.8/37.7% | 8.1% | 3 |

> replay-ordering=heard: misdecodes 11

### `N-hops` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.682 | - | - | 0.820 | 0.823 | 0.355 | 1.73x | 31.0/36.8% | 8.0% | 3 |
| 2 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 3 | 0.699 | - | - | 0.791 | 0.939 | 0.354 | 1.80x | 32.3/38.4% | 8.1% | 3 |
| 4 | 0.707 | - | - | 0.703 | 0.943 | 0.375 | 1.78x | 31.7/37.5% | 8.3% | 3 |
| 5 | 0.695 | - | - | 0.686 | 0.948 | 0.355 | 1.77x | 31.3/37.2% | 8.3% | 3 |

> hops-apart=3: decode_failures 32

> hops-apart=4: decode_failures 32

> hops-apart=5: decode_failures 24

### `N-place` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.700 | - | - | 0.700 | 0.965 | 0.355 | 1.80x | 31.5/37.5% | 8.1% | 3 |
| routers | 0.696 | - | - | 0.767 | 0.934 | 0.363 | 1.75x | 31.0/37.1% | 8.0% | 3 |
| alternate-routers | 0.692 | - | - | 0.865 | 0.867 | 0.346 | 1.77x | 32.0/38.0% | 8.4% | 3 |
| beside-router | 0.688 | - | - | 0.795 | 0.930 | 0.313 | 1.76x | 31.5/37.7% | 8.0% | 3 |
| random-clients | 0.699 | - | - | 0.769 | 0.772 | 0.336 | 1.75x | 30.9/37.0% | 8.0% | 3 |
| hops-apart | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

> place=spread: decode_failures 23

> place=routers: decode_failures 2

> place=beside-router: decode_failures 25

> place=random-clients: decode_failures 1

### `N-servers` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.691 | - | - | 0.854 | 0.856 | 0.363 | 1.76x | 31.4/37.5% | 8.2% | 2 |
| 3 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 5 | 0.712 | - | - | 0.883 | 0.887 | 0.367 | 1.81x | 32.8/38.7% | 8.2% | 5 |
| 8 | 0.699 | - | - | 0.909 | 0.911 | 0.362 | 1.85x | 33.5/39.8% | 8.2% | 8 |

### `P-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 0.122 | - | - | 0.210 | 0.212 | 0.000 | 0.06x | 0.6/0.8% | 0.2% | 3 |
| MEDIUM_TURBO | 0.390 | - | - | 0.445 | 0.449 | 0.000 | 0.39x | 4.1/4.5% | 1.5% | 3 |
| LONG_TURBO | 0.598 | - | - | 0.796 | 0.817 | 0.217 | 1.54x | 21.8/26.3% | 6.4% | 3 |

> preset=LONG_TURBO: decode_failures 1

### `P-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 0.655 | - | - | 0.834 | 0.835 | 0.348 | 2.33x | 46.0/54.4% | 11.8% | 3 |
| 02-06 | 0.689 | - | - | 0.834 | 0.879 | 0.377 | 1.79x | 33.0/39.1% | 8.3% | 3 |
| 00-08 | 0.687 | - | - | 0.832 | 0.869 | 0.364 | 1.87x | 34.9/41.5% | 8.6% | 3 |

> catch-up-hours=: misdecodes 14

> catch-up-hours=02-06: decode_failures 26

> catch-up-hours=00-08: decode_failures 22

### `P-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.836 | - | - | 0.941 | 0.973 | 0.552 | 2.90x | 55.7/61.8% | 7.6% | 3 |
| True | 0.451 | - | - | 0.550 | 0.689 | 0.326 | 6.45x | 78.8/81.6% | 13.7% | 3 |

> no-congestion-scaling=False: decode_failures 75

> no-congestion-scaling=True: queue drops 31.3% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 45

### `P-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 0.726 | - | - | 0.896 | 0.899 | 0.374 | 1.65x | 30.2/36.0% | 7.8% | 3 |
| sinusoid | 0.706 | - | - | 0.891 | 0.894 | 0.355 | 1.61x | 29.2/34.9% | 7.5% | 3 |
| commuter | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `P-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.238 | - | - | 0.436 | 0.437 | 0.000 | 0.17x | 1.7/2.3% | 0.7% | 3 |
| LONG_FAST | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| LITE_FAST | 0.683 | - | - | 0.853 | 0.859 | 0.374 | 1.37x | 20.7/25.7% | 5.9% | 3 |
| NARROW_SLOW | 0.724 | - | - | 0.889 | 0.898 | 0.390 | 1.70x | 29.6/36.8% | 7.7% | 3 |

> preset=LITE_FAST: decode_failures 1

> preset=NARROW_SLOW: decode_failures 1

### `P-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.238 | - | - | 0.436 | 0.437 | 0.000 | 0.17x | 1.7/2.3% | 0.7% | 3 |
| LONG_FAST | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| LONG_MODERATE | 0.607 | - | - | 0.768 | 0.772 | 0.461 | 4.33x | 71.9/75.5% | 16.1% | 3 |

> preset=LONG_MODERATE: queue drops 11.2% of transmissions - airtime here is measured through a cap

> preset=LONG_MODERATE: decode_failures 5

### `Q-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.687 | - | - | 0 | 0.000 | 0.345 | 1.71x | 30.3/36.3% | 7.9% | 3 |
| sr | 0.699 | - | - | 0.791 | 0.939 | 0.354 | 1.80x | 32.3/38.4% | 8.1% | 3 |

> protocol=sr: decode_failures 32

### `Q-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| random | 0.652 | - | - | 0.882 | 0.888 | 0.249 | 1.75x | 31.3/37.1% | 7.9% | 3 |

### `Q-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 0.625 | - | - | 0.823 | 0.827 | 0.322 | 2.81x | 49.2/56.9% | 12.1% | 3 |
| 3600 | 0.745 | - | - | 0.926 | 0.928 | 0.345 | 1.18x | 22.0/26.3% | 5.6% | 3 |
| 10800 | 0.768 | - | - | 0.940 | 0.941 | 0.372 | 0.78x | 14.5/17.5% | 3.7% | 3 |
| 43200 | 0.787 | - | - | 0.946 | 0.947 | 0.377 | 0.53x | 10.1/12.1% | 2.5% | 3 |

### `Q-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.687 | - | - | 0 | 0.000 | 0.345 | 1.71x | 30.3/36.3% | 7.9% | 3 |
| chain | 0.670 | - | - | 0.794 | 0.875 | 0.365 | 1.93x | 35.6/42.1% | 9.1% | 3 |
| sr | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `Q-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| clustered | 0.556 | - | - | 0.652 | 0.652 | 0.268 | 1.64x | 45.6/46.8% | 7.4% | 3 |
| corridor | 0.489 | - | - | 0.760 | 0.762 | 0.154 | 1.97x | 32.0/35.9% | 8.4% | 3 |
| hub | 0.919 | - | - | 0.967 | 0.967 | 0.675 | 1.78x | 56.5/58.0% | 8.9% | 3 |

### `R-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.836 | - | - | 0.941 | 0.973 | 0.552 | 2.90x | 55.7/61.8% | 7.6% | 3 |
| True | 0.823 | - | - | 0.927 | 0.970 | 0.535 | 3.14x | 58.8/64.7% | 8.1% | 3 |

> no-adopt-hop-recommendation=False: decode_failures 75

> no-adopt-hop-recommendation=True: decode_failures 61

### `R-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 0.298 | - | - | 0.566 | 0.570 | 0.061 | 6.55x | 33.9/49.0% | 6.4% | 3 |
| truesize | 0.335 | - | - | 0.632 | 0.633 | 0.072 | 3.62x | 20.7/37.1% | 5.3% | 3 |

> congestion-input=hotstore: decode_failures 14

> congestion-input=truesize: decode_failures 21

### `R-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 0.849 | - | - | 0.975 | 0.978 | 0.574 | 2.65x | 51.8/57.3% | 6.9% | 3 |
| adaptive | 0.836 | - | - | 0.941 | 0.973 | 0.552 | 2.90x | 55.7/61.8% | 7.6% | 3 |

> congestion-mode=static: decode_failures 9

> congestion-mode=adaptive: decode_failures 75

### `R-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.645 | - | - | 0.838 | 0.846 | 0.323 | 2.00x | 36.9/43.2% | 9.5% | 3 |
| True | 0.653 | - | - | 0.840 | 0.843 | 0.357 | 2.00x | 36.7/43.3% | 9.5% | 3 |

### `R-dmmode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 0.641 | - | - | 0.834 | 0.841 | 0.360 | 2.19x | 39.4/46.1% | 10.0% | 3 |
| directed-with-late-flood | 0.645 | - | - | 0.838 | 0.846 | 0.323 | 2.00x | 36.9/43.2% | 9.5% | 3 |
| m4-early-flood | 0.655 | - | - | 0.852 | 0.857 | 0.336 | 2.02x | 36.9/43.5% | 9.5% | 3 |

### `R-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 0.653 | - | - | 0.840 | 0.843 | 0.357 | 2.00x | 36.7/43.3% | 9.5% | 3 |
| m4-early-flood | 0.655 | - | - | 0.863 | 0.869 | 0.343 | 2.02x | 37.1/43.6% | 9.5% | 3 |

### `R-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.695 | - | - | 0.865 | 0.866 | 0.368 | 1.92x | 37.5/41.7% | 8.3% | 3 |
| True | 0.750 | - | - | 0.871 | 0.872 | 0.421 | 2.02x | 37.5/41.6% | 8.0% | 3 |

### `R-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 0.778 | - | - | 0.930 | 0.934 | 0.508 | 0.92x | 15.1/16.5% | 2.7% | 3 |
| 2.8 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `R-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 120 | 0.471 | - | - | 0.682 | 0.690 | 0.200 | 3.28x | 35.6/48.2% | 6.8% | 3 |
| 250 | 0.294 | - | - | 0.554 | 0.559 | 0.060 | 6.92x | 35.6/51.8% | 6.9% | 3 |
| 500 | 0.175 | - | - | 0.290 | 0.307 | 0.000 | 12.85x | 35.7/56.1% | 7.9% | 3 |

> nodes=120: decode_failures 15

> nodes=250: decode_failures 32

> nodes=500: decode_failures 172

### `R-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.622 | - | - | 0.768 | 0.770 | 0.376 | 3.77x | 62.5/67.6% | 13.2% | 3 |
| 100 | 0.752 | - | - | 0.857 | 0.859 | 0.491 | 2.13x | 38.1/42.1% | 8.0% | 3 |
| 120 | 0.752 | - | - | 0.857 | 0.859 | 0.491 | 2.13x | 38.1/42.1% | 8.0% | 3 |
| 250 | 0.752 | - | - | 0.857 | 0.859 | 0.491 | 2.13x | 38.1/42.1% | 8.0% | 3 |

### `R-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.186 | - | - | 0.307 | 0.330 | 0.052 | 14.46x | 63.3/76.2% | 14.0% | 3 |
| 120 | 0.298 | - | - | 0.566 | 0.570 | 0.061 | 6.55x | 33.9/49.0% | 6.4% | 3 |
| 250 | 0.300 | - | - | 0.567 | 0.570 | 0.059 | 6.51x | 33.8/48.6% | 6.5% | 3 |

> max-num-nodes=10: decode_failures 52

> max-num-nodes=120: decode_failures 14

> max-num-nodes=250: decode_failures 17

### `R-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.25 | 0.684 | - | - | 0.841 | 0.842 | 0.414 | 1.52x | 27.3/32.8% | 6.9% | 3 |
| 0.5 | 0.716 | - | - | 0.863 | 0.864 | 0.346 | 1.33x | 23.3/28.4% | 6.0% | 3 |
| 0.75 | 0.777 | - | - | 0.932 | 0.933 | 0.452 | 1.20x | 20.3/23.8% | 4.5% | 3 |

### `R-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.25 | 0.684 | - | - | 0.833 | 0.836 | 0.401 | 1.55x | 27.7/33.1% | 7.1% | 3 |
| 0.5 | 0.720 | - | - | 0.888 | 0.890 | 0.356 | 1.33x | 23.6/28.4% | 6.2% | 3 |
| 0.75 | 0.770 | - | - | 0.919 | 0.919 | 0.471 | 1.19x | 20.5/23.9% | 4.5% | 3 |

### `R-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 0.467 | - | - | 0.660 | 0.667 | 0.207 | 3.10x | 34.1/46.0% | 6.5% | 3 |
| 250 | 0.298 | - | - | 0.566 | 0.570 | 0.061 | 6.55x | 33.9/49.0% | 6.4% | 3 |
| 500 | 0.175 | - | - | 0.293 | 0.307 | 0.000 | 12.25x | 33.7/53.2% | 6.9% | 3 |

> nodes=120: decode_failures 2

> nodes=250: decode_failures 14

> nodes=500: decode_failures 82

### `R-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.752 | - | - | 0.857 | 0.859 | 0.491 | 2.13x | 38.1/42.1% | 8.0% | 3 |
| baymesh-2026-08 | 0.752 | - | - | 0.857 | 0.859 | 0.491 | 2.13x | 38.1/42.1% | 8.0% | 3 |
| constrained | 0.622 | - | - | 0.768 | 0.770 | 0.376 | 3.77x | 62.5/67.6% | 13.2% | 3 |

### `R-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| KNOWN_ONLY | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| CORE_PORTNUMS_ONLY | 0.695 | - | - | 0.811 | 0.887 | 0.368 | 1.71x | 30.8/36.6% | 7.9% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 3

### `R-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| True | 0.693 | - | - | 0.873 | 0.875 | 0.357 | 1.77x | 31.9/37.9% | 8.1% | 3 |

### `R-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.836 | - | - | 0.941 | 0.973 | 0.552 | 2.90x | 55.7/61.8% | 7.6% | 3 |
| True | 0.829 | - | - | 0.937 | 0.970 | 0.558 | 2.93x | 55.9/62.0% | 7.6% | 3 |

> extra-repeats=False: decode_failures 75

> extra-repeats=True: decode_failures 82

### `R-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.682 | - | - | 0.894 | 0.895 | 0.256 | 1.74x | 31.8/37.5% | 8.1% | 3 |
| baymesh-2026-08 | 0.649 | - | - | 0.859 | 0.860 | 0.256 | 1.64x | 30.8/37.4% | 7.4% | 3 |

### `R-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.699 | - | - | 0.894 | 0.897 | 0.278 | 1.77x | 31.6/37.1% | 7.8% | 3 |
| baymesh-2026-08 | 0.714 | - | - | 0.839 | 0.840 | 0.343 | 1.85x | 34.4/41.6% | 7.5% | 3 |

### `R-routerlate` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.05 | 0.706 | - | - | 0.867 | 0.867 | 0.366 | 1.92x | 37.8/43.4% | 8.0% | 3 |
| 0.1 | 0.703 | - | - | 0.868 | 0.868 | 0.404 | 2.07x | 39.3/44.1% | 8.1% | 3 |
| 0.2 | 0.695 | - | - | 0.861 | 0.862 | 0.405 | 2.39x | 47.6/53.6% | 8.2% | 3 |

### `R-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| BALANCED | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| STRICT | 0.605 | - | - | 0.810 | 0.812 | 0.292 | 1.93x | 34.2/40.7% | 8.7% | 3 |

### `R-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 0.764 | - | - | 0.932 | 0.933 | 0.373 | 0.89x | 16.8/20.5% | 4.4% | 3 |
| signing=true | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `R-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| local-typical | 0.396 | - | - | 0.659 | 0.753 | 0.000 | 1.99x | 23.7/34.4% | 6.9% | 3 |
| event | 0.127 | - | - | 0.140 | 0.356 | 0.000 | 1.46x | 20.4/27.3% | 6.1% | 3 |
| backbone | 0.949 | - | - | 0.986 | 0.986 | 0.772 | 1.86x | 58.3/59.8% | 8.4% | 3 |

> siting-mix=local-typical: decode_failures 18

> siting-mix=backbone: misdecodes 1

### `R-srretries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.692 | - | - | 0.864 | 0.868 | 0.352 | 1.66x | 30.1/35.7% | 7.6% | 3 |
| 1 | 0.691 | - | - | 0.882 | 0.885 | 0.328 | 1.65x | 29.9/35.4% | 7.6% | 3 |
| 2 | 0.701 | - | - | 0.883 | 0.886 | 0.373 | 1.68x | 30.6/36.2% | 7.7% | 3 |
| 4 | 0.688 | - | - | 0.855 | 0.861 | 0.348 | 1.68x | 30.3/36.0% | 7.7% | 3 |

### `R-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.25 | 0.691 | - | - | 0.875 | 0.878 | 0.353 | 1.78x | 32.4/38.5% | 8.3% | 3 |
| 1.0 | 0.687 | - | - | 0.866 | 0.867 | 0.339 | 1.97x | 35.4/42.0% | 9.1% | 3 |
| 4.0 | 0.640 | - | - | 0.826 | 0.830 | 0.345 | 2.36x | 42.3/49.8% | 10.7% | 3 |

### `R-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.436 | - | - | 0.532 | 0.665 | 0.319 | 6.54x | 79.0/81.7% | 13.8% | 3 |
| 1.0 | 0.401 | - | - | 0.489 | 0.629 | 0.294 | 6.80x | 78.3/80.8% | 14.3% | 3 |

> traceroute-per-hour=0.0: queue drops 33.3% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 44

> traceroute-per-hour=1.0: queue drops 38.7% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 48

### `R-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 0.766 | - | - | 0.930 | 0.933 | 0.489 | 0.89x | 16.7/18.4% | 4.0% | 3 |
| 2.5 | 0.774 | - | - | 0.946 | 0.946 | 0.494 | 0.91x | 16.9/18.8% | 4.0% | 3 |
| 2.6 | 0.774 | - | - | 0.945 | 0.946 | 0.489 | 0.90x | 16.9/18.9% | 4.0% | 3 |
| 2.7 | 0.777 | - | - | 0.943 | 0.943 | 0.476 | 0.90x | 17.4/19.5% | 4.7% | 3 |
| 2.8 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |

### `R-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.436 | - | - | 0.532 | 0.665 | 0.319 | 6.54x | 79.0/81.7% | 13.8% | 3 |
| 25 | 0.436 | - | - | 0.532 | 0.665 | 0.319 | 6.54x | 79.0/81.7% | 13.8% | 3 |
| 100 | 0.436 | - | - | 0.532 | 0.665 | 0.319 | 6.54x | 79.0/81.7% | 13.8% | 3 |
| 2000 | 0.436 | - | - | 0.532 | 0.665 | 0.319 | 6.54x | 79.0/81.7% | 13.8% | 3 |

> warm-num-nodes=0: queue drops 33.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 44

> warm-num-nodes=25: queue drops 33.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 44

> warm-num-nodes=100: queue drops 33.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 44

> warm-num-nodes=2000: queue drops 33.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 44

### `X-amplifiers` - amplifier-mix  `--scenario ridge`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| sprinkled | 0.752 | - | - | 0.898 | 0.898 | 0.526 | 1.64x | 33.3/41.2% | 7.3% | 3 |
| arms-race | 0.885 | - | - | 0.940 | 0.941 | 0.432 | 1.38x | 37.1/42.7% | 8.1% | 3 |

### `X-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.1 | 0.796 | - | - | 0.877 | 0.877 | 0.647 | 1.58x | 35.7/37.6% | 6.8% | 3 |
| 0.3 | 0.888 | - | - | 0.981 | 0.982 | 0.773 | 1.41x | 41.2/44.6% | 7.1% | 3 |

> amplify-worst=0.3: misdecodes 1

### `X-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.649 | - | - | 0.859 | 0.860 | 0.256 | 1.64x | 30.8/37.4% | 7.4% | 3 |
| inverse | 0.629 | - | - | 0.871 | 0.874 | 0.273 | 1.65x | 27.0/31.4% | 5.8% | 3 |
| random | 0.633 | - | - | 0.849 | 0.854 | 0.239 | 1.59x | 30.3/35.1% | 8.0% | 3 |

### `X-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.745 | - | - | 0.926 | 0.928 | 0.345 | 1.18x | 22.0/26.3% | 5.6% | 3 |
| 900 | 0.625 | - | - | 0.823 | 0.827 | 0.322 | 2.81x | 49.2/56.9% | 12.1% | 3 |
| 300 | 0.295 | - | - | 0.416 | 0.560 | 0.144 | 5.79x | 76.5/79.6% | 20.4% | 3 |

> broadcast-interval-s=300: queue drops 23.9% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 14

### `X-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.832 | - | - | 0.919 | 0.919 | 0.585 | 1.34x | 22.2/26.2% | 5.5% | 3 |
| 900 | 0.698 | - | - | 0.802 | 0.802 | 0.532 | 3.12x | 50.0/57.5% | 11.9% | 3 |
| 300 | 0.332 | - | - | 0.420 | 0.485 | 0.207 | 5.75x | 76.3/79.6% | 19.2% | 3 |

> broadcast-interval-s=300: queue drops 18.4% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 23

### `X-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 0.25 | 0.742 | - | - | 0.898 | 0.899 | 0.438 | 1.53x | 35.3/39.8% | 7.8% | 3 |
| 1.0 | 0.862 | - | - | 0.952 | 0.952 | 0.698 | 1.21x | 42.6/45.2% | 7.8% | 3 |

### `X-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| temporal | 0.585 | - | - | 0.823 | 0.825 | 0.335 | 1.83x | 33.2/39.4% | 7.8% | 3 |
| transient | 0.688 | - | - | 0.865 | 0.866 | 0.360 | 1.76x | 32.1/38.1% | 8.1% | 3 |
| periodic | 0.466 | - | - | 0.624 | 0.636 | 0.184 | 1.58x | 28.6/33.8% | 6.5% | 3 |

### `X-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.649 | - | - | 0.859 | 0.860 | 0.256 | 1.64x | 30.8/37.4% | 7.4% | 3 |
| no-mute | 0.671 | - | - | 0.895 | 0.896 | 0.310 | 1.82x | 30.3/35.2% | 7.9% | 3 |
| all-routers | 0.739 | - | - | 0.918 | 0.918 | 0.451 | 3.93x | 59.1/65.1% | 8.5% | 3 |

### `X-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 0.612 | - | - | 0.779 | 0.792 | 0.291 | 1.70x | 31.0/36.8% | 7.5% | 3 |
| 10000 | 0.466 | - | - | 0.624 | 0.636 | 0.184 | 1.58x | 28.6/33.8% | 6.5% | 3 |
| 4000 | 0.160 | - | - | 0.217 | 0.297 | 0.053 | 1.28x | 23.2/26.6% | 4.0% | 3 |
| 2000 | 0.002 | - | - | 0.001 | 0.004 | 0.000 | 0.33x | 6.0/6.7% | 0.7% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 5

### `X-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.649 | - | - | 0.859 | 0.860 | 0.256 | 1.64x | 30.8/37.4% | 7.4% | 3 |
| local-typical | 0.292 | - | - | 0.412 | 0.662 | 0.000 | 1.76x | 23.3/27.7% | 6.2% | 3 |
| basement-heavy | 0.035 | - | - | 0.220 | 0.223 | 0.000 | 0.49x | 4.7/9.2% | 2.6% | 3 |

> siting-mix=local-typical: decode_failures 4

### `X-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 0.696 | - | - | 0.880 | 0.882 | 0.367 | 1.79x | 32.4/38.3% | 8.3% | 3 |
| 1.25 | 0.398 | - | - | 0.458 | 0.458 | 0.000 | 2.07x | 26.4/31.6% | 7.7% | 3 |
| 1.5 | 0.213 | - | - | 0.359 | 0.369 | 0.000 | 1.86x | 20.2/25.3% | 6.7% | 3 |
| 2.0 | 0.070 | - | - | 0.118 | 0.188 | 0.000 | 0.90x | 8.1/11.1% | 4.0% | 3 |

> stretch=1.5: decode_failures 3

> stretch=2.0: decode_failures 7

### `X-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.213 | - | - | 0.359 | 0.369 | 0.000 | 1.86x | 20.2/25.3% | 6.7% | 3 |
| 1.0 | 0.619 | - | - | 0.720 | 0.720 | 0.369 | 1.35x | 33.5/35.7% | 6.7% | 3 |

> duct-per-hour=0.0: decode_failures 3

### `X-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.723 | - | - | 0.867 | 0.876 | 0.000 | 3.34x | 44.0/53.6% | 8.4% | 3 |
| inverse | 0.709 | - | - | 0.881 | 0.888 | 0.000 | 3.24x | 37.2/46.6% | 5.2% | 3 |

> role-placement=degree: decode_failures 49

> role-placement=inverse: decode_failures 38

