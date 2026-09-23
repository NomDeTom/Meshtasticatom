# Sweep blocks-2026-09-23-5641980

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** coastal
- **seed base** 5641980 · seeds 5641980
- **blocks** 87 run
- **compute** 13.4 h of simulator time across every cell
- **generated** 2026-09-23T09:42:56+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>84 warnings</summary>

- DB-hotstore: max-num-nodes=10: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 54
- DB-hotstore-stress: max-num-nodes=120: decode_failures 77
- DB-hotstore-stress: max-num-nodes=250: decode_failures 65
- DB-warm: warm-num-nodes=0: queue drops 25.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 110
- DB-warm: warm-num-nodes=25: queue drops 25.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 110
- DB-warm: warm-num-nodes=100: queue drops 25.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 110
- DB-warm: warm-num-nodes=2000: queue drops 25.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 110
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 7
- DG-burst: burst-loss=0.3: decode_failures 35
- DG-loss: extra-loss=0.1: decode_failures 2
- DG-loss: extra-loss=0.3: decode_failures 3
- DG-outage: burst-loss=0.1: decode_failures 59
- DG-outage: burst-loss=0.2: decode_failures 40
- DG-outage: burst-loss=0.3: decode_failures 30
- LD-chatty-hops: broadcast-interval-s=300: queue drops 16.4% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 32
- LD-chatty: broadcast-interval-s=300: queue drops 11.1% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 46
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 25.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 110
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 37.7% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 113
- MS-density: nodes=90: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 143
- MS-hopscale: nodes=500: decode_failures 323
- MS-hopscale: slower: 44.6 s per simulated hour against 18 over 33 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-oversubscribed: nodes=250: decode_failures 77
- MS-oversubscribed: nodes=500: decode_failures 129
- MS-stretch: stretch=1.25: decode_failures 3
- MS-stretch: stretch=2.0: decode_failures 16
- RF-bw500: preset=SHORT_TURBO: decode_failures 8
- RF-eu-presets: preset=SHORT_FAST: decode_failures 9
- RF-noise: noise-profile=temporal: decode_failures 2
- RF-preset: preset=SHORT_FAST: decode_failures 9
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 8
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 8
- RF-txpower: tx-power=22: decode_failures 1
- RF-txpower: tx-power=17: decode_failures 18
- RF-txpower: tx-power=14: decode_failures 5
- RT-hoplimit: hop-limit=3: decode_failures 3
- RT-hopspread: hop-limit=3: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 3
- SC-signing: signature-policy=STRICT: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 37
- SF-bucket-mode: bucket-mode=time: misdecodes 32
- SF-bucket-mode: bucket-mode=window: misdecodes 30
- SF-bucket-time: time-bucket-s=600: misdecodes 113
- SF-bucket-time: time-bucket-s=1800: misdecodes 32
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-cadence: trigger=interval: misdecodes 20
- SF-cadence: trigger=interval: decode_failures 5
- SF-cadence: trigger=aimd: misdecodes 5
- SF-cadence: trigger=bucket+interval: misdecodes 11
- SF-capacity-local: capacity=4: decode_failures 83
- SF-capacity-local: capacity=8: decode_failures 99
- SF-capacity: capacity=4: decode_failures 83
- SF-capacity: capacity=8: decode_failures 99
- SF-capacity-window: capacity=8: misdecodes 35
- SF-capacity-window: capacity=8: decode_failures 13
- SF-capacity-window: capacity=16: misdecodes 21
- SF-capacity-window: capacity=32: misdecodes 30
- SF-catchup: catch-up-hours=: misdecodes 11
- SF-catchup: catch-up-hours=02-06: decode_failures 22
- SF-catchup: catch-up-hours=00-08: decode_failures 20
- SF-hops-flat: faster: 1.8 s per simulated hour against 3.65 over 33 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: faster: 2.08 s per simulated hour against 4.52 over 33 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=spread: decode_failures 22
- SF-place-spread: place=spread: decode_failures 22
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 6
- SF-replay-order: replay-ordering=heard: misdecodes 23
- SF-window-size: window-size=8: misdecodes 171
- SF-window-size: window-size=16: misdecodes 63
- SF-window-size: window-size=32: misdecodes 30
- TH-congestion-input: congestion-input=hotstore: decode_failures 77
- TH-congestion-input: congestion-input=truesize: decode_failures 36
- TH-congestion-input: slower: 36.7 s per simulated hour against 10.5 over 33 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: queue drops 22.6% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 94

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 36.7 | 10.5 | 3.48x | 33 |
| `MS-hopscale` | 44.6 | 18 | 2.47x | 33 |
| `DB-hotstore-stress` | 41.4 | 22.6 | 1.83x | 33 |
| `RF-txpower` | 2.86 | 1.59 | 1.80x | 33 |
| `MS-oversubscribed` | 34.8 | 19.7 | 1.76x | 33 |
| `SF-resolve` | 2.44 | 1.53 | 1.59x | 33 |
| `DG-outage` | 10.8 | 6.97 | 1.55x | 33 |
| `LD-chatty` | 7.66 | 4.97 | 1.54x | 33 |
| `LD-chatty-hops` | 6.54 | 4.32 | 1.51x | 33 |
| `RF-noise` | 3.4 | 5.27 | 0.65x | 33 |
| `SF-signed` | 1.12 | 1.74 | 0.64x | 33 |
| `SF-catchup` | 5.91 | 9.35 | 0.63x | 33 |
| `MS-density` | 1.9 | 3.49 | 0.55x | 33 |
| `RF-stretch-duct` | 1.03 | 2 | 0.52x | 33 |
| `SF-hops-flat` | 1.8 | 3.65 | 0.49x | 33 |
| `SF-hops-spread` | 2.08 | 4.52 | 0.46x | 33 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.990 | 0.990 | 0.907 → 0.922 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.983 | 0.983 | 0.910 → 0.914 | 1x bytes_on_air | up | 2 |
| `AD-siting` | siting-mix | **held** | 0.036 → 0.987 | 0.951 | 0.021 → 0.890 | 91x sr_bytes | down | 3 |
| `RF-preset-turbo` | preset | **held** | 0.076 → 0.990 | 0.914 | 0.045 → 0.922 | 26x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **text** | 0.101 → 0.929 | 0.827 | 0.099 → 0.922 | 5.3x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.132 → 0.941 | 0.809 | 0.131 → 0.865 | 1e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.248 → 0.929 | 0.680 | 0.242 → 0.922 | 2.1x advert_bytes | down | 4 |
| `MS-hopscale` | nodes | **text** | 0.335 → 0.929 | 0.594 | 0.325 → 0.922 | 19x sr_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.315 → 0.875 | 0.560 | 0.308 → 0.869 | 1.7x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **text** | 0.334 → 0.831 | 0.497 | 0.324 → 0.823 | 6.9x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.561 → 0.975 | 0.414 | 0.555 → 0.975 | 2.2x sr_bytes | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.543 → 0.929 | 0.386 | 0.536 → 0.922 | 2.5x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.543 → 0.929 | 0.386 | 0.536 → 0.922 | 2.8x sr_airtime | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.586 → 0.954 | 0.368 | 0.577 → 0.953 | 8.4x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.595 → 0.960 | 0.366 | 0.578 → 0.959 | 2.3x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.540 → 0.892 | 0.352 | 0.350 → 0.574 | 6.1x sr_airtime | up | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.626 → 0.935 | 0.310 | 0.612 → 0.932 | 7.5x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.622 → 0.929 | 0.307 | 0.599 → 0.922 | 2.2x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.635 → 0.929 | 0.293 | 0.602 → 0.922 | 2.5x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.565 → 0.792 | 0.227 | 0.550 → 0.777 | 1.6x sr_airtime | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.757 → 0.970 | 0.213 | 0.752 → 0.969 | 4.2x sr_airtime | down | 2 |
| `MS-density` | nodes | **text** | 0.813 → 0.975 | 0.162 | 0.800 → 0.974 | 4.4x sr_airtime | up | 5 |
| `MS-size` | nodes | **text** | 0.769 → 0.929 | 0.160 | 0.752 → 0.922 | 6.3x sr_bytes | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.799 → 0.953 | 0.154 | 0.768 → 0.951 | 2.4x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.799 → 0.942 | 0.143 | 0.768 → 0.940 | 2.2x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.794 → 0.929 | 0.134 | 0.788 → 0.922 | 1.4x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.799 → 0.929 | 0.130 | 0.768 → 0.922 | 2.2x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.815 → 0.929 | 0.113 | 0.815 → 0.922 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.822 → 0.929 | 0.107 | 0.806 → 0.922 | 1.6x sr_bytes | down | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.640 → 0.730 | 0.090 | 0.637 → 0.726 | 1.4x sr_airtime | down | 2 |
| `DB-hotstore` | max-num-nodes | **text** | 0.863 → 0.945 | 0.082 | 0.854 → 0.943 | 2.5x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.863 → 0.945 | 0.082 | 0.854 → 0.943 | 2.4x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.887 → 0.953 | 0.066 | 0.873 → 0.951 | 5.4x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.902 → 0.960 | 0.058 | 0.890 → 0.958 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.902 → 0.960 | 0.058 | 0.890 → 0.958 | 2.6x bytes_on_air | up | 3 |
| `SF-place-flat` | place | **held** | 0.937 → 0.990 | 0.053 | 0.912 → 0.922 | 2.8x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.937 → 0.990 | 0.053 | 0.912 → 0.922 | 2.8x sr_bytes | up | 6 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.939 → 0.990 | 0.051 | 0.920 → 0.922 | 27x sr_airtime | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.929 → 0.972 | 0.043 | 0.922 → 0.971 | 1.5x bytes_on_air | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.886 → 0.929 | 0.042 | 0.873 → 0.922 | 1.5x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.947 → 0.990 | 0.042 | 0.899 → 0.922 | 13x advert_bytes | down | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.929 → 0.969 | 0.040 | 0.922 → 0.967 | 1.6x bytes_on_air | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.885 → 0.918 | 0.033 | 0.564 → 0.597 | 1.3x sr_airtime | up | 2 |
| `AD-badrouters` | role-placement | **text** | 0.872 → 0.902 | 0.030 | 0.856 → 0.890 | 1.3x sr_bytes | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.929 → 0.957 | 0.029 | 0.922 → 0.955 | 1.6x bytes_on_air | up | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.905 → 0.929 | 0.023 | 0.892 → 0.922 | 1.3x sr_airtime | down | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.963 → 0.985 | 0.022 | 0.899 → 0.920 | 9.6x advert_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.969 → 0.991 | 0.022 | 0.911 → 0.922 | 6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.969 → 0.991 | 0.022 | 0.911 → 0.922 | 6x sr_bytes | up | 4 |
| `MS-roles` | role-mix | **text** | 0.902 → 0.921 | 0.019 | 0.890 → 0.915 | 1.6x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.909 → 0.928 | 0.019 | 0.899 → 0.923 | 1.7x sr_bytes | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.932 → 0.950 | 0.017 | 0.930 → 0.949 | 1.1x bytes_on_air | up | 2 |
| `SF-hops-flat` | hops-apart | **text** | 0.911 → 0.929 | 0.017 | 0.909 → 0.922 | 1.9x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.911 → 0.929 | 0.017 | 0.909 → 0.922 | 1.9x sr_bytes | up | 5 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.913 → 0.929 | 0.016 | 0.906 → 0.922 | 2.4x advert_bytes | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.883 → 0.898 | 0.015 | 0.883 → 0.898 | 1.2x sr_airtime | up | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.929 → 0.944 | 0.015 | 0.922 → 0.941 | 3.3x bytes_on_air | down | 2 |
| `SF-capacity` | capacity | **held** | 0.979 → 0.993 | 0.015 | 0.910 → 0.925 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.979 → 0.993 | 0.015 | 0.910 → 0.925 | 5.3x advert_bytes | up | 5 |
| `FW-mixed` | legacy-fraction | **text** | 0.929 → 0.941 | 0.013 | 0.922 → 0.940 | 2.2x bytes_on_air | up | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.929 → 0.941 | 0.013 | 0.922 → 0.939 | 1.3x bytes_on_air | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.917 → 0.929 | 0.011 | 0.911 → 0.922 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.917 → 0.929 | 0.011 | 0.911 → 0.922 | 1.2x sr_airtime | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.977 → 0.988 | 0.011 | 0.910 → 0.921 | 2.6x sr_bytes | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.926 → 0.937 | 0.011 | 0.922 → 0.934 | 2.2x bytes_on_air | up | 4 |
| `AD-worst` | role-placement | **text** | 0.816 → 0.826 | 0.010 | 0.806 → 0.821 | 1.1x sr_bytes | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.929 → 0.938 | 0.009 | 0.913 → 0.922 | 2.6x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.893 → 0.902 | 0.009 | 0.893 → 0.902 | 1.1x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.929 → 0.937 | 0.008 | 0.922 → 0.933 | 1.4x sr_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.982 → 0.990 | 0.008 | 0.916 → 0.922 | 5.8x advert_bytes | = | 3 |
| `FW-versions` | profile | **text** | 0.928 → 0.936 | 0.008 | 0.922 → 0.935 | 3.5x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **held** | 0.982 → 0.990 | 0.007 | 0.920 → 0.922 | 3.4x bytes_on_air | up | 2 |
| `SF-capacity-window` | capacity | **held** | 0.982 → 0.989 | 0.007 | 0.913 → 0.921 | 2.4x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.922 → 0.929 | 0.007 | 0.916 → 0.925 | 1.3x sr_bytes | down | 4 |
| `SF-width` | short-id-bits | **text** | 0.922 → 0.929 | 0.007 | 0.915 → 0.922 | 3.1x advert_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.922 → 0.929 | 0.007 | 0.914 → 0.922 | 3x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.922 → 0.929 | 0.007 | 0.915 → 0.922 | 1.2x sr_bytes | down | 2 |
| `SF-window-size` | window-size | **text** | 0.919 → 0.925 | 0.006 | 0.912 → 0.918 | 4.8x advert_bytes | up | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.917 → 0.922 | 0.006 | 0.910 → 0.915 | 5.4x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **text** | 0.924 → 0.929 | 0.005 | 0.918 → 0.922 | 1x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.898 → 0.902 | 0.004 | 0.898 → 0.902 | 1.2x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.970 → 0.973 | 0.003 | 0.969 → 0.972 | 1.1x bytes_on_air | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.968 → 0.970 | 0.002 | 0.967 → 0.969 | 1.2x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.936 → 0.938 | 0.001 | 0.911 → 0.913 | 1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.970 → 0.971 | 0.001 | 0.969 → 0.970 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| sprinkled | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.992 | 0.992 | 0.723 | 1.09x | 20.5/25.2/27.4% | 1.4/5.5% | 3 |
| arms-race | 1 | 0.969 | 0.967 | 0.002 | - | - | 0.994 | 0.994 | 0.777 | 0.91x | 22.4/26.4/28.7% | 0.9/5.5% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario coastal`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.953 | 0.950 | 0.003 | - | - | 0.997 | 0.998 | 0.887 | 1.21x | 21.2/27.0/31.6% | 1.6/4.9% | 3 |
| 0.3 | 1 | 0.972 | 0.971 | 0.001 | - | - | 1.000 | 1.000 | 0.894 | 0.95x | 24.7/30.1/33.3% | 1.1/5.3% | 3 |

### `AD-badrouters` - role-placement  `--scenario coastal`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.902 | 0.890 | 0.012 | - | - | 0.987 | 0.989 | 0.455 | 1.20x | 18.9/26.9/29.5% | 1.9/5.2% | 3 |
| inverse | 1 | 0.902 | 0.889 | 0.013 | - | - | 0.984 | 0.987 | 0.765 | 1.20x | 16.6/21.2/23.3% | 2.1/3.8% | 3 |
| random | 1 | 0.872 | 0.856 | 0.016 | - | - | 0.978 | 0.979 | 0.587 | 1.22x | 17.9/22.9/24.9% | 2.1/4.9% | 3 |

### `AD-flooding` - role-mix  `--scenario coastal`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.902 | 0.890 | 0.012 | - | - | 0.987 | 0.989 | 0.455 | 1.20x | 18.9/26.9/29.5% | 1.9/5.2% | 3 |
| all-routers | 1 | 0.960 | 0.958 | 0.002 | - | - | 0.991 | 0.991 | 0.867 | 3.06x | 40.4/48.5/50.5% | 5.0/5.4% | 3 |

### `AD-nomute` - role-mix  `--scenario coastal`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.902 | 0.890 | 0.012 | - | - | 0.987 | 0.989 | 0.455 | 1.20x | 18.9/26.9/29.5% | 1.9/5.2% | 3 |
| no-mute | 1 | 0.926 | 0.917 | 0.010 | - | - | 0.990 | 0.993 | 0.726 | 1.42x | 20.9/27.2/29.1% | 2.1/5.4% | 3 |
| all-routers | 1 | 0.960 | 0.958 | 0.002 | - | - | 0.991 | 0.991 | 0.867 | 3.06x | 40.4/48.5/50.5% | 5.0/5.4% | 3 |

### `AD-siting` - siting-mix  `--scenario coastal`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.902 | 0.890 | 0.012 | - | - | 0.987 | 0.989 | 0.455 | 1.20x | 18.9/26.9/29.5% | 1.9/5.2% | 3 |
| local-typical | 1 | 0.650 | 0.645 | 0.005 | - | - | 0.820 | 0.820 | 0.000 | 1.32x | 16.1/28.5/37.4% | 2.1/5.7% | 3 |
| basement-heavy | 1 | 0.021 | 0.021 | 0.000 | - | - | 0.036 | 0.036 | 0.000 | 0.32x | 0.2/3.1/5.8% | 0.2/1.9% | 3 |

### `AD-worst` - role-placement  `--scenario coastal`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.927 | 0.928 | 0.000 | 2.35x | 17.8/28.5/36.9% | 1.8/5.4% | 3 |
| inverse | 1 | 0.816 | 0.806 | 0.009 | - | - | 0.936 | 0.936 | 0.000 | 2.31x | 15.7/24.8/33.6% | 1.8/3.3% | 3 |

### `BL-control` - protocol  `--scenario coastal`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.914 | 0.914 | 0.000 | - | - | 0 | 0.000 | 0.677 | 1.42x | 21.3/27.6/30.2% | 2.0/5.3% | 3 |
| sr | 1 | 0.925 | 0.910 | 0.015 | - | - | 0.983 | 0.987 | 0.714 | 1.46x | 22.0/28.4/31.0% | 2.0/5.5% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario coastal`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.863 | 0.854 | 0.009 | - | - | 0.944 | 0.951 | 0.618 | 3.50x | 48.3/63.8/69.3% | 4.9/10.6% | 3 |
| 100 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.983 | 0.983 | 0.765 | 1.74x | 24.7/34.7/39.3% | 2.3/5.5% | 3 |
| 120 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.983 | 0.983 | 0.765 | 1.74x | 24.7/34.7/39.3% | 2.3/5.5% | 3 |
| 250 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.983 | 0.983 | 0.765 | 1.74x | 24.7/34.7/39.3% | 2.3/5.5% | 3 |

> max-num-nodes=10: decode_failures 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario coastal`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.356 | 0.350 | 0.006 | - | - | 0.540 | 0.700 | 0.126 | 11.60x | 43.4/60.1/74.7% | 4.1/11.3% | 3 |
| 120 | 1 | 0.577 | 0.564 | 0.012 | - | - | 0.885 | 0.901 | 0.171 | 4.51x | 17.2/29.1/42.2% | 1.5/6.1% | 3 |
| 250 | 1 | 0.585 | 0.574 | 0.011 | - | - | 0.892 | 0.911 | 0.176 | 4.41x | 16.7/28.0/40.3% | 1.4/5.9% | 3 |

> max-num-nodes=10: decode_failures 54

> max-num-nodes=120: decode_failures 77

> max-num-nodes=250: decode_failures 65

### `DB-platform` - platform-mix  `--scenario coastal`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.983 | 0.983 | 0.765 | 1.74x | 24.7/34.7/39.3% | 2.3/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.983 | 0.983 | 0.765 | 1.74x | 24.7/34.7/39.3% | 2.3/5.5% | 3 |
| constrained | 1 | 0.863 | 0.854 | 0.010 | - | - | 0.948 | 0.950 | 0.640 | 3.51x | 48.4/63.9/69.6% | 4.9/10.6% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario coastal`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.730 | 0.726 | 0.004 | - | - | 0.830 | 0.877 | 0.587 | 5.67x | 63.1/75.7/78.9% | 4.1/13.6% | 3 |
| 25 | 1 | 0.730 | 0.726 | 0.004 | - | - | 0.830 | 0.877 | 0.587 | 5.67x | 63.1/75.7/78.9% | 4.1/13.6% | 3 |
| 100 | 1 | 0.730 | 0.726 | 0.004 | - | - | 0.830 | 0.877 | 0.587 | 5.67x | 63.1/75.7/78.9% | 4.1/13.6% | 3 |
| 2000 | 1 | 0.730 | 0.726 | 0.004 | - | - | 0.830 | 0.877 | 0.587 | 5.67x | 63.1/75.7/78.9% | 4.1/13.6% | 3 |

> warm-num-nodes=0: queue drops 25.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 110

> warm-num-nodes=25: queue drops 25.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 110

> warm-num-nodes=100: queue drops 25.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 110

> warm-num-nodes=2000: queue drops 25.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 110

### `DG-burst` - burst-loss  `--scenario coastal`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.830 | 0.810 | 0.020 | - | - | 0.968 | 0.973 | 0.586 | 1.37x | 21.2/27.2/29.6% | 1.9/5.1% | 3 |
| 0.2 | 1 | 0.742 | 0.714 | 0.029 | - | - | 0.919 | 0.950 | 0.468 | 1.31x | 20.7/26.3/28.7% | 1.9/4.6% | 3 |
| 0.3 | 1 | 0.635 | 0.602 | 0.033 | - | - | 0.794 | 0.917 | 0.375 | 1.20x | 19.3/24.6/26.8% | 1.8/4.1% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 7

> burst-loss=0.3: decode_failures 35

### `DG-loss` - extra-loss  `--scenario coastal`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.895 | 0.886 | 0.009 | - | - | 0.972 | 0.976 | 0.630 | 1.50x | 23.0/29.0/31.7% | 2.1/5.3% | 3 |
| 0.2 | 1 | 0.871 | 0.861 | 0.010 | - | - | 0.968 | 0.971 | 0.591 | 1.59x | 24.4/30.6/33.2% | 2.3/5.3% | 3 |
| 0.3 | 1 | 0.822 | 0.806 | 0.016 | - | - | 0.944 | 0.962 | 0.507 | 1.60x | 24.8/31.4/33.7% | 2.4/5.1% | 3 |

> extra-loss=0.1: decode_failures 2

> extra-loss=0.3: decode_failures 3

### `DG-outage` - burst-loss  `--scenario coastal`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.1 | 1 | 0.816 | 0.805 | 0.011 | - | - | 0.907 | 0.978 | 0.561 | 1.38x | 21.3/27.0/29.6% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.724 | 0.703 | 0.021 | - | - | 0.867 | 0.966 | 0.403 | 1.32x | 20.6/26.6/28.7% | 1.9/4.8% | 3 |
| 0.3 | 1 | 0.622 | 0.599 | 0.023 | - | - | 0.734 | 0.898 | 0.423 | 1.22x | 19.4/25.0/26.7% | 1.9/4.4% | 3 |

> burst-loss=0.1: decode_failures 59

> burst-loss=0.2: decode_failures 40

> burst-loss=0.3: decode_failures 30

### `DM-mode` - dm-mode  `--scenario coastal`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.883 | 0.883 | 0.000 | - | - | 0.972 | 0.976 | 0.669 | 1.93x | 29.0/37.2/40.5% | 2.7/7.3% | 3 |
| directed-with-late-flood | 1 | 0.898 | 0.898 | 0.000 | - | - | 0.975 | 0.983 | 0.685 | 1.78x | 27.1/34.6/37.7% | 2.5/6.8% | 3 |
| m4-early-flood | 1 | 0.891 | 0.891 | 0.000 | - | - | 0.970 | 0.978 | 0.675 | 1.80x | 27.4/35.0/38.2% | 2.5/6.9% | 3 |

### `FW-firmware` - profile  `--scenario coastal`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.982 | 0.983 | 0.387 | 0.77x | 10.3/12.8/14.8% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario coastal`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.929 | 0.925 | 0.004 | - | - | 0.984 | 0.986 | 0.800 | 1.24x | 16.1/21.4/23.0% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.941 | 0.940 | 0.002 | - | - | 0.990 | 0.991 | 0.717 | 1.04x | 15.3/19.3/22.1% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.936 | 0.934 | 0.002 | - | - | 0.993 | 0.994 | 0.771 | 0.92x | 13.0/17.4/20.3% | 1.5/3.5% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario coastal`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.988 | 0.989 | 0.787 | 1.26x | 16.3/22.3/24.0% | 1.9/4.8% | 3 |
| 0.5 | 1 | 0.936 | 0.934 | 0.002 | - | - | 0.988 | 0.988 | 0.691 | 1.02x | 15.3/19.1/22.0% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.937 | 0.934 | 0.003 | - | - | 0.995 | 0.995 | 0.779 | 0.91x | 12.9/17.7/20.6% | 1.4/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario coastal`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.944 | 0.941 | 0.003 | - | - | 0.994 | 0.994 | 0.699 | 0.75x | 11.8/15.6/17.2% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

### `FW-versions` - profile  `--scenario coastal`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.932 | 0.929 | 0.002 | - | - | 0.991 | 0.991 | 0.414 | 0.76x | 10.8/14.0/16.3% | 1.2/2.6% | 3 |
| 2.5 | 1 | 0.928 | 0.927 | 0.001 | - | - | 0.989 | 0.990 | 0.416 | 0.77x | 10.9/14.1/16.3% | 1.2/2.6% | 3 |
| 2.6 | 1 | 0.936 | 0.935 | 0.002 | - | - | 0.995 | 0.996 | 0.468 | 0.73x | 10.6/13.9/16.1% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.932 | 0.931 | 0.001 | - | - | 0.987 | 0.988 | 0.424 | 0.76x | 11.3/15.8/17.9% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.935 | 0.932 | 0.003 | - | - | 0.988 | 0.990 | 0.703 | 0.92x | 13.9/17.9/19.7% | 1.3/3.4% | 3 |
| 900 | 1 | 0.887 | 0.873 | 0.014 | - | - | 0.979 | 0.980 | 0.630 | 2.34x | 35.1/44.5/48.3% | 3.3/8.7% | 3 |
| 300 | 1 | 0.626 | 0.612 | 0.013 | - | - | 0.763 | 0.885 | 0.404 | 4.76x | 62.2/74.9/79.0% | 6.8/16.7% | 3 |

> broadcast-interval-s=300: queue drops 11.1% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 46

### `LD-chatty-hops` - broadcast-interval-s  `--scenario coastal`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.954 | 0.953 | 0.001 | - | - | 0.994 | 0.995 | 0.741 | 0.98x | 14.6/18.5/20.5% | 1.4/3.5% | 3 |
| 900 | 1 | 0.905 | 0.899 | 0.005 | - | - | 0.965 | 0.966 | 0.734 | 2.57x | 37.5/47.3/51.5% | 3.7/9.0% | 3 |
| 300 | 1 | 0.586 | 0.577 | 0.010 | - | - | 0.715 | 0.793 | 0.418 | 5.13x | 64.5/76.1/79.8% | 7.6/17.2% | 3 |

> broadcast-interval-s=300: queue drops 16.4% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 32

### `LD-diurnal` - diurnal  `--scenario coastal`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.937 | 0.933 | 0.004 | - | - | 0.990 | 0.990 | 0.710 | 1.28x | 19.4/25.1/27.5% | 1.8/4.8% | 3 |
| sinusoid | 1 | 0.933 | 0.928 | 0.005 | - | - | 0.992 | 0.993 | 0.676 | 1.26x | 19.2/24.8/27.1% | 1.8/4.8% | 3 |
| commuter | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.887 | 0.873 | 0.014 | - | - | 0.979 | 0.980 | 0.630 | 2.34x | 35.1/44.5/48.3% | 3.3/8.7% | 3 |
| 3600 | 1 | 0.935 | 0.932 | 0.003 | - | - | 0.988 | 0.990 | 0.703 | 0.92x | 13.9/17.9/19.7% | 1.3/3.4% | 3 |
| 10800 | 1 | 0.948 | 0.946 | 0.003 | - | - | 0.996 | 0.997 | 0.712 | 0.65x | 9.6/12.4/13.7% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.953 | 0.951 | 0.002 | - | - | 0.997 | 0.998 | 0.717 | 0.48x | 7.2/9.2/10.2% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario coastal`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.926 | 0.920 | 0.006 | - | - | 0.992 | 0.993 | 0.710 | 1.56x | 23.7/30.4/33.2% | 2.2/5.8% | 3 |
| 1.0 | 1 | 0.913 | 0.904 | 0.009 | - | - | 0.985 | 0.986 | 0.679 | 1.73x | 26.3/33.7/36.7% | 2.4/6.5% | 3 |
| 4.0 | 1 | 0.886 | 0.873 | 0.013 | - | - | 0.974 | 0.978 | 0.626 | 2.15x | 33.0/42.4/46.3% | 3.0/8.5% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario coastal`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.730 | 0.726 | 0.004 | - | - | 0.830 | 0.877 | 0.587 | 5.67x | 63.1/75.7/78.9% | 4.1/13.6% | 3 |
| 1.0 | 1 | 0.640 | 0.637 | 0.003 | - | - | 0.743 | 0.813 | 0.516 | 6.14x | 65.7/77.2/79.9% | 4.5/14.9% | 3 |

> traceroute-per-hour=0.0: queue drops 25.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 110

> traceroute-per-hour=1.0: queue drops 37.7% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 113

### `MS-density` - nodes  `--scenario coastal`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.813 | 0.800 | 0.013 | - | - | 0.941 | 0.948 | 0.345 | 1.59x | 26.6/33.4/36.4% | 3.5/7.4% | 3 |
| 60 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 90 | 1 | 0.964 | 0.964 | 0.001 | - | - | 0.999 | 0.999 | 0.874 | 1.52x | 20.6/28.3/32.1% | 1.4/5.1% | 3 |
| 120 | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 0.999 | 0.866 | 2.08x | 26.2/38.2/42.8% | 1.4/5.2% | 3 |
| 150 | 1 | 0.975 | 0.974 | 0.001 | - | - | 0.998 | 0.998 | 0.882 | 2.55x | 31.3/44.6/49.6% | 1.3/5.7% | 3 |

> nodes=90: misdecodes 1

### `MS-hopscale` - nodes  `--scenario coastal`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 120 | 1 | 0.832 | 0.822 | 0.010 | - | - | 0.978 | 0.979 | 0.422 | 2.15x | 16.5/25.3/30.0% | 1.4/4.9% | 3 |
| 250 | 1 | 0.581 | 0.569 | 0.012 | - | - | 0.891 | 0.914 | 0.187 | 4.80x | 18.4/31.2/44.9% | 1.6/6.7% | 3 |
| 500 | 1 | 0.335 | 0.325 | 0.010 | - | - | 0.609 | 0.621 | 0.082 | 10.28x | 18.4/37.9/54.8% | 1.7/7.5% | 3 |

> nodes=250: decode_failures 143

> nodes=500: decode_failures 323

> slower: 44.6 s per simulated hour against 18 over 33 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-oversubscribed` - nodes  `--scenario coastal`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.831 | 0.823 | 0.008 | - | - | 0.978 | 0.979 | 0.426 | 2.02x | 15.6/23.6/28.3% | 1.4/4.6% | 3 |
| 250 | 1 | 0.577 | 0.564 | 0.012 | - | - | 0.885 | 0.901 | 0.171 | 4.51x | 17.2/29.1/42.2% | 1.5/6.1% | 3 |
| 500 | 1 | 0.334 | 0.324 | 0.010 | - | - | 0.619 | 0.625 | 0.080 | 9.87x | 17.4/36.3/52.9% | 1.6/7.1% | 3 |

> nodes=250: decode_failures 77

> nodes=500: decode_failures 129

### `MS-roles` - role-mix  `--scenario coastal`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.921 | 0.915 | 0.007 | - | - | 0.989 | 0.991 | 0.663 | 1.40x | 21.2/27.3/30.0% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.902 | 0.890 | 0.012 | - | - | 0.987 | 0.989 | 0.455 | 1.20x | 18.9/26.9/29.5% | 1.9/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario coastal`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.928 | 0.923 | 0.005 | - | - | 0.985 | 0.986 | 0.657 | 1.42x | 21.5/27.6/30.2% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.909 | 0.899 | 0.010 | - | - | 0.979 | 0.980 | 0.469 | 1.35x | 20.6/30.1/33.4% | 2.2/5.3% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario coastal`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.05 | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.983 | 0.983 | 0.696 | 1.60x | 23.1/32.4/37.5% | 2.2/5.4% | 3 |
| 0.1 | 1 | 0.939 | 0.936 | 0.003 | - | - | 0.989 | 0.990 | 0.714 | 1.70x | 25.3/36.2/41.4% | 2.3/5.4% | 3 |
| 0.2 | 1 | 0.941 | 0.939 | 0.002 | - | - | 0.985 | 0.985 | 0.712 | 1.92x | 27.8/41.6/46.8% | 2.6/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario coastal`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| local-typical | 1 | 0.628 | 0.623 | 0.005 | - | - | 0.784 | 0.785 | 0.000 | 1.55x | 18.3/30.4/38.5% | 2.4/5.7% | 3 |
| event | 1 | 0.561 | 0.555 | 0.006 | - | - | 0.713 | 0.713 | 0.000 | 1.67x | 10.1/19.2/31.5% | 2.8/4.7% | 3 |
| backbone | 1 | 0.975 | 0.975 | 0.000 | - | - | 1.000 | 1.000 | 0.837 | 1.17x | 31.4/37.9/41.2% | 1.4/5.6% | 3 |

### `MS-size` - nodes  `--scenario coastal`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.918 | 0.910 | 0.008 | - | - | 0.987 | 0.990 | 0.641 | 1.57x | 32.0/39.2/45.3% | 3.3/8.0% | 3 |
| 60 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 90 | 1 | 0.886 | 0.883 | 0.003 | - | - | 0.991 | 0.992 | 0.633 | 1.72x | 16.9/25.4/31.2% | 1.6/5.4% | 3 |
| 120 | 1 | 0.832 | 0.822 | 0.010 | - | - | 0.978 | 0.979 | 0.422 | 2.15x | 16.5/25.3/30.0% | 1.4/4.9% | 3 |
| 150 | 1 | 0.769 | 0.752 | 0.018 | - | - | 0.946 | 0.948 | 0.374 | 2.80x | 17.1/29.0/34.7% | 1.5/5.8% | 3 |

### `MS-stretch` - stretch  `--scenario coastal`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 1.25 | 1 | 0.787 | 0.771 | 0.016 | - | - | 0.937 | 0.946 | 0.485 | 1.45x | 14.8/21.8/23.1% | 2.2/4.9% | 3 |
| 1.5 | 1 | 0.565 | 0.550 | 0.016 | - | - | 0.810 | 0.816 | 0.123 | 1.40x | 12.0/17.7/23.5% | 2.1/5.3% | 3 |
| 2.0 | 1 | 0.248 | 0.242 | 0.007 | - | - | 0.466 | 0.509 | 0.000 | 1.28x | 7.2/12.7/16.5% | 2.1/4.3% | 3 |

> stretch=1.25: decode_failures 3

> stretch=2.0: decode_failures 16

### `MS-topology` - topology  `--scenario coastal`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| clustered | 1 | 0.949 | 0.949 | 0.000 | - | - | 0.994 | 0.994 | 0.206 | 1.19x | 24.1/30.1/34.1% | 1.7/5.6% | 3 |
| corridor | 1 | 0.595 | 0.578 | 0.017 | - | - | 0.884 | 0.885 | 0.304 | 1.28x | 14.4/29.3/33.4% | 1.7/5.9% | 3 |
| hub | 1 | 0.960 | 0.959 | 0.002 | - | - | 0.985 | 0.985 | 0.885 | 1.15x | 28.2/36.0/38.6% | 1.5/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario coastal`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.898 | 0.898 | 0.000 | - | - | 0.975 | 0.983 | 0.685 | 1.78x | 27.1/34.6/37.7% | 2.5/6.8% | 3 |
| True | 1 | 0.902 | 0.902 | 0.000 | - | - | 0.973 | 0.982 | 0.666 | 1.79x | 27.1/34.9/38.1% | 2.5/6.9% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario coastal`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.902 | 0.902 | 0.000 | - | - | 0.973 | 0.982 | 0.666 | 1.79x | 27.1/34.9/38.1% | 2.5/6.9% | 3 |
| m4-early-flood | 1 | 0.893 | 0.893 | 0.000 | - | - | 0.967 | 0.977 | 0.672 | 1.80x | 27.3/35.1/38.3% | 2.5/6.9% | 3 |

### `PR-protocol` - protocol  `--scenario coastal`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.914 | 0.914 | 0.000 | - | - | 0 | 0.000 | 0.677 | 1.42x | 21.3/27.6/30.2% | 2.0/5.3% | 3 |
| chain | 1 | 0.908 | 0.907 | 0.001 | - | - | 0.935 | 0.985 | 0.658 | 1.66x | 25.1/32.2/35.4% | 2.4/6.2% | 3 |
| sr | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario coastal`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| True | 1 | 0.924 | 0.918 | 0.006 | - | - | 0.991 | 0.991 | 0.696 | 1.46x | 22.0/28.3/31.0% | 2.0/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario coastal`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 0.999 | 0.866 | 2.08x | 26.2/38.2/42.8% | 1.4/5.2% | 3 |
| True | 1 | 0.971 | 0.970 | 0.001 | - | - | 0.999 | 0.999 | 0.876 | 2.10x | 26.3/38.2/42.8% | 1.4/5.2% | 3 |

### `RF-bw500` - preset  `--scenario coastal`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.315 | 0.308 | 0.006 | - | - | 0.625 | 0.630 | 0.000 | 0.08x | 0.5/0.8/1.3% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.563 | 0.561 | 0.002 | - | - | 0.713 | 0.716 | 0.113 | 0.31x | 2.8/4.3/5.2% | 0.5/1.2% | 3 |
| LONG_TURBO | 1 | 0.875 | 0.869 | 0.005 | - | - | 0.944 | 0.946 | 0.652 | 1.46x | 16.0/22.2/23.2% | 2.2/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 8

### `RF-duct` - duct-per-hour  `--scenario coastal`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 0.25 | 1 | 0.930 | 0.925 | 0.005 | - | - | 0.984 | 0.985 | 0.734 | 1.23x | 21.9/27.4/29.5% | 1.6/5.1% | 3 |
| 1.0 | 1 | 0.957 | 0.955 | 0.003 | - | - | 0.995 | 0.995 | 0.835 | 0.90x | 26.1/30.5/31.5% | 1.1/5.1% | 3 |

### `RF-eu-presets` - preset  `--scenario coastal`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.543 | 0.536 | 0.007 | - | - | 0.693 | 0.702 | 0.000 | 0.20x | 1.5/2.6/2.9% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| LITE_FAST | 1 | 0.885 | 0.880 | 0.005 | - | - | 0.974 | 0.975 | 0.577 | 1.16x | 14.2/20.0/22.6% | 1.7/4.1% | 3 |
| NARROW_SLOW | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.979 | 0.980 | 0.626 | 1.47x | 18.3/25.8/29.2% | 2.3/5.2% | 3 |

> preset=SHORT_FAST: decode_failures 9

### `RF-noise` - noise-profile  `--scenario coastal`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| temporal | 1 | 0.863 | 0.851 | 0.012 | - | - | 0.968 | 0.973 | 0.593 | 1.46x | 20.9/27.7/30.5% | 2.1/5.3% | 3 |
| transient | 1 | 0.912 | 0.904 | 0.008 | - | - | 0.979 | 0.980 | 0.682 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| periodic | 1 | 0.794 | 0.788 | 0.007 | - | - | 0.862 | 0.863 | 0.574 | 1.36x | 20.8/26.5/28.9% | 2.0/4.8% | 3 |

> noise-profile=temporal: decode_failures 2

### `RF-preset` - preset  `--scenario coastal`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.543 | 0.536 | 0.007 | - | - | 0.693 | 0.702 | 0.000 | 0.20x | 1.5/2.6/2.9% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| LONG_MODERATE | 1 | 0.857 | 0.847 | 0.010 | - | - | 0.946 | 0.950 | 0.744 | 3.75x | 58.2/66.7/70.6% | 5.4/12.8% | 3 |

> preset=SHORT_FAST: decode_failures 9

### `RF-preset-turbo` - preset  `--scenario coastal`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.046 | 0.045 | 0.000 | - | - | 0.076 | 0.078 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.315 | 0.308 | 0.006 | - | - | 0.625 | 0.630 | 0.000 | 0.08x | 0.5/0.8/1.3% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| LONG_TURBO | 1 | 0.875 | 0.869 | 0.005 | - | - | 0.944 | 0.946 | 0.652 | 1.46x | 16.0/22.2/23.2% | 2.2/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.910 | 0.903 | 0.007 | - | - | 0.983 | 0.983 | 0.733 | 2.03x | 26.9/34.3/35.5% | 3.0/7.2% | 3 |

> preset=SHORT_TURBO: decode_failures 8

### `RF-pulse` - noise-pulse-interval-ms  `--scenario coastal`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.873 | 0.865 | 0.008 | - | - | 0.941 | 0.942 | 0.630 | 1.42x | 21.5/27.8/30.3% | 2.0/5.2% | 3 |
| 10000 | 1 | 0.794 | 0.788 | 0.007 | - | - | 0.862 | 0.863 | 0.574 | 1.36x | 20.8/26.5/28.9% | 2.0/4.8% | 3 |
| 4000 | 1 | 0.528 | 0.522 | 0.006 | - | - | 0.575 | 0.621 | 0.324 | 1.21x | 18.8/23.8/25.7% | 1.8/3.7% | 3 |
| 2000 | 1 | 0.131 | 0.131 | 0.000 | - | - | 0.132 | 0.216 | 0.053 | 0.80x | 12.9/16.7/18.2% | 1.2/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 8

### `RF-stretch-duct` - duct-per-hour  `--scenario coastal`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.565 | 0.550 | 0.016 | - | - | 0.810 | 0.816 | 0.123 | 1.40x | 12.0/17.7/23.5% | 2.1/5.3% | 3 |
| 1.0 | 1 | 0.792 | 0.777 | 0.015 | - | - | 0.927 | 0.927 | 0.536 | 1.00x | 19.8/24.4/27.4% | 1.3/5.0% | 3 |

### `RF-txpower` - tx-power  `--scenario coastal`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 22 | 1 | 0.526 | 0.523 | 0.003 | - | - | 0.659 | 0.662 | 0.102 | 1.39x | 11.5/17.5/21.1% | 2.1/4.7% | 3 |
| 17 | 1 | 0.263 | 0.256 | 0.007 | - | - | 0.459 | 0.486 | 0.000 | 1.31x | 7.1/13.4/16.9% | 2.2/4.6% | 3 |
| 14 | 1 | 0.101 | 0.099 | 0.003 | - | - | 0.201 | 0.239 | 0.000 | 0.87x | 3.7/9.0/12.9% | 1.3/3.4% | 3 |

> tx-power=22: decode_failures 1

> tx-power=17: decode_failures 18

> tx-power=14: decode_failures 5

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario coastal`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 0.999 | 0.866 | 2.08x | 26.2/38.2/42.8% | 1.4/5.2% | 3 |
| True | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.999 | 1.000 | 0.852 | 2.44x | 30.2/42.9/47.6% | 1.7/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario coastal`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.932 | 0.930 | 0.003 | - | - | 0.984 | 0.984 | 0.683 | 1.55x | 22.6/30.3/34.0% | 2.1/5.4% | 3 |
| True | 1 | 0.950 | 0.949 | 0.001 | - | - | 0.991 | 0.991 | 0.713 | 1.67x | 23.9/32.0/35.7% | 2.3/5.5% | 3 |

### `RT-hopassign` - hop-assign  `--scenario coastal`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| random | 1 | 0.905 | 0.892 | 0.013 | - | - | 0.989 | 0.989 | 0.624 | 1.40x | 21.0/27.3/30.0% | 2.0/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario coastal`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.799 | 0.768 | 0.031 | - | - | 0.968 | 0.974 | 0.392 | 1.07x | 16.7/22.8/25.2% | 1.5/4.6% | 3 |
| 7 | 1 | 0.942 | 0.940 | 0.003 | - | - | 0.989 | 0.990 | 0.730 | 1.55x | 23.1/29.6/32.4% | 2.2/5.6% | 3 |
| 15 | 1 | 0.953 | 0.951 | 0.002 | - | - | 0.991 | 0.991 | 0.768 | 1.53x | 22.6/29.0/31.8% | 2.1/5.4% | 3 |
| 32 | 1 | 0.952 | 0.950 | 0.001 | - | - | 0.990 | 0.990 | 0.776 | 1.55x | 23.0/29.4/32.2% | 2.2/5.5% | 3 |

> hop-limit=3: decode_failures 3

### `RT-hopspread` - hop-limit  `--scenario coastal`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.799 | 0.768 | 0.031 | - | - | 0.968 | 0.974 | 0.392 | 1.07x | 16.7/22.8/25.2% | 1.5/4.6% | 3 |
| 5 | 1 | 0.909 | 0.900 | 0.009 | - | - | 0.987 | 0.987 | 0.666 | 1.46x | 22.0/28.3/31.1% | 2.0/5.4% | 3 |
| 7 | 1 | 0.942 | 0.940 | 0.003 | - | - | 0.989 | 0.990 | 0.730 | 1.55x | 23.1/29.6/32.4% | 2.2/5.6% | 3 |

> hop-limit=3: decode_failures 3

### `RT-rebroadcast` - rebroadcast-mode  `--scenario coastal`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.920 | 0.920 | 0.000 | - | - | 0.939 | 0.990 | 0.690 | 1.42x | 21.4/27.8/30.3% | 2.0/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario coastal`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.799 | 0.768 | 0.031 | - | - | 0.968 | 0.974 | 0.392 | 1.07x | 16.7/22.8/25.2% | 1.5/4.6% | 3 |
| True | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

> hop-spread=False: decode_failures 3

### `SC-signing` - signature-policy  `--scenario coastal`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| BALANCED | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| STRICT | 1 | 0.815 | 0.815 | 0.000 | - | - | 0.883 | 0.887 | 0.585 | 1.53x | 23.0/29.6/32.3% | 2.1/5.5% | 3 |

> signature-policy=STRICT: decode_failures 2

### `SF-advert-transport` - advert-transport  `--scenario coastal`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| dm | 1 | 0.922 | 0.914 | 0.008 | - | - | 0.990 | 0.991 | 0.670 | 1.44x | 21.7/27.9/30.6% | 2.0/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario coastal`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.913 | 0.906 | 0.007 | - | - | 0.976 | 0.978 | 0.690 | 1.46x | 22.1/28.5/31.2% | 2.1/5.4% | 3 |
| local | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| time | 1 | 0.922 | 0.915 | 0.007 | - | - | 0.988 | 0.989 | 0.685 | 1.50x | 22.7/29.1/31.9% | 2.1/5.6% | 3 |
| window | 1 | 0.920 | 0.913 | 0.007 | - | - | 0.984 | 0.986 | 0.692 | 1.44x | 21.6/27.8/30.5% | 2.0/5.3% | 3 |

> bucket-mode=global: misdecodes 37

> bucket-mode=time: misdecodes 32

> bucket-mode=window: misdecodes 30

### `SF-bucket-time` - time-bucket-s  `--scenario coastal`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.917 | 0.910 | 0.007 | - | - | 0.983 | 0.987 | 0.691 | 1.58x | 23.8/30.5/33.2% | 2.2/5.9% | 3 |
| 1800 | 1 | 0.922 | 0.915 | 0.007 | - | - | 0.988 | 0.989 | 0.685 | 1.50x | 22.7/29.1/31.9% | 2.1/5.6% | 3 |
| 3600 | 1 | 0.922 | 0.915 | 0.008 | - | - | 0.987 | 0.990 | 0.700 | 1.44x | 21.8/28.1/30.5% | 2.0/5.4% | 3 |

> time-bucket-s=600: misdecodes 113

> time-bucket-s=1800: misdecodes 32

> time-bucket-s=3600: misdecodes 11

### `SF-cadence` - trigger  `--scenario coastal`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| interval | 1 | 0.910 | 0.901 | 0.009 | - | - | 0.980 | 0.987 | 0.647 | 1.95x | 28.8/37.2/40.8% | 2.8/7.8% | 3 |
| aimd | 1 | 0.916 | 0.915 | 0.001 | - | - | 0.947 | 0.985 | 0.700 | 1.46x | 22.0/28.4/31.0% | 2.1/5.4% | 3 |
| bucket+interval | 1 | 0.909 | 0.899 | 0.011 | - | - | 0.985 | 0.985 | 0.660 | 1.96x | 29.0/37.1/40.7% | 2.8/7.6% | 3 |

> trigger=interval: misdecodes 20

> trigger=interval: decode_failures 5

> trigger=aimd: misdecodes 5

> trigger=bucket+interval: misdecodes 11

### `SF-capacity` - capacity  `--scenario coastal`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.923 | 0.917 | 0.006 | - | - | 0.984 | 0.988 | 0.700 | 1.45x | 21.9/28.2/30.9% | 2.0/5.5% | 3 |
| 8 | 1 | 0.930 | 0.925 | 0.005 | - | - | 0.986 | 0.992 | 0.709 | 1.45x | 22.0/28.2/31.0% | 2.0/5.4% | 3 |
| 16 | 1 | 0.917 | 0.910 | 0.007 | - | - | 0.979 | 0.981 | 0.672 | 1.44x | 21.6/28.0/30.6% | 2.0/5.4% | 3 |
| 32 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 50 | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.993 | 0.993 | 0.705 | 1.46x | 22.0/28.3/30.9% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 83

> capacity=8: decode_failures 99

### `SF-capacity-local` - capacity  `--scenario coastal`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.923 | 0.917 | 0.006 | - | - | 0.984 | 0.988 | 0.700 | 1.45x | 21.9/28.2/30.9% | 2.0/5.5% | 3 |
| 8 | 1 | 0.930 | 0.925 | 0.005 | - | - | 0.986 | 0.992 | 0.709 | 1.45x | 22.0/28.2/31.0% | 2.0/5.4% | 3 |
| 16 | 1 | 0.917 | 0.910 | 0.007 | - | - | 0.979 | 0.981 | 0.672 | 1.44x | 21.6/28.0/30.6% | 2.0/5.4% | 3 |
| 32 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 50 | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.993 | 0.993 | 0.705 | 1.46x | 22.0/28.3/30.9% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 83

> capacity=8: decode_failures 99

### `SF-capacity-window` - capacity  `--scenario coastal`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.926 | 0.920 | 0.005 | - | - | 0.982 | 0.988 | 0.698 | 1.43x | 21.6/27.8/30.5% | 2.0/5.3% | 3 |
| 16 | 1 | 0.927 | 0.921 | 0.006 | - | - | 0.989 | 0.990 | 0.673 | 1.44x | 21.7/28.0/30.6% | 2.0/5.4% | 3 |
| 32 | 1 | 0.920 | 0.913 | 0.007 | - | - | 0.984 | 0.986 | 0.692 | 1.44x | 21.6/27.8/30.5% | 2.0/5.3% | 3 |

> capacity=8: misdecodes 35

> capacity=8: decode_failures 13

> capacity=16: misdecodes 21

> capacity=32: misdecodes 30

### `SF-catchup` - catch-up-hours  `--scenario coastal`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.909 | 0.899 | 0.011 | - | - | 0.985 | 0.985 | 0.660 | 1.96x | 29.0/37.1/40.7% | 2.8/7.6% | 3 |
| 02-06 | 1 | 0.921 | 0.918 | 0.003 | - | - | 0.963 | 0.987 | 0.688 | 1.46x | 22.1/28.6/31.3% | 2.1/5.5% | 3 |
| 00-08 | 1 | 0.923 | 0.920 | 0.003 | - | - | 0.965 | 0.989 | 0.691 | 1.53x | 23.1/29.8/32.8% | 2.2/5.9% | 3 |

> catch-up-hours=: misdecodes 11

> catch-up-hours=02-06: decode_failures 22

> catch-up-hours=00-08: decode_failures 20

### `SF-hops-flat` - hops-apart  `--scenario coastal`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.911 | 0.909 | 0.002 | - | - | 0.976 | 0.977 | 0.674 | 1.46x | 21.9/28.3/31.0% | 2.1/5.4% | 3 |
| 2 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 3 | 1 | 0.925 | 0.910 | 0.015 | - | - | 0.983 | 0.987 | 0.714 | 1.46x | 22.0/28.4/31.0% | 2.0/5.5% | 3 |
| 4 | 1 | 0.928 | 0.915 | 0.012 | - | - | 0.989 | 0.991 | 0.709 | 1.45x | 21.8/28.2/30.7% | 2.0/5.4% | 3 |

> faster: 1.8 s per simulated hour against 3.65 over 33 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario coastal`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.911 | 0.909 | 0.002 | - | - | 0.976 | 0.977 | 0.674 | 1.46x | 21.9/28.3/31.0% | 2.1/5.4% | 3 |
| 2 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 3 | 1 | 0.925 | 0.910 | 0.015 | - | - | 0.983 | 0.987 | 0.714 | 1.46x | 22.0/28.4/31.0% | 2.0/5.5% | 3 |
| 4 | 1 | 0.928 | 0.915 | 0.012 | - | - | 0.989 | 0.991 | 0.709 | 1.45x | 21.8/28.2/30.7% | 2.0/5.4% | 3 |
| 5 | 1 | 0.928 | 0.915 | 0.012 | - | - | 0.989 | 0.991 | 0.709 | 1.45x | 21.8/28.2/30.7% | 2.0/5.4% | 3 |

> faster: 2.08 s per simulated hour against 4.52 over 33 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario coastal`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.917 | 0.911 | 0.006 | - | - | 0.981 | 0.983 | 0.700 | 1.46x | 22.0/28.2/30.9% | 2.0/5.4% | 3 |
| 30 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 120 | 1 | 0.924 | 0.918 | 0.006 | - | - | 0.990 | 0.990 | 0.674 | 1.48x | 22.2/28.5/31.2% | 2.1/5.5% | 3 |
| 600 | 1 | 0.922 | 0.916 | 0.006 | - | - | 0.989 | 0.989 | 0.681 | 1.46x | 22.1/28.5/31.2% | 2.1/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario coastal`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.917 | 0.911 | 0.006 | - | - | 0.981 | 0.983 | 0.700 | 1.46x | 22.0/28.2/30.9% | 2.0/5.4% | 3 |
| 30 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 120 | 1 | 0.924 | 0.918 | 0.006 | - | - | 0.990 | 0.990 | 0.674 | 1.48x | 22.2/28.5/31.2% | 2.1/5.5% | 3 |
| 600 | 1 | 0.922 | 0.916 | 0.006 | - | - | 0.989 | 0.989 | 0.681 | 1.46x | 22.1/28.5/31.2% | 2.1/5.4% | 3 |

### `SF-place-flat` - place  `--scenario coastal`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.930 | 0.912 | 0.018 | - | - | 0.937 | 0.988 | 0.690 | 1.48x | 22.2/28.3/31.1% | 2.1/5.4% | 3 |
| routers | 1 | 0.923 | 0.921 | 0.002 | - | - | 0.988 | 0.988 | 0.694 | 1.46x | 22.0/28.4/31.1% | 2.0/5.4% | 3 |
| alternate-routers | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.985 | 0.985 | 0.711 | 1.45x | 21.8/28.3/30.9% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.917 | 0.915 | 0.002 | - | - | 0.987 | 0.988 | 0.678 | 1.47x | 22.1/28.5/31.1% | 2.0/5.5% | 3 |
| random-clients | 1 | 0.930 | 0.919 | 0.011 | - | - | 0.989 | 0.990 | 0.715 | 1.47x | 22.1/28.5/31.0% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

> place=spread: decode_failures 22

### `SF-place-spread` - place  `--scenario coastal`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.930 | 0.912 | 0.018 | - | - | 0.937 | 0.988 | 0.690 | 1.48x | 22.2/28.3/31.1% | 2.1/5.4% | 3 |
| routers | 1 | 0.923 | 0.921 | 0.002 | - | - | 0.988 | 0.988 | 0.694 | 1.46x | 22.0/28.4/31.1% | 2.0/5.4% | 3 |
| alternate-routers | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.985 | 0.985 | 0.711 | 1.45x | 21.8/28.3/30.9% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.917 | 0.915 | 0.002 | - | - | 0.987 | 0.988 | 0.678 | 1.47x | 22.1/28.5/31.1% | 2.0/5.5% | 3 |
| random-clients | 1 | 0.930 | 0.919 | 0.011 | - | - | 0.989 | 0.990 | 0.715 | 1.47x | 22.1/28.5/31.0% | 2.0/5.4% | 3 |
| hops-apart | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

> place=spread: decode_failures 22

### `SF-provide-transport` - provide-transport  `--scenario coastal`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| broadcast | 1 | 0.938 | 0.913 | 0.025 | - | - | 0.987 | 0.988 | 0.747 | 1.54x | 23.1/29.5/32.3% | 2.2/5.7% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario coastal`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| heard | 1 | 0.922 | 0.915 | 0.007 | - | - | 0.987 | 0.988 | 0.697 | 1.45x | 21.9/28.3/31.0% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 23

### `SF-replay-order-broadcast` - replay-ordering  `--scenario coastal`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.938 | 0.913 | 0.025 | - | - | 0.987 | 0.988 | 0.747 | 1.54x | 23.1/29.5/32.3% | 2.2/5.7% | 3 |
| heard | 1 | 0.936 | 0.911 | 0.025 | - | - | 0.987 | 0.988 | 0.752 | 1.54x | 23.2/29.6/32.3% | 2.1/5.8% | 3 |

> replay-ordering=heard: misdecodes 6

### `SF-resolve` - resolve  `--scenario coastal`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| enum | 1 | 0.923 | 0.916 | 0.007 | - | - | 0.982 | 0.990 | 0.704 | 1.44x | 21.8/28.0/30.7% | 2.0/5.5% | 3 |
| hybrid | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario coastal`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.923 | 0.921 | 0.002 | - | - | 0.988 | 0.988 | 0.694 | 1.46x | 22.0/28.4/31.1% | 2.0/5.4% | 3 |
| 6 | 1 | 0.916 | 0.910 | 0.005 | - | - | 0.977 | 0.979 | 0.694 | 1.49x | 22.6/29.2/32.0% | 2.1/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario coastal`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.923 | 0.919 | 0.004 | - | - | 0.969 | 0.975 | 0.702 | 1.44x | 21.8/28.1/30.8% | 2.0/5.4% | 2 |
| 3 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 5 | 1 | 0.927 | 0.913 | 0.014 | - | - | 0.988 | 0.989 | 0.712 | 1.50x | 22.4/28.9/31.4% | 2.1/5.5% | 5 |
| 8 | 1 | 0.926 | 0.911 | 0.015 | - | - | 0.991 | 0.993 | 0.680 | 1.54x | 23.1/29.4/32.0% | 2.1/5.6% | 8 |

### `SF-servers-spread` - servers  `--scenario coastal`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.923 | 0.919 | 0.004 | - | - | 0.969 | 0.975 | 0.702 | 1.44x | 21.8/28.1/30.8% | 2.0/5.4% | 2 |
| 3 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 5 | 1 | 0.927 | 0.913 | 0.014 | - | - | 0.988 | 0.989 | 0.712 | 1.50x | 22.4/28.9/31.4% | 2.1/5.5% | 5 |
| 8 | 1 | 0.926 | 0.911 | 0.015 | - | - | 0.991 | 0.993 | 0.680 | 1.54x | 23.1/29.4/32.0% | 2.1/5.6% | 8 |

### `SF-signed` - signed  `--scenario coastal`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| True | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario coastal`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.929 | 0.925 | 0.004 | - | - | 0.987 | 0.992 | 0.703 | 1.35x | 20.4/26.3/28.8% | 1.9/5.0% | 3 |
| 1 | 1 | 0.927 | 0.922 | 0.005 | - | - | 0.987 | 0.989 | 0.703 | 1.33x | 20.2/26.1/28.6% | 1.9/5.0% | 3 |
| 2 | 1 | 0.922 | 0.916 | 0.005 | - | - | 0.984 | 0.986 | 0.693 | 1.34x | 20.2/26.0/28.5% | 1.9/5.0% | 3 |
| 4 | 1 | 0.928 | 0.923 | 0.005 | - | - | 0.989 | 0.990 | 0.702 | 1.35x | 20.5/26.4/29.0% | 1.9/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario coastal`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.922 | 0.915 | 0.007 | - | - | 0.988 | 0.988 | 0.693 | 1.45x | 21.9/28.2/30.7% | 2.0/5.4% | 3 |
| 24 | 1 | 0.927 | 0.921 | 0.006 | - | - | 0.991 | 0.991 | 0.697 | 1.45x | 21.8/28.1/30.6% | 2.0/5.3% | 3 |
| 32 | 1 | 0.929 | 0.922 | 0.006 | - | - | 0.990 | 0.990 | 0.707 | 1.45x | 21.8/28.1/30.7% | 2.0/5.4% | 3 |
| 64 | 1 | 0.923 | 0.918 | 0.006 | - | - | 0.989 | 0.989 | 0.693 | 1.47x | 22.2/28.5/31.1% | 2.1/5.5% | 3 |

### `SF-window-size` - window-size  `--scenario coastal`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.919 | 0.912 | 0.007 | - | - | 0.985 | 0.987 | 0.685 | 1.55x | 23.3/29.9/32.7% | 2.2/5.8% | 3 |
| 16 | 1 | 0.925 | 0.918 | 0.007 | - | - | 0.990 | 0.992 | 0.700 | 1.48x | 22.2/28.6/31.3% | 2.0/5.5% | 3 |
| 32 | 1 | 0.920 | 0.913 | 0.007 | - | - | 0.984 | 0.986 | 0.692 | 1.44x | 21.6/27.8/30.5% | 2.0/5.3% | 3 |

> window-size=8: misdecodes 171

> window-size=16: misdecodes 63

> window-size=32: misdecodes 30

### `TH-congestion` - no-congestion-scaling  `--scenario coastal`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 0.999 | 0.866 | 2.08x | 26.2/38.2/42.8% | 1.4/5.2% | 3 |
| True | 1 | 0.757 | 0.752 | 0.005 | - | - | 0.865 | 0.898 | 0.603 | 5.54x | 62.4/75.5/78.7% | 4.0/13.4% | 3 |

> no-congestion-scaling=True: queue drops 22.6% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 94

### `TH-congestion-input` - congestion-input  `--scenario coastal`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.577 | 0.564 | 0.012 | - | - | 0.885 | 0.901 | 0.171 | 4.51x | 17.2/29.1/42.2% | 1.5/6.1% | 3 |
| truesize | 1 | 0.608 | 0.597 | 0.011 | - | - | 0.918 | 0.927 | 0.182 | 3.51x | 13.2/23.9/35.8% | 1.1/5.4% | 3 |

> congestion-input=hotstore: decode_failures 77

> congestion-input=truesize: decode_failures 36

> slower: 36.7 s per simulated hour against 10.5 over 33 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario coastal`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.973 | 0.972 | 0.001 | - | - | 1.000 | 1.000 | 0.874 | 1.95x | 24.7/35.7/40.0% | 1.4/4.9% | 3 |
| adaptive | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 0.999 | 0.866 | 2.08x | 26.2/38.2/42.8% | 1.4/5.2% | 3 |

