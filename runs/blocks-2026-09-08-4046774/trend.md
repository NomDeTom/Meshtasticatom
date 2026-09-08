# Sweep blocks-2026-09-08-4046774

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** coastal
- **seed base** 4046774 · seeds 4046774
- **blocks** 87 run
- **compute** 10.5 h of simulator time across every cell
- **generated** 2026-09-08T08:30:16+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>76 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 22
- AD-worst: role-placement=inverse: misdecodes 1
- BL-control: protocol=sr: decode_failures 41
- BL-control: slower: 6.18 s per simulated hour against 1.75 over 18 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 108
- DB-warm: warm-num-nodes=0: queue drops 23.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 104
- DB-warm: warm-num-nodes=25: queue drops 23.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 104
- DB-warm: warm-num-nodes=100: queue drops 23.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 104
- DB-warm: warm-num-nodes=2000: queue drops 23.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 104
- DG-burst: burst-loss=0.2: decode_failures 19
- DG-burst: burst-loss=0.3: decode_failures 34
- DG-loss: extra-loss=0.3: decode_failures 4
- DG-outage: burst-loss=0.1: decode_failures 43
- DG-outage: burst-loss=0.2: decode_failures 36
- DG-outage: burst-loss=0.3: decode_failures 29
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 36
- LD-chatty: broadcast-interval-s=300: decode_failures 23
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 23.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 104
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 31.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 99
- MS-density: nodes=40: decode_failures 20
- MS-hopscale: nodes=120: decode_failures 40
- MS-hopscale: nodes=500: decode_failures 25
- MS-oversubscribed: nodes=120: decode_failures 17
- MS-oversubscribed: nodes=500: decode_failures 13
- MS-siting: siting-mix=event: decode_failures 6
- MS-size: nodes=120: decode_failures 40
- MS-stretch: stretch=1.25: decode_failures 27
- MS-stretch: stretch=1.5: decode_failures 1
- MS-topology: topology=corridor: decode_failures 10
- RF-eu-presets: preset=SHORT_FAST: decode_failures 17
- RF-preset: preset=SHORT_FAST: decode_failures 17
- RF-preset: preset=LONG_MODERATE: decode_failures 6
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 1
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 1
- RF-txpower: tx-power=14: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 24
- SF-bucket-mode: bucket-mode=time: misdecodes 34
- SF-bucket-mode: bucket-mode=window: misdecodes 26
- SF-bucket-time: time-bucket-s=600: misdecodes 105
- SF-bucket-time: time-bucket-s=1800: misdecodes 34
- SF-bucket-time: time-bucket-s=3600: misdecodes 10
- SF-cadence: trigger=interval: misdecodes 5
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=bucket+interval: misdecodes 7
- SF-capacity-local: capacity=4: decode_failures 78
- SF-capacity-local: capacity=8: decode_failures 17
- SF-capacity: capacity=4: decode_failures 78
- SF-capacity: capacity=8: decode_failures 17
- SF-capacity-window: capacity=8: misdecodes 15
- SF-capacity-window: capacity=8: decode_failures 7
- SF-capacity-window: capacity=16: misdecodes 23
- SF-capacity-window: capacity=16: decode_failures 1
- SF-capacity-window: capacity=32: misdecodes 26
- SF-catchup: catch-up-hours=: misdecodes 7
- SF-catchup: catch-up-hours=02-06: decode_failures 3
- SF-catchup: catch-up-hours=00-08: decode_failures 3
- SF-hops-flat: hops-apart=3: decode_failures 41
- SF-hops-flat: hops-apart=4: decode_failures 22
- SF-hops-spread: hops-apart=3: decode_failures 41
- SF-hops-spread: hops-apart=4: decode_failures 22
- SF-hops-spread: hops-apart=5: decode_failures 25
- SF-place-flat: place=spread: decode_failures 40
- SF-place-spread: place=spread: decode_failures 40
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 6
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-window-size: window-size=8: misdecodes 117
- SF-window-size: window-size=16: misdecodes 59
- SF-window-size: window-size=32: misdecodes 26
- TH-congestion: no-congestion-scaling=True: queue drops 19.7% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 78

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 6.18 | 1.75 | 3.54x | 18 |
| `AD-siting` | 2.74 | 1.44 | 1.90x | 18 |
| `MS-size` | 5.49 | 3.4 | 1.62x | 18 |
| `MS-stretch` | 3.48 | 2.2 | 1.58x | 18 |
| `SF-hops-flat` | 5.47 | 3.52 | 1.55x | 18 |
| `SF-capacity` | 1.17 | 1.76 | 0.66x | 18 |
| `RF-preset-turbo` | 1.01 | 1.56 | 0.65x | 14 |
| `SF-provide-transport` | 1.24 | 1.93 | 0.64x | 18 |
| `RF-bw500` | 1.42 | 2.44 | 0.58x | 18 |
| `SF-catchup` | 5.63 | 9.66 | 0.58x | 18 |
| `AD-badrouters` | 1.27 | 2.26 | 0.56x | 18 |
| `DB-hotstore` | 1.52 | 2.81 | 0.54x | 18 |
| `RF-stretch-duct` | 1.68 | 3.11 | 0.54x | 18 |
| `SF-cadence` | 1.95 | 3.67 | 0.53x | 18 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.981 | 0.981 | 0.863 → 0.871 | 1.1x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.030 → 0.981 | 0.951 | 0.035 → 0.871 | 87x sr_bytes | up | 5 |
| `BL-control` | protocol | **held** | 0 → 0.945 | 0.945 | 0.868 → 0.872 | 1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.084 → 0.981 | 0.897 | 0.050 → 0.871 | 14x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.125 → 0.920 | 0.795 | 0.102 → 0.810 | 83x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.187 → 0.981 | 0.795 | 0.094 → 0.871 | 7.1x sr_bytes | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.189 → 0.974 | 0.785 | 0.075 → 0.847 | 5.8x advert_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.253 → 0.981 | 0.728 | 0.242 → 0.980 | 2.2x sr_airtime | up | 4 |
| `RF-bw500` | preset | **text** | 0.104 → 0.801 | 0.697 | 0.102 → 0.794 | 4.6x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.312 → 0.878 | 0.566 | 0.288 → 0.871 | 2x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.312 → 0.878 | 0.566 | 0.288 → 0.871 | 2.1x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.334 → 0.878 | 0.544 | 0.329 → 0.871 | 11x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.336 → 0.805 | 0.469 | 0.332 → 0.783 | 4.5x bytes_on_air | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.397 → 0.757 | 0.360 | 0.384 → 0.739 | 1.5x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.560 → 0.912 | 0.352 | 0.539 → 0.909 | 7x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.603 → 0.947 | 0.344 | 0.586 → 0.946 | 7.4x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.613 → 0.952 | 0.339 | 0.589 → 0.946 | 1.8x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.562 → 0.878 | 0.316 | 0.531 → 0.871 | 2.8x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.577 → 0.878 | 0.301 | 0.539 → 0.871 | 2.7x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.597 → 0.881 | 0.284 | 0.344 → 0.574 | 5.4x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.711 → 0.970 | 0.260 | 0.668 → 0.969 | 4.9x advert_bytes | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.739 → 0.968 | 0.229 | 0.734 → 0.967 | 5x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.753 → 0.950 | 0.197 | 0.719 → 0.949 | 1.8x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.753 → 0.933 | 0.180 | 0.719 → 0.929 | 1.7x sr_bytes | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.705 → 0.878 | 0.173 | 0.705 → 0.871 | 1.5x sr_airtime | down | 3 |
| `RF-noise` | noise-profile | **text** | 0.710 → 0.878 | 0.168 | 0.703 → 0.872 | 1.4x sr_airtime | down | 4 |
| `MS-size` | nodes | **text** | 0.724 → 0.883 | 0.159 | 0.714 → 0.880 | 6.3x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.753 → 0.878 | 0.125 | 0.719 → 0.871 | 1.7x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.756 → 0.878 | 0.122 | 0.738 → 0.871 | 1.6x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.830 → 0.922 | 0.092 | 0.821 → 0.920 | 2.3x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.831 → 0.920 | 0.089 | 0.820 → 0.918 | 5.2x sr_airtime | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.834 → 0.922 | 0.088 | 0.824 → 0.920 | 2.3x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.878 → 0.966 | 0.088 | 0.871 → 0.965 | 1.4x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.878 → 0.960 | 0.082 | 0.871 → 0.953 | 1.5x sr_airtime | up | 3 |
| `SF-place-flat` | place | **held** | 0.909 → 0.981 | 0.072 | 0.863 → 0.878 | 3.2x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.909 → 0.981 | 0.072 | 0.863 → 0.878 | 3.2x sr_bytes | up | 6 |
| `RF-duct` | duct-per-hour | **text** | 0.878 → 0.950 | 0.072 | 0.871 → 0.945 | 1.5x bytes_on_air | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.857 → 0.924 | 0.067 | 0.847 → 0.920 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.857 → 0.924 | 0.067 | 0.847 → 0.920 | 2.3x bytes_on_air | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.657 → 0.718 | 0.061 | 0.654 → 0.716 | 1.2x sr_airtime | down | 2 |
| `FW-versions` | profile | **text** | 0.878 → 0.935 | 0.057 | 0.871 → 0.928 | 3.5x bytes_on_air | down | 5 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.826 → 0.878 | 0.052 | 0.812 → 0.871 | 1.5x sr_airtime | down | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.865 → 0.910 | 0.045 | 0.862 → 0.905 | 2.3x bytes_on_air | up | 4 |
| `FW-firmware` | profile | **text** | 0.878 → 0.923 | 0.045 | 0.871 → 0.914 | 3.5x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.867 → 0.910 | 0.043 | 0.863 → 0.904 | 2.2x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.938 → 0.981 | 0.043 | 0.871 → 0.876 | 21x sr_airtime | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.878 → 0.918 | 0.039 | 0.871 → 0.915 | 3.4x bytes_on_air | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.945 → 0.981 | 0.036 | 0.870 → 0.875 | 2.3x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.945 → 0.981 | 0.036 | 0.861 → 0.875 | 3.1x sr_bytes | down | 5 |
| `SF-cadence` | trigger | **held** | 0.947 → 0.981 | 0.034 | 0.849 → 0.874 | 13x advert_bytes | down | 4 |
| `MS-roles` | role-mix | **text** | 0.857 → 0.889 | 0.032 | 0.847 → 0.879 | 1.2x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.580 → 0.610 | 0.031 | 0.570 → 0.601 | 1.4x sr_airtime | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.878 → 0.905 | 0.027 | 0.871 → 0.875 | 2.3x sr_airtime | up | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.873 → 0.900 | 0.027 | 0.865 → 0.893 | 1.2x sr_bytes | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.859 → 0.884 | 0.025 | 0.849 → 0.881 | 9.7x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.890 → 0.913 | 0.023 | 0.884 → 0.909 | 1.1x sr_bytes | up | 2 |
| `AD-badrouters` | role-placement | **held** | 0.954 → 0.974 | 0.020 | 0.832 → 0.847 | 1.2x sr_bytes | down | 3 |
| `LD-diurnal` | diurnal | **text** | 0.878 → 0.898 | 0.019 | 0.871 → 0.893 | 1.4x sr_bytes | down | 3 |
| `SF-window-size` | window-size | **held** | 0.972 → 0.991 | 0.019 | 0.863 → 0.880 | 4.9x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **held** | 0.955 → 0.973 | 0.018 | 0.838 → 0.853 | 1.2x sr_airtime | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.878 → 0.894 | 0.016 | 0.871 → 0.888 | 1.3x bytes_on_air | up | 4 |
| `AD-worst` | role-placement | **text** | 0.820 → 0.836 | 0.016 | 0.814 → 0.832 | 1x bytes_on_air | down | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.867 → 0.878 | 0.011 | 0.860 → 0.872 | 1.2x sr_bytes | down | 4 |
| `SF-width` | short-id-bits | **held** | 0.973 → 0.983 | 0.010 | 0.866 → 0.874 | 3.1x advert_bytes | down | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.971 → 0.981 | 0.010 | 0.870 → 0.875 | 2.6x advert_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.871 → 0.881 | 0.010 | 0.864 → 0.875 | 5.4x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.974 → 0.984 | 0.010 | 0.869 → 0.876 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.974 → 0.984 | 0.010 | 0.869 → 0.876 | 1.2x sr_airtime | up | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.965 → 0.975 | 0.010 | 0.853 → 0.857 | 1.1x sr_bytes | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.972 → 0.981 | 0.009 | 0.861 → 0.871 | 7.5x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.972 → 0.981 | 0.009 | 0.861 → 0.871 | 7.5x sr_bytes | up | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.961 → 0.968 | 0.007 | 0.959 → 0.967 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.878 → 0.885 | 0.007 | 0.871 → 0.877 | 1.4x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.976 → 0.983 | 0.007 | 0.871 → 0.875 | 1x sr_bytes | down | 2 |
| `SF-resolve` | resolve | **text** | 0.878 → 0.884 | 0.006 | 0.871 → 0.877 | 5.7x advert_bytes | = | 3 |
| `SF-capacity-window` | capacity | **held** | 0.975 → 0.981 | 0.006 | 0.875 → 0.877 | 2.3x advert_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.976 → 0.981 | 0.006 | 0.869 → 0.871 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.976 → 0.981 | 0.006 | 0.869 → 0.871 | 5.3x advert_bytes | down | 5 |
| `PR-repeats` | extra-repeats | **text** | 0.878 → 0.883 | 0.005 | 0.871 → 0.879 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.968 → 0.972 | 0.004 | 0.967 → 0.971 | 1.2x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.853 → 0.857 | 0.003 | 0.853 → 0.857 | 1x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.977 → 0.980 | 0.003 | 0.870 → 0.870 | 2.3x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.978 → 0.981 | 0.003 | 0.871 → 0.873 | 2.6x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.878 → 0.881 | 0.003 | 0.871 → 0.874 | 1.1x sr_bytes | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.967 → 0.968 | 0.001 | 0.966 → 0.967 | 1x sr_bytes | down | 2 |

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
| none | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| sprinkled | 1 | 0.942 | 0.940 | 0.002 | - | - | 0.990 | 0.992 | 0.731 | 1.13x | 20.3/25.2/27.9% | 1.6/5.4% | 3 |
| arms-race | 1 | 0.966 | 0.965 | 0.001 | - | - | 0.994 | 0.995 | 0.892 | 0.97x | 20.6/25.0/27.9% | 1.1/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario coastal`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.909 | 0.900 | 0.010 | - | - | 0.981 | 0.982 | 0.681 | 1.21x | 18.1/23.9/29.8% | 1.8/4.3% | 3 |
| 0.3 | 1 | 0.960 | 0.953 | 0.007 | - | - | 0.999 | 0.999 | 0.889 | 1.00x | 22.7/26.1/32.2% | 1.4/4.8% | 3 |

### `AD-badrouters` - role-placement  `--scenario coastal`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.857 | 0.847 | 0.009 | - | - | 0.974 | 0.975 | 0.513 | 1.19x | 16.4/22.2/24.6% | 2.1/4.8% | 3 |
| inverse | 1 | 0.849 | 0.832 | 0.017 | - | - | 0.962 | 0.968 | 0.516 | 1.18x | 14.7/19.1/22.9% | 2.1/3.5% | 3 |
| random | 1 | 0.850 | 0.840 | 0.010 | - | - | 0.954 | 0.956 | 0.492 | 1.16x | 15.9/19.8/23.8% | 2.0/5.0% | 3 |

### `AD-flooding` - role-mix  `--scenario coastal`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.857 | 0.847 | 0.009 | - | - | 0.974 | 0.975 | 0.513 | 1.19x | 16.4/22.2/24.6% | 2.1/4.8% | 3 |
| all-routers | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.990 | 0.992 | 0.740 | 2.79x | 33.1/38.5/43.3% | 4.6/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario coastal`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.857 | 0.847 | 0.009 | - | - | 0.974 | 0.975 | 0.513 | 1.19x | 16.4/22.2/24.6% | 2.1/4.8% | 3 |
| no-mute | 1 | 0.899 | 0.892 | 0.008 | - | - | 0.983 | 0.984 | 0.601 | 1.35x | 17.8/21.4/25.8% | 2.1/4.9% | 3 |
| all-routers | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.990 | 0.992 | 0.740 | 2.79x | 33.1/38.5/43.3% | 4.6/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario coastal`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.857 | 0.847 | 0.009 | - | - | 0.974 | 0.975 | 0.513 | 1.19x | 16.4/22.2/24.6% | 2.1/4.8% | 3 |
| local-typical | 1 | 0.605 | 0.593 | 0.012 | - | - | 0.718 | 0.830 | 0.000 | 1.25x | 11.7/22.9/33.2% | 1.9/5.4% | 3 |
| basement-heavy | 1 | 0.078 | 0.075 | 0.003 | - | - | 0.189 | 0.197 | 0.000 | 0.66x | 2.2/7.5/14.2% | 0.6/3.4% | 3 |

> siting-mix=local-typical: decode_failures 22

### `AD-worst` - role-placement  `--scenario coastal`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.836 | 0.832 | 0.003 | - | - | 0.942 | 0.943 | 0.000 | 2.33x | 19.1/31.3/40.2% | 1.7/5.8% | 3 |
| inverse | 1 | 0.820 | 0.814 | 0.006 | - | - | 0.953 | 0.953 | 0.000 | 2.24x | 17.0/26.6/33.2% | 1.6/3.5% | 3 |

> role-placement=inverse: misdecodes 1

### `BL-control` - protocol  `--scenario coastal`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.868 | 0.868 | 0.000 | - | - | 0 | 0.000 | 0.650 | 1.35x | 17.6/22.3/27.2% | 2.1/5.1% | 3 |
| sr | 1 | 0.889 | 0.872 | 0.017 | - | - | 0.945 | 0.982 | 0.669 | 1.39x | 18.2/23.2/28.4% | 2.1/5.5% | 3 |

> protocol=sr: decode_failures 41

> slower: 6.18 s per simulated hour against 1.75 over 18 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario coastal`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.834 | 0.824 | 0.010 | - | - | 0.931 | 0.935 | 0.601 | 3.29x | 42.9/50.6/60.1% | 4.4/10.4% | 3 |
| 100 | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.976 | 0.977 | 0.758 | 1.61x | 21.6/25.7/31.5% | 2.2/5.2% | 3 |
| 120 | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.976 | 0.977 | 0.758 | 1.61x | 21.6/25.7/31.5% | 2.2/5.2% | 3 |
| 250 | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.976 | 0.977 | 0.758 | 1.61x | 21.6/25.7/31.5% | 2.2/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario coastal`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.349 | 0.344 | 0.005 | - | - | 0.597 | 0.640 | 0.160 | 11.35x | 41.7/62.9/71.9% | 3.9/11.1% | 3 |
| 120 | 1 | 0.580 | 0.570 | 0.010 | - | - | 0.875 | 0.876 | 0.222 | 4.62x | 17.0/31.8/40.6% | 1.5/6.6% | 3 |
| 250 | 1 | 0.584 | 0.574 | 0.010 | - | - | 0.881 | 0.881 | 0.225 | 4.42x | 16.2/30.0/38.4% | 1.4/6.2% | 3 |

> max-num-nodes=10: decode_failures 108

### `DB-platform` - platform-mix  `--scenario coastal`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.976 | 0.977 | 0.758 | 1.61x | 21.6/25.7/31.5% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.976 | 0.977 | 0.758 | 1.61x | 21.6/25.7/31.5% | 2.2/5.2% | 3 |
| constrained | 1 | 0.830 | 0.821 | 0.009 | - | - | 0.923 | 0.926 | 0.603 | 3.29x | 42.8/50.5/60.0% | 4.5/10.3% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario coastal`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.718 | 0.716 | 0.002 | - | - | 0.803 | 0.874 | 0.581 | 5.51x | 59.6/76.5/81.2% | 4.0/12.5% | 3 |
| 25 | 1 | 0.718 | 0.716 | 0.002 | - | - | 0.803 | 0.874 | 0.581 | 5.51x | 59.6/76.5/81.2% | 4.0/12.5% | 3 |
| 100 | 1 | 0.718 | 0.716 | 0.002 | - | - | 0.803 | 0.874 | 0.581 | 5.51x | 59.6/76.5/81.2% | 4.0/12.5% | 3 |
| 2000 | 1 | 0.718 | 0.716 | 0.002 | - | - | 0.803 | 0.874 | 0.581 | 5.51x | 59.6/76.5/81.2% | 4.0/12.5% | 3 |

> warm-num-nodes=0: queue drops 23.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 104

> warm-num-nodes=25: queue drops 23.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 104

> warm-num-nodes=100: queue drops 23.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 104

> warm-num-nodes=2000: queue drops 23.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 104

### `DG-burst` - burst-loss  `--scenario coastal`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.786 | 0.765 | 0.021 | - | - | 0.961 | 0.966 | 0.539 | 1.30x | 17.2/22.0/26.9% | 2.0/4.8% | 3 |
| 0.2 | 1 | 0.682 | 0.650 | 0.033 | - | - | 0.909 | 0.929 | 0.441 | 1.22x | 16.7/21.2/25.9% | 1.9/4.5% | 3 |
| 0.3 | 1 | 0.577 | 0.539 | 0.038 | - | - | 0.787 | 0.860 | 0.310 | 1.09x | 15.2/19.2/23.8% | 1.7/3.8% | 3 |

> burst-loss=0.2: decode_failures 19

> burst-loss=0.3: decode_failures 34

### `DG-loss` - extra-loss  `--scenario coastal`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.859 | 0.851 | 0.008 | - | - | 0.974 | 0.977 | 0.612 | 1.43x | 18.9/23.8/29.0% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.805 | 0.791 | 0.015 | - | - | 0.953 | 0.957 | 0.526 | 1.45x | 19.3/24.3/29.4% | 2.2/4.9% | 3 |
| 0.3 | 1 | 0.756 | 0.738 | 0.018 | - | - | 0.926 | 0.950 | 0.436 | 1.49x | 20.2/25.4/30.6% | 2.3/4.8% | 3 |

> extra-loss=0.3: decode_failures 4

### `DG-outage` - burst-loss  `--scenario coastal`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.780 | 0.766 | 0.014 | - | - | 0.906 | 0.962 | 0.531 | 1.29x | 17.3/22.1/26.7% | 1.9/4.8% | 3 |
| 0.2 | 1 | 0.661 | 0.634 | 0.027 | - | - | 0.877 | 0.930 | 0.461 | 1.21x | 16.4/21.0/25.8% | 1.8/4.3% | 3 |
| 0.3 | 1 | 0.562 | 0.531 | 0.031 | - | - | 0.766 | 0.887 | 0.324 | 1.15x | 16.0/20.3/25.0% | 1.7/3.9% | 3 |

> burst-loss=0.1: decode_failures 43

> burst-loss=0.2: decode_failures 36

> burst-loss=0.3: decode_failures 29

### `DM-mode` - dm-mode  `--scenario coastal`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.838 | 0.838 | 0.000 | - | - | 0.955 | 0.964 | 0.600 | 1.81x | 23.5/29.8/36.0% | 2.8/6.7% | 3 |
| directed-with-late-flood | 1 | 0.853 | 0.853 | 0.000 | - | - | 0.973 | 0.978 | 0.634 | 1.66x | 21.8/27.9/33.8% | 2.5/6.5% | 3 |
| m4-early-flood | 1 | 0.853 | 0.853 | 0.000 | - | - | 0.962 | 0.971 | 0.636 | 1.63x | 21.3/27.2/33.0% | 2.5/6.3% | 3 |

### `FW-firmware` - profile  `--scenario coastal`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.923 | 0.914 | 0.009 | - | - | 0.989 | 0.992 | 0.728 | 0.71x | 8.9/11.8/12.8% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario coastal`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.867 | 0.863 | 0.003 | - | - | 0.957 | 0.958 | 0.482 | 1.22x | 14.3/24.1/26.0% | 1.9/4.7% | 3 |
| 0.5 | 1 | 0.910 | 0.904 | 0.006 | - | - | 0.989 | 0.990 | 0.683 | 1.01x | 13.1/17.2/20.1% | 1.6/3.9% | 3 |
| 0.75 | 1 | 0.891 | 0.883 | 0.008 | - | - | 0.986 | 0.986 | 0.712 | 0.87x | 11.1/14.9/17.4% | 1.4/3.5% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario coastal`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.865 | 0.862 | 0.003 | - | - | 0.956 | 0.958 | 0.490 | 1.20x | 14.0/23.3/25.3% | 1.8/4.6% | 3 |
| 0.5 | 1 | 0.910 | 0.905 | 0.006 | - | - | 0.982 | 0.983 | 0.710 | 0.98x | 12.7/16.9/19.7% | 1.6/3.9% | 3 |
| 0.75 | 1 | 0.895 | 0.887 | 0.008 | - | - | 0.987 | 0.990 | 0.705 | 0.85x | 10.9/14.9/17.7% | 1.4/3.5% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario coastal`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.918 | 0.915 | 0.003 | - | - | 0.991 | 0.992 | 0.707 | 0.72x | 9.8/12.9/15.6% | 1.1/3.0% | 3 |
| signing=true | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `FW-versions` - profile  `--scenario coastal`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.920 | 0.909 | 0.011 | - | - | 0.993 | 0.994 | 0.703 | 0.72x | 9.6/13.2/13.8% | 1.1/2.6% | 3 |
| 2.5 | 1 | 0.926 | 0.917 | 0.009 | - | - | 0.997 | 0.997 | 0.732 | 0.73x | 9.4/12.9/13.5% | 1.1/2.5% | 3 |
| 2.6 | 1 | 0.920 | 0.911 | 0.010 | - | - | 0.989 | 0.989 | 0.716 | 0.71x | 9.5/13.2/13.7% | 1.1/2.7% | 3 |
| 2.7 | 1 | 0.935 | 0.928 | 0.007 | - | - | 0.997 | 0.999 | 0.708 | 0.71x | 9.8/13.5/14.6% | 1.0/3.0% | 3 |
| 2.8 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.912 | 0.909 | 0.003 | - | - | 0.990 | 0.990 | 0.717 | 0.90x | 11.6/14.9/17.9% | 1.4/3.4% | 3 |
| 900 | 1 | 0.831 | 0.820 | 0.011 | - | - | 0.954 | 0.956 | 0.599 | 2.17x | 28.2/35.6/43.0% | 3.3/8.2% | 3 |
| 300 | 1 | 0.560 | 0.539 | 0.021 | - | - | 0.760 | 0.850 | 0.346 | 4.67x | 55.8/67.9/76.4% | 7.0/16.2% | 3 |

> broadcast-interval-s=300: decode_failures 23

### `LD-chatty-hops` - broadcast-interval-s  `--scenario coastal`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.947 | 0.946 | 0.001 | - | - | 0.995 | 0.996 | 0.807 | 1.00x | 12.5/16.1/19.1% | 1.6/3.5% | 3 |
| 900 | 1 | 0.898 | 0.889 | 0.009 | - | - | 0.978 | 0.980 | 0.714 | 2.49x | 31.1/39.0/46.5% | 3.8/8.7% | 3 |
| 300 | 1 | 0.603 | 0.586 | 0.017 | - | - | 0.772 | 0.816 | 0.375 | 5.20x | 59.9/70.6/78.1% | 8.0/16.7% | 3 |

> broadcast-interval-s=300: decode_failures 36

### `LD-diurnal` - diurnal  `--scenario coastal`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.898 | 0.893 | 0.004 | - | - | 0.985 | 0.986 | 0.677 | 1.30x | 16.9/21.7/26.2% | 2.0/5.0% | 3 |
| sinusoid | 1 | 0.888 | 0.882 | 0.006 | - | - | 0.980 | 0.981 | 0.665 | 1.26x | 16.4/20.9/25.3% | 1.9/4.7% | 3 |
| commuter | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.831 | 0.820 | 0.011 | - | - | 0.954 | 0.956 | 0.599 | 2.17x | 28.2/35.6/43.0% | 3.3/8.2% | 3 |
| 3600 | 1 | 0.912 | 0.909 | 0.003 | - | - | 0.990 | 0.990 | 0.717 | 0.90x | 11.6/14.9/17.9% | 1.4/3.4% | 3 |
| 10800 | 1 | 0.920 | 0.917 | 0.002 | - | - | 0.993 | 0.993 | 0.715 | 0.61x | 7.9/10.2/12.3% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.993 | 0.994 | 0.696 | 0.44x | 5.6/7.3/8.7% | 0.7/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario coastal`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.877 | 0.871 | 0.007 | - | - | 0.978 | 0.978 | 0.655 | 1.45x | 18.9/24.1/29.1% | 2.2/5.5% | 3 |
| 1.0 | 1 | 0.870 | 0.861 | 0.009 | - | - | 0.979 | 0.980 | 0.634 | 1.61x | 21.2/27.0/32.8% | 2.4/6.2% | 3 |
| 4.0 | 1 | 0.826 | 0.812 | 0.014 | - | - | 0.958 | 0.962 | 0.597 | 2.01x | 26.7/34.3/41.9% | 3.0/8.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario coastal`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.718 | 0.716 | 0.002 | - | - | 0.803 | 0.874 | 0.581 | 5.51x | 59.6/76.5/81.2% | 4.0/12.5% | 3 |
| 1.0 | 1 | 0.657 | 0.654 | 0.003 | - | - | 0.755 | 0.833 | 0.542 | 5.90x | 62.6/76.9/81.0% | 4.4/13.4% | 3 |

> traceroute-per-hour=0.0: queue drops 23.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 104

> traceroute-per-hour=1.0: queue drops 31.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 99

### `MS-density` - nodes  `--scenario coastal`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.711 | 0.668 | 0.043 | - | - | 0.804 | 0.951 | 0.398 | 1.27x | 17.9/26.7/28.2% | 2.6/6.3% | 3 |
| 60 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 90 | 1 | 0.951 | 0.948 | 0.003 | - | - | 0.998 | 0.998 | 0.770 | 1.65x | 20.2/28.4/33.2% | 1.5/5.0% | 3 |
| 120 | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.998 | 0.998 | 0.886 | 2.14x | 25.0/44.1/49.8% | 1.4/5.2% | 3 |
| 150 | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 0.999 | 0.872 | 2.48x | 28.5/44.4/50.2% | 1.2/5.5% | 3 |

> nodes=40: decode_failures 20

### `MS-hopscale` - nodes  `--scenario coastal`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 120 | 1 | 0.805 | 0.785 | 0.020 | - | - | 0.924 | 0.960 | 0.361 | 2.35x | 15.3/31.1/41.5% | 1.6/5.6% | 3 |
| 250 | 1 | 0.571 | 0.561 | 0.010 | - | - | 0.865 | 0.866 | 0.223 | 4.88x | 18.1/33.4/43.0% | 1.5/7.1% | 3 |
| 500 | 1 | 0.334 | 0.329 | 0.004 | - | - | 0.542 | 0.543 | 0.108 | 10.09x | 19.1/33.0/53.8% | 1.7/6.3% | 3 |

> nodes=120: decode_failures 40

> nodes=500: decode_failures 25

### `MS-oversubscribed` - nodes  `--scenario coastal`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.805 | 0.783 | 0.022 | - | - | 0.934 | 0.966 | 0.362 | 2.17x | 14.1/28.8/38.6% | 1.5/5.1% | 3 |
| 250 | 1 | 0.580 | 0.570 | 0.010 | - | - | 0.875 | 0.876 | 0.222 | 4.62x | 17.0/31.8/40.6% | 1.5/6.6% | 3 |
| 500 | 1 | 0.336 | 0.332 | 0.004 | - | - | 0.542 | 0.544 | 0.107 | 9.58x | 18.2/31.2/50.7% | 1.6/5.9% | 3 |

> nodes=120: decode_failures 17

> nodes=500: decode_failures 13

### `MS-roles` - role-mix  `--scenario coastal`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.889 | 0.879 | 0.010 | - | - | 0.984 | 0.984 | 0.578 | 1.35x | 17.5/22.6/27.3% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.857 | 0.847 | 0.009 | - | - | 0.974 | 0.975 | 0.513 | 1.19x | 16.4/22.2/24.6% | 2.1/4.8% | 3 |

### `MS-roles-fav` - role-mix  `--scenario coastal`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.900 | 0.893 | 0.008 | - | - | 0.981 | 0.981 | 0.630 | 1.40x | 18.2/23.3/27.8% | 2.1/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.873 | 0.865 | 0.009 | - | - | 0.958 | 0.958 | 0.644 | 1.34x | 18.8/24.5/27.7% | 2.3/4.9% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario coastal`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.05 | 1 | 0.882 | 0.875 | 0.006 | - | - | 0.976 | 0.977 | 0.657 | 1.46x | 19.9/24.7/30.9% | 2.1/5.2% | 3 |
| 0.1 | 1 | 0.893 | 0.888 | 0.005 | - | - | 0.977 | 0.977 | 0.648 | 1.60x | 22.0/27.8/33.3% | 2.2/5.3% | 3 |
| 0.2 | 1 | 0.894 | 0.888 | 0.006 | - | - | 0.973 | 0.974 | 0.631 | 1.76x | 23.8/30.2/38.7% | 2.4/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario coastal`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| local-typical | 1 | 0.646 | 0.629 | 0.017 | - | - | 0.822 | 0.831 | 0.000 | 1.53x | 12.9/23.1/33.6% | 2.5/5.3% | 3 |
| event | 1 | 0.253 | 0.242 | 0.011 | - | - | 0.480 | 0.494 | 0.000 | 1.26x | 6.4/14.2/20.1% | 2.2/4.7% | 3 |
| backbone | 1 | 0.981 | 0.980 | 0.001 | - | - | 1.000 | 1.000 | 0.944 | 1.06x | 28.6/36.5/38.7% | 1.4/5.4% | 3 |

> siting-mix=event: decode_failures 6

### `MS-size` - nodes  `--scenario coastal`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.875 | 0.861 | 0.014 | - | - | 0.969 | 0.972 | 0.788 | 1.40x | 24.8/34.9/36.5% | 2.9/7.8% | 3 |
| 60 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 90 | 1 | 0.883 | 0.880 | 0.002 | - | - | 0.970 | 0.971 | 0.598 | 1.68x | 17.2/24.2/25.8% | 1.7/4.9% | 3 |
| 120 | 1 | 0.805 | 0.785 | 0.020 | - | - | 0.924 | 0.960 | 0.361 | 2.35x | 15.3/31.1/41.5% | 1.6/5.6% | 3 |
| 150 | 1 | 0.724 | 0.714 | 0.010 | - | - | 0.961 | 0.963 | 0.287 | 2.77x | 15.6/31.9/42.0% | 1.5/5.8% | 3 |

> nodes=120: decode_failures 40

### `MS-stretch` - stretch  `--scenario coastal`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 1.25 | 1 | 0.655 | 0.642 | 0.013 | - | - | 0.844 | 0.863 | 0.282 | 1.32x | 12.3/18.8/21.1% | 1.9/4.9% | 3 |
| 1.5 | 1 | 0.397 | 0.384 | 0.013 | - | - | 0.660 | 0.663 | 0.084 | 1.19x | 8.3/14.7/17.6% | 1.6/4.3% | 3 |
| 2.0 | 1 | 0.095 | 0.094 | 0.001 | - | - | 0.187 | 0.192 | 0.000 | 0.80x | 3.2/7.9/11.7% | 1.2/2.7% | 3 |

> stretch=1.25: decode_failures 27

> stretch=1.5: decode_failures 1

### `MS-topology` - topology  `--scenario coastal`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| clustered | 1 | 0.934 | 0.924 | 0.011 | - | - | 0.998 | 0.998 | 0.423 | 1.03x | 26.9/37.0/38.0% | 1.3/5.6% | 3 |
| corridor | 1 | 0.613 | 0.589 | 0.025 | - | - | 0.833 | 0.854 | 0.210 | 1.22x | 14.3/19.5/22.8% | 2.0/5.1% | 3 |
| hub | 1 | 0.952 | 0.946 | 0.006 | - | - | 0.982 | 0.984 | 0.704 | 1.15x | 28.8/37.6/38.3% | 1.6/5.6% | 3 |

> topology=corridor: decode_failures 10

### `PR-crladder` - coding-rate-ladder  `--scenario coastal`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.853 | 0.853 | 0.000 | - | - | 0.973 | 0.978 | 0.634 | 1.66x | 21.8/27.9/33.8% | 2.5/6.5% | 3 |
| True | 1 | 0.857 | 0.857 | 0.000 | - | - | 0.975 | 0.980 | 0.625 | 1.66x | 21.8/27.9/33.8% | 2.5/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario coastal`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.857 | 0.857 | 0.000 | - | - | 0.975 | 0.980 | 0.625 | 1.66x | 21.8/27.9/33.8% | 2.5/6.5% | 3 |
| m4-early-flood | 1 | 0.853 | 0.853 | 0.000 | - | - | 0.965 | 0.975 | 0.620 | 1.66x | 21.7/27.5/33.5% | 2.5/6.5% | 3 |

### `PR-protocol` - protocol  `--scenario coastal`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.868 | 0.868 | 0.000 | - | - | 0 | 0.000 | 0.650 | 1.35x | 17.6/22.3/27.2% | 2.1/5.1% | 3 |
| chain | 1 | 0.866 | 0.863 | 0.003 | - | - | 0.946 | 0.977 | 0.650 | 1.52x | 20.0/25.6/31.2% | 2.3/5.9% | 3 |
| sr | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario coastal`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| True | 1 | 0.883 | 0.879 | 0.004 | - | - | 0.979 | 0.979 | 0.668 | 1.39x | 18.1/23.1/27.8% | 2.1/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario coastal`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.998 | 0.998 | 0.886 | 2.14x | 25.0/44.1/49.8% | 1.4/5.2% | 3 |
| True | 1 | 0.967 | 0.966 | 0.001 | - | - | 0.998 | 0.998 | 0.891 | 2.13x | 24.7/43.8/49.4% | 1.4/5.2% | 3 |

### `RF-bw500` - preset  `--scenario coastal`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.104 | 0.102 | 0.002 | - | - | 0.201 | 0.203 | 0.000 | 0.04x | 0.1/0.4/0.6% | 0.1/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.456 | 0.445 | 0.011 | - | - | 0.744 | 0.747 | 0.113 | 0.27x | 2.0/3.8/4.4% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.801 | 0.794 | 0.007 | - | - | 0.873 | 0.875 | 0.418 | 1.32x | 13.5/18.7/23.2% | 2.1/4.9% | 3 |

### `RF-duct` - duct-per-hour  `--scenario coastal`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.895 | 0.887 | 0.008 | - | - | 0.984 | 0.984 | 0.705 | 1.31x | 19.6/24.3/28.7% | 2.0/5.3% | 3 |
| 1.0 | 1 | 0.950 | 0.945 | 0.004 | - | - | 0.994 | 0.994 | 0.844 | 0.92x | 24.5/29.4/31.8% | 1.1/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario coastal`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.312 | 0.288 | 0.025 | - | - | 0.570 | 0.624 | 0.000 | 0.14x | 1.0/1.8/2.4% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| LITE_FAST | 1 | 0.842 | 0.825 | 0.017 | - | - | 0.960 | 0.963 | 0.489 | 1.04x | 11.9/15.5/18.3% | 1.5/4.1% | 3 |
| NARROW_SLOW | 1 | 0.827 | 0.823 | 0.004 | - | - | 0.954 | 0.956 | 0.452 | 1.30x | 15.4/21.4/24.4% | 1.8/5.1% | 3 |

> preset=SHORT_FAST: decode_failures 17

### `RF-noise` - noise-profile  `--scenario coastal`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| temporal | 1 | 0.801 | 0.788 | 0.013 | - | - | 0.951 | 0.956 | 0.512 | 1.39x | 17.5/22.5/27.3% | 2.1/5.1% | 3 |
| transient | 1 | 0.878 | 0.872 | 0.006 | - | - | 0.982 | 0.982 | 0.647 | 1.37x | 17.9/22.7/27.4% | 2.1/5.2% | 3 |
| periodic | 1 | 0.710 | 0.703 | 0.008 | - | - | 0.815 | 0.824 | 0.493 | 1.27x | 16.7/21.2/25.7% | 1.9/4.5% | 3 |

### `RF-preset` - preset  `--scenario coastal`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.312 | 0.288 | 0.025 | - | - | 0.570 | 0.624 | 0.000 | 0.14x | 1.0/1.8/2.4% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| LONG_MODERATE | 1 | 0.845 | 0.830 | 0.015 | - | - | 0.961 | 0.965 | 0.644 | 3.50x | 51.9/61.6/66.2% | 5.2/12.5% | 3 |

> preset=SHORT_FAST: decode_failures 17

> preset=LONG_MODERATE: decode_failures 6

### `RF-preset-turbo` - preset  `--scenario coastal`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.035 | 0.035 | 0.000 | - | - | 0.030 | 0.090 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.104 | 0.102 | 0.002 | - | - | 0.201 | 0.203 | 0.000 | 0.04x | 0.1/0.4/0.6% | 0.1/0.1% | 3 |
| LONG_FAST | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| LONG_TURBO | 1 | 0.801 | 0.794 | 0.007 | - | - | 0.873 | 0.875 | 0.418 | 1.32x | 13.5/18.7/23.2% | 2.1/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.858 | 0.853 | 0.005 | - | - | 0.961 | 0.963 | 0.560 | 1.89x | 23.1/29.3/35.0% | 2.9/6.9% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario coastal`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.818 | 0.810 | 0.008 | - | - | 0.920 | 0.920 | 0.597 | 1.35x | 17.8/22.6/27.4% | 2.0/5.1% | 3 |
| 10000 | 1 | 0.710 | 0.703 | 0.008 | - | - | 0.815 | 0.824 | 0.493 | 1.27x | 16.7/21.2/25.7% | 1.9/4.5% | 3 |
| 4000 | 1 | 0.440 | 0.436 | 0.004 | - | - | 0.502 | 0.565 | 0.258 | 1.09x | 14.8/18.7/22.9% | 1.7/3.5% | 3 |
| 2000 | 1 | 0.102 | 0.102 | 0.000 | - | - | 0.125 | 0.203 | 0.043 | 0.72x | 9.9/12.9/16.0% | 1.1/1.9% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 1

### `RF-stretch-duct` - duct-per-hour  `--scenario coastal`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.397 | 0.384 | 0.013 | - | - | 0.660 | 0.663 | 0.084 | 1.19x | 8.3/14.7/17.6% | 1.6/4.3% | 3 |
| 1.0 | 1 | 0.757 | 0.739 | 0.018 | - | - | 0.871 | 0.871 | 0.603 | 0.97x | 17.1/23.1/24.5% | 1.3/4.7% | 3 |

> duct-per-hour=0.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario coastal`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 22 | 1 | 0.409 | 0.400 | 0.009 | - | - | 0.672 | 0.679 | 0.104 | 1.23x | 8.5/14.9/17.6% | 1.7/4.3% | 3 |
| 17 | 1 | 0.104 | 0.102 | 0.002 | - | - | 0.220 | 0.220 | 0.000 | 0.84x | 3.7/8.9/11.9% | 1.4/2.9% | 3 |
| 14 | 1 | 0.050 | 0.050 | 0.000 | - | - | 0.084 | 0.091 | 0.000 | 0.53x | 1.7/4.8/7.0% | 0.6/1.9% | 3 |

> tx-power=14: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario coastal`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.998 | 0.998 | 0.886 | 2.14x | 25.0/44.1/49.8% | 1.4/5.2% | 3 |
| True | 1 | 0.961 | 0.959 | 0.002 | - | - | 0.996 | 0.996 | 0.867 | 2.47x | 28.2/49.4/55.2% | 1.7/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario coastal`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.884 | 0.006 | - | - | 0.978 | 0.979 | 0.668 | 1.44x | 19.9/24.1/29.9% | 2.1/5.3% | 3 |
| True | 1 | 0.913 | 0.909 | 0.004 | - | - | 0.978 | 0.978 | 0.728 | 1.53x | 20.9/25.0/30.9% | 2.3/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario coastal`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| random | 1 | 0.885 | 0.877 | 0.008 | - | - | 0.988 | 0.990 | 0.621 | 1.35x | 17.6/22.5/27.3% | 2.0/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario coastal`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.753 | 0.719 | 0.034 | - | - | 0.968 | 0.974 | 0.335 | 1.00x | 14.0/18.2/22.7% | 1.4/4.7% | 3 |
| 7 | 1 | 0.933 | 0.929 | 0.004 | - | - | 0.988 | 0.990 | 0.785 | 1.52x | 19.2/24.4/29.0% | 2.4/5.4% | 3 |
| 15 | 1 | 0.950 | 0.949 | 0.001 | - | - | 0.989 | 0.990 | 0.850 | 1.54x | 19.3/24.4/29.3% | 2.4/5.4% | 3 |
| 32 | 1 | 0.949 | 0.948 | 0.001 | - | - | 0.987 | 0.988 | 0.840 | 1.52x | 19.2/24.4/29.1% | 2.4/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario coastal`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.753 | 0.719 | 0.034 | - | - | 0.968 | 0.974 | 0.335 | 1.00x | 14.0/18.2/22.7% | 1.4/4.7% | 3 |
| 5 | 1 | 0.883 | 0.872 | 0.011 | - | - | 0.981 | 0.982 | 0.595 | 1.40x | 18.2/23.1/27.8% | 2.1/5.2% | 3 |
| 7 | 1 | 0.933 | 0.929 | 0.004 | - | - | 0.988 | 0.990 | 0.785 | 1.52x | 19.2/24.4/29.0% | 2.4/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario coastal`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.876 | 0.876 | 0.000 | - | - | 0.938 | 0.980 | 0.656 | 1.36x | 17.7/22.6/27.4% | 2.1/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario coastal`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.753 | 0.719 | 0.034 | - | - | 0.968 | 0.974 | 0.335 | 1.00x | 14.0/18.2/22.7% | 1.4/4.7% | 3 |
| True | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario coastal`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| BALANCED | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| STRICT | 1 | 0.705 | 0.705 | 0.000 | - | - | 0.814 | 0.817 | 0.503 | 1.53x | 19.8/25.3/30.3% | 2.4/5.6% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario coastal`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| dm | 1 | 0.880 | 0.873 | 0.006 | - | - | 0.978 | 0.978 | 0.656 | 1.37x | 17.9/22.8/27.7% | 2.1/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario coastal`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.876 | 0.870 | 0.007 | - | - | 0.971 | 0.973 | 0.660 | 1.38x | 18.1/23.0/27.9% | 2.1/5.3% | 3 |
| local | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| time | 1 | 0.881 | 0.875 | 0.007 | - | - | 0.979 | 0.982 | 0.658 | 1.39x | 18.1/23.1/28.1% | 2.1/5.3% | 3 |
| window | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.978 | 0.980 | 0.656 | 1.36x | 17.8/22.7/27.5% | 2.1/5.2% | 3 |

> bucket-mode=global: misdecodes 24

> bucket-mode=time: misdecodes 34

> bucket-mode=window: misdecodes 26

### `SF-bucket-time` - time-bucket-s  `--scenario coastal`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.871 | 0.864 | 0.007 | - | - | 0.977 | 0.982 | 0.652 | 1.49x | 19.4/24.8/29.9% | 2.3/5.7% | 3 |
| 1800 | 1 | 0.881 | 0.875 | 0.007 | - | - | 0.979 | 0.982 | 0.658 | 1.39x | 18.1/23.1/28.1% | 2.1/5.3% | 3 |
| 3600 | 1 | 0.877 | 0.870 | 0.007 | - | - | 0.980 | 0.981 | 0.654 | 1.38x | 18.0/22.9/27.6% | 2.1/5.3% | 3 |

> time-bucket-s=600: misdecodes 105

> time-bucket-s=1800: misdecodes 34

> time-bucket-s=3600: misdecodes 10

### `SF-cadence` - trigger  `--scenario coastal`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| interval | 1 | 0.871 | 0.861 | 0.010 | - | - | 0.980 | 0.983 | 0.641 | 1.74x | 23.1/29.5/35.7% | 2.5/6.9% | 3 |
| aimd | 1 | 0.875 | 0.874 | 0.002 | - | - | 0.947 | 0.981 | 0.657 | 1.36x | 17.8/22.6/27.6% | 2.1/5.2% | 3 |
| bucket+interval | 1 | 0.859 | 0.849 | 0.010 | - | - | 0.969 | 0.969 | 0.625 | 1.76x | 23.2/29.6/35.9% | 2.6/7.1% | 3 |

> trigger=interval: misdecodes 5

> trigger=aimd: misdecodes 2

> trigger=bucket+interval: misdecodes 7

### `SF-capacity` - capacity  `--scenario coastal`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.877 | 0.870 | 0.008 | - | - | 0.977 | 0.979 | 0.650 | 1.37x | 18.0/22.9/27.8% | 2.1/5.3% | 3 |
| 8 | 1 | 0.877 | 0.870 | 0.007 | - | - | 0.980 | 0.981 | 0.650 | 1.37x | 17.9/22.8/27.7% | 2.1/5.2% | 3 |
| 16 | 1 | 0.876 | 0.871 | 0.005 | - | - | 0.976 | 0.976 | 0.654 | 1.38x | 17.9/22.9/27.7% | 2.1/5.2% | 3 |
| 32 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 50 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.976 | 0.977 | 0.656 | 1.38x | 18.0/22.9/27.9% | 2.1/5.3% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 17

### `SF-capacity-local` - capacity  `--scenario coastal`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.877 | 0.870 | 0.008 | - | - | 0.977 | 0.979 | 0.650 | 1.37x | 18.0/22.9/27.8% | 2.1/5.3% | 3 |
| 8 | 1 | 0.877 | 0.870 | 0.007 | - | - | 0.980 | 0.981 | 0.650 | 1.37x | 17.9/22.8/27.7% | 2.1/5.2% | 3 |
| 16 | 1 | 0.876 | 0.871 | 0.005 | - | - | 0.976 | 0.976 | 0.654 | 1.38x | 17.9/22.9/27.7% | 2.1/5.2% | 3 |
| 32 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 50 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.976 | 0.977 | 0.656 | 1.38x | 18.0/22.9/27.9% | 2.1/5.3% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 17

### `SF-capacity-window` - capacity  `--scenario coastal`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.884 | 0.877 | 0.007 | - | - | 0.981 | 0.984 | 0.652 | 1.34x | 17.5/22.4/27.1% | 2.0/5.1% | 3 |
| 16 | 1 | 0.883 | 0.876 | 0.006 | - | - | 0.975 | 0.977 | 0.664 | 1.37x | 17.9/22.7/27.5% | 2.1/5.2% | 3 |
| 32 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.978 | 0.980 | 0.656 | 1.36x | 17.8/22.7/27.5% | 2.1/5.2% | 3 |

> capacity=8: misdecodes 15

> capacity=8: decode_failures 7

> capacity=16: misdecodes 23

> capacity=16: decode_failures 1

> capacity=32: misdecodes 26

### `SF-catchup` - catch-up-hours  `--scenario coastal`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.859 | 0.849 | 0.010 | - | - | 0.969 | 0.969 | 0.625 | 1.76x | 23.2/29.6/35.9% | 2.6/7.1% | 3 |
| 02-06 | 1 | 0.884 | 0.881 | 0.003 | - | - | 0.960 | 0.981 | 0.669 | 1.40x | 18.3/23.3/28.2% | 2.1/5.4% | 3 |
| 00-08 | 1 | 0.879 | 0.875 | 0.004 | - | - | 0.957 | 0.977 | 0.648 | 1.47x | 19.3/24.6/29.8% | 2.2/5.7% | 3 |

> catch-up-hours=: misdecodes 7

> catch-up-hours=02-06: decode_failures 3

> catch-up-hours=00-08: decode_failures 3

### `SF-hops-flat` - hops-apart  `--scenario coastal`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.878 | 0.875 | 0.003 | - | - | 0.949 | 0.950 | 0.644 | 1.38x | 18.1/23.0/27.9% | 2.1/5.2% | 3 |
| 2 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 3 | 1 | 0.889 | 0.872 | 0.017 | - | - | 0.945 | 0.982 | 0.669 | 1.39x | 18.2/23.2/28.4% | 2.1/5.5% | 3 |
| 4 | 1 | 0.891 | 0.870 | 0.021 | - | - | 0.954 | 0.984 | 0.650 | 1.40x | 18.3/23.4/28.6% | 2.1/5.4% | 3 |

> hops-apart=3: decode_failures 41

> hops-apart=4: decode_failures 22

### `SF-hops-spread` - hops-apart  `--scenario coastal`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.878 | 0.875 | 0.003 | - | - | 0.949 | 0.950 | 0.644 | 1.38x | 18.1/23.0/27.9% | 2.1/5.2% | 3 |
| 2 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 3 | 1 | 0.889 | 0.872 | 0.017 | - | - | 0.945 | 0.982 | 0.669 | 1.39x | 18.2/23.2/28.4% | 2.1/5.5% | 3 |
| 4 | 1 | 0.891 | 0.870 | 0.021 | - | - | 0.954 | 0.984 | 0.650 | 1.40x | 18.3/23.4/28.6% | 2.1/5.4% | 3 |
| 5 | 1 | 0.888 | 0.861 | 0.027 | - | - | 0.946 | 0.977 | 0.662 | 1.41x | 18.4/23.5/28.9% | 2.1/5.6% | 3 |

> hops-apart=3: decode_failures 41

> hops-apart=4: decode_failures 22

> hops-apart=5: decode_failures 25

### `SF-jitter-global` - advert-jitter-s  `--scenario coastal`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.974 | 0.974 | 0.644 | 1.38x | 18.0/23.0/27.8% | 2.1/5.3% | 3 |
| 30 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 120 | 1 | 0.882 | 0.876 | 0.007 | - | - | 0.984 | 0.984 | 0.653 | 1.39x | 18.2/23.1/28.1% | 2.1/5.3% | 3 |
| 600 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.978 | 0.978 | 0.671 | 1.38x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario coastal`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.974 | 0.974 | 0.644 | 1.38x | 18.0/23.0/27.8% | 2.1/5.3% | 3 |
| 30 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 120 | 1 | 0.882 | 0.876 | 0.007 | - | - | 0.984 | 0.984 | 0.653 | 1.39x | 18.2/23.1/28.1% | 2.1/5.3% | 3 |
| 600 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.978 | 0.978 | 0.671 | 1.38x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `SF-place-flat` - place  `--scenario coastal`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.898 | 0.874 | 0.024 | - | - | 0.909 | 0.970 | 0.659 | 1.41x | 18.2/23.6/28.2% | 2.1/5.1% | 3 |
| routers | 1 | 0.878 | 0.870 | 0.008 | - | - | 0.980 | 0.982 | 0.671 | 1.37x | 17.9/22.8/27.4% | 2.1/5.3% | 3 |
| alternate-routers | 1 | 0.875 | 0.868 | 0.007 | - | - | 0.974 | 0.975 | 0.650 | 1.38x | 18.0/23.0/27.8% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.881 | 0.878 | 0.003 | - | - | 0.980 | 0.981 | 0.654 | 1.38x | 18.0/22.9/27.8% | 2.1/5.2% | 3 |
| random-clients | 1 | 0.869 | 0.863 | 0.006 | - | - | 0.972 | 0.972 | 0.651 | 1.41x | 18.4/23.4/28.3% | 2.1/5.2% | 3 |
| hops-apart | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

> place=spread: decode_failures 40

### `SF-place-spread` - place  `--scenario coastal`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.898 | 0.874 | 0.024 | - | - | 0.909 | 0.970 | 0.659 | 1.41x | 18.2/23.6/28.2% | 2.1/5.1% | 3 |
| routers | 1 | 0.878 | 0.870 | 0.008 | - | - | 0.980 | 0.982 | 0.671 | 1.37x | 17.9/22.8/27.4% | 2.1/5.3% | 3 |
| alternate-routers | 1 | 0.875 | 0.868 | 0.007 | - | - | 0.974 | 0.975 | 0.650 | 1.38x | 18.0/23.0/27.8% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.881 | 0.878 | 0.003 | - | - | 0.980 | 0.981 | 0.654 | 1.38x | 18.0/22.9/27.8% | 2.1/5.2% | 3 |
| random-clients | 1 | 0.869 | 0.863 | 0.006 | - | - | 0.972 | 0.972 | 0.651 | 1.41x | 18.4/23.4/28.3% | 2.1/5.2% | 3 |
| hops-apart | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

> place=spread: decode_failures 40

### `SF-provide-transport` - provide-transport  `--scenario coastal`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| broadcast | 1 | 0.905 | 0.875 | 0.031 | - | - | 0.983 | 0.984 | 0.676 | 1.43x | 18.6/23.7/28.6% | 2.1/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario coastal`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| heard | 1 | 0.881 | 0.874 | 0.006 | - | - | 0.983 | 0.986 | 0.664 | 1.38x | 18.1/23.0/27.8% | 2.1/5.3% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario coastal`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.905 | 0.875 | 0.031 | - | - | 0.983 | 0.984 | 0.676 | 1.43x | 18.6/23.7/28.6% | 2.1/5.4% | 3 |
| heard | 1 | 0.903 | 0.871 | 0.032 | - | - | 0.976 | 0.979 | 0.688 | 1.41x | 18.4/23.4/28.3% | 2.1/5.3% | 3 |

> replay-ordering=heard: misdecodes 6

### `SF-resolve` - resolve  `--scenario coastal`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| enum | 1 | 0.884 | 0.877 | 0.007 | - | - | 0.978 | 0.980 | 0.663 | 1.36x | 17.9/22.8/27.7% | 2.1/5.3% | 3 |
| hybrid | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario coastal`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.878 | 0.870 | 0.008 | - | - | 0.980 | 0.982 | 0.671 | 1.37x | 17.9/22.8/27.4% | 2.1/5.3% | 3 |
| 6 | 1 | 0.877 | 0.870 | 0.007 | - | - | 0.977 | 0.978 | 0.653 | 1.41x | 18.5/23.6/28.5% | 2.1/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario coastal`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.873 | 0.870 | 0.003 | - | - | 0.972 | 0.973 | 0.637 | 1.36x | 17.8/22.6/27.5% | 2.1/5.2% | 2 |
| 3 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 5 | 1 | 0.877 | 0.869 | 0.008 | - | - | 0.980 | 0.981 | 0.662 | 1.40x | 18.2/23.3/28.2% | 2.1/5.5% | 5 |
| 8 | 1 | 0.876 | 0.861 | 0.015 | - | - | 0.976 | 0.977 | 0.660 | 1.45x | 18.8/23.9/29.0% | 2.2/5.7% | 8 |

### `SF-servers-spread` - servers  `--scenario coastal`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.873 | 0.870 | 0.003 | - | - | 0.972 | 0.973 | 0.637 | 1.36x | 17.8/22.6/27.5% | 2.1/5.2% | 2 |
| 3 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 5 | 1 | 0.877 | 0.869 | 0.008 | - | - | 0.980 | 0.981 | 0.662 | 1.40x | 18.2/23.3/28.2% | 2.1/5.5% | 5 |
| 8 | 1 | 0.876 | 0.861 | 0.015 | - | - | 0.976 | 0.977 | 0.660 | 1.45x | 18.8/23.9/29.0% | 2.2/5.7% | 8 |

### `SF-signed` - signed  `--scenario coastal`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| True | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario coastal`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.877 | 0.868 | 0.009 | - | - | 0.979 | 0.981 | 0.656 | 1.29x | 16.8/21.5/26.0% | 2.0/4.9% | 3 |
| 1 | 1 | 0.875 | 0.868 | 0.008 | - | - | 0.974 | 0.975 | 0.647 | 1.30x | 16.9/21.5/26.0% | 2.0/4.9% | 3 |
| 2 | 1 | 0.878 | 0.872 | 0.006 | - | - | 0.973 | 0.974 | 0.645 | 1.29x | 16.8/21.5/26.0% | 2.0/4.8% | 3 |
| 4 | 1 | 0.867 | 0.860 | 0.007 | - | - | 0.969 | 0.970 | 0.661 | 1.30x | 17.0/21.8/26.3% | 2.0/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario coastal`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.983 | 0.983 | 0.661 | 1.37x | 17.8/22.8/27.6% | 2.1/5.2% | 3 |
| 24 | 1 | 0.872 | 0.866 | 0.006 | - | - | 0.973 | 0.973 | 0.649 | 1.35x | 17.8/22.5/27.3% | 2.0/5.2% | 3 |
| 32 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.981 | 0.982 | 0.650 | 1.39x | 18.1/23.1/27.9% | 2.1/5.3% | 3 |
| 64 | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.975 | 0.975 | 0.659 | 1.37x | 17.9/22.7/27.5% | 2.1/5.2% | 3 |

### `SF-window-size` - window-size  `--scenario coastal`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.871 | 0.863 | 0.008 | - | - | 0.972 | 0.974 | 0.648 | 1.45x | 19.0/24.2/29.2% | 2.2/5.5% | 3 |
| 16 | 1 | 0.888 | 0.880 | 0.007 | - | - | 0.991 | 0.992 | 0.652 | 1.39x | 18.1/23.0/28.0% | 2.1/5.3% | 3 |
| 32 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.978 | 0.980 | 0.656 | 1.36x | 17.8/22.7/27.5% | 2.1/5.2% | 3 |

> window-size=8: misdecodes 117

> window-size=16: misdecodes 59

> window-size=32: misdecodes 26

### `TH-congestion` - no-congestion-scaling  `--scenario coastal`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.998 | 0.998 | 0.886 | 2.14x | 25.0/44.1/49.8% | 1.4/5.2% | 3 |
| True | 1 | 0.739 | 0.734 | 0.004 | - | - | 0.843 | 0.883 | 0.591 | 5.34x | 58.4/76.0/80.7% | 3.9/12.0% | 3 |

> no-congestion-scaling=True: queue drops 19.7% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 78

### `TH-congestion-input` - congestion-input  `--scenario coastal`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.580 | 0.570 | 0.010 | - | - | 0.875 | 0.876 | 0.222 | 4.62x | 17.0/31.8/40.6% | 1.5/6.6% | 3 |
| truesize | 1 | 0.610 | 0.601 | 0.009 | - | - | 0.902 | 0.902 | 0.239 | 3.59x | 13.0/26.2/33.8% | 1.1/5.7% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario coastal`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.972 | 0.971 | 0.001 | - | - | 0.999 | 1.000 | 0.897 | 1.98x | 23.0/41.2/46.5% | 1.3/4.9% | 3 |
| adaptive | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.998 | 0.998 | 0.886 | 2.14x | 25.0/44.1/49.8% | 1.4/5.2% | 3 |

