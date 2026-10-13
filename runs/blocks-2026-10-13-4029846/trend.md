# Sweep blocks-2026-10-13-4029846

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 4029846 · seeds 4029846
- **blocks** 87 run
- **compute** 11.8 h of simulator time across every cell
- **generated** 2026-10-13T11:13:13+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>92 warnings</summary>

- AD-siting: faster: 0.599 s per simulated hour against 1.39 over 53 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-worst: role-placement=degree: misdecodes 1
- DB-hotstore: max-num-nodes=10: decode_failures 36
- DB-hotstore: slower: 4.94 s per simulated hour against 2.36 over 53 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 93
- DB-hotstore-stress: max-num-nodes=120: decode_failures 3
- DB-hotstore-stress: max-num-nodes=250: decode_failures 4
- DB-warm: warm-num-nodes=0: queue drops 22.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 116
- DB-warm: warm-num-nodes=25: queue drops 22.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 116
- DB-warm: warm-num-nodes=100: queue drops 22.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 116
- DB-warm: warm-num-nodes=2000: queue drops 22.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 116
- DG-burst: burst-loss=0.2: decode_failures 30
- DG-burst: burst-loss=0.3: decode_failures 31
- DG-loss: extra-loss=0.3: decode_failures 8
- DG-outage: burst-loss=0.1: decode_failures 16
- DG-outage: burst-loss=0.2: decode_failures 42
- DG-outage: burst-loss=0.3: decode_failures 42
- LD-chatty-hops: broadcast-interval-s=300: queue drops 21.2% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 31
- LD-chatty: broadcast-interval-s=300: queue drops 14.6% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 23
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 22.3% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 116
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 28.0% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 98
- MS-hopscale: nodes=250: decode_failures 77
- MS-hopscale: nodes=500: decode_failures 161
- MS-oversubscribed: nodes=250: decode_failures 3
- MS-oversubscribed: nodes=500: decode_failures 42
- MS-size: nodes=90: decode_failures 13
- MS-stretch: stretch=1.5: decode_failures 22
- MS-stretch: stretch=2.0: decode_failures 4
- RF-bw500: preset=SHORT_TURBO: decode_failures 8
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 3
- RF-eu-presets: preset=SHORT_FAST: decode_failures 20
- RF-preset: preset=SHORT_FAST: decode_failures 20
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 10
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 8
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 7
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 22
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 1
- RF-stretch-duct: slower: 4.22 s per simulated hour against 1.81 over 53 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 23
- RF-txpower: tx-power=17: decode_failures 8
- RF-txpower: tx-power=14: decode_failures 6
- RF-txpower: slower: 3.55 s per simulated hour against 1.58 over 53 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-adopt: no-adopt-hop-recommendation=True: misdecodes 1
- RT-hoplimit: hop-limit=3: decode_failures 1
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 36
- SF-bucket-mode: bucket-mode=time: misdecodes 25
- SF-bucket-mode: bucket-mode=window: misdecodes 23
- SF-bucket-time: time-bucket-s=600: misdecodes 127
- SF-bucket-time: time-bucket-s=1800: misdecodes 25
- SF-bucket-time: time-bucket-s=3600: misdecodes 10
- SF-cadence: trigger=interval: misdecodes 13
- SF-cadence: trigger=interval: decode_failures 2
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 1
- SF-cadence: trigger=bucket+interval: misdecodes 24
- SF-capacity-local: capacity=4: decode_failures 95
- SF-capacity-local: capacity=8: decode_failures 28
- SF-capacity-local: capacity=16: decode_failures 1
- SF-capacity: capacity=4: decode_failures 95
- SF-capacity: capacity=8: decode_failures 28
- SF-capacity: capacity=16: decode_failures 1
- SF-capacity-window: capacity=8: misdecodes 17
- SF-capacity-window: capacity=8: decode_failures 51
- SF-capacity-window: capacity=16: misdecodes 20
- SF-capacity-window: capacity=32: misdecodes 23
- SF-catchup: catch-up-hours=: misdecodes 24
- SF-catchup: catch-up-hours=02-06: decode_failures 42
- SF-catchup: catch-up-hours=00-08: decode_failures 39
- SF-hops-flat: faster: 1.86 s per simulated hour against 3.96 over 53 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: hops-apart=5: decode_failures 45
- SF-place-flat: place=spread: decode_failures 33
- SF-place-flat: place=random-clients: decode_failures 41
- SF-place-spread: place=spread: decode_failures 33
- SF-place-spread: place=random-clients: decode_failures 41
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 6
- SF-replay-order: replay-ordering=heard: misdecodes 10
- SF-window-size: window-size=8: misdecodes 103
- SF-window-size: window-size=16: misdecodes 81
- SF-window-size: window-size=32: misdecodes 23
- TH-congestion-input: congestion-input=hotstore: decode_failures 3
- TH-congestion: no-congestion-scaling=True: queue drops 19.3% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 98

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-stretch-duct` | 4.22 | 1.81 | 2.33x | 53 |
| `RF-txpower` | 3.55 | 1.58 | 2.25x | 53 |
| `DB-hotstore` | 4.94 | 2.36 | 2.09x | 53 |
| `SF-place-spread` | 5.24 | 2.75 | 1.90x | 53 |
| `SF-place-flat` | 4.78 | 2.86 | 1.67x | 53 |
| `MS-hopscale` | 29 | 17.6 | 1.65x | 53 |
| `RF-bw500` | 2.82 | 1.88 | 1.50x | 53 |
| `SF-sr-retries` | 1.03 | 1.55 | 0.67x | 53 |
| `RT-hoplimit` | 1.17 | 1.75 | 0.66x | 53 |
| `RF-noise` | 3.22 | 4.92 | 0.66x | 53 |
| `SF-servers-spread` | 1.47 | 2.25 | 0.65x | 53 |
| `FW-mixed` | 1.07 | 1.67 | 0.64x | 53 |
| `FW-firmware` | 1.08 | 1.69 | 0.64x | 53 |
| `LD-chatty` | 3 | 4.78 | 0.63x | 53 |
| `MS-siting` | 1.11 | 1.84 | 0.61x | 52 |
| `FW-mixed-26` | 1.03 | 1.71 | 0.60x | 53 |
| `FW-versions` | 0.84 | 1.52 | 0.55x | 53 |
| `SF-hops-spread` | 2.57 | 4.81 | 0.53x | 53 |
| `SF-hops-flat` | 1.86 | 3.96 | 0.47x | 53 |
| `AD-siting` | 0.599 | 1.39 | 0.43x | 53 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.994 | 0.994 | 0.897 → 0.906 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.990 | 0.990 | 0.893 → 0.907 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **text** | 0.057 → 0.913 | 0.856 | 0.055 → 0.907 | 4.6x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **text** | 0.105 → 0.913 | 0.808 | 0.100 → 0.907 | 3.3x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.086 → 0.884 | 0.798 | 0.085 → 0.876 | 6x advert_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.151 → 0.943 | 0.792 | 0.136 → 0.847 | 88x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.254 → 0.975 | 0.721 | 0.246 → 0.975 | 3x sr_airtime | up | 4 |
| `MS-stretch` | stretch | **text** | 0.200 → 0.913 | 0.712 | 0.197 → 0.907 | 3.7x sr_airtime | down | 4 |
| `RF-bw500` | preset | **text** | 0.259 → 0.866 | 0.608 | 0.254 → 0.858 | 2.3x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.400 → 0.990 | 0.590 | 0.321 → 0.907 | 8.2x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.409 → 0.969 | 0.560 | 0.322 → 0.805 | 4.6x bytes_on_air | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.447 → 0.913 | 0.466 | 0.435 → 0.907 | 2x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.447 → 0.913 | 0.466 | 0.435 → 0.907 | 2x sr_bytes | up | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.571 → 0.930 | 0.359 | 0.564 → 0.927 | 14x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.609 → 0.947 | 0.338 | 0.598 → 0.945 | 9.9x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.537 → 0.865 | 0.329 | 0.522 → 0.837 | 2x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.612 → 0.913 | 0.301 | 0.584 → 0.907 | 2.2x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.629 → 0.913 | 0.284 | 0.594 → 0.907 | 2.2x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.680 → 0.962 | 0.282 | 0.666 → 0.960 | 2.1x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.583 → 0.852 | 0.269 | 0.322 → 0.536 | 5.4x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.739 → 0.970 | 0.231 | 0.734 → 0.969 | 4.4x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.768 → 0.958 | 0.190 | 0.742 → 0.957 | 2.3x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.768 → 0.940 | 0.172 | 0.742 → 0.938 | 2x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.750 → 0.913 | 0.163 | 0.744 → 0.907 | 4.6x sr_airtime | down | 5 |
| `RF-noise` | noise-profile | **text** | 0.751 → 0.913 | 0.161 | 0.744 → 0.907 | 1.4x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.812 → 0.970 | 0.159 | 0.800 → 0.969 | 4.9x sr_airtime | up | 5 |
| `RT-spread` | hop-spread | **text** | 0.768 → 0.913 | 0.145 | 0.742 → 0.907 | 1.5x sr_bytes | up | 2 |
| `SF-place-flat` | place | **held** | 0.865 → 0.990 | 0.126 | 0.892 → 0.907 | 6.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.865 → 0.990 | 0.126 | 0.892 → 0.907 | 6.6x sr_bytes | up | 6 |
| `SC-signing` | signature-policy | **text** | 0.790 → 0.913 | 0.122 | 0.790 → 0.907 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.797 → 0.913 | 0.115 | 0.782 → 0.907 | 1.4x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.895 → 0.994 | 0.099 | 0.895 → 0.907 | 3.8x sr_bytes | down | 5 |
| `DB-platform` | platform-mix | **text** | 0.841 → 0.925 | 0.084 | 0.831 → 0.922 | 2.5x sr_airtime | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.907 → 0.990 | 0.083 | 0.900 → 0.907 | 26x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.844 → 0.925 | 0.081 | 0.835 → 0.922 | 2.4x sr_airtime | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.875 → 0.942 | 0.067 | 0.865 → 0.940 | 5.7x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.913 → 0.976 | 0.063 | 0.907 → 0.975 | 1.4x sr_bytes | up | 3 |
| `SF-cadence` | trigger | **held** | 0.928 → 0.990 | 0.062 | 0.880 → 0.907 | 13x advert_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.884 → 0.942 | 0.058 | 0.876 → 0.939 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.884 → 0.942 | 0.058 | 0.876 → 0.939 | 2.2x bytes_on_air | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.913 → 0.967 | 0.054 | 0.907 → 0.963 | 1.8x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.913 → 0.967 | 0.054 | 0.907 → 0.963 | 1.6x bytes_on_air | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.663 → 0.717 | 0.054 | 0.658 → 0.713 | 1.2x sr_airtime | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.860 → 0.913 | 0.052 | 0.850 → 0.907 | 1.6x sr_airtime | down | 4 |
| `TH-congestion-input` | congestion-input | **text** | 0.536 → 0.579 | 0.042 | 0.525 → 0.570 | 1.4x sr_airtime | up | 2 |
| `FW-versions` | profile | **text** | 0.876 → 0.913 | 0.037 | 0.874 → 0.907 | 3.5x bytes_on_air | up | 5 |
| `FW-firmware` | profile | **text** | 0.879 → 0.913 | 0.033 | 0.876 → 0.907 | 3.5x bytes_on_air | up | 2 |
| `MS-roles` | role-mix | **text** | 0.884 → 0.917 | 0.033 | 0.876 → 0.912 | 1.1x bytes_on_air | down | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.957 → 0.988 | 0.031 | 0.883 → 0.901 | 9.3x advert_bytes | down | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.882 → 0.913 | 0.030 | 0.871 → 0.907 | 1.2x sr_airtime | down | 2 |
| `AD-badrouters` | role-placement | **held** | 0.967 → 0.988 | 0.021 | 0.858 → 0.876 | 1.6x sr_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.969 → 0.989 | 0.020 | 0.895 → 0.902 | 2.1x advert_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.913 → 0.932 | 0.020 | 0.907 → 0.928 | 2.2x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.913 → 0.932 | 0.019 | 0.907 → 0.927 | 2.1x bytes_on_air | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.866 → 0.884 | 0.018 | 0.866 → 0.884 | 1.1x sr_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.909 → 0.927 | 0.018 | 0.903 → 0.924 | 1.2x sr_bytes | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.913 → 0.929 | 0.016 | 0.890 → 0.907 | 3.5x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.913 → 0.929 | 0.016 | 0.907 → 0.926 | 3.3x bytes_on_air | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.978 → 0.994 | 0.016 | 0.897 → 0.907 | 1.4x sr_bytes | up | 4 |
| `AD-worst` | role-placement | **text** | 0.806 → 0.822 | 0.015 | 0.800 → 0.819 | 1.2x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.910 → 0.926 | 0.015 | 0.905 → 0.922 | 1.2x sr_airtime | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.912 → 0.923 | 0.012 | 0.905 → 0.918 | 1.3x bytes_on_air | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.985 → 0.997 | 0.012 | 0.893 → 0.907 | 6.3x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.985 → 0.997 | 0.012 | 0.893 → 0.907 | 6.3x sr_bytes | up | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.874 → 0.884 | 0.011 | 0.874 → 0.884 | 1.1x sr_bytes | down | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.902 → 0.913 | 0.011 | 0.895 → 0.907 | 2.9x advert_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **text** | 0.905 → 0.915 | 0.011 | 0.898 → 0.910 | 1.2x sr_bytes | down | 4 |
| `SF-capacity` | capacity | **held** | 0.984 → 0.994 | 0.010 | 0.898 → 0.907 | 5.2x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.984 → 0.994 | 0.010 | 0.898 → 0.907 | 5.2x advert_bytes | down | 5 |
| `LD-diurnal` | diurnal | **text** | 0.912 → 0.920 | 0.008 | 0.906 → 0.917 | 1.3x sr_bytes | down | 3 |
| `SF-window-size` | window-size | **held** | 0.986 → 0.993 | 0.007 | 0.890 → 0.898 | 4.7x advert_bytes | down | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.902 → 0.908 | 0.006 | 0.895 → 0.901 | 5.3x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.906 → 0.913 | 0.006 | 0.899 → 0.907 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.906 → 0.913 | 0.006 | 0.899 → 0.907 | 1.2x sr_airtime | up | 4 |
| `SF-width` | short-id-bits | **text** | 0.906 → 0.913 | 0.006 | 0.899 → 0.907 | 3.1x advert_bytes | up | 4 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.874 → 0.879 | 0.005 | 0.874 → 0.879 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.907 → 0.913 | 0.005 | 0.900 → 0.907 | 1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.984 → 0.989 | 0.005 | 0.890 → 0.898 | 1.1x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.966 → 0.970 | 0.005 | 0.964 → 0.969 | 1.2x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.987 → 0.992 | 0.004 | 0.900 → 0.901 | 2.8x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.910 → 0.913 | 0.003 | 0.902 → 0.907 | 1x sr_bytes | down | 2 |
| `SF-resolve` | resolve | **held** | 0.990 → 0.993 | 0.003 | 0.904 → 0.907 | 5.6x advert_bytes | = | 3 |
| `SF-advert-transport` | advert-transport | **text** | 0.910 → 0.913 | 0.002 | 0.903 → 0.907 | 2.7x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.998 → 1.000 | 0.002 | 0.969 → 0.970 | 1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.970 → 0.970 | 0.001 | 0.968 → 0.969 | 1x sr_bytes | down | 2 |

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
| none | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| sprinkled | 1 | 0.952 | 0.951 | 0.002 | - | - | 0.992 | 0.993 | 0.844 | 1.21x | 18.9/25.9/28.3% | 1.4/5.4% | 3 |
| arms-race | 1 | 0.976 | 0.975 | 0.001 | - | - | 0.997 | 0.997 | 0.924 | 1.08x | 24.0/31.2/32.3% | 1.3/5.5% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.926 | 0.921 | 0.006 | - | - | 0.991 | 0.991 | 0.771 | 1.20x | 20.5/26.2/28.9% | 1.7/5.3% | 3 |
| 0.3 | 1 | 0.967 | 0.963 | 0.004 | - | - | 0.998 | 0.998 | 0.902 | 0.88x | 20.4/27.5/31.5% | 1.0/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.884 | 0.876 | 0.007 | - | - | 0.967 | 0.969 | 0.443 | 1.27x | 17.3/28.0/32.1% | 2.1/5.3% | 3 |
| inverse | 1 | 0.882 | 0.872 | 0.011 | - | - | 0.984 | 0.987 | 0.526 | 1.21x | 16.0/20.6/23.6% | 2.2/3.7% | 3 |
| random | 1 | 0.872 | 0.858 | 0.014 | - | - | 0.988 | 0.990 | 0.408 | 1.19x | 16.8/21.2/23.1% | 2.0/5.3% | 3 |

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.884 | 0.876 | 0.007 | - | - | 0.967 | 0.969 | 0.443 | 1.27x | 17.3/28.0/32.1% | 2.1/5.3% | 3 |
| all-routers | 1 | 0.942 | 0.939 | 0.003 | - | - | 0.993 | 0.993 | 0.553 | 2.83x | 34.9/47.1/50.3% | 4.6/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.884 | 0.876 | 0.007 | - | - | 0.967 | 0.969 | 0.443 | 1.27x | 17.3/28.0/32.1% | 2.1/5.3% | 3 |
| no-mute | 1 | 0.917 | 0.912 | 0.005 | - | - | 0.992 | 0.993 | 0.529 | 1.35x | 18.5/25.4/27.8% | 2.2/5.4% | 3 |
| all-routers | 1 | 0.942 | 0.939 | 0.003 | - | - | 0.993 | 0.993 | 0.553 | 2.83x | 34.9/47.1/50.3% | 4.6/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.884 | 0.876 | 0.007 | - | - | 0.967 | 0.969 | 0.443 | 1.27x | 17.3/28.0/32.1% | 2.1/5.3% | 3 |
| local-typical | 1 | 0.630 | 0.629 | 0.001 | - | - | 0.767 | 0.767 | 0.000 | 1.21x | 13.1/26.1/31.9% | 2.0/4.8% | 3 |
| basement-heavy | 1 | 0.086 | 0.085 | 0.001 | - | - | 0.176 | 0.187 | 0.000 | 0.57x | 1.2/8.7/13.0% | 0.4/3.3% | 3 |

> faster: 0.599 s per simulated hour against 1.39 over 53 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.822 | 0.819 | 0.003 | - | - | 0.947 | 0.947 | 0.000 | 2.23x | 19.6/32.0/40.4% | 1.7/5.5% | 3 |
| inverse | 1 | 0.806 | 0.800 | 0.006 | - | - | 0.957 | 0.957 | 0.000 | 2.14x | 15.9/26.1/34.7% | 1.7/3.3% | 3 |

> role-placement=degree: misdecodes 1

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.906 | 0.906 | 0.000 | - | - | 0 | 0.000 | 0.434 | 1.40x | 17.5/29.3/32.3% | 2.0/5.2% | 3 |
| sr | 1 | 0.909 | 0.897 | 0.012 | - | - | 0.994 | 0.994 | 0.434 | 1.46x | 18.3/30.4/33.4% | 2.1/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.844 | 0.835 | 0.009 | - | - | 0.936 | 0.951 | 0.376 | 3.32x | 43.5/64.5/69.4% | 4.7/10.3% | 3 |
| 100 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.986 | 0.988 | 0.480 | 1.70x | 22.9/35.8/39.7% | 2.4/5.4% | 3 |
| 120 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.986 | 0.988 | 0.480 | 1.70x | 22.9/35.8/39.7% | 2.4/5.4% | 3 |
| 250 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.986 | 0.988 | 0.480 | 1.70x | 22.9/35.8/39.7% | 2.4/5.4% | 3 |

> max-num-nodes=10: decode_failures 36

> slower: 4.94 s per simulated hour against 2.36 over 53 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.329 | 0.322 | 0.007 | - | - | 0.583 | 0.654 | 0.071 | 11.60x | 46.0/65.3/76.6% | 4.0/11.0% | 3 |
| 120 | 1 | 0.536 | 0.525 | 0.011 | - | - | 0.839 | 0.840 | 0.085 | 4.84x | 19.1/35.8/46.8% | 1.6/6.4% | 3 |
| 250 | 1 | 0.546 | 0.536 | 0.011 | - | - | 0.852 | 0.853 | 0.086 | 4.67x | 18.3/34.2/45.0% | 1.6/6.2% | 3 |

> max-num-nodes=10: decode_failures 93

> max-num-nodes=120: decode_failures 3

> max-num-nodes=250: decode_failures 4

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.986 | 0.988 | 0.480 | 1.70x | 22.9/35.8/39.7% | 2.4/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.986 | 0.988 | 0.480 | 1.70x | 22.9/35.8/39.7% | 2.4/5.4% | 3 |
| constrained | 1 | 0.841 | 0.831 | 0.009 | - | - | 0.939 | 0.946 | 0.375 | 3.33x | 43.6/64.4/69.3% | 4.8/10.3% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.830 | 0.872 | 0.417 | 5.56x | 62.0/75.1/79.7% | 3.8/12.9% | 3 |
| 25 | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.830 | 0.872 | 0.417 | 5.56x | 62.0/75.1/79.7% | 3.8/12.9% | 3 |
| 100 | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.830 | 0.872 | 0.417 | 5.56x | 62.0/75.1/79.7% | 3.8/12.9% | 3 |
| 2000 | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.830 | 0.872 | 0.417 | 5.56x | 62.0/75.1/79.7% | 3.8/12.9% | 3 |

> warm-num-nodes=0: queue drops 22.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 116

> warm-num-nodes=25: queue drops 22.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 116

> warm-num-nodes=100: queue drops 22.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 116

> warm-num-nodes=2000: queue drops 22.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 116

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.822 | 0.804 | 0.018 | - | - | 0.975 | 0.979 | 0.355 | 1.38x | 17.9/29.2/32.1% | 2.1/5.0% | 3 |
| 0.2 | 1 | 0.727 | 0.695 | 0.032 | - | - | 0.934 | 0.957 | 0.225 | 1.28x | 17.2/27.8/30.4% | 1.9/4.6% | 3 |
| 0.3 | 1 | 0.629 | 0.594 | 0.035 | - | - | 0.829 | 0.908 | 0.193 | 1.19x | 16.5/26.5/29.0% | 1.8/4.1% | 3 |

> burst-loss=0.2: decode_failures 30

> burst-loss=0.3: decode_failures 31

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.879 | 0.870 | 0.009 | - | - | 0.980 | 0.985 | 0.352 | 1.51x | 19.6/31.3/34.2% | 2.2/5.4% | 3 |
| 0.2 | 1 | 0.846 | 0.835 | 0.011 | - | - | 0.968 | 0.970 | 0.292 | 1.54x | 20.6/32.5/35.3% | 2.3/5.3% | 3 |
| 0.3 | 1 | 0.797 | 0.782 | 0.015 | - | - | 0.942 | 0.955 | 0.210 | 1.56x | 21.6/33.3/36.1% | 2.4/5.2% | 3 |

> extra-loss=0.3: decode_failures 8

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.810 | 0.795 | 0.014 | - | - | 0.953 | 0.984 | 0.373 | 1.38x | 18.1/28.9/31.7% | 2.0/5.1% | 3 |
| 0.2 | 1 | 0.706 | 0.679 | 0.027 | - | - | 0.892 | 0.955 | 0.298 | 1.29x | 17.3/27.8/30.5% | 1.9/4.5% | 3 |
| 0.3 | 1 | 0.612 | 0.584 | 0.027 | - | - | 0.805 | 0.926 | 0.166 | 1.21x | 17.0/26.6/29.1% | 1.8/4.3% | 3 |

> burst-loss=0.1: decode_failures 16

> burst-loss=0.2: decode_failures 42

> burst-loss=0.3: decode_failures 42

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.866 | 0.866 | 0.000 | - | - | 0.972 | 0.976 | 0.396 | 1.96x | 25.0/40.6/44.1% | 2.8/7.3% | 3 |
| directed-with-late-flood | 1 | 0.884 | 0.884 | 0.000 | - | - | 0.976 | 0.981 | 0.395 | 1.79x | 22.9/37.6/40.9% | 2.6/6.7% | 3 |
| m4-early-flood | 1 | 0.877 | 0.877 | 0.000 | - | - | 0.975 | 0.979 | 0.410 | 1.80x | 23.1/37.9/41.2% | 2.6/6.8% | 3 |

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.879 | 0.876 | 0.003 | - | - | 0.959 | 0.959 | 0.000 | 0.74x | 9.4/12.9/15.5% | 1.2/2.1% | 3 |
| 2.8 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.932 | 0.927 | 0.004 | - | - | 0.992 | 0.993 | 0.676 | 1.26x | 17.1/24.0/27.0% | 2.0/4.9% | 3 |
| 0.5 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.991 | 0.994 | 0.697 | 1.05x | 14.0/19.3/22.6% | 1.6/3.8% | 3 |
| 0.75 | 1 | 0.923 | 0.920 | 0.003 | - | - | 0.991 | 0.992 | 0.614 | 0.94x | 12.3/17.4/18.5% | 1.5/3.7% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.932 | 0.928 | 0.005 | - | - | 0.990 | 0.991 | 0.670 | 1.27x | 17.6/24.2/27.3% | 2.0/5.0% | 3 |
| 0.5 | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.993 | 0.994 | 0.684 | 1.03x | 13.8/19.4/22.5% | 1.6/3.8% | 3 |
| 0.75 | 1 | 0.919 | 0.916 | 0.003 | - | - | 0.987 | 0.988 | 0.586 | 0.90x | 12.0/17.2/18.1% | 1.5/3.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.996 | 0.997 | 0.485 | 0.77x | 9.9/17.6/19.5% | 1.1/3.2% | 3 |
| signing=true | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.883 | 0.881 | 0.002 | - | - | 0.961 | 0.961 | 0.000 | 0.75x | 10.1/14.1/17.2% | 1.2/2.6% | 3 |
| 2.5 | 1 | 0.876 | 0.874 | 0.002 | - | - | 0.953 | 0.953 | 0.000 | 0.76x | 10.0/14.1/17.1% | 1.2/2.6% | 3 |
| 2.6 | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.955 | 0.955 | 0.000 | 0.73x | 10.0/13.9/17.2% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.897 | 0.897 | 0.000 | - | - | 0.959 | 0.959 | 0.000 | 0.77x | 10.4/16.8/19.5% | 1.2/3.0% | 3 |
| 2.8 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.930 | 0.927 | 0.003 | - | - | 0.997 | 0.997 | 0.459 | 0.96x | 12.2/20.2/22.2% | 1.4/3.7% | 3 |
| 900 | 1 | 0.875 | 0.865 | 0.009 | - | - | 0.971 | 0.971 | 0.381 | 2.32x | 29.3/47.6/51.8% | 3.4/8.4% | 3 |
| 300 | 1 | 0.571 | 0.564 | 0.007 | - | - | 0.661 | 0.777 | 0.187 | 4.69x | 57.7/76.0/79.7% | 7.3/16.0% | 3 |

> broadcast-interval-s=300: queue drops 14.6% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 23

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.992 | 0.992 | 0.652 | 1.04x | 13.2/20.7/22.7% | 1.5/3.6% | 3 |
| 900 | 1 | 0.903 | 0.898 | 0.004 | - | - | 0.978 | 0.979 | 0.517 | 2.72x | 34.7/51.4/55.8% | 4.1/9.0% | 3 |
| 300 | 1 | 0.609 | 0.598 | 0.011 | - | - | 0.744 | 0.783 | 0.287 | 5.15x | 61.3/76.1/79.8% | 8.3/16.3% | 3 |

> broadcast-interval-s=300: queue drops 21.2% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 31

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.920 | 0.917 | 0.004 | - | - | 0.992 | 0.995 | 0.459 | 1.35x | 17.3/28.5/31.3% | 2.0/5.1% | 3 |
| sinusoid | 1 | 0.912 | 0.906 | 0.006 | - | - | 0.991 | 0.992 | 0.410 | 1.31x | 16.6/27.5/30.1% | 1.9/4.9% | 3 |
| commuter | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.875 | 0.865 | 0.009 | - | - | 0.971 | 0.971 | 0.381 | 2.32x | 29.3/47.6/51.8% | 3.4/8.4% | 3 |
| 3600 | 1 | 0.930 | 0.927 | 0.003 | - | - | 0.997 | 0.997 | 0.459 | 0.96x | 12.2/20.2/22.2% | 1.4/3.7% | 3 |
| 10800 | 1 | 0.931 | 0.928 | 0.004 | - | - | 0.995 | 0.997 | 0.504 | 0.63x | 8.0/13.0/14.3% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.942 | 0.940 | 0.002 | - | - | 0.999 | 1.000 | 0.498 | 0.46x | 5.8/9.6/10.5% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.905 | 0.898 | 0.007 | - | - | 0.989 | 0.991 | 0.436 | 1.53x | 19.3/31.9/34.8% | 2.2/5.6% | 3 |
| 1.0 | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.985 | 0.988 | 0.410 | 1.69x | 21.5/35.4/38.8% | 2.4/6.3% | 3 |
| 4.0 | 1 | 0.860 | 0.850 | 0.011 | - | - | 0.970 | 0.970 | 0.373 | 2.22x | 28.3/46.2/50.3% | 3.2/8.1% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.830 | 0.872 | 0.417 | 5.56x | 62.0/75.1/79.7% | 3.8/12.9% | 3 |
| 1.0 | 1 | 0.663 | 0.658 | 0.005 | - | - | 0.781 | 0.832 | 0.385 | 5.93x | 64.8/76.1/80.6% | 4.1/14.0% | 3 |

> traceroute-per-hour=0.0: queue drops 22.3% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 116

> traceroute-per-hour=1.0: queue drops 28.0% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 98

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.812 | 0.800 | 0.011 | - | - | 0.937 | 0.938 | 0.250 | 1.56x | 22.8/37.1/41.0% | 3.8/7.6% | 3 |
| 60 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 90 | 1 | 0.944 | 0.942 | 0.002 | - | - | 0.990 | 0.991 | 0.743 | 1.62x | 20.0/32.7/35.6% | 1.5/4.9% | 3 |
| 120 | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.998 | 0.998 | 0.656 | 1.99x | 24.2/36.6/41.2% | 1.2/5.2% | 3 |
| 150 | 1 | 0.968 | 0.966 | 0.001 | - | - | 0.997 | 0.997 | 0.559 | 2.65x | 30.4/46.2/51.3% | 1.4/5.6% | 3 |

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 120 | 1 | 0.816 | 0.807 | 0.009 | - | - | 0.968 | 0.969 | 0.413 | 2.29x | 16.1/28.7/33.5% | 1.6/5.5% | 3 |
| 250 | 1 | 0.535 | 0.523 | 0.012 | - | - | 0.833 | 0.835 | 0.095 | 5.14x | 20.2/37.6/49.3% | 1.7/6.8% | 3 |
| 500 | 1 | 0.324 | 0.321 | 0.003 | - | - | 0.400 | 0.402 | 0.058 | 10.46x | 19.9/34.2/63.1% | 1.7/6.1% | 3 |

> nodes=250: decode_failures 77

> nodes=500: decode_failures 161

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.816 | 0.805 | 0.010 | - | - | 0.969 | 0.970 | 0.399 | 2.12x | 14.9/26.7/31.1% | 1.5/5.0% | 3 |
| 250 | 1 | 0.536 | 0.525 | 0.011 | - | - | 0.839 | 0.840 | 0.085 | 4.84x | 19.1/35.8/46.8% | 1.6/6.4% | 3 |
| 500 | 1 | 0.325 | 0.322 | 0.003 | - | - | 0.409 | 0.409 | 0.053 | 9.74x | 18.4/32.1/59.4% | 1.6/5.7% | 3 |

> nodes=250: decode_failures 3

> nodes=500: decode_failures 42

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.917 | 0.912 | 0.005 | - | - | 0.993 | 0.994 | 0.484 | 1.45x | 18.3/30.0/33.0% | 2.1/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.884 | 0.876 | 0.007 | - | - | 0.967 | 0.969 | 0.443 | 1.27x | 17.3/28.0/32.1% | 2.1/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.989 | 0.990 | 0.510 | 1.50x | 19.2/30.6/33.5% | 2.2/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.910 | 0.905 | 0.006 | - | - | 0.977 | 0.977 | 0.578 | 1.41x | 19.5/31.4/35.5% | 2.5/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.05 | 1 | 0.912 | 0.905 | 0.006 | - | - | 0.991 | 0.991 | 0.427 | 1.58x | 21.8/34.6/39.1% | 2.2/5.4% | 3 |
| 0.1 | 1 | 0.916 | 0.910 | 0.006 | - | - | 0.997 | 0.998 | 0.429 | 1.66x | 23.1/36.9/41.9% | 2.3/5.3% | 3 |
| 0.2 | 1 | 0.923 | 0.918 | 0.005 | - | - | 0.991 | 0.991 | 0.520 | 1.88x | 26.2/41.6/46.8% | 2.5/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| local-typical | 1 | 0.689 | 0.687 | 0.002 | - | - | 0.816 | 0.817 | 0.000 | 1.47x | 16.0/28.4/33.4% | 2.2/4.9% | 3 |
| event | 1 | 0.254 | 0.246 | 0.008 | - | - | 0.436 | 0.443 | 0.000 | 1.29x | 7.8/12.9/21.5% | 2.0/4.8% | 3 |
| backbone | 1 | 0.975 | 0.975 | 0.001 | - | - | 0.995 | 0.996 | 0.918 | 1.02x | 34.4/39.8/42.3% | 1.1/5.5% | 3 |

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.911 | 0.903 | 0.008 | - | - | 0.967 | 0.975 | 0.716 | 1.63x | 32.4/42.3/47.9% | 3.6/8.0% | 3 |
| 60 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 90 | 1 | 0.839 | 0.832 | 0.008 | - | - | 0.953 | 0.960 | 0.479 | 1.77x | 16.2/27.3/31.0% | 1.7/5.2% | 3 |
| 120 | 1 | 0.816 | 0.807 | 0.009 | - | - | 0.968 | 0.969 | 0.413 | 2.29x | 16.1/28.7/33.5% | 1.6/5.5% | 3 |
| 150 | 1 | 0.750 | 0.744 | 0.006 | - | - | 0.959 | 0.960 | 0.352 | 2.88x | 17.4/31.4/37.5% | 1.5/5.6% | 3 |

> nodes=90: decode_failures 13

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 1.25 | 1 | 0.735 | 0.726 | 0.009 | - | - | 0.892 | 0.896 | 0.000 | 1.46x | 13.9/24.6/27.0% | 2.3/5.1% | 3 |
| 1.5 | 1 | 0.537 | 0.522 | 0.015 | - | - | 0.652 | 0.794 | 0.080 | 1.43x | 11.1/16.7/20.4% | 2.1/4.8% | 3 |
| 2.0 | 1 | 0.200 | 0.197 | 0.003 | - | - | 0.317 | 0.369 | 0.000 | 1.13x | 6.2/11.5/13.3% | 1.8/4.1% | 3 |

> stretch=1.5: decode_failures 22

> stretch=2.0: decode_failures 4

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| clustered | 1 | 0.876 | 0.874 | 0.002 | - | - | 0.934 | 0.935 | 0.000 | 1.08x | 26.0/35.1/36.6% | 1.3/5.4% | 3 |
| corridor | 1 | 0.680 | 0.666 | 0.013 | - | - | 0.911 | 0.917 | 0.256 | 1.31x | 15.2/28.0/30.6% | 1.9/5.6% | 3 |
| hub | 1 | 0.962 | 0.960 | 0.001 | - | - | 0.995 | 0.995 | 0.817 | 1.12x | 29.0/36.7/38.5% | 1.4/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.884 | 0.884 | 0.000 | - | - | 0.976 | 0.981 | 0.395 | 1.79x | 22.9/37.6/40.9% | 2.6/6.7% | 3 |
| True | 1 | 0.874 | 0.874 | 0.000 | - | - | 0.977 | 0.982 | 0.395 | 1.83x | 23.4/38.6/42.0% | 2.7/6.9% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.874 | 0.874 | 0.000 | - | - | 0.977 | 0.982 | 0.395 | 1.83x | 23.4/38.6/42.0% | 2.7/6.9% | 3 |
| m4-early-flood | 1 | 0.879 | 0.879 | 0.000 | - | - | 0.978 | 0.985 | 0.402 | 1.82x | 23.2/38.4/41.9% | 2.6/6.9% | 3 |

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.906 | 0.906 | 0.000 | - | - | 0 | 0.000 | 0.434 | 1.40x | 17.5/29.3/32.3% | 2.0/5.2% | 3 |
| chain | 1 | 0.896 | 0.893 | 0.003 | - | - | 0.938 | 0.991 | 0.424 | 1.63x | 20.8/34.6/37.3% | 2.4/6.0% | 3 |
| sr | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| True | 1 | 0.910 | 0.902 | 0.007 | - | - | 0.991 | 0.992 | 0.431 | 1.47x | 18.5/30.5/33.4% | 2.1/5.5% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.998 | 0.998 | 0.656 | 1.99x | 24.2/36.6/41.2% | 1.2/5.2% | 3 |
| True | 1 | 0.970 | 0.968 | 0.001 | - | - | 0.999 | 0.999 | 0.667 | 2.02x | 24.3/36.8/41.4% | 1.2/5.2% | 3 |

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.259 | 0.254 | 0.004 | - | - | 0.429 | 0.478 | 0.000 | 0.06x | 0.4/0.7/0.8% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.589 | 0.574 | 0.015 | - | - | 0.925 | 0.928 | 0.091 | 0.33x | 2.7/4.3/5.0% | 0.5/1.2% | 3 |
| LONG_TURBO | 1 | 0.866 | 0.858 | 0.009 | - | - | 0.981 | 0.984 | 0.247 | 1.40x | 15.4/24.4/27.6% | 2.1/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 8

> preset=MEDIUM_TURBO: decode_failures 3

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 0.25 | 1 | 0.919 | 0.911 | 0.007 | - | - | 0.989 | 0.990 | 0.504 | 1.34x | 20.2/31.2/33.9% | 1.9/5.4% | 3 |
| 1.0 | 1 | 0.967 | 0.963 | 0.004 | - | - | 0.999 | 0.999 | 0.828 | 0.81x | 28.2/33.9/35.3% | 0.9/5.1% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.447 | 0.435 | 0.012 | - | - | 0.842 | 0.875 | 0.000 | 0.17x | 1.3/2.1/2.5% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| LITE_FAST | 1 | 0.888 | 0.878 | 0.010 | - | - | 0.988 | 0.990 | 0.318 | 1.12x | 13.7/21.9/23.8% | 1.7/4.2% | 3 |
| NARROW_SLOW | 1 | 0.884 | 0.876 | 0.008 | - | - | 0.980 | 0.982 | 0.342 | 1.44x | 16.9/29.5/31.2% | 2.1/5.3% | 3 |

> preset=SHORT_FAST: decode_failures 20

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| temporal | 1 | 0.856 | 0.845 | 0.011 | - | - | 0.978 | 0.981 | 0.279 | 1.48x | 19.0/30.3/33.2% | 2.2/5.5% | 3 |
| transient | 1 | 0.907 | 0.899 | 0.008 | - | - | 0.991 | 0.991 | 0.427 | 1.48x | 18.7/30.7/33.5% | 2.1/5.5% | 3 |
| periodic | 1 | 0.751 | 0.744 | 0.007 | - | - | 0.833 | 0.839 | 0.308 | 1.35x | 17.6/28.2/30.9% | 2.0/4.8% | 3 |

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.447 | 0.435 | 0.012 | - | - | 0.842 | 0.875 | 0.000 | 0.17x | 1.3/2.1/2.5% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| LONG_MODERATE | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.901 | 0.908 | 0.613 | 3.58x | 53.8/71.3/73.4% | 5.4/12.0% | 3 |

> preset=SHORT_FAST: decode_failures 20

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.057 | 0.055 | 0.001 | - | - | 0.234 | 0.245 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.259 | 0.254 | 0.004 | - | - | 0.429 | 0.478 | 0.000 | 0.06x | 0.4/0.7/0.8% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| LONG_TURBO | 1 | 0.866 | 0.858 | 0.009 | - | - | 0.981 | 0.984 | 0.247 | 1.40x | 15.4/24.4/27.6% | 2.1/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.895 | 0.886 | 0.009 | - | - | 0.978 | 0.981 | 0.525 | 2.03x | 23.8/39.8/43.3% | 3.0/7.2% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 10

> preset=SHORT_TURBO: decode_failures 8

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.856 | 0.847 | 0.008 | - | - | 0.943 | 0.943 | 0.392 | 1.42x | 18.2/30.0/32.8% | 2.1/5.2% | 3 |
| 10000 | 1 | 0.751 | 0.744 | 0.007 | - | - | 0.833 | 0.839 | 0.308 | 1.35x | 17.6/28.2/30.9% | 2.0/4.8% | 3 |
| 4000 | 1 | 0.481 | 0.477 | 0.005 | - | - | 0.535 | 0.590 | 0.125 | 1.15x | 15.7/24.3/26.4% | 1.7/3.6% | 3 |
| 2000 | 1 | 0.136 | 0.136 | 0.000 | - | - | 0.151 | 0.220 | 0.037 | 0.76x | 11.0/16.8/18.5% | 1.2/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 7

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.537 | 0.522 | 0.015 | - | - | 0.652 | 0.794 | 0.080 | 1.43x | 11.1/16.7/20.4% | 2.1/4.8% | 3 |
| 1.0 | 1 | 0.865 | 0.837 | 0.028 | - | - | 0.935 | 0.943 | 0.622 | 0.92x | 20.9/25.6/28.3% | 1.1/4.8% | 3 |

> duct-per-hour=0.0: decode_failures 22

> duct-per-hour=1.0: decode_failures 1

> slower: 4.22 s per simulated hour against 1.81 over 53 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 22 | 1 | 0.533 | 0.519 | 0.015 | - | - | 0.632 | 0.811 | 0.087 | 1.39x | 11.1/16.3/20.6% | 2.2/4.7% | 3 |
| 17 | 1 | 0.225 | 0.221 | 0.003 | - | - | 0.348 | 0.396 | 0.000 | 1.18x | 6.7/12.2/14.1% | 2.0/4.1% | 3 |
| 14 | 1 | 0.105 | 0.100 | 0.005 | - | - | 0.308 | 0.341 | 0.000 | 0.74x | 3.1/7.2/11.8% | 1.0/3.1% | 3 |

> tx-power=22: decode_failures 23

> tx-power=17: decode_failures 8

> tx-power=14: decode_failures 6

> slower: 3.55 s per simulated hour against 1.58 over 53 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.998 | 0.998 | 0.656 | 1.99x | 24.2/36.6/41.2% | 1.2/5.2% | 3 |
| True | 1 | 0.966 | 0.964 | 0.002 | - | - | 0.998 | 0.998 | 0.618 | 2.37x | 28.0/41.2/45.9% | 1.4/5.9% | 3 |

> no-adopt-hop-recommendation=True: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.991 | 0.991 | 0.436 | 1.52x | 20.7/33.2/36.8% | 2.1/5.3% | 3 |
| True | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.989 | 0.989 | 0.499 | 1.62x | 21.9/34.1/37.7% | 2.3/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| random | 1 | 0.882 | 0.871 | 0.011 | - | - | 0.980 | 0.981 | 0.456 | 1.36x | 17.5/28.9/31.6% | 2.0/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.768 | 0.742 | 0.026 | - | - | 0.959 | 0.962 | 0.254 | 1.08x | 14.2/25.6/27.7% | 1.5/4.6% | 3 |
| 7 | 1 | 0.940 | 0.938 | 0.002 | - | - | 0.988 | 0.990 | 0.635 | 1.63x | 20.8/31.9/34.9% | 2.4/5.6% | 3 |
| 15 | 1 | 0.958 | 0.957 | 0.001 | - | - | 0.994 | 0.995 | 0.751 | 1.61x | 20.5/31.4/34.5% | 2.4/5.5% | 3 |
| 32 | 1 | 0.955 | 0.954 | 0.001 | - | - | 0.992 | 0.993 | 0.732 | 1.62x | 20.6/31.5/34.7% | 2.4/5.5% | 3 |

> hop-limit=3: decode_failures 1

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.768 | 0.742 | 0.026 | - | - | 0.959 | 0.962 | 0.254 | 1.08x | 14.2/25.6/27.7% | 1.5/4.6% | 3 |
| 5 | 1 | 0.898 | 0.892 | 0.006 | - | - | 0.988 | 0.989 | 0.473 | 1.47x | 19.0/30.2/33.0% | 2.1/5.4% | 3 |
| 7 | 1 | 0.940 | 0.938 | 0.002 | - | - | 0.988 | 0.990 | 0.635 | 1.63x | 20.8/31.9/34.9% | 2.4/5.6% | 3 |

> hop-limit=3: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.900 | 0.900 | 0.000 | - | - | 0.907 | 0.993 | 0.416 | 1.40x | 17.6/29.4/32.2% | 2.0/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.768 | 0.742 | 0.026 | - | - | 0.959 | 0.962 | 0.254 | 1.08x | 14.2/25.6/27.7% | 1.5/4.6% | 3 |
| True | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

> hop-spread=False: decode_failures 1

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| BALANCED | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| STRICT | 1 | 0.790 | 0.790 | 0.000 | - | - | 0.881 | 0.883 | 0.316 | 1.58x | 20.2/32.5/35.7% | 2.3/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| dm | 1 | 0.910 | 0.903 | 0.007 | - | - | 0.991 | 0.991 | 0.458 | 1.41x | 17.9/30.1/32.8% | 2.0/5.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.911 | 0.905 | 0.006 | - | - | 0.988 | 0.991 | 0.447 | 1.44x | 18.2/30.2/33.0% | 2.1/5.3% | 3 |
| local | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| time | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.987 | 0.988 | 0.404 | 1.47x | 18.5/30.9/33.6% | 2.1/5.5% | 3 |
| window | 1 | 0.903 | 0.895 | 0.008 | - | - | 0.986 | 0.988 | 0.434 | 1.42x | 17.8/29.9/32.7% | 2.0/5.3% | 3 |

> bucket-mode=global: misdecodes 36

> bucket-mode=time: misdecodes 25

> bucket-mode=window: misdecodes 23

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.904 | 0.895 | 0.009 | - | - | 0.988 | 0.989 | 0.442 | 1.59x | 20.4/33.3/36.0% | 2.3/5.9% | 3 |
| 1800 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.987 | 0.988 | 0.404 | 1.47x | 18.5/30.9/33.6% | 2.1/5.5% | 3 |
| 3600 | 1 | 0.908 | 0.901 | 0.007 | - | - | 0.989 | 0.993 | 0.466 | 1.43x | 18.2/30.0/32.8% | 2.1/5.3% | 3 |

> time-bucket-s=600: misdecodes 127

> time-bucket-s=1800: misdecodes 25

> time-bucket-s=3600: misdecodes 10

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| interval | 1 | 0.889 | 0.880 | 0.009 | - | - | 0.969 | 0.981 | 0.409 | 1.87x | 24.3/39.7/42.3% | 2.7/7.2% | 3 |
| aimd | 1 | 0.900 | 0.898 | 0.002 | - | - | 0.928 | 0.987 | 0.437 | 1.45x | 18.2/30.3/33.2% | 2.1/5.3% | 3 |
| bucket+interval | 1 | 0.892 | 0.883 | 0.009 | - | - | 0.988 | 0.988 | 0.401 | 1.91x | 24.9/40.4/43.1% | 2.8/7.4% | 3 |

> trigger=interval: misdecodes 13

> trigger=interval: decode_failures 2

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 1

> trigger=bucket+interval: misdecodes 24

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.906 | 0.899 | 0.008 | - | - | 0.990 | 0.991 | 0.425 | 1.45x | 18.4/30.9/33.7% | 2.1/5.6% | 3 |
| 8 | 1 | 0.914 | 0.907 | 0.006 | - | - | 0.994 | 0.994 | 0.456 | 1.44x | 18.3/30.4/33.2% | 2.1/5.5% | 3 |
| 16 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.989 | 0.990 | 0.427 | 1.45x | 18.3/30.6/33.4% | 2.1/5.5% | 3 |
| 32 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 50 | 1 | 0.904 | 0.898 | 0.006 | - | - | 0.984 | 0.985 | 0.424 | 1.44x | 18.2/30.3/33.1% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 95

> capacity=8: decode_failures 28

> capacity=16: decode_failures 1

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.906 | 0.899 | 0.008 | - | - | 0.990 | 0.991 | 0.425 | 1.45x | 18.4/30.9/33.7% | 2.1/5.6% | 3 |
| 8 | 1 | 0.914 | 0.907 | 0.006 | - | - | 0.994 | 0.994 | 0.456 | 1.44x | 18.3/30.4/33.2% | 2.1/5.5% | 3 |
| 16 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.989 | 0.990 | 0.427 | 1.45x | 18.3/30.6/33.4% | 2.1/5.5% | 3 |
| 32 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 50 | 1 | 0.904 | 0.898 | 0.006 | - | - | 0.984 | 0.985 | 0.424 | 1.44x | 18.2/30.3/33.1% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 95

> capacity=8: decode_failures 28

> capacity=16: decode_failures 1

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.908 | 0.902 | 0.006 | - | - | 0.969 | 0.992 | 0.430 | 1.41x | 17.8/29.8/32.6% | 2.0/5.3% | 3 |
| 16 | 1 | 0.909 | 0.902 | 0.007 | - | - | 0.989 | 0.989 | 0.440 | 1.42x | 17.8/30.0/32.8% | 2.0/5.4% | 3 |
| 32 | 1 | 0.903 | 0.895 | 0.008 | - | - | 0.986 | 0.988 | 0.434 | 1.42x | 17.8/29.9/32.7% | 2.0/5.3% | 3 |

> capacity=8: misdecodes 17

> capacity=8: decode_failures 51

> capacity=16: misdecodes 20

> capacity=32: misdecodes 23

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.892 | 0.883 | 0.009 | - | - | 0.988 | 0.988 | 0.401 | 1.91x | 24.9/40.4/43.1% | 2.8/7.4% | 3 |
| 02-06 | 1 | 0.906 | 0.901 | 0.004 | - | - | 0.957 | 0.992 | 0.431 | 1.47x | 18.6/31.2/33.8% | 2.1/5.6% | 3 |
| 00-08 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.957 | 0.991 | 0.419 | 1.54x | 19.8/33.2/35.8% | 2.2/6.0% | 3 |

> catch-up-hours=: misdecodes 24

> catch-up-hours=02-06: decode_failures 42

> catch-up-hours=00-08: decode_failures 39

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.902 | 0.899 | 0.002 | - | - | 0.978 | 0.979 | 0.433 | 1.44x | 17.9/30.0/33.0% | 2.1/5.3% | 3 |
| 2 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 3 | 1 | 0.909 | 0.897 | 0.012 | - | - | 0.994 | 0.994 | 0.434 | 1.46x | 18.3/30.4/33.4% | 2.1/5.4% | 3 |
| 4 | 1 | 0.911 | 0.899 | 0.012 | - | - | 0.991 | 0.991 | 0.443 | 1.46x | 18.2/30.4/33.4% | 2.1/5.5% | 3 |

> faster: 1.86 s per simulated hour against 3.96 over 53 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.902 | 0.899 | 0.002 | - | - | 0.978 | 0.979 | 0.433 | 1.44x | 17.9/30.0/33.0% | 2.1/5.3% | 3 |
| 2 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 3 | 1 | 0.909 | 0.897 | 0.012 | - | - | 0.994 | 0.994 | 0.434 | 1.46x | 18.3/30.4/33.4% | 2.1/5.4% | 3 |
| 4 | 1 | 0.911 | 0.899 | 0.012 | - | - | 0.991 | 0.991 | 0.443 | 1.46x | 18.2/30.4/33.4% | 2.1/5.5% | 3 |
| 5 | 1 | 0.911 | 0.895 | 0.017 | - | - | 0.895 | 0.989 | 0.408 | 1.47x | 18.8/30.4/33.5% | 2.1/5.5% | 3 |

> hops-apart=5: decode_failures 45

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.907 | 0.900 | 0.006 | - | - | 0.992 | 0.992 | 0.420 | 1.44x | 18.3/30.3/33.1% | 2.1/5.4% | 3 |
| 30 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 120 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.991 | 0.991 | 0.416 | 1.44x | 18.1/30.3/33.2% | 2.1/5.4% | 3 |
| 600 | 1 | 0.908 | 0.900 | 0.008 | - | - | 0.991 | 0.991 | 0.430 | 1.44x | 18.1/30.4/33.1% | 2.1/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.907 | 0.900 | 0.006 | - | - | 0.992 | 0.992 | 0.420 | 1.44x | 18.3/30.3/33.1% | 2.1/5.4% | 3 |
| 30 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 120 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.991 | 0.991 | 0.416 | 1.44x | 18.1/30.3/33.2% | 2.1/5.4% | 3 |
| 600 | 1 | 0.908 | 0.900 | 0.008 | - | - | 0.991 | 0.991 | 0.430 | 1.44x | 18.1/30.4/33.1% | 2.1/5.4% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.913 | 0.892 | 0.021 | - | - | 0.865 | 0.976 | 0.417 | 1.48x | 19.1/30.7/33.6% | 2.2/5.3% | 3 |
| routers | 1 | 0.902 | 0.900 | 0.001 | - | - | 0.987 | 0.988 | 0.441 | 1.44x | 17.9/30.0/33.1% | 2.1/5.3% | 3 |
| alternate-routers | 1 | 0.902 | 0.902 | 0.001 | - | - | 0.983 | 0.985 | 0.417 | 1.44x | 18.0/30.4/33.3% | 2.1/5.4% | 3 |
| beside-router | 1 | 0.901 | 0.898 | 0.003 | - | - | 0.990 | 0.991 | 0.434 | 1.44x | 18.1/30.1/33.1% | 2.1/5.3% | 3 |
| random-clients | 1 | 0.920 | 0.901 | 0.019 | - | - | 0.957 | 0.991 | 0.420 | 1.46x | 18.6/30.5/33.3% | 2.2/5.3% | 3 |
| hops-apart | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

> place=spread: decode_failures 33

> place=random-clients: decode_failures 41

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.913 | 0.892 | 0.021 | - | - | 0.865 | 0.976 | 0.417 | 1.48x | 19.1/30.7/33.6% | 2.2/5.3% | 3 |
| routers | 1 | 0.902 | 0.900 | 0.001 | - | - | 0.987 | 0.988 | 0.441 | 1.44x | 17.9/30.0/33.1% | 2.1/5.3% | 3 |
| alternate-routers | 1 | 0.902 | 0.902 | 0.001 | - | - | 0.983 | 0.985 | 0.417 | 1.44x | 18.0/30.4/33.3% | 2.1/5.4% | 3 |
| beside-router | 1 | 0.901 | 0.898 | 0.003 | - | - | 0.990 | 0.991 | 0.434 | 1.44x | 18.1/30.1/33.1% | 2.1/5.3% | 3 |
| random-clients | 1 | 0.920 | 0.901 | 0.019 | - | - | 0.957 | 0.991 | 0.420 | 1.46x | 18.6/30.5/33.3% | 2.2/5.3% | 3 |
| hops-apart | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

> place=spread: decode_failures 33

> place=random-clients: decode_failures 41

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| broadcast | 1 | 0.929 | 0.890 | 0.039 | - | - | 0.989 | 0.991 | 0.483 | 1.54x | 19.5/32.3/35.1% | 2.2/5.7% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| heard | 1 | 0.907 | 0.900 | 0.007 | - | - | 0.992 | 0.993 | 0.428 | 1.45x | 18.2/30.4/33.2% | 2.1/5.4% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.929 | 0.890 | 0.039 | - | - | 0.989 | 0.991 | 0.483 | 1.54x | 19.5/32.3/35.1% | 2.2/5.7% | 3 |
| heard | 1 | 0.930 | 0.898 | 0.032 | - | - | 0.984 | 0.988 | 0.499 | 1.54x | 19.6/32.2/35.0% | 2.3/5.7% | 3 |

> replay-ordering=heard: misdecodes 6

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| enum | 1 | 0.911 | 0.904 | 0.007 | - | - | 0.993 | 0.994 | 0.433 | 1.43x | 18.2/30.8/33.5% | 2.1/5.5% | 3 |
| hybrid | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.902 | 0.900 | 0.001 | - | - | 0.987 | 0.988 | 0.441 | 1.44x | 17.9/30.0/33.1% | 2.1/5.3% | 3 |
| 6 | 1 | 0.904 | 0.901 | 0.002 | - | - | 0.992 | 0.992 | 0.443 | 1.49x | 18.7/31.2/34.2% | 2.1/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.904 | 0.902 | 0.003 | - | - | 0.985 | 0.986 | 0.432 | 1.43x | 17.9/30.1/33.1% | 2.1/5.3% | 2 |
| 3 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 5 | 1 | 0.907 | 0.895 | 0.012 | - | - | 0.995 | 0.996 | 0.445 | 1.48x | 18.6/31.0/33.9% | 2.1/5.5% | 5 |
| 8 | 1 | 0.906 | 0.893 | 0.013 | - | - | 0.997 | 0.997 | 0.424 | 1.52x | 19.1/31.5/34.6% | 2.2/5.7% | 8 |

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.904 | 0.902 | 0.003 | - | - | 0.985 | 0.986 | 0.432 | 1.43x | 17.9/30.1/33.1% | 2.1/5.3% | 2 |
| 3 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 5 | 1 | 0.907 | 0.895 | 0.012 | - | - | 0.995 | 0.996 | 0.445 | 1.48x | 18.6/31.0/33.9% | 2.1/5.5% | 5 |
| 8 | 1 | 0.906 | 0.893 | 0.013 | - | - | 0.997 | 0.997 | 0.424 | 1.52x | 19.1/31.5/34.6% | 2.2/5.7% | 8 |

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| True | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.907 | 0.900 | 0.007 | - | - | 0.991 | 0.994 | 0.404 | 1.35x | 17.3/28.4/31.0% | 1.9/5.0% | 3 |
| 1 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.994 | 0.994 | 0.422 | 1.36x | 17.4/28.6/31.4% | 2.0/5.1% | 3 |
| 2 | 1 | 0.912 | 0.908 | 0.005 | - | - | 0.992 | 0.993 | 0.432 | 1.36x | 17.5/28.9/31.6% | 2.0/5.1% | 3 |
| 4 | 1 | 0.905 | 0.898 | 0.006 | - | - | 0.990 | 0.990 | 0.414 | 1.34x | 17.1/28.2/30.9% | 1.9/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.906 | 0.899 | 0.008 | - | - | 0.990 | 0.991 | 0.436 | 1.45x | 18.3/30.8/33.6% | 2.1/5.5% | 3 |
| 24 | 1 | 0.907 | 0.900 | 0.007 | - | - | 0.990 | 0.991 | 0.426 | 1.42x | 17.9/30.1/32.8% | 2.1/5.4% | 3 |
| 32 | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.990 | 0.991 | 0.423 | 1.44x | 18.2/30.3/33.1% | 2.1/5.4% | 3 |
| 64 | 1 | 0.910 | 0.903 | 0.007 | - | - | 0.996 | 0.997 | 0.438 | 1.45x | 18.4/30.5/33.4% | 2.1/5.5% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.900 | 0.890 | 0.009 | - | - | 0.989 | 0.991 | 0.429 | 1.53x | 19.5/32.2/35.1% | 2.2/5.7% | 3 |
| 16 | 1 | 0.906 | 0.898 | 0.008 | - | - | 0.993 | 0.994 | 0.433 | 1.49x | 18.9/31.3/34.0% | 2.2/5.5% | 3 |
| 32 | 1 | 0.903 | 0.895 | 0.008 | - | - | 0.986 | 0.988 | 0.434 | 1.42x | 17.8/29.9/32.7% | 2.0/5.3% | 3 |

> window-size=8: misdecodes 103

> window-size=16: misdecodes 81

> window-size=32: misdecodes 23

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.998 | 0.998 | 0.656 | 1.99x | 24.2/36.6/41.2% | 1.2/5.2% | 3 |
| True | 1 | 0.739 | 0.734 | 0.005 | - | - | 0.860 | 0.887 | 0.426 | 5.45x | 61.4/74.9/79.5% | 3.7/12.8% | 3 |

> no-congestion-scaling=True: queue drops 19.3% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 98

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.536 | 0.525 | 0.011 | - | - | 0.839 | 0.840 | 0.085 | 4.84x | 19.1/35.8/46.8% | 1.6/6.4% | 3 |
| truesize | 1 | 0.579 | 0.570 | 0.009 | - | - | 0.871 | 0.873 | 0.098 | 3.55x | 13.9/28.1/37.4% | 1.2/5.3% | 3 |

> congestion-input=hotstore: decode_failures 3

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.971 | 0.970 | 0.001 | - | - | 1.000 | 1.000 | 0.619 | 1.95x | 23.5/35.3/39.7% | 1.2/5.0% | 3 |
| adaptive | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.998 | 0.998 | 0.656 | 1.99x | 24.2/36.6/41.2% | 1.2/5.2% | 3 |

