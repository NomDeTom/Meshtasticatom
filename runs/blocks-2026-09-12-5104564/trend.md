# Sweep blocks-2026-09-12-5104564

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 5104564 · seeds 5104564
- **blocks** 87 run
- **compute** 10.7 h of simulator time across every cell
- **generated** 2026-09-12T08:42:27+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>63 warnings</summary>

- DB-hotstore: max-num-nodes=10: decode_failures 5
- DB-hotstore-stress: max-num-nodes=10: decode_failures 83
- DB-platform: platform-mix=constrained: decode_failures 1
- DB-warm: warm-num-nodes=0: decode_failures 93
- DB-warm: warm-num-nodes=25: decode_failures 93
- DB-warm: warm-num-nodes=100: decode_failures 93
- DB-warm: warm-num-nodes=2000: decode_failures 93
- DG-burst: burst-loss=0.2: decode_failures 6
- DG-burst: burst-loss=0.3: decode_failures 13
- DG-outage: burst-loss=0.1: decode_failures 30
- DG-outage: burst-loss=0.2: decode_failures 43
- DG-outage: burst-loss=0.3: decode_failures 32
- LD-chatty-hops: broadcast-interval-s=300: queue drops 13.9% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 35
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 93
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 14.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 98
- MS-density: nodes=40: decode_failures 2
- MS-hopscale: nodes=500: decode_failures 217
- MS-oversubscribed: nodes=500: decode_failures 131
- MS-stretch: stretch=1.5: decode_failures 34
- RF-bw500: preset=SHORT_TURBO: decode_failures 2
- RF-eu-presets: preset=SHORT_FAST: decode_failures 33
- RF-preset: preset=SHORT_FAST: decode_failures 33
- RF-preset: preset=LONG_MODERATE: decode_failures 49
- RF-preset: slower: 7.1 s per simulated hour against 3.01 over 22 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 8
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 34
- RF-txpower: tx-power=14: decode_failures 5
- SF-bucket-mode: bucket-mode=global: misdecodes 60
- SF-bucket-mode: bucket-mode=time: misdecodes 40
- SF-bucket-mode: bucket-mode=window: misdecodes 41
- SF-bucket-time: time-bucket-s=600: misdecodes 116
- SF-bucket-time: time-bucket-s=1800: misdecodes 40
- SF-bucket-time: time-bucket-s=3600: misdecodes 13
- SF-cadence: trigger=interval: misdecodes 24
- SF-cadence: trigger=aimd: misdecodes 7
- SF-cadence: trigger=aimd: decode_failures 4
- SF-cadence: trigger=bucket+interval: misdecodes 34
- SF-capacity-local: capacity=4: decode_failures 70
- SF-capacity-local: capacity=8: decode_failures 5
- SF-capacity: capacity=4: decode_failures 70
- SF-capacity: capacity=8: decode_failures 5
- SF-capacity-window: capacity=8: misdecodes 32
- SF-capacity-window: capacity=8: decode_failures 17
- SF-capacity-window: capacity=16: misdecodes 31
- SF-capacity-window: capacity=32: misdecodes 41
- SF-catchup: catch-up-hours=: misdecodes 34
- SF-catchup: catch-up-hours=02-06: misdecodes 1
- SF-catchup: catch-up-hours=02-06: decode_failures 45
- SF-catchup: catch-up-hours=00-08: misdecodes 2
- SF-catchup: catch-up-hours=00-08: decode_failures 44
- SF-hops-flat: faster: 1.6 s per simulated hour against 3.45 over 22 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: faster: 1.55 s per simulated hour against 4.56 over 22 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=spread: decode_failures 4
- SF-place-spread: place=spread: decode_failures 4
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 16
- SF-replay-order: replay-ordering=heard: misdecodes 26
- SF-window-size: window-size=8: misdecodes 111
- SF-window-size: window-size=16: misdecodes 59
- SF-window-size: window-size=32: misdecodes 41
- TH-congestion: no-congestion-scaling=True: decode_failures 115

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-preset` | 7.1 | 3.01 | 2.36x | 22 |
| `RF-eu-presets` | 3.93 | 2.03 | 1.94x | 22 |
| `RF-stretch-duct` | 4.86 | 2.8 | 1.74x | 22 |
| `MS-stretch` | 3.63 | 2.21 | 1.64x | 22 |
| `SF-bucket-mode` | 1.07 | 1.63 | 0.66x | 22 |
| `DG-burst` | 3.21 | 4.96 | 0.65x | 22 |
| `MS-siting` | 1.32 | 2.04 | 0.65x | 22 |
| `FW-mixed` | 1.07 | 1.69 | 0.63x | 22 |
| `PR-protocol` | 0.931 | 1.49 | 0.62x | 22 |
| `SF-place-spread` | 1.8 | 2.92 | 0.62x | 22 |
| `RT-hoplimit` | 1.16 | 1.89 | 0.61x | 22 |
| `SF-sr-retries` | 1.01 | 1.65 | 0.61x | 22 |
| `LD-chatty-hops` | 2.44 | 4.34 | 0.56x | 22 |
| `SF-place-flat` | 1.53 | 3.01 | 0.51x | 22 |
| `SF-hops-flat` | 1.6 | 3.45 | 0.46x | 22 |
| `SF-hops-spread` | 1.55 | 4.57 | 0.34x | 22 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.985 | 0.985 | 0.879 → 0.883 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.968 | 0.968 | 0.867 → 0.883 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.126 → 0.968 | 0.842 | 0.148 → 0.878 | 8.8x advert_bytes | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.104 → 0.885 | 0.781 | 0.104 → 0.878 | 5.7x sr_airtime | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.125 → 0.903 | 0.778 | 0.123 → 0.813 | 1e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.119 → 0.893 | 0.773 | 0.032 → 0.768 | 8.5x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **held** | 0.210 → 0.968 | 0.758 | 0.159 → 0.878 | 7.4x sr_bytes | down | 4 |
| `RF-bw500` | preset | **held** | 0.256 → 0.978 | 0.722 | 0.300 → 0.833 | 4x advert_bytes | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.304 → 0.943 | 0.638 | 0.295 → 0.942 | 2.6x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.313 → 0.885 | 0.572 | 0.308 → 0.878 | 19x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.311 → 0.792 | 0.481 | 0.306 → 0.777 | 5.6x sr_bytes | down | 3 |
| `SF-place-flat` | place | **held** | 0.510 → 0.985 | 0.475 | 0.861 → 0.878 | 2.6x sr_airtime | up | 6 |
| `SF-place-spread` | place | **held** | 0.510 → 0.985 | 0.475 | 0.861 → 0.878 | 2.6x sr_airtime | up | 6 |
| `RF-eu-presets` | preset | **text** | 0.502 → 0.885 | 0.383 | 0.487 → 0.878 | 2.7x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.502 → 0.885 | 0.383 | 0.487 → 0.878 | 2.7x sr_bytes | up | 3 |
| `MS-topology` | topology | **held** | 0.620 → 0.990 | 0.371 | 0.593 → 0.943 | 2.2x sr_airtime | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.566 → 0.885 | 0.319 | 0.534 → 0.878 | 2.9x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.590 → 0.896 | 0.306 | 0.578 → 0.893 | 8.6x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.552 → 0.851 | 0.299 | 0.544 → 0.851 | 11x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.607 → 0.885 | 0.278 | 0.565 → 0.878 | 2.7x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.489 → 0.743 | 0.254 | 0.323 → 0.528 | 5.1x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.593 → 0.794 | 0.201 | 0.571 → 0.763 | 1.9x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.758 → 0.957 | 0.199 | 0.742 → 0.954 | 4.1x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.698 → 0.885 | 0.187 | 0.686 → 0.878 | 4.5x sr_bytes | down | 5 |
| `RF-noise` | noise-profile | **text** | 0.711 → 0.885 | 0.174 | 0.703 → 0.878 | 1.4x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.772 → 0.929 | 0.156 | 0.768 → 0.922 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.772 → 0.929 | 0.156 | 0.768 → 0.922 | 2.6x bytes_on_air | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.739 → 0.885 | 0.146 | 0.718 → 0.878 | 1.7x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.744 → 0.885 | 0.141 | 0.744 → 0.878 | 1.2x sr_airtime | down | 3 |
| `MS-density` | nodes | **text** | 0.820 → 0.957 | 0.138 | 0.806 → 0.954 | 4.4x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.739 → 0.855 | 0.116 | 0.718 → 0.855 | 1.9x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.739 → 0.849 | 0.110 | 0.718 → 0.848 | 1.8x sr_bytes | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.794 → 0.885 | 0.091 | 0.774 → 0.878 | 1.8x sr_bytes | down | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.803 → 0.887 | 0.084 | 0.668 → 0.743 | 1.5x sr_airtime | down | 2 |
| `MS-roles` | role-mix | **text** | 0.772 → 0.856 | 0.084 | 0.768 → 0.852 | 1.1x bytes_on_air | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.784 → 0.863 | 0.078 | 0.781 → 0.858 | 1.2x sr_bytes | down | 2 |
| `DB-hotstore` | max-num-nodes | **text** | 0.849 → 0.922 | 0.073 | 0.839 → 0.918 | 2.4x sr_airtime | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.822 → 0.885 | 0.063 | 0.807 → 0.878 | 1.5x sr_bytes | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.860 → 0.922 | 0.062 | 0.844 → 0.918 | 2.3x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.851 → 0.912 | 0.061 | 0.834 → 0.910 | 5.1x bytes_on_air | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.885 → 0.941 | 0.055 | 0.878 → 0.938 | 1.6x sr_bytes | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.918 → 0.968 | 0.049 | 0.875 → 0.878 | 27x sr_airtime | down | 3 |
| `AD-worst` | role-placement | **text** | 0.749 → 0.794 | 0.045 | 0.736 → 0.791 | 1.2x sr_bytes | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.885 → 0.927 | 0.042 | 0.878 → 0.926 | 1.2x bytes_on_air | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.885 → 0.926 | 0.041 | 0.878 → 0.921 | 1.2x bytes_on_air | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.723 → 0.759 | 0.036 | 0.524 → 0.557 | 1.4x sr_airtime | up | 2 |
| `AD-badrouters` | role-placement | **held** | 0.859 → 0.893 | 0.034 | 0.721 → 0.768 | 1.4x sr_bytes | down | 3 |
| `FW-versions` | profile | **text** | 0.885 → 0.919 | 0.034 | 0.878 → 0.916 | 3.2x bytes_on_air | down | 5 |
| `FW-mixed` | legacy-fraction | **held** | 0.956 → 0.988 | 0.033 | 0.861 → 0.888 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.958 → 0.991 | 0.033 | 0.866 → 0.891 | 2.1x bytes_on_air | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.853 → 0.885 | 0.032 | 0.837 → 0.878 | 1.4x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.936 → 0.968 | 0.032 | 0.851 → 0.878 | 14x sr_bytes | down | 4 |
| `FW-firmware` | profile | **text** | 0.885 → 0.914 | 0.029 | 0.878 → 0.910 | 3.1x bytes_on_air | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.885 → 0.909 | 0.024 | 0.878 → 0.901 | 1.4x bytes_on_air | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.885 → 0.907 | 0.022 | 0.878 → 0.904 | 3.4x bytes_on_air | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.961 → 0.981 | 0.020 | 0.867 → 0.878 | 5.9x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.961 → 0.981 | 0.020 | 0.867 → 0.878 | 5.9x sr_bytes | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.968 → 0.986 | 0.018 | 0.878 → 0.882 | 1.6x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.968 → 0.986 | 0.018 | 0.878 → 0.882 | 1.6x sr_bytes | down | 5 |
| `LD-diurnal` | diurnal | **held** | 0.968 → 0.984 | 0.016 | 0.878 → 0.895 | 1.3x sr_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.958 → 0.974 | 0.016 | 0.872 → 0.883 | 2.6x advert_bytes | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.871 → 0.887 | 0.016 | 0.861 → 0.883 | 9.5x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.876 → 0.891 | 0.015 | 0.869 → 0.885 | 1.1x sr_airtime | down | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.958 → 0.973 | 0.014 | 0.872 → 0.880 | 5.5x advert_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.885 → 0.899 | 0.014 | 0.878 → 0.878 | 2.7x sr_airtime | up | 2 |
| `SF-capacity-window` | capacity | **held** | 0.962 → 0.974 | 0.012 | 0.875 → 0.883 | 2.3x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.897 → 0.909 | 0.012 | 0.890 → 0.903 | 1.1x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **text** | 0.878 → 0.889 | 0.011 | 0.871 → 0.883 | 4.5x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.962 → 0.972 | 0.010 | 0.870 → 0.878 | 3.1x advert_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.953 → 0.963 | 0.010 | 0.855 → 0.862 | 1.1x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.855 → 0.862 | 0.008 | 0.855 → 0.862 | 1x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **text** | 0.851 → 0.858 | 0.007 | 0.851 → 0.858 | 1.3x sr_airtime | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.878 → 0.885 | 0.007 | 0.871 → 0.878 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.878 → 0.885 | 0.007 | 0.871 → 0.878 | 1.1x sr_bytes | up | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.952 → 0.957 | 0.006 | 0.947 → 0.954 | 1.2x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.893 → 0.899 | 0.006 | 0.869 → 0.878 | 1.2x sr_bytes | down | 2 |
| `SF-capacity` | capacity | **held** | 0.963 → 0.968 | 0.005 | 0.873 → 0.878 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.963 → 0.968 | 0.005 | 0.873 → 0.878 | 5.3x advert_bytes | up | 5 |
| `SF-replay-order` | replay-ordering | **text** | 0.881 → 0.885 | 0.004 | 0.874 → 0.878 | 1.3x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.882 → 0.885 | 0.003 | 0.873 → 0.878 | 3.1x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **text** | 0.882 → 0.885 | 0.003 | 0.873 → 0.878 | 5.7x advert_bytes | = | 3 |
| `PR-repeats` | extra-repeats | **text** | 0.885 → 0.888 | 0.003 | 0.878 → 0.880 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.957 → 0.960 | 0.003 | 0.954 → 0.957 | 1.1x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.983 → 0.985 | 0.002 | 0.875 → 0.878 | 2.7x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.957 → 0.958 | 0.000 | 0.954 → 0.954 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| sprinkled | 1 | 0.888 | 0.883 | 0.005 | - | - | 0.967 | 0.968 | 0.000 | 1.12x | 18.5/23.0/27.4% | 1.5/5.3% | 3 |
| arms-race | 1 | 0.927 | 0.926 | 0.002 | - | - | 0.969 | 0.969 | 0.340 | 1.10x | 21.7/28.3/31.0% | 1.5/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.991 | 0.992 | 0.500 | 1.29x | 19.9/26.2/30.4% | 1.9/5.3% | 3 |
| 0.3 | 1 | 0.941 | 0.938 | 0.003 | - | - | 0.997 | 0.998 | 0.832 | 1.12x | 19.5/26.3/31.5% | 1.4/5.2% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.772 | 0.768 | 0.004 | - | - | 0.893 | 0.893 | 0.174 | 1.12x | 17.6/24.4/31.2% | 1.8/5.4% | 3 |
| inverse | 1 | 0.741 | 0.721 | 0.020 | - | - | 0.890 | 0.891 | 0.133 | 1.12x | 14.2/19.8/25.3% | 2.1/3.3% | 3 |
| random | 1 | 0.750 | 0.738 | 0.012 | - | - | 0.859 | 0.863 | 0.175 | 1.19x | 16.0/20.7/23.9% | 2.1/5.0% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.772 | 0.768 | 0.004 | - | - | 0.893 | 0.893 | 0.174 | 1.12x | 17.6/24.4/31.2% | 1.8/5.4% | 3 |
| all-routers | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.985 | 0.987 | 0.294 | 2.87x | 35.6/45.1/52.0% | 4.8/5.4% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.772 | 0.768 | 0.004 | - | - | 0.893 | 0.893 | 0.174 | 1.12x | 17.6/24.4/31.2% | 1.8/5.4% | 3 |
| no-mute | 1 | 0.850 | 0.846 | 0.004 | - | - | 0.942 | 0.942 | 0.176 | 1.36x | 19.1/24.8/30.4% | 2.1/5.6% | 3 |
| all-routers | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.985 | 0.987 | 0.294 | 2.87x | 35.6/45.1/52.0% | 4.8/5.4% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.772 | 0.768 | 0.004 | - | - | 0.893 | 0.893 | 0.174 | 1.12x | 17.6/24.4/31.2% | 1.8/5.4% | 3 |
| local-typical | 1 | 0.460 | 0.453 | 0.006 | - | - | 0.645 | 0.647 | 0.000 | 1.27x | 13.8/25.2/30.2% | 2.0/5.5% | 3 |
| basement-heavy | 1 | 0.032 | 0.032 | 0.000 | - | - | 0.119 | 0.122 | 0.000 | 0.54x | 0.2/9.6/17.0% | 0.2/3.3% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.794 | 0.791 | 0.004 | - | - | 0.921 | 0.921 | 0.000 | 2.20x | 15.7/25.1/32.2% | 1.7/5.0% | 3 |
| inverse | 1 | 0.749 | 0.736 | 0.012 | - | - | 0.919 | 0.920 | 0.000 | 2.03x | 13.8/21.7/28.1% | 1.6/3.0% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.883 | 0.883 | 0.000 | - | - | 0 | 0.000 | 0.177 | 1.28x | 19.1/25.8/30.5% | 1.9/5.3% | 3 |
| sr | 1 | 0.889 | 0.879 | 0.009 | - | - | 0.985 | 0.986 | 0.216 | 1.30x | 19.4/26.1/30.8% | 2.0/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.849 | 0.839 | 0.009 | - | - | 0.926 | 0.945 | 0.192 | 3.27x | 44.3/58.8/67.5% | 4.9/10.4% | 3 |
| 100 | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.980 | 0.981 | 0.182 | 1.62x | 22.6/31.0/37.3% | 2.2/5.4% | 3 |
| 120 | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.980 | 0.981 | 0.182 | 1.62x | 22.6/31.0/37.3% | 2.2/5.4% | 3 |
| 250 | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.980 | 0.981 | 0.182 | 1.62x | 22.6/31.0/37.3% | 2.2/5.4% | 3 |

> max-num-nodes=10: decode_failures 5

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.328 | 0.323 | 0.005 | - | - | 0.489 | 0.508 | 0.106 | 12.01x | 40.1/58.7/71.8% | 4.2/11.6% | 3 |
| 120 | 1 | 0.531 | 0.524 | 0.007 | - | - | 0.723 | 0.724 | 0.124 | 4.61x | 15.3/26.4/38.0% | 1.5/5.5% | 3 |
| 250 | 1 | 0.535 | 0.528 | 0.007 | - | - | 0.743 | 0.745 | 0.140 | 4.52x | 15.1/25.5/37.4% | 1.5/5.4% | 3 |

> max-num-nodes=10: decode_failures 83

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.980 | 0.981 | 0.182 | 1.62x | 22.6/31.0/37.3% | 2.2/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.980 | 0.981 | 0.182 | 1.62x | 22.6/31.0/37.3% | 2.2/5.4% | 3 |
| constrained | 1 | 0.860 | 0.844 | 0.016 | - | - | 0.953 | 0.957 | 0.195 | 3.28x | 44.3/58.7/67.6% | 4.9/10.4% | 3 |

> platform-mix=constrained: decode_failures 1

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.756 | 0.743 | 0.013 | - | - | 0.887 | 0.930 | 0.475 | 5.79x | 58.1/70.8/75.6% | 4.1/11.5% | 3 |
| 25 | 1 | 0.756 | 0.743 | 0.013 | - | - | 0.887 | 0.930 | 0.475 | 5.79x | 58.1/70.8/75.6% | 4.1/11.5% | 3 |
| 100 | 1 | 0.756 | 0.743 | 0.013 | - | - | 0.887 | 0.930 | 0.475 | 5.79x | 58.1/70.8/75.6% | 4.1/11.5% | 3 |
| 2000 | 1 | 0.756 | 0.743 | 0.013 | - | - | 0.887 | 0.930 | 0.475 | 5.79x | 58.1/70.8/75.6% | 4.1/11.5% | 3 |

> warm-num-nodes=0: decode_failures 93

> warm-num-nodes=25: decode_failures 93

> warm-num-nodes=100: decode_failures 93

> warm-num-nodes=2000: decode_failures 93

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.789 | 0.773 | 0.017 | - | - | 0.952 | 0.953 | 0.169 | 1.23x | 18.6/25.3/30.1% | 1.9/4.9% | 3 |
| 0.2 | 1 | 0.714 | 0.681 | 0.032 | - | - | 0.931 | 0.935 | 0.115 | 1.16x | 17.8/24.2/29.1% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.607 | 0.565 | 0.043 | - | - | 0.849 | 0.874 | 0.086 | 1.08x | 16.6/23.0/28.1% | 1.7/4.2% | 3 |

> burst-loss=0.2: decode_failures 6

> burst-loss=0.3: decode_failures 13

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.854 | 0.845 | 0.009 | - | - | 0.959 | 0.960 | 0.155 | 1.38x | 20.5/27.5/32.7% | 2.1/5.3% | 3 |
| 0.2 | 1 | 0.831 | 0.818 | 0.014 | - | - | 0.952 | 0.953 | 0.143 | 1.43x | 21.1/28.7/34.2% | 2.2/5.2% | 3 |
| 0.3 | 1 | 0.794 | 0.774 | 0.020 | - | - | 0.936 | 0.939 | 0.117 | 1.48x | 22.2/29.8/35.8% | 2.3/5.1% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.775 | 0.762 | 0.013 | - | - | 0.918 | 0.945 | 0.139 | 1.24x | 18.8/25.6/30.3% | 1.9/5.2% | 3 |
| 0.2 | 1 | 0.673 | 0.653 | 0.021 | - | - | 0.865 | 0.928 | 0.135 | 1.16x | 17.6/24.4/29.2% | 1.7/4.7% | 3 |
| 0.3 | 1 | 0.566 | 0.534 | 0.031 | - | - | 0.752 | 0.879 | 0.070 | 1.10x | 16.9/23.2/28.5% | 1.6/4.6% | 3 |

> burst-loss=0.1: decode_failures 30

> burst-loss=0.2: decode_failures 43

> burst-loss=0.3: decode_failures 32

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.851 | 0.851 | 0.000 | - | - | 0.952 | 0.953 | 0.163 | 1.75x | 26.1/35.0/41.4% | 2.6/7.3% | 3 |
| directed-with-late-flood | 1 | 0.855 | 0.855 | 0.000 | - | - | 0.957 | 0.958 | 0.165 | 1.58x | 23.6/31.9/38.0% | 2.4/6.7% | 3 |
| m4-early-flood | 1 | 0.858 | 0.858 | 0.000 | - | - | 0.957 | 0.958 | 0.182 | 1.57x | 23.6/31.8/37.7% | 2.4/6.6% | 3 |

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.914 | 0.910 | 0.004 | - | - | 0.991 | 0.991 | 0.524 | 0.76x | 9.8/12.3/13.6% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.893 | 0.888 | 0.005 | - | - | 0.975 | 0.977 | 0.477 | 1.21x | 16.2/22.9/24.0% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.866 | 0.861 | 0.005 | - | - | 0.956 | 0.956 | 0.000 | 1.04x | 14.3/18.8/22.5% | 1.6/4.3% | 3 |
| 0.75 | 1 | 0.879 | 0.869 | 0.009 | - | - | 0.988 | 0.989 | 0.419 | 0.88x | 12.4/16.2/17.0% | 1.4/3.8% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.896 | 0.891 | 0.005 | - | - | 0.976 | 0.977 | 0.457 | 1.22x | 16.5/23.1/24.4% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.871 | 0.866 | 0.005 | - | - | 0.958 | 0.959 | 0.000 | 1.01x | 14.3/18.3/22.0% | 1.5/4.3% | 3 |
| 0.75 | 1 | 0.882 | 0.871 | 0.011 | - | - | 0.991 | 0.992 | 0.460 | 0.86x | 12.4/16.0/17.0% | 1.3/3.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.907 | 0.904 | 0.003 | - | - | 0.985 | 0.987 | 0.230 | 0.68x | 10.7/14.7/17.4% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.916 | 0.913 | 0.003 | - | - | 0.994 | 0.994 | 0.577 | 0.76x | 10.1/13.4/14.9% | 1.2/2.5% | 3 |
| 2.5 | 1 | 0.914 | 0.910 | 0.004 | - | - | 0.994 | 0.995 | 0.607 | 0.76x | 10.1/13.2/14.7% | 1.2/2.3% | 3 |
| 2.6 | 1 | 0.909 | 0.906 | 0.003 | - | - | 0.989 | 0.989 | 0.587 | 0.73x | 9.9/13.2/14.8% | 1.2/2.4% | 3 |
| 2.7 | 1 | 0.919 | 0.916 | 0.002 | - | - | 0.986 | 0.986 | 0.583 | 0.78x | 10.8/15.3/17.5% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.896 | 0.893 | 0.003 | - | - | 0.975 | 0.975 | 0.185 | 0.83x | 12.7/16.9/19.9% | 1.3/3.4% | 3 |
| 900 | 1 | 0.851 | 0.834 | 0.016 | - | - | 0.940 | 0.941 | 0.188 | 2.09x | 31.0/41.5/49.1% | 3.2/8.6% | 3 |
| 300 | 1 | 0.590 | 0.578 | 0.012 | - | - | 0.694 | 0.756 | 0.131 | 4.51x | 59.6/74.1/80.0% | 7.1/16.1% | 3 |

> broadcast-interval-s=300: decode_failures 35

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.851 | 0.851 | 0.001 | - | - | 0.913 | 0.914 | 0.207 | 0.90x | 13.5/17.7/20.6% | 1.3/3.5% | 3 |
| 900 | 1 | 0.819 | 0.816 | 0.003 | - | - | 0.891 | 0.892 | 0.193 | 2.37x | 34.2/45.0/51.7% | 3.6/9.0% | 3 |
| 300 | 1 | 0.552 | 0.544 | 0.008 | - | - | 0.677 | 0.684 | 0.112 | 5.04x | 62.7/76.3/80.8% | 7.6/17.3% | 3 |

> broadcast-interval-s=300: queue drops 13.9% of transmissions - airtime here is measured through a cap

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.899 | 0.895 | 0.004 | - | - | 0.984 | 0.985 | 0.211 | 1.16x | 17.9/23.9/28.3% | 1.8/4.9% | 3 |
| sinusoid | 1 | 0.891 | 0.886 | 0.005 | - | - | 0.975 | 0.976 | 0.203 | 1.15x | 17.4/23.4/27.7% | 1.7/4.8% | 3 |
| commuter | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.851 | 0.834 | 0.016 | - | - | 0.940 | 0.941 | 0.188 | 2.09x | 31.0/41.5/49.1% | 3.2/8.6% | 3 |
| 3600 | 1 | 0.896 | 0.893 | 0.003 | - | - | 0.975 | 0.975 | 0.185 | 0.83x | 12.7/16.9/19.9% | 1.3/3.4% | 3 |
| 10800 | 1 | 0.907 | 0.905 | 0.002 | - | - | 0.989 | 0.989 | 0.177 | 0.58x | 8.8/11.6/13.6% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.912 | 0.910 | 0.001 | - | - | 0.991 | 0.991 | 0.208 | 0.39x | 5.9/7.8/9.1% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.882 | 0.873 | 0.008 | - | - | 0.965 | 0.968 | 0.194 | 1.38x | 20.9/28.0/33.0% | 2.1/5.7% | 3 |
| 1.0 | 1 | 0.870 | 0.862 | 0.008 | - | - | 0.957 | 0.959 | 0.199 | 1.50x | 22.4/30.4/36.0% | 2.3/6.3% | 3 |
| 4.0 | 1 | 0.853 | 0.837 | 0.016 | - | - | 0.949 | 0.949 | 0.162 | 1.90x | 28.4/39.0/46.6% | 2.8/8.2% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.756 | 0.743 | 0.013 | - | - | 0.887 | 0.930 | 0.475 | 5.79x | 58.1/70.8/75.6% | 4.1/11.5% | 3 |
| 1.0 | 1 | 0.677 | 0.668 | 0.009 | - | - | 0.803 | 0.881 | 0.417 | 6.49x | 62.0/73.7/78.2% | 4.7/12.7% | 3 |

> traceroute-per-hour=0.0: decode_failures 93

> traceroute-per-hour=1.0: queue drops 14.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 98

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.820 | 0.806 | 0.014 | - | - | 0.928 | 0.937 | 0.238 | 1.46x | 22.9/34.6/39.8% | 3.4/7.8% | 3 |
| 60 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 90 | 1 | 0.934 | 0.931 | 0.003 | - | - | 0.985 | 0.986 | 0.638 | 1.64x | 19.4/26.6/28.5% | 1.5/5.2% | 3 |
| 120 | 1 | 0.957 | 0.954 | 0.003 | - | - | 0.996 | 0.996 | 0.769 | 1.97x | 22.0/30.3/34.1% | 1.3/5.1% | 3 |
| 150 | 1 | 0.951 | 0.948 | 0.003 | - | - | 0.999 | 0.999 | 0.549 | 2.57x | 27.7/37.2/43.5% | 1.3/5.5% | 3 |

> nodes=40: decode_failures 2

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 120 | 1 | 0.790 | 0.778 | 0.012 | - | - | 0.966 | 0.967 | 0.160 | 2.24x | 16.2/23.8/27.2% | 1.6/5.7% | 3 |
| 250 | 1 | 0.533 | 0.526 | 0.007 | - | - | 0.734 | 0.734 | 0.134 | 4.93x | 16.5/28.5/41.5% | 1.7/6.1% | 3 |
| 500 | 1 | 0.313 | 0.308 | 0.005 | - | - | 0.508 | 0.566 | 0.107 | 9.86x | 18.5/29.3/41.7% | 1.7/6.3% | 3 |

> nodes=500: decode_failures 217

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.792 | 0.777 | 0.015 | - | - | 0.962 | 0.963 | 0.185 | 2.12x | 15.5/22.2/25.5% | 1.5/5.3% | 3 |
| 250 | 1 | 0.531 | 0.524 | 0.007 | - | - | 0.723 | 0.724 | 0.124 | 4.61x | 15.3/26.4/38.0% | 1.5/5.5% | 3 |
| 500 | 1 | 0.311 | 0.306 | 0.005 | - | - | 0.494 | 0.557 | 0.110 | 9.32x | 17.7/27.2/40.3% | 1.6/5.8% | 3 |

> nodes=500: decode_failures 131

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.856 | 0.852 | 0.003 | - | - | 0.946 | 0.948 | 0.200 | 1.27x | 19.3/25.9/30.5% | 1.9/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.772 | 0.768 | 0.004 | - | - | 0.893 | 0.893 | 0.174 | 1.12x | 17.6/24.4/31.2% | 1.8/5.4% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.863 | 0.858 | 0.005 | - | - | 0.942 | 0.945 | 0.191 | 1.31x | 19.9/26.3/30.6% | 1.9/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.784 | 0.781 | 0.004 | - | - | 0.873 | 0.874 | 0.199 | 1.28x | 20.1/27.5/35.0% | 2.1/5.3% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.05 | 1 | 0.894 | 0.887 | 0.007 | - | - | 0.956 | 0.958 | 0.230 | 1.44x | 21.5/30.2/35.7% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.906 | 0.898 | 0.008 | - | - | 0.978 | 0.979 | 0.203 | 1.60x | 22.6/32.9/41.1% | 2.2/5.4% | 3 |
| 0.2 | 1 | 0.909 | 0.901 | 0.007 | - | - | 0.979 | 0.979 | 0.189 | 1.76x | 26.7/36.6/42.8% | 2.4/5.4% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| local-typical | 1 | 0.519 | 0.516 | 0.003 | - | - | 0.700 | 0.701 | 0.000 | 1.42x | 15.5/27.8/30.8% | 2.3/5.5% | 3 |
| event | 1 | 0.304 | 0.295 | 0.009 | - | - | 0.469 | 0.469 | 0.000 | 1.38x | 8.6/18.7/27.2% | 2.1/5.1% | 3 |
| backbone | 1 | 0.943 | 0.942 | 0.000 | - | - | 0.992 | 0.992 | 0.165 | 1.13x | 27.6/36.4/39.1% | 1.3/5.5% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.857 | 0.833 | 0.025 | - | - | 0.946 | 0.952 | 0.640 | 1.52x | 28.1/36.7/40.9% | 3.6/7.8% | 3 |
| 60 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 90 | 1 | 0.841 | 0.837 | 0.004 | - | - | 0.964 | 0.965 | 0.000 | 1.75x | 16.4/25.2/29.2% | 1.7/5.4% | 3 |
| 120 | 1 | 0.790 | 0.778 | 0.012 | - | - | 0.966 | 0.967 | 0.160 | 2.24x | 16.2/23.8/27.2% | 1.6/5.7% | 3 |
| 150 | 1 | 0.698 | 0.686 | 0.012 | - | - | 0.892 | 0.893 | 0.136 | 2.81x | 16.1/28.3/37.7% | 1.6/5.4% | 3 |

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 1.25 | 1 | 0.742 | 0.734 | 0.008 | - | - | 0.944 | 0.948 | 0.000 | 1.37x | 15.2/21.0/26.4% | 2.1/5.5% | 3 |
| 1.5 | 1 | 0.593 | 0.571 | 0.022 | - | - | 0.818 | 0.859 | 0.000 | 1.41x | 11.6/19.1/21.5% | 2.0/5.5% | 3 |
| 2.0 | 1 | 0.162 | 0.159 | 0.003 | - | - | 0.210 | 0.213 | 0.000 | 1.04x | 6.0/10.8/15.3% | 1.6/3.5% | 3 |

> stretch=1.5: decode_failures 34

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| clustered | 1 | 0.729 | 0.729 | 0.000 | - | - | 0.843 | 0.844 | 0.274 | 1.04x | 24.4/33.5/34.8% | 1.5/5.1% | 3 |
| corridor | 1 | 0.600 | 0.593 | 0.007 | - | - | 0.620 | 0.624 | 0.243 | 1.18x | 15.7/19.4/23.6% | 1.7/4.7% | 3 |
| hub | 1 | 0.944 | 0.943 | 0.001 | - | - | 0.990 | 0.991 | 0.721 | 1.22x | 27.9/35.6/37.5% | 1.7/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.855 | 0.855 | 0.000 | - | - | 0.957 | 0.958 | 0.165 | 1.58x | 23.6/31.9/38.0% | 2.4/6.7% | 3 |
| True | 1 | 0.862 | 0.862 | 0.000 | - | - | 0.963 | 0.967 | 0.178 | 1.58x | 23.4/32.0/38.0% | 2.4/6.7% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.862 | 0.862 | 0.000 | - | - | 0.963 | 0.967 | 0.178 | 1.58x | 23.4/32.0/38.0% | 2.4/6.7% | 3 |
| m4-early-flood | 1 | 0.855 | 0.855 | 0.000 | - | - | 0.953 | 0.955 | 0.179 | 1.61x | 23.8/32.5/38.6% | 2.4/6.9% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.883 | 0.883 | 0.000 | - | - | 0 | 0.000 | 0.177 | 1.28x | 19.1/25.8/30.5% | 1.9/5.3% | 3 |
| chain | 1 | 0.871 | 0.867 | 0.004 | - | - | 0.936 | 0.963 | 0.171 | 1.49x | 22.6/30.3/35.4% | 2.3/6.2% | 3 |
| sr | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| True | 1 | 0.888 | 0.880 | 0.007 | - | - | 0.969 | 0.973 | 0.199 | 1.33x | 19.9/26.7/31.4% | 2.0/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.957 | 0.954 | 0.003 | - | - | 0.996 | 0.996 | 0.769 | 1.97x | 22.0/30.3/34.1% | 1.3/5.1% | 3 |
| True | 1 | 0.958 | 0.954 | 0.003 | - | - | 0.996 | 0.996 | 0.761 | 1.97x | 22.0/29.7/33.5% | 1.3/5.0% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.303 | 0.300 | 0.004 | - | - | 0.256 | 0.260 | 0.000 | 0.07x | 0.4/0.8/1.4% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.652 | 0.647 | 0.005 | - | - | 0.929 | 0.929 | 0.000 | 0.33x | 2.8/5.4/6.3% | 0.5/1.5% | 3 |
| LONG_TURBO | 1 | 0.839 | 0.833 | 0.006 | - | - | 0.978 | 0.978 | 0.000 | 1.33x | 15.2/22.7/25.8% | 2.0/5.3% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.893 | 0.887 | 0.006 | - | - | 0.972 | 0.974 | 0.273 | 1.28x | 20.8/27.9/32.2% | 1.8/5.5% | 3 |
| 1.0 | 1 | 0.926 | 0.921 | 0.005 | - | - | 0.981 | 0.982 | 0.527 | 1.09x | 23.1/29.8/33.2% | 1.4/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.502 | 0.487 | 0.015 | - | - | 0.887 | 0.913 | 0.000 | 0.17x | 1.3/2.3/3.5% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| LITE_FAST | 1 | 0.867 | 0.859 | 0.008 | - | - | 0.976 | 0.976 | 0.000 | 0.99x | 13.1/19.3/21.5% | 1.5/4.2% | 3 |
| NARROW_SLOW | 1 | 0.869 | 0.861 | 0.008 | - | - | 0.964 | 0.966 | 0.000 | 1.24x | 16.5/24.1/27.0% | 1.9/5.4% | 3 |

> preset=SHORT_FAST: decode_failures 33

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| temporal | 1 | 0.824 | 0.811 | 0.013 | - | - | 0.941 | 0.945 | 0.036 | 1.31x | 18.6/26.2/30.6% | 2.0/5.4% | 3 |
| transient | 1 | 0.880 | 0.873 | 0.007 | - | - | 0.968 | 0.970 | 0.167 | 1.31x | 19.6/26.3/31.1% | 2.0/5.4% | 3 |
| periodic | 1 | 0.711 | 0.703 | 0.008 | - | - | 0.796 | 0.802 | 0.128 | 1.20x | 18.0/24.5/29.1% | 1.8/4.7% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.502 | 0.487 | 0.015 | - | - | 0.887 | 0.913 | 0.000 | 0.17x | 1.3/2.3/3.5% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| LONG_MODERATE | 1 | 0.846 | 0.835 | 0.011 | - | - | 0.941 | 0.965 | 0.277 | 3.38x | 52.8/62.2/66.4% | 4.4/13.6% | 3 |

> preset=SHORT_FAST: decode_failures 33

> preset=LONG_MODERATE: decode_failures 49

> slower: 7.1 s per simulated hour against 3.01 over 22 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.104 | 0.104 | 0.000 | - | - | 0.351 | 0.351 | 0.000 | 0.01x | 0.1/0.1/0.2% | 0.0/0.1% | 3 |
| SHORT_TURBO | 1 | 0.303 | 0.300 | 0.004 | - | - | 0.256 | 0.260 | 0.000 | 0.07x | 0.4/0.8/1.4% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| LONG_TURBO | 1 | 0.839 | 0.833 | 0.006 | - | - | 0.978 | 0.978 | 0.000 | 1.33x | 15.2/22.7/25.8% | 2.0/5.3% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.874 | 0.862 | 0.012 | - | - | 0.962 | 0.964 | 0.000 | 1.82x | 25.6/34.1/38.1% | 2.7/7.2% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.819 | 0.813 | 0.006 | - | - | 0.903 | 0.904 | 0.178 | 1.26x | 19.2/25.8/30.5% | 1.9/5.2% | 3 |
| 10000 | 1 | 0.711 | 0.703 | 0.008 | - | - | 0.796 | 0.802 | 0.128 | 1.20x | 18.0/24.5/29.1% | 1.8/4.7% | 3 |
| 4000 | 1 | 0.493 | 0.485 | 0.008 | - | - | 0.554 | 0.595 | 0.076 | 1.05x | 15.7/21.7/26.3% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.123 | 0.123 | 0.000 | - | - | 0.125 | 0.210 | 0.015 | 0.73x | 10.6/15.7/20.3% | 1.1/2.2% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 8

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.593 | 0.571 | 0.022 | - | - | 0.818 | 0.859 | 0.000 | 1.41x | 11.6/19.1/21.5% | 2.0/5.5% | 3 |
| 1.0 | 1 | 0.794 | 0.763 | 0.030 | - | - | 0.926 | 0.928 | 0.355 | 1.17x | 15.4/22.0/25.7% | 1.7/5.2% | 3 |

> duct-per-hour=0.0: decode_failures 34

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 22 | 1 | 0.564 | 0.553 | 0.011 | - | - | 0.858 | 0.860 | 0.000 | 1.43x | 11.8/21.4/24.3% | 2.1/6.1% | 3 |
| 17 | 1 | 0.257 | 0.255 | 0.002 | - | - | 0.184 | 0.189 | 0.000 | 1.30x | 8.0/14.0/19.3% | 2.2/5.1% | 3 |
| 14 | 1 | 0.149 | 0.148 | 0.001 | - | - | 0.126 | 0.134 | 0.000 | 0.95x | 4.6/9.7/12.2% | 1.5/4.0% | 3 |

> tx-power=14: decode_failures 5

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.957 | 0.954 | 0.003 | - | - | 0.996 | 0.996 | 0.769 | 1.97x | 22.0/30.3/34.1% | 1.3/5.1% | 3 |
| True | 1 | 0.952 | 0.947 | 0.005 | - | - | 0.996 | 0.996 | 0.738 | 2.37x | 26.0/34.5/38.5% | 1.5/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.897 | 0.890 | 0.007 | - | - | 0.966 | 0.969 | 0.208 | 1.40x | 20.8/28.5/33.9% | 2.0/5.4% | 3 |
| True | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.968 | 0.970 | 0.234 | 1.49x | 21.9/29.2/34.5% | 2.2/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| random | 1 | 0.822 | 0.807 | 0.015 | - | - | 0.934 | 0.936 | 0.158 | 1.23x | 18.6/25.2/30.1% | 1.8/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.739 | 0.718 | 0.021 | - | - | 0.896 | 0.898 | 0.095 | 0.99x | 16.0/22.4/27.5% | 1.4/4.9% | 3 |
| 7 | 1 | 0.849 | 0.848 | 0.001 | - | - | 0.915 | 0.915 | 0.210 | 1.39x | 20.8/27.3/31.8% | 2.1/5.4% | 3 |
| 15 | 1 | 0.855 | 0.855 | 0.000 | - | - | 0.912 | 0.912 | 0.216 | 1.40x | 20.8/27.5/32.0% | 2.1/5.5% | 3 |
| 32 | 1 | 0.855 | 0.855 | 0.000 | - | - | 0.912 | 0.912 | 0.216 | 1.40x | 20.8/27.5/32.0% | 2.1/5.5% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.739 | 0.718 | 0.021 | - | - | 0.896 | 0.898 | 0.095 | 0.99x | 16.0/22.4/27.5% | 1.4/4.9% | 3 |
| 5 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.915 | 0.916 | 0.181 | 1.29x | 19.8/26.6/31.3% | 2.0/5.4% | 3 |
| 7 | 1 | 0.849 | 0.848 | 0.001 | - | - | 0.915 | 0.915 | 0.210 | 1.39x | 20.8/27.3/31.8% | 2.1/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.875 | 0.875 | 0.000 | - | - | 0.918 | 0.968 | 0.172 | 1.29x | 19.2/26.1/30.7% | 2.0/5.4% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.739 | 0.718 | 0.021 | - | - | 0.896 | 0.898 | 0.095 | 0.99x | 16.0/22.4/27.5% | 1.4/4.9% | 3 |
| True | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| BALANCED | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| STRICT | 1 | 0.744 | 0.744 | 0.000 | - | - | 0.831 | 0.834 | 0.069 | 1.37x | 20.6/27.4/32.2% | 2.1/5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| dm | 1 | 0.882 | 0.873 | 0.009 | - | - | 0.966 | 0.968 | 0.191 | 1.28x | 19.5/26.1/30.7% | 2.0/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.888 | 0.880 | 0.007 | - | - | 0.967 | 0.970 | 0.190 | 1.30x | 19.8/26.4/31.0% | 2.0/5.3% | 3 |
| local | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| time | 1 | 0.878 | 0.872 | 0.007 | - | - | 0.958 | 0.960 | 0.184 | 1.35x | 20.5/27.3/32.2% | 2.1/5.6% | 3 |
| window | 1 | 0.889 | 0.883 | 0.005 | - | - | 0.974 | 0.975 | 0.183 | 1.28x | 19.3/25.9/30.5% | 1.9/5.3% | 3 |

> bucket-mode=global: misdecodes 60

> bucket-mode=time: misdecodes 40

> bucket-mode=window: misdecodes 41

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.883 | 0.875 | 0.008 | - | - | 0.973 | 0.974 | 0.180 | 1.47x | 22.3/29.6/34.4% | 2.2/6.1% | 3 |
| 1800 | 1 | 0.878 | 0.872 | 0.007 | - | - | 0.958 | 0.960 | 0.184 | 1.35x | 20.5/27.3/32.2% | 2.1/5.6% | 3 |
| 3600 | 1 | 0.886 | 0.880 | 0.006 | - | - | 0.972 | 0.975 | 0.181 | 1.31x | 19.7/26.5/31.2% | 2.0/5.4% | 3 |

> time-bucket-s=600: misdecodes 116

> time-bucket-s=1800: misdecodes 40

> time-bucket-s=3600: misdecodes 13

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| interval | 1 | 0.863 | 0.851 | 0.012 | - | - | 0.952 | 0.959 | 0.185 | 1.77x | 26.7/35.6/41.7% | 2.6/7.6% | 3 |
| aimd | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.936 | 0.975 | 0.165 | 1.30x | 19.6/26.4/31.2% | 2.0/5.4% | 3 |
| bucket+interval | 1 | 0.871 | 0.861 | 0.010 | - | - | 0.954 | 0.954 | 0.189 | 1.80x | 27.0/36.1/42.5% | 2.7/8.0% | 3 |

> trigger=interval: misdecodes 24

> trigger=aimd: misdecodes 7

> trigger=aimd: decode_failures 4

> trigger=bucket+interval: misdecodes 34

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.881 | 0.873 | 0.008 | - | - | 0.967 | 0.970 | 0.204 | 1.28x | 19.5/26.0/30.9% | 1.9/5.4% | 3 |
| 8 | 1 | 0.883 | 0.877 | 0.006 | - | - | 0.963 | 0.964 | 0.185 | 1.30x | 19.6/26.3/31.1% | 2.0/5.4% | 3 |
| 16 | 1 | 0.882 | 0.874 | 0.007 | - | - | 0.968 | 0.970 | 0.190 | 1.31x | 19.6/26.3/31.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 50 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.190 | 1.31x | 19.6/26.4/31.2% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 70

> capacity=8: decode_failures 5

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.881 | 0.873 | 0.008 | - | - | 0.967 | 0.970 | 0.204 | 1.28x | 19.5/26.0/30.9% | 1.9/5.4% | 3 |
| 8 | 1 | 0.883 | 0.877 | 0.006 | - | - | 0.963 | 0.964 | 0.185 | 1.30x | 19.6/26.3/31.1% | 2.0/5.4% | 3 |
| 16 | 1 | 0.882 | 0.874 | 0.007 | - | - | 0.968 | 0.970 | 0.190 | 1.31x | 19.6/26.3/31.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 50 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.190 | 1.31x | 19.6/26.4/31.2% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 70

> capacity=8: decode_failures 5

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.882 | 0.875 | 0.007 | - | - | 0.962 | 0.971 | 0.185 | 1.29x | 19.4/26.1/30.9% | 1.9/5.4% | 3 |
| 16 | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.965 | 0.967 | 0.169 | 1.29x | 19.5/26.1/30.9% | 2.0/5.3% | 3 |
| 32 | 1 | 0.889 | 0.883 | 0.005 | - | - | 0.974 | 0.975 | 0.183 | 1.28x | 19.3/25.9/30.5% | 1.9/5.3% | 3 |

> capacity=8: misdecodes 32

> capacity=8: decode_failures 17

> capacity=16: misdecodes 31

> capacity=32: misdecodes 41

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.871 | 0.861 | 0.010 | - | - | 0.954 | 0.954 | 0.189 | 1.80x | 27.0/36.1/42.5% | 2.7/8.0% | 3 |
| 02-06 | 1 | 0.887 | 0.883 | 0.004 | - | - | 0.955 | 0.979 | 0.215 | 1.33x | 20.3/27.0/31.7% | 2.0/5.5% | 3 |
| 00-08 | 1 | 0.882 | 0.877 | 0.005 | - | - | 0.952 | 0.970 | 0.213 | 1.41x | 21.6/28.4/33.7% | 2.1/5.9% | 3 |

> catch-up-hours=: misdecodes 34

> catch-up-hours=02-06: misdecodes 1

> catch-up-hours=02-06: decode_failures 45

> catch-up-hours=00-08: misdecodes 2

> catch-up-hours=00-08: decode_failures 44

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.879 | 0.878 | 0.001 | - | - | 0.986 | 0.986 | 0.197 | 1.31x | 19.6/26.4/31.2% | 2.0/5.4% | 3 |
| 2 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 3 | 1 | 0.889 | 0.879 | 0.009 | - | - | 0.985 | 0.986 | 0.216 | 1.30x | 19.4/26.1/30.8% | 2.0/5.3% | 3 |
| 4 | 1 | 0.895 | 0.882 | 0.013 | - | - | 0.983 | 0.984 | 0.220 | 1.32x | 19.8/26.6/31.4% | 2.0/5.4% | 3 |

> faster: 1.6 s per simulated hour against 3.45 over 22 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.879 | 0.878 | 0.001 | - | - | 0.986 | 0.986 | 0.197 | 1.31x | 19.6/26.4/31.2% | 2.0/5.4% | 3 |
| 2 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 3 | 1 | 0.889 | 0.879 | 0.009 | - | - | 0.985 | 0.986 | 0.216 | 1.30x | 19.4/26.1/30.8% | 2.0/5.3% | 3 |
| 4 | 1 | 0.895 | 0.882 | 0.013 | - | - | 0.983 | 0.984 | 0.220 | 1.32x | 19.8/26.6/31.4% | 2.0/5.4% | 3 |
| 5 | 1 | 0.895 | 0.882 | 0.013 | - | - | 0.983 | 0.984 | 0.220 | 1.32x | 19.8/26.6/31.4% | 2.0/5.4% | 3 |

> faster: 1.55 s per simulated hour against 4.56 over 22 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.882 | 0.874 | 0.008 | - | - | 0.964 | 0.966 | 0.185 | 1.29x | 19.2/25.8/30.5% | 1.9/5.3% | 3 |
| 30 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 120 | 1 | 0.878 | 0.871 | 0.008 | - | - | 0.963 | 0.965 | 0.196 | 1.32x | 19.8/26.5/31.3% | 2.0/5.4% | 3 |
| 600 | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.967 | 0.968 | 0.171 | 1.31x | 19.7/26.4/31.1% | 2.0/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.882 | 0.874 | 0.008 | - | - | 0.964 | 0.966 | 0.185 | 1.29x | 19.2/25.8/30.5% | 1.9/5.3% | 3 |
| 30 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 120 | 1 | 0.878 | 0.871 | 0.008 | - | - | 0.963 | 0.965 | 0.196 | 1.32x | 19.8/26.5/31.3% | 2.0/5.4% | 3 |
| 600 | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.967 | 0.968 | 0.171 | 1.31x | 19.7/26.4/31.1% | 2.0/5.4% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.874 | 0.871 | 0.002 | - | - | 0.510 | 0.879 | 0.160 | 1.29x | 19.4/26.0/30.8% | 1.9/5.5% | 3 |
| routers | 1 | 0.881 | 0.878 | 0.004 | - | - | 0.985 | 0.986 | 0.196 | 1.30x | 19.6/26.4/31.1% | 2.0/5.5% | 3 |
| alternate-routers | 1 | 0.877 | 0.875 | 0.002 | - | - | 0.982 | 0.982 | 0.185 | 1.30x | 19.4/26.2/31.0% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.984 | 0.985 | 0.194 | 1.31x | 19.4/26.6/31.3% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.880 | 0.861 | 0.020 | - | - | 0.971 | 0.974 | 0.191 | 1.32x | 19.5/26.4/31.1% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

> place=spread: decode_failures 4

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.874 | 0.871 | 0.002 | - | - | 0.510 | 0.879 | 0.160 | 1.29x | 19.4/26.0/30.8% | 1.9/5.5% | 3 |
| routers | 1 | 0.881 | 0.878 | 0.004 | - | - | 0.985 | 0.986 | 0.196 | 1.30x | 19.6/26.4/31.1% | 2.0/5.5% | 3 |
| alternate-routers | 1 | 0.877 | 0.875 | 0.002 | - | - | 0.982 | 0.982 | 0.185 | 1.30x | 19.4/26.2/31.0% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.984 | 0.985 | 0.194 | 1.31x | 19.4/26.6/31.3% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.880 | 0.861 | 0.020 | - | - | 0.971 | 0.974 | 0.191 | 1.32x | 19.5/26.4/31.1% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

> place=spread: decode_failures 4

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| broadcast | 1 | 0.899 | 0.878 | 0.021 | - | - | 0.970 | 0.972 | 0.209 | 1.39x | 20.7/27.7/32.4% | 2.1/5.7% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| heard | 1 | 0.881 | 0.874 | 0.008 | - | - | 0.969 | 0.971 | 0.191 | 1.29x | 19.5/26.1/30.8% | 1.9/5.3% | 3 |

> replay-ordering=heard: misdecodes 26

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.899 | 0.878 | 0.021 | - | - | 0.970 | 0.972 | 0.209 | 1.39x | 20.7/27.7/32.4% | 2.1/5.7% | 3 |
| heard | 1 | 0.893 | 0.869 | 0.025 | - | - | 0.966 | 0.968 | 0.224 | 1.40x | 21.0/28.0/32.9% | 2.1/5.7% | 3 |

> replay-ordering=heard: misdecodes 16

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| enum | 1 | 0.882 | 0.873 | 0.009 | - | - | 0.966 | 0.968 | 0.174 | 1.30x | 20.0/26.6/31.3% | 2.0/5.5% | 3 |
| hybrid | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.881 | 0.878 | 0.004 | - | - | 0.985 | 0.986 | 0.196 | 1.30x | 19.6/26.4/31.1% | 2.0/5.5% | 3 |
| 6 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.983 | 0.984 | 0.206 | 1.36x | 20.6/27.6/32.4% | 2.1/5.8% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.880 | 0.873 | 0.007 | - | - | 0.961 | 0.963 | 0.196 | 1.30x | 19.4/26.1/30.8% | 1.9/5.3% | 2 |
| 3 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 5 | 1 | 0.882 | 0.873 | 0.009 | - | - | 0.963 | 0.966 | 0.175 | 1.32x | 20.1/26.8/31.5% | 2.0/5.5% | 5 |
| 8 | 1 | 0.883 | 0.867 | 0.016 | - | - | 0.981 | 0.981 | 0.181 | 1.39x | 21.1/27.9/32.7% | 2.1/5.7% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.880 | 0.873 | 0.007 | - | - | 0.961 | 0.963 | 0.196 | 1.30x | 19.4/26.1/30.8% | 1.9/5.3% | 2 |
| 3 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 5 | 1 | 0.882 | 0.873 | 0.009 | - | - | 0.963 | 0.966 | 0.175 | 1.32x | 20.1/26.8/31.5% | 2.0/5.5% | 5 |
| 8 | 1 | 0.883 | 0.867 | 0.016 | - | - | 0.981 | 0.981 | 0.181 | 1.39x | 21.1/27.9/32.7% | 2.1/5.7% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| True | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.891 | 0.885 | 0.006 | - | - | 0.972 | 0.976 | 0.196 | 1.20x | 18.1/24.2/28.7% | 1.8/4.9% | 3 |
| 1 | 1 | 0.887 | 0.879 | 0.008 | - | - | 0.966 | 0.969 | 0.207 | 1.17x | 17.6/23.9/28.3% | 1.8/4.9% | 3 |
| 2 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.964 | 0.966 | 0.162 | 1.17x | 17.6/23.8/28.3% | 1.8/4.9% | 3 |
| 4 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.960 | 0.962 | 0.188 | 1.19x | 17.9/24.2/28.8% | 1.8/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.884 | 0.876 | 0.008 | - | - | 0.972 | 0.975 | 0.182 | 1.29x | 19.4/26.1/30.7% | 1.9/5.3% | 3 |
| 24 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.962 | 0.964 | 0.205 | 1.30x | 19.6/26.2/31.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.968 | 0.970 | 0.184 | 1.31x | 19.7/26.4/31.2% | 1.9/5.4% | 3 |
| 64 | 1 | 0.878 | 0.870 | 0.008 | - | - | 0.963 | 0.965 | 0.178 | 1.30x | 19.5/26.1/30.9% | 2.0/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.884 | 0.875 | 0.008 | - | - | 0.971 | 0.971 | 0.174 | 1.40x | 21.0/28.0/32.9% | 2.1/5.7% | 3 |
| 16 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.967 | 0.968 | 0.173 | 1.34x | 20.2/26.9/31.6% | 2.0/5.5% | 3 |
| 32 | 1 | 0.889 | 0.883 | 0.005 | - | - | 0.974 | 0.975 | 0.183 | 1.28x | 19.3/25.9/30.5% | 1.9/5.3% | 3 |

> window-size=8: misdecodes 111

> window-size=16: misdecodes 59

> window-size=32: misdecodes 41

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.957 | 0.954 | 0.003 | - | - | 0.996 | 0.996 | 0.769 | 1.97x | 22.0/30.3/34.1% | 1.3/5.1% | 3 |
| True | 1 | 0.758 | 0.742 | 0.016 | - | - | 0.903 | 0.935 | 0.471 | 5.87x | 58.4/71.2/76.0% | 4.2/11.7% | 3 |

> no-congestion-scaling=True: decode_failures 115

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.531 | 0.524 | 0.007 | - | - | 0.723 | 0.724 | 0.124 | 4.61x | 15.3/26.4/38.0% | 1.5/5.5% | 3 |
| truesize | 1 | 0.565 | 0.557 | 0.007 | - | - | 0.759 | 0.760 | 0.129 | 3.53x | 11.9/20.9/31.7% | 1.1/4.8% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.960 | 0.957 | 0.003 | - | - | 0.996 | 0.997 | 0.765 | 1.84x | 20.6/27.9/31.3% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.957 | 0.954 | 0.003 | - | - | 0.996 | 0.996 | 0.769 | 1.97x | 22.0/30.3/34.1% | 1.3/5.1% | 3 |

