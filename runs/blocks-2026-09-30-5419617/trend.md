# Sweep blocks-2026-09-30-5419617

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 5419617 · seeds 5419617
- **blocks** 87 run
- **compute** 9.8 h of simulator time across every cell
- **generated** 2026-09-30T09:40:25+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>96 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 3
- AD-worst: role-placement=degree: decode_failures 2
- AD-worst: role-placement=inverse: decode_failures 22
- AD-worst: slower: 8.29 s per simulated hour against 3.48 over 40 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 19
- DB-hotstore-stress: max-num-nodes=10: decode_failures 6
- DB-hotstore-stress: faster: 10 s per simulated hour against 22.7 over 40 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DB-warm: warm-num-nodes=0: decode_failures 99
- DB-warm: warm-num-nodes=25: decode_failures 99
- DB-warm: warm-num-nodes=100: decode_failures 99
- DB-warm: warm-num-nodes=2000: decode_failures 99
- DG-burst: burst-loss=0.1: decode_failures 26
- DG-burst: burst-loss=0.2: decode_failures 19
- DG-burst: burst-loss=0.3: decode_failures 36
- DG-loss: extra-loss=0.2: decode_failures 6
- DG-loss: extra-loss=0.3: decode_failures 7
- DG-outage: burst-loss=0.1: decode_failures 32
- DG-outage: burst-loss=0.2: decode_failures 34
- DG-outage: burst-loss=0.3: decode_failures 24
- DM-mode: dm-mode=flood-only: decode_failures 23
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 29
- DM-mode: dm-mode=m4-early-flood: decode_failures 21
- DM-mode: slower: 9.39 s per simulated hour against 3.29 over 40 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 27
- LD-chatty: broadcast-interval-s=300: decode_failures 26
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 99
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 70
- MS-density: nodes=40: decode_failures 16
- MS-hopscale: faster: 6.64 s per simulated hour against 18.2 over 40 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-oversubscribed: faster: 7.78 s per simulated hour against 20.1 over 40 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-siting: siting-mix=local-typical: decode_failures 16
- MS-size: nodes=90: decode_failures 44
- MS-stretch: stretch=1.25: decode_failures 15
- MS-stretch: stretch=2.0: decode_failures 3
- MS-topology: topology=clustered: misdecodes 1
- MS-topology: topology=clustered: decode_failures 1
- PR-crladder: coding-rate-ladder=False: decode_failures 29
- RF-bw500: preset=SHORT_TURBO: decode_failures 5
- RF-noise: noise-profile=temporal: decode_failures 1
- RF-noise: noise-profile=periodic: decode_failures 24
- RF-preset: faster: 1.41 s per simulated hour against 2.97 over 40 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 5
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: misdecodes 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 24
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- RF-stretch-duct: faster: 0.928 s per simulated hour against 1.87 over 40 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=22: decode_failures 3
- RF-txpower: tx-power=17: decode_failures 2
- RT-hoplimit: hop-limit=3: decode_failures 6
- RT-hopspread: hop-limit=3: decode_failures 6
- RT-spread: hop-spread=False: decode_failures 6
- SF-bucket-mode: bucket-mode=global: misdecodes 26
- SF-bucket-mode: bucket-mode=time: misdecodes 22
- SF-bucket-mode: bucket-mode=window: misdecodes 19
- SF-bucket-time: time-bucket-s=600: misdecodes 106
- SF-bucket-time: time-bucket-s=1800: misdecodes 22
- SF-bucket-time: time-bucket-s=3600: misdecodes 10
- SF-bucket-time: time-bucket-s=3600: decode_failures 2
- SF-cadence: trigger=interval: misdecodes 10
- SF-cadence: trigger=interval: decode_failures 2
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=aimd: decode_failures 13
- SF-cadence: trigger=bucket+interval: misdecodes 18
- SF-capacity-local: capacity=4: decode_failures 98
- SF-capacity-local: capacity=8: decode_failures 98
- SF-capacity-local: capacity=16: decode_failures 7
- SF-capacity: capacity=4: decode_failures 98
- SF-capacity: capacity=8: decode_failures 98
- SF-capacity: capacity=16: decode_failures 7
- SF-capacity-window: capacity=8: misdecodes 14
- SF-capacity-window: capacity=8: decode_failures 81
- SF-capacity-window: capacity=16: misdecodes 27
- SF-capacity-window: capacity=16: decode_failures 7
- SF-capacity-window: capacity=32: misdecodes 19
- SF-catchup: catch-up-hours=: misdecodes 18
- SF-catchup: catch-up-hours=02-06: misdecodes 1
- SF-catchup: catch-up-hours=02-06: decode_failures 33
- SF-catchup: catch-up-hours=00-08: misdecodes 2
- SF-catchup: catch-up-hours=00-08: decode_failures 33
- SF-hops-flat: hops-apart=3: decode_failures 19
- SF-hops-flat: hops-apart=4: decode_failures 36
- SF-hops-spread: hops-apart=3: decode_failures 19
- SF-hops-spread: hops-apart=4: decode_failures 36
- SF-hops-spread: hops-apart=5: decode_failures 13
- SF-place-flat: place=spread: decode_failures 4
- SF-place-flat: place=random-clients: decode_failures 3
- SF-place-spread: place=spread: decode_failures 4
- SF-place-spread: place=random-clients: decode_failures 3
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 6
- SF-replay-order: replay-ordering=heard: misdecodes 10
- SF-servers-allrouters: servers=6: decode_failures 1
- SF-window-size: window-size=8: misdecodes 121
- SF-window-size: window-size=16: misdecodes 49
- SF-window-size: window-size=32: misdecodes 19
- TH-congestion-input: faster: 5.19 s per simulated hour against 11.2 over 40 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- TH-congestion: no-congestion-scaling=True: decode_failures 90

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `DM-mode` | 9.39 | 3.29 | 2.85x | 40 |
| `AD-worst` | 8.29 | 3.48 | 2.38x | 40 |
| `BL-control` | 3.7 | 1.88 | 1.97x | 40 |
| `PR-crladder` | 5.29 | 2.79 | 1.90x | 40 |
| `RT-hopspread` | 3.42 | 2.04 | 1.68x | 40 |
| `SF-cadence` | 5.59 | 3.63 | 1.54x | 40 |
| `SF-servers-allrouters` | 2.82 | 1.85 | 1.53x | 40 |
| `SF-hops-spread` | 3.23 | 4.83 | 0.67x | 40 |
| `SF-place-spread` | 1.89 | 2.82 | 0.67x | 40 |
| `AD-siting` | 0.904 | 1.55 | 0.58x | 40 |
| `AD-badrouters` | 1.22 | 2.13 | 0.57x | 40 |
| `RF-eu-presets` | 1.08 | 1.94 | 0.55x | 40 |
| `DB-platform` | 1.39 | 2.52 | 0.55x | 40 |
| `RF-stretch-duct` | 0.928 | 1.87 | 0.50x | 40 |
| `RF-preset` | 1.41 | 2.97 | 0.47x | 40 |
| `TH-congestion-input` | 5.19 | 11.2 | 0.46x | 40 |
| `DB-hotstore-stress` | 10 | 22.7 | 0.44x | 40 |
| `MS-oversubscribed` | 7.78 | 20.1 | 0.39x | 40 |
| `MS-hopscale` | 6.64 | 18.2 | 0.36x | 40 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.912 | 0.912 | 0.657 → 0.691 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.046 → 0.912 | 0.866 | 0.025 → 0.683 | 1.2e+02x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.092 → 0.912 | 0.820 | 0.045 → 0.683 | 16x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.167 → 0.960 | 0.793 | 0.164 → 0.959 | 5.2x sr_bytes | up | 4 |
| `MS-stretch` | stretch | **held** | 0.123 → 0.912 | 0.789 | 0.066 → 0.683 | 8.5x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.009 → 0.778 | 0.769 | 0.005 → 0.601 | 6.8x bytes_on_air | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.084 → 0.847 | 0.763 | 0.060 → 0.621 | 1.7e+02x sr_airtime | down | 4 |
| `BL-control` | protocol | **held** | 0 → 0.709 | 0.709 | 0.685 → 0.691 | 1x bytes_on_air | up | 2 |
| `MS-hopscale` | nodes | **held** | 0.264 → 0.912 | 0.649 | 0.182 → 0.683 | 7.2x bytes_on_air | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.296 → 0.912 | 0.616 | 0.138 → 0.683 | 3.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.296 → 0.912 | 0.616 | 0.138 → 0.689 | 3.4x sr_airtime | up | 3 |
| `RF-bw500` | preset | **held** | 0.202 → 0.801 | 0.599 | 0.074 → 0.557 | 4.3x advert_bytes | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.262 → 0.826 | 0.564 | 0.183 → 0.518 | 4.3x bytes_on_air | down | 3 |
| `MS-topology` | topology | **text** | 0.355 → 0.880 | 0.525 | 0.345 → 0.876 | 2.1x advert_bytes | up | 4 |
| `SF-place-flat` | place | **held** | 0.446 → 0.912 | 0.467 | 0.671 → 0.690 | 2.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.446 → 0.912 | 0.467 | 0.671 → 0.690 | 2.6x sr_bytes | up | 6 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.176 → 0.536 | 0.360 | 0.171 → 0.530 | 2.8x sr_airtime | up | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.562 → 0.912 | 0.351 | 0.675 → 0.685 | 4x sr_bytes | down | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.481 → 0.828 | 0.346 | 0.458 → 0.820 | 7.4x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **held** | 0.578 → 0.912 | 0.334 | 0.353 → 0.683 | 1.7x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.595 → 0.896 | 0.301 | 0.584 → 0.892 | 5.1x advert_bytes | up | 5 |
| `DG-burst` | burst-loss | **text** | 0.408 → 0.702 | 0.294 | 0.369 → 0.683 | 1.9x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.644 → 0.927 | 0.284 | 0.404 → 0.715 | 6.5x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.561 → 0.838 | 0.277 | 0.513 → 0.833 | 2.1x sr_bytes | up | 4 |
| `MS-size` | nodes | **text** | 0.426 → 0.702 | 0.276 | 0.420 → 0.683 | 3.2x sr_airtime | down | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.561 → 0.794 | 0.233 | 0.513 → 0.783 | 1.8x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.619 → 0.849 | 0.230 | 0.603 → 0.843 | 3.5x sr_airtime | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.709 → 0.912 | 0.203 | 0.675 → 0.685 | 4x sr_bytes | down | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.702 → 0.900 | 0.199 | 0.683 → 0.897 | 2.2x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.702 → 0.899 | 0.198 | 0.683 → 0.895 | 2.5x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.715 → 0.912 | 0.198 | 0.513 → 0.683 | 1.3x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **held** | 0.730 → 0.920 | 0.190 | 0.546 → 0.741 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **held** | 0.730 → 0.920 | 0.190 | 0.546 → 0.741 | 2.2x bytes_on_air | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.521 → 0.702 | 0.181 | 0.494 → 0.683 | 1.3x sr_bytes | down | 4 |
| `MS-roles` | role-mix | **held** | 0.730 → 0.909 | 0.179 | 0.546 → 0.702 | 1.2x advert_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.731 → 0.887 | 0.155 | 0.583 → 0.707 | 1.2x advert_bytes | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.702 → 0.847 | 0.145 | 0.683 → 0.836 | 1.4x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.730 → 0.872 | 0.142 | 0.546 → 0.627 | 1.2x advert_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.561 → 0.702 | 0.140 | 0.513 → 0.683 | 1.6x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.566 → 0.702 | 0.136 | 0.566 → 0.683 | 1.2x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.642 → 0.766 | 0.124 | 0.616 → 0.760 | 4.9x sr_airtime | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.625 → 0.749 | 0.123 | 0.615 → 0.735 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.636 → 0.753 | 0.117 | 0.626 → 0.740 | 2.1x bytes_on_air | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.367 → 0.481 | 0.114 | 0.214 → 0.307 | 3.6x sr_airtime | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.628 → 0.734 | 0.106 | 0.606 → 0.725 | 2x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.810 → 0.912 | 0.102 | 0.680 → 0.683 | 33x sr_airtime | down | 3 |
| `DB-platform` | platform-mix | **text** | 0.634 → 0.734 | 0.101 | 0.612 → 0.725 | 2.1x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.839 → 0.912 | 0.074 | 0.631 → 0.683 | 14x advert_bytes | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.645 → 0.702 | 0.056 | 0.620 → 0.683 | 1.4x sr_airtime | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.850 → 0.905 | 0.056 | 0.678 → 0.685 | 2.5x advert_bytes | up | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.702 → 0.750 | 0.048 | 0.683 → 0.741 | 3.3x bytes_on_air | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.570 → 0.616 | 0.046 | 0.558 → 0.600 | 1.2x sr_airtime | down | 2 |
| `FW-versions` | profile | **text** | 0.660 → 0.702 | 0.041 | 0.652 → 0.683 | 3.5x bytes_on_air | up | 5 |
| `FW-firmware` | profile | **text** | 0.664 → 0.702 | 0.037 | 0.657 → 0.683 | 3.5x bytes_on_air | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.702 → 0.738 | 0.036 | 0.660 → 0.683 | 3.5x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.660 → 0.696 | 0.036 | 0.631 → 0.682 | 9.4x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.707 → 0.737 | 0.031 | 0.695 → 0.728 | 1.1x sr_bytes | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.841 → 0.871 | 0.030 | 0.630 → 0.655 | 1.3x sr_airtime | up | 3 |
| `SF-servers-allrouters` | servers | **held** | 0.882 → 0.909 | 0.027 | 0.669 → 0.690 | 3.3x sr_bytes | up | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.309 → 0.334 | 0.025 | 0.305 → 0.330 | 1.9x sr_airtime | up | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.888 → 0.912 | 0.024 | 0.675 → 0.683 | 1.1x sr_airtime | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.892 → 0.915 | 0.024 | 0.668 → 0.683 | 5.3x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.892 → 0.915 | 0.024 | 0.668 → 0.683 | 5.3x sr_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.889 → 0.912 | 0.023 | 0.679 → 0.688 | 1.3x sr_bytes | down | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.676 → 0.698 | 0.022 | 0.656 → 0.681 | 5.1x advert_bytes | up | 3 |
| `SF-capacity` | capacity | **held** | 0.894 → 0.914 | 0.020 | 0.676 → 0.683 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.894 → 0.914 | 0.020 | 0.676 → 0.683 | 5.3x advert_bytes | up | 5 |
| `SF-width` | short-id-bits | **held** | 0.900 → 0.919 | 0.019 | 0.673 → 0.685 | 3.1x advert_bytes | down | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.895 → 0.912 | 0.018 | 0.671 → 0.683 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.895 → 0.912 | 0.018 | 0.671 → 0.683 | 1.1x sr_bytes | up | 4 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.686 → 0.702 | 0.015 | 0.668 → 0.685 | 2.6x advert_bytes | up | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.878 → 0.892 | 0.013 | 0.657 → 0.660 | 1.1x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **held** | 0.912 → 0.924 | 0.012 | 0.683 → 0.697 | 1.5x sr_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.900 → 0.912 | 0.012 | 0.681 → 0.683 | 5.8x advert_bytes | = | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.838 → 0.849 | 0.011 | 0.831 → 0.843 | 1.2x sr_airtime | down | 2 |
| `SF-window-size` | window-size | **text** | 0.693 → 0.702 | 0.009 | 0.672 → 0.685 | 4.2x advert_bytes | up | 3 |
| `AD-worst` | role-placement | **text** | 0.600 → 0.608 | 0.008 | 0.577 → 0.590 | 1.1x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.905 → 0.912 | 0.007 | 0.683 → 0.693 | 1.2x sr_bytes | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.900 → 0.907 | 0.006 | 0.684 → 0.689 | 1.3x sr_bytes | up | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.650 → 0.655 | 0.006 | 0.650 → 0.655 | 1.3x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.907 → 0.912 | 0.005 | 0.679 → 0.683 | 2.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.849 → 0.854 | 0.005 | 0.843 → 0.849 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.849 → 0.854 | 0.005 | 0.843 → 0.848 | 1.1x bytes_on_air | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.645 → 0.650 | 0.005 | 0.645 → 0.650 | 1.1x sr_bytes | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.698 → 0.702 | 0.004 | 0.683 → 0.684 | 1.1x sr_bytes | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario flat`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| sprinkled | 1 | 0.741 | 0.735 | 0.005 | - | - | 0.941 | 0.942 | 0.403 | 1.25x | 14.2/21.2/22.6% | 1.8/5.2% | 3 |
| arms-race | 1 | 0.900 | 0.897 | 0.003 | - | - | 0.946 | 0.947 | 0.617 | 1.10x | 18.9/24.3/26.6% | 1.5/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.787 | 0.766 | 0.021 | - | - | 0.876 | 0.877 | 0.268 | 1.39x | 16.2/21.9/24.1% | 2.1/5.1% | 3 |
| 0.3 | 1 | 0.899 | 0.895 | 0.004 | - | - | 0.992 | 0.993 | 0.685 | 1.23x | 20.7/26.0/31.1% | 1.8/5.2% | 3 |

> amplify-worst=0.1: decode_failures 3

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.568 | 0.546 | 0.023 | - | - | 0.730 | 0.739 | 0.000 | 1.11x | 11.7/18.3/22.2% | 1.8/4.7% | 3 |
| inverse | 1 | 0.637 | 0.609 | 0.029 | - | - | 0.860 | 0.865 | 0.264 | 1.17x | 11.7/16.7/19.4% | 2.2/3.9% | 3 |
| random | 1 | 0.649 | 0.627 | 0.023 | - | - | 0.872 | 0.878 | 0.184 | 1.15x | 11.7/19.1/24.2% | 1.9/4.6% | 3 |

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.568 | 0.546 | 0.023 | - | - | 0.730 | 0.739 | 0.000 | 1.11x | 11.7/18.3/22.2% | 1.8/4.7% | 3 |
| all-routers | 1 | 0.757 | 0.741 | 0.017 | - | - | 0.920 | 0.922 | 0.235 | 2.45x | 22.6/32.5/36.7% | 4.1/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.568 | 0.546 | 0.023 | - | - | 0.730 | 0.739 | 0.000 | 1.11x | 11.7/18.3/22.2% | 1.8/4.7% | 3 |
| no-mute | 1 | 0.696 | 0.676 | 0.020 | - | - | 0.884 | 0.890 | 0.293 | 1.35x | 13.6/19.7/22.2% | 2.0/4.6% | 3 |
| all-routers | 1 | 0.757 | 0.741 | 0.017 | - | - | 0.920 | 0.922 | 0.235 | 2.45x | 22.6/32.5/36.7% | 4.1/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.568 | 0.546 | 0.023 | - | - | 0.730 | 0.739 | 0.000 | 1.11x | 11.7/18.3/22.2% | 1.8/4.7% | 3 |
| local-typical | 1 | 0.609 | 0.601 | 0.008 | - | - | 0.778 | 0.785 | 0.000 | 1.30x | 10.5/19.2/30.0% | 2.1/5.0% | 3 |
| basement-heavy | 1 | 0.005 | 0.005 | 0.000 | - | - | 0.009 | 0.021 | 0.000 | 0.20x | 0.2/1.4/2.3% | 0.2/0.9% | 3 |

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.608 | 0.590 | 0.017 | - | - | 0.848 | 0.852 | 0.000 | 2.37x | 11.8/24.3/29.2% | 1.9/5.7% | 3 |
| inverse | 1 | 0.600 | 0.577 | 0.023 | - | - | 0.853 | 0.862 | 0.000 | 2.38x | 10.9/22.5/26.5% | 2.0/3.3% | 3 |

> role-placement=degree: decode_failures 2

> role-placement=inverse: decode_failures 22

> slower: 8.29 s per simulated hour against 3.48 over 40 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.691 | 0.691 | 0.000 | - | - | 0 | 0.000 | 0.193 | 1.29x | 13.4/20.4/23.0% | 1.8/4.8% | 3 |
| sr | 1 | 0.698 | 0.685 | 0.012 | - | - | 0.709 | 0.904 | 0.196 | 1.32x | 13.5/21.1/23.7% | 1.8/4.8% | 3 |

> protocol=sr: decode_failures 19

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.628 | 0.606 | 0.023 | - | - | 0.808 | 0.812 | 0.191 | 2.80x | 27.4/45.5/50.6% | 4.2/8.7% | 3 |
| 100 | 1 | 0.734 | 0.725 | 0.010 | - | - | 0.882 | 0.883 | 0.199 | 1.54x | 15.0/26.0/29.4% | 2.2/5.0% | 3 |
| 120 | 1 | 0.734 | 0.725 | 0.010 | - | - | 0.882 | 0.883 | 0.199 | 1.54x | 15.0/26.0/29.4% | 2.2/5.0% | 3 |
| 250 | 1 | 0.734 | 0.725 | 0.010 | - | - | 0.882 | 0.883 | 0.199 | 1.54x | 15.0/26.0/29.4% | 2.2/5.0% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.217 | 0.214 | 0.003 | - | - | 0.367 | 0.369 | 0.052 | 10.49x | 29.7/46.3/57.0% | 3.8/10.0% | 3 |
| 120 | 1 | 0.309 | 0.305 | 0.004 | - | - | 0.481 | 0.481 | 0.070 | 4.61x | 13.1/20.2/24.5% | 1.7/4.1% | 3 |
| 250 | 1 | 0.311 | 0.307 | 0.004 | - | - | 0.479 | 0.480 | 0.079 | 4.66x | 13.1/20.0/24.5% | 1.7/4.1% | 3 |

> max-num-nodes=10: decode_failures 6

> faster: 10 s per simulated hour against 22.7 over 40 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.734 | 0.725 | 0.010 | - | - | 0.882 | 0.883 | 0.199 | 1.54x | 15.0/26.0/29.4% | 2.2/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.734 | 0.725 | 0.010 | - | - | 0.882 | 0.883 | 0.199 | 1.54x | 15.0/26.0/29.4% | 2.2/5.0% | 3 |
| constrained | 1 | 0.634 | 0.612 | 0.022 | - | - | 0.807 | 0.817 | 0.195 | 2.80x | 27.5/45.4/50.5% | 4.3/8.7% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.616 | 0.600 | 0.016 | - | - | 0.817 | 0.853 | 0.358 | 5.84x | 46.9/68.8/76.5% | 4.1/11.6% | 3 |
| 25 | 1 | 0.616 | 0.600 | 0.016 | - | - | 0.817 | 0.853 | 0.358 | 5.84x | 46.9/68.8/76.5% | 4.1/11.6% | 3 |
| 100 | 1 | 0.616 | 0.600 | 0.016 | - | - | 0.817 | 0.853 | 0.358 | 5.84x | 46.9/68.8/76.5% | 4.1/11.6% | 3 |
| 2000 | 1 | 0.616 | 0.600 | 0.016 | - | - | 0.817 | 0.853 | 0.358 | 5.84x | 46.9/68.8/76.5% | 4.1/11.6% | 3 |

> warm-num-nodes=0: decode_failures 99

> warm-num-nodes=25: decode_failures 99

> warm-num-nodes=100: decode_failures 99

> warm-num-nodes=2000: decode_failures 99

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.590 | 0.565 | 0.025 | - | - | 0.837 | 0.863 | 0.130 | 1.21x | 12.5/19.9/22.8% | 1.7/4.3% | 3 |
| 0.2 | 1 | 0.497 | 0.466 | 0.030 | - | - | 0.754 | 0.800 | 0.091 | 1.11x | 11.3/18.8/21.6% | 1.6/3.8% | 3 |
| 0.3 | 1 | 0.408 | 0.369 | 0.039 | - | - | 0.673 | 0.744 | 0.060 | 0.99x | 10.2/17.0/20.0% | 1.4/3.4% | 3 |

> burst-loss=0.1: decode_failures 26

> burst-loss=0.2: decode_failures 19

> burst-loss=0.3: decode_failures 36

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.648 | 0.629 | 0.019 | - | - | 0.880 | 0.881 | 0.139 | 1.32x | 13.4/21.3/24.3% | 1.9/4.5% | 3 |
| 0.2 | 1 | 0.599 | 0.574 | 0.025 | - | - | 0.857 | 0.872 | 0.086 | 1.32x | 13.2/21.7/24.9% | 2.0/4.3% | 3 |
| 0.3 | 1 | 0.521 | 0.494 | 0.027 | - | - | 0.750 | 0.791 | 0.068 | 1.30x | 13.2/21.5/25.1% | 2.0/4.0% | 3 |

> extra-loss=0.2: decode_failures 6

> extra-loss=0.3: decode_failures 7

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.577 | 0.551 | 0.026 | - | - | 0.820 | 0.852 | 0.125 | 1.23x | 12.6/20.1/23.0% | 1.8/4.5% | 3 |
| 0.2 | 1 | 0.482 | 0.458 | 0.024 | - | - | 0.694 | 0.802 | 0.083 | 1.13x | 11.6/18.5/21.5% | 1.7/4.0% | 3 |
| 0.3 | 1 | 0.376 | 0.353 | 0.023 | - | - | 0.578 | 0.738 | 0.053 | 1.02x | 10.6/17.3/20.5% | 1.5/3.6% | 3 |

> burst-loss=0.1: decode_failures 32

> burst-loss=0.2: decode_failures 34

> burst-loss=0.3: decode_failures 24

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.630 | 0.630 | 0.000 | - | - | 0.841 | 0.873 | 0.177 | 1.69x | 17.4/27.1/30.0% | 2.4/6.2% | 3 |
| directed-with-late-flood | 1 | 0.655 | 0.655 | 0.000 | - | - | 0.871 | 0.899 | 0.194 | 1.54x | 15.9/25.1/28.2% | 2.1/5.8% | 3 |
| m4-early-flood | 1 | 0.642 | 0.642 | 0.000 | - | - | 0.849 | 0.884 | 0.190 | 1.55x | 16.0/25.4/28.3% | 2.2/5.8% | 3 |

> dm-mode=flood-only: decode_failures 23

> dm-mode=directed-with-late-flood: decode_failures 29

> dm-mode=m4-early-flood: decode_failures 21

> slower: 9.39 s per simulated hour against 3.29 over 40 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.664 | 0.657 | 0.007 | - | - | 0.885 | 0.888 | 0.036 | 0.69x | 6.6/10.3/12.9% | 1.1/2.0% | 3 |
| 2.8 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.941 | 0.943 | 0.313 | 1.23x | 13.8/19.3/25.8% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.625 | 0.615 | 0.010 | - | - | 0.881 | 0.883 | 0.121 | 0.99x | 10.2/17.6/19.4% | 1.6/3.7% | 3 |
| 0.75 | 1 | 0.707 | 0.700 | 0.008 | - | - | 0.912 | 0.913 | 0.314 | 0.89x | 9.0/14.5/18.0% | 1.4/3.4% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.753 | 0.740 | 0.014 | - | - | 0.942 | 0.945 | 0.285 | 1.22x | 13.5/19.5/26.0% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.636 | 0.626 | 0.010 | - | - | 0.883 | 0.885 | 0.147 | 0.97x | 10.0/17.0/18.8% | 1.5/3.7% | 3 |
| 0.75 | 1 | 0.705 | 0.696 | 0.009 | - | - | 0.909 | 0.911 | 0.316 | 0.90x | 9.5/14.7/18.6% | 1.4/3.5% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.750 | 0.741 | 0.009 | - | - | 0.932 | 0.932 | 0.246 | 0.73x | 7.6/12.3/14.1% | 1.0/2.9% | 3 |
| signing=true | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.666 | 0.660 | 0.006 | - | - | 0.886 | 0.888 | 0.037 | 0.71x | 6.8/11.3/14.0% | 1.1/2.4% | 3 |
| 2.5 | 1 | 0.660 | 0.652 | 0.008 | - | - | 0.892 | 0.893 | 0.035 | 0.72x | 6.8/11.1/13.7% | 1.1/2.3% | 3 |
| 2.6 | 1 | 0.663 | 0.657 | 0.006 | - | - | 0.894 | 0.894 | 0.035 | 0.70x | 6.9/11.2/14.0% | 1.1/2.4% | 3 |
| 2.7 | 1 | 0.688 | 0.682 | 0.006 | - | - | 0.886 | 0.886 | 0.037 | 0.74x | 7.0/14.7/16.8% | 1.0/2.9% | 3 |
| 2.8 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.728 | 0.715 | 0.013 | - | - | 0.927 | 0.930 | 0.208 | 0.90x | 9.2/14.4/16.1% | 1.3/3.3% | 3 |
| 900 | 1 | 0.642 | 0.616 | 0.026 | - | - | 0.881 | 0.884 | 0.187 | 2.03x | 20.9/32.5/35.8% | 2.8/7.3% | 3 |
| 300 | 1 | 0.444 | 0.404 | 0.040 | - | - | 0.644 | 0.727 | 0.110 | 4.14x | 40.1/59.9/63.8% | 6.2/13.3% | 3 |

> broadcast-interval-s=300: decode_failures 26

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.828 | 0.820 | 0.007 | - | - | 0.945 | 0.947 | 0.340 | 1.02x | 10.0/14.7/16.6% | 1.5/3.4% | 3 |
| 900 | 1 | 0.741 | 0.725 | 0.016 | - | - | 0.888 | 0.889 | 0.277 | 2.30x | 23.1/33.7/37.7% | 3.3/7.6% | 3 |
| 300 | 1 | 0.481 | 0.458 | 0.023 | - | - | 0.615 | 0.697 | 0.189 | 4.66x | 43.7/63.2/66.5% | 6.8/14.4% | 3 |

> broadcast-interval-s=300: decode_failures 27

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.710 | 0.694 | 0.015 | - | - | 0.915 | 0.918 | 0.211 | 1.23x | 12.7/19.8/22.3% | 1.7/4.5% | 3 |
| sinusoid | 1 | 0.713 | 0.697 | 0.016 | - | - | 0.924 | 0.926 | 0.212 | 1.18x | 12.2/18.7/21.0% | 1.7/4.3% | 3 |
| commuter | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.642 | 0.616 | 0.026 | - | - | 0.881 | 0.884 | 0.187 | 2.03x | 20.9/32.5/35.8% | 2.8/7.3% | 3 |
| 3600 | 1 | 0.728 | 0.715 | 0.013 | - | - | 0.927 | 0.930 | 0.208 | 0.90x | 9.2/14.4/16.1% | 1.3/3.3% | 3 |
| 10800 | 1 | 0.743 | 0.733 | 0.010 | - | - | 0.940 | 0.940 | 0.211 | 0.58x | 5.9/9.5/10.6% | 0.8/2.2% | 3 |
| 43200 | 1 | 0.766 | 0.760 | 0.006 | - | - | 0.951 | 0.952 | 0.239 | 0.42x | 4.2/6.9/7.7% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.692 | 0.673 | 0.018 | - | - | 0.904 | 0.907 | 0.199 | 1.38x | 14.3/22.1/24.7% | 1.9/5.1% | 3 |
| 1.0 | 1 | 0.680 | 0.662 | 0.018 | - | - | 0.892 | 0.896 | 0.195 | 1.50x | 15.6/24.2/27.2% | 2.1/5.6% | 3 |
| 4.0 | 1 | 0.645 | 0.620 | 0.025 | - | - | 0.878 | 0.882 | 0.171 | 1.83x | 19.0/30.2/33.8% | 2.6/7.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.616 | 0.600 | 0.016 | - | - | 0.817 | 0.853 | 0.358 | 5.84x | 46.9/68.8/76.5% | 4.1/11.6% | 3 |
| 1.0 | 1 | 0.570 | 0.558 | 0.011 | - | - | 0.788 | 0.829 | 0.333 | 6.41x | 50.7/70.8/78.1% | 4.6/12.2% | 3 |

> traceroute-per-hour=0.0: decode_failures 99

> traceroute-per-hour=1.0: decode_failures 70

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.595 | 0.584 | 0.011 | - | - | 0.789 | 0.844 | 0.240 | 1.31x | 12.6/24.3/27.1% | 3.0/6.1% | 3 |
| 60 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 90 | 1 | 0.830 | 0.824 | 0.006 | - | - | 0.977 | 0.978 | 0.338 | 1.73x | 15.6/26.8/33.1% | 1.6/5.1% | 3 |
| 120 | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.977 | 0.978 | 0.495 | 2.20x | 18.4/32.5/38.0% | 1.4/5.0% | 3 |
| 150 | 1 | 0.896 | 0.892 | 0.004 | - | - | 0.998 | 0.998 | 0.630 | 2.72x | 21.8/38.1/43.7% | 1.5/5.5% | 3 |

> nodes=40: decode_failures 16

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 120 | 1 | 0.518 | 0.514 | 0.004 | - | - | 0.830 | 0.830 | 0.049 | 2.27x | 10.8/21.0/26.2% | 1.6/4.8% | 3 |
| 250 | 1 | 0.310 | 0.306 | 0.004 | - | - | 0.480 | 0.480 | 0.076 | 4.89x | 13.9/21.3/26.2% | 1.8/4.4% | 3 |
| 500 | 1 | 0.184 | 0.182 | 0.002 | - | - | 0.264 | 0.264 | 0.032 | 9.60x | 13.2/19.0/33.9% | 1.8/4.9% | 3 |

> faster: 6.64 s per simulated hour against 18.2 over 40 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.521 | 0.518 | 0.004 | - | - | 0.826 | 0.831 | 0.058 | 2.11x | 10.1/19.5/24.4% | 1.5/4.5% | 3 |
| 250 | 1 | 0.309 | 0.305 | 0.004 | - | - | 0.481 | 0.481 | 0.070 | 4.61x | 13.1/20.2/24.5% | 1.7/4.1% | 3 |
| 500 | 1 | 0.184 | 0.183 | 0.002 | - | - | 0.262 | 0.263 | 0.029 | 9.06x | 12.5/17.8/31.8% | 1.7/4.5% | 3 |

> faster: 7.78 s per simulated hour against 20.1 over 40 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.723 | 0.702 | 0.021 | - | - | 0.909 | 0.911 | 0.233 | 1.35x | 14.0/20.9/23.6% | 1.9/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.568 | 0.546 | 0.023 | - | - | 0.730 | 0.739 | 0.000 | 1.11x | 11.7/18.3/22.2% | 1.8/4.7% | 3 |

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.725 | 0.707 | 0.018 | - | - | 0.887 | 0.890 | 0.251 | 1.37x | 14.0/21.0/23.8% | 2.0/4.8% | 3 |
| baymesh-2026-08 | 1 | 0.600 | 0.583 | 0.017 | - | - | 0.731 | 0.733 | 0.000 | 1.21x | 12.0/20.9/25.3% | 2.0/4.6% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.05 | 1 | 0.700 | 0.686 | 0.014 | - | - | 0.894 | 0.896 | 0.191 | 1.46x | 14.6/25.0/30.2% | 2.1/5.0% | 3 |
| 0.1 | 1 | 0.706 | 0.688 | 0.018 | - | - | 0.900 | 0.903 | 0.202 | 1.50x | 14.7/26.3/30.9% | 2.2/4.9% | 3 |
| 0.2 | 1 | 0.695 | 0.679 | 0.016 | - | - | 0.889 | 0.893 | 0.191 | 1.64x | 17.0/28.3/37.2% | 2.6/4.8% | 3 |

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| local-typical | 1 | 0.627 | 0.615 | 0.012 | - | - | 0.763 | 0.785 | 0.000 | 1.53x | 11.6/20.4/26.9% | 2.4/5.1% | 3 |
| event | 1 | 0.167 | 0.164 | 0.002 | - | - | 0.424 | 0.424 | 0.000 | 0.93x | 2.5/16.0/21.4% | 1.0/5.1% | 3 |
| backbone | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.990 | 0.990 | 0.810 | 1.24x | 24.2/33.0/36.6% | 1.7/5.5% | 3 |

> siting-mix=local-typical: decode_failures 16

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.690 | 0.674 | 0.017 | - | - | 0.854 | 0.856 | 0.252 | 1.26x | 16.8/25.5/29.4% | 2.9/6.8% | 3 |
| 60 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 90 | 1 | 0.598 | 0.585 | 0.013 | - | - | 0.862 | 0.888 | 0.000 | 1.68x | 12.5/18.7/22.0% | 1.7/5.3% | 3 |
| 120 | 1 | 0.518 | 0.514 | 0.004 | - | - | 0.830 | 0.830 | 0.049 | 2.27x | 10.8/21.0/26.2% | 1.6/4.8% | 3 |
| 150 | 1 | 0.426 | 0.420 | 0.006 | - | - | 0.660 | 0.660 | 0.103 | 2.81x | 11.8/21.6/32.4% | 1.7/4.4% | 3 |

> nodes=90: decode_failures 44

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 1.25 | 1 | 0.394 | 0.377 | 0.017 | - | - | 0.598 | 0.671 | 0.000 | 1.27x | 9.4/17.3/21.7% | 1.8/4.6% | 3 |
| 1.5 | 1 | 0.176 | 0.171 | 0.004 | - | - | 0.325 | 0.327 | 0.000 | 1.08x | 5.9/12.7/19.8% | 1.5/4.5% | 3 |
| 2.0 | 1 | 0.067 | 0.066 | 0.001 | - | - | 0.123 | 0.181 | 0.000 | 0.59x | 2.1/6.4/8.7% | 0.7/2.9% | 3 |

> stretch=1.25: decode_failures 15

> stretch=2.0: decode_failures 3

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| clustered | 1 | 0.880 | 0.876 | 0.004 | - | - | 0.948 | 0.956 | 0.000 | 1.24x | 25.2/34.8/35.9% | 1.7/5.8% | 3 |
| corridor | 1 | 0.355 | 0.345 | 0.010 | - | - | 0.512 | 0.514 | 0.033 | 1.27x | 11.7/19.7/23.2% | 2.0/5.3% | 3 |
| hub | 1 | 0.854 | 0.851 | 0.003 | - | - | 0.934 | 0.934 | 0.417 | 1.27x | 22.8/35.1/36.7% | 1.9/5.3% | 3 |

> topology=clustered: misdecodes 1

> topology=clustered: decode_failures 1

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.655 | 0.655 | 0.000 | - | - | 0.871 | 0.899 | 0.194 | 1.54x | 15.9/25.1/28.2% | 2.1/5.8% | 3 |
| True | 1 | 0.650 | 0.650 | 0.000 | - | - | 0.872 | 0.887 | 0.185 | 1.56x | 16.0/25.6/28.5% | 2.2/5.9% | 3 |

> coding-rate-ladder=False: decode_failures 29

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.650 | 0.650 | 0.000 | - | - | 0.872 | 0.887 | 0.185 | 1.56x | 16.0/25.6/28.5% | 2.2/5.9% | 3 |
| m4-early-flood | 1 | 0.645 | 0.645 | 0.000 | - | - | 0.874 | 0.891 | 0.170 | 1.57x | 16.2/25.5/28.6% | 2.2/5.9% | 3 |

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.691 | 0.691 | 0.000 | - | - | 0 | 0.000 | 0.193 | 1.29x | 13.4/20.4/23.0% | 1.8/4.8% | 3 |
| chain | 1 | 0.661 | 0.657 | 0.004 | - | - | 0.806 | 0.891 | 0.195 | 1.51x | 15.6/24.4/26.8% | 2.1/5.6% | 3 |
| sr | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| True | 1 | 0.706 | 0.693 | 0.014 | - | - | 0.905 | 0.907 | 0.206 | 1.34x | 13.8/21.2/23.6% | 1.8/4.8% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.977 | 0.978 | 0.495 | 2.20x | 18.4/32.5/38.0% | 1.4/5.0% | 3 |
| True | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.974 | 0.974 | 0.509 | 2.23x | 18.4/32.2/37.6% | 1.5/5.0% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.076 | 0.074 | 0.002 | - | - | 0.202 | 0.225 | 0.000 | 0.03x | 0.1/0.4/0.5% | 0.0/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.203 | 0.200 | 0.003 | - | - | 0.381 | 0.382 | 0.000 | 0.17x | 1.0/2.0/3.4% | 0.2/0.8% | 3 |
| LONG_TURBO | 1 | 0.569 | 0.557 | 0.012 | - | - | 0.801 | 0.804 | 0.000 | 1.27x | 10.4/19.0/22.5% | 1.8/4.8% | 3 |

> preset=SHORT_TURBO: decode_failures 5

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 0.25 | 1 | 0.720 | 0.702 | 0.018 | - | - | 0.915 | 0.917 | 0.251 | 1.28x | 15.7/22.7/25.2% | 1.7/4.9% | 3 |
| 1.0 | 1 | 0.847 | 0.836 | 0.011 | - | - | 0.954 | 0.954 | 0.559 | 0.98x | 20.0/24.9/27.5% | 1.3/4.8% | 3 |

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.142 | 0.138 | 0.005 | - | - | 0.296 | 0.297 | 0.000 | 0.09x | 0.4/1.0/1.8% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| LITE_FAST | 1 | 0.582 | 0.569 | 0.013 | - | - | 0.833 | 0.836 | 0.049 | 0.99x | 8.7/15.0/18.1% | 1.6/4.0% | 3 |
| NARROW_SLOW | 1 | 0.631 | 0.609 | 0.022 | - | - | 0.888 | 0.889 | 0.148 | 1.29x | 11.4/20.2/23.4% | 2.0/4.9% | 3 |

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| temporal | 1 | 0.542 | 0.513 | 0.029 | - | - | 0.821 | 0.829 | 0.054 | 1.25x | 12.8/19.7/22.6% | 1.9/4.4% | 3 |
| transient | 1 | 0.685 | 0.667 | 0.017 | - | - | 0.900 | 0.901 | 0.201 | 1.34x | 13.9/21.3/23.7% | 1.8/4.9% | 3 |
| periodic | 1 | 0.534 | 0.520 | 0.014 | - | - | 0.715 | 0.743 | 0.097 | 1.18x | 11.9/19.0/21.6% | 1.7/4.0% | 3 |

> noise-profile=temporal: decode_failures 1

> noise-profile=periodic: decode_failures 24

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.142 | 0.138 | 0.005 | - | - | 0.296 | 0.297 | 0.000 | 0.09x | 0.4/1.0/1.8% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| LONG_MODERATE | 1 | 0.707 | 0.689 | 0.017 | - | - | 0.852 | 0.855 | 0.325 | 3.44x | 39.3/56.5/59.9% | 5.0/12.2% | 3 |

> faster: 1.41 s per simulated hour against 2.97 over 40 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.025 | 0.025 | 0.000 | - | - | 0.046 | 0.046 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.076 | 0.074 | 0.002 | - | - | 0.202 | 0.225 | 0.000 | 0.03x | 0.1/0.4/0.5% | 0.0/0.2% | 3 |
| LONG_FAST | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| LONG_TURBO | 1 | 0.569 | 0.557 | 0.012 | - | - | 0.801 | 0.804 | 0.000 | 1.27x | 10.4/19.0/22.5% | 1.8/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.679 | 0.655 | 0.024 | - | - | 0.890 | 0.893 | 0.193 | 1.84x | 16.7/27.5/30.6% | 2.6/6.6% | 3 |

> preset=SHORT_TURBO: decode_failures 5

> preset=EXTRA_LONG_TURBO: misdecodes 1

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.642 | 0.621 | 0.022 | - | - | 0.847 | 0.851 | 0.144 | 1.28x | 13.5/20.8/23.4% | 1.8/4.6% | 3 |
| 10000 | 1 | 0.534 | 0.520 | 0.014 | - | - | 0.715 | 0.743 | 0.097 | 1.18x | 11.9/19.0/21.6% | 1.7/4.0% | 3 |
| 4000 | 1 | 0.300 | 0.297 | 0.003 | - | - | 0.395 | 0.493 | 0.043 | 0.97x | 10.1/16.2/18.6% | 1.5/3.1% | 3 |
| 2000 | 1 | 0.060 | 0.060 | 0.000 | - | - | 0.084 | 0.155 | 0.012 | 0.66x | 6.8/11.7/14.2% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 24

> noise-pulse-interval-ms=4000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.176 | 0.171 | 0.004 | - | - | 0.325 | 0.327 | 0.000 | 1.08x | 5.9/12.7/19.8% | 1.5/4.5% | 3 |
| 1.0 | 1 | 0.536 | 0.530 | 0.006 | - | - | 0.636 | 0.636 | 0.353 | 0.93x | 12.8/17.4/21.0% | 1.4/4.2% | 3 |

> faster: 0.928 s per simulated hour against 1.87 over 40 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 22 | 1 | 0.175 | 0.171 | 0.004 | - | - | 0.304 | 0.323 | 0.000 | 1.09x | 6.0/12.5/19.4% | 1.6/4.5% | 3 |
| 17 | 1 | 0.078 | 0.076 | 0.001 | - | - | 0.208 | 0.224 | 0.000 | 0.65x | 2.6/7.7/10.0% | 0.8/3.2% | 3 |
| 14 | 1 | 0.046 | 0.045 | 0.001 | - | - | 0.092 | 0.125 | 0.000 | 0.45x | 1.1/4.9/6.5% | 0.5/2.2% | 3 |

> tx-power=22: decode_failures 3

> tx-power=17: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.977 | 0.978 | 0.495 | 2.20x | 18.4/32.5/38.0% | 1.4/5.0% | 3 |
| True | 1 | 0.838 | 0.831 | 0.008 | - | - | 0.977 | 0.977 | 0.469 | 2.52x | 20.6/36.0/42.0% | 1.7/5.5% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.707 | 0.695 | 0.012 | - | - | 0.897 | 0.898 | 0.198 | 1.41x | 14.3/23.4/27.0% | 2.0/5.0% | 3 |
| True | 1 | 0.737 | 0.728 | 0.009 | - | - | 0.887 | 0.892 | 0.217 | 1.49x | 14.6/24.4/27.8% | 2.2/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| random | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.888 | 0.892 | 0.223 | 1.33x | 13.8/20.2/23.1% | 1.9/4.8% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.561 | 0.513 | 0.049 | - | - | 0.866 | 0.868 | 0.058 | 1.07x | 11.3/17.8/20.7% | 1.5/4.3% | 3 |
| 7 | 1 | 0.794 | 0.783 | 0.011 | - | - | 0.928 | 0.928 | 0.340 | 1.45x | 14.6/21.4/24.1% | 2.1/4.9% | 3 |
| 15 | 1 | 0.838 | 0.833 | 0.005 | - | - | 0.922 | 0.922 | 0.366 | 1.52x | 15.2/22.1/24.9% | 2.3/5.1% | 3 |
| 32 | 1 | 0.836 | 0.830 | 0.006 | - | - | 0.921 | 0.922 | 0.389 | 1.52x | 15.1/22.1/24.9% | 2.3/5.1% | 3 |

> hop-limit=3: decode_failures 6

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.561 | 0.513 | 0.049 | - | - | 0.866 | 0.868 | 0.058 | 1.07x | 11.3/17.8/20.7% | 1.5/4.3% | 3 |
| 5 | 1 | 0.712 | 0.692 | 0.019 | - | - | 0.909 | 0.911 | 0.191 | 1.31x | 13.7/20.6/22.9% | 1.8/4.7% | 3 |
| 7 | 1 | 0.794 | 0.783 | 0.011 | - | - | 0.928 | 0.928 | 0.340 | 1.45x | 14.6/21.4/24.1% | 2.1/4.9% | 3 |

> hop-limit=3: decode_failures 6

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| KNOWN_ONLY | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.680 | 0.680 | 0.000 | - | - | 0.810 | 0.903 | 0.188 | 1.28x | 13.1/20.2/22.7% | 1.8/4.6% | 3 |

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.561 | 0.513 | 0.049 | - | - | 0.866 | 0.868 | 0.058 | 1.07x | 11.3/17.8/20.7% | 1.5/4.3% | 3 |
| True | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

> hop-spread=False: decode_failures 6

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| BALANCED | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| STRICT | 1 | 0.566 | 0.566 | 0.000 | - | - | 0.778 | 0.780 | 0.143 | 1.39x | 14.4/22.2/24.8% | 1.9/5.0% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| dm | 1 | 0.697 | 0.679 | 0.019 | - | - | 0.907 | 0.908 | 0.202 | 1.29x | 13.4/20.7/23.2% | 1.8/4.8% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.686 | 0.668 | 0.019 | - | - | 0.897 | 0.903 | 0.190 | 1.34x | 13.9/21.4/23.8% | 1.8/4.9% | 3 |
| local | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| time | 1 | 0.698 | 0.681 | 0.017 | - | - | 0.907 | 0.912 | 0.201 | 1.36x | 14.1/21.9/24.3% | 1.9/5.0% | 3 |
| window | 1 | 0.702 | 0.685 | 0.017 | - | - | 0.905 | 0.908 | 0.197 | 1.33x | 13.7/21.1/23.6% | 1.9/4.8% | 3 |

> bucket-mode=global: misdecodes 26

> bucket-mode=time: misdecodes 22

> bucket-mode=window: misdecodes 19

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.676 | 0.656 | 0.019 | - | - | 0.888 | 0.894 | 0.200 | 1.47x | 14.9/23.5/26.0% | 2.0/5.3% | 3 |
| 1800 | 1 | 0.698 | 0.681 | 0.017 | - | - | 0.907 | 0.912 | 0.201 | 1.36x | 14.1/21.9/24.3% | 1.9/5.0% | 3 |
| 3600 | 1 | 0.690 | 0.673 | 0.017 | - | - | 0.903 | 0.910 | 0.205 | 1.34x | 13.9/21.5/24.1% | 1.8/4.9% | 3 |

> time-bucket-s=600: misdecodes 106

> time-bucket-s=1800: misdecodes 22

> time-bucket-s=3600: misdecodes 10

> time-bucket-s=3600: decode_failures 2

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| interval | 1 | 0.663 | 0.639 | 0.024 | - | - | 0.865 | 0.887 | 0.196 | 1.80x | 18.1/29.2/31.9% | 2.5/7.0% | 3 |
| aimd | 1 | 0.684 | 0.676 | 0.008 | - | - | 0.839 | 0.903 | 0.201 | 1.32x | 13.8/21.1/23.6% | 1.8/4.9% | 3 |
| bucket+interval | 1 | 0.660 | 0.631 | 0.029 | - | - | 0.883 | 0.885 | 0.181 | 1.84x | 18.6/29.9/32.8% | 2.6/7.2% | 3 |

> trigger=interval: misdecodes 10

> trigger=interval: decode_failures 2

> trigger=aimd: misdecodes 4

> trigger=aimd: decode_failures 13

> trigger=bucket+interval: misdecodes 18

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.695 | 0.676 | 0.019 | - | - | 0.894 | 0.906 | 0.186 | 1.33x | 13.9/21.2/24.0% | 1.8/4.9% | 3 |
| 8 | 1 | 0.702 | 0.680 | 0.022 | - | - | 0.907 | 0.917 | 0.187 | 1.32x | 13.6/21.3/24.0% | 1.8/5.0% | 3 |
| 16 | 1 | 0.693 | 0.677 | 0.015 | - | - | 0.902 | 0.903 | 0.191 | 1.33x | 13.8/21.2/23.8% | 1.9/4.8% | 3 |
| 32 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 50 | 1 | 0.697 | 0.677 | 0.019 | - | - | 0.914 | 0.917 | 0.201 | 1.35x | 13.9/21.4/23.9% | 1.8/4.9% | 3 |

> capacity=4: decode_failures 98

> capacity=8: decode_failures 98

> capacity=16: decode_failures 7

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.695 | 0.676 | 0.019 | - | - | 0.894 | 0.906 | 0.186 | 1.33x | 13.9/21.2/24.0% | 1.8/4.9% | 3 |
| 8 | 1 | 0.702 | 0.680 | 0.022 | - | - | 0.907 | 0.917 | 0.187 | 1.32x | 13.6/21.3/24.0% | 1.8/5.0% | 3 |
| 16 | 1 | 0.693 | 0.677 | 0.015 | - | - | 0.902 | 0.903 | 0.191 | 1.33x | 13.8/21.2/23.8% | 1.9/4.8% | 3 |
| 32 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 50 | 1 | 0.697 | 0.677 | 0.019 | - | - | 0.914 | 0.917 | 0.201 | 1.35x | 13.9/21.4/23.9% | 1.8/4.9% | 3 |

> capacity=4: decode_failures 98

> capacity=8: decode_failures 98

> capacity=16: decode_failures 7

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.686 | 0.678 | 0.008 | - | - | 0.850 | 0.908 | 0.187 | 1.32x | 13.6/20.9/23.4% | 1.8/4.8% | 3 |
| 16 | 1 | 0.699 | 0.681 | 0.018 | - | - | 0.903 | 0.908 | 0.198 | 1.32x | 13.6/21.1/23.5% | 1.8/4.8% | 3 |
| 32 | 1 | 0.702 | 0.685 | 0.017 | - | - | 0.905 | 0.908 | 0.197 | 1.33x | 13.7/21.1/23.6% | 1.9/4.8% | 3 |

> capacity=8: misdecodes 14

> capacity=8: decode_failures 81

> capacity=16: misdecodes 27

> capacity=16: decode_failures 7

> capacity=32: misdecodes 19

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.660 | 0.631 | 0.029 | - | - | 0.883 | 0.885 | 0.181 | 1.84x | 18.6/29.9/32.8% | 2.6/7.2% | 3 |
| 02-06 | 1 | 0.696 | 0.682 | 0.014 | - | - | 0.874 | 0.918 | 0.186 | 1.35x | 14.0/21.7/24.2% | 1.9/5.0% | 3 |
| 00-08 | 1 | 0.690 | 0.677 | 0.013 | - | - | 0.871 | 0.908 | 0.200 | 1.43x | 14.8/23.1/25.7% | 2.0/5.4% | 3 |

> catch-up-hours=: misdecodes 18

> catch-up-hours=02-06: misdecodes 1

> catch-up-hours=02-06: decode_failures 33

> catch-up-hours=00-08: misdecodes 2

> catch-up-hours=00-08: decode_failures 33

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.680 | 0.677 | 0.003 | - | - | 0.867 | 0.869 | 0.189 | 1.31x | 13.4/20.9/23.4% | 1.8/4.9% | 3 |
| 2 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 3 | 1 | 0.698 | 0.685 | 0.012 | - | - | 0.709 | 0.904 | 0.196 | 1.32x | 13.5/21.1/23.7% | 1.8/4.8% | 3 |
| 4 | 1 | 0.715 | 0.675 | 0.039 | - | - | 0.837 | 0.909 | 0.199 | 1.35x | 13.7/21.3/23.4% | 2.0/5.0% | 3 |

> hops-apart=3: decode_failures 19

> hops-apart=4: decode_failures 36

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.680 | 0.677 | 0.003 | - | - | 0.867 | 0.869 | 0.189 | 1.31x | 13.4/20.9/23.4% | 1.8/4.9% | 3 |
| 2 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 3 | 1 | 0.698 | 0.685 | 0.012 | - | - | 0.709 | 0.904 | 0.196 | 1.32x | 13.5/21.1/23.7% | 1.8/4.8% | 3 |
| 4 | 1 | 0.715 | 0.675 | 0.039 | - | - | 0.837 | 0.909 | 0.199 | 1.35x | 13.7/21.3/23.4% | 2.0/5.0% | 3 |
| 5 | 1 | 0.686 | 0.676 | 0.010 | - | - | 0.562 | 0.907 | 0.199 | 1.31x | 13.5/20.7/23.2% | 1.8/4.8% | 3 |

> hops-apart=3: decode_failures 19

> hops-apart=4: decode_failures 36

> hops-apart=5: decode_failures 13

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.686 | 0.671 | 0.015 | - | - | 0.895 | 0.900 | 0.180 | 1.33x | 13.7/21.3/23.8% | 1.8/4.9% | 3 |
| 30 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 120 | 1 | 0.693 | 0.675 | 0.018 | - | - | 0.909 | 0.910 | 0.202 | 1.36x | 14.0/21.6/24.3% | 1.9/4.9% | 3 |
| 600 | 1 | 0.697 | 0.679 | 0.018 | - | - | 0.905 | 0.907 | 0.193 | 1.34x | 13.8/21.4/23.8% | 1.9/4.9% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.686 | 0.671 | 0.015 | - | - | 0.895 | 0.900 | 0.180 | 1.33x | 13.7/21.3/23.8% | 1.8/4.9% | 3 |
| 30 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 120 | 1 | 0.693 | 0.675 | 0.018 | - | - | 0.909 | 0.910 | 0.202 | 1.36x | 14.0/21.6/24.3% | 1.9/4.9% | 3 |
| 600 | 1 | 0.697 | 0.679 | 0.018 | - | - | 0.905 | 0.907 | 0.193 | 1.34x | 13.8/21.4/23.8% | 1.9/4.9% | 3 |

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.681 | 0.678 | 0.003 | - | - | 0.446 | 0.787 | 0.196 | 1.32x | 13.5/20.8/23.5% | 1.9/4.8% | 3 |
| routers | 1 | 0.695 | 0.690 | 0.005 | - | - | 0.882 | 0.884 | 0.194 | 1.32x | 13.5/21.0/23.5% | 1.8/5.0% | 3 |
| alternate-routers | 1 | 0.687 | 0.685 | 0.003 | - | - | 0.883 | 0.883 | 0.205 | 1.32x | 13.4/21.1/23.5% | 1.8/5.1% | 3 |
| beside-router | 1 | 0.688 | 0.684 | 0.004 | - | - | 0.894 | 0.896 | 0.194 | 1.33x | 13.6/21.3/23.7% | 1.9/4.9% | 3 |
| random-clients | 1 | 0.704 | 0.671 | 0.033 | - | - | 0.874 | 0.883 | 0.191 | 1.35x | 13.9/20.9/24.0% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

> place=spread: decode_failures 4

> place=random-clients: decode_failures 3

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.681 | 0.678 | 0.003 | - | - | 0.446 | 0.787 | 0.196 | 1.32x | 13.5/20.8/23.5% | 1.9/4.8% | 3 |
| routers | 1 | 0.695 | 0.690 | 0.005 | - | - | 0.882 | 0.884 | 0.194 | 1.32x | 13.5/21.0/23.5% | 1.8/5.0% | 3 |
| alternate-routers | 1 | 0.687 | 0.685 | 0.003 | - | - | 0.883 | 0.883 | 0.205 | 1.32x | 13.4/21.1/23.5% | 1.8/5.1% | 3 |
| beside-router | 1 | 0.688 | 0.684 | 0.004 | - | - | 0.894 | 0.896 | 0.194 | 1.33x | 13.6/21.3/23.7% | 1.9/4.9% | 3 |
| random-clients | 1 | 0.704 | 0.671 | 0.033 | - | - | 0.874 | 0.883 | 0.191 | 1.35x | 13.9/20.9/24.0% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

> place=spread: decode_failures 4

> place=random-clients: decode_failures 3

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| broadcast | 1 | 0.738 | 0.660 | 0.078 | - | - | 0.892 | 0.899 | 0.216 | 1.45x | 14.8/23.0/25.5% | 2.0/5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| heard | 1 | 0.698 | 0.684 | 0.014 | - | - | 0.912 | 0.915 | 0.201 | 1.34x | 13.9/21.4/23.9% | 1.9/4.9% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.738 | 0.660 | 0.078 | - | - | 0.892 | 0.899 | 0.216 | 1.45x | 14.8/23.0/25.5% | 2.0/5.3% | 3 |
| heard | 1 | 0.731 | 0.657 | 0.073 | - | - | 0.878 | 0.884 | 0.235 | 1.47x | 15.0/23.3/25.6% | 2.0/5.3% | 3 |

> replay-ordering=heard: misdecodes 6

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| enum | 1 | 0.698 | 0.681 | 0.017 | - | - | 0.900 | 0.911 | 0.205 | 1.34x | 13.9/21.4/24.0% | 1.8/4.9% | 3 |
| hybrid | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.695 | 0.690 | 0.005 | - | - | 0.882 | 0.884 | 0.194 | 1.32x | 13.5/21.0/23.5% | 1.8/5.0% | 3 |
| 6 | 1 | 0.699 | 0.669 | 0.030 | - | - | 0.909 | 0.914 | 0.199 | 1.35x | 14.1/21.6/24.3% | 1.8/5.2% | 6 |

> servers=6: decode_failures 1

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.693 | 0.676 | 0.018 | - | - | 0.892 | 0.898 | 0.203 | 1.32x | 13.6/20.8/23.4% | 1.8/4.8% | 2 |
| 3 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 5 | 1 | 0.689 | 0.672 | 0.017 | - | - | 0.912 | 0.914 | 0.198 | 1.37x | 14.2/22.0/24.4% | 1.9/4.9% | 5 |
| 8 | 1 | 0.690 | 0.668 | 0.021 | - | - | 0.915 | 0.919 | 0.191 | 1.39x | 14.1/22.5/24.6% | 1.9/5.0% | 8 |

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.693 | 0.676 | 0.018 | - | - | 0.892 | 0.898 | 0.203 | 1.32x | 13.6/20.8/23.4% | 1.8/4.8% | 2 |
| 3 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 5 | 1 | 0.689 | 0.672 | 0.017 | - | - | 0.912 | 0.914 | 0.198 | 1.37x | 14.2/22.0/24.4% | 1.9/4.9% | 5 |
| 8 | 1 | 0.690 | 0.668 | 0.021 | - | - | 0.915 | 0.919 | 0.191 | 1.39x | 14.1/22.5/24.6% | 1.9/5.0% | 8 |

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| True | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.701 | 0.684 | 0.017 | - | - | 0.900 | 0.912 | 0.204 | 1.24x | 12.8/19.9/22.2% | 1.7/4.5% | 3 |
| 1 | 1 | 0.704 | 0.688 | 0.016 | - | - | 0.905 | 0.906 | 0.217 | 1.25x | 13.0/19.8/22.3% | 1.7/4.5% | 3 |
| 2 | 1 | 0.699 | 0.686 | 0.013 | - | - | 0.907 | 0.909 | 0.205 | 1.26x | 13.0/20.1/22.6% | 1.7/4.5% | 3 |
| 4 | 1 | 0.700 | 0.689 | 0.011 | - | - | 0.901 | 0.903 | 0.211 | 1.25x | 12.9/19.9/22.3% | 1.7/4.5% | 3 |

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.697 | 0.681 | 0.016 | - | - | 0.906 | 0.908 | 0.209 | 1.32x | 13.6/21.0/23.5% | 1.8/4.8% | 3 |
| 24 | 1 | 0.704 | 0.685 | 0.019 | - | - | 0.919 | 0.922 | 0.195 | 1.34x | 13.9/21.5/24.0% | 1.8/4.9% | 3 |
| 32 | 1 | 0.702 | 0.683 | 0.018 | - | - | 0.912 | 0.914 | 0.195 | 1.35x | 13.9/21.4/24.0% | 1.9/4.9% | 3 |
| 64 | 1 | 0.690 | 0.673 | 0.017 | - | - | 0.900 | 0.903 | 0.193 | 1.35x | 14.0/21.4/23.9% | 1.8/4.9% | 3 |

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.693 | 0.672 | 0.020 | - | - | 0.904 | 0.906 | 0.194 | 1.38x | 14.3/22.1/24.6% | 1.9/5.1% | 3 |
| 16 | 1 | 0.699 | 0.682 | 0.017 | - | - | 0.905 | 0.908 | 0.187 | 1.35x | 14.0/21.8/24.2% | 1.9/5.0% | 3 |
| 32 | 1 | 0.702 | 0.685 | 0.017 | - | - | 0.905 | 0.908 | 0.197 | 1.33x | 13.7/21.1/23.6% | 1.9/4.8% | 3 |

> window-size=8: misdecodes 121

> window-size=16: misdecodes 49

> window-size=32: misdecodes 19

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.977 | 0.978 | 0.495 | 2.20x | 18.4/32.5/38.0% | 1.4/5.0% | 3 |
| True | 1 | 0.619 | 0.603 | 0.016 | - | - | 0.841 | 0.862 | 0.374 | 5.80x | 46.7/68.6/76.3% | 4.1/11.5% | 3 |

> no-congestion-scaling=True: decode_failures 90

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.309 | 0.305 | 0.004 | - | - | 0.481 | 0.481 | 0.070 | 4.61x | 13.1/20.2/24.5% | 1.7/4.1% | 3 |
| truesize | 1 | 0.334 | 0.330 | 0.004 | - | - | 0.499 | 0.499 | 0.087 | 2.56x | 6.8/13.9/17.4% | 0.8/2.9% | 3 |

> faster: 5.19 s per simulated hour against 11.2 over 40 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.854 | 0.848 | 0.006 | - | - | 0.978 | 0.980 | 0.499 | 1.99x | 16.4/29.7/34.7% | 1.3/4.6% | 3 |
| adaptive | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.977 | 0.978 | 0.495 | 2.20x | 18.4/32.5/38.0% | 1.4/5.0% | 3 |

