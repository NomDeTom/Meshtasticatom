# Sweep blocks-2026-10-29-3640454

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 3640454 · seeds 3640454
- **blocks** 87 run
- **compute** 9.2 h of simulator time across every cell
- **generated** 2026-10-29T09:50:54+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>76 warnings</summary>

- AD-siting: siting-mix=basement-heavy: decode_failures 7
- BL-control: protocol=sr: decode_failures 13
- DB-hotstore-stress: max-num-nodes=10: decode_failures 15
- DB-warm: warm-num-nodes=0: decode_failures 87
- DB-warm: warm-num-nodes=25: decode_failures 87
- DB-warm: warm-num-nodes=100: decode_failures 87
- DB-warm: warm-num-nodes=2000: decode_failures 87
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 14
- DG-burst: burst-loss=0.3: decode_failures 31
- DG-loss: extra-loss=0.3: decode_failures 2
- DG-outage: burst-loss=0.1: decode_failures 8
- DG-outage: burst-loss=0.2: decode_failures 38
- DG-outage: burst-loss=0.3: decode_failures 25
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 1
- FW-mixed: legacy-fraction=0.25: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 9
- LD-chatty: broadcast-interval-s=300: decode_failures 19
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 87
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 13.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 85
- MS-hopscale: nodes=500: decode_failures 107
- MS-oversubscribed: nodes=500: decode_failures 70
- MS-stretch: stretch=1.25: decode_failures 6
- MS-stretch: stretch=1.5: decode_failures 3
- MS-topology: topology=corridor: decode_failures 2
- PR-crladder: coding-rate-ladder=False: decode_failures 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 6
- RF-eu-presets: preset=SHORT_FAST: decode_failures 8
- RF-noise: noise-profile=periodic: decode_failures 2
- RF-preset: preset=SHORT_FAST: decode_failures 8
- RF-preset: preset=LONG_MODERATE: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 3
- RF-txpower: tx-power=22: decode_failures 4
- RF-txpower: tx-power=14: decode_failures 1
- RT-hoplimit: hop-limit=3: decode_failures 1
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 24
- SF-bucket-mode: bucket-mode=time: misdecodes 19
- SF-bucket-mode: bucket-mode=window: misdecodes 18
- SF-bucket-time: time-bucket-s=600: misdecodes 102
- SF-bucket-time: time-bucket-s=1800: misdecodes 19
- SF-bucket-time: time-bucket-s=3600: misdecodes 10
- SF-cadence: trigger=interval: misdecodes 4
- SF-cadence: trigger=interval: decode_failures 4
- SF-cadence: trigger=aimd: decode_failures 1
- SF-cadence: trigger=bucket+interval: misdecodes 6
- SF-capacity-local: capacity=4: decode_failures 101
- SF-capacity-local: capacity=8: decode_failures 36
- SF-capacity-local: capacity=16: decode_failures 2
- SF-capacity: capacity=4: decode_failures 101
- SF-capacity: capacity=8: decode_failures 36
- SF-capacity: capacity=16: decode_failures 2
- SF-capacity-window: capacity=8: misdecodes 9
- SF-capacity-window: capacity=8: decode_failures 60
- SF-capacity-window: capacity=16: misdecodes 23
- SF-capacity-window: capacity=32: misdecodes 18
- SF-catchup: catch-up-hours=: misdecodes 6
- SF-catchup: catch-up-hours=02-06: decode_failures 40
- SF-catchup: catch-up-hours=00-08: decode_failures 39
- SF-hops-flat: hops-apart=3: decode_failures 13
- SF-hops-spread: hops-apart=3: decode_failures 13
- SF-hops-spread: faster: 1.66 s per simulated hour against 4.52 over 69 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-jitter-global: advert-jitter-s=1: misdecodes 1
- SF-jitter-local: advert-jitter-s=1: misdecodes 1
- SF-place-flat: place=spread: decode_failures 1
- SF-place-spread: place=spread: decode_failures 1
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 16
- SF-window-size: window-size=8: misdecodes 129
- SF-window-size: window-size=16: misdecodes 51
- SF-window-size: window-size=32: misdecodes 18
- TH-congestion: no-congestion-scaling=True: decode_failures 81

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-servers-spread` | 1.45 | 2.21 | 0.66x | 69 |
| `LD-chatty` | 2.96 | 4.58 | 0.65x | 69 |
| `DM-mode` | 1.89 | 3.06 | 0.62x | 69 |
| `TH-congestion-input` | 6.16 | 10.3 | 0.60x | 69 |
| `SF-place-spread` | 1.63 | 2.79 | 0.58x | 69 |
| `DB-hotstore` | 1.34 | 2.3 | 0.58x | 69 |
| `RF-preset` | 1.57 | 2.77 | 0.57x | 69 |
| `RF-preset-turbo` | 0.846 | 1.53 | 0.55x | 65 |
| `SC-signing` | 0.969 | 1.75 | 0.55x | 69 |
| `SF-capacity` | 0.928 | 1.7 | 0.55x | 69 |
| `SF-hops-spread` | 1.66 | 4.52 | 0.37x | 69 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.965 | 0.965 | 0.822 → 0.843 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.962 | 0.962 | 0.838 → 0.843 | 1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.120 → 0.965 | 0.845 | 0.058 → 0.841 | 9x advert_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.131 → 0.967 | 0.836 | 0.044 → 0.841 | 10x sr_bytes | up | 5 |
| `MS-siting` | siting-mix | **text** | 0.144 → 0.975 | 0.831 | 0.144 → 0.974 | 6.6x sr_airtime | up | 4 |
| `MS-stretch` | stretch | **held** | 0.136 → 0.965 | 0.829 | 0.074 → 0.841 | 11x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.099 → 0.919 | 0.820 | 0.089 → 0.788 | 1.6e+02x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.147 → 0.926 | 0.779 | 0.091 → 0.753 | 11x sr_bytes | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.189 → 0.952 | 0.763 | 0.070 → 0.778 | 5.1x advert_bytes | down | 3 |
| `RF-eu-presets` | preset | **held** | 0.287 → 0.968 | 0.681 | 0.222 → 0.841 | 6.1x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.287 → 0.965 | 0.678 | 0.222 → 0.841 | 9.2x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.420 → 0.965 | 0.545 | 0.310 → 0.841 | 8x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.433 → 0.847 | 0.414 | 0.313 → 0.673 | 4.5x bytes_on_air | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.485 → 0.856 | 0.371 | 0.462 → 0.841 | 2.1x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.546 → 0.910 | 0.363 | 0.536 → 0.906 | 1.9x sr_bytes | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.558 → 0.915 | 0.357 | 0.531 → 0.910 | 8.2x sr_airtime | down | 3 |
| `MS-density` | nodes | **text** | 0.606 → 0.959 | 0.353 | 0.591 → 0.957 | 3.9x advert_bytes | up | 5 |
| `DG-burst` | burst-loss | **text** | 0.514 → 0.856 | 0.342 | 0.476 → 0.841 | 2.1x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.345 → 0.683 | 0.338 | 0.340 → 0.676 | 2.7x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.559 → 0.879 | 0.320 | 0.526 → 0.867 | 7.8x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.623 → 0.931 | 0.308 | 0.574 → 0.927 | 2.4x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.623 → 0.894 | 0.271 | 0.574 → 0.886 | 2x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.618 → 0.856 | 0.238 | 0.608 → 0.841 | 3.2x sr_airtime | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.623 → 0.856 | 0.233 | 0.574 → 0.841 | 1.7x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.712 → 0.938 | 0.227 | 0.707 → 0.936 | 5.5x sr_airtime | down | 2 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.410 → 0.602 | 0.192 | 0.305 → 0.488 | 4.9x sr_airtime | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.698 → 0.856 | 0.158 | 0.679 → 0.841 | 1.3x sr_bytes | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.713 → 0.856 | 0.143 | 0.684 → 0.841 | 1.5x sr_bytes | down | 4 |
| `AD-badrouters` | role-placement | **text** | 0.681 → 0.803 | 0.121 | 0.643 → 0.778 | 1.2x sr_bytes | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.803 → 0.913 | 0.111 | 0.778 → 0.908 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.803 → 0.913 | 0.111 | 0.778 → 0.908 | 2.4x bytes_on_air | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.762 → 0.856 | 0.094 | 0.762 → 0.841 | 1.3x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.835 → 0.927 | 0.092 | 0.828 → 0.923 | 1.4x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.856 → 0.946 | 0.090 | 0.841 → 0.942 | 1.2x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.814 → 0.902 | 0.089 | 0.795 → 0.894 | 5.3x sr_airtime | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.801 → 0.887 | 0.086 | 0.777 → 0.876 | 2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.801 → 0.887 | 0.086 | 0.777 → 0.876 | 2x sr_airtime | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.880 → 0.965 | 0.085 | 0.840 → 0.841 | 26x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.900 → 0.981 | 0.081 | 0.839 → 0.843 | 2.8x sr_bytes | down | 6 |
| `SF-place-spread` | place | **held** | 0.900 → 0.981 | 0.081 | 0.839 → 0.843 | 2.8x sr_bytes | down | 6 |
| `RF-duct` | duct-per-hour | **text** | 0.856 → 0.925 | 0.069 | 0.841 → 0.918 | 1.4x sr_bytes | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.896 → 0.965 | 0.069 | 0.838 → 0.846 | 2.8x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.896 → 0.965 | 0.069 | 0.838 → 0.846 | 2.8x sr_bytes | up | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.768 → 0.832 | 0.064 | 0.628 → 0.690 | 1.4x sr_airtime | down | 2 |
| `SF-cadence` | trigger | **held** | 0.907 → 0.965 | 0.058 | 0.816 → 0.846 | 13x advert_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.920 → 0.967 | 0.047 | 0.835 → 0.840 | 3.2x sr_bytes | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.856 → 0.902 | 0.046 | 0.841 → 0.894 | 1.3x bytes_on_air | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.944 → 0.988 | 0.044 | 0.831 → 0.841 | 8.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.944 → 0.988 | 0.044 | 0.831 → 0.841 | 8.4x sr_bytes | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.849 → 0.892 | 0.043 | 0.830 → 0.857 | 2.1x bytes_on_air | down | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.851 → 0.894 | 0.042 | 0.836 → 0.856 | 2x bytes_on_air | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.816 → 0.856 | 0.040 | 0.796 → 0.841 | 1.4x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.856 → 0.894 | 0.038 | 0.841 → 0.885 | 3.2x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.602 → 0.633 | 0.031 | 0.488 → 0.517 | 1.5x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.921 → 0.952 | 0.031 | 0.816 → 0.842 | 9.4x advert_bytes | down | 3 |
| `FW-versions` | profile | **text** | 0.856 → 0.886 | 0.030 | 0.841 → 0.880 | 3.1x bytes_on_air | down | 5 |
| `AD-worst` | role-placement | **text** | 0.783 → 0.812 | 0.029 | 0.768 → 0.801 | 1.1x bytes_on_air | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.935 → 0.960 | 0.025 | 0.838 → 0.846 | 2.4x advert_bytes | up | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.856 → 0.880 | 0.024 | 0.833 → 0.841 | 2.5x sr_airtime | up | 2 |
| `LD-diurnal` | diurnal | **text** | 0.853 → 0.874 | 0.021 | 0.839 → 0.863 | 1.4x sr_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.851 → 0.869 | 0.019 | 0.835 → 0.857 | 1.1x sr_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.947 → 0.965 | 0.018 | 0.833 → 0.841 | 1.1x advert_bytes | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.949 → 0.965 | 0.016 | 0.834 → 0.841 | 5.3x advert_bytes | down | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.948 → 0.963 | 0.015 | 0.806 → 0.812 | 1.2x sr_bytes | up | 2 |
| `MS-roles` | role-mix | **text** | 0.803 → 0.817 | 0.014 | 0.778 → 0.798 | 1.2x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.934 → 0.948 | 0.014 | 0.807 → 0.820 | 1x advert_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.952 → 0.965 | 0.012 | 0.835 → 0.842 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.952 → 0.965 | 0.012 | 0.835 → 0.842 | 1.2x sr_airtime | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.952 → 0.965 | 0.012 | 0.841 → 0.847 | 3.1x advert_bytes | down | 4 |
| `SF-window-size` | window-size | **text** | 0.847 → 0.860 | 0.012 | 0.831 → 0.846 | 4.5x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.926 → 0.938 | 0.012 | 0.924 → 0.936 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.953 → 0.965 | 0.011 | 0.836 → 0.841 | 2.5x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.954 → 0.965 | 0.011 | 0.837 → 0.841 | 1.1x sr_bytes | down | 2 |
| `SF-capacity` | capacity | **held** | 0.954 → 0.965 | 0.011 | 0.837 → 0.847 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.954 → 0.965 | 0.011 | 0.837 → 0.847 | 5.3x advert_bytes | up | 5 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.951 → 0.962 | 0.011 | 0.832 → 0.833 | 1x sr_airtime | up | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.876 → 0.886 | 0.010 | 0.861 → 0.875 | 1.1x sr_bytes | up | 2 |
| `FW-firmware` | profile | **held** | 0.958 → 0.965 | 0.007 | 0.841 → 0.842 | 3x bytes_on_air | up | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.854 → 0.860 | 0.006 | 0.839 → 0.846 | 2.5x advert_bytes | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.805 → 0.811 | 0.006 | 0.805 → 0.811 | 1.3x sr_airtime | down | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.965 → 0.970 | 0.006 | 0.841 → 0.843 | 1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.807 → 0.811 | 0.004 | 0.807 → 0.811 | 1.2x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **held** | 0.961 → 0.965 | 0.003 | 0.841 → 0.841 | 5.7x advert_bytes | = | 3 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.995 → 0.998 | 0.002 | 0.936 → 0.938 | 1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.995 → 0.996 | 0.001 | 0.936 → 0.936 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| sprinkled | 1 | 0.835 | 0.828 | 0.006 | - | - | 0.965 | 0.966 | 0.574 | 1.16x | 13.1/19.6/23.9% | 1.7/4.9% | 3 |
| arms-race | 1 | 0.927 | 0.923 | 0.004 | - | - | 0.987 | 0.987 | 0.706 | 1.14x | 17.7/23.0/27.7% | 1.6/5.1% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.896 | 0.887 | 0.010 | - | - | 0.929 | 0.930 | 0.785 | 1.24x | 16.6/23.5/24.8% | 2.1/4.8% | 3 |
| 0.3 | 1 | 0.946 | 0.942 | 0.004 | - | - | 0.987 | 0.988 | 0.856 | 1.03x | 18.0/23.5/26.8% | 1.4/5.2% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.803 | 0.778 | 0.025 | - | - | 0.952 | 0.956 | 0.625 | 1.14x | 14.1/19.1/20.1% | 2.1/4.4% | 3 |
| inverse | 1 | 0.705 | 0.674 | 0.031 | - | - | 0.911 | 0.915 | 0.407 | 1.10x | 11.6/16.9/20.3% | 1.8/3.9% | 3 |
| random | 1 | 0.681 | 0.643 | 0.039 | - | - | 0.897 | 0.901 | 0.389 | 1.03x | 11.9/16.3/20.8% | 1.7/4.2% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.803 | 0.778 | 0.025 | - | - | 0.952 | 0.956 | 0.625 | 1.14x | 14.1/19.1/20.1% | 2.1/4.4% | 3 |
| all-routers | 1 | 0.913 | 0.908 | 0.005 | - | - | 0.987 | 0.988 | 0.843 | 2.76x | 30.2/35.8/39.0% | 4.4/5.5% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.803 | 0.778 | 0.025 | - | - | 0.952 | 0.956 | 0.625 | 1.14x | 14.1/19.1/20.1% | 2.1/4.4% | 3 |
| no-mute | 1 | 0.810 | 0.788 | 0.022 | - | - | 0.953 | 0.958 | 0.612 | 1.26x | 14.1/20.0/21.0% | 2.1/4.5% | 3 |
| all-routers | 1 | 0.913 | 0.908 | 0.005 | - | - | 0.987 | 0.988 | 0.843 | 2.76x | 30.2/35.8/39.0% | 4.4/5.5% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.803 | 0.778 | 0.025 | - | - | 0.952 | 0.956 | 0.625 | 1.14x | 14.1/19.1/20.1% | 2.1/4.4% | 3 |
| local-typical | 1 | 0.448 | 0.437 | 0.011 | - | - | 0.684 | 0.687 | 0.000 | 1.20x | 8.0/15.7/20.6% | 2.0/4.8% | 3 |
| basement-heavy | 1 | 0.074 | 0.070 | 0.004 | - | - | 0.189 | 0.251 | 0.000 | 0.52x | 0.9/6.8/9.8% | 0.4/2.7% | 3 |

> siting-mix=basement-heavy: decode_failures 7

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.812 | 0.801 | 0.011 | - | - | 0.948 | 0.949 | 0.000 | 2.37x | 15.3/25.5/32.4% | 1.9/5.1% | 3 |
| inverse | 1 | 0.783 | 0.768 | 0.015 | - | - | 0.950 | 0.951 | 0.000 | 2.25x | 13.7/22.6/29.4% | 1.8/3.3% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.843 | 0.843 | 0.000 | - | - | 0 | 0.000 | 0.713 | 1.21x | 14.3/19.3/22.2% | 2.0/4.4% | 3 |
| sr | 1 | 0.872 | 0.838 | 0.035 | - | - | 0.962 | 0.989 | 0.707 | 1.26x | 14.7/19.8/23.1% | 2.0/4.5% | 3 |

> protocol=sr: decode_failures 13

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.801 | 0.777 | 0.024 | - | - | 0.933 | 0.936 | 0.662 | 2.69x | 32.0/43.0/48.9% | 4.5/9.0% | 3 |
| 100 | 1 | 0.887 | 0.876 | 0.011 | - | - | 0.980 | 0.980 | 0.737 | 1.41x | 17.5/23.5/27.2% | 2.3/4.9% | 3 |
| 120 | 1 | 0.887 | 0.876 | 0.011 | - | - | 0.980 | 0.980 | 0.737 | 1.41x | 17.5/23.5/27.2% | 2.3/4.9% | 3 |
| 250 | 1 | 0.887 | 0.876 | 0.011 | - | - | 0.980 | 0.980 | 0.737 | 1.41x | 17.5/23.5/27.2% | 2.3/4.9% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.309 | 0.305 | 0.005 | - | - | 0.410 | 0.413 | 0.096 | 11.09x | 39.2/53.9/74.1% | 3.9/10.4% | 3 |
| 120 | 1 | 0.495 | 0.488 | 0.007 | - | - | 0.602 | 0.604 | 0.125 | 4.38x | 15.8/23.9/38.2% | 1.5/4.8% | 3 |
| 250 | 1 | 0.493 | 0.486 | 0.007 | - | - | 0.592 | 0.595 | 0.129 | 4.28x | 15.5/23.2/37.2% | 1.5/4.7% | 3 |

> max-num-nodes=10: decode_failures 15

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.887 | 0.876 | 0.011 | - | - | 0.980 | 0.980 | 0.737 | 1.41x | 17.5/23.5/27.2% | 2.3/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.887 | 0.876 | 0.011 | - | - | 0.980 | 0.980 | 0.737 | 1.41x | 17.5/23.5/27.2% | 2.3/4.9% | 3 |
| constrained | 1 | 0.801 | 0.777 | 0.024 | - | - | 0.933 | 0.936 | 0.662 | 2.69x | 32.0/43.0/48.9% | 4.5/9.0% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.693 | 0.690 | 0.004 | - | - | 0.832 | 0.925 | 0.495 | 5.66x | 55.4/71.7/75.6% | 3.8/12.0% | 3 |
| 25 | 1 | 0.693 | 0.690 | 0.004 | - | - | 0.832 | 0.925 | 0.495 | 5.66x | 55.4/71.7/75.6% | 3.8/12.0% | 3 |
| 100 | 1 | 0.693 | 0.690 | 0.004 | - | - | 0.832 | 0.925 | 0.495 | 5.66x | 55.4/71.7/75.6% | 3.8/12.0% | 3 |
| 2000 | 1 | 0.693 | 0.690 | 0.004 | - | - | 0.832 | 0.925 | 0.495 | 5.66x | 55.4/71.7/75.6% | 3.8/12.0% | 3 |

> warm-num-nodes=0: decode_failures 87

> warm-num-nodes=25: decode_failures 87

> warm-num-nodes=100: decode_failures 87

> warm-num-nodes=2000: decode_failures 87

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.753 | 0.727 | 0.026 | - | - | 0.930 | 0.934 | 0.592 | 1.17x | 13.9/19.1/21.5% | 1.8/4.2% | 3 |
| 0.2 | 1 | 0.644 | 0.605 | 0.039 | - | - | 0.878 | 0.892 | 0.481 | 1.08x | 12.8/17.9/20.1% | 1.7/3.9% | 3 |
| 0.3 | 1 | 0.514 | 0.476 | 0.038 | - | - | 0.723 | 0.820 | 0.390 | 0.98x | 11.7/16.9/18.5% | 1.5/3.2% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 14

> burst-loss=0.3: decode_failures 31

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.825 | 0.808 | 0.017 | - | - | 0.956 | 0.958 | 0.670 | 1.31x | 15.5/21.0/23.5% | 2.1/4.5% | 3 |
| 0.2 | 1 | 0.776 | 0.754 | 0.022 | - | - | 0.930 | 0.934 | 0.600 | 1.36x | 16.1/22.1/24.3% | 2.2/4.4% | 3 |
| 0.3 | 1 | 0.713 | 0.684 | 0.029 | - | - | 0.885 | 0.900 | 0.536 | 1.36x | 16.3/22.4/24.6% | 2.2/4.2% | 3 |

> extra-loss=0.3: decode_failures 2

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.744 | 0.723 | 0.022 | - | - | 0.933 | 0.944 | 0.566 | 1.18x | 14.2/19.2/21.4% | 1.8/4.3% | 3 |
| 0.2 | 1 | 0.610 | 0.583 | 0.027 | - | - | 0.774 | 0.861 | 0.456 | 1.09x | 13.1/18.3/19.9% | 1.7/4.0% | 3 |
| 0.3 | 1 | 0.485 | 0.462 | 0.023 | - | - | 0.643 | 0.821 | 0.342 | 1.00x | 12.1/17.1/18.7% | 1.6/3.1% | 3 |

> burst-loss=0.1: decode_failures 8

> burst-loss=0.2: decode_failures 38

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.806 | 0.806 | 0.000 | - | - | 0.936 | 0.940 | 0.684 | 1.66x | 19.5/26.3/29.7% | 2.6/6.0% | 3 |
| directed-with-late-flood | 1 | 0.811 | 0.811 | 0.000 | - | - | 0.936 | 0.949 | 0.675 | 1.51x | 17.9/24.3/27.5% | 2.4/5.7% | 3 |
| m4-early-flood | 1 | 0.805 | 0.805 | 0.000 | - | - | 0.940 | 0.947 | 0.671 | 1.51x | 17.9/24.3/27.6% | 2.3/5.7% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 1

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.853 | 0.842 | 0.011 | - | - | 0.958 | 0.959 | 0.600 | 0.72x | 8.0/10.6/12.8% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.858 | 0.841 | 0.017 | - | - | 0.964 | 0.971 | 0.702 | 1.12x | 13.2/19.1/21.1% | 1.8/4.3% | 3 |
| 0.5 | 1 | 0.894 | 0.856 | 0.038 | - | - | 0.965 | 0.973 | 0.755 | 0.94x | 11.1/15.7/18.6% | 1.5/4.0% | 3 |
| 0.75 | 1 | 0.851 | 0.836 | 0.016 | - | - | 0.965 | 0.968 | 0.659 | 0.85x | 9.3/12.7/15.1% | 1.3/3.3% | 3 |

> legacy-fraction=0.25: decode_failures 1

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.854 | 0.836 | 0.018 | - | - | 0.960 | 0.966 | 0.689 | 1.11x | 13.2/19.5/21.3% | 1.8/4.3% | 3 |
| 0.5 | 1 | 0.892 | 0.857 | 0.035 | - | - | 0.959 | 0.965 | 0.741 | 0.92x | 11.1/15.6/18.1% | 1.6/3.9% | 3 |
| 0.75 | 1 | 0.849 | 0.830 | 0.019 | - | - | 0.961 | 0.965 | 0.643 | 0.82x | 9.0/12.6/15.1% | 1.2/3.2% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.894 | 0.885 | 0.009 | - | - | 0.971 | 0.971 | 0.744 | 0.67x | 8.4/11.2/12.8% | 1.0/2.6% | 3 |
| signing=true | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.879 | 0.871 | 0.008 | - | - | 0.972 | 0.973 | 0.675 | 0.73x | 8.4/11.9/13.8% | 1.3/2.8% | 3 |
| 2.5 | 1 | 0.864 | 0.854 | 0.009 | - | - | 0.962 | 0.964 | 0.645 | 0.74x | 8.4/11.7/13.6% | 1.3/2.8% | 3 |
| 2.6 | 1 | 0.871 | 0.863 | 0.008 | - | - | 0.956 | 0.957 | 0.661 | 0.70x | 8.1/11.7/13.7% | 1.2/2.7% | 3 |
| 2.7 | 1 | 0.886 | 0.880 | 0.006 | - | - | 0.971 | 0.972 | 0.700 | 0.71x | 8.4/12.0/14.4% | 1.2/2.9% | 3 |
| 2.8 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.879 | 0.867 | 0.012 | - | - | 0.958 | 0.961 | 0.725 | 0.84x | 9.9/13.2/15.5% | 1.3/3.1% | 3 |
| 900 | 1 | 0.814 | 0.795 | 0.018 | - | - | 0.935 | 0.937 | 0.637 | 1.94x | 22.8/31.1/34.9% | 3.1/7.0% | 3 |
| 300 | 1 | 0.559 | 0.526 | 0.033 | - | - | 0.748 | 0.780 | 0.446 | 4.26x | 47.3/61.9/65.9% | 7.2/13.7% | 3 |

> broadcast-interval-s=300: decode_failures 19

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.977 | 0.978 | 0.803 | 0.93x | 11.0/14.3/16.6% | 1.5/3.3% | 3 |
| 900 | 1 | 0.843 | 0.829 | 0.014 | - | - | 0.940 | 0.942 | 0.720 | 2.14x | 25.1/33.4/37.2% | 3.3/7.5% | 3 |
| 300 | 1 | 0.558 | 0.531 | 0.027 | - | - | 0.734 | 0.754 | 0.435 | 4.66x | 51.9/65.6/68.2% | 7.6/14.5% | 3 |

> broadcast-interval-s=300: decode_failures 9

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.874 | 0.863 | 0.011 | - | - | 0.965 | 0.966 | 0.716 | 1.16x | 13.8/18.5/21.2% | 1.8/4.3% | 3 |
| sinusoid | 1 | 0.853 | 0.839 | 0.014 | - | - | 0.950 | 0.950 | 0.702 | 1.13x | 13.5/17.9/20.9% | 1.8/4.2% | 3 |
| commuter | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.814 | 0.795 | 0.018 | - | - | 0.935 | 0.937 | 0.637 | 1.94x | 22.8/31.1/34.9% | 3.1/7.0% | 3 |
| 3600 | 1 | 0.879 | 0.867 | 0.012 | - | - | 0.958 | 0.961 | 0.725 | 0.84x | 9.9/13.2/15.5% | 1.3/3.1% | 3 |
| 10800 | 1 | 0.893 | 0.886 | 0.006 | - | - | 0.964 | 0.966 | 0.742 | 0.56x | 6.6/8.7/10.2% | 0.9/2.1% | 3 |
| 43200 | 1 | 0.902 | 0.894 | 0.008 | - | - | 0.969 | 0.971 | 0.748 | 0.42x | 4.9/6.5/7.7% | 0.7/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.848 | 0.832 | 0.017 | - | - | 0.953 | 0.953 | 0.704 | 1.34x | 15.7/21.4/24.5% | 2.1/4.9% | 3 |
| 1.0 | 1 | 0.851 | 0.833 | 0.018 | - | - | 0.960 | 0.960 | 0.698 | 1.46x | 17.2/23.5/26.9% | 2.2/5.4% | 3 |
| 4.0 | 1 | 0.816 | 0.796 | 0.020 | - | - | 0.949 | 0.949 | 0.668 | 1.77x | 20.8/29.7/33.0% | 2.8/6.7% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.693 | 0.690 | 0.004 | - | - | 0.832 | 0.925 | 0.495 | 5.66x | 55.4/71.7/75.6% | 3.8/12.0% | 3 |
| 1.0 | 1 | 0.632 | 0.628 | 0.004 | - | - | 0.768 | 0.896 | 0.445 | 6.17x | 58.5/73.9/77.8% | 4.3/13.1% | 3 |

> traceroute-per-hour=0.0: decode_failures 87

> traceroute-per-hour=1.0: queue drops 13.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 85

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.606 | 0.591 | 0.015 | - | - | 0.899 | 0.902 | 0.287 | 1.11x | 12.4/20.2/22.1% | 2.7/6.1% | 3 |
| 60 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 90 | 1 | 0.900 | 0.895 | 0.005 | - | - | 0.979 | 0.981 | 0.712 | 1.56x | 17.1/28.0/31.8% | 1.4/4.7% | 3 |
| 120 | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.995 | 0.996 | 0.756 | 2.06x | 21.4/33.0/36.9% | 1.4/5.2% | 3 |
| 150 | 1 | 0.959 | 0.957 | 0.002 | - | - | 0.998 | 0.999 | 0.839 | 2.48x | 25.3/37.2/42.7% | 1.2/5.6% | 3 |

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 120 | 1 | 0.700 | 0.689 | 0.010 | - | - | 0.873 | 0.873 | 0.419 | 2.16x | 14.2/27.9/35.7% | 1.5/4.8% | 3 |
| 250 | 1 | 0.494 | 0.487 | 0.007 | - | - | 0.599 | 0.599 | 0.128 | 4.70x | 16.9/25.5/40.6% | 1.6/5.3% | 3 |
| 500 | 1 | 0.315 | 0.310 | 0.004 | - | - | 0.420 | 0.424 | 0.136 | 9.53x | 19.1/27.3/38.5% | 1.6/6.9% | 3 |

> nodes=500: decode_failures 107

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.684 | 0.673 | 0.011 | - | - | 0.847 | 0.848 | 0.411 | 2.06x | 13.6/26.1/33.6% | 1.5/4.4% | 3 |
| 250 | 1 | 0.495 | 0.488 | 0.007 | - | - | 0.602 | 0.604 | 0.125 | 4.38x | 15.8/23.9/38.2% | 1.5/4.8% | 3 |
| 500 | 1 | 0.317 | 0.313 | 0.004 | - | - | 0.433 | 0.437 | 0.131 | 9.07x | 18.2/26.2/36.7% | 1.5/6.6% | 3 |

> nodes=500: decode_failures 70

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.817 | 0.798 | 0.019 | - | - | 0.941 | 0.943 | 0.624 | 1.26x | 15.0/20.0/22.9% | 2.0/4.6% | 3 |
| baymesh-2026-08 | 1 | 0.803 | 0.778 | 0.025 | - | - | 0.952 | 0.956 | 0.625 | 1.14x | 14.1/19.1/20.1% | 2.1/4.4% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.830 | 0.812 | 0.018 | - | - | 0.948 | 0.949 | 0.652 | 1.29x | 15.3/20.5/23.5% | 2.0/4.6% | 3 |
| baymesh-2026-08 | 1 | 0.828 | 0.806 | 0.022 | - | - | 0.963 | 0.964 | 0.677 | 1.23x | 15.3/20.2/22.1% | 2.2/4.5% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.05 | 1 | 0.876 | 0.865 | 0.012 | - | - | 0.977 | 0.977 | 0.741 | 1.35x | 16.2/22.3/24.9% | 2.1/4.8% | 3 |
| 0.1 | 1 | 0.881 | 0.870 | 0.012 | - | - | 0.977 | 0.978 | 0.731 | 1.44x | 18.0/23.6/27.6% | 2.3/4.7% | 3 |
| 0.2 | 1 | 0.902 | 0.894 | 0.008 | - | - | 0.985 | 0.985 | 0.740 | 1.61x | 20.3/28.0/33.1% | 2.4/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| local-typical | 1 | 0.568 | 0.560 | 0.008 | - | - | 0.824 | 0.826 | 0.000 | 1.38x | 8.1/16.9/20.7% | 2.2/4.9% | 3 |
| event | 1 | 0.144 | 0.144 | 0.001 | - | - | 0.269 | 0.269 | 0.000 | 0.95x | 4.6/12.2/15.7% | 1.5/3.6% | 3 |
| backbone | 1 | 0.975 | 0.974 | 0.001 | - | - | 0.999 | 0.999 | 0.924 | 1.15x | 23.3/33.0/35.5% | 1.3/5.7% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.769 | 0.725 | 0.044 | - | - | 0.933 | 0.946 | 0.567 | 1.26x | 19.2/23.5/32.0% | 2.7/6.4% | 3 |
| 60 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 90 | 1 | 0.703 | 0.695 | 0.008 | - | - | 0.923 | 0.924 | 0.253 | 1.58x | 12.9/22.0/27.7% | 1.5/4.4% | 3 |
| 120 | 1 | 0.700 | 0.689 | 0.010 | - | - | 0.873 | 0.873 | 0.419 | 2.16x | 14.2/27.9/35.7% | 1.5/4.8% | 3 |
| 150 | 1 | 0.618 | 0.608 | 0.009 | - | - | 0.749 | 0.751 | 0.263 | 2.51x | 14.2/24.6/33.7% | 1.4/4.3% | 3 |

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 1.25 | 1 | 0.595 | 0.565 | 0.029 | - | - | 0.829 | 0.849 | 0.107 | 1.33x | 11.9/17.0/18.8% | 2.0/4.5% | 3 |
| 1.5 | 1 | 0.345 | 0.340 | 0.005 | - | - | 0.486 | 0.494 | 0.145 | 1.59x | 10.4/20.8/25.4% | 2.5/4.7% | 3 |
| 2.0 | 1 | 0.074 | 0.074 | 0.000 | - | - | 0.136 | 0.136 | 0.000 | 0.59x | 2.4/6.5/9.4% | 0.9/2.2% | 3 |

> stretch=1.25: decode_failures 6

> stretch=1.5: decode_failures 3

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| clustered | 1 | 0.910 | 0.906 | 0.004 | - | - | 0.999 | 0.999 | 0.000 | 1.21x | 22.9/29.6/32.8% | 1.6/5.5% | 3 |
| corridor | 1 | 0.546 | 0.536 | 0.011 | - | - | 0.660 | 0.666 | 0.105 | 1.39x | 15.3/24.4/26.6% | 2.2/6.2% | 3 |
| hub | 1 | 0.907 | 0.895 | 0.012 | - | - | 0.967 | 0.967 | 0.748 | 1.19x | 22.5/34.2/36.3% | 1.7/5.5% | 3 |

> topology=corridor: decode_failures 2

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.811 | 0.811 | 0.000 | - | - | 0.936 | 0.949 | 0.675 | 1.51x | 17.9/24.3/27.5% | 2.4/5.7% | 3 |
| True | 1 | 0.807 | 0.807 | 0.000 | - | - | 0.934 | 0.940 | 0.683 | 1.52x | 18.1/24.4/27.5% | 2.4/5.8% | 3 |

> coding-rate-ladder=False: decode_failures 1

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.807 | 0.807 | 0.000 | - | - | 0.934 | 0.940 | 0.683 | 1.52x | 18.1/24.4/27.5% | 2.4/5.8% | 3 |
| m4-early-flood | 1 | 0.820 | 0.820 | 0.000 | - | - | 0.948 | 0.955 | 0.695 | 1.51x | 17.9/24.3/27.5% | 2.3/5.7% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.843 | 0.843 | 0.000 | - | - | 0 | 0.000 | 0.713 | 1.21x | 14.3/19.3/22.2% | 2.0/4.4% | 3 |
| chain | 1 | 0.828 | 0.822 | 0.006 | - | - | 0.890 | 0.953 | 0.684 | 1.45x | 17.2/23.2/26.3% | 2.2/5.3% | 3 |
| sr | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| True | 1 | 0.857 | 0.843 | 0.014 | - | - | 0.970 | 0.971 | 0.713 | 1.27x | 15.0/20.2/23.0% | 2.0/4.6% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.995 | 0.996 | 0.756 | 2.06x | 21.4/33.0/36.9% | 1.4/5.2% | 3 |
| True | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.996 | 0.996 | 0.753 | 2.10x | 21.6/33.4/37.4% | 1.4/5.3% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.091 | 0.091 | 0.000 | - | - | 0.147 | 0.148 | 0.000 | 0.03x | 0.2/0.3/0.4% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.410 | 0.401 | 0.010 | - | - | 0.625 | 0.809 | 0.000 | 0.27x | 1.7/2.9/3.7% | 0.4/0.8% | 3 |
| LONG_TURBO | 1 | 0.774 | 0.753 | 0.021 | - | - | 0.926 | 0.929 | 0.486 | 1.24x | 11.6/16.3/19.4% | 2.1/4.4% | 3 |

> preset=MEDIUM_TURBO: decode_failures 6

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.976 | 0.976 | 0.743 | 1.15x | 16.1/21.7/24.3% | 1.8/4.8% | 3 |
| 1.0 | 1 | 0.925 | 0.918 | 0.007 | - | - | 0.986 | 0.986 | 0.809 | 1.04x | 17.8/23.2/26.1% | 1.6/5.1% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.224 | 0.222 | 0.002 | - | - | 0.287 | 0.502 | 0.000 | 0.12x | 0.6/1.5/1.8% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| LITE_FAST | 1 | 0.810 | 0.793 | 0.017 | - | - | 0.955 | 0.957 | 0.538 | 0.97x | 9.7/14.8/17.2% | 1.7/3.4% | 3 |
| NARROW_SLOW | 1 | 0.842 | 0.825 | 0.017 | - | - | 0.968 | 0.968 | 0.642 | 1.22x | 12.5/19.3/21.4% | 2.0/4.6% | 3 |

> preset=SHORT_FAST: decode_failures 8

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| temporal | 1 | 0.776 | 0.751 | 0.024 | - | - | 0.937 | 0.940 | 0.592 | 1.27x | 14.4/20.4/22.4% | 2.2/4.1% | 3 |
| transient | 1 | 0.843 | 0.826 | 0.017 | - | - | 0.955 | 0.958 | 0.683 | 1.25x | 14.8/20.0/22.9% | 1.9/4.5% | 3 |
| periodic | 1 | 0.698 | 0.679 | 0.020 | - | - | 0.817 | 0.826 | 0.576 | 1.16x | 13.6/18.8/21.2% | 1.8/4.0% | 3 |

> noise-profile=periodic: decode_failures 2

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.224 | 0.222 | 0.002 | - | - | 0.287 | 0.502 | 0.000 | 0.12x | 0.6/1.5/1.8% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| LONG_MODERATE | 1 | 0.824 | 0.807 | 0.017 | - | - | 0.943 | 0.944 | 0.663 | 3.33x | 42.6/55.6/62.0% | 4.7/13.1% | 3 |

> preset=SHORT_FAST: decode_failures 8

> preset=LONG_MODERATE: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.044 | 0.044 | 0.000 | - | - | 0.131 | 0.132 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.091 | 0.091 | 0.000 | - | - | 0.147 | 0.148 | 0.000 | 0.03x | 0.2/0.3/0.4% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| LONG_TURBO | 1 | 0.774 | 0.753 | 0.021 | - | - | 0.926 | 0.929 | 0.486 | 1.24x | 11.6/16.3/19.4% | 2.1/4.4% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.847 | 0.826 | 0.022 | - | - | 0.967 | 0.971 | 0.724 | 1.68x | 18.6/26.0/28.8% | 2.8/6.2% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.805 | 0.788 | 0.017 | - | - | 0.919 | 0.921 | 0.664 | 1.21x | 14.4/19.6/22.2% | 1.9/4.3% | 3 |
| 10000 | 1 | 0.698 | 0.679 | 0.020 | - | - | 0.817 | 0.826 | 0.576 | 1.16x | 13.6/18.8/21.2% | 1.8/4.0% | 3 |
| 4000 | 1 | 0.404 | 0.398 | 0.006 | - | - | 0.469 | 0.566 | 0.312 | 0.99x | 11.4/16.5/18.2% | 1.6/3.0% | 3 |
| 2000 | 1 | 0.089 | 0.089 | 0.000 | - | - | 0.099 | 0.186 | 0.044 | 0.72x | 8.9/12.1/13.5% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 2

> noise-pulse-interval-ms=4000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.345 | 0.340 | 0.005 | - | - | 0.486 | 0.494 | 0.145 | 1.59x | 10.4/20.8/25.4% | 2.5/4.7% | 3 |
| 1.0 | 1 | 0.683 | 0.676 | 0.007 | - | - | 0.765 | 0.765 | 0.572 | 1.18x | 15.0/22.7/26.4% | 1.7/4.4% | 3 |

> duct-per-hour=0.0: decode_failures 3

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 22 | 1 | 0.371 | 0.362 | 0.009 | - | - | 0.526 | 0.758 | 0.000 | 1.47x | 9.7/16.3/18.3% | 2.4/4.0% | 3 |
| 17 | 1 | 0.091 | 0.091 | 0.000 | - | - | 0.142 | 0.145 | 0.000 | 0.70x | 3.3/7.5/9.8% | 1.1/2.2% | 3 |
| 14 | 1 | 0.059 | 0.058 | 0.001 | - | - | 0.120 | 0.141 | 0.000 | 0.54x | 1.8/6.2/9.2% | 0.8/2.2% | 3 |

> tx-power=22: decode_failures 4

> tx-power=14: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.995 | 0.996 | 0.756 | 2.06x | 21.4/33.0/36.9% | 1.4/5.2% | 3 |
| True | 1 | 0.926 | 0.924 | 0.003 | - | - | 0.993 | 0.994 | 0.734 | 2.48x | 24.9/38.2/42.3% | 1.7/6.0% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.876 | 0.861 | 0.015 | - | - | 0.975 | 0.976 | 0.720 | 1.34x | 15.9/22.0/25.1% | 2.1/4.9% | 3 |
| True | 1 | 0.886 | 0.875 | 0.011 | - | - | 0.977 | 0.978 | 0.746 | 1.41x | 16.6/22.5/26.0% | 2.2/5.0% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| random | 1 | 0.846 | 0.833 | 0.013 | - | - | 0.947 | 0.951 | 0.684 | 1.22x | 14.6/19.4/22.1% | 1.8/4.5% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.623 | 0.574 | 0.049 | - | - | 0.835 | 0.837 | 0.411 | 0.97x | 11.6/16.5/18.6% | 1.5/3.9% | 3 |
| 7 | 1 | 0.894 | 0.886 | 0.008 | - | - | 0.967 | 0.968 | 0.789 | 1.42x | 16.8/21.7/25.1% | 2.3/5.0% | 3 |
| 15 | 1 | 0.931 | 0.927 | 0.004 | - | - | 0.977 | 0.977 | 0.835 | 1.45x | 17.1/21.8/25.3% | 2.3/5.1% | 3 |
| 32 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.973 | 0.973 | 0.831 | 1.41x | 16.7/21.5/24.7% | 2.3/5.0% | 3 |

> hop-limit=3: decode_failures 1

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.623 | 0.574 | 0.049 | - | - | 0.835 | 0.837 | 0.411 | 0.97x | 11.6/16.5/18.6% | 1.5/3.9% | 3 |
| 5 | 1 | 0.815 | 0.794 | 0.021 | - | - | 0.963 | 0.964 | 0.635 | 1.24x | 14.7/20.1/22.5% | 1.9/4.6% | 3 |
| 7 | 1 | 0.894 | 0.886 | 0.008 | - | - | 0.967 | 0.968 | 0.789 | 1.42x | 16.8/21.7/25.1% | 2.3/5.0% | 3 |

> hop-limit=3: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| KNOWN_ONLY | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.840 | 0.840 | 0.000 | - | - | 0.880 | 0.966 | 0.697 | 1.23x | 14.4/19.5/22.4% | 1.9/4.4% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.623 | 0.574 | 0.049 | - | - | 0.835 | 0.837 | 0.411 | 0.97x | 11.6/16.5/18.6% | 1.5/3.9% | 3 |
| True | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

> hop-spread=False: decode_failures 1

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| BALANCED | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| STRICT | 1 | 0.762 | 0.762 | 0.000 | - | - | 0.885 | 0.888 | 0.644 | 1.36x | 16.0/21.4/25.0% | 2.1/4.9% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| dm | 1 | 0.853 | 0.836 | 0.018 | - | - | 0.953 | 0.954 | 0.724 | 1.24x | 14.8/20.1/22.8% | 1.9/4.6% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.854 | 0.839 | 0.015 | - | - | 0.961 | 0.962 | 0.701 | 1.26x | 15.0/20.2/23.0% | 2.0/4.6% | 3 |
| local | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| time | 1 | 0.856 | 0.841 | 0.014 | - | - | 0.965 | 0.967 | 0.711 | 1.29x | 15.3/20.7/23.7% | 2.0/4.8% | 3 |
| window | 1 | 0.860 | 0.846 | 0.014 | - | - | 0.960 | 0.962 | 0.708 | 1.25x | 14.8/19.9/22.8% | 1.9/4.5% | 3 |

> bucket-mode=global: misdecodes 24

> bucket-mode=time: misdecodes 19

> bucket-mode=window: misdecodes 18

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.848 | 0.834 | 0.014 | - | - | 0.956 | 0.958 | 0.688 | 1.39x | 16.3/22.1/24.8% | 2.2/5.3% | 3 |
| 1800 | 1 | 0.856 | 0.841 | 0.014 | - | - | 0.965 | 0.967 | 0.711 | 1.29x | 15.3/20.7/23.7% | 2.0/4.8% | 3 |
| 3600 | 1 | 0.853 | 0.840 | 0.013 | - | - | 0.949 | 0.958 | 0.714 | 1.25x | 14.9/19.9/22.8% | 2.0/4.6% | 3 |

> time-bucket-s=600: misdecodes 102

> time-bucket-s=1800: misdecodes 19

> time-bucket-s=3600: misdecodes 10

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| interval | 1 | 0.845 | 0.827 | 0.018 | - | - | 0.958 | 0.966 | 0.689 | 1.67x | 19.3/26.6/29.7% | 2.7/6.7% | 3 |
| aimd | 1 | 0.850 | 0.846 | 0.005 | - | - | 0.907 | 0.965 | 0.697 | 1.28x | 15.2/20.4/23.4% | 2.0/4.7% | 3 |
| bucket+interval | 1 | 0.837 | 0.816 | 0.021 | - | - | 0.952 | 0.953 | 0.691 | 1.68x | 19.2/27.1/30.2% | 2.8/6.8% | 3 |

> trigger=interval: misdecodes 4

> trigger=interval: decode_failures 4

> trigger=aimd: decode_failures 1

> trigger=bucket+interval: misdecodes 6

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.861 | 0.847 | 0.015 | - | - | 0.960 | 0.964 | 0.724 | 1.25x | 14.9/20.1/22.9% | 1.9/4.6% | 3 |
| 8 | 1 | 0.861 | 0.846 | 0.015 | - | - | 0.964 | 0.965 | 0.707 | 1.23x | 14.7/19.8/22.6% | 1.9/4.5% | 3 |
| 16 | 1 | 0.851 | 0.837 | 0.014 | - | - | 0.954 | 0.956 | 0.704 | 1.25x | 14.9/20.1/22.9% | 2.0/4.6% | 3 |
| 32 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 50 | 1 | 0.853 | 0.840 | 0.014 | - | - | 0.964 | 0.964 | 0.697 | 1.25x | 14.8/20.0/22.9% | 1.9/4.6% | 3 |

> capacity=4: decode_failures 101

> capacity=8: decode_failures 36

> capacity=16: decode_failures 2

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.861 | 0.847 | 0.015 | - | - | 0.960 | 0.964 | 0.724 | 1.25x | 14.9/20.1/22.9% | 1.9/4.6% | 3 |
| 8 | 1 | 0.861 | 0.846 | 0.015 | - | - | 0.964 | 0.965 | 0.707 | 1.23x | 14.7/19.8/22.6% | 1.9/4.5% | 3 |
| 16 | 1 | 0.851 | 0.837 | 0.014 | - | - | 0.954 | 0.956 | 0.704 | 1.25x | 14.9/20.1/22.9% | 2.0/4.6% | 3 |
| 32 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 50 | 1 | 0.853 | 0.840 | 0.014 | - | - | 0.964 | 0.964 | 0.697 | 1.25x | 14.8/20.0/22.9% | 1.9/4.6% | 3 |

> capacity=4: decode_failures 101

> capacity=8: decode_failures 36

> capacity=16: decode_failures 2

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.850 | 0.838 | 0.012 | - | - | 0.935 | 0.967 | 0.706 | 1.25x | 14.7/20.0/22.9% | 1.9/4.6% | 3 |
| 16 | 1 | 0.853 | 0.839 | 0.014 | - | - | 0.955 | 0.957 | 0.694 | 1.25x | 14.7/19.9/22.9% | 1.9/4.5% | 3 |
| 32 | 1 | 0.860 | 0.846 | 0.014 | - | - | 0.960 | 0.962 | 0.708 | 1.25x | 14.8/19.9/22.8% | 1.9/4.5% | 3 |

> capacity=8: misdecodes 9

> capacity=8: decode_failures 60

> capacity=16: misdecodes 23

> capacity=32: misdecodes 18

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.837 | 0.816 | 0.021 | - | - | 0.952 | 0.953 | 0.691 | 1.68x | 19.2/27.1/30.2% | 2.8/6.8% | 3 |
| 02-06 | 1 | 0.852 | 0.842 | 0.010 | - | - | 0.921 | 0.960 | 0.725 | 1.29x | 15.4/20.6/23.5% | 2.0/4.9% | 3 |
| 00-08 | 1 | 0.853 | 0.842 | 0.011 | - | - | 0.930 | 0.963 | 0.715 | 1.35x | 15.9/21.6/24.4% | 2.1/5.4% | 3 |

> catch-up-hours=: misdecodes 6

> catch-up-hours=02-06: decode_failures 40

> catch-up-hours=00-08: decode_failures 39

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.851 | 0.846 | 0.005 | - | - | 0.896 | 0.896 | 0.713 | 1.23x | 14.6/19.5/22.5% | 1.9/4.5% | 3 |
| 2 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 3 | 1 | 0.872 | 0.838 | 0.035 | - | - | 0.962 | 0.989 | 0.707 | 1.26x | 14.7/19.8/23.1% | 2.0/4.5% | 3 |
| 4 | 1 | 0.879 | 0.843 | 0.036 | - | - | 0.963 | 0.972 | 0.718 | 1.26x | 14.9/20.2/22.9% | 2.0/4.7% | 3 |

> hops-apart=3: decode_failures 13

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.851 | 0.846 | 0.005 | - | - | 0.896 | 0.896 | 0.713 | 1.23x | 14.6/19.5/22.5% | 1.9/4.5% | 3 |
| 2 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 3 | 1 | 0.872 | 0.838 | 0.035 | - | - | 0.962 | 0.989 | 0.707 | 1.26x | 14.7/19.8/23.1% | 2.0/4.5% | 3 |
| 4 | 1 | 0.879 | 0.843 | 0.036 | - | - | 0.963 | 0.972 | 0.718 | 1.26x | 14.9/20.2/22.9% | 2.0/4.7% | 3 |
| 5 | 1 | 0.879 | 0.843 | 0.036 | - | - | 0.963 | 0.972 | 0.718 | 1.26x | 14.9/20.2/22.9% | 2.0/4.7% | 3 |

> hops-apart=3: decode_failures 13

> faster: 1.66 s per simulated hour against 4.52 over 69 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.849 | 0.835 | 0.014 | - | - | 0.952 | 0.957 | 0.688 | 1.26x | 15.0/20.1/23.0% | 1.9/4.6% | 3 |
| 30 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 120 | 1 | 0.854 | 0.841 | 0.014 | - | - | 0.957 | 0.959 | 0.707 | 1.27x | 15.1/20.3/23.3% | 2.0/4.7% | 3 |
| 600 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.958 | 0.961 | 0.715 | 1.26x | 14.9/20.1/23.0% | 2.0/4.6% | 3 |

> advert-jitter-s=1: misdecodes 1

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.849 | 0.835 | 0.014 | - | - | 0.952 | 0.957 | 0.688 | 1.26x | 15.0/20.1/23.0% | 1.9/4.6% | 3 |
| 30 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 120 | 1 | 0.854 | 0.841 | 0.014 | - | - | 0.957 | 0.959 | 0.707 | 1.27x | 15.1/20.3/23.3% | 2.0/4.7% | 3 |
| 600 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.958 | 0.961 | 0.715 | 1.26x | 14.9/20.1/23.0% | 2.0/4.6% | 3 |

> advert-jitter-s=1: misdecodes 1

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.900 | 0.839 | 0.061 | - | - | 0.981 | 0.989 | 0.720 | 1.28x | 15.0/20.0/23.1% | 2.0/4.7% | 3 |
| routers | 1 | 0.856 | 0.840 | 0.016 | - | - | 0.920 | 0.981 | 0.710 | 1.24x | 14.6/19.6/22.7% | 1.9/4.5% | 3 |
| alternate-routers | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.900 | 0.900 | 0.714 | 1.25x | 14.8/19.9/22.6% | 1.9/4.7% | 3 |
| beside-router | 1 | 0.873 | 0.842 | 0.030 | - | - | 0.959 | 0.984 | 0.707 | 1.24x | 14.6/19.6/22.8% | 2.0/4.5% | 3 |
| random-clients | 1 | 0.855 | 0.843 | 0.011 | - | - | 0.972 | 0.972 | 0.715 | 1.26x | 14.8/20.2/23.2% | 1.9/4.5% | 3 |
| hops-apart | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

> place=spread: decode_failures 1

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.900 | 0.839 | 0.061 | - | - | 0.981 | 0.989 | 0.720 | 1.28x | 15.0/20.0/23.1% | 2.0/4.7% | 3 |
| routers | 1 | 0.856 | 0.840 | 0.016 | - | - | 0.920 | 0.981 | 0.710 | 1.24x | 14.6/19.6/22.7% | 1.9/4.5% | 3 |
| alternate-routers | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.900 | 0.900 | 0.714 | 1.25x | 14.8/19.9/22.6% | 1.9/4.7% | 3 |
| beside-router | 1 | 0.873 | 0.842 | 0.030 | - | - | 0.959 | 0.984 | 0.707 | 1.24x | 14.6/19.6/22.8% | 2.0/4.5% | 3 |
| random-clients | 1 | 0.855 | 0.843 | 0.011 | - | - | 0.972 | 0.972 | 0.715 | 1.26x | 14.8/20.2/23.2% | 1.9/4.5% | 3 |
| hops-apart | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

> place=spread: decode_failures 1

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| broadcast | 1 | 0.880 | 0.833 | 0.047 | - | - | 0.951 | 0.953 | 0.733 | 1.32x | 15.6/21.0/23.7% | 2.1/4.8% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| heard | 1 | 0.852 | 0.837 | 0.015 | - | - | 0.954 | 0.955 | 0.711 | 1.26x | 14.9/20.1/23.0% | 2.0/4.6% | 3 |

> replay-ordering=heard: misdecodes 16

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.880 | 0.833 | 0.047 | - | - | 0.951 | 0.953 | 0.733 | 1.32x | 15.6/21.0/23.7% | 2.1/4.8% | 3 |
| heard | 1 | 0.878 | 0.832 | 0.045 | - | - | 0.962 | 0.966 | 0.732 | 1.32x | 15.6/21.0/23.7% | 2.1/4.8% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| enum | 1 | 0.859 | 0.841 | 0.018 | - | - | 0.961 | 0.965 | 0.711 | 1.25x | 14.9/20.3/22.9% | 1.9/4.7% | 3 |
| hybrid | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.856 | 0.840 | 0.016 | - | - | 0.920 | 0.981 | 0.710 | 1.24x | 14.6/19.6/22.7% | 1.9/4.5% | 3 |
| 6 | 1 | 0.867 | 0.835 | 0.032 | - | - | 0.967 | 0.984 | 0.688 | 1.28x | 15.0/20.2/23.8% | 2.1/4.8% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.845 | 0.839 | 0.006 | - | - | 0.944 | 0.945 | 0.706 | 1.25x | 14.9/20.0/22.9% | 1.9/4.6% | 2 |
| 3 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 5 | 1 | 0.878 | 0.839 | 0.039 | - | - | 0.984 | 0.987 | 0.726 | 1.29x | 15.2/20.7/23.5% | 2.0/4.8% | 5 |
| 8 | 1 | 0.876 | 0.831 | 0.045 | - | - | 0.988 | 0.991 | 0.725 | 1.32x | 15.5/21.2/24.0% | 2.0/4.8% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.845 | 0.839 | 0.006 | - | - | 0.944 | 0.945 | 0.706 | 1.25x | 14.9/20.0/22.9% | 1.9/4.6% | 2 |
| 3 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 5 | 1 | 0.878 | 0.839 | 0.039 | - | - | 0.984 | 0.987 | 0.726 | 1.29x | 15.2/20.7/23.5% | 2.0/4.8% | 5 |
| 8 | 1 | 0.876 | 0.831 | 0.045 | - | - | 0.988 | 0.991 | 0.725 | 1.32x | 15.5/21.2/24.0% | 2.0/4.8% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| True | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.858 | 0.842 | 0.016 | - | - | 0.959 | 0.959 | 0.684 | 1.18x | 13.9/18.8/21.6% | 1.8/4.3% | 3 |
| 1 | 1 | 0.869 | 0.857 | 0.012 | - | - | 0.966 | 0.969 | 0.695 | 1.18x | 14.0/18.7/21.5% | 1.8/4.3% | 3 |
| 2 | 1 | 0.862 | 0.847 | 0.015 | - | - | 0.967 | 0.968 | 0.699 | 1.17x | 13.9/18.8/21.6% | 1.8/4.3% | 3 |
| 4 | 1 | 0.851 | 0.835 | 0.015 | - | - | 0.963 | 0.963 | 0.701 | 1.19x | 14.1/19.0/21.8% | 1.8/4.3% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.856 | 0.843 | 0.014 | - | - | 0.957 | 0.958 | 0.705 | 1.24x | 14.8/19.9/22.7% | 1.9/4.6% | 3 |
| 24 | 1 | 0.857 | 0.843 | 0.014 | - | - | 0.952 | 0.954 | 0.712 | 1.24x | 14.6/19.8/22.7% | 1.9/4.5% | 3 |
| 32 | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.965 | 0.966 | 0.697 | 1.23x | 14.6/19.6/22.6% | 1.9/4.5% | 3 |
| 64 | 1 | 0.859 | 0.847 | 0.012 | - | - | 0.953 | 0.953 | 0.711 | 1.26x | 14.9/20.2/23.1% | 2.0/4.6% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.847 | 0.831 | 0.016 | - | - | 0.953 | 0.954 | 0.706 | 1.32x | 15.6/21.2/23.9% | 2.1/4.9% | 3 |
| 16 | 1 | 0.852 | 0.834 | 0.018 | - | - | 0.965 | 0.967 | 0.698 | 1.26x | 14.9/20.2/22.9% | 2.0/4.6% | 3 |
| 32 | 1 | 0.860 | 0.846 | 0.014 | - | - | 0.960 | 0.962 | 0.708 | 1.25x | 14.8/19.9/22.8% | 1.9/4.5% | 3 |

> window-size=8: misdecodes 129

> window-size=16: misdecodes 51

> window-size=32: misdecodes 18

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.995 | 0.996 | 0.756 | 2.06x | 21.4/33.0/36.9% | 1.4/5.2% | 3 |
| True | 1 | 0.712 | 0.707 | 0.004 | - | - | 0.840 | 0.933 | 0.501 | 5.53x | 54.4/71.0/75.1% | 3.7/11.7% | 3 |

> no-congestion-scaling=True: decode_failures 81

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.495 | 0.488 | 0.007 | - | - | 0.602 | 0.604 | 0.125 | 4.38x | 15.8/23.9/38.2% | 1.5/4.8% | 3 |
| truesize | 1 | 0.525 | 0.517 | 0.007 | - | - | 0.633 | 0.635 | 0.135 | 3.17x | 11.5/18.0/28.5% | 1.1/3.8% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.941 | 0.938 | 0.002 | - | - | 0.998 | 0.998 | 0.753 | 1.98x | 20.2/31.7/35.4% | 1.4/4.9% | 3 |
| adaptive | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.995 | 0.996 | 0.756 | 2.06x | 21.4/33.0/36.9% | 1.4/5.2% | 3 |

