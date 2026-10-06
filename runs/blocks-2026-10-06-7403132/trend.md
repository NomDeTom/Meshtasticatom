# Sweep blocks-2026-10-06-7403132

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 7403132 · seeds 7403132
- **blocks** 87 run
- **compute** 9.7 h of simulator time across every cell
- **generated** 2026-10-06T10:21:03+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>70 warnings</summary>

- DB-hotstore-stress: max-num-nodes=10: decode_failures 93
- DB-hotstore-stress: max-num-nodes=120: decode_failures 2
- DB-warm: warm-num-nodes=0: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 77
- DB-warm: warm-num-nodes=25: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 77
- DB-warm: warm-num-nodes=100: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 77
- DB-warm: warm-num-nodes=2000: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 77
- DG-burst: burst-loss=0.2: decode_failures 25
- DG-burst: burst-loss=0.3: decode_failures 42
- DG-outage: burst-loss=0.1: decode_failures 40
- DG-outage: burst-loss=0.2: decode_failures 24
- DG-outage: burst-loss=0.3: decode_failures 30
- LD-chatty-hops: broadcast-interval-s=300: queue drops 11.1% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 24
- LD-chatty: broadcast-interval-s=3600: misdecodes 1
- LD-chatty: broadcast-interval-s=300: decode_failures 14
- LD-interval: broadcast-interval-s=3600: misdecodes 1
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 15.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 77
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 23.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 66
- MS-density: nodes=40: decode_failures 3
- MS-hopscale: nodes=250: decode_failures 4
- MS-hopscale: nodes=500: decode_failures 197
- MS-oversubscribed: nodes=250: decode_failures 2
- MS-oversubscribed: nodes=500: decode_failures 150
- MS-siting: siting-mix=event: decode_failures 1
- MS-siting: faster: 0.923 s per simulated hour against 1.92 over 45 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-stretch: stretch=1.25: decode_failures 40
- MS-stretch: stretch=2.0: decode_failures 1
- MS-topology: topology=corridor: decode_failures 1
- RF-bw500: faster: 0.819 s per simulated hour against 1.82 over 46 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=17: decode_failures 2
- RT-adopt: no-adopt-hop-recommendation=True: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 32
- SF-bucket-mode: bucket-mode=time: misdecodes 50
- SF-bucket-mode: bucket-mode=window: misdecodes 35
- SF-bucket-time: time-bucket-s=600: misdecodes 107
- SF-bucket-time: time-bucket-s=1800: misdecodes 50
- SF-bucket-time: time-bucket-s=3600: misdecodes 12
- SF-cadence: trigger=interval: misdecodes 33
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 31
- SF-capacity-local: capacity=4: decode_failures 88
- SF-capacity-local: capacity=8: decode_failures 17
- SF-capacity: capacity=4: decode_failures 88
- SF-capacity: capacity=8: decode_failures 17
- SF-capacity-window: capacity=8: misdecodes 28
- SF-capacity-window: capacity=8: decode_failures 21
- SF-capacity-window: capacity=16: misdecodes 18
- SF-capacity-window: capacity=32: misdecodes 35
- SF-catchup: catch-up-hours=: misdecodes 31
- SF-catchup: catch-up-hours=02-06: decode_failures 14
- SF-catchup: catch-up-hours=00-08: decode_failures 14
- SF-catchup: faster: 4.32 s per simulated hour against 9.33 over 46 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: faster: 1.66 s per simulated hour against 3.92 over 46 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: faster: 1.5 s per simulated hour against 4.73 over 46 prior run(s) - 3.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-spread: faster: 1.18 s per simulated hour against 2.8 over 46 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 15
- SF-replay-order: replay-ordering=heard: misdecodes 19
- SF-sr-retries: sr-retries=1: misdecodes 1
- SF-window-size: window-size=8: misdecodes 113
- SF-window-size: window-size=16: misdecodes 73
- SF-window-size: window-size=32: misdecodes 35
- TH-congestion-input: congestion-input=hotstore: decode_failures 2
- TH-congestion: no-congestion-scaling=True: queue drops 12.0% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 77

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `MS-oversubscribed` | 36.8 | 19.9 | 1.85x | 46 |
| `MS-stretch` | 3.34 | 2.1 | 1.59x | 46 |
| `PR-dmmode-cr` | 1.85 | 2.79 | 0.66x | 46 |
| `RT-favourites` | 1.1 | 1.65 | 0.66x | 46 |
| `RF-stretch-duct` | 1.22 | 1.87 | 0.66x | 46 |
| `SF-place-flat` | 1.8 | 2.86 | 0.63x | 46 |
| `LD-diurnal` | 0.964 | 1.55 | 0.62x | 46 |
| `RT-hopspread` | 1.25 | 2.04 | 0.61x | 46 |
| `SF-servers-spread` | 1.27 | 2.32 | 0.55x | 46 |
| `AD-worst` | 1.86 | 3.44 | 0.54x | 46 |
| `SF-cadence` | 1.94 | 3.61 | 0.54x | 46 |
| `RF-preset-turbo` | 0.834 | 1.56 | 0.54x | 42 |
| `FW-signing-cost` | 0.847 | 1.6 | 0.53x | 46 |
| `SF-jitter-global` | 0.935 | 1.77 | 0.53x | 46 |
| `RT-hopassign` | 0.928 | 1.85 | 0.50x | 46 |
| `MS-siting` | 0.923 | 1.92 | 0.48x | 45 |
| `SF-catchup` | 4.32 | 9.33 | 0.46x | 46 |
| `RF-bw500` | 0.819 | 1.82 | 0.45x | 46 |
| `SF-hops-flat` | 1.66 | 3.92 | 0.42x | 46 |
| `SF-place-spread` | 1.18 | 2.8 | 0.42x | 46 |
| `SF-hops-spread` | 1.5 | 4.73 | 0.32x | 46 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.996 | 0.996 | 0.921 → 0.926 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.992 | 0.992 | 0.921 → 0.926 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.087 → 0.992 | 0.905 | 0.058 → 0.923 | 27x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.105 → 0.992 | 0.888 | 0.089 → 0.923 | 12x advert_bytes | down | 4 |
| `MS-stretch` | stretch | **held** | 0.120 → 0.992 | 0.873 | 0.145 → 0.923 | 8.8x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.072 → 0.896 | 0.824 | 0.070 → 0.888 | 3.1x advert_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.120 → 0.941 | 0.821 | 0.117 → 0.870 | 1.4e+02x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.164 → 0.981 | 0.817 | 0.160 → 0.981 | 6x sr_airtime | up | 4 |
| `RF-bw500` | preset | **held** | 0.242 → 0.960 | 0.718 | 0.193 → 0.863 | 4.2x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.327 → 0.931 | 0.604 | 0.320 → 0.923 | 20x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.333 → 0.931 | 0.598 | 0.329 → 0.923 | 2.2x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.333 → 0.931 | 0.598 | 0.329 → 0.923 | 3.3x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **text** | 0.331 → 0.829 | 0.497 | 0.324 → 0.821 | 7x sr_bytes | down | 3 |
| `MS-topology` | topology | **held** | 0.622 → 0.992 | 0.370 | 0.578 → 0.932 | 1.8x sr_airtime | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.613 → 0.957 | 0.345 | 0.583 → 0.955 | 7.9x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.610 → 0.931 | 0.321 | 0.582 → 0.923 | 2.7x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.449 → 0.759 | 0.310 | 0.444 → 0.755 | 2.3x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.634 → 0.943 | 0.309 | 0.591 → 0.939 | 6.4x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.638 → 0.931 | 0.293 | 0.595 → 0.923 | 3x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.706 → 0.973 | 0.268 | 0.686 → 0.971 | 4.8x sr_airtime | up | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.635 → 0.864 | 0.229 | 0.345 → 0.571 | 4.5x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.749 → 0.960 | 0.211 | 0.709 → 0.959 | 2.1x sr_bytes | up | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.760 → 0.967 | 0.207 | 0.749 → 0.964 | 4.2x sr_airtime | down | 2 |
| `RT-hopspread` | hop-limit | **text** | 0.749 → 0.944 | 0.195 | 0.709 → 0.940 | 2x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.749 → 0.931 | 0.182 | 0.709 → 0.923 | 2.1x sr_bytes | up | 2 |
| `MS-size` | nodes | **text** | 0.753 → 0.931 | 0.178 | 0.741 → 0.923 | 4.9x sr_bytes | down | 5 |
| `RF-noise` | noise-profile | **text** | 0.779 → 0.931 | 0.152 | 0.770 → 0.923 | 1.6x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.786 → 0.931 | 0.145 | 0.786 → 0.923 | 1.2x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.829 → 0.931 | 0.102 | 0.809 → 0.923 | 1.6x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.859 → 0.948 | 0.089 | 0.842 → 0.942 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.860 → 0.948 | 0.089 | 0.840 → 0.942 | 2.2x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.650 → 0.726 | 0.076 | 0.640 → 0.718 | 1.3x sr_airtime | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.896 → 0.954 | 0.057 | 0.888 → 0.948 | 2.7x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.896 → 0.954 | 0.057 | 0.888 → 0.948 | 2.7x bytes_on_air | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.843 → 0.896 | 0.053 | 0.822 → 0.888 | 1.3x sr_bytes | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.906 → 0.955 | 0.050 | 0.890 → 0.953 | 5.1x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.943 → 0.992 | 0.049 | 0.922 → 0.923 | 24x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.955 → 0.992 | 0.038 | 0.899 → 0.923 | 17x sr_bytes | down | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.931 → 0.968 | 0.037 | 0.923 → 0.967 | 1.8x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.931 → 0.968 | 0.037 | 0.923 → 0.966 | 1.5x bytes_on_air | up | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.896 → 0.931 | 0.035 | 0.884 → 0.923 | 1.4x sr_airtime | down | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.572 → 0.606 | 0.034 | 0.560 → 0.595 | 1.4x sr_airtime | up | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.931 → 0.964 | 0.033 | 0.923 → 0.962 | 1.7x bytes_on_air | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.899 → 0.931 | 0.032 | 0.886 → 0.923 | 1.5x sr_airtime | down | 4 |
| `MS-roles` | role-mix | **text** | 0.896 → 0.927 | 0.031 | 0.888 → 0.921 | 1.3x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.903 → 0.931 | 0.028 | 0.895 → 0.923 | 2.1x bytes_on_air | down | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.906 → 0.931 | 0.025 | 0.898 → 0.923 | 2.1x bytes_on_air | down | 4 |
| `SF-servers-flat` | servers | **held** | 0.975 → 0.998 | 0.023 | 0.919 → 0.923 | 6.2x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.975 → 0.998 | 0.023 | 0.919 → 0.923 | 6.2x sr_bytes | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.931 → 0.954 | 0.023 | 0.923 → 0.950 | 3.4x bytes_on_air | down | 2 |
| `SF-place-flat` | place | **text** | 0.922 → 0.940 | 0.018 | 0.917 → 0.923 | 2.1x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.922 → 0.940 | 0.018 | 0.917 → 0.923 | 2.1x sr_bytes | down | 6 |
| `SF-catchup` | catch-up-hours | **text** | 0.914 → 0.930 | 0.016 | 0.899 → 0.925 | 9.5x advert_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.921 → 0.936 | 0.015 | 0.915 → 0.931 | 1.1x bytes_on_air | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.983 → 0.996 | 0.013 | 0.915 → 0.923 | 1.9x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.983 → 0.996 | 0.013 | 0.915 → 0.923 | 1.9x sr_bytes | up | 5 |
| `FW-versions` | profile | **text** | 0.919 → 0.931 | 0.012 | 0.914 → 0.923 | 3.4x bytes_on_air | up | 5 |
| `FW-firmware` | profile | **text** | 0.919 → 0.931 | 0.012 | 0.914 → 0.923 | 3.4x bytes_on_air | up | 2 |
| `AD-worst` | role-placement | **text** | 0.782 → 0.794 | 0.011 | 0.777 → 0.790 | 1.1x sr_bytes | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.931 → 0.941 | 0.010 | 0.915 → 0.923 | 2.3x sr_airtime | up | 2 |
| `SF-capacity-window` | capacity | **held** | 0.984 → 0.993 | 0.009 | 0.917 → 0.924 | 2.2x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **text** | 0.895 → 0.903 | 0.008 | 0.895 → 0.903 | 1.2x sr_airtime | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.930 → 0.938 | 0.008 | 0.922 → 0.931 | 1.1x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **text** | 0.924 → 0.931 | 0.007 | 0.913 → 0.923 | 5.7x advert_bytes | = | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.926 → 0.933 | 0.007 | 0.917 → 0.923 | 2.6x advert_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **text** | 0.926 → 0.933 | 0.007 | 0.919 → 0.927 | 1.1x sr_airtime | up | 4 |
| `SF-window-size` | window-size | **held** | 0.987 → 0.994 | 0.007 | 0.919 → 0.924 | 4.8x advert_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.987 → 0.993 | 0.006 | 0.916 → 0.924 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.987 → 0.993 | 0.006 | 0.916 → 0.924 | 5.3x advert_bytes | down | 5 |
| `LD-diurnal` | diurnal | **text** | 0.931 → 0.937 | 0.006 | 0.923 → 0.932 | 1.3x sr_bytes | down | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.985 → 0.990 | 0.005 | 0.911 → 0.918 | 5.4x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.992 → 0.996 | 0.004 | 0.919 → 0.923 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.992 → 0.996 | 0.004 | 0.919 → 0.923 | 1.1x sr_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.989 → 0.993 | 0.004 | 0.915 → 0.923 | 1.3x bytes_on_air | down | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.963 → 0.967 | 0.004 | 0.960 → 0.964 | 1.2x sr_airtime | down | 2 |
| `SF-width` | short-id-bits | **held** | 0.989 → 0.993 | 0.004 | 0.920 → 0.923 | 3.1x advert_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.984 → 0.987 | 0.003 | 0.917 → 0.918 | 2.2x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.931 → 0.934 | 0.003 | 0.923 → 0.927 | 1x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.931 → 0.933 | 0.002 | 0.923 → 0.925 | 1.1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.980 → 0.982 | 0.002 | 0.901 → 0.901 | 1.1x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.992 → 0.994 | 0.002 | 0.923 → 0.923 | 2.8x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.967 → 0.968 | 0.001 | 0.964 → 0.965 | 1.1x bytes_on_air | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.997 → 0.998 | 0.001 | 0.964 → 0.965 | 1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.990 → 0.991 | 0.001 | 0.915 → 0.915 | 1.1x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.901 → 0.901 | 0.000 | 0.901 → 0.901 | 1.1x sr_airtime | down | 2 |

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
| none | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| sprinkled | 1 | 0.932 | 0.924 | 0.009 | - | - | 0.998 | 0.998 | 0.485 | 1.11x | 19.5/23.5/25.9% | 1.6/5.1% | 3 |
| arms-race | 1 | 0.968 | 0.966 | 0.002 | - | - | 0.998 | 0.998 | 0.867 | 0.90x | 20.6/24.7/26.7% | 1.0/5.1% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.936 | 0.927 | 0.009 | - | - | 0.987 | 0.988 | 0.847 | 1.17x | 19.7/23.5/27.1% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.997 | 0.997 | 0.888 | 0.98x | 23.5/28.5/32.1% | 1.1/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.982 | 0.983 | 0.700 | 1.07x | 16.2/20.8/24.4% | 1.7/5.2% | 3 |
| inverse | 1 | 0.857 | 0.841 | 0.016 | - | - | 0.982 | 0.985 | 0.712 | 1.18x | 15.6/20.1/23.0% | 2.1/4.1% | 3 |
| random | 1 | 0.843 | 0.822 | 0.021 | - | - | 0.982 | 0.982 | 0.615 | 1.10x | 15.7/19.2/23.4% | 1.8/5.1% | 3 |

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.982 | 0.983 | 0.700 | 1.07x | 16.2/20.8/24.4% | 1.7/5.2% | 3 |
| all-routers | 1 | 0.954 | 0.948 | 0.005 | - | - | 0.998 | 1.000 | 0.884 | 2.85x | 34.9/41.9/44.8% | 4.6/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.982 | 0.983 | 0.700 | 1.07x | 16.2/20.8/24.4% | 1.7/5.2% | 3 |
| no-mute | 1 | 0.906 | 0.896 | 0.010 | - | - | 0.986 | 0.986 | 0.793 | 1.23x | 17.5/21.0/24.7% | 1.9/5.2% | 3 |
| all-routers | 1 | 0.954 | 0.948 | 0.005 | - | - | 0.998 | 1.000 | 0.884 | 2.85x | 34.9/41.9/44.8% | 4.6/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.982 | 0.983 | 0.700 | 1.07x | 16.2/20.8/24.4% | 1.7/5.2% | 3 |
| local-typical | 1 | 0.762 | 0.758 | 0.004 | - | - | 0.895 | 0.895 | 0.235 | 1.27x | 15.1/22.8/28.7% | 2.0/5.1% | 3 |
| basement-heavy | 1 | 0.072 | 0.070 | 0.002 | - | - | 0.325 | 0.332 | 0.000 | 0.52x | 1.3/6.1/9.1% | 0.3/3.1% | 3 |

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.794 | 0.790 | 0.004 | - | - | 0.926 | 0.926 | 0.000 | 2.36x | 20.1/31.3/40.0% | 1.8/5.7% | 3 |
| inverse | 1 | 0.782 | 0.777 | 0.005 | - | - | 0.932 | 0.932 | 0.000 | 2.34x | 17.3/25.6/34.6% | 1.9/3.6% | 3 |

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.926 | 0.926 | 0.000 | - | - | 0 | 0.000 | 0.747 | 1.31x | 18.0/23.3/27.7% | 1.9/5.1% | 3 |
| sr | 1 | 0.930 | 0.921 | 0.009 | - | - | 0.996 | 0.997 | 0.741 | 1.35x | 18.6/23.9/28.3% | 2.0/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.860 | 0.840 | 0.020 | - | - | 0.948 | 0.952 | 0.754 | 3.15x | 42.6/54.9/64.0% | 4.4/10.2% | 3 |
| 100 | 1 | 0.948 | 0.942 | 0.006 | - | - | 0.990 | 0.990 | 0.857 | 1.54x | 21.3/28.6/34.5% | 2.2/5.3% | 3 |
| 120 | 1 | 0.948 | 0.942 | 0.006 | - | - | 0.990 | 0.990 | 0.857 | 1.54x | 21.3/28.6/34.5% | 2.2/5.3% | 3 |
| 250 | 1 | 0.948 | 0.942 | 0.006 | - | - | 0.990 | 0.990 | 0.857 | 1.54x | 21.3/28.6/34.5% | 2.2/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.356 | 0.345 | 0.012 | - | - | 0.635 | 0.661 | 0.115 | 11.43x | 43.3/59.7/69.1% | 3.9/11.1% | 3 |
| 120 | 1 | 0.572 | 0.560 | 0.012 | - | - | 0.861 | 0.861 | 0.183 | 4.63x | 17.9/29.3/36.5% | 1.5/5.5% | 3 |
| 250 | 1 | 0.582 | 0.571 | 0.012 | - | - | 0.864 | 0.865 | 0.194 | 4.49x | 17.2/28.5/35.3% | 1.5/5.5% | 3 |

> max-num-nodes=10: decode_failures 93

> max-num-nodes=120: decode_failures 2

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.948 | 0.942 | 0.006 | - | - | 0.990 | 0.990 | 0.857 | 1.54x | 21.3/28.6/34.5% | 2.2/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.948 | 0.942 | 0.006 | - | - | 0.990 | 0.990 | 0.857 | 1.54x | 21.3/28.6/34.5% | 2.2/5.3% | 3 |
| constrained | 1 | 0.859 | 0.842 | 0.016 | - | - | 0.944 | 0.946 | 0.763 | 3.15x | 42.6/54.8/63.9% | 4.4/10.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.726 | 0.718 | 0.009 | - | - | 0.786 | 0.843 | 0.545 | 5.69x | 60.7/73.0/78.4% | 3.9/13.7% | 3 |
| 25 | 1 | 0.726 | 0.718 | 0.009 | - | - | 0.786 | 0.843 | 0.545 | 5.69x | 60.7/73.0/78.4% | 3.9/13.7% | 3 |
| 100 | 1 | 0.726 | 0.718 | 0.009 | - | - | 0.786 | 0.843 | 0.545 | 5.69x | 60.7/73.0/78.4% | 3.9/13.7% | 3 |
| 2000 | 1 | 0.726 | 0.718 | 0.009 | - | - | 0.786 | 0.843 | 0.545 | 5.69x | 60.7/73.0/78.4% | 3.9/13.7% | 3 |

> warm-num-nodes=0: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 77

> warm-num-nodes=25: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 77

> warm-num-nodes=100: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 77

> warm-num-nodes=2000: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 77

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.833 | 0.814 | 0.019 | - | - | 0.970 | 0.971 | 0.670 | 1.27x | 17.7/23.0/27.4% | 1.9/4.9% | 3 |
| 0.2 | 1 | 0.745 | 0.716 | 0.029 | - | - | 0.935 | 0.962 | 0.602 | 1.19x | 16.7/22.1/26.4% | 1.8/4.5% | 3 |
| 0.3 | 1 | 0.638 | 0.595 | 0.043 | - | - | 0.829 | 0.888 | 0.479 | 1.10x | 15.7/20.5/24.6% | 1.7/4.1% | 3 |

> burst-loss=0.2: decode_failures 25

> burst-loss=0.3: decode_failures 42

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.907 | 0.899 | 0.008 | - | - | 0.980 | 0.984 | 0.769 | 1.39x | 19.2/24.9/29.3% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.880 | 0.867 | 0.013 | - | - | 0.975 | 0.978 | 0.727 | 1.45x | 20.0/25.7/30.3% | 2.2/5.1% | 3 |
| 0.3 | 1 | 0.829 | 0.809 | 0.020 | - | - | 0.951 | 0.958 | 0.672 | 1.48x | 20.6/26.4/31.1% | 2.2/5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.830 | 0.813 | 0.017 | - | - | 0.956 | 0.985 | 0.680 | 1.26x | 17.5/23.2/27.4% | 1.9/5.2% | 3 |
| 0.2 | 1 | 0.704 | 0.683 | 0.021 | - | - | 0.839 | 0.928 | 0.546 | 1.16x | 16.4/21.6/25.7% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.610 | 0.582 | 0.028 | - | - | 0.755 | 0.882 | 0.473 | 1.13x | 16.1/20.9/25.0% | 1.8/4.0% | 3 |

> burst-loss=0.1: decode_failures 40

> burst-loss=0.2: decode_failures 24

> burst-loss=0.3: decode_failures 30

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.895 | 0.895 | 0.000 | - | - | 0.982 | 0.986 | 0.712 | 1.79x | 24.2/32.3/38.0% | 2.7/7.0% | 3 |
| directed-with-late-flood | 1 | 0.901 | 0.901 | 0.000 | - | - | 0.980 | 0.984 | 0.723 | 1.60x | 21.9/29.0/34.2% | 2.5/6.4% | 3 |
| m4-early-flood | 1 | 0.903 | 0.903 | 0.000 | - | - | 0.987 | 0.993 | 0.726 | 1.59x | 21.7/28.8/34.1% | 2.4/6.3% | 3 |

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.919 | 0.914 | 0.005 | - | - | 0.995 | 0.995 | 0.753 | 0.71x | 9.2/11.6/13.7% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.916 | 0.910 | 0.006 | - | - | 0.987 | 0.989 | 0.754 | 1.14x | 15.3/20.4/22.1% | 1.7/4.6% | 3 |
| 0.5 | 1 | 0.906 | 0.898 | 0.008 | - | - | 0.990 | 0.991 | 0.593 | 0.97x | 13.4/16.5/19.0% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.919 | 0.913 | 0.006 | - | - | 0.995 | 0.997 | 0.714 | 0.90x | 11.7/16.6/18.9% | 1.4/3.8% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.919 | 0.911 | 0.007 | - | - | 0.992 | 0.992 | 0.791 | 1.13x | 15.5/20.3/21.9% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.903 | 0.895 | 0.008 | - | - | 0.992 | 0.992 | 0.524 | 0.96x | 13.5/16.8/19.5% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.914 | 0.908 | 0.006 | - | - | 0.989 | 0.990 | 0.735 | 0.87x | 11.5/16.3/18.7% | 1.3/3.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.954 | 0.950 | 0.004 | - | - | 0.998 | 0.999 | 0.836 | 0.70x | 9.9/13.4/16.1% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.922 | 0.917 | 0.005 | - | - | 0.994 | 0.994 | 0.761 | 0.72x | 9.9/12.8/15.2% | 1.1/2.7% | 3 |
| 2.5 | 1 | 0.919 | 0.914 | 0.005 | - | - | 0.990 | 0.990 | 0.781 | 0.73x | 9.8/12.5/14.9% | 1.1/2.6% | 3 |
| 2.6 | 1 | 0.924 | 0.919 | 0.005 | - | - | 0.994 | 0.995 | 0.755 | 0.70x | 9.8/12.7/15.5% | 1.0/2.7% | 3 |
| 2.7 | 1 | 0.924 | 0.920 | 0.005 | - | - | 0.992 | 0.992 | 0.751 | 0.71x | 9.7/13.1/16.4% | 1.0/3.0% | 3 |
| 2.8 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.993 | 0.993 | 0.806 | 0.88x | 11.9/15.8/18.6% | 1.3/3.5% | 3 |
| 900 | 1 | 0.906 | 0.890 | 0.016 | - | - | 0.985 | 0.985 | 0.751 | 2.11x | 28.6/37.5/44.0% | 3.1/8.3% | 3 |
| 300 | 1 | 0.634 | 0.591 | 0.043 | - | - | 0.785 | 0.807 | 0.461 | 4.64x | 58.4/70.7/78.0% | 6.9/16.9% | 3 |

> broadcast-interval-s=3600: misdecodes 1

> broadcast-interval-s=300: decode_failures 14

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.957 | 0.955 | 0.002 | - | - | 0.993 | 0.993 | 0.828 | 0.95x | 13.2/16.3/19.1% | 1.4/3.5% | 3 |
| 900 | 1 | 0.915 | 0.908 | 0.007 | - | - | 0.979 | 0.979 | 0.793 | 2.38x | 32.3/40.6/47.3% | 3.6/8.8% | 3 |
| 300 | 1 | 0.613 | 0.583 | 0.030 | - | - | 0.792 | 0.810 | 0.489 | 5.10x | 62.3/72.9/79.2% | 7.9/17.3% | 3 |

> broadcast-interval-s=300: queue drops 11.1% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 24

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.935 | 0.929 | 0.007 | - | - | 0.995 | 0.995 | 0.778 | 1.23x | 16.7/22.4/26.5% | 1.8/5.0% | 3 |
| sinusoid | 1 | 0.937 | 0.932 | 0.005 | - | - | 0.993 | 0.993 | 0.773 | 1.17x | 16.1/21.4/25.2% | 1.7/4.7% | 3 |
| commuter | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.906 | 0.890 | 0.016 | - | - | 0.985 | 0.985 | 0.751 | 2.11x | 28.6/37.5/44.0% | 3.1/8.3% | 3 |
| 3600 | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.993 | 0.993 | 0.806 | 0.88x | 11.9/15.8/18.6% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.953 | 0.948 | 0.005 | - | - | 0.998 | 1.000 | 0.825 | 0.63x | 8.6/11.3/13.1% | 0.9/2.5% | 3 |
| 43200 | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.997 | 0.998 | 0.809 | 0.46x | 6.3/8.2/9.6% | 0.7/1.8% | 3 |

> broadcast-interval-s=3600: misdecodes 1

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.927 | 0.919 | 0.009 | - | - | 0.993 | 0.994 | 0.769 | 1.40x | 19.1/25.4/29.8% | 2.1/5.5% | 3 |
| 1.0 | 1 | 0.913 | 0.904 | 0.009 | - | - | 0.975 | 0.977 | 0.749 | 1.57x | 21.5/28.3/33.6% | 2.4/6.3% | 3 |
| 4.0 | 1 | 0.899 | 0.886 | 0.014 | - | - | 0.979 | 0.982 | 0.730 | 1.92x | 26.8/34.8/41.5% | 2.9/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.726 | 0.718 | 0.009 | - | - | 0.786 | 0.843 | 0.545 | 5.69x | 60.7/73.0/78.4% | 3.9/13.7% | 3 |
| 1.0 | 1 | 0.650 | 0.640 | 0.010 | - | - | 0.720 | 0.778 | 0.453 | 6.17x | 64.1/74.9/80.0% | 4.3/14.9% | 3 |

> traceroute-per-hour=0.0: queue drops 15.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 77

> traceroute-per-hour=1.0: queue drops 23.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 66

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.706 | 0.686 | 0.019 | - | - | 0.886 | 0.913 | 0.519 | 1.39x | 19.8/26.9/30.3% | 3.2/6.3% | 3 |
| 60 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 90 | 1 | 0.941 | 0.940 | 0.002 | - | - | 0.997 | 0.998 | 0.736 | 1.49x | 19.3/24.2/27.7% | 1.3/4.8% | 3 |
| 120 | 1 | 0.967 | 0.964 | 0.003 | - | - | 0.997 | 0.997 | 0.862 | 2.02x | 23.1/34.7/40.5% | 1.3/5.2% | 3 |
| 150 | 1 | 0.973 | 0.971 | 0.002 | - | - | 0.999 | 0.999 | 0.817 | 2.70x | 30.8/48.1/55.1% | 1.3/5.7% | 3 |

> nodes=40: decode_failures 3

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 120 | 1 | 0.830 | 0.824 | 0.006 | - | - | 0.985 | 0.986 | 0.370 | 2.13x | 16.3/24.8/29.3% | 1.4/5.7% | 3 |
| 250 | 1 | 0.564 | 0.551 | 0.013 | - | - | 0.862 | 0.863 | 0.172 | 4.87x | 18.6/31.3/38.9% | 1.6/5.9% | 3 |
| 500 | 1 | 0.327 | 0.320 | 0.007 | - | - | 0.557 | 0.574 | 0.098 | 10.35x | 18.8/32.9/56.4% | 1.8/7.3% | 3 |

> nodes=250: decode_failures 4

> nodes=500: decode_failures 197

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.829 | 0.821 | 0.007 | - | - | 0.984 | 0.985 | 0.392 | 2.04x | 15.5/23.6/27.7% | 1.4/5.3% | 3 |
| 250 | 1 | 0.572 | 0.560 | 0.012 | - | - | 0.861 | 0.861 | 0.183 | 4.63x | 17.9/29.3/36.5% | 1.5/5.5% | 3 |
| 500 | 1 | 0.331 | 0.324 | 0.007 | - | - | 0.575 | 0.585 | 0.092 | 9.47x | 17.2/30.2/52.1% | 1.6/6.4% | 3 |

> nodes=250: decode_failures 2

> nodes=500: decode_failures 150

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.927 | 0.921 | 0.006 | - | - | 0.988 | 0.988 | 0.761 | 1.35x | 18.4/24.5/28.8% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.982 | 0.983 | 0.700 | 1.07x | 16.2/20.8/24.4% | 1.7/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.936 | 0.931 | 0.005 | - | - | 0.989 | 0.990 | 0.793 | 1.42x | 19.6/25.3/29.4% | 2.0/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.921 | 0.915 | 0.006 | - | - | 0.978 | 0.979 | 0.799 | 1.27x | 19.1/24.5/28.3% | 2.1/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.05 | 1 | 0.930 | 0.922 | 0.008 | - | - | 0.993 | 0.994 | 0.779 | 1.41x | 20.5/26.0/31.9% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.928 | 0.915 | 0.013 | - | - | 0.989 | 0.990 | 0.830 | 1.53x | 22.4/29.5/36.4% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.928 | 0.919 | 0.009 | - | - | 0.992 | 0.992 | 0.843 | 1.69x | 23.6/34.5/40.9% | 2.3/5.0% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| local-typical | 1 | 0.805 | 0.802 | 0.003 | - | - | 0.928 | 0.928 | 0.300 | 1.46x | 16.4/26.0/31.3% | 2.1/5.3% | 3 |
| event | 1 | 0.164 | 0.160 | 0.005 | - | - | 0.300 | 0.412 | 0.000 | 0.94x | 5.2/8.0/15.1% | 1.7/3.4% | 3 |
| backbone | 1 | 0.981 | 0.981 | 0.001 | - | - | 1.000 | 1.000 | 0.930 | 0.98x | 25.8/33.0/35.3% | 1.2/5.5% | 3 |

> siting-mix=event: decode_failures 1

> faster: 0.923 s per simulated hour against 1.92 over 45 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.880 | 0.870 | 0.010 | - | - | 0.968 | 0.969 | 0.766 | 1.45x | 25.7/32.7/35.8% | 3.2/7.7% | 3 |
| 60 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 90 | 1 | 0.845 | 0.841 | 0.004 | - | - | 0.963 | 0.965 | 0.473 | 1.69x | 15.8/26.5/31.5% | 1.6/5.2% | 3 |
| 120 | 1 | 0.830 | 0.824 | 0.006 | - | - | 0.985 | 0.986 | 0.370 | 2.13x | 16.3/24.8/29.3% | 1.4/5.7% | 3 |
| 150 | 1 | 0.753 | 0.741 | 0.013 | - | - | 0.871 | 0.871 | 0.131 | 2.76x | 16.9/24.9/29.8% | 1.5/5.7% | 3 |

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 1.25 | 1 | 0.743 | 0.732 | 0.011 | - | - | 0.871 | 0.913 | 0.520 | 1.36x | 13.1/20.2/23.7% | 2.1/5.1% | 3 |
| 1.5 | 1 | 0.449 | 0.444 | 0.005 | - | - | 0.605 | 0.605 | 0.000 | 1.39x | 10.2/13.9/19.3% | 2.3/4.6% | 3 |
| 2.0 | 1 | 0.146 | 0.145 | 0.002 | - | - | 0.120 | 0.121 | 0.000 | 0.99x | 5.1/8.4/11.9% | 1.5/3.1% | 3 |

> stretch=1.25: decode_failures 40

> stretch=2.0: decode_failures 1

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| clustered | 1 | 0.931 | 0.922 | 0.009 | - | - | 0.991 | 0.992 | 0.528 | 1.23x | 21.6/33.9/35.9% | 1.7/5.5% | 3 |
| corridor | 1 | 0.592 | 0.578 | 0.014 | - | - | 0.622 | 0.622 | 0.206 | 1.35x | 15.5/25.2/29.0% | 2.0/4.7% | 3 |
| hub | 1 | 0.937 | 0.932 | 0.004 | - | - | 0.968 | 0.969 | 0.698 | 1.10x | 28.6/35.8/36.7% | 1.5/5.7% | 3 |

> topology=corridor: decode_failures 1

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.901 | 0.901 | 0.000 | - | - | 0.980 | 0.984 | 0.723 | 1.60x | 21.9/29.0/34.2% | 2.5/6.4% | 3 |
| True | 1 | 0.901 | 0.901 | 0.000 | - | - | 0.982 | 0.988 | 0.726 | 1.61x | 22.0/29.2/34.6% | 2.4/6.4% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.901 | 0.901 | 0.000 | - | - | 0.982 | 0.988 | 0.726 | 1.61x | 22.0/29.2/34.6% | 2.4/6.4% | 3 |
| m4-early-flood | 1 | 0.901 | 0.901 | 0.000 | - | - | 0.982 | 0.986 | 0.720 | 1.60x | 21.8/29.0/34.2% | 2.4/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.926 | 0.926 | 0.000 | - | - | 0 | 0.000 | 0.747 | 1.31x | 18.0/23.3/27.7% | 1.9/5.1% | 3 |
| chain | 1 | 0.923 | 0.921 | 0.002 | - | - | 0.955 | 0.990 | 0.760 | 1.50x | 20.5/27.5/32.2% | 2.2/6.0% | 3 |
| sr | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| True | 1 | 0.934 | 0.927 | 0.006 | - | - | 0.994 | 0.995 | 0.791 | 1.34x | 18.3/24.0/28.2% | 2.0/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.967 | 0.964 | 0.003 | - | - | 0.997 | 0.997 | 0.862 | 2.02x | 23.1/34.7/40.5% | 1.3/5.2% | 3 |
| True | 1 | 0.967 | 0.965 | 0.002 | - | - | 0.998 | 0.998 | 0.865 | 2.05x | 23.5/34.8/40.6% | 1.3/5.2% | 3 |

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.198 | 0.193 | 0.005 | - | - | 0.242 | 0.248 | 0.000 | 0.05x | 0.3/0.5/0.6% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.496 | 0.493 | 0.003 | - | - | 0.661 | 0.663 | 0.275 | 0.29x | 2.0/3.7/5.1% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.871 | 0.863 | 0.008 | - | - | 0.960 | 0.960 | 0.726 | 1.29x | 13.9/20.3/24.2% | 2.0/4.9% | 3 |

> faster: 0.819 s per simulated hour against 1.82 over 46 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.936 | 0.927 | 0.008 | - | - | 0.993 | 0.994 | 0.798 | 1.26x | 19.1/24.6/28.8% | 1.8/5.2% | 3 |
| 1.0 | 1 | 0.964 | 0.962 | 0.003 | - | - | 0.997 | 0.998 | 0.897 | 0.77x | 23.0/27.3/29.5% | 0.9/4.9% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.333 | 0.329 | 0.004 | - | - | 0.486 | 0.488 | 0.098 | 0.14x | 0.9/1.4/1.9% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| LITE_FAST | 1 | 0.893 | 0.890 | 0.003 | - | - | 0.965 | 0.968 | 0.733 | 1.03x | 12.5/17.7/20.2% | 1.5/4.1% | 3 |
| NARROW_SLOW | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.973 | 0.974 | 0.751 | 1.33x | 16.1/23.5/26.8% | 2.0/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| temporal | 1 | 0.868 | 0.851 | 0.017 | - | - | 0.968 | 0.972 | 0.667 | 1.36x | 18.1/23.9/28.2% | 2.0/5.2% | 3 |
| transient | 1 | 0.924 | 0.915 | 0.009 | - | - | 0.984 | 0.987 | 0.777 | 1.30x | 17.7/23.5/27.7% | 1.9/5.1% | 3 |
| periodic | 1 | 0.779 | 0.770 | 0.009 | - | - | 0.842 | 0.847 | 0.672 | 1.25x | 17.2/22.5/26.6% | 1.9/4.7% | 3 |

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.333 | 0.329 | 0.004 | - | - | 0.486 | 0.488 | 0.098 | 0.14x | 0.9/1.4/1.9% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| LONG_MODERATE | 1 | 0.872 | 0.851 | 0.021 | - | - | 0.953 | 0.959 | 0.789 | 3.26x | 50.2/58.2/64.0% | 4.5/12.7% | 3 |

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.058 | 0.058 | 0.000 | - | - | 0.087 | 0.087 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.198 | 0.193 | 0.005 | - | - | 0.242 | 0.248 | 0.000 | 0.05x | 0.3/0.5/0.6% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| LONG_TURBO | 1 | 0.871 | 0.863 | 0.008 | - | - | 0.960 | 0.960 | 0.726 | 1.29x | 13.9/20.3/24.2% | 2.0/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.964 | 0.965 | 0.814 | 1.82x | 23.8/30.4/35.0% | 2.7/7.0% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.878 | 0.870 | 0.008 | - | - | 0.941 | 0.946 | 0.732 | 1.27x | 17.5/23.1/27.2% | 2.0/4.9% | 3 |
| 10000 | 1 | 0.779 | 0.770 | 0.009 | - | - | 0.842 | 0.847 | 0.672 | 1.25x | 17.2/22.5/26.6% | 1.9/4.7% | 3 |
| 4000 | 1 | 0.503 | 0.494 | 0.009 | - | - | 0.554 | 0.599 | 0.399 | 1.09x | 15.3/19.5/23.3% | 1.6/3.6% | 3 |
| 2000 | 1 | 0.117 | 0.117 | 0.000 | - | - | 0.120 | 0.197 | 0.055 | 0.73x | 10.6/13.6/16.4% | 1.2/2.0% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.449 | 0.444 | 0.005 | - | - | 0.605 | 0.605 | 0.000 | 1.39x | 10.2/13.9/19.3% | 2.3/4.6% | 3 |
| 1.0 | 1 | 0.759 | 0.755 | 0.004 | - | - | 0.839 | 0.844 | 0.558 | 0.84x | 15.4/18.8/21.1% | 1.1/4.4% | 3 |

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 22 | 1 | 0.479 | 0.474 | 0.004 | - | - | 0.625 | 0.625 | 0.182 | 1.40x | 10.1/17.9/22.9% | 2.2/4.5% | 3 |
| 17 | 1 | 0.199 | 0.193 | 0.006 | - | - | 0.240 | 0.244 | 0.000 | 1.16x | 5.9/10.1/12.5% | 1.8/3.6% | 3 |
| 14 | 1 | 0.090 | 0.089 | 0.001 | - | - | 0.105 | 0.108 | 0.000 | 0.74x | 3.3/6.8/8.8% | 1.2/2.4% | 3 |

> tx-power=17: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.967 | 0.964 | 0.003 | - | - | 0.997 | 0.997 | 0.862 | 2.02x | 23.1/34.7/40.5% | 1.3/5.2% | 3 |
| True | 1 | 0.963 | 0.960 | 0.003 | - | - | 0.995 | 0.996 | 0.853 | 2.37x | 26.8/39.2/45.2% | 1.5/5.9% | 3 |

> no-adopt-hop-recommendation=True: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.930 | 0.922 | 0.007 | - | - | 0.995 | 0.996 | 0.764 | 1.36x | 19.6/25.0/29.6% | 2.0/5.2% | 3 |
| True | 1 | 0.938 | 0.931 | 0.006 | - | - | 0.989 | 0.989 | 0.793 | 1.42x | 20.6/25.6/30.4% | 2.0/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| random | 1 | 0.896 | 0.884 | 0.012 | - | - | 0.984 | 0.985 | 0.746 | 1.30x | 17.8/23.7/27.8% | 1.9/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.749 | 0.709 | 0.040 | - | - | 0.961 | 0.964 | 0.473 | 0.98x | 14.0/19.8/23.6% | 1.4/4.6% | 3 |
| 7 | 1 | 0.944 | 0.940 | 0.004 | - | - | 0.990 | 0.990 | 0.793 | 1.46x | 19.9/25.4/29.8% | 2.2/5.5% | 3 |
| 15 | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.991 | 0.991 | 0.826 | 1.44x | 19.8/25.1/29.4% | 2.1/5.4% | 3 |
| 32 | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.991 | 0.991 | 0.826 | 1.44x | 19.8/25.1/29.4% | 2.1/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.749 | 0.709 | 0.040 | - | - | 0.961 | 0.964 | 0.473 | 0.98x | 14.0/19.8/23.6% | 1.4/4.6% | 3 |
| 5 | 1 | 0.907 | 0.898 | 0.009 | - | - | 0.992 | 0.992 | 0.737 | 1.33x | 18.3/24.0/28.1% | 2.0/5.2% | 3 |
| 7 | 1 | 0.944 | 0.940 | 0.004 | - | - | 0.990 | 0.990 | 0.793 | 1.46x | 19.9/25.4/29.8% | 2.2/5.5% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.922 | 0.922 | 0.000 | - | - | 0.943 | 0.993 | 0.746 | 1.30x | 17.9/23.3/27.6% | 1.9/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.749 | 0.709 | 0.040 | - | - | 0.961 | 0.964 | 0.473 | 0.98x | 14.0/19.8/23.6% | 1.4/4.6% | 3 |
| True | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| BALANCED | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| STRICT | 1 | 0.786 | 0.786 | 0.000 | - | - | 0.847 | 0.848 | 0.617 | 1.40x | 19.3/25.0/29.6% | 2.0/5.4% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| dm | 1 | 0.931 | 0.923 | 0.009 | - | - | 0.994 | 0.995 | 0.780 | 1.29x | 17.8/23.5/27.7% | 1.9/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.933 | 0.922 | 0.011 | - | - | 0.993 | 0.995 | 0.792 | 1.34x | 18.3/24.1/28.2% | 2.0/5.3% | 3 |
| local | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| time | 1 | 0.926 | 0.917 | 0.009 | - | - | 0.990 | 0.993 | 0.799 | 1.37x | 18.8/24.8/29.1% | 2.1/5.5% | 3 |
| window | 1 | 0.927 | 0.919 | 0.009 | - | - | 0.987 | 0.989 | 0.783 | 1.33x | 18.1/23.7/28.0% | 2.0/5.2% | 3 |

> bucket-mode=global: misdecodes 32

> bucket-mode=time: misdecodes 50

> bucket-mode=window: misdecodes 35

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.923 | 0.911 | 0.012 | - | - | 0.985 | 0.988 | 0.758 | 1.47x | 20.0/26.4/31.1% | 2.2/5.9% | 3 |
| 1800 | 1 | 0.926 | 0.917 | 0.009 | - | - | 0.990 | 0.993 | 0.799 | 1.37x | 18.8/24.8/29.1% | 2.1/5.5% | 3 |
| 3600 | 1 | 0.926 | 0.918 | 0.009 | - | - | 0.985 | 0.990 | 0.764 | 1.34x | 18.3/23.9/28.2% | 2.0/5.2% | 3 |

> time-bucket-s=600: misdecodes 107

> time-bucket-s=1800: misdecodes 50

> time-bucket-s=3600: misdecodes 12

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| interval | 1 | 0.920 | 0.907 | 0.013 | - | - | 0.987 | 0.993 | 0.754 | 1.78x | 25.1/34.3/39.8% | 2.5/8.2% | 3 |
| aimd | 1 | 0.921 | 0.919 | 0.002 | - | - | 0.955 | 0.997 | 0.760 | 1.31x | 17.9/23.8/28.0% | 1.9/5.2% | 3 |
| bucket+interval | 1 | 0.914 | 0.899 | 0.015 | - | - | 0.982 | 0.986 | 0.736 | 1.80x | 25.5/34.4/39.9% | 2.6/7.9% | 3 |

> trigger=interval: misdecodes 33

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 31

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.930 | 0.921 | 0.009 | - | - | 0.993 | 0.997 | 0.748 | 1.31x | 18.0/23.7/27.9% | 1.9/5.3% | 3 |
| 8 | 1 | 0.931 | 0.924 | 0.007 | - | - | 0.990 | 0.993 | 0.777 | 1.34x | 18.3/24.0/28.3% | 2.0/5.2% | 3 |
| 16 | 1 | 0.925 | 0.916 | 0.009 | - | - | 0.987 | 0.987 | 0.758 | 1.31x | 17.9/23.7/27.9% | 2.0/5.2% | 3 |
| 32 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 50 | 1 | 0.928 | 0.919 | 0.008 | - | - | 0.989 | 0.990 | 0.752 | 1.34x | 18.3/24.1/28.5% | 2.0/5.2% | 3 |

> capacity=4: decode_failures 88

> capacity=8: decode_failures 17

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.930 | 0.921 | 0.009 | - | - | 0.993 | 0.997 | 0.748 | 1.31x | 18.0/23.7/27.9% | 1.9/5.3% | 3 |
| 8 | 1 | 0.931 | 0.924 | 0.007 | - | - | 0.990 | 0.993 | 0.777 | 1.34x | 18.3/24.0/28.3% | 2.0/5.2% | 3 |
| 16 | 1 | 0.925 | 0.916 | 0.009 | - | - | 0.987 | 0.987 | 0.758 | 1.31x | 17.9/23.7/27.9% | 2.0/5.2% | 3 |
| 32 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 50 | 1 | 0.928 | 0.919 | 0.008 | - | - | 0.989 | 0.990 | 0.752 | 1.34x | 18.3/24.1/28.5% | 2.0/5.2% | 3 |

> capacity=4: decode_failures 88

> capacity=8: decode_failures 17

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.924 | 0.917 | 0.007 | - | - | 0.984 | 0.991 | 0.772 | 1.31x | 18.0/23.5/27.7% | 1.9/5.1% | 3 |
| 16 | 1 | 0.931 | 0.924 | 0.007 | - | - | 0.993 | 0.994 | 0.764 | 1.32x | 18.0/23.7/28.0% | 1.9/5.2% | 3 |
| 32 | 1 | 0.927 | 0.919 | 0.009 | - | - | 0.987 | 0.989 | 0.783 | 1.33x | 18.1/23.7/28.0% | 2.0/5.2% | 3 |

> capacity=8: misdecodes 28

> capacity=8: decode_failures 21

> capacity=16: misdecodes 18

> capacity=32: misdecodes 35

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.914 | 0.899 | 0.015 | - | - | 0.982 | 0.986 | 0.736 | 1.80x | 25.5/34.4/39.9% | 2.6/7.9% | 3 |
| 02-06 | 1 | 0.928 | 0.923 | 0.005 | - | - | 0.974 | 0.993 | 0.773 | 1.35x | 18.5/24.7/29.0% | 2.0/5.4% | 3 |
| 00-08 | 1 | 0.930 | 0.925 | 0.005 | - | - | 0.977 | 0.993 | 0.777 | 1.40x | 19.1/25.5/30.1% | 2.1/5.8% | 3 |

> catch-up-hours=: misdecodes 31

> catch-up-hours=02-06: decode_failures 14

> catch-up-hours=00-08: decode_failures 14

> faster: 4.32 s per simulated hour against 9.33 over 46 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.983 | 0.984 | 0.760 | 1.33x | 18.3/23.9/28.3% | 1.9/5.2% | 3 |
| 2 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 3 | 1 | 0.930 | 0.921 | 0.009 | - | - | 0.996 | 0.997 | 0.741 | 1.35x | 18.6/23.9/28.3% | 2.0/5.3% | 3 |
| 4 | 1 | 0.926 | 0.915 | 0.011 | - | - | 0.995 | 0.997 | 0.730 | 1.35x | 18.8/23.9/28.4% | 2.0/5.3% | 3 |

> faster: 1.66 s per simulated hour against 3.92 over 46 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.983 | 0.984 | 0.760 | 1.33x | 18.3/23.9/28.3% | 1.9/5.2% | 3 |
| 2 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 3 | 1 | 0.930 | 0.921 | 0.009 | - | - | 0.996 | 0.997 | 0.741 | 1.35x | 18.6/23.9/28.3% | 2.0/5.3% | 3 |
| 4 | 1 | 0.926 | 0.915 | 0.011 | - | - | 0.995 | 0.997 | 0.730 | 1.35x | 18.8/23.9/28.4% | 2.0/5.3% | 3 |
| 5 | 1 | 0.926 | 0.915 | 0.011 | - | - | 0.995 | 0.997 | 0.730 | 1.35x | 18.8/23.9/28.4% | 2.0/5.3% | 3 |

> faster: 1.5 s per simulated hour against 4.73 over 46 prior run(s) - 3.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.929 | 0.919 | 0.010 | - | - | 0.992 | 0.993 | 0.767 | 1.32x | 18.1/23.8/28.1% | 2.0/5.2% | 3 |
| 30 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 120 | 1 | 0.930 | 0.922 | 0.007 | - | - | 0.992 | 0.992 | 0.759 | 1.34x | 18.2/24.0/28.3% | 2.0/5.3% | 3 |
| 600 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.996 | 0.997 | 0.777 | 1.33x | 18.2/24.0/28.3% | 2.0/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.929 | 0.919 | 0.010 | - | - | 0.992 | 0.993 | 0.767 | 1.32x | 18.1/23.8/28.1% | 2.0/5.2% | 3 |
| 30 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 120 | 1 | 0.930 | 0.922 | 0.007 | - | - | 0.992 | 0.992 | 0.759 | 1.34x | 18.2/24.0/28.3% | 2.0/5.3% | 3 |
| 600 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.996 | 0.997 | 0.777 | 1.33x | 18.2/24.0/28.3% | 2.0/5.2% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.940 | 0.918 | 0.022 | - | - | 0.995 | 0.997 | 0.758 | 1.35x | 18.5/24.0/28.7% | 2.0/5.3% | 3 |
| routers | 1 | 0.924 | 0.917 | 0.007 | - | - | 0.987 | 0.987 | 0.741 | 1.33x | 18.4/24.1/28.6% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.989 | 0.989 | 0.731 | 1.34x | 18.5/24.1/28.5% | 2.0/5.3% | 3 |
| beside-router | 1 | 0.922 | 0.917 | 0.006 | - | - | 0.988 | 0.989 | 0.749 | 1.33x | 18.3/23.8/28.2% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.928 | 0.920 | 0.008 | - | - | 0.992 | 0.993 | 0.752 | 1.34x | 18.5/23.9/28.4% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.940 | 0.918 | 0.022 | - | - | 0.995 | 0.997 | 0.758 | 1.35x | 18.5/24.0/28.7% | 2.0/5.3% | 3 |
| routers | 1 | 0.924 | 0.917 | 0.007 | - | - | 0.987 | 0.987 | 0.741 | 1.33x | 18.4/24.1/28.6% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.989 | 0.989 | 0.731 | 1.34x | 18.5/24.1/28.5% | 2.0/5.3% | 3 |
| beside-router | 1 | 0.922 | 0.917 | 0.006 | - | - | 0.988 | 0.989 | 0.749 | 1.33x | 18.3/23.8/28.2% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.928 | 0.920 | 0.008 | - | - | 0.992 | 0.993 | 0.752 | 1.34x | 18.5/23.9/28.4% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

> faster: 1.18 s per simulated hour against 2.8 over 46 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| broadcast | 1 | 0.941 | 0.915 | 0.026 | - | - | 0.991 | 0.991 | 0.803 | 1.38x | 18.9/24.9/29.1% | 2.1/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| heard | 1 | 0.933 | 0.925 | 0.008 | - | - | 0.995 | 0.996 | 0.780 | 1.33x | 18.2/24.0/28.2% | 2.0/5.2% | 3 |

> replay-ordering=heard: misdecodes 19

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.941 | 0.915 | 0.026 | - | - | 0.991 | 0.991 | 0.803 | 1.38x | 18.9/24.9/29.1% | 2.1/5.4% | 3 |
| heard | 1 | 0.941 | 0.915 | 0.026 | - | - | 0.990 | 0.992 | 0.810 | 1.41x | 19.2/25.3/29.6% | 2.1/5.5% | 3 |

> replay-ordering=heard: misdecodes 15

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| enum | 1 | 0.924 | 0.913 | 0.010 | - | - | 0.989 | 0.989 | 0.761 | 1.32x | 18.0/24.0/28.2% | 2.0/5.3% | 3 |
| hybrid | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.924 | 0.917 | 0.007 | - | - | 0.987 | 0.987 | 0.741 | 1.33x | 18.4/24.1/28.6% | 1.9/5.3% | 3 |
| 6 | 1 | 0.926 | 0.918 | 0.007 | - | - | 0.984 | 0.985 | 0.755 | 1.39x | 19.0/25.1/29.6% | 2.0/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.923 | 0.919 | 0.005 | - | - | 0.975 | 0.977 | 0.784 | 1.32x | 18.1/23.8/28.1% | 2.0/5.2% | 2 |
| 3 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 5 | 1 | 0.932 | 0.919 | 0.013 | - | - | 0.989 | 0.991 | 0.822 | 1.36x | 18.5/24.8/28.9% | 2.0/5.4% | 5 |
| 8 | 1 | 0.935 | 0.920 | 0.015 | - | - | 0.998 | 0.998 | 0.801 | 1.40x | 19.0/25.4/29.6% | 2.2/5.5% | 8 |

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.923 | 0.919 | 0.005 | - | - | 0.975 | 0.977 | 0.784 | 1.32x | 18.1/23.8/28.1% | 2.0/5.2% | 2 |
| 3 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 5 | 1 | 0.932 | 0.919 | 0.013 | - | - | 0.989 | 0.991 | 0.822 | 1.36x | 18.5/24.8/28.9% | 2.0/5.4% | 5 |
| 8 | 1 | 0.935 | 0.920 | 0.015 | - | - | 0.998 | 0.998 | 0.801 | 1.40x | 19.0/25.4/29.6% | 2.2/5.5% | 8 |

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| True | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.933 | 0.926 | 0.006 | - | - | 0.992 | 0.994 | 0.781 | 1.23x | 16.8/22.1/26.1% | 1.8/4.8% | 3 |
| 1 | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.985 | 0.987 | 0.751 | 1.24x | 16.9/22.4/26.3% | 1.8/4.9% | 3 |
| 2 | 1 | 0.930 | 0.922 | 0.007 | - | - | 0.990 | 0.991 | 0.790 | 1.26x | 17.2/22.7/26.7% | 1.8/4.9% | 3 |
| 4 | 1 | 0.933 | 0.927 | 0.006 | - | - | 0.991 | 0.993 | 0.797 | 1.21x | 16.5/21.9/25.9% | 1.8/4.8% | 3 |

> sr-retries=1: misdecodes 1

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.928 | 0.920 | 0.009 | - | - | 0.993 | 0.994 | 0.781 | 1.32x | 18.1/23.9/28.2% | 2.0/5.2% | 3 |
| 24 | 1 | 0.928 | 0.920 | 0.008 | - | - | 0.990 | 0.991 | 0.757 | 1.33x | 18.3/23.9/28.2% | 2.0/5.2% | 3 |
| 32 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.992 | 0.993 | 0.785 | 1.33x | 18.1/24.0/28.3% | 2.0/5.3% | 3 |
| 64 | 1 | 0.928 | 0.920 | 0.007 | - | - | 0.989 | 0.990 | 0.773 | 1.33x | 18.2/24.0/28.2% | 2.0/5.2% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.928 | 0.921 | 0.008 | - | - | 0.990 | 0.991 | 0.784 | 1.42x | 19.2/25.5/29.9% | 2.1/5.6% | 3 |
| 16 | 1 | 0.932 | 0.924 | 0.008 | - | - | 0.994 | 0.995 | 0.786 | 1.35x | 18.4/24.5/28.6% | 2.0/5.3% | 3 |
| 32 | 1 | 0.927 | 0.919 | 0.009 | - | - | 0.987 | 0.989 | 0.783 | 1.33x | 18.1/23.7/28.0% | 2.0/5.2% | 3 |

> window-size=8: misdecodes 113

> window-size=16: misdecodes 73

> window-size=32: misdecodes 35

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.967 | 0.964 | 0.003 | - | - | 0.997 | 0.997 | 0.862 | 2.02x | 23.1/34.7/40.5% | 1.3/5.2% | 3 |
| True | 1 | 0.760 | 0.749 | 0.011 | - | - | 0.824 | 0.869 | 0.574 | 5.48x | 58.9/72.0/77.9% | 3.8/13.2% | 3 |

> no-congestion-scaling=True: queue drops 12.0% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 77

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.572 | 0.560 | 0.012 | - | - | 0.861 | 0.861 | 0.183 | 4.63x | 17.9/29.3/36.5% | 1.5/5.5% | 3 |
| truesize | 1 | 0.606 | 0.595 | 0.012 | - | - | 0.877 | 0.878 | 0.194 | 3.59x | 13.7/24.3/30.3% | 1.1/4.6% | 3 |

> congestion-input=hotstore: decode_failures 2

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.968 | 0.965 | 0.003 | - | - | 0.997 | 0.997 | 0.863 | 1.88x | 21.2/32.4/37.7% | 1.2/4.9% | 3 |
| adaptive | 1 | 0.967 | 0.964 | 0.003 | - | - | 0.997 | 0.997 | 0.862 | 2.02x | 23.1/34.7/40.5% | 1.3/5.2% | 3 |

