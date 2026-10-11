# Sweep blocks-2026-10-11-9985801

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 9985801 · seeds 9985801
- **blocks** 87 run
- **compute** 8.4 h of simulator time across every cell
- **generated** 2026-10-11T09:42:08+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>70 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 4
- AD-siting: faster: 0.687 s per simulated hour against 1.45 over 51 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-worst: role-placement=degree: misdecodes 2
- DB-warm: warm-num-nodes=0: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 28
- DB-warm: warm-num-nodes=25: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 28
- DB-warm: warm-num-nodes=100: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 28
- DB-warm: warm-num-nodes=2000: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 28
- DG-burst: burst-loss=0.1: decode_failures 2
- DG-burst: burst-loss=0.2: decode_failures 9
- DG-burst: burst-loss=0.3: decode_failures 32
- DG-outage: burst-loss=0.1: decode_failures 13
- DG-outage: burst-loss=0.2: decode_failures 36
- DG-outage: burst-loss=0.3: decode_failures 27
- FW-mixed-26: legacy-fraction=0.5: decode_failures 7
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 8
- LD-chatty: broadcast-interval-s=300: decode_failures 16
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 10.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 28
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 15.7% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 80
- MS-density: nodes=90: decode_failures 26
- MS-hopscale: nodes=500: decode_failures 20
- MS-oversubscribed: nodes=500: decode_failures 6
- MS-siting: siting-mix=event: decode_failures 5
- MS-size: nodes=150: decode_failures 1
- MS-stretch: stretch=2.0: decode_failures 7
- PR-repeats-busy: extra-repeats=True: misdecodes 2
- RF-eu-presets: preset=SHORT_FAST: decode_failures 7
- RF-preset: preset=SHORT_FAST: decode_failures 7
- RF-preset: preset=LONG_MODERATE: decode_failures 3
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- RF-txpower: tx-power=17: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 46
- SF-bucket-mode: bucket-mode=time: misdecodes 28
- SF-bucket-mode: bucket-mode=window: misdecodes 20
- SF-bucket-time: time-bucket-s=600: misdecodes 127
- SF-bucket-time: time-bucket-s=1800: misdecodes 28
- SF-bucket-time: time-bucket-s=3600: misdecodes 7
- SF-cadence: trigger=interval: misdecodes 19
- SF-cadence: trigger=interval: decode_failures 1
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 11
- SF-capacity-local: capacity=4: decode_failures 101
- SF-capacity-local: capacity=8: decode_failures 40
- SF-capacity: capacity=4: decode_failures 101
- SF-capacity: capacity=8: decode_failures 40
- SF-capacity-window: capacity=8: misdecodes 25
- SF-capacity-window: capacity=8: decode_failures 42
- SF-capacity-window: capacity=16: misdecodes 21
- SF-capacity-window: capacity=16: decode_failures 1
- SF-capacity-window: capacity=32: misdecodes 20
- SF-catchup: catch-up-hours=: misdecodes 11
- SF-catchup: catch-up-hours=02-06: decode_failures 11
- SF-catchup: catch-up-hours=00-08: decode_failures 12
- SF-hops-flat: hops-apart=4: decode_failures 43
- SF-hops-spread: hops-apart=4: decode_failures 43
- SF-hops-spread: hops-apart=5: decode_failures 43
- SF-place-flat: place=spread: decode_failures 13
- SF-place-spread: place=spread: decode_failures 13
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 17
- SF-window-size: window-size=8: misdecodes 136
- SF-window-size: window-size=16: misdecodes 58
- SF-window-size: window-size=32: misdecodes 20
- TH-congestion: no-congestion-scaling=True: decode_failures 56

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `DB-hotstore` | 1.58 | 2.37 | 0.67x | 51 |
| `SF-bucket-mode` | 0.979 | 1.47 | 0.67x | 51 |
| `SF-width` | 1.1 | 1.68 | 0.66x | 51 |
| `RT-rebroadcast` | 1.01 | 1.58 | 0.64x | 51 |
| `RF-duct` | 1.12 | 1.75 | 0.64x | 51 |
| `SF-capacity` | 1.1 | 1.75 | 0.63x | 51 |
| `SF-replay-order-broadcast` | 1.06 | 1.72 | 0.61x | 51 |
| `MS-oversubscribed` | 11.6 | 20.1 | 0.58x | 51 |
| `TH-congestion-input` | 6.22 | 11.2 | 0.56x | 51 |
| `RF-stretch-duct` | 0.956 | 1.84 | 0.52x | 51 |
| `MS-hopscale` | 9.04 | 17.9 | 0.51x | 51 |
| `DB-warm` | 16.8 | 33.5 | 0.50x | 51 |
| `DB-hotstore-stress` | 11.2 | 22.3 | 0.50x | 51 |
| `AD-siting` | 0.687 | 1.45 | 0.47x | 51 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.991 | 0.991 | 0.863 → 0.868 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.988 | 0.988 | 0.855 → 0.863 | 1.2x bytes_on_air | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.000 → 0.948 | 0.948 | 0.006 → 0.785 | 5.5x bytes_on_air | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.072 → 0.978 | 0.905 | 0.070 → 0.977 | 6.5x advert_bytes | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.123 → 0.936 | 0.813 | 0.100 → 0.813 | 1e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.064 → 0.863 | 0.799 | 0.062 → 0.855 | 5.1x advert_bytes | up | 5 |
| `MS-stretch` | stretch | **held** | 0.215 → 0.988 | 0.772 | 0.128 → 0.855 | 4.9x advert_bytes | down | 4 |
| `RF-txpower` | tx-power | **text** | 0.093 → 0.863 | 0.769 | 0.093 → 0.855 | 4.9x sr_airtime | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.237 → 0.988 | 0.750 | 0.293 → 0.855 | 7.9x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.237 → 0.988 | 0.750 | 0.293 → 0.855 | 11x sr_airtime | up | 3 |
| `RF-bw500` | preset | **held** | 0.288 → 0.977 | 0.689 | 0.156 → 0.816 | 3.6x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.380 → 0.988 | 0.608 | 0.307 → 0.855 | 7.8x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.379 → 0.841 | 0.462 | 0.305 → 0.674 | 5.1x bytes_on_air | down | 3 |
| `SF-place-flat` | place | **held** | 0.541 → 0.988 | 0.447 | 0.855 → 0.869 | 1.8x advert_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.541 → 0.988 | 0.447 | 0.855 → 0.869 | 1.8x advert_bytes | up | 6 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.347 → 0.703 | 0.356 | 0.341 → 0.693 | 2.2x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.548 → 0.892 | 0.344 | 0.525 → 0.888 | 7.7x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.588 → 0.927 | 0.339 | 0.564 → 0.925 | 7.2x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.531 → 0.863 | 0.332 | 0.504 → 0.855 | 2.4x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.561 → 0.863 | 0.301 | 0.529 → 0.855 | 2.4x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.685 → 0.947 | 0.262 | 0.675 → 0.947 | 1.7x sr_bytes | up | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.725 → 0.964 | 0.238 | 0.719 → 0.961 | 4.7x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.676 → 0.908 | 0.232 | 0.664 → 0.899 | 4.6x sr_bytes | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.703 → 0.928 | 0.226 | 0.679 → 0.927 | 2.6x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.703 → 0.910 | 0.207 | 0.679 → 0.908 | 2.3x sr_bytes | up | 3 |
| `DB-hotstore-stress` | max-num-nodes | **text** | 0.300 → 0.482 | 0.183 | 0.298 → 0.479 | 5x sr_airtime | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.698 → 0.869 | 0.172 | 0.687 → 0.863 | 1.5x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.798 → 0.964 | 0.166 | 0.781 → 0.961 | 5.2x sr_airtime | up | 5 |
| `RT-spread` | hop-spread | **text** | 0.703 → 0.863 | 0.160 | 0.679 → 0.855 | 1.6x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.727 → 0.863 | 0.136 | 0.708 → 0.855 | 1.5x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.729 → 0.863 | 0.134 | 0.729 → 0.855 | 1.3x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.801 → 0.902 | 0.101 | 0.785 → 0.898 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.801 → 0.902 | 0.101 | 0.785 → 0.898 | 2.4x bytes_on_air | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.863 → 0.963 | 0.100 | 0.855 → 0.960 | 1.2x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.799 → 0.898 | 0.100 | 0.786 → 0.895 | 1.9x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.802 → 0.898 | 0.097 | 0.790 → 0.895 | 2x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.826 → 0.911 | 0.084 | 0.814 → 0.908 | 4.9x sr_airtime | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.863 → 0.939 | 0.077 | 0.855 → 0.937 | 1.6x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.863 → 0.937 | 0.074 | 0.855 → 0.930 | 1.3x bytes_on_air | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.757 → 0.826 | 0.068 | 0.658 → 0.707 | 1.2x sr_airtime | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.920 → 0.988 | 0.068 | 0.855 → 0.861 | 26x sr_airtime | down | 3 |
| `MS-roles` | role-mix | **text** | 0.801 → 0.868 | 0.067 | 0.785 → 0.861 | 1.6x sr_bytes | down | 2 |
| `SF-cadence` | trigger | **held** | 0.926 → 0.988 | 0.062 | 0.829 → 0.857 | 13x advert_bytes | down | 4 |
| `AD-badrouters` | role-placement | **text** | 0.770 → 0.823 | 0.053 | 0.747 → 0.808 | 1.1x sr_bytes | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.941 → 0.991 | 0.050 | 0.855 → 0.868 | 2.4x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.941 → 0.991 | 0.050 | 0.855 → 0.868 | 2.4x sr_bytes | down | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.819 → 0.868 | 0.049 | 0.806 → 0.862 | 1.5x sr_bytes | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.841 → 0.889 | 0.048 | 0.833 → 0.884 | 2.1x bytes_on_air | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.816 → 0.863 | 0.047 | 0.806 → 0.856 | 1.4x sr_airtime | down | 4 |
| `FW-versions` | profile | **text** | 0.863 → 0.907 | 0.045 | 0.855 → 0.899 | 3.3x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.863 → 0.905 | 0.043 | 0.855 → 0.900 | 3.2x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.842 → 0.883 | 0.041 | 0.834 → 0.877 | 2.1x bytes_on_air | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.863 → 0.903 | 0.041 | 0.855 → 0.899 | 3.3x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.412 → 0.446 | 0.033 | 0.478 → 0.508 | 1.6x sr_airtime | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.863 → 0.894 | 0.032 | 0.855 → 0.858 | 2.9x sr_airtime | up | 2 |
| `LD-diurnal` | diurnal | **text** | 0.863 → 0.887 | 0.024 | 0.855 → 0.880 | 1.3x advert_bytes | down | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.959 → 0.982 | 0.023 | 0.830 → 0.857 | 9.3x advert_bytes | down | 3 |
| `AD-worst` | role-placement | **text** | 0.805 → 0.827 | 0.022 | 0.798 → 0.825 | 1.4x sr_bytes | down | 2 |
| `DM-mode` | dm-mode | **text** | 0.816 → 0.834 | 0.019 | 0.816 → 0.834 | 1.1x sr_airtime | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.863 → 0.881 | 0.018 | 0.855 → 0.875 | 1.3x bytes_on_air | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.869 → 0.885 | 0.016 | 0.862 → 0.880 | 1.2x sr_bytes | up | 2 |
| `SF-capacity` | capacity | **text** | 0.863 → 0.877 | 0.014 | 0.855 → 0.869 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.863 → 0.877 | 0.014 | 0.855 → 0.869 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-window` | capacity | **held** | 0.972 → 0.986 | 0.014 | 0.859 → 0.866 | 1.6x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.863 → 0.876 | 0.013 | 0.855 → 0.869 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.863 → 0.876 | 0.013 | 0.855 → 0.869 | 1.1x sr_airtime | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.862 → 0.875 | 0.013 | 0.853 → 0.868 | 5.5x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.863 → 0.875 | 0.012 | 0.855 → 0.868 | 3.5x advert_bytes | down | 4 |
| `SF-servers-flat` | servers | **text** | 0.863 → 0.873 | 0.010 | 0.850 → 0.869 | 6.5x sr_bytes | down | 4 |
| `SF-servers-spread` | servers | **text** | 0.863 → 0.873 | 0.010 | 0.850 → 0.869 | 6.5x sr_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.976 → 0.986 | 0.010 | 0.856 → 0.865 | 2.1x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.863 → 0.872 | 0.009 | 0.855 → 0.865 | 1.1x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **text** | 0.865 → 0.874 | 0.009 | 0.858 → 0.866 | 6.9x advert_bytes | up | 3 |
| `SF-replay-order` | replay-ordering | **text** | 0.863 → 0.871 | 0.008 | 0.855 → 0.864 | 1.1x sr_airtime | up | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.863 → 0.871 | 0.008 | 0.855 → 0.862 | 2.8x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **text** | 0.863 → 0.871 | 0.008 | 0.855 → 0.864 | 3.1x advert_bytes | down | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.956 → 0.964 | 0.007 | 0.954 → 0.961 | 1.2x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **text** | 0.863 → 0.869 | 0.007 | 0.855 → 0.861 | 5.7x advert_bytes | = | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.988 → 0.993 | 0.006 | 0.861 → 0.866 | 1.1x sr_airtime | up | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.982 → 0.988 | 0.005 | 0.855 → 0.856 | 1.1x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.964 → 0.967 | 0.004 | 0.961 → 0.965 | 1.1x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.962 → 0.966 | 0.003 | 0.832 → 0.834 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.983 → 0.987 | 0.003 | 0.855 → 0.858 | 1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.966 → 0.968 | 0.002 | 0.834 → 0.834 | 1.2x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.994 → 0.995 | 0.001 | 0.960 → 0.961 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| sprinkled | 1 | 0.930 | 0.925 | 0.005 | - | - | 0.976 | 0.977 | 0.744 | 1.22x | 16.8/21.0/26.3% | 1.8/4.8% | 3 |
| arms-race | 1 | 0.963 | 0.960 | 0.003 | - | - | 0.996 | 0.997 | 0.901 | 1.12x | 19.6/24.0/27.7% | 1.4/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.1 | 1 | 0.904 | 0.893 | 0.012 | - | - | 0.936 | 0.939 | 0.685 | 1.27x | 18.4/22.7/26.2% | 2.0/4.9% | 3 |
| 0.3 | 1 | 0.939 | 0.937 | 0.003 | - | - | 0.992 | 0.992 | 0.700 | 1.04x | 19.4/25.5/27.6% | 1.3/4.6% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.801 | 0.785 | 0.017 | - | - | 0.948 | 0.951 | 0.000 | 1.14x | 15.7/21.3/28.3% | 1.9/4.8% | 3 |
| inverse | 1 | 0.770 | 0.747 | 0.023 | - | - | 0.933 | 0.944 | 0.000 | 1.11x | 14.1/17.8/20.9% | 1.9/3.7% | 3 |
| random | 1 | 0.823 | 0.808 | 0.015 | - | - | 0.960 | 0.962 | 0.000 | 1.19x | 15.2/19.6/23.2% | 2.1/4.8% | 3 |

> role-placement=inverse: decode_failures 4

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.801 | 0.785 | 0.017 | - | - | 0.948 | 0.951 | 0.000 | 1.14x | 15.7/21.3/28.3% | 1.9/4.8% | 3 |
| all-routers | 1 | 0.902 | 0.898 | 0.004 | - | - | 0.990 | 0.993 | 0.000 | 2.73x | 30.9/39.1/42.6% | 4.5/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.801 | 0.785 | 0.017 | - | - | 0.948 | 0.951 | 0.000 | 1.14x | 15.7/21.3/28.3% | 1.9/4.8% | 3 |
| no-mute | 1 | 0.836 | 0.829 | 0.007 | - | - | 0.956 | 0.957 | 0.000 | 1.31x | 17.2/20.7/26.0% | 2.1/5.0% | 3 |
| all-routers | 1 | 0.902 | 0.898 | 0.004 | - | - | 0.990 | 0.993 | 0.000 | 2.73x | 30.9/39.1/42.6% | 4.5/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.801 | 0.785 | 0.017 | - | - | 0.948 | 0.951 | 0.000 | 1.14x | 15.7/21.3/28.3% | 1.9/4.8% | 3 |
| local-typical | 1 | 0.615 | 0.612 | 0.004 | - | - | 0.789 | 0.789 | 0.000 | 1.23x | 12.9/22.2/28.7% | 2.1/5.2% | 3 |
| basement-heavy | 1 | 0.006 | 0.006 | 0.000 | - | - | 0.000 | 0.000 | 0.000 | 0.23x | 0.2/1.8/4.0% | 0.2/1.3% | 3 |

> faster: 0.687 s per simulated hour against 1.45 over 51 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.827 | 0.825 | 0.003 | - | - | 0.940 | 0.940 | 0.000 | 2.46x | 19.4/31.8/40.9% | 1.9/5.8% | 3 |
| inverse | 1 | 0.805 | 0.798 | 0.007 | - | - | 0.935 | 0.936 | 0.000 | 2.32x | 17.1/27.0/33.9% | 1.8/3.7% | 3 |

> role-placement=degree: misdecodes 2

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.863 | 0.863 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.29x | 17.7/22.1/26.9% | 1.9/4.9% | 3 |
| sr | 1 | 0.884 | 0.868 | 0.016 | - | - | 0.991 | 0.995 | 0.000 | 1.33x | 18.2/22.9/27.7% | 1.9/5.1% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.966 | 0.971 | 0.000 | 2.96x | 38.3/51.3/58.3% | 4.2/9.7% | 3 |
| 100 | 1 | 0.898 | 0.895 | 0.003 | - | - | 0.988 | 0.990 | 0.000 | 1.57x | 20.6/27.9/32.7% | 2.2/5.2% | 3 |
| 120 | 1 | 0.898 | 0.895 | 0.003 | - | - | 0.988 | 0.990 | 0.000 | 1.57x | 20.6/27.9/32.7% | 2.2/5.2% | 3 |
| 250 | 1 | 0.898 | 0.895 | 0.003 | - | - | 0.988 | 0.990 | 0.000 | 1.57x | 20.6/27.9/32.7% | 2.2/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.300 | 0.298 | 0.002 | - | - | 0.263 | 0.263 | 0.048 | 11.39x | 41.4/57.0/69.7% | 4.1/11.0% | 3 |
| 120 | 1 | 0.482 | 0.478 | 0.004 | - | - | 0.412 | 0.413 | 0.066 | 4.17x | 15.7/23.5/31.0% | 1.4/4.6% | 3 |
| 250 | 1 | 0.482 | 0.479 | 0.004 | - | - | 0.405 | 0.406 | 0.067 | 4.06x | 15.3/22.9/30.4% | 1.4/4.5% | 3 |

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.898 | 0.895 | 0.003 | - | - | 0.988 | 0.990 | 0.000 | 1.57x | 20.6/27.9/32.7% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.898 | 0.895 | 0.003 | - | - | 0.988 | 0.990 | 0.000 | 1.57x | 20.6/27.9/32.7% | 2.2/5.2% | 3 |
| constrained | 1 | 0.802 | 0.790 | 0.011 | - | - | 0.961 | 0.967 | 0.000 | 2.95x | 38.2/51.2/58.1% | 4.1/9.7% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.714 | 0.707 | 0.007 | - | - | 0.826 | 0.838 | 0.514 | 5.59x | 60.5/72.9/76.3% | 3.9/12.5% | 3 |
| 25 | 1 | 0.714 | 0.707 | 0.007 | - | - | 0.826 | 0.838 | 0.514 | 5.59x | 60.5/72.9/76.3% | 3.9/12.5% | 3 |
| 100 | 1 | 0.714 | 0.707 | 0.007 | - | - | 0.826 | 0.838 | 0.514 | 5.59x | 60.5/72.9/76.3% | 3.9/12.5% | 3 |
| 2000 | 1 | 0.714 | 0.707 | 0.007 | - | - | 0.826 | 0.838 | 0.514 | 5.59x | 60.5/72.9/76.3% | 3.9/12.5% | 3 |

> warm-num-nodes=0: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 28

> warm-num-nodes=25: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 28

> warm-num-nodes=100: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 28

> warm-num-nodes=2000: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 28

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.1 | 1 | 0.760 | 0.743 | 0.017 | - | - | 0.956 | 0.960 | 0.000 | 1.27x | 17.7/21.8/26.7% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.677 | 0.648 | 0.029 | - | - | 0.935 | 0.941 | 0.000 | 1.18x | 16.7/20.5/25.1% | 1.8/4.2% | 3 |
| 0.3 | 1 | 0.561 | 0.529 | 0.033 | - | - | 0.810 | 0.875 | 0.000 | 1.05x | 15.1/18.6/23.0% | 1.6/3.7% | 3 |

> burst-loss=0.1: decode_failures 2

> burst-loss=0.2: decode_failures 9

> burst-loss=0.3: decode_failures 32

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.1 | 1 | 0.832 | 0.823 | 0.009 | - | - | 0.984 | 0.987 | 0.000 | 1.38x | 19.1/23.5/28.3% | 2.1/4.9% | 3 |
| 0.2 | 1 | 0.785 | 0.772 | 0.013 | - | - | 0.945 | 0.949 | 0.000 | 1.41x | 19.4/24.0/28.8% | 2.1/4.7% | 3 |
| 0.3 | 1 | 0.727 | 0.708 | 0.019 | - | - | 0.924 | 0.927 | 0.000 | 1.42x | 19.3/24.3/29.0% | 2.2/4.5% | 3 |

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.1 | 1 | 0.761 | 0.748 | 0.013 | - | - | 0.969 | 0.977 | 0.000 | 1.24x | 17.3/21.4/26.3% | 1.8/4.8% | 3 |
| 0.2 | 1 | 0.644 | 0.623 | 0.021 | - | - | 0.872 | 0.928 | 0.000 | 1.16x | 16.2/20.4/24.6% | 1.7/4.2% | 3 |
| 0.3 | 1 | 0.531 | 0.504 | 0.026 | - | - | 0.772 | 0.860 | 0.000 | 1.09x | 15.6/19.5/24.0% | 1.7/4.1% | 3 |

> burst-loss=0.1: decode_failures 13

> burst-loss=0.2: decode_failures 36

> burst-loss=0.3: decode_failures 27

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.816 | 0.816 | 0.000 | - | - | 0.972 | 0.976 | 0.000 | 1.81x | 24.9/30.0/36.4% | 2.7/6.8% | 3 |
| directed-with-late-flood | 1 | 0.834 | 0.834 | 0.000 | - | - | 0.968 | 0.980 | 0.000 | 1.63x | 22.5/27.3/33.6% | 2.5/6.3% | 3 |
| m4-early-flood | 1 | 0.833 | 0.833 | 0.000 | - | - | 0.977 | 0.986 | 0.000 | 1.62x | 22.6/27.2/33.5% | 2.4/6.3% | 3 |

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.977 | 0.978 | 0.455 | 0.74x | 9.1/11.7/13.2% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.25 | 1 | 0.841 | 0.833 | 0.008 | - | - | 0.956 | 0.959 | 0.134 | 1.14x | 13.4/18.8/21.4% | 1.7/4.6% | 3 |
| 0.5 | 1 | 0.872 | 0.859 | 0.013 | - | - | 0.957 | 0.958 | 0.651 | 1.01x | 11.8/16.9/20.5% | 1.6/4.1% | 3 |
| 0.75 | 1 | 0.889 | 0.884 | 0.005 | - | - | 0.973 | 0.975 | 0.433 | 0.93x | 11.3/15.4/18.7% | 1.4/3.4% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.25 | 1 | 0.842 | 0.834 | 0.008 | - | - | 0.956 | 0.960 | 0.151 | 1.15x | 13.4/18.9/21.4% | 1.9/4.7% | 3 |
| 0.5 | 1 | 0.879 | 0.865 | 0.014 | - | - | 0.959 | 0.965 | 0.593 | 1.01x | 12.0/17.1/20.9% | 1.4/4.1% | 3 |
| 0.75 | 1 | 0.883 | 0.877 | 0.006 | - | - | 0.971 | 0.972 | 0.403 | 0.90x | 10.9/15.2/18.6% | 1.4/3.4% | 3 |

> legacy-fraction=0.5: decode_failures 7

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.995 | 0.997 | 0.000 | 0.71x | 10.1/12.6/15.8% | 1.1/2.9% | 3 |
| signing=true | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.898 | 0.891 | 0.007 | - | - | 0.977 | 0.978 | 0.402 | 0.74x | 9.4/12.9/14.8% | 1.1/2.6% | 3 |
| 2.5 | 1 | 0.898 | 0.892 | 0.007 | - | - | 0.979 | 0.979 | 0.408 | 0.78x | 9.8/13.4/15.3% | 1.2/2.6% | 3 |
| 2.6 | 1 | 0.892 | 0.884 | 0.007 | - | - | 0.968 | 0.970 | 0.392 | 0.73x | 9.4/13.1/15.3% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.907 | 0.899 | 0.008 | - | - | 0.980 | 0.983 | 0.411 | 0.75x | 9.5/14.2/17.1% | 1.0/3.1% | 3 |
| 2.8 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.991 | 0.992 | 0.000 | 0.90x | 12.4/15.1/18.3% | 1.4/3.4% | 3 |
| 900 | 1 | 0.826 | 0.814 | 0.012 | - | - | 0.970 | 0.971 | 0.000 | 2.09x | 28.5/34.9/42.5% | 3.1/7.8% | 3 |
| 300 | 1 | 0.548 | 0.525 | 0.024 | - | - | 0.790 | 0.835 | 0.000 | 4.55x | 55.9/67.2/74.4% | 7.1/15.4% | 3 |

> broadcast-interval-s=300: decode_failures 16

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.927 | 0.925 | 0.001 | - | - | 0.996 | 0.997 | 0.000 | 0.99x | 13.1/16.0/19.1% | 1.5/3.5% | 3 |
| 900 | 1 | 0.866 | 0.859 | 0.007 | - | - | 0.989 | 0.989 | 0.000 | 2.50x | 32.9/39.3/46.7% | 3.7/8.7% | 3 |
| 300 | 1 | 0.588 | 0.564 | 0.023 | - | - | 0.872 | 0.882 | 0.000 | 5.22x | 60.2/71.1/76.8% | 8.3/16.5% | 3 |

> broadcast-interval-s=300: decode_failures 8

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.987 | 0.988 | 0.000 | 1.25x | 17.1/21.2/25.7% | 1.8/4.8% | 3 |
| sinusoid | 1 | 0.877 | 0.869 | 0.008 | - | - | 0.989 | 0.993 | 0.000 | 1.22x | 16.7/20.7/24.9% | 1.8/4.6% | 3 |
| commuter | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.826 | 0.814 | 0.012 | - | - | 0.970 | 0.971 | 0.000 | 2.09x | 28.5/34.9/42.5% | 3.1/7.8% | 3 |
| 3600 | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.991 | 0.992 | 0.000 | 0.90x | 12.4/15.1/18.3% | 1.4/3.4% | 3 |
| 10800 | 1 | 0.908 | 0.905 | 0.003 | - | - | 0.995 | 0.996 | 0.000 | 0.61x | 8.3/10.2/12.2% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.911 | 0.908 | 0.003 | - | - | 0.997 | 0.998 | 0.000 | 0.43x | 5.8/7.1/8.7% | 0.7/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.25 | 1 | 0.863 | 0.856 | 0.007 | - | - | 0.986 | 0.988 | 0.000 | 1.43x | 19.7/24.3/29.6% | 2.1/5.4% | 3 |
| 1.0 | 1 | 0.849 | 0.840 | 0.009 | - | - | 0.984 | 0.986 | 0.000 | 1.57x | 21.7/26.6/32.5% | 2.4/6.0% | 3 |
| 4.0 | 1 | 0.816 | 0.806 | 0.011 | - | - | 0.966 | 0.967 | 0.000 | 1.93x | 26.9/32.9/40.9% | 2.9/7.7% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.714 | 0.707 | 0.007 | - | - | 0.826 | 0.838 | 0.514 | 5.59x | 60.5/72.9/76.3% | 3.9/12.5% | 3 |
| 1.0 | 1 | 0.663 | 0.658 | 0.005 | - | - | 0.757 | 0.800 | 0.473 | 5.93x | 62.9/74.8/77.4% | 4.1/13.2% | 3 |

> traceroute-per-hour=0.0: queue drops 10.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 28

> traceroute-per-hour=1.0: queue drops 15.7% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 80

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.798 | 0.781 | 0.017 | - | - | 0.909 | 0.922 | 0.650 | 1.49x | 22.7/28.6/31.8% | 3.5/6.8% | 3 |
| 60 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 90 | 1 | 0.933 | 0.925 | 0.008 | - | - | 0.984 | 0.989 | 0.191 | 1.48x | 19.4/27.8/29.6% | 1.3/4.8% | 3 |
| 120 | 1 | 0.964 | 0.961 | 0.002 | - | - | 0.994 | 0.994 | 0.836 | 1.92x | 23.2/32.5/37.2% | 1.3/5.0% | 3 |
| 150 | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.999 | 0.999 | 0.758 | 2.33x | 27.3/38.9/44.1% | 1.1/5.4% | 3 |

> nodes=90: decode_failures 26

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 120 | 1 | 0.685 | 0.669 | 0.016 | - | - | 0.855 | 0.855 | 0.000 | 2.03x | 14.0/25.4/31.3% | 1.5/4.6% | 3 |
| 250 | 1 | 0.483 | 0.480 | 0.004 | - | - | 0.406 | 0.406 | 0.069 | 4.39x | 16.6/24.8/33.4% | 1.5/4.9% | 3 |
| 500 | 1 | 0.309 | 0.307 | 0.002 | - | - | 0.380 | 0.381 | 0.034 | 10.23x | 18.2/34.5/61.9% | 1.7/5.5% | 3 |

> nodes=500: decode_failures 20

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.687 | 0.674 | 0.013 | - | - | 0.841 | 0.842 | 0.000 | 1.88x | 13.0/23.4/29.0% | 1.4/4.3% | 3 |
| 250 | 1 | 0.482 | 0.478 | 0.004 | - | - | 0.412 | 0.413 | 0.066 | 4.17x | 15.7/23.5/31.0% | 1.4/4.6% | 3 |
| 500 | 1 | 0.307 | 0.305 | 0.002 | - | - | 0.379 | 0.379 | 0.029 | 9.53x | 16.9/31.2/56.9% | 1.6/5.0% | 3 |

> nodes=500: decode_failures 6

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.868 | 0.861 | 0.007 | - | - | 0.974 | 0.975 | 0.000 | 1.37x | 18.6/22.8/27.8% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.801 | 0.785 | 0.017 | - | - | 0.948 | 0.951 | 0.000 | 1.14x | 15.7/21.3/28.3% | 1.9/4.8% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.868 | 0.862 | 0.006 | - | - | 0.978 | 0.980 | 0.000 | 1.39x | 18.8/23.6/28.1% | 2.1/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.819 | 0.806 | 0.013 | - | - | 0.952 | 0.953 | 0.000 | 1.28x | 17.3/24.3/30.8% | 2.1/4.9% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.05 | 1 | 0.869 | 0.864 | 0.006 | - | - | 0.990 | 0.992 | 0.000 | 1.47x | 19.8/26.4/31.9% | 2.2/5.1% | 3 |
| 0.1 | 1 | 0.871 | 0.865 | 0.006 | - | - | 0.985 | 0.988 | 0.000 | 1.55x | 19.9/28.7/32.8% | 2.2/5.0% | 3 |
| 0.2 | 1 | 0.881 | 0.875 | 0.005 | - | - | 0.989 | 0.992 | 0.000 | 1.72x | 21.6/33.2/36.1% | 2.4/4.9% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| local-typical | 1 | 0.761 | 0.756 | 0.004 | - | - | 0.954 | 0.957 | 0.000 | 1.56x | 16.4/23.6/29.2% | 2.4/5.5% | 3 |
| event | 1 | 0.072 | 0.070 | 0.002 | - | - | 0.162 | 0.205 | 0.000 | 0.57x | 1.1/6.7/10.2% | 0.6/2.8% | 3 |
| backbone | 1 | 0.978 | 0.977 | 0.000 | - | - | 1.000 | 1.000 | 0.924 | 1.10x | 23.5/31.1/33.8% | 1.4/5.5% | 3 |

> siting-mix=event: decode_failures 5

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.908 | 0.899 | 0.009 | - | - | 0.975 | 0.978 | 0.792 | 1.57x | 28.6/35.1/38.3% | 3.3/7.8% | 3 |
| 60 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 90 | 1 | 0.787 | 0.778 | 0.009 | - | - | 0.922 | 0.924 | 0.312 | 1.55x | 15.3/22.2/25.0% | 1.4/4.4% | 3 |
| 120 | 1 | 0.685 | 0.669 | 0.016 | - | - | 0.855 | 0.855 | 0.000 | 2.03x | 14.0/25.4/31.3% | 1.5/4.6% | 3 |
| 150 | 1 | 0.676 | 0.664 | 0.012 | - | - | 0.840 | 0.842 | 0.031 | 2.56x | 16.0/25.6/31.6% | 1.5/5.0% | 3 |

> nodes=150: decode_failures 1

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 1.25 | 1 | 0.639 | 0.626 | 0.013 | - | - | 0.767 | 0.775 | 0.000 | 1.40x | 12.4/18.2/21.3% | 2.1/4.4% | 3 |
| 1.5 | 1 | 0.347 | 0.341 | 0.006 | - | - | 0.519 | 0.520 | 0.000 | 1.42x | 9.4/14.8/15.8% | 2.3/4.3% | 3 |
| 2.0 | 1 | 0.129 | 0.128 | 0.002 | - | - | 0.215 | 0.249 | 0.000 | 0.86x | 4.0/8.6/10.5% | 1.4/2.7% | 3 |

> stretch=2.0: decode_failures 7

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| clustered | 1 | 0.911 | 0.904 | 0.006 | - | - | 0.974 | 0.977 | 0.544 | 1.20x | 19.8/33.5/34.9% | 1.6/5.3% | 3 |
| corridor | 1 | 0.685 | 0.675 | 0.010 | - | - | 0.885 | 0.885 | 0.377 | 1.35x | 16.2/25.2/27.2% | 1.9/5.8% | 3 |
| hub | 1 | 0.947 | 0.947 | 0.001 | - | - | 0.981 | 0.981 | 0.788 | 1.20x | 28.0/37.0/38.9% | 1.5/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.834 | 0.834 | 0.000 | - | - | 0.968 | 0.980 | 0.000 | 1.63x | 22.5/27.3/33.6% | 2.5/6.3% | 3 |
| True | 1 | 0.834 | 0.834 | 0.000 | - | - | 0.966 | 0.979 | 0.000 | 1.65x | 22.8/27.4/33.9% | 2.5/6.4% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.834 | 0.834 | 0.000 | - | - | 0.966 | 0.979 | 0.000 | 1.65x | 22.8/27.4/33.9% | 2.5/6.4% | 3 |
| m4-early-flood | 1 | 0.832 | 0.832 | 0.000 | - | - | 0.962 | 0.975 | 0.000 | 1.63x | 22.6/27.4/33.5% | 2.4/6.3% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.863 | 0.863 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.29x | 17.7/22.1/26.9% | 1.9/4.9% | 3 |
| chain | 1 | 0.858 | 0.855 | 0.003 | - | - | 0.934 | 0.980 | 0.000 | 1.52x | 21.2/25.6/31.3% | 2.3/5.8% | 3 |
| sr | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| True | 1 | 0.872 | 0.865 | 0.007 | - | - | 0.993 | 0.996 | 0.000 | 1.35x | 18.5/22.7/27.8% | 2.0/5.1% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.961 | 0.002 | - | - | 0.994 | 0.994 | 0.836 | 1.92x | 23.2/32.5/37.2% | 1.3/5.0% | 3 |
| True | 1 | 0.963 | 0.960 | 0.002 | - | - | 0.995 | 0.995 | 0.829 | 1.92x | 22.9/32.1/36.7% | 1.3/4.9% | 3 |

> extra-repeats=True: misdecodes 2

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.158 | 0.156 | 0.002 | - | - | 0.288 | 0.291 | 0.000 | 0.04x | 0.2/0.4/0.7% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.418 | 0.414 | 0.004 | - | - | 0.607 | 0.608 | 0.000 | 0.27x | 2.1/2.8/3.4% | 0.4/0.9% | 3 |
| LONG_TURBO | 1 | 0.825 | 0.816 | 0.010 | - | - | 0.977 | 0.978 | 0.000 | 1.33x | 13.8/19.4/22.9% | 2.0/4.8% | 3 |

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 0.25 | 1 | 0.889 | 0.881 | 0.009 | - | - | 0.988 | 0.992 | 0.156 | 1.27x | 20.2/24.6/28.9% | 1.8/5.2% | 3 |
| 1.0 | 1 | 0.937 | 0.930 | 0.006 | - | - | 0.998 | 0.998 | 0.522 | 1.05x | 24.3/28.3/31.1% | 1.4/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.295 | 0.293 | 0.002 | - | - | 0.237 | 0.350 | 0.000 | 0.14x | 0.9/1.5/2.0% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| LITE_FAST | 1 | 0.848 | 0.839 | 0.009 | - | - | 0.985 | 0.986 | 0.000 | 1.03x | 12.7/16.2/20.2% | 1.5/3.8% | 3 |
| NARROW_SLOW | 1 | 0.847 | 0.838 | 0.009 | - | - | 0.987 | 0.989 | 0.000 | 1.29x | 16.0/20.7/25.9% | 2.0/5.0% | 3 |

> preset=SHORT_FAST: decode_failures 7

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| temporal | 1 | 0.780 | 0.764 | 0.016 | - | - | 0.967 | 0.973 | 0.000 | 1.34x | 17.9/22.5/27.4% | 2.0/4.8% | 3 |
| transient | 1 | 0.869 | 0.863 | 0.007 | - | - | 0.991 | 0.992 | 0.000 | 1.37x | 18.7/23.0/27.9% | 2.1/5.1% | 3 |
| periodic | 1 | 0.698 | 0.687 | 0.010 | - | - | 0.824 | 0.829 | 0.000 | 1.25x | 17.3/21.1/25.9% | 1.9/4.4% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.295 | 0.293 | 0.002 | - | - | 0.237 | 0.350 | 0.000 | 0.14x | 0.9/1.5/2.0% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| LONG_MODERATE | 1 | 0.836 | 0.814 | 0.022 | - | - | 0.954 | 0.960 | 0.561 | 3.35x | 45.7/57.8/61.8% | 5.2/12.4% | 3 |

> preset=SHORT_FAST: decode_failures 7

> preset=LONG_MODERATE: decode_failures 3

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.064 | 0.062 | 0.001 | - | - | 0.199 | 0.202 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.158 | 0.156 | 0.002 | - | - | 0.288 | 0.291 | 0.000 | 0.04x | 0.2/0.4/0.7% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| LONG_TURBO | 1 | 0.825 | 0.816 | 0.010 | - | - | 0.977 | 0.978 | 0.000 | 1.33x | 13.8/19.4/22.9% | 2.0/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.983 | 0.985 | 0.000 | 1.86x | 23.5/29.2/34.0% | 2.9/6.9% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 1

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.820 | 0.813 | 0.007 | - | - | 0.936 | 0.941 | 0.000 | 1.31x | 18.3/22.4/27.2% | 2.0/4.9% | 3 |
| 10000 | 1 | 0.698 | 0.687 | 0.010 | - | - | 0.824 | 0.829 | 0.000 | 1.25x | 17.3/21.1/25.9% | 1.9/4.4% | 3 |
| 4000 | 1 | 0.439 | 0.433 | 0.006 | - | - | 0.520 | 0.592 | 0.000 | 1.06x | 14.6/18.1/22.5% | 1.6/3.4% | 3 |
| 2000 | 1 | 0.100 | 0.100 | 0.000 | - | - | 0.123 | 0.196 | 0.000 | 0.71x | 9.5/12.8/15.3% | 1.1/1.9% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.347 | 0.341 | 0.006 | - | - | 0.519 | 0.520 | 0.000 | 1.42x | 9.4/14.8/15.8% | 2.3/4.3% | 3 |
| 1.0 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.793 | 0.793 | 0.521 | 1.03x | 14.5/18.1/21.5% | 1.6/4.3% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 22 | 1 | 0.364 | 0.359 | 0.005 | - | - | 0.526 | 0.529 | 0.000 | 1.53x | 11.0/16.2/18.0% | 2.5/4.9% | 3 |
| 17 | 1 | 0.146 | 0.145 | 0.001 | - | - | 0.245 | 0.260 | 0.000 | 0.95x | 4.5/9.1/12.7% | 1.5/3.0% | 3 |
| 14 | 1 | 0.093 | 0.093 | 0.000 | - | - | 0.224 | 0.227 | 0.000 | 0.65x | 2.5/6.2/9.0% | 0.8/2.6% | 3 |

> tx-power=17: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.961 | 0.002 | - | - | 0.994 | 0.994 | 0.836 | 1.92x | 23.2/32.5/37.2% | 1.3/5.0% | 3 |
| True | 1 | 0.956 | 0.954 | 0.003 | - | - | 0.992 | 0.993 | 0.827 | 2.31x | 27.0/37.3/42.1% | 1.5/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.990 | 0.993 | 0.000 | 1.41x | 19.2/24.9/30.3% | 2.1/5.1% | 3 |
| True | 1 | 0.885 | 0.880 | 0.005 | - | - | 0.991 | 0.994 | 0.000 | 1.48x | 20.0/26.1/31.4% | 2.2/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| random | 1 | 0.863 | 0.856 | 0.007 | - | - | 0.982 | 0.983 | 0.000 | 1.34x | 18.3/22.6/27.6% | 2.0/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.703 | 0.679 | 0.024 | - | - | 0.969 | 0.971 | 0.000 | 1.00x | 14.3/18.0/23.3% | 1.5/4.4% | 3 |
| 7 | 1 | 0.910 | 0.908 | 0.002 | - | - | 0.988 | 0.988 | 0.000 | 1.48x | 19.8/24.0/28.9% | 2.2/5.3% | 3 |
| 15 | 1 | 0.928 | 0.927 | 0.002 | - | - | 0.994 | 0.994 | 0.000 | 1.50x | 19.9/24.2/28.9% | 2.2/5.3% | 3 |
| 32 | 1 | 0.928 | 0.927 | 0.001 | - | - | 0.992 | 0.992 | 0.000 | 1.51x | 20.0/24.3/29.1% | 2.3/5.3% | 3 |

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.703 | 0.679 | 0.024 | - | - | 0.969 | 0.971 | 0.000 | 1.00x | 14.3/18.0/23.3% | 1.5/4.4% | 3 |
| 5 | 1 | 0.860 | 0.852 | 0.008 | - | - | 0.991 | 0.992 | 0.000 | 1.34x | 18.5/22.4/27.4% | 2.0/5.1% | 3 |
| 7 | 1 | 0.910 | 0.908 | 0.002 | - | - | 0.988 | 0.988 | 0.000 | 1.48x | 19.8/24.0/28.9% | 2.2/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| KNOWN_ONLY | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.861 | 0.861 | 0.000 | - | - | 0.920 | 0.993 | 0.000 | 1.30x | 17.9/22.3/27.1% | 1.9/4.9% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.703 | 0.679 | 0.024 | - | - | 0.969 | 0.971 | 0.000 | 1.00x | 14.3/18.0/23.3% | 1.5/4.4% | 3 |
| True | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| BALANCED | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| STRICT | 1 | 0.729 | 0.729 | 0.000 | - | - | 0.872 | 0.874 | 0.000 | 1.42x | 19.4/23.7/28.7% | 2.1/5.4% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| dm | 1 | 0.871 | 0.862 | 0.009 | - | - | 0.983 | 0.984 | 0.000 | 1.32x | 18.2/22.2/27.1% | 2.0/5.1% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.989 | 0.990 | 0.000 | 1.34x | 18.5/22.7/27.6% | 2.0/5.1% | 3 |
| local | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| time | 1 | 0.875 | 0.868 | 0.007 | - | - | 0.992 | 0.995 | 0.000 | 1.38x | 19.0/23.4/28.3% | 2.1/5.2% | 3 |
| window | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.985 | 0.988 | 0.000 | 1.32x | 18.1/22.5/27.4% | 2.0/5.0% | 3 |

> bucket-mode=global: misdecodes 46

> bucket-mode=time: misdecodes 28

> bucket-mode=window: misdecodes 20

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.862 | 0.853 | 0.009 | - | - | 0.987 | 0.989 | 0.000 | 1.52x | 20.7/24.9/30.4% | 2.3/5.8% | 3 |
| 1800 | 1 | 0.875 | 0.868 | 0.007 | - | - | 0.992 | 0.995 | 0.000 | 1.38x | 19.0/23.4/28.3% | 2.1/5.2% | 3 |
| 3600 | 1 | 0.874 | 0.867 | 0.007 | - | - | 0.987 | 0.992 | 0.000 | 1.33x | 18.3/22.6/27.5% | 2.0/5.0% | 3 |

> time-bucket-s=600: misdecodes 127

> time-bucket-s=1800: misdecodes 28

> time-bucket-s=3600: misdecodes 7

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| interval | 1 | 0.841 | 0.829 | 0.012 | - | - | 0.978 | 0.983 | 0.000 | 1.79x | 24.3/28.9/35.3% | 2.6/7.0% | 3 |
| aimd | 1 | 0.859 | 0.857 | 0.002 | - | - | 0.926 | 0.988 | 0.000 | 1.38x | 18.9/23.4/28.3% | 2.0/5.2% | 3 |
| bucket+interval | 1 | 0.841 | 0.830 | 0.011 | - | - | 0.982 | 0.983 | 0.000 | 1.81x | 24.8/29.3/35.9% | 2.6/7.0% | 3 |

> trigger=interval: misdecodes 19

> trigger=interval: decode_failures 1

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 11

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.877 | 0.869 | 0.008 | - | - | 0.989 | 0.995 | 0.000 | 1.33x | 18.4/22.6/27.6% | 2.0/5.2% | 3 |
| 8 | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.985 | 0.987 | 0.000 | 1.33x | 18.3/22.7/27.4% | 2.0/5.0% | 3 |
| 16 | 1 | 0.871 | 0.864 | 0.007 | - | - | 0.990 | 0.992 | 0.000 | 1.34x | 18.6/22.9/27.8% | 2.0/5.1% | 3 |
| 32 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 50 | 1 | 0.873 | 0.866 | 0.007 | - | - | 0.986 | 0.989 | 0.000 | 1.33x | 18.3/22.5/27.4% | 2.0/5.1% | 3 |

> capacity=4: decode_failures 101

> capacity=8: decode_failures 40

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.877 | 0.869 | 0.008 | - | - | 0.989 | 0.995 | 0.000 | 1.33x | 18.4/22.6/27.6% | 2.0/5.2% | 3 |
| 8 | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.985 | 0.987 | 0.000 | 1.33x | 18.3/22.7/27.4% | 2.0/5.0% | 3 |
| 16 | 1 | 0.871 | 0.864 | 0.007 | - | - | 0.990 | 0.992 | 0.000 | 1.34x | 18.6/22.9/27.8% | 2.0/5.1% | 3 |
| 32 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 50 | 1 | 0.873 | 0.866 | 0.007 | - | - | 0.986 | 0.989 | 0.000 | 1.33x | 18.3/22.5/27.4% | 2.0/5.1% | 3 |

> capacity=4: decode_failures 101

> capacity=8: decode_failures 40

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.866 | 0.860 | 0.006 | - | - | 0.972 | 0.988 | 0.000 | 1.31x | 18.1/22.3/27.2% | 2.0/5.0% | 3 |
| 16 | 1 | 0.868 | 0.859 | 0.008 | - | - | 0.986 | 0.989 | 0.000 | 1.33x | 18.4/22.9/27.7% | 2.0/5.0% | 3 |
| 32 | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.985 | 0.988 | 0.000 | 1.32x | 18.1/22.5/27.4% | 2.0/5.0% | 3 |

> capacity=8: misdecodes 25

> capacity=8: decode_failures 42

> capacity=16: misdecodes 21

> capacity=16: decode_failures 1

> capacity=32: misdecodes 20

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.841 | 0.830 | 0.011 | - | - | 0.982 | 0.983 | 0.000 | 1.81x | 24.8/29.3/35.9% | 2.6/7.0% | 3 |
| 02-06 | 1 | 0.862 | 0.857 | 0.005 | - | - | 0.959 | 0.992 | 0.000 | 1.37x | 18.9/23.1/28.1% | 2.1/5.2% | 3 |
| 00-08 | 1 | 0.862 | 0.857 | 0.005 | - | - | 0.961 | 0.991 | 0.000 | 1.43x | 19.7/23.9/29.2% | 2.1/5.5% | 3 |

> catch-up-hours=: misdecodes 11

> catch-up-hours=02-06: decode_failures 11

> catch-up-hours=00-08: decode_failures 12

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.869 | 0.867 | 0.002 | - | - | 0.970 | 0.971 | 0.000 | 1.33x | 18.2/22.5/27.5% | 1.9/5.0% | 3 |
| 2 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 3 | 1 | 0.884 | 0.868 | 0.016 | - | - | 0.991 | 0.995 | 0.000 | 1.33x | 18.2/22.9/27.7% | 1.9/5.1% | 3 |
| 4 | 1 | 0.890 | 0.866 | 0.024 | - | - | 0.941 | 0.984 | 0.000 | 1.34x | 18.3/23.2/28.1% | 1.9/5.2% | 3 |

> hops-apart=4: decode_failures 43

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.869 | 0.867 | 0.002 | - | - | 0.970 | 0.971 | 0.000 | 1.33x | 18.2/22.5/27.5% | 1.9/5.0% | 3 |
| 2 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 3 | 1 | 0.884 | 0.868 | 0.016 | - | - | 0.991 | 0.995 | 0.000 | 1.33x | 18.2/22.9/27.7% | 1.9/5.1% | 3 |
| 4 | 1 | 0.890 | 0.866 | 0.024 | - | - | 0.941 | 0.984 | 0.000 | 1.34x | 18.3/23.2/28.1% | 1.9/5.2% | 3 |
| 5 | 1 | 0.890 | 0.866 | 0.024 | - | - | 0.941 | 0.984 | 0.000 | 1.34x | 18.3/23.2/28.1% | 1.9/5.2% | 3 |

> hops-apart=4: decode_failures 43

> hops-apart=5: decode_failures 43

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.865 | 0.858 | 0.007 | - | - | 0.984 | 0.986 | 0.000 | 1.34x | 18.6/22.8/27.8% | 2.0/5.1% | 3 |
| 30 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 120 | 1 | 0.866 | 0.858 | 0.008 | - | - | 0.985 | 0.987 | 0.000 | 1.33x | 18.4/22.6/27.6% | 2.0/5.1% | 3 |
| 600 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.986 | 0.987 | 0.000 | 1.33x | 18.3/22.6/27.6% | 2.0/5.1% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.865 | 0.858 | 0.007 | - | - | 0.984 | 0.986 | 0.000 | 1.34x | 18.6/22.8/27.8% | 2.0/5.1% | 3 |
| 30 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 120 | 1 | 0.866 | 0.858 | 0.008 | - | - | 0.985 | 0.987 | 0.000 | 1.33x | 18.4/22.6/27.6% | 2.0/5.1% | 3 |
| 600 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.986 | 0.987 | 0.000 | 1.33x | 18.3/22.6/27.6% | 2.0/5.1% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.541 | 0.906 | 0.000 | 1.34x | 18.2/23.1/27.7% | 2.0/5.1% | 3 |
| routers | 1 | 0.870 | 0.865 | 0.005 | - | - | 0.986 | 0.987 | 0.000 | 1.31x | 18.0/22.6/27.5% | 1.9/5.0% | 3 |
| alternate-routers | 1 | 0.868 | 0.863 | 0.005 | - | - | 0.986 | 0.987 | 0.000 | 1.33x | 18.2/22.9/27.7% | 1.9/5.1% | 3 |
| beside-router | 1 | 0.875 | 0.864 | 0.011 | - | - | 0.985 | 0.989 | 0.000 | 1.33x | 18.0/23.0/27.9% | 1.9/5.0% | 3 |
| random-clients | 1 | 0.869 | 0.860 | 0.009 | - | - | 0.980 | 0.982 | 0.000 | 1.33x | 18.3/22.7/27.6% | 2.0/5.1% | 3 |
| hops-apart | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

> place=spread: decode_failures 13

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.541 | 0.906 | 0.000 | 1.34x | 18.2/23.1/27.7% | 2.0/5.1% | 3 |
| routers | 1 | 0.870 | 0.865 | 0.005 | - | - | 0.986 | 0.987 | 0.000 | 1.31x | 18.0/22.6/27.5% | 1.9/5.0% | 3 |
| alternate-routers | 1 | 0.868 | 0.863 | 0.005 | - | - | 0.986 | 0.987 | 0.000 | 1.33x | 18.2/22.9/27.7% | 1.9/5.1% | 3 |
| beside-router | 1 | 0.875 | 0.864 | 0.011 | - | - | 0.985 | 0.989 | 0.000 | 1.33x | 18.0/23.0/27.9% | 1.9/5.0% | 3 |
| random-clients | 1 | 0.869 | 0.860 | 0.009 | - | - | 0.980 | 0.982 | 0.000 | 1.33x | 18.3/22.7/27.6% | 2.0/5.1% | 3 |
| hops-apart | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

> place=spread: decode_failures 13

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| broadcast | 1 | 0.894 | 0.858 | 0.036 | - | - | 0.983 | 0.987 | 0.000 | 1.42x | 19.6/23.9/29.0% | 2.1/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| heard | 1 | 0.871 | 0.864 | 0.007 | - | - | 0.985 | 0.990 | 0.000 | 1.34x | 18.4/22.7/27.6% | 2.0/5.1% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.894 | 0.858 | 0.036 | - | - | 0.983 | 0.987 | 0.000 | 1.42x | 19.6/23.9/29.0% | 2.1/5.4% | 3 |
| heard | 1 | 0.892 | 0.855 | 0.036 | - | - | 0.987 | 0.990 | 0.000 | 1.41x | 19.5/23.5/28.7% | 2.1/5.3% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| enum | 1 | 0.869 | 0.861 | 0.009 | - | - | 0.989 | 0.991 | 0.000 | 1.33x | 18.3/22.5/27.5% | 2.0/5.1% | 3 |
| hybrid | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.870 | 0.865 | 0.005 | - | - | 0.986 | 0.987 | 0.000 | 1.31x | 18.0/22.6/27.5% | 1.9/5.0% | 3 |
| 6 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.976 | 0.976 | 0.000 | 1.37x | 18.7/23.8/28.7% | 2.0/5.3% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.873 | 0.869 | 0.004 | - | - | 0.984 | 0.984 | 0.000 | 1.32x | 18.2/22.6/27.5% | 1.9/5.0% | 2 |
| 3 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 5 | 1 | 0.872 | 0.858 | 0.013 | - | - | 0.992 | 0.994 | 0.000 | 1.38x | 19.0/23.3/28.4% | 2.1/5.2% | 5 |
| 8 | 1 | 0.867 | 0.850 | 0.017 | - | - | 0.992 | 0.995 | 0.000 | 1.40x | 19.4/23.9/29.0% | 2.1/5.3% | 8 |

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.873 | 0.869 | 0.004 | - | - | 0.984 | 0.984 | 0.000 | 1.32x | 18.2/22.6/27.5% | 1.9/5.0% | 2 |
| 3 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 5 | 1 | 0.872 | 0.858 | 0.013 | - | - | 0.992 | 0.994 | 0.000 | 1.38x | 19.0/23.3/28.4% | 2.1/5.2% | 5 |
| 8 | 1 | 0.867 | 0.850 | 0.017 | - | - | 0.992 | 0.995 | 0.000 | 1.40x | 19.4/23.9/29.0% | 2.1/5.3% | 8 |

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| True | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.869 | 0.861 | 0.008 | - | - | 0.988 | 0.989 | 0.000 | 1.26x | 17.3/21.3/26.0% | 1.9/4.7% | 3 |
| 1 | 1 | 0.870 | 0.861 | 0.009 | - | - | 0.988 | 0.990 | 0.000 | 1.25x | 17.2/21.2/25.9% | 1.8/4.7% | 3 |
| 2 | 1 | 0.873 | 0.866 | 0.007 | - | - | 0.993 | 0.994 | 0.000 | 1.24x | 17.2/21.1/25.6% | 1.9/4.7% | 3 |
| 4 | 1 | 0.873 | 0.866 | 0.007 | - | - | 0.993 | 0.994 | 0.000 | 1.24x | 17.2/21.1/25.6% | 1.9/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.871 | 0.862 | 0.008 | - | - | 0.989 | 0.992 | 0.000 | 1.34x | 18.5/23.1/28.0% | 2.0/5.1% | 3 |
| 24 | 1 | 0.871 | 0.864 | 0.007 | - | - | 0.988 | 0.991 | 0.000 | 1.34x | 18.5/22.8/27.7% | 2.0/5.1% | 3 |
| 32 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.988 | 0.991 | 0.000 | 1.35x | 18.7/22.9/28.0% | 2.0/5.1% | 3 |
| 64 | 1 | 0.868 | 0.861 | 0.007 | - | - | 0.987 | 0.988 | 0.000 | 1.34x | 18.5/22.8/27.7% | 2.0/5.1% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.865 | 0.858 | 0.007 | - | - | 0.988 | 0.989 | 0.000 | 1.46x | 19.9/24.5/29.8% | 2.2/5.5% | 3 |
| 16 | 1 | 0.867 | 0.860 | 0.007 | - | - | 0.983 | 0.983 | 0.000 | 1.37x | 18.8/23.3/28.2% | 2.1/5.2% | 3 |
| 32 | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.985 | 0.988 | 0.000 | 1.32x | 18.1/22.5/27.4% | 2.0/5.0% | 3 |

> window-size=8: misdecodes 136

> window-size=16: misdecodes 58

> window-size=32: misdecodes 20

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.961 | 0.002 | - | - | 0.994 | 0.994 | 0.836 | 1.92x | 23.2/32.5/37.2% | 1.3/5.0% | 3 |
| True | 1 | 0.725 | 0.719 | 0.006 | - | - | 0.827 | 0.850 | 0.519 | 5.49x | 59.9/72.6/75.9% | 3.8/12.5% | 3 |

> no-congestion-scaling=True: decode_failures 56

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.482 | 0.478 | 0.004 | - | - | 0.412 | 0.413 | 0.066 | 4.17x | 15.7/23.5/31.0% | 1.4/4.6% | 3 |
| truesize | 1 | 0.512 | 0.508 | 0.004 | - | - | 0.446 | 0.447 | 0.075 | 2.99x | 11.5/17.0/22.9% | 1.0/3.3% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.967 | 0.965 | 0.002 | - | - | 0.998 | 0.998 | 0.853 | 1.82x | 21.8/30.6/35.3% | 1.2/4.8% | 3 |
| adaptive | 1 | 0.964 | 0.961 | 0.002 | - | - | 0.994 | 0.994 | 0.836 | 1.92x | 23.2/32.5/37.2% | 1.3/5.0% | 3 |

