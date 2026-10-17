# Sweep blocks-2026-10-17-6753573

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 6753573 · seeds 6753573
- **blocks** 87 run
- **compute** 9.4 h of simulator time across every cell
- **generated** 2026-10-17T08:48:24+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>71 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 16
- AD-worst: role-placement=degree: misdecodes 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 54
- DB-warm: warm-num-nodes=0: queue drops 14.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 124
- DB-warm: warm-num-nodes=25: queue drops 14.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 124
- DB-warm: warm-num-nodes=100: queue drops 14.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 124
- DB-warm: warm-num-nodes=2000: queue drops 14.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 124
- DG-burst: burst-loss=0.2: decode_failures 7
- DG-burst: burst-loss=0.3: decode_failures 28
- DG-outage: burst-loss=0.1: decode_failures 20
- DG-outage: burst-loss=0.2: decode_failures 35
- DG-outage: burst-loss=0.3: decode_failures 29
- FW-mixed: legacy-fraction=0.5: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 16
- LD-chatty: broadcast-interval-s=300: decode_failures 8
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 14.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 124
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 24.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 113
- MS-density: nodes=40: decode_failures 2
- MS-hopscale: nodes=500: decode_failures 22
- MS-oversubscribed: nodes=500: decode_failures 8
- MS-size: nodes=150: decode_failures 16
- MS-stretch: stretch=2.0: decode_failures 8
- RF-bw500: preset=SHORT_TURBO: decode_failures 15
- RF-preset: faster: 1.03 s per simulated hour against 2.85 over 57 prior run(s) - 2.8x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 4
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 15
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 4
- RF-txpower: tx-power=22: decode_failures 18
- RF-txpower: tx-power=17: decode_failures 13
- RF-txpower: tx-power=14: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 59
- SF-bucket-mode: bucket-mode=time: misdecodes 42
- SF-bucket-mode: bucket-mode=window: misdecodes 16
- SF-bucket-time: time-bucket-s=600: misdecodes 135
- SF-bucket-time: time-bucket-s=1800: misdecodes 42
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-cadence: trigger=interval: misdecodes 13
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 7
- SF-capacity-local: capacity=4: decode_failures 90
- SF-capacity-local: capacity=8: decode_failures 16
- SF-capacity: capacity=4: decode_failures 90
- SF-capacity: capacity=8: decode_failures 16
- SF-capacity-window: capacity=8: misdecodes 20
- SF-capacity-window: capacity=8: decode_failures 17
- SF-capacity-window: capacity=16: misdecodes 24
- SF-capacity-window: capacity=32: misdecodes 16
- SF-catchup: catch-up-hours=: misdecodes 7
- SF-catchup: catch-up-hours=02-06: decode_failures 3
- SF-catchup: catch-up-hours=00-08: decode_failures 5
- SF-catchup: faster: 4.23 s per simulated hour against 8.67 over 57 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: faster: 1.33 s per simulated hour against 3.96 over 57 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: hops-apart=5: decode_failures 20
- SF-place-flat: place=spread: decode_failures 20
- SF-place-flat: place=random-clients: decode_failures 38
- SF-place-spread: place=spread: decode_failures 20
- SF-place-spread: place=random-clients: decode_failures 38
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 11
- SF-replay-order: replay-ordering=heard: misdecodes 24
- SF-window-size: window-size=8: misdecodes 155
- SF-window-size: window-size=16: misdecodes 61
- SF-window-size: window-size=32: misdecodes 16
- TH-congestion: no-congestion-scaling=True: queue drops 13.5% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 8
- TH-congestion: faster: 5.69 s per simulated hour against 17.1 over 57 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-bw500` | 3.44 | 1.94 | 1.77x | 57 |
| `RF-txpower` | 2.75 | 1.57 | 1.76x | 57 |
| `SF-place-spread` | 4.19 | 2.75 | 1.52x | 57 |
| `FW-mixed` | 1.09 | 1.66 | 0.66x | 57 |
| `MS-hopscale` | 11.6 | 17.9 | 0.65x | 57 |
| `LD-chatty` | 2.9 | 4.67 | 0.62x | 57 |
| `SF-jitter-global` | 1.07 | 1.74 | 0.62x | 57 |
| `RF-duct` | 1.08 | 1.75 | 0.61x | 57 |
| `MS-oversubscribed` | 12.2 | 20.1 | 0.61x | 57 |
| `RT-adopt` | 2.41 | 3.98 | 0.60x | 57 |
| `SF-servers-spread` | 1.28 | 2.21 | 0.58x | 57 |
| `PR-protocol` | 0.799 | 1.38 | 0.58x | 57 |
| `SF-servers-flat` | 1.29 | 2.28 | 0.57x | 57 |
| `SF-hops-spread` | 2.62 | 4.65 | 0.56x | 57 |
| `SF-resolve` | 0.817 | 1.53 | 0.54x | 57 |
| `SF-capacity-window` | 0.848 | 1.59 | 0.53x | 57 |
| `RT-hopspread` | 1.08 | 2.03 | 0.53x | 57 |
| `BL-control` | 0.917 | 1.81 | 0.51x | 57 |
| `SF-catchup` | 4.23 | 8.67 | 0.49x | 57 |
| `RF-preset` | 1.03 | 2.85 | 0.36x | 57 |
| `SF-hops-flat` | 1.33 | 3.96 | 0.34x | 57 |
| `TH-congestion` | 5.69 | 17.1 | 0.33x | 57 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.956 | 0.956 | 0.857 → 0.858 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.953 | 0.953 | 0.851 → 0.858 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.099 → 0.953 | 0.853 | 0.120 → 0.851 | 17x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.150 → 0.953 | 0.803 | 0.084 → 0.851 | 11x sr_bytes | up | 5 |
| `AD-siting` | siting-mix | **held** | 0.143 → 0.932 | 0.789 | 0.052 → 0.813 | 7.6x sr_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.146 → 0.894 | 0.748 | 0.111 → 0.793 | 83x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.188 → 0.855 | 0.668 | 0.182 → 0.851 | 3.2x advert_bytes | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.395 → 0.976 | 0.582 | 0.389 → 0.976 | 2.3x sr_airtime | up | 4 |
| `RF-bw500` | preset | **text** | 0.252 → 0.797 | 0.545 | 0.243 → 0.793 | 2.2x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.327 → 0.855 | 0.528 | 0.323 → 0.851 | 11x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.362 → 0.855 | 0.493 | 0.359 → 0.851 | 1.9x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.362 → 0.855 | 0.493 | 0.359 → 0.851 | 2.3x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.478 → 0.968 | 0.490 | 0.324 → 0.785 | 4.1x bytes_on_air | down | 3 |
| `MS-density` | nodes | **text** | 0.571 → 0.965 | 0.393 | 0.566 → 0.963 | 5.8x advert_bytes | up | 5 |
| `DG-outage` | burst-loss | **text** | 0.547 → 0.855 | 0.308 | 0.520 → 0.851 | 2.8x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.623 → 0.920 | 0.297 | 0.613 → 0.918 | 8.9x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.588 → 0.883 | 0.295 | 0.574 → 0.881 | 8x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.562 → 0.855 | 0.293 | 0.531 → 0.851 | 2.3x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.577 → 0.856 | 0.279 | 0.324 → 0.536 | 5.1x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.450 → 0.664 | 0.213 | 0.435 → 0.652 | 1.4x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.736 → 0.948 | 0.212 | 0.728 → 0.948 | 2.4x sr_bytes | up | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.733 → 0.914 | 0.181 | 0.712 → 0.913 | 1.7x sr_bytes | up | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.783 → 0.961 | 0.178 | 0.775 → 0.960 | 4.5x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **held** | 0.782 → 0.956 | 0.174 | 0.685 → 0.851 | 1.4x sr_airtime | down | 4 |
| `MS-size` | nodes | **text** | 0.683 → 0.855 | 0.172 | 0.666 → 0.851 | 8.8x sr_bytes | down | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.733 → 0.902 | 0.169 | 0.712 → 0.899 | 1.6x sr_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.816 → 0.955 | 0.139 | 0.848 → 0.856 | 3.5x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.816 → 0.955 | 0.139 | 0.848 → 0.856 | 3.5x sr_bytes | up | 6 |
| `RT-spread` | hop-spread | **text** | 0.733 → 0.855 | 0.123 | 0.712 → 0.851 | 1.7x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.745 → 0.855 | 0.110 | 0.735 → 0.851 | 1.4x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.786 → 0.889 | 0.103 | 0.780 → 0.887 | 2.3x sr_airtime | down | 3 |
| `SC-signing` | signature-policy | **text** | 0.756 → 0.855 | 0.099 | 0.756 → 0.851 | 1.4x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.790 → 0.889 | 0.099 | 0.784 → 0.887 | 2.3x sr_airtime | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.855 → 0.945 | 0.090 | 0.851 → 0.941 | 1.3x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.855 → 0.939 | 0.084 | 0.851 → 0.938 | 2.1x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.817 → 0.899 | 0.082 | 0.813 → 0.897 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.817 → 0.899 | 0.082 | 0.813 → 0.897 | 2.3x bytes_on_air | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.699 → 0.769 | 0.070 | 0.691 → 0.762 | 1.5x sr_airtime | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.825 → 0.895 | 0.070 | 0.819 → 0.893 | 5.2x sr_airtime | up | 4 |
| `MS-roles` | role-mix | **text** | 0.817 → 0.870 | 0.053 | 0.813 → 0.866 | 1.1x bytes_on_air | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.855 → 0.908 | 0.053 | 0.851 → 0.906 | 1.3x bytes_on_air | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.855 → 0.905 | 0.049 | 0.851 → 0.898 | 2.2x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.855 → 0.904 | 0.049 | 0.851 → 0.898 | 2.2x bytes_on_air | up | 4 |
| `MS-roles-fav` | role-mix | **text** | 0.835 → 0.880 | 0.045 | 0.832 → 0.877 | 1.1x sr_bytes | down | 2 |
| `FW-versions` | profile | **text** | 0.855 → 0.895 | 0.040 | 0.851 → 0.894 | 3.2x bytes_on_air | down | 5 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.817 → 0.855 | 0.039 | 0.810 → 0.852 | 1.5x sr_airtime | down | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.915 → 0.953 | 0.037 | 0.851 → 0.862 | 25x sr_airtime | down | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.535 → 0.567 | 0.031 | 0.526 → 0.559 | 1.3x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.855 → 0.886 | 0.031 | 0.851 → 0.885 | 3.4x bytes_on_air | down | 2 |
| `FW-firmware` | profile | **held** | 0.953 → 0.983 | 0.030 | 0.851 → 0.882 | 3.2x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.924 → 0.953 | 0.029 | 0.832 → 0.855 | 14x advert_bytes | down | 4 |
| `AD-worst` | role-placement | **text** | 0.788 → 0.816 | 0.029 | 0.775 → 0.808 | 1.3x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **held** | 0.927 → 0.955 | 0.028 | 0.811 → 0.813 | 1.3x sr_bytes | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.812 → 0.837 | 0.025 | 0.812 → 0.837 | 1.3x sr_airtime | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.866 → 0.889 | 0.023 | 0.863 → 0.887 | 1.1x bytes_on_air | up | 2 |
| `SF-servers-flat` | servers | **held** | 0.953 → 0.975 | 0.022 | 0.847 → 0.859 | 6.2x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.953 → 0.975 | 0.022 | 0.847 → 0.859 | 6.2x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.935 → 0.956 | 0.021 | 0.851 → 0.858 | 2.2x sr_bytes | down | 5 |
| `LD-diurnal` | diurnal | **text** | 0.855 → 0.872 | 0.017 | 0.851 → 0.870 | 1.1x sr_bytes | down | 3 |
| `SF-catchup` | catch-up-hours | **text** | 0.844 → 0.861 | 0.016 | 0.839 → 0.858 | 9.4x advert_bytes | up | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.841 → 0.855 | 0.015 | 0.832 → 0.851 | 1.2x sr_airtime | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.855 → 0.869 | 0.014 | 0.851 → 0.852 | 2.5x sr_airtime | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.855 → 0.869 | 0.014 | 0.851 → 0.866 | 1.3x bytes_on_air | up | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.950 → 0.963 | 0.013 | 0.851 → 0.858 | 3.4x advert_bytes | down | 4 |
| `SF-resolve` | resolve | **held** | 0.953 → 0.965 | 0.013 | 0.851 → 0.862 | 5.7x advert_bytes | = | 3 |
| `SF-hops-flat` | hops-apart | **text** | 0.855 → 0.867 | 0.012 | 0.851 → 0.858 | 1.7x sr_bytes | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.944 → 0.955 | 0.011 | 0.846 → 0.854 | 3x advert_bytes | down | 4 |
| `SF-window-size` | window-size | **held** | 0.949 → 0.960 | 0.011 | 0.850 → 0.856 | 6x advert_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.854 → 0.865 | 0.011 | 0.851 → 0.861 | 1x sr_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.855 → 0.866 | 0.011 | 0.851 → 0.862 | 3.1x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.939 → 0.948 | 0.008 | 0.832 → 0.837 | 1.2x sr_airtime | up | 2 |
| `SF-capacity` | capacity | **text** | 0.854 → 0.862 | 0.008 | 0.850 → 0.859 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.854 → 0.862 | 0.008 | 0.850 → 0.859 | 5.3x advert_bytes | down | 5 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.950 → 0.958 | 0.008 | 0.853 → 0.857 | 5.4x advert_bytes | up | 3 |
| `SF-replay-order` | replay-ordering | **text** | 0.855 → 0.863 | 0.008 | 0.851 → 0.858 | 1.2x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.953 → 0.961 | 0.007 | 0.952 → 0.960 | 1.2x sr_airtime | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.956 → 0.961 | 0.005 | 0.856 → 0.860 | 2.1x advert_bytes | down | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.948 → 0.954 | 0.005 | 0.847 → 0.852 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.948 → 0.954 | 0.005 | 0.847 → 0.852 | 1.1x sr_airtime | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.950 → 0.955 | 0.005 | 0.847 → 0.852 | 2.4x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.855 → 0.860 | 0.004 | 0.851 → 0.858 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.867 → 0.869 | 0.002 | 0.849 → 0.852 | 1.2x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.948 → 0.949 | 0.002 | 0.832 → 0.832 | 1.2x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.960 → 0.961 | 0.001 | 0.959 → 0.960 | 1.1x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.961 → 0.962 | 0.001 | 0.960 → 0.961 | 1x bytes_on_air | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario valleys`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| sprinkled | 1 | 0.905 | 0.904 | 0.001 | - | - | 0.958 | 0.959 | 0.445 | 1.10x | 18.7/25.5/28.5% | 1.5/5.4% | 3 |
| arms-race | 1 | 0.939 | 0.938 | 0.001 | - | - | 0.969 | 0.969 | 0.636 | 1.04x | 23.5/28.5/30.7% | 1.2/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.891 | 0.887 | 0.005 | - | - | 0.987 | 0.989 | 0.498 | 1.38x | 19.4/29.2/31.8% | 2.0/5.3% | 3 |
| 0.3 | 1 | 0.945 | 0.941 | 0.004 | - | - | 0.992 | 0.994 | 0.877 | 1.10x | 18.9/28.0/30.2% | 1.5/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.932 | 0.933 | 0.178 | 1.23x | 16.9/26.6/29.8% | 2.0/5.2% | 3 |
| inverse | 1 | 0.822 | 0.811 | 0.010 | - | - | 0.955 | 0.955 | 0.419 | 1.17x | 14.2/19.6/22.9% | 2.0/3.3% | 3 |
| random | 1 | 0.820 | 0.812 | 0.007 | - | - | 0.927 | 0.928 | 0.411 | 1.17x | 14.4/21.6/24.8% | 1.9/4.9% | 3 |

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.932 | 0.933 | 0.178 | 1.23x | 16.9/26.6/29.8% | 2.0/5.2% | 3 |
| all-routers | 1 | 0.899 | 0.897 | 0.002 | - | - | 0.958 | 0.959 | 0.697 | 2.78x | 33.8/41.9/45.0% | 4.7/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.932 | 0.933 | 0.178 | 1.23x | 16.9/26.6/29.8% | 2.0/5.2% | 3 |
| no-mute | 1 | 0.856 | 0.850 | 0.005 | - | - | 0.958 | 0.959 | 0.465 | 1.36x | 17.2/23.8/29.4% | 2.1/5.3% | 3 |
| all-routers | 1 | 0.899 | 0.897 | 0.002 | - | - | 0.958 | 0.959 | 0.697 | 2.78x | 33.8/41.9/45.0% | 4.7/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.932 | 0.933 | 0.178 | 1.23x | 16.9/26.6/29.8% | 2.0/5.2% | 3 |
| local-typical | 1 | 0.725 | 0.714 | 0.011 | - | - | 0.849 | 0.879 | 0.000 | 1.29x | 12.6/25.4/31.0% | 2.1/5.4% | 3 |
| basement-heavy | 1 | 0.052 | 0.052 | 0.000 | - | - | 0.143 | 0.143 | 0.000 | 0.47x | 1.3/5.0/7.8% | 0.4/2.0% | 3 |

> siting-mix=local-typical: decode_failures 16

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.816 | 0.808 | 0.008 | - | - | 0.961 | 0.962 | 0.000 | 2.33x | 17.2/28.5/37.6% | 1.8/5.8% | 3 |
| inverse | 1 | 0.788 | 0.775 | 0.013 | - | - | 0.955 | 0.955 | 0.000 | 2.22x | 15.1/23.9/33.4% | 1.7/3.0% | 3 |

> role-placement=degree: misdecodes 1

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.858 | 0.858 | 0.000 | - | - | 0 | 0.000 | 0.492 | 1.32x | 17.2/25.9/28.4% | 1.9/4.9% | 3 |
| sr | 1 | 0.865 | 0.857 | 0.008 | - | - | 0.956 | 0.960 | 0.520 | 1.38x | 17.8/26.8/29.5% | 2.0/5.2% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.790 | 0.784 | 0.006 | - | - | 0.903 | 0.905 | 0.415 | 3.09x | 41.8/58.2/64.9% | 4.3/9.7% | 3 |
| 100 | 1 | 0.889 | 0.887 | 0.002 | - | - | 0.956 | 0.956 | 0.546 | 1.56x | 21.5/31.2/35.7% | 2.2/5.1% | 3 |
| 120 | 1 | 0.889 | 0.887 | 0.002 | - | - | 0.956 | 0.956 | 0.546 | 1.56x | 21.5/31.2/35.7% | 2.2/5.1% | 3 |
| 250 | 1 | 0.889 | 0.887 | 0.002 | - | - | 0.956 | 0.956 | 0.546 | 1.56x | 21.5/31.2/35.7% | 2.2/5.1% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.331 | 0.324 | 0.007 | - | - | 0.577 | 0.587 | 0.139 | 11.44x | 39.3/60.3/74.2% | 4.0/10.8% | 3 |
| 120 | 1 | 0.535 | 0.526 | 0.009 | - | - | 0.843 | 0.845 | 0.223 | 4.52x | 15.5/29.6/41.9% | 1.5/5.6% | 3 |
| 250 | 1 | 0.545 | 0.536 | 0.009 | - | - | 0.856 | 0.858 | 0.222 | 4.39x | 14.9/28.0/40.0% | 1.5/5.4% | 3 |

> max-num-nodes=10: decode_failures 54

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.889 | 0.887 | 0.002 | - | - | 0.956 | 0.956 | 0.546 | 1.56x | 21.5/31.2/35.7% | 2.2/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.889 | 0.887 | 0.002 | - | - | 0.956 | 0.956 | 0.546 | 1.56x | 21.5/31.2/35.7% | 2.2/5.1% | 3 |
| constrained | 1 | 0.786 | 0.780 | 0.006 | - | - | 0.905 | 0.905 | 0.436 | 3.08x | 41.8/58.0/64.8% | 4.3/9.7% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.899 | 0.920 | 0.473 | 5.41x | 56.9/73.5/79.1% | 3.9/12.7% | 3 |
| 25 | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.899 | 0.920 | 0.473 | 5.41x | 56.9/73.5/79.1% | 3.9/12.7% | 3 |
| 100 | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.899 | 0.920 | 0.473 | 5.41x | 56.9/73.5/79.1% | 3.9/12.7% | 3 |
| 2000 | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.899 | 0.920 | 0.473 | 5.41x | 56.9/73.5/79.1% | 3.9/12.7% | 3 |

> warm-num-nodes=0: queue drops 14.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 124

> warm-num-nodes=25: queue drops 14.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 124

> warm-num-nodes=100: queue drops 14.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 124

> warm-num-nodes=2000: queue drops 14.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 124

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.757 | 0.743 | 0.015 | - | - | 0.934 | 0.936 | 0.419 | 1.29x | 17.0/25.7/28.3% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.665 | 0.638 | 0.027 | - | - | 0.903 | 0.904 | 0.316 | 1.20x | 16.0/24.3/26.9% | 1.7/4.3% | 3 |
| 0.3 | 1 | 0.562 | 0.531 | 0.031 | - | - | 0.802 | 0.864 | 0.253 | 1.11x | 14.9/23.3/25.6% | 1.6/4.1% | 3 |

> burst-loss=0.2: decode_failures 7

> burst-loss=0.3: decode_failures 28

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.830 | 0.824 | 0.006 | - | - | 0.949 | 0.949 | 0.460 | 1.43x | 18.4/27.7/30.5% | 1.9/5.1% | 3 |
| 0.2 | 1 | 0.791 | 0.783 | 0.008 | - | - | 0.937 | 0.939 | 0.421 | 1.47x | 19.2/28.8/31.7% | 2.1/5.1% | 3 |
| 0.3 | 1 | 0.745 | 0.735 | 0.010 | - | - | 0.920 | 0.929 | 0.329 | 1.49x | 19.6/29.6/32.5% | 2.2/4.9% | 3 |

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.754 | 0.742 | 0.013 | - | - | 0.913 | 0.942 | 0.360 | 1.29x | 17.2/25.9/28.8% | 1.8/5.1% | 3 |
| 0.2 | 1 | 0.667 | 0.651 | 0.016 | - | - | 0.870 | 0.922 | 0.313 | 1.23x | 16.2/25.0/27.6% | 1.7/4.7% | 3 |
| 0.3 | 1 | 0.547 | 0.520 | 0.026 | - | - | 0.746 | 0.847 | 0.200 | 1.14x | 15.6/24.0/26.5% | 1.6/4.3% | 3 |

> burst-loss=0.1: decode_failures 20

> burst-loss=0.2: decode_failures 35

> burst-loss=0.3: decode_failures 29

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.812 | 0.812 | 0.000 | - | - | 0.930 | 0.932 | 0.452 | 1.82x | 23.7/35.3/39.0% | 2.5/6.9% | 3 |
| directed-with-late-flood | 1 | 0.837 | 0.837 | 0.000 | - | - | 0.939 | 0.941 | 0.491 | 1.65x | 21.5/32.4/35.9% | 2.3/6.3% | 3 |
| m4-early-flood | 1 | 0.835 | 0.835 | 0.000 | - | - | 0.944 | 0.944 | 0.482 | 1.64x | 21.4/32.3/35.8% | 2.2/6.2% | 3 |

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.883 | 0.882 | 0.002 | - | - | 0.983 | 0.983 | 0.469 | 0.77x | 9.2/12.4/15.5% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.877 | 0.874 | 0.003 | - | - | 0.969 | 0.969 | 0.084 | 1.29x | 15.7/24.8/28.4% | 2.1/5.0% | 3 |
| 0.5 | 1 | 0.890 | 0.887 | 0.003 | - | - | 0.975 | 0.975 | 0.588 | 1.07x | 14.0/21.5/25.5% | 1.6/4.3% | 3 |
| 0.75 | 1 | 0.904 | 0.898 | 0.006 | - | - | 0.984 | 0.987 | 0.587 | 0.90x | 12.0/15.9/18.3% | 1.4/3.6% | 3 |

> legacy-fraction=0.5: misdecodes 1

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.873 | 0.870 | 0.003 | - | - | 0.965 | 0.965 | 0.095 | 1.25x | 15.5/24.3/27.8% | 1.9/4.9% | 3 |
| 0.5 | 1 | 0.880 | 0.877 | 0.003 | - | - | 0.966 | 0.966 | 0.497 | 1.04x | 14.2/21.5/25.4% | 1.5/4.3% | 3 |
| 0.75 | 1 | 0.905 | 0.898 | 0.007 | - | - | 0.989 | 0.989 | 0.542 | 0.87x | 12.0/16.0/18.4% | 1.3/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.886 | 0.885 | 0.002 | - | - | 0.966 | 0.967 | 0.556 | 0.73x | 9.8/15.3/17.1% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.866 | 0.864 | 0.002 | - | - | 0.978 | 0.978 | 0.428 | 0.77x | 9.6/13.9/17.4% | 1.2/2.1% | 3 |
| 2.5 | 1 | 0.869 | 0.868 | 0.002 | - | - | 0.980 | 0.980 | 0.408 | 0.78x | 9.8/13.9/17.1% | 1.3/2.1% | 3 |
| 2.6 | 1 | 0.869 | 0.867 | 0.002 | - | - | 0.976 | 0.976 | 0.416 | 0.76x | 9.5/13.9/17.8% | 1.2/2.1% | 3 |
| 2.7 | 1 | 0.895 | 0.894 | 0.001 | - | - | 0.976 | 0.977 | 0.500 | 0.80x | 10.3/17.9/20.7% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.883 | 0.881 | 0.002 | - | - | 0.968 | 0.970 | 0.525 | 0.93x | 12.0/18.0/19.8% | 1.3/3.5% | 3 |
| 900 | 1 | 0.825 | 0.819 | 0.007 | - | - | 0.944 | 0.946 | 0.444 | 2.22x | 28.8/42.8/47.0% | 3.1/8.3% | 3 |
| 300 | 1 | 0.588 | 0.574 | 0.015 | - | - | 0.796 | 0.820 | 0.268 | 4.61x | 55.6/74.3/78.9% | 6.9/15.7% | 3 |

> broadcast-interval-s=300: decode_failures 8

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.920 | 0.918 | 0.001 | - | - | 0.971 | 0.971 | 0.613 | 1.03x | 12.8/18.9/20.5% | 1.6/3.6% | 3 |
| 900 | 1 | 0.875 | 0.870 | 0.005 | - | - | 0.945 | 0.948 | 0.553 | 2.48x | 30.6/44.7/48.9% | 3.9/8.5% | 3 |
| 300 | 1 | 0.623 | 0.613 | 0.010 | - | - | 0.765 | 0.777 | 0.349 | 5.11x | 58.6/75.9/79.9% | 8.0/16.4% | 3 |

> broadcast-interval-s=300: decode_failures 16

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.872 | 0.870 | 0.002 | - | - | 0.960 | 0.961 | 0.511 | 1.26x | 16.6/25.0/27.4% | 1.8/4.8% | 3 |
| sinusoid | 1 | 0.867 | 0.862 | 0.006 | - | - | 0.965 | 0.965 | 0.505 | 1.25x | 16.2/24.5/26.9% | 1.7/4.7% | 3 |
| commuter | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.825 | 0.819 | 0.007 | - | - | 0.944 | 0.946 | 0.444 | 2.22x | 28.8/42.8/47.0% | 3.1/8.3% | 3 |
| 3600 | 1 | 0.883 | 0.881 | 0.002 | - | - | 0.968 | 0.970 | 0.525 | 0.93x | 12.0/18.0/19.8% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.890 | 0.889 | 0.002 | - | - | 0.963 | 0.964 | 0.565 | 0.63x | 8.1/12.0/13.2% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.895 | 0.893 | 0.002 | - | - | 0.969 | 0.969 | 0.552 | 0.45x | 5.8/8.6/9.4% | 0.6/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.855 | 0.852 | 0.003 | - | - | 0.955 | 0.955 | 0.510 | 1.44x | 18.7/28.1/31.0% | 2.0/5.4% | 3 |
| 1.0 | 1 | 0.844 | 0.839 | 0.005 | - | - | 0.950 | 0.950 | 0.480 | 1.60x | 20.9/31.5/34.8% | 2.3/6.0% | 3 |
| 4.0 | 1 | 0.817 | 0.810 | 0.007 | - | - | 0.936 | 0.938 | 0.471 | 1.96x | 25.6/39.0/43.6% | 2.7/7.6% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.899 | 0.920 | 0.473 | 5.41x | 56.9/73.5/79.1% | 3.9/12.7% | 3 |
| 1.0 | 1 | 0.699 | 0.691 | 0.008 | - | - | 0.840 | 0.883 | 0.410 | 6.00x | 62.0/75.9/80.7% | 4.4/13.7% | 3 |

> traceroute-per-hour=0.0: queue drops 14.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 124

> traceroute-per-hour=1.0: queue drops 24.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 113

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.571 | 0.566 | 0.006 | - | - | 0.695 | 0.702 | 0.000 | 1.11x | 20.3/28.1/32.2% | 2.5/6.5% | 3 |
| 60 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 90 | 1 | 0.933 | 0.930 | 0.002 | - | - | 0.989 | 0.989 | 0.591 | 1.65x | 19.0/35.4/38.3% | 1.5/5.1% | 3 |
| 120 | 1 | 0.961 | 0.960 | 0.001 | - | - | 0.999 | 0.999 | 0.631 | 1.98x | 22.6/36.7/42.4% | 1.3/5.2% | 3 |
| 150 | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.997 | 0.997 | 0.811 | 2.81x | 28.7/52.3/60.3% | 1.5/5.2% | 3 |

> nodes=40: decode_failures 2

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 120 | 1 | 0.784 | 0.775 | 0.009 | - | - | 0.959 | 0.960 | 0.200 | 2.41x | 16.3/33.0/42.1% | 1.7/5.5% | 3 |
| 250 | 1 | 0.532 | 0.524 | 0.008 | - | - | 0.837 | 0.837 | 0.197 | 4.82x | 16.3/31.5/45.0% | 1.6/6.3% | 3 |
| 500 | 1 | 0.327 | 0.323 | 0.004 | - | - | 0.475 | 0.482 | 0.129 | 9.94x | 18.1/30.0/42.0% | 1.6/6.4% | 3 |

> nodes=500: decode_failures 22

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.792 | 0.785 | 0.007 | - | - | 0.968 | 0.968 | 0.200 | 2.24x | 15.1/30.8/39.0% | 1.5/5.0% | 3 |
| 250 | 1 | 0.535 | 0.526 | 0.009 | - | - | 0.843 | 0.845 | 0.223 | 4.52x | 15.5/29.6/41.9% | 1.5/5.6% | 3 |
| 500 | 1 | 0.328 | 0.324 | 0.004 | - | - | 0.478 | 0.479 | 0.125 | 9.18x | 16.8/27.9/39.1% | 1.5/5.9% | 3 |

> nodes=500: decode_failures 8

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.870 | 0.866 | 0.004 | - | - | 0.955 | 0.956 | 0.488 | 1.40x | 18.1/27.4/30.1% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.932 | 0.933 | 0.178 | 1.23x | 16.9/26.6/29.8% | 2.0/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.880 | 0.877 | 0.003 | - | - | 0.949 | 0.951 | 0.522 | 1.47x | 18.6/27.8/30.6% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.835 | 0.832 | 0.003 | - | - | 0.914 | 0.915 | 0.252 | 1.41x | 19.3/30.2/33.5% | 2.5/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.05 | 1 | 0.869 | 0.866 | 0.003 | - | - | 0.956 | 0.956 | 0.509 | 1.52x | 20.4/32.3/35.4% | 2.2/5.2% | 3 |
| 0.1 | 1 | 0.866 | 0.863 | 0.003 | - | - | 0.955 | 0.955 | 0.471 | 1.56x | 21.9/32.6/37.5% | 2.2/5.0% | 3 |
| 0.2 | 1 | 0.866 | 0.863 | 0.003 | - | - | 0.949 | 0.949 | 0.610 | 1.75x | 24.7/36.4/40.6% | 2.3/5.0% | 3 |

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| local-typical | 1 | 0.728 | 0.721 | 0.006 | - | - | 0.879 | 0.883 | 0.163 | 1.60x | 13.9/27.1/34.0% | 2.2/5.4% | 3 |
| event | 1 | 0.395 | 0.389 | 0.006 | - | - | 0.578 | 0.582 | 0.000 | 1.55x | 8.7/22.5/25.9% | 2.6/5.0% | 3 |
| backbone | 1 | 0.976 | 0.976 | 0.000 | - | - | 0.996 | 0.997 | 0.889 | 1.10x | 28.2/33.2/37.2% | 1.3/5.4% | 3 |

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.749 | 0.745 | 0.003 | - | - | 0.945 | 0.945 | 0.052 | 1.19x | 25.0/34.6/38.0% | 2.5/7.6% | 3 |
| 60 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 90 | 1 | 0.817 | 0.812 | 0.005 | - | - | 0.969 | 0.969 | 0.249 | 1.72x | 15.1/29.9/36.2% | 1.6/5.4% | 3 |
| 120 | 1 | 0.784 | 0.775 | 0.009 | - | - | 0.959 | 0.960 | 0.200 | 2.41x | 16.3/33.0/42.1% | 1.7/5.5% | 3 |
| 150 | 1 | 0.683 | 0.666 | 0.017 | - | - | 0.923 | 0.931 | 0.197 | 2.75x | 14.7/30.1/42.0% | 1.5/5.7% | 3 |

> nodes=150: decode_failures 16

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 1.25 | 1 | 0.653 | 0.647 | 0.006 | - | - | 0.868 | 0.869 | 0.144 | 1.47x | 12.9/23.0/25.8% | 2.1/5.6% | 3 |
| 1.5 | 1 | 0.450 | 0.435 | 0.015 | - | - | 0.753 | 0.762 | 0.000 | 1.43x | 12.1/19.1/23.7% | 2.2/5.4% | 3 |
| 2.0 | 1 | 0.188 | 0.182 | 0.005 | - | - | 0.310 | 0.377 | 0.000 | 1.06x | 6.4/10.0/13.6% | 1.9/3.6% | 3 |

> stretch=2.0: decode_failures 8

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| clustered | 1 | 0.948 | 0.948 | 0.000 | - | - | 0.982 | 0.982 | 0.575 | 1.15x | 25.8/35.2/35.8% | 1.5/5.5% | 3 |
| corridor | 1 | 0.736 | 0.728 | 0.009 | - | - | 0.943 | 0.945 | 0.135 | 1.34x | 16.6/27.8/30.0% | 1.9/5.7% | 3 |
| hub | 1 | 0.943 | 0.942 | 0.001 | - | - | 0.983 | 0.983 | 0.622 | 1.20x | 25.5/36.3/38.0% | 1.7/5.4% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.837 | 0.837 | 0.000 | - | - | 0.939 | 0.941 | 0.491 | 1.65x | 21.5/32.4/35.9% | 2.3/6.3% | 3 |
| True | 1 | 0.832 | 0.832 | 0.000 | - | - | 0.948 | 0.948 | 0.472 | 1.65x | 21.4/32.5/36.0% | 2.2/6.4% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.832 | 0.832 | 0.000 | - | - | 0.948 | 0.948 | 0.472 | 1.65x | 21.4/32.5/36.0% | 2.2/6.4% | 3 |
| m4-early-flood | 1 | 0.832 | 0.832 | 0.000 | - | - | 0.949 | 0.950 | 0.459 | 1.66x | 21.7/32.9/36.3% | 2.3/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.858 | 0.858 | 0.000 | - | - | 0 | 0.000 | 0.492 | 1.32x | 17.2/25.9/28.4% | 1.9/4.9% | 3 |
| chain | 1 | 0.853 | 0.851 | 0.002 | - | - | 0.926 | 0.956 | 0.498 | 1.56x | 20.5/30.6/34.0% | 2.1/5.9% | 3 |
| sr | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| True | 1 | 0.860 | 0.858 | 0.002 | - | - | 0.953 | 0.954 | 0.510 | 1.38x | 17.8/26.8/29.6% | 2.0/5.1% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.961 | 0.960 | 0.001 | - | - | 0.999 | 0.999 | 0.631 | 1.98x | 22.6/36.7/42.4% | 1.3/5.2% | 3 |
| True | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.998 | 0.998 | 0.634 | 2.00x | 22.4/36.7/42.3% | 1.3/5.2% | 3 |

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.252 | 0.243 | 0.009 | - | - | 0.455 | 0.512 | 0.000 | 0.06x | 0.4/0.7/0.9% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.518 | 0.508 | 0.011 | - | - | 0.795 | 0.798 | 0.000 | 0.30x | 2.5/4.1/5.5% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.797 | 0.793 | 0.004 | - | - | 0.950 | 0.950 | 0.344 | 1.34x | 14.4/22.7/26.7% | 1.9/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 15

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.873 | 0.869 | 0.004 | - | - | 0.958 | 0.960 | 0.552 | 1.31x | 19.5/28.5/30.8% | 1.8/5.2% | 3 |
| 1.0 | 1 | 0.908 | 0.906 | 0.002 | - | - | 0.969 | 0.970 | 0.695 | 1.07x | 22.9/30.2/31.9% | 1.4/5.2% | 3 |

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.362 | 0.359 | 0.003 | - | - | 0.633 | 0.633 | 0.000 | 0.14x | 1.1/2.2/2.4% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| LITE_FAST | 1 | 0.803 | 0.798 | 0.004 | - | - | 0.946 | 0.946 | 0.381 | 1.03x | 12.4/19.7/22.8% | 1.4/4.0% | 3 |
| NARROW_SLOW | 1 | 0.807 | 0.801 | 0.005 | - | - | 0.958 | 0.958 | 0.382 | 1.33x | 16.5/25.1/30.4% | 1.9/5.1% | 3 |

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| temporal | 1 | 0.786 | 0.780 | 0.006 | - | - | 0.936 | 0.938 | 0.375 | 1.35x | 17.4/26.5/28.9% | 1.9/5.0% | 3 |
| transient | 1 | 0.850 | 0.846 | 0.005 | - | - | 0.956 | 0.957 | 0.474 | 1.37x | 17.7/26.7/29.6% | 1.8/5.2% | 3 |
| periodic | 1 | 0.688 | 0.685 | 0.003 | - | - | 0.782 | 0.787 | 0.388 | 1.26x | 16.5/24.8/27.3% | 1.7/4.5% | 3 |

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.362 | 0.359 | 0.003 | - | - | 0.633 | 0.633 | 0.000 | 0.14x | 1.1/2.2/2.4% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| LONG_MODERATE | 1 | 0.811 | 0.806 | 0.005 | - | - | 0.903 | 0.905 | 0.502 | 3.48x | 50.5/65.5/69.2% | 5.0/12.2% | 3 |

> faster: 1.03 s per simulated hour against 2.85 over 57 prior run(s) - 2.8x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.084 | 0.084 | 0.000 | - | - | 0.150 | 0.273 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.252 | 0.243 | 0.009 | - | - | 0.455 | 0.512 | 0.000 | 0.06x | 0.4/0.7/0.9% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| LONG_TURBO | 1 | 0.797 | 0.793 | 0.004 | - | - | 0.950 | 0.950 | 0.344 | 1.34x | 14.4/22.7/26.7% | 1.9/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.851 | 0.847 | 0.004 | - | - | 0.949 | 0.949 | 0.549 | 1.93x | 24.0/36.2/40.0% | 2.9/6.8% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 4

> preset=SHORT_TURBO: decode_failures 15

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.797 | 0.793 | 0.004 | - | - | 0.894 | 0.894 | 0.460 | 1.34x | 17.6/26.4/29.1% | 1.9/4.9% | 3 |
| 10000 | 1 | 0.688 | 0.685 | 0.003 | - | - | 0.782 | 0.787 | 0.388 | 1.26x | 16.5/24.8/27.3% | 1.7/4.5% | 3 |
| 4000 | 1 | 0.459 | 0.455 | 0.004 | - | - | 0.548 | 0.570 | 0.193 | 1.09x | 14.5/21.8/24.1% | 1.6/3.6% | 3 |
| 2000 | 1 | 0.111 | 0.111 | 0.000 | - | - | 0.146 | 0.207 | 0.028 | 0.73x | 10.0/15.3/17.3% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 4

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.450 | 0.435 | 0.015 | - | - | 0.753 | 0.762 | 0.000 | 1.43x | 12.1/19.1/23.7% | 2.2/5.4% | 3 |
| 1.0 | 1 | 0.664 | 0.652 | 0.012 | - | - | 0.866 | 0.870 | 0.329 | 1.07x | 14.4/21.3/22.9% | 1.5/4.8% | 3 |

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 22 | 1 | 0.471 | 0.459 | 0.012 | - | - | 0.725 | 0.748 | 0.000 | 1.52x | 12.3/19.3/23.8% | 2.3/5.1% | 3 |
| 17 | 1 | 0.219 | 0.210 | 0.009 | - | - | 0.473 | 0.510 | 0.000 | 1.21x | 7.4/13.9/16.5% | 1.8/4.3% | 3 |
| 14 | 1 | 0.120 | 0.120 | 0.000 | - | - | 0.099 | 0.230 | 0.000 | 0.81x | 3.7/8.3/9.5% | 1.3/2.9% | 3 |

> tx-power=22: decode_failures 18

> tx-power=17: decode_failures 13

> tx-power=14: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.961 | 0.960 | 0.001 | - | - | 0.999 | 0.999 | 0.631 | 1.98x | 22.6/36.7/42.4% | 1.3/5.2% | 3 |
| True | 1 | 0.953 | 0.952 | 0.001 | - | - | 0.997 | 0.997 | 0.606 | 2.33x | 25.8/40.7/46.5% | 1.5/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.866 | 0.863 | 0.003 | - | - | 0.957 | 0.957 | 0.526 | 1.42x | 19.1/29.8/32.4% | 2.0/5.1% | 3 |
| True | 1 | 0.889 | 0.887 | 0.002 | - | - | 0.958 | 0.959 | 0.563 | 1.51x | 19.9/30.5/33.1% | 2.2/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| random | 1 | 0.841 | 0.832 | 0.008 | - | - | 0.940 | 0.941 | 0.466 | 1.36x | 17.5/26.3/29.0% | 2.0/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.733 | 0.712 | 0.020 | - | - | 0.932 | 0.934 | 0.268 | 1.05x | 14.5/23.1/25.7% | 1.4/4.8% | 3 |
| 7 | 1 | 0.902 | 0.899 | 0.003 | - | - | 0.958 | 0.959 | 0.594 | 1.54x | 19.3/28.5/31.1% | 2.4/5.4% | 3 |
| 15 | 1 | 0.914 | 0.913 | 0.001 | - | - | 0.960 | 0.961 | 0.640 | 1.54x | 19.2/28.5/31.0% | 2.4/5.4% | 3 |
| 32 | 1 | 0.914 | 0.913 | 0.001 | - | - | 0.960 | 0.961 | 0.640 | 1.54x | 19.2/28.5/31.0% | 2.4/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.733 | 0.712 | 0.020 | - | - | 0.932 | 0.934 | 0.268 | 1.05x | 14.5/23.1/25.7% | 1.4/4.8% | 3 |
| 5 | 1 | 0.865 | 0.861 | 0.004 | - | - | 0.955 | 0.956 | 0.489 | 1.40x | 18.0/27.2/29.9% | 2.0/5.3% | 3 |
| 7 | 1 | 0.902 | 0.899 | 0.003 | - | - | 0.958 | 0.959 | 0.594 | 1.54x | 19.3/28.5/31.1% | 2.4/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.862 | 0.862 | 0.000 | - | - | 0.915 | 0.962 | 0.483 | 1.33x | 17.4/26.1/28.7% | 1.9/5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.733 | 0.712 | 0.020 | - | - | 0.932 | 0.934 | 0.268 | 1.05x | 14.5/23.1/25.7% | 1.4/4.8% | 3 |
| True | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| BALANCED | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| STRICT | 1 | 0.756 | 0.756 | 0.000 | - | - | 0.859 | 0.859 | 0.356 | 1.48x | 19.1/28.6/31.5% | 2.1/5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| dm | 1 | 0.866 | 0.862 | 0.004 | - | - | 0.962 | 0.964 | 0.514 | 1.35x | 17.6/26.4/29.0% | 1.9/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.861 | 0.858 | 0.004 | - | - | 0.963 | 0.964 | 0.497 | 1.38x | 17.9/26.9/29.7% | 1.9/5.2% | 3 |
| local | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| time | 1 | 0.859 | 0.857 | 0.003 | - | - | 0.950 | 0.951 | 0.494 | 1.39x | 18.0/26.9/29.8% | 1.9/5.2% | 3 |
| window | 1 | 0.860 | 0.856 | 0.004 | - | - | 0.956 | 0.956 | 0.474 | 1.37x | 17.8/26.8/29.6% | 2.0/5.1% | 3 |

> bucket-mode=global: misdecodes 59

> bucket-mode=time: misdecodes 42

> bucket-mode=window: misdecodes 16

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.857 | 0.854 | 0.004 | - | - | 0.957 | 0.958 | 0.496 | 1.54x | 19.8/29.5/32.9% | 2.1/5.8% | 3 |
| 1800 | 1 | 0.859 | 0.857 | 0.003 | - | - | 0.950 | 0.951 | 0.494 | 1.39x | 18.0/26.9/29.8% | 1.9/5.2% | 3 |
| 3600 | 1 | 0.856 | 0.853 | 0.003 | - | - | 0.958 | 0.960 | 0.487 | 1.39x | 18.1/27.1/29.9% | 1.9/5.2% | 3 |

> time-bucket-s=600: misdecodes 135

> time-bucket-s=1800: misdecodes 42

> time-bucket-s=3600: misdecodes 11

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| interval | 1 | 0.836 | 0.832 | 0.004 | - | - | 0.936 | 0.942 | 0.477 | 1.80x | 23.3/35.9/39.3% | 2.4/7.2% | 3 |
| aimd | 1 | 0.857 | 0.855 | 0.001 | - | - | 0.924 | 0.956 | 0.498 | 1.37x | 17.8/26.8/29.5% | 1.9/5.2% | 3 |
| bucket+interval | 1 | 0.844 | 0.839 | 0.006 | - | - | 0.947 | 0.947 | 0.479 | 1.82x | 23.6/36.0/39.7% | 2.4/7.2% | 3 |

> trigger=interval: misdecodes 13

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 7

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.859 | 0.856 | 0.004 | - | - | 0.955 | 0.956 | 0.491 | 1.37x | 17.8/26.8/29.4% | 1.9/5.2% | 3 |
| 8 | 1 | 0.862 | 0.859 | 0.003 | - | - | 0.960 | 0.962 | 0.497 | 1.39x | 18.0/27.0/29.7% | 2.0/5.2% | 3 |
| 16 | 1 | 0.857 | 0.854 | 0.004 | - | - | 0.955 | 0.955 | 0.508 | 1.37x | 17.7/26.5/29.3% | 1.9/5.1% | 3 |
| 32 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 50 | 1 | 0.854 | 0.850 | 0.005 | - | - | 0.956 | 0.956 | 0.480 | 1.37x | 17.9/26.9/29.5% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 90

> capacity=8: decode_failures 16

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.859 | 0.856 | 0.004 | - | - | 0.955 | 0.956 | 0.491 | 1.37x | 17.8/26.8/29.4% | 1.9/5.2% | 3 |
| 8 | 1 | 0.862 | 0.859 | 0.003 | - | - | 0.960 | 0.962 | 0.497 | 1.39x | 18.0/27.0/29.7% | 2.0/5.2% | 3 |
| 16 | 1 | 0.857 | 0.854 | 0.004 | - | - | 0.955 | 0.955 | 0.508 | 1.37x | 17.7/26.5/29.3% | 1.9/5.1% | 3 |
| 32 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 50 | 1 | 0.854 | 0.850 | 0.005 | - | - | 0.956 | 0.956 | 0.480 | 1.37x | 17.9/26.9/29.5% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 90

> capacity=8: decode_failures 16

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.860 | 0.856 | 0.004 | - | - | 0.958 | 0.961 | 0.505 | 1.36x | 17.6/26.6/29.3% | 1.9/5.1% | 3 |
| 16 | 1 | 0.864 | 0.860 | 0.004 | - | - | 0.961 | 0.962 | 0.479 | 1.36x | 17.7/26.7/29.4% | 1.9/5.2% | 3 |
| 32 | 1 | 0.860 | 0.856 | 0.004 | - | - | 0.956 | 0.956 | 0.474 | 1.37x | 17.8/26.8/29.6% | 2.0/5.1% | 3 |

> capacity=8: misdecodes 20

> capacity=8: decode_failures 17

> capacity=16: misdecodes 24

> capacity=32: misdecodes 16

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.844 | 0.839 | 0.006 | - | - | 0.947 | 0.947 | 0.479 | 1.82x | 23.6/36.0/39.7% | 2.4/7.2% | 3 |
| 02-06 | 1 | 0.858 | 0.856 | 0.002 | - | - | 0.935 | 0.956 | 0.476 | 1.42x | 18.4/27.6/30.5% | 1.9/5.4% | 3 |
| 00-08 | 1 | 0.861 | 0.858 | 0.003 | - | - | 0.943 | 0.962 | 0.475 | 1.48x | 19.2/28.8/31.9% | 2.0/5.7% | 3 |

> catch-up-hours=: misdecodes 7

> catch-up-hours=02-06: decode_failures 3

> catch-up-hours=00-08: decode_failures 5

> faster: 4.23 s per simulated hour against 8.67 over 57 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.858 | 0.858 | 0.001 | - | - | 0.953 | 0.953 | 0.514 | 1.38x | 17.9/27.1/29.7% | 2.0/5.2% | 3 |
| 2 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 3 | 1 | 0.865 | 0.857 | 0.008 | - | - | 0.956 | 0.960 | 0.520 | 1.38x | 17.8/26.8/29.5% | 2.0/5.2% | 3 |
| 4 | 1 | 0.867 | 0.853 | 0.014 | - | - | 0.955 | 0.957 | 0.495 | 1.38x | 17.9/27.2/29.9% | 1.9/5.3% | 3 |

> faster: 1.33 s per simulated hour against 3.96 over 57 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.858 | 0.858 | 0.001 | - | - | 0.953 | 0.953 | 0.514 | 1.38x | 17.9/27.1/29.7% | 2.0/5.2% | 3 |
| 2 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 3 | 1 | 0.865 | 0.857 | 0.008 | - | - | 0.956 | 0.960 | 0.520 | 1.38x | 17.8/26.8/29.5% | 2.0/5.2% | 3 |
| 4 | 1 | 0.867 | 0.853 | 0.014 | - | - | 0.955 | 0.957 | 0.495 | 1.38x | 17.9/27.2/29.9% | 1.9/5.3% | 3 |
| 5 | 1 | 0.868 | 0.853 | 0.015 | - | - | 0.935 | 0.955 | 0.492 | 1.38x | 17.8/27.1/29.8% | 1.9/5.3% | 3 |

> hops-apart=5: decode_failures 20

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.855 | 0.852 | 0.003 | - | - | 0.954 | 0.954 | 0.480 | 1.39x | 18.2/27.2/30.0% | 2.0/5.2% | 3 |
| 30 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 120 | 1 | 0.851 | 0.847 | 0.004 | - | - | 0.949 | 0.949 | 0.504 | 1.36x | 17.7/26.7/29.3% | 1.9/5.1% | 3 |
| 600 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.948 | 0.948 | 0.483 | 1.37x | 17.7/26.8/29.6% | 1.9/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.855 | 0.852 | 0.003 | - | - | 0.954 | 0.954 | 0.480 | 1.39x | 18.2/27.2/30.0% | 2.0/5.2% | 3 |
| 30 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 120 | 1 | 0.851 | 0.847 | 0.004 | - | - | 0.949 | 0.949 | 0.504 | 1.36x | 17.7/26.7/29.3% | 1.9/5.1% | 3 |
| 600 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.948 | 0.948 | 0.483 | 1.37x | 17.7/26.8/29.6% | 1.9/5.2% | 3 |

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.870 | 0.848 | 0.022 | - | - | 0.816 | 0.965 | 0.526 | 1.39x | 17.9/27.0/29.4% | 2.0/5.2% | 3 |
| routers | 1 | 0.852 | 0.852 | 0.001 | - | - | 0.955 | 0.955 | 0.493 | 1.39x | 17.8/27.0/29.7% | 2.0/5.2% | 3 |
| alternate-routers | 1 | 0.857 | 0.856 | 0.000 | - | - | 0.955 | 0.955 | 0.505 | 1.39x | 17.9/27.1/29.6% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.851 | 0.850 | 0.001 | - | - | 0.948 | 0.948 | 0.479 | 1.38x | 17.9/27.1/29.8% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.865 | 0.848 | 0.017 | - | - | 0.867 | 0.960 | 0.541 | 1.39x | 18.2/27.0/29.6% | 2.0/5.3% | 3 |
| hops-apart | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

> place=spread: decode_failures 20

> place=random-clients: decode_failures 38

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.870 | 0.848 | 0.022 | - | - | 0.816 | 0.965 | 0.526 | 1.39x | 17.9/27.0/29.4% | 2.0/5.2% | 3 |
| routers | 1 | 0.852 | 0.852 | 0.001 | - | - | 0.955 | 0.955 | 0.493 | 1.39x | 17.8/27.0/29.7% | 2.0/5.2% | 3 |
| alternate-routers | 1 | 0.857 | 0.856 | 0.000 | - | - | 0.955 | 0.955 | 0.505 | 1.39x | 17.9/27.1/29.6% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.851 | 0.850 | 0.001 | - | - | 0.948 | 0.948 | 0.479 | 1.38x | 17.9/27.1/29.8% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.865 | 0.848 | 0.017 | - | - | 0.867 | 0.960 | 0.541 | 1.39x | 18.2/27.0/29.6% | 2.0/5.3% | 3 |
| hops-apart | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

> place=spread: decode_failures 20

> place=random-clients: decode_failures 38

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| broadcast | 1 | 0.869 | 0.852 | 0.017 | - | - | 0.953 | 0.955 | 0.531 | 1.42x | 18.4/27.5/30.4% | 2.0/5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| heard | 1 | 0.863 | 0.858 | 0.005 | - | - | 0.959 | 0.961 | 0.506 | 1.36x | 17.6/26.5/29.3% | 1.9/5.1% | 3 |

> replay-ordering=heard: misdecodes 24

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.869 | 0.852 | 0.017 | - | - | 0.953 | 0.955 | 0.531 | 1.42x | 18.4/27.5/30.4% | 2.0/5.3% | 3 |
| heard | 1 | 0.867 | 0.849 | 0.018 | - | - | 0.952 | 0.954 | 0.521 | 1.44x | 18.6/27.9/30.8% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| enum | 1 | 0.866 | 0.862 | 0.004 | - | - | 0.965 | 0.968 | 0.486 | 1.38x | 17.9/27.0/29.7% | 1.9/5.3% | 3 |
| hybrid | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.852 | 0.852 | 0.001 | - | - | 0.955 | 0.955 | 0.493 | 1.39x | 17.8/27.0/29.7% | 2.0/5.2% | 3 |
| 6 | 1 | 0.850 | 0.847 | 0.004 | - | - | 0.950 | 0.950 | 0.466 | 1.41x | 18.3/27.7/30.4% | 2.0/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.861 | 0.859 | 0.002 | - | - | 0.956 | 0.957 | 0.500 | 1.36x | 17.6/26.5/29.3% | 1.9/5.1% | 2 |
| 3 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 5 | 1 | 0.855 | 0.847 | 0.008 | - | - | 0.968 | 0.972 | 0.483 | 1.38x | 17.9/26.8/29.5% | 2.0/5.2% | 5 |
| 8 | 1 | 0.865 | 0.853 | 0.012 | - | - | 0.975 | 0.976 | 0.508 | 1.43x | 18.4/27.7/30.5% | 2.0/5.4% | 8 |

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.861 | 0.859 | 0.002 | - | - | 0.956 | 0.957 | 0.500 | 1.36x | 17.6/26.5/29.3% | 1.9/5.1% | 2 |
| 3 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 5 | 1 | 0.855 | 0.847 | 0.008 | - | - | 0.968 | 0.972 | 0.483 | 1.38x | 17.9/26.8/29.5% | 2.0/5.2% | 5 |
| 8 | 1 | 0.865 | 0.853 | 0.012 | - | - | 0.975 | 0.976 | 0.508 | 1.43x | 18.4/27.7/30.5% | 2.0/5.4% | 8 |

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| True | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.865 | 0.861 | 0.004 | - | - | 0.963 | 0.966 | 0.476 | 1.29x | 16.8/25.2/27.6% | 1.8/4.8% | 3 |
| 1 | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.952 | 0.953 | 0.459 | 1.30x | 16.9/25.4/28.0% | 1.8/4.9% | 3 |
| 2 | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.952 | 0.953 | 0.459 | 1.30x | 16.9/25.4/28.0% | 1.8/4.9% | 3 |
| 4 | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.952 | 0.953 | 0.459 | 1.30x | 16.9/25.4/28.0% | 1.8/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.853 | 0.849 | 0.004 | - | - | 0.952 | 0.952 | 0.488 | 1.36x | 17.7/26.6/29.4% | 1.9/5.1% | 3 |
| 24 | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.955 | 0.956 | 0.482 | 1.39x | 18.0/27.2/29.9% | 2.0/5.2% | 3 |
| 32 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.953 | 0.953 | 0.504 | 1.38x | 17.9/26.9/29.6% | 1.9/5.2% | 3 |
| 64 | 1 | 0.849 | 0.846 | 0.003 | - | - | 0.944 | 0.944 | 0.474 | 1.35x | 17.4/26.4/29.0% | 1.9/5.1% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.859 | 0.855 | 0.005 | - | - | 0.960 | 0.960 | 0.510 | 1.42x | 18.5/27.7/30.7% | 2.0/5.4% | 3 |
| 16 | 1 | 0.854 | 0.850 | 0.004 | - | - | 0.949 | 0.949 | 0.496 | 1.39x | 18.1/27.1/29.8% | 1.9/5.2% | 3 |
| 32 | 1 | 0.860 | 0.856 | 0.004 | - | - | 0.956 | 0.956 | 0.474 | 1.37x | 17.8/26.8/29.6% | 2.0/5.1% | 3 |

> window-size=8: misdecodes 155

> window-size=16: misdecodes 61

> window-size=32: misdecodes 16

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.961 | 0.960 | 0.001 | - | - | 0.999 | 0.999 | 0.631 | 1.98x | 22.6/36.7/42.4% | 1.3/5.2% | 3 |
| True | 1 | 0.783 | 0.775 | 0.007 | - | - | 0.923 | 0.931 | 0.469 | 5.37x | 56.7/73.5/79.2% | 3.8/12.5% | 3 |

> no-congestion-scaling=True: queue drops 13.5% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 8

> faster: 5.69 s per simulated hour against 17.1 over 57 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.535 | 0.526 | 0.009 | - | - | 0.843 | 0.845 | 0.223 | 4.52x | 15.5/29.6/41.9% | 1.5/5.6% | 3 |
| truesize | 1 | 0.567 | 0.559 | 0.008 | - | - | 0.871 | 0.873 | 0.241 | 3.48x | 11.6/24.5/35.0% | 1.1/5.0% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.962 | 0.961 | 0.001 | - | - | 0.999 | 0.999 | 0.626 | 1.91x | 21.2/34.7/40.0% | 1.2/4.9% | 3 |
| adaptive | 1 | 0.961 | 0.960 | 0.001 | - | - | 0.999 | 0.999 | 0.631 | 1.98x | 22.6/36.7/42.4% | 1.3/5.2% | 3 |

