# Sweep blocks-2026-10-26-7101151

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 7101151 · seeds 7101151
- **blocks** 87 run
- **compute** 10.9 h of simulator time across every cell
- **generated** 2026-10-26T09:40:42+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>74 warnings</summary>

- AD-siting: siting-mix=basement-heavy: decode_failures 4
- BL-control: protocol=sr: decode_failures 28
- BL-control: slower: 4.41 s per simulated hour against 1.81 over 66 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 53
- DB-warm: warm-num-nodes=0: queue drops 21.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 121
- DB-warm: warm-num-nodes=25: queue drops 21.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 121
- DB-warm: warm-num-nodes=100: queue drops 21.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 121
- DB-warm: warm-num-nodes=2000: queue drops 21.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 121
- DG-burst: burst-loss=0.2: decode_failures 6
- DG-burst: burst-loss=0.3: decode_failures 33
- DG-loss: faster: 1.12 s per simulated hour against 2.25 over 66 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DG-outage: burst-loss=0.1: decode_failures 49
- DG-outage: burst-loss=0.2: decode_failures 47
- DG-outage: burst-loss=0.3: decode_failures 26
- FW-signing-cost: profile-flag=signing=false: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: queue drops 13.8% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 6
- LD-chatty: broadcast-interval-s=300: decode_failures 13
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 21.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 121
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 28.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 102
- MS-density: nodes=90: misdecodes 1
- MS-density: nodes=150: misdecodes 1
- MS-density: nodes=150: decode_failures 9
- MS-hopscale: nodes=250: decode_failures 3
- MS-hopscale: nodes=500: decode_failures 223
- MS-oversubscribed: nodes=500: decode_failures 160
- MS-size: nodes=150: decode_failures 2
- MS-topology: topology=corridor: decode_failures 24
- PR-repeats-busy: extra-repeats=True: misdecodes 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-txpower: tx-power=17: decode_failures 1
- RT-adopt: no-adopt-hop-recommendation=True: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 30
- SF-bucket-mode: bucket-mode=time: misdecodes 42
- SF-bucket-mode: bucket-mode=window: misdecodes 31
- SF-bucket-time: time-bucket-s=600: misdecodes 105
- SF-bucket-time: time-bucket-s=1800: misdecodes 42
- SF-bucket-time: time-bucket-s=3600: misdecodes 18
- SF-cadence: trigger=interval: misdecodes 24
- SF-cadence: trigger=aimd: misdecodes 7
- SF-cadence: trigger=bucket+interval: misdecodes 26
- SF-capacity-local: capacity=4: decode_failures 16
- SF-capacity-local: capacity=8: decode_failures 5
- SF-capacity: capacity=4: decode_failures 16
- SF-capacity: capacity=8: decode_failures 5
- SF-capacity: faster: 0.837 s per simulated hour against 1.7 over 66 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-capacity-window: capacity=8: misdecodes 16
- SF-capacity-window: capacity=16: misdecodes 13
- SF-capacity-window: capacity=32: misdecodes 31
- SF-catchup: catch-up-hours=: misdecodes 26
- SF-catchup: catch-up-hours=02-06: decode_failures 2
- SF-catchup: catch-up-hours=00-08: misdecodes 2
- SF-catchup: faster: 2.7 s per simulated hour against 8.76 over 66 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: hops-apart=3: decode_failures 28
- SF-hops-flat: hops-apart=4: decode_failures 21
- SF-hops-spread: hops-apart=3: decode_failures 28
- SF-hops-spread: hops-apart=4: decode_failures 21
- SF-hops-spread: hops-apart=5: decode_failures 46
- SF-place-spread: faster: 1.02 s per simulated hour against 2.77 over 66 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 24
- SF-replay-order: replay-ordering=heard: misdecodes 30
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 130
- SF-window-size: window-size=16: misdecodes 61
- SF-window-size: window-size=32: misdecodes 31
- TH-congestion: no-congestion-scaling=True: queue drops 19.1% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 101

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 4.41 | 1.81 | 2.44x | 66 |
| `MS-oversubscribed` | 35.2 | 19.6 | 1.80x | 66 |
| `MS-siting` | 1.22 | 1.82 | 0.67x | 65 |
| `FW-firmware` | 1.08 | 1.63 | 0.66x | 66 |
| `SF-cadence` | 2.39 | 3.61 | 0.66x | 66 |
| `DB-hotstore` | 1.56 | 2.36 | 0.66x | 66 |
| `AD-nomute` | 1.49 | 2.25 | 0.66x | 66 |
| `SF-jitter-global` | 1.15 | 1.77 | 0.65x | 66 |
| `RT-hopspread` | 1.32 | 2.03 | 0.65x | 66 |
| `AD-siting` | 0.891 | 1.42 | 0.63x | 66 |
| `SF-capacity-window` | 0.981 | 1.6 | 0.61x | 66 |
| `SF-advert-transport` | 1.01 | 1.68 | 0.60x | 66 |
| `RF-preset` | 1.67 | 2.81 | 0.59x | 66 |
| `SF-place-flat` | 1.66 | 2.83 | 0.59x | 66 |
| `RF-stretch-duct` | 1.07 | 1.82 | 0.58x | 66 |
| `FW-signing-cost` | 0.903 | 1.55 | 0.58x | 66 |
| `SF-replay-order` | 0.906 | 1.56 | 0.58x | 66 |
| `RT-hopassign` | 1.02 | 1.76 | 0.58x | 66 |
| `SF-servers-spread` | 1.29 | 2.22 | 0.58x | 66 |
| `SF-bucket-mode` | 0.818 | 1.43 | 0.57x | 66 |
| `LD-interval` | 0.747 | 1.31 | 0.57x | 66 |
| `SF-jitter-local` | 0.938 | 1.78 | 0.53x | 66 |
| `DG-loss` | 1.12 | 2.25 | 0.50x | 66 |
| `SF-capacity` | 0.837 | 1.7 | 0.49x | 66 |
| `SF-place-spread` | 1.02 | 2.77 | 0.37x | 66 |
| `SF-catchup` | 2.7 | 8.76 | 0.31x | 66 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.983 | 0.983 | 0.891 → 0.901 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.965 | 0.965 | 0.897 → 0.899 | 1.1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **text** | 0.101 → 0.907 | 0.806 | 0.101 → 0.901 | 4.4x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.149 → 0.945 | 0.796 | 0.124 → 0.862 | 90x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **text** | 0.125 → 0.907 | 0.782 | 0.125 → 0.901 | 4.4x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.064 → 0.845 | 0.780 | 0.063 → 0.828 | 4.2x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.178 → 0.907 | 0.729 | 0.178 → 0.901 | 3.5x advert_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.236 → 0.849 | 0.614 | 0.228 → 0.844 | 2x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.304 → 0.907 | 0.603 | 0.298 → 0.901 | 17x sr_bytes | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.425 → 0.977 | 0.552 | 0.424 → 0.977 | 1.7x sr_airtime | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.425 → 0.907 | 0.482 | 0.414 → 0.901 | 1.8x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.425 → 0.907 | 0.482 | 0.414 → 0.901 | 2.4x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **text** | 0.306 → 0.787 | 0.481 | 0.298 → 0.781 | 6.4x sr_bytes | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.575 → 0.907 | 0.332 | 0.543 → 0.901 | 3.7x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.609 → 0.924 | 0.316 | 0.581 → 0.922 | 6.8x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.637 → 0.948 | 0.311 | 0.618 → 0.943 | 2.3x sr_bytes | up | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.470 → 0.774 | 0.304 | 0.452 → 0.761 | 1.6x sr_airtime | up | 2 |
| `DG-burst` | burst-loss | **text** | 0.616 → 0.907 | 0.291 | 0.570 → 0.901 | 3.4x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.672 → 0.954 | 0.281 | 0.649 → 0.953 | 8.7x sr_airtime | down | 3 |
| `MS-density` | nodes | **text** | 0.697 → 0.970 | 0.272 | 0.678 → 0.968 | 4.4x advert_bytes | up | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.532 → 0.787 | 0.255 | 0.307 → 0.499 | 5.1x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.714 → 0.959 | 0.245 | 0.705 → 0.957 | 4.7x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.681 → 0.907 | 0.226 | 0.669 → 0.901 | 5.3x sr_bytes | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.743 → 0.963 | 0.220 | 0.693 → 0.962 | 2.8x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.743 → 0.943 | 0.200 | 0.693 → 0.939 | 2.4x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.806 → 0.985 | 0.179 | 0.719 → 0.901 | 1.5x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.743 → 0.907 | 0.164 | 0.693 → 0.901 | 2.4x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.775 → 0.907 | 0.132 | 0.775 → 0.901 | 1.5x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.786 → 0.907 | 0.121 | 0.768 → 0.901 | 1.8x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.845 → 0.935 | 0.090 | 0.828 → 0.932 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.845 → 0.935 | 0.090 | 0.828 → 0.932 | 2.6x bytes_on_air | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.833 → 0.921 | 0.089 | 0.817 → 0.917 | 2.3x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.834 → 0.921 | 0.087 | 0.820 → 0.917 | 2.4x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.753 → 0.831 | 0.078 | 0.632 → 0.686 | 1.4x sr_airtime | down | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.911 → 0.983 | 0.072 | 0.894 → 0.901 | 3.4x sr_bytes | down | 5 |
| `LD-interval` | broadcast-interval-s | **text** | 0.870 → 0.937 | 0.067 | 0.858 → 0.936 | 5.4x sr_airtime | up | 4 |
| `MS-roles-fav` | role-mix | **text** | 0.845 → 0.912 | 0.067 | 0.829 → 0.906 | 1.2x sr_bytes | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.907 → 0.970 | 0.063 | 0.901 → 0.970 | 1.5x bytes_on_air | up | 3 |
| `MS-roles` | role-mix | **text** | 0.845 → 0.906 | 0.061 | 0.828 → 0.900 | 1.2x bytes_on_air | down | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.907 → 0.960 | 0.053 | 0.901 → 0.959 | 1.7x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.907 → 0.952 | 0.045 | 0.901 → 0.948 | 1.3x bytes_on_air | up | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.503 → 0.541 | 0.038 | 0.494 → 0.533 | 1.5x sr_airtime | up | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.887 → 0.920 | 0.033 | 0.884 → 0.918 | 2x bytes_on_air | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.874 → 0.907 | 0.033 | 0.864 → 0.901 | 1.6x sr_airtime | down | 4 |
| `AD-badrouters` | role-placement | **held** | 0.949 → 0.980 | 0.031 | 0.827 → 0.835 | 1.2x sr_bytes | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.954 → 0.983 | 0.029 | 0.899 → 0.901 | 22x sr_airtime | down | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.888 → 0.916 | 0.028 | 0.886 → 0.914 | 2.2x bytes_on_air | down | 4 |
| `AD-worst` | role-placement | **text** | 0.835 → 0.863 | 0.028 | 0.828 → 0.862 | 1.4x sr_bytes | down | 2 |
| `SF-cadence` | trigger | **held** | 0.959 → 0.983 | 0.024 | 0.885 → 0.901 | 18x sr_bytes | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.961 → 0.983 | 0.022 | 0.895 → 0.901 | 3.4x sr_bytes | down | 4 |
| `SF-place-flat` | place | **text** | 0.896 → 0.917 | 0.022 | 0.894 → 0.903 | 3.1x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.896 → 0.917 | 0.022 | 0.894 → 0.903 | 3.1x sr_bytes | down | 6 |
| `FW-signing-cost` | profile-flag | **text** | 0.907 → 0.928 | 0.021 | 0.901 → 0.926 | 3.3x bytes_on_air | down | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.964 → 0.983 | 0.019 | 0.886 → 0.901 | 1.4x bytes_on_air | down | 4 |
| `SF-servers-flat` | servers | **held** | 0.971 → 0.988 | 0.017 | 0.890 → 0.905 | 8.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.971 → 0.988 | 0.017 | 0.890 → 0.905 | 8.4x sr_bytes | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.890 → 0.907 | 0.017 | 0.877 → 0.901 | 1.4x sr_bytes | down | 2 |
| `FW-versions` | profile | **text** | 0.893 → 0.910 | 0.017 | 0.886 → 0.907 | 3.3x bytes_on_air | up | 5 |
| `SF-sr-retries` | sr-retries | **held** | 0.967 → 0.983 | 0.016 | 0.888 → 0.902 | 1.1x sr_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.908 → 0.922 | 0.014 | 0.901 → 0.918 | 1.2x sr_bytes | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.896 → 0.908 | 0.012 | 0.885 → 0.905 | 12x sr_bytes | up | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.973 → 0.985 | 0.011 | 0.889 → 0.901 | 5.2x advert_bytes | up | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.975 → 0.986 | 0.011 | 0.895 → 0.898 | 1.4x sr_bytes | up | 2 |
| `FW-firmware` | profile | **text** | 0.897 → 0.907 | 0.010 | 0.891 → 0.901 | 3.3x bytes_on_air | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.949 → 0.959 | 0.010 | 0.947 → 0.957 | 1.2x bytes_on_air | down | 2 |
| `DM-mode` | dm-mode | **held** | 0.969 → 0.979 | 0.010 | 0.876 → 0.884 | 1.2x sr_airtime | up | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.973 → 0.983 | 0.010 | 0.893 → 0.901 | 1.3x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.875 → 0.884 | 0.009 | 0.875 → 0.884 | 1.2x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.974 → 0.983 | 0.009 | 0.892 → 0.901 | 2.5x advert_bytes | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.976 → 0.985 | 0.009 | 0.897 → 0.906 | 3.1x advert_bytes | down | 4 |
| `SF-provide-transport` | provide-transport | **held** | 0.975 → 0.983 | 0.008 | 0.895 → 0.901 | 1.6x sr_airtime | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.901 → 0.909 | 0.008 | 0.895 → 0.904 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.901 → 0.909 | 0.008 | 0.895 → 0.904 | 1.1x sr_bytes | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.907 → 0.914 | 0.007 | 0.901 → 0.911 | 1.4x sr_bytes | down | 3 |
| `SF-servers-allrouters` | servers | **held** | 0.968 → 0.976 | 0.007 | 0.894 → 0.894 | 2.4x sr_bytes | up | 2 |
| `SF-capacity` | capacity | **held** | 0.976 → 0.983 | 0.007 | 0.897 → 0.905 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.976 → 0.983 | 0.007 | 0.897 → 0.905 | 5.3x advert_bytes | up | 5 |
| `SF-window-size` | window-size | **held** | 0.977 → 0.982 | 0.006 | 0.893 → 0.899 | 5.1x advert_bytes | up | 3 |
| `SF-resolve` | resolve | **text** | 0.907 → 0.912 | 0.005 | 0.901 → 0.907 | 5.7x advert_bytes | = | 3 |
| `SF-capacity-window` | capacity | **text** | 0.901 → 0.906 | 0.005 | 0.895 → 0.901 | 3.3x advert_bytes | up | 3 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.875 → 0.878 | 0.003 | 0.875 → 0.878 | 1x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.981 → 0.983 | 0.001 | 0.901 → 0.901 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.958 → 0.959 | 0.001 | 0.956 → 0.957 | 1.1x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.982 → 0.983 | 0.001 | 0.900 → 0.901 | 3x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.959 → 0.960 | 0.001 | 0.957 → 0.959 | 1x sr_bytes | down | 2 |

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
| none | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| sprinkled | 1 | 0.943 | 0.941 | 0.002 | - | - | 0.980 | 0.981 | 0.649 | 1.12x | 18.7/25.1/29.3% | 1.3/5.3% | 3 |
| arms-race | 1 | 0.970 | 0.970 | 0.001 | - | - | 0.994 | 0.994 | 0.926 | 0.87x | 20.8/25.7/28.5% | 1.0/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.939 | 0.930 | 0.009 | - | - | 0.992 | 0.992 | 0.728 | 1.18x | 19.3/25.8/28.4% | 1.6/5.3% | 3 |
| 0.3 | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.999 | 0.999 | 0.870 | 0.96x | 19.3/24.9/28.5% | 1.3/4.8% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.845 | 0.828 | 0.016 | - | - | 0.949 | 0.952 | 0.438 | 1.10x | 14.7/26.5/28.8% | 1.9/5.2% | 3 |
| inverse | 1 | 0.860 | 0.835 | 0.025 | - | - | 0.980 | 0.982 | 0.605 | 1.11x | 15.1/19.8/22.9% | 2.0/3.8% | 3 |
| random | 1 | 0.845 | 0.827 | 0.018 | - | - | 0.961 | 0.962 | 0.545 | 1.07x | 14.9/20.9/23.3% | 1.8/5.0% | 3 |

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.845 | 0.828 | 0.016 | - | - | 0.949 | 0.952 | 0.438 | 1.10x | 14.7/26.5/28.8% | 1.9/5.2% | 3 |
| all-routers | 1 | 0.935 | 0.932 | 0.003 | - | - | 0.974 | 0.974 | 0.821 | 2.88x | 36.8/50.5/52.6% | 4.8/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.845 | 0.828 | 0.016 | - | - | 0.949 | 0.952 | 0.438 | 1.10x | 14.7/26.5/28.8% | 1.9/5.2% | 3 |
| no-mute | 1 | 0.901 | 0.892 | 0.009 | - | - | 0.984 | 0.985 | 0.653 | 1.26x | 17.0/24.6/27.0% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.935 | 0.932 | 0.003 | - | - | 0.974 | 0.974 | 0.821 | 2.88x | 36.8/50.5/52.6% | 4.8/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.845 | 0.828 | 0.016 | - | - | 0.949 | 0.952 | 0.438 | 1.10x | 14.7/26.5/28.8% | 1.9/5.2% | 3 |
| local-typical | 1 | 0.768 | 0.766 | 0.003 | - | - | 0.895 | 0.896 | 0.000 | 1.26x | 17.8/30.3/33.4% | 2.0/5.4% | 3 |
| basement-heavy | 1 | 0.064 | 0.063 | 0.001 | - | - | 0.240 | 0.282 | 0.000 | 0.64x | 1.3/8.4/15.3% | 0.2/3.6% | 3 |

> siting-mix=basement-heavy: decode_failures 4

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.863 | 0.862 | 0.001 | - | - | 0.953 | 0.953 | 0.060 | 2.35x | 18.9/29.4/39.6% | 1.8/5.4% | 3 |
| inverse | 1 | 0.835 | 0.828 | 0.007 | - | - | 0.958 | 0.958 | 0.078 | 2.22x | 16.9/25.1/34.1% | 1.8/3.5% | 3 |

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.897 | 0.897 | 0.000 | - | - | 0 | 0.000 | 0.640 | 1.27x | 17.2/27.5/30.6% | 2.0/5.1% | 3 |
| sr | 1 | 0.913 | 0.899 | 0.014 | - | - | 0.965 | 0.985 | 0.621 | 1.37x | 18.4/29.2/32.5% | 2.1/5.6% | 3 |

> protocol=sr: decode_failures 28

> slower: 4.41 s per simulated hour against 1.81 over 66 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.834 | 0.820 | 0.015 | - | - | 0.923 | 0.926 | 0.630 | 3.13x | 42.9/64.3/69.2% | 4.7/10.2% | 3 |
| 100 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.976 | 0.977 | 0.723 | 1.53x | 21.5/35.0/38.5% | 2.2/5.2% | 3 |
| 120 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.976 | 0.977 | 0.723 | 1.53x | 21.5/35.0/38.5% | 2.2/5.2% | 3 |
| 250 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.976 | 0.977 | 0.723 | 1.53x | 21.5/35.0/38.5% | 2.2/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.314 | 0.307 | 0.007 | - | - | 0.532 | 0.538 | 0.115 | 11.59x | 41.3/63.9/73.4% | 4.0/11.2% | 3 |
| 120 | 1 | 0.503 | 0.494 | 0.009 | - | - | 0.782 | 0.784 | 0.155 | 4.70x | 16.8/32.6/41.3% | 1.5/5.3% | 3 |
| 250 | 1 | 0.508 | 0.499 | 0.009 | - | - | 0.787 | 0.787 | 0.150 | 4.60x | 16.5/31.5/40.1% | 1.5/5.1% | 3 |

> max-num-nodes=10: decode_failures 53

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.976 | 0.977 | 0.723 | 1.53x | 21.5/35.0/38.5% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.976 | 0.977 | 0.723 | 1.53x | 21.5/35.0/38.5% | 2.2/5.2% | 3 |
| constrained | 1 | 0.833 | 0.817 | 0.015 | - | - | 0.920 | 0.925 | 0.621 | 3.13x | 42.8/64.3/69.2% | 4.7/10.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.831 | 0.866 | 0.504 | 5.83x | 58.7/76.2/80.4% | 4.3/12.6% | 3 |
| 25 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.831 | 0.866 | 0.504 | 5.83x | 58.7/76.2/80.4% | 4.3/12.6% | 3 |
| 100 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.831 | 0.866 | 0.504 | 5.83x | 58.7/76.2/80.4% | 4.3/12.6% | 3 |
| 2000 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.831 | 0.866 | 0.504 | 5.83x | 58.7/76.2/80.4% | 4.3/12.6% | 3 |

> warm-num-nodes=0: queue drops 21.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 121

> warm-num-nodes=25: queue drops 21.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 121

> warm-num-nodes=100: queue drops 21.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 121

> warm-num-nodes=2000: queue drops 21.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 121

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.820 | 0.802 | 0.018 | - | - | 0.973 | 0.975 | 0.549 | 1.25x | 17.2/27.3/30.6% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.725 | 0.688 | 0.037 | - | - | 0.942 | 0.949 | 0.446 | 1.16x | 16.3/25.8/28.9% | 1.8/4.5% | 3 |
| 0.3 | 1 | 0.616 | 0.570 | 0.046 | - | - | 0.833 | 0.881 | 0.330 | 1.09x | 15.6/24.8/27.8% | 1.7/4.2% | 3 |

> burst-loss=0.2: decode_failures 6

> burst-loss=0.3: decode_failures 33

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.885 | 0.875 | 0.010 | - | - | 0.983 | 0.985 | 0.591 | 1.39x | 19.1/29.6/32.8% | 2.2/5.3% | 3 |
| 0.2 | 1 | 0.841 | 0.829 | 0.013 | - | - | 0.964 | 0.964 | 0.496 | 1.44x | 19.8/30.9/34.3% | 2.2/5.3% | 3 |
| 0.3 | 1 | 0.786 | 0.768 | 0.019 | - | - | 0.935 | 0.936 | 0.455 | 1.47x | 20.5/32.0/35.1% | 2.3/5.2% | 3 |

> faster: 1.12 s per simulated hour against 2.25 over 66 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.932 | 0.967 | 0.556 | 1.27x | 17.4/27.4/30.6% | 2.0/5.2% | 3 |
| 0.2 | 1 | 0.693 | 0.667 | 0.026 | - | - | 0.884 | 0.937 | 0.390 | 1.18x | 17.1/26.5/29.5% | 1.9/4.7% | 3 |
| 0.3 | 1 | 0.575 | 0.543 | 0.032 | - | - | 0.702 | 0.891 | 0.253 | 1.11x | 15.8/25.1/27.8% | 1.7/4.1% | 3 |

> burst-loss=0.1: decode_failures 49

> burst-loss=0.2: decode_failures 47

> burst-loss=0.3: decode_failures 26

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.876 | 0.876 | 0.000 | - | - | 0.974 | 0.974 | 0.624 | 1.75x | 23.5/37.4/41.6% | 2.8/7.0% | 3 |
| directed-with-late-flood | 1 | 0.884 | 0.884 | 0.000 | - | - | 0.969 | 0.972 | 0.614 | 1.58x | 21.4/33.8/37.6% | 2.5/6.4% | 3 |
| m4-early-flood | 1 | 0.884 | 0.884 | 0.000 | - | - | 0.979 | 0.981 | 0.628 | 1.61x | 21.8/34.6/38.5% | 2.5/6.6% | 3 |

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.897 | 0.891 | 0.006 | - | - | 0.991 | 0.992 | 0.431 | 0.71x | 9.1/11.6/13.0% | 1.2/1.8% | 3 |
| 2.8 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.896 | 0.889 | 0.007 | - | - | 0.977 | 0.979 | 0.560 | 1.22x | 16.8/25.4/28.8% | 1.9/4.9% | 3 |
| 0.5 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.996 | 0.997 | 0.693 | 1.00x | 14.0/20.9/23.8% | 1.4/4.2% | 3 |
| 0.75 | 1 | 0.887 | 0.884 | 0.003 | - | - | 0.986 | 0.987 | 0.540 | 0.91x | 12.7/16.9/19.3% | 1.4/3.7% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.906 | 0.903 | 0.003 | - | - | 0.981 | 0.982 | 0.564 | 1.20x | 16.6/25.6/28.7% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.916 | 0.914 | 0.002 | - | - | 0.993 | 0.994 | 0.668 | 0.97x | 13.9/20.6/23.9% | 1.4/4.3% | 3 |
| 0.75 | 1 | 0.888 | 0.886 | 0.001 | - | - | 0.987 | 0.988 | 0.494 | 0.85x | 12.3/16.4/18.9% | 1.4/3.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.928 | 0.926 | 0.002 | - | - | 0.988 | 0.988 | 0.645 | 0.69x | 9.7/15.9/18.0% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

> profile-flag=signing=false: misdecodes 1

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.895 | 0.891 | 0.005 | - | - | 0.995 | 0.997 | 0.420 | 0.70x | 9.8/12.9/14.3% | 1.2/2.2% | 3 |
| 2.5 | 1 | 0.893 | 0.886 | 0.007 | - | - | 0.995 | 0.996 | 0.367 | 0.73x | 10.0/13.1/14.4% | 1.2/2.3% | 3 |
| 2.6 | 1 | 0.895 | 0.891 | 0.004 | - | - | 0.995 | 0.996 | 0.390 | 0.70x | 9.9/13.2/14.6% | 1.2/2.3% | 3 |
| 2.7 | 1 | 0.910 | 0.907 | 0.003 | - | - | 0.996 | 0.997 | 0.398 | 0.73x | 10.9/15.1/18.0% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.987 | 0.987 | 0.661 | 0.88x | 11.9/18.7/20.9% | 1.4/3.5% | 3 |
| 900 | 1 | 0.870 | 0.858 | 0.011 | - | - | 0.957 | 0.960 | 0.620 | 2.10x | 27.8/44.1/49.2% | 3.2/8.3% | 3 |
| 300 | 1 | 0.609 | 0.581 | 0.028 | - | - | 0.779 | 0.799 | 0.418 | 4.57x | 57.1/76.9/80.8% | 7.5/16.6% | 3 |

> broadcast-interval-s=300: decode_failures 13

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.954 | 0.953 | 0.001 | - | - | 0.990 | 0.990 | 0.795 | 0.95x | 12.6/18.9/21.0% | 1.5/3.6% | 3 |
| 900 | 1 | 0.913 | 0.908 | 0.005 | - | - | 0.971 | 0.971 | 0.721 | 2.33x | 30.5/45.8/50.8% | 3.8/8.6% | 3 |
| 300 | 1 | 0.672 | 0.649 | 0.023 | - | - | 0.840 | 0.858 | 0.427 | 5.05x | 60.4/77.4/81.2% | 8.2/17.7% | 3 |

> broadcast-interval-s=300: queue drops 13.8% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 6

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.913 | 0.909 | 0.004 | - | - | 0.980 | 0.980 | 0.630 | 1.23x | 16.7/26.7/29.8% | 1.9/5.1% | 3 |
| sinusoid | 1 | 0.914 | 0.911 | 0.003 | - | - | 0.983 | 0.984 | 0.614 | 1.23x | 16.6/26.0/29.0% | 2.0/4.9% | 3 |
| commuter | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.870 | 0.858 | 0.011 | - | - | 0.957 | 0.960 | 0.620 | 2.10x | 27.8/44.1/49.2% | 3.2/8.3% | 3 |
| 3600 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.987 | 0.987 | 0.661 | 0.88x | 11.9/18.7/20.9% | 1.4/3.5% | 3 |
| 10800 | 1 | 0.932 | 0.930 | 0.002 | - | - | 0.988 | 0.989 | 0.686 | 0.59x | 8.0/12.3/13.7% | 1.0/2.3% | 3 |
| 43200 | 1 | 0.937 | 0.936 | 0.000 | - | - | 0.995 | 0.995 | 0.657 | 0.43x | 5.9/9.1/10.0% | 0.7/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.900 | 0.894 | 0.006 | - | - | 0.979 | 0.979 | 0.634 | 1.40x | 18.9/29.9/33.3% | 2.2/5.6% | 3 |
| 1.0 | 1 | 0.890 | 0.883 | 0.008 | - | - | 0.973 | 0.973 | 0.622 | 1.58x | 21.3/33.7/37.5% | 2.5/6.4% | 3 |
| 4.0 | 1 | 0.874 | 0.864 | 0.010 | - | - | 0.969 | 0.969 | 0.594 | 1.94x | 26.6/41.5/46.4% | 3.0/8.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.693 | 0.686 | 0.007 | - | - | 0.831 | 0.866 | 0.504 | 5.83x | 58.7/76.2/80.4% | 4.3/12.6% | 3 |
| 1.0 | 1 | 0.638 | 0.632 | 0.006 | - | - | 0.753 | 0.820 | 0.477 | 6.24x | 62.1/77.2/80.8% | 4.6/13.1% | 3 |

> traceroute-per-hour=0.0: queue drops 21.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 121

> traceroute-per-hour=1.0: queue drops 28.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 102

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.697 | 0.678 | 0.019 | - | - | 0.866 | 0.868 | 0.425 | 1.26x | 17.4/29.8/32.2% | 2.8/6.7% | 3 |
| 60 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 90 | 1 | 0.940 | 0.939 | 0.002 | - | - | 0.992 | 0.992 | 0.420 | 1.61x | 19.9/30.5/34.8% | 1.5/5.0% | 3 |
| 120 | 1 | 0.959 | 0.957 | 0.002 | - | - | 0.998 | 0.998 | 0.813 | 2.08x | 22.9/39.8/44.9% | 1.4/4.9% | 3 |
| 150 | 1 | 0.970 | 0.968 | 0.001 | - | - | 0.998 | 0.999 | 0.839 | 2.68x | 28.1/46.6/53.0% | 1.4/5.4% | 3 |

> nodes=90: misdecodes 1

> nodes=150: misdecodes 1

> nodes=150: decode_failures 9

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 120 | 1 | 0.791 | 0.786 | 0.005 | - | - | 0.978 | 0.978 | 0.301 | 2.27x | 16.6/27.5/33.1% | 1.6/5.3% | 3 |
| 250 | 1 | 0.500 | 0.491 | 0.009 | - | - | 0.783 | 0.783 | 0.149 | 4.95x | 17.9/34.3/43.5% | 1.6/5.7% | 3 |
| 500 | 1 | 0.304 | 0.298 | 0.006 | - | - | 0.534 | 0.573 | 0.090 | 10.20x | 17.1/38.0/57.6% | 1.7/6.6% | 3 |

> nodes=250: decode_failures 3

> nodes=500: decode_failures 223

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.787 | 0.781 | 0.005 | - | - | 0.979 | 0.979 | 0.312 | 2.10x | 15.4/25.5/30.6% | 1.5/4.9% | 3 |
| 250 | 1 | 0.503 | 0.494 | 0.009 | - | - | 0.782 | 0.784 | 0.155 | 4.70x | 16.8/32.6/41.3% | 1.5/5.3% | 3 |
| 500 | 1 | 0.306 | 0.298 | 0.007 | - | - | 0.545 | 0.575 | 0.092 | 9.60x | 16.0/36.1/54.9% | 1.6/6.3% | 3 |

> nodes=500: decode_failures 160

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.984 | 0.986 | 0.603 | 1.31x | 17.6/28.2/31.5% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.845 | 0.828 | 0.016 | - | - | 0.949 | 0.952 | 0.438 | 1.10x | 14.7/26.5/28.8% | 1.9/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.912 | 0.906 | 0.006 | - | - | 0.979 | 0.980 | 0.644 | 1.38x | 18.7/28.9/32.2% | 2.2/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.845 | 0.829 | 0.017 | - | - | 0.937 | 0.938 | 0.447 | 1.23x | 17.3/30.2/31.9% | 2.2/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.05 | 1 | 0.900 | 0.895 | 0.005 | - | - | 0.971 | 0.972 | 0.635 | 1.45x | 19.1/33.5/37.8% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.898 | 0.890 | 0.008 | - | - | 0.974 | 0.974 | 0.630 | 1.57x | 22.4/37.2/42.3% | 2.3/5.3% | 3 |
| 0.2 | 1 | 0.893 | 0.886 | 0.006 | - | - | 0.964 | 0.964 | 0.642 | 1.77x | 25.7/43.1/47.9% | 2.3/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| local-typical | 1 | 0.806 | 0.805 | 0.001 | - | - | 0.914 | 0.914 | 0.000 | 1.46x | 20.2/32.2/35.3% | 2.2/5.5% | 3 |
| event | 1 | 0.425 | 0.424 | 0.001 | - | - | 0.643 | 0.644 | 0.000 | 1.36x | 11.4/29.5/33.8% | 1.9/5.3% | 3 |
| backbone | 1 | 0.977 | 0.977 | 0.000 | - | - | 0.999 | 0.999 | 0.933 | 1.10x | 28.3/37.3/39.9% | 1.3/5.5% | 3 |

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.832 | 0.821 | 0.011 | - | - | 0.945 | 0.947 | 0.401 | 1.40x | 24.8/37.7/42.8% | 3.2/7.7% | 3 |
| 60 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 90 | 1 | 0.876 | 0.872 | 0.004 | - | - | 0.983 | 0.984 | 0.621 | 1.71x | 16.6/29.6/33.3% | 1.7/4.8% | 3 |
| 120 | 1 | 0.791 | 0.786 | 0.005 | - | - | 0.978 | 0.978 | 0.301 | 2.27x | 16.6/27.5/33.1% | 1.6/5.3% | 3 |
| 150 | 1 | 0.681 | 0.669 | 0.013 | - | - | 0.916 | 0.917 | 0.275 | 2.89x | 15.6/28.4/33.3% | 1.6/5.3% | 3 |

> nodes=150: decode_failures 2

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 1.25 | 1 | 0.718 | 0.709 | 0.009 | - | - | 0.890 | 0.890 | 0.252 | 1.35x | 13.9/22.8/26.2% | 2.0/5.2% | 3 |
| 1.5 | 1 | 0.470 | 0.452 | 0.018 | - | - | 0.678 | 0.681 | 0.000 | 1.32x | 10.5/19.2/22.8% | 2.0/4.6% | 3 |
| 2.0 | 1 | 0.178 | 0.178 | 0.001 | - | - | 0.290 | 0.293 | 0.000 | 1.05x | 5.2/12.8/16.8% | 1.5/4.1% | 3 |

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| clustered | 1 | 0.897 | 0.891 | 0.006 | - | - | 0.975 | 0.976 | 0.751 | 0.92x | 19.7/28.6/30.6% | 1.1/5.0% | 3 |
| corridor | 1 | 0.637 | 0.618 | 0.019 | - | - | 0.726 | 0.771 | 0.023 | 1.28x | 15.1/23.3/25.5% | 1.9/5.4% | 3 |
| hub | 1 | 0.948 | 0.943 | 0.005 | - | - | 0.981 | 0.983 | 0.667 | 1.15x | 26.1/35.9/37.3% | 1.5/5.5% | 3 |

> topology=corridor: decode_failures 24

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.884 | 0.884 | 0.000 | - | - | 0.969 | 0.972 | 0.614 | 1.58x | 21.4/33.8/37.6% | 2.5/6.4% | 3 |
| True | 1 | 0.875 | 0.875 | 0.000 | - | - | 0.971 | 0.973 | 0.623 | 1.60x | 21.7/34.6/38.4% | 2.5/6.6% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.875 | 0.875 | 0.000 | - | - | 0.971 | 0.973 | 0.623 | 1.60x | 21.7/34.6/38.4% | 2.5/6.6% | 3 |
| m4-early-flood | 1 | 0.878 | 0.878 | 0.000 | - | - | 0.972 | 0.975 | 0.638 | 1.59x | 21.5/34.4/38.1% | 2.4/6.5% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.897 | 0.897 | 0.000 | - | - | 0 | 0.000 | 0.640 | 1.27x | 17.2/27.5/30.6% | 2.0/5.1% | 3 |
| chain | 1 | 0.894 | 0.891 | 0.003 | - | - | 0.965 | 0.983 | 0.614 | 1.51x | 20.5/32.9/36.7% | 2.3/6.2% | 3 |
| sr | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| True | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.981 | 0.982 | 0.650 | 1.34x | 18.0/28.7/31.9% | 2.1/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.959 | 0.957 | 0.002 | - | - | 0.998 | 0.998 | 0.813 | 2.08x | 22.9/39.8/44.9% | 1.4/4.9% | 3 |
| True | 1 | 0.958 | 0.956 | 0.002 | - | - | 0.998 | 0.998 | 0.830 | 2.13x | 23.2/40.5/45.7% | 1.5/5.0% | 3 |

> extra-repeats=True: misdecodes 2

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.236 | 0.228 | 0.008 | - | - | 0.476 | 0.478 | 0.000 | 0.05x | 0.3/0.9/1.0% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.561 | 0.550 | 0.011 | - | - | 0.801 | 0.801 | 0.017 | 0.27x | 2.4/4.4/6.0% | 0.4/1.2% | 3 |
| LONG_TURBO | 1 | 0.849 | 0.844 | 0.006 | - | - | 0.949 | 0.949 | 0.596 | 1.25x | 13.9/23.2/25.2% | 1.9/5.1% | 3 |

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.919 | 0.914 | 0.004 | - | - | 0.985 | 0.985 | 0.690 | 1.24x | 19.5/29.6/32.7% | 1.9/5.4% | 3 |
| 1.0 | 1 | 0.952 | 0.948 | 0.004 | - | - | 0.992 | 0.992 | 0.837 | 0.98x | 24.6/32.7/34.9% | 1.3/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.425 | 0.414 | 0.012 | - | - | 0.693 | 0.693 | 0.000 | 0.14x | 1.2/2.2/3.2% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| LITE_FAST | 1 | 0.862 | 0.856 | 0.006 | - | - | 0.962 | 0.962 | 0.530 | 1.01x | 12.0/21.5/23.4% | 1.5/4.1% | 3 |
| NARROW_SLOW | 1 | 0.880 | 0.875 | 0.004 | - | - | 0.969 | 0.969 | 0.610 | 1.28x | 16.6/26.5/28.7% | 1.9/5.4% | 3 |

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| temporal | 1 | 0.844 | 0.832 | 0.012 | - | - | 0.961 | 0.961 | 0.500 | 1.34x | 18.1/28.6/31.9% | 2.0/5.4% | 3 |
| transient | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.985 | 0.987 | 0.608 | 1.33x | 17.8/28.4/31.7% | 2.1/5.4% | 3 |
| periodic | 1 | 0.728 | 0.719 | 0.009 | - | - | 0.806 | 0.809 | 0.468 | 1.23x | 16.9/26.4/29.6% | 1.9/4.7% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.425 | 0.414 | 0.012 | - | - | 0.693 | 0.693 | 0.000 | 0.14x | 1.2/2.2/3.2% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| LONG_MODERATE | 1 | 0.851 | 0.840 | 0.011 | - | - | 0.932 | 0.933 | 0.706 | 3.31x | 49.8/67.0/70.1% | 4.9/11.9% | 3 |

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.101 | 0.101 | 0.000 | - | - | 0.231 | 0.235 | 0.000 | 0.01x | 0.0/0.2/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.236 | 0.228 | 0.008 | - | - | 0.476 | 0.478 | 0.000 | 0.05x | 0.3/0.9/1.0% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| LONG_TURBO | 1 | 0.849 | 0.844 | 0.006 | - | - | 0.949 | 0.949 | 0.596 | 1.25x | 13.9/23.2/25.2% | 1.9/5.1% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.890 | 0.885 | 0.005 | - | - | 0.966 | 0.966 | 0.660 | 1.79x | 22.6/36.5/40.1% | 2.8/7.1% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.868 | 0.862 | 0.006 | - | - | 0.945 | 0.946 | 0.587 | 1.31x | 17.8/28.3/31.6% | 2.0/5.2% | 3 |
| 10000 | 1 | 0.728 | 0.719 | 0.009 | - | - | 0.806 | 0.809 | 0.468 | 1.23x | 16.9/26.4/29.6% | 1.9/4.7% | 3 |
| 4000 | 1 | 0.481 | 0.474 | 0.007 | - | - | 0.552 | 0.575 | 0.260 | 1.06x | 14.9/23.3/25.7% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.124 | 0.124 | 0.000 | - | - | 0.149 | 0.209 | 0.057 | 0.73x | 10.8/16.8/18.4% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.470 | 0.452 | 0.018 | - | - | 0.678 | 0.681 | 0.000 | 1.32x | 10.5/19.2/22.8% | 2.0/4.6% | 3 |
| 1.0 | 1 | 0.774 | 0.761 | 0.012 | - | - | 0.879 | 0.879 | 0.518 | 1.03x | 17.5/24.2/26.2% | 1.4/4.7% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 22 | 1 | 0.530 | 0.515 | 0.015 | - | - | 0.760 | 0.764 | 0.104 | 1.25x | 11.4/18.6/22.6% | 1.9/4.5% | 3 |
| 17 | 1 | 0.207 | 0.198 | 0.009 | - | - | 0.415 | 0.417 | 0.000 | 1.13x | 6.3/17.9/21.7% | 1.5/5.1% | 3 |
| 14 | 1 | 0.125 | 0.125 | 0.001 | - | - | 0.241 | 0.253 | 0.000 | 0.87x | 4.5/10.7/13.9% | 1.4/3.5% | 3 |

> tx-power=17: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.959 | 0.957 | 0.002 | - | - | 0.998 | 0.998 | 0.813 | 2.08x | 22.9/39.8/44.9% | 1.4/4.9% | 3 |
| True | 1 | 0.949 | 0.947 | 0.002 | - | - | 0.996 | 0.996 | 0.800 | 2.46x | 26.4/45.2/50.2% | 1.7/5.6% | 3 |

> no-adopt-hop-recommendation=True: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.908 | 0.901 | 0.007 | - | - | 0.981 | 0.982 | 0.680 | 1.38x | 18.6/31.2/34.3% | 2.0/5.3% | 3 |
| True | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.978 | 0.979 | 0.693 | 1.46x | 19.7/32.3/35.3% | 2.2/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| random | 1 | 0.890 | 0.877 | 0.013 | - | - | 0.968 | 0.968 | 0.648 | 1.27x | 16.8/27.4/30.5% | 2.0/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.743 | 0.693 | 0.050 | - | - | 0.962 | 0.965 | 0.220 | 0.98x | 13.6/23.7/26.5% | 1.4/4.8% | 3 |
| 7 | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.989 | 0.989 | 0.763 | 1.42x | 18.8/29.1/32.5% | 2.3/5.4% | 3 |
| 15 | 1 | 0.955 | 0.954 | 0.001 | - | - | 0.986 | 0.986 | 0.854 | 1.42x | 18.8/28.8/32.1% | 2.2/5.3% | 3 |
| 32 | 1 | 0.963 | 0.962 | 0.001 | - | - | 0.995 | 0.996 | 0.873 | 1.45x | 19.1/29.1/32.3% | 2.3/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.743 | 0.693 | 0.050 | - | - | 0.962 | 0.965 | 0.220 | 0.98x | 13.6/23.7/26.5% | 1.4/4.8% | 3 |
| 5 | 1 | 0.894 | 0.884 | 0.010 | - | - | 0.981 | 0.982 | 0.575 | 1.29x | 17.5/27.8/31.0% | 2.0/5.3% | 3 |
| 7 | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.989 | 0.989 | 0.763 | 1.42x | 18.8/29.1/32.5% | 2.3/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.899 | 0.899 | 0.000 | - | - | 0.954 | 0.976 | 0.650 | 1.28x | 17.3/27.7/30.9% | 2.0/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.743 | 0.693 | 0.050 | - | - | 0.962 | 0.965 | 0.220 | 0.98x | 13.6/23.7/26.5% | 1.4/4.8% | 3 |
| True | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| BALANCED | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| STRICT | 1 | 0.775 | 0.775 | 0.000 | - | - | 0.862 | 0.863 | 0.484 | 1.47x | 20.0/31.1/34.5% | 2.4/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| dm | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.982 | 0.982 | 0.632 | 1.31x | 17.7/28.4/31.7% | 2.0/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.900 | 0.892 | 0.007 | - | - | 0.974 | 0.975 | 0.638 | 1.33x | 18.0/29.0/32.3% | 2.1/5.4% | 3 |
| local | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| time | 1 | 0.903 | 0.898 | 0.006 | - | - | 0.982 | 0.982 | 0.635 | 1.35x | 18.2/29.2/32.5% | 2.1/5.5% | 3 |
| window | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.982 | 0.984 | 0.637 | 1.30x | 17.4/28.2/31.3% | 2.0/5.3% | 3 |

> bucket-mode=global: misdecodes 30

> bucket-mode=time: misdecodes 42

> bucket-mode=window: misdecodes 31

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.896 | 0.889 | 0.007 | - | - | 0.973 | 0.973 | 0.640 | 1.46x | 19.7/31.5/35.0% | 2.2/6.0% | 3 |
| 1800 | 1 | 0.903 | 0.898 | 0.006 | - | - | 0.982 | 0.982 | 0.635 | 1.35x | 18.2/29.2/32.5% | 2.1/5.5% | 3 |
| 3600 | 1 | 0.907 | 0.901 | 0.005 | - | - | 0.985 | 0.985 | 0.627 | 1.32x | 17.8/28.7/31.9% | 2.0/5.4% | 3 |

> time-bucket-s=600: misdecodes 105

> time-bucket-s=1800: misdecodes 42

> time-bucket-s=3600: misdecodes 18

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| interval | 1 | 0.897 | 0.887 | 0.010 | - | - | 0.974 | 0.979 | 0.637 | 1.77x | 24.5/40.2/44.0% | 2.6/9.4% | 3 |
| aimd | 1 | 0.895 | 0.892 | 0.003 | - | - | 0.959 | 0.980 | 0.627 | 1.32x | 17.8/28.7/31.9% | 2.1/5.4% | 3 |
| bucket+interval | 1 | 0.896 | 0.885 | 0.011 | - | - | 0.976 | 0.977 | 0.661 | 1.76x | 24.1/39.4/43.3% | 2.6/8.2% | 3 |

> trigger=interval: misdecodes 24

> trigger=aimd: misdecodes 7

> trigger=bucket+interval: misdecodes 26

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.976 | 0.977 | 0.650 | 1.33x | 17.8/28.6/31.8% | 2.0/5.4% | 3 |
| 8 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.979 | 0.979 | 0.639 | 1.32x | 17.8/28.4/31.5% | 2.0/5.3% | 3 |
| 16 | 1 | 0.910 | 0.905 | 0.005 | - | - | 0.983 | 0.984 | 0.659 | 1.35x | 18.2/29.1/32.3% | 2.1/5.5% | 3 |
| 32 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 50 | 1 | 0.904 | 0.898 | 0.006 | - | - | 0.982 | 0.982 | 0.630 | 1.35x | 18.1/29.0/32.2% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 16

> capacity=8: decode_failures 5

> faster: 0.837 s per simulated hour against 1.7 over 66 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.976 | 0.977 | 0.650 | 1.33x | 17.8/28.6/31.8% | 2.0/5.4% | 3 |
| 8 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.979 | 0.979 | 0.639 | 1.32x | 17.8/28.4/31.5% | 2.0/5.3% | 3 |
| 16 | 1 | 0.910 | 0.905 | 0.005 | - | - | 0.983 | 0.984 | 0.659 | 1.35x | 18.2/29.1/32.3% | 2.1/5.5% | 3 |
| 32 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 50 | 1 | 0.904 | 0.898 | 0.006 | - | - | 0.982 | 0.982 | 0.630 | 1.35x | 18.1/29.0/32.2% | 2.1/5.5% | 3 |

> capacity=4: decode_failures 16

> capacity=8: decode_failures 5

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.901 | 0.895 | 0.006 | - | - | 0.978 | 0.979 | 0.634 | 1.32x | 17.9/28.6/31.8% | 2.0/5.4% | 3 |
| 16 | 1 | 0.906 | 0.901 | 0.004 | - | - | 0.980 | 0.980 | 0.614 | 1.30x | 17.6/28.2/31.5% | 2.0/5.3% | 3 |
| 32 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.982 | 0.984 | 0.637 | 1.30x | 17.4/28.2/31.3% | 2.0/5.3% | 3 |

> capacity=8: misdecodes 16

> capacity=16: misdecodes 13

> capacity=32: misdecodes 31

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.896 | 0.885 | 0.011 | - | - | 0.976 | 0.977 | 0.661 | 1.76x | 24.1/39.4/43.3% | 2.6/8.2% | 3 |
| 02-06 | 1 | 0.907 | 0.904 | 0.003 | - | - | 0.975 | 0.984 | 0.640 | 1.36x | 18.3/29.6/32.9% | 2.1/5.6% | 3 |
| 00-08 | 1 | 0.908 | 0.905 | 0.004 | - | - | 0.976 | 0.986 | 0.637 | 1.40x | 18.9/30.5/34.0% | 2.2/5.8% | 3 |

> catch-up-hours=: misdecodes 26

> catch-up-hours=02-06: decode_failures 2

> catch-up-hours=00-08: misdecodes 2

> faster: 2.7 s per simulated hour against 8.76 over 66 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.903 | 0.901 | 0.001 | - | - | 0.977 | 0.978 | 0.625 | 1.35x | 18.0/28.8/32.2% | 2.1/5.4% | 3 |
| 2 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 3 | 1 | 0.913 | 0.899 | 0.014 | - | - | 0.965 | 0.985 | 0.621 | 1.37x | 18.4/29.2/32.5% | 2.1/5.6% | 3 |
| 4 | 1 | 0.910 | 0.895 | 0.016 | - | - | 0.961 | 0.990 | 0.694 | 1.34x | 17.9/28.7/32.0% | 2.1/5.5% | 3 |

> hops-apart=3: decode_failures 28

> hops-apart=4: decode_failures 21

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.903 | 0.901 | 0.001 | - | - | 0.977 | 0.978 | 0.625 | 1.35x | 18.0/28.8/32.2% | 2.1/5.4% | 3 |
| 2 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 3 | 1 | 0.913 | 0.899 | 0.014 | - | - | 0.965 | 0.985 | 0.621 | 1.37x | 18.4/29.2/32.5% | 2.1/5.6% | 3 |
| 4 | 1 | 0.910 | 0.895 | 0.016 | - | - | 0.961 | 0.990 | 0.694 | 1.34x | 17.9/28.7/32.0% | 2.1/5.5% | 3 |
| 5 | 1 | 0.903 | 0.894 | 0.009 | - | - | 0.911 | 0.984 | 0.673 | 1.34x | 17.9/28.7/31.9% | 2.1/5.4% | 3 |

> hops-apart=3: decode_failures 28

> hops-apart=4: decode_failures 21

> hops-apart=5: decode_failures 46

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.909 | 0.904 | 0.005 | - | - | 0.981 | 0.983 | 0.656 | 1.31x | 17.6/28.4/31.6% | 2.0/5.4% | 3 |
| 30 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 120 | 1 | 0.904 | 0.899 | 0.006 | - | - | 0.978 | 0.979 | 0.624 | 1.32x | 17.8/28.7/32.0% | 2.0/5.4% | 3 |
| 600 | 1 | 0.901 | 0.895 | 0.006 | - | - | 0.980 | 0.982 | 0.612 | 1.33x | 17.9/28.8/32.0% | 2.1/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.909 | 0.904 | 0.005 | - | - | 0.981 | 0.983 | 0.656 | 1.31x | 17.6/28.4/31.6% | 2.0/5.4% | 3 |
| 30 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 120 | 1 | 0.904 | 0.899 | 0.006 | - | - | 0.978 | 0.979 | 0.624 | 1.32x | 17.8/28.7/32.0% | 2.0/5.4% | 3 |
| 600 | 1 | 0.901 | 0.895 | 0.006 | - | - | 0.980 | 0.982 | 0.612 | 1.33x | 17.9/28.8/32.0% | 2.1/5.4% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.917 | 0.895 | 0.022 | - | - | 0.974 | 0.981 | 0.657 | 1.38x | 18.6/29.1/32.7% | 2.1/5.6% | 3 |
| routers | 1 | 0.896 | 0.894 | 0.001 | - | - | 0.968 | 0.968 | 0.637 | 1.32x | 17.7/28.6/31.8% | 2.0/5.4% | 3 |
| alternate-routers | 1 | 0.897 | 0.896 | 0.001 | - | - | 0.971 | 0.971 | 0.656 | 1.32x | 17.9/28.8/32.1% | 2.0/5.4% | 3 |
| beside-router | 1 | 0.903 | 0.901 | 0.003 | - | - | 0.980 | 0.980 | 0.631 | 1.32x | 17.6/28.4/31.6% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.910 | 0.903 | 0.008 | - | - | 0.983 | 0.986 | 0.625 | 1.35x | 18.1/29.2/32.4% | 2.1/5.4% | 3 |
| hops-apart | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.917 | 0.895 | 0.022 | - | - | 0.974 | 0.981 | 0.657 | 1.38x | 18.6/29.1/32.7% | 2.1/5.6% | 3 |
| routers | 1 | 0.896 | 0.894 | 0.001 | - | - | 0.968 | 0.968 | 0.637 | 1.32x | 17.7/28.6/31.8% | 2.0/5.4% | 3 |
| alternate-routers | 1 | 0.897 | 0.896 | 0.001 | - | - | 0.971 | 0.971 | 0.656 | 1.32x | 17.9/28.8/32.1% | 2.0/5.4% | 3 |
| beside-router | 1 | 0.903 | 0.901 | 0.003 | - | - | 0.980 | 0.980 | 0.631 | 1.32x | 17.6/28.4/31.6% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.910 | 0.903 | 0.008 | - | - | 0.983 | 0.986 | 0.625 | 1.35x | 18.1/29.2/32.4% | 2.1/5.4% | 3 |
| hops-apart | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

> faster: 1.02 s per simulated hour against 2.77 over 66 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| broadcast | 1 | 0.909 | 0.895 | 0.014 | - | - | 0.975 | 0.977 | 0.644 | 1.35x | 18.2/28.9/32.1% | 2.1/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| heard | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.973 | 0.973 | 0.634 | 1.31x | 17.7/28.4/31.6% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 30

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.909 | 0.895 | 0.014 | - | - | 0.975 | 0.977 | 0.644 | 1.35x | 18.2/28.9/32.1% | 2.1/5.4% | 3 |
| heard | 1 | 0.916 | 0.898 | 0.018 | - | - | 0.986 | 0.986 | 0.654 | 1.38x | 18.5/29.6/32.8% | 2.1/5.5% | 3 |

> replay-ordering=heard: misdecodes 24

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| enum | 1 | 0.912 | 0.907 | 0.005 | - | - | 0.984 | 0.985 | 0.666 | 1.32x | 17.7/28.6/31.8% | 2.0/5.5% | 3 |
| hybrid | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.896 | 0.894 | 0.001 | - | - | 0.968 | 0.968 | 0.637 | 1.32x | 17.7/28.6/31.8% | 2.0/5.4% | 3 |
| 6 | 1 | 0.896 | 0.894 | 0.002 | - | - | 0.976 | 0.976 | 0.612 | 1.38x | 18.4/29.9/33.2% | 2.1/5.7% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.901 | 0.896 | 0.004 | - | - | 0.971 | 0.971 | 0.653 | 1.33x | 17.9/28.6/31.9% | 2.1/5.4% | 2 |
| 3 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 5 | 1 | 0.913 | 0.905 | 0.008 | - | - | 0.988 | 0.988 | 0.635 | 1.34x | 18.1/28.9/32.1% | 2.1/5.6% | 5 |
| 8 | 1 | 0.900 | 0.890 | 0.010 | - | - | 0.976 | 0.978 | 0.643 | 1.40x | 18.9/30.0/33.3% | 2.2/5.6% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.901 | 0.896 | 0.004 | - | - | 0.971 | 0.971 | 0.653 | 1.33x | 17.9/28.6/31.9% | 2.1/5.4% | 2 |
| 3 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 5 | 1 | 0.913 | 0.905 | 0.008 | - | - | 0.988 | 0.988 | 0.635 | 1.34x | 18.1/28.9/32.1% | 2.1/5.6% | 5 |
| 8 | 1 | 0.900 | 0.890 | 0.010 | - | - | 0.976 | 0.978 | 0.643 | 1.40x | 18.9/30.0/33.3% | 2.2/5.6% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| True | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.906 | 0.902 | 0.005 | - | - | 0.981 | 0.983 | 0.625 | 1.27x | 17.1/27.2/30.2% | 2.0/5.1% | 3 |
| 1 | 1 | 0.894 | 0.888 | 0.005 | - | - | 0.967 | 0.967 | 0.624 | 1.26x | 17.0/27.0/30.1% | 1.9/5.1% | 3 |
| 2 | 1 | 0.906 | 0.899 | 0.006 | - | - | 0.982 | 0.983 | 0.629 | 1.27x | 17.0/27.1/30.1% | 2.0/5.1% | 3 |
| 4 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.983 | 0.984 | 0.614 | 1.27x | 17.0/27.0/30.0% | 1.9/5.1% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.909 | 0.904 | 0.006 | - | - | 0.985 | 0.987 | 0.636 | 1.31x | 17.6/28.1/31.2% | 2.1/5.3% | 3 |
| 24 | 1 | 0.911 | 0.906 | 0.005 | - | - | 0.983 | 0.983 | 0.647 | 1.32x | 17.7/28.2/31.4% | 2.1/5.3% | 3 |
| 32 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.983 | 0.983 | 0.638 | 1.31x | 17.6/28.4/31.6% | 2.0/5.3% | 3 |
| 64 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.976 | 0.977 | 0.639 | 1.35x | 18.0/29.1/32.3% | 2.1/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.901 | 0.893 | 0.008 | - | - | 0.979 | 0.979 | 0.641 | 1.41x | 18.9/30.6/34.2% | 2.2/5.8% | 3 |
| 16 | 1 | 0.900 | 0.894 | 0.006 | - | - | 0.977 | 0.977 | 0.613 | 1.33x | 18.0/29.1/32.3% | 2.1/5.4% | 3 |
| 32 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.982 | 0.984 | 0.637 | 1.30x | 17.4/28.2/31.3% | 2.0/5.3% | 3 |

> window-size=8: misdecodes 130

> window-size=16: misdecodes 61

> window-size=32: misdecodes 31

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.959 | 0.957 | 0.002 | - | - | 0.998 | 0.998 | 0.813 | 2.08x | 22.9/39.8/44.9% | 1.4/4.9% | 3 |
| True | 1 | 0.714 | 0.705 | 0.009 | - | - | 0.851 | 0.884 | 0.531 | 5.71x | 57.9/76.0/80.2% | 4.1/12.7% | 3 |

> no-congestion-scaling=True: queue drops 19.1% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 101

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.503 | 0.494 | 0.009 | - | - | 0.782 | 0.784 | 0.155 | 4.70x | 16.8/32.6/41.3% | 1.5/5.3% | 3 |
| truesize | 1 | 0.541 | 0.533 | 0.009 | - | - | 0.820 | 0.821 | 0.168 | 3.43x | 12.1/25.0/32.5% | 1.1/4.3% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.960 | 0.959 | 0.002 | - | - | 0.998 | 0.998 | 0.831 | 2.02x | 21.9/38.4/43.2% | 1.4/4.7% | 3 |
| adaptive | 1 | 0.959 | 0.957 | 0.002 | - | - | 0.998 | 0.998 | 0.813 | 2.08x | 22.9/39.8/44.9% | 1.4/4.9% | 3 |

