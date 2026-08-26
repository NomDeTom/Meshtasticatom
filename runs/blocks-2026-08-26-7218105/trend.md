# Sweep blocks-2026-08-26-7218105

- **sim version** `1.4.0`
- **transport** `9692acc`
- **ground** valleys
- **seed base** 7218105 · seeds 7218105
- **blocks** 87 run
- **compute** 10.8 h of simulator time across every cell
- **generated** 2026-08-26T04:42:11+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>73 warnings</summary>

- AD-siting: siting-mix=basement-heavy: decode_failures 3
- DB-hotstore-stress: max-num-nodes=10: decode_failures 45
- DB-hotstore-stress: max-num-nodes=120: decode_failures 87
- DB-hotstore-stress: max-num-nodes=250: decode_failures 96
- DB-warm: warm-num-nodes=0: decode_failures 78
- DB-warm: warm-num-nodes=25: decode_failures 78
- DB-warm: warm-num-nodes=100: decode_failures 78
- DB-warm: warm-num-nodes=2000: decode_failures 78
- DG-burst: burst-loss=0.2: decode_failures 2
- DG-burst: burst-loss=0.3: decode_failures 25
- DG-outage: burst-loss=0.1: decode_failures 31
- DG-outage: burst-loss=0.2: decode_failures 39
- DG-outage: burst-loss=0.3: decode_failures 28
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 5
- LD-chatty: broadcast-interval-s=300: decode_failures 31
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 78
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 12.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 125
- MS-hopscale: nodes=250: decode_failures 158
- MS-hopscale: nodes=500: decode_failures 12
- MS-oversubscribed: nodes=250: decode_failures 87
- MS-oversubscribed: nodes=500: decode_failures 40
- MS-stretch: stretch=1.25: decode_failures 3
- MS-stretch: faster: 1.55 s per simulated hour against 3.48 over 5 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- PR-repeats-busy: extra-repeats=True: misdecodes 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 16
- RF-bw500: preset=LONG_TURBO: decode_failures 1
- RF-duct: duct-per-hour=1.0: misdecodes 1
- RF-eu-presets: preset=LITE_FAST: decode_failures 7
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 1
- RF-preset: preset=LONG_MODERATE: decode_failures 8
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 1
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 23
- RF-stretch-duct: faster: 0.949 s per simulated hour against 3.25 over 5 prior run(s) - 3.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=22: decode_failures 11
- SF-bucket-mode: bucket-mode=global: misdecodes 49
- SF-bucket-mode: bucket-mode=time: misdecodes 33
- SF-bucket-mode: bucket-mode=window: misdecodes 27
- SF-bucket-time: time-bucket-s=600: misdecodes 118
- SF-bucket-time: time-bucket-s=1800: misdecodes 33
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-cadence: trigger=interval: misdecodes 11
- SF-cadence: trigger=aimd: misdecodes 5
- SF-cadence: trigger=bucket+interval: misdecodes 30
- SF-capacity-local: capacity=4: decode_failures 77
- SF-capacity-local: capacity=8: decode_failures 39
- SF-capacity: capacity=4: decode_failures 77
- SF-capacity: capacity=8: decode_failures 39
- SF-capacity-window: capacity=8: misdecodes 49
- SF-capacity-window: capacity=8: decode_failures 8
- SF-capacity-window: capacity=16: misdecodes 31
- SF-capacity-window: capacity=16: decode_failures 2
- SF-capacity-window: capacity=32: misdecodes 27
- SF-catchup: catch-up-hours=: misdecodes 30
- SF-catchup: catch-up-hours=02-06: decode_failures 6
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 3
- SF-hops-flat: hops-apart=4: decode_failures 21
- SF-hops-spread: hops-apart=4: decode_failures 21
- SF-hops-spread: hops-apart=5: decode_failures 16
- SF-place-flat: place=spread: decode_failures 32
- SF-place-flat: place=random-clients: decode_failures 39
- SF-place-spread: place=spread: decode_failures 32
- SF-place-spread: place=random-clients: decode_failures 39
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 17
- SF-replay-order: replay-ordering=heard: misdecodes 7
- SF-window-size: window-size=8: misdecodes 145
- SF-window-size: window-size=16: misdecodes 96
- SF-window-size: window-size=32: misdecodes 27
- TH-congestion-input: congestion-input=hotstore: decode_failures 87
- TH-congestion-input: congestion-input=truesize: decode_failures 101
- TH-congestion-input: slower: 48.8 s per simulated hour against 18.3 over 5 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: decode_failures 101

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 48.8 | 18.3 | 2.66x | 5 |
| `MS-oversubscribed` | 32.8 | 20.1 | 1.63x | 5 |
| `SF-window-size` | 1.2 | 1.8 | 0.67x | 5 |
| `DB-platform` | 2.19 | 3.31 | 0.66x | 5 |
| `MS-siting` | 1.22 | 1.87 | 0.65x | 5 |
| `AD-worst` | 3.1 | 4.84 | 0.64x | 5 |
| `AD-badrouters` | 1.52 | 2.42 | 0.63x | 5 |
| `SF-catchup` | 5.55 | 9.35 | 0.59x | 5 |
| `FW-firmware` | 1.08 | 1.93 | 0.56x | 5 |
| `RT-rebroadcast` | 1.02 | 1.96 | 0.52x | 5 |
| `MS-stretch` | 1.55 | 3.48 | 0.45x | 5 |
| `RF-stretch-duct` | 0.949 | 3.25 | 0.29x | 5 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.984 | 0.984 | 0.837 → 0.853 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.971 | 0.971 | 0.827 → 0.841 | 1.1x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.076 → 0.971 | 0.894 | 0.048 → 0.841 | 31x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.101 → 0.971 | 0.869 | 0.054 → 0.841 | 12x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.106 → 0.947 | 0.841 | 0.030 → 0.778 | 10x advert_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.153 → 0.979 | 0.826 | 0.153 → 0.979 | 6.9x sr_airtime | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.121 → 0.924 | 0.803 | 0.100 → 0.794 | 93x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.202 → 0.971 | 0.768 | 0.083 → 0.841 | 7.2x sr_bytes | down | 4 |
| `RF-bw500` | preset | **held** | 0.238 → 0.917 | 0.679 | 0.112 → 0.736 | 7.6x sr_bytes | up | 3 |
| `RF-preset` | preset | **held** | 0.341 → 0.973 | 0.631 | 0.221 → 0.841 | 7.7x sr_airtime | up | 3 |
| `RF-eu-presets` | preset | **held** | 0.341 → 0.971 | 0.629 | 0.221 → 0.841 | 7.2x sr_bytes | up | 4 |
| `MS-topology` | topology | **held** | 0.444 → 0.978 | 0.534 | 0.531 → 0.946 | 3.5x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.328 → 0.841 | 0.513 | 0.328 → 0.841 | 12x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.508 → 0.951 | 0.444 | 0.330 → 0.753 | 4.8x bytes_on_air | down | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.600 → 0.984 | 0.383 | 0.833 → 0.853 | 2.1x sr_bytes | down | 5 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.218 → 0.596 | 0.378 | 0.218 → 0.596 | 3.2x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.495 → 0.841 | 0.346 | 0.495 → 0.841 | 2.3x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.543 → 0.871 | 0.328 | 0.543 → 0.871 | 7.6x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.520 → 0.841 | 0.321 | 0.520 → 0.841 | 2.5x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.587 → 0.905 | 0.319 | 0.587 → 0.905 | 7.1x sr_airtime | down | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.670 → 0.984 | 0.313 | 0.833 → 0.853 | 2.1x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.487 → 0.796 | 0.308 | 0.330 → 0.548 | 6x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.703 → 0.967 | 0.263 | 0.703 → 0.967 | 6.5x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.644 → 0.907 | 0.263 | 0.644 → 0.907 | 2.4x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.644 → 0.884 | 0.240 | 0.644 → 0.884 | 2.1x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.644 → 0.841 | 0.197 | 0.644 → 0.841 | 1.8x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.764 → 0.951 | 0.186 | 0.764 → 0.951 | 3.8x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **text** | 0.676 → 0.841 | 0.165 | 0.676 → 0.841 | 1.3x sr_bytes | down | 4 |
| `MS-size` | nodes | **text** | 0.708 → 0.845 | 0.137 | 0.708 → 0.845 | 5.6x sr_bytes | down | 5 |
| `DB-hotstore` | max-num-nodes | **text** | 0.741 → 0.872 | 0.131 | 0.741 → 0.872 | 2.1x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.743 → 0.872 | 0.128 | 0.743 → 0.872 | 2.1x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.713 → 0.841 | 0.128 | 0.713 → 0.841 | 1.6x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.714 → 0.841 | 0.127 | 0.714 → 0.841 | 1.3x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.778 → 0.899 | 0.122 | 0.778 → 0.899 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.778 → 0.899 | 0.122 | 0.778 → 0.899 | 2.4x bytes_on_air | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.841 → 0.953 | 0.112 | 0.841 → 0.953 | 1.2x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.841 → 0.950 | 0.109 | 0.841 → 0.950 | 1.9x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.795 → 0.889 | 0.094 | 0.795 → 0.889 | 5.6x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.841 → 0.922 | 0.081 | 0.841 → 0.922 | 1.3x bytes_on_air | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.730 → 0.793 | 0.063 | 0.730 → 0.793 | 1.7x sr_bytes | down | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.841 → 0.901 | 0.060 | 0.841 → 0.901 | 2.3x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.841 → 0.900 | 0.059 | 0.841 → 0.900 | 2.2x bytes_on_air | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.699 → 0.755 | 0.056 | 0.699 → 0.755 | 1.2x sr_airtime | down | 2 |
| `AD-worst` | role-placement | **text** | 0.781 → 0.832 | 0.051 | 0.781 → 0.832 | 1.3x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **text** | 0.778 → 0.827 | 0.049 | 0.778 → 0.827 | 1.2x bytes_on_air | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.793 → 0.841 | 0.047 | 0.793 → 0.841 | 1.3x sr_bytes | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.923 → 0.971 | 0.047 | 0.837 → 0.841 | 26x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.926 → 0.973 | 0.047 | 0.837 → 0.858 | 2.8x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.926 → 0.973 | 0.047 | 0.837 → 0.858 | 2.8x sr_bytes | up | 6 |
| `SF-cadence` | trigger | **held** | 0.927 → 0.971 | 0.044 | 0.814 → 0.841 | 14x sr_bytes | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.798 → 0.841 | 0.043 | 0.798 → 0.841 | 1.5x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.841 → 0.876 | 0.035 | 0.841 → 0.876 | 3.3x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.544 → 0.574 | 0.029 | 0.544 → 0.574 | 1.4x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.814 → 0.839 | 0.025 | 0.814 → 0.839 | 10x sr_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.840 → 0.861 | 0.022 | 0.840 → 0.861 | 3.5x bytes_on_air | down | 5 |
| `DM-mode` | dm-mode | **text** | 0.799 → 0.821 | 0.021 | 0.799 → 0.821 | 1.2x sr_airtime | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.841 → 0.859 | 0.018 | 0.841 → 0.859 | 1.3x sr_bytes | down | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.953 → 0.971 | 0.018 | 0.841 → 0.844 | 1.3x bytes_on_air | down | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.967 → 0.984 | 0.018 | 0.839 → 0.850 | 1.2x sr_bytes | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.841 → 0.858 | 0.017 | 0.841 → 0.858 | 2.1x sr_airtime | up | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.846 → 0.862 | 0.016 | 0.846 → 0.862 | 1.2x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.826 → 0.841 | 0.016 | 0.826 → 0.841 | 5.4x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.965 → 0.978 | 0.013 | 0.834 → 0.843 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.965 → 0.978 | 0.013 | 0.834 → 0.843 | 1.1x sr_airtime | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.965 → 0.977 | 0.012 | 0.836 → 0.841 | 2.5x sr_bytes | up | 2 |
| `FW-firmware` | profile | **held** | 0.971 → 0.982 | 0.011 | 0.841 → 0.850 | 3.3x bytes_on_air | down | 2 |
| `SF-window-size` | window-size | **text** | 0.829 → 0.840 | 0.011 | 0.829 → 0.840 | 5x advert_bytes | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.970 → 0.980 | 0.010 | 0.841 → 0.848 | 6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.970 → 0.980 | 0.010 | 0.841 → 0.848 | 6x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.965 → 0.975 | 0.010 | 0.840 → 0.844 | 2x advert_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.961 → 0.971 | 0.010 | 0.840 → 0.841 | 5.9x advert_bytes | = | 3 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.811 → 0.821 | 0.010 | 0.811 → 0.821 | 1.1x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.942 → 0.951 | 0.009 | 0.942 → 0.951 | 1.2x bytes_on_air | down | 2 |
| `SF-width` | short-id-bits | **held** | 0.971 → 0.980 | 0.009 | 0.841 → 0.848 | 3.1x advert_bytes | down | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.841 → 0.850 | 0.009 | 0.841 → 0.850 | 1.1x sr_airtime | up | 2 |
| `SF-capacity` | capacity | **text** | 0.837 → 0.845 | 0.008 | 0.837 → 0.845 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **text** | 0.837 → 0.845 | 0.008 | 0.837 → 0.845 | 5.4x advert_bytes | up | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.826 → 0.834 | 0.007 | 0.826 → 0.834 | 1.2x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.965 → 0.971 | 0.006 | 0.836 → 0.841 | 2.7x advert_bytes | = | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.858 → 0.863 | 0.005 | 0.858 → 0.863 | 1.1x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.837 → 0.841 | 0.004 | 0.837 → 0.841 | 2.8x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.838 → 0.841 | 0.003 | 0.838 → 0.841 | 1x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.955 → 0.958 | 0.002 | 0.811 → 0.811 | 1.1x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.997 → 0.998 | 0.001 | 0.951 → 0.951 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.997 → 0.998 | 0.001 | 0.951 → 0.951 | 1.1x sr_airtime | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario valleys`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| sprinkled | 0.875 | - | - | 0.981 | 0.981 | 0.582 | 1.22x | 25.1/27.7% | 5.4% | 3 |
| arms-race | 0.953 | - | - | 0.988 | 0.988 | 0.860 | 1.10x | 26.1/28.9% | 5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.1 | 0.897 | - | - | 0.991 | 0.993 | 0.635 | 1.25x | 24.2/29.2% | 5.1% | 3 |
| 0.3 | 0.950 | - | - | 0.993 | 0.993 | 0.883 | 1.03x | 25.4/27.6% | 5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.778 | - | - | 0.947 | 0.948 | 0.224 | 1.15x | 23.9/28.3% | 5.3% | 3 |
| inverse | 0.793 | - | - | 0.972 | 0.975 | 0.190 | 1.15x | 16.7/20.6% | 4.6% | 3 |
| random | 0.730 | - | - | 0.922 | 0.925 | 0.111 | 1.08x | 18.7/23.7% | 4.8% | 3 |

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.778 | - | - | 0.947 | 0.948 | 0.224 | 1.15x | 23.9/28.3% | 5.3% | 3 |
| all-routers | 0.899 | - | - | 0.978 | 0.978 | 0.621 | 2.72x | 40.2/43.3% | 5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.778 | - | - | 0.947 | 0.948 | 0.224 | 1.15x | 23.9/28.3% | 5.3% | 3 |
| no-mute | 0.843 | - | - | 0.983 | 0.985 | 0.221 | 1.31x | 22.1/25.4% | 5.2% | 3 |
| all-routers | 0.899 | - | - | 0.978 | 0.978 | 0.621 | 2.72x | 40.2/43.3% | 5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.778 | - | - | 0.947 | 0.948 | 0.224 | 1.15x | 23.9/28.3% | 5.3% | 3 |
| local-typical | 0.489 | - | - | 0.746 | 0.748 | 0.000 | 1.17x | 21.6/26.7% | 5.1% | 3 |
| basement-heavy | 0.030 | - | - | 0.106 | 0.127 | 0.000 | 0.31x | 2.1/5.3% | 1.9% | 3 |

> siting-mix=basement-heavy: decode_failures 3

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.832 | - | - | 0.971 | 0.971 | 0.000 | 2.41x | 25.3/33.9% | 6.0% | 3 |
| inverse | 0.781 | - | - | 0.969 | 0.971 | 0.000 | 2.26x | 22.5/31.9% | 3.3% | 3 |

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.837 | - | - | 0 | 0.000 | 0.247 | 1.35x | 24.0/27.5% | 5.1% | 3 |
| sr | 0.853 | - | - | 0.984 | 0.985 | 0.274 | 1.37x | 24.4/27.9% | 5.2% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.741 | - | - | 0.859 | 0.859 | 0.237 | 3.02x | 53.6/60.1% | 10.0% | 3 |
| 100 | 0.872 | - | - | 0.961 | 0.962 | 0.289 | 1.61x | 29.9/34.2% | 5.3% | 3 |
| 120 | 0.872 | - | - | 0.961 | 0.962 | 0.289 | 1.61x | 29.9/34.2% | 5.3% | 3 |
| 250 | 0.872 | - | - | 0.961 | 0.962 | 0.289 | 1.61x | 29.9/34.2% | 5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.330 | - | - | 0.487 | 0.645 | 0.145 | 11.72x | 63.0/76.4% | 11.1% | 3 |
| 120 | 0.544 | - | - | 0.796 | 0.853 | 0.223 | 4.64x | 28.4/42.1% | 5.4% | 3 |
| 250 | 0.548 | - | - | 0.791 | 0.862 | 0.230 | 4.49x | 27.6/41.0% | 5.1% | 3 |

> max-num-nodes=10: decode_failures 45

> max-num-nodes=120: decode_failures 87

> max-num-nodes=250: decode_failures 96

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.872 | - | - | 0.961 | 0.962 | 0.289 | 1.61x | 29.9/34.2% | 5.3% | 3 |
| baymesh-2026-08 | 0.872 | - | - | 0.961 | 0.962 | 0.289 | 1.61x | 29.9/34.2% | 5.3% | 3 |
| constrained | 0.743 | - | - | 0.857 | 0.857 | 0.253 | 3.03x | 53.6/60.1% | 10.0% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.755 | - | - | 0.916 | 0.944 | 0.601 | 5.43x | 70.7/77.6% | 12.6% | 3 |
| 25 | 0.755 | - | - | 0.916 | 0.944 | 0.601 | 5.43x | 70.7/77.6% | 12.6% | 3 |
| 100 | 0.755 | - | - | 0.916 | 0.944 | 0.601 | 5.43x | 70.7/77.6% | 12.6% | 3 |
| 2000 | 0.755 | - | - | 0.916 | 0.944 | 0.601 | 5.43x | 70.7/77.6% | 12.6% | 3 |

> warm-num-nodes=0: decode_failures 78

> warm-num-nodes=25: decode_failures 78

> warm-num-nodes=100: decode_failures 78

> warm-num-nodes=2000: decode_failures 78

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.1 | 0.736 | - | - | 0.938 | 0.942 | 0.193 | 1.26x | 22.6/26.4% | 4.8% | 3 |
| 0.2 | 0.640 | - | - | 0.898 | 0.907 | 0.174 | 1.18x | 21.8/25.0% | 4.3% | 3 |
| 0.3 | 0.520 | - | - | 0.763 | 0.824 | 0.145 | 1.06x | 20.0/23.0% | 3.8% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 25

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.1 | 0.810 | - | - | 0.956 | 0.959 | 0.254 | 1.40x | 24.7/28.1% | 5.0% | 3 |
| 0.2 | 0.759 | - | - | 0.936 | 0.938 | 0.212 | 1.43x | 25.5/28.9% | 4.9% | 3 |
| 0.3 | 0.713 | - | - | 0.917 | 0.919 | 0.185 | 1.45x | 26.3/29.8% | 4.8% | 3 |

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.1 | 0.722 | - | - | 0.896 | 0.931 | 0.210 | 1.26x | 23.0/26.9% | 4.9% | 3 |
| 0.2 | 0.621 | - | - | 0.848 | 0.909 | 0.148 | 1.18x | 21.8/25.1% | 4.4% | 3 |
| 0.3 | 0.495 | - | - | 0.647 | 0.826 | 0.141 | 1.09x | 20.2/23.2% | 4.1% | 3 |

> burst-loss=0.1: decode_failures 31

> burst-loss=0.2: decode_failures 39

> burst-loss=0.3: decode_failures 28

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 0.799 | - | - | 0.946 | 0.946 | 0.277 | 1.76x | 31.3/35.7% | 6.7% | 3 |
| directed-with-late-flood | 0.821 | - | - | 0.964 | 0.970 | 0.249 | 1.60x | 28.8/33.0% | 6.2% | 3 |
| m4-early-flood | 0.808 | - | - | 0.948 | 0.951 | 0.269 | 1.60x | 28.9/33.0% | 6.2% | 3 |

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 0.850 | - | - | 0.982 | 0.982 | 0.527 | 0.73x | 11.1/12.3% | 1.8% | 3 |
| 2.8 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.25 | 0.894 | - | - | 0.989 | 0.990 | 0.754 | 1.12x | 18.5/20.4% | 4.4% | 3 |
| 0.5 | 0.900 | - | - | 0.989 | 0.989 | 0.618 | 1.05x | 16.9/18.5% | 3.9% | 3 |
| 0.75 | 0.860 | - | - | 0.974 | 0.975 | 0.468 | 0.88x | 14.0/17.5% | 3.4% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.25 | 0.896 | - | - | 0.991 | 0.992 | 0.754 | 1.10x | 18.1/20.4% | 4.4% | 3 |
| 0.5 | 0.901 | - | - | 0.991 | 0.992 | 0.679 | 1.02x | 17.0/18.3% | 3.8% | 3 |
| 0.75 | 0.858 | - | - | 0.971 | 0.971 | 0.476 | 0.85x | 13.7/17.2% | 3.4% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 0.876 | - | - | 0.986 | 0.987 | 0.263 | 0.73x | 13.7/16.0% | 2.9% | 3 |
| signing=true | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 0.845 | - | - | 0.982 | 0.983 | 0.509 | 0.73x | 12.0/13.4% | 2.6% | 3 |
| 2.5 | 0.840 | - | - | 0.983 | 0.983 | 0.523 | 0.73x | 11.9/13.3% | 2.5% | 3 |
| 2.6 | 0.841 | - | - | 0.985 | 0.986 | 0.507 | 0.70x | 11.8/13.3% | 2.5% | 3 |
| 2.7 | 0.861 | - | - | 0.970 | 0.972 | 0.516 | 0.75x | 15.1/16.7% | 3.2% | 3 |
| 2.8 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.871 | - | - | 0.982 | 0.983 | 0.273 | 0.91x | 16.2/18.6% | 3.5% | 3 |
| 900 | 0.795 | - | - | 0.956 | 0.960 | 0.222 | 2.11x | 37.1/42.4% | 7.9% | 3 |
| 300 | 0.543 | - | - | 0.727 | 0.793 | 0.195 | 4.50x | 68.7/76.3% | 14.8% | 3 |

> broadcast-interval-s=300: decode_failures 31

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.905 | - | - | 0.979 | 0.979 | 0.287 | 0.97x | 16.2/19.0% | 3.5% | 3 |
| 900 | 0.842 | - | - | 0.945 | 0.946 | 0.292 | 2.37x | 39.3/45.0% | 8.5% | 3 |
| 300 | 0.587 | - | - | 0.779 | 0.792 | 0.164 | 4.93x | 70.2/77.7% | 15.4% | 3 |

> broadcast-interval-s=300: decode_failures 5

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 0.859 | - | - | 0.978 | 0.978 | 0.275 | 1.22x | 22.0/25.1% | 4.7% | 3 |
| sinusoid | 0.853 | - | - | 0.975 | 0.977 | 0.272 | 1.23x | 21.9/25.1% | 4.6% | 3 |
| commuter | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 0.795 | - | - | 0.956 | 0.960 | 0.222 | 2.11x | 37.1/42.4% | 7.9% | 3 |
| 3600 | 0.871 | - | - | 0.982 | 0.983 | 0.273 | 0.91x | 16.2/18.6% | 3.5% | 3 |
| 10800 | 0.884 | - | - | 0.994 | 0.995 | 0.270 | 0.59x | 10.7/12.3% | 2.3% | 3 |
| 43200 | 0.889 | - | - | 0.992 | 0.992 | 0.296 | 0.43x | 7.7/8.9% | 1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.25 | 0.834 | - | - | 0.967 | 0.967 | 0.247 | 1.44x | 25.6/29.4% | 5.5% | 3 |
| 1.0 | 0.825 | - | - | 0.955 | 0.956 | 0.260 | 1.56x | 27.9/32.0% | 6.0% | 3 |
| 4.0 | 0.798 | - | - | 0.948 | 0.948 | 0.252 | 1.93x | 35.0/40.1% | 7.6% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.755 | - | - | 0.916 | 0.944 | 0.601 | 5.43x | 70.7/77.6% | 12.6% | 3 |
| 1.0 | 0.699 | - | - | 0.884 | 0.923 | 0.540 | 5.90x | 72.4/79.0% | 13.3% | 3 |

> traceroute-per-hour=0.0: decode_failures 78

> traceroute-per-hour=1.0: queue drops 12.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 125

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.703 | - | - | 0.840 | 0.842 | 0.000 | 1.36x | 30.5/34.6% | 7.1% | 3 |
| 60 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 90 | 0.930 | - | - | 0.997 | 0.998 | 0.785 | 1.50x | 25.1/29.3% | 4.7% | 3 |
| 120 | 0.951 | - | - | 0.997 | 0.998 | 0.849 | 1.88x | 32.0/38.0% | 4.9% | 3 |
| 150 | 0.967 | - | - | 0.999 | 0.999 | 0.857 | 2.42x | 40.9/44.5% | 5.5% | 3 |

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 120 | 0.754 | - | - | 0.957 | 0.958 | 0.352 | 2.10x | 24.1/31.5% | 5.1% | 3 |
| 250 | 0.549 | - | - | 0.782 | 0.852 | 0.238 | 4.82x | 30.0/44.8% | 5.7% | 3 |
| 500 | 0.328 | - | - | 0.501 | 0.501 | 0.105 | 10.22x | 33.3/51.1% | 5.6% | 3 |

> nodes=250: decode_failures 158

> nodes=500: decode_failures 12

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 0.753 | - | - | 0.951 | 0.952 | 0.346 | 1.98x | 22.8/29.5% | 4.8% | 3 |
| 250 | 0.544 | - | - | 0.796 | 0.853 | 0.223 | 4.64x | 28.4/42.1% | 5.4% | 3 |
| 500 | 0.330 | - | - | 0.508 | 0.511 | 0.101 | 9.45x | 30.9/47.5% | 5.1% | 3 |

> nodes=250: decode_failures 87

> nodes=500: decode_failures 40

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.827 | - | - | 0.972 | 0.972 | 0.274 | 1.35x | 24.1/27.7% | 5.1% | 3 |
| baymesh-2026-08 | 0.778 | - | - | 0.947 | 0.948 | 0.224 | 1.15x | 23.9/28.3% | 5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.826 | - | - | 0.960 | 0.961 | 0.274 | 1.39x | 24.3/28.3% | 5.4% | 3 |
| baymesh-2026-08 | 0.834 | - | - | 0.953 | 0.954 | 0.298 | 1.31x | 26.9/31.5% | 5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.05 | 0.844 | - | - | 0.965 | 0.967 | 0.248 | 1.47x | 27.6/31.4% | 5.3% | 3 |
| 0.1 | 0.844 | - | - | 0.957 | 0.957 | 0.276 | 1.57x | 30.1/34.3% | 5.1% | 3 |
| 0.2 | 0.842 | - | - | 0.953 | 0.953 | 0.235 | 1.77x | 35.7/42.7% | 5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| local-typical | 0.528 | - | - | 0.764 | 0.765 | 0.000 | 1.36x | 22.8/27.3% | 5.2% | 3 |
| event | 0.153 | - | - | 0.224 | 0.348 | 0.000 | 1.02x | 9.7/13.7% | 3.3% | 3 |
| backbone | 0.979 | - | - | 0.999 | 0.999 | 0.938 | 1.08x | 33.8/35.8% | 5.5% | 3 |

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.832 | - | - | 0.943 | 0.949 | 0.162 | 1.28x | 31.0/32.9% | 7.7% | 3 |
| 60 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 90 | 0.845 | - | - | 0.972 | 0.974 | 0.321 | 1.65x | 21.6/24.8% | 4.8% | 3 |
| 120 | 0.754 | - | - | 0.957 | 0.958 | 0.352 | 2.10x | 24.1/31.5% | 5.1% | 3 |
| 150 | 0.708 | - | - | 0.946 | 0.946 | 0.316 | 2.74x | 28.0/36.4% | 5.7% | 3 |

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 1.25 | 0.571 | - | - | 0.774 | 0.783 | 0.260 | 1.31x | 17.9/21.2% | 5.2% | 3 |
| 1.5 | 0.218 | - | - | 0.346 | 0.348 | 0.000 | 1.14x | 13.3/16.6% | 4.1% | 3 |
| 2.0 | 0.083 | - | - | 0.202 | 0.205 | 0.000 | 0.68x | 9.6/13.3% | 3.0% | 3 |

> stretch=1.25: decode_failures 3

> faster: 1.55 s per simulated hour against 3.48 over 5 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| clustered | 0.918 | - | - | 0.966 | 0.966 | 0.272 | 1.05x | 29.2/31.4% | 5.6% | 3 |
| corridor | 0.531 | - | - | 0.444 | 0.446 | 0.336 | 1.45x | 21.7/24.2% | 4.6% | 3 |
| hub | 0.946 | - | - | 0.978 | 0.978 | 0.786 | 1.19x | 36.3/37.7% | 5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.821 | - | - | 0.964 | 0.970 | 0.249 | 1.60x | 28.8/33.0% | 6.2% | 3 |
| True | 0.811 | - | - | 0.955 | 0.958 | 0.249 | 1.62x | 29.2/33.4% | 6.3% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 0.811 | - | - | 0.955 | 0.958 | 0.249 | 1.62x | 29.2/33.4% | 6.3% | 3 |
| m4-early-flood | 0.811 | - | - | 0.958 | 0.961 | 0.247 | 1.61x | 29.0/33.1% | 6.2% | 3 |

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.837 | - | - | 0 | 0.000 | 0.247 | 1.35x | 24.0/27.5% | 5.1% | 3 |
| chain | 0.827 | - | - | 0.924 | 0.964 | 0.246 | 1.54x | 27.5/31.6% | 5.9% | 3 |
| sr | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| True | 0.850 | - | - | 0.972 | 0.972 | 0.275 | 1.38x | 24.4/28.0% | 5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.951 | - | - | 0.997 | 0.998 | 0.849 | 1.88x | 32.0/38.0% | 4.9% | 3 |
| True | 0.951 | - | - | 0.998 | 0.998 | 0.845 | 1.92x | 32.5/38.6% | 5.0% | 3 |

> extra-repeats=True: misdecodes 1

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 0.112 | - | - | 0.238 | 0.240 | 0.000 | 0.03x | 0.5/0.7% | 0.1% | 3 |
| MEDIUM_TURBO | 0.326 | - | - | 0.544 | 0.581 | 0.000 | 0.25x | 3.3/4.3% | 0.9% | 3 |
| LONG_TURBO | 0.736 | - | - | 0.917 | 0.919 | 0.368 | 1.33x | 21.3/23.3% | 4.6% | 3 |

> preset=MEDIUM_TURBO: decode_failures 16

> preset=LONG_TURBO: decode_failures 1

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 0.25 | 0.855 | - | - | 0.974 | 0.974 | 0.340 | 1.30x | 25.7/29.0% | 5.2% | 3 |
| 1.0 | 0.922 | - | - | 0.992 | 0.992 | 0.648 | 1.04x | 30.1/33.0% | 5.2% | 3 |

> duct-per-hour=1.0: misdecodes 1

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.221 | - | - | 0.341 | 0.342 | 0.000 | 0.12x | 1.5/2.3% | 0.4% | 3 |
| LONG_FAST | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| LITE_FAST | 0.785 | - | - | 0.934 | 0.942 | 0.242 | 1.02x | 16.9/19.8% | 4.0% | 3 |
| NARROW_SLOW | 0.794 | - | - | 0.955 | 0.956 | 0.269 | 1.32x | 23.5/26.3% | 5.0% | 3 |

> preset=LITE_FAST: decode_failures 7

> preset=NARROW_SLOW: decode_failures 1

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| temporal | 0.749 | - | - | 0.933 | 0.935 | 0.223 | 1.36x | 24.5/27.6% | 5.0% | 3 |
| transient | 0.840 | - | - | 0.972 | 0.974 | 0.247 | 1.36x | 24.3/27.8% | 5.2% | 3 |
| periodic | 0.676 | - | - | 0.809 | 0.810 | 0.195 | 1.24x | 22.1/25.2% | 4.4% | 3 |

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.221 | - | - | 0.341 | 0.342 | 0.000 | 0.12x | 1.5/2.3% | 0.4% | 3 |
| LONG_FAST | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| LONG_MODERATE | 0.834 | - | - | 0.973 | 0.973 | 0.684 | 3.46x | 63.0/66.6% | 12.7% | 3 |

> preset=LONG_MODERATE: decode_failures 8

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 0.048 | - | - | 0.076 | 0.078 | 0.000 | 0.01x | 0.1/0.1% | 0.0% | 3 |
| SHORT_TURBO | 0.112 | - | - | 0.238 | 0.240 | 0.000 | 0.03x | 0.5/0.7% | 0.1% | 3 |
| LONG_FAST | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| LONG_TURBO | 0.736 | - | - | 0.917 | 0.919 | 0.368 | 1.33x | 21.3/23.3% | 4.6% | 3 |
| EXTRA_LONG_TURBO | 0.825 | - | - | 0.949 | 0.964 | 0.269 | 1.91x | 31.3/36.7% | 6.9% | 3 |

> preset=LONG_TURBO: decode_failures 1

> preset=EXTRA_LONG_TURBO: decode_failures 23

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 0.794 | - | - | 0.924 | 0.927 | 0.247 | 1.31x | 23.6/27.1% | 4.9% | 3 |
| 10000 | 0.676 | - | - | 0.809 | 0.810 | 0.195 | 1.24x | 22.1/25.2% | 4.4% | 3 |
| 4000 | 0.430 | - | - | 0.539 | 0.570 | 0.115 | 1.05x | 18.9/21.5% | 3.4% | 3 |
| 2000 | 0.100 | - | - | 0.121 | 0.199 | 0.034 | 0.71x | 13.2/15.2% | 2.0% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.218 | - | - | 0.346 | 0.348 | 0.000 | 1.14x | 13.3/16.6% | 4.1% | 3 |
| 1.0 | 0.596 | - | - | 0.692 | 0.693 | 0.412 | 0.93x | 16.5/19.8% | 4.2% | 3 |

> faster: 0.949 s per simulated hour against 3.25 over 5 prior run(s) - 3.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 22 | 0.298 | - | - | 0.492 | 0.562 | 0.000 | 1.47x | 17.8/23.8% | 4.7% | 3 |
| 17 | 0.108 | - | - | 0.220 | 0.220 | 0.000 | 0.77x | 8.8/13.2% | 3.1% | 3 |
| 14 | 0.054 | - | - | 0.101 | 0.102 | 0.000 | 0.55x | 5.4/9.3% | 2.2% | 3 |

> tx-power=22: decode_failures 11

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.951 | - | - | 0.997 | 0.998 | 0.849 | 1.88x | 32.0/38.0% | 4.9% | 3 |
| True | 0.942 | - | - | 0.998 | 0.999 | 0.830 | 2.27x | 37.5/43.4% | 5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.846 | - | - | 0.970 | 0.971 | 0.249 | 1.44x | 26.5/29.8% | 5.3% | 3 |
| True | 0.862 | - | - | 0.958 | 0.959 | 0.284 | 1.49x | 26.7/30.0% | 5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| random | 0.793 | - | - | 0.956 | 0.957 | 0.272 | 1.29x | 22.6/25.7% | 5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.644 | - | - | 0.904 | 0.905 | 0.096 | 1.00x | 19.3/22.5% | 4.3% | 3 |
| 7 | 0.884 | - | - | 0.973 | 0.975 | 0.278 | 1.49x | 24.9/28.9% | 5.4% | 3 |
| 15 | 0.905 | - | - | 0.967 | 0.969 | 0.321 | 1.49x | 24.9/28.8% | 5.4% | 3 |
| 32 | 0.907 | - | - | 0.968 | 0.970 | 0.308 | 1.52x | 25.3/29.4% | 5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.644 | - | - | 0.904 | 0.905 | 0.096 | 1.00x | 19.3/22.5% | 4.3% | 3 |
| 5 | 0.818 | - | - | 0.962 | 0.964 | 0.205 | 1.32x | 23.2/26.7% | 5.0% | 3 |
| 7 | 0.884 | - | - | 0.973 | 0.975 | 0.278 | 1.49x | 24.9/28.9% | 5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| KNOWN_ONLY | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| CORE_PORTNUMS_ONLY | 0.837 | - | - | 0.923 | 0.975 | 0.277 | 1.33x | 23.6/27.0% | 5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.644 | - | - | 0.904 | 0.905 | 0.096 | 1.00x | 19.3/22.5% | 4.3% | 3 |
| True | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| BALANCED | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| STRICT | 0.714 | - | - | 0.857 | 0.859 | 0.160 | 1.46x | 26.2/30.0% | 5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| dm | 0.837 | - | - | 0.970 | 0.970 | 0.242 | 1.33x | 23.7/27.5% | 5.1% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 0.836 | - | - | 0.965 | 0.965 | 0.270 | 1.39x | 24.6/28.2% | 5.2% | 3 |
| local | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| time | 0.838 | - | - | 0.969 | 0.970 | 0.244 | 1.39x | 24.6/28.4% | 5.3% | 3 |
| window | 0.840 | - | - | 0.965 | 0.966 | 0.263 | 1.34x | 23.8/27.3% | 5.1% | 3 |

> bucket-mode=global: misdecodes 49

> bucket-mode=time: misdecodes 33

> bucket-mode=window: misdecodes 27

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 0.826 | - | - | 0.966 | 0.966 | 0.254 | 1.49x | 26.7/30.6% | 5.8% | 3 |
| 1800 | 0.838 | - | - | 0.969 | 0.970 | 0.244 | 1.39x | 24.6/28.4% | 5.3% | 3 |
| 3600 | 0.841 | - | - | 0.970 | 0.972 | 0.251 | 1.37x | 24.3/28.0% | 5.2% | 3 |

> time-bucket-s=600: misdecodes 118

> time-bucket-s=1800: misdecodes 33

> time-bucket-s=3600: misdecodes 11

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| interval | 0.827 | - | - | 0.965 | 0.968 | 0.258 | 1.78x | 33.0/37.9% | 8.0% | 3 |
| aimd | 0.835 | - | - | 0.927 | 0.977 | 0.269 | 1.35x | 24.1/27.6% | 5.1% | 3 |
| bucket+interval | 0.814 | - | - | 0.956 | 0.956 | 0.219 | 1.83x | 33.7/39.5% | 9.1% | 3 |

> trigger=interval: misdecodes 11

> trigger=aimd: misdecodes 5

> trigger=bucket+interval: misdecodes 30

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.838 | - | - | 0.966 | 0.970 | 0.250 | 1.35x | 24.1/27.9% | 5.3% | 3 |
| 8 | 0.845 | - | - | 0.972 | 0.974 | 0.243 | 1.37x | 24.3/28.1% | 5.2% | 3 |
| 16 | 0.837 | - | - | 0.970 | 0.971 | 0.241 | 1.35x | 23.8/27.4% | 5.1% | 3 |
| 32 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 50 | 0.841 | - | - | 0.973 | 0.974 | 0.258 | 1.35x | 24.1/27.6% | 5.1% | 3 |

> capacity=4: decode_failures 77

> capacity=8: decode_failures 39

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.838 | - | - | 0.966 | 0.970 | 0.250 | 1.35x | 24.1/27.9% | 5.3% | 3 |
| 8 | 0.845 | - | - | 0.972 | 0.974 | 0.243 | 1.37x | 24.3/28.1% | 5.2% | 3 |
| 16 | 0.837 | - | - | 0.970 | 0.971 | 0.241 | 1.35x | 23.8/27.4% | 5.1% | 3 |
| 32 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 50 | 0.841 | - | - | 0.973 | 0.974 | 0.258 | 1.35x | 24.1/27.6% | 5.1% | 3 |

> capacity=4: decode_failures 77

> capacity=8: decode_failures 39

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.844 | - | - | 0.967 | 0.970 | 0.271 | 1.35x | 24.1/27.7% | 5.1% | 3 |
| 16 | 0.844 | - | - | 0.975 | 0.976 | 0.267 | 1.36x | 24.0/27.7% | 5.1% | 3 |
| 32 | 0.840 | - | - | 0.965 | 0.966 | 0.263 | 1.34x | 23.8/27.3% | 5.1% | 3 |

> capacity=8: misdecodes 49

> capacity=8: decode_failures 8

> capacity=16: misdecodes 31

> capacity=16: decode_failures 2

> capacity=32: misdecodes 27

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 0.814 | - | - | 0.956 | 0.956 | 0.219 | 1.83x | 33.7/39.5% | 9.1% | 3 |
| 02-06 | 0.839 | - | - | 0.949 | 0.977 | 0.257 | 1.38x | 24.6/28.3% | 5.3% | 3 |
| 00-08 | 0.834 | - | - | 0.944 | 0.970 | 0.256 | 1.43x | 25.7/29.6% | 5.6% | 3 |

> catch-up-hours=: misdecodes 30

> catch-up-hours=02-06: decode_failures 6

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 3

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.833 | - | - | 0.971 | 0.971 | 0.270 | 1.38x | 24.4/28.0% | 5.2% | 3 |
| 2 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 3 | 0.853 | - | - | 0.984 | 0.985 | 0.274 | 1.37x | 24.4/27.9% | 5.2% | 3 |
| 4 | 0.841 | - | - | 0.670 | 0.963 | 0.248 | 1.36x | 23.8/27.4% | 5.2% | 3 |

> hops-apart=4: decode_failures 21

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.833 | - | - | 0.971 | 0.971 | 0.270 | 1.38x | 24.4/28.0% | 5.2% | 3 |
| 2 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 3 | 0.853 | - | - | 0.984 | 0.985 | 0.274 | 1.37x | 24.4/27.9% | 5.2% | 3 |
| 4 | 0.841 | - | - | 0.670 | 0.963 | 0.248 | 1.36x | 23.8/27.4% | 5.2% | 3 |
| 5 | 0.839 | - | - | 0.600 | 0.940 | 0.264 | 1.36x | 24.1/27.5% | 5.2% | 3 |

> hops-apart=4: decode_failures 21

> hops-apart=5: decode_failures 16

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.840 | - | - | 0.970 | 0.970 | 0.244 | 1.35x | 24.2/27.6% | 5.1% | 3 |
| 30 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 120 | 0.834 | - | - | 0.965 | 0.966 | 0.267 | 1.36x | 24.2/27.7% | 5.2% | 3 |
| 600 | 0.843 | - | - | 0.978 | 0.979 | 0.240 | 1.38x | 24.5/28.1% | 5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.840 | - | - | 0.970 | 0.970 | 0.244 | 1.35x | 24.2/27.6% | 5.1% | 3 |
| 30 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 120 | 0.834 | - | - | 0.965 | 0.966 | 0.267 | 1.36x | 24.2/27.7% | 5.2% | 3 |
| 600 | 0.843 | - | - | 0.978 | 0.979 | 0.240 | 1.38x | 24.5/28.1% | 5.2% | 3 |

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.857 | - | - | 0.926 | 0.982 | 0.247 | 1.38x | 24.4/28.0% | 5.1% | 3 |
| routers | 0.841 | - | - | 0.965 | 0.966 | 0.241 | 1.36x | 24.2/27.8% | 5.2% | 3 |
| alternate-routers | 0.837 | - | - | 0.973 | 0.973 | 0.243 | 1.36x | 24.3/27.9% | 5.2% | 3 |
| beside-router | 0.845 | - | - | 0.957 | 0.959 | 0.256 | 1.36x | 24.3/27.8% | 5.2% | 3 |
| random-clients | 0.858 | - | - | 0.933 | 0.970 | 0.244 | 1.38x | 24.7/28.1% | 5.1% | 3 |
| hops-apart | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

> place=spread: decode_failures 32

> place=random-clients: decode_failures 39

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.857 | - | - | 0.926 | 0.982 | 0.247 | 1.38x | 24.4/28.0% | 5.1% | 3 |
| routers | 0.841 | - | - | 0.965 | 0.966 | 0.241 | 1.36x | 24.2/27.8% | 5.2% | 3 |
| alternate-routers | 0.837 | - | - | 0.973 | 0.973 | 0.243 | 1.36x | 24.3/27.9% | 5.2% | 3 |
| beside-router | 0.845 | - | - | 0.957 | 0.959 | 0.256 | 1.36x | 24.3/27.8% | 5.2% | 3 |
| random-clients | 0.858 | - | - | 0.933 | 0.970 | 0.244 | 1.38x | 24.7/28.1% | 5.1% | 3 |
| hops-apart | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

> place=spread: decode_failures 32

> place=random-clients: decode_failures 39

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| broadcast | 0.858 | - | - | 0.965 | 0.966 | 0.255 | 1.40x | 24.9/28.5% | 5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| heard | 0.838 | - | - | 0.972 | 0.972 | 0.254 | 1.37x | 24.2/28.0% | 5.1% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.858 | - | - | 0.965 | 0.966 | 0.255 | 1.40x | 24.9/28.5% | 5.3% | 3 |
| heard | 0.863 | - | - | 0.968 | 0.968 | 0.285 | 1.41x | 24.8/28.5% | 5.3% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| enum | 0.840 | - | - | 0.961 | 0.964 | 0.245 | 1.36x | 24.3/28.2% | 5.3% | 3 |
| hybrid | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.841 | - | - | 0.965 | 0.966 | 0.241 | 1.36x | 24.2/27.8% | 5.2% | 3 |
| 6 | 0.836 | - | - | 0.977 | 0.977 | 0.247 | 1.40x | 25.2/28.9% | 5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.846 | - | - | 0.973 | 0.974 | 0.269 | 1.36x | 24.2/27.8% | 5.2% | 2 |
| 3 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 5 | 0.846 | - | - | 0.970 | 0.970 | 0.257 | 1.39x | 24.8/28.6% | 5.2% | 5 |
| 8 | 0.848 | - | - | 0.980 | 0.982 | 0.254 | 1.44x | 25.8/29.6% | 5.4% | 8 |

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.846 | - | - | 0.973 | 0.974 | 0.269 | 1.36x | 24.2/27.8% | 5.2% | 2 |
| 3 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 5 | 0.846 | - | - | 0.970 | 0.970 | 0.257 | 1.39x | 24.8/28.6% | 5.2% | 5 |
| 8 | 0.848 | - | - | 0.980 | 0.982 | 0.254 | 1.44x | 25.8/29.6% | 5.4% | 8 |

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| True | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.847 | - | - | 0.977 | 0.977 | 0.280 | 1.24x | 21.9/25.1% | 4.6% | 3 |
| 1 | 0.841 | - | - | 0.967 | 0.968 | 0.274 | 1.24x | 21.9/25.0% | 4.7% | 3 |
| 2 | 0.850 | - | - | 0.984 | 0.985 | 0.262 | 1.23x | 21.9/25.2% | 4.7% | 3 |
| 4 | 0.839 | - | - | 0.978 | 0.979 | 0.229 | 1.24x | 22.0/25.1% | 4.6% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 0.848 | - | - | 0.980 | 0.980 | 0.276 | 1.36x | 24.2/27.9% | 5.2% | 3 |
| 24 | 0.844 | - | - | 0.972 | 0.972 | 0.279 | 1.38x | 24.4/28.1% | 5.2% | 3 |
| 32 | 0.841 | - | - | 0.971 | 0.971 | 0.265 | 1.37x | 24.4/28.0% | 5.2% | 3 |
| 64 | 0.847 | - | - | 0.972 | 0.972 | 0.254 | 1.38x | 24.6/28.3% | 5.2% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.829 | - | - | 0.960 | 0.961 | 0.252 | 1.46x | 25.9/29.6% | 5.5% | 3 |
| 16 | 0.832 | - | - | 0.965 | 0.965 | 0.253 | 1.41x | 25.2/28.9% | 5.4% | 3 |
| 32 | 0.840 | - | - | 0.965 | 0.966 | 0.263 | 1.34x | 23.8/27.3% | 5.1% | 3 |

> window-size=8: misdecodes 145

> window-size=16: misdecodes 96

> window-size=32: misdecodes 27

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.951 | - | - | 0.997 | 0.998 | 0.849 | 1.88x | 32.0/38.0% | 4.9% | 3 |
| True | 0.764 | - | - | 0.935 | 0.955 | 0.618 | 5.31x | 70.2/77.1% | 12.5% | 3 |

> no-congestion-scaling=True: decode_failures 101

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 0.544 | - | - | 0.796 | 0.853 | 0.223 | 4.64x | 28.4/42.1% | 5.4% | 3 |
| truesize | 0.574 | - | - | 0.824 | 0.882 | 0.241 | 3.60x | 23.5/35.0% | 4.5% | 3 |

> congestion-input=hotstore: decode_failures 87

> congestion-input=truesize: decode_failures 101

> slower: 48.8 s per simulated hour against 18.3 over 5 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 0.951 | - | - | 0.998 | 0.998 | 0.853 | 1.79x | 30.1/35.6% | 4.6% | 3 |
| adaptive | 0.951 | - | - | 0.997 | 0.998 | 0.849 | 1.88x | 32.0/38.0% | 4.9% | 3 |

