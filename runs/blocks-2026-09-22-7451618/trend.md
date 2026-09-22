# Sweep blocks-2026-09-22-7451618

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** coastal
- **seed base** 7451618 · seeds 7451618
- **blocks** 87 run
- **compute** 10.8 h of simulator time across every cell
- **generated** 2026-09-22T08:52:38+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>88 warnings</summary>

- AD-siting: siting-mix=basement-heavy: decode_failures 2
- AD-worst: role-placement=degree: decode_failures 64
- AD-worst: role-placement=inverse: decode_failures 46
- AD-worst: slower: 17.9 s per simulated hour against 3.48 over 32 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 39
- BL-control: slower: 5.27 s per simulated hour against 1.72 over 32 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 40
- DB-hotstore-stress: max-num-nodes=120: decode_failures 33
- DB-hotstore-stress: max-num-nodes=250: decode_failures 64
- DB-warm: warm-num-nodes=0: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 105
- DB-warm: warm-num-nodes=25: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 105
- DB-warm: warm-num-nodes=100: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 105
- DB-warm: warm-num-nodes=2000: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 105
- DG-burst: burst-loss=0.2: decode_failures 4
- DG-burst: burst-loss=0.3: decode_failures 27
- DG-loss: extra-loss=0.3: decode_failures 4
- DG-outage: burst-loss=0.1: decode_failures 45
- DG-outage: burst-loss=0.2: decode_failures 29
- DG-outage: burst-loss=0.3: decode_failures 33
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 9
- LD-chatty: broadcast-interval-s=300: decode_failures 23
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 14.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 105
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 25.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 93
- MS-density: nodes=40: decode_failures 1
- MS-hopscale: nodes=250: decode_failures 98
- MS-hopscale: nodes=500: decode_failures 7
- MS-oversubscribed: nodes=250: decode_failures 33
- MS-oversubscribed: nodes=500: decode_failures 12
- MS-size: nodes=40: decode_failures 11
- MS-stretch: stretch=1.25: decode_failures 1
- MS-stretch: stretch=2.0: 3 archives requested, 2 placed - group on the placed count
- RF-bw500: preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count
- RF-eu-presets: preset=SHORT_FAST: decode_failures 2
- RF-preset: preset=SHORT_FAST: decode_failures 2
- RF-preset-turbo: preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-stretch-duct: faster: 0.772 s per simulated hour against 2.28 over 32 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=22: decode_failures 1
- RF-txpower: tx-power=17: decode_failures 2
- RF-txpower: tx-power=14: 3 archives requested, 2 placed - group on the placed count
- SF-bucket-mode: bucket-mode=global: misdecodes 35
- SF-bucket-mode: bucket-mode=time: misdecodes 37
- SF-bucket-mode: bucket-mode=window: misdecodes 29
- SF-bucket-time: time-bucket-s=600: misdecodes 114
- SF-bucket-time: time-bucket-s=1800: misdecodes 37
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-cadence: trigger=interval: misdecodes 16
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 11
- SF-capacity-local: capacity=4: decode_failures 91
- SF-capacity-local: capacity=8: decode_failures 22
- SF-capacity: capacity=4: decode_failures 91
- SF-capacity: capacity=8: decode_failures 22
- SF-capacity-window: capacity=8: misdecodes 23
- SF-capacity-window: capacity=8: decode_failures 23
- SF-capacity-window: capacity=16: misdecodes 20
- SF-capacity-window: capacity=32: misdecodes 29
- SF-catchup: catch-up-hours=: misdecodes 11
- SF-catchup: catch-up-hours=02-06: decode_failures 8
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 5
- SF-hops-flat: hops-apart=3: decode_failures 39
- SF-hops-flat: hops-apart=4: decode_failures 33
- SF-hops-spread: hops-apart=3: decode_failures 39
- SF-hops-spread: hops-apart=4: decode_failures 33
- SF-hops-spread: hops-apart=5: decode_failures 34
- SF-place-flat: place=spread: decode_failures 31
- SF-place-flat: place=random-clients: decode_failures 6
- SF-place-spread: place=spread: decode_failures 31
- SF-place-spread: place=random-clients: decode_failures 6
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 9
- SF-replay-order: replay-ordering=heard: misdecodes 14
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 133
- SF-window-size: window-size=16: misdecodes 72
- SF-window-size: window-size=32: misdecodes 29
- TH-congestion-input: congestion-input=hotstore: decode_failures 33
- TH-congestion-input: congestion-input=truesize: decode_failures 46
- TH-congestion-input: slower: 28.2 s per simulated hour against 10.4 over 32 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: queue drops 13.7% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 106

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 17.9 | 3.48 | 5.14x | 32 |
| `BL-control` | 5.27 | 1.72 | 3.06x | 32 |
| `TH-congestion-input` | 28.2 | 10.4 | 2.71x | 32 |
| `SF-hops-spread` | 7.77 | 4.42 | 1.76x | 32 |
| `MS-siting` | 1.27 | 1.92 | 0.66x | 31 |
| `MS-stretch` | 1.33 | 2.02 | 0.66x | 32 |
| `SF-advert-transport` | 1.16 | 1.77 | 0.66x | 32 |
| `RF-noise` | 3.31 | 5.27 | 0.63x | 32 |
| `RF-bw500` | 1.07 | 1.85 | 0.58x | 32 |
| `SF-catchup` | 5.33 | 9.41 | 0.57x | 32 |
| `SF-cadence` | 1.92 | 3.41 | 0.56x | 32 |
| `MS-topology` | 1.08 | 1.94 | 0.56x | 32 |
| `RF-preset` | 1.58 | 2.99 | 0.53x | 32 |
| `RF-stretch-duct` | 0.772 | 2.28 | 0.34x | 32 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.980 | 0.980 | 0.854 → 0.861 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.919 | 0.919 | 0.858 → 0.865 | 1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.074 → 0.980 | 0.905 | 0.080 → 0.861 | 55x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.079 → 0.980 | 0.901 | 0.110 → 0.861 | 75x sr_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.082 → 0.980 | 0.897 | 0.061 → 0.861 | 56x sr_bytes | up | 5 |
| `RF-eu-presets` | preset | **held** | 0.144 → 0.980 | 0.835 | 0.243 → 0.861 | 21x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.144 → 0.980 | 0.835 | 0.243 → 0.861 | 26x sr_airtime | up | 3 |
| `RF-bw500` | preset | **held** | 0.082 → 0.901 | 0.819 | 0.134 → 0.771 | 56x sr_bytes | up | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.121 → 0.926 | 0.804 | 0.102 → 0.806 | 1e+02x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.290 → 0.978 | 0.688 | 0.289 → 0.978 | 3.5x sr_airtime | up | 4 |
| `AD-siting` | siting-mix | **text** | 0.080 → 0.755 | 0.676 | 0.078 → 0.744 | 3.7x advert_bytes | down | 3 |
| `MS-hopscale` | nodes | **text** | 0.328 → 0.872 | 0.544 | 0.324 → 0.861 | 11x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.329 → 0.779 | 0.450 | 0.325 → 0.770 | 4.7x bytes_on_air | down | 3 |
| `MS-topology` | topology | **text** | 0.559 → 0.958 | 0.399 | 0.550 → 0.957 | 1.7x sr_bytes | up | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.291 → 0.663 | 0.372 | 0.284 → 0.648 | 2.2x sr_airtime | up | 2 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.418 → 0.784 | 0.366 | 0.323 → 0.540 | 7.2x sr_airtime | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.580 → 0.925 | 0.345 | 0.567 → 0.923 | 8.7x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.534 → 0.872 | 0.338 | 0.506 → 0.861 | 2.3x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.555 → 0.886 | 0.331 | 0.535 → 0.880 | 7.3x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.564 → 0.872 | 0.308 | 0.527 → 0.861 | 1.9x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.691 → 0.971 | 0.280 | 0.677 → 0.969 | 6x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.685 → 0.927 | 0.242 | 0.640 → 0.927 | 2.7x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.685 → 0.913 | 0.228 | 0.640 → 0.910 | 2.2x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.742 → 0.965 | 0.223 | 0.736 → 0.963 | 3.7x sr_airtime | down | 2 |
| `RT-spread` | hop-spread | **text** | 0.685 → 0.872 | 0.187 | 0.640 → 0.861 | 1.7x sr_bytes | up | 2 |
| `AD-flooding` | role-mix | **text** | 0.755 → 0.917 | 0.162 | 0.744 → 0.911 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.755 → 0.917 | 0.162 | 0.744 → 0.911 | 2.3x bytes_on_air | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.717 → 0.872 | 0.155 | 0.706 → 0.861 | 1.4x sr_bytes | down | 4 |
| `MS-size` | nodes | **held** | 0.848 → 0.980 | 0.132 | 0.737 → 0.861 | 4.3x sr_airtime | up | 5 |
| `SC-signing` | signature-policy | **text** | 0.745 → 0.872 | 0.127 | 0.745 → 0.861 | 1.2x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.749 → 0.872 | 0.123 | 0.731 → 0.861 | 1.4x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.798 → 0.912 | 0.114 | 0.784 → 0.907 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.807 → 0.912 | 0.104 | 0.795 → 0.907 | 2.2x sr_airtime | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.812 → 0.914 | 0.102 | 0.798 → 0.909 | 5x sr_airtime | up | 4 |
| `MS-roles` | role-mix | **text** | 0.755 → 0.854 | 0.098 | 0.744 → 0.843 | 1.1x advert_bytes | down | 2 |
| `SF-place-flat` | place | **held** | 0.896 → 0.981 | 0.085 | 0.856 → 0.870 | 3.8x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.896 → 0.981 | 0.085 | 0.856 → 0.870 | 3.8x sr_bytes | up | 6 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.653 → 0.736 | 0.083 | 0.648 → 0.730 | 1.5x sr_airtime | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.872 → 0.954 | 0.082 | 0.861 → 0.953 | 1.6x sr_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.891 → 0.964 | 0.073 | 0.800 → 0.870 | 1.1x advert_bytes | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.872 → 0.938 | 0.066 | 0.861 → 0.932 | 1.6x sr_bytes | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.914 → 0.980 | 0.065 | 0.861 → 0.868 | 25x sr_airtime | down | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.917 → 0.980 | 0.062 | 0.854 → 0.867 | 3.9x sr_bytes | down | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.919 → 0.980 | 0.060 | 0.854 → 0.865 | 3.1x sr_bytes | down | 4 |
| `AD-badrouters` | role-placement | **held** | 0.868 → 0.926 | 0.058 | 0.744 → 0.797 | 1.2x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.872 → 0.930 | 0.058 | 0.861 → 0.924 | 1.2x bytes_on_air | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.818 → 0.872 | 0.054 | 0.802 → 0.861 | 1.5x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.932 → 0.980 | 0.048 | 0.841 → 0.861 | 13x sr_bytes | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.872 → 0.908 | 0.036 | 0.861 → 0.902 | 3.4x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.872 → 0.907 | 0.035 | 0.861 → 0.901 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.872 → 0.906 | 0.034 | 0.861 → 0.901 | 2x sr_bytes | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.841 → 0.872 | 0.031 | 0.824 → 0.861 | 1.1x sr_airtime | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.872 → 0.901 | 0.029 | 0.861 → 0.867 | 2.3x sr_airtime | up | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.557 → 0.586 | 0.029 | 0.537 → 0.566 | 1.4x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **held** | 0.764 → 0.792 | 0.027 | 0.824 → 0.837 | 1.2x sr_bytes | down | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.942 → 0.967 | 0.025 | 0.841 → 0.865 | 9.3x advert_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.964 → 0.988 | 0.024 | 0.854 → 0.873 | 1.3x sr_bytes | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.823 → 0.842 | 0.019 | 0.823 → 0.842 | 1.2x sr_airtime | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.879 → 0.898 | 0.019 | 0.871 → 0.889 | 1.1x sr_bytes | up | 2 |
| `FW-versions` | profile | **text** | 0.872 → 0.891 | 0.019 | 0.861 → 0.884 | 3.1x bytes_on_air | down | 5 |
| `LD-diurnal` | diurnal | **text** | 0.872 → 0.889 | 0.017 | 0.861 → 0.882 | 1.4x sr_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.963 → 0.980 | 0.017 | 0.859 → 0.871 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.963 → 0.980 | 0.017 | 0.859 → 0.871 | 5.4x advert_bytes | up | 5 |
| `FW-firmware` | profile | **text** | 0.872 → 0.888 | 0.016 | 0.861 → 0.879 | 3x bytes_on_air | down | 2 |
| `SF-width` | short-id-bits | **text** | 0.870 → 0.885 | 0.015 | 0.861 → 0.876 | 3.2x advert_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.860 → 0.875 | 0.015 | 0.851 → 0.867 | 5.1x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.966 → 0.980 | 0.014 | 0.861 → 0.874 | 1.3x bytes_on_air | down | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.969 → 0.981 | 0.012 | 0.855 → 0.867 | 1x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.831 → 0.842 | 0.011 | 0.831 → 0.842 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.969 → 0.980 | 0.011 | 0.861 → 0.868 | 2.5x advert_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.973 → 0.983 | 0.010 | 0.863 → 0.874 | 2.5x advert_bytes | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.971 → 0.980 | 0.009 | 0.855 → 0.868 | 5.8x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.971 → 0.980 | 0.009 | 0.855 → 0.868 | 5.8x sr_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.972 → 0.981 | 0.009 | 0.856 → 0.863 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.972 → 0.981 | 0.009 | 0.856 → 0.863 | 1.2x sr_airtime | up | 4 |
| `SF-window-size` | window-size | **held** | 0.970 → 0.979 | 0.009 | 0.857 → 0.863 | 4.7x advert_bytes | up | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.972 → 0.980 | 0.008 | 0.861 → 0.862 | 1.1x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.872 → 0.878 | 0.006 | 0.861 → 0.868 | 2.6x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.971 → 0.976 | 0.006 | 0.855 → 0.864 | 2.3x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.959 → 0.965 | 0.005 | 0.958 → 0.963 | 1.1x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.831 → 0.835 | 0.004 | 0.831 → 0.835 | 1.1x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.872 → 0.875 | 0.003 | 0.861 → 0.867 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.998 → 0.999 | 0.001 | 0.963 → 0.964 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.965 → 0.965 | 0.001 | 0.963 → 0.964 | 1x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **text** | 0.872 → 0.872 | 0.000 | 0.861 → 0.862 | 5.7x advert_bytes | = | 3 |

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
| none | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| sprinkled | 1 | 0.927 | 0.922 | 0.005 | - | - | 0.969 | 0.970 | 0.698 | 1.20x | 17.0/23.2/28.9% | 1.8/5.2% | 3 |
| arms-race | 1 | 0.954 | 0.953 | 0.001 | - | - | 0.977 | 0.978 | 0.881 | 0.93x | 21.3/27.3/29.6% | 1.1/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario coastal`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.1 | 1 | 0.916 | 0.905 | 0.011 | - | - | 0.990 | 0.991 | 0.773 | 1.14x | 17.6/22.3/27.9% | 1.6/4.8% | 3 |
| 0.3 | 1 | 0.930 | 0.924 | 0.006 | - | - | 0.990 | 0.990 | 0.859 | 1.08x | 20.5/26.2/29.5% | 1.6/4.3% | 3 |

### `AD-badrouters` - role-placement  `--scenario coastal`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.755 | 0.744 | 0.011 | - | - | 0.868 | 0.870 | 0.340 | 1.18x | 14.7/22.0/25.9% | 2.0/5.0% | 3 |
| inverse | 1 | 0.795 | 0.782 | 0.013 | - | - | 0.920 | 0.922 | 0.505 | 1.16x | 13.7/19.4/22.8% | 2.1/3.5% | 3 |
| random | 1 | 0.811 | 0.797 | 0.013 | - | - | 0.926 | 0.927 | 0.526 | 1.06x | 12.6/18.9/23.6% | 1.8/4.6% | 3 |

### `AD-flooding` - role-mix  `--scenario coastal`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.755 | 0.744 | 0.011 | - | - | 0.868 | 0.870 | 0.340 | 1.18x | 14.7/22.0/25.9% | 2.0/5.0% | 3 |
| all-routers | 1 | 0.917 | 0.911 | 0.005 | - | - | 0.995 | 0.995 | 0.764 | 2.72x | 30.0/37.2/41.4% | 4.5/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario coastal`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.755 | 0.744 | 0.011 | - | - | 0.868 | 0.870 | 0.340 | 1.18x | 14.7/22.0/25.9% | 2.0/5.0% | 3 |
| no-mute | 1 | 0.852 | 0.841 | 0.011 | - | - | 0.959 | 0.960 | 0.596 | 1.29x | 15.6/21.8/25.6% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.917 | 0.911 | 0.005 | - | - | 0.995 | 0.995 | 0.764 | 2.72x | 30.0/37.2/41.4% | 4.5/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario coastal`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.755 | 0.744 | 0.011 | - | - | 0.868 | 0.870 | 0.340 | 1.18x | 14.7/22.0/25.9% | 2.0/5.0% | 3 |
| local-typical | 1 | 0.449 | 0.447 | 0.002 | - | - | 0.612 | 0.613 | 0.000 | 1.13x | 8.7/21.8/28.2% | 1.7/4.7% | 3 |
| basement-heavy | 1 | 0.080 | 0.078 | 0.001 | - | - | 0.249 | 0.251 | 0.000 | 0.55x | 1.2/6.5/10.2% | 0.4/3.1% | 3 |

> siting-mix=basement-heavy: decode_failures 2

### `AD-worst` - role-placement  `--scenario coastal`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.841 | 0.837 | 0.004 | - | - | 0.792 | 0.937 | 0.000 | 2.17x | 21.6/32.1/39.0% | 1.6/5.4% | 3 |
| inverse | 1 | 0.829 | 0.824 | 0.005 | - | - | 0.764 | 0.937 | 0.000 | 2.07x | 18.5/25.5/32.5% | 1.6/3.2% | 3 |

> role-placement=degree: decode_failures 64

> role-placement=inverse: decode_failures 46

> slower: 17.9 s per simulated hour against 3.48 over 32 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario coastal`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.858 | 0.858 | 0.000 | - | - | 0 | 0.000 | 0.589 | 1.23x | 14.7/21.5/25.4% | 1.8/5.0% | 3 |
| sr | 1 | 0.878 | 0.865 | 0.014 | - | - | 0.919 | 0.973 | 0.562 | 1.27x | 15.6/22.3/26.3% | 1.9/5.3% | 3 |

> protocol=sr: decode_failures 39

> slower: 5.27 s per simulated hour against 1.72 over 32 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario coastal`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.807 | 0.795 | 0.012 | - | - | 0.912 | 0.919 | 0.571 | 2.97x | 35.8/50.7/55.9% | 4.3/9.8% | 3 |
| 100 | 1 | 0.912 | 0.907 | 0.005 | - | - | 0.969 | 0.970 | 0.667 | 1.49x | 18.3/26.4/29.4% | 2.2/5.0% | 3 |
| 120 | 1 | 0.912 | 0.907 | 0.005 | - | - | 0.969 | 0.970 | 0.667 | 1.49x | 18.3/26.4/29.4% | 2.2/5.0% | 3 |
| 250 | 1 | 0.912 | 0.907 | 0.005 | - | - | 0.969 | 0.970 | 0.667 | 1.49x | 18.3/26.4/29.4% | 2.2/5.0% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario coastal`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.331 | 0.323 | 0.008 | - | - | 0.418 | 0.545 | 0.191 | 11.48x | 40.8/57.6/67.3% | 3.9/10.4% | 3 |
| 120 | 1 | 0.557 | 0.537 | 0.020 | - | - | 0.784 | 0.799 | 0.272 | 4.42x | 16.0/26.7/33.9% | 1.4/5.1% | 3 |
| 250 | 1 | 0.559 | 0.540 | 0.019 | - | - | 0.754 | 0.808 | 0.265 | 4.33x | 15.7/25.8/32.6% | 1.4/4.8% | 3 |

> max-num-nodes=10: decode_failures 40

> max-num-nodes=120: decode_failures 33

> max-num-nodes=250: decode_failures 64

### `DB-platform` - platform-mix  `--scenario coastal`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.912 | 0.907 | 0.005 | - | - | 0.969 | 0.970 | 0.667 | 1.49x | 18.3/26.4/29.4% | 2.2/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.912 | 0.907 | 0.005 | - | - | 0.969 | 0.970 | 0.667 | 1.49x | 18.3/26.4/29.4% | 2.2/5.0% | 3 |
| constrained | 1 | 0.798 | 0.784 | 0.014 | - | - | 0.914 | 0.918 | 0.551 | 2.97x | 35.7/50.8/56.0% | 4.3/9.8% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario coastal`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.736 | 0.730 | 0.005 | - | - | 0.860 | 0.886 | 0.574 | 5.42x | 57.3/76.1/78.9% | 3.8/11.8% | 3 |
| 25 | 1 | 0.736 | 0.730 | 0.005 | - | - | 0.860 | 0.886 | 0.574 | 5.42x | 57.3/76.1/78.9% | 3.8/11.8% | 3 |
| 100 | 1 | 0.736 | 0.730 | 0.005 | - | - | 0.860 | 0.886 | 0.574 | 5.42x | 57.3/76.1/78.9% | 3.8/11.8% | 3 |
| 2000 | 1 | 0.736 | 0.730 | 0.005 | - | - | 0.860 | 0.886 | 0.574 | 5.42x | 57.3/76.1/78.9% | 3.8/11.8% | 3 |

> warm-num-nodes=0: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 105

> warm-num-nodes=25: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 105

> warm-num-nodes=100: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 105

> warm-num-nodes=2000: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 105

### `DG-burst` - burst-loss  `--scenario coastal`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.1 | 1 | 0.774 | 0.754 | 0.019 | - | - | 0.952 | 0.960 | 0.497 | 1.20x | 14.7/21.3/25.3% | 1.8/4.7% | 3 |
| 0.2 | 1 | 0.677 | 0.648 | 0.029 | - | - | 0.902 | 0.927 | 0.386 | 1.12x | 13.9/20.5/24.0% | 1.7/4.2% | 3 |
| 0.3 | 1 | 0.564 | 0.527 | 0.037 | - | - | 0.780 | 0.856 | 0.324 | 1.03x | 13.1/19.3/22.8% | 1.5/3.8% | 3 |

> burst-loss=0.2: decode_failures 4

> burst-loss=0.3: decode_failures 27

### `DG-loss` - extra-loss  `--scenario coastal`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.1 | 1 | 0.835 | 0.822 | 0.013 | - | - | 0.966 | 0.969 | 0.547 | 1.30x | 16.0/23.1/27.0% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.799 | 0.780 | 0.019 | - | - | 0.965 | 0.971 | 0.491 | 1.37x | 17.0/24.2/28.2% | 2.0/4.8% | 3 |
| 0.3 | 1 | 0.749 | 0.731 | 0.018 | - | - | 0.919 | 0.947 | 0.441 | 1.40x | 17.6/24.9/28.8% | 2.0/4.7% | 3 |

> extra-loss=0.3: decode_failures 4

### `DG-outage` - burst-loss  `--scenario coastal`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.1 | 1 | 0.764 | 0.748 | 0.016 | - | - | 0.955 | 0.966 | 0.509 | 1.19x | 14.7/21.1/25.2% | 1.8/4.8% | 3 |
| 0.2 | 1 | 0.640 | 0.617 | 0.023 | - | - | 0.777 | 0.894 | 0.382 | 1.10x | 13.6/19.9/24.1% | 1.7/3.9% | 3 |
| 0.3 | 1 | 0.534 | 0.506 | 0.028 | - | - | 0.781 | 0.876 | 0.282 | 1.05x | 13.3/19.5/23.2% | 1.5/4.0% | 3 |

> burst-loss=0.1: decode_failures 45

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 33

### `DM-mode` - dm-mode  `--scenario coastal`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.823 | 0.823 | 0.000 | - | - | 0.958 | 0.968 | 0.535 | 1.68x | 20.3/29.2/34.6% | 2.5/6.8% | 3 |
| directed-with-late-flood | 1 | 0.842 | 0.842 | 0.000 | - | - | 0.966 | 0.973 | 0.555 | 1.52x | 18.5/26.7/31.7% | 2.3/6.2% | 3 |
| m4-early-flood | 1 | 0.833 | 0.833 | 0.000 | - | - | 0.955 | 0.965 | 0.556 | 1.52x | 18.4/26.8/32.0% | 2.3/6.3% | 3 |

### `FW-firmware` - profile  `--scenario coastal`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.888 | 0.879 | 0.009 | - | - | 0.988 | 0.989 | 0.606 | 0.76x | 9.2/11.6/13.2% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario coastal`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.25 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.981 | 0.982 | 0.716 | 1.14x | 14.8/21.4/24.0% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.885 | 0.875 | 0.010 | - | - | 0.975 | 0.977 | 0.733 | 0.97x | 11.9/17.2/20.2% | 1.4/4.3% | 3 |
| 0.75 | 1 | 0.906 | 0.895 | 0.011 | - | - | 0.984 | 0.987 | 0.689 | 0.90x | 11.5/15.7/17.8% | 1.4/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario coastal`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.25 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.984 | 0.985 | 0.717 | 1.12x | 14.7/21.2/23.8% | 1.6/4.7% | 3 |
| 0.5 | 1 | 0.885 | 0.874 | 0.010 | - | - | 0.977 | 0.980 | 0.752 | 0.97x | 12.2/17.3/20.7% | 1.4/4.4% | 3 |
| 0.75 | 1 | 0.902 | 0.892 | 0.010 | - | - | 0.986 | 0.987 | 0.652 | 0.84x | 11.0/15.1/17.4% | 1.3/3.4% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario coastal`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.908 | 0.902 | 0.006 | - | - | 0.992 | 0.992 | 0.608 | 0.66x | 8.1/12.2/14.8% | 1.0/2.9% | 3 |
| signing=true | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `FW-versions` - profile  `--scenario coastal`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.883 | 0.876 | 0.007 | - | - | 0.989 | 0.993 | 0.625 | 0.75x | 9.5/12.4/14.0% | 1.2/2.6% | 3 |
| 2.5 | 1 | 0.882 | 0.873 | 0.009 | - | - | 0.988 | 0.988 | 0.625 | 0.76x | 9.6/12.5/14.2% | 1.2/2.6% | 3 |
| 2.6 | 1 | 0.880 | 0.872 | 0.008 | - | - | 0.987 | 0.988 | 0.617 | 0.73x | 9.4/12.6/14.0% | 1.2/2.7% | 3 |
| 2.7 | 1 | 0.891 | 0.884 | 0.007 | - | - | 0.990 | 0.991 | 0.592 | 0.75x | 10.0/13.7/14.7% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.886 | 0.880 | 0.007 | - | - | 0.982 | 0.983 | 0.603 | 0.84x | 10.2/14.4/17.3% | 1.3/3.4% | 3 |
| 900 | 1 | 0.812 | 0.798 | 0.014 | - | - | 0.953 | 0.956 | 0.474 | 2.05x | 24.7/35.7/42.0% | 3.1/8.2% | 3 |
| 300 | 1 | 0.555 | 0.535 | 0.020 | - | - | 0.756 | 0.854 | 0.320 | 4.39x | 50.9/67.7/75.3% | 6.5/15.8% | 3 |

> broadcast-interval-s=300: decode_failures 23

### `LD-chatty-hops` - broadcast-interval-s  `--scenario coastal`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.925 | 0.923 | 0.002 | - | - | 0.978 | 0.979 | 0.702 | 0.91x | 10.9/14.7/17.8% | 1.4/3.4% | 3 |
| 900 | 1 | 0.870 | 0.864 | 0.007 | - | - | 0.963 | 0.964 | 0.657 | 2.26x | 26.7/36.7/43.3% | 3.4/8.4% | 3 |
| 300 | 1 | 0.580 | 0.567 | 0.013 | - | - | 0.770 | 0.846 | 0.352 | 4.94x | 54.8/70.6/77.5% | 7.4/17.0% | 3 |

> broadcast-interval-s=300: decode_failures 9

### `LD-diurnal` - diurnal  `--scenario coastal`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.889 | 0.882 | 0.007 | - | - | 0.982 | 0.983 | 0.604 | 1.16x | 13.9/20.1/24.1% | 1.7/4.8% | 3 |
| sinusoid | 1 | 0.879 | 0.870 | 0.009 | - | - | 0.986 | 0.988 | 0.559 | 1.14x | 13.7/19.8/23.6% | 1.7/4.6% | 3 |
| commuter | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.812 | 0.798 | 0.014 | - | - | 0.953 | 0.956 | 0.474 | 2.05x | 24.7/35.7/42.0% | 3.1/8.2% | 3 |
| 3600 | 1 | 0.886 | 0.880 | 0.007 | - | - | 0.982 | 0.983 | 0.603 | 0.84x | 10.2/14.4/17.3% | 1.3/3.4% | 3 |
| 10800 | 1 | 0.910 | 0.906 | 0.004 | - | - | 0.994 | 0.994 | 0.619 | 0.57x | 7.0/9.7/11.8% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.914 | 0.909 | 0.004 | - | - | 0.993 | 0.993 | 0.640 | 0.40x | 4.8/6.7/8.2% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario coastal`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.25 | 1 | 0.869 | 0.859 | 0.010 | - | - | 0.979 | 0.979 | 0.556 | 1.32x | 16.0/23.2/27.7% | 2.0/5.4% | 3 |
| 1.0 | 1 | 0.864 | 0.854 | 0.010 | - | - | 0.977 | 0.977 | 0.581 | 1.45x | 17.7/25.6/30.6% | 2.2/6.0% | 3 |
| 4.0 | 1 | 0.818 | 0.802 | 0.015 | - | - | 0.954 | 0.955 | 0.524 | 1.82x | 22.4/33.0/39.5% | 2.7/7.8% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario coastal`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.736 | 0.730 | 0.005 | - | - | 0.860 | 0.886 | 0.574 | 5.42x | 57.3/76.1/78.9% | 3.8/11.8% | 3 |
| 1.0 | 1 | 0.653 | 0.648 | 0.005 | - | - | 0.786 | 0.833 | 0.489 | 6.00x | 61.4/78.0/80.3% | 4.4/13.5% | 3 |

> traceroute-per-hour=0.0: queue drops 14.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 105

> traceroute-per-hour=1.0: queue drops 25.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 93

### `MS-density` - nodes  `--scenario coastal`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.691 | 0.677 | 0.014 | - | - | 0.833 | 0.877 | 0.307 | 1.24x | 17.2/20.3/27.1% | 2.7/6.5% | 3 |
| 60 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 90 | 1 | 0.950 | 0.948 | 0.002 | - | - | 0.995 | 0.996 | 0.856 | 1.69x | 19.9/31.0/35.1% | 1.5/5.1% | 3 |
| 120 | 1 | 0.965 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.868 | 2.09x | 24.0/40.7/44.7% | 1.4/5.1% | 3 |
| 150 | 1 | 0.971 | 0.969 | 0.002 | - | - | 0.998 | 0.998 | 0.843 | 2.53x | 28.8/47.1/52.2% | 1.2/5.6% | 3 |

> nodes=40: decode_failures 1

### `MS-hopscale` - nodes  `--scenario coastal`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 120 | 1 | 0.777 | 0.768 | 0.008 | - | - | 0.929 | 0.932 | 0.486 | 2.08x | 15.1/22.7/27.0% | 1.5/5.1% | 3 |
| 250 | 1 | 0.552 | 0.532 | 0.019 | - | - | 0.745 | 0.788 | 0.251 | 4.62x | 17.0/27.6/34.8% | 1.5/5.2% | 3 |
| 500 | 1 | 0.328 | 0.324 | 0.004 | - | - | 0.488 | 0.489 | 0.111 | 9.90x | 20.0/29.6/41.3% | 1.7/6.2% | 3 |

> nodes=250: decode_failures 98

> nodes=500: decode_failures 7

### `MS-oversubscribed` - nodes  `--scenario coastal`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.779 | 0.770 | 0.009 | - | - | 0.932 | 0.933 | 0.507 | 2.02x | 14.7/22.0/26.0% | 1.4/4.9% | 3 |
| 250 | 1 | 0.557 | 0.537 | 0.020 | - | - | 0.784 | 0.799 | 0.272 | 4.42x | 16.0/26.7/33.9% | 1.4/5.1% | 3 |
| 500 | 1 | 0.329 | 0.325 | 0.004 | - | - | 0.486 | 0.486 | 0.110 | 9.32x | 18.8/27.8/38.8% | 1.6/5.8% | 3 |

> nodes=250: decode_failures 33

> nodes=500: decode_failures 12

### `MS-roles` - role-mix  `--scenario coastal`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.854 | 0.843 | 0.010 | - | - | 0.966 | 0.967 | 0.579 | 1.28x | 15.6/22.3/26.6% | 1.9/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.755 | 0.744 | 0.011 | - | - | 0.868 | 0.870 | 0.340 | 1.18x | 14.7/22.0/25.9% | 2.0/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario coastal`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.878 | 0.870 | 0.008 | - | - | 0.964 | 0.965 | 0.636 | 1.32x | 16.0/22.1/26.5% | 2.0/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.809 | 0.800 | 0.010 | - | - | 0.891 | 0.893 | 0.385 | 1.33x | 16.3/24.0/28.0% | 2.4/5.0% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario coastal`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.05 | 1 | 0.875 | 0.866 | 0.009 | - | - | 0.977 | 0.977 | 0.574 | 1.33x | 16.2/24.4/29.3% | 1.9/5.1% | 3 |
| 0.1 | 1 | 0.883 | 0.874 | 0.009 | - | - | 0.971 | 0.971 | 0.596 | 1.50x | 18.2/27.8/31.6% | 2.0/5.1% | 3 |
| 0.2 | 1 | 0.879 | 0.872 | 0.007 | - | - | 0.966 | 0.966 | 0.616 | 1.67x | 22.0/30.9/34.4% | 2.2/5.1% | 3 |

### `MS-siting` - siting-mix  `--scenario coastal`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| local-typical | 1 | 0.574 | 0.572 | 0.002 | - | - | 0.699 | 0.699 | 0.000 | 1.40x | 10.2/24.0/31.0% | 2.0/4.6% | 3 |
| event | 1 | 0.290 | 0.289 | 0.001 | - | - | 0.501 | 0.503 | 0.000 | 1.45x | 7.2/16.6/30.5% | 2.0/5.3% | 3 |
| backbone | 1 | 0.978 | 0.978 | 0.000 | - | - | 0.999 | 0.999 | 0.920 | 1.03x | 27.6/36.2/37.9% | 1.1/5.4% | 3 |

### `MS-size` - nodes  `--scenario coastal`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.829 | 0.814 | 0.014 | - | - | 0.848 | 0.923 | 0.397 | 1.49x | 24.5/34.4/35.3% | 3.3/7.5% | 3 |
| 60 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 90 | 1 | 0.809 | 0.796 | 0.013 | - | - | 0.973 | 0.977 | 0.548 | 1.62x | 15.5/21.8/27.5% | 1.5/4.6% | 3 |
| 120 | 1 | 0.777 | 0.768 | 0.008 | - | - | 0.929 | 0.932 | 0.486 | 2.08x | 15.1/22.7/27.0% | 1.5/5.1% | 3 |
| 150 | 1 | 0.747 | 0.737 | 0.010 | - | - | 0.867 | 0.869 | 0.319 | 2.75x | 15.9/28.7/32.7% | 1.5/5.5% | 3 |

> nodes=40: decode_failures 11

### `MS-stretch` - stretch  `--scenario coastal`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 1.25 | 1 | 0.595 | 0.581 | 0.014 | - | - | 0.757 | 0.764 | 0.269 | 1.22x | 11.0/16.5/21.5% | 1.9/4.8% | 3 |
| 1.5 | 1 | 0.291 | 0.284 | 0.007 | - | - | 0.516 | 0.517 | 0.103 | 1.18x | 8.5/12.4/15.5% | 1.9/4.3% | 3 |
| 2.0 | 1 | 0.110 | 0.110 | 0.000 | - | - | 0.079 | 0.158 | 0.000 | 0.76x | 3.7/5.6/8.7% | 1.2/2.5% | 2 |

> stretch=1.25: decode_failures 1

> stretch=2.0: 3 archives requested, 2 placed - group on the placed count

### `MS-topology` - topology  `--scenario coastal`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| clustered | 1 | 0.914 | 0.905 | 0.009 | - | - | 0.972 | 0.974 | 0.000 | 1.00x | 19.4/26.1/28.2% | 1.3/5.3% | 3 |
| corridor | 1 | 0.559 | 0.550 | 0.009 | - | - | 0.770 | 0.775 | 0.287 | 1.34x | 14.4/24.6/30.1% | 1.9/5.5% | 3 |
| hub | 1 | 0.958 | 0.957 | 0.001 | - | - | 0.980 | 0.980 | 0.895 | 1.16x | 29.0/36.9/38.0% | 1.5/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario coastal`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.842 | 0.842 | 0.000 | - | - | 0.966 | 0.973 | 0.555 | 1.52x | 18.5/26.7/31.7% | 2.3/6.2% | 3 |
| True | 1 | 0.831 | 0.831 | 0.000 | - | - | 0.963 | 0.973 | 0.551 | 1.53x | 18.5/27.0/32.3% | 2.3/6.3% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario coastal`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.831 | 0.831 | 0.000 | - | - | 0.963 | 0.973 | 0.551 | 1.53x | 18.5/27.0/32.3% | 2.3/6.3% | 3 |
| m4-early-flood | 1 | 0.835 | 0.835 | 0.000 | - | - | 0.963 | 0.973 | 0.534 | 1.55x | 18.7/27.3/32.5% | 2.3/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario coastal`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.858 | 0.858 | 0.000 | - | - | 0 | 0.000 | 0.589 | 1.23x | 14.7/21.5/25.4% | 1.8/5.0% | 3 |
| chain | 1 | 0.856 | 0.854 | 0.002 | - | - | 0.915 | 0.972 | 0.607 | 1.43x | 17.4/25.1/30.0% | 2.2/5.8% | 3 |
| sr | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `PR-repeats` - extra-repeats  `--scenario coastal`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| True | 1 | 0.875 | 0.867 | 0.008 | - | - | 0.981 | 0.982 | 0.591 | 1.29x | 15.6/22.4/26.6% | 2.0/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario coastal`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.868 | 2.09x | 24.0/40.7/44.7% | 1.4/5.1% | 3 |
| True | 1 | 0.965 | 0.964 | 0.002 | - | - | 0.999 | 0.999 | 0.881 | 2.07x | 23.6/39.9/43.7% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario coastal`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.134 | 0.134 | 0.000 | - | - | 0.082 | 0.165 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.1% | 2 |
| MEDIUM_TURBO | 1 | 0.306 | 0.302 | 0.004 | - | - | 0.542 | 0.543 | 0.094 | 0.21x | 1.5/2.7/3.6% | 0.3/0.9% | 3 |
| LONG_TURBO | 1 | 0.775 | 0.771 | 0.004 | - | - | 0.901 | 0.901 | 0.448 | 1.24x | 12.3/18.3/22.9% | 1.8/4.9% | 3 |

> preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count

### `RF-duct` - duct-per-hour  `--scenario coastal`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 0.25 | 1 | 0.874 | 0.863 | 0.011 | - | - | 0.979 | 0.979 | 0.580 | 1.23x | 16.7/23.4/27.3% | 1.8/5.2% | 3 |
| 1.0 | 1 | 0.938 | 0.932 | 0.006 | - | - | 0.992 | 0.992 | 0.804 | 1.00x | 23.9/28.7/31.8% | 1.3/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario coastal`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.244 | 0.243 | 0.001 | - | - | 0.144 | 0.193 | 0.031 | 0.11x | 0.6/1.3/2.1% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| LITE_FAST | 1 | 0.817 | 0.810 | 0.006 | - | - | 0.962 | 0.965 | 0.452 | 0.96x | 10.5/16.4/19.7% | 1.4/3.9% | 3 |
| NARROW_SLOW | 1 | 0.854 | 0.846 | 0.008 | - | - | 0.964 | 0.964 | 0.542 | 1.25x | 14.1/21.4/24.3% | 1.9/5.0% | 3 |

> preset=SHORT_FAST: decode_failures 2

### `RF-noise` - noise-profile  `--scenario coastal`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| temporal | 1 | 0.773 | 0.756 | 0.017 | - | - | 0.952 | 0.953 | 0.405 | 1.24x | 14.9/22.0/26.3% | 1.8/4.9% | 3 |
| transient | 1 | 0.862 | 0.852 | 0.010 | - | - | 0.969 | 0.972 | 0.563 | 1.24x | 14.9/21.7/25.9% | 1.9/5.0% | 3 |
| periodic | 1 | 0.717 | 0.706 | 0.011 | - | - | 0.833 | 0.835 | 0.434 | 1.18x | 14.4/20.8/24.4% | 1.8/4.4% | 3 |

### `RF-preset` - preset  `--scenario coastal`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.244 | 0.243 | 0.001 | - | - | 0.144 | 0.193 | 0.031 | 0.11x | 0.6/1.3/2.1% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| LONG_MODERATE | 1 | 0.832 | 0.816 | 0.016 | - | - | 0.948 | 0.949 | 0.512 | 3.19x | 45.4/56.2/60.4% | 4.9/12.6% | 3 |

> preset=SHORT_FAST: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario coastal`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.061 | 0.061 | 0.000 | - | - | 0.162 | 0.166 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.134 | 0.134 | 0.000 | - | - | 0.082 | 0.165 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.1% | 2 |
| LONG_FAST | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| LONG_TURBO | 1 | 0.775 | 0.771 | 0.004 | - | - | 0.901 | 0.901 | 0.448 | 1.24x | 12.3/18.3/22.9% | 1.8/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.840 | 0.832 | 0.008 | - | - | 0.942 | 0.945 | 0.570 | 1.79x | 20.3/28.2/32.2% | 2.7/6.8% | 3 |

> preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count

### `RF-pulse` - noise-pulse-interval-ms  `--scenario coastal`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.817 | 0.806 | 0.011 | - | - | 0.926 | 0.926 | 0.539 | 1.24x | 15.0/21.8/25.8% | 1.9/4.9% | 3 |
| 10000 | 1 | 0.717 | 0.706 | 0.011 | - | - | 0.833 | 0.835 | 0.434 | 1.18x | 14.4/20.8/24.4% | 1.8/4.4% | 3 |
| 4000 | 1 | 0.443 | 0.438 | 0.004 | - | - | 0.525 | 0.582 | 0.254 | 1.02x | 12.8/18.5/21.7% | 1.5/3.4% | 3 |
| 2000 | 1 | 0.102 | 0.102 | 0.000 | - | - | 0.121 | 0.214 | 0.044 | 0.71x | 9.2/13.4/15.7% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario coastal`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.291 | 0.284 | 0.007 | - | - | 0.516 | 0.517 | 0.103 | 1.18x | 8.5/12.4/15.5% | 1.9/4.3% | 3 |
| 1.0 | 1 | 0.663 | 0.648 | 0.015 | - | - | 0.775 | 0.778 | 0.536 | 0.89x | 14.1/17.8/19.7% | 1.3/4.5% | 3 |

> faster: 0.772 s per simulated hour against 2.28 over 32 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario coastal`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 22 | 1 | 0.288 | 0.281 | 0.008 | - | - | 0.546 | 0.554 | 0.085 | 1.24x | 8.6/13.6/17.3% | 1.9/4.5% | 3 |
| 17 | 1 | 0.138 | 0.138 | 0.000 | - | - | 0.121 | 0.162 | 0.000 | 0.82x | 4.4/6.6/10.6% | 1.3/3.1% | 3 |
| 14 | 1 | 0.080 | 0.080 | 0.000 | - | - | 0.074 | 0.149 | 0.000 | 0.57x | 2.5/4.9/6.8% | 0.8/2.4% | 2 |

> tx-power=22: decode_failures 1

> tx-power=17: decode_failures 2

> tx-power=14: 3 archives requested, 2 placed - group on the placed count

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario coastal`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.868 | 2.09x | 24.0/40.7/44.7% | 1.4/5.1% | 3 |
| True | 1 | 0.959 | 0.958 | 0.002 | - | - | 0.997 | 0.997 | 0.855 | 2.40x | 27.0/44.3/48.8% | 1.6/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario coastal`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.879 | 0.871 | 0.009 | - | - | 0.979 | 0.980 | 0.602 | 1.34x | 16.3/24.4/28.9% | 1.8/5.1% | 3 |
| True | 1 | 0.898 | 0.889 | 0.009 | - | - | 0.982 | 0.982 | 0.625 | 1.41x | 16.9/24.9/29.3% | 2.0/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario coastal`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| random | 1 | 0.841 | 0.824 | 0.017 | - | - | 0.961 | 0.963 | 0.586 | 1.25x | 15.0/21.8/25.8% | 1.9/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario coastal`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.685 | 0.640 | 0.045 | - | - | 0.939 | 0.947 | 0.265 | 0.95x | 12.1/18.8/22.2% | 1.3/4.6% | 3 |
| 7 | 1 | 0.913 | 0.910 | 0.002 | - | - | 0.974 | 0.974 | 0.692 | 1.43x | 17.0/23.0/27.8% | 2.2/5.3% | 3 |
| 15 | 1 | 0.927 | 0.927 | 0.001 | - | - | 0.970 | 0.971 | 0.710 | 1.44x | 17.1/23.1/27.7% | 2.2/5.3% | 3 |
| 32 | 1 | 0.927 | 0.927 | 0.001 | - | - | 0.970 | 0.971 | 0.710 | 1.44x | 17.1/23.1/27.7% | 2.2/5.3% | 3 |

### `RT-hopspread` - hop-limit  `--scenario coastal`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.685 | 0.640 | 0.045 | - | - | 0.939 | 0.947 | 0.265 | 0.95x | 12.1/18.8/22.2% | 1.3/4.6% | 3 |
| 5 | 1 | 0.862 | 0.849 | 0.013 | - | - | 0.976 | 0.978 | 0.527 | 1.27x | 15.3/22.0/26.0% | 1.9/5.1% | 3 |
| 7 | 1 | 0.913 | 0.910 | 0.002 | - | - | 0.974 | 0.974 | 0.692 | 1.43x | 17.0/23.0/27.8% | 2.2/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario coastal`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| KNOWN_ONLY | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.868 | 0.868 | 0.000 | - | - | 0.914 | 0.977 | 0.568 | 1.20x | 14.4/21.0/24.9% | 1.7/4.9% | 3 |

### `RT-spread` - hop-spread  `--scenario coastal`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.685 | 0.640 | 0.045 | - | - | 0.939 | 0.947 | 0.265 | 0.95x | 12.1/18.8/22.2% | 1.3/4.6% | 3 |
| True | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `SC-signing` - signature-policy  `--scenario coastal`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| BALANCED | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| STRICT | 1 | 0.745 | 0.745 | 0.000 | - | - | 0.861 | 0.862 | 0.493 | 1.35x | 16.3/23.3/27.7% | 2.1/5.4% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario coastal`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| dm | 1 | 0.878 | 0.868 | 0.011 | - | - | 0.982 | 0.982 | 0.589 | 1.22x | 14.9/21.5/25.6% | 1.8/5.1% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario coastal`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.876 | 0.868 | 0.008 | - | - | 0.979 | 0.981 | 0.562 | 1.26x | 15.3/22.1/26.2% | 1.9/5.1% | 3 |
| local | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| time | 1 | 0.869 | 0.861 | 0.008 | - | - | 0.969 | 0.972 | 0.571 | 1.30x | 15.6/22.6/26.8% | 2.0/5.2% | 3 |
| window | 1 | 0.873 | 0.863 | 0.010 | - | - | 0.979 | 0.981 | 0.556 | 1.26x | 15.1/22.1/26.1% | 1.9/5.1% | 3 |

> bucket-mode=global: misdecodes 35

> bucket-mode=time: misdecodes 37

> bucket-mode=window: misdecodes 29

### `SF-bucket-time` - time-bucket-s  `--scenario coastal`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.860 | 0.851 | 0.009 | - | - | 0.972 | 0.973 | 0.568 | 1.40x | 16.9/24.3/28.9% | 2.1/5.7% | 3 |
| 1800 | 1 | 0.869 | 0.861 | 0.008 | - | - | 0.969 | 0.972 | 0.571 | 1.30x | 15.6/22.6/26.8% | 2.0/5.2% | 3 |
| 3600 | 1 | 0.875 | 0.867 | 0.009 | - | - | 0.981 | 0.987 | 0.577 | 1.27x | 15.3/22.2/26.4% | 1.9/5.2% | 3 |

> time-bucket-s=600: misdecodes 114

> time-bucket-s=1800: misdecodes 37

> time-bucket-s=3600: misdecodes 11

### `SF-cadence` - trigger  `--scenario coastal`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| interval | 1 | 0.852 | 0.841 | 0.011 | - | - | 0.963 | 0.973 | 0.543 | 1.72x | 21.1/30.5/36.2% | 2.6/7.6% | 3 |
| aimd | 1 | 0.863 | 0.861 | 0.002 | - | - | 0.932 | 0.983 | 0.556 | 1.28x | 15.4/22.3/26.4% | 1.9/5.2% | 3 |
| bucket+interval | 1 | 0.853 | 0.841 | 0.012 | - | - | 0.967 | 0.968 | 0.540 | 1.73x | 21.1/30.6/36.2% | 2.6/7.6% | 3 |

> trigger=interval: misdecodes 16

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 11

### `SF-capacity` - capacity  `--scenario coastal`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.867 | 0.859 | 0.008 | - | - | 0.963 | 0.970 | 0.561 | 1.24x | 15.1/21.7/26.0% | 1.9/5.1% | 3 |
| 8 | 1 | 0.868 | 0.860 | 0.008 | - | - | 0.969 | 0.973 | 0.560 | 1.25x | 15.1/21.8/26.0% | 1.9/5.1% | 3 |
| 16 | 1 | 0.873 | 0.863 | 0.009 | - | - | 0.978 | 0.980 | 0.565 | 1.26x | 15.1/21.9/26.1% | 1.9/5.1% | 3 |
| 32 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 50 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.979 | 0.980 | 0.589 | 1.26x | 15.2/22.1/26.3% | 1.9/5.1% | 3 |

> capacity=4: decode_failures 91

> capacity=8: decode_failures 22

### `SF-capacity-local` - capacity  `--scenario coastal`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.867 | 0.859 | 0.008 | - | - | 0.963 | 0.970 | 0.561 | 1.24x | 15.1/21.7/26.0% | 1.9/5.1% | 3 |
| 8 | 1 | 0.868 | 0.860 | 0.008 | - | - | 0.969 | 0.973 | 0.560 | 1.25x | 15.1/21.8/26.0% | 1.9/5.1% | 3 |
| 16 | 1 | 0.873 | 0.863 | 0.009 | - | - | 0.978 | 0.980 | 0.565 | 1.26x | 15.1/21.9/26.1% | 1.9/5.1% | 3 |
| 32 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 50 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.979 | 0.980 | 0.589 | 1.26x | 15.2/22.1/26.3% | 1.9/5.1% | 3 |

> capacity=4: decode_failures 91

> capacity=8: decode_failures 22

### `SF-capacity-window` - capacity  `--scenario coastal`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.973 | 0.983 | 0.574 | 1.22x | 14.7/21.3/25.4% | 1.8/5.0% | 3 |
| 16 | 1 | 0.881 | 0.873 | 0.008 | - | - | 0.983 | 0.984 | 0.575 | 1.26x | 15.1/22.1/26.2% | 1.9/5.1% | 3 |
| 32 | 1 | 0.873 | 0.863 | 0.010 | - | - | 0.979 | 0.981 | 0.556 | 1.26x | 15.1/22.1/26.1% | 1.9/5.1% | 3 |

> capacity=8: misdecodes 23

> capacity=8: decode_failures 23

> capacity=16: misdecodes 20

> capacity=32: misdecodes 29

### `SF-catchup` - catch-up-hours  `--scenario coastal`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.853 | 0.841 | 0.012 | - | - | 0.967 | 0.968 | 0.540 | 1.73x | 21.1/30.6/36.2% | 2.6/7.6% | 3 |
| 02-06 | 1 | 0.869 | 0.865 | 0.004 | - | - | 0.942 | 0.977 | 0.594 | 1.29x | 15.7/22.5/26.8% | 2.0/5.2% | 3 |
| 00-08 | 1 | 0.867 | 0.862 | 0.005 | - | - | 0.949 | 0.977 | 0.566 | 1.35x | 16.4/23.4/28.0% | 2.0/5.5% | 3 |

> catch-up-hours=: misdecodes 11

> catch-up-hours=02-06: decode_failures 8

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 5

### `SF-hops-flat` - hops-apart  `--scenario coastal`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.856 | 0.854 | 0.002 | - | - | 0.960 | 0.960 | 0.556 | 1.26x | 15.2/22.1/26.2% | 1.8/5.1% | 3 |
| 2 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 3 | 1 | 0.878 | 0.865 | 0.014 | - | - | 0.919 | 0.973 | 0.562 | 1.27x | 15.6/22.3/26.3% | 1.9/5.3% | 3 |
| 4 | 1 | 0.889 | 0.865 | 0.023 | - | - | 0.942 | 0.983 | 0.576 | 1.28x | 15.3/22.3/26.3% | 1.9/5.2% | 3 |

> hops-apart=3: decode_failures 39

> hops-apart=4: decode_failures 33

### `SF-hops-spread` - hops-apart  `--scenario coastal`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.856 | 0.854 | 0.002 | - | - | 0.960 | 0.960 | 0.556 | 1.26x | 15.2/22.1/26.2% | 1.8/5.1% | 3 |
| 2 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 3 | 1 | 0.878 | 0.865 | 0.014 | - | - | 0.919 | 0.973 | 0.562 | 1.27x | 15.6/22.3/26.3% | 1.9/5.3% | 3 |
| 4 | 1 | 0.889 | 0.865 | 0.023 | - | - | 0.942 | 0.983 | 0.576 | 1.28x | 15.3/22.3/26.3% | 1.9/5.2% | 3 |
| 5 | 1 | 0.899 | 0.867 | 0.032 | - | - | 0.917 | 0.979 | 0.565 | 1.30x | 15.7/22.6/26.6% | 1.9/5.3% | 3 |

> hops-apart=3: decode_failures 39

> hops-apart=4: decode_failures 33

> hops-apart=5: decode_failures 34

### `SF-jitter-global` - advert-jitter-s  `--scenario coastal`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.865 | 0.856 | 0.008 | - | - | 0.972 | 0.975 | 0.569 | 1.26x | 15.2/22.1/26.1% | 1.9/5.1% | 3 |
| 30 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 120 | 1 | 0.872 | 0.863 | 0.010 | - | - | 0.979 | 0.980 | 0.572 | 1.26x | 15.1/21.9/26.1% | 1.9/5.1% | 3 |
| 600 | 1 | 0.871 | 0.861 | 0.009 | - | - | 0.981 | 0.982 | 0.572 | 1.25x | 15.1/21.9/25.9% | 1.9/5.1% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario coastal`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.865 | 0.856 | 0.008 | - | - | 0.972 | 0.975 | 0.569 | 1.26x | 15.2/22.1/26.1% | 1.9/5.1% | 3 |
| 30 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 120 | 1 | 0.872 | 0.863 | 0.010 | - | - | 0.979 | 0.980 | 0.572 | 1.26x | 15.1/21.9/26.1% | 1.9/5.1% | 3 |
| 600 | 1 | 0.871 | 0.861 | 0.009 | - | - | 0.981 | 0.982 | 0.572 | 1.25x | 15.1/21.9/25.9% | 1.9/5.1% | 3 |

### `SF-place-flat` - place  `--scenario coastal`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.902 | 0.856 | 0.046 | - | - | 0.896 | 0.951 | 0.558 | 1.29x | 15.3/22.1/25.8% | 1.9/5.1% | 3 |
| routers | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.976 | 0.977 | 0.580 | 1.25x | 15.0/22.0/26.1% | 1.8/5.2% | 3 |
| alternate-routers | 1 | 0.870 | 0.865 | 0.005 | - | - | 0.965 | 0.966 | 0.551 | 1.23x | 14.8/21.5/25.6% | 1.8/5.1% | 3 |
| beside-router | 1 | 0.875 | 0.870 | 0.005 | - | - | 0.981 | 0.981 | 0.582 | 1.27x | 15.2/22.2/26.5% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.903 | 0.861 | 0.042 | - | - | 0.977 | 0.990 | 0.589 | 1.26x | 15.2/22.0/26.1% | 1.8/5.1% | 3 |
| hops-apart | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

> place=spread: decode_failures 31

> place=random-clients: decode_failures 6

### `SF-place-spread` - place  `--scenario coastal`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.902 | 0.856 | 0.046 | - | - | 0.896 | 0.951 | 0.558 | 1.29x | 15.3/22.1/25.8% | 1.9/5.1% | 3 |
| routers | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.976 | 0.977 | 0.580 | 1.25x | 15.0/22.0/26.1% | 1.8/5.2% | 3 |
| alternate-routers | 1 | 0.870 | 0.865 | 0.005 | - | - | 0.965 | 0.966 | 0.551 | 1.23x | 14.8/21.5/25.6% | 1.8/5.1% | 3 |
| beside-router | 1 | 0.875 | 0.870 | 0.005 | - | - | 0.981 | 0.981 | 0.582 | 1.27x | 15.2/22.2/26.5% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.903 | 0.861 | 0.042 | - | - | 0.977 | 0.990 | 0.589 | 1.26x | 15.2/22.0/26.1% | 1.8/5.1% | 3 |
| hops-apart | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

> place=spread: decode_failures 31

> place=random-clients: decode_failures 6

### `SF-provide-transport` - provide-transport  `--scenario coastal`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| broadcast | 1 | 0.901 | 0.867 | 0.035 | - | - | 0.981 | 0.983 | 0.609 | 1.31x | 15.7/22.7/26.9% | 1.9/5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario coastal`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| heard | 1 | 0.871 | 0.862 | 0.009 | - | - | 0.972 | 0.974 | 0.561 | 1.26x | 15.2/22.2/26.3% | 1.9/5.1% | 3 |

> replay-ordering=heard: misdecodes 14

### `SF-replay-order-broadcast` - replay-ordering  `--scenario coastal`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.901 | 0.867 | 0.035 | - | - | 0.981 | 0.983 | 0.609 | 1.31x | 15.7/22.7/26.9% | 1.9/5.3% | 3 |
| heard | 1 | 0.892 | 0.855 | 0.037 | - | - | 0.969 | 0.971 | 0.602 | 1.31x | 15.8/22.7/26.9% | 2.0/5.3% | 3 |

> replay-ordering=heard: misdecodes 9

### `SF-resolve` - resolve  `--scenario coastal`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| enum | 1 | 0.872 | 0.862 | 0.009 | - | - | 0.980 | 0.986 | 0.559 | 1.26x | 15.2/21.9/26.3% | 1.9/5.2% | 3 |
| hybrid | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `SF-servers-allrouters` - servers  `--scenario coastal`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.976 | 0.977 | 0.580 | 1.25x | 15.0/22.0/26.1% | 1.8/5.2% | 3 |
| 6 | 1 | 0.866 | 0.855 | 0.011 | - | - | 0.971 | 0.972 | 0.575 | 1.27x | 15.3/22.4/26.5% | 1.9/5.3% | 6 |

### `SF-servers-flat` - servers  `--scenario coastal`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.874 | 0.868 | 0.005 | - | - | 0.971 | 0.972 | 0.580 | 1.24x | 14.8/21.5/25.5% | 1.8/5.0% | 2 |
| 3 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 5 | 1 | 0.870 | 0.857 | 0.012 | - | - | 0.978 | 0.978 | 0.564 | 1.30x | 15.6/22.6/26.9% | 2.0/5.2% | 5 |
| 8 | 1 | 0.871 | 0.855 | 0.017 | - | - | 0.980 | 0.981 | 0.590 | 1.31x | 15.9/23.0/27.1% | 2.0/5.3% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario coastal`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.874 | 0.868 | 0.005 | - | - | 0.971 | 0.972 | 0.580 | 1.24x | 14.8/21.5/25.5% | 1.8/5.0% | 2 |
| 3 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 5 | 1 | 0.870 | 0.857 | 0.012 | - | - | 0.978 | 0.978 | 0.564 | 1.30x | 15.6/22.6/26.9% | 2.0/5.2% | 5 |
| 8 | 1 | 0.871 | 0.855 | 0.017 | - | - | 0.980 | 0.981 | 0.590 | 1.31x | 15.9/23.0/27.1% | 2.0/5.3% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario coastal`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| True | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario coastal`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.863 | 0.854 | 0.009 | - | - | 0.964 | 0.976 | 0.563 | 1.15x | 13.9/20.3/24.1% | 1.7/4.7% | 3 |
| 1 | 1 | 0.883 | 0.873 | 0.010 | - | - | 0.988 | 0.990 | 0.573 | 1.15x | 13.9/20.1/23.9% | 1.7/4.7% | 3 |
| 2 | 1 | 0.876 | 0.867 | 0.009 | - | - | 0.981 | 0.984 | 0.566 | 1.17x | 14.0/20.3/24.2% | 1.7/4.7% | 3 |
| 4 | 1 | 0.875 | 0.868 | 0.007 | - | - | 0.974 | 0.977 | 0.602 | 1.16x | 14.0/20.2/24.1% | 1.7/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario coastal`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.876 | 0.867 | 0.009 | - | - | 0.977 | 0.977 | 0.576 | 1.26x | 15.2/22.0/26.2% | 1.9/5.1% | 3 |
| 24 | 1 | 0.870 | 0.861 | 0.009 | - | - | 0.979 | 0.979 | 0.568 | 1.23x | 14.9/21.6/25.7% | 1.9/5.0% | 3 |
| 32 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.980 | 0.981 | 0.582 | 1.26x | 15.2/22.1/26.2% | 1.9/5.1% | 3 |
| 64 | 1 | 0.885 | 0.876 | 0.009 | - | - | 0.986 | 0.988 | 0.598 | 1.27x | 15.2/21.9/26.2% | 1.9/5.1% | 3 |

### `SF-window-size` - window-size  `--scenario coastal`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.869 | 0.858 | 0.010 | - | - | 0.974 | 0.977 | 0.568 | 1.37x | 16.6/23.7/28.1% | 2.1/5.5% | 3 |
| 16 | 1 | 0.866 | 0.857 | 0.009 | - | - | 0.970 | 0.971 | 0.572 | 1.29x | 15.6/22.5/26.8% | 2.0/5.2% | 3 |
| 32 | 1 | 0.873 | 0.863 | 0.010 | - | - | 0.979 | 0.981 | 0.556 | 1.26x | 15.1/22.1/26.1% | 1.9/5.1% | 3 |

> window-size=8: misdecodes 133

> window-size=16: misdecodes 72

> window-size=32: misdecodes 29

### `TH-congestion` - no-congestion-scaling  `--scenario coastal`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.868 | 2.09x | 24.0/40.7/44.7% | 1.4/5.1% | 3 |
| True | 1 | 0.742 | 0.736 | 0.006 | - | - | 0.862 | 0.892 | 0.570 | 5.35x | 56.5/76.0/78.9% | 3.7/11.8% | 3 |

> no-congestion-scaling=True: queue drops 13.7% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 106

### `TH-congestion-input` - congestion-input  `--scenario coastal`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.557 | 0.537 | 0.020 | - | - | 0.784 | 0.799 | 0.272 | 4.42x | 16.0/26.7/33.9% | 1.4/5.1% | 3 |
| truesize | 1 | 0.586 | 0.566 | 0.020 | - | - | 0.802 | 0.830 | 0.269 | 3.42x | 12.2/21.8/27.6% | 1.1/4.2% | 3 |

> congestion-input=hotstore: decode_failures 33

> congestion-input=truesize: decode_failures 46

> slower: 28.2 s per simulated hour against 10.4 over 32 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario coastal`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.965 | 0.964 | 0.001 | - | - | 0.999 | 0.999 | 0.860 | 2.01x | 23.0/38.7/42.6% | 1.3/4.9% | 3 |
| adaptive | 1 | 0.965 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.868 | 2.09x | 24.0/40.7/44.7% | 1.4/5.1% | 3 |

