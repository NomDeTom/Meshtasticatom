# Sweep blocks-2026-08-31-3116302

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 3116302 · seeds 3116302
- **blocks** 87 run
- **compute** 10.1 h of simulator time across every cell
- **generated** 2026-08-31T09:55:24+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>71 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 2
- AD-siting: siting-mix=local-typical: decode_failures 6
- AD-worst: role-placement=degree: decode_failures 18
- AD-worst: role-placement=inverse: decode_failures 14
- BL-control: protocol=sr: decode_failures 23
- BL-control: slower: 5.11 s per simulated hour against 1.72 over 10 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 18
- DB-hotstore-stress: faster: 11.9 s per simulated hour against 23.9 over 10 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DB-warm: warm-num-nodes=0: decode_failures 75
- DB-warm: warm-num-nodes=25: decode_failures 75
- DB-warm: warm-num-nodes=100: decode_failures 75
- DB-warm: warm-num-nodes=2000: decode_failures 75
- DG-burst: burst-loss=0.2: decode_failures 5
- DG-burst: burst-loss=0.3: decode_failures 40
- DG-outage: burst-loss=0.1: decode_failures 13
- DG-outage: burst-loss=0.2: decode_failures 14
- DG-outage: burst-loss=0.3: decode_failures 40
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 3
- LD-chatty: broadcast-interval-s=300: decode_failures 34
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 75
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 56
- MS-hopscale: nodes=500: decode_failures 142
- MS-oversubscribed: nodes=500: decode_failures 95
- MS-siting: siting-mix=event: decode_failures 23
- MS-siting: slower: 3.4 s per simulated hour against 1.5 over 10 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.25: decode_failures 2
- MS-stretch: stretch=1.5: decode_failures 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 2
- RF-eu-presets: preset=SHORT_FAST: decode_failures 12
- RF-preset: preset=SHORT_FAST: decode_failures 12
- RF-preset: preset=LONG_MODERATE: decode_failures 2
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 1
- RF-txpower: tx-power=17: decode_failures 5
- RF-txpower: tx-power=14: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 44
- SF-bucket-mode: bucket-mode=time: misdecodes 24
- SF-bucket-mode: bucket-mode=window: misdecodes 22
- SF-bucket-time: time-bucket-s=600: misdecodes 140
- SF-bucket-time: time-bucket-s=1800: misdecodes 24
- SF-bucket-time: time-bucket-s=3600: misdecodes 6
- SF-cadence: trigger=interval: misdecodes 6
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=bucket+interval: misdecodes 13
- SF-capacity-local: capacity=4: decode_failures 110
- SF-capacity-local: capacity=8: decode_failures 62
- SF-capacity: capacity=4: decode_failures 110
- SF-capacity: capacity=8: decode_failures 62
- SF-capacity-window: capacity=8: misdecodes 32
- SF-capacity-window: capacity=8: decode_failures 57
- SF-capacity-window: capacity=16: misdecodes 39
- SF-capacity-window: capacity=32: misdecodes 22
- SF-catchup: catch-up-hours=: misdecodes 13
- SF-catchup: catch-up-hours=02-06: decode_failures 40
- SF-catchup: catch-up-hours=00-08: decode_failures 40
- SF-hops-flat: hops-apart=3: decode_failures 23
- SF-hops-flat: hops-apart=4: decode_failures 37
- SF-hops-spread: hops-apart=3: decode_failures 23
- SF-hops-spread: hops-apart=4: decode_failures 37
- SF-hops-spread: hops-apart=5: decode_failures 37
- SF-place-flat: place=spread: decode_failures 25
- SF-place-spread: place=spread: decode_failures 25
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 17
- SF-replay-order: replay-ordering=heard: misdecodes 27
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-window-size: window-size=8: misdecodes 176
- SF-window-size: window-size=16: misdecodes 72
- SF-window-size: window-size=32: misdecodes 22
- TH-congestion: no-congestion-scaling=True: decode_failures 22

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 5.11 | 1.72 | 2.97x | 10 |
| `MS-siting` | 3.4 | 1.5 | 2.27x | 10 |
| `AD-worst` | 7.14 | 3.77 | 1.89x | 10 |
| `SF-hops-spread` | 7.38 | 4.53 | 1.63x | 10 |
| `SF-provide-transport` | 2.96 | 1.93 | 1.53x | 10 |
| `AD-badrouters` | 1.57 | 2.42 | 0.65x | 10 |
| `TH-congestion` | 10.1 | 19.9 | 0.51x | 10 |
| `TH-congestion-input` | 6.26 | 12.4 | 0.51x | 10 |
| `DB-hotstore-stress` | 11.9 | 23.9 | 0.50x | 10 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.964 | 0.964 | 0.803 → 0.826 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.944 | 0.944 | 0.815 → 0.826 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.067 → 0.964 | 0.897 | 0.059 → 0.824 | 18x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.153 → 0.964 | 0.811 | 0.086 → 0.824 | 9.2x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.111 → 0.900 | 0.789 | 0.098 → 0.755 | 1.1e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.111 → 0.828 | 0.716 | 0.109 → 0.824 | 3.1x sr_bytes | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.074 → 0.789 | 0.716 | 0.072 → 0.782 | 4.1x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.254 → 0.969 | 0.715 | 0.245 → 0.963 | 2.4x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.185 → 0.828 | 0.643 | 0.182 → 0.824 | 11x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.351 → 0.964 | 0.613 | 0.272 → 0.824 | 4.5x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.351 → 0.964 | 0.613 | 0.272 → 0.824 | 5.8x sr_airtime | up | 3 |
| `RF-bw500` | preset | **text** | 0.145 → 0.705 | 0.560 | 0.143 → 0.695 | 2.4x advert_bytes | up | 3 |
| `MS-topology` | topology | **text** | 0.456 → 0.945 | 0.490 | 0.446 → 0.944 | 2.8x sr_airtime | up | 4 |
| `MS-size` | nodes | **held** | 0.528 → 0.964 | 0.436 | 0.420 → 0.824 | 2.9x advert_bytes | down | 5 |
| `MS-oversubscribed` | nodes | **held** | 0.366 → 0.800 | 0.434 | 0.181 → 0.523 | 4.5x sr_bytes | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.333 → 0.705 | 0.372 | 0.318 → 0.683 | 1.6x sr_airtime | up | 2 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.554 → 0.896 | 0.342 | 0.540 → 0.895 | 9.3x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.495 → 0.828 | 0.333 | 0.475 → 0.824 | 2.3x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.539 → 0.854 | 0.315 | 0.521 → 0.851 | 7.5x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.527 → 0.828 | 0.300 | 0.496 → 0.824 | 2.3x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.623 → 0.896 | 0.273 | 0.595 → 0.895 | 2x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.623 → 0.872 | 0.249 | 0.595 → 0.870 | 1.9x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.662 → 0.890 | 0.228 | 0.644 → 0.882 | 4.2x sr_airtime | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.742 → 0.964 | 0.222 | 0.815 → 0.824 | 2.2x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.742 → 0.964 | 0.222 | 0.815 → 0.824 | 3.2x sr_bytes | down | 5 |
| `MS-density` | nodes | **text** | 0.685 → 0.892 | 0.208 | 0.677 → 0.886 | 5.2x sr_airtime | up | 5 |
| `RT-spread` | hop-spread | **text** | 0.623 → 0.828 | 0.205 | 0.595 → 0.824 | 1.4x sr_bytes | up | 2 |
| `SF-place-flat` | place | **held** | 0.790 → 0.976 | 0.185 | 0.811 → 0.826 | 2.5x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.790 → 0.976 | 0.185 | 0.811 → 0.826 | 2.5x sr_bytes | up | 6 |
| `RF-noise` | noise-profile | **held** | 0.784 → 0.964 | 0.180 | 0.643 → 0.824 | 1.3x sr_airtime | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.673 → 0.828 | 0.154 | 0.659 → 0.824 | 1.4x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.761 → 0.875 | 0.113 | 0.755 → 0.873 | 2.2x sr_airtime | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.828 → 0.940 | 0.112 | 0.824 → 0.936 | 1.6x sr_bytes | up | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.332 → 0.443 | 0.111 | 0.234 → 0.339 | 3.8x sr_airtime | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.717 → 0.828 | 0.111 | 0.717 → 0.824 | 1.2x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.828 → 0.935 | 0.108 | 0.824 → 0.934 | 1.3x bytes_on_air | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.769 → 0.875 | 0.105 | 0.763 → 0.873 | 2.2x sr_airtime | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.773 → 0.875 | 0.101 | 0.766 → 0.872 | 5.2x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.789 → 0.879 | 0.090 | 0.782 → 0.877 | 2.1x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.789 → 0.879 | 0.090 | 0.782 → 0.877 | 2.1x bytes_on_air | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.828 → 0.914 | 0.087 | 0.824 → 0.908 | 1.3x bytes_on_air | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.764 → 0.834 | 0.070 | 0.758 → 0.828 | 2.2x bytes_on_air | down | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.894 → 0.964 | 0.070 | 0.823 → 0.824 | 28x sr_airtime | down | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.762 → 0.832 | 0.070 | 0.755 → 0.825 | 2.3x bytes_on_air | down | 4 |
| `SF-cadence` | trigger | **held** | 0.904 → 0.964 | 0.060 | 0.795 → 0.824 | 13x advert_bytes | down | 4 |
| `AD-badrouters` | role-placement | **text** | 0.734 → 0.789 | 0.055 | 0.720 → 0.782 | 1.6x sr_bytes | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.612 → 0.662 | 0.050 | 0.597 → 0.646 | 1.2x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.828 → 0.874 | 0.046 | 0.824 → 0.871 | 3.2x bytes_on_air | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.783 → 0.828 | 0.045 | 0.775 → 0.824 | 1.5x sr_airtime | down | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.834 → 0.870 | 0.036 | 0.829 → 0.866 | 1.1x bytes_on_air | up | 2 |
| `FW-versions` | profile | **text** | 0.828 → 0.863 | 0.035 | 0.824 → 0.857 | 3.4x bytes_on_air | down | 5 |
| `MS-roles` | role-mix | **text** | 0.789 → 0.824 | 0.034 | 0.782 → 0.818 | 1.1x bytes_on_air | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.796 → 0.828 | 0.032 | 0.783 → 0.824 | 1.1x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.340 → 0.370 | 0.029 | 0.337 → 0.366 | 1.7x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.802 → 0.830 | 0.027 | 0.795 → 0.827 | 9.3x advert_bytes | up | 3 |
| `AD-worst` | role-placement | **held** | 0.786 → 0.813 | 0.027 | 0.692 → 0.721 | 1.1x sr_bytes | down | 2 |
| `DM-mode` | dm-mode | **text** | 0.773 → 0.797 | 0.024 | 0.773 → 0.797 | 1.3x sr_airtime | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.828 → 0.848 | 0.020 | 0.824 → 0.845 | 1.3x bytes_on_air | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.828 → 0.848 | 0.020 | 0.818 → 0.824 | 3x sr_airtime | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.957 → 0.976 | 0.019 | 0.814 → 0.824 | 5.4x advert_bytes | up | 3 |
| `SF-window-size` | window-size | **held** | 0.956 → 0.974 | 0.018 | 0.810 → 0.826 | 5.3x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.876 → 0.890 | 0.014 | 0.866 → 0.882 | 1.2x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.963 → 0.976 | 0.013 | 0.819 → 0.824 | 2.9x advert_bytes | up | 4 |
| `FW-firmware` | profile | **text** | 0.828 → 0.840 | 0.012 | 0.824 → 0.832 | 3.4x bytes_on_air | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.953 → 0.965 | 0.012 | 0.821 → 0.828 | 1.8x advert_bytes | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.828 → 0.839 | 0.011 | 0.824 → 0.833 | 1.3x sr_bytes | down | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.844 → 0.854 | 0.010 | 0.840 → 0.849 | 1.2x sr_bytes | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.956 → 0.966 | 0.010 | 0.814 → 0.824 | 7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.956 → 0.966 | 0.010 | 0.814 → 0.824 | 7x sr_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.818 → 0.828 | 0.010 | 0.813 → 0.824 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.818 → 0.828 | 0.010 | 0.813 → 0.824 | 1.1x sr_bytes | up | 4 |
| `SF-capacity` | capacity | **text** | 0.819 → 0.828 | 0.009 | 0.813 → 0.824 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **text** | 0.819 → 0.828 | 0.009 | 0.813 → 0.824 | 5.3x advert_bytes | up | 5 |
| `SF-width` | short-id-bits | **held** | 0.964 → 0.973 | 0.009 | 0.816 → 0.824 | 3.1x advert_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.819 → 0.828 | 0.009 | 0.813 → 0.824 | 3x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.821 → 0.828 | 0.007 | 0.816 → 0.824 | 1.2x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.951 → 0.957 | 0.006 | 0.795 → 0.799 | 1.1x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.828 → 0.833 | 0.005 | 0.824 → 0.828 | 1x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.960 → 0.965 | 0.005 | 0.821 → 0.826 | 2.6x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.952 → 0.957 | 0.005 | 0.797 → 0.799 | 1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.844 → 0.848 | 0.004 | 0.812 → 0.818 | 1x sr_airtime | down | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.823 → 0.827 | 0.004 | 0.818 → 0.822 | 1.1x sr_bytes | up | 4 |
| `SF-resolve` | resolve | **text** | 0.825 → 0.828 | 0.003 | 0.820 → 0.824 | 5.7x advert_bytes | = | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.890 → 0.892 | 0.002 | 0.882 → 0.885 | 1x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.955 → 0.957 | 0.002 | 0.879 → 0.882 | 1.1x sr_bytes | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario flat`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| sprinkled | 1 | 0.844 | 0.834 | 0.010 | - | - | 0.969 | 0.970 | 0.575 | 1.29x | 15.7/21.7/24.4% | 2.1/5.2% | 3 |
| arms-race | 1 | 0.935 | 0.934 | 0.002 | - | - | 0.985 | 0.986 | 0.715 | 1.08x | 19.5/25.9/27.8% | 1.2/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.870 | 0.860 | 0.010 | - | - | 0.953 | 0.954 | 0.644 | 1.29x | 15.8/24.2/28.0% | 2.0/5.5% | 3 |
| 0.3 | 1 | 0.940 | 0.936 | 0.003 | - | - | 0.998 | 0.999 | 0.722 | 1.09x | 20.3/27.0/30.0% | 1.5/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.789 | 0.782 | 0.007 | - | - | 0.950 | 0.951 | 0.313 | 1.23x | 13.6/25.1/29.8% | 1.9/5.6% | 3 |
| inverse | 1 | 0.756 | 0.732 | 0.024 | - | - | 0.932 | 0.947 | 0.253 | 1.20x | 12.5/17.8/20.7% | 2.2/3.7% | 3 |
| random | 1 | 0.734 | 0.720 | 0.015 | - | - | 0.898 | 0.902 | 0.250 | 1.25x | 13.0/20.9/25.5% | 2.2/5.0% | 3 |

> role-placement=inverse: decode_failures 2

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.789 | 0.782 | 0.007 | - | - | 0.950 | 0.951 | 0.313 | 1.23x | 13.6/25.1/29.8% | 1.9/5.6% | 3 |
| all-routers | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.970 | 0.971 | 0.576 | 2.57x | 25.7/36.7/42.6% | 4.3/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.789 | 0.782 | 0.007 | - | - | 0.950 | 0.951 | 0.313 | 1.23x | 13.6/25.1/29.8% | 1.9/5.6% | 3 |
| no-mute | 1 | 0.805 | 0.800 | 0.005 | - | - | 0.960 | 0.960 | 0.331 | 1.35x | 14.6/23.0/26.3% | 2.0/5.4% | 3 |
| all-routers | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.970 | 0.971 | 0.576 | 2.57x | 25.7/36.7/42.6% | 4.3/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.789 | 0.782 | 0.007 | - | - | 0.950 | 0.951 | 0.313 | 1.23x | 13.6/25.1/29.8% | 1.9/5.6% | 3 |
| local-typical | 1 | 0.522 | 0.518 | 0.004 | - | - | 0.673 | 0.762 | 0.000 | 1.20x | 9.1/18.5/28.5% | 1.8/5.1% | 3 |
| basement-heavy | 1 | 0.074 | 0.072 | 0.002 | - | - | 0.238 | 0.239 | 0.000 | 0.58x | 0.4/8.0/12.8% | 0.3/3.2% | 3 |

> siting-mix=local-typical: decode_failures 6

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.727 | 0.721 | 0.006 | - | - | 0.813 | 0.925 | 0.000 | 2.36x | 14.0/24.8/31.4% | 1.9/5.5% | 3 |
| inverse | 1 | 0.701 | 0.692 | 0.009 | - | - | 0.786 | 0.912 | 0.000 | 2.29x | 12.6/23.0/29.5% | 1.9/3.2% | 3 |

> role-placement=degree: decode_failures 18

> role-placement=inverse: decode_failures 14

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.826 | 0.826 | 0.000 | - | - | 0 | 0.000 | 0.324 | 1.37x | 15.1/23.9/28.3% | 1.9/5.2% | 3 |
| sr | 1 | 0.836 | 0.815 | 0.021 | - | - | 0.944 | 0.977 | 0.326 | 1.42x | 15.4/24.7/29.2% | 2.0/5.5% | 3 |

> protocol=sr: decode_failures 23

> slower: 5.11 s per simulated hour against 1.72 over 10 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.769 | 0.763 | 0.006 | - | - | 0.900 | 0.901 | 0.476 | 3.23x | 35.2/52.1/62.0% | 5.0/9.6% | 3 |
| 100 | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.966 | 0.966 | 0.558 | 1.71x | 19.0/28.8/35.1% | 2.6/5.3% | 3 |
| 120 | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.966 | 0.966 | 0.558 | 1.71x | 19.0/28.8/35.1% | 2.6/5.3% | 3 |
| 250 | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.966 | 0.966 | 0.558 | 1.71x | 19.0/28.8/35.1% | 2.6/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.237 | 0.234 | 0.003 | - | - | 0.332 | 0.345 | 0.079 | 10.47x | 27.5/39.9/54.8% | 3.8/9.8% | 3 |
| 120 | 1 | 0.340 | 0.337 | 0.003 | - | - | 0.443 | 0.444 | 0.094 | 4.49x | 11.7/17.3/25.0% | 1.6/4.3% | 3 |
| 250 | 1 | 0.342 | 0.339 | 0.003 | - | - | 0.438 | 0.439 | 0.097 | 4.47x | 11.7/17.1/24.7% | 1.6/4.3% | 3 |

> max-num-nodes=10: decode_failures 18

> faster: 11.9 s per simulated hour against 23.9 over 10 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.966 | 0.966 | 0.558 | 1.71x | 19.0/28.8/35.1% | 2.6/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.966 | 0.966 | 0.558 | 1.71x | 19.0/28.8/35.1% | 2.6/5.3% | 3 |
| constrained | 1 | 0.761 | 0.755 | 0.007 | - | - | 0.889 | 0.889 | 0.469 | 3.22x | 35.2/52.2/62.0% | 4.9/9.6% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.662 | 0.646 | 0.016 | - | - | 0.768 | 0.775 | 0.476 | 5.66x | 47.2/63.3/69.5% | 3.9/11.2% | 3 |
| 25 | 1 | 0.662 | 0.646 | 0.016 | - | - | 0.768 | 0.775 | 0.476 | 5.66x | 47.2/63.3/69.5% | 3.9/11.2% | 3 |
| 100 | 1 | 0.662 | 0.646 | 0.016 | - | - | 0.768 | 0.775 | 0.476 | 5.66x | 47.2/63.3/69.5% | 3.9/11.2% | 3 |
| 2000 | 1 | 0.662 | 0.646 | 0.016 | - | - | 0.768 | 0.775 | 0.476 | 5.66x | 47.2/63.3/69.5% | 3.9/11.2% | 3 |

> warm-num-nodes=0: decode_failures 75

> warm-num-nodes=25: decode_failures 75

> warm-num-nodes=100: decode_failures 75

> warm-num-nodes=2000: decode_failures 75

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.729 | 0.715 | 0.014 | - | - | 0.941 | 0.942 | 0.291 | 1.32x | 14.7/23.6/27.9% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.631 | 0.606 | 0.024 | - | - | 0.889 | 0.896 | 0.242 | 1.22x | 13.7/22.2/26.8% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.527 | 0.496 | 0.031 | - | - | 0.795 | 0.830 | 0.216 | 1.09x | 12.1/20.3/24.6% | 1.6/3.9% | 3 |

> burst-loss=0.2: decode_failures 5

> burst-loss=0.3: decode_failures 40

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.790 | 0.783 | 0.007 | - | - | 0.966 | 0.966 | 0.314 | 1.42x | 15.7/25.2/29.7% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.739 | 0.727 | 0.012 | - | - | 0.937 | 0.937 | 0.296 | 1.44x | 15.8/25.8/30.5% | 2.1/5.2% | 3 |
| 0.3 | 1 | 0.673 | 0.659 | 0.015 | - | - | 0.894 | 0.896 | 0.266 | 1.43x | 15.7/26.0/31.2% | 2.1/5.1% | 3 |

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.722 | 0.708 | 0.014 | - | - | 0.933 | 0.944 | 0.283 | 1.32x | 14.7/23.6/27.9% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.612 | 0.596 | 0.016 | - | - | 0.831 | 0.879 | 0.249 | 1.22x | 13.6/22.4/26.5% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.495 | 0.475 | 0.019 | - | - | 0.785 | 0.831 | 0.183 | 1.13x | 12.6/21.2/25.7% | 1.6/4.6% | 3 |

> burst-loss=0.1: decode_failures 13

> burst-loss=0.2: decode_failures 14

> burst-loss=0.3: decode_failures 40

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.773 | 0.773 | 0.000 | - | - | 0.935 | 0.937 | 0.305 | 1.84x | 20.2/32.5/38.0% | 2.5/6.9% | 3 |
| directed-with-late-flood | 1 | 0.797 | 0.797 | 0.000 | - | - | 0.952 | 0.955 | 0.318 | 1.67x | 18.5/29.7/34.7% | 2.3/6.5% | 3 |
| m4-early-flood | 1 | 0.796 | 0.796 | 0.000 | - | - | 0.951 | 0.955 | 0.307 | 1.68x | 18.7/29.8/35.0% | 2.3/6.5% | 3 |

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.840 | 0.832 | 0.008 | - | - | 0.973 | 0.977 | 0.517 | 0.75x | 7.8/10.7/13.5% | 1.1/2.2% | 3 |
| 2.8 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.771 | 0.766 | 0.005 | - | - | 0.928 | 0.928 | 0.360 | 1.25x | 13.7/22.8/24.9% | 2.0/4.9% | 3 |
| 0.5 | 1 | 0.834 | 0.828 | 0.006 | - | - | 0.972 | 0.975 | 0.523 | 1.09x | 11.6/16.9/19.2% | 1.7/4.0% | 3 |
| 0.75 | 1 | 0.764 | 0.758 | 0.006 | - | - | 0.971 | 0.971 | 0.340 | 0.88x | 9.4/14.2/14.9% | 1.3/3.5% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.765 | 0.758 | 0.007 | - | - | 0.929 | 0.930 | 0.336 | 1.22x | 13.6/22.0/24.5% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.832 | 0.825 | 0.006 | - | - | 0.975 | 0.977 | 0.509 | 1.08x | 11.7/16.8/19.5% | 1.7/4.0% | 3 |
| 0.75 | 1 | 0.762 | 0.755 | 0.007 | - | - | 0.972 | 0.973 | 0.320 | 0.84x | 9.2/14.0/14.8% | 1.3/3.4% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.874 | 0.871 | 0.003 | - | - | 0.990 | 0.990 | 0.342 | 0.77x | 8.6/14.2/16.8% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.971 | 0.973 | 0.534 | 0.75x | 8.2/11.8/14.7% | 1.1/2.6% | 3 |
| 2.5 | 1 | 0.838 | 0.830 | 0.008 | - | - | 0.969 | 0.972 | 0.505 | 0.78x | 8.5/11.9/14.9% | 1.2/2.7% | 3 |
| 2.6 | 1 | 0.846 | 0.840 | 0.006 | - | - | 0.972 | 0.975 | 0.503 | 0.74x | 8.3/11.8/14.9% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.863 | 0.857 | 0.005 | - | - | 0.971 | 0.972 | 0.518 | 0.73x | 8.4/12.0/14.8% | 1.1/2.8% | 3 |
| 2.8 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.977 | 0.979 | 0.351 | 0.93x | 10.3/16.5/19.1% | 1.3/3.5% | 3 |
| 900 | 1 | 0.773 | 0.766 | 0.007 | - | - | 0.932 | 0.932 | 0.325 | 2.19x | 24.2/38.4/44.9% | 3.0/8.5% | 3 |
| 300 | 1 | 0.539 | 0.521 | 0.018 | - | - | 0.757 | 0.788 | 0.244 | 4.51x | 45.8/69.3/76.9% | 7.0/15.7% | 3 |

> broadcast-interval-s=300: decode_failures 34

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.896 | 0.895 | 0.002 | - | - | 0.970 | 0.972 | 0.354 | 1.04x | 11.2/16.6/19.6% | 1.6/3.5% | 3 |
| 900 | 1 | 0.819 | 0.815 | 0.004 | - | - | 0.925 | 0.926 | 0.341 | 2.53x | 27.3/40.4/46.9% | 3.8/8.6% | 3 |
| 300 | 1 | 0.554 | 0.540 | 0.014 | - | - | 0.756 | 0.763 | 0.236 | 5.03x | 50.1/70.8/77.6% | 8.2/15.8% | 3 |

> broadcast-interval-s=300: decode_failures 3

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.834 | 0.831 | 0.004 | - | - | 0.964 | 0.965 | 0.323 | 1.29x | 14.4/22.8/26.9% | 1.8/5.0% | 3 |
| sinusoid | 1 | 0.839 | 0.833 | 0.005 | - | - | 0.973 | 0.973 | 0.316 | 1.30x | 14.3/22.7/26.6% | 1.8/4.9% | 3 |
| commuter | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.773 | 0.766 | 0.007 | - | - | 0.932 | 0.932 | 0.325 | 2.19x | 24.2/38.4/44.9% | 3.0/8.5% | 3 |
| 3600 | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.977 | 0.979 | 0.351 | 0.93x | 10.3/16.5/19.1% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.868 | 0.865 | 0.002 | - | - | 0.986 | 0.988 | 0.326 | 0.66x | 7.3/11.7/13.5% | 1.0/2.5% | 3 |
| 43200 | 1 | 0.875 | 0.872 | 0.002 | - | - | 0.989 | 0.989 | 0.348 | 0.47x | 5.1/8.3/9.5% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.825 | 0.820 | 0.006 | - | - | 0.969 | 0.970 | 0.341 | 1.46x | 16.1/25.6/30.2% | 2.0/5.7% | 3 |
| 1.0 | 1 | 0.803 | 0.798 | 0.005 | - | - | 0.947 | 0.948 | 0.324 | 1.62x | 18.0/28.5/33.5% | 2.3/6.3% | 3 |
| 4.0 | 1 | 0.783 | 0.775 | 0.008 | - | - | 0.948 | 0.948 | 0.315 | 1.97x | 22.0/35.2/41.9% | 2.7/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.662 | 0.646 | 0.016 | - | - | 0.768 | 0.775 | 0.476 | 5.66x | 47.2/63.3/69.5% | 3.9/11.2% | 3 |
| 1.0 | 1 | 0.612 | 0.597 | 0.015 | - | - | 0.725 | 0.745 | 0.447 | 6.18x | 51.0/66.9/72.9% | 4.3/12.0% | 3 |

> traceroute-per-hour=0.0: decode_failures 75

> traceroute-per-hour=1.0: decode_failures 56

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.685 | 0.677 | 0.008 | - | - | 0.862 | 0.864 | 0.279 | 1.30x | 15.7/24.6/27.9% | 3.1/6.4% | 3 |
| 60 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 90 | 1 | 0.875 | 0.871 | 0.004 | - | - | 0.971 | 0.972 | 0.380 | 1.71x | 15.5/26.0/31.9% | 1.6/4.8% | 3 |
| 120 | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.957 | 0.957 | 0.688 | 2.04x | 18.0/26.2/30.0% | 1.4/5.0% | 3 |
| 150 | 1 | 0.892 | 0.886 | 0.006 | - | - | 0.999 | 0.999 | 0.644 | 2.58x | 22.2/33.0/37.0% | 1.4/5.3% | 3 |

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 120 | 1 | 0.528 | 0.522 | 0.006 | - | - | 0.789 | 0.790 | 0.178 | 2.36x | 12.0/22.1/26.1% | 1.7/5.2% | 3 |
| 250 | 1 | 0.342 | 0.339 | 0.003 | - | - | 0.438 | 0.440 | 0.098 | 4.91x | 13.0/19.0/26.7% | 1.8/4.7% | 3 |
| 500 | 1 | 0.185 | 0.182 | 0.003 | - | - | 0.377 | 0.394 | 0.009 | 9.42x | 12.7/18.8/32.9% | 1.7/5.3% | 3 |

> nodes=500: decode_failures 142

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.528 | 0.523 | 0.006 | - | - | 0.800 | 0.800 | 0.183 | 2.21x | 11.3/20.8/24.9% | 1.5/4.8% | 3 |
| 250 | 1 | 0.340 | 0.337 | 0.003 | - | - | 0.443 | 0.444 | 0.094 | 4.49x | 11.7/17.3/25.0% | 1.6/4.3% | 3 |
| 500 | 1 | 0.183 | 0.181 | 0.003 | - | - | 0.366 | 0.379 | 0.007 | 8.86x | 12.1/17.8/31.0% | 1.6/4.9% | 3 |

> nodes=500: decode_failures 95

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.824 | 0.818 | 0.006 | - | - | 0.971 | 0.972 | 0.323 | 1.39x | 15.5/24.6/28.9% | 1.9/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.789 | 0.782 | 0.007 | - | - | 0.950 | 0.951 | 0.313 | 1.23x | 13.6/25.1/29.8% | 1.9/5.6% | 3 |

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.963 | 0.964 | 0.340 | 1.49x | 16.2/25.3/29.5% | 2.1/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.844 | 0.840 | 0.004 | - | - | 0.961 | 0.961 | 0.364 | 1.37x | 15.6/27.1/32.5% | 2.4/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.05 | 1 | 0.838 | 0.834 | 0.004 | - | - | 0.963 | 0.964 | 0.500 | 1.51x | 16.2/27.0/33.4% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.838 | 0.835 | 0.004 | - | - | 0.965 | 0.966 | 0.494 | 1.61x | 18.3/29.2/35.4% | 2.4/5.3% | 3 |
| 0.2 | 1 | 0.848 | 0.845 | 0.003 | - | - | 0.965 | 0.965 | 0.529 | 1.80x | 18.8/35.7/43.3% | 2.7/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| local-typical | 1 | 0.551 | 0.548 | 0.003 | - | - | 0.802 | 0.802 | 0.000 | 1.40x | 9.4/22.9/31.4% | 2.1/5.3% | 3 |
| event | 1 | 0.254 | 0.245 | 0.009 | - | - | 0.532 | 0.566 | 0.000 | 1.16x | 5.6/16.1/24.0% | 1.5/5.0% | 3 |
| backbone | 1 | 0.969 | 0.963 | 0.006 | - | - | 0.995 | 0.997 | 0.803 | 1.25x | 23.5/35.5/36.8% | 1.8/5.7% | 3 |

> siting-mix=event: decode_failures 23

> slower: 3.4 s per simulated hour against 1.5 over 10 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.784 | 0.771 | 0.014 | - | - | 0.853 | 0.856 | 0.569 | 1.51x | 21.2/35.6/38.2% | 3.7/7.3% | 3 |
| 60 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 90 | 1 | 0.663 | 0.649 | 0.014 | - | - | 0.932 | 0.934 | 0.272 | 1.80x | 12.0/21.5/25.9% | 1.8/4.9% | 3 |
| 120 | 1 | 0.528 | 0.522 | 0.006 | - | - | 0.789 | 0.790 | 0.178 | 2.36x | 12.0/22.1/26.1% | 1.7/5.2% | 3 |
| 150 | 1 | 0.428 | 0.420 | 0.008 | - | - | 0.528 | 0.530 | 0.192 | 2.85x | 12.7/19.1/24.2% | 1.6/4.6% | 3 |

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 1.25 | 1 | 0.544 | 0.531 | 0.013 | - | - | 0.831 | 0.837 | 0.000 | 1.39x | 10.7/18.9/23.1% | 2.2/5.4% | 3 |
| 1.5 | 1 | 0.333 | 0.318 | 0.015 | - | - | 0.662 | 0.665 | 0.000 | 1.25x | 8.1/15.8/20.5% | 1.8/5.1% | 3 |
| 2.0 | 1 | 0.111 | 0.109 | 0.003 | - | - | 0.325 | 0.327 | 0.000 | 0.72x | 3.0/8.6/10.3% | 1.1/3.4% | 3 |

> stretch=1.25: decode_failures 2

> stretch=1.5: decode_failures 1

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| clustered | 1 | 0.887 | 0.882 | 0.004 | - | - | 0.957 | 0.957 | 0.591 | 1.23x | 18.7/28.9/32.0% | 1.8/5.2% | 3 |
| corridor | 1 | 0.456 | 0.446 | 0.009 | - | - | 0.528 | 0.529 | 0.113 | 1.32x | 13.6/17.9/22.0% | 2.1/5.2% | 3 |
| hub | 1 | 0.945 | 0.944 | 0.001 | - | - | 0.989 | 0.989 | 0.776 | 1.28x | 22.6/34.6/35.9% | 1.7/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.797 | 0.797 | 0.000 | - | - | 0.952 | 0.955 | 0.318 | 1.67x | 18.5/29.7/34.7% | 2.3/6.5% | 3 |
| True | 1 | 0.799 | 0.799 | 0.000 | - | - | 0.957 | 0.958 | 0.317 | 1.67x | 18.3/29.7/34.7% | 2.3/6.6% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.799 | 0.799 | 0.000 | - | - | 0.957 | 0.958 | 0.317 | 1.67x | 18.3/29.7/34.7% | 2.3/6.6% | 3 |
| m4-early-flood | 1 | 0.795 | 0.795 | 0.000 | - | - | 0.951 | 0.954 | 0.318 | 1.71x | 18.9/30.4/35.6% | 2.3/6.6% | 3 |

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.826 | 0.826 | 0.000 | - | - | 0 | 0.000 | 0.324 | 1.37x | 15.1/23.9/28.3% | 1.9/5.2% | 3 |
| chain | 1 | 0.806 | 0.803 | 0.003 | - | - | 0.909 | 0.957 | 0.291 | 1.60x | 17.8/28.4/33.1% | 2.2/6.2% | 3 |
| sr | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| True | 1 | 0.833 | 0.828 | 0.005 | - | - | 0.968 | 0.969 | 0.354 | 1.41x | 15.7/24.8/29.0% | 2.0/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.957 | 0.957 | 0.688 | 2.04x | 18.0/26.2/30.0% | 1.4/5.0% | 3 |
| True | 1 | 0.892 | 0.885 | 0.008 | - | - | 0.958 | 0.959 | 0.694 | 2.07x | 18.0/26.2/30.2% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.145 | 0.143 | 0.002 | - | - | 0.396 | 0.397 | 0.000 | 0.04x | 0.1/0.5/0.7% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.377 | 0.361 | 0.015 | - | - | 0.740 | 0.744 | 0.000 | 0.24x | 1.7/3.1/4.3% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.705 | 0.695 | 0.010 | - | - | 0.941 | 0.943 | 0.207 | 1.31x | 10.9/17.5/22.3% | 2.0/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.856 | 0.851 | 0.005 | - | - | 0.970 | 0.970 | 0.443 | 1.29x | 18.4/26.6/30.2% | 1.8/5.4% | 3 |
| 1.0 | 1 | 0.914 | 0.908 | 0.006 | - | - | 0.982 | 0.982 | 0.711 | 1.11x | 25.5/32.1/34.2% | 1.5/5.6% | 3 |

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.274 | 0.272 | 0.002 | - | - | 0.351 | 0.561 | 0.000 | 0.12x | 0.7/1.5/2.1% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| LITE_FAST | 1 | 0.703 | 0.696 | 0.007 | - | - | 0.947 | 0.951 | 0.183 | 1.04x | 9.7/16.6/21.2% | 1.5/4.2% | 3 |
| NARROW_SLOW | 1 | 0.749 | 0.741 | 0.008 | - | - | 0.951 | 0.953 | 0.353 | 1.33x | 12.9/22.7/26.4% | 1.8/5.5% | 3 |

> preset=SHORT_FAST: decode_failures 12

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| temporal | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.906 | 0.907 | 0.145 | 1.37x | 14.8/24.6/28.6% | 2.0/5.4% | 3 |
| transient | 1 | 0.813 | 0.806 | 0.007 | - | - | 0.961 | 0.961 | 0.302 | 1.40x | 15.6/24.8/29.2% | 2.0/5.5% | 3 |
| periodic | 1 | 0.649 | 0.643 | 0.005 | - | - | 0.784 | 0.786 | 0.250 | 1.28x | 14.2/22.8/26.7% | 1.8/4.8% | 3 |

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.274 | 0.272 | 0.002 | - | - | 0.351 | 0.561 | 0.000 | 0.12x | 0.7/1.5/2.1% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| LONG_MODERATE | 1 | 0.785 | 0.769 | 0.016 | - | - | 0.936 | 0.937 | 0.562 | 3.57x | 44.4/66.4/69.6% | 5.4/11.8% | 3 |

> preset=SHORT_FAST: decode_failures 12

> preset=LONG_MODERATE: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.059 | 0.059 | 0.000 | - | - | 0.067 | 0.072 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.145 | 0.143 | 0.002 | - | - | 0.396 | 0.397 | 0.000 | 0.04x | 0.1/0.5/0.7% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| LONG_TURBO | 1 | 0.705 | 0.695 | 0.010 | - | - | 0.941 | 0.943 | 0.207 | 1.31x | 10.9/17.5/22.3% | 2.0/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.819 | 0.813 | 0.006 | - | - | 0.955 | 0.956 | 0.435 | 1.93x | 20.2/30.8/34.8% | 3.0/7.1% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.762 | 0.755 | 0.006 | - | - | 0.900 | 0.901 | 0.278 | 1.37x | 15.4/24.4/28.6% | 1.8/5.2% | 3 |
| 10000 | 1 | 0.649 | 0.643 | 0.005 | - | - | 0.784 | 0.786 | 0.250 | 1.28x | 14.2/22.8/26.7% | 1.8/4.8% | 3 |
| 4000 | 1 | 0.400 | 0.395 | 0.006 | - | - | 0.517 | 0.543 | 0.152 | 1.07x | 12.0/19.7/23.5% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.098 | 0.098 | 0.000 | - | - | 0.111 | 0.178 | 0.035 | 0.71x | 7.8/13.4/16.6% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.333 | 0.318 | 0.015 | - | - | 0.662 | 0.665 | 0.000 | 1.25x | 8.1/15.8/20.5% | 1.8/5.1% | 3 |
| 1.0 | 1 | 0.705 | 0.683 | 0.022 | - | - | 0.860 | 0.860 | 0.521 | 1.03x | 15.4/21.6/23.0% | 1.4/4.9% | 3 |

> duct-per-hour=0.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 22 | 1 | 0.351 | 0.336 | 0.015 | - | - | 0.677 | 0.684 | 0.000 | 1.28x | 8.3/16.1/22.1% | 1.9/5.2% | 3 |
| 17 | 1 | 0.133 | 0.130 | 0.003 | - | - | 0.360 | 0.368 | 0.000 | 0.83x | 3.3/11.4/13.6% | 1.1/4.0% | 3 |
| 14 | 1 | 0.086 | 0.086 | 0.000 | - | - | 0.153 | 0.336 | 0.000 | 0.60x | 1.9/6.5/9.3% | 0.9/3.0% | 3 |

> tx-power=17: decode_failures 5

> tx-power=14: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.957 | 0.957 | 0.688 | 2.04x | 18.0/26.2/30.0% | 1.4/5.0% | 3 |
| True | 1 | 0.876 | 0.866 | 0.010 | - | - | 0.949 | 0.951 | 0.665 | 2.37x | 20.6/29.5/33.9% | 1.6/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.834 | 0.829 | 0.005 | - | - | 0.959 | 0.960 | 0.502 | 1.49x | 15.9/25.7/32.4% | 2.1/5.3% | 3 |
| True | 1 | 0.870 | 0.866 | 0.004 | - | - | 0.967 | 0.968 | 0.566 | 1.61x | 17.3/26.4/33.2% | 2.6/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| random | 1 | 0.796 | 0.783 | 0.013 | - | - | 0.951 | 0.952 | 0.305 | 1.39x | 15.2/24.2/28.3% | 1.9/5.4% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.623 | 0.595 | 0.028 | - | - | 0.885 | 0.888 | 0.186 | 1.07x | 12.4/20.3/25.2% | 1.5/5.0% | 3 |
| 7 | 1 | 0.872 | 0.870 | 0.002 | - | - | 0.958 | 0.959 | 0.360 | 1.53x | 16.7/25.0/29.2% | 2.3/5.3% | 3 |
| 15 | 1 | 0.896 | 0.895 | 0.001 | - | - | 0.954 | 0.954 | 0.381 | 1.57x | 17.1/25.4/29.5% | 2.4/5.3% | 3 |
| 32 | 1 | 0.895 | 0.894 | 0.001 | - | - | 0.953 | 0.954 | 0.360 | 1.56x | 16.9/25.2/29.4% | 2.4/5.3% | 3 |

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.623 | 0.595 | 0.028 | - | - | 0.885 | 0.888 | 0.186 | 1.07x | 12.4/20.3/25.2% | 1.5/5.0% | 3 |
| 5 | 1 | 0.794 | 0.786 | 0.009 | - | - | 0.938 | 0.941 | 0.282 | 1.37x | 14.9/23.6/27.8% | 1.9/5.2% | 3 |
| 7 | 1 | 0.872 | 0.870 | 0.002 | - | - | 0.958 | 0.959 | 0.360 | 1.53x | 16.7/25.0/29.2% | 2.3/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.823 | 0.823 | 0.000 | - | - | 0.894 | 0.966 | 0.331 | 1.38x | 15.2/24.1/28.5% | 1.9/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.623 | 0.595 | 0.028 | - | - | 0.885 | 0.888 | 0.186 | 1.07x | 12.4/20.3/25.2% | 1.5/5.0% | 3 |
| True | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| BALANCED | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| STRICT | 1 | 0.717 | 0.717 | 0.000 | - | - | 0.867 | 0.868 | 0.182 | 1.51x | 16.8/26.7/31.3% | 2.1/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| dm | 1 | 0.819 | 0.813 | 0.006 | - | - | 0.965 | 0.965 | 0.331 | 1.38x | 15.3/24.5/28.9% | 1.9/5.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.824 | 0.819 | 0.005 | - | - | 0.963 | 0.965 | 0.324 | 1.43x | 15.9/25.2/29.4% | 2.0/5.5% | 3 |
| local | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| time | 1 | 0.830 | 0.824 | 0.006 | - | - | 0.976 | 0.977 | 0.324 | 1.43x | 15.9/25.2/29.5% | 2.0/5.6% | 3 |
| window | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.963 | 0.964 | 0.337 | 1.39x | 15.4/24.5/28.8% | 1.9/5.3% | 3 |

> bucket-mode=global: misdecodes 44

> bucket-mode=time: misdecodes 24

> bucket-mode=window: misdecodes 22

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.820 | 0.814 | 0.006 | - | - | 0.957 | 0.960 | 0.332 | 1.56x | 17.1/27.5/32.1% | 2.2/6.1% | 3 |
| 1800 | 1 | 0.830 | 0.824 | 0.006 | - | - | 0.976 | 0.977 | 0.324 | 1.43x | 15.9/25.2/29.5% | 2.0/5.6% | 3 |
| 3600 | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.964 | 0.967 | 0.330 | 1.41x | 15.7/24.9/29.1% | 2.0/5.4% | 3 |

> time-bucket-s=600: misdecodes 140

> time-bucket-s=1800: misdecodes 24

> time-bucket-s=3600: misdecodes 6

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| interval | 1 | 0.802 | 0.795 | 0.007 | - | - | 0.953 | 0.959 | 0.337 | 1.85x | 20.3/33.0/37.6% | 2.7/7.4% | 3 |
| aimd | 1 | 0.814 | 0.813 | 0.002 | - | - | 0.904 | 0.962 | 0.321 | 1.40x | 15.5/24.6/28.8% | 1.9/5.3% | 3 |
| bucket+interval | 1 | 0.802 | 0.795 | 0.007 | - | - | 0.951 | 0.952 | 0.333 | 1.93x | 21.1/34.3/39.0% | 2.8/7.6% | 3 |

> trigger=interval: misdecodes 6

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 2

> trigger=bucket+interval: misdecodes 13

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.823 | 0.816 | 0.006 | - | - | 0.966 | 0.969 | 0.331 | 1.40x | 15.6/24.8/29.2% | 1.9/5.5% | 3 |
| 8 | 1 | 0.825 | 0.819 | 0.005 | - | - | 0.964 | 0.966 | 0.333 | 1.41x | 15.8/25.0/29.4% | 1.9/5.5% | 3 |
| 16 | 1 | 0.819 | 0.813 | 0.006 | - | - | 0.963 | 0.965 | 0.327 | 1.40x | 15.6/24.7/28.9% | 1.9/5.4% | 3 |
| 32 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 50 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.967 | 0.968 | 0.316 | 1.41x | 15.7/24.8/29.1% | 1.9/5.5% | 3 |

> capacity=4: decode_failures 110

> capacity=8: decode_failures 62

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.823 | 0.816 | 0.006 | - | - | 0.966 | 0.969 | 0.331 | 1.40x | 15.6/24.8/29.2% | 1.9/5.5% | 3 |
| 8 | 1 | 0.825 | 0.819 | 0.005 | - | - | 0.964 | 0.966 | 0.333 | 1.41x | 15.8/25.0/29.4% | 1.9/5.5% | 3 |
| 16 | 1 | 0.819 | 0.813 | 0.006 | - | - | 0.963 | 0.965 | 0.327 | 1.40x | 15.6/24.7/28.9% | 1.9/5.4% | 3 |
| 32 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 50 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.967 | 0.968 | 0.316 | 1.41x | 15.7/24.8/29.1% | 1.9/5.5% | 3 |

> capacity=4: decode_failures 110

> capacity=8: decode_failures 62

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.828 | 0.823 | 0.005 | - | - | 0.953 | 0.974 | 0.325 | 1.39x | 15.4/24.4/28.7% | 1.9/5.3% | 3 |
| 16 | 1 | 0.833 | 0.828 | 0.005 | - | - | 0.965 | 0.967 | 0.327 | 1.39x | 15.4/24.6/28.7% | 1.9/5.3% | 3 |
| 32 | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.963 | 0.964 | 0.337 | 1.39x | 15.4/24.5/28.8% | 1.9/5.3% | 3 |

> capacity=8: misdecodes 32

> capacity=8: decode_failures 57

> capacity=16: misdecodes 39

> capacity=32: misdecodes 22

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.802 | 0.795 | 0.007 | - | - | 0.951 | 0.952 | 0.333 | 1.93x | 21.1/34.3/39.0% | 2.8/7.6% | 3 |
| 02-06 | 1 | 0.830 | 0.827 | 0.003 | - | - | 0.940 | 0.972 | 0.329 | 1.42x | 15.9/25.3/29.5% | 2.0/5.6% | 3 |
| 00-08 | 1 | 0.826 | 0.823 | 0.003 | - | - | 0.933 | 0.967 | 0.336 | 1.51x | 16.7/26.8/31.4% | 2.1/6.0% | 3 |

> catch-up-hours=: misdecodes 13

> catch-up-hours=02-06: decode_failures 40

> catch-up-hours=00-08: decode_failures 40

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.824 | 0.822 | 0.002 | - | - | 0.962 | 0.962 | 0.306 | 1.39x | 15.4/24.3/28.7% | 1.9/5.3% | 3 |
| 2 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 3 | 1 | 0.836 | 0.815 | 0.021 | - | - | 0.944 | 0.977 | 0.326 | 1.42x | 15.4/24.7/29.2% | 2.0/5.5% | 3 |
| 4 | 1 | 0.834 | 0.822 | 0.011 | - | - | 0.742 | 0.972 | 0.320 | 1.40x | 15.4/24.5/28.9% | 2.0/5.4% | 3 |

> hops-apart=3: decode_failures 23

> hops-apart=4: decode_failures 37

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.824 | 0.822 | 0.002 | - | - | 0.962 | 0.962 | 0.306 | 1.39x | 15.4/24.3/28.7% | 1.9/5.3% | 3 |
| 2 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 3 | 1 | 0.836 | 0.815 | 0.021 | - | - | 0.944 | 0.977 | 0.326 | 1.42x | 15.4/24.7/29.2% | 2.0/5.5% | 3 |
| 4 | 1 | 0.834 | 0.822 | 0.011 | - | - | 0.742 | 0.972 | 0.320 | 1.40x | 15.4/24.5/28.9% | 2.0/5.4% | 3 |
| 5 | 1 | 0.844 | 0.818 | 0.026 | - | - | 0.842 | 0.982 | 0.330 | 1.41x | 15.3/24.4/28.8% | 2.0/5.5% | 3 |

> hops-apart=3: decode_failures 23

> hops-apart=4: decode_failures 37

> hops-apart=5: decode_failures 37

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.962 | 0.963 | 0.302 | 1.40x | 15.6/24.6/29.0% | 2.0/5.4% | 3 |
| 30 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 120 | 1 | 0.818 | 0.813 | 0.006 | - | - | 0.962 | 0.962 | 0.314 | 1.42x | 15.7/24.9/29.1% | 2.0/5.5% | 3 |
| 600 | 1 | 0.825 | 0.819 | 0.005 | - | - | 0.965 | 0.966 | 0.330 | 1.41x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.962 | 0.963 | 0.302 | 1.40x | 15.6/24.6/29.0% | 2.0/5.4% | 3 |
| 30 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 120 | 1 | 0.818 | 0.813 | 0.006 | - | - | 0.962 | 0.962 | 0.314 | 1.42x | 15.7/24.9/29.1% | 2.0/5.5% | 3 |
| 600 | 1 | 0.825 | 0.819 | 0.005 | - | - | 0.965 | 0.966 | 0.330 | 1.41x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.833 | 0.819 | 0.014 | - | - | 0.790 | 0.974 | 0.312 | 1.41x | 15.6/24.4/28.6% | 2.0/5.2% | 3 |
| routers | 1 | 0.827 | 0.826 | 0.001 | - | - | 0.960 | 0.960 | 0.333 | 1.40x | 15.5/24.6/28.9% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.822 | 0.820 | 0.002 | - | - | 0.959 | 0.960 | 0.311 | 1.40x | 15.6/24.7/29.0% | 1.9/5.4% | 3 |
| beside-router | 1 | 0.826 | 0.824 | 0.002 | - | - | 0.961 | 0.961 | 0.336 | 1.40x | 15.6/24.7/29.0% | 1.9/5.3% | 3 |
| random-clients | 1 | 0.825 | 0.811 | 0.014 | - | - | 0.976 | 0.978 | 0.328 | 1.43x | 15.8/24.9/29.3% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

> place=spread: decode_failures 25

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.833 | 0.819 | 0.014 | - | - | 0.790 | 0.974 | 0.312 | 1.41x | 15.6/24.4/28.6% | 2.0/5.2% | 3 |
| routers | 1 | 0.827 | 0.826 | 0.001 | - | - | 0.960 | 0.960 | 0.333 | 1.40x | 15.5/24.6/28.9% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.822 | 0.820 | 0.002 | - | - | 0.959 | 0.960 | 0.311 | 1.40x | 15.6/24.7/29.0% | 1.9/5.4% | 3 |
| beside-router | 1 | 0.826 | 0.824 | 0.002 | - | - | 0.961 | 0.961 | 0.336 | 1.40x | 15.6/24.7/29.0% | 1.9/5.3% | 3 |
| random-clients | 1 | 0.825 | 0.811 | 0.014 | - | - | 0.976 | 0.978 | 0.328 | 1.43x | 15.8/24.9/29.3% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

> place=spread: decode_failures 25

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| broadcast | 1 | 0.848 | 0.818 | 0.030 | - | - | 0.959 | 0.961 | 0.383 | 1.52x | 16.8/26.5/30.8% | 2.1/5.7% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| heard | 1 | 0.821 | 0.816 | 0.005 | - | - | 0.961 | 0.961 | 0.333 | 1.41x | 15.7/24.8/29.2% | 2.0/5.5% | 3 |

> replay-ordering=heard: misdecodes 27

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.848 | 0.818 | 0.030 | - | - | 0.959 | 0.961 | 0.383 | 1.52x | 16.8/26.5/30.8% | 2.1/5.7% | 3 |
| heard | 1 | 0.844 | 0.812 | 0.031 | - | - | 0.962 | 0.962 | 0.382 | 1.51x | 16.6/26.3/30.6% | 2.1/5.7% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| enum | 1 | 0.825 | 0.820 | 0.005 | - | - | 0.964 | 0.964 | 0.330 | 1.40x | 15.6/24.8/29.2% | 1.9/5.5% | 3 |
| hybrid | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.827 | 0.826 | 0.001 | - | - | 0.960 | 0.960 | 0.333 | 1.40x | 15.5/24.6/28.9% | 1.9/5.3% | 3 |
| 6 | 1 | 0.825 | 0.821 | 0.004 | - | - | 0.965 | 0.965 | 0.329 | 1.41x | 15.7/25.0/29.4% | 2.0/5.5% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.824 | 0.821 | 0.003 | - | - | 0.956 | 0.956 | 0.329 | 1.39x | 15.5/24.6/28.7% | 1.9/5.4% | 2 |
| 3 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 5 | 1 | 0.823 | 0.815 | 0.007 | - | - | 0.964 | 0.964 | 0.355 | 1.45x | 16.1/25.4/29.8% | 2.0/5.6% | 5 |
| 8 | 1 | 0.824 | 0.814 | 0.009 | - | - | 0.966 | 0.967 | 0.348 | 1.49x | 16.5/26.5/30.7% | 2.0/5.6% | 8 |

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.824 | 0.821 | 0.003 | - | - | 0.956 | 0.956 | 0.329 | 1.39x | 15.5/24.6/28.7% | 1.9/5.4% | 2 |
| 3 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 5 | 1 | 0.823 | 0.815 | 0.007 | - | - | 0.964 | 0.964 | 0.355 | 1.45x | 16.1/25.4/29.8% | 2.0/5.6% | 5 |
| 8 | 1 | 0.824 | 0.814 | 0.009 | - | - | 0.966 | 0.967 | 0.348 | 1.49x | 16.5/26.5/30.7% | 2.0/5.6% | 8 |

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| True | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.823 | 0.818 | 0.005 | - | - | 0.961 | 0.964 | 0.301 | 1.34x | 14.9/23.8/27.9% | 1.9/5.2% | 3 |
| 1 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.964 | 0.966 | 0.334 | 1.32x | 14.6/23.2/27.1% | 1.9/5.1% | 3 |
| 2 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.964 | 0.966 | 0.334 | 1.32x | 14.6/23.2/27.1% | 1.9/5.1% | 3 |
| 4 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.964 | 0.966 | 0.334 | 1.32x | 14.6/23.2/27.1% | 1.9/5.1% | 3 |

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.829 | 0.824 | 0.005 | - | - | 0.973 | 0.973 | 0.345 | 1.39x | 15.4/24.5/28.8% | 1.9/5.4% | 3 |
| 24 | 1 | 0.823 | 0.816 | 0.007 | - | - | 0.972 | 0.973 | 0.351 | 1.40x | 15.6/24.8/29.1% | 1.9/5.5% | 3 |
| 32 | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.964 | 0.965 | 0.337 | 1.40x | 15.7/24.7/29.0% | 2.0/5.4% | 3 |
| 64 | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.967 | 0.968 | 0.323 | 1.40x | 15.5/24.6/28.8% | 1.9/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.816 | 0.810 | 0.006 | - | - | 0.956 | 0.957 | 0.308 | 1.50x | 16.6/26.4/30.9% | 2.0/5.8% | 3 |
| 16 | 1 | 0.831 | 0.826 | 0.005 | - | - | 0.974 | 0.975 | 0.307 | 1.44x | 15.9/25.4/29.6% | 2.0/5.5% | 3 |
| 32 | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.963 | 0.964 | 0.337 | 1.39x | 15.4/24.5/28.8% | 1.9/5.3% | 3 |

> window-size=8: misdecodes 176

> window-size=16: misdecodes 72

> window-size=32: misdecodes 22

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.957 | 0.957 | 0.688 | 2.04x | 18.0/26.2/30.0% | 1.4/5.0% | 3 |
| True | 1 | 0.662 | 0.644 | 0.018 | - | - | 0.783 | 0.786 | 0.477 | 5.63x | 46.9/63.1/69.5% | 3.9/11.3% | 3 |

> no-congestion-scaling=True: decode_failures 22

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.340 | 0.337 | 0.003 | - | - | 0.443 | 0.444 | 0.094 | 4.49x | 11.7/17.3/25.0% | 1.6/4.3% | 3 |
| truesize | 1 | 0.370 | 0.366 | 0.003 | - | - | 0.460 | 0.461 | 0.110 | 2.65x | 7.1/11.1/16.0% | 0.9/2.9% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.889 | 0.879 | 0.010 | - | - | 0.955 | 0.956 | 0.682 | 2.00x | 17.5/25.5/29.3% | 1.3/5.0% | 3 |
| adaptive | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.957 | 0.957 | 0.688 | 2.04x | 18.0/26.2/30.0% | 1.4/5.0% | 3 |

