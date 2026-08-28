# Sweep blocks-2026-08-28-4161552

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 4161552 · seeds 4161552
- **blocks** 87 run
- **compute** 11.3 h of simulator time across every cell
- **generated** 2026-08-28T15:51:29+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>83 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 35
- AD-badrouters: role-placement=random: decode_failures 1
- AD-badrouters: slower: 4.97 s per simulated hour against 2.42 over 7 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 54
- DB-hotstore-stress: max-num-nodes=250: decode_failures 4
- DB-warm: warm-num-nodes=0: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 95
- DB-warm: warm-num-nodes=25: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 95
- DB-warm: warm-num-nodes=100: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 95
- DB-warm: warm-num-nodes=2000: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 95
- DG-burst: burst-loss=0.2: decode_failures 5
- DG-burst: burst-loss=0.3: decode_failures 30
- DG-loss: extra-loss=0.3: decode_failures 16
- DG-outage: burst-loss=0.1: decode_failures 27
- DG-outage: burst-loss=0.2: decode_failures 29
- DG-outage: burst-loss=0.3: decode_failures 27
- DM-mode: dm-mode=m4-early-flood: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 12
- LD-chatty: broadcast-interval-s=300: decode_failures 18
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 19.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 95
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 29.3% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 79
- MS-density: nodes=150: decode_failures 1
- MS-hopscale: nodes=120: decode_failures 1
- MS-hopscale: nodes=250: decode_failures 58
- MS-hopscale: nodes=500: decode_failures 75
- MS-oversubscribed: nodes=500: decode_failures 59
- MS-router-late: router-late-fraction=0.2: misdecodes 1
- MS-siting: siting-mix=event: decode_failures 1
- MS-size: nodes=120: decode_failures 1
- MS-stretch: stretch=2.0: decode_failures 8
- MS-topology: topology=hub: decode_failures 2
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 2
- RF-noise: noise-profile=periodic: decode_failures 20
- RF-preset: preset=LONG_MODERATE: decode_failures 2
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 20
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 6
- RF-pulse: slower: 3.36 s per simulated hour against 1.6 over 7 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=14: decode_failures 2
- RT-hoplimit: hop-limit=3: decode_failures 7
- RT-hopspread: hop-limit=3: decode_failures 7
- RT-spread: hop-spread=False: decode_failures 7
- SF-bucket-mode: bucket-mode=global: misdecodes 38
- SF-bucket-mode: bucket-mode=time: misdecodes 34
- SF-bucket-mode: bucket-mode=window: misdecodes 11
- SF-bucket-time: time-bucket-s=600: misdecodes 98
- SF-bucket-time: time-bucket-s=1800: misdecodes 34
- SF-bucket-time: time-bucket-s=3600: misdecodes 3
- SF-cadence: trigger=interval: misdecodes 11
- SF-cadence: trigger=interval: decode_failures 8
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=aimd: decode_failures 1
- SF-cadence: trigger=bucket+interval: misdecodes 19
- SF-capacity-local: capacity=4: decode_failures 100
- SF-capacity-local: capacity=8: decode_failures 24
- SF-capacity: capacity=4: decode_failures 100
- SF-capacity: capacity=8: decode_failures 24
- SF-capacity-window: capacity=8: misdecodes 34
- SF-capacity-window: capacity=8: decode_failures 29
- SF-capacity-window: capacity=16: misdecodes 14
- SF-capacity-window: capacity=32: misdecodes 11
- SF-catchup: catch-up-hours=: misdecodes 19
- SF-catchup: catch-up-hours=02-06: decode_failures 46
- SF-catchup: catch-up-hours=00-08: decode_failures 46
- SF-hops-flat: hops-apart=4: decode_failures 15
- SF-hops-spread: hops-apart=4: decode_failures 15
- SF-hops-spread: hops-apart=5: decode_failures 28
- SF-place-flat: place=spread: decode_failures 39
- SF-place-spread: place=spread: decode_failures 39
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 4
- SF-replay-order: replay-ordering=heard: misdecodes 6
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 121
- SF-window-size: window-size=16: misdecodes 65
- SF-window-size: window-size=32: misdecodes 11
- TH-congestion: no-congestion-scaling=True: queue drops 18.8% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 101

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-pulse` | 3.36 | 1.6 | 2.10x | 7 |
| `AD-badrouters` | 4.97 | 2.42 | 2.05x | 7 |
| `SF-cadence` | 4.79 | 2.75 | 1.74x | 7 |
| `RF-stretch-duct` | 1.72 | 2.97 | 0.58x | 7 |
| `TH-congestion-input` | 9.97 | 18.3 | 0.54x | 7 |
| `RF-bw500` | 1.43 | 2.64 | 0.54x | 7 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.980 | 0.980 | 0.878 → 0.881 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.978 | 0.978 | 0.878 → 0.883 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.131 → 0.978 | 0.847 | 0.127 → 0.977 | 4.5x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **text** | 0.088 → 0.897 | 0.809 | 0.087 → 0.883 | 3.7x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **text** | 0.105 → 0.897 | 0.793 | 0.103 → 0.883 | 3.7x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.148 → 0.922 | 0.774 | 0.139 → 0.825 | 1e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.152 → 0.897 | 0.745 | 0.145 → 0.883 | 2.9x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.101 → 0.826 | 0.726 | 0.098 → 0.805 | 2.9x advert_bytes | down | 3 |
| `RF-bw500` | preset | **text** | 0.168 → 0.797 | 0.629 | 0.166 → 0.794 | 2.4x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.272 → 0.897 | 0.625 | 0.270 → 0.883 | 3.8x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.272 → 0.897 | 0.625 | 0.270 → 0.883 | 3.8x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.384 → 0.978 | 0.594 | 0.303 → 0.883 | 8.9x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.387 → 0.928 | 0.541 | 0.304 → 0.719 | 4.4x sr_bytes | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.317 → 0.713 | 0.396 | 0.313 → 0.709 | 2.7x sr_airtime | up | 2 |
| `MS-density` | nodes | **text** | 0.591 → 0.965 | 0.374 | 0.579 → 0.962 | 6x advert_bytes | up | 5 |
| `MS-topology` | topology | **text** | 0.601 → 0.966 | 0.364 | 0.584 → 0.963 | 2x sr_airtime | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.580 → 0.938 | 0.358 | 0.556 → 0.933 | 8.1x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.567 → 0.920 | 0.354 | 0.554 → 0.912 | 9.4x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.424 → 0.756 | 0.333 | 0.321 → 0.541 | 6x sr_airtime | up | 3 |
| `DG-outage` | burst-loss | **text** | 0.567 → 0.897 | 0.330 | 0.534 → 0.883 | 2x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.589 → 0.897 | 0.308 | 0.552 → 0.883 | 1.9x sr_bytes | down | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.716 → 0.949 | 0.232 | 0.705 → 0.945 | 5.4x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.727 → 0.928 | 0.202 | 0.664 → 0.922 | 2.6x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.727 → 0.916 | 0.189 | 0.664 → 0.906 | 2.3x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.720 → 0.897 | 0.177 | 0.713 → 0.883 | 3.6x sr_airtime | down | 5 |
| `RF-noise` | noise-profile | **held** | 0.807 → 0.978 | 0.171 | 0.718 → 0.883 | 1.3x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.727 → 0.897 | 0.171 | 0.664 → 0.883 | 1.9x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.769 → 0.897 | 0.128 | 0.744 → 0.883 | 1.6x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.826 → 0.935 | 0.109 | 0.805 → 0.926 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.826 → 0.935 | 0.109 | 0.805 → 0.926 | 2.3x bytes_on_air | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.790 → 0.897 | 0.107 | 0.790 → 0.883 | 1.2x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.800 → 0.904 | 0.103 | 0.780 → 0.892 | 2.1x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.804 → 0.904 | 0.100 | 0.781 → 0.892 | 2x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.709 → 0.799 | 0.090 | 0.619 → 0.699 | 1.7x sr_airtime | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.849 → 0.934 | 0.085 | 0.823 → 0.930 | 5.5x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.896 → 0.978 | 0.082 | 0.878 → 0.883 | 29x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.871 → 0.944 | 0.073 | 0.860 → 0.939 | 1.4x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.897 → 0.955 | 0.058 | 0.883 → 0.953 | 1.4x bytes_on_air | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.852 → 0.908 | 0.057 | 0.844 → 0.906 | 2.2x bytes_on_air | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.897 → 0.951 | 0.053 | 0.883 → 0.945 | 1.6x bytes_on_air | up | 3 |
| `SF-cadence` | trigger | **held** | 0.925 → 0.978 | 0.053 | 0.850 → 0.885 | 14x sr_bytes | down | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.855 → 0.907 | 0.052 | 0.847 → 0.904 | 2.1x bytes_on_air | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.852 → 0.900 | 0.049 | 0.824 → 0.886 | 1.5x sr_airtime | down | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.850 → 0.897 | 0.047 | 0.824 → 0.883 | 1.3x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.743 → 0.785 | 0.042 | 0.539 → 0.570 | 1.4x sr_airtime | up | 2 |
| `MS-roles` | role-mix | **text** | 0.826 → 0.868 | 0.042 | 0.805 → 0.847 | 1.2x bytes_on_air | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.940 → 0.981 | 0.041 | 0.873 → 0.883 | 6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.940 → 0.981 | 0.041 | 0.873 → 0.883 | 6x sr_bytes | up | 4 |
| `SF-place-flat` | place | **held** | 0.939 → 0.978 | 0.039 | 0.879 → 0.885 | 3.8x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.939 → 0.978 | 0.039 | 0.879 → 0.885 | 3.8x sr_bytes | up | 6 |
| `SF-hops-flat` | hops-apart | **held** | 0.940 → 0.980 | 0.039 | 0.879 → 0.890 | 1.8x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.940 → 0.980 | 0.039 | 0.879 → 0.890 | 2x sr_bytes | up | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.838 → 0.875 | 0.037 | 0.814 → 0.853 | 1.1x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **text** | 0.794 → 0.826 | 0.032 | 0.764 → 0.805 | 1.7x sr_bytes | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.897 → 0.928 | 0.031 | 0.883 → 0.922 | 3.3x bytes_on_air | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.871 → 0.897 | 0.025 | 0.850 → 0.889 | 9.6x advert_bytes | up | 3 |
| `AD-worst` | role-placement | **text** | 0.819 → 0.840 | 0.021 | 0.810 → 0.835 | 1.1x bytes_on_air | down | 2 |
| `FW-versions` | profile | **text** | 0.891 → 0.910 | 0.019 | 0.883 → 0.902 | 3.4x bytes_on_air | up | 5 |
| `SF-provide-transport` | provide-transport | **text** | 0.897 → 0.916 | 0.019 | 0.879 → 0.883 | 2.8x sr_airtime | up | 2 |
| `SF-capacity` | capacity | **held** | 0.960 → 0.978 | 0.018 | 0.875 → 0.886 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.960 → 0.978 | 0.018 | 0.875 → 0.886 | 5.3x advert_bytes | up | 5 |
| `PR-repeats` | extra-repeats | **held** | 0.964 → 0.978 | 0.015 | 0.878 → 0.883 | 1x sr_airtime | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.958 → 0.972 | 0.014 | 0.880 → 0.887 | 1.7x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.964 → 0.978 | 0.014 | 0.879 → 0.886 | 1.3x bytes_on_air | down | 4 |
| `SF-width` | short-id-bits | **held** | 0.965 → 0.978 | 0.014 | 0.876 → 0.885 | 3.1x advert_bytes | down | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.965 → 0.978 | 0.013 | 0.879 → 0.887 | 3.2x advert_bytes | up | 4 |
| `LD-diurnal` | diurnal | **text** | 0.897 → 0.909 | 0.011 | 0.883 → 0.894 | 1.3x sr_bytes | down | 3 |
| `SF-window-size` | window-size | **text** | 0.889 → 0.900 | 0.011 | 0.872 → 0.887 | 6x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.895 → 0.905 | 0.010 | 0.878 → 0.889 | 1.2x sr_bytes | down | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.960 → 0.970 | 0.010 | 0.875 → 0.879 | 1x sr_bytes | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.897 → 0.906 | 0.009 | 0.884 → 0.891 | 1.1x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **held** | 0.969 → 0.978 | 0.009 | 0.879 → 0.883 | 5.7x advert_bytes | = | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.969 → 0.978 | 0.009 | 0.879 → 0.883 | 1x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.851 → 0.858 | 0.007 | 0.851 → 0.858 | 1x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.892 → 0.900 | 0.007 | 0.878 → 0.886 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.892 → 0.900 | 0.007 | 0.878 → 0.886 | 1.1x sr_bytes | down | 4 |
| `DM-mode` | dm-mode | **held** | 0.948 → 0.954 | 0.006 | 0.845 → 0.851 | 1.1x sr_airtime | down | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.887 → 0.893 | 0.006 | 0.870 → 0.879 | 5.3x advert_bytes | up | 3 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.949 → 0.954 | 0.005 | 0.945 → 0.950 | 1.1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.943 → 0.949 | 0.005 | 0.939 → 0.945 | 1.2x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.881 → 0.886 | 0.004 | 0.879 → 0.882 | 2.2x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.974 → 0.978 | 0.004 | 0.883 → 0.885 | 2.7x sr_airtime | down | 2 |
| `FW-firmware` | profile | **text** | 0.893 → 0.897 | 0.004 | 0.883 → 0.885 | 3.4x bytes_on_air | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.949 → 0.952 | 0.004 | 0.945 → 0.949 | 1x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.856 → 0.858 | 0.002 | 0.856 → 0.858 | 1x sr_bytes | down | 2 |

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
| none | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| sprinkled | 1 | 0.871 | 0.860 | 0.011 | - | - | 0.959 | 0.960 | 0.676 | 1.26x | 18.5/28.0/30.7% | 1.9/5.0% | 3 |
| arms-race | 1 | 0.944 | 0.939 | 0.005 | - | - | 0.981 | 0.982 | 0.855 | 1.03x | 22.2/28.7/30.3% | 1.3/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.1 | 1 | 0.907 | 0.903 | 0.004 | - | - | 0.973 | 0.973 | 0.620 | 1.27x | 18.4/26.8/31.7% | 1.8/5.0% | 3 |
| 0.3 | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.996 | 0.997 | 0.811 | 0.99x | 21.2/26.7/31.9% | 1.3/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.826 | 0.805 | 0.021 | - | - | 0.929 | 0.932 | 0.427 | 1.25x | 15.3/28.4/32.1% | 2.2/5.0% | 3 |
| inverse | 1 | 0.800 | 0.778 | 0.022 | - | - | 0.904 | 0.937 | 0.343 | 1.15x | 14.2/20.0/26.3% | 1.8/3.7% | 3 |
| random | 1 | 0.794 | 0.764 | 0.030 | - | - | 0.935 | 0.938 | 0.292 | 1.14x | 15.1/22.0/28.5% | 1.8/4.6% | 3 |

> role-placement=inverse: decode_failures 35

> role-placement=random: decode_failures 1

> slower: 4.97 s per simulated hour against 2.42 over 7 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.826 | 0.805 | 0.021 | - | - | 0.929 | 0.932 | 0.427 | 1.25x | 15.3/28.4/32.1% | 2.2/5.0% | 3 |
| all-routers | 1 | 0.935 | 0.926 | 0.009 | - | - | 0.985 | 0.987 | 0.812 | 2.80x | 31.3/45.5/48.7% | 4.5/5.4% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.826 | 0.805 | 0.021 | - | - | 0.929 | 0.932 | 0.427 | 1.25x | 15.3/28.4/32.1% | 2.2/5.0% | 3 |
| no-mute | 1 | 0.870 | 0.848 | 0.022 | - | - | 0.958 | 0.961 | 0.579 | 1.38x | 16.0/24.4/30.6% | 2.1/5.2% | 3 |
| all-routers | 1 | 0.935 | 0.926 | 0.009 | - | - | 0.985 | 0.987 | 0.812 | 2.80x | 31.3/45.5/48.7% | 4.5/5.4% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.826 | 0.805 | 0.021 | - | - | 0.929 | 0.932 | 0.427 | 1.25x | 15.3/28.4/32.1% | 2.2/5.0% | 3 |
| local-typical | 1 | 0.665 | 0.656 | 0.009 | - | - | 0.830 | 0.832 | 0.000 | 1.27x | 15.0/23.7/28.2% | 1.9/5.4% | 3 |
| basement-heavy | 1 | 0.101 | 0.098 | 0.003 | - | - | 0.325 | 0.326 | 0.000 | 0.60x | 1.6/10.6/17.4% | 0.4/3.9% | 3 |

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.840 | 0.835 | 0.005 | - | - | 0.950 | 0.951 | 0.000 | 2.38x | 18.0/31.6/38.8% | 1.9/5.8% | 3 |
| inverse | 1 | 0.819 | 0.810 | 0.009 | - | - | 0.962 | 0.962 | 0.000 | 2.25x | 16.3/25.3/32.2% | 1.8/3.2% | 3 |

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.878 | 0.878 | 0.000 | - | - | 0 | 0.000 | 0.654 | 1.40x | 15.4/28.2/34.0% | 2.2/4.9% | 3 |
| sr | 1 | 0.902 | 0.881 | 0.021 | - | - | 0.980 | 0.985 | 0.672 | 1.47x | 16.5/29.5/35.4% | 2.3/5.0% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.800 | 0.780 | 0.020 | - | - | 0.874 | 0.877 | 0.612 | 3.19x | 36.2/64.0/69.9% | 4.7/9.4% | 3 |
| 100 | 1 | 0.904 | 0.892 | 0.011 | - | - | 0.958 | 0.959 | 0.682 | 1.66x | 19.7/37.2/42.2% | 2.4/5.1% | 3 |
| 120 | 1 | 0.904 | 0.892 | 0.011 | - | - | 0.958 | 0.959 | 0.682 | 1.66x | 19.7/37.2/42.2% | 2.4/5.1% | 3 |
| 250 | 1 | 0.904 | 0.892 | 0.011 | - | - | 0.958 | 0.959 | 0.682 | 1.66x | 19.7/37.2/42.2% | 2.4/5.1% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.326 | 0.321 | 0.005 | - | - | 0.424 | 0.479 | 0.067 | 11.61x | 41.0/62.8/74.7% | 4.0/11.2% | 3 |
| 120 | 1 | 0.548 | 0.539 | 0.009 | - | - | 0.743 | 0.745 | 0.114 | 4.53x | 16.2/29.9/41.2% | 1.5/6.0% | 3 |
| 250 | 1 | 0.552 | 0.541 | 0.010 | - | - | 0.756 | 0.758 | 0.103 | 4.39x | 15.9/28.4/39.1% | 1.4/5.8% | 3 |

> max-num-nodes=10: decode_failures 54

> max-num-nodes=250: decode_failures 4

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.904 | 0.892 | 0.011 | - | - | 0.958 | 0.959 | 0.682 | 1.66x | 19.7/37.2/42.2% | 2.4/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.904 | 0.892 | 0.011 | - | - | 0.958 | 0.959 | 0.682 | 1.66x | 19.7/37.2/42.2% | 2.4/5.1% | 3 |
| constrained | 1 | 0.804 | 0.781 | 0.023 | - | - | 0.888 | 0.888 | 0.612 | 3.19x | 36.2/63.8/69.8% | 4.7/9.3% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.707 | 0.699 | 0.009 | - | - | 0.799 | 0.896 | 0.506 | 5.51x | 56.0/76.7/80.6% | 4.2/11.6% | 3 |
| 25 | 1 | 0.707 | 0.699 | 0.009 | - | - | 0.799 | 0.896 | 0.506 | 5.51x | 56.0/76.7/80.6% | 4.2/11.6% | 3 |
| 100 | 1 | 0.707 | 0.699 | 0.009 | - | - | 0.799 | 0.896 | 0.506 | 5.51x | 56.0/76.7/80.6% | 4.2/11.6% | 3 |
| 2000 | 1 | 0.707 | 0.699 | 0.009 | - | - | 0.799 | 0.896 | 0.506 | 5.51x | 56.0/76.7/80.6% | 4.2/11.6% | 3 |

> warm-num-nodes=0: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 95

> warm-num-nodes=25: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 95

> warm-num-nodes=100: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 95

> warm-num-nodes=2000: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 95

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.1 | 1 | 0.802 | 0.778 | 0.024 | - | - | 0.950 | 0.959 | 0.543 | 1.36x | 15.7/28.2/34.0% | 2.1/4.9% | 3 |
| 0.2 | 1 | 0.705 | 0.664 | 0.040 | - | - | 0.900 | 0.919 | 0.436 | 1.26x | 14.7/26.7/32.3% | 2.0/4.5% | 3 |
| 0.3 | 1 | 0.589 | 0.552 | 0.037 | - | - | 0.767 | 0.876 | 0.315 | 1.12x | 13.5/24.5/29.8% | 1.7/3.8% | 3 |

> burst-loss=0.2: decode_failures 5

> burst-loss=0.3: decode_failures 30

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.1 | 1 | 0.871 | 0.855 | 0.016 | - | - | 0.966 | 0.968 | 0.594 | 1.48x | 16.9/30.0/35.9% | 2.3/5.2% | 3 |
| 0.2 | 1 | 0.826 | 0.805 | 0.021 | - | - | 0.935 | 0.940 | 0.536 | 1.52x | 17.9/31.3/37.1% | 2.4/5.2% | 3 |
| 0.3 | 1 | 0.769 | 0.744 | 0.024 | - | - | 0.888 | 0.915 | 0.485 | 1.52x | 18.5/31.5/37.0% | 2.4/5.0% | 3 |

> extra-loss=0.3: decode_failures 16

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.1 | 1 | 0.792 | 0.770 | 0.022 | - | - | 0.929 | 0.947 | 0.537 | 1.36x | 15.6/28.0/33.9% | 2.1/4.8% | 3 |
| 0.2 | 1 | 0.688 | 0.662 | 0.026 | - | - | 0.830 | 0.932 | 0.434 | 1.28x | 14.9/27.0/33.0% | 2.0/4.8% | 3 |
| 0.3 | 1 | 0.567 | 0.534 | 0.033 | - | - | 0.776 | 0.877 | 0.337 | 1.17x | 14.0/24.9/30.6% | 1.8/3.9% | 3 |

> burst-loss=0.1: decode_failures 27

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 27

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.845 | 0.845 | 0.000 | - | - | 0.954 | 0.961 | 0.615 | 1.91x | 21.3/38.3/45.6% | 2.9/6.5% | 3 |
| directed-with-late-flood | 1 | 0.851 | 0.851 | 0.000 | - | - | 0.951 | 0.956 | 0.629 | 1.77x | 19.8/35.7/42.9% | 2.7/6.2% | 3 |
| m4-early-flood | 1 | 0.846 | 0.846 | 0.000 | - | - | 0.948 | 0.954 | 0.622 | 1.77x | 19.8/35.6/42.8% | 2.7/6.2% | 3 |

> dm-mode=m4-early-flood: decode_failures 2

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.893 | 0.885 | 0.008 | - | - | 0.977 | 0.978 | 0.681 | 0.76x | 8.6/12.6/14.9% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.25 | 1 | 0.886 | 0.878 | 0.008 | - | - | 0.972 | 0.973 | 0.529 | 1.18x | 13.9/23.4/27.1% | 1.8/4.5% | 3 |
| 0.5 | 1 | 0.855 | 0.847 | 0.008 | - | - | 0.956 | 0.961 | 0.534 | 1.06x | 12.9/21.0/24.7% | 1.5/4.4% | 3 |
| 0.75 | 1 | 0.907 | 0.904 | 0.003 | - | - | 0.981 | 0.982 | 0.736 | 0.95x | 11.9/18.8/21.7% | 1.4/3.7% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.25 | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.971 | 0.972 | 0.598 | 1.18x | 13.7/23.3/27.0% | 1.8/4.5% | 3 |
| 0.5 | 1 | 0.852 | 0.844 | 0.008 | - | - | 0.955 | 0.957 | 0.537 | 1.04x | 13.3/20.4/24.1% | 1.6/4.3% | 3 |
| 0.75 | 1 | 0.908 | 0.906 | 0.002 | - | - | 0.982 | 0.983 | 0.755 | 0.91x | 11.5/18.6/21.8% | 1.4/3.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.928 | 0.922 | 0.006 | - | - | 0.991 | 0.992 | 0.683 | 0.77x | 9.2/16.9/21.1% | 1.1/3.0% | 3 |
| signing=true | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.891 | 0.884 | 0.007 | - | - | 0.972 | 0.972 | 0.675 | 0.76x | 9.0/13.5/16.6% | 1.2/2.0% | 3 |
| 2.5 | 1 | 0.891 | 0.884 | 0.007 | - | - | 0.968 | 0.968 | 0.700 | 0.79x | 9.2/13.7/16.7% | 1.3/2.0% | 3 |
| 2.6 | 1 | 0.891 | 0.883 | 0.008 | - | - | 0.976 | 0.977 | 0.698 | 0.76x | 9.1/13.7/16.9% | 1.2/2.0% | 3 |
| 2.7 | 1 | 0.910 | 0.902 | 0.007 | - | - | 0.975 | 0.977 | 0.692 | 0.80x | 9.9/17.6/20.7% | 1.2/2.9% | 3 |
| 2.8 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.920 | 0.912 | 0.009 | - | - | 0.985 | 0.986 | 0.689 | 0.96x | 10.7/19.6/23.8% | 1.5/3.5% | 3 |
| 900 | 1 | 0.849 | 0.823 | 0.026 | - | - | 0.936 | 0.942 | 0.606 | 2.27x | 25.3/45.1/53.5% | 3.5/7.9% | 3 |
| 300 | 1 | 0.567 | 0.554 | 0.012 | - | - | 0.674 | 0.786 | 0.431 | 4.65x | 52.2/73.6/80.0% | 7.5/13.0% | 3 |

> broadcast-interval-s=300: decode_failures 18

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.938 | 0.933 | 0.004 | - | - | 0.983 | 0.983 | 0.702 | 1.06x | 12.1/20.6/24.9% | 1.6/3.6% | 3 |
| 900 | 1 | 0.876 | 0.858 | 0.018 | - | - | 0.945 | 0.947 | 0.673 | 2.54x | 29.4/47.7/56.3% | 4.0/8.2% | 3 |
| 300 | 1 | 0.580 | 0.556 | 0.024 | - | - | 0.731 | 0.784 | 0.476 | 5.10x | 57.1/74.6/80.5% | 8.7/13.6% | 3 |

> broadcast-interval-s=300: decode_failures 12

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.909 | 0.894 | 0.014 | - | - | 0.980 | 0.980 | 0.651 | 1.33x | 14.9/27.3/33.3% | 2.0/4.9% | 3 |
| sinusoid | 1 | 0.905 | 0.891 | 0.014 | - | - | 0.978 | 0.979 | 0.659 | 1.32x | 14.7/26.8/32.4% | 2.0/4.7% | 3 |
| commuter | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.849 | 0.823 | 0.026 | - | - | 0.936 | 0.942 | 0.606 | 2.27x | 25.3/45.1/53.5% | 3.5/7.9% | 3 |
| 3600 | 1 | 0.920 | 0.912 | 0.009 | - | - | 0.985 | 0.986 | 0.689 | 0.96x | 10.7/19.6/23.8% | 1.5/3.5% | 3 |
| 10800 | 1 | 0.931 | 0.925 | 0.006 | - | - | 0.989 | 0.990 | 0.673 | 0.67x | 7.5/13.5/16.4% | 1.0/2.4% | 3 |
| 43200 | 1 | 0.934 | 0.930 | 0.004 | - | - | 0.991 | 0.991 | 0.675 | 0.48x | 5.4/9.8/11.9% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.25 | 1 | 0.900 | 0.886 | 0.014 | - | - | 0.978 | 0.980 | 0.659 | 1.51x | 16.8/30.6/36.9% | 2.3/5.4% | 3 |
| 1.0 | 1 | 0.884 | 0.867 | 0.017 | - | - | 0.970 | 0.971 | 0.639 | 1.70x | 18.9/34.4/41.6% | 2.6/6.1% | 3 |
| 4.0 | 1 | 0.852 | 0.824 | 0.028 | - | - | 0.947 | 0.949 | 0.612 | 2.13x | 24.3/43.6/52.3% | 3.3/7.6% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.707 | 0.699 | 0.009 | - | - | 0.799 | 0.896 | 0.506 | 5.51x | 56.0/76.7/80.6% | 4.2/11.6% | 3 |
| 1.0 | 1 | 0.626 | 0.619 | 0.007 | - | - | 0.709 | 0.849 | 0.441 | 6.10x | 60.7/77.6/81.3% | 4.7/12.2% | 3 |

> traceroute-per-hour=0.0: queue drops 19.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 95

> traceroute-per-hour=1.0: queue drops 29.3% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 79

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.591 | 0.579 | 0.012 | - | - | 0.642 | 0.657 | 0.387 | 1.14x | 17.2/23.9/25.5% | 3.0/5.6% | 3 |
| 60 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 90 | 1 | 0.937 | 0.933 | 0.004 | - | - | 0.986 | 0.986 | 0.551 | 1.70x | 19.6/34.7/37.4% | 1.6/5.1% | 3 |
| 120 | 1 | 0.949 | 0.945 | 0.004 | - | - | 0.997 | 0.997 | 0.762 | 2.08x | 22.2/43.0/46.6% | 1.5/5.2% | 3 |
| 150 | 1 | 0.965 | 0.962 | 0.003 | - | - | 0.989 | 0.989 | 0.706 | 2.78x | 30.3/48.5/54.0% | 1.4/5.9% | 3 |

> nodes=150: decode_failures 1

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 120 | 1 | 0.735 | 0.721 | 0.014 | - | - | 0.932 | 0.938 | 0.132 | 2.38x | 15.9/34.0/41.5% | 1.6/5.1% | 3 |
| 250 | 1 | 0.548 | 0.538 | 0.010 | - | - | 0.736 | 0.750 | 0.104 | 4.84x | 17.3/32.0/44.1% | 1.6/6.5% | 3 |
| 500 | 1 | 0.306 | 0.303 | 0.003 | - | - | 0.384 | 0.394 | 0.059 | 9.96x | 17.8/31.9/45.8% | 1.6/6.9% | 3 |

> nodes=120: decode_failures 1

> nodes=250: decode_failures 58

> nodes=500: decode_failures 75

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.734 | 0.719 | 0.015 | - | - | 0.928 | 0.937 | 0.145 | 2.24x | 15.1/31.8/38.9% | 1.5/4.8% | 3 |
| 250 | 1 | 0.548 | 0.539 | 0.009 | - | - | 0.743 | 0.745 | 0.114 | 4.53x | 16.2/29.9/41.2% | 1.5/6.0% | 3 |
| 500 | 1 | 0.306 | 0.304 | 0.003 | - | - | 0.387 | 0.402 | 0.061 | 9.34x | 16.5/29.9/43.6% | 1.5/6.4% | 3 |

> nodes=500: decode_failures 59

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.868 | 0.847 | 0.021 | - | - | 0.944 | 0.947 | 0.585 | 1.47x | 16.4/29.9/36.2% | 2.2/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.826 | 0.805 | 0.021 | - | - | 0.929 | 0.932 | 0.427 | 1.25x | 15.3/28.4/32.1% | 2.2/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.875 | 0.853 | 0.022 | - | - | 0.953 | 0.953 | 0.615 | 1.50x | 16.8/30.1/36.4% | 2.3/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.838 | 0.814 | 0.024 | - | - | 0.919 | 0.922 | 0.468 | 1.37x | 16.3/31.9/35.8% | 2.4/4.9% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.05 | 1 | 0.898 | 0.882 | 0.016 | - | - | 0.969 | 0.970 | 0.632 | 1.58x | 19.5/35.0/42.5% | 2.3/5.0% | 3 |
| 0.1 | 1 | 0.896 | 0.879 | 0.016 | - | - | 0.968 | 0.969 | 0.642 | 1.67x | 19.4/37.9/44.1% | 2.3/5.0% | 3 |
| 0.2 | 1 | 0.901 | 0.886 | 0.016 | - | - | 0.964 | 0.964 | 0.658 | 1.86x | 21.1/42.2/47.4% | 2.6/5.1% | 3 |

> router-late-fraction=0.2: misdecodes 1

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| local-typical | 1 | 0.726 | 0.716 | 0.010 | - | - | 0.909 | 0.913 | 0.000 | 1.54x | 15.6/28.0/32.7% | 2.5/5.3% | 3 |
| event | 1 | 0.131 | 0.127 | 0.004 | - | - | 0.298 | 0.306 | 0.000 | 0.86x | 3.4/9.1/14.7% | 1.1/3.1% | 3 |
| backbone | 1 | 0.978 | 0.977 | 0.001 | - | - | 1.000 | 1.000 | 0.898 | 1.13x | 31.1/39.0/40.3% | 1.3/5.5% | 3 |

> siting-mix=event: decode_failures 1

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.816 | 0.806 | 0.011 | - | - | 0.922 | 0.924 | 0.521 | 1.40x | 27.0/35.9/40.6% | 3.3/7.6% | 3 |
| 60 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 90 | 1 | 0.779 | 0.766 | 0.013 | - | - | 0.949 | 0.950 | 0.332 | 1.80x | 14.7/33.4/36.7% | 1.7/5.2% | 3 |
| 120 | 1 | 0.735 | 0.721 | 0.014 | - | - | 0.932 | 0.938 | 0.132 | 2.38x | 15.9/34.0/41.5% | 1.6/5.1% | 3 |
| 150 | 1 | 0.720 | 0.713 | 0.007 | - | - | 0.825 | 0.826 | 0.060 | 2.90x | 16.3/35.0/44.7% | 1.5/5.1% | 3 |

> nodes=120: decode_failures 1

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 1.25 | 1 | 0.631 | 0.623 | 0.007 | - | - | 0.785 | 0.786 | 0.314 | 1.37x | 13.0/21.8/25.8% | 2.0/4.8% | 3 |
| 1.5 | 1 | 0.317 | 0.313 | 0.004 | - | - | 0.489 | 0.492 | 0.000 | 1.53x | 11.3/23.5/28.3% | 2.3/5.6% | 3 |
| 2.0 | 1 | 0.152 | 0.145 | 0.007 | - | - | 0.374 | 0.398 | 0.000 | 0.97x | 4.4/14.4/17.6% | 1.5/4.3% | 3 |

> stretch=2.0: decode_failures 8

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| clustered | 1 | 0.886 | 0.869 | 0.018 | - | - | 0.977 | 0.984 | 0.653 | 1.06x | 19.9/32.5/34.9% | 1.3/5.1% | 3 |
| corridor | 1 | 0.601 | 0.584 | 0.018 | - | - | 0.776 | 0.778 | 0.364 | 1.28x | 15.2/24.8/27.0% | 1.9/5.6% | 3 |
| hub | 1 | 0.966 | 0.963 | 0.003 | - | - | 0.989 | 0.991 | 0.623 | 1.18x | 26.9/37.1/38.3% | 1.7/5.7% | 3 |

> topology=hub: decode_failures 2

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.851 | 0.851 | 0.000 | - | - | 0.951 | 0.956 | 0.629 | 1.77x | 19.8/35.7/42.9% | 2.7/6.2% | 3 |
| True | 1 | 0.858 | 0.858 | 0.000 | - | - | 0.954 | 0.961 | 0.639 | 1.79x | 20.2/36.3/43.5% | 2.7/6.2% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.858 | 0.858 | 0.000 | - | - | 0.954 | 0.961 | 0.639 | 1.79x | 20.2/36.3/43.5% | 2.7/6.2% | 3 |
| m4-early-flood | 1 | 0.856 | 0.856 | 0.000 | - | - | 0.953 | 0.963 | 0.638 | 1.79x | 20.2/36.4/43.5% | 2.7/6.2% | 3 |

> dm-mode=m4-early-flood: decode_failures 2

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.878 | 0.878 | 0.000 | - | - | 0 | 0.000 | 0.654 | 1.40x | 15.4/28.2/34.0% | 2.2/4.9% | 3 |
| chain | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.915 | 0.976 | 0.651 | 1.64x | 18.4/33.5/40.4% | 2.5/5.9% | 3 |
| sr | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| True | 1 | 0.891 | 0.878 | 0.014 | - | - | 0.964 | 0.967 | 0.663 | 1.46x | 16.2/29.6/35.7% | 2.2/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.949 | 0.945 | 0.004 | - | - | 0.997 | 0.997 | 0.762 | 2.08x | 22.2/43.0/46.6% | 1.5/5.2% | 3 |
| True | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.999 | 0.999 | 0.771 | 2.11x | 22.5/43.3/46.9% | 1.5/5.2% | 3 |

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.168 | 0.166 | 0.002 | - | - | 0.388 | 0.392 | 0.000 | 0.05x | 0.2/0.9/1.2% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.374 | 0.371 | 0.003 | - | - | 0.510 | 0.512 | 0.000 | 0.25x | 2.0/4.1/5.1% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.797 | 0.794 | 0.004 | - | - | 0.878 | 0.879 | 0.328 | 1.38x | 13.1/24.5/26.4% | 2.0/4.6% | 3 |

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 0.25 | 1 | 0.909 | 0.894 | 0.015 | - | - | 0.972 | 0.973 | 0.707 | 1.33x | 19.5/31.3/36.5% | 2.0/5.3% | 3 |
| 1.0 | 1 | 0.951 | 0.945 | 0.006 | - | - | 0.988 | 0.990 | 0.843 | 0.90x | 25.2/31.9/34.6% | 1.2/5.0% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.272 | 0.270 | 0.003 | - | - | 0.464 | 0.465 | 0.000 | 0.12x | 0.8/1.7/3.0% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| LITE_FAST | 1 | 0.829 | 0.822 | 0.008 | - | - | 0.922 | 0.927 | 0.478 | 1.07x | 11.9/22.2/24.3% | 1.6/3.9% | 3 |
| NARROW_SLOW | 1 | 0.847 | 0.841 | 0.006 | - | - | 0.931 | 0.933 | 0.559 | 1.39x | 15.4/28.3/30.8% | 2.1/5.0% | 3 |

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| temporal | 1 | 0.827 | 0.805 | 0.021 | - | - | 0.942 | 0.943 | 0.437 | 1.43x | 16.1/29.0/34.1% | 2.1/5.2% | 3 |
| transient | 1 | 0.889 | 0.874 | 0.015 | - | - | 0.968 | 0.969 | 0.641 | 1.45x | 16.0/29.4/35.5% | 2.2/5.3% | 3 |
| periodic | 1 | 0.732 | 0.718 | 0.013 | - | - | 0.807 | 0.822 | 0.491 | 1.32x | 14.9/26.9/32.4% | 2.1/4.6% | 3 |

> noise-profile=periodic: decode_failures 20

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.272 | 0.270 | 0.003 | - | - | 0.464 | 0.465 | 0.000 | 0.12x | 0.8/1.7/3.0% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| LONG_MODERATE | 1 | 0.830 | 0.820 | 0.010 | - | - | 0.881 | 0.884 | 0.688 | 3.58x | 48.1/70.1/72.9% | 5.6/11.7% | 3 |

> preset=LONG_MODERATE: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.088 | 0.087 | 0.001 | - | - | 0.267 | 0.268 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.1% | 3 |
| SHORT_TURBO | 1 | 0.168 | 0.166 | 0.002 | - | - | 0.388 | 0.392 | 0.000 | 0.05x | 0.2/0.9/1.2% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| LONG_TURBO | 1 | 0.797 | 0.794 | 0.004 | - | - | 0.878 | 0.879 | 0.328 | 1.38x | 13.1/24.5/26.4% | 2.0/4.6% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.868 | 0.846 | 0.022 | - | - | 0.955 | 0.959 | 0.640 | 1.97x | 21.7/37.3/42.4% | 2.9/6.6% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 1

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.842 | 0.825 | 0.017 | - | - | 0.922 | 0.923 | 0.618 | 1.38x | 15.6/28.3/34.2% | 2.1/4.9% | 3 |
| 10000 | 1 | 0.732 | 0.718 | 0.013 | - | - | 0.807 | 0.822 | 0.491 | 1.32x | 14.9/26.9/32.4% | 2.1/4.6% | 3 |
| 4000 | 1 | 0.473 | 0.467 | 0.006 | - | - | 0.521 | 0.572 | 0.282 | 1.13x | 13.6/23.5/28.1% | 1.7/3.6% | 3 |
| 2000 | 1 | 0.139 | 0.139 | 0.000 | - | - | 0.148 | 0.217 | 0.076 | 0.76x | 9.7/16.3/19.7% | 1.2/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 20

> noise-pulse-interval-ms=4000: decode_failures 6

> slower: 3.36 s per simulated hour against 1.6 over 7 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.317 | 0.313 | 0.004 | - | - | 0.489 | 0.492 | 0.000 | 1.53x | 11.3/23.5/28.3% | 2.3/5.6% | 3 |
| 1.0 | 1 | 0.713 | 0.709 | 0.003 | - | - | 0.798 | 0.801 | 0.549 | 0.94x | 18.4/26.2/27.9% | 1.2/4.3% | 3 |

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 22 | 1 | 0.349 | 0.344 | 0.004 | - | - | 0.499 | 0.502 | 0.000 | 1.53x | 11.2/23.2/28.0% | 2.3/5.6% | 3 |
| 17 | 1 | 0.160 | 0.158 | 0.002 | - | - | 0.358 | 0.361 | 0.000 | 1.04x | 5.2/18.1/21.2% | 1.5/4.5% | 3 |
| 14 | 1 | 0.105 | 0.103 | 0.002 | - | - | 0.274 | 0.275 | 0.000 | 0.77x | 2.9/11.2/14.5% | 1.0/4.0% | 3 |

> tx-power=14: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.949 | 0.945 | 0.004 | - | - | 0.997 | 0.997 | 0.762 | 2.08x | 22.2/43.0/46.6% | 1.5/5.2% | 3 |
| True | 1 | 0.943 | 0.939 | 0.005 | - | - | 0.999 | 0.999 | 0.744 | 2.45x | 25.7/48.2/52.2% | 1.7/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.897 | 0.884 | 0.013 | - | - | 0.968 | 0.968 | 0.632 | 1.57x | 18.9/34.7/40.4% | 2.3/5.1% | 3 |
| True | 1 | 0.906 | 0.891 | 0.016 | - | - | 0.971 | 0.972 | 0.659 | 1.62x | 19.5/35.0/40.7% | 2.4/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| random | 1 | 0.850 | 0.824 | 0.026 | - | - | 0.945 | 0.948 | 0.619 | 1.42x | 15.9/29.0/35.1% | 2.2/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.727 | 0.664 | 0.063 | - | - | 0.916 | 0.928 | 0.393 | 1.05x | 12.3/24.3/29.1% | 1.5/4.6% | 3 |
| 7 | 1 | 0.916 | 0.906 | 0.010 | - | - | 0.973 | 0.974 | 0.694 | 1.59x | 18.2/30.8/37.1% | 2.5/5.3% | 3 |
| 15 | 1 | 0.928 | 0.922 | 0.006 | - | - | 0.969 | 0.969 | 0.723 | 1.59x | 18.3/30.6/36.9% | 2.5/5.3% | 3 |
| 32 | 1 | 0.928 | 0.922 | 0.006 | - | - | 0.969 | 0.969 | 0.723 | 1.59x | 18.3/30.6/36.9% | 2.5/5.3% | 3 |

> hop-limit=3: decode_failures 7

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.727 | 0.664 | 0.063 | - | - | 0.916 | 0.928 | 0.393 | 1.05x | 12.3/24.3/29.1% | 1.5/4.6% | 3 |
| 5 | 1 | 0.868 | 0.846 | 0.022 | - | - | 0.958 | 0.961 | 0.637 | 1.45x | 16.4/29.2/35.2% | 2.3/5.2% | 3 |
| 7 | 1 | 0.916 | 0.906 | 0.010 | - | - | 0.973 | 0.974 | 0.694 | 1.59x | 18.2/30.8/37.1% | 2.5/5.3% | 3 |

> hop-limit=3: decode_failures 7

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.878 | 0.878 | 0.000 | - | - | 0.896 | 0.967 | 0.645 | 1.42x | 15.8/28.7/34.7% | 2.2/4.9% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.727 | 0.664 | 0.063 | - | - | 0.916 | 0.928 | 0.393 | 1.05x | 12.3/24.3/29.1% | 1.5/4.6% | 3 |
| True | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

> hop-spread=False: decode_failures 7

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| BALANCED | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| STRICT | 1 | 0.790 | 0.790 | 0.000 | - | - | 0.888 | 0.890 | 0.480 | 1.56x | 17.7/31.4/37.8% | 2.4/5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| dm | 1 | 0.901 | 0.885 | 0.015 | - | - | 0.974 | 0.976 | 0.654 | 1.42x | 16.0/29.2/35.4% | 2.2/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.892 | 0.880 | 0.012 | - | - | 0.966 | 0.967 | 0.638 | 1.44x | 16.1/29.2/35.2% | 2.2/5.2% | 3 |
| local | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| time | 1 | 0.893 | 0.879 | 0.014 | - | - | 0.965 | 0.972 | 0.635 | 1.49x | 16.6/30.3/36.5% | 2.3/5.4% | 3 |
| window | 1 | 0.900 | 0.887 | 0.013 | - | - | 0.972 | 0.974 | 0.644 | 1.44x | 15.9/29.1/35.3% | 2.2/5.2% | 3 |

> bucket-mode=global: misdecodes 38

> bucket-mode=time: misdecodes 34

> bucket-mode=window: misdecodes 11

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.887 | 0.870 | 0.017 | - | - | 0.967 | 0.971 | 0.639 | 1.60x | 17.9/32.6/38.9% | 2.5/5.9% | 3 |
| 1800 | 1 | 0.893 | 0.879 | 0.014 | - | - | 0.965 | 0.972 | 0.635 | 1.49x | 16.6/30.3/36.5% | 2.3/5.4% | 3 |
| 3600 | 1 | 0.893 | 0.879 | 0.014 | - | - | 0.969 | 0.969 | 0.658 | 1.45x | 16.1/29.3/35.4% | 2.2/5.2% | 3 |

> time-bucket-s=600: misdecodes 98

> time-bucket-s=1800: misdecodes 34

> time-bucket-s=3600: misdecodes 3

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| interval | 1 | 0.876 | 0.854 | 0.022 | - | - | 0.960 | 0.963 | 0.628 | 1.93x | 22.6/40.1/47.7% | 2.9/8.0% | 3 |
| aimd | 1 | 0.888 | 0.885 | 0.004 | - | - | 0.925 | 0.978 | 0.652 | 1.44x | 16.0/29.3/35.5% | 2.2/5.2% | 3 |
| bucket+interval | 1 | 0.871 | 0.850 | 0.021 | - | - | 0.950 | 0.952 | 0.613 | 1.98x | 23.6/41.4/49.1% | 2.9/8.1% | 3 |

> trigger=interval: misdecodes 11

> trigger=interval: decode_failures 8

> trigger=aimd: misdecodes 4

> trigger=aimd: decode_failures 1

> trigger=bucket+interval: misdecodes 19

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.890 | 0.875 | 0.015 | - | - | 0.968 | 0.971 | 0.631 | 1.45x | 16.3/29.7/35.8% | 2.2/5.4% | 3 |
| 8 | 1 | 0.899 | 0.886 | 0.012 | - | - | 0.977 | 0.980 | 0.649 | 1.43x | 16.0/29.3/35.3% | 2.2/5.2% | 3 |
| 16 | 1 | 0.890 | 0.875 | 0.015 | - | - | 0.960 | 0.963 | 0.655 | 1.45x | 16.0/29.4/35.5% | 2.2/5.2% | 3 |
| 32 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 50 | 1 | 0.896 | 0.881 | 0.015 | - | - | 0.969 | 0.971 | 0.644 | 1.46x | 16.2/29.6/35.8% | 2.2/5.3% | 3 |

> capacity=4: decode_failures 100

> capacity=8: decode_failures 24

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.890 | 0.875 | 0.015 | - | - | 0.968 | 0.971 | 0.631 | 1.45x | 16.3/29.7/35.8% | 2.2/5.4% | 3 |
| 8 | 1 | 0.899 | 0.886 | 0.012 | - | - | 0.977 | 0.980 | 0.649 | 1.43x | 16.0/29.3/35.3% | 2.2/5.2% | 3 |
| 16 | 1 | 0.890 | 0.875 | 0.015 | - | - | 0.960 | 0.963 | 0.655 | 1.45x | 16.0/29.4/35.5% | 2.2/5.2% | 3 |
| 32 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 50 | 1 | 0.896 | 0.881 | 0.015 | - | - | 0.969 | 0.971 | 0.644 | 1.46x | 16.2/29.6/35.8% | 2.2/5.3% | 3 |

> capacity=4: decode_failures 100

> capacity=8: decode_failures 24

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.896 | 0.886 | 0.011 | - | - | 0.958 | 0.969 | 0.654 | 1.42x | 15.8/28.8/34.9% | 2.2/5.1% | 3 |
| 16 | 1 | 0.896 | 0.880 | 0.016 | - | - | 0.971 | 0.976 | 0.648 | 1.43x | 15.9/29.0/35.3% | 2.2/5.1% | 3 |
| 32 | 1 | 0.900 | 0.887 | 0.013 | - | - | 0.972 | 0.974 | 0.644 | 1.44x | 15.9/29.1/35.3% | 2.2/5.2% | 3 |

> capacity=8: misdecodes 34

> capacity=8: decode_failures 29

> capacity=16: misdecodes 14

> capacity=32: misdecodes 11

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.871 | 0.850 | 0.021 | - | - | 0.950 | 0.952 | 0.613 | 1.98x | 23.6/41.4/49.1% | 2.9/8.1% | 3 |
| 02-06 | 1 | 0.897 | 0.889 | 0.008 | - | - | 0.947 | 0.978 | 0.647 | 1.49x | 16.6/30.5/37.0% | 2.2/5.6% | 3 |
| 00-08 | 1 | 0.889 | 0.880 | 0.009 | - | - | 0.949 | 0.975 | 0.641 | 1.56x | 17.8/32.5/39.1% | 2.3/6.2% | 3 |

> catch-up-hours=: misdecodes 19

> catch-up-hours=02-06: decode_failures 46

> catch-up-hours=00-08: decode_failures 46

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.891 | 0.890 | 0.001 | - | - | 0.940 | 0.941 | 0.627 | 1.45x | 15.9/29.3/35.2% | 2.2/5.0% | 3 |
| 2 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 3 | 1 | 0.902 | 0.881 | 0.021 | - | - | 0.980 | 0.985 | 0.672 | 1.47x | 16.5/29.5/35.4% | 2.3/5.0% | 3 |
| 4 | 1 | 0.907 | 0.879 | 0.028 | - | - | 0.963 | 0.988 | 0.663 | 1.48x | 16.7/29.5/35.9% | 2.3/5.2% | 3 |

> hops-apart=4: decode_failures 15

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.891 | 0.890 | 0.001 | - | - | 0.940 | 0.941 | 0.627 | 1.45x | 15.9/29.3/35.2% | 2.2/5.0% | 3 |
| 2 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 3 | 1 | 0.902 | 0.881 | 0.021 | - | - | 0.980 | 0.985 | 0.672 | 1.47x | 16.5/29.5/35.4% | 2.3/5.0% | 3 |
| 4 | 1 | 0.907 | 0.879 | 0.028 | - | - | 0.963 | 0.988 | 0.663 | 1.48x | 16.7/29.5/35.9% | 2.3/5.2% | 3 |
| 5 | 1 | 0.909 | 0.880 | 0.029 | - | - | 0.952 | 0.989 | 0.650 | 1.46x | 16.5/29.4/35.7% | 2.2/5.3% | 3 |

> hops-apart=4: decode_failures 15

> hops-apart=5: decode_failures 28

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.900 | 0.886 | 0.013 | - | - | 0.974 | 0.976 | 0.628 | 1.44x | 16.1/29.3/35.2% | 2.2/5.2% | 3 |
| 30 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 120 | 1 | 0.892 | 0.878 | 0.014 | - | - | 0.973 | 0.975 | 0.623 | 1.46x | 16.1/29.4/35.6% | 2.3/5.2% | 3 |
| 600 | 1 | 0.895 | 0.881 | 0.014 | - | - | 0.977 | 0.978 | 0.639 | 1.45x | 16.1/29.4/35.6% | 2.2/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.900 | 0.886 | 0.013 | - | - | 0.974 | 0.976 | 0.628 | 1.44x | 16.1/29.3/35.2% | 2.2/5.2% | 3 |
| 30 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 120 | 1 | 0.892 | 0.878 | 0.014 | - | - | 0.973 | 0.975 | 0.623 | 1.46x | 16.1/29.4/35.6% | 2.3/5.2% | 3 |
| 600 | 1 | 0.895 | 0.881 | 0.014 | - | - | 0.977 | 0.978 | 0.639 | 1.45x | 16.1/29.4/35.6% | 2.2/5.2% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.910 | 0.884 | 0.027 | - | - | 0.939 | 0.983 | 0.638 | 1.48x | 16.8/29.8/35.9% | 2.3/5.2% | 3 |
| routers | 1 | 0.881 | 0.879 | 0.002 | - | - | 0.940 | 0.940 | 0.624 | 1.45x | 15.9/29.5/35.4% | 2.2/5.0% | 3 |
| alternate-routers | 1 | 0.883 | 0.880 | 0.003 | - | - | 0.942 | 0.942 | 0.651 | 1.46x | 16.2/29.5/35.6% | 2.2/5.2% | 3 |
| beside-router | 1 | 0.887 | 0.885 | 0.002 | - | - | 0.961 | 0.962 | 0.625 | 1.44x | 16.0/29.3/35.2% | 2.2/5.0% | 3 |
| random-clients | 1 | 0.892 | 0.882 | 0.009 | - | - | 0.971 | 0.973 | 0.654 | 1.46x | 16.6/29.2/35.4% | 2.3/5.0% | 3 |
| hops-apart | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

> place=spread: decode_failures 39

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.910 | 0.884 | 0.027 | - | - | 0.939 | 0.983 | 0.638 | 1.48x | 16.8/29.8/35.9% | 2.3/5.2% | 3 |
| routers | 1 | 0.881 | 0.879 | 0.002 | - | - | 0.940 | 0.940 | 0.624 | 1.45x | 15.9/29.5/35.4% | 2.2/5.0% | 3 |
| alternate-routers | 1 | 0.883 | 0.880 | 0.003 | - | - | 0.942 | 0.942 | 0.651 | 1.46x | 16.2/29.5/35.6% | 2.2/5.2% | 3 |
| beside-router | 1 | 0.887 | 0.885 | 0.002 | - | - | 0.961 | 0.962 | 0.625 | 1.44x | 16.0/29.3/35.2% | 2.2/5.0% | 3 |
| random-clients | 1 | 0.892 | 0.882 | 0.009 | - | - | 0.971 | 0.973 | 0.654 | 1.46x | 16.6/29.2/35.4% | 2.3/5.0% | 3 |
| hops-apart | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

> place=spread: decode_failures 39

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| broadcast | 1 | 0.916 | 0.879 | 0.037 | - | - | 0.970 | 0.972 | 0.716 | 1.56x | 17.4/31.3/37.5% | 2.4/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| heard | 1 | 0.893 | 0.879 | 0.015 | - | - | 0.969 | 0.972 | 0.639 | 1.46x | 16.3/29.8/36.0% | 2.2/5.3% | 3 |

> replay-ordering=heard: misdecodes 6

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.916 | 0.879 | 0.037 | - | - | 0.970 | 0.972 | 0.716 | 1.56x | 17.4/31.3/37.5% | 2.4/5.4% | 3 |
| heard | 1 | 0.911 | 0.875 | 0.036 | - | - | 0.960 | 0.963 | 0.695 | 1.53x | 17.0/30.7/36.8% | 2.3/5.3% | 3 |

> replay-ordering=heard: misdecodes 4

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| enum | 1 | 0.895 | 0.879 | 0.016 | - | - | 0.969 | 0.972 | 0.651 | 1.44x | 16.1/29.6/35.6% | 2.2/5.4% | 3 |
| hybrid | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.881 | 0.879 | 0.002 | - | - | 0.940 | 0.940 | 0.624 | 1.45x | 15.9/29.5/35.4% | 2.2/5.0% | 3 |
| 6 | 1 | 0.886 | 0.882 | 0.004 | - | - | 0.941 | 0.941 | 0.641 | 1.49x | 16.4/30.2/36.3% | 2.3/5.3% | 6 |

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.889 | 0.882 | 0.007 | - | - | 0.940 | 0.941 | 0.664 | 1.43x | 15.9/28.9/34.9% | 2.2/5.1% | 2 |
| 3 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 5 | 1 | 0.901 | 0.882 | 0.019 | - | - | 0.978 | 0.980 | 0.628 | 1.48x | 16.4/30.0/36.1% | 2.2/5.2% | 5 |
| 8 | 1 | 0.898 | 0.873 | 0.025 | - | - | 0.981 | 0.983 | 0.630 | 1.54x | 17.2/31.2/37.5% | 2.3/5.5% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.889 | 0.882 | 0.007 | - | - | 0.940 | 0.941 | 0.664 | 1.43x | 15.9/28.9/34.9% | 2.2/5.1% | 2 |
| 3 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 5 | 1 | 0.901 | 0.882 | 0.019 | - | - | 0.978 | 0.980 | 0.628 | 1.48x | 16.4/30.0/36.1% | 2.2/5.2% | 5 |
| 8 | 1 | 0.898 | 0.873 | 0.025 | - | - | 0.981 | 0.983 | 0.630 | 1.54x | 17.2/31.2/37.5% | 2.3/5.5% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| True | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.905 | 0.889 | 0.016 | - | - | 0.972 | 0.977 | 0.658 | 1.35x | 15.1/27.5/33.3% | 2.0/4.8% | 3 |
| 1 | 1 | 0.895 | 0.881 | 0.014 | - | - | 0.970 | 0.972 | 0.652 | 1.35x | 15.1/27.5/33.0% | 2.1/4.8% | 3 |
| 2 | 1 | 0.896 | 0.878 | 0.018 | - | - | 0.968 | 0.969 | 0.678 | 1.35x | 15.1/27.3/32.9% | 2.1/4.8% | 3 |
| 4 | 1 | 0.896 | 0.881 | 0.015 | - | - | 0.968 | 0.969 | 0.629 | 1.37x | 15.2/27.7/33.5% | 2.1/4.8% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.900 | 0.885 | 0.014 | - | - | 0.972 | 0.976 | 0.650 | 1.44x | 16.0/29.2/35.3% | 2.2/5.2% | 3 |
| 24 | 1 | 0.892 | 0.876 | 0.016 | - | - | 0.965 | 0.965 | 0.661 | 1.45x | 16.2/29.6/35.7% | 2.2/5.3% | 3 |
| 32 | 1 | 0.897 | 0.883 | 0.015 | - | - | 0.978 | 0.981 | 0.645 | 1.44x | 16.0/29.1/35.2% | 2.2/5.2% | 3 |
| 64 | 1 | 0.892 | 0.879 | 0.013 | - | - | 0.970 | 0.972 | 0.642 | 1.44x | 16.0/29.2/35.4% | 2.2/5.2% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.895 | 0.878 | 0.018 | - | - | 0.971 | 0.974 | 0.650 | 1.54x | 17.1/31.1/37.5% | 2.3/5.5% | 3 |
| 16 | 1 | 0.889 | 0.872 | 0.017 | - | - | 0.963 | 0.967 | 0.661 | 1.46x | 16.2/29.5/35.6% | 2.2/5.2% | 3 |
| 32 | 1 | 0.900 | 0.887 | 0.013 | - | - | 0.972 | 0.974 | 0.644 | 1.44x | 15.9/29.1/35.3% | 2.2/5.2% | 3 |

> window-size=8: misdecodes 121

> window-size=16: misdecodes 65

> window-size=32: misdecodes 11

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.949 | 0.945 | 0.004 | - | - | 0.997 | 0.997 | 0.762 | 2.08x | 22.2/43.0/46.6% | 1.5/5.2% | 3 |
| True | 1 | 0.716 | 0.705 | 0.011 | - | - | 0.815 | 0.896 | 0.514 | 5.52x | 56.1/76.7/80.6% | 4.1/11.3% | 3 |

> no-congestion-scaling=True: queue drops 18.8% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 101

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.548 | 0.539 | 0.009 | - | - | 0.743 | 0.745 | 0.114 | 4.53x | 16.2/29.9/41.2% | 1.5/6.0% | 3 |
| truesize | 1 | 0.580 | 0.570 | 0.010 | - | - | 0.785 | 0.788 | 0.104 | 3.46x | 12.4/24.0/33.3% | 1.1/5.1% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.954 | 0.950 | 0.004 | - | - | 0.998 | 0.999 | 0.777 | 2.01x | 21.4/41.1/44.6% | 1.4/5.0% | 3 |
| adaptive | 1 | 0.949 | 0.945 | 0.004 | - | - | 0.997 | 0.997 | 0.762 | 2.08x | 22.2/43.0/46.6% | 1.5/5.2% | 3 |

