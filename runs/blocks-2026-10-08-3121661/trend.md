# Sweep blocks-2026-10-08-3121661

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 3121661 · seeds 3121661
- **blocks** 87 run
- **compute** 9.7 h of simulator time across every cell
- **generated** 2026-10-08T10:12:24+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>85 warnings</summary>

- DB-hotstore-stress: max-num-nodes=10: decode_failures 73
- DB-hotstore-stress: max-num-nodes=120: decode_failures 86
- DB-hotstore-stress: max-num-nodes=250: decode_failures 122
- DB-warm: warm-num-nodes=0: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 102
- DB-warm: warm-num-nodes=25: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 102
- DB-warm: warm-num-nodes=100: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 102
- DB-warm: warm-num-nodes=2000: queue drops 14.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 102
- DG-burst: burst-loss=0.2: decode_failures 5
- DG-burst: burst-loss=0.3: decode_failures 15
- DG-outage: burst-loss=0.1: decode_failures 32
- DG-outage: burst-loss=0.2: decode_failures 26
- DG-outage: burst-loss=0.3: decode_failures 20
- DM-mode: faster: 1.45 s per simulated hour against 3.24 over 48 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- LD-chatty-hops: broadcast-interval-s=300: queue drops 12.2% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 11
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 14.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 102
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 27.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 93
- MS-density: nodes=40: decode_failures 22
- MS-density: nodes=120: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 154
- MS-hopscale: nodes=500: decode_failures 2
- MS-oversubscribed: nodes=250: decode_failures 86
- MS-siting: siting-mix=event: decode_failures 1
- MS-siting: siting-mix=backbone: misdecodes 1
- MS-stretch: stretch=1.25: decode_failures 34
- MS-stretch: stretch=2.0: decode_failures 14
- MS-stretch: slower: 4.8 s per simulated hour against 2.1 over 48 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-topology: topology=clustered: misdecodes 1
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 2
- RF-duct: duct-per-hour=1.0: misdecodes 1
- RF-eu-presets: preset=SHORT_FAST: decode_failures 19
- RF-preset: preset=SHORT_FAST: decode_failures 19
- RF-preset: preset=LONG_MODERATE: decode_failures 1
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 4
- RF-pulse: faster: 0.819 s per simulated hour against 1.67 over 48 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=17: decode_failures 1
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-adopt: no-adopt-hop-recommendation=True: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 35
- SF-bucket-mode: bucket-mode=time: misdecodes 48
- SF-bucket-mode: bucket-mode=window: misdecodes 23
- SF-bucket-time: time-bucket-s=600: misdecodes 120
- SF-bucket-time: time-bucket-s=1800: misdecodes 48
- SF-bucket-time: time-bucket-s=3600: misdecodes 17
- SF-cadence: trigger=interval: misdecodes 21
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 26
- SF-capacity-local: capacity=4: decode_failures 55
- SF-capacity-local: capacity=8: decode_failures 7
- SF-capacity: capacity=4: decode_failures 55
- SF-capacity: capacity=8: decode_failures 7
- SF-capacity-window: capacity=8: misdecodes 26
- SF-capacity-window: capacity=8: decode_failures 13
- SF-capacity-window: capacity=16: misdecodes 16
- SF-capacity-window: capacity=32: misdecodes 23
- SF-catchup: catch-up-hours=: misdecodes 26
- SF-catchup: catch-up-hours=02-06: decode_failures 7
- SF-catchup: catch-up-hours=00-08: decode_failures 7
- SF-hops-flat: faster: 1.83 s per simulated hour against 3.92 over 48 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: faster: 1.99 s per simulated hour against 4.72 over 48 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=spread: decode_failures 41
- SF-place-spread: place=spread: decode_failures 41
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 21
- SF-replay-order: replay-ordering=heard: misdecodes 14
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-servers-spread: faster: 1.1 s per simulated hour against 2.32 over 48 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-window-size: window-size=8: misdecodes 111
- SF-window-size: window-size=16: misdecodes 56
- SF-window-size: window-size=32: misdecodes 23
- TH-congestion-input: congestion-input=hotstore: decode_failures 86
- TH-congestion-input: congestion-input=truesize: decode_failures 71
- TH-congestion-input: slower: 44.4 s per simulated hour against 10.8 over 48 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 14.9% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 102

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 44.4 | 10.8 | 4.09x | 48 |
| `MS-stretch` | 4.8 | 2.1 | 2.28x | 48 |
| `DB-hotstore-stress` | 42.9 | 22.3 | 1.93x | 48 |
| `RF-eu-presets` | 3.01 | 1.85 | 1.63x | 48 |
| `RF-txpower` | 1.04 | 1.58 | 0.66x | 48 |
| `RF-preset-turbo` | 1 | 1.53 | 0.65x | 44 |
| `LD-traceroute-small` | 24.6 | 37.8 | 0.65x | 48 |
| `PR-dmmode-cr` | 1.7 | 2.68 | 0.63x | 48 |
| `RF-stretch-duct` | 1.18 | 1.87 | 0.63x | 48 |
| `SF-signed` | 1.09 | 1.73 | 0.63x | 48 |
| `SF-servers-flat` | 1.48 | 2.4 | 0.62x | 48 |
| `MS-siting` | 1.17 | 1.92 | 0.61x | 47 |
| `FW-signing-cost` | 0.968 | 1.6 | 0.60x | 48 |
| `PR-repeats` | 1.01 | 1.67 | 0.60x | 48 |
| `RF-noise` | 2.84 | 4.92 | 0.58x | 48 |
| `SF-jitter-local` | 1.01 | 1.79 | 0.56x | 48 |
| `SF-catchup` | 5.09 | 9.28 | 0.55x | 48 |
| `SF-capacity` | 0.952 | 1.75 | 0.54x | 48 |
| `LD-chatty-hops` | 2.19 | 4.21 | 0.52x | 48 |
| `RF-pulse` | 0.819 | 1.67 | 0.49x | 48 |
| `SF-servers-spread` | 1.1 | 2.32 | 0.47x | 48 |
| `SF-hops-flat` | 1.83 | 3.92 | 0.47x | 48 |
| `DM-mode` | 1.45 | 3.24 | 0.45x | 48 |
| `SF-hops-spread` | 1.99 | 4.72 | 0.42x | 48 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.995 | 0.995 | 0.878 → 0.878 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.965 | 0.965 | 0.868 → 0.878 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **held** | 0.044 → 0.999 | 0.955 | 0.134 → 0.979 | 75x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.088 → 0.965 | 0.876 | 0.086 → 0.873 | 12x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.107 → 0.912 | 0.805 | 0.103 → 0.819 | 1.4e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **text** | 0.130 → 0.877 | 0.748 | 0.127 → 0.873 | 4.6x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.147 → 0.877 | 0.730 | 0.143 → 0.873 | 2.8x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.141 → 0.828 | 0.687 | 0.139 → 0.821 | 2.3x advert_bytes | down | 3 |
| `MS-hopscale` | nodes | **held** | 0.363 → 0.965 | 0.601 | 0.302 → 0.873 | 12x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.361 → 0.962 | 0.601 | 0.304 → 0.794 | 5.1x sr_bytes | down | 3 |
| `RF-bw500` | preset | **text** | 0.275 → 0.789 | 0.514 | 0.258 → 0.784 | 2.3x sr_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.398 → 0.877 | 0.479 | 0.384 → 0.873 | 3.1x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.398 → 0.877 | 0.479 | 0.384 → 0.873 | 3x sr_bytes | up | 3 |
| `MS-topology` | topology | **text** | 0.521 → 0.965 | 0.444 | 0.512 → 0.964 | 1.7x sr_airtime | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.617 → 0.951 | 0.334 | 0.598 → 0.949 | 7.2x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.556 → 0.877 | 0.321 | 0.533 → 0.873 | 2.5x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.593 → 0.911 | 0.317 | 0.571 → 0.908 | 6x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.408 → 0.716 | 0.307 | 0.402 → 0.706 | 1.5x sr_airtime | up | 2 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.500 → 0.802 | 0.302 | 0.330 → 0.550 | 5.3x sr_airtime | up | 3 |
| `DG-burst` | burst-loss | **text** | 0.590 → 0.877 | 0.287 | 0.551 → 0.873 | 2.7x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.733 → 0.964 | 0.231 | 0.708 → 0.962 | 5.1x sr_airtime | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.758 → 0.964 | 0.205 | 0.750 → 0.962 | 3.8x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.734 → 0.936 | 0.203 | 0.715 → 0.935 | 1.9x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.734 → 0.929 | 0.195 | 0.715 → 0.926 | 1.7x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.703 → 0.896 | 0.193 | 0.696 → 0.888 | 3.6x sr_bytes | down | 5 |
| `RF-noise` | noise-profile | **held** | 0.805 → 0.965 | 0.159 | 0.716 → 0.873 | 1.2x sr_airtime | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.734 → 0.877 | 0.144 | 0.715 → 0.873 | 1.6x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **held** | 0.836 → 0.965 | 0.129 | 0.754 → 0.873 | 1.3x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.796 → 0.905 | 0.110 | 0.784 → 0.901 | 2.1x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.667 → 0.772 | 0.104 | 0.661 → 0.764 | 1.5x sr_airtime | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.803 → 0.905 | 0.102 | 0.790 → 0.901 | 2x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.778 → 0.877 | 0.099 | 0.768 → 0.873 | 1.6x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.828 → 0.927 | 0.098 | 0.821 → 0.925 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.828 → 0.927 | 0.098 | 0.821 → 0.925 | 2.5x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.838 → 0.921 | 0.083 | 0.830 → 0.920 | 5.3x sr_airtime | up | 4 |
| `SF-place-flat` | place | **held** | 0.890 → 0.970 | 0.080 | 0.870 → 0.885 | 4.5x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.890 → 0.970 | 0.080 | 0.870 → 0.885 | 4.5x sr_bytes | up | 6 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.877 → 0.950 | 0.073 | 0.873 → 0.947 | 1.6x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.877 → 0.950 | 0.073 | 0.873 → 0.945 | 1.2x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.877 → 0.943 | 0.065 | 0.873 → 0.938 | 1.4x bytes_on_air | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.944 → 0.995 | 0.051 | 0.870 → 0.882 | 2.2x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.944 → 0.995 | 0.051 | 0.870 → 0.882 | 2.2x sr_bytes | up | 5 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.920 → 0.965 | 0.044 | 0.872 → 0.873 | 24x sr_airtime | down | 3 |
| `AD-worst` | role-placement | **text** | 0.800 → 0.842 | 0.042 | 0.785 → 0.833 | 1.1x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **text** | 0.787 → 0.828 | 0.042 | 0.774 → 0.821 | 1.1x sr_bytes | down | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.838 → 0.877 | 0.040 | 0.830 → 0.873 | 1.5x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.877 → 0.916 | 0.039 | 0.873 → 0.914 | 3.4x bytes_on_air | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.852 → 0.888 | 0.036 | 0.844 → 0.886 | 11x sr_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.552 → 0.588 | 0.036 | 0.540 → 0.576 | 1.4x sr_airtime | up | 2 |
| `FW-mixed` | legacy-fraction | **held** | 0.943 → 0.978 | 0.036 | 0.862 → 0.876 | 2.3x bytes_on_air | up | 4 |
| `SF-cadence` | trigger | **held** | 0.932 → 0.965 | 0.032 | 0.844 → 0.873 | 16x sr_bytes | down | 4 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.949 → 0.977 | 0.028 | 0.866 → 0.880 | 2.4x bytes_on_air | up | 4 |
| `MS-roles` | role-mix | **text** | 0.828 → 0.856 | 0.028 | 0.821 → 0.852 | 1.4x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.877 → 0.902 | 0.024 | 0.873 → 0.899 | 1.3x sr_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.877 → 0.900 | 0.023 | 0.873 → 0.880 | 2.1x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **text** | 0.838 → 0.859 | 0.021 | 0.838 → 0.859 | 1.3x sr_airtime | up | 3 |
| `FW-versions` | profile | **text** | 0.856 → 0.877 | 0.021 | 0.848 → 0.873 | 3.4x bytes_on_air | up | 5 |
| `SF-servers-flat` | servers | **held** | 0.955 → 0.974 | 0.020 | 0.872 → 0.881 | 6.7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.955 → 0.974 | 0.020 | 0.872 → 0.881 | 6.7x sr_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.891 → 0.911 | 0.019 | 0.887 → 0.907 | 1.1x bytes_on_air | up | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.863 → 0.882 | 0.019 | 0.858 → 0.878 | 1.4x sr_bytes | down | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.873 → 0.888 | 0.015 | 0.868 → 0.885 | 1.2x sr_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.950 → 0.965 | 0.014 | 0.865 → 0.877 | 1.4x bytes_on_air | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.955 → 0.968 | 0.013 | 0.868 → 0.881 | 2.1x advert_bytes | up | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.874 → 0.885 | 0.011 | 0.868 → 0.879 | 5.2x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **text** | 0.877 → 0.888 | 0.011 | 0.873 → 0.884 | 1x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **text** | 0.874 → 0.885 | 0.011 | 0.868 → 0.881 | 6.1x advert_bytes | up | 3 |
| `FW-firmware` | profile | **held** | 0.965 → 0.975 | 0.011 | 0.869 → 0.873 | 3.3x bytes_on_air | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.850 → 0.859 | 0.009 | 0.850 → 0.859 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.965 → 0.973 | 0.009 | 0.873 → 0.881 | 3.4x advert_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.965 → 0.973 | 0.009 | 0.872 → 0.881 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.965 → 0.973 | 0.009 | 0.872 → 0.881 | 1.1x sr_bytes | up | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.850 → 0.858 | 0.009 | 0.850 → 0.858 | 1.1x sr_airtime | down | 2 |
| `SF-capacity` | capacity | **text** | 0.877 → 0.885 | 0.008 | 0.873 → 0.879 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.877 → 0.885 | 0.008 | 0.873 → 0.879 | 5.3x advert_bytes | down | 5 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.892 → 0.900 | 0.008 | 0.871 → 0.880 | 1.1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.957 → 0.964 | 0.007 | 0.954 → 0.962 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.957 → 0.965 | 0.007 | 0.871 → 0.873 | 1.2x sr_bytes | down | 2 |
| `SF-width` | short-id-bits | **text** | 0.877 → 0.884 | 0.007 | 0.873 → 0.878 | 3.1x advert_bytes | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.945 → 0.950 | 0.006 | 0.870 → 0.872 | 2.3x sr_airtime | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.965 → 0.970 | 0.005 | 0.873 → 0.877 | 3.2x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **text** | 0.877 → 0.883 | 0.005 | 0.873 → 0.878 | 5.9x advert_bytes | = | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.965 → 0.969 | 0.005 | 0.873 → 0.874 | 1.1x sr_bytes | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.998 → 1.000 | 0.002 | 0.961 → 0.962 | 1x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.999 → 1.000 | 0.001 | 0.962 → 0.962 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| sprinkled | 1 | 0.923 | 0.918 | 0.005 | - | - | 0.971 | 0.971 | 0.659 | 1.17x | 19.5/26.2/28.2% | 1.6/5.2% | 3 |
| arms-race | 1 | 0.950 | 0.945 | 0.005 | - | - | 0.986 | 0.986 | 0.686 | 1.04x | 22.0/29.9/31.5% | 1.2/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.911 | 0.896 | 0.016 | - | - | 0.965 | 0.966 | 0.641 | 1.13x | 16.6/24.3/27.4% | 1.7/5.3% | 3 |
| 0.3 | 1 | 0.950 | 0.947 | 0.003 | - | - | 0.994 | 0.995 | 0.858 | 0.96x | 19.3/25.7/31.1% | 1.2/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.828 | 0.821 | 0.008 | - | - | 0.932 | 0.937 | 0.193 | 1.11x | 15.8/25.6/30.2% | 1.8/5.3% | 3 |
| inverse | 1 | 0.787 | 0.774 | 0.012 | - | - | 0.901 | 0.907 | 0.400 | 1.06x | 13.6/18.5/20.2% | 1.9/3.4% | 3 |
| random | 1 | 0.803 | 0.792 | 0.011 | - | - | 0.934 | 0.936 | 0.219 | 1.03x | 14.3/20.4/25.2% | 1.7/5.2% | 3 |

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.828 | 0.821 | 0.008 | - | - | 0.932 | 0.937 | 0.193 | 1.11x | 15.8/25.6/30.2% | 1.8/5.3% | 3 |
| all-routers | 1 | 0.927 | 0.925 | 0.002 | - | - | 0.997 | 0.997 | 0.524 | 2.79x | 33.9/47.1/51.4% | 4.6/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.828 | 0.821 | 0.008 | - | - | 0.932 | 0.937 | 0.193 | 1.11x | 15.8/25.6/30.2% | 1.8/5.3% | 3 |
| no-mute | 1 | 0.862 | 0.852 | 0.010 | - | - | 0.967 | 0.967 | 0.436 | 1.20x | 15.6/23.5/27.1% | 1.8/5.3% | 3 |
| all-routers | 1 | 0.927 | 0.925 | 0.002 | - | - | 0.997 | 0.997 | 0.524 | 2.79x | 33.9/47.1/51.4% | 4.6/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.828 | 0.821 | 0.008 | - | - | 0.932 | 0.937 | 0.193 | 1.11x | 15.8/25.6/30.2% | 1.8/5.3% | 3 |
| local-typical | 1 | 0.817 | 0.799 | 0.018 | - | - | 0.952 | 0.955 | 0.000 | 1.27x | 13.9/23.5/30.0% | 2.1/5.3% | 3 |
| basement-heavy | 1 | 0.141 | 0.139 | 0.002 | - | - | 0.420 | 0.421 | 0.000 | 0.67x | 2.5/9.6/17.0% | 0.3/3.4% | 3 |

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.842 | 0.833 | 0.009 | - | - | 0.968 | 0.969 | 0.000 | 2.50x | 17.1/30.6/34.9% | 1.8/5.8% | 3 |
| inverse | 1 | 0.800 | 0.785 | 0.015 | - | - | 0.956 | 0.957 | 0.000 | 2.31x | 14.2/25.5/31.7% | 1.8/3.3% | 3 |

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.878 | 0.878 | 0.000 | - | - | 0 | 0.000 | 0.421 | 1.24x | 16.2/27.7/31.2% | 1.8/5.3% | 3 |
| sr | 1 | 0.897 | 0.878 | 0.020 | - | - | 0.995 | 0.996 | 0.435 | 1.25x | 16.3/27.8/31.3% | 1.8/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.796 | 0.784 | 0.012 | - | - | 0.896 | 0.897 | 0.389 | 2.94x | 38.3/67.7/71.2% | 3.9/10.2% | 3 |
| 100 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.967 | 0.967 | 0.530 | 1.50x | 20.0/38.2/41.7% | 2.0/5.3% | 3 |
| 120 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.967 | 0.967 | 0.530 | 1.50x | 20.0/38.2/41.7% | 2.0/5.3% | 3 |
| 250 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.967 | 0.967 | 0.530 | 1.50x | 20.0/38.2/41.7% | 2.0/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.336 | 0.330 | 0.005 | - | - | 0.500 | 0.568 | 0.109 | 12.04x | 40.3/61.6/73.4% | 4.3/11.0% | 3 |
| 120 | 1 | 0.552 | 0.540 | 0.012 | - | - | 0.802 | 0.817 | 0.155 | 4.92x | 16.6/31.3/42.2% | 1.7/6.0% | 3 |
| 250 | 1 | 0.561 | 0.550 | 0.011 | - | - | 0.802 | 0.832 | 0.139 | 4.73x | 16.0/30.0/40.3% | 1.6/5.7% | 3 |

> max-num-nodes=10: decode_failures 73

> max-num-nodes=120: decode_failures 86

> max-num-nodes=250: decode_failures 122

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.967 | 0.967 | 0.530 | 1.50x | 20.0/38.2/41.7% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.967 | 0.967 | 0.530 | 1.50x | 20.0/38.2/41.7% | 2.0/5.3% | 3 |
| constrained | 1 | 0.803 | 0.790 | 0.013 | - | - | 0.916 | 0.916 | 0.386 | 2.94x | 38.3/67.7/71.3% | 3.9/10.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.772 | 0.764 | 0.008 | - | - | 0.865 | 0.921 | 0.501 | 5.46x | 60.4/75.4/78.5% | 4.0/12.7% | 3 |
| 25 | 1 | 0.772 | 0.764 | 0.008 | - | - | 0.865 | 0.921 | 0.501 | 5.46x | 60.4/75.4/78.5% | 4.0/12.7% | 3 |
| 100 | 1 | 0.772 | 0.764 | 0.008 | - | - | 0.865 | 0.921 | 0.501 | 5.46x | 60.4/75.4/78.5% | 4.0/12.7% | 3 |
| 2000 | 1 | 0.772 | 0.764 | 0.008 | - | - | 0.865 | 0.921 | 0.501 | 5.46x | 60.4/75.4/78.5% | 4.0/12.7% | 3 |

> warm-num-nodes=0: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 102

> warm-num-nodes=25: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 102

> warm-num-nodes=100: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 102

> warm-num-nodes=2000: queue drops 14.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 102

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.785 | 0.773 | 0.012 | - | - | 0.946 | 0.949 | 0.329 | 1.18x | 15.9/26.3/29.9% | 1.7/4.8% | 3 |
| 0.2 | 1 | 0.685 | 0.657 | 0.027 | - | - | 0.899 | 0.909 | 0.239 | 1.11x | 15.1/24.9/28.4% | 1.6/4.4% | 3 |
| 0.3 | 1 | 0.590 | 0.551 | 0.039 | - | - | 0.835 | 0.870 | 0.171 | 1.02x | 14.2/23.1/26.6% | 1.5/3.9% | 3 |

> burst-loss=0.2: decode_failures 5

> burst-loss=0.3: decode_failures 15

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.957 | 0.959 | 0.368 | 1.34x | 17.8/29.1/32.8% | 1.9/5.3% | 3 |
| 0.2 | 1 | 0.828 | 0.819 | 0.009 | - | - | 0.956 | 0.960 | 0.305 | 1.39x | 18.8/29.6/33.7% | 2.0/5.1% | 3 |
| 0.3 | 1 | 0.778 | 0.768 | 0.011 | - | - | 0.939 | 0.942 | 0.230 | 1.41x | 19.5/30.3/34.5% | 2.1/5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.768 | 0.758 | 0.010 | - | - | 0.892 | 0.933 | 0.357 | 1.20x | 16.2/26.9/30.3% | 1.7/5.1% | 3 |
| 0.2 | 1 | 0.655 | 0.633 | 0.022 | - | - | 0.854 | 0.912 | 0.282 | 1.11x | 15.1/25.0/28.5% | 1.5/4.5% | 3 |
| 0.3 | 1 | 0.556 | 0.533 | 0.023 | - | - | 0.759 | 0.867 | 0.234 | 1.05x | 14.5/23.9/27.5% | 1.5/4.5% | 3 |

> burst-loss=0.1: decode_failures 32

> burst-loss=0.2: decode_failures 26

> burst-loss=0.3: decode_failures 20

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.838 | 0.838 | 0.000 | - | - | 0.950 | 0.951 | 0.362 | 1.68x | 22.0/37.3/41.6% | 2.4/7.1% | 3 |
| directed-with-late-flood | 1 | 0.858 | 0.858 | 0.000 | - | - | 0.953 | 0.956 | 0.385 | 1.46x | 19.3/33.1/37.1% | 2.0/6.4% | 3 |
| m4-early-flood | 1 | 0.859 | 0.859 | 0.000 | - | - | 0.955 | 0.958 | 0.378 | 1.49x | 19.7/33.7/37.7% | 2.1/6.5% | 3 |

> faster: 1.45 s per simulated hour against 3.24 over 48 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.975 | 0.976 | 0.000 | 0.67x | 9.0/11.8/14.3% | 1.1/2.0% | 3 |
| 2.8 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.867 | 0.862 | 0.005 | - | - | 0.943 | 0.943 | 0.197 | 1.12x | 15.3/24.5/26.3% | 1.6/4.7% | 3 |
| 0.5 | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.969 | 0.970 | 0.212 | 0.96x | 13.8/20.6/22.8% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.883 | 0.876 | 0.006 | - | - | 0.978 | 0.980 | 0.000 | 0.77x | 10.3/15.5/17.1% | 1.2/2.8% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.872 | 0.866 | 0.005 | - | - | 0.949 | 0.951 | 0.273 | 1.12x | 15.2/24.4/26.5% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.880 | 0.875 | 0.005 | - | - | 0.966 | 0.968 | 0.338 | 0.94x | 13.6/20.2/22.7% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.887 | 0.880 | 0.007 | - | - | 0.977 | 0.979 | 0.000 | 0.74x | 10.3/15.3/17.3% | 1.3/2.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.916 | 0.914 | 0.003 | - | - | 0.980 | 0.980 | 0.490 | 0.64x | 8.7/15.5/17.8% | 0.9/2.9% | 3 |
| signing=true | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.870 | 0.864 | 0.006 | - | - | 0.976 | 0.977 | 0.000 | 0.66x | 9.2/12.4/15.4% | 1.1/2.2% | 3 |
| 2.5 | 1 | 0.863 | 0.857 | 0.005 | - | - | 0.970 | 0.971 | 0.000 | 0.70x | 9.7/13.1/16.1% | 1.2/2.2% | 3 |
| 2.6 | 1 | 0.856 | 0.848 | 0.009 | - | - | 0.968 | 0.968 | 0.000 | 0.66x | 9.4/12.8/15.8% | 1.1/2.2% | 3 |
| 2.7 | 1 | 0.870 | 0.866 | 0.004 | - | - | 0.968 | 0.968 | 0.000 | 0.69x | 9.6/16.0/18.6% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.911 | 0.908 | 0.003 | - | - | 0.977 | 0.977 | 0.453 | 0.83x | 10.9/18.2/20.8% | 1.2/3.4% | 3 |
| 900 | 1 | 0.838 | 0.830 | 0.008 | - | - | 0.946 | 0.947 | 0.345 | 2.01x | 26.2/44.3/49.2% | 2.8/8.5% | 3 |
| 300 | 1 | 0.593 | 0.571 | 0.023 | - | - | 0.790 | 0.804 | 0.195 | 4.26x | 52.7/74.6/79.0% | 6.4/16.0% | 3 |

> broadcast-interval-s=300: decode_failures 11

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.951 | 0.949 | 0.002 | - | - | 0.990 | 0.991 | 0.660 | 0.90x | 11.6/18.6/21.2% | 1.2/3.5% | 3 |
| 900 | 1 | 0.896 | 0.890 | 0.005 | - | - | 0.956 | 0.957 | 0.551 | 2.36x | 30.2/46.7/52.0% | 3.3/8.8% | 3 |
| 300 | 1 | 0.617 | 0.598 | 0.019 | - | - | 0.730 | 0.730 | 0.303 | 4.73x | 58.5/75.5/79.5% | 7.3/16.7% | 3 |

> broadcast-interval-s=300: queue drops 12.2% of transmissions - airtime here is measured through a cap

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.902 | 0.899 | 0.003 | - | - | 0.973 | 0.974 | 0.450 | 1.14x | 14.9/25.7/29.2% | 1.6/5.0% | 3 |
| sinusoid | 1 | 0.878 | 0.875 | 0.004 | - | - | 0.952 | 0.953 | 0.436 | 1.15x | 15.2/25.5/28.8% | 1.6/4.8% | 3 |
| commuter | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.838 | 0.830 | 0.008 | - | - | 0.946 | 0.947 | 0.345 | 2.01x | 26.2/44.3/49.2% | 2.8/8.5% | 3 |
| 3600 | 1 | 0.911 | 0.908 | 0.003 | - | - | 0.977 | 0.977 | 0.453 | 0.83x | 10.9/18.2/20.8% | 1.2/3.4% | 3 |
| 10800 | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.981 | 0.982 | 0.476 | 0.55x | 7.1/11.8/13.5% | 0.8/2.2% | 3 |
| 43200 | 1 | 0.921 | 0.920 | 0.001 | - | - | 0.982 | 0.982 | 0.494 | 0.41x | 5.3/8.7/10.0% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.876 | 0.870 | 0.006 | - | - | 0.965 | 0.965 | 0.396 | 1.30x | 17.0/29.3/33.0% | 1.9/5.6% | 3 |
| 1.0 | 1 | 0.866 | 0.861 | 0.005 | - | - | 0.955 | 0.956 | 0.385 | 1.44x | 18.9/32.6/36.7% | 2.0/6.2% | 3 |
| 4.0 | 1 | 0.838 | 0.830 | 0.008 | - | - | 0.947 | 0.948 | 0.342 | 1.80x | 23.6/40.9/46.0% | 2.5/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.764 | 0.008 | - | - | 0.865 | 0.921 | 0.501 | 5.46x | 60.4/75.4/78.5% | 4.0/12.7% | 3 |
| 1.0 | 1 | 0.667 | 0.661 | 0.006 | - | - | 0.763 | 0.850 | 0.443 | 6.12x | 64.9/76.8/79.9% | 4.6/14.0% | 3 |

> traceroute-per-hour=0.0: queue drops 14.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 102

> traceroute-per-hour=1.0: queue drops 27.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 93

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.733 | 0.708 | 0.025 | - | - | 0.864 | 0.897 | 0.368 | 1.42x | 19.1/28.5/35.5% | 3.4/7.5% | 3 |
| 60 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 90 | 1 | 0.932 | 0.929 | 0.003 | - | - | 0.993 | 0.994 | 0.757 | 1.64x | 18.5/33.7/37.1% | 1.5/5.0% | 3 |
| 120 | 1 | 0.964 | 0.962 | 0.002 | - | - | 1.000 | 1.000 | 0.773 | 1.96x | 23.8/37.1/41.0% | 1.3/5.1% | 3 |
| 150 | 1 | 0.956 | 0.954 | 0.002 | - | - | 0.999 | 1.000 | 0.764 | 2.66x | 28.1/44.4/50.3% | 1.4/5.7% | 3 |

> nodes=40: decode_failures 22

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 120 | 1 | 0.816 | 0.809 | 0.007 | - | - | 0.963 | 0.963 | 0.393 | 2.28x | 17.1/28.3/32.8% | 1.7/5.0% | 3 |
| 250 | 1 | 0.552 | 0.540 | 0.012 | - | - | 0.813 | 0.823 | 0.151 | 5.09x | 17.3/32.6/44.1% | 1.7/6.4% | 3 |
| 500 | 1 | 0.306 | 0.302 | 0.003 | - | - | 0.363 | 0.364 | 0.080 | 9.88x | 18.6/27.4/36.8% | 1.7/5.7% | 3 |

> nodes=250: decode_failures 154

> nodes=500: decode_failures 2

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.802 | 0.794 | 0.008 | - | - | 0.962 | 0.962 | 0.359 | 2.17x | 16.5/27.1/31.4% | 1.6/4.8% | 3 |
| 250 | 1 | 0.552 | 0.540 | 0.012 | - | - | 0.802 | 0.817 | 0.155 | 4.92x | 16.6/31.3/42.2% | 1.7/6.0% | 3 |
| 500 | 1 | 0.307 | 0.304 | 0.003 | - | - | 0.361 | 0.361 | 0.073 | 9.04x | 17.0/25.1/34.1% | 1.6/5.3% | 3 |

> nodes=250: decode_failures 86

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.856 | 0.852 | 0.004 | - | - | 0.930 | 0.932 | 0.421 | 1.29x | 16.7/28.5/32.1% | 1.8/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.828 | 0.821 | 0.008 | - | - | 0.932 | 0.937 | 0.193 | 1.11x | 15.8/25.6/30.2% | 1.8/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.938 | 0.938 | 0.464 | 1.34x | 17.5/28.0/31.9% | 1.9/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.863 | 0.858 | 0.005 | - | - | 0.942 | 0.943 | 0.267 | 1.28x | 17.7/29.5/34.2% | 2.1/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.05 | 1 | 0.883 | 0.877 | 0.005 | - | - | 0.964 | 0.964 | 0.412 | 1.42x | 18.3/35.1/39.9% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.873 | 0.867 | 0.006 | - | - | 0.959 | 0.961 | 0.342 | 1.50x | 20.0/38.6/43.4% | 1.9/5.3% | 3 |
| 0.2 | 1 | 0.870 | 0.865 | 0.004 | - | - | 0.950 | 0.950 | 0.337 | 1.70x | 23.7/42.1/46.2% | 2.2/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| local-typical | 1 | 0.848 | 0.833 | 0.015 | - | - | 0.973 | 0.975 | 0.000 | 1.41x | 16.0/26.8/31.9% | 2.0/5.3% | 3 |
| event | 1 | 0.134 | 0.134 | 0.000 | - | - | 0.044 | 0.096 | 0.000 | 0.83x | 3.9/8.5/15.6% | 1.0/3.7% | 3 |
| backbone | 1 | 0.981 | 0.979 | 0.002 | - | - | 0.999 | 0.999 | 0.942 | 1.01x | 29.0/39.1/41.7% | 1.2/5.5% | 3 |

> siting-mix=event: decode_failures 1

> siting-mix=backbone: misdecodes 1

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.896 | 0.888 | 0.009 | - | - | 0.977 | 0.977 | 0.755 | 1.54x | 25.7/38.2/42.9% | 3.3/7.8% | 3 |
| 60 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 90 | 1 | 0.842 | 0.834 | 0.008 | - | - | 0.969 | 0.970 | 0.359 | 1.76x | 15.8/27.5/31.5% | 1.7/5.1% | 3 |
| 120 | 1 | 0.816 | 0.809 | 0.007 | - | - | 0.963 | 0.963 | 0.393 | 2.28x | 17.1/28.3/32.8% | 1.7/5.0% | 3 |
| 150 | 1 | 0.703 | 0.696 | 0.007 | - | - | 0.936 | 0.937 | 0.267 | 2.99x | 16.1/32.7/43.2% | 1.7/5.4% | 3 |

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 1.25 | 1 | 0.654 | 0.633 | 0.020 | - | - | 0.817 | 0.855 | 0.000 | 1.28x | 11.7/22.9/27.8% | 1.8/5.0% | 3 |
| 1.5 | 1 | 0.408 | 0.402 | 0.007 | - | - | 0.674 | 0.676 | 0.000 | 1.17x | 9.6/16.6/23.5% | 1.7/4.9% | 3 |
| 2.0 | 1 | 0.147 | 0.143 | 0.004 | - | - | 0.348 | 0.416 | 0.000 | 0.81x | 3.8/10.2/14.6% | 1.0/4.1% | 3 |

> stretch=1.25: decode_failures 34

> stretch=2.0: decode_failures 14

> slower: 4.8 s per simulated hour against 2.1 over 48 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| clustered | 1 | 0.942 | 0.942 | 0.000 | - | - | 0.972 | 0.972 | 0.512 | 1.15x | 24.4/33.8/35.8% | 1.4/5.5% | 3 |
| corridor | 1 | 0.521 | 0.512 | 0.009 | - | - | 0.664 | 0.664 | 0.261 | 1.22x | 12.3/28.0/31.3% | 1.7/5.4% | 3 |
| hub | 1 | 0.965 | 0.964 | 0.001 | - | - | 0.994 | 0.994 | 0.846 | 1.25x | 27.3/37.5/39.3% | 1.7/5.7% | 3 |

> topology=clustered: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.858 | 0.858 | 0.000 | - | - | 0.953 | 0.956 | 0.385 | 1.46x | 19.3/33.1/37.1% | 2.0/6.4% | 3 |
| True | 1 | 0.850 | 0.850 | 0.000 | - | - | 0.956 | 0.958 | 0.370 | 1.48x | 19.4/33.5/37.6% | 2.1/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.850 | 0.850 | 0.000 | - | - | 0.956 | 0.958 | 0.370 | 1.48x | 19.4/33.5/37.6% | 2.1/6.5% | 3 |
| m4-early-flood | 1 | 0.859 | 0.859 | 0.000 | - | - | 0.953 | 0.955 | 0.370 | 1.46x | 19.2/33.0/37.1% | 2.1/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.878 | 0.878 | 0.000 | - | - | 0 | 0.000 | 0.421 | 1.24x | 16.2/27.7/31.2% | 1.8/5.3% | 3 |
| chain | 1 | 0.870 | 0.868 | 0.002 | - | - | 0.934 | 0.959 | 0.375 | 1.44x | 19.0/32.5/36.3% | 2.0/6.1% | 3 |
| sr | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| True | 1 | 0.888 | 0.884 | 0.005 | - | - | 0.970 | 0.970 | 0.449 | 1.26x | 16.4/28.0/31.5% | 1.8/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.962 | 0.002 | - | - | 1.000 | 1.000 | 0.773 | 1.96x | 23.8/37.1/41.0% | 1.3/5.1% | 3 |
| True | 1 | 0.963 | 0.961 | 0.002 | - | - | 0.998 | 0.998 | 0.784 | 2.00x | 24.2/37.7/41.6% | 1.4/5.1% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.275 | 0.258 | 0.017 | - | - | 0.561 | 0.567 | 0.000 | 0.06x | 0.3/0.7/0.9% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.543 | 0.531 | 0.012 | - | - | 0.808 | 0.810 | 0.000 | 0.28x | 2.1/4.7/6.1% | 0.3/1.3% | 3 |
| LONG_TURBO | 1 | 0.789 | 0.784 | 0.005 | - | - | 0.916 | 0.917 | 0.251 | 1.21x | 13.0/23.4/26.5% | 1.7/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.971 | 0.971 | 0.560 | 1.06x | 18.3/28.7/32.1% | 1.4/5.2% | 3 |
| 1.0 | 1 | 0.943 | 0.938 | 0.004 | - | - | 0.985 | 0.985 | 0.738 | 0.89x | 21.9/30.3/33.3% | 1.0/5.3% | 3 |

> duct-per-hour=1.0: misdecodes 1

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.398 | 0.384 | 0.015 | - | - | 0.595 | 0.634 | 0.000 | 0.14x | 1.0/2.1/3.0% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| LITE_FAST | 1 | 0.832 | 0.827 | 0.005 | - | - | 0.948 | 0.948 | 0.178 | 0.95x | 11.9/21.4/24.7% | 1.4/4.1% | 3 |
| NARROW_SLOW | 1 | 0.854 | 0.850 | 0.004 | - | - | 0.955 | 0.956 | 0.337 | 1.21x | 15.2/26.6/30.5% | 1.6/5.2% | 3 |

> preset=SHORT_FAST: decode_failures 19

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| temporal | 1 | 0.804 | 0.799 | 0.005 | - | - | 0.932 | 0.934 | 0.171 | 1.23x | 16.1/27.0/30.6% | 1.8/5.1% | 3 |
| transient | 1 | 0.872 | 0.868 | 0.005 | - | - | 0.954 | 0.955 | 0.400 | 1.25x | 16.2/27.8/31.4% | 1.8/5.3% | 3 |
| periodic | 1 | 0.722 | 0.716 | 0.006 | - | - | 0.805 | 0.806 | 0.306 | 1.16x | 15.4/25.3/28.7% | 1.7/4.6% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.398 | 0.384 | 0.015 | - | - | 0.595 | 0.634 | 0.000 | 0.14x | 1.0/2.1/3.0% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| LONG_MODERATE | 1 | 0.817 | 0.805 | 0.012 | - | - | 0.914 | 0.914 | 0.598 | 3.27x | 50.1/69.7/71.3% | 4.9/12.4% | 3 |

> preset=SHORT_FAST: decode_failures 19

> preset=LONG_MODERATE: decode_failures 1

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.086 | 0.086 | 0.000 | - | - | 0.088 | 0.090 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.275 | 0.258 | 0.017 | - | - | 0.561 | 0.567 | 0.000 | 0.06x | 0.3/0.7/0.9% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| LONG_TURBO | 1 | 0.789 | 0.784 | 0.005 | - | - | 0.916 | 0.917 | 0.251 | 1.21x | 13.0/23.4/26.5% | 1.7/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.860 | 0.854 | 0.006 | - | - | 0.946 | 0.947 | 0.424 | 1.74x | 22.2/36.6/40.2% | 2.6/7.0% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.825 | 0.819 | 0.006 | - | - | 0.912 | 0.912 | 0.363 | 1.23x | 16.3/27.6/31.1% | 1.7/5.1% | 3 |
| 10000 | 1 | 0.722 | 0.716 | 0.006 | - | - | 0.805 | 0.806 | 0.306 | 1.16x | 15.4/25.3/28.7% | 1.7/4.6% | 3 |
| 4000 | 1 | 0.462 | 0.458 | 0.004 | - | - | 0.518 | 0.576 | 0.151 | 1.00x | 13.5/21.7/24.9% | 1.5/3.6% | 3 |
| 2000 | 1 | 0.103 | 0.103 | 0.000 | - | - | 0.107 | 0.181 | 0.025 | 0.70x | 9.7/15.1/18.2% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 4

> faster: 0.819 s per simulated hour against 1.67 over 48 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.408 | 0.402 | 0.007 | - | - | 0.674 | 0.676 | 0.000 | 1.17x | 9.6/16.6/23.5% | 1.7/4.9% | 3 |
| 1.0 | 1 | 0.716 | 0.706 | 0.010 | - | - | 0.848 | 0.852 | 0.497 | 0.90x | 15.6/20.7/25.0% | 1.2/4.5% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 22 | 1 | 0.517 | 0.503 | 0.014 | - | - | 0.766 | 0.773 | 0.000 | 1.29x | 10.4/20.2/26.6% | 1.8/5.3% | 3 |
| 17 | 1 | 0.242 | 0.232 | 0.011 | - | - | 0.439 | 0.457 | 0.000 | 1.19x | 7.0/14.3/16.0% | 1.9/4.3% | 3 |
| 14 | 1 | 0.130 | 0.127 | 0.002 | - | - | 0.232 | 0.241 | 0.000 | 0.80x | 3.9/8.4/10.9% | 1.2/3.1% | 3 |

> tx-power=17: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.962 | 0.002 | - | - | 1.000 | 1.000 | 0.773 | 1.96x | 23.8/37.1/41.0% | 1.3/5.1% | 3 |
| True | 1 | 0.957 | 0.954 | 0.003 | - | - | 0.998 | 0.998 | 0.751 | 2.40x | 28.4/43.3/46.9% | 1.6/5.8% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

> no-adopt-hop-recommendation=True: decode_failures 1

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.891 | 0.887 | 0.004 | - | - | 0.971 | 0.971 | 0.363 | 1.38x | 17.9/34.4/38.5% | 1.9/5.3% | 3 |
| True | 1 | 0.911 | 0.907 | 0.004 | - | - | 0.967 | 0.967 | 0.474 | 1.46x | 18.6/34.1/38.2% | 2.1/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| random | 1 | 0.876 | 0.871 | 0.006 | - | - | 0.957 | 0.961 | 0.506 | 1.27x | 16.7/28.1/31.6% | 1.8/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.734 | 0.715 | 0.019 | - | - | 0.912 | 0.913 | 0.213 | 0.99x | 13.2/24.7/27.9% | 1.4/5.1% | 3 |
| 7 | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.973 | 0.973 | 0.626 | 1.40x | 18.0/29.1/32.9% | 1.9/5.5% | 3 |
| 15 | 1 | 0.936 | 0.935 | 0.002 | - | - | 0.973 | 0.973 | 0.657 | 1.41x | 18.3/29.1/33.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.936 | 0.935 | 0.002 | - | - | 0.973 | 0.973 | 0.657 | 1.41x | 18.3/29.1/33.0% | 2.0/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.734 | 0.715 | 0.019 | - | - | 0.912 | 0.913 | 0.213 | 0.99x | 13.2/24.7/27.9% | 1.4/5.1% | 3 |
| 5 | 1 | 0.888 | 0.881 | 0.006 | - | - | 0.957 | 0.959 | 0.495 | 1.28x | 16.5/28.0/31.7% | 1.8/5.3% | 3 |
| 7 | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.973 | 0.973 | 0.626 | 1.40x | 18.0/29.1/32.9% | 1.9/5.5% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.872 | 0.872 | 0.000 | - | - | 0.920 | 0.965 | 0.415 | 1.21x | 15.8/26.8/30.3% | 1.7/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.734 | 0.715 | 0.019 | - | - | 0.912 | 0.913 | 0.213 | 0.99x | 13.2/24.7/27.9% | 1.4/5.1% | 3 |
| True | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| BALANCED | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| STRICT | 1 | 0.754 | 0.754 | 0.000 | - | - | 0.836 | 0.836 | 0.270 | 1.31x | 17.0/28.5/32.3% | 1.9/5.3% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| dm | 1 | 0.883 | 0.877 | 0.006 | - | - | 0.970 | 0.970 | 0.404 | 1.24x | 16.4/27.7/31.0% | 1.8/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.881 | 0.876 | 0.005 | - | - | 0.966 | 0.967 | 0.401 | 1.27x | 16.6/28.3/31.9% | 1.8/5.4% | 3 |
| local | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| time | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.973 | 0.973 | 0.427 | 1.30x | 17.2/28.9/32.3% | 1.8/5.4% | 3 |
| window | 1 | 0.885 | 0.881 | 0.004 | - | - | 0.968 | 0.968 | 0.427 | 1.26x | 16.4/28.1/31.6% | 1.8/5.3% | 3 |

> bucket-mode=global: misdecodes 35

> bucket-mode=time: misdecodes 48

> bucket-mode=window: misdecodes 23

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.874 | 0.868 | 0.005 | - | - | 0.963 | 0.964 | 0.412 | 1.40x | 18.5/31.0/34.5% | 1.9/5.9% | 3 |
| 1800 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.973 | 0.973 | 0.427 | 1.30x | 17.2/28.9/32.3% | 1.8/5.4% | 3 |
| 3600 | 1 | 0.879 | 0.874 | 0.005 | - | - | 0.964 | 0.964 | 0.388 | 1.24x | 16.2/27.5/30.9% | 1.8/5.2% | 3 |

> time-bucket-s=600: misdecodes 120

> time-bucket-s=1800: misdecodes 48

> time-bucket-s=3600: misdecodes 17

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| interval | 1 | 0.868 | 0.862 | 0.006 | - | - | 0.957 | 0.966 | 0.390 | 1.71x | 23.4/38.3/42.1% | 2.4/7.7% | 3 |
| aimd | 1 | 0.874 | 0.872 | 0.002 | - | - | 0.932 | 0.963 | 0.391 | 1.28x | 16.7/28.5/32.0% | 1.8/5.4% | 3 |
| bucket+interval | 1 | 0.852 | 0.844 | 0.008 | - | - | 0.952 | 0.954 | 0.368 | 1.74x | 23.6/39.2/43.0% | 2.4/8.1% | 3 |

> trigger=interval: misdecodes 21

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 26

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.970 | 0.971 | 0.439 | 1.24x | 16.3/27.7/31.1% | 1.8/5.2% | 3 |
| 8 | 1 | 0.881 | 0.876 | 0.005 | - | - | 0.970 | 0.970 | 0.410 | 1.23x | 16.2/27.5/30.9% | 1.7/5.2% | 3 |
| 16 | 1 | 0.879 | 0.874 | 0.005 | - | - | 0.965 | 0.966 | 0.411 | 1.25x | 16.4/27.8/31.4% | 1.8/5.3% | 3 |
| 32 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 50 | 1 | 0.882 | 0.877 | 0.005 | - | - | 0.966 | 0.966 | 0.397 | 1.26x | 16.7/28.1/31.6% | 1.8/5.3% | 3 |

> capacity=4: decode_failures 55

> capacity=8: decode_failures 7

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.885 | 0.879 | 0.006 | - | - | 0.970 | 0.971 | 0.439 | 1.24x | 16.3/27.7/31.1% | 1.8/5.2% | 3 |
| 8 | 1 | 0.881 | 0.876 | 0.005 | - | - | 0.970 | 0.970 | 0.410 | 1.23x | 16.2/27.5/30.9% | 1.7/5.2% | 3 |
| 16 | 1 | 0.879 | 0.874 | 0.005 | - | - | 0.965 | 0.966 | 0.411 | 1.25x | 16.4/27.8/31.4% | 1.8/5.3% | 3 |
| 32 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 50 | 1 | 0.882 | 0.877 | 0.005 | - | - | 0.966 | 0.966 | 0.397 | 1.26x | 16.7/28.1/31.6% | 1.8/5.3% | 3 |

> capacity=4: decode_failures 55

> capacity=8: decode_failures 7

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.873 | 0.868 | 0.005 | - | - | 0.955 | 0.964 | 0.388 | 1.24x | 16.3/27.8/31.3% | 1.8/5.3% | 3 |
| 16 | 1 | 0.876 | 0.872 | 0.004 | - | - | 0.959 | 0.961 | 0.385 | 1.24x | 16.3/27.7/31.2% | 1.8/5.2% | 3 |
| 32 | 1 | 0.885 | 0.881 | 0.004 | - | - | 0.968 | 0.968 | 0.427 | 1.26x | 16.4/28.1/31.6% | 1.8/5.3% | 3 |

> capacity=8: misdecodes 26

> capacity=8: decode_failures 13

> capacity=16: misdecodes 16

> capacity=32: misdecodes 23

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.852 | 0.844 | 0.008 | - | - | 0.952 | 0.954 | 0.368 | 1.74x | 23.6/39.2/43.0% | 2.4/8.1% | 3 |
| 02-06 | 1 | 0.888 | 0.886 | 0.003 | - | - | 0.959 | 0.975 | 0.408 | 1.29x | 16.9/28.7/32.3% | 1.8/5.4% | 3 |
| 00-08 | 1 | 0.877 | 0.875 | 0.003 | - | - | 0.947 | 0.964 | 0.397 | 1.34x | 17.7/30.0/33.6% | 1.9/5.6% | 3 |

> catch-up-hours=: misdecodes 26

> catch-up-hours=02-06: decode_failures 7

> catch-up-hours=00-08: decode_failures 7

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.870 | 0.870 | 0.000 | - | - | 0.944 | 0.944 | 0.395 | 1.26x | 16.3/28.0/31.6% | 1.8/5.3% | 3 |
| 2 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 3 | 1 | 0.897 | 0.878 | 0.020 | - | - | 0.995 | 0.996 | 0.435 | 1.25x | 16.3/27.8/31.3% | 1.8/5.3% | 3 |
| 4 | 1 | 0.905 | 0.882 | 0.023 | - | - | 0.961 | 0.972 | 0.434 | 1.27x | 16.4/28.2/31.9% | 1.8/5.4% | 3 |

> faster: 1.83 s per simulated hour against 3.92 over 48 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.870 | 0.870 | 0.000 | - | - | 0.944 | 0.944 | 0.395 | 1.26x | 16.3/28.0/31.6% | 1.8/5.3% | 3 |
| 2 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 3 | 1 | 0.897 | 0.878 | 0.020 | - | - | 0.995 | 0.996 | 0.435 | 1.25x | 16.3/27.8/31.3% | 1.8/5.3% | 3 |
| 4 | 1 | 0.905 | 0.882 | 0.023 | - | - | 0.961 | 0.972 | 0.434 | 1.27x | 16.4/28.2/31.9% | 1.8/5.4% | 3 |
| 5 | 1 | 0.901 | 0.882 | 0.018 | - | - | 0.972 | 0.974 | 0.421 | 1.25x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

> faster: 1.99 s per simulated hour against 4.72 over 48 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.965 | 0.965 | 0.399 | 1.26x | 16.5/28.1/31.5% | 1.8/5.3% | 3 |
| 30 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 120 | 1 | 0.878 | 0.872 | 0.006 | - | - | 0.965 | 0.966 | 0.422 | 1.25x | 16.4/27.9/31.4% | 1.8/5.3% | 3 |
| 600 | 1 | 0.886 | 0.881 | 0.004 | - | - | 0.973 | 0.974 | 0.420 | 1.24x | 16.2/27.6/31.0% | 1.8/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.965 | 0.965 | 0.399 | 1.26x | 16.5/28.1/31.5% | 1.8/5.3% | 3 |
| 30 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 120 | 1 | 0.878 | 0.872 | 0.006 | - | - | 0.965 | 0.966 | 0.422 | 1.25x | 16.4/27.9/31.4% | 1.8/5.3% | 3 |
| 600 | 1 | 0.886 | 0.881 | 0.004 | - | - | 0.973 | 0.974 | 0.420 | 1.24x | 16.2/27.6/31.0% | 1.8/5.2% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.904 | 0.885 | 0.019 | - | - | 0.890 | 0.980 | 0.406 | 1.28x | 17.1/28.2/32.0% | 1.8/5.4% | 3 |
| routers | 1 | 0.870 | 0.870 | 0.001 | - | - | 0.945 | 0.945 | 0.408 | 1.27x | 16.6/28.6/32.2% | 1.8/5.4% | 3 |
| alternate-routers | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.955 | 0.956 | 0.433 | 1.25x | 16.4/28.2/31.7% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.875 | 0.874 | 0.000 | - | - | 0.947 | 0.947 | 0.391 | 1.25x | 16.4/28.1/31.7% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.970 | 0.970 | 0.412 | 1.26x | 16.6/28.2/31.7% | 1.8/5.3% | 3 |
| hops-apart | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

> place=spread: decode_failures 41

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.904 | 0.885 | 0.019 | - | - | 0.890 | 0.980 | 0.406 | 1.28x | 17.1/28.2/32.0% | 1.8/5.4% | 3 |
| routers | 1 | 0.870 | 0.870 | 0.001 | - | - | 0.945 | 0.945 | 0.408 | 1.27x | 16.6/28.6/32.2% | 1.8/5.4% | 3 |
| alternate-routers | 1 | 0.879 | 0.877 | 0.002 | - | - | 0.955 | 0.956 | 0.433 | 1.25x | 16.4/28.2/31.7% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.875 | 0.874 | 0.000 | - | - | 0.947 | 0.947 | 0.391 | 1.25x | 16.4/28.1/31.7% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.970 | 0.970 | 0.412 | 1.26x | 16.6/28.2/31.7% | 1.8/5.3% | 3 |
| hops-apart | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

> place=spread: decode_failures 41

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| broadcast | 1 | 0.900 | 0.880 | 0.020 | - | - | 0.967 | 0.967 | 0.445 | 1.29x | 17.0/28.5/32.0% | 1.8/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| heard | 1 | 0.879 | 0.874 | 0.006 | - | - | 0.969 | 0.971 | 0.403 | 1.27x | 16.6/28.3/31.8% | 1.8/5.4% | 3 |

> replay-ordering=heard: misdecodes 14

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.900 | 0.880 | 0.020 | - | - | 0.967 | 0.967 | 0.445 | 1.29x | 17.0/28.5/32.0% | 1.8/5.4% | 3 |
| heard | 1 | 0.892 | 0.871 | 0.022 | - | - | 0.960 | 0.961 | 0.423 | 1.29x | 17.0/28.7/32.1% | 1.8/5.4% | 3 |

> replay-ordering=heard: misdecodes 21

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| enum | 1 | 0.883 | 0.878 | 0.005 | - | - | 0.961 | 0.962 | 0.421 | 1.25x | 16.5/28.0/31.3% | 1.7/5.3% | 3 |
| hybrid | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.870 | 0.870 | 0.001 | - | - | 0.945 | 0.945 | 0.408 | 1.27x | 16.6/28.6/32.2% | 1.8/5.4% | 3 |
| 6 | 1 | 0.874 | 0.872 | 0.002 | - | - | 0.950 | 0.951 | 0.398 | 1.28x | 16.6/28.7/32.2% | 1.8/5.5% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.882 | 0.881 | 0.001 | - | - | 0.955 | 0.955 | 0.411 | 1.24x | 16.2/27.6/31.1% | 1.8/5.2% | 2 |
| 3 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 5 | 1 | 0.884 | 0.878 | 0.006 | - | - | 0.974 | 0.974 | 0.422 | 1.29x | 16.8/28.5/32.1% | 1.9/5.4% | 5 |
| 8 | 1 | 0.881 | 0.872 | 0.009 | - | - | 0.971 | 0.972 | 0.412 | 1.33x | 17.5/29.4/32.8% | 1.9/5.5% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.882 | 0.881 | 0.001 | - | - | 0.955 | 0.955 | 0.411 | 1.24x | 16.2/27.6/31.1% | 1.8/5.2% | 2 |
| 3 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 5 | 1 | 0.884 | 0.878 | 0.006 | - | - | 0.974 | 0.974 | 0.422 | 1.29x | 16.8/28.5/32.1% | 1.9/5.4% | 5 |
| 8 | 1 | 0.881 | 0.872 | 0.009 | - | - | 0.971 | 0.972 | 0.412 | 1.33x | 17.5/29.4/32.8% | 1.9/5.5% | 8 |

> servers=8: misdecodes 1

> faster: 1.1 s per simulated hour against 2.32 over 48 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| True | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.873 | 0.868 | 0.005 | - | - | 0.953 | 0.953 | 0.406 | 1.16x | 15.2/26.1/29.4% | 1.6/4.9% | 3 |
| 1 | 1 | 0.887 | 0.883 | 0.004 | - | - | 0.966 | 0.966 | 0.441 | 1.15x | 14.9/25.6/28.7% | 1.7/4.9% | 3 |
| 2 | 1 | 0.885 | 0.881 | 0.004 | - | - | 0.961 | 0.962 | 0.437 | 1.16x | 15.0/25.7/28.9% | 1.6/4.9% | 3 |
| 4 | 1 | 0.888 | 0.885 | 0.004 | - | - | 0.965 | 0.965 | 0.421 | 1.15x | 15.0/25.9/29.1% | 1.6/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.882 | 0.877 | 0.005 | - | - | 0.967 | 0.967 | 0.433 | 1.24x | 16.2/27.6/31.1% | 1.7/5.2% | 3 |
| 24 | 1 | 0.878 | 0.873 | 0.005 | - | - | 0.968 | 0.968 | 0.389 | 1.25x | 16.4/27.8/31.2% | 1.8/5.3% | 3 |
| 32 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.965 | 0.965 | 0.400 | 1.26x | 16.5/28.0/31.5% | 1.8/5.3% | 3 |
| 64 | 1 | 0.884 | 0.878 | 0.006 | - | - | 0.971 | 0.971 | 0.413 | 1.26x | 16.6/28.0/31.4% | 1.8/5.3% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.874 | 0.868 | 0.006 | - | - | 0.961 | 0.962 | 0.400 | 1.33x | 17.5/29.8/33.4% | 1.9/5.6% | 3 |
| 16 | 1 | 0.876 | 0.870 | 0.006 | - | - | 0.963 | 0.963 | 0.415 | 1.29x | 16.9/28.6/32.2% | 1.8/5.4% | 3 |
| 32 | 1 | 0.885 | 0.881 | 0.004 | - | - | 0.968 | 0.968 | 0.427 | 1.26x | 16.4/28.1/31.6% | 1.8/5.3% | 3 |

> window-size=8: misdecodes 111

> window-size=16: misdecodes 56

> window-size=32: misdecodes 23

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.962 | 0.002 | - | - | 1.000 | 1.000 | 0.773 | 1.96x | 23.8/37.1/41.0% | 1.3/5.1% | 3 |
| True | 1 | 0.758 | 0.750 | 0.009 | - | - | 0.862 | 0.908 | 0.498 | 5.47x | 60.4/75.3/78.6% | 4.1/12.6% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: queue drops 14.9% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 102

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.552 | 0.540 | 0.012 | - | - | 0.802 | 0.817 | 0.155 | 4.92x | 16.6/31.3/42.2% | 1.7/6.0% | 3 |
| truesize | 1 | 0.588 | 0.576 | 0.012 | - | - | 0.837 | 0.843 | 0.153 | 3.67x | 12.2/25.4/34.3% | 1.2/5.1% | 3 |

> congestion-input=hotstore: decode_failures 86

> congestion-input=truesize: decode_failures 71

> slower: 44.4 s per simulated hour against 10.8 over 48 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.964 | 0.962 | 0.002 | - | - | 0.999 | 0.999 | 0.779 | 1.91x | 23.0/36.0/39.6% | 1.3/4.8% | 3 |
| adaptive | 1 | 0.964 | 0.962 | 0.002 | - | - | 1.000 | 1.000 | 0.773 | 1.96x | 23.8/37.1/41.0% | 1.3/5.1% | 3 |

> congestion-mode=adaptive: misdecodes 1

