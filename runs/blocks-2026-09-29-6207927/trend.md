# Sweep blocks-2026-09-29-6207927

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 6207927 · seeds 6207927
- **blocks** 87 run
- **compute** 9.5 h of simulator time across every cell
- **generated** 2026-09-29T10:00:12+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>75 warnings</summary>

- AD-amplifiers: amplifier-mix=sprinkled: misdecodes 1
- AD-amplify-worst: amplify-worst=0.1: decode_failures 7
- AD-siting: siting-mix=local-typical: decode_failures 4
- AD-siting: siting-mix=basement-heavy: decode_failures 3
- BL-control: protocol=sr: decode_failures 26
- BL-control: slower: 4.85 s per simulated hour against 1.84 over 39 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 28
- DB-hotstore-stress: max-num-nodes=120: decode_failures 55
- DB-hotstore-stress: max-num-nodes=250: decode_failures 56
- DB-warm: warm-num-nodes=0: decode_failures 81
- DB-warm: warm-num-nodes=25: decode_failures 81
- DB-warm: warm-num-nodes=100: decode_failures 81
- DB-warm: warm-num-nodes=2000: decode_failures 81
- DG-burst: burst-loss=0.2: decode_failures 2
- DG-burst: burst-loss=0.3: decode_failures 27
- DG-outage: burst-loss=0.1: decode_failures 13
- DG-outage: burst-loss=0.2: decode_failures 38
- DG-outage: burst-loss=0.3: decode_failures 15
- DM-mode: faster: 1.21 s per simulated hour against 3.31 over 39 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- LD-chatty-hops: faster: 1.78 s per simulated hour against 4.32 over 39 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- LD-chatty: broadcast-interval-s=300: decode_failures 1
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 81
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 86
- MS-density: nodes=40: decode_failures 7
- MS-hopscale: nodes=250: decode_failures 107
- MS-hopscale: nodes=500: decode_failures 70
- MS-oversubscribed: nodes=250: decode_failures 55
- MS-oversubscribed: nodes=500: decode_failures 69
- MS-siting: siting-mix=local-typical: decode_failures 5
- MS-size: nodes=40: decode_failures 16
- MS-stretch: stretch=2.0: decode_failures 4
- RF-bw500: faster: 0.906 s per simulated hour against 1.82 over 39 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-eu-presets: faster: 0.724 s per simulated hour against 2 over 39 prior run(s) - 2.8x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=17: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 27
- SF-bucket-mode: bucket-mode=time: misdecodes 43
- SF-bucket-mode: bucket-mode=window: misdecodes 31
- SF-bucket-time: time-bucket-s=600: misdecodes 129
- SF-bucket-time: time-bucket-s=1800: misdecodes 43
- SF-bucket-time: time-bucket-s=3600: misdecodes 17
- SF-cadence: trigger=interval: misdecodes 14
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 12
- SF-cadence: trigger=bucket+interval: misdecodes 24
- SF-capacity-local: capacity=4: decode_failures 86
- SF-capacity-local: capacity=8: decode_failures 30
- SF-capacity: capacity=4: decode_failures 86
- SF-capacity: capacity=8: decode_failures 30
- SF-capacity-window: capacity=8: misdecodes 23
- SF-capacity-window: capacity=8: decode_failures 22
- SF-capacity-window: capacity=16: misdecodes 26
- SF-capacity-window: capacity=32: misdecodes 31
- SF-catchup: catch-up-hours=: misdecodes 24
- SF-catchup: catch-up-hours=02-06: decode_failures 25
- SF-catchup: catch-up-hours=00-08: decode_failures 22
- SF-hops-flat: hops-apart=3: decode_failures 26
- SF-hops-flat: hops-apart=4: decode_failures 29
- SF-hops-spread: hops-apart=3: decode_failures 26
- SF-hops-spread: hops-apart=4: decode_failures 29
- SF-hops-spread: hops-apart=5: decode_failures 26
- SF-place-flat: place=spread: decode_failures 19
- SF-place-flat: place=random-clients: decode_failures 25
- SF-place-spread: place=spread: decode_failures 19
- SF-place-spread: place=random-clients: decode_failures 25
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 22
- SF-replay-order: replay-ordering=heard: misdecodes 9
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-width: short-id-bits=24: misdecodes 1
- SF-window-size: window-size=8: misdecodes 94
- SF-window-size: window-size=16: misdecodes 49
- SF-window-size: window-size=32: misdecodes 31
- TH-congestion-input: congestion-input=hotstore: decode_failures 55
- TH-congestion-input: congestion-input=truesize: decode_failures 85
- TH-congestion-input: slower: 35.3 s per simulated hour against 11.2 over 39 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: decode_failures 75

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 35.3 | 11.2 | 3.16x | 39 |
| `BL-control` | 4.85 | 1.84 | 2.64x | 39 |
| `AD-amplify-worst` | 2.84 | 1.83 | 1.55x | 39 |
| `MS-topology` | 1.3 | 1.97 | 0.66x | 39 |
| `RT-hopassign` | 1.25 | 1.88 | 0.66x | 39 |
| `SF-replay-order` | 1.1 | 1.69 | 0.65x | 39 |
| `RT-favourites` | 1.04 | 1.67 | 0.62x | 39 |
| `SF-cadence` | 2.2 | 3.63 | 0.61x | 39 |
| `AD-nomute` | 1.46 | 2.41 | 0.60x | 39 |
| `SF-signed` | 1.02 | 1.74 | 0.58x | 39 |
| `AD-flooding` | 1.5 | 2.57 | 0.58x | 39 |
| `RF-pulse` | 1 | 1.72 | 0.58x | 39 |
| `FW-versions` | 0.923 | 1.62 | 0.57x | 39 |
| `MS-roles` | 1.04 | 1.82 | 0.57x | 39 |
| `RF-stretch-duct` | 1.07 | 1.9 | 0.56x | 39 |
| `PR-dmmode-cr` | 1.61 | 2.94 | 0.55x | 39 |
| `LD-chatty` | 2.8 | 5.14 | 0.55x | 39 |
| `SF-catchup` | 5.13 | 9.48 | 0.54x | 39 |
| `DG-outage` | 3.75 | 6.97 | 0.54x | 39 |
| `AD-badrouters` | 1.15 | 2.17 | 0.53x | 39 |
| `DG-loss` | 1.2 | 2.28 | 0.53x | 39 |
| `RF-txpower` | 0.828 | 1.61 | 0.51x | 39 |
| `LD-traceroute` | 1.07 | 2.1 | 0.51x | 39 |
| `RT-hopspread` | 1.03 | 2.05 | 0.50x | 39 |
| `RF-preset` | 1.49 | 2.98 | 0.50x | 39 |
| `RF-bw500` | 0.906 | 1.82 | 0.50x | 39 |
| `LD-chatty-hops` | 1.78 | 4.32 | 0.41x | 39 |
| `DM-mode` | 1.21 | 3.31 | 0.37x | 39 |
| `RF-eu-presets` | 0.724 | 2 | 0.36x | 39 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.883 | 0.883 | 0.695 → 0.716 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.014 → 0.883 | 0.869 | 0.042 → 0.716 | 2.3e+02x sr_bytes | down | 4 |
| `BL-control` | protocol | **held** | 0 → 0.847 | 0.847 | 0.705 → 0.712 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.038 → 0.883 | 0.845 | 0.031 → 0.716 | 48x advert_bytes | up | 5 |
| `MS-siting` | siting-mix | **text** | 0.198 → 0.965 | 0.767 | 0.192 → 0.963 | 3.1x sr_airtime | up | 4 |
| `AD-siting` | siting-mix | **held** | 0.112 → 0.868 | 0.756 | 0.028 → 0.704 | 8.7x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **held** | 0.149 → 0.883 | 0.734 | 0.078 → 0.716 | 6.3x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.080 → 0.814 | 0.734 | 0.073 → 0.665 | 1.2e+02x sr_airtime | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.244 → 0.883 | 0.639 | 0.172 → 0.716 | 4x advert_bytes | up | 4 |
| `RF-preset` | preset | **held** | 0.244 → 0.883 | 0.639 | 0.172 → 0.718 | 5.6x sr_airtime | up | 3 |
| `RF-bw500` | preset | **held** | 0.239 → 0.765 | 0.525 | 0.106 → 0.564 | 3.7x sr_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.199 → 0.724 | 0.525 | 0.196 → 0.716 | 8.7x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.389 → 0.906 | 0.517 | 0.386 → 0.904 | 4.2x sr_airtime | up | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.380 → 0.852 | 0.472 | 0.198 → 0.567 | 4x bytes_on_air | down | 3 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.527 → 0.925 | 0.398 | 0.385 → 0.767 | 8.7x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.192 → 0.562 | 0.370 | 0.190 → 0.557 | 3.6x sr_airtime | up | 2 |
| `MS-density` | nodes | **text** | 0.545 → 0.903 | 0.358 | 0.527 → 0.896 | 5.3x sr_airtime | up | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.506 → 0.843 | 0.337 | 0.494 → 0.841 | 7.7x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.528 → 0.864 | 0.336 | 0.506 → 0.863 | 2.2x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.390 → 0.724 | 0.334 | 0.374 → 0.716 | 2.1x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.427 → 0.724 | 0.296 | 0.399 → 0.716 | 2.2x sr_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.528 → 0.800 | 0.272 | 0.506 → 0.796 | 1.8x sr_bytes | up | 3 |
| `MS-size` | nodes | **held** | 0.629 → 0.901 | 0.272 | 0.520 → 0.716 | 3.5x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.640 → 0.866 | 0.226 | 0.616 → 0.854 | 4.1x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.765 → 0.988 | 0.223 | 0.716 → 0.918 | 2x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.683 → 0.883 | 0.200 | 0.538 → 0.716 | 1.5x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.528 → 0.724 | 0.196 | 0.506 → 0.716 | 1.5x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **held** | 0.694 → 0.883 | 0.189 | 0.548 → 0.716 | 1.3x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.697 → 0.883 | 0.186 | 0.705 → 0.716 | 4.8x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.697 → 0.883 | 0.186 | 0.705 → 0.716 | 4.8x sr_bytes | up | 6 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.291 → 0.476 | 0.185 | 0.213 → 0.316 | 4.9x sr_airtime | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.724 → 0.904 | 0.180 | 0.716 → 0.901 | 1.4x sr_airtime | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.552 → 0.724 | 0.172 | 0.538 → 0.716 | 1.5x sr_bytes | down | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.653 → 0.808 | 0.155 | 0.642 → 0.803 | 5.8x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.691 → 0.844 | 0.153 | 0.603 → 0.750 | 2.2x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **held** | 0.701 → 0.844 | 0.143 | 0.610 → 0.750 | 2.2x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.721 → 0.850 | 0.129 | 0.711 → 0.843 | 1.2x bytes_on_air | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.786 → 0.883 | 0.097 | 0.624 → 0.716 | 1.5x sr_airtime | down | 4 |
| `FW-versions` | profile | **text** | 0.724 → 0.819 | 0.095 | 0.716 → 0.809 | 3.5x bytes_on_air | down | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.795 → 0.883 | 0.088 | 0.712 → 0.717 | 1.9x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.795 → 0.883 | 0.088 | 0.703 → 0.717 | 2.1x sr_bytes | up | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.745 → 0.823 | 0.078 | 0.548 → 0.606 | 1.5x sr_airtime | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.476 → 0.553 | 0.077 | 0.310 → 0.349 | 2.6x sr_airtime | up | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.856 → 0.932 | 0.076 | 0.739 → 0.793 | 1.2x sr_bytes | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.707 → 0.781 | 0.074 | 0.704 → 0.773 | 2.1x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.707 → 0.781 | 0.074 | 0.704 → 0.773 | 2.1x bytes_on_air | up | 3 |
| `FW-firmware` | profile | **text** | 0.724 → 0.796 | 0.072 | 0.716 → 0.780 | 3.4x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.721 → 0.792 | 0.072 | 0.713 → 0.787 | 2.1x bytes_on_air | up | 4 |
| `AD-badrouters` | role-placement | **text** | 0.636 → 0.707 | 0.071 | 0.626 → 0.704 | 2x sr_bytes | down | 3 |
| `SF-cadence` | trigger | **held** | 0.813 → 0.883 | 0.070 | 0.664 → 0.716 | 15x advert_bytes | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.724 → 0.791 | 0.068 | 0.716 → 0.787 | 3.2x bytes_on_air | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.817 → 0.883 | 0.066 | 0.716 → 0.716 | 25x sr_airtime | down | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.719 → 0.781 | 0.063 | 0.710 → 0.773 | 2.1x bytes_on_air | up | 4 |
| `MS-roles` | role-mix | **held** | 0.868 → 0.921 | 0.053 | 0.704 → 0.752 | 1.2x sr_bytes | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.850 → 0.895 | 0.046 | 0.694 → 0.716 | 8.7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.850 → 0.895 | 0.046 | 0.694 → 0.716 | 8.7x sr_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.841 → 0.883 | 0.042 | 0.707 → 0.718 | 1.3x bytes_on_air | down | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.676 → 0.712 | 0.036 | 0.664 → 0.708 | 9.2x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.850 → 0.883 | 0.033 | 0.705 → 0.716 | 3x advert_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.849 → 0.882 | 0.033 | 0.693 → 0.712 | 1.2x sr_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.856 → 0.885 | 0.030 | 0.699 → 0.720 | 4.5x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **held** | 0.847 → 0.876 | 0.029 | 0.727 → 0.747 | 1.1x bytes_on_air | down | 2 |
| `AD-worst` | role-placement | **text** | 0.602 → 0.630 | 0.029 | 0.582 → 0.618 | 1.2x sr_bytes | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.859 → 0.885 | 0.026 | 0.703 → 0.720 | 2.8x advert_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.859 → 0.885 | 0.026 | 0.707 → 0.720 | 2.4x advert_bytes | up | 3 |
| `SF-capacity` | capacity | **held** | 0.858 → 0.883 | 0.025 | 0.704 → 0.716 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.858 → 0.883 | 0.025 | 0.704 → 0.716 | 5.3x advert_bytes | down | 5 |
| `SF-provide-transport` | provide-transport | **held** | 0.863 → 0.883 | 0.020 | 0.705 → 0.716 | 2.6x sr_airtime | down | 2 |
| `DM-mode` | dm-mode | **held** | 0.830 → 0.848 | 0.018 | 0.666 → 0.676 | 1.2x sr_airtime | down | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.830 → 0.848 | 0.018 | 0.674 → 0.676 | 1.1x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.865 → 0.883 | 0.018 | 0.711 → 0.716 | 2.5x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.703 → 0.720 | 0.017 | 0.694 → 0.716 | 2.8x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.850 → 0.866 | 0.016 | 0.836 → 0.854 | 1.1x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.868 → 0.883 | 0.014 | 0.703 → 0.716 | 1x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.724 → 0.737 | 0.013 | 0.716 → 0.730 | 1.2x sr_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.870 → 0.883 | 0.013 | 0.710 → 0.716 | 5.9x advert_bytes | = | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.870 → 0.883 | 0.013 | 0.716 → 0.719 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.870 → 0.883 | 0.013 | 0.716 → 0.719 | 1.1x sr_airtime | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.716 → 0.724 | 0.008 | 0.706 → 0.716 | 1.2x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.875 → 0.883 | 0.008 | 0.712 → 0.716 | 1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.974 → 0.981 | 0.007 | 0.854 → 0.856 | 1x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.674 → 0.679 | 0.005 | 0.674 → 0.679 | 1.1x sr_airtime | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.710 → 0.715 | 0.005 | 0.701 → 0.706 | 5.2x advert_bytes | up | 3 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.866 → 0.870 | 0.003 | 0.854 → 0.859 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.863 → 0.864 | 0.001 | 0.705 → 0.705 | 1.1x sr_bytes | up | 2 |

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
| none | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| sprinkled | 1 | 0.876 | 0.870 | 0.005 | - | - | 0.930 | 0.930 | 0.646 | 1.20x | 16.9/22.1/25.3% | 1.7/5.0% | 3 |
| arms-race | 1 | 0.904 | 0.901 | 0.002 | - | - | 0.946 | 0.946 | 0.573 | 1.02x | 18.8/23.3/27.0% | 1.4/5.1% | 3 |

> amplifier-mix=sprinkled: misdecodes 1

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.818 | 0.801 | 0.016 | - | - | 0.765 | 0.770 | 0.518 | 1.25x | 15.1/22.0/26.2% | 2.0/4.9% | 3 |
| 0.3 | 1 | 0.925 | 0.918 | 0.007 | - | - | 0.988 | 0.991 | 0.753 | 1.13x | 20.6/25.2/29.0% | 1.7/4.6% | 3 |

> amplify-worst=0.1: decode_failures 7

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.707 | 0.704 | 0.003 | - | - | 0.868 | 0.869 | 0.309 | 1.20x | 12.4/25.0/27.7% | 1.9/5.1% | 3 |
| inverse | 1 | 0.636 | 0.626 | 0.011 | - | - | 0.844 | 0.846 | 0.255 | 1.11x | 11.5/18.1/21.1% | 2.0/3.4% | 3 |
| random | 1 | 0.672 | 0.658 | 0.014 | - | - | 0.870 | 0.871 | 0.000 | 1.08x | 12.0/17.9/21.5% | 1.9/4.4% | 3 |

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.707 | 0.704 | 0.003 | - | - | 0.868 | 0.869 | 0.309 | 1.20x | 12.4/25.0/27.7% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.781 | 0.773 | 0.007 | - | - | 0.874 | 0.875 | 0.313 | 2.50x | 24.6/37.9/42.2% | 4.1/5.0% | 3 |

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.707 | 0.704 | 0.003 | - | - | 0.868 | 0.869 | 0.309 | 1.20x | 12.4/25.0/27.7% | 1.9/5.1% | 3 |
| no-mute | 1 | 0.753 | 0.747 | 0.006 | - | - | 0.926 | 0.927 | 0.326 | 1.36x | 13.8/22.1/27.0% | 2.2/5.1% | 3 |
| all-routers | 1 | 0.781 | 0.773 | 0.007 | - | - | 0.874 | 0.875 | 0.313 | 2.50x | 24.6/37.9/42.2% | 4.1/5.0% | 3 |

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.707 | 0.704 | 0.003 | - | - | 0.868 | 0.869 | 0.309 | 1.20x | 12.4/25.0/27.7% | 1.9/5.1% | 3 |
| local-typical | 1 | 0.561 | 0.548 | 0.012 | - | - | 0.703 | 0.722 | 0.000 | 1.31x | 10.9/21.0/26.5% | 2.2/5.1% | 3 |
| basement-heavy | 1 | 0.028 | 0.028 | 0.000 | - | - | 0.112 | 0.190 | 0.000 | 0.32x | 0.2/3.1/6.7% | 0.2/2.4% | 3 |

> siting-mix=local-typical: decode_failures 4

> siting-mix=basement-heavy: decode_failures 3

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.630 | 0.618 | 0.012 | - | - | 0.843 | 0.843 | 0.000 | 2.24x | 12.4/23.3/30.8% | 1.8/5.2% | 3 |
| inverse | 1 | 0.602 | 0.582 | 0.019 | - | - | 0.844 | 0.847 | 0.000 | 2.18x | 10.8/21.0/29.6% | 1.8/3.1% | 3 |

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.705 | 0.705 | 0.000 | - | - | 0 | 0.000 | 0.218 | 1.32x | 14.1/23.0/28.2% | 2.0/5.0% | 3 |
| sr | 1 | 0.738 | 0.712 | 0.026 | - | - | 0.847 | 0.954 | 0.232 | 1.36x | 14.5/23.7/29.2% | 2.1/5.1% | 3 |

> protocol=sr: decode_failures 26

> slower: 4.85 s per simulated hour against 1.84 over 39 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.621 | 0.610 | 0.010 | - | - | 0.701 | 0.702 | 0.235 | 3.02x | 31.5/53.3/59.3% | 4.6/8.9% | 3 |
| 100 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.844 | 0.845 | 0.315 | 1.66x | 17.2/31.0/34.3% | 2.5/5.0% | 3 |
| 120 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.844 | 0.845 | 0.315 | 1.66x | 17.2/31.0/34.3% | 2.5/5.0% | 3 |
| 250 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.844 | 0.845 | 0.315 | 1.66x | 17.2/31.0/34.3% | 2.5/5.0% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.216 | 0.213 | 0.003 | - | - | 0.291 | 0.426 | 0.048 | 10.44x | 27.4/47.2/56.9% | 3.6/9.7% | 3 |
| 120 | 1 | 0.317 | 0.310 | 0.006 | - | - | 0.476 | 0.596 | 0.056 | 4.93x | 13.3/22.8/30.2% | 1.7/5.5% | 3 |
| 250 | 1 | 0.322 | 0.316 | 0.006 | - | - | 0.474 | 0.597 | 0.054 | 4.88x | 13.0/22.4/29.2% | 1.7/5.2% | 3 |

> max-num-nodes=10: decode_failures 28

> max-num-nodes=120: decode_failures 55

> max-num-nodes=250: decode_failures 56

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.844 | 0.845 | 0.315 | 1.66x | 17.2/31.0/34.3% | 2.5/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.844 | 0.845 | 0.315 | 1.66x | 17.2/31.0/34.3% | 2.5/5.0% | 3 |
| constrained | 1 | 0.614 | 0.603 | 0.012 | - | - | 0.691 | 0.691 | 0.228 | 3.01x | 31.3/53.3/59.1% | 4.6/8.8% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.630 | 0.606 | 0.025 | - | - | 0.823 | 0.878 | 0.300 | 5.53x | 43.3/70.0/76.2% | 3.9/12.0% | 3 |
| 25 | 1 | 0.630 | 0.606 | 0.025 | - | - | 0.823 | 0.878 | 0.300 | 5.53x | 43.3/70.0/76.2% | 3.9/12.0% | 3 |
| 100 | 1 | 0.630 | 0.606 | 0.025 | - | - | 0.823 | 0.878 | 0.300 | 5.53x | 43.3/70.0/76.2% | 3.9/12.0% | 3 |
| 2000 | 1 | 0.630 | 0.606 | 0.025 | - | - | 0.823 | 0.878 | 0.300 | 5.53x | 43.3/70.0/76.2% | 3.9/12.0% | 3 |

> warm-num-nodes=0: decode_failures 81

> warm-num-nodes=25: decode_failures 81

> warm-num-nodes=100: decode_failures 81

> warm-num-nodes=2000: decode_failures 81

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.625 | 0.608 | 0.017 | - | - | 0.833 | 0.836 | 0.158 | 1.24x | 12.9/22.0/27.6% | 1.9/4.8% | 3 |
| 0.2 | 1 | 0.508 | 0.486 | 0.022 | - | - | 0.738 | 0.756 | 0.083 | 1.12x | 12.0/20.0/25.6% | 1.7/4.1% | 3 |
| 0.3 | 1 | 0.427 | 0.399 | 0.029 | - | - | 0.668 | 0.702 | 0.056 | 1.02x | 11.1/18.8/24.2% | 1.5/3.7% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 27

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.674 | 0.662 | 0.012 | - | - | 0.845 | 0.845 | 0.156 | 1.34x | 14.3/23.1/29.0% | 2.1/4.9% | 3 |
| 0.2 | 1 | 0.612 | 0.602 | 0.010 | - | - | 0.786 | 0.788 | 0.116 | 1.34x | 14.2/23.5/29.6% | 2.0/4.7% | 3 |
| 0.3 | 1 | 0.552 | 0.538 | 0.014 | - | - | 0.742 | 0.746 | 0.057 | 1.31x | 14.3/24.0/29.6% | 2.0/4.5% | 3 |

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.607 | 0.593 | 0.014 | - | - | 0.815 | 0.833 | 0.142 | 1.24x | 13.3/21.9/27.4% | 1.9/5.0% | 3 |
| 0.2 | 1 | 0.498 | 0.481 | 0.017 | - | - | 0.694 | 0.752 | 0.067 | 1.14x | 12.4/20.5/26.1% | 1.7/4.3% | 3 |
| 0.3 | 1 | 0.390 | 0.374 | 0.016 | - | - | 0.567 | 0.664 | 0.040 | 1.05x | 11.6/19.1/24.6% | 1.6/3.8% | 3 |

> burst-loss=0.1: decode_failures 13

> burst-loss=0.2: decode_failures 38

> burst-loss=0.3: decode_failures 15

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.669 | 0.669 | 0.000 | - | - | 0.841 | 0.843 | 0.210 | 1.70x | 17.3/29.4/36.0% | 2.5/6.7% | 3 |
| directed-with-late-flood | 1 | 0.676 | 0.676 | 0.000 | - | - | 0.848 | 0.850 | 0.218 | 1.57x | 16.2/27.3/33.8% | 2.4/6.3% | 3 |
| m4-early-flood | 1 | 0.666 | 0.666 | 0.000 | - | - | 0.830 | 0.830 | 0.211 | 1.55x | 15.9/27.2/33.5% | 2.3/6.2% | 3 |

> faster: 1.21 s per simulated hour against 3.31 over 39 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.796 | 0.780 | 0.016 | - | - | 0.944 | 0.945 | 0.487 | 0.71x | 7.4/10.9/12.6% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.721 | 0.713 | 0.008 | - | - | 0.882 | 0.882 | 0.481 | 1.12x | 12.2/18.8/21.5% | 1.8/4.6% | 3 |
| 0.5 | 1 | 0.792 | 0.787 | 0.006 | - | - | 0.909 | 0.910 | 0.319 | 1.03x | 10.3/17.7/21.4% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.783 | 0.766 | 0.018 | - | - | 0.939 | 0.941 | 0.055 | 0.94x | 9.5/14.7/17.1% | 1.6/2.9% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.719 | 0.710 | 0.009 | - | - | 0.886 | 0.887 | 0.460 | 1.13x | 12.1/18.9/21.3% | 1.7/4.6% | 3 |
| 0.5 | 1 | 0.781 | 0.773 | 0.008 | - | - | 0.893 | 0.895 | 0.327 | 1.00x | 10.1/16.9/20.7% | 1.6/3.8% | 3 |
| 0.75 | 1 | 0.766 | 0.753 | 0.012 | - | - | 0.926 | 0.926 | 0.083 | 0.93x | 9.6/14.8/17.5% | 1.5/2.9% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.791 | 0.787 | 0.004 | - | - | 0.935 | 0.936 | 0.257 | 0.76x | 8.2/13.7/17.2% | 1.1/3.0% | 3 |
| signing=true | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.792 | 0.780 | 0.012 | - | - | 0.929 | 0.930 | 0.482 | 0.71x | 7.7/11.4/13.4% | 1.2/2.0% | 3 |
| 2.5 | 1 | 0.793 | 0.779 | 0.013 | - | - | 0.930 | 0.932 | 0.487 | 0.73x | 7.8/11.6/13.6% | 1.2/2.1% | 3 |
| 2.6 | 1 | 0.778 | 0.766 | 0.012 | - | - | 0.918 | 0.919 | 0.452 | 0.70x | 7.6/11.4/13.5% | 1.2/2.0% | 3 |
| 2.7 | 1 | 0.819 | 0.809 | 0.010 | - | - | 0.931 | 0.935 | 0.488 | 0.74x | 7.8/13.7/15.7% | 1.1/2.8% | 3 |
| 2.8 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.773 | 0.767 | 0.007 | - | - | 0.925 | 0.926 | 0.248 | 0.92x | 9.6/15.8/19.5% | 1.4/3.6% | 3 |
| 900 | 1 | 0.653 | 0.642 | 0.011 | - | - | 0.799 | 0.802 | 0.222 | 2.06x | 21.1/35.3/43.2% | 3.2/7.8% | 3 |
| 300 | 1 | 0.402 | 0.385 | 0.017 | - | - | 0.527 | 0.529 | 0.119 | 4.34x | 42.2/65.2/74.6% | 7.0/15.3% | 3 |

> broadcast-interval-s=300: decode_failures 1

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.843 | 0.841 | 0.002 | - | - | 0.953 | 0.954 | 0.434 | 1.02x | 10.7/16.0/19.9% | 1.5/3.5% | 3 |
| 900 | 1 | 0.753 | 0.747 | 0.006 | - | - | 0.882 | 0.883 | 0.398 | 2.37x | 24.3/37.3/45.2% | 3.6/8.0% | 3 |
| 300 | 1 | 0.506 | 0.494 | 0.012 | - | - | 0.659 | 0.661 | 0.326 | 4.88x | 46.9/68.4/76.0% | 7.7/15.5% | 3 |

> faster: 1.78 s per simulated hour against 4.32 over 39 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.737 | 0.730 | 0.008 | - | - | 0.890 | 0.890 | 0.222 | 1.25x | 12.9/21.9/27.1% | 1.9/4.9% | 3 |
| sinusoid | 1 | 0.734 | 0.726 | 0.008 | - | - | 0.895 | 0.895 | 0.237 | 1.24x | 12.9/21.6/26.6% | 1.9/4.8% | 3 |
| commuter | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.653 | 0.642 | 0.011 | - | - | 0.799 | 0.802 | 0.222 | 2.06x | 21.1/35.3/43.2% | 3.2/7.8% | 3 |
| 3600 | 1 | 0.773 | 0.767 | 0.007 | - | - | 0.925 | 0.926 | 0.248 | 0.92x | 9.6/15.8/19.5% | 1.4/3.6% | 3 |
| 10800 | 1 | 0.783 | 0.777 | 0.005 | - | - | 0.931 | 0.931 | 0.269 | 0.60x | 6.2/10.4/12.8% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.808 | 0.803 | 0.005 | - | - | 0.950 | 0.950 | 0.282 | 0.41x | 4.2/7.0/8.7% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.710 | 0.700 | 0.009 | - | - | 0.860 | 0.860 | 0.215 | 1.41x | 14.7/24.5/30.3% | 2.1/5.4% | 3 |
| 1.0 | 1 | 0.692 | 0.683 | 0.009 | - | - | 0.843 | 0.844 | 0.234 | 1.52x | 15.7/26.4/32.7% | 2.3/5.9% | 3 |
| 4.0 | 1 | 0.637 | 0.624 | 0.012 | - | - | 0.786 | 0.788 | 0.200 | 1.86x | 19.4/32.8/40.8% | 2.8/7.5% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.630 | 0.606 | 0.025 | - | - | 0.823 | 0.878 | 0.300 | 5.53x | 43.3/70.0/76.2% | 3.9/12.0% | 3 |
| 1.0 | 1 | 0.569 | 0.548 | 0.021 | - | - | 0.745 | 0.828 | 0.268 | 6.20x | 47.9/73.2/78.7% | 4.4/13.6% | 3 |

> traceroute-per-hour=0.0: decode_failures 81

> traceroute-per-hour=1.0: decode_failures 86

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.545 | 0.527 | 0.018 | - | - | 0.694 | 0.723 | 0.219 | 1.20x | 13.6/19.5/22.1% | 2.8/5.9% | 3 |
| 60 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 90 | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.980 | 0.982 | 0.312 | 1.76x | 17.2/28.1/33.0% | 1.7/5.6% | 3 |
| 120 | 1 | 0.866 | 0.854 | 0.012 | - | - | 0.981 | 0.981 | 0.468 | 2.12x | 16.9/32.3/36.9% | 1.4/5.2% | 3 |
| 150 | 1 | 0.903 | 0.896 | 0.007 | - | - | 0.982 | 0.982 | 0.599 | 2.62x | 21.1/41.4/47.6% | 1.4/5.6% | 3 |

> nodes=40: decode_failures 7

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 120 | 1 | 0.577 | 0.567 | 0.010 | - | - | 0.876 | 0.878 | 0.000 | 2.29x | 11.5/23.7/27.9% | 1.6/5.5% | 3 |
| 250 | 1 | 0.316 | 0.309 | 0.006 | - | - | 0.480 | 0.594 | 0.060 | 5.21x | 13.8/24.1/31.5% | 1.8/5.8% | 3 |
| 500 | 1 | 0.199 | 0.196 | 0.003 | - | - | 0.379 | 0.386 | 0.026 | 9.47x | 13.1/20.5/30.9% | 1.7/5.5% | 3 |

> nodes=250: decode_failures 107

> nodes=500: decode_failures 70

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.577 | 0.567 | 0.010 | - | - | 0.852 | 0.855 | 0.000 | 2.20x | 10.7/22.7/26.6% | 1.6/5.3% | 3 |
| 250 | 1 | 0.317 | 0.310 | 0.006 | - | - | 0.476 | 0.596 | 0.056 | 4.93x | 13.3/22.8/30.2% | 1.7/5.5% | 3 |
| 500 | 1 | 0.201 | 0.198 | 0.003 | - | - | 0.380 | 0.391 | 0.025 | 8.78x | 12.2/19.0/28.6% | 1.5/5.0% | 3 |

> nodes=250: decode_failures 55

> nodes=500: decode_failures 69

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.756 | 0.752 | 0.004 | - | - | 0.921 | 0.922 | 0.311 | 1.38x | 13.8/23.8/29.4% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.707 | 0.704 | 0.003 | - | - | 0.868 | 0.869 | 0.309 | 1.20x | 12.4/25.0/27.7% | 1.9/5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.797 | 0.793 | 0.003 | - | - | 0.932 | 0.932 | 0.355 | 1.45x | 14.6/24.0/29.4% | 2.2/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.741 | 0.739 | 0.002 | - | - | 0.856 | 0.856 | 0.333 | 1.40x | 14.5/27.7/31.6% | 2.5/5.0% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.05 | 1 | 0.726 | 0.718 | 0.007 | - | - | 0.856 | 0.857 | 0.242 | 1.49x | 15.3/27.6/33.7% | 2.3/5.1% | 3 |
| 0.1 | 1 | 0.714 | 0.707 | 0.008 | - | - | 0.844 | 0.844 | 0.219 | 1.58x | 16.1/32.7/36.7% | 2.3/5.0% | 3 |
| 0.2 | 1 | 0.722 | 0.712 | 0.010 | - | - | 0.841 | 0.842 | 0.225 | 1.76x | 18.0/37.3/42.0% | 2.5/4.9% | 3 |

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| local-typical | 1 | 0.610 | 0.595 | 0.015 | - | - | 0.738 | 0.759 | 0.000 | 1.48x | 12.5/20.5/25.8% | 2.2/5.1% | 3 |
| event | 1 | 0.198 | 0.192 | 0.006 | - | - | 0.448 | 0.448 | 0.000 | 1.15x | 5.6/14.1/22.7% | 1.5/5.4% | 3 |
| backbone | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.996 | 0.996 | 0.849 | 1.15x | 24.7/32.8/35.4% | 1.4/5.3% | 3 |

> siting-mix=local-typical: decode_failures 5

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.728 | 0.715 | 0.013 | - | - | 0.827 | 0.874 | 0.324 | 1.37x | 20.7/30.5/34.6% | 3.2/7.2% | 3 |
| 60 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 90 | 1 | 0.671 | 0.663 | 0.007 | - | - | 0.901 | 0.902 | 0.108 | 1.76x | 12.1/23.3/30.0% | 1.7/5.3% | 3 |
| 120 | 1 | 0.577 | 0.567 | 0.010 | - | - | 0.876 | 0.878 | 0.000 | 2.29x | 11.5/23.7/27.9% | 1.6/5.5% | 3 |
| 150 | 1 | 0.530 | 0.520 | 0.010 | - | - | 0.629 | 0.633 | 0.133 | 2.88x | 12.8/23.7/31.9% | 1.6/5.5% | 3 |

> nodes=40: decode_failures 16

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 1.25 | 1 | 0.318 | 0.306 | 0.012 | - | - | 0.458 | 0.461 | 0.030 | 1.60x | 10.9/27.3/29.0% | 2.2/5.9% | 3 |
| 1.5 | 1 | 0.192 | 0.190 | 0.002 | - | - | 0.255 | 0.255 | 0.000 | 1.21x | 7.3/17.0/23.2% | 1.9/4.9% | 3 |
| 2.0 | 1 | 0.079 | 0.078 | 0.001 | - | - | 0.149 | 0.185 | 0.000 | 0.68x | 3.1/6.8/9.7% | 1.0/2.8% | 3 |

> stretch=2.0: decode_failures 4

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| clustered | 1 | 0.883 | 0.881 | 0.003 | - | - | 0.983 | 0.984 | 0.000 | 1.20x | 24.9/33.6/36.2% | 1.6/5.8% | 3 |
| corridor | 1 | 0.389 | 0.386 | 0.004 | - | - | 0.517 | 0.519 | 0.080 | 1.61x | 14.8/29.6/34.1% | 2.1/7.1% | 3 |
| hub | 1 | 0.906 | 0.904 | 0.002 | - | - | 0.961 | 0.963 | 0.743 | 1.28x | 20.6/32.0/34.1% | 1.9/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.676 | 0.676 | 0.000 | - | - | 0.848 | 0.850 | 0.218 | 1.57x | 16.2/27.3/33.8% | 2.4/6.3% | 3 |
| True | 1 | 0.674 | 0.674 | 0.000 | - | - | 0.830 | 0.833 | 0.212 | 1.56x | 16.0/27.3/33.7% | 2.3/6.2% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.674 | 0.674 | 0.000 | - | - | 0.830 | 0.833 | 0.212 | 1.56x | 16.0/27.3/33.7% | 2.3/6.2% | 3 |
| m4-early-flood | 1 | 0.679 | 0.679 | 0.000 | - | - | 0.834 | 0.837 | 0.216 | 1.58x | 16.2/27.4/33.8% | 2.4/6.3% | 3 |

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.705 | 0.705 | 0.000 | - | - | 0 | 0.000 | 0.218 | 1.32x | 14.1/23.0/28.2% | 2.0/5.0% | 3 |
| chain | 1 | 0.698 | 0.695 | 0.003 | - | - | 0.803 | 0.850 | 0.223 | 1.52x | 15.4/26.5/32.6% | 2.3/5.9% | 3 |
| sr | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| True | 1 | 0.711 | 0.703 | 0.008 | - | - | 0.868 | 0.869 | 0.229 | 1.38x | 14.4/23.7/29.2% | 2.1/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.866 | 0.854 | 0.012 | - | - | 0.981 | 0.981 | 0.468 | 2.12x | 16.9/32.3/36.9% | 1.4/5.2% | 3 |
| True | 1 | 0.867 | 0.856 | 0.011 | - | - | 0.974 | 0.975 | 0.498 | 2.15x | 17.2/32.9/37.5% | 1.4/5.2% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.108 | 0.106 | 0.001 | - | - | 0.239 | 0.248 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.213 | 0.212 | 0.001 | - | - | 0.300 | 0.301 | 0.000 | 0.18x | 1.1/2.8/4.0% | 0.3/0.9% | 3 |
| LONG_TURBO | 1 | 0.576 | 0.564 | 0.012 | - | - | 0.765 | 0.766 | 0.184 | 1.31x | 10.2/20.4/25.5% | 1.8/4.7% | 3 |

> faster: 0.906 s per simulated hour against 1.82 over 39 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.721 | 0.711 | 0.010 | - | - | 0.879 | 0.881 | 0.241 | 1.34x | 14.7/24.0/29.3% | 2.0/5.3% | 3 |
| 1.0 | 1 | 0.850 | 0.843 | 0.007 | - | - | 0.931 | 0.933 | 0.598 | 1.10x | 22.1/30.1/33.2% | 1.5/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.174 | 0.172 | 0.002 | - | - | 0.244 | 0.246 | 0.000 | 0.10x | 0.6/1.4/2.0% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| LITE_FAST | 1 | 0.602 | 0.593 | 0.009 | - | - | 0.805 | 0.806 | 0.163 | 0.99x | 8.5/16.0/20.7% | 1.4/4.0% | 3 |
| NARROW_SLOW | 1 | 0.640 | 0.632 | 0.008 | - | - | 0.831 | 0.832 | 0.186 | 1.25x | 11.9/21.4/27.9% | 1.8/4.9% | 3 |

> faster: 0.724 s per simulated hour against 2 over 39 prior run(s) - 2.8x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| temporal | 1 | 0.550 | 0.538 | 0.012 | - | - | 0.745 | 0.746 | 0.129 | 1.24x | 12.4/21.6/27.2% | 1.9/5.0% | 3 |
| transient | 1 | 0.705 | 0.694 | 0.011 | - | - | 0.858 | 0.858 | 0.217 | 1.32x | 13.7/22.8/28.2% | 2.0/5.1% | 3 |
| periodic | 1 | 0.551 | 0.543 | 0.008 | - | - | 0.683 | 0.688 | 0.110 | 1.20x | 12.8/20.8/26.1% | 1.8/4.4% | 3 |

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.174 | 0.172 | 0.002 | - | - | 0.244 | 0.246 | 0.000 | 0.10x | 0.6/1.4/2.0% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| LONG_MODERATE | 1 | 0.733 | 0.718 | 0.015 | - | - | 0.876 | 0.880 | 0.495 | 3.47x | 40.7/59.5/64.8% | 5.4/12.2% | 3 |

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.031 | 0.031 | 0.000 | - | - | 0.038 | 0.042 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.108 | 0.106 | 0.001 | - | - | 0.239 | 0.248 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.1% | 3 |
| LONG_FAST | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| LONG_TURBO | 1 | 0.576 | 0.564 | 0.012 | - | - | 0.765 | 0.766 | 0.184 | 1.31x | 10.2/20.4/25.5% | 1.8/4.7% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.698 | 0.689 | 0.009 | - | - | 0.839 | 0.839 | 0.224 | 1.86x | 18.6/29.4/36.3% | 2.8/6.8% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.671 | 0.665 | 0.007 | - | - | 0.814 | 0.815 | 0.202 | 1.30x | 13.7/22.9/28.3% | 2.0/5.0% | 3 |
| 10000 | 1 | 0.551 | 0.543 | 0.008 | - | - | 0.683 | 0.688 | 0.110 | 1.20x | 12.8/20.8/26.1% | 1.8/4.4% | 3 |
| 4000 | 1 | 0.308 | 0.303 | 0.005 | - | - | 0.403 | 0.421 | 0.028 | 1.00x | 10.9/18.1/22.5% | 1.6/3.4% | 3 |
| 2000 | 1 | 0.073 | 0.073 | 0.000 | - | - | 0.080 | 0.120 | 0.009 | 0.69x | 7.8/13.3/15.8% | 1.1/1.9% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.192 | 0.190 | 0.002 | - | - | 0.255 | 0.255 | 0.000 | 1.21x | 7.3/17.0/23.2% | 1.9/4.9% | 3 |
| 1.0 | 1 | 0.562 | 0.557 | 0.004 | - | - | 0.618 | 0.618 | 0.387 | 0.98x | 14.5/22.6/24.4% | 1.4/4.4% | 3 |

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 22 | 1 | 0.201 | 0.200 | 0.001 | - | - | 0.274 | 0.277 | 0.000 | 1.24x | 7.4/17.3/23.6% | 1.9/5.1% | 3 |
| 17 | 1 | 0.097 | 0.093 | 0.004 | - | - | 0.127 | 0.155 | 0.000 | 0.77x | 4.1/7.5/9.8% | 1.4/2.9% | 3 |
| 14 | 1 | 0.042 | 0.042 | 0.000 | - | - | 0.014 | 0.042 | 0.000 | 0.45x | 1.8/3.8/4.8% | 0.7/1.8% | 3 |

> tx-power=17: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.866 | 0.854 | 0.012 | - | - | 0.981 | 0.981 | 0.468 | 2.12x | 16.9/32.3/36.9% | 1.4/5.2% | 3 |
| True | 1 | 0.850 | 0.836 | 0.014 | - | - | 0.970 | 0.971 | 0.452 | 2.41x | 19.3/36.2/40.7% | 1.6/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.736 | 0.727 | 0.009 | - | - | 0.876 | 0.878 | 0.241 | 1.45x | 14.8/26.2/31.6% | 2.2/5.1% | 3 |
| True | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.847 | 0.848 | 0.308 | 1.57x | 16.1/26.3/32.0% | 2.5/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| random | 1 | 0.716 | 0.706 | 0.010 | - | - | 0.881 | 0.881 | 0.312 | 1.34x | 13.9/22.6/27.8% | 2.0/4.9% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.528 | 0.506 | 0.022 | - | - | 0.764 | 0.764 | 0.141 | 1.02x | 10.5/18.7/23.7% | 1.5/4.2% | 3 |
| 7 | 1 | 0.800 | 0.796 | 0.004 | - | - | 0.911 | 0.911 | 0.402 | 1.52x | 15.9/24.4/29.9% | 2.3/5.2% | 3 |
| 15 | 1 | 0.854 | 0.853 | 0.001 | - | - | 0.923 | 0.924 | 0.562 | 1.56x | 16.3/24.2/29.8% | 2.4/5.2% | 3 |
| 32 | 1 | 0.864 | 0.863 | 0.001 | - | - | 0.934 | 0.935 | 0.597 | 1.55x | 16.3/24.3/29.7% | 2.4/5.2% | 3 |

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.528 | 0.506 | 0.022 | - | - | 0.764 | 0.764 | 0.141 | 1.02x | 10.5/18.7/23.7% | 1.5/4.2% | 3 |
| 5 | 1 | 0.714 | 0.704 | 0.010 | - | - | 0.887 | 0.890 | 0.298 | 1.31x | 13.6/22.3/27.4% | 2.0/4.9% | 3 |
| 7 | 1 | 0.800 | 0.796 | 0.004 | - | - | 0.911 | 0.911 | 0.402 | 1.52x | 15.9/24.4/29.9% | 2.3/5.2% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.716 | 0.716 | 0.000 | - | - | 0.817 | 0.873 | 0.232 | 1.34x | 14.1/23.2/28.5% | 2.1/5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.528 | 0.506 | 0.022 | - | - | 0.764 | 0.764 | 0.141 | 1.02x | 10.5/18.7/23.7% | 1.5/4.2% | 3 |
| True | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| BALANCED | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| STRICT | 1 | 0.548 | 0.548 | 0.000 | - | - | 0.694 | 0.694 | 0.158 | 1.44x | 15.3/25.0/30.8% | 2.2/5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| dm | 1 | 0.720 | 0.711 | 0.009 | - | - | 0.865 | 0.866 | 0.228 | 1.34x | 14.0/23.2/28.7% | 2.0/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.859 | 0.860 | 0.220 | 1.37x | 14.4/23.8/29.2% | 2.1/5.3% | 3 |
| local | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| time | 1 | 0.712 | 0.703 | 0.009 | - | - | 0.864 | 0.864 | 0.228 | 1.38x | 14.4/24.1/29.5% | 2.1/5.3% | 3 |
| window | 1 | 0.730 | 0.720 | 0.010 | - | - | 0.885 | 0.886 | 0.231 | 1.35x | 14.2/23.5/28.8% | 2.0/5.1% | 3 |

> bucket-mode=global: misdecodes 27

> bucket-mode=time: misdecodes 43

> bucket-mode=window: misdecodes 31

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.710 | 0.701 | 0.009 | - | - | 0.860 | 0.861 | 0.246 | 1.47x | 14.9/25.6/31.5% | 2.2/5.8% | 3 |
| 1800 | 1 | 0.712 | 0.703 | 0.009 | - | - | 0.864 | 0.864 | 0.228 | 1.38x | 14.4/24.1/29.5% | 2.1/5.3% | 3 |
| 3600 | 1 | 0.715 | 0.706 | 0.009 | - | - | 0.864 | 0.864 | 0.221 | 1.36x | 14.2/23.4/28.9% | 2.1/5.2% | 3 |

> time-bucket-s=600: misdecodes 129

> time-bucket-s=1800: misdecodes 43

> time-bucket-s=3600: misdecodes 17

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| interval | 1 | 0.680 | 0.670 | 0.010 | - | - | 0.813 | 0.823 | 0.207 | 1.76x | 17.0/31.2/38.6% | 2.6/7.9% | 3 |
| aimd | 1 | 0.708 | 0.705 | 0.003 | - | - | 0.830 | 0.872 | 0.218 | 1.36x | 14.2/23.6/29.0% | 2.1/5.2% | 3 |
| bucket+interval | 1 | 0.676 | 0.664 | 0.012 | - | - | 0.817 | 0.818 | 0.219 | 1.79x | 17.5/32.3/39.5% | 2.6/8.0% | 3 |

> trigger=interval: misdecodes 14

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 12

> trigger=bucket+interval: misdecodes 24

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.724 | 0.715 | 0.010 | - | - | 0.873 | 0.876 | 0.239 | 1.35x | 13.9/23.5/29.1% | 2.1/5.3% | 3 |
| 8 | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.868 | 0.869 | 0.235 | 1.35x | 14.2/23.5/29.0% | 2.1/5.2% | 3 |
| 16 | 1 | 0.712 | 0.704 | 0.008 | - | - | 0.865 | 0.866 | 0.229 | 1.34x | 14.0/23.2/28.6% | 2.0/5.1% | 3 |
| 32 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 50 | 1 | 0.718 | 0.709 | 0.009 | - | - | 0.858 | 0.858 | 0.224 | 1.35x | 14.2/23.5/28.8% | 2.0/5.2% | 3 |

> capacity=4: decode_failures 86

> capacity=8: decode_failures 30

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.724 | 0.715 | 0.010 | - | - | 0.873 | 0.876 | 0.239 | 1.35x | 13.9/23.5/29.1% | 2.1/5.3% | 3 |
| 8 | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.868 | 0.869 | 0.235 | 1.35x | 14.2/23.5/29.0% | 2.1/5.2% | 3 |
| 16 | 1 | 0.712 | 0.704 | 0.008 | - | - | 0.865 | 0.866 | 0.229 | 1.34x | 14.0/23.2/28.6% | 2.0/5.1% | 3 |
| 32 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 50 | 1 | 0.718 | 0.709 | 0.009 | - | - | 0.858 | 0.858 | 0.224 | 1.35x | 14.2/23.5/28.8% | 2.0/5.2% | 3 |

> capacity=4: decode_failures 86

> capacity=8: decode_failures 30

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.718 | 0.709 | 0.009 | - | - | 0.862 | 0.871 | 0.240 | 1.36x | 14.1/23.6/29.0% | 2.1/5.2% | 3 |
| 16 | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.859 | 0.861 | 0.253 | 1.34x | 14.2/23.2/28.6% | 2.0/5.1% | 3 |
| 32 | 1 | 0.730 | 0.720 | 0.010 | - | - | 0.885 | 0.886 | 0.231 | 1.35x | 14.2/23.5/28.8% | 2.0/5.1% | 3 |

> capacity=8: misdecodes 23

> capacity=8: decode_failures 22

> capacity=16: misdecodes 26

> capacity=32: misdecodes 31

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.676 | 0.664 | 0.012 | - | - | 0.817 | 0.818 | 0.219 | 1.79x | 17.5/32.3/39.5% | 2.6/8.0% | 3 |
| 02-06 | 1 | 0.712 | 0.708 | 0.004 | - | - | 0.839 | 0.866 | 0.236 | 1.39x | 14.4/24.2/29.7% | 2.1/5.4% | 3 |
| 00-08 | 1 | 0.712 | 0.707 | 0.005 | - | - | 0.836 | 0.856 | 0.242 | 1.44x | 14.7/25.0/31.0% | 2.2/5.9% | 3 |

> catch-up-hours=: misdecodes 24

> catch-up-hours=02-06: decode_failures 25

> catch-up-hours=00-08: decode_failures 22

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.720 | 0.716 | 0.004 | - | - | 0.850 | 0.853 | 0.237 | 1.33x | 13.8/23.0/28.3% | 2.0/5.0% | 3 |
| 2 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 3 | 1 | 0.738 | 0.712 | 0.026 | - | - | 0.847 | 0.954 | 0.232 | 1.36x | 14.5/23.7/29.2% | 2.1/5.1% | 3 |
| 4 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.795 | 0.957 | 0.232 | 1.36x | 14.4/23.5/29.0% | 2.1/5.1% | 3 |

> hops-apart=3: decode_failures 26

> hops-apart=4: decode_failures 29

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.720 | 0.716 | 0.004 | - | - | 0.850 | 0.853 | 0.237 | 1.33x | 13.8/23.0/28.3% | 2.0/5.0% | 3 |
| 2 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 3 | 1 | 0.738 | 0.712 | 0.026 | - | - | 0.847 | 0.954 | 0.232 | 1.36x | 14.5/23.7/29.2% | 2.1/5.1% | 3 |
| 4 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.795 | 0.957 | 0.232 | 1.36x | 14.4/23.5/29.0% | 2.1/5.1% | 3 |
| 5 | 1 | 0.743 | 0.703 | 0.040 | - | - | 0.867 | 0.966 | 0.229 | 1.38x | 14.5/24.0/29.5% | 2.0/5.2% | 3 |

> hops-apart=3: decode_failures 26

> hops-apart=4: decode_failures 29

> hops-apart=5: decode_failures 26

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.873 | 0.875 | 0.236 | 1.36x | 14.3/23.6/29.0% | 2.1/5.2% | 3 |
| 30 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 120 | 1 | 0.727 | 0.719 | 0.008 | - | - | 0.870 | 0.870 | 0.239 | 1.35x | 14.2/23.3/28.6% | 2.0/5.1% | 3 |
| 600 | 1 | 0.725 | 0.716 | 0.009 | - | - | 0.877 | 0.878 | 0.245 | 1.36x | 14.2/23.6/29.0% | 2.0/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.873 | 0.875 | 0.236 | 1.36x | 14.3/23.6/29.0% | 2.1/5.2% | 3 |
| 30 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 120 | 1 | 0.727 | 0.719 | 0.008 | - | - | 0.870 | 0.870 | 0.239 | 1.35x | 14.2/23.3/28.6% | 2.0/5.1% | 3 |
| 600 | 1 | 0.725 | 0.716 | 0.009 | - | - | 0.877 | 0.878 | 0.245 | 1.36x | 14.2/23.6/29.0% | 2.0/5.2% | 3 |

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.734 | 0.714 | 0.021 | - | - | 0.697 | 0.930 | 0.222 | 1.34x | 14.2/23.1/28.4% | 2.0/5.0% | 3 |
| routers | 1 | 0.720 | 0.716 | 0.004 | - | - | 0.868 | 0.868 | 0.230 | 1.35x | 14.2/23.5/28.9% | 2.1/5.1% | 3 |
| alternate-routers | 1 | 0.710 | 0.705 | 0.005 | - | - | 0.858 | 0.858 | 0.212 | 1.34x | 14.0/23.4/28.7% | 2.0/5.1% | 3 |
| beside-router | 1 | 0.712 | 0.706 | 0.007 | - | - | 0.882 | 0.882 | 0.222 | 1.35x | 14.1/23.5/28.9% | 2.0/5.1% | 3 |
| random-clients | 1 | 0.741 | 0.705 | 0.036 | - | - | 0.866 | 0.948 | 0.226 | 1.38x | 14.6/23.8/29.5% | 2.1/5.2% | 3 |
| hops-apart | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

> place=spread: decode_failures 19

> place=random-clients: decode_failures 25

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.734 | 0.714 | 0.021 | - | - | 0.697 | 0.930 | 0.222 | 1.34x | 14.2/23.1/28.4% | 2.0/5.0% | 3 |
| routers | 1 | 0.720 | 0.716 | 0.004 | - | - | 0.868 | 0.868 | 0.230 | 1.35x | 14.2/23.5/28.9% | 2.1/5.1% | 3 |
| alternate-routers | 1 | 0.710 | 0.705 | 0.005 | - | - | 0.858 | 0.858 | 0.212 | 1.34x | 14.0/23.4/28.7% | 2.0/5.1% | 3 |
| beside-router | 1 | 0.712 | 0.706 | 0.007 | - | - | 0.882 | 0.882 | 0.222 | 1.35x | 14.1/23.5/28.9% | 2.0/5.1% | 3 |
| random-clients | 1 | 0.741 | 0.705 | 0.036 | - | - | 0.866 | 0.948 | 0.226 | 1.38x | 14.6/23.8/29.5% | 2.1/5.2% | 3 |
| hops-apart | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

> place=spread: decode_failures 19

> place=random-clients: decode_failures 25

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| broadcast | 1 | 0.739 | 0.705 | 0.035 | - | - | 0.863 | 0.863 | 0.232 | 1.38x | 14.3/24.0/29.4% | 2.1/5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| heard | 1 | 0.721 | 0.712 | 0.009 | - | - | 0.875 | 0.875 | 0.226 | 1.37x | 14.3/23.7/29.1% | 2.0/5.2% | 3 |

> replay-ordering=heard: misdecodes 9

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.739 | 0.705 | 0.035 | - | - | 0.863 | 0.863 | 0.232 | 1.38x | 14.3/24.0/29.4% | 2.1/5.3% | 3 |
| heard | 1 | 0.740 | 0.705 | 0.035 | - | - | 0.864 | 0.865 | 0.238 | 1.39x | 14.4/24.1/29.5% | 2.1/5.3% | 3 |

> replay-ordering=heard: misdecodes 22

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| enum | 1 | 0.720 | 0.710 | 0.011 | - | - | 0.870 | 0.872 | 0.235 | 1.35x | 14.1/23.3/28.8% | 2.1/5.3% | 3 |
| hybrid | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.720 | 0.716 | 0.004 | - | - | 0.868 | 0.868 | 0.230 | 1.35x | 14.2/23.5/28.9% | 2.1/5.1% | 3 |
| 6 | 1 | 0.703 | 0.694 | 0.008 | - | - | 0.857 | 0.857 | 0.230 | 1.38x | 14.3/24.0/29.7% | 2.1/5.4% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.709 | 0.703 | 0.005 | - | - | 0.850 | 0.852 | 0.224 | 1.35x | 14.0/23.2/28.6% | 2.1/5.1% | 2 |
| 3 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 5 | 1 | 0.737 | 0.715 | 0.022 | - | - | 0.895 | 0.898 | 0.229 | 1.38x | 14.5/24.2/29.6% | 2.1/5.3% | 5 |
| 8 | 1 | 0.725 | 0.694 | 0.031 | - | - | 0.887 | 0.888 | 0.220 | 1.43x | 14.7/25.2/30.5% | 2.1/5.5% | 8 |

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.709 | 0.703 | 0.005 | - | - | 0.850 | 0.852 | 0.224 | 1.35x | 14.0/23.2/28.6% | 2.1/5.1% | 2 |
| 3 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 5 | 1 | 0.737 | 0.715 | 0.022 | - | - | 0.895 | 0.898 | 0.229 | 1.38x | 14.5/24.2/29.6% | 2.1/5.3% | 5 |
| 8 | 1 | 0.725 | 0.694 | 0.031 | - | - | 0.887 | 0.888 | 0.220 | 1.43x | 14.7/25.2/30.5% | 2.1/5.5% | 8 |

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| True | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.849 | 0.851 | 0.220 | 1.27x | 13.2/22.0/27.1% | 1.9/4.8% | 3 |
| 1 | 1 | 0.722 | 0.712 | 0.010 | - | - | 0.882 | 0.884 | 0.233 | 1.26x | 13.0/21.8/26.9% | 1.9/4.8% | 3 |
| 2 | 1 | 0.713 | 0.705 | 0.007 | - | - | 0.870 | 0.871 | 0.206 | 1.24x | 12.8/21.3/26.3% | 1.9/4.7% | 3 |
| 4 | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.868 | 0.868 | 0.245 | 1.25x | 13.1/21.8/26.8% | 1.9/4.8% | 3 |

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.718 | 0.711 | 0.007 | - | - | 0.864 | 0.865 | 0.222 | 1.34x | 14.0/23.3/28.6% | 2.0/5.2% | 3 |
| 24 | 1 | 0.715 | 0.707 | 0.008 | - | - | 0.860 | 0.861 | 0.211 | 1.35x | 14.2/23.5/29.0% | 2.0/5.2% | 3 |
| 32 | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.883 | 0.883 | 0.241 | 1.37x | 14.2/23.6/29.1% | 2.0/5.2% | 3 |
| 64 | 1 | 0.712 | 0.705 | 0.007 | - | - | 0.850 | 0.852 | 0.239 | 1.37x | 14.3/23.7/29.1% | 2.1/5.2% | 3 |

> short-id-bits=24: misdecodes 1

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.712 | 0.703 | 0.010 | - | - | 0.864 | 0.865 | 0.227 | 1.42x | 14.6/24.6/30.2% | 2.1/5.4% | 3 |
| 16 | 1 | 0.709 | 0.699 | 0.010 | - | - | 0.856 | 0.856 | 0.230 | 1.38x | 14.3/23.9/29.4% | 2.1/5.2% | 3 |
| 32 | 1 | 0.730 | 0.720 | 0.010 | - | - | 0.885 | 0.886 | 0.231 | 1.35x | 14.2/23.5/28.8% | 2.0/5.1% | 3 |

> window-size=8: misdecodes 94

> window-size=16: misdecodes 49

> window-size=32: misdecodes 31

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.866 | 0.854 | 0.012 | - | - | 0.981 | 0.981 | 0.468 | 2.12x | 16.9/32.3/36.9% | 1.4/5.2% | 3 |
| True | 1 | 0.640 | 0.616 | 0.024 | - | - | 0.832 | 0.885 | 0.283 | 5.52x | 43.1/70.0/76.1% | 3.9/11.9% | 3 |

> no-congestion-scaling=True: decode_failures 75

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.317 | 0.310 | 0.006 | - | - | 0.476 | 0.596 | 0.056 | 4.93x | 13.3/22.8/30.2% | 1.7/5.5% | 3 |
| truesize | 1 | 0.356 | 0.349 | 0.008 | - | - | 0.553 | 0.650 | 0.064 | 2.61x | 6.4/14.5/20.9% | 0.8/3.6% | 3 |

> congestion-input=hotstore: decode_failures 55

> congestion-input=truesize: decode_failures 85

> slower: 35.3 s per simulated hour against 11.2 over 39 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.870 | 0.859 | 0.011 | - | - | 0.981 | 0.983 | 0.462 | 2.08x | 16.4/32.0/36.2% | 1.4/5.2% | 3 |
| adaptive | 1 | 0.866 | 0.854 | 0.012 | - | - | 0.981 | 0.981 | 0.468 | 2.12x | 16.9/32.3/36.9% | 1.4/5.2% | 3 |

