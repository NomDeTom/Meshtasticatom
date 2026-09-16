# Sweep blocks-2026-09-16-8922254

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 8922254 · seeds 8922254
- **blocks** 87 run
- **compute** 9.5 h of simulator time across every cell
- **generated** 2026-09-16T08:54:44+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>84 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 37
- AD-badrouters: slower: 4.65 s per simulated hour against 2.13 over 26 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=no-mute: decode_failures 1
- AD-siting: siting-mix=basement-heavy: decode_failures 2
- DB-hotstore-stress: max-num-nodes=10: decode_failures 33
- DB-hotstore-stress: max-num-nodes=120: decode_failures 50
- DB-hotstore-stress: max-num-nodes=250: decode_failures 50
- DB-warm: warm-num-nodes=0: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 81
- DB-warm: warm-num-nodes=25: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 81
- DB-warm: warm-num-nodes=100: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 81
- DB-warm: warm-num-nodes=2000: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 81
- DG-burst: burst-loss=0.2: decode_failures 6
- DG-burst: burst-loss=0.3: decode_failures 37
- DG-loss: extra-loss=0.3: decode_failures 14
- DG-outage: burst-loss=0.1: decode_failures 30
- DG-outage: burst-loss=0.2: decode_failures 30
- DG-outage: burst-loss=0.3: decode_failures 27
- DM-mode: dm-mode=m4-early-flood: decode_failures 3
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 20
- LD-chatty: broadcast-interval-s=300: decode_failures 20
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 10.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 81
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 18.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 71
- MS-hopscale: nodes=250: decode_failures 3
- MS-hopscale: nodes=500: decode_failures 16
- MS-oversubscribed: nodes=250: decode_failures 50
- MS-oversubscribed: nodes=500: decode_failures 30
- MS-stretch: faster: 1.17 s per simulated hour against 2.38 over 26 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 1
- RF-eu-presets: preset=LITE_FAST: decode_failures 7
- RF-noise: noise-profile=temporal: decode_failures 31
- RF-noise: noise-profile=periodic: decode_failures 1
- RF-preset: preset=LONG_MODERATE: decode_failures 12
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 7
- RF-stretch-duct: faster: 0.992 s per simulated hour against 2.31 over 26 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=22: decode_failures 2
- RF-txpower: tx-power=14: decode_failures 3
- RT-hoplimit: hop-limit=15: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 29
- SF-bucket-mode: bucket-mode=time: misdecodes 33
- SF-bucket-mode: bucket-mode=window: misdecodes 10
- SF-bucket-time: time-bucket-s=600: misdecodes 116
- SF-bucket-time: time-bucket-s=1800: misdecodes 33
- SF-bucket-time: time-bucket-s=3600: misdecodes 4
- SF-cadence: trigger=interval: misdecodes 21
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 23
- SF-capacity-local: capacity=4: decode_failures 75
- SF-capacity-local: capacity=8: decode_failures 34
- SF-capacity-local: capacity=16: decode_failures 3
- SF-capacity: capacity=4: decode_failures 75
- SF-capacity: capacity=8: decode_failures 34
- SF-capacity: capacity=16: decode_failures 3
- SF-capacity-window: capacity=8: misdecodes 20
- SF-capacity-window: capacity=8: decode_failures 37
- SF-capacity-window: capacity=16: misdecodes 26
- SF-capacity-window: capacity=32: misdecodes 10
- SF-catchup: catch-up-hours=: misdecodes 23
- SF-catchup: catch-up-hours=02-06: decode_failures 40
- SF-catchup: catch-up-hours=00-08: decode_failures 38
- SF-hops-flat: hops-apart=4: decode_failures 2
- SF-hops-spread: hops-apart=4: decode_failures 2
- SF-hops-spread: hops-apart=5: decode_failures 2
- SF-place-flat: place=spread: decode_failures 16
- SF-place-spread: place=spread: decode_failures 16
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 8
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-servers-allrouters: servers=6: misdecodes 2
- SF-servers-flat: servers=5: decode_failures 1
- SF-servers-spread: servers=5: decode_failures 1
- SF-window-size: window-size=8: misdecodes 135
- SF-window-size: window-size=16: misdecodes 57
- SF-window-size: window-size=32: misdecodes 10
- TH-congestion-input: congestion-input=hotstore: decode_failures 50
- TH-congestion-input: congestion-input=truesize: decode_failures 2
- TH-congestion: no-congestion-scaling=True: queue drops 10.8% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 84

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-badrouters` | 4.65 | 2.13 | 2.18x | 26 |
| `FW-firmware` | 1.15 | 1.72 | 0.67x | 26 |
| `RF-pulse` | 1.09 | 1.67 | 0.65x | 26 |
| `MS-hopscale` | 11.6 | 18 | 0.65x | 26 |
| `SF-capacity-window` | 1.07 | 1.67 | 0.64x | 26 |
| `RT-spread` | 1.27 | 2.15 | 0.59x | 26 |
| `MS-topology` | 1.12 | 1.89 | 0.59x | 26 |
| `SF-hops-flat` | 2.02 | 3.45 | 0.58x | 26 |
| `RT-hoplimit` | 0.919 | 1.79 | 0.51x | 26 |
| `SF-hops-spread` | 2.3 | 4.57 | 0.50x | 26 |
| `MS-stretch` | 1.17 | 2.38 | 0.49x | 26 |
| `RF-stretch-duct` | 0.992 | 2.31 | 0.43x | 26 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.981 | 0.981 | 0.874 → 0.877 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.976 | 0.976 | 0.865 → 0.879 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.133 → 0.976 | 0.843 | 0.076 → 0.879 | 9.8x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.045 → 0.885 | 0.841 | 0.043 → 0.879 | 7.8x sr_airtime | up | 5 |
| `MS-stretch` | stretch | **held** | 0.167 → 0.976 | 0.809 | 0.122 → 0.879 | 9.2x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.123 → 0.912 | 0.789 | 0.117 → 0.808 | 92x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.047 → 0.804 | 0.757 | 0.046 → 0.798 | 5.4x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.228 → 0.976 | 0.748 | 0.225 → 0.975 | 4x sr_airtime | up | 4 |
| `RF-eu-presets` | preset | **held** | 0.241 → 0.976 | 0.735 | 0.352 → 0.879 | 8.2x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.241 → 0.976 | 0.735 | 0.352 → 0.879 | 12x sr_airtime | up | 3 |
| `RF-bw500` | preset | **held** | 0.206 → 0.896 | 0.690 | 0.158 → 0.780 | 5.4x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.300 → 0.885 | 0.585 | 0.296 → 0.879 | 8.6x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.303 → 0.813 | 0.510 | 0.299 → 0.804 | 4.4x bytes_on_air | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.544 → 0.885 | 0.342 | 0.517 → 0.879 | 2.2x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.612 → 0.942 | 0.330 | 0.599 → 0.940 | 7.5x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.585 → 0.912 | 0.328 | 0.559 → 0.909 | 7.3x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.635 → 0.959 | 0.324 | 0.620 → 0.958 | 2x sr_airtime | up | 4 |
| `DG-burst` | burst-loss | **text** | 0.574 → 0.885 | 0.311 | 0.537 → 0.879 | 2.2x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.307 → 0.594 | 0.287 | 0.313 → 0.504 | 8.2x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.457 → 0.714 | 0.257 | 0.450 → 0.704 | 1.8x sr_airtime | up | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.713 → 0.941 | 0.228 | 0.688 → 0.939 | 2.2x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.748 → 0.967 | 0.219 | 0.723 → 0.963 | 4.5x sr_airtime | up | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.713 → 0.920 | 0.207 | 0.688 → 0.918 | 1.9x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.762 → 0.967 | 0.205 | 0.750 → 0.963 | 4.4x sr_airtime | down | 2 |
| `RT-spread` | hop-spread | **text** | 0.713 → 0.885 | 0.172 | 0.688 → 0.879 | 1.5x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **text** | 0.716 → 0.885 | 0.169 | 0.709 → 0.879 | 1.7x sr_bytes | down | 4 |
| `MS-size` | nodes | **text** | 0.724 → 0.885 | 0.161 | 0.714 → 0.879 | 5.5x sr_bytes | down | 5 |
| `DG-loss` | extra-loss | **text** | 0.753 → 0.885 | 0.133 | 0.736 → 0.879 | 1.4x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.753 → 0.885 | 0.132 | 0.753 → 0.879 | 1.2x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.804 → 0.932 | 0.128 | 0.798 → 0.929 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.804 → 0.932 | 0.128 | 0.798 → 0.929 | 2.4x bytes_on_air | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.823 → 0.914 | 0.090 | 0.807 → 0.907 | 2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.827 → 0.914 | 0.087 | 0.809 → 0.907 | 2x sr_airtime | down | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.818 → 0.896 | 0.078 | 0.811 → 0.888 | 1.2x sr_bytes | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.682 → 0.759 | 0.077 | 0.671 → 0.747 | 1.4x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.885 → 0.957 | 0.071 | 0.879 → 0.955 | 1.9x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.849 → 0.920 | 0.071 | 0.839 → 0.917 | 5.1x sr_airtime | up | 4 |
| `MS-roles` | role-mix | **text** | 0.804 → 0.875 | 0.071 | 0.798 → 0.866 | 1.2x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.570 → 0.636 | 0.066 | 0.497 → 0.533 | 1.4x sr_airtime | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.912 → 0.976 | 0.064 | 0.877 → 0.879 | 28x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.914 → 0.976 | 0.062 | 0.870 → 0.883 | 4.4x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.914 → 0.976 | 0.062 | 0.870 → 0.883 | 4.4x sr_bytes | up | 6 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.885 → 0.947 | 0.061 | 0.879 → 0.943 | 1.2x bytes_on_air | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.833 → 0.885 | 0.052 | 0.824 → 0.879 | 1.5x sr_airtime | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.885 → 0.937 | 0.052 | 0.879 → 0.932 | 1.5x bytes_on_air | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.885 → 0.926 | 0.040 | 0.879 → 0.921 | 2x bytes_on_air | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.846 → 0.885 | 0.040 | 0.837 → 0.879 | 1.3x sr_airtime | down | 2 |
| `SF-cadence` | trigger | **held** | 0.938 → 0.976 | 0.039 | 0.838 → 0.885 | 14x advert_bytes | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.885 → 0.924 | 0.038 | 0.879 → 0.921 | 3.3x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.885 → 0.922 | 0.037 | 0.879 → 0.918 | 2.1x bytes_on_air | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.848 → 0.881 | 0.033 | 0.838 → 0.879 | 9.3x advert_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.885 → 0.917 | 0.032 | 0.879 → 0.908 | 3.4x bytes_on_air | down | 5 |
| `RT-favourites` | favourite-routers | **text** | 0.881 → 0.909 | 0.029 | 0.874 → 0.905 | 1.1x sr_bytes | up | 2 |
| `DM-mode` | dm-mode | **text** | 0.836 → 0.862 | 0.025 | 0.836 → 0.862 | 1.2x sr_airtime | up | 3 |
| `SF-hops-flat` | hops-apart | **text** | 0.878 → 0.903 | 0.025 | 0.874 → 0.879 | 3.1x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.878 → 0.903 | 0.025 | 0.874 → 0.879 | 3.1x sr_bytes | up | 5 |
| `SF-servers-flat` | servers | **held** | 0.965 → 0.989 | 0.024 | 0.877 → 0.880 | 6.3x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.965 → 0.989 | 0.024 | 0.877 → 0.880 | 6.3x sr_bytes | up | 4 |
| `LD-diurnal` | diurnal | **text** | 0.885 → 0.908 | 0.022 | 0.879 → 0.904 | 1.2x sr_bytes | down | 3 |
| `FW-firmware` | profile | **text** | 0.885 → 0.906 | 0.020 | 0.879 → 0.894 | 3.3x bytes_on_air | down | 2 |
| `AD-badrouters` | role-placement | **held** | 0.906 → 0.926 | 0.020 | 0.776 → 0.798 | 1.5x sr_bytes | down | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.947 → 0.963 | 0.016 | 0.842 → 0.846 | 1x sr_bytes | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.881 → 0.896 | 0.015 | 0.875 → 0.887 | 1.3x bytes_on_air | up | 4 |
| `AD-worst` | role-placement | **text** | 0.840 → 0.854 | 0.014 | 0.836 → 0.853 | 1.2x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.961 → 0.974 | 0.013 | 0.875 → 0.881 | 2x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.963 → 0.976 | 0.013 | 0.874 → 0.879 | 1x advert_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.959 → 0.972 | 0.013 | 0.877 → 0.877 | 3.2x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.873 → 0.885 | 0.012 | 0.867 → 0.879 | 5.5x advert_bytes | up | 3 |
| `SF-provide-transport` | provide-transport | **held** | 0.964 → 0.976 | 0.012 | 0.866 → 0.879 | 2.4x sr_airtime | down | 2 |
| `SF-capacity` | capacity | **held** | 0.965 → 0.976 | 0.012 | 0.874 → 0.882 | 5.2x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.965 → 0.976 | 0.012 | 0.874 → 0.882 | 5.2x advert_bytes | down | 5 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.965 → 0.976 | 0.011 | 0.872 → 0.879 | 3.5x advert_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **text** | 0.871 → 0.882 | 0.011 | 0.862 → 0.878 | 1.3x sr_bytes | up | 4 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.947 → 0.957 | 0.010 | 0.842 → 0.852 | 1.2x sr_bytes | down | 2 |
| `SF-width` | short-id-bits | **text** | 0.878 → 0.888 | 0.010 | 0.871 → 0.883 | 3.2x advert_bytes | down | 4 |
| `SF-window-size` | window-size | **held** | 0.961 → 0.971 | 0.010 | 0.867 → 0.875 | 6.5x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.881 → 0.889 | 0.008 | 0.875 → 0.885 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.881 → 0.889 | 0.008 | 0.875 → 0.885 | 1.1x sr_airtime | down | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.893 → 0.900 | 0.007 | 0.866 → 0.875 | 1.1x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **held** | 0.969 → 0.976 | 0.007 | 0.879 → 0.879 | 5.8x advert_bytes | = | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.971 → 0.976 | 0.005 | 0.876 → 0.879 | 1x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.963 → 0.967 | 0.004 | 0.958 → 0.963 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.976 → 0.980 | 0.004 | 0.879 → 0.882 | 2.7x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.967 → 0.970 | 0.003 | 0.963 → 0.967 | 1.1x bytes_on_air | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.967 → 0.968 | 0.001 | 0.963 → 0.965 | 1x sr_bytes | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario rolling`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| sprinkled | 1 | 0.892 | 0.887 | 0.006 | - | - | 0.981 | 0.983 | 0.696 | 1.33x | 16.5/24.6/28.0% | 2.0/5.2% | 3 |
| arms-race | 1 | 0.947 | 0.943 | 0.004 | - | - | 0.995 | 0.997 | 0.801 | 1.10x | 18.9/24.4/27.2% | 1.4/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.913 | 0.905 | 0.008 | - | - | 0.959 | 0.961 | 0.796 | 1.12x | 18.3/21.9/28.2% | 1.6/4.8% | 3 |
| 0.3 | 1 | 0.957 | 0.955 | 0.002 | - | - | 0.996 | 0.997 | 0.896 | 0.99x | 21.2/26.2/29.2% | 1.3/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.926 | 0.929 | 0.239 | 1.16x | 14.4/22.0/27.2% | 1.9/5.4% | 3 |
| inverse | 1 | 0.794 | 0.776 | 0.019 | - | - | 0.906 | 0.922 | 0.542 | 1.14x | 13.4/17.9/20.0% | 2.0/3.5% | 3 |
| random | 1 | 0.792 | 0.779 | 0.013 | - | - | 0.915 | 0.916 | 0.517 | 1.09x | 13.6/18.9/22.3% | 1.9/3.9% | 3 |

> role-placement=inverse: decode_failures 37

> slower: 4.65 s per simulated hour against 2.13 over 26 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.926 | 0.929 | 0.239 | 1.16x | 14.4/22.0/27.2% | 1.9/5.4% | 3 |
| all-routers | 1 | 0.932 | 0.929 | 0.003 | - | - | 0.985 | 0.986 | 0.823 | 2.79x | 31.4/40.9/43.9% | 4.5/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.926 | 0.929 | 0.239 | 1.16x | 14.4/22.0/27.2% | 1.9/5.4% | 3 |
| no-mute | 1 | 0.864 | 0.852 | 0.011 | - | - | 0.963 | 0.964 | 0.645 | 1.29x | 15.7/21.8/25.2% | 2.1/5.3% | 3 |
| all-routers | 1 | 0.932 | 0.929 | 0.003 | - | - | 0.985 | 0.986 | 0.823 | 2.79x | 31.4/40.9/43.9% | 4.5/5.3% | 3 |

> role-mix=no-mute: decode_failures 1

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.926 | 0.929 | 0.239 | 1.16x | 14.4/22.0/27.2% | 1.9/5.4% | 3 |
| local-typical | 1 | 0.672 | 0.659 | 0.013 | - | - | 0.842 | 0.842 | 0.154 | 1.19x | 12.5/19.6/25.5% | 2.1/4.9% | 3 |
| basement-heavy | 1 | 0.047 | 0.046 | 0.001 | - | - | 0.179 | 0.194 | 0.000 | 0.41x | 0.2/4.5/9.3% | 0.2/2.3% | 3 |

> siting-mix=basement-heavy: decode_failures 2

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.854 | 0.853 | 0.002 | - | - | 0.969 | 0.970 | 0.000 | 2.21x | 19.3/30.6/39.0% | 1.6/5.4% | 3 |
| inverse | 1 | 0.840 | 0.836 | 0.005 | - | - | 0.973 | 0.973 | 0.000 | 2.10x | 16.9/25.5/31.4% | 1.6/3.3% | 3 |

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.877 | 0.877 | 0.000 | - | - | 0 | 0.000 | 0.587 | 1.35x | 16.7/23.4/27.3% | 2.0/5.1% | 3 |
| sr | 1 | 0.886 | 0.874 | 0.011 | - | - | 0.981 | 0.984 | 0.592 | 1.40x | 17.2/24.3/28.6% | 2.2/5.5% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.823 | 0.807 | 0.017 | - | - | 0.920 | 0.922 | 0.603 | 3.02x | 34.4/54.6/60.9% | 4.3/9.7% | 3 |
| 100 | 1 | 0.914 | 0.907 | 0.007 | - | - | 0.966 | 0.969 | 0.740 | 1.57x | 17.9/30.6/34.4% | 2.2/5.2% | 3 |
| 120 | 1 | 0.914 | 0.907 | 0.007 | - | - | 0.966 | 0.969 | 0.740 | 1.57x | 17.9/30.6/34.4% | 2.2/5.2% | 3 |
| 250 | 1 | 0.914 | 0.907 | 0.007 | - | - | 0.966 | 0.969 | 0.740 | 1.57x | 17.9/30.6/34.4% | 2.2/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.316 | 0.313 | 0.003 | - | - | 0.307 | 0.349 | 0.171 | 11.35x | 37.8/53.2/75.7% | 4.0/10.2% | 3 |
| 120 | 1 | 0.505 | 0.497 | 0.008 | - | - | 0.570 | 0.587 | 0.259 | 4.49x | 14.8/24.8/41.9% | 1.5/5.0% | 3 |
| 250 | 1 | 0.513 | 0.504 | 0.009 | - | - | 0.594 | 0.612 | 0.259 | 4.36x | 14.6/24.2/40.4% | 1.5/4.9% | 3 |

> max-num-nodes=10: decode_failures 33

> max-num-nodes=120: decode_failures 50

> max-num-nodes=250: decode_failures 50

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.914 | 0.907 | 0.007 | - | - | 0.966 | 0.969 | 0.740 | 1.57x | 17.9/30.6/34.4% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.914 | 0.907 | 0.007 | - | - | 0.966 | 0.969 | 0.740 | 1.57x | 17.9/30.6/34.4% | 2.2/5.2% | 3 |
| constrained | 1 | 0.827 | 0.809 | 0.018 | - | - | 0.925 | 0.928 | 0.617 | 3.02x | 34.5/54.6/60.9% | 4.4/9.7% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.759 | 0.747 | 0.011 | - | - | 0.835 | 0.888 | 0.630 | 5.50x | 57.3/73.0/78.4% | 3.8/12.7% | 3 |
| 25 | 1 | 0.759 | 0.747 | 0.011 | - | - | 0.835 | 0.888 | 0.630 | 5.50x | 57.3/73.0/78.4% | 3.8/12.7% | 3 |
| 100 | 1 | 0.759 | 0.747 | 0.011 | - | - | 0.835 | 0.888 | 0.630 | 5.50x | 57.3/73.0/78.4% | 3.8/12.7% | 3 |
| 2000 | 1 | 0.759 | 0.747 | 0.011 | - | - | 0.835 | 0.888 | 0.630 | 5.50x | 57.3/73.0/78.4% | 3.8/12.7% | 3 |

> warm-num-nodes=0: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 81

> warm-num-nodes=25: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 81

> warm-num-nodes=100: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 81

> warm-num-nodes=2000: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 81

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.790 | 0.774 | 0.016 | - | - | 0.954 | 0.957 | 0.520 | 1.29x | 16.0/22.9/27.3% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.694 | 0.663 | 0.031 | - | - | 0.904 | 0.930 | 0.436 | 1.19x | 15.0/21.4/25.7% | 1.8/4.6% | 3 |
| 0.3 | 1 | 0.574 | 0.537 | 0.037 | - | - | 0.782 | 0.856 | 0.342 | 1.09x | 14.0/19.7/24.0% | 1.6/3.9% | 3 |

> burst-loss=0.2: decode_failures 6

> burst-loss=0.3: decode_failures 37

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.849 | 0.842 | 0.007 | - | - | 0.949 | 0.952 | 0.565 | 1.43x | 17.6/24.8/29.4% | 2.1/5.4% | 3 |
| 0.2 | 1 | 0.810 | 0.799 | 0.011 | - | - | 0.946 | 0.953 | 0.520 | 1.47x | 18.2/25.4/30.2% | 2.2/5.2% | 3 |
| 0.3 | 1 | 0.753 | 0.736 | 0.016 | - | - | 0.905 | 0.929 | 0.426 | 1.47x | 18.7/26.4/30.9% | 2.2/5.1% | 3 |

> extra-loss=0.3: decode_failures 14

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.786 | 0.775 | 0.012 | - | - | 0.910 | 0.939 | 0.520 | 1.28x | 16.1/22.6/27.2% | 2.0/5.1% | 3 |
| 0.2 | 1 | 0.657 | 0.637 | 0.020 | - | - | 0.846 | 0.924 | 0.438 | 1.19x | 14.7/21.3/25.5% | 1.8/4.7% | 3 |
| 0.3 | 1 | 0.544 | 0.517 | 0.027 | - | - | 0.745 | 0.868 | 0.267 | 1.13x | 14.6/20.2/24.8% | 1.7/4.1% | 3 |

> burst-loss=0.1: decode_failures 30

> burst-loss=0.2: decode_failures 30

> burst-loss=0.3: decode_failures 27

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.956 | 0.961 | 0.536 | 1.88x | 23.2/33.0/38.5% | 2.9/7.2% | 3 |
| directed-with-late-flood | 1 | 0.852 | 0.852 | 0.000 | - | - | 0.957 | 0.960 | 0.587 | 1.68x | 20.8/29.3/34.5% | 2.6/6.5% | 3 |
| m4-early-flood | 1 | 0.862 | 0.862 | 0.000 | - | - | 0.960 | 0.969 | 0.599 | 1.69x | 21.1/29.8/35.0% | 2.6/6.6% | 3 |

> dm-mode=m4-early-flood: decode_failures 3

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.906 | 0.894 | 0.011 | - | - | 0.978 | 0.979 | 0.795 | 0.74x | 9.4/11.8/13.5% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.910 | 0.899 | 0.012 | - | - | 0.989 | 0.991 | 0.780 | 1.21x | 14.9/20.5/24.9% | 1.8/4.6% | 3 |
| 0.5 | 1 | 0.926 | 0.921 | 0.005 | - | - | 0.995 | 0.996 | 0.744 | 1.05x | 14.2/18.5/20.7% | 1.5/4.0% | 3 |
| 0.75 | 1 | 0.901 | 0.891 | 0.010 | - | - | 0.981 | 0.982 | 0.625 | 0.95x | 11.3/16.3/18.5% | 1.5/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.913 | 0.904 | 0.009 | - | - | 0.989 | 0.990 | 0.788 | 1.21x | 15.1/20.6/24.9% | 1.9/4.6% | 3 |
| 0.5 | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.994 | 0.995 | 0.725 | 1.02x | 13.9/18.2/20.1% | 1.5/4.0% | 3 |
| 0.75 | 1 | 0.899 | 0.888 | 0.011 | - | - | 0.984 | 0.984 | 0.590 | 0.91x | 11.2/16.2/18.5% | 1.4/3.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.924 | 0.921 | 0.003 | - | - | 0.988 | 0.989 | 0.627 | 0.74x | 9.3/13.6/16.3% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.902 | 0.890 | 0.012 | - | - | 0.978 | 0.979 | 0.740 | 0.74x | 9.6/12.6/15.1% | 1.1/2.5% | 3 |
| 2.5 | 1 | 0.908 | 0.897 | 0.011 | - | - | 0.980 | 0.983 | 0.753 | 0.73x | 9.3/12.3/14.6% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.913 | 0.902 | 0.011 | - | - | 0.992 | 0.993 | 0.766 | 0.72x | 9.4/12.3/14.9% | 1.1/2.5% | 3 |
| 2.7 | 1 | 0.917 | 0.908 | 0.009 | - | - | 0.986 | 0.986 | 0.667 | 0.76x | 9.7/14.9/18.1% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.912 | 0.909 | 0.003 | - | - | 0.986 | 0.986 | 0.635 | 0.95x | 11.5/16.5/19.1% | 1.4/3.7% | 3 |
| 900 | 1 | 0.849 | 0.839 | 0.009 | - | - | 0.958 | 0.960 | 0.549 | 2.19x | 26.7/37.8/44.4% | 3.3/8.5% | 3 |
| 300 | 1 | 0.585 | 0.559 | 0.026 | - | - | 0.773 | 0.819 | 0.331 | 4.48x | 51.8/68.7/76.9% | 6.7/16.6% | 3 |

> broadcast-interval-s=300: decode_failures 20

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.942 | 0.940 | 0.002 | - | - | 0.991 | 0.992 | 0.596 | 1.04x | 12.3/17.3/19.7% | 1.6/3.7% | 3 |
| 900 | 1 | 0.893 | 0.889 | 0.004 | - | - | 0.969 | 0.969 | 0.593 | 2.43x | 29.0/39.5/45.5% | 3.7/8.6% | 3 |
| 300 | 1 | 0.612 | 0.599 | 0.013 | - | - | 0.778 | 0.806 | 0.378 | 5.01x | 56.8/71.7/77.9% | 7.7/17.0% | 3 |

> broadcast-interval-s=300: decode_failures 20

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.986 | 0.987 | 0.618 | 1.30x | 16.1/22.9/26.8% | 2.0/5.1% | 3 |
| sinusoid | 1 | 0.888 | 0.882 | 0.005 | - | - | 0.976 | 0.976 | 0.602 | 1.26x | 15.5/22.1/25.7% | 1.9/4.9% | 3 |
| commuter | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.849 | 0.839 | 0.009 | - | - | 0.958 | 0.960 | 0.549 | 2.19x | 26.7/37.8/44.4% | 3.3/8.5% | 3 |
| 3600 | 1 | 0.912 | 0.909 | 0.003 | - | - | 0.986 | 0.986 | 0.635 | 0.95x | 11.5/16.5/19.1% | 1.4/3.7% | 3 |
| 10800 | 1 | 0.920 | 0.917 | 0.003 | - | - | 0.985 | 0.986 | 0.613 | 0.67x | 8.0/11.7/13.4% | 1.0/2.6% | 3 |
| 43200 | 1 | 0.920 | 0.917 | 0.002 | - | - | 0.984 | 0.986 | 0.626 | 0.45x | 5.4/7.9/9.1% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.868 | 0.859 | 0.008 | - | - | 0.967 | 0.971 | 0.578 | 1.49x | 18.3/26.0/30.4% | 2.2/5.8% | 3 |
| 1.0 | 1 | 0.865 | 0.859 | 0.007 | - | - | 0.968 | 0.971 | 0.562 | 1.64x | 20.3/28.6/33.9% | 2.5/6.4% | 3 |
| 4.0 | 1 | 0.833 | 0.824 | 0.009 | - | - | 0.946 | 0.947 | 0.567 | 2.05x | 25.3/35.5/43.2% | 3.0/8.2% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.759 | 0.747 | 0.011 | - | - | 0.835 | 0.888 | 0.630 | 5.50x | 57.3/73.0/78.4% | 3.8/12.7% | 3 |
| 1.0 | 1 | 0.682 | 0.671 | 0.011 | - | - | 0.760 | 0.833 | 0.560 | 6.03x | 61.3/75.6/80.1% | 4.2/13.9% | 3 |

> traceroute-per-hour=0.0: queue drops 10.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 81

> traceroute-per-hour=1.0: queue drops 18.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 71

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.748 | 0.723 | 0.025 | - | - | 0.872 | 0.879 | 0.342 | 1.29x | 17.4/25.3/27.9% | 3.0/6.3% | 3 |
| 60 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 90 | 1 | 0.946 | 0.944 | 0.002 | - | - | 0.996 | 0.996 | 0.753 | 1.66x | 20.3/30.3/34.4% | 1.5/5.2% | 3 |
| 120 | 1 | 0.967 | 0.963 | 0.003 | - | - | 0.998 | 0.998 | 0.880 | 1.94x | 21.3/32.3/39.0% | 1.3/5.1% | 3 |
| 150 | 1 | 0.964 | 0.962 | 0.002 | - | - | 0.998 | 0.998 | 0.867 | 2.65x | 29.2/46.4/52.3% | 1.3/5.8% | 3 |

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 120 | 1 | 0.808 | 0.798 | 0.010 | - | - | 0.963 | 0.963 | 0.463 | 2.28x | 17.0/26.3/33.9% | 1.6/5.1% | 3 |
| 250 | 1 | 0.514 | 0.505 | 0.008 | - | - | 0.597 | 0.600 | 0.265 | 4.61x | 15.4/25.5/43.1% | 1.6/5.3% | 3 |
| 500 | 1 | 0.300 | 0.296 | 0.004 | - | - | 0.481 | 0.481 | 0.105 | 9.81x | 17.9/28.9/48.5% | 1.6/5.9% | 3 |

> nodes=250: decode_failures 3

> nodes=500: decode_failures 16

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.813 | 0.804 | 0.009 | - | - | 0.959 | 0.961 | 0.471 | 2.09x | 15.7/24.1/30.8% | 1.5/4.7% | 3 |
| 250 | 1 | 0.505 | 0.497 | 0.008 | - | - | 0.570 | 0.587 | 0.259 | 4.49x | 14.8/24.8/41.9% | 1.5/5.0% | 3 |
| 500 | 1 | 0.303 | 0.299 | 0.004 | - | - | 0.473 | 0.475 | 0.094 | 9.05x | 16.6/26.7/44.9% | 1.5/5.5% | 3 |

> nodes=250: decode_failures 50

> nodes=500: decode_failures 30

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.875 | 0.866 | 0.009 | - | - | 0.969 | 0.969 | 0.568 | 1.36x | 16.7/24.0/28.5% | 2.1/5.6% | 3 |
| baymesh-2026-08 | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.926 | 0.929 | 0.239 | 1.16x | 14.4/22.0/27.2% | 1.9/5.4% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.969 | 0.969 | 0.598 | 1.46x | 17.7/25.1/28.7% | 2.2/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.818 | 0.811 | 0.007 | - | - | 0.902 | 0.905 | 0.242 | 1.30x | 16.0/25.5/30.3% | 2.2/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.05 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.966 | 0.968 | 0.603 | 1.46x | 17.4/26.3/30.7% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.889 | 0.883 | 0.006 | - | - | 0.964 | 0.966 | 0.675 | 1.56x | 17.9/31.2/35.0% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.896 | 0.887 | 0.009 | - | - | 0.973 | 0.973 | 0.666 | 1.80x | 20.5/38.6/43.3% | 2.4/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| local-typical | 1 | 0.756 | 0.745 | 0.011 | - | - | 0.950 | 0.951 | 0.132 | 1.35x | 13.1/20.8/26.4% | 2.0/5.1% | 3 |
| event | 1 | 0.228 | 0.225 | 0.003 | - | - | 0.409 | 0.412 | 0.000 | 1.16x | 6.0/13.5/20.1% | 1.6/4.5% | 3 |
| backbone | 1 | 0.976 | 0.975 | 0.000 | - | - | 0.998 | 0.998 | 0.784 | 1.17x | 27.2/37.4/38.9% | 1.5/5.5% | 3 |

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.875 | 0.868 | 0.008 | - | - | 0.976 | 0.978 | 0.633 | 1.47x | 26.2/35.6/39.4% | 3.5/7.6% | 3 |
| 60 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 90 | 1 | 0.841 | 0.826 | 0.015 | - | - | 0.969 | 0.972 | 0.590 | 1.71x | 17.2/23.4/29.0% | 1.7/4.5% | 3 |
| 120 | 1 | 0.808 | 0.798 | 0.010 | - | - | 0.963 | 0.963 | 0.463 | 2.28x | 17.0/26.3/33.9% | 1.6/5.1% | 3 |
| 150 | 1 | 0.724 | 0.714 | 0.010 | - | - | 0.852 | 0.853 | 0.367 | 2.71x | 16.4/25.3/29.8% | 1.5/5.5% | 3 |

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 1.25 | 1 | 0.638 | 0.626 | 0.012 | - | - | 0.796 | 0.799 | 0.241 | 1.25x | 11.0/17.5/22.6% | 1.8/4.8% | 3 |
| 1.5 | 1 | 0.457 | 0.450 | 0.007 | - | - | 0.673 | 0.676 | 0.072 | 1.30x | 8.8/15.3/18.9% | 1.9/5.2% | 3 |
| 2.0 | 1 | 0.124 | 0.122 | 0.002 | - | - | 0.167 | 0.171 | 0.000 | 0.90x | 4.5/6.9/9.3% | 1.5/2.6% | 3 |

> faster: 1.17 s per simulated hour against 2.38 over 26 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| clustered | 1 | 0.905 | 0.898 | 0.007 | - | - | 0.992 | 0.993 | 0.000 | 1.22x | 26.4/38.1/39.0% | 1.7/5.8% | 3 |
| corridor | 1 | 0.635 | 0.620 | 0.015 | - | - | 0.700 | 0.702 | 0.276 | 1.46x | 16.3/21.4/23.4% | 2.4/5.2% | 3 |
| hub | 1 | 0.959 | 0.958 | 0.001 | - | - | 0.980 | 0.980 | 0.848 | 1.20x | 28.8/37.6/39.0% | 1.6/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.852 | 0.852 | 0.000 | - | - | 0.957 | 0.960 | 0.587 | 1.68x | 20.8/29.3/34.5% | 2.6/6.5% | 3 |
| True | 1 | 0.842 | 0.842 | 0.000 | - | - | 0.947 | 0.957 | 0.579 | 1.70x | 21.0/30.1/35.4% | 2.5/6.6% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.842 | 0.842 | 0.000 | - | - | 0.947 | 0.957 | 0.579 | 1.70x | 21.0/30.1/35.4% | 2.5/6.6% | 3 |
| m4-early-flood | 1 | 0.846 | 0.846 | 0.000 | - | - | 0.963 | 0.968 | 0.589 | 1.70x | 21.0/30.1/35.3% | 2.6/6.6% | 3 |

> dm-mode=m4-early-flood: decode_failures 1

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.877 | 0.877 | 0.000 | - | - | 0 | 0.000 | 0.587 | 1.35x | 16.7/23.4/27.3% | 2.0/5.1% | 3 |
| chain | 1 | 0.866 | 0.865 | 0.002 | - | - | 0.901 | 0.972 | 0.574 | 1.57x | 19.5/27.5/32.3% | 2.4/6.1% | 3 |
| sr | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| True | 1 | 0.878 | 0.874 | 0.005 | - | - | 0.963 | 0.966 | 0.594 | 1.39x | 17.2/24.4/28.5% | 2.1/5.5% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.967 | 0.963 | 0.003 | - | - | 0.998 | 0.998 | 0.880 | 1.94x | 21.3/32.3/39.0% | 1.3/5.1% | 3 |
| True | 1 | 0.968 | 0.965 | 0.003 | - | - | 0.999 | 0.999 | 0.895 | 1.96x | 21.4/32.4/39.1% | 1.3/5.1% | 3 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.159 | 0.158 | 0.001 | - | - | 0.206 | 0.209 | 0.000 | 0.05x | 0.2/0.4/0.6% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.488 | 0.484 | 0.004 | - | - | 0.653 | 0.655 | 0.093 | 0.27x | 1.9/3.3/4.6% | 0.4/1.2% | 3 |
| LONG_TURBO | 1 | 0.789 | 0.780 | 0.010 | - | - | 0.896 | 0.898 | 0.468 | 1.23x | 11.8/18.7/22.8% | 1.8/4.9% | 3 |

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.895 | 0.889 | 0.007 | - | - | 0.972 | 0.972 | 0.630 | 1.12x | 15.8/22.2/26.6% | 1.6/5.0% | 3 |
| 1.0 | 1 | 0.937 | 0.932 | 0.006 | - | - | 0.985 | 0.985 | 0.772 | 0.89x | 20.5/26.5/29.8% | 1.1/5.0% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.354 | 0.352 | 0.002 | - | - | 0.241 | 0.241 | 0.022 | 0.15x | 0.9/1.9/2.6% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| LITE_FAST | 1 | 0.817 | 0.804 | 0.012 | - | - | 0.896 | 0.910 | 0.535 | 0.97x | 10.6/15.7/18.6% | 1.4/3.9% | 3 |
| NARROW_SLOW | 1 | 0.854 | 0.844 | 0.010 | - | - | 0.957 | 0.961 | 0.575 | 1.26x | 14.0/19.7/24.1% | 1.9/5.2% | 3 |

> preset=LITE_FAST: decode_failures 7

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| temporal | 1 | 0.780 | 0.770 | 0.010 | - | - | 0.916 | 0.935 | 0.435 | 1.31x | 15.2/22.8/27.2% | 2.0/5.3% | 3 |
| transient | 1 | 0.871 | 0.863 | 0.008 | - | - | 0.963 | 0.966 | 0.555 | 1.39x | 17.1/24.3/28.2% | 2.1/5.4% | 3 |
| periodic | 1 | 0.716 | 0.709 | 0.007 | - | - | 0.808 | 0.822 | 0.496 | 1.28x | 15.9/22.1/26.4% | 1.9/4.7% | 3 |

> noise-profile=temporal: decode_failures 31

> noise-profile=periodic: decode_failures 1

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.354 | 0.352 | 0.002 | - | - | 0.241 | 0.241 | 0.022 | 0.15x | 0.9/1.9/2.6% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| LONG_MODERATE | 1 | 0.855 | 0.837 | 0.018 | - | - | 0.971 | 0.978 | 0.725 | 3.45x | 48.3/62.3/65.3% | 5.2/12.0% | 3 |

> preset=LONG_MODERATE: decode_failures 12

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.045 | 0.043 | 0.001 | - | - | 0.178 | 0.179 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.159 | 0.158 | 0.001 | - | - | 0.206 | 0.209 | 0.000 | 0.05x | 0.2/0.4/0.6% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| LONG_TURBO | 1 | 0.789 | 0.780 | 0.010 | - | - | 0.896 | 0.898 | 0.468 | 1.23x | 11.8/18.7/22.8% | 1.8/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.852 | 0.844 | 0.008 | - | - | 0.930 | 0.932 | 0.630 | 1.87x | 20.6/29.4/34.8% | 2.8/6.8% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.815 | 0.808 | 0.008 | - | - | 0.912 | 0.914 | 0.545 | 1.36x | 16.8/23.8/28.0% | 2.1/5.2% | 3 |
| 10000 | 1 | 0.716 | 0.709 | 0.007 | - | - | 0.808 | 0.822 | 0.496 | 1.28x | 15.9/22.1/26.4% | 1.9/4.7% | 3 |
| 4000 | 1 | 0.452 | 0.447 | 0.005 | - | - | 0.501 | 0.575 | 0.260 | 1.09x | 13.7/19.1/22.6% | 1.7/3.5% | 3 |
| 2000 | 1 | 0.117 | 0.117 | 0.000 | - | - | 0.123 | 0.231 | 0.057 | 0.73x | 9.4/14.1/16.1% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 1

> noise-pulse-interval-ms=4000: decode_failures 7

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.457 | 0.450 | 0.007 | - | - | 0.673 | 0.676 | 0.072 | 1.30x | 8.8/15.3/18.9% | 1.9/5.2% | 3 |
| 1.0 | 1 | 0.714 | 0.704 | 0.010 | - | - | 0.845 | 0.845 | 0.439 | 0.88x | 13.0/17.6/20.1% | 1.3/4.3% | 3 |

> faster: 0.992 s per simulated hour against 2.31 over 26 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 22 | 1 | 0.452 | 0.441 | 0.011 | - | - | 0.614 | 0.616 | 0.108 | 1.31x | 8.8/15.0/18.9% | 1.9/4.7% | 3 |
| 17 | 1 | 0.156 | 0.155 | 0.001 | - | - | 0.181 | 0.184 | 0.000 | 1.04x | 5.1/9.0/12.2% | 1.7/3.6% | 3 |
| 14 | 1 | 0.077 | 0.076 | 0.001 | - | - | 0.133 | 0.152 | 0.000 | 0.59x | 2.6/4.3/6.0% | 1.0/2.2% | 3 |

> tx-power=22: decode_failures 2

> tx-power=14: decode_failures 3

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.967 | 0.963 | 0.003 | - | - | 0.998 | 0.998 | 0.880 | 1.94x | 21.3/32.3/39.0% | 1.3/5.1% | 3 |
| True | 1 | 0.963 | 0.958 | 0.005 | - | - | 0.997 | 0.997 | 0.876 | 2.34x | 25.7/37.8/44.4% | 1.5/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.968 | 0.971 | 0.596 | 1.40x | 16.7/25.0/30.4% | 2.0/5.4% | 3 |
| True | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.977 | 0.979 | 0.604 | 1.46x | 17.3/26.5/30.9% | 2.1/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| random | 1 | 0.846 | 0.837 | 0.009 | - | - | 0.977 | 0.979 | 0.587 | 1.33x | 16.4/23.4/27.6% | 2.0/5.4% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.713 | 0.688 | 0.025 | - | - | 0.957 | 0.961 | 0.276 | 1.02x | 12.9/19.9/24.8% | 1.5/5.0% | 3 |
| 7 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.980 | 0.980 | 0.599 | 1.53x | 18.3/25.5/29.4% | 2.4/5.5% | 3 |
| 15 | 1 | 0.941 | 0.939 | 0.002 | - | - | 0.984 | 0.985 | 0.601 | 1.55x | 18.5/25.5/29.1% | 2.4/5.5% | 3 |
| 32 | 1 | 0.940 | 0.939 | 0.001 | - | - | 0.982 | 0.983 | 0.608 | 1.56x | 18.6/25.7/29.3% | 2.4/5.5% | 3 |

> hop-limit=15: misdecodes 1

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.713 | 0.688 | 0.025 | - | - | 0.957 | 0.961 | 0.276 | 1.02x | 12.9/19.9/24.8% | 1.5/5.0% | 3 |
| 5 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.981 | 0.981 | 0.573 | 1.40x | 17.1/24.1/28.3% | 2.1/5.5% | 3 |
| 7 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.980 | 0.980 | 0.599 | 1.53x | 18.3/25.5/29.4% | 2.4/5.5% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.877 | 0.877 | 0.000 | - | - | 0.912 | 0.977 | 0.591 | 1.36x | 16.7/23.6/27.7% | 2.1/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.713 | 0.688 | 0.025 | - | - | 0.957 | 0.961 | 0.276 | 1.02x | 12.9/19.9/24.8% | 1.5/5.0% | 3 |
| True | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| BALANCED | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| STRICT | 1 | 0.753 | 0.753 | 0.000 | - | - | 0.849 | 0.853 | 0.440 | 1.47x | 18.0/25.6/29.6% | 2.2/5.6% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| dm | 1 | 0.888 | 0.882 | 0.006 | - | - | 0.980 | 0.981 | 0.604 | 1.37x | 16.8/24.0/28.1% | 2.1/5.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.881 | 0.876 | 0.006 | - | - | 0.969 | 0.972 | 0.607 | 1.39x | 17.1/24.2/28.4% | 2.1/5.5% | 3 |
| local | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| time | 1 | 0.877 | 0.872 | 0.005 | - | - | 0.972 | 0.974 | 0.581 | 1.43x | 17.7/25.1/29.3% | 2.2/5.7% | 3 |
| window | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.965 | 0.971 | 0.569 | 1.37x | 16.9/24.0/28.1% | 2.1/5.3% | 3 |

> bucket-mode=global: misdecodes 29

> bucket-mode=time: misdecodes 33

> bucket-mode=window: misdecodes 10

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.873 | 0.867 | 0.006 | - | - | 0.966 | 0.969 | 0.575 | 1.51x | 18.7/27.0/31.4% | 2.3/6.2% | 3 |
| 1800 | 1 | 0.877 | 0.872 | 0.005 | - | - | 0.972 | 0.974 | 0.581 | 1.43x | 17.7/25.1/29.3% | 2.2/5.7% | 3 |
| 3600 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.978 | 0.604 | 1.39x | 17.0/24.4/28.4% | 2.1/5.4% | 3 |

> time-bucket-s=600: misdecodes 116

> time-bucket-s=1800: misdecodes 33

> time-bucket-s=3600: misdecodes 4

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| interval | 1 | 0.859 | 0.850 | 0.009 | - | - | 0.951 | 0.954 | 0.566 | 1.82x | 21.8/33.9/39.6% | 2.6/9.1% | 3 |
| aimd | 1 | 0.886 | 0.885 | 0.001 | - | - | 0.938 | 0.982 | 0.605 | 1.40x | 17.3/24.6/28.7% | 2.1/5.4% | 3 |
| bucket+interval | 1 | 0.848 | 0.838 | 0.011 | - | - | 0.955 | 0.957 | 0.582 | 1.89x | 22.4/35.3/41.3% | 2.8/9.4% | 3 |

> trigger=interval: misdecodes 21

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 23

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.887 | 0.882 | 0.006 | - | - | 0.975 | 0.977 | 0.595 | 1.37x | 16.9/24.2/28.5% | 2.1/5.5% | 3 |
| 8 | 1 | 0.879 | 0.875 | 0.005 | - | - | 0.965 | 0.971 | 0.587 | 1.39x | 17.1/24.3/28.6% | 2.1/5.5% | 3 |
| 16 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.967 | 0.970 | 0.596 | 1.37x | 16.9/24.0/28.1% | 2.1/5.4% | 3 |
| 32 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 50 | 1 | 0.880 | 0.874 | 0.006 | - | - | 0.973 | 0.973 | 0.573 | 1.38x | 17.1/24.2/28.3% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 75

> capacity=8: decode_failures 34

> capacity=16: decode_failures 3

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.887 | 0.882 | 0.006 | - | - | 0.975 | 0.977 | 0.595 | 1.37x | 16.9/24.2/28.5% | 2.1/5.5% | 3 |
| 8 | 1 | 0.879 | 0.875 | 0.005 | - | - | 0.965 | 0.971 | 0.587 | 1.39x | 17.1/24.3/28.6% | 2.1/5.5% | 3 |
| 16 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.967 | 0.970 | 0.596 | 1.37x | 16.9/24.0/28.1% | 2.1/5.4% | 3 |
| 32 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 50 | 1 | 0.880 | 0.874 | 0.006 | - | - | 0.973 | 0.973 | 0.573 | 1.38x | 17.1/24.2/28.3% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 75

> capacity=8: decode_failures 34

> capacity=16: decode_failures 3

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.886 | 0.880 | 0.006 | - | - | 0.961 | 0.982 | 0.593 | 1.39x | 17.0/24.0/28.2% | 2.1/5.3% | 3 |
| 16 | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.974 | 0.978 | 0.595 | 1.40x | 17.1/24.4/28.6% | 2.1/5.4% | 3 |
| 32 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.965 | 0.971 | 0.569 | 1.37x | 16.9/24.0/28.1% | 2.1/5.3% | 3 |

> capacity=8: misdecodes 20

> capacity=8: decode_failures 37

> capacity=16: misdecodes 26

> capacity=32: misdecodes 10

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.848 | 0.838 | 0.011 | - | - | 0.955 | 0.957 | 0.582 | 1.89x | 22.4/35.3/41.3% | 2.8/9.4% | 3 |
| 02-06 | 1 | 0.880 | 0.877 | 0.003 | - | - | 0.939 | 0.967 | 0.605 | 1.39x | 17.2/24.6/29.0% | 2.1/5.7% | 3 |
| 00-08 | 1 | 0.881 | 0.879 | 0.003 | - | - | 0.945 | 0.971 | 0.613 | 1.45x | 17.9/26.0/30.6% | 2.2/6.2% | 3 |

> catch-up-hours=: misdecodes 23

> catch-up-hours=02-06: decode_failures 40

> catch-up-hours=00-08: decode_failures 38

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.878 | 0.877 | 0.002 | - | - | 0.961 | 0.961 | 0.592 | 1.37x | 16.9/23.9/27.9% | 2.1/5.2% | 3 |
| 2 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 3 | 1 | 0.886 | 0.874 | 0.011 | - | - | 0.981 | 0.984 | 0.592 | 1.40x | 17.2/24.3/28.6% | 2.2/5.5% | 3 |
| 4 | 1 | 0.903 | 0.878 | 0.026 | - | - | 0.984 | 0.989 | 0.673 | 1.40x | 17.1/24.3/28.6% | 2.1/5.2% | 3 |

> hops-apart=4: decode_failures 2

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.878 | 0.877 | 0.002 | - | - | 0.961 | 0.961 | 0.592 | 1.37x | 16.9/23.9/27.9% | 2.1/5.2% | 3 |
| 2 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 3 | 1 | 0.886 | 0.874 | 0.011 | - | - | 0.981 | 0.984 | 0.592 | 1.40x | 17.2/24.3/28.6% | 2.2/5.5% | 3 |
| 4 | 1 | 0.903 | 0.878 | 0.026 | - | - | 0.984 | 0.989 | 0.673 | 1.40x | 17.1/24.3/28.6% | 2.1/5.2% | 3 |
| 5 | 1 | 0.903 | 0.878 | 0.026 | - | - | 0.984 | 0.989 | 0.673 | 1.40x | 17.1/24.3/28.6% | 2.1/5.2% | 3 |

> hops-apart=4: decode_failures 2

> hops-apart=5: decode_failures 2

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.889 | 0.885 | 0.004 | - | - | 0.977 | 0.978 | 0.595 | 1.41x | 17.2/24.6/28.7% | 2.1/5.5% | 3 |
| 30 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 120 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.976 | 0.977 | 0.589 | 1.37x | 16.9/24.0/28.2% | 2.1/5.4% | 3 |
| 600 | 1 | 0.883 | 0.876 | 0.006 | - | - | 0.976 | 0.977 | 0.616 | 1.41x | 17.3/24.5/28.8% | 2.1/5.5% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.889 | 0.885 | 0.004 | - | - | 0.977 | 0.978 | 0.595 | 1.41x | 17.2/24.6/28.7% | 2.1/5.5% | 3 |
| 30 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 120 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.976 | 0.977 | 0.589 | 1.37x | 16.9/24.0/28.2% | 2.1/5.4% | 3 |
| 600 | 1 | 0.883 | 0.876 | 0.006 | - | - | 0.976 | 0.977 | 0.616 | 1.41x | 17.3/24.5/28.8% | 2.1/5.5% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.897 | 0.875 | 0.022 | - | - | 0.914 | 0.972 | 0.590 | 1.42x | 17.2/24.6/28.7% | 2.2/5.4% | 3 |
| routers | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.959 | 0.959 | 0.567 | 1.37x | 17.0/23.9/27.9% | 2.1/5.2% | 3 |
| alternate-routers | 1 | 0.886 | 0.883 | 0.003 | - | - | 0.969 | 0.971 | 0.606 | 1.38x | 17.1/24.1/28.1% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.873 | 0.870 | 0.003 | - | - | 0.952 | 0.952 | 0.619 | 1.40x | 17.3/24.4/28.5% | 2.1/5.3% | 3 |
| random-clients | 1 | 0.885 | 0.876 | 0.009 | - | - | 0.972 | 0.973 | 0.582 | 1.39x | 17.2/24.1/28.2% | 2.1/5.2% | 3 |
| hops-apart | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

> place=spread: decode_failures 16

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.897 | 0.875 | 0.022 | - | - | 0.914 | 0.972 | 0.590 | 1.42x | 17.2/24.6/28.7% | 2.2/5.4% | 3 |
| routers | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.959 | 0.959 | 0.567 | 1.37x | 17.0/23.9/27.9% | 2.1/5.2% | 3 |
| alternate-routers | 1 | 0.886 | 0.883 | 0.003 | - | - | 0.969 | 0.971 | 0.606 | 1.38x | 17.1/24.1/28.1% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.873 | 0.870 | 0.003 | - | - | 0.952 | 0.952 | 0.619 | 1.40x | 17.3/24.4/28.5% | 2.1/5.3% | 3 |
| random-clients | 1 | 0.885 | 0.876 | 0.009 | - | - | 0.972 | 0.973 | 0.582 | 1.39x | 17.2/24.1/28.2% | 2.1/5.2% | 3 |
| hops-apart | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

> place=spread: decode_failures 16

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| broadcast | 1 | 0.893 | 0.866 | 0.027 | - | - | 0.964 | 0.967 | 0.642 | 1.46x | 18.0/25.6/29.9% | 2.2/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| heard | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.971 | 0.975 | 0.609 | 1.38x | 17.1/24.3/28.3% | 2.1/5.4% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.893 | 0.866 | 0.027 | - | - | 0.964 | 0.967 | 0.642 | 1.46x | 18.0/25.6/29.9% | 2.2/5.6% | 3 |
| heard | 1 | 0.900 | 0.875 | 0.026 | - | - | 0.966 | 0.971 | 0.652 | 1.45x | 17.9/25.4/29.5% | 2.2/5.6% | 3 |

> replay-ordering=heard: misdecodes 8

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| enum | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.969 | 0.974 | 0.594 | 1.40x | 17.2/24.7/29.0% | 2.1/5.7% | 3 |
| hybrid | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.959 | 0.959 | 0.567 | 1.37x | 17.0/23.9/27.9% | 2.1/5.2% | 3 |
| 6 | 1 | 0.880 | 0.877 | 0.004 | - | - | 0.972 | 0.972 | 0.568 | 1.43x | 17.6/25.1/29.3% | 2.2/5.5% | 6 |

> servers=6: misdecodes 2

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.883 | 0.880 | 0.003 | - | - | 0.965 | 0.965 | 0.614 | 1.38x | 17.0/24.2/28.2% | 2.1/5.3% | 2 |
| 3 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 5 | 1 | 0.892 | 0.879 | 0.013 | - | - | 0.986 | 0.990 | 0.622 | 1.41x | 17.4/24.9/29.2% | 2.1/5.6% | 5 |
| 8 | 1 | 0.891 | 0.877 | 0.014 | - | - | 0.989 | 0.991 | 0.587 | 1.46x | 18.0/25.8/30.2% | 2.2/5.7% | 8 |

> servers=5: decode_failures 1

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.883 | 0.880 | 0.003 | - | - | 0.965 | 0.965 | 0.614 | 1.38x | 17.0/24.2/28.2% | 2.1/5.3% | 2 |
| 3 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 5 | 1 | 0.892 | 0.879 | 0.013 | - | - | 0.986 | 0.990 | 0.622 | 1.41x | 17.4/24.9/29.2% | 2.1/5.6% | 5 |
| 8 | 1 | 0.891 | 0.877 | 0.014 | - | - | 0.989 | 0.991 | 0.587 | 1.46x | 18.0/25.8/30.2% | 2.2/5.7% | 8 |

> servers=5: decode_failures 1

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| True | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.871 | 0.862 | 0.010 | - | - | 0.963 | 0.966 | 0.586 | 1.34x | 16.4/23.2/27.1% | 2.0/5.1% | 3 |
| 1 | 1 | 0.882 | 0.878 | 0.005 | - | - | 0.969 | 0.971 | 0.588 | 1.33x | 16.4/23.3/27.1% | 2.0/5.1% | 3 |
| 2 | 1 | 0.881 | 0.875 | 0.005 | - | - | 0.968 | 0.969 | 0.552 | 1.30x | 16.1/22.9/26.7% | 2.0/5.0% | 3 |
| 4 | 1 | 0.880 | 0.876 | 0.005 | - | - | 0.965 | 0.969 | 0.588 | 1.32x | 16.3/23.0/26.8% | 2.0/5.1% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.972 | 0.972 | 0.578 | 1.39x | 17.2/24.4/28.6% | 2.1/5.5% | 3 |
| 24 | 1 | 0.888 | 0.883 | 0.006 | - | - | 0.973 | 0.974 | 0.596 | 1.38x | 17.0/24.2/28.3% | 2.1/5.4% | 3 |
| 32 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.976 | 0.977 | 0.579 | 1.37x | 16.8/24.0/28.0% | 2.1/5.4% | 3 |
| 64 | 1 | 0.878 | 0.871 | 0.008 | - | - | 0.975 | 0.975 | 0.588 | 1.41x | 17.4/24.6/28.9% | 2.1/5.5% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.873 | 0.867 | 0.006 | - | - | 0.961 | 0.963 | 0.552 | 1.46x | 18.0/25.7/30.0% | 2.2/5.8% | 3 |
| 16 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.971 | 0.972 | 0.584 | 1.42x | 17.5/24.9/29.0% | 2.2/5.6% | 3 |
| 32 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.965 | 0.971 | 0.569 | 1.37x | 16.9/24.0/28.1% | 2.1/5.3% | 3 |

> window-size=8: misdecodes 135

> window-size=16: misdecodes 57

> window-size=32: misdecodes 10

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.967 | 0.963 | 0.003 | - | - | 0.998 | 0.998 | 0.880 | 1.94x | 21.3/32.3/39.0% | 1.3/5.1% | 3 |
| True | 1 | 0.762 | 0.750 | 0.011 | - | - | 0.845 | 0.897 | 0.647 | 5.50x | 57.2/73.0/78.4% | 3.8/12.7% | 3 |

> no-congestion-scaling=True: queue drops 10.8% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 84

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.505 | 0.497 | 0.008 | - | - | 0.570 | 0.587 | 0.259 | 4.49x | 14.8/24.8/41.9% | 1.5/5.0% | 3 |
| truesize | 1 | 0.542 | 0.533 | 0.009 | - | - | 0.636 | 0.638 | 0.253 | 3.32x | 10.8/19.3/33.0% | 1.1/4.2% | 3 |

> congestion-input=hotstore: decode_failures 50

> congestion-input=truesize: decode_failures 2

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.970 | 0.967 | 0.003 | - | - | 0.998 | 0.999 | 0.883 | 1.81x | 20.0/30.4/36.8% | 1.2/4.8% | 3 |
| adaptive | 1 | 0.967 | 0.963 | 0.003 | - | - | 0.998 | 0.998 | 0.880 | 1.94x | 21.3/32.3/39.0% | 1.3/5.1% | 3 |

