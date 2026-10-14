# Sweep blocks-2026-10-14-8096368

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 8096368 · seeds 8096368
- **blocks** 87 run
- **compute** 8.9 h of simulator time across every cell
- **generated** 2026-10-14T08:34:58+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>86 warnings</summary>

- AD-amplify-worst: faster: 0.834 s per simulated hour against 1.85 over 54 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-badrouters: role-placement=inverse: decode_failures 1
- AD-worst: role-placement=degree: decode_failures 87
- AD-worst: role-placement=inverse: decode_failures 80
- AD-worst: slower: 26.3 s per simulated hour against 3.39 over 54 prior run(s) - 7.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 38
- DB-hotstore-stress: max-num-nodes=120: decode_failures 38
- DB-hotstore-stress: max-num-nodes=250: decode_failures 6
- DB-warm: warm-num-nodes=0: decode_failures 61
- DB-warm: warm-num-nodes=25: decode_failures 61
- DB-warm: warm-num-nodes=100: decode_failures 61
- DB-warm: warm-num-nodes=2000: decode_failures 61
- DG-burst: burst-loss=0.2: decode_failures 3
- DG-burst: burst-loss=0.3: decode_failures 27
- DG-loss: extra-loss=0.3: decode_failures 12
- DG-outage: burst-loss=0.1: decode_failures 30
- DG-outage: burst-loss=0.2: decode_failures 19
- DG-outage: burst-loss=0.3: decode_failures 25
- DM-mode: dm-mode=directed-with-late-flood: misdecodes 1
- DM-mode: dm-mode=m4-early-flood: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=900: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 2
- LD-chatty: broadcast-interval-s=300: decode_failures 11
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 61
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 11.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 86
- MS-density: nodes=150: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 80
- MS-hopscale: nodes=500: decode_failures 63
- MS-oversubscribed: nodes=250: decode_failures 38
- MS-oversubscribed: nodes=500: decode_failures 19
- MS-siting: siting-mix=event: decode_failures 9
- MS-stretch: stretch=1.25: decode_failures 2
- MS-stretch: stretch=1.5: decode_failures 7
- PR-crladder: coding-rate-ladder=False: misdecodes 1
- PR-crladder: faster: 1.29 s per simulated hour against 2.77 over 54 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-bw500: preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 25
- RF-preset: faster: 0.831 s per simulated hour against 2.91 over 54 prior run(s) - 3.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-preset-turbo: preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 6
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 7
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 10
- RF-txpower: tx-power=22: decode_failures 17
- RF-txpower: tx-power=17: 3 archives requested, 2 placed - group on the placed count
- RT-hoplimit: hop-limit=3: decode_failures 3
- RT-hopspread: hop-limit=3: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 3
- SF-bucket-mode: bucket-mode=global: misdecodes 36
- SF-bucket-mode: bucket-mode=time: misdecodes 38
- SF-bucket-mode: bucket-mode=window: misdecodes 21
- SF-bucket-time: time-bucket-s=600: misdecodes 90
- SF-bucket-time: time-bucket-s=1800: misdecodes 38
- SF-bucket-time: time-bucket-s=3600: misdecodes 14
- SF-cadence: trigger=interval: misdecodes 14
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 3
- SF-capacity-local: capacity=4: decode_failures 91
- SF-capacity-local: capacity=8: decode_failures 26
- SF-capacity: capacity=4: decode_failures 91
- SF-capacity: capacity=8: decode_failures 26
- SF-capacity-window: capacity=8: misdecodes 25
- SF-capacity-window: capacity=8: decode_failures 29
- SF-capacity-window: capacity=16: misdecodes 26
- SF-capacity-window: capacity=16: decode_failures 1
- SF-capacity-window: capacity=32: misdecodes 21
- SF-catchup: catch-up-hours=: misdecodes 3
- SF-catchup: catch-up-hours=02-06: decode_failures 13
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 12
- SF-hops-flat: hops-apart=4: decode_failures 19
- SF-hops-spread: hops-apart=4: decode_failures 19
- SF-hops-spread: hops-apart=5: decode_failures 29
- SF-place-flat: place=spread: decode_failures 14
- SF-place-spread: place=spread: decode_failures 14
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 5
- SF-replay-order: replay-ordering=heard: misdecodes 18
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-signed: faster: 0.826 s per simulated hour against 1.7 over 54 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-window-size: window-size=8: misdecodes 136
- SF-window-size: window-size=16: misdecodes 46
- SF-window-size: window-size=32: misdecodes 21
- TH-congestion-input: congestion-input=hotstore: decode_failures 38
- TH-congestion: no-congestion-scaling=True: decode_failures 91

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 26.3 | 3.39 | 7.76x | 54 |
| `RF-stretch-duct` | 3.39 | 1.82 | 1.86x | 54 |
| `RF-bw500` | 3.35 | 1.91 | 1.76x | 54 |
| `TH-congestion-input` | 17.5 | 11.1 | 1.57x | 54 |
| `MS-stretch` | 1.35 | 2.03 | 0.66x | 54 |
| `RF-duct` | 1.09 | 1.75 | 0.62x | 54 |
| `FW-versions` | 0.926 | 1.51 | 0.61x | 54 |
| `MS-oversubscribed` | 12.2 | 20.3 | 0.60x | 54 |
| `SF-cadence` | 2.13 | 3.61 | 0.59x | 54 |
| `SF-place-flat` | 1.66 | 2.86 | 0.58x | 54 |
| `RF-noise` | 2.79 | 4.92 | 0.57x | 54 |
| `DM-mode` | 1.76 | 3.12 | 0.56x | 54 |
| `SF-replay-order` | 0.883 | 1.58 | 0.56x | 54 |
| `DB-hotstore` | 1.29 | 2.36 | 0.55x | 54 |
| `RT-favourites` | 0.893 | 1.65 | 0.54x | 54 |
| `MS-router-late` | 0.918 | 1.72 | 0.53x | 54 |
| `DB-warm` | 17.6 | 33.6 | 0.52x | 54 |
| `SF-servers-spread` | 1.17 | 2.25 | 0.52x | 54 |
| `AD-nomute` | 1.19 | 2.3 | 0.52x | 54 |
| `SF-resolve` | 0.792 | 1.53 | 0.52x | 54 |
| `RT-rebroadcast` | 0.802 | 1.57 | 0.51x | 54 |
| `SF-signed` | 0.826 | 1.7 | 0.49x | 54 |
| `PR-crladder` | 1.29 | 2.77 | 0.47x | 54 |
| `AD-amplify-worst` | 0.834 | 1.85 | 0.45x | 54 |
| `RF-preset` | 0.831 | 2.91 | 0.29x | 54 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.872 | 0.872 | 0.732 → 0.736 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.864 | 0.864 | 0.732 → 0.738 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.141 → 0.944 | 0.803 | 0.135 → 0.944 | 4x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.091 → 0.864 | 0.773 | 0.043 → 0.738 | 32x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.096 → 0.864 | 0.768 | 0.068 → 0.738 | 57x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.071 → 0.818 | 0.747 | 0.070 → 0.693 | 2.3e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.222 → 0.950 | 0.727 | 0.079 → 0.788 | 7x sr_bytes | down | 3 |
| `RF-bw500` | preset | **held** | 0.103 → 0.824 | 0.721 | 0.147 → 0.690 | 48x sr_bytes | up | 3 |
| `MS-stretch` | stretch | **text** | 0.119 → 0.746 | 0.626 | 0.117 → 0.738 | 4.2x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.254 → 0.864 | 0.610 | 0.279 → 0.738 | 5.6x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.254 → 0.864 | 0.610 | 0.279 → 0.738 | 6.8x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.327 → 0.895 | 0.568 | 0.306 → 0.738 | 9x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.326 → 0.886 | 0.560 | 0.308 → 0.712 | 4.8x sr_bytes | down | 3 |
| `MS-topology` | topology | **held** | 0.485 → 0.992 | 0.507 | 0.543 → 0.948 | 3.9x sr_airtime | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.437 → 0.744 | 0.307 | 0.311 → 0.517 | 5.5x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.653 → 0.957 | 0.304 | 0.644 → 0.956 | 4.8x sr_airtime | up | 5 |
| `DG-burst` | burst-loss | **text** | 0.452 → 0.746 | 0.294 | 0.420 → 0.738 | 2.3x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.326 → 0.615 | 0.289 | 0.321 → 0.583 | 2.4x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.458 → 0.746 | 0.288 | 0.433 → 0.738 | 2.2x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.559 → 0.847 | 0.287 | 0.546 → 0.846 | 7.8x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.597 → 0.861 | 0.263 | 0.562 → 0.859 | 3.6x sr_bytes | up | 4 |
| `SF-place-flat` | place | **held** | 0.641 → 0.881 | 0.240 | 0.727 → 0.743 | 1.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.641 → 0.881 | 0.240 | 0.727 → 0.743 | 1.6x sr_bytes | up | 6 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.505 → 0.744 | 0.239 | 0.481 → 0.738 | 7.6x sr_airtime | down | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.597 → 0.828 | 0.231 | 0.562 → 0.825 | 2.8x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.728 → 0.943 | 0.215 | 0.721 → 0.940 | 5.3x sr_airtime | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.746 → 0.955 | 0.209 | 0.738 → 0.953 | 1.4x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.746 → 0.904 | 0.159 | 0.738 → 0.900 | 1.2x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.640 → 0.798 | 0.158 | 0.608 → 0.788 | 1.6x sr_bytes | down | 3 |
| `RF-noise` | noise-profile | **held** | 0.721 → 0.872 | 0.151 | 0.601 → 0.738 | 1.3x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.597 → 0.746 | 0.148 | 0.562 → 0.738 | 2x sr_bytes | up | 2 |
| `MS-size` | nodes | **text** | 0.717 → 0.846 | 0.130 | 0.713 → 0.837 | 7.2x sr_bytes | down | 5 |
| `SC-signing` | signature-policy | **held** | 0.739 → 0.864 | 0.126 | 0.621 → 0.738 | 1.2x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.620 → 0.746 | 0.126 | 0.599 → 0.738 | 1.7x sr_bytes | down | 4 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.864 → 0.984 | 0.120 | 0.738 → 0.851 | 2.2x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.864 → 0.974 | 0.110 | 0.738 → 0.845 | 2.1x bytes_on_air | up | 4 |
| `FW-versions` | profile | **held** | 0.864 → 0.969 | 0.104 | 0.738 → 0.823 | 3.4x bytes_on_air | down | 5 |
| `RF-duct` | duct-per-hour | **text** | 0.746 → 0.847 | 0.101 | 0.738 → 0.838 | 1.2x bytes_on_air | up | 3 |
| `FW-firmware` | profile | **held** | 0.864 → 0.960 | 0.096 | 0.738 → 0.804 | 3.3x bytes_on_air | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.708 → 0.795 | 0.088 | 0.692 → 0.792 | 5.6x sr_airtime | up | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.864 → 0.951 | 0.087 | 0.738 → 0.799 | 1.4x sr_airtime | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.771 → 0.847 | 0.076 | 0.759 → 0.840 | 2.1x bytes_on_air | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.710 → 0.781 | 0.071 | 0.702 → 0.779 | 2.1x sr_airtime | down | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.801 → 0.872 | 0.071 | 0.728 → 0.747 | 4.6x sr_bytes | down | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.665 → 0.734 | 0.069 | 0.660 → 0.727 | 1.3x sr_airtime | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.802 → 0.864 | 0.063 | 0.735 → 0.738 | 27x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.720 → 0.781 | 0.061 | 0.711 → 0.779 | 2.1x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.798 → 0.847 | 0.049 | 0.788 → 0.840 | 2.1x bytes_on_air | up | 2 |
| `SF-cadence` | trigger | **held** | 0.825 → 0.864 | 0.039 | 0.710 → 0.738 | 15x advert_bytes | down | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.727 → 0.761 | 0.034 | 0.512 → 0.546 | 1.3x bytes_on_air | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.714 → 0.746 | 0.032 | 0.699 → 0.738 | 1.4x sr_airtime | down | 4 |
| `AD-worst` | role-placement | **text** | 0.819 → 0.849 | 0.030 | 0.808 → 0.842 | 1x bytes_on_air | down | 2 |
| `SF-hops-flat` | hops-apart | **text** | 0.729 → 0.756 | 0.027 | 0.728 → 0.738 | 2.6x sr_bytes | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.746 → 0.772 | 0.026 | 0.738 → 0.768 | 3.5x bytes_on_air | down | 2 |
| `DM-mode` | dm-mode | **held** | 0.839 → 0.863 | 0.024 | 0.704 → 0.722 | 1.2x sr_airtime | down | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.851 → 0.874 | 0.023 | 0.720 → 0.737 | 1.4x sr_bytes | down | 4 |
| `PR-repeats` | extra-repeats | **held** | 0.864 → 0.886 | 0.021 | 0.738 → 0.755 | 1.1x sr_bytes | up | 2 |
| `LD-diurnal` | diurnal | **held** | 0.864 → 0.885 | 0.021 | 0.738 → 0.758 | 1.2x sr_bytes | down | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.813 → 0.833 | 0.020 | 0.804 → 0.826 | 1.1x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **held** | 0.845 → 0.864 | 0.020 | 0.728 → 0.738 | 5.9x advert_bytes | = | 3 |
| `SF-servers-flat` | servers | **text** | 0.729 → 0.749 | 0.019 | 0.718 → 0.738 | 7.7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **text** | 0.729 → 0.749 | 0.019 | 0.718 → 0.738 | 7.7x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.855 → 0.874 | 0.019 | 0.731 → 0.743 | 2.2x advert_bytes | up | 3 |
| `SF-catchup` | catch-up-hours | **text** | 0.724 → 0.743 | 0.019 | 0.710 → 0.738 | 9.3x advert_bytes | up | 3 |
| `SF-window-size` | window-size | **held** | 0.863 → 0.882 | 0.019 | 0.731 → 0.743 | 5.6x advert_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.746 → 0.764 | 0.019 | 0.727 → 0.738 | 2.5x sr_airtime | up | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.847 → 0.865 | 0.018 | 0.738 → 0.754 | 1.2x bytes_on_air | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.758 → 0.775 | 0.017 | 0.752 → 0.771 | 1.2x sr_bytes | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.859 → 0.874 | 0.015 | 0.734 → 0.743 | 3.2x advert_bytes | up | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.704 → 0.717 | 0.013 | 0.704 → 0.717 | 1.1x sr_airtime | up | 2 |
| `SF-capacity` | capacity | **held** | 0.856 → 0.868 | 0.012 | 0.735 → 0.740 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.856 → 0.868 | 0.012 | 0.735 → 0.740 | 5.3x advert_bytes | up | 5 |
| `MS-roles` | role-mix | **text** | 0.798 → 0.809 | 0.012 | 0.788 → 0.799 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.848 → 0.859 | 0.012 | 0.723 → 0.734 | 5x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.858 → 0.869 | 0.011 | 0.729 → 0.738 | 3.1x advert_bytes | down | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.861 → 0.872 | 0.010 | 0.738 → 0.742 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.861 → 0.872 | 0.010 | 0.738 → 0.742 | 1.1x sr_airtime | down | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.863 → 0.873 | 0.010 | 0.727 → 0.738 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.943 → 0.949 | 0.007 | 0.940 → 0.947 | 1.1x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.743 → 0.749 | 0.006 | 0.734 → 0.743 | 2.2x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.938 → 0.943 | 0.004 | 0.934 → 0.940 | 1.1x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.746 → 0.750 | 0.004 | 0.738 → 0.741 | 2.7x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.743 → 0.746 | 0.003 | 0.733 → 0.738 | 1.2x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.844 → 0.846 | 0.003 | 0.717 → 0.719 | 1x sr_bytes | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.995 → 0.996 | 0.000 | 0.940 → 0.940 | 1x sr_bytes | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario alpine`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| sprinkled | 1 | 0.906 | 0.897 | 0.009 | - | - | 0.966 | 0.966 | 0.672 | 1.26x | 17.6/26.2/28.4% | 1.9/5.1% | 3 |
| arms-race | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.989 | 0.990 | 0.794 | 1.01x | 20.2/24.9/29.5% | 1.1/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.1 | 1 | 0.848 | 0.843 | 0.005 | - | - | 0.941 | 0.942 | 0.441 | 1.36x | 17.1/22.0/23.9% | 2.0/5.0% | 3 |
| 0.3 | 1 | 0.904 | 0.900 | 0.004 | - | - | 0.983 | 0.984 | 0.676 | 1.31x | 18.2/24.4/27.3% | 2.0/5.1% | 3 |

> faster: 0.834 s per simulated hour against 1.85 over 54 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.798 | 0.788 | 0.010 | - | - | 0.950 | 0.951 | 0.366 | 1.29x | 15.2/21.6/26.6% | 2.2/5.0% | 3 |
| inverse | 1 | 0.640 | 0.608 | 0.032 | - | - | 0.865 | 0.868 | 0.253 | 1.09x | 10.8/16.0/20.2% | 2.0/3.5% | 3 |
| random | 1 | 0.738 | 0.717 | 0.021 | - | - | 0.909 | 0.920 | 0.372 | 1.20x | 12.8/17.2/19.1% | 2.1/3.8% | 3 |

> role-placement=inverse: decode_failures 1

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.798 | 0.788 | 0.010 | - | - | 0.950 | 0.951 | 0.366 | 1.29x | 15.2/21.6/26.6% | 2.2/5.0% | 3 |
| all-routers | 1 | 0.847 | 0.840 | 0.007 | - | - | 0.930 | 0.931 | 0.536 | 2.72x | 28.0/33.9/38.0% | 4.5/5.5% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.798 | 0.788 | 0.010 | - | - | 0.950 | 0.951 | 0.366 | 1.29x | 15.2/21.6/26.6% | 2.2/5.0% | 3 |
| no-mute | 1 | 0.771 | 0.759 | 0.012 | - | - | 0.941 | 0.942 | 0.255 | 1.34x | 14.4/19.5/23.6% | 2.1/4.9% | 3 |
| all-routers | 1 | 0.847 | 0.840 | 0.007 | - | - | 0.930 | 0.931 | 0.536 | 2.72x | 28.0/33.9/38.0% | 4.5/5.5% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.798 | 0.788 | 0.010 | - | - | 0.950 | 0.951 | 0.366 | 1.29x | 15.2/21.6/26.6% | 2.2/5.0% | 3 |
| local-typical | 1 | 0.544 | 0.526 | 0.018 | - | - | 0.779 | 0.799 | 0.000 | 1.28x | 10.9/19.6/26.2% | 2.3/4.8% | 3 |
| basement-heavy | 1 | 0.079 | 0.079 | 0.000 | - | - | 0.222 | 0.223 | 0.000 | 0.67x | 1.4/9.2/13.8% | 0.6/3.4% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.849 | 0.842 | 0.007 | - | - | 0.921 | 0.967 | 0.000 | 2.38x | 16.1/28.9/33.1% | 1.8/5.4% | 3 |
| inverse | 1 | 0.819 | 0.808 | 0.011 | - | - | 0.925 | 0.965 | 0.000 | 2.28x | 15.2/25.5/32.0% | 1.8/3.3% | 3 |

> role-placement=degree: decode_failures 87

> role-placement=inverse: decode_failures 80

> slower: 26.3 s per simulated hour against 3.39 over 54 prior run(s) - 7.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.732 | 0.732 | 0.000 | - | - | 0 | 0.000 | 0.314 | 1.35x | 15.6/22.9/26.7% | 2.1/4.9% | 3 |
| sr | 1 | 0.756 | 0.736 | 0.020 | - | - | 0.872 | 0.878 | 0.326 | 1.40x | 16.3/23.8/27.6% | 2.2/5.2% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.720 | 0.711 | 0.008 | - | - | 0.827 | 0.828 | 0.348 | 3.15x | 35.8/49.6/58.0% | 4.4/10.4% | 3 |
| 100 | 1 | 0.781 | 0.779 | 0.002 | - | - | 0.868 | 0.868 | 0.361 | 1.63x | 18.9/26.6/31.3% | 2.2/5.3% | 3 |
| 120 | 1 | 0.781 | 0.779 | 0.002 | - | - | 0.868 | 0.868 | 0.361 | 1.63x | 18.9/26.6/31.3% | 2.2/5.3% | 3 |
| 250 | 1 | 0.781 | 0.779 | 0.002 | - | - | 0.868 | 0.868 | 0.361 | 1.63x | 18.9/26.6/31.3% | 2.2/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.318 | 0.311 | 0.007 | - | - | 0.437 | 0.488 | 0.103 | 11.41x | 38.9/55.6/66.0% | 4.1/11.0% | 3 |
| 120 | 1 | 0.522 | 0.512 | 0.011 | - | - | 0.727 | 0.742 | 0.138 | 4.46x | 15.3/24.6/32.4% | 1.5/5.5% | 3 |
| 250 | 1 | 0.528 | 0.517 | 0.011 | - | - | 0.744 | 0.746 | 0.142 | 4.33x | 14.9/23.3/31.1% | 1.5/5.5% | 3 |

> max-num-nodes=10: decode_failures 38

> max-num-nodes=120: decode_failures 38

> max-num-nodes=250: decode_failures 6

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.781 | 0.779 | 0.002 | - | - | 0.868 | 0.868 | 0.361 | 1.63x | 18.9/26.6/31.3% | 2.2/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.781 | 0.779 | 0.002 | - | - | 0.868 | 0.868 | 0.361 | 1.63x | 18.9/26.6/31.3% | 2.2/5.3% | 3 |
| constrained | 1 | 0.710 | 0.702 | 0.008 | - | - | 0.818 | 0.822 | 0.334 | 3.15x | 35.9/49.7/57.9% | 4.5/10.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.734 | 0.727 | 0.007 | - | - | 0.823 | 0.933 | 0.539 | 5.84x | 54.2/69.7/75.4% | 4.1/12.3% | 3 |
| 25 | 1 | 0.734 | 0.727 | 0.007 | - | - | 0.823 | 0.933 | 0.539 | 5.84x | 54.2/69.7/75.4% | 4.1/12.3% | 3 |
| 100 | 1 | 0.734 | 0.727 | 0.007 | - | - | 0.823 | 0.933 | 0.539 | 5.84x | 54.2/69.7/75.4% | 4.1/12.3% | 3 |
| 2000 | 1 | 0.734 | 0.727 | 0.007 | - | - | 0.823 | 0.933 | 0.539 | 5.84x | 54.2/69.7/75.4% | 4.1/12.3% | 3 |

> warm-num-nodes=0: decode_failures 61

> warm-num-nodes=25: decode_failures 61

> warm-num-nodes=100: decode_failures 61

> warm-num-nodes=2000: decode_failures 61

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.1 | 1 | 0.649 | 0.632 | 0.017 | - | - | 0.828 | 0.829 | 0.257 | 1.27x | 14.8/21.8/25.6% | 2.0/4.5% | 3 |
| 0.2 | 1 | 0.559 | 0.529 | 0.030 | - | - | 0.788 | 0.797 | 0.221 | 1.18x | 13.7/20.2/24.3% | 1.8/4.0% | 3 |
| 0.3 | 1 | 0.452 | 0.420 | 0.032 | - | - | 0.666 | 0.708 | 0.169 | 1.06x | 12.5/18.4/22.2% | 1.6/3.5% | 3 |

> burst-loss=0.2: decode_failures 3

> burst-loss=0.3: decode_failures 27

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.1 | 1 | 0.715 | 0.701 | 0.014 | - | - | 0.858 | 0.860 | 0.302 | 1.41x | 16.1/23.5/27.7% | 2.2/4.8% | 3 |
| 0.2 | 1 | 0.676 | 0.660 | 0.016 | - | - | 0.838 | 0.840 | 0.299 | 1.46x | 16.8/23.7/28.1% | 2.2/4.6% | 3 |
| 0.3 | 1 | 0.620 | 0.599 | 0.021 | - | - | 0.778 | 0.798 | 0.276 | 1.42x | 16.6/23.1/27.5% | 2.2/4.3% | 3 |

> extra-loss=0.3: decode_failures 12

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.1 | 1 | 0.650 | 0.636 | 0.014 | - | - | 0.800 | 0.838 | 0.257 | 1.29x | 14.9/22.6/26.3% | 2.0/4.8% | 3 |
| 0.2 | 1 | 0.542 | 0.521 | 0.021 | - | - | 0.761 | 0.790 | 0.217 | 1.21x | 14.0/20.7/24.7% | 1.9/4.2% | 3 |
| 0.3 | 1 | 0.458 | 0.433 | 0.024 | - | - | 0.612 | 0.715 | 0.161 | 1.10x | 13.2/19.2/23.0% | 1.7/3.8% | 3 |

> burst-loss=0.1: decode_failures 30

> burst-loss=0.2: decode_failures 19

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.722 | 0.722 | 0.000 | - | - | 0.863 | 0.865 | 0.325 | 1.76x | 20.3/30.0/34.6% | 2.7/6.4% | 3 |
| directed-with-late-flood | 1 | 0.704 | 0.704 | 0.000 | - | - | 0.839 | 0.842 | 0.317 | 1.60x | 18.5/27.7/32.1% | 2.5/5.9% | 3 |
| m4-early-flood | 1 | 0.704 | 0.704 | 0.000 | - | - | 0.839 | 0.842 | 0.317 | 1.60x | 18.5/27.7/32.1% | 2.5/5.9% | 3 |

> dm-mode=directed-with-late-flood: misdecodes 1

> dm-mode=m4-early-flood: misdecodes 1

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.813 | 0.804 | 0.008 | - | - | 0.960 | 0.961 | 0.325 | 0.75x | 7.7/10.7/11.7% | 1.2/2.1% | 3 |
| 2.8 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.25 | 1 | 0.852 | 0.845 | 0.007 | - | - | 0.949 | 0.950 | 0.576 | 1.23x | 14.3/19.1/21.2% | 1.8/4.5% | 3 |
| 0.5 | 1 | 0.851 | 0.843 | 0.008 | - | - | 0.946 | 0.946 | 0.509 | 1.10x | 11.5/16.1/19.3% | 1.8/4.1% | 3 |
| 0.75 | 1 | 0.827 | 0.824 | 0.004 | - | - | 0.974 | 0.975 | 0.370 | 0.90x | 10.0/14.6/16.4% | 1.5/2.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.25 | 1 | 0.851 | 0.842 | 0.009 | - | - | 0.949 | 0.950 | 0.601 | 1.22x | 14.0/18.7/20.7% | 1.8/4.4% | 3 |
| 0.5 | 1 | 0.857 | 0.851 | 0.006 | - | - | 0.951 | 0.951 | 0.439 | 1.07x | 11.5/16.5/19.1% | 1.6/4.1% | 3 |
| 0.75 | 1 | 0.838 | 0.834 | 0.004 | - | - | 0.984 | 0.985 | 0.411 | 0.87x | 9.9/14.4/16.1% | 1.3/2.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.772 | 0.768 | 0.004 | - | - | 0.881 | 0.881 | 0.326 | 0.70x | 8.4/12.7/15.2% | 1.1/2.8% | 3 |
| signing=true | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.815 | 0.806 | 0.009 | - | - | 0.966 | 0.967 | 0.346 | 0.77x | 8.3/11.8/13.2% | 1.2/2.6% | 3 |
| 2.5 | 1 | 0.802 | 0.794 | 0.008 | - | - | 0.951 | 0.951 | 0.339 | 0.77x | 8.0/11.6/12.8% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.817 | 0.809 | 0.007 | - | - | 0.969 | 0.971 | 0.306 | 0.74x | 8.1/11.5/12.9% | 1.2/2.6% | 3 |
| 2.7 | 1 | 0.830 | 0.823 | 0.007 | - | - | 0.961 | 0.961 | 0.321 | 0.78x | 8.1/14.5/16.2% | 1.1/2.9% | 3 |
| 2.8 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.744 | 0.738 | 0.006 | - | - | 0.847 | 0.847 | 0.359 | 0.89x | 10.2/15.1/17.7% | 1.4/3.2% | 3 |
| 900 | 1 | 0.708 | 0.692 | 0.016 | - | - | 0.834 | 0.836 | 0.335 | 2.15x | 24.7/36.3/41.9% | 3.4/7.7% | 3 |
| 300 | 1 | 0.505 | 0.481 | 0.023 | - | - | 0.631 | 0.689 | 0.266 | 4.79x | 51.0/66.5/75.2% | 7.4/15.6% | 3 |

> broadcast-interval-s=300: decode_failures 11

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.847 | 0.846 | 0.001 | - | - | 0.938 | 0.938 | 0.382 | 0.97x | 10.9/15.4/18.0% | 1.5/3.3% | 3 |
| 900 | 1 | 0.785 | 0.780 | 0.005 | - | - | 0.893 | 0.894 | 0.356 | 2.43x | 27.6/38.7/44.5% | 3.8/8.2% | 3 |
| 300 | 1 | 0.559 | 0.546 | 0.013 | - | - | 0.725 | 0.731 | 0.291 | 5.50x | 56.0/69.9/77.7% | 8.9/16.6% | 3 |

> broadcast-interval-s=900: misdecodes 1

> broadcast-interval-s=300: decode_failures 2

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.759 | 0.754 | 0.006 | - | - | 0.876 | 0.876 | 0.335 | 1.27x | 14.5/21.5/25.2% | 1.9/4.6% | 3 |
| sinusoid | 1 | 0.765 | 0.758 | 0.006 | - | - | 0.885 | 0.886 | 0.328 | 1.24x | 14.3/21.2/24.5% | 1.9/4.5% | 3 |
| commuter | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.708 | 0.692 | 0.016 | - | - | 0.834 | 0.836 | 0.335 | 2.15x | 24.7/36.3/41.9% | 3.4/7.7% | 3 |
| 3600 | 1 | 0.744 | 0.738 | 0.006 | - | - | 0.847 | 0.847 | 0.359 | 0.89x | 10.2/15.1/17.7% | 1.4/3.2% | 3 |
| 10800 | 1 | 0.774 | 0.769 | 0.005 | - | - | 0.881 | 0.882 | 0.361 | 0.58x | 6.8/9.9/11.5% | 0.9/2.1% | 3 |
| 43200 | 1 | 0.795 | 0.792 | 0.003 | - | - | 0.898 | 0.898 | 0.344 | 0.41x | 4.8/6.9/8.1% | 0.6/1.5% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.25 | 1 | 0.735 | 0.723 | 0.012 | - | - | 0.860 | 0.860 | 0.340 | 1.42x | 16.4/24.5/28.5% | 2.2/5.2% | 3 |
| 1.0 | 1 | 0.738 | 0.727 | 0.011 | - | - | 0.868 | 0.869 | 0.318 | 1.55x | 18.0/26.8/31.1% | 2.4/5.7% | 3 |
| 4.0 | 1 | 0.714 | 0.699 | 0.014 | - | - | 0.846 | 0.849 | 0.337 | 1.90x | 22.4/32.9/38.5% | 2.9/7.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.734 | 0.727 | 0.007 | - | - | 0.823 | 0.933 | 0.539 | 5.84x | 54.2/69.7/75.4% | 4.1/12.3% | 3 |
| 1.0 | 1 | 0.665 | 0.660 | 0.005 | - | - | 0.756 | 0.902 | 0.497 | 6.56x | 59.0/73.3/78.1% | 4.8/13.8% | 3 |

> traceroute-per-hour=0.0: decode_failures 61

> traceroute-per-hour=1.0: queue drops 11.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 86

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.653 | 0.644 | 0.009 | - | - | 0.887 | 0.890 | 0.254 | 1.39x | 15.7/28.4/29.9% | 3.1/6.9% | 3 |
| 60 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 90 | 1 | 0.907 | 0.904 | 0.003 | - | - | 0.987 | 0.988 | 0.617 | 1.62x | 16.7/27.6/32.1% | 1.5/4.7% | 3 |
| 120 | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.996 | 0.996 | 0.775 | 2.15x | 22.2/31.6/35.5% | 1.5/5.3% | 3 |
| 150 | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.999 | 1.000 | 0.707 | 2.72x | 25.9/35.7/39.9% | 1.4/5.6% | 3 |

> nodes=150: misdecodes 1

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 120 | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.895 | 0.895 | 0.000 | 2.18x | 14.9/22.3/28.0% | 1.5/5.3% | 3 |
| 250 | 1 | 0.518 | 0.508 | 0.010 | - | - | 0.713 | 0.729 | 0.139 | 4.73x | 16.2/26.4/33.9% | 1.7/6.1% | 3 |
| 500 | 1 | 0.309 | 0.306 | 0.004 | - | - | 0.327 | 0.331 | 0.099 | 9.61x | 18.0/25.8/43.5% | 1.7/5.3% | 3 |

> nodes=250: decode_failures 80

> nodes=500: decode_failures 63

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.715 | 0.712 | 0.003 | - | - | 0.886 | 0.886 | 0.000 | 2.04x | 13.7/20.7/26.1% | 1.4/4.9% | 3 |
| 250 | 1 | 0.522 | 0.512 | 0.011 | - | - | 0.727 | 0.742 | 0.138 | 4.46x | 15.3/24.6/32.4% | 1.5/5.5% | 3 |
| 500 | 1 | 0.311 | 0.308 | 0.004 | - | - | 0.326 | 0.329 | 0.103 | 9.04x | 16.9/24.5/40.4% | 1.5/5.0% | 3 |

> nodes=250: decode_failures 38

> nodes=500: decode_failures 19

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.809 | 0.799 | 0.011 | - | - | 0.959 | 0.963 | 0.269 | 1.35x | 15.6/23.3/26.9% | 2.1/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.798 | 0.788 | 0.010 | - | - | 0.950 | 0.951 | 0.366 | 1.29x | 15.2/21.6/26.6% | 2.2/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.813 | 0.804 | 0.009 | - | - | 0.960 | 0.961 | 0.262 | 1.39x | 15.8/23.8/27.5% | 2.1/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.833 | 0.826 | 0.007 | - | - | 0.943 | 0.944 | 0.424 | 1.48x | 17.2/24.1/30.2% | 2.6/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.05 | 1 | 0.744 | 0.738 | 0.007 | - | - | 0.847 | 0.851 | 0.332 | 1.48x | 17.7/25.2/29.3% | 2.1/5.2% | 3 |
| 0.1 | 1 | 0.755 | 0.749 | 0.006 | - | - | 0.865 | 0.867 | 0.353 | 1.57x | 18.4/26.8/31.5% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.761 | 0.754 | 0.006 | - | - | 0.865 | 0.866 | 0.334 | 1.72x | 20.0/29.5/35.6% | 2.3/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| local-typical | 1 | 0.607 | 0.591 | 0.016 | - | - | 0.843 | 0.847 | 0.000 | 1.45x | 12.2/20.3/25.5% | 2.3/4.8% | 3 |
| event | 1 | 0.141 | 0.135 | 0.006 | - | - | 0.299 | 0.325 | 0.000 | 0.95x | 4.2/9.0/12.6% | 1.3/3.7% | 3 |
| backbone | 1 | 0.944 | 0.944 | 0.000 | - | - | 0.967 | 0.967 | 0.792 | 1.24x | 21.4/30.7/35.1% | 1.6/5.5% | 3 |

> siting-mix=event: decode_failures 9

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.756 | 0.749 | 0.007 | - | - | 0.905 | 0.905 | 0.302 | 1.34x | 20.1/27.7/31.3% | 3.1/6.9% | 3 |
| 60 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 90 | 1 | 0.846 | 0.837 | 0.009 | - | - | 0.980 | 0.981 | 0.367 | 1.79x | 14.2/25.6/28.5% | 1.7/5.0% | 3 |
| 120 | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.895 | 0.895 | 0.000 | 2.18x | 14.9/22.3/28.0% | 1.5/5.3% | 3 |
| 150 | 1 | 0.735 | 0.724 | 0.011 | - | - | 0.979 | 0.980 | 0.255 | 3.01x | 17.7/26.5/33.2% | 1.8/6.1% | 3 |

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 1.25 | 1 | 0.636 | 0.618 | 0.018 | - | - | 0.863 | 0.864 | 0.306 | 1.35x | 11.3/21.4/24.5% | 1.9/4.9% | 3 |
| 1.5 | 1 | 0.326 | 0.321 | 0.005 | - | - | 0.402 | 0.461 | 0.000 | 1.22x | 7.9/15.5/19.5% | 1.8/4.8% | 3 |
| 2.0 | 1 | 0.119 | 0.117 | 0.003 | - | - | 0.267 | 0.271 | 0.000 | 0.86x | 4.2/8.1/9.1% | 1.3/2.9% | 3 |

> stretch=1.25: decode_failures 2

> stretch=1.5: decode_failures 7

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| clustered | 1 | 0.939 | 0.939 | 0.001 | - | - | 0.983 | 0.985 | 0.461 | 1.29x | 29.9/39.8/43.5% | 1.7/5.5% | 3 |
| corridor | 1 | 0.548 | 0.543 | 0.005 | - | - | 0.485 | 0.487 | 0.302 | 1.45x | 17.2/23.4/26.7% | 2.2/5.0% | 3 |
| hub | 1 | 0.948 | 0.948 | 0.000 | - | - | 0.992 | 0.992 | 0.627 | 1.24x | 25.0/34.2/35.3% | 1.7/5.7% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.704 | 0.704 | 0.000 | - | - | 0.839 | 0.842 | 0.317 | 1.60x | 18.5/27.7/32.1% | 2.5/5.9% | 3 |
| True | 1 | 0.717 | 0.717 | 0.000 | - | - | 0.844 | 0.846 | 0.313 | 1.62x | 18.7/27.9/32.3% | 2.5/5.9% | 3 |

> coding-rate-ladder=False: misdecodes 1

> faster: 1.29 s per simulated hour against 2.77 over 54 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.717 | 0.717 | 0.000 | - | - | 0.844 | 0.846 | 0.313 | 1.62x | 18.7/27.9/32.3% | 2.5/5.9% | 3 |
| m4-early-flood | 1 | 0.719 | 0.719 | 0.000 | - | - | 0.846 | 0.852 | 0.320 | 1.60x | 18.6/27.5/31.9% | 2.5/5.9% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.732 | 0.732 | 0.000 | - | - | 0 | 0.000 | 0.314 | 1.35x | 15.6/22.9/26.7% | 2.1/4.9% | 3 |
| chain | 1 | 0.738 | 0.734 | 0.004 | - | - | 0.829 | 0.870 | 0.344 | 1.55x | 17.7/26.9/31.3% | 2.3/5.7% | 3 |
| sr | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| True | 1 | 0.765 | 0.755 | 0.010 | - | - | 0.886 | 0.888 | 0.350 | 1.39x | 15.9/23.6/27.4% | 2.2/5.0% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.996 | 0.996 | 0.775 | 2.15x | 22.2/31.6/35.5% | 1.5/5.3% | 3 |
| True | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.995 | 0.996 | 0.801 | 2.15x | 22.0/31.2/35.0% | 1.5/5.2% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.147 | 0.147 | 0.000 | - | - | 0.103 | 0.205 | 0.000 | 0.05x | 0.2/0.5/0.8% | 0.1/0.2% | 2 |
| MEDIUM_TURBO | 1 | 0.390 | 0.382 | 0.007 | - | - | 0.511 | 0.569 | 0.000 | 0.27x | 1.8/3.8/5.0% | 0.4/1.2% | 3 |
| LONG_TURBO | 1 | 0.697 | 0.690 | 0.007 | - | - | 0.824 | 0.825 | 0.249 | 1.37x | 11.2/20.0/23.4% | 2.1/4.8% | 3 |

> preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count

> preset=MEDIUM_TURBO: decode_failures 25

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 0.25 | 1 | 0.765 | 0.758 | 0.007 | - | - | 0.866 | 0.867 | 0.400 | 1.31x | 16.6/24.0/27.6% | 2.0/5.0% | 3 |
| 1.0 | 1 | 0.847 | 0.838 | 0.009 | - | - | 0.924 | 0.924 | 0.567 | 1.18x | 20.2/27.4/29.3% | 1.5/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.282 | 0.279 | 0.004 | - | - | 0.254 | 0.384 | 0.000 | 0.14x | 0.8/1.7/2.3% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| LITE_FAST | 1 | 0.714 | 0.708 | 0.006 | - | - | 0.862 | 0.862 | 0.281 | 1.05x | 10.9/17.0/18.2% | 1.6/3.9% | 3 |
| NARROW_SLOW | 1 | 0.717 | 0.711 | 0.006 | - | - | 0.857 | 0.857 | 0.307 | 1.28x | 14.0/20.7/23.3% | 1.9/4.7% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| temporal | 1 | 0.676 | 0.663 | 0.013 | - | - | 0.828 | 0.833 | 0.300 | 1.37x | 15.6/22.9/26.7% | 2.0/4.8% | 3 |
| transient | 1 | 0.743 | 0.733 | 0.011 | - | - | 0.872 | 0.873 | 0.331 | 1.36x | 15.7/23.2/27.1% | 2.1/5.0% | 3 |
| periodic | 1 | 0.609 | 0.601 | 0.008 | - | - | 0.721 | 0.730 | 0.256 | 1.27x | 14.7/21.1/24.9% | 2.0/4.3% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.282 | 0.279 | 0.004 | - | - | 0.254 | 0.384 | 0.000 | 0.14x | 0.8/1.7/2.3% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| LONG_MODERATE | 1 | 0.731 | 0.720 | 0.011 | - | - | 0.846 | 0.849 | 0.377 | 3.51x | 44.7/54.8/59.2% | 5.1/12.9% | 3 |

> faster: 0.831 s per simulated hour against 2.91 over 54 prior run(s) - 3.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.043 | 0.043 | 0.000 | - | - | 0.091 | 0.091 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.147 | 0.147 | 0.000 | - | - | 0.103 | 0.205 | 0.000 | 0.05x | 0.2/0.5/0.8% | 0.1/0.2% | 2 |
| LONG_FAST | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| LONG_TURBO | 1 | 0.697 | 0.690 | 0.007 | - | - | 0.824 | 0.825 | 0.249 | 1.37x | 11.2/20.0/23.4% | 2.1/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.733 | 0.726 | 0.007 | - | - | 0.864 | 0.866 | 0.371 | 1.81x | 20.4/27.0/32.7% | 2.8/6.7% | 3 |

> preset=SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.701 | 0.693 | 0.008 | - | - | 0.818 | 0.820 | 0.313 | 1.32x | 15.3/22.8/26.4% | 2.0/4.7% | 3 |
| 10000 | 1 | 0.609 | 0.601 | 0.008 | - | - | 0.721 | 0.730 | 0.256 | 1.27x | 14.7/21.1/24.9% | 2.0/4.3% | 3 |
| 4000 | 1 | 0.362 | 0.356 | 0.006 | - | - | 0.434 | 0.472 | 0.153 | 1.09x | 12.5/17.8/21.3% | 1.7/3.3% | 3 |
| 2000 | 1 | 0.070 | 0.070 | 0.000 | - | - | 0.071 | 0.134 | 0.027 | 0.73x | 8.6/12.1/14.4% | 1.1/2.2% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 6

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.326 | 0.321 | 0.005 | - | - | 0.402 | 0.461 | 0.000 | 1.22x | 7.9/15.5/19.5% | 1.8/4.8% | 3 |
| 1.0 | 1 | 0.615 | 0.583 | 0.032 | - | - | 0.675 | 0.690 | 0.327 | 1.01x | 12.8/18.5/22.0% | 1.4/4.5% | 3 |

> duct-per-hour=0.0: decode_failures 7

> duct-per-hour=1.0: decode_failures 10

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 22 | 1 | 0.350 | 0.344 | 0.006 | - | - | 0.422 | 0.461 | 0.000 | 1.47x | 9.0/17.3/22.3% | 2.2/5.4% | 3 |
| 17 | 1 | 0.147 | 0.147 | 0.000 | - | - | 0.096 | 0.192 | 0.000 | 1.07x | 5.3/10.0/14.2% | 1.9/3.5% | 2 |
| 14 | 1 | 0.068 | 0.068 | 0.001 | - | - | 0.143 | 0.143 | 0.000 | 0.60x | 2.3/5.1/6.5% | 0.9/2.1% | 3 |

> tx-power=22: decode_failures 17

> tx-power=17: 3 archives requested, 2 placed - group on the placed count

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.996 | 0.996 | 0.775 | 2.15x | 22.2/31.6/35.5% | 1.5/5.3% | 3 |
| True | 1 | 0.938 | 0.934 | 0.004 | - | - | 0.997 | 0.998 | 0.771 | 2.45x | 24.6/34.7/38.7% | 1.7/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.758 | 0.752 | 0.006 | - | - | 0.874 | 0.875 | 0.348 | 1.38x | 16.1/23.7/27.3% | 1.9/5.2% | 3 |
| True | 1 | 0.775 | 0.771 | 0.004 | - | - | 0.870 | 0.870 | 0.372 | 1.49x | 17.8/25.1/28.5% | 2.1/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| random | 1 | 0.808 | 0.799 | 0.009 | - | - | 0.951 | 0.952 | 0.267 | 1.33x | 15.5/22.6/26.2% | 2.1/4.9% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.597 | 0.562 | 0.035 | - | - | 0.888 | 0.890 | 0.155 | 1.06x | 11.7/19.6/23.0% | 1.5/4.3% | 3 |
| 7 | 1 | 0.828 | 0.825 | 0.003 | - | - | 0.926 | 0.926 | 0.375 | 1.53x | 17.4/24.7/28.7% | 2.4/5.2% | 3 |
| 15 | 1 | 0.858 | 0.858 | 0.001 | - | - | 0.931 | 0.931 | 0.491 | 1.52x | 17.3/24.4/28.3% | 2.3/5.2% | 3 |
| 32 | 1 | 0.861 | 0.859 | 0.001 | - | - | 0.936 | 0.936 | 0.470 | 1.53x | 17.5/24.4/28.4% | 2.4/5.2% | 3 |

> hop-limit=3: decode_failures 3

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.597 | 0.562 | 0.035 | - | - | 0.888 | 0.890 | 0.155 | 1.06x | 11.7/19.6/23.0% | 1.5/4.3% | 3 |
| 5 | 1 | 0.767 | 0.758 | 0.010 | - | - | 0.926 | 0.926 | 0.253 | 1.36x | 15.5/23.0/27.0% | 2.1/5.0% | 3 |
| 7 | 1 | 0.828 | 0.825 | 0.003 | - | - | 0.926 | 0.926 | 0.375 | 1.53x | 17.4/24.7/28.7% | 2.4/5.2% | 3 |

> hop-limit=3: decode_failures 3

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| KNOWN_ONLY | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.735 | 0.735 | 0.000 | - | - | 0.802 | 0.858 | 0.341 | 1.32x | 15.2/22.5/26.2% | 2.0/4.8% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.597 | 0.562 | 0.035 | - | - | 0.888 | 0.890 | 0.155 | 1.06x | 11.7/19.6/23.0% | 1.5/4.3% | 3 |
| True | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

> hop-spread=False: decode_failures 3

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| BALANCED | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| STRICT | 1 | 0.621 | 0.621 | 0.000 | - | - | 0.739 | 0.739 | 0.262 | 1.46x | 16.9/24.7/28.6% | 2.3/5.2% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| dm | 1 | 0.750 | 0.741 | 0.009 | - | - | 0.867 | 0.869 | 0.337 | 1.35x | 15.6/23.2/27.0% | 2.1/4.9% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.752 | 0.743 | 0.010 | - | - | 0.873 | 0.875 | 0.320 | 1.37x | 15.8/23.3/27.2% | 2.1/5.0% | 3 |
| local | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| time | 1 | 0.743 | 0.734 | 0.009 | - | - | 0.859 | 0.862 | 0.328 | 1.41x | 16.2/24.2/28.2% | 2.2/5.1% | 3 |
| window | 1 | 0.753 | 0.743 | 0.010 | - | - | 0.874 | 0.877 | 0.325 | 1.34x | 15.4/22.8/26.6% | 2.1/4.9% | 3 |

> bucket-mode=global: misdecodes 36

> bucket-mode=time: misdecodes 38

> bucket-mode=window: misdecodes 21

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.732 | 0.723 | 0.009 | - | - | 0.848 | 0.851 | 0.325 | 1.46x | 16.6/25.1/29.0% | 2.2/5.4% | 3 |
| 1800 | 1 | 0.743 | 0.734 | 0.009 | - | - | 0.859 | 0.862 | 0.328 | 1.41x | 16.2/24.2/28.2% | 2.2/5.1% | 3 |
| 3600 | 1 | 0.739 | 0.729 | 0.010 | - | - | 0.855 | 0.858 | 0.330 | 1.37x | 15.8/23.3/27.2% | 2.1/5.0% | 3 |

> time-bucket-s=600: misdecodes 90

> time-bucket-s=1800: misdecodes 38

> time-bucket-s=3600: misdecodes 14

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| interval | 1 | 0.736 | 0.722 | 0.014 | - | - | 0.856 | 0.860 | 0.342 | 1.79x | 20.1/31.2/36.2% | 2.7/6.9% | 3 |
| aimd | 1 | 0.735 | 0.732 | 0.004 | - | - | 0.825 | 0.854 | 0.325 | 1.36x | 15.8/23.2/26.9% | 2.1/4.9% | 3 |
| bucket+interval | 1 | 0.724 | 0.710 | 0.014 | - | - | 0.844 | 0.845 | 0.318 | 1.80x | 20.2/31.1/36.0% | 2.6/6.9% | 3 |

> trigger=interval: misdecodes 14

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 3

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.743 | 0.735 | 0.008 | - | - | 0.856 | 0.864 | 0.338 | 1.36x | 15.7/23.4/27.2% | 2.1/5.0% | 3 |
| 8 | 1 | 0.747 | 0.737 | 0.010 | - | - | 0.866 | 0.868 | 0.319 | 1.35x | 15.6/23.1/26.8% | 2.1/4.9% | 3 |
| 16 | 1 | 0.748 | 0.740 | 0.008 | - | - | 0.867 | 0.869 | 0.332 | 1.36x | 15.6/23.3/27.0% | 2.1/5.0% | 3 |
| 32 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 50 | 1 | 0.747 | 0.740 | 0.007 | - | - | 0.868 | 0.869 | 0.310 | 1.37x | 15.8/23.3/27.2% | 2.1/5.0% | 3 |

> capacity=4: decode_failures 91

> capacity=8: decode_failures 26

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.743 | 0.735 | 0.008 | - | - | 0.856 | 0.864 | 0.338 | 1.36x | 15.7/23.4/27.2% | 2.1/5.0% | 3 |
| 8 | 1 | 0.747 | 0.737 | 0.010 | - | - | 0.866 | 0.868 | 0.319 | 1.35x | 15.6/23.1/26.8% | 2.1/4.9% | 3 |
| 16 | 1 | 0.748 | 0.740 | 0.008 | - | - | 0.867 | 0.869 | 0.332 | 1.36x | 15.6/23.3/27.0% | 2.1/5.0% | 3 |
| 32 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 50 | 1 | 0.747 | 0.740 | 0.007 | - | - | 0.868 | 0.869 | 0.310 | 1.37x | 15.8/23.3/27.2% | 2.1/5.0% | 3 |

> capacity=4: decode_failures 91

> capacity=8: decode_failures 26

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.748 | 0.739 | 0.009 | - | - | 0.855 | 0.868 | 0.335 | 1.37x | 15.8/23.3/27.2% | 2.1/5.0% | 3 |
| 16 | 1 | 0.742 | 0.731 | 0.011 | - | - | 0.862 | 0.864 | 0.334 | 1.37x | 15.8/23.3/27.1% | 2.1/5.0% | 3 |
| 32 | 1 | 0.753 | 0.743 | 0.010 | - | - | 0.874 | 0.877 | 0.325 | 1.34x | 15.4/22.8/26.6% | 2.1/4.9% | 3 |

> capacity=8: misdecodes 25

> capacity=8: decode_failures 29

> capacity=16: misdecodes 26

> capacity=16: decode_failures 1

> capacity=32: misdecodes 21

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.724 | 0.710 | 0.014 | - | - | 0.844 | 0.845 | 0.318 | 1.80x | 20.2/31.1/36.0% | 2.6/6.9% | 3 |
| 02-06 | 1 | 0.741 | 0.736 | 0.005 | - | - | 0.838 | 0.867 | 0.325 | 1.41x | 16.2/24.2/28.2% | 2.2/5.1% | 3 |
| 00-08 | 1 | 0.743 | 0.738 | 0.005 | - | - | 0.849 | 0.870 | 0.326 | 1.45x | 16.6/25.0/29.0% | 2.2/5.4% | 3 |

> catch-up-hours=: misdecodes 3

> catch-up-hours=02-06: decode_failures 13

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 12

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.729 | 0.728 | 0.001 | - | - | 0.847 | 0.848 | 0.317 | 1.35x | 15.8/23.1/26.7% | 2.1/4.9% | 3 |
| 2 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 3 | 1 | 0.756 | 0.736 | 0.020 | - | - | 0.872 | 0.878 | 0.326 | 1.40x | 16.3/23.8/27.6% | 2.2/5.2% | 3 |
| 4 | 1 | 0.755 | 0.732 | 0.022 | - | - | 0.856 | 0.868 | 0.339 | 1.38x | 16.0/23.5/27.6% | 2.1/5.0% | 3 |

> hops-apart=4: decode_failures 19

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.729 | 0.728 | 0.001 | - | - | 0.847 | 0.848 | 0.317 | 1.35x | 15.8/23.1/26.7% | 2.1/4.9% | 3 |
| 2 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 3 | 1 | 0.756 | 0.736 | 0.020 | - | - | 0.872 | 0.878 | 0.326 | 1.40x | 16.3/23.8/27.6% | 2.2/5.2% | 3 |
| 4 | 1 | 0.755 | 0.732 | 0.022 | - | - | 0.856 | 0.868 | 0.339 | 1.38x | 16.0/23.5/27.6% | 2.1/5.0% | 3 |
| 5 | 1 | 0.783 | 0.747 | 0.036 | - | - | 0.801 | 0.961 | 0.356 | 1.39x | 16.0/23.1/26.8% | 2.2/5.0% | 3 |

> hops-apart=4: decode_failures 19

> hops-apart=5: decode_failures 29

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.751 | 0.742 | 0.009 | - | - | 0.872 | 0.874 | 0.325 | 1.36x | 15.7/23.3/26.9% | 2.1/4.9% | 3 |
| 30 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 120 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.329 | 1.37x | 15.7/23.3/27.1% | 2.1/5.0% | 3 |
| 600 | 1 | 0.747 | 0.739 | 0.008 | - | - | 0.861 | 0.862 | 0.344 | 1.38x | 15.9/23.5/27.4% | 2.1/5.0% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.751 | 0.742 | 0.009 | - | - | 0.872 | 0.874 | 0.325 | 1.36x | 15.7/23.3/26.9% | 2.1/4.9% | 3 |
| 30 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 120 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.329 | 1.37x | 15.7/23.3/27.1% | 2.1/5.0% | 3 |
| 600 | 1 | 0.747 | 0.739 | 0.008 | - | - | 0.861 | 0.862 | 0.344 | 1.38x | 15.9/23.5/27.4% | 2.1/5.0% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.748 | 0.739 | 0.009 | - | - | 0.641 | 0.925 | 0.315 | 1.36x | 15.6/23.0/26.8% | 2.1/4.9% | 3 |
| routers | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.877 | 0.879 | 0.319 | 1.36x | 15.8/23.1/26.9% | 2.1/5.1% | 3 |
| alternate-routers | 1 | 0.748 | 0.739 | 0.009 | - | - | 0.874 | 0.878 | 0.326 | 1.39x | 16.1/23.6/27.5% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.748 | 0.733 | 0.015 | - | - | 0.881 | 0.881 | 0.327 | 1.37x | 15.8/23.1/27.0% | 2.1/5.0% | 3 |
| random-clients | 1 | 0.742 | 0.727 | 0.015 | - | - | 0.860 | 0.861 | 0.316 | 1.36x | 15.8/23.2/26.8% | 2.1/5.0% | 3 |
| hops-apart | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

> place=spread: decode_failures 14

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.748 | 0.739 | 0.009 | - | - | 0.641 | 0.925 | 0.315 | 1.36x | 15.6/23.0/26.8% | 2.1/4.9% | 3 |
| routers | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.877 | 0.879 | 0.319 | 1.36x | 15.8/23.1/26.9% | 2.1/5.1% | 3 |
| alternate-routers | 1 | 0.748 | 0.739 | 0.009 | - | - | 0.874 | 0.878 | 0.326 | 1.39x | 16.1/23.6/27.5% | 2.1/5.3% | 3 |
| beside-router | 1 | 0.748 | 0.733 | 0.015 | - | - | 0.881 | 0.881 | 0.327 | 1.37x | 15.8/23.1/27.0% | 2.1/5.0% | 3 |
| random-clients | 1 | 0.742 | 0.727 | 0.015 | - | - | 0.860 | 0.861 | 0.316 | 1.36x | 15.8/23.2/26.8% | 2.1/5.0% | 3 |
| hops-apart | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

> place=spread: decode_failures 14

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| broadcast | 1 | 0.764 | 0.727 | 0.038 | - | - | 0.863 | 0.864 | 0.326 | 1.43x | 16.3/24.4/28.2% | 2.2/5.2% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| heard | 1 | 0.743 | 0.733 | 0.010 | - | - | 0.865 | 0.866 | 0.330 | 1.36x | 15.8/23.3/27.1% | 2.1/4.9% | 3 |

> replay-ordering=heard: misdecodes 18

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.764 | 0.727 | 0.038 | - | - | 0.863 | 0.864 | 0.326 | 1.43x | 16.3/24.4/28.2% | 2.2/5.2% | 3 |
| heard | 1 | 0.769 | 0.738 | 0.032 | - | - | 0.873 | 0.875 | 0.325 | 1.43x | 16.5/24.4/28.3% | 2.2/5.2% | 3 |

> replay-ordering=heard: misdecodes 5

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| enum | 1 | 0.738 | 0.728 | 0.009 | - | - | 0.845 | 0.852 | 0.333 | 1.34x | 15.5/23.0/26.8% | 2.1/4.9% | 3 |
| hybrid | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.877 | 0.879 | 0.319 | 1.36x | 15.8/23.1/26.9% | 2.1/5.1% | 3 |
| 6 | 1 | 0.743 | 0.734 | 0.009 | - | - | 0.874 | 0.875 | 0.322 | 1.38x | 15.8/23.6/27.5% | 2.1/5.2% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.741 | 0.738 | 0.003 | - | - | 0.857 | 0.859 | 0.350 | 1.36x | 15.8/23.1/26.8% | 2.1/4.9% | 2 |
| 3 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 5 | 1 | 0.729 | 0.718 | 0.012 | - | - | 0.854 | 0.854 | 0.328 | 1.39x | 16.0/23.9/27.7% | 2.2/5.2% | 5 |
| 8 | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.870 | 0.873 | 0.324 | 1.44x | 16.3/24.8/28.8% | 2.2/5.4% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.741 | 0.738 | 0.003 | - | - | 0.857 | 0.859 | 0.350 | 1.36x | 15.8/23.1/26.8% | 2.1/4.9% | 2 |
| 3 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 5 | 1 | 0.729 | 0.718 | 0.012 | - | - | 0.854 | 0.854 | 0.328 | 1.39x | 16.0/23.9/27.7% | 2.2/5.2% | 5 |
| 8 | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.870 | 0.873 | 0.324 | 1.44x | 16.3/24.8/28.8% | 2.2/5.4% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| True | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |

> faster: 0.826 s per simulated hour against 1.7 over 54 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.748 | 0.737 | 0.012 | - | - | 0.874 | 0.877 | 0.339 | 1.27x | 14.5/21.6/25.3% | 2.0/4.6% | 3 |
| 1 | 1 | 0.742 | 0.732 | 0.010 | - | - | 0.857 | 0.862 | 0.322 | 1.28x | 14.6/21.9/25.7% | 1.9/4.7% | 3 |
| 2 | 1 | 0.729 | 0.720 | 0.009 | - | - | 0.851 | 0.854 | 0.323 | 1.27x | 14.6/21.7/25.4% | 2.0/4.6% | 3 |
| 4 | 1 | 0.737 | 0.730 | 0.007 | - | - | 0.852 | 0.855 | 0.319 | 1.28x | 14.6/21.9/25.6% | 2.0/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.740 | 0.730 | 0.010 | - | - | 0.865 | 0.867 | 0.343 | 1.37x | 15.8/23.4/27.1% | 2.1/5.0% | 3 |
| 24 | 1 | 0.744 | 0.734 | 0.010 | - | - | 0.869 | 0.870 | 0.314 | 1.37x | 15.8/23.5/27.2% | 2.1/5.0% | 3 |
| 32 | 1 | 0.746 | 0.738 | 0.008 | - | - | 0.864 | 0.865 | 0.325 | 1.38x | 15.9/23.6/27.3% | 2.1/5.0% | 3 |
| 64 | 1 | 0.739 | 0.729 | 0.010 | - | - | 0.858 | 0.860 | 0.325 | 1.37x | 15.8/23.3/27.1% | 2.1/5.0% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.754 | 0.741 | 0.013 | - | - | 0.882 | 0.882 | 0.318 | 1.46x | 16.7/25.1/29.2% | 2.2/5.3% | 3 |
| 16 | 1 | 0.742 | 0.731 | 0.011 | - | - | 0.863 | 0.865 | 0.320 | 1.38x | 15.9/23.8/27.6% | 2.1/5.0% | 3 |
| 32 | 1 | 0.753 | 0.743 | 0.010 | - | - | 0.874 | 0.877 | 0.325 | 1.34x | 15.4/22.8/26.6% | 2.1/4.9% | 3 |

> window-size=8: misdecodes 136

> window-size=16: misdecodes 46

> window-size=32: misdecodes 21

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.996 | 0.996 | 0.775 | 2.15x | 22.2/31.6/35.5% | 1.5/5.3% | 3 |
| True | 1 | 0.728 | 0.721 | 0.006 | - | - | 0.812 | 0.934 | 0.524 | 5.91x | 54.7/69.8/75.7% | 4.2/12.6% | 3 |

> no-congestion-scaling=True: decode_failures 91

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.522 | 0.512 | 0.011 | - | - | 0.727 | 0.742 | 0.138 | 4.46x | 15.3/24.6/32.4% | 1.5/5.5% | 3 |
| truesize | 1 | 0.556 | 0.546 | 0.010 | - | - | 0.761 | 0.766 | 0.155 | 3.33x | 11.4/19.5/26.4% | 1.1/4.5% | 3 |

> congestion-input=hotstore: decode_failures 38

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.949 | 0.947 | 0.003 | - | - | 0.999 | 0.999 | 0.801 | 2.01x | 20.6/29.2/32.9% | 1.4/4.9% | 3 |
| adaptive | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.996 | 0.996 | 0.775 | 2.15x | 22.2/31.6/35.5% | 1.5/5.3% | 3 |

