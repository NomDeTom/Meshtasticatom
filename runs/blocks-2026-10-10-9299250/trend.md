# Sweep blocks-2026-10-10-9299250

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 9299250 · seeds 9299250
- **blocks** 87 run
- **compute** 12.1 h of simulator time across every cell
- **generated** 2026-10-10T10:18:15+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>120 warnings</summary>

- AD-amplifiers: amplifier-mix=sprinkled: misdecodes 1
- AD-badrouters: role-placement=degree: decode_failures 1
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 1
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 1
- AD-siting: siting-mix=uniform: decode_failures 1
- AD-worst: role-placement=inverse: misdecodes 1
- BL-control: protocol=sr: decode_failures 1
- DB-hotstore: max-num-nodes=10: decode_failures 10
- DB-hotstore-stress: max-num-nodes=10: decode_failures 53
- DB-hotstore-stress: max-num-nodes=120: decode_failures 2
- DB-platform: platform-mix=constrained: decode_failures 3
- DB-warm: warm-num-nodes=0: queue drops 16.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 122
- DB-warm: warm-num-nodes=25: queue drops 16.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 122
- DB-warm: warm-num-nodes=100: queue drops 16.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 122
- DB-warm: warm-num-nodes=2000: queue drops 16.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 122
- DG-burst: burst-loss=0.2: decode_failures 22
- DG-burst: burst-loss=0.3: decode_failures 35
- DG-loss: extra-loss=0.2: decode_failures 22
- DG-loss: extra-loss=0.3: decode_failures 33
- DG-outage: burst-loss=0.1: decode_failures 40
- DG-outage: burst-loss=0.2: decode_failures 39
- DG-outage: burst-loss=0.3: decode_failures 25
- DM-mode: dm-mode=flood-only: decode_failures 16
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 39
- DM-mode: dm-mode=m4-early-flood: decode_failures 34
- DM-mode: slower: 11.4 s per simulated hour against 3.14 over 50 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.5: decode_failures 2
- FW-mixed: legacy-fraction=0.5: decode_failures 14
- LD-chatty-hops: broadcast-interval-s=300: queue drops 10.7% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 16
- LD-chatty: broadcast-interval-s=300: decode_failures 43
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 16.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 122
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 23.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 116
- MS-density: nodes=40: decode_failures 1
- MS-hopscale: nodes=500: decode_failures 4
- MS-hopscale: faster: 8.72 s per simulated hour against 18 over 50 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-oversubscribed: nodes=250: decode_failures 2
- MS-oversubscribed: faster: 9.2 s per simulated hour against 20.5 over 50 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-roles: role-mix=baymesh-2026-08: decode_failures 1
- MS-router-late: router-late-fraction=0.1: decode_failures 1
- MS-stretch: stretch=1.5: decode_failures 2
- MS-stretch: stretch=2.0: decode_failures 1
- PR-crladder: coding-rate-ladder=False: decode_failures 39
- PR-crladder: coding-rate-ladder=True: decode_failures 33
- PR-crladder: slower: 13 s per simulated hour against 2.77 over 50 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 33
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 46
- PR-dmmode-cr: slower: 13.6 s per simulated hour against 2.57 over 50 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats: extra-repeats=True: decode_failures 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 2
- RF-noise: noise-profile=temporal: decode_failures 44
- RF-noise: noise-profile=transient: decode_failures 9
- RF-noise: noise-profile=periodic: decode_failures 9
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 3
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 38
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 9
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 9
- RF-pulse: slower: 4.28 s per simulated hour against 1.62 over 50 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 2
- RF-txpower: tx-power=14: decode_failures 19
- RT-hoplimit: hop-limit=3: decode_failures 9
- RT-hopspread: hop-limit=3: decode_failures 9
- RT-spread: hop-spread=False: decode_failures 9
- SF-bucket-mode: bucket-mode=global: misdecodes 41
- SF-bucket-mode: bucket-mode=time: misdecodes 18
- SF-bucket-mode: bucket-mode=window: misdecodes 19
- SF-bucket-time: time-bucket-s=600: misdecodes 107
- SF-bucket-time: time-bucket-s=1800: misdecodes 18
- SF-bucket-time: time-bucket-s=3600: misdecodes 4
- SF-bucket-time: time-bucket-s=3600: decode_failures 4
- SF-cadence: trigger=interval: misdecodes 12
- SF-cadence: trigger=interval: decode_failures 20
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 14
- SF-cadence: trigger=bucket+interval: misdecodes 17
- SF-capacity-local: capacity=4: decode_failures 106
- SF-capacity-local: capacity=8: decode_failures 81
- SF-capacity-local: capacity=16: decode_failures 67
- SF-capacity: capacity=4: decode_failures 106
- SF-capacity: capacity=8: decode_failures 81
- SF-capacity: capacity=16: decode_failures 67
- SF-capacity-window: capacity=8: misdecodes 9
- SF-capacity-window: capacity=8: decode_failures 119
- SF-capacity-window: capacity=16: misdecodes 21
- SF-capacity-window: capacity=16: decode_failures 14
- SF-capacity-window: capacity=32: misdecodes 19
- SF-catchup: catch-up-hours=: misdecodes 17
- SF-catchup: catch-up-hours=02-06: misdecodes 1
- SF-catchup: catch-up-hours=02-06: decode_failures 53
- SF-catchup: catch-up-hours=00-08: decode_failures 53
- SF-hops-flat: hops-apart=3: decode_failures 1
- SF-hops-flat: hops-apart=4: decode_failures 32
- SF-hops-spread: hops-apart=3: decode_failures 1
- SF-hops-spread: hops-apart=4: decode_failures 32
- SF-hops-spread: hops-apart=5: decode_failures 34
- SF-jitter-global: advert-jitter-s=600: decode_failures 1
- SF-jitter-local: advert-jitter-s=600: decode_failures 1
- SF-place-flat: place=spread: decode_failures 37
- SF-place-spread: place=spread: decode_failures 37
- SF-provide-transport: provide-transport=broadcast: decode_failures 3
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 3
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 2
- SF-replay-order: replay-ordering=heard: misdecodes 18
- SF-servers-flat: servers=2: decode_failures 2
- SF-servers-flat: servers=8: misdecodes 5
- SF-servers-spread: servers=2: decode_failures 2
- SF-servers-spread: servers=8: misdecodes 5
- SF-window-size: window-size=8: misdecodes 132
- SF-window-size: window-size=16: misdecodes 62
- SF-window-size: window-size=32: misdecodes 19
- TH-congestion-input: congestion-input=hotstore: decode_failures 2
- TH-congestion: no-congestion-scaling=True: queue drops 15.4% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 101

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `PR-dmmode-cr` | 13.6 | 2.57 | 5.30x | 50 |
| `PR-crladder` | 13 | 2.77 | 4.68x | 50 |
| `DM-mode` | 11.4 | 3.14 | 3.65x | 50 |
| `RF-pulse` | 4.28 | 1.62 | 2.64x | 50 |
| `SF-cadence` | 6.93 | 3.61 | 1.92x | 50 |
| `RF-txpower` | 2.91 | 1.54 | 1.89x | 50 |
| `SF-capacity` | 3.05 | 1.73 | 1.77x | 50 |
| `RT-spread` | 3.86 | 2.24 | 1.73x | 50 |
| `SF-capacity-local` | 3.03 | 1.76 | 1.73x | 50 |
| `SF-replay-order-broadcast` | 2.86 | 1.7 | 1.68x | 50 |
| `DG-loss` | 3.73 | 2.25 | 1.66x | 50 |
| `DB-hotstore` | 3.82 | 2.36 | 1.62x | 50 |
| `RF-noise` | 7.92 | 4.91 | 1.61x | 50 |
| `FW-mixed` | 2.69 | 1.67 | 1.61x | 50 |
| `SF-provide-transport` | 2.83 | 1.76 | 1.61x | 50 |
| `MS-roles` | 2.58 | 1.7 | 1.52x | 50 |
| `PR-repeats` | 2.5 | 1.66 | 1.50x | 50 |
| `RF-preset` | 1.9 | 2.91 | 0.66x | 50 |
| `DB-hotstore-stress` | 12.9 | 22.4 | 0.57x | 50 |
| `MS-hopscale` | 8.72 | 18 | 0.48x | 50 |
| `MS-oversubscribed` | 9.2 | 20.5 | 0.45x | 50 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.987 | 0.987 | 0.877 → 0.877 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.986 | 0.986 | 0.877 → 0.881 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.106 → 0.986 | 0.880 | 0.082 → 0.881 | 11x sr_airtime | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.114 → 0.913 | 0.799 | 0.120 → 0.812 | 1.8e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.071 → 0.826 | 0.755 | 0.069 → 0.810 | 5.3x sr_bytes | down | 3 |
| `RF-txpower` | tx-power | **text** | 0.143 → 0.890 | 0.748 | 0.139 → 0.881 | 2.9x advert_bytes | down | 4 |
| `MS-stretch` | stretch | **text** | 0.180 → 0.890 | 0.711 | 0.177 → 0.881 | 3.4x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.321 → 0.970 | 0.649 | 0.315 → 0.970 | 2.2x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **held** | 0.428 → 0.986 | 0.558 | 0.336 → 0.881 | 7.4x bytes_on_air | down | 4 |
| `RF-bw500` | preset | **text** | 0.246 → 0.800 | 0.555 | 0.236 → 0.796 | 1.9x sr_bytes | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.418 → 0.935 | 0.517 | 0.333 → 0.775 | 4.5x bytes_on_air | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.445 → 0.890 | 0.446 | 0.436 → 0.881 | 2.2x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.445 → 0.890 | 0.446 | 0.436 → 0.881 | 2.6x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.582 → 0.956 | 0.374 | 0.568 → 0.954 | 2.4x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.568 → 0.890 | 0.322 | 0.543 → 0.881 | 1.8x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.625 → 0.932 | 0.307 | 0.607 → 0.928 | 9.6x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.585 → 0.890 | 0.306 | 0.552 → 0.881 | 2x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.658 → 0.963 | 0.304 | 0.647 → 0.962 | 5.1x sr_airtime | up | 5 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.603 → 0.905 | 0.302 | 0.583 → 0.899 | 7.3x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.363 → 0.630 | 0.268 | 0.333 → 0.542 | 6.2x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.723 → 0.954 | 0.232 | 0.715 → 0.952 | 4.4x sr_airtime | down | 2 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.552 → 0.782 | 0.231 | 0.537 → 0.764 | 1.5x sr_bytes | up | 2 |
| `MS-size` | nodes | **text** | 0.685 → 0.890 | 0.206 | 0.674 → 0.881 | 3.5x sr_airtime | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.740 → 0.933 | 0.193 | 0.707 → 0.931 | 2.6x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.740 → 0.926 | 0.186 | 0.707 → 0.922 | 2.1x sr_bytes | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.720 → 0.890 | 0.170 | 0.720 → 0.881 | 1.3x sr_airtime | down | 3 |
| `RF-noise` | noise-profile | **held** | 0.831 → 0.986 | 0.155 | 0.729 → 0.881 | 1.8x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.740 → 0.890 | 0.150 | 0.707 → 0.881 | 1.7x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.774 → 0.890 | 0.116 | 0.759 → 0.881 | 1.4x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.826 → 0.938 | 0.112 | 0.810 → 0.933 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.826 → 0.938 | 0.112 | 0.810 → 0.933 | 2.5x bytes_on_air | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.879 → 0.986 | 0.107 | 0.881 → 0.888 | 33x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.836 → 0.926 | 0.089 | 0.825 → 0.922 | 2.1x sr_airtime | up | 4 |
| `SF-cadence` | trigger | **held** | 0.897 → 0.986 | 0.089 | 0.857 → 0.881 | 13x advert_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.807 → 0.890 | 0.084 | 0.791 → 0.881 | 1.1x sr_bytes | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.846 → 0.926 | 0.080 | 0.834 → 0.922 | 2.1x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.914 → 0.990 | 0.076 | 0.874 → 0.884 | 6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.914 → 0.990 | 0.076 | 0.874 → 0.884 | 6x sr_bytes | up | 6 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.890 → 0.966 | 0.076 | 0.881 → 0.963 | 1.8x sr_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.904 → 0.979 | 0.075 | 0.873 → 0.878 | 2.9x sr_bytes | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.782 → 0.846 | 0.064 | 0.665 → 0.710 | 1.3x sr_airtime | down | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.923 → 0.987 | 0.064 | 0.871 → 0.881 | 3.2x sr_bytes | down | 5 |
| `LD-interval` | broadcast-interval-s | **text** | 0.864 → 0.921 | 0.057 | 0.848 → 0.917 | 4.9x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.890 → 0.942 | 0.051 | 0.881 → 0.934 | 1.3x sr_bytes | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.936 → 0.987 | 0.051 | 0.877 → 0.881 | 2.7x sr_bytes | down | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.890 → 0.938 | 0.048 | 0.881 → 0.931 | 1.2x bytes_on_air | up | 3 |
| `MS-roles` | role-mix | **text** | 0.826 → 0.872 | 0.046 | 0.810 → 0.863 | 1.2x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.624 → 0.669 | 0.044 | 0.539 → 0.571 | 1.5x sr_airtime | up | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.842 → 0.884 | 0.042 | 0.834 → 0.878 | 1.1x bytes_on_air | down | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.939 → 0.981 | 0.042 | 0.857 → 0.883 | 9.1x advert_bytes | down | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.877 → 0.919 | 0.042 | 0.871 → 0.917 | 2.1x bytes_on_air | up | 4 |
| `FW-versions` | profile | **text** | 0.890 → 0.928 | 0.038 | 0.881 → 0.926 | 3.4x bytes_on_air | down | 5 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.853 → 0.890 | 0.037 | 0.838 → 0.881 | 1.4x sr_airtime | down | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.882 → 0.910 | 0.029 | 0.879 → 0.908 | 2x bytes_on_air | up | 4 |
| `AD-badrouters` | role-placement | **text** | 0.799 → 0.826 | 0.026 | 0.777 → 0.810 | 1.4x sr_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.890 → 0.916 | 0.026 | 0.868 → 0.881 | 3.5x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.943 → 0.969 | 0.025 | 0.850 → 0.863 | 1.3x sr_airtime | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.890 → 0.913 | 0.022 | 0.881 → 0.906 | 3.3x bytes_on_air | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.894 → 0.914 | 0.020 | 0.884 → 0.909 | 1.2x sr_bytes | up | 2 |
| `FW-firmware` | profile | **text** | 0.890 → 0.909 | 0.019 | 0.881 → 0.906 | 3.3x bytes_on_air | down | 2 |
| `SF-resolve` | resolve | **held** | 0.971 → 0.986 | 0.015 | 0.878 → 0.881 | 5.8x advert_bytes | = | 3 |
| `AD-worst` | role-placement | **text** | 0.869 → 0.883 | 0.014 | 0.864 → 0.881 | 1.1x sr_bytes | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.979 → 0.992 | 0.013 | 0.877 → 0.881 | 4.1x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.979 → 0.992 | 0.013 | 0.877 → 0.881 | 4.1x sr_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.978 → 0.991 | 0.013 | 0.873 → 0.879 | 4.5x advert_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.885 → 0.897 | 0.013 | 0.875 → 0.887 | 1.2x sr_bytes | down | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.854 → 0.864 | 0.010 | 0.854 → 0.864 | 1.1x sr_bytes | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.890 → 0.899 | 0.009 | 0.881 → 0.890 | 1.3x bytes_on_air | up | 4 |
| `SF-width` | short-id-bits | **text** | 0.884 → 0.893 | 0.009 | 0.875 → 0.883 | 3.1x advert_bytes | up | 4 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.856 → 0.864 | 0.008 | 0.856 → 0.864 | 1x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.883 → 0.890 | 0.008 | 0.873 → 0.881 | 2.3x advert_bytes | down | 4 |
| `SF-capacity` | capacity | **held** | 0.979 → 0.986 | 0.007 | 0.874 → 0.881 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.979 → 0.986 | 0.007 | 0.874 → 0.881 | 5.3x advert_bytes | up | 5 |
| `LD-diurnal` | diurnal | **held** | 0.986 → 0.993 | 0.007 | 0.881 → 0.888 | 1.2x advert_bytes | down | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.948 → 0.954 | 0.006 | 0.944 → 0.952 | 1.2x bytes_on_air | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.986 → 0.992 | 0.006 | 0.880 → 0.881 | 1.1x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.890 → 0.895 | 0.005 | 0.881 → 0.886 | 1.1x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.986 → 0.990 | 0.004 | 0.877 → 0.882 | 1.2x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.986 → 0.990 | 0.004 | 0.877 → 0.882 | 1.2x sr_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.883 → 0.887 | 0.004 | 0.871 → 0.877 | 5.6x advert_bytes | up | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.954 → 0.958 | 0.004 | 0.952 → 0.956 | 1x sr_bytes | up | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.881 → 0.884 | 0.003 | 0.879 → 0.884 | 2.5x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.887 → 0.890 | 0.003 | 0.878 → 0.881 | 2.7x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.916 → 0.918 | 0.002 | 0.868 → 0.874 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.954 → 0.956 | 0.002 | 0.952 → 0.954 | 1x sr_airtime | down | 2 |

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
| none | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| sprinkled | 1 | 0.931 | 0.929 | 0.002 | - | - | 0.990 | 0.990 | 0.710 | 1.26x | 20.2/26.0/28.7% | 1.7/5.4% | 3 |
| arms-race | 1 | 0.966 | 0.963 | 0.003 | - | - | 0.995 | 0.995 | 0.904 | 1.02x | 23.9/28.6/30.7% | 1.1/5.5% | 3 |

> amplifier-mix=sprinkled: misdecodes 1

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.1 | 1 | 0.907 | 0.900 | 0.007 | - | - | 0.988 | 0.991 | 0.656 | 1.32x | 19.5/27.3/31.3% | 1.9/5.5% | 3 |
| 0.3 | 1 | 0.938 | 0.931 | 0.007 | - | - | 0.992 | 0.993 | 0.604 | 1.14x | 21.1/27.0/30.4% | 1.7/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.826 | 0.810 | 0.015 | - | - | 0.923 | 0.925 | 0.373 | 1.17x | 17.5/25.6/30.8% | 2.0/5.4% | 3 |
| inverse | 1 | 0.799 | 0.777 | 0.022 | - | - | 0.927 | 0.932 | 0.489 | 1.05x | 13.5/17.9/21.3% | 1.9/3.0% | 3 |
| random | 1 | 0.811 | 0.799 | 0.012 | - | - | 0.922 | 0.925 | 0.455 | 1.18x | 15.8/19.5/25.1% | 2.0/4.6% | 3 |

> role-placement=degree: decode_failures 1

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.826 | 0.810 | 0.015 | - | - | 0.923 | 0.925 | 0.373 | 1.17x | 17.5/25.6/30.8% | 2.0/5.4% | 3 |
| all-routers | 1 | 0.938 | 0.933 | 0.005 | - | - | 0.995 | 0.996 | 0.703 | 2.89x | 37.3/45.2/49.9% | 4.8/5.6% | 3 |

> role-mix=baymesh-2026-08: decode_failures 1

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.826 | 0.810 | 0.015 | - | - | 0.923 | 0.925 | 0.373 | 1.17x | 17.5/25.6/30.8% | 2.0/5.4% | 3 |
| no-mute | 1 | 0.875 | 0.866 | 0.008 | - | - | 0.956 | 0.960 | 0.577 | 1.32x | 18.0/24.2/29.3% | 2.0/5.4% | 3 |
| all-routers | 1 | 0.938 | 0.933 | 0.005 | - | - | 0.995 | 0.996 | 0.703 | 2.89x | 37.3/45.2/49.9% | 4.8/5.6% | 3 |

> role-mix=baymesh-2026-08: decode_failures 1

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.826 | 0.810 | 0.015 | - | - | 0.923 | 0.925 | 0.373 | 1.17x | 17.5/25.6/30.8% | 2.0/5.4% | 3 |
| local-typical | 1 | 0.578 | 0.575 | 0.003 | - | - | 0.720 | 0.724 | 0.000 | 1.25x | 14.2/29.1/31.2% | 2.0/5.4% | 3 |
| basement-heavy | 1 | 0.071 | 0.069 | 0.002 | - | - | 0.249 | 0.251 | 0.000 | 0.64x | 0.9/8.2/14.6% | 0.4/3.6% | 3 |

> siting-mix=uniform: decode_failures 1

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.883 | 0.881 | 0.002 | - | - | 0.981 | 0.981 | 0.000 | 2.21x | 20.2/32.8/38.4% | 1.8/5.7% | 3 |
| inverse | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.981 | 0.981 | 0.000 | 2.05x | 16.8/26.5/32.1% | 1.7/3.3% | 3 |

> role-placement=inverse: misdecodes 1

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.877 | 0.877 | 0.000 | - | - | 0 | 0.000 | 0.538 | 1.35x | 18.9/25.1/31.6% | 2.1/5.2% | 3 |
| sr | 1 | 0.889 | 0.877 | 0.012 | - | - | 0.987 | 0.988 | 0.520 | 1.40x | 19.3/26.1/32.6% | 2.1/5.6% | 3 |

> protocol=sr: decode_failures 1

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.836 | 0.825 | 0.011 | - | - | 0.942 | 0.952 | 0.561 | 3.39x | 43.5/60.7/69.8% | 4.8/10.5% | 3 |
| 100 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.988 | 0.988 | 0.673 | 1.75x | 22.9/33.7/40.5% | 2.6/5.6% | 3 |
| 120 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.988 | 0.988 | 0.673 | 1.75x | 22.9/33.7/40.5% | 2.6/5.6% | 3 |
| 250 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.988 | 0.988 | 0.673 | 1.75x | 22.9/33.7/40.5% | 2.6/5.6% | 3 |

> max-num-nodes=10: decode_failures 10

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.338 | 0.333 | 0.005 | - | - | 0.363 | 0.392 | 0.168 | 11.78x | 40.5/63.4/74.1% | 4.2/10.9% | 3 |
| 120 | 1 | 0.549 | 0.539 | 0.011 | - | - | 0.624 | 0.627 | 0.228 | 4.51x | 15.6/29.8/38.3% | 1.5/5.3% | 3 |
| 250 | 1 | 0.552 | 0.542 | 0.010 | - | - | 0.630 | 0.631 | 0.230 | 4.36x | 15.1/28.3/36.7% | 1.5/5.1% | 3 |

> max-num-nodes=10: decode_failures 53

> max-num-nodes=120: decode_failures 2

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.988 | 0.988 | 0.673 | 1.75x | 22.9/33.7/40.5% | 2.6/5.6% | 3 |
| baymesh-2026-08 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.988 | 0.988 | 0.673 | 1.75x | 22.9/33.7/40.5% | 2.6/5.6% | 3 |
| constrained | 1 | 0.846 | 0.834 | 0.012 | - | - | 0.958 | 0.960 | 0.552 | 3.40x | 43.6/60.7/69.9% | 4.9/10.5% | 3 |

> platform-mix=constrained: decode_failures 3

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.717 | 0.710 | 0.007 | - | - | 0.846 | 0.930 | 0.527 | 5.84x | 60.8/73.9/78.7% | 4.1/13.2% | 3 |
| 25 | 1 | 0.717 | 0.710 | 0.007 | - | - | 0.846 | 0.930 | 0.527 | 5.84x | 60.8/73.9/78.7% | 4.1/13.2% | 3 |
| 100 | 1 | 0.717 | 0.710 | 0.007 | - | - | 0.846 | 0.930 | 0.527 | 5.84x | 60.8/73.9/78.7% | 4.1/13.2% | 3 |
| 2000 | 1 | 0.717 | 0.710 | 0.007 | - | - | 0.846 | 0.930 | 0.527 | 5.84x | 60.8/73.9/78.7% | 4.1/13.2% | 3 |

> warm-num-nodes=0: queue drops 16.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 122

> warm-num-nodes=25: queue drops 16.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 122

> warm-num-nodes=100: queue drops 16.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 122

> warm-num-nodes=2000: queue drops 16.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 122

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.1 | 1 | 0.798 | 0.777 | 0.021 | - | - | 0.961 | 0.967 | 0.441 | 1.32x | 18.6/25.0/31.5% | 2.0/5.2% | 3 |
| 0.2 | 1 | 0.695 | 0.665 | 0.030 | - | - | 0.883 | 0.930 | 0.330 | 1.22x | 17.4/23.4/29.7% | 1.9/4.7% | 3 |
| 0.3 | 1 | 0.585 | 0.552 | 0.032 | - | - | 0.770 | 0.859 | 0.253 | 1.13x | 16.3/22.2/28.3% | 1.7/4.0% | 3 |

> burst-loss=0.2: decode_failures 22

> burst-loss=0.3: decode_failures 35

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.1 | 1 | 0.859 | 0.847 | 0.013 | - | - | 0.979 | 0.980 | 0.478 | 1.48x | 20.6/27.5/34.2% | 2.2/5.6% | 3 |
| 0.2 | 1 | 0.829 | 0.812 | 0.017 | - | - | 0.956 | 0.969 | 0.427 | 1.48x | 20.8/27.7/34.5% | 2.2/5.3% | 3 |
| 0.3 | 1 | 0.774 | 0.759 | 0.015 | - | - | 0.879 | 0.941 | 0.372 | 1.51x | 21.8/28.9/35.9% | 2.2/5.2% | 3 |

> extra-loss=0.2: decode_failures 22

> extra-loss=0.3: decode_failures 33

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.1 | 1 | 0.786 | 0.769 | 0.017 | - | - | 0.912 | 0.964 | 0.396 | 1.30x | 18.4/24.5/30.9% | 1.9/5.2% | 3 |
| 0.2 | 1 | 0.663 | 0.647 | 0.016 | - | - | 0.779 | 0.908 | 0.330 | 1.22x | 17.5/23.6/29.9% | 1.9/4.8% | 3 |
| 0.3 | 1 | 0.568 | 0.543 | 0.025 | - | - | 0.715 | 0.852 | 0.260 | 1.15x | 16.5/23.2/29.3% | 1.7/4.6% | 3 |

> burst-loss=0.1: decode_failures 40

> burst-loss=0.2: decode_failures 39

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.850 | 0.850 | 0.000 | - | - | 0.969 | 0.984 | 0.458 | 1.89x | 25.9/35.3/43.8% | 2.8/7.4% | 3 |
| directed-with-late-flood | 1 | 0.854 | 0.854 | 0.000 | - | - | 0.944 | 0.984 | 0.480 | 1.72x | 23.7/32.3/40.5% | 2.5/6.7% | 3 |
| m4-early-flood | 1 | 0.863 | 0.863 | 0.000 | - | - | 0.943 | 0.989 | 0.501 | 1.70x | 23.5/32.1/40.2% | 2.5/6.7% | 3 |

> dm-mode=flood-only: decode_failures 16

> dm-mode=directed-with-late-flood: decode_failures 39

> dm-mode=m4-early-flood: decode_failures 34

> slower: 11.4 s per simulated hour against 3.14 over 50 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.909 | 0.906 | 0.003 | - | - | 0.993 | 0.994 | 0.719 | 0.76x | 9.5/12.4/13.9% | 1.2/1.8% | 3 |
| 2.8 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.25 | 1 | 0.882 | 0.879 | 0.003 | - | - | 0.976 | 0.977 | 0.451 | 1.27x | 17.8/25.7/29.6% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.900 | 0.892 | 0.007 | - | - | 0.981 | 0.988 | 0.713 | 1.08x | 13.6/19.7/22.5% | 1.7/4.2% | 3 |
| 0.75 | 1 | 0.910 | 0.908 | 0.003 | - | - | 0.990 | 0.992 | 0.725 | 0.97x | 12.9/17.6/19.1% | 1.5/3.8% | 3 |

> legacy-fraction=0.5: decode_failures 14

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.25 | 1 | 0.877 | 0.871 | 0.006 | - | - | 0.971 | 0.974 | 0.447 | 1.25x | 17.6/25.5/29.4% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.904 | 0.895 | 0.009 | - | - | 0.991 | 0.992 | 0.713 | 1.07x | 13.7/19.9/22.6% | 1.7/4.3% | 3 |
| 0.75 | 1 | 0.919 | 0.917 | 0.002 | - | - | 0.995 | 0.996 | 0.737 | 0.94x | 12.5/17.3/18.9% | 1.4/3.8% | 3 |

> legacy-fraction=0.5: decode_failures 2

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.913 | 0.906 | 0.007 | - | - | 0.992 | 0.994 | 0.549 | 0.73x | 10.5/14.4/18.7% | 1.1/3.2% | 3 |
| signing=true | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.992 | 0.993 | 0.685 | 0.77x | 10.0/13.4/15.6% | 1.2/2.4% | 3 |
| 2.5 | 1 | 0.907 | 0.904 | 0.003 | - | - | 0.992 | 0.992 | 0.692 | 0.77x | 10.0/13.4/15.3% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.904 | 0.902 | 0.002 | - | - | 0.987 | 0.989 | 0.709 | 0.73x | 9.8/13.1/15.5% | 1.2/2.4% | 3 |
| 2.7 | 1 | 0.928 | 0.926 | 0.002 | - | - | 0.996 | 0.996 | 0.709 | 0.81x | 10.4/16.4/19.3% | 1.2/3.2% | 3 |
| 2.8 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.905 | 0.899 | 0.007 | - | - | 0.993 | 0.994 | 0.558 | 0.94x | 13.1/17.4/22.0% | 1.4/3.8% | 3 |
| 900 | 1 | 0.864 | 0.848 | 0.016 | - | - | 0.990 | 0.990 | 0.469 | 2.18x | 30.0/40.4/50.1% | 3.3/8.6% | 3 |
| 300 | 1 | 0.603 | 0.583 | 0.021 | - | - | 0.765 | 0.846 | 0.263 | 4.64x | 57.2/72.0/80.5% | 7.3/15.9% | 3 |

> broadcast-interval-s=300: decode_failures 43

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.932 | 0.928 | 0.004 | - | - | 0.984 | 0.984 | 0.724 | 0.99x | 13.1/17.2/21.9% | 1.6/3.6% | 3 |
| 900 | 1 | 0.893 | 0.887 | 0.006 | - | - | 0.956 | 0.959 | 0.688 | 2.44x | 32.4/41.9/51.8% | 3.9/8.7% | 3 |
| 300 | 1 | 0.625 | 0.607 | 0.017 | - | - | 0.745 | 0.757 | 0.398 | 5.16x | 61.9/73.4/80.7% | 8.0/16.7% | 3 |

> broadcast-interval-s=300: queue drops 10.7% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 16

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.989 | 0.989 | 0.515 | 1.28x | 17.9/24.0/30.3% | 2.0/5.1% | 3 |
| sinusoid | 1 | 0.894 | 0.885 | 0.009 | - | - | 0.993 | 0.993 | 0.486 | 1.23x | 17.2/23.1/29.1% | 1.9/4.9% | 3 |
| commuter | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.864 | 0.848 | 0.016 | - | - | 0.990 | 0.990 | 0.469 | 2.18x | 30.0/40.4/50.1% | 3.3/8.6% | 3 |
| 3600 | 1 | 0.905 | 0.899 | 0.007 | - | - | 0.993 | 0.994 | 0.558 | 0.94x | 13.1/17.4/22.0% | 1.4/3.8% | 3 |
| 10800 | 1 | 0.917 | 0.911 | 0.005 | - | - | 0.992 | 0.995 | 0.574 | 0.63x | 8.7/11.8/14.8% | 1.0/2.6% | 3 |
| 43200 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.994 | 0.997 | 0.586 | 0.43x | 6.0/8.0/10.0% | 0.6/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.25 | 1 | 0.887 | 0.877 | 0.010 | - | - | 0.990 | 0.991 | 0.507 | 1.42x | 19.8/26.8/33.6% | 2.1/5.8% | 3 |
| 1.0 | 1 | 0.881 | 0.868 | 0.013 | - | - | 0.996 | 0.998 | 0.501 | 1.59x | 22.2/29.9/37.5% | 2.4/6.5% | 3 |
| 4.0 | 1 | 0.853 | 0.838 | 0.015 | - | - | 0.975 | 0.978 | 0.462 | 2.00x | 27.8/38.1/48.0% | 2.9/8.2% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.717 | 0.710 | 0.007 | - | - | 0.846 | 0.930 | 0.527 | 5.84x | 60.8/73.9/78.7% | 4.1/13.2% | 3 |
| 1.0 | 1 | 0.670 | 0.665 | 0.005 | - | - | 0.782 | 0.890 | 0.482 | 6.27x | 63.4/75.7/79.9% | 4.4/14.4% | 3 |

> traceroute-per-hour=0.0: queue drops 16.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 122

> traceroute-per-hour=1.0: queue drops 23.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 116

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.658 | 0.647 | 0.011 | - | - | 0.809 | 0.822 | 0.109 | 1.18x | 19.9/29.7/32.3% | 2.7/6.8% | 3 |
| 60 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 90 | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.997 | 0.997 | 0.847 | 1.65x | 20.4/29.5/33.5% | 1.5/5.1% | 3 |
| 120 | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.822 | 2.00x | 22.7/35.0/40.0% | 1.3/5.1% | 3 |
| 150 | 1 | 0.963 | 0.962 | 0.001 | - | - | 0.999 | 0.999 | 0.808 | 2.58x | 26.4/42.5/49.1% | 1.3/5.3% | 3 |

> nodes=40: decode_failures 1

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 120 | 1 | 0.788 | 0.780 | 0.008 | - | - | 0.939 | 0.939 | 0.168 | 2.23x | 16.1/30.1/34.2% | 1.6/4.8% | 3 |
| 250 | 1 | 0.559 | 0.549 | 0.010 | - | - | 0.640 | 0.642 | 0.229 | 4.76x | 16.5/31.4/40.6% | 1.6/5.8% | 3 |
| 500 | 1 | 0.340 | 0.336 | 0.004 | - | - | 0.428 | 0.429 | 0.078 | 10.07x | 18.7/34.2/48.0% | 1.6/7.0% | 3 |

> nodes=500: decode_failures 4

> faster: 8.72 s per simulated hour against 18 over 50 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.783 | 0.775 | 0.008 | - | - | 0.935 | 0.936 | 0.184 | 2.13x | 15.4/29.2/33.0% | 1.5/4.6% | 3 |
| 250 | 1 | 0.549 | 0.539 | 0.011 | - | - | 0.624 | 0.627 | 0.228 | 4.51x | 15.6/29.8/38.3% | 1.5/5.3% | 3 |
| 500 | 1 | 0.338 | 0.333 | 0.004 | - | - | 0.418 | 0.418 | 0.075 | 9.54x | 17.8/32.5/44.6% | 1.5/6.3% | 3 |

> nodes=250: decode_failures 2

> faster: 9.2 s per simulated hour against 20.5 over 50 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.872 | 0.863 | 0.008 | - | - | 0.951 | 0.953 | 0.546 | 1.38x | 19.0/25.5/32.1% | 2.1/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.826 | 0.810 | 0.015 | - | - | 0.923 | 0.925 | 0.373 | 1.17x | 17.5/25.6/30.8% | 2.0/5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 1

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.884 | 0.878 | 0.005 | - | - | 0.949 | 0.953 | 0.617 | 1.43x | 19.6/26.1/32.7% | 2.2/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.842 | 0.834 | 0.007 | - | - | 0.916 | 0.918 | 0.432 | 1.31x | 19.4/28.9/34.4% | 2.2/5.4% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.05 | 1 | 0.895 | 0.886 | 0.009 | - | - | 0.988 | 0.991 | 0.530 | 1.52x | 20.3/30.1/38.3% | 2.3/5.5% | 3 |
| 0.1 | 1 | 0.898 | 0.889 | 0.009 | - | - | 0.985 | 0.988 | 0.549 | 1.67x | 22.5/34.7/42.4% | 2.5/5.5% | 3 |
| 0.2 | 1 | 0.899 | 0.890 | 0.010 | - | - | 0.985 | 0.987 | 0.545 | 1.86x | 26.1/41.2/48.1% | 2.5/5.5% | 3 |

> router-late-fraction=0.1: decode_failures 1

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| local-typical | 1 | 0.635 | 0.632 | 0.002 | - | - | 0.805 | 0.807 | 0.000 | 1.47x | 15.9/30.3/35.1% | 2.3/5.5% | 3 |
| event | 1 | 0.321 | 0.315 | 0.007 | - | - | 0.651 | 0.653 | 0.000 | 1.52x | 10.0/25.5/35.7% | 1.9/6.4% | 3 |
| backbone | 1 | 0.970 | 0.970 | 0.001 | - | - | 0.996 | 0.997 | 0.829 | 1.19x | 29.6/36.4/40.5% | 1.5/5.8% | 3 |

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.846 | 0.834 | 0.012 | - | - | 0.937 | 0.945 | 0.169 | 1.45x | 27.3/35.6/38.9% | 3.2/7.7% | 3 |
| 60 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 90 | 1 | 0.883 | 0.878 | 0.005 | - | - | 0.971 | 0.971 | 0.615 | 1.79x | 16.7/29.3/33.4% | 1.7/5.4% | 3 |
| 120 | 1 | 0.788 | 0.780 | 0.008 | - | - | 0.939 | 0.939 | 0.168 | 2.23x | 16.1/30.1/34.2% | 1.6/4.8% | 3 |
| 150 | 1 | 0.685 | 0.674 | 0.011 | - | - | 0.864 | 0.864 | 0.276 | 2.74x | 15.1/29.8/41.0% | 1.5/5.4% | 3 |

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 1.25 | 1 | 0.640 | 0.630 | 0.011 | - | - | 0.852 | 0.853 | 0.160 | 1.33x | 12.7/19.3/23.2% | 2.0/4.8% | 3 |
| 1.5 | 1 | 0.552 | 0.537 | 0.015 | - | - | 0.851 | 0.860 | 0.047 | 1.44x | 10.9/17.9/23.0% | 2.3/5.0% | 3 |
| 2.0 | 1 | 0.180 | 0.177 | 0.003 | - | - | 0.414 | 0.422 | 0.000 | 1.09x | 5.4/10.8/13.7% | 1.8/4.0% | 3 |

> stretch=1.5: decode_failures 2

> stretch=2.0: decode_failures 1

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| clustered | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.959 | 0.963 | 0.294 | 1.19x | 20.5/34.4/35.4% | 1.8/5.3% | 3 |
| corridor | 1 | 0.582 | 0.568 | 0.014 | - | - | 0.833 | 0.834 | 0.310 | 1.39x | 16.6/24.8/28.5% | 2.0/5.0% | 3 |
| hub | 1 | 0.956 | 0.954 | 0.002 | - | - | 0.989 | 0.989 | 0.841 | 1.14x | 24.0/33.1/34.5% | 1.7/5.4% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.854 | 0.854 | 0.000 | - | - | 0.944 | 0.984 | 0.480 | 1.72x | 23.7/32.3/40.5% | 2.5/6.7% | 3 |
| True | 1 | 0.864 | 0.864 | 0.000 | - | - | 0.941 | 0.990 | 0.496 | 1.68x | 23.2/31.6/39.6% | 2.5/6.7% | 3 |

> coding-rate-ladder=False: decode_failures 39

> coding-rate-ladder=True: decode_failures 33

> slower: 13 s per simulated hour against 2.77 over 50 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.864 | 0.864 | 0.000 | - | - | 0.941 | 0.990 | 0.496 | 1.68x | 23.2/31.6/39.6% | 2.5/6.7% | 3 |
| m4-early-flood | 1 | 0.856 | 0.856 | 0.000 | - | - | 0.936 | 0.990 | 0.488 | 1.69x | 23.4/32.1/40.1% | 2.5/6.8% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 33

> dm-mode=m4-early-flood: decode_failures 46

> slower: 13.6 s per simulated hour against 2.57 over 50 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.877 | 0.877 | 0.000 | - | - | 0 | 0.000 | 0.538 | 1.35x | 18.9/25.1/31.6% | 2.1/5.2% | 3 |
| chain | 1 | 0.881 | 0.879 | 0.002 | - | - | 0.894 | 0.993 | 0.515 | 1.62x | 22.3/29.9/37.5% | 2.5/6.3% | 3 |
| sr | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| True | 1 | 0.895 | 0.886 | 0.010 | - | - | 0.986 | 0.990 | 0.537 | 1.42x | 19.6/26.2/33.0% | 2.2/5.6% | 3 |

> extra-repeats=True: decode_failures 1

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.822 | 2.00x | 22.7/35.0/40.0% | 1.3/5.1% | 3 |
| True | 1 | 0.958 | 0.956 | 0.002 | - | - | 0.999 | 0.999 | 0.827 | 2.05x | 23.0/35.4/40.4% | 1.3/5.1% | 3 |

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.246 | 0.236 | 0.009 | - | - | 0.572 | 0.578 | 0.000 | 0.06x | 0.3/0.7/1.1% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.552 | 0.545 | 0.007 | - | - | 0.914 | 0.916 | 0.000 | 0.31x | 2.2/5.1/6.0% | 0.5/1.3% | 3 |
| LONG_TURBO | 1 | 0.800 | 0.796 | 0.005 | - | - | 0.970 | 0.971 | 0.286 | 1.31x | 14.7/21.7/24.6% | 2.0/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 0.25 | 1 | 0.905 | 0.894 | 0.011 | - | - | 0.988 | 0.991 | 0.589 | 1.34x | 21.0/27.2/33.3% | 2.0/5.7% | 3 |
| 1.0 | 1 | 0.942 | 0.934 | 0.008 | - | - | 0.996 | 0.996 | 0.717 | 1.11x | 23.6/29.7/33.9% | 1.5/5.7% | 3 |

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.445 | 0.436 | 0.009 | - | - | 0.828 | 0.830 | 0.000 | 0.16x | 1.2/2.5/3.0% | 0.3/0.7% | 3 |
| LONG_FAST | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| LITE_FAST | 1 | 0.829 | 0.825 | 0.004 | - | - | 0.977 | 0.977 | 0.326 | 1.07x | 12.4/19.6/24.5% | 1.6/4.1% | 3 |
| NARROW_SLOW | 1 | 0.857 | 0.854 | 0.003 | - | - | 0.979 | 0.979 | 0.411 | 1.38x | 17.1/25.6/31.0% | 2.1/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| temporal | 1 | 0.815 | 0.801 | 0.013 | - | - | 0.888 | 0.974 | 0.310 | 1.39x | 18.5/26.2/32.3% | 2.1/5.5% | 3 |
| transient | 1 | 0.890 | 0.879 | 0.010 | - | - | 0.984 | 0.992 | 0.523 | 1.42x | 19.5/26.1/32.9% | 2.1/5.6% | 3 |
| periodic | 1 | 0.738 | 0.729 | 0.009 | - | - | 0.831 | 0.844 | 0.389 | 1.27x | 17.9/23.8/29.9% | 1.9/4.8% | 3 |

> noise-profile=temporal: decode_failures 44

> noise-profile=transient: decode_failures 9

> noise-profile=periodic: decode_failures 9

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.445 | 0.436 | 0.009 | - | - | 0.828 | 0.830 | 0.000 | 0.16x | 1.2/2.5/3.0% | 0.3/0.7% | 3 |
| LONG_FAST | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| LONG_MODERATE | 1 | 0.836 | 0.820 | 0.016 | - | - | 0.949 | 0.951 | 0.613 | 3.67x | 55.2/65.6/71.2% | 5.5/12.9% | 3 |

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.082 | 0.082 | 0.000 | - | - | 0.106 | 0.113 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.246 | 0.236 | 0.009 | - | - | 0.572 | 0.578 | 0.000 | 0.06x | 0.3/0.7/1.1% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| LONG_TURBO | 1 | 0.800 | 0.796 | 0.005 | - | - | 0.970 | 0.971 | 0.286 | 1.31x | 14.7/21.7/24.6% | 2.0/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.984 | 0.984 | 0.583 | 1.99x | 24.1/36.0/42.8% | 2.9/7.1% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 3

> preset=SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.823 | 0.812 | 0.011 | - | - | 0.913 | 0.929 | 0.453 | 1.36x | 18.9/25.4/31.9% | 2.0/5.3% | 3 |
| 10000 | 1 | 0.738 | 0.729 | 0.009 | - | - | 0.831 | 0.844 | 0.389 | 1.27x | 17.9/23.8/29.9% | 1.9/4.8% | 3 |
| 4000 | 1 | 0.478 | 0.472 | 0.006 | - | - | 0.524 | 0.613 | 0.204 | 1.10x | 15.9/21.3/26.6% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.120 | 0.120 | 0.000 | - | - | 0.114 | 0.205 | 0.040 | 0.75x | 11.0/15.4/19.4% | 1.2/2.0% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 38

> noise-pulse-interval-ms=10000: decode_failures 9

> noise-pulse-interval-ms=4000: decode_failures 9

> slower: 4.28 s per simulated hour against 1.62 over 50 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.552 | 0.537 | 0.015 | - | - | 0.851 | 0.860 | 0.047 | 1.44x | 10.9/17.9/23.0% | 2.3/5.0% | 3 |
| 1.0 | 1 | 0.782 | 0.764 | 0.018 | - | - | 0.933 | 0.940 | 0.526 | 1.20x | 17.0/23.5/26.6% | 1.7/5.1% | 3 |

> duct-per-hour=0.0: decode_failures 2

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 22 | 1 | 0.508 | 0.499 | 0.009 | - | - | 0.855 | 0.857 | 0.000 | 1.37x | 10.6/20.2/23.2% | 2.2/5.3% | 3 |
| 17 | 1 | 0.224 | 0.220 | 0.004 | - | - | 0.513 | 0.517 | 0.000 | 1.23x | 6.5/13.2/21.6% | 1.9/4.7% | 3 |
| 14 | 1 | 0.143 | 0.139 | 0.004 | - | - | 0.344 | 0.393 | 0.000 | 0.91x | 3.8/8.5/14.9% | 1.3/3.6% | 3 |

> tx-power=14: decode_failures 19

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.822 | 2.00x | 22.7/35.0/40.0% | 1.3/5.1% | 3 |
| True | 1 | 0.948 | 0.944 | 0.004 | - | - | 0.997 | 0.997 | 0.801 | 2.40x | 26.7/39.7/45.1% | 1.6/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.894 | 0.884 | 0.010 | - | - | 0.991 | 0.992 | 0.522 | 1.51x | 20.2/29.3/36.8% | 2.4/5.5% | 3 |
| True | 1 | 0.914 | 0.909 | 0.005 | - | - | 0.984 | 0.986 | 0.639 | 1.61x | 21.4/30.6/38.0% | 2.5/5.5% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| random | 1 | 0.807 | 0.791 | 0.015 | - | - | 0.922 | 0.924 | 0.547 | 1.28x | 17.7/23.6/29.7% | 2.0/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.740 | 0.707 | 0.033 | - | - | 0.894 | 0.900 | 0.350 | 1.06x | 14.9/20.8/26.4% | 1.5/4.8% | 3 |
| 7 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.984 | 0.984 | 0.723 | 1.55x | 20.5/26.8/33.8% | 2.5/5.5% | 3 |
| 15 | 1 | 0.928 | 0.927 | 0.002 | - | - | 0.969 | 0.970 | 0.729 | 1.56x | 20.7/26.8/33.9% | 2.5/5.5% | 3 |
| 32 | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.976 | 0.977 | 0.726 | 1.56x | 20.7/27.0/33.9% | 2.5/5.5% | 3 |

> hop-limit=3: decode_failures 9

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.740 | 0.707 | 0.033 | - | - | 0.894 | 0.900 | 0.350 | 1.06x | 14.9/20.8/26.4% | 1.5/4.8% | 3 |
| 5 | 1 | 0.877 | 0.865 | 0.012 | - | - | 0.967 | 0.968 | 0.575 | 1.38x | 18.9/24.9/31.6% | 2.1/5.3% | 3 |
| 7 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.984 | 0.984 | 0.723 | 1.55x | 20.5/26.8/33.8% | 2.5/5.5% | 3 |

> hop-limit=3: decode_failures 9

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| KNOWN_ONLY | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.888 | 0.888 | 0.000 | - | - | 0.879 | 0.993 | 0.526 | 1.37x | 19.1/25.4/32.0% | 2.1/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.740 | 0.707 | 0.033 | - | - | 0.894 | 0.900 | 0.350 | 1.06x | 14.9/20.8/26.4% | 1.5/4.8% | 3 |
| True | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

> hop-spread=False: decode_failures 9

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| BALANCED | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| STRICT | 1 | 0.720 | 0.720 | 0.000 | - | - | 0.823 | 0.824 | 0.375 | 1.48x | 20.5/27.3/34.3% | 2.3/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| dm | 1 | 0.887 | 0.878 | 0.009 | - | - | 0.987 | 0.988 | 0.504 | 1.38x | 19.1/25.8/32.5% | 2.1/5.6% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.888 | 0.878 | 0.010 | - | - | 0.986 | 0.992 | 0.516 | 1.40x | 19.4/26.0/32.8% | 2.1/5.6% | 3 |
| local | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| time | 1 | 0.887 | 0.877 | 0.010 | - | - | 0.984 | 0.987 | 0.516 | 1.42x | 19.6/26.3/33.0% | 2.2/5.7% | 3 |
| window | 1 | 0.883 | 0.873 | 0.010 | - | - | 0.979 | 0.984 | 0.507 | 1.42x | 19.7/26.5/33.3% | 2.2/5.7% | 3 |

> bucket-mode=global: misdecodes 41

> bucket-mode=time: misdecodes 18

> bucket-mode=window: misdecodes 19

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.883 | 0.871 | 0.012 | - | - | 0.987 | 0.990 | 0.492 | 1.56x | 21.2/28.6/35.7% | 2.4/6.3% | 3 |
| 1800 | 1 | 0.887 | 0.877 | 0.010 | - | - | 0.984 | 0.987 | 0.516 | 1.42x | 19.6/26.3/33.0% | 2.2/5.7% | 3 |
| 3600 | 1 | 0.886 | 0.876 | 0.010 | - | - | 0.986 | 0.990 | 0.515 | 1.40x | 19.4/26.0/32.7% | 2.1/5.6% | 3 |

> time-bucket-s=600: misdecodes 107

> time-bucket-s=1800: misdecodes 18

> time-bucket-s=3600: misdecodes 4

> time-bucket-s=3600: decode_failures 4

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| interval | 1 | 0.873 | 0.859 | 0.013 | - | - | 0.977 | 0.992 | 0.502 | 1.87x | 25.0/34.0/41.7% | 2.8/7.7% | 3 |
| aimd | 1 | 0.880 | 0.877 | 0.003 | - | - | 0.897 | 0.988 | 0.508 | 1.42x | 19.6/26.1/32.8% | 2.2/5.5% | 3 |
| bucket+interval | 1 | 0.872 | 0.857 | 0.014 | - | - | 0.981 | 0.984 | 0.487 | 1.91x | 25.7/34.8/42.5% | 2.8/7.8% | 3 |

> trigger=interval: misdecodes 12

> trigger=interval: decode_failures 20

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 14

> trigger=bucket+interval: misdecodes 17

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.888 | 0.878 | 0.011 | - | - | 0.980 | 0.989 | 0.523 | 1.40x | 19.3/26.0/32.7% | 2.1/5.6% | 3 |
| 8 | 1 | 0.885 | 0.875 | 0.011 | - | - | 0.979 | 0.985 | 0.509 | 1.39x | 19.2/25.8/32.4% | 2.1/5.6% | 3 |
| 16 | 1 | 0.885 | 0.874 | 0.012 | - | - | 0.985 | 0.992 | 0.494 | 1.39x | 19.2/25.8/32.3% | 2.1/5.6% | 3 |
| 32 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 50 | 1 | 0.884 | 0.875 | 0.009 | - | - | 0.983 | 0.984 | 0.523 | 1.42x | 19.6/26.3/33.1% | 2.1/5.6% | 3 |

> capacity=4: decode_failures 106

> capacity=8: decode_failures 81

> capacity=16: decode_failures 67

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.888 | 0.878 | 0.011 | - | - | 0.980 | 0.989 | 0.523 | 1.40x | 19.3/26.0/32.7% | 2.1/5.6% | 3 |
| 8 | 1 | 0.885 | 0.875 | 0.011 | - | - | 0.979 | 0.985 | 0.509 | 1.39x | 19.2/25.8/32.4% | 2.1/5.6% | 3 |
| 16 | 1 | 0.885 | 0.874 | 0.012 | - | - | 0.985 | 0.992 | 0.494 | 1.39x | 19.2/25.8/32.3% | 2.1/5.6% | 3 |
| 32 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 50 | 1 | 0.884 | 0.875 | 0.009 | - | - | 0.983 | 0.984 | 0.523 | 1.42x | 19.6/26.3/33.1% | 2.1/5.6% | 3 |

> capacity=4: decode_failures 106

> capacity=8: decode_failures 81

> capacity=16: decode_failures 67

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.878 | 0.875 | 0.004 | - | - | 0.904 | 0.991 | 0.515 | 1.38x | 19.1/25.7/32.4% | 2.1/5.4% | 3 |
| 16 | 1 | 0.888 | 0.878 | 0.010 | - | - | 0.979 | 0.992 | 0.497 | 1.40x | 19.4/26.1/32.7% | 2.1/5.5% | 3 |
| 32 | 1 | 0.883 | 0.873 | 0.010 | - | - | 0.979 | 0.984 | 0.507 | 1.42x | 19.7/26.5/33.3% | 2.2/5.7% | 3 |

> capacity=8: misdecodes 9

> capacity=8: decode_failures 119

> capacity=16: misdecodes 21

> capacity=16: decode_failures 14

> capacity=32: misdecodes 19

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.872 | 0.857 | 0.014 | - | - | 0.981 | 0.984 | 0.487 | 1.91x | 25.7/34.8/42.5% | 2.8/7.8% | 3 |
| 02-06 | 1 | 0.889 | 0.883 | 0.006 | - | - | 0.939 | 0.989 | 0.515 | 1.43x | 19.7/26.7/33.3% | 2.2/5.7% | 3 |
| 00-08 | 1 | 0.887 | 0.881 | 0.007 | - | - | 0.940 | 0.991 | 0.526 | 1.50x | 20.4/27.8/34.5% | 2.3/6.0% | 3 |

> catch-up-hours=: misdecodes 17

> catch-up-hours=02-06: misdecodes 1

> catch-up-hours=02-06: decode_failures 53

> catch-up-hours=00-08: decode_failures 53

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.881 | 0.877 | 0.003 | - | - | 0.979 | 0.979 | 0.514 | 1.41x | 19.6/26.2/32.8% | 2.2/5.5% | 3 |
| 2 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 3 | 1 | 0.889 | 0.877 | 0.012 | - | - | 0.987 | 0.988 | 0.520 | 1.40x | 19.3/26.1/32.6% | 2.1/5.6% | 3 |
| 4 | 1 | 0.899 | 0.877 | 0.022 | - | - | 0.936 | 0.994 | 0.566 | 1.40x | 19.4/26.0/32.5% | 2.1/5.5% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 32

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.881 | 0.877 | 0.003 | - | - | 0.979 | 0.979 | 0.514 | 1.41x | 19.6/26.2/32.8% | 2.2/5.5% | 3 |
| 2 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 3 | 1 | 0.889 | 0.877 | 0.012 | - | - | 0.987 | 0.988 | 0.520 | 1.40x | 19.3/26.1/32.6% | 2.1/5.6% | 3 |
| 4 | 1 | 0.899 | 0.877 | 0.022 | - | - | 0.936 | 0.994 | 0.566 | 1.40x | 19.4/26.0/32.5% | 2.1/5.5% | 3 |
| 5 | 1 | 0.893 | 0.871 | 0.022 | - | - | 0.923 | 0.993 | 0.573 | 1.42x | 19.6/26.4/32.9% | 2.2/5.6% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 32

> hops-apart=5: decode_failures 34

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.987 | 0.989 | 0.527 | 1.40x | 19.3/25.9/32.6% | 2.1/5.6% | 3 |
| 30 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 120 | 1 | 0.892 | 0.882 | 0.009 | - | - | 0.990 | 0.993 | 0.516 | 1.42x | 19.6/26.4/33.1% | 2.1/5.7% | 3 |
| 600 | 1 | 0.889 | 0.877 | 0.011 | - | - | 0.989 | 0.991 | 0.511 | 1.39x | 19.2/26.0/32.5% | 2.1/5.6% | 3 |

> advert-jitter-s=600: decode_failures 1

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.987 | 0.989 | 0.527 | 1.40x | 19.3/25.9/32.6% | 2.1/5.6% | 3 |
| 30 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 120 | 1 | 0.892 | 0.882 | 0.009 | - | - | 0.990 | 0.993 | 0.516 | 1.42x | 19.6/26.4/33.1% | 2.1/5.7% | 3 |
| 600 | 1 | 0.889 | 0.877 | 0.011 | - | - | 0.989 | 0.991 | 0.511 | 1.39x | 19.2/26.0/32.5% | 2.1/5.6% | 3 |

> advert-jitter-s=600: decode_failures 1

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.906 | 0.877 | 0.029 | - | - | 0.914 | 0.969 | 0.573 | 1.41x | 19.5/25.8/32.3% | 2.1/5.5% | 3 |
| routers | 1 | 0.884 | 0.884 | 0.001 | - | - | 0.982 | 0.982 | 0.515 | 1.38x | 19.3/26.0/32.7% | 2.1/5.4% | 3 |
| alternate-routers | 1 | 0.885 | 0.883 | 0.002 | - | - | 0.985 | 0.985 | 0.524 | 1.41x | 19.5/26.5/33.2% | 2.1/5.5% | 3 |
| beside-router | 1 | 0.876 | 0.874 | 0.002 | - | - | 0.979 | 0.979 | 0.523 | 1.41x | 19.7/26.4/33.1% | 2.1/5.5% | 3 |
| random-clients | 1 | 0.892 | 0.884 | 0.008 | - | - | 0.990 | 0.990 | 0.540 | 1.42x | 19.7/26.5/33.3% | 2.2/5.5% | 3 |
| hops-apart | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

> place=spread: decode_failures 37

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.906 | 0.877 | 0.029 | - | - | 0.914 | 0.969 | 0.573 | 1.41x | 19.5/25.8/32.3% | 2.1/5.5% | 3 |
| routers | 1 | 0.884 | 0.884 | 0.001 | - | - | 0.982 | 0.982 | 0.515 | 1.38x | 19.3/26.0/32.7% | 2.1/5.4% | 3 |
| alternate-routers | 1 | 0.885 | 0.883 | 0.002 | - | - | 0.985 | 0.985 | 0.524 | 1.41x | 19.5/26.5/33.2% | 2.1/5.5% | 3 |
| beside-router | 1 | 0.876 | 0.874 | 0.002 | - | - | 0.979 | 0.979 | 0.523 | 1.41x | 19.7/26.4/33.1% | 2.1/5.5% | 3 |
| random-clients | 1 | 0.892 | 0.884 | 0.008 | - | - | 0.990 | 0.990 | 0.540 | 1.42x | 19.7/26.5/33.3% | 2.2/5.5% | 3 |
| hops-apart | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

> place=spread: decode_failures 37

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| broadcast | 1 | 0.916 | 0.868 | 0.049 | - | - | 0.988 | 0.991 | 0.624 | 1.54x | 21.1/28.3/35.3% | 2.4/6.0% | 3 |

> provide-transport=broadcast: decode_failures 3

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| heard | 1 | 0.890 | 0.880 | 0.011 | - | - | 0.992 | 0.994 | 0.517 | 1.41x | 19.6/26.2/32.9% | 2.2/5.6% | 3 |

> replay-ordering=heard: misdecodes 18

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.916 | 0.868 | 0.049 | - | - | 0.988 | 0.991 | 0.624 | 1.54x | 21.1/28.3/35.3% | 2.4/6.0% | 3 |
| heard | 1 | 0.918 | 0.874 | 0.044 | - | - | 0.987 | 0.989 | 0.639 | 1.53x | 20.9/28.3/35.1% | 2.3/5.9% | 3 |

> replay-ordering=tip: decode_failures 3

> replay-ordering=heard: misdecodes 2

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| enum | 1 | 0.888 | 0.878 | 0.010 | - | - | 0.971 | 0.988 | 0.533 | 1.40x | 19.3/26.1/32.7% | 2.1/5.7% | 3 |
| hybrid | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.884 | 0.884 | 0.001 | - | - | 0.982 | 0.982 | 0.515 | 1.38x | 19.3/26.0/32.7% | 2.1/5.4% | 3 |
| 6 | 1 | 0.881 | 0.879 | 0.002 | - | - | 0.985 | 0.985 | 0.513 | 1.43x | 19.8/26.8/33.5% | 2.2/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.885 | 0.878 | 0.006 | - | - | 0.979 | 0.979 | 0.535 | 1.39x | 19.3/25.9/32.5% | 2.1/5.6% | 2 |
| 3 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 5 | 1 | 0.889 | 0.877 | 0.012 | - | - | 0.991 | 0.993 | 0.519 | 1.43x | 19.7/26.5/33.3% | 2.1/5.7% | 5 |
| 8 | 1 | 0.891 | 0.877 | 0.015 | - | - | 0.992 | 0.994 | 0.530 | 1.50x | 20.6/27.7/34.7% | 2.2/6.0% | 8 |

> servers=2: decode_failures 2

> servers=8: misdecodes 5

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.885 | 0.878 | 0.006 | - | - | 0.979 | 0.979 | 0.535 | 1.39x | 19.3/25.9/32.5% | 2.1/5.6% | 2 |
| 3 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 5 | 1 | 0.889 | 0.877 | 0.012 | - | - | 0.991 | 0.993 | 0.519 | 1.43x | 19.7/26.5/33.3% | 2.1/5.7% | 5 |
| 8 | 1 | 0.891 | 0.877 | 0.015 | - | - | 0.992 | 0.994 | 0.530 | 1.50x | 20.6/27.7/34.7% | 2.2/6.0% | 8 |

> servers=2: decode_failures 2

> servers=8: misdecodes 5

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| True | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.897 | 0.887 | 0.010 | - | - | 0.990 | 0.995 | 0.531 | 1.30x | 18.1/24.2/30.5% | 2.0/5.1% | 3 |
| 1 | 1 | 0.894 | 0.885 | 0.009 | - | - | 0.987 | 0.989 | 0.542 | 1.28x | 17.8/23.6/29.9% | 1.9/5.0% | 3 |
| 2 | 1 | 0.889 | 0.880 | 0.009 | - | - | 0.987 | 0.989 | 0.543 | 1.30x | 18.0/24.2/30.4% | 2.0/5.1% | 3 |
| 4 | 1 | 0.885 | 0.875 | 0.009 | - | - | 0.988 | 0.989 | 0.534 | 1.29x | 17.9/23.9/30.1% | 2.0/5.1% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.891 | 0.881 | 0.010 | - | - | 0.986 | 0.988 | 0.516 | 1.39x | 19.3/25.9/32.6% | 2.1/5.6% | 3 |
| 24 | 1 | 0.884 | 0.875 | 0.009 | - | - | 0.986 | 0.988 | 0.500 | 1.42x | 19.6/26.5/33.2% | 2.2/5.7% | 3 |
| 32 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.986 | 0.988 | 0.510 | 1.40x | 19.4/26.1/32.7% | 2.1/5.6% | 3 |
| 64 | 1 | 0.893 | 0.883 | 0.010 | - | - | 0.989 | 0.992 | 0.500 | 1.43x | 19.8/26.5/33.2% | 2.2/5.7% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.891 | 0.879 | 0.012 | - | - | 0.991 | 0.993 | 0.523 | 1.51x | 20.7/28.0/34.8% | 2.3/6.0% | 3 |
| 16 | 1 | 0.884 | 0.875 | 0.009 | - | - | 0.978 | 0.984 | 0.503 | 1.44x | 20.0/26.9/33.7% | 2.2/5.7% | 3 |
| 32 | 1 | 0.883 | 0.873 | 0.010 | - | - | 0.979 | 0.984 | 0.507 | 1.42x | 19.7/26.5/33.3% | 2.2/5.7% | 3 |

> window-size=8: misdecodes 132

> window-size=16: misdecodes 62

> window-size=32: misdecodes 19

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.822 | 2.00x | 22.7/35.0/40.0% | 1.3/5.1% | 3 |
| True | 1 | 0.723 | 0.715 | 0.008 | - | - | 0.862 | 0.928 | 0.524 | 5.80x | 60.4/74.0/78.8% | 4.1/13.1% | 3 |

> no-congestion-scaling=True: queue drops 15.4% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 101

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.549 | 0.539 | 0.011 | - | - | 0.624 | 0.627 | 0.228 | 4.51x | 15.6/29.8/38.3% | 1.5/5.3% | 3 |
| truesize | 1 | 0.582 | 0.571 | 0.011 | - | - | 0.669 | 0.671 | 0.241 | 3.44x | 11.9/23.6/30.8% | 1.1/4.4% | 3 |

> congestion-input=hotstore: decode_failures 2

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.956 | 0.954 | 0.002 | - | - | 0.999 | 0.999 | 0.828 | 1.94x | 21.9/33.6/38.5% | 1.3/4.9% | 3 |
| adaptive | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.822 | 2.00x | 22.7/35.0/40.0% | 1.3/5.1% | 3 |

