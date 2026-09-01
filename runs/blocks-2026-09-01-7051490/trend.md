# Sweep blocks-2026-09-01-7051490

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 7051490 · seeds 7051490
- **blocks** 87 run
- **compute** 10.5 h of simulator time across every cell
- **generated** 2026-09-01T09:26:31+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>79 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 6
- DB-hotstore-stress: max-num-nodes=10: decode_failures 49
- DB-hotstore-stress: max-num-nodes=250: decode_failures 56
- DB-warm: warm-num-nodes=0: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 97
- DB-warm: warm-num-nodes=25: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 97
- DB-warm: warm-num-nodes=100: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 97
- DB-warm: warm-num-nodes=2000: queue drops 19.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 97
- DG-burst: burst-loss=0.3: decode_failures 35
- DG-outage: burst-loss=0.1: decode_failures 7
- DG-outage: burst-loss=0.2: decode_failures 25
- DG-outage: burst-loss=0.3: decode_failures 26
- LD-chatty-hops: broadcast-interval-s=300: queue drops 16.2% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 5
- LD-chatty: broadcast-interval-s=300: queue drops 11.2% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 13
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 19.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 97
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 31.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 102
- MS-density: nodes=40: decode_failures 1
- MS-density: nodes=120: misdecodes 1
- MS-density: nodes=150: misdecodes 1
- MS-hopscale: nodes=120: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 129
- MS-hopscale: nodes=500: decode_failures 209
- MS-oversubscribed: nodes=500: decode_failures 7
- MS-siting: siting-mix=local-typical: decode_failures 6
- MS-size: nodes=120: misdecodes 1
- MS-size: nodes=150: decode_failures 1
- MS-topology: topology=clustered: misdecodes 1
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-preset: preset=LONG_MODERATE: decode_failures 2
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 1
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 6
- SF-bucket-mode: bucket-mode=global: misdecodes 35
- SF-bucket-mode: bucket-mode=time: misdecodes 40
- SF-bucket-mode: bucket-mode=window: misdecodes 27
- SF-bucket-time: time-bucket-s=600: misdecodes 117
- SF-bucket-time: time-bucket-s=1800: misdecodes 40
- SF-bucket-time: time-bucket-s=3600: misdecodes 19
- SF-cadence: trigger=interval: misdecodes 20
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=bucket+interval: misdecodes 23
- SF-capacity-local: capacity=4: decode_failures 54
- SF-capacity-local: capacity=8: decode_failures 5
- SF-capacity: capacity=4: decode_failures 54
- SF-capacity: capacity=8: decode_failures 5
- SF-capacity-window: capacity=8: misdecodes 32
- SF-capacity-window: capacity=8: decode_failures 2
- SF-capacity-window: capacity=16: misdecodes 20
- SF-capacity-window: capacity=32: misdecodes 27
- SF-catchup: catch-up-hours=: misdecodes 23
- SF-catchup: catch-up-hours=02-06: decode_failures 14
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 14
- SF-hops-flat: hops-apart=4: decode_failures 14
- SF-hops-spread: hops-apart=4: decode_failures 14
- SF-hops-spread: hops-apart=5: decode_failures 14
- SF-place-flat: place=spread: decode_failures 36
- SF-place-spread: place=spread: decode_failures 36
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 19
- SF-replay-order: replay-ordering=heard: misdecodes 25
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 2
- SF-servers-spread: servers=8: misdecodes 2
- SF-window-size: window-size=8: misdecodes 134
- SF-window-size: window-size=16: misdecodes 61
- SF-window-size: window-size=32: misdecodes 27
- TH-congestion-input: congestion-input=truesize: decode_failures 2
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 19.8% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 74

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `MS-hopscale` | 34.3 | 18.1 | 1.90x | 11 |
| `SF-servers-allrouters` | 3.09 | 1.85 | 1.67x | 11 |
| `SF-replay-order` | 1.2 | 1.8 | 0.66x | 11 |
| `DG-loss` | 1.46 | 2.27 | 0.64x | 11 |
| `MS-oversubscribed` | 12.5 | 19.4 | 0.64x | 11 |
| `SF-cadence` | 2.31 | 3.62 | 0.64x | 11 |
| `RF-preset` | 1.82 | 2.94 | 0.62x | 11 |
| `DM-mode` | 1.84 | 3.06 | 0.60x | 11 |
| `SF-catchup` | 5.67 | 9.85 | 0.58x | 11 |
| `AD-badrouters` | 1.38 | 2.42 | 0.57x | 11 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.989 | 0.989 | 0.883 → 0.888 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.977 | 0.977 | 0.883 → 0.886 | 1.2x bytes_on_air | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.117 → 0.979 | 0.862 | 0.071 → 0.877 | 10x sr_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.156 → 0.937 | 0.780 | 0.132 → 0.838 | 85x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.116 → 0.887 | 0.770 | 0.114 → 0.883 | 3.6x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **text** | 0.152 → 0.885 | 0.734 | 0.146 → 0.883 | 3x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.221 → 0.885 | 0.664 | 0.218 → 0.883 | 3.4x sr_airtime | down | 4 |
| `MS-hopscale` | nodes | **text** | 0.302 → 0.885 | 0.584 | 0.297 → 0.883 | 16x sr_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.283 → 0.836 | 0.553 | 0.279 → 0.823 | 2.9x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.441 → 0.982 | 0.540 | 0.301 → 0.787 | 4.9x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.547 → 0.979 | 0.432 | 0.543 → 0.979 | 1.8x sr_airtime | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.516 → 0.885 | 0.369 | 0.512 → 0.883 | 2x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.516 → 0.885 | 0.369 | 0.512 → 0.883 | 3x sr_airtime | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.586 → 0.942 | 0.356 | 0.576 → 0.941 | 7.8x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.652 → 0.968 | 0.317 | 0.640 → 0.967 | 1.8x sr_airtime | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.573 → 0.885 | 0.312 | 0.548 → 0.883 | 2.5x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.522 → 0.830 | 0.309 | 0.330 → 0.537 | 6.2x sr_airtime | up | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.603 → 0.901 | 0.298 | 0.587 → 0.900 | 7.4x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.599 → 0.885 | 0.287 | 0.564 → 0.883 | 2.7x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.715 → 0.967 | 0.252 | 0.689 → 0.966 | 4.5x sr_airtime | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.712 → 0.956 | 0.245 | 0.696 → 0.955 | 4.7x sr_airtime | down | 2 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.541 → 0.768 | 0.227 | 0.530 → 0.754 | 1.6x sr_airtime | up | 2 |
| `MS-size` | nodes | **text** | 0.683 → 0.885 | 0.202 | 0.669 → 0.883 | 5x sr_bytes | down | 5 |
| `RF-noise` | noise-profile | **held** | 0.793 → 0.993 | 0.199 | 0.701 → 0.891 | 1.6x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.748 → 0.944 | 0.196 | 0.713 → 0.944 | 3.1x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.748 → 0.925 | 0.177 | 0.713 → 0.924 | 2.6x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.748 → 0.885 | 0.138 | 0.713 → 0.883 | 1.8x sr_bytes | up | 2 |
| `DB-hotstore` | max-num-nodes | **text** | 0.827 → 0.927 | 0.100 | 0.819 → 0.924 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.837 → 0.927 | 0.090 | 0.828 → 0.924 | 2.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.799 → 0.885 | 0.086 | 0.788 → 0.883 | 1.5x sr_bytes | down | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.627 → 0.711 | 0.084 | 0.616 → 0.700 | 1.2x sr_airtime | down | 2 |
| `SC-signing` | signature-policy | **text** | 0.803 → 0.885 | 0.082 | 0.803 → 0.883 | 1.2x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.885 → 0.964 | 0.078 | 0.883 → 0.964 | 1.4x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.885 → 0.959 | 0.073 | 0.883 → 0.956 | 1.4x bytes_on_air | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.825 → 0.886 | 0.061 | 0.816 → 0.877 | 1.1x sr_bytes | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.861 → 0.917 | 0.056 | 0.856 → 0.916 | 5.6x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.886 → 0.940 | 0.054 | 0.877 → 0.937 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.886 → 0.940 | 0.054 | 0.877 → 0.937 | 2.6x bytes_on_air | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.885 → 0.936 | 0.050 | 0.883 → 0.933 | 1.4x bytes_on_air | up | 3 |
| `FW-versions` | profile | **text** | 0.885 → 0.935 | 0.050 | 0.883 → 0.935 | 3x bytes_on_air | down | 5 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.885 → 0.924 | 0.038 | 0.883 → 0.921 | 2.1x bytes_on_air | up | 4 |
| `FW-firmware` | profile | **text** | 0.885 → 0.919 | 0.034 | 0.883 → 0.917 | 3x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.885 → 0.919 | 0.034 | 0.883 → 0.916 | 2.1x bytes_on_air | up | 4 |
| `TH-congestion-input` | congestion-input | **text** | 0.543 → 0.576 | 0.033 | 0.532 → 0.566 | 1.3x sr_airtime | up | 2 |
| `SF-hops-flat` | hops-apart | **text** | 0.885 → 0.914 | 0.029 | 0.883 → 0.893 | 3.9x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.885 → 0.914 | 0.029 | 0.883 → 0.893 | 3.9x sr_bytes | up | 5 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.858 → 0.885 | 0.027 | 0.852 → 0.883 | 1.5x sr_airtime | down | 4 |
| `SF-place-flat` | place | **text** | 0.885 → 0.912 | 0.027 | 0.883 → 0.889 | 4.9x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.885 → 0.912 | 0.027 | 0.883 → 0.889 | 4.9x sr_bytes | down | 6 |
| `FW-signing-cost` | profile-flag | **text** | 0.885 → 0.911 | 0.026 | 0.883 → 0.911 | 3.4x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.958 → 0.983 | 0.025 | 0.872 → 0.884 | 16x sr_bytes | up | 4 |
| `AD-worst` | role-placement | **text** | 0.844 → 0.865 | 0.021 | 0.833 → 0.860 | 1.1x bytes_on_air | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.885 → 0.902 | 0.017 | 0.883 → 0.898 | 1.4x bytes_on_air | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.976 → 0.992 | 0.015 | 0.882 → 0.883 | 7.2x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.976 → 0.992 | 0.015 | 0.882 → 0.883 | 7.2x sr_bytes | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.885 → 0.900 | 0.014 | 0.883 → 0.883 | 2x sr_airtime | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.964 → 0.977 | 0.014 | 0.883 → 0.888 | 12x sr_airtime | down | 3 |
| `LD-diurnal` | diurnal | **text** | 0.885 → 0.899 | 0.013 | 0.883 → 0.897 | 1.3x sr_bytes | down | 3 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.867 → 0.879 | 0.012 | 0.867 → 0.879 | 1.1x sr_airtime | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.977 → 0.989 | 0.011 | 0.883 → 0.893 | 3.1x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.977 → 0.989 | 0.011 | 0.881 → 0.887 | 3.1x advert_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.977 → 0.989 | 0.011 | 0.883 → 0.888 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.977 → 0.989 | 0.011 | 0.883 → 0.888 | 1.1x sr_bytes | down | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.880 → 0.891 | 0.011 | 0.876 → 0.889 | 9.5x advert_bytes | up | 3 |
| `SF-window-size` | window-size | **held** | 0.979 → 0.989 | 0.009 | 0.882 → 0.887 | 6.1x advert_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.980 → 0.989 | 0.009 | 0.886 → 0.891 | 2.6x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.910 → 0.918 | 0.009 | 0.905 → 0.914 | 1.1x bytes_on_air | up | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.885 → 0.894 | 0.009 | 0.883 → 0.885 | 1.3x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.956 → 0.964 | 0.008 | 0.955 → 0.963 | 1.1x bytes_on_air | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.882 → 0.890 | 0.007 | 0.878 → 0.887 | 5.5x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.977 → 0.985 | 0.007 | 0.883 → 0.888 | 1x bytes_on_air | up | 2 |
| `SF-capacity` | capacity | **held** | 0.977 → 0.985 | 0.007 | 0.883 → 0.886 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.977 → 0.985 | 0.007 | 0.883 → 0.886 | 5.3x advert_bytes | down | 5 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.867 → 0.874 | 0.007 | 0.867 → 0.874 | 1.1x sr_airtime | down | 2 |
| `SF-width` | short-id-bits | **text** | 0.885 → 0.892 | 0.007 | 0.883 → 0.891 | 3.1x advert_bytes | down | 4 |
| `SF-replay-order` | replay-ordering | **held** | 0.977 → 0.984 | 0.006 | 0.883 → 0.887 | 1.3x sr_bytes | up | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.884 → 0.890 | 0.006 | 0.881 → 0.889 | 3.1x sr_bytes | down | 2 |
| `DM-mode` | dm-mode | **text** | 0.868 → 0.874 | 0.006 | 0.868 → 0.874 | 1.4x sr_airtime | up | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.910 → 0.915 | 0.005 | 0.908 → 0.908 | 1.2x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.895 → 0.900 | 0.005 | 0.876 → 0.883 | 1.2x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **held** | 0.979 → 0.984 | 0.005 | 0.877 → 0.884 | 1.2x sr_bytes | down | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.895 → 0.899 | 0.004 | 0.891 → 0.898 | 1.2x sr_bytes | up | 4 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.956 → 0.960 | 0.004 | 0.955 → 0.958 | 1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.953 → 0.956 | 0.003 | 0.952 → 0.955 | 1.2x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **held** | 0.977 → 0.980 | 0.002 | 0.883 → 0.883 | 5.7x advert_bytes | = | 3 |

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
| none | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| sprinkled | 1 | 0.933 | 0.932 | 0.001 | - | - | 0.975 | 0.976 | 0.684 | 1.18x | 20.2/25.5/27.5% | 1.6/5.3% | 3 |
| arms-race | 1 | 0.964 | 0.964 | 0.000 | - | - | 0.984 | 0.984 | 0.910 | 0.89x | 22.0/27.0/28.7% | 0.8/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.1 | 1 | 0.945 | 0.940 | 0.006 | - | - | 0.995 | 0.996 | 0.827 | 1.04x | 19.1/24.7/26.7% | 1.3/5.3% | 3 |
| 0.3 | 1 | 0.959 | 0.956 | 0.003 | - | - | 0.999 | 1.000 | 0.867 | 0.88x | 23.0/28.4/29.9% | 1.0/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.886 | 0.877 | 0.009 | - | - | 0.979 | 0.983 | 0.657 | 1.08x | 16.5/23.2/24.6% | 1.7/5.2% | 3 |
| inverse | 1 | 0.838 | 0.832 | 0.006 | - | - | 0.965 | 0.967 | 0.577 | 1.08x | 14.4/20.9/22.4% | 1.9/3.7% | 3 |
| random | 1 | 0.825 | 0.816 | 0.009 | - | - | 0.974 | 0.975 | 0.463 | 1.07x | 14.7/21.7/24.5% | 1.8/4.9% | 3 |

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.886 | 0.877 | 0.009 | - | - | 0.979 | 0.983 | 0.657 | 1.08x | 16.5/23.2/24.6% | 1.7/5.2% | 3 |
| all-routers | 1 | 0.940 | 0.937 | 0.003 | - | - | 0.991 | 0.992 | 0.814 | 2.77x | 36.0/48.2/50.4% | 4.5/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.886 | 0.877 | 0.009 | - | - | 0.979 | 0.983 | 0.657 | 1.08x | 16.5/23.2/24.6% | 1.7/5.2% | 3 |
| no-mute | 1 | 0.889 | 0.883 | 0.006 | - | - | 0.986 | 0.986 | 0.634 | 1.17x | 16.2/23.9/25.2% | 1.9/5.3% | 3 |
| all-routers | 1 | 0.940 | 0.937 | 0.003 | - | - | 0.991 | 0.992 | 0.814 | 2.77x | 36.0/48.2/50.4% | 4.5/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.886 | 0.877 | 0.009 | - | - | 0.979 | 0.983 | 0.657 | 1.08x | 16.5/23.2/24.6% | 1.7/5.2% | 3 |
| local-typical | 1 | 0.788 | 0.778 | 0.010 | - | - | 0.825 | 0.947 | 0.000 | 1.16x | 14.3/21.5/27.2% | 1.9/5.1% | 3 |
| basement-heavy | 1 | 0.071 | 0.071 | 0.001 | - | - | 0.117 | 0.196 | 0.000 | 0.64x | 1.1/6.7/12.5% | 0.5/3.9% | 3 |

> siting-mix=local-typical: decode_failures 6

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.865 | 0.860 | 0.005 | - | - | 0.948 | 0.949 | 0.080 | 2.53x | 20.4/33.2/38.9% | 1.9/5.9% | 3 |
| inverse | 1 | 0.844 | 0.833 | 0.011 | - | - | 0.953 | 0.953 | 0.128 | 2.36x | 17.3/25.8/33.9% | 1.9/3.3% | 3 |

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.883 | 0.883 | 0.000 | - | - | 0 | 0.000 | 0.628 | 1.17x | 16.3/25.2/28.3% | 1.6/5.2% | 3 |
| sr | 1 | 0.895 | 0.888 | 0.007 | - | - | 0.989 | 0.990 | 0.625 | 1.21x | 16.8/25.9/28.9% | 1.6/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.827 | 0.819 | 0.008 | - | - | 0.932 | 0.933 | 0.545 | 3.04x | 42.9/65.0/68.9% | 4.1/10.4% | 3 |
| 100 | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.986 | 0.986 | 0.691 | 1.53x | 22.4/36.4/39.5% | 2.1/5.4% | 3 |
| 120 | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.986 | 0.986 | 0.691 | 1.53x | 22.4/36.4/39.5% | 2.1/5.4% | 3 |
| 250 | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.986 | 0.986 | 0.691 | 1.53x | 22.4/36.4/39.5% | 2.1/5.4% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.335 | 0.330 | 0.006 | - | - | 0.522 | 0.588 | 0.139 | 11.53x | 39.0/65.4/74.2% | 3.9/10.9% | 3 |
| 120 | 1 | 0.543 | 0.532 | 0.011 | - | - | 0.830 | 0.830 | 0.198 | 4.51x | 15.4/32.1/38.8% | 1.4/5.4% | 3 |
| 250 | 1 | 0.548 | 0.537 | 0.011 | - | - | 0.829 | 0.835 | 0.197 | 4.35x | 14.8/30.8/37.4% | 1.4/5.1% | 3 |

> max-num-nodes=10: decode_failures 49

> max-num-nodes=250: decode_failures 56

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.986 | 0.986 | 0.691 | 1.53x | 22.4/36.4/39.5% | 2.1/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.986 | 0.986 | 0.691 | 1.53x | 22.4/36.4/39.5% | 2.1/5.4% | 3 |
| constrained | 1 | 0.837 | 0.828 | 0.009 | - | - | 0.941 | 0.942 | 0.536 | 3.03x | 42.7/65.0/68.8% | 4.1/10.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.711 | 0.700 | 0.011 | - | - | 0.813 | 0.852 | 0.464 | 5.43x | 60.3/75.2/79.4% | 4.0/12.4% | 3 |
| 25 | 1 | 0.711 | 0.700 | 0.011 | - | - | 0.813 | 0.852 | 0.464 | 5.43x | 60.3/75.2/79.4% | 4.0/12.4% | 3 |
| 100 | 1 | 0.711 | 0.700 | 0.011 | - | - | 0.813 | 0.852 | 0.464 | 5.43x | 60.3/75.2/79.4% | 4.0/12.4% | 3 |
| 2000 | 1 | 0.711 | 0.700 | 0.011 | - | - | 0.813 | 0.852 | 0.464 | 5.43x | 60.3/75.2/79.4% | 4.0/12.4% | 3 |

> warm-num-nodes=0: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 97

> warm-num-nodes=25: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 97

> warm-num-nodes=100: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 97

> warm-num-nodes=2000: queue drops 19.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 97

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.1 | 1 | 0.796 | 0.783 | 0.013 | - | - | 0.966 | 0.968 | 0.524 | 1.17x | 16.6/25.4/28.5% | 1.6/5.1% | 3 |
| 0.2 | 1 | 0.707 | 0.674 | 0.033 | - | - | 0.941 | 0.943 | 0.439 | 1.07x | 15.3/23.6/26.4% | 1.5/4.6% | 3 |
| 0.3 | 1 | 0.599 | 0.564 | 0.034 | - | - | 0.830 | 0.905 | 0.321 | 0.99x | 14.3/22.4/24.8% | 1.4/4.1% | 3 |

> burst-loss=0.3: decode_failures 35

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.1 | 1 | 0.868 | 0.863 | 0.005 | - | - | 0.981 | 0.983 | 0.554 | 1.28x | 18.1/27.3/30.3% | 1.8/5.4% | 3 |
| 0.2 | 1 | 0.832 | 0.826 | 0.006 | - | - | 0.965 | 0.966 | 0.522 | 1.31x | 18.8/28.0/30.7% | 1.9/5.1% | 3 |
| 0.3 | 1 | 0.799 | 0.788 | 0.011 | - | - | 0.966 | 0.969 | 0.424 | 1.39x | 20.3/30.2/32.5% | 2.1/5.1% | 3 |

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.1 | 1 | 0.798 | 0.789 | 0.009 | - | - | 0.956 | 0.973 | 0.536 | 1.15x | 16.1/24.8/27.6% | 1.6/5.0% | 3 |
| 0.2 | 1 | 0.673 | 0.653 | 0.020 | - | - | 0.859 | 0.941 | 0.403 | 1.09x | 15.5/24.0/26.6% | 1.5/4.7% | 3 |
| 0.3 | 1 | 0.573 | 0.548 | 0.025 | - | - | 0.729 | 0.895 | 0.350 | 1.01x | 14.3/22.9/25.4% | 1.5/4.2% | 3 |

> burst-loss=0.1: decode_failures 7

> burst-loss=0.2: decode_failures 25

> burst-loss=0.3: decode_failures 26

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.868 | 0.868 | 0.000 | - | - | 0.978 | 0.979 | 0.603 | 1.58x | 22.4/34.2/37.7% | 2.2/7.0% | 3 |
| directed-with-late-flood | 1 | 0.874 | 0.874 | 0.000 | - | - | 0.983 | 0.984 | 0.599 | 1.42x | 20.0/30.8/34.4% | 1.9/6.4% | 3 |
| m4-early-flood | 1 | 0.872 | 0.872 | 0.000 | - | - | 0.978 | 0.979 | 0.608 | 1.43x | 20.2/31.0/34.7% | 1.9/6.5% | 3 |

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.919 | 0.917 | 0.002 | - | - | 0.982 | 0.983 | 0.660 | 0.72x | 9.6/13.0/13.8% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.25 | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.981 | 0.981 | 0.542 | 1.20x | 16.7/25.7/28.5% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.909 | 0.906 | 0.003 | - | - | 0.992 | 0.992 | 0.590 | 0.97x | 14.4/18.9/21.6% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.919 | 0.916 | 0.004 | - | - | 0.994 | 0.994 | 0.765 | 0.82x | 12.2/15.5/17.8% | 1.4/3.1% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.25 | 1 | 0.904 | 0.900 | 0.004 | - | - | 0.977 | 0.977 | 0.526 | 1.17x | 16.6/25.1/27.9% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.912 | 0.908 | 0.004 | - | - | 0.993 | 0.995 | 0.590 | 0.95x | 14.5/18.4/21.5% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.924 | 0.921 | 0.003 | - | - | 0.991 | 0.991 | 0.791 | 0.79x | 12.0/15.1/17.8% | 1.3/3.1% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.911 | 0.911 | 0.001 | - | - | 0.990 | 0.990 | 0.676 | 0.63x | 9.0/14.4/16.5% | 0.9/3.0% | 3 |
| signing=true | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.922 | 0.921 | 0.001 | - | - | 0.982 | 0.984 | 0.667 | 0.72x | 10.0/14.0/15.4% | 1.2/2.3% | 3 |
| 2.5 | 1 | 0.917 | 0.915 | 0.001 | - | - | 0.982 | 0.983 | 0.648 | 0.74x | 10.2/14.3/15.6% | 1.3/2.3% | 3 |
| 2.6 | 1 | 0.922 | 0.921 | 0.001 | - | - | 0.986 | 0.987 | 0.640 | 0.71x | 10.1/14.3/15.8% | 1.2/2.4% | 3 |
| 2.7 | 1 | 0.935 | 0.935 | 0.001 | - | - | 0.985 | 0.986 | 0.666 | 0.74x | 10.7/16.3/18.5% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.901 | 0.900 | 0.001 | - | - | 0.987 | 0.987 | 0.662 | 0.82x | 11.3/17.6/19.7% | 1.1/3.6% | 3 |
| 900 | 1 | 0.861 | 0.856 | 0.005 | - | - | 0.977 | 0.978 | 0.613 | 1.94x | 27.2/41.0/45.5% | 2.7/8.7% | 3 |
| 300 | 1 | 0.603 | 0.587 | 0.016 | - | - | 0.792 | 0.832 | 0.344 | 4.22x | 55.0/75.5/77.4% | 6.0/16.5% | 3 |

> broadcast-interval-s=300: queue drops 11.2% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 13

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.942 | 0.941 | 0.001 | - | - | 0.991 | 0.992 | 0.777 | 0.88x | 11.9/17.9/20.0% | 1.3/3.6% | 3 |
| 900 | 1 | 0.907 | 0.903 | 0.004 | - | - | 0.979 | 0.979 | 0.712 | 2.20x | 29.6/43.1/47.6% | 3.1/8.8% | 3 |
| 300 | 1 | 0.586 | 0.576 | 0.010 | - | - | 0.738 | 0.747 | 0.418 | 4.68x | 59.0/77.0/79.2% | 7.1/16.9% | 3 |

> broadcast-interval-s=300: queue drops 16.2% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 5

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.899 | 0.897 | 0.002 | - | - | 0.987 | 0.988 | 0.654 | 1.11x | 15.4/24.0/27.0% | 1.5/5.0% | 3 |
| sinusoid | 1 | 0.896 | 0.894 | 0.002 | - | - | 0.982 | 0.982 | 0.659 | 1.11x | 15.5/24.0/26.8% | 1.5/4.9% | 3 |
| commuter | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.861 | 0.856 | 0.005 | - | - | 0.977 | 0.978 | 0.613 | 1.94x | 27.2/41.0/45.5% | 2.7/8.7% | 3 |
| 3600 | 1 | 0.901 | 0.900 | 0.001 | - | - | 0.987 | 0.987 | 0.662 | 0.82x | 11.3/17.6/19.7% | 1.1/3.6% | 3 |
| 10800 | 1 | 0.914 | 0.912 | 0.001 | - | - | 0.991 | 0.991 | 0.689 | 0.55x | 7.6/11.6/13.1% | 0.8/2.4% | 3 |
| 43200 | 1 | 0.917 | 0.916 | 0.001 | - | - | 0.992 | 0.992 | 0.694 | 0.39x | 5.4/8.3/9.3% | 0.5/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.25 | 1 | 0.881 | 0.877 | 0.004 | - | - | 0.982 | 0.984 | 0.614 | 1.28x | 17.9/27.4/30.7% | 1.8/5.7% | 3 |
| 1.0 | 1 | 0.879 | 0.876 | 0.003 | - | - | 0.977 | 0.979 | 0.619 | 1.41x | 19.8/30.3/34.0% | 1.9/6.4% | 3 |
| 4.0 | 1 | 0.858 | 0.852 | 0.006 | - | - | 0.969 | 0.972 | 0.590 | 1.81x | 25.8/39.4/44.0% | 2.5/8.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.711 | 0.700 | 0.011 | - | - | 0.813 | 0.852 | 0.464 | 5.43x | 60.3/75.2/79.4% | 4.0/12.4% | 3 |
| 1.0 | 1 | 0.627 | 0.616 | 0.012 | - | - | 0.740 | 0.782 | 0.399 | 5.97x | 64.4/76.7/80.1% | 4.5/13.9% | 3 |

> traceroute-per-hour=0.0: queue drops 19.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 97

> traceroute-per-hour=1.0: queue drops 31.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 102

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.715 | 0.689 | 0.026 | - | - | 0.932 | 0.935 | 0.140 | 1.31x | 19.5/27.1/30.5% | 3.2/6.8% | 3 |
| 60 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 90 | 1 | 0.954 | 0.953 | 0.002 | - | - | 0.996 | 0.996 | 0.806 | 1.65x | 21.4/32.9/35.9% | 1.5/5.1% | 3 |
| 120 | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.996 | 0.996 | 0.800 | 2.05x | 25.5/39.2/43.5% | 1.4/5.2% | 3 |
| 150 | 1 | 0.967 | 0.966 | 0.002 | - | - | 0.996 | 0.996 | 0.832 | 2.71x | 30.9/46.7/51.6% | 1.4/6.0% | 3 |

> nodes=40: decode_failures 1

> nodes=120: misdecodes 1

> nodes=150: misdecodes 1

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 120 | 1 | 0.787 | 0.783 | 0.004 | - | - | 0.971 | 0.972 | 0.431 | 2.27x | 16.7/27.8/33.9% | 1.6/5.5% | 3 |
| 250 | 1 | 0.542 | 0.531 | 0.011 | - | - | 0.828 | 0.837 | 0.188 | 4.89x | 16.4/35.5/42.2% | 1.6/5.9% | 3 |
| 500 | 1 | 0.302 | 0.297 | 0.004 | - | - | 0.445 | 0.450 | 0.110 | 10.05x | 17.6/33.2/55.1% | 1.7/6.0% | 3 |

> nodes=120: misdecodes 1

> nodes=250: decode_failures 129

> nodes=500: decode_failures 209

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.791 | 0.787 | 0.004 | - | - | 0.982 | 0.982 | 0.414 | 2.17x | 15.7/26.3/32.1% | 1.5/5.2% | 3 |
| 250 | 1 | 0.543 | 0.532 | 0.011 | - | - | 0.830 | 0.830 | 0.198 | 4.51x | 15.4/32.1/38.8% | 1.4/5.4% | 3 |
| 500 | 1 | 0.305 | 0.301 | 0.004 | - | - | 0.441 | 0.442 | 0.115 | 9.16x | 16.2/30.8/49.5% | 1.5/5.4% | 3 |

> nodes=500: decode_failures 7

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.888 | 0.884 | 0.004 | - | - | 0.984 | 0.985 | 0.623 | 1.19x | 16.7/25.5/28.7% | 1.7/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.886 | 0.877 | 0.009 | - | - | 0.979 | 0.983 | 0.657 | 1.08x | 16.5/23.2/24.6% | 1.7/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.910 | 0.908 | 0.002 | - | - | 0.981 | 0.982 | 0.683 | 1.26x | 17.2/26.5/29.6% | 1.8/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.915 | 0.908 | 0.007 | - | - | 0.980 | 0.983 | 0.708 | 1.23x | 19.0/26.5/28.9% | 2.1/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.05 | 1 | 0.898 | 0.892 | 0.006 | - | - | 0.981 | 0.983 | 0.623 | 1.33x | 19.3/31.1/33.8% | 1.7/5.3% | 3 |
| 0.1 | 1 | 0.902 | 0.898 | 0.004 | - | - | 0.982 | 0.983 | 0.619 | 1.48x | 22.3/36.5/40.1% | 1.9/5.4% | 3 |
| 0.2 | 1 | 0.898 | 0.889 | 0.009 | - | - | 0.983 | 0.983 | 0.603 | 1.67x | 25.2/42.9/45.2% | 2.4/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| local-typical | 1 | 0.797 | 0.791 | 0.006 | - | - | 0.800 | 0.935 | 0.000 | 1.45x | 17.3/24.0/31.4% | 2.2/5.4% | 3 |
| event | 1 | 0.547 | 0.543 | 0.004 | - | - | 0.765 | 0.767 | 0.000 | 1.52x | 10.1/19.5/25.5% | 2.3/5.0% | 3 |
| backbone | 1 | 0.979 | 0.979 | 0.000 | - | - | 0.999 | 0.999 | 0.929 | 0.96x | 27.2/33.9/35.2% | 0.9/5.6% | 3 |

> siting-mix=local-typical: decode_failures 6

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.871 | 0.864 | 0.006 | - | - | 0.972 | 0.977 | 0.558 | 1.39x | 25.4/34.3/37.1% | 3.3/7.7% | 3 |
| 60 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 90 | 1 | 0.854 | 0.847 | 0.007 | - | - | 0.981 | 0.981 | 0.475 | 1.69x | 16.6/28.5/30.6% | 1.6/5.1% | 3 |
| 120 | 1 | 0.787 | 0.783 | 0.004 | - | - | 0.971 | 0.972 | 0.431 | 2.27x | 16.7/27.8/33.9% | 1.6/5.5% | 3 |
| 150 | 1 | 0.683 | 0.669 | 0.015 | - | - | 0.937 | 0.938 | 0.289 | 2.83x | 16.2/29.5/35.5% | 1.5/6.1% | 3 |

> nodes=120: misdecodes 1

> nodes=150: decode_failures 1

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 1.25 | 1 | 0.747 | 0.733 | 0.014 | - | - | 0.937 | 0.941 | 0.317 | 1.39x | 14.7/23.9/28.6% | 2.2/5.1% | 3 |
| 1.5 | 1 | 0.541 | 0.530 | 0.011 | - | - | 0.759 | 0.762 | 0.156 | 1.49x | 10.3/21.6/27.7% | 2.1/4.9% | 3 |
| 2.0 | 1 | 0.221 | 0.218 | 0.003 | - | - | 0.464 | 0.467 | 0.000 | 1.27x | 6.4/18.1/23.5% | 1.7/5.4% | 3 |

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| clustered | 1 | 0.882 | 0.881 | 0.001 | - | - | 0.952 | 0.952 | 0.000 | 1.01x | 34.3/38.9/40.2% | 1.0/5.6% | 3 |
| corridor | 1 | 0.652 | 0.640 | 0.012 | - | - | 0.753 | 0.753 | 0.439 | 1.23x | 16.8/21.2/24.1% | 1.8/5.1% | 3 |
| hub | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.997 | 0.997 | 0.798 | 1.19x | 29.5/37.4/38.3% | 1.6/5.6% | 3 |

> topology=clustered: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.874 | 0.874 | 0.000 | - | - | 0.983 | 0.984 | 0.599 | 1.42x | 20.0/30.8/34.4% | 1.9/6.4% | 3 |
| True | 1 | 0.867 | 0.867 | 0.000 | - | - | 0.976 | 0.978 | 0.598 | 1.44x | 20.2/30.8/34.6% | 2.0/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.867 | 0.867 | 0.000 | - | - | 0.976 | 0.978 | 0.598 | 1.44x | 20.2/30.8/34.6% | 2.0/6.5% | 3 |
| m4-early-flood | 1 | 0.879 | 0.879 | 0.000 | - | - | 0.977 | 0.978 | 0.611 | 1.43x | 20.1/30.9/34.5% | 1.9/6.5% | 3 |

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.883 | 0.883 | 0.000 | - | - | 0 | 0.000 | 0.628 | 1.17x | 16.3/25.2/28.3% | 1.6/5.2% | 3 |
| chain | 1 | 0.888 | 0.886 | 0.002 | - | - | 0.960 | 0.989 | 0.620 | 1.36x | 19.4/29.8/33.1% | 1.9/6.2% | 3 |
| sr | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| True | 1 | 0.892 | 0.888 | 0.003 | - | - | 0.985 | 0.985 | 0.640 | 1.24x | 17.4/26.6/29.7% | 1.7/5.5% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.996 | 0.996 | 0.800 | 2.05x | 25.5/39.2/43.5% | 1.4/5.2% | 3 |
| True | 1 | 0.960 | 0.958 | 0.002 | - | - | 0.998 | 0.998 | 0.806 | 2.07x | 25.5/39.0/43.4% | 1.4/5.2% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.283 | 0.279 | 0.004 | - | - | 0.582 | 0.582 | 0.000 | 0.06x | 0.3/0.9/1.3% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.612 | 0.598 | 0.014 | - | - | 0.845 | 0.846 | 0.110 | 0.32x | 2.6/5.1/6.8% | 0.5/1.3% | 3 |
| LONG_TURBO | 1 | 0.836 | 0.823 | 0.013 | - | - | 0.966 | 0.967 | 0.416 | 1.25x | 14.3/23.5/26.7% | 1.9/5.1% | 3 |

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 0.25 | 1 | 0.899 | 0.897 | 0.002 | - | - | 0.978 | 0.980 | 0.661 | 0.95x | 16.1/23.6/26.6% | 1.2/4.8% | 3 |
| 1.0 | 1 | 0.936 | 0.933 | 0.002 | - | - | 0.994 | 0.995 | 0.778 | 0.83x | 22.8/28.9/31.3% | 1.0/5.2% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.516 | 0.512 | 0.005 | - | - | 0.740 | 0.741 | 0.114 | 0.19x | 1.3/2.5/3.5% | 0.3/0.7% | 3 |
| LONG_FAST | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| LITE_FAST | 1 | 0.843 | 0.840 | 0.003 | - | - | 0.968 | 0.969 | 0.507 | 0.94x | 12.5/18.0/20.9% | 1.4/4.0% | 3 |
| NARROW_SLOW | 1 | 0.849 | 0.842 | 0.007 | - | - | 0.985 | 0.987 | 0.517 | 1.19x | 16.5/24.0/27.0% | 1.7/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| temporal | 1 | 0.826 | 0.818 | 0.009 | - | - | 0.975 | 0.977 | 0.447 | 1.23x | 16.7/25.2/27.5% | 1.8/5.4% | 3 |
| transient | 1 | 0.895 | 0.891 | 0.004 | - | - | 0.993 | 0.993 | 0.633 | 1.21x | 16.9/26.0/28.9% | 1.6/5.4% | 3 |
| periodic | 1 | 0.704 | 0.701 | 0.004 | - | - | 0.793 | 0.795 | 0.483 | 1.13x | 15.9/24.3/26.9% | 1.6/4.7% | 3 |

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.516 | 0.512 | 0.005 | - | - | 0.740 | 0.741 | 0.114 | 0.19x | 1.3/2.5/3.5% | 0.3/0.7% | 3 |
| LONG_FAST | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| LONG_MODERATE | 1 | 0.867 | 0.860 | 0.006 | - | - | 0.949 | 0.952 | 0.637 | 3.08x | 49.8/61.0/64.5% | 4.0/13.3% | 3 |

> preset=LONG_MODERATE: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.116 | 0.114 | 0.003 | - | - | 0.272 | 0.280 | 0.000 | 0.01x | 0.0/0.2/0.3% | 0.0/0.1% | 3 |
| SHORT_TURBO | 1 | 0.283 | 0.279 | 0.004 | - | - | 0.582 | 0.582 | 0.000 | 0.06x | 0.3/0.9/1.3% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| LONG_TURBO | 1 | 0.836 | 0.823 | 0.013 | - | - | 0.966 | 0.967 | 0.416 | 1.25x | 14.3/23.5/26.7% | 1.9/5.1% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.887 | 0.882 | 0.005 | - | - | 0.980 | 0.980 | 0.653 | 1.69x | 22.7/33.4/35.9% | 2.4/7.1% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.841 | 0.838 | 0.003 | - | - | 0.937 | 0.937 | 0.583 | 1.19x | 16.7/25.6/28.7% | 1.6/5.2% | 3 |
| 10000 | 1 | 0.704 | 0.701 | 0.004 | - | - | 0.793 | 0.795 | 0.483 | 1.13x | 15.9/24.3/26.9% | 1.6/4.7% | 3 |
| 4000 | 1 | 0.506 | 0.501 | 0.004 | - | - | 0.589 | 0.618 | 0.276 | 1.02x | 14.3/22.1/24.0% | 1.6/3.8% | 3 |
| 2000 | 1 | 0.132 | 0.132 | 0.000 | - | - | 0.156 | 0.223 | 0.059 | 0.73x | 10.7/16.3/17.7% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 1

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.541 | 0.530 | 0.011 | - | - | 0.759 | 0.762 | 0.156 | 1.49x | 10.3/21.6/27.7% | 2.1/4.9% | 3 |
| 1.0 | 1 | 0.768 | 0.754 | 0.014 | - | - | 0.883 | 0.883 | 0.548 | 1.02x | 17.3/26.0/28.3% | 1.4/4.6% | 3 |

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 22 | 1 | 0.551 | 0.534 | 0.016 | - | - | 0.751 | 0.752 | 0.122 | 1.50x | 10.8/21.8/28.3% | 2.2/5.0% | 3 |
| 17 | 1 | 0.252 | 0.248 | 0.004 | - | - | 0.500 | 0.500 | 0.000 | 1.36x | 6.7/19.2/24.0% | 1.9/5.6% | 3 |
| 14 | 1 | 0.152 | 0.146 | 0.006 | - | - | 0.391 | 0.393 | 0.000 | 0.94x | 3.6/14.5/19.1% | 1.2/4.5% | 3 |

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.996 | 0.996 | 0.800 | 2.05x | 25.5/39.2/43.5% | 1.4/5.2% | 3 |
| True | 1 | 0.953 | 0.952 | 0.002 | - | - | 0.996 | 0.997 | 0.772 | 2.38x | 28.9/43.2/47.4% | 1.7/5.7% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.910 | 0.905 | 0.005 | - | - | 0.991 | 0.991 | 0.642 | 1.33x | 18.7/31.5/33.9% | 1.8/5.4% | 3 |
| True | 1 | 0.918 | 0.914 | 0.005 | - | - | 0.982 | 0.983 | 0.700 | 1.43x | 19.9/33.0/35.2% | 2.0/5.5% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| random | 1 | 0.894 | 0.885 | 0.009 | - | - | 0.977 | 0.978 | 0.658 | 1.19x | 16.6/25.2/28.4% | 1.6/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.748 | 0.713 | 0.035 | - | - | 0.962 | 0.963 | 0.413 | 0.92x | 13.2/20.9/24.5% | 1.2/4.9% | 3 |
| 7 | 1 | 0.925 | 0.924 | 0.001 | - | - | 0.980 | 0.980 | 0.746 | 1.34x | 18.1/26.9/30.2% | 1.9/5.4% | 3 |
| 15 | 1 | 0.944 | 0.944 | 0.000 | - | - | 0.985 | 0.985 | 0.799 | 1.34x | 18.3/26.7/30.0% | 1.9/5.4% | 3 |
| 32 | 1 | 0.943 | 0.943 | 0.000 | - | - | 0.986 | 0.986 | 0.779 | 1.35x | 18.2/27.0/30.2% | 1.9/5.5% | 3 |

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.748 | 0.713 | 0.035 | - | - | 0.962 | 0.963 | 0.413 | 0.92x | 13.2/20.9/24.5% | 1.2/4.9% | 3 |
| 5 | 1 | 0.882 | 0.878 | 0.005 | - | - | 0.974 | 0.977 | 0.635 | 1.24x | 17.1/25.9/29.1% | 1.7/5.4% | 3 |
| 7 | 1 | 0.925 | 0.924 | 0.001 | - | - | 0.980 | 0.980 | 0.746 | 1.34x | 18.1/26.9/30.2% | 1.9/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.888 | 0.888 | 0.000 | - | - | 0.964 | 0.987 | 0.630 | 1.19x | 16.6/25.6/28.8% | 1.6/5.4% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 6

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.748 | 0.713 | 0.035 | - | - | 0.962 | 0.963 | 0.413 | 0.92x | 13.2/20.9/24.5% | 1.2/4.9% | 3 |
| True | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| BALANCED | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| STRICT | 1 | 0.803 | 0.803 | 0.000 | - | - | 0.903 | 0.904 | 0.544 | 1.30x | 18.1/27.8/30.9% | 1.8/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| dm | 1 | 0.896 | 0.893 | 0.003 | - | - | 0.989 | 0.989 | 0.645 | 1.19x | 16.8/25.8/28.8% | 1.7/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.890 | 0.887 | 0.003 | - | - | 0.986 | 0.987 | 0.629 | 1.19x | 16.6/25.7/28.8% | 1.6/5.4% | 3 |
| local | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| time | 1 | 0.883 | 0.881 | 0.003 | - | - | 0.978 | 0.979 | 0.622 | 1.24x | 17.5/26.8/29.9% | 1.7/5.6% | 3 |
| window | 1 | 0.891 | 0.887 | 0.004 | - | - | 0.989 | 0.990 | 0.625 | 1.19x | 16.6/25.5/28.6% | 1.6/5.3% | 3 |

> bucket-mode=global: misdecodes 35

> bucket-mode=time: misdecodes 40

> bucket-mode=window: misdecodes 27

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.979 | 0.980 | 0.625 | 1.34x | 19.2/29.1/32.2% | 1.8/6.2% | 3 |
| 1800 | 1 | 0.883 | 0.881 | 0.003 | - | - | 0.978 | 0.979 | 0.622 | 1.24x | 17.5/26.8/29.9% | 1.7/5.6% | 3 |
| 3600 | 1 | 0.890 | 0.887 | 0.003 | - | - | 0.981 | 0.983 | 0.631 | 1.22x | 17.1/26.1/29.2% | 1.7/5.4% | 3 |

> time-bucket-s=600: misdecodes 117

> time-bucket-s=1800: misdecodes 40

> time-bucket-s=3600: misdecodes 19

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| interval | 1 | 0.876 | 0.872 | 0.004 | - | - | 0.976 | 0.978 | 0.619 | 1.61x | 23.7/36.1/40.0% | 2.2/8.5% | 3 |
| aimd | 1 | 0.885 | 0.884 | 0.000 | - | - | 0.958 | 0.980 | 0.625 | 1.19x | 16.7/25.6/28.7% | 1.6/5.3% | 3 |
| bucket+interval | 1 | 0.880 | 0.876 | 0.004 | - | - | 0.983 | 0.984 | 0.619 | 1.63x | 23.8/36.5/40.3% | 2.2/8.6% | 3 |

> trigger=interval: misdecodes 20

> trigger=aimd: misdecodes 2

> trigger=bucket+interval: misdecodes 23

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.889 | 0.886 | 0.003 | - | - | 0.984 | 0.985 | 0.636 | 1.21x | 17.0/26.0/29.2% | 1.7/5.4% | 3 |
| 8 | 1 | 0.888 | 0.884 | 0.004 | - | - | 0.984 | 0.985 | 0.630 | 1.19x | 16.6/25.6/28.6% | 1.6/5.3% | 3 |
| 16 | 1 | 0.888 | 0.885 | 0.003 | - | - | 0.985 | 0.985 | 0.619 | 1.18x | 16.3/25.1/28.2% | 1.6/5.2% | 3 |
| 32 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 50 | 1 | 0.886 | 0.883 | 0.003 | - | - | 0.979 | 0.980 | 0.642 | 1.19x | 16.6/25.6/28.7% | 1.6/5.3% | 3 |

> capacity=4: decode_failures 54

> capacity=8: decode_failures 5

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.889 | 0.886 | 0.003 | - | - | 0.984 | 0.985 | 0.636 | 1.21x | 17.0/26.0/29.2% | 1.7/5.4% | 3 |
| 8 | 1 | 0.888 | 0.884 | 0.004 | - | - | 0.984 | 0.985 | 0.630 | 1.19x | 16.6/25.6/28.6% | 1.6/5.3% | 3 |
| 16 | 1 | 0.888 | 0.885 | 0.003 | - | - | 0.985 | 0.985 | 0.619 | 1.18x | 16.3/25.1/28.2% | 1.6/5.2% | 3 |
| 32 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 50 | 1 | 0.886 | 0.883 | 0.003 | - | - | 0.979 | 0.980 | 0.642 | 1.19x | 16.6/25.6/28.7% | 1.6/5.3% | 3 |

> capacity=4: decode_failures 54

> capacity=8: decode_failures 5

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.893 | 0.891 | 0.002 | - | - | 0.982 | 0.985 | 0.622 | 1.18x | 16.3/25.1/28.1% | 1.6/5.2% | 3 |
| 16 | 1 | 0.889 | 0.886 | 0.003 | - | - | 0.980 | 0.982 | 0.645 | 1.19x | 16.5/25.6/28.7% | 1.6/5.3% | 3 |
| 32 | 1 | 0.891 | 0.887 | 0.004 | - | - | 0.989 | 0.990 | 0.625 | 1.19x | 16.6/25.5/28.6% | 1.6/5.3% | 3 |

> capacity=8: misdecodes 32

> capacity=8: decode_failures 2

> capacity=16: misdecodes 20

> capacity=32: misdecodes 27

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.880 | 0.876 | 0.004 | - | - | 0.983 | 0.984 | 0.619 | 1.63x | 23.8/36.5/40.3% | 2.2/8.6% | 3 |
| 02-06 | 1 | 0.891 | 0.889 | 0.002 | - | - | 0.973 | 0.990 | 0.639 | 1.24x | 17.6/26.9/30.0% | 1.7/5.7% | 3 |
| 00-08 | 1 | 0.890 | 0.888 | 0.002 | - | - | 0.977 | 0.990 | 0.614 | 1.29x | 18.5/28.3/31.3% | 1.8/6.1% | 3 |

> catch-up-hours=: misdecodes 23

> catch-up-hours=02-06: decode_failures 14

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 14

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.894 | 0.893 | 0.000 | - | - | 0.973 | 0.974 | 0.638 | 1.20x | 16.7/25.9/28.9% | 1.6/5.3% | 3 |
| 2 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 3 | 1 | 0.895 | 0.888 | 0.007 | - | - | 0.989 | 0.990 | 0.625 | 1.21x | 16.8/25.9/28.9% | 1.6/5.3% | 3 |
| 4 | 1 | 0.914 | 0.883 | 0.031 | - | - | 0.974 | 0.993 | 0.680 | 1.24x | 17.0/26.0/29.1% | 1.7/5.3% | 3 |

> hops-apart=4: decode_failures 14

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.894 | 0.893 | 0.000 | - | - | 0.973 | 0.974 | 0.638 | 1.20x | 16.7/25.9/28.9% | 1.6/5.3% | 3 |
| 2 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 3 | 1 | 0.895 | 0.888 | 0.007 | - | - | 0.989 | 0.990 | 0.625 | 1.21x | 16.8/25.9/28.9% | 1.6/5.3% | 3 |
| 4 | 1 | 0.914 | 0.883 | 0.031 | - | - | 0.974 | 0.993 | 0.680 | 1.24x | 17.0/26.0/29.1% | 1.7/5.3% | 3 |
| 5 | 1 | 0.914 | 0.883 | 0.031 | - | - | 0.974 | 0.993 | 0.680 | 1.24x | 17.0/26.0/29.1% | 1.7/5.3% | 3 |

> hops-apart=4: decode_failures 14

> hops-apart=5: decode_failures 14

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.989 | 0.989 | 0.634 | 1.21x | 16.8/26.0/29.1% | 1.7/5.4% | 3 |
| 30 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 120 | 1 | 0.888 | 0.885 | 0.003 | - | - | 0.983 | 0.984 | 0.621 | 1.21x | 16.9/26.1/29.2% | 1.7/5.4% | 3 |
| 600 | 1 | 0.891 | 0.888 | 0.003 | - | - | 0.988 | 0.988 | 0.624 | 1.20x | 16.7/25.6/28.8% | 1.6/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.989 | 0.989 | 0.634 | 1.21x | 16.8/26.0/29.1% | 1.7/5.4% | 3 |
| 30 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 120 | 1 | 0.888 | 0.885 | 0.003 | - | - | 0.983 | 0.984 | 0.621 | 1.21x | 16.9/26.1/29.2% | 1.7/5.4% | 3 |
| 600 | 1 | 0.891 | 0.888 | 0.003 | - | - | 0.988 | 0.988 | 0.624 | 1.20x | 16.7/25.6/28.8% | 1.6/5.4% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.912 | 0.883 | 0.029 | - | - | 0.963 | 0.991 | 0.661 | 1.24x | 17.1/26.3/29.4% | 1.7/5.3% | 3 |
| routers | 1 | 0.890 | 0.889 | 0.001 | - | - | 0.985 | 0.985 | 0.641 | 1.21x | 16.8/26.1/29.2% | 1.6/5.4% | 3 |
| alternate-routers | 1 | 0.885 | 0.884 | 0.001 | - | - | 0.975 | 0.976 | 0.616 | 1.20x | 16.6/25.7/28.7% | 1.6/5.3% | 3 |
| beside-router | 1 | 0.888 | 0.886 | 0.001 | - | - | 0.983 | 0.984 | 0.637 | 1.22x | 17.0/26.3/29.2% | 1.6/5.4% | 3 |
| random-clients | 1 | 0.896 | 0.887 | 0.009 | - | - | 0.968 | 0.971 | 0.635 | 1.21x | 16.6/25.6/28.7% | 1.7/5.4% | 3 |
| hops-apart | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

> place=spread: decode_failures 36

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.912 | 0.883 | 0.029 | - | - | 0.963 | 0.991 | 0.661 | 1.24x | 17.1/26.3/29.4% | 1.7/5.3% | 3 |
| routers | 1 | 0.890 | 0.889 | 0.001 | - | - | 0.985 | 0.985 | 0.641 | 1.21x | 16.8/26.1/29.2% | 1.6/5.4% | 3 |
| alternate-routers | 1 | 0.885 | 0.884 | 0.001 | - | - | 0.975 | 0.976 | 0.616 | 1.20x | 16.6/25.7/28.7% | 1.6/5.3% | 3 |
| beside-router | 1 | 0.888 | 0.886 | 0.001 | - | - | 0.983 | 0.984 | 0.637 | 1.22x | 17.0/26.3/29.2% | 1.6/5.4% | 3 |
| random-clients | 1 | 0.896 | 0.887 | 0.009 | - | - | 0.968 | 0.971 | 0.635 | 1.21x | 16.6/25.6/28.7% | 1.7/5.4% | 3 |
| hops-apart | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

> place=spread: decode_failures 36

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| broadcast | 1 | 0.900 | 0.883 | 0.017 | - | - | 0.980 | 0.981 | 0.668 | 1.25x | 17.5/26.8/30.0% | 1.7/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| heard | 1 | 0.891 | 0.887 | 0.004 | - | - | 0.984 | 0.985 | 0.644 | 1.22x | 17.1/26.4/29.4% | 1.7/5.5% | 3 |

> replay-ordering=heard: misdecodes 25

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.900 | 0.883 | 0.017 | - | - | 0.980 | 0.981 | 0.668 | 1.25x | 17.5/26.8/30.0% | 1.7/5.6% | 3 |
| heard | 1 | 0.895 | 0.876 | 0.018 | - | - | 0.975 | 0.976 | 0.666 | 1.25x | 17.5/26.8/29.8% | 1.7/5.5% | 3 |

> replay-ordering=heard: misdecodes 19

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| enum | 1 | 0.887 | 0.883 | 0.004 | - | - | 0.980 | 0.982 | 0.645 | 1.20x | 16.9/26.0/29.1% | 1.6/5.5% | 3 |
| hybrid | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.890 | 0.889 | 0.001 | - | - | 0.985 | 0.985 | 0.641 | 1.21x | 16.8/26.1/29.2% | 1.6/5.4% | 3 |
| 6 | 1 | 0.884 | 0.881 | 0.003 | - | - | 0.980 | 0.981 | 0.625 | 1.25x | 17.5/27.2/30.2% | 1.7/5.7% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.884 | 0.882 | 0.002 | - | - | 0.976 | 0.977 | 0.632 | 1.20x | 16.6/25.7/28.8% | 1.6/5.3% | 2 |
| 3 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 5 | 1 | 0.889 | 0.882 | 0.007 | - | - | 0.983 | 0.985 | 0.618 | 1.25x | 17.4/26.8/29.9% | 1.7/5.5% | 5 |
| 8 | 1 | 0.896 | 0.883 | 0.013 | - | - | 0.992 | 0.992 | 0.629 | 1.28x | 17.8/27.4/30.5% | 1.7/5.7% | 8 |

> servers=8: misdecodes 2

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.884 | 0.882 | 0.002 | - | - | 0.976 | 0.977 | 0.632 | 1.20x | 16.6/25.7/28.8% | 1.6/5.3% | 2 |
| 3 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 5 | 1 | 0.889 | 0.882 | 0.007 | - | - | 0.983 | 0.985 | 0.618 | 1.25x | 17.4/26.8/29.9% | 1.7/5.5% | 5 |
| 8 | 1 | 0.896 | 0.883 | 0.013 | - | - | 0.992 | 0.992 | 0.629 | 1.28x | 17.8/27.4/30.5% | 1.7/5.7% | 8 |

> servers=8: misdecodes 2

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| True | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.895 | 0.891 | 0.004 | - | - | 0.988 | 0.988 | 0.647 | 1.14x | 15.9/24.7/27.5% | 1.5/5.1% | 3 |
| 1 | 1 | 0.896 | 0.894 | 0.002 | - | - | 0.991 | 0.991 | 0.671 | 1.11x | 15.5/24.0/26.9% | 1.5/4.9% | 3 |
| 2 | 1 | 0.899 | 0.898 | 0.001 | - | - | 0.988 | 0.990 | 0.659 | 1.11x | 15.5/23.9/26.7% | 1.5/4.9% | 3 |
| 4 | 1 | 0.895 | 0.892 | 0.003 | - | - | 0.989 | 0.990 | 0.633 | 1.11x | 15.6/24.0/26.9% | 1.5/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.892 | 0.891 | 0.001 | - | - | 0.982 | 0.984 | 0.655 | 1.20x | 16.7/25.8/28.9% | 1.6/5.4% | 3 |
| 24 | 1 | 0.886 | 0.884 | 0.002 | - | - | 0.981 | 0.981 | 0.621 | 1.21x | 16.9/25.9/29.1% | 1.7/5.4% | 3 |
| 32 | 1 | 0.885 | 0.883 | 0.003 | - | - | 0.977 | 0.979 | 0.645 | 1.21x | 16.9/26.0/29.0% | 1.6/5.4% | 3 |
| 64 | 1 | 0.887 | 0.884 | 0.003 | - | - | 0.981 | 0.982 | 0.631 | 1.22x | 17.0/26.2/29.3% | 1.7/5.5% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.888 | 0.883 | 0.004 | - | - | 0.986 | 0.987 | 0.632 | 1.29x | 18.3/27.8/30.9% | 1.8/5.8% | 3 |
| 16 | 1 | 0.886 | 0.882 | 0.004 | - | - | 0.979 | 0.980 | 0.636 | 1.23x | 17.1/26.2/29.3% | 1.7/5.4% | 3 |
| 32 | 1 | 0.891 | 0.887 | 0.004 | - | - | 0.989 | 0.990 | 0.625 | 1.19x | 16.6/25.5/28.6% | 1.6/5.3% | 3 |

> window-size=8: misdecodes 134

> window-size=16: misdecodes 61

> window-size=32: misdecodes 27

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.996 | 0.996 | 0.800 | 2.05x | 25.5/39.2/43.5% | 1.4/5.2% | 3 |
| True | 1 | 0.712 | 0.696 | 0.016 | - | - | 0.841 | 0.850 | 0.474 | 5.47x | 60.6/75.3/79.5% | 4.1/12.6% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: queue drops 19.8% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 74

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.543 | 0.532 | 0.011 | - | - | 0.830 | 0.830 | 0.198 | 4.51x | 15.4/32.1/38.8% | 1.4/5.4% | 3 |
| truesize | 1 | 0.576 | 0.566 | 0.010 | - | - | 0.856 | 0.858 | 0.222 | 3.50x | 11.9/26.9/32.2% | 1.1/4.8% | 3 |

> congestion-input=truesize: decode_failures 2

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.964 | 0.963 | 0.001 | - | - | 0.999 | 1.000 | 0.801 | 1.86x | 23.0/35.4/39.4% | 1.3/4.7% | 3 |
| adaptive | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.996 | 0.996 | 0.800 | 2.05x | 25.5/39.2/43.5% | 1.4/5.2% | 3 |

> congestion-mode=adaptive: misdecodes 1

