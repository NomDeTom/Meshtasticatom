# Sweep blocks-2026-10-24-1019153

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 1019153 · seeds 1019153
- **blocks** 87 run
- **compute** 11.2 h of simulator time across every cell
- **generated** 2026-10-24T08:23:54+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>118 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 10
- AD-badrouters: role-placement=random: decode_failures 3
- AD-siting: siting-mix=local-typical: decode_failures 22
- AD-siting: siting-mix=basement-heavy: decode_failures 2
- AD-worst: role-placement=degree: decode_failures 38
- AD-worst: role-placement=inverse: decode_failures 31
- AD-worst: slower: 14.9 s per simulated hour against 3.39 over 64 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 31
- BL-control: slower: 5.74 s per simulated hour against 1.81 over 64 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 41
- DB-hotstore-stress: max-num-nodes=120: decode_failures 55
- DB-hotstore-stress: max-num-nodes=250: decode_failures 25
- DB-warm: warm-num-nodes=0: decode_failures 64
- DB-warm: warm-num-nodes=25: decode_failures 64
- DB-warm: warm-num-nodes=100: decode_failures 64
- DB-warm: warm-num-nodes=2000: decode_failures 64
- DG-burst: burst-loss=0.1: decode_failures 12
- DG-burst: burst-loss=0.2: decode_failures 31
- DG-burst: burst-loss=0.3: decode_failures 28
- DG-loss: extra-loss=0.1: decode_failures 1
- DG-loss: extra-loss=0.3: decode_failures 15
- DG-outage: burst-loss=0.1: decode_failures 17
- DG-outage: burst-loss=0.2: decode_failures 34
- DG-outage: burst-loss=0.3: decode_failures 20
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 12
- DM-mode: dm-mode=m4-early-flood: decode_failures 9
- FW-mixed-26: legacy-fraction=0.25: decode_failures 30
- FW-mixed-26: legacy-fraction=0.5: decode_failures 17
- FW-mixed-26: slower: 4.97 s per simulated hour against 1.7 over 64 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.25: decode_failures 19
- FW-mixed: legacy-fraction=0.5: decode_failures 23
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 20
- LD-chatty: broadcast-interval-s=300: decode_failures 19
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 1
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 64
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 48
- LD-traceroute-small: faster: 15.5 s per simulated hour against 36.9 over 64 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-density: nodes=40: decode_failures 12
- MS-hopscale: nodes=120: decode_failures 5
- MS-hopscale: nodes=250: decode_failures 50
- MS-hopscale: nodes=500: decode_failures 141
- MS-oversubscribed: nodes=250: decode_failures 55
- MS-oversubscribed: nodes=500: decode_failures 124
- MS-router-late: router-late-fraction=0.2: decode_failures 1
- MS-siting: siting-mix=local-typical: decode_failures 13
- MS-siting: siting-mix=event: decode_failures 11
- MS-size: nodes=90: decode_failures 51
- MS-size: nodes=120: decode_failures 5
- MS-size: nodes=150: decode_failures 84
- MS-size: slower: 10.5 s per simulated hour against 3.38 over 64 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.25: decode_failures 14
- MS-stretch: stretch=1.5: decode_failures 1
- PR-crladder: coding-rate-ladder=False: decode_failures 12
- PR-crladder: coding-rate-ladder=True: decode_failures 1
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 1
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 25
- RF-bw500: preset=SHORT_TURBO: decode_failures 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 2
- RF-noise: noise-profile=temporal: decode_failures 18
- RF-noise: noise-profile=periodic: decode_failures 5
- RF-preset: preset=LONG_MODERATE: decode_failures 4
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 5
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 1
- RF-txpower: tx-power=17: decode_failures 1
- RT-hoplimit: hop-limit=3: decode_failures 11
- RT-hopspread: hop-limit=3: decode_failures 11
- RT-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 11
- SC-signing: signature-policy=STRICT: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 21
- SF-bucket-mode: bucket-mode=time: misdecodes 13
- SF-bucket-mode: bucket-mode=window: misdecodes 9
- SF-bucket-time: time-bucket-s=600: misdecodes 106
- SF-bucket-time: time-bucket-s=1800: misdecodes 13
- SF-bucket-time: time-bucket-s=3600: misdecodes 4
- SF-bucket-time: time-bucket-s=3600: decode_failures 1
- SF-cadence: trigger=interval: misdecodes 12
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 13
- SF-capacity-local: capacity=4: decode_failures 90
- SF-capacity-local: capacity=8: decode_failures 84
- SF-capacity-local: capacity=16: decode_failures 2
- SF-capacity: capacity=4: decode_failures 90
- SF-capacity: capacity=8: decode_failures 84
- SF-capacity: capacity=16: decode_failures 2
- SF-capacity-window: capacity=8: misdecodes 5
- SF-capacity-window: capacity=8: decode_failures 84
- SF-capacity-window: capacity=16: misdecodes 13
- SF-capacity-window: capacity=16: decode_failures 10
- SF-capacity-window: capacity=32: misdecodes 9
- SF-catchup: catch-up-hours=: misdecodes 13
- SF-catchup: catch-up-hours=02-06: decode_failures 41
- SF-catchup: catch-up-hours=00-08: decode_failures 41
- SF-hops-flat: hops-apart=3: decode_failures 31
- SF-hops-flat: hops-apart=4: decode_failures 29
- SF-hops-spread: hops-apart=3: decode_failures 31
- SF-hops-spread: hops-apart=4: decode_failures 29
- SF-hops-spread: hops-apart=5: decode_failures 15
- SF-jitter-global: advert-jitter-s=1: decode_failures 1
- SF-jitter-local: advert-jitter-s=1: decode_failures 1
- SF-place-flat: place=spread: decode_failures 8
- SF-place-flat: place=random-clients: decode_failures 18
- SF-place-spread: place=spread: decode_failures 8
- SF-place-spread: place=random-clients: decode_failures 18
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 3
- SF-replay-order: replay-ordering=heard: misdecodes 8
- SF-servers-flat: servers=2: decode_failures 8
- SF-servers-spread: servers=2: decode_failures 8
- SF-sr-retries: sr-retries=0: decode_failures 8
- SF-window-size: window-size=8: misdecodes 116
- SF-window-size: window-size=16: misdecodes 47
- SF-window-size: window-size=32: misdecodes 9
- TH-congestion-input: congestion-input=hotstore: decode_failures 55
- TH-congestion-input: congestion-input=truesize: decode_failures 45
- TH-congestion-input: slower: 21.7 s per simulated hour against 10.2 over 64 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: decode_failures 75

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 14.9 | 3.39 | 4.38x | 64 |
| `BL-control` | 5.74 | 1.81 | 3.17x | 64 |
| `MS-size` | 10.5 | 3.38 | 3.11x | 64 |
| `FW-mixed-26` | 4.97 | 1.7 | 2.93x | 64 |
| `TH-congestion-input` | 21.7 | 10.2 | 2.12x | 64 |
| `MS-oversubscribed` | 35.5 | 19 | 1.87x | 64 |
| `PR-crladder` | 5.02 | 2.77 | 1.81x | 64 |
| `RT-spread` | 4.04 | 2.24 | 1.81x | 64 |
| `MS-siting` | 3.21 | 1.82 | 1.77x | 63 |
| `AD-badrouters` | 3.4 | 1.93 | 1.76x | 64 |
| `FW-mixed` | 2.81 | 1.66 | 1.69x | 64 |
| `DM-mode` | 5.18 | 3.12 | 1.66x | 64 |
| `PR-dmmode-cr` | 4.06 | 2.57 | 1.58x | 64 |
| `DG-loss` | 3.45 | 2.25 | 1.53x | 64 |
| `RT-hoplimit` | 2.62 | 1.73 | 1.52x | 64 |
| `SF-provide-transport` | 1.17 | 1.78 | 0.66x | 64 |
| `TH-congestion-mode` | 2.16 | 3.33 | 0.65x | 64 |
| `RF-txpower` | 1.01 | 1.58 | 0.64x | 64 |
| `RT-hopassign` | 1.12 | 1.77 | 0.64x | 64 |
| `SF-capacity` | 1.09 | 1.72 | 0.64x | 64 |
| `TH-congestion` | 10 | 17.1 | 0.59x | 64 |
| `DB-platform` | 1.44 | 2.45 | 0.59x | 64 |
| `SF-resolve` | 0.892 | 1.53 | 0.58x | 64 |
| `RF-preset-turbo` | 0.873 | 1.53 | 0.57x | 60 |
| `LD-diurnal` | 0.84 | 1.52 | 0.55x | 64 |
| `LD-traceroute-small` | 15.5 | 36.9 | 0.42x | 64 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.919 | 0.919 | 0.665 → 0.697 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.858 | 0.858 | 0.693 → 0.697 | 1.1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.067 → 0.919 | 0.853 | 0.047 → 0.683 | 19x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.085 → 0.919 | 0.835 | 0.065 → 0.683 | 13x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.087 → 0.919 | 0.832 | 0.031 → 0.683 | 15x sr_airtime | up | 5 |
| `AD-siting` | siting-mix | **held** | 0.099 → 0.917 | 0.818 | 0.018 → 0.648 | 14x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.143 → 0.956 | 0.813 | 0.135 → 0.953 | 3.2x advert_bytes | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.054 → 0.863 | 0.809 | 0.059 → 0.633 | 2.9e+02x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.087 → 0.802 | 0.715 | 0.078 → 0.537 | 11x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **held** | 0.247 → 0.919 | 0.672 | 0.125 → 0.683 | 3.8x advert_bytes | up | 4 |
| `RF-preset` | preset | **held** | 0.247 → 0.919 | 0.672 | 0.125 → 0.704 | 4.8x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.386 → 0.902 | 0.516 | 0.367 → 0.899 | 5.7x advert_bytes | up | 5 |
| `MS-hopscale` | nodes | **text** | 0.188 → 0.691 | 0.503 | 0.183 → 0.683 | 9.2x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.421 → 0.895 | 0.474 | 0.410 → 0.895 | 2.4x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **held** | 0.482 → 0.919 | 0.437 | 0.343 → 0.683 | 2x advert_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.550 → 0.929 | 0.379 | 0.674 → 0.688 | 1.7x advert_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.550 → 0.929 | 0.379 | 0.674 → 0.688 | 1.7x advert_bytes | up | 6 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.593 → 0.953 | 0.360 | 0.383 → 0.734 | 8.9x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.502 → 0.853 | 0.351 | 0.472 → 0.851 | 3.2x sr_bytes | up | 4 |
| `MS-size` | nodes | **held** | 0.575 → 0.919 | 0.345 | 0.402 → 0.708 | 9.2x sr_bytes | down | 5 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.178 → 0.506 | 0.328 | 0.170 → 0.479 | 2.7x sr_airtime | up | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.596 → 0.919 | 0.323 | 0.682 → 0.693 | 3.5x sr_bytes | down | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.516 → 0.829 | 0.312 | 0.505 → 0.827 | 8x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.388 → 0.691 | 0.303 | 0.363 → 0.683 | 1.5x sr_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.502 → 0.791 | 0.289 | 0.472 → 0.787 | 2.5x sr_bytes | up | 3 |
| `MS-oversubscribed` | nodes | **text** | 0.187 → 0.467 | 0.280 | 0.181 → 0.451 | 4.4x sr_bytes | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.691 → 0.903 | 0.212 | 0.683 → 0.888 | 1.3x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.689 → 0.892 | 0.204 | 0.673 → 0.888 | 3.1x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **held** | 0.721 → 0.923 | 0.201 | 0.514 → 0.683 | 1.6x sr_bytes | down | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.691 → 0.890 | 0.199 | 0.683 → 0.887 | 2.2x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.725 → 0.917 | 0.192 | 0.520 → 0.648 | 1.5x sr_airtime | down | 3 |
| `RT-spread` | hop-spread | **text** | 0.502 → 0.691 | 0.189 | 0.472 → 0.683 | 1.7x sr_bytes | up | 2 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.356 → 0.540 | 0.184 | 0.206 → 0.291 | 3.8x sr_airtime | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.512 → 0.691 | 0.179 | 0.501 → 0.683 | 1.2x advert_bytes | down | 4 |
| `SC-signing` | signature-policy | **held** | 0.773 → 0.919 | 0.146 | 0.559 → 0.683 | 1.3x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.638 → 0.774 | 0.136 | 0.627 → 0.771 | 5.7x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.691 → 0.827 | 0.135 | 0.683 → 0.812 | 1.4x bytes_on_air | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.664 → 0.780 | 0.117 | 0.655 → 0.777 | 2x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.666 → 0.780 | 0.114 | 0.658 → 0.777 | 2.1x sr_airtime | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.817 → 0.919 | 0.102 | 0.682 → 0.693 | 3.5x sr_bytes | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.818 → 0.919 | 0.101 | 0.683 → 0.687 | 29x sr_airtime | down | 3 |
| `FW-mixed` | legacy-fraction | **held** | 0.833 → 0.933 | 0.100 | 0.657 → 0.691 | 2.2x bytes_on_air | up | 4 |
| `SF-cadence` | trigger | **held** | 0.843 → 0.919 | 0.077 | 0.644 → 0.683 | 14x advert_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.661 → 0.734 | 0.073 | 0.648 → 0.728 | 1.9x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.661 → 0.734 | 0.073 | 0.648 → 0.728 | 1.9x bytes_on_air | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.870 → 0.941 | 0.071 | 0.675 → 0.687 | 5.6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.870 → 0.941 | 0.071 | 0.675 → 0.687 | 5.6x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.855 → 0.923 | 0.068 | 0.675 → 0.686 | 2.1x sr_bytes | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.832 → 0.898 | 0.066 | 0.612 → 0.677 | 1.3x sr_airtime | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.691 → 0.755 | 0.064 | 0.675 → 0.683 | 3.6x sr_airtime | up | 2 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.874 → 0.938 | 0.063 | 0.670 → 0.688 | 2.2x bytes_on_air | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.633 → 0.692 | 0.058 | 0.621 → 0.683 | 1.4x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.691 → 0.748 | 0.057 | 0.683 → 0.744 | 3.3x bytes_on_air | down | 2 |
| `FW-firmware` | profile | **held** | 0.919 → 0.974 | 0.055 | 0.676 → 0.683 | 3.4x bytes_on_air | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.707 → 0.761 | 0.054 | 0.701 → 0.756 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.533 → 0.583 | 0.050 | 0.290 → 0.322 | 2.1x sr_airtime | up | 2 |
| `FW-versions` | profile | **held** | 0.919 → 0.967 | 0.047 | 0.666 → 0.702 | 3.5x bytes_on_air | down | 5 |
| `AD-worst` | role-placement | **text** | 0.616 → 0.656 | 0.040 | 0.603 → 0.647 | 1.1x sr_airtime | down | 2 |
| `MS-roles` | role-mix | **text** | 0.661 → 0.700 | 0.039 | 0.648 → 0.693 | 1.2x sr_bytes | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.904 → 0.942 | 0.039 | 0.686 → 0.701 | 1.2x sr_bytes | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.658 → 0.695 | 0.038 | 0.645 → 0.691 | 9.5x advert_bytes | up | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.860 → 0.892 | 0.033 | 0.649 → 0.660 | 1.1x sr_airtime | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.685 → 0.715 | 0.030 | 0.678 → 0.707 | 1.2x bytes_on_air | up | 4 |
| `DM-mode` | dm-mode | **held** | 0.860 → 0.890 | 0.030 | 0.641 → 0.663 | 1.4x sr_airtime | down | 3 |
| `SF-capacity` | capacity | **held** | 0.903 → 0.931 | 0.028 | 0.678 → 0.691 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.903 → 0.931 | 0.028 | 0.678 → 0.691 | 5.3x advert_bytes | up | 5 |
| `LD-diurnal` | diurnal | **text** | 0.691 → 0.717 | 0.025 | 0.683 → 0.710 | 1.2x sr_bytes | down | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.691 → 0.714 | 0.022 | 0.683 → 0.703 | 1.2x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.871 → 0.892 | 0.021 | 0.660 → 0.663 | 1.1x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.921 → 0.942 | 0.021 | 0.715 → 0.736 | 1.1x sr_bytes | down | 2 |
| `SF-width` | short-id-bits | **text** | 0.680 → 0.694 | 0.014 | 0.670 → 0.685 | 3.1x advert_bytes | down | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.909 → 0.921 | 0.012 | 0.677 → 0.683 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.909 → 0.921 | 0.012 | 0.677 → 0.683 | 1.1x sr_airtime | down | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.912 → 0.923 | 0.011 | 0.683 → 0.686 | 2.8x advert_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.691 → 0.701 | 0.010 | 0.683 → 0.693 | 1.1x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **text** | 0.691 → 0.701 | 0.010 | 0.683 → 0.693 | 5.8x advert_bytes | = | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.912 → 0.920 | 0.008 | 0.678 → 0.683 | 5.4x advert_bytes | down | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.906 → 0.913 | 0.007 | 0.672 → 0.675 | 1x advert_bytes | down | 2 |
| `SF-window-size` | window-size | **held** | 0.918 → 0.924 | 0.005 | 0.683 → 0.686 | 5.3x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.887 → 0.892 | 0.005 | 0.883 → 0.888 | 1.1x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.892 → 0.897 | 0.004 | 0.888 → 0.893 | 1x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.687 → 0.691 | 0.004 | 0.679 → 0.683 | 1x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.919 → 0.923 | 0.003 | 0.681 → 0.683 | 2.6x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.688 → 0.690 | 0.002 | 0.670 → 0.678 | 2.3x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.892 → 0.894 | 0.002 | 0.888 → 0.890 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| sprinkled | 1 | 0.781 | 0.777 | 0.004 | - | - | 0.895 | 0.896 | 0.363 | 1.35x | 16.0/21.0/24.8% | 2.1/5.1% | 3 |
| arms-race | 1 | 0.890 | 0.887 | 0.003 | - | - | 0.930 | 0.931 | 0.690 | 1.22x | 20.1/26.5/28.4% | 1.5/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.1 | 1 | 0.776 | 0.766 | 0.010 | - | - | 0.905 | 0.908 | 0.489 | 1.33x | 14.7/20.5/22.8% | 2.2/4.2% | 3 |
| 0.3 | 1 | 0.903 | 0.888 | 0.015 | - | - | 0.955 | 0.955 | 0.749 | 1.18x | 17.7/23.6/27.5% | 1.7/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.661 | 0.648 | 0.013 | - | - | 0.917 | 0.922 | 0.000 | 1.29x | 13.2/21.2/23.8% | 2.0/5.0% | 3 |
| inverse | 1 | 0.531 | 0.520 | 0.011 | - | - | 0.725 | 0.909 | 0.000 | 1.13x | 10.0/15.9/17.6% | 1.8/3.7% | 3 |
| random | 1 | 0.548 | 0.529 | 0.019 | - | - | 0.845 | 0.854 | 0.000 | 1.15x | 10.5/17.4/19.9% | 2.1/3.8% | 3 |

> role-placement=inverse: decode_failures 10

> role-placement=random: decode_failures 3

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.661 | 0.648 | 0.013 | - | - | 0.917 | 0.922 | 0.000 | 1.29x | 13.2/21.2/23.8% | 2.0/5.0% | 3 |
| all-routers | 1 | 0.734 | 0.728 | 0.006 | - | - | 0.906 | 0.909 | 0.000 | 2.41x | 20.1/31.9/35.5% | 4.1/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.661 | 0.648 | 0.013 | - | - | 0.917 | 0.922 | 0.000 | 1.29x | 13.2/21.2/23.8% | 2.0/5.0% | 3 |
| no-mute | 1 | 0.688 | 0.676 | 0.011 | - | - | 0.933 | 0.941 | 0.000 | 1.38x | 13.0/20.7/21.8% | 2.3/4.5% | 3 |
| all-routers | 1 | 0.734 | 0.728 | 0.006 | - | - | 0.906 | 0.909 | 0.000 | 2.41x | 20.1/31.9/35.5% | 4.1/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.661 | 0.648 | 0.013 | - | - | 0.917 | 0.922 | 0.000 | 1.29x | 13.2/21.2/23.8% | 2.0/5.0% | 3 |
| local-typical | 1 | 0.509 | 0.503 | 0.006 | - | - | 0.692 | 0.747 | 0.000 | 1.22x | 10.6/21.8/27.3% | 1.9/5.6% | 3 |
| basement-heavy | 1 | 0.018 | 0.018 | 0.000 | - | - | 0.099 | 0.140 | 0.000 | 0.24x | 0.2/1.9/3.0% | 0.2/1.4% | 3 |

> siting-mix=local-typical: decode_failures 22

> siting-mix=basement-heavy: decode_failures 2

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.656 | 0.647 | 0.009 | - | - | 0.836 | 0.848 | 0.000 | 2.34x | 12.2/21.4/27.2% | 1.8/5.6% | 3 |
| inverse | 1 | 0.616 | 0.603 | 0.013 | - | - | 0.842 | 0.853 | 0.000 | 2.31x | 10.7/20.1/27.6% | 1.8/3.2% | 3 |

> role-placement=degree: decode_failures 38

> role-placement=inverse: decode_failures 31

> slower: 14.9 s per simulated hour against 3.39 over 64 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.697 | 0.697 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.38x | 12.9/21.4/23.0% | 2.2/5.2% | 3 |
| sr | 1 | 0.723 | 0.693 | 0.030 | - | - | 0.858 | 0.916 | 0.000 | 1.45x | 13.6/22.6/24.2% | 2.2/5.4% | 3 |

> protocol=sr: decode_failures 31

> slower: 5.74 s per simulated hour against 1.81 over 64 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.666 | 0.658 | 0.008 | - | - | 0.831 | 0.832 | 0.000 | 3.13x | 28.4/46.7/51.1% | 5.1/9.3% | 3 |
| 100 | 1 | 0.780 | 0.777 | 0.004 | - | - | 0.918 | 0.918 | 0.000 | 1.73x | 16.0/26.8/28.8% | 2.7/5.2% | 3 |
| 120 | 1 | 0.780 | 0.777 | 0.004 | - | - | 0.918 | 0.918 | 0.000 | 1.73x | 16.0/26.8/28.8% | 2.7/5.2% | 3 |
| 250 | 1 | 0.780 | 0.777 | 0.004 | - | - | 0.918 | 0.918 | 0.000 | 1.73x | 16.0/26.8/28.8% | 2.7/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.210 | 0.206 | 0.005 | - | - | 0.356 | 0.406 | 0.079 | 9.55x | 26.8/37.9/50.2% | 3.4/9.7% | 3 |
| 120 | 1 | 0.296 | 0.290 | 0.006 | - | - | 0.533 | 0.541 | 0.105 | 4.42x | 12.2/19.5/24.9% | 1.5/5.2% | 3 |
| 250 | 1 | 0.297 | 0.291 | 0.006 | - | - | 0.540 | 0.551 | 0.103 | 4.40x | 12.3/19.2/24.6% | 1.5/5.1% | 3 |

> max-num-nodes=10: decode_failures 41

> max-num-nodes=120: decode_failures 55

> max-num-nodes=250: decode_failures 25

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.780 | 0.777 | 0.004 | - | - | 0.918 | 0.918 | 0.000 | 1.73x | 16.0/26.8/28.8% | 2.7/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.780 | 0.777 | 0.004 | - | - | 0.918 | 0.918 | 0.000 | 1.73x | 16.0/26.8/28.8% | 2.7/5.2% | 3 |
| constrained | 1 | 0.664 | 0.655 | 0.009 | - | - | 0.832 | 0.839 | 0.000 | 3.14x | 28.5/46.8/51.3% | 5.1/9.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.691 | 0.677 | 0.014 | - | - | 0.898 | 0.918 | 0.431 | 5.58x | 48.0/64.9/72.0% | 3.7/12.1% | 3 |
| 25 | 1 | 0.691 | 0.677 | 0.014 | - | - | 0.898 | 0.918 | 0.431 | 5.58x | 48.0/64.9/72.0% | 3.7/12.1% | 3 |
| 100 | 1 | 0.691 | 0.677 | 0.014 | - | - | 0.898 | 0.918 | 0.431 | 5.58x | 48.0/64.9/72.0% | 3.7/12.1% | 3 |
| 2000 | 1 | 0.691 | 0.677 | 0.014 | - | - | 0.898 | 0.918 | 0.431 | 5.58x | 48.0/64.9/72.0% | 3.7/12.1% | 3 |

> warm-num-nodes=0: decode_failures 64

> warm-num-nodes=25: decode_failures 64

> warm-num-nodes=100: decode_failures 64

> warm-num-nodes=2000: decode_failures 64

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.1 | 1 | 0.593 | 0.578 | 0.015 | - | - | 0.866 | 0.886 | 0.000 | 1.31x | 12.3/20.6/22.7% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.488 | 0.472 | 0.016 | - | - | 0.741 | 0.835 | 0.000 | 1.19x | 11.2/19.0/20.7% | 1.9/4.3% | 3 |
| 0.3 | 1 | 0.388 | 0.363 | 0.025 | - | - | 0.641 | 0.713 | 0.000 | 1.06x | 10.2/17.3/18.9% | 1.6/3.8% | 3 |

> burst-loss=0.1: decode_failures 12

> burst-loss=0.2: decode_failures 31

> burst-loss=0.3: decode_failures 28

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.1 | 1 | 0.644 | 0.634 | 0.011 | - | - | 0.901 | 0.904 | 0.000 | 1.43x | 13.3/22.2/24.2% | 2.2/5.1% | 3 |
| 0.2 | 1 | 0.588 | 0.575 | 0.014 | - | - | 0.858 | 0.869 | 0.000 | 1.41x | 13.2/22.1/23.8% | 2.2/4.8% | 3 |
| 0.3 | 1 | 0.512 | 0.501 | 0.012 | - | - | 0.749 | 0.814 | 0.000 | 1.38x | 13.0/21.7/23.6% | 2.2/4.3% | 3 |

> extra-loss=0.1: decode_failures 1

> extra-loss=0.3: decode_failures 15

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.1 | 1 | 0.594 | 0.582 | 0.012 | - | - | 0.835 | 0.880 | 0.000 | 1.32x | 12.4/20.9/23.1% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.483 | 0.469 | 0.015 | - | - | 0.720 | 0.792 | 0.000 | 1.21x | 11.6/19.6/21.4% | 1.9/4.5% | 3 |
| 0.3 | 1 | 0.353 | 0.343 | 0.011 | - | - | 0.482 | 0.675 | 0.000 | 1.09x | 10.5/17.6/19.0% | 1.6/3.9% | 3 |

> burst-loss=0.1: decode_failures 17

> burst-loss=0.2: decode_failures 34

> burst-loss=0.3: decode_failures 20

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.641 | 0.641 | 0.000 | - | - | 0.890 | 0.902 | 0.000 | 1.76x | 16.2/27.2/29.4% | 2.8/6.7% | 3 |
| directed-with-late-flood | 1 | 0.649 | 0.649 | 0.000 | - | - | 0.860 | 0.910 | 0.000 | 1.62x | 15.1/25.6/27.5% | 2.6/6.4% | 3 |
| m4-early-flood | 1 | 0.663 | 0.663 | 0.000 | - | - | 0.887 | 0.915 | 0.000 | 1.65x | 15.3/25.6/27.9% | 2.6/6.6% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 12

> dm-mode=m4-early-flood: decode_failures 9

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.685 | 0.676 | 0.009 | - | - | 0.974 | 0.975 | 0.236 | 0.77x | 7.3/10.3/13.7% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.25 | 1 | 0.688 | 0.673 | 0.015 | - | - | 0.833 | 0.931 | 0.135 | 1.24x | 12.0/17.1/22.2% | 1.9/4.3% | 3 |
| 0.5 | 1 | 0.666 | 0.657 | 0.008 | - | - | 0.858 | 0.882 | 0.277 | 1.09x | 11.3/17.4/19.3% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.703 | 0.691 | 0.012 | - | - | 0.933 | 0.935 | 0.000 | 0.93x | 8.6/12.9/14.9% | 1.4/3.3% | 3 |

> legacy-fraction=0.25: decode_failures 19

> legacy-fraction=0.5: decode_failures 23

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.25 | 1 | 0.704 | 0.685 | 0.019 | - | - | 0.875 | 0.943 | 0.142 | 1.22x | 11.9/17.2/21.9% | 1.9/4.3% | 3 |
| 0.5 | 1 | 0.679 | 0.670 | 0.009 | - | - | 0.874 | 0.892 | 0.296 | 1.04x | 10.7/16.7/18.4% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.701 | 0.688 | 0.013 | - | - | 0.938 | 0.942 | 0.000 | 0.90x | 8.6/12.8/14.8% | 1.3/3.3% | 3 |

> legacy-fraction=0.25: decode_failures 30

> legacy-fraction=0.5: decode_failures 17

> slower: 4.97 s per simulated hour against 1.7 over 64 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.748 | 0.744 | 0.004 | - | - | 0.956 | 0.958 | 0.000 | 0.78x | 7.5/12.9/14.2% | 1.2/3.3% | 3 |
| signing=true | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.680 | 0.674 | 0.006 | - | - | 0.955 | 0.957 | 0.236 | 0.77x | 7.4/11.2/14.4% | 1.2/2.9% | 3 |
| 2.5 | 1 | 0.672 | 0.666 | 0.006 | - | - | 0.951 | 0.953 | 0.222 | 0.76x | 7.4/11.0/14.1% | 1.2/2.8% | 3 |
| 2.6 | 1 | 0.675 | 0.669 | 0.006 | - | - | 0.948 | 0.950 | 0.250 | 0.75x | 7.5/11.2/14.6% | 1.2/2.9% | 3 |
| 2.7 | 1 | 0.707 | 0.702 | 0.004 | - | - | 0.967 | 0.967 | 0.234 | 0.79x | 7.6/13.4/16.4% | 1.2/3.1% | 3 |
| 2.8 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.741 | 0.734 | 0.007 | - | - | 0.953 | 0.953 | 0.000 | 0.98x | 9.2/15.3/16.7% | 1.5/3.8% | 3 |
| 900 | 1 | 0.638 | 0.627 | 0.011 | - | - | 0.883 | 0.885 | 0.000 | 2.18x | 20.0/33.4/36.0% | 3.4/8.0% | 3 |
| 300 | 1 | 0.394 | 0.383 | 0.011 | - | - | 0.593 | 0.685 | 0.000 | 4.73x | 41.6/61.9/66.0% | 7.3/14.3% | 3 |

> broadcast-interval-s=300: decode_failures 19

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.829 | 0.827 | 0.003 | - | - | 0.972 | 0.973 | 0.000 | 1.08x | 10.0/15.6/16.8% | 1.7/3.7% | 3 |
| 900 | 1 | 0.749 | 0.744 | 0.006 | - | - | 0.931 | 0.935 | 0.000 | 2.48x | 22.9/36.0/38.3% | 4.1/8.3% | 3 |
| 300 | 1 | 0.516 | 0.505 | 0.012 | - | - | 0.760 | 0.832 | 0.000 | 5.21x | 45.7/66.9/69.6% | 8.7/15.1% | 3 |

> broadcast-interval-s=300: decode_failures 20

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.717 | 0.710 | 0.007 | - | - | 0.936 | 0.939 | 0.000 | 1.35x | 12.6/21.1/22.9% | 2.1/5.2% | 3 |
| sinusoid | 1 | 0.711 | 0.703 | 0.007 | - | - | 0.939 | 0.941 | 0.000 | 1.27x | 11.9/19.9/21.6% | 1.9/4.8% | 3 |
| commuter | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.638 | 0.627 | 0.011 | - | - | 0.883 | 0.885 | 0.000 | 2.18x | 20.0/33.4/36.0% | 3.4/8.0% | 3 |
| 3600 | 1 | 0.741 | 0.734 | 0.007 | - | - | 0.953 | 0.953 | 0.000 | 0.98x | 9.2/15.3/16.7% | 1.5/3.8% | 3 |
| 10800 | 1 | 0.755 | 0.750 | 0.005 | - | - | 0.958 | 0.959 | 0.000 | 0.64x | 5.9/10.0/11.0% | 1.0/2.6% | 3 |
| 43200 | 1 | 0.774 | 0.771 | 0.003 | - | - | 0.966 | 0.967 | 0.000 | 0.44x | 4.1/6.9/7.7% | 0.7/1.9% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.25 | 1 | 0.692 | 0.682 | 0.009 | - | - | 0.926 | 0.928 | 0.000 | 1.49x | 13.8/23.1/25.2% | 2.3/5.7% | 3 |
| 1.0 | 1 | 0.674 | 0.665 | 0.009 | - | - | 0.906 | 0.912 | 0.000 | 1.58x | 14.8/24.9/27.1% | 2.5/6.0% | 3 |
| 4.0 | 1 | 0.633 | 0.621 | 0.012 | - | - | 0.880 | 0.884 | 0.000 | 1.92x | 18.0/30.5/32.8% | 3.0/7.4% | 3 |

> traceroute-per-hour=4.0: decode_failures 1

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.677 | 0.014 | - | - | 0.898 | 0.918 | 0.431 | 5.58x | 48.0/64.9/72.0% | 3.7/12.1% | 3 |
| 1.0 | 1 | 0.628 | 0.612 | 0.016 | - | - | 0.832 | 0.879 | 0.385 | 6.33x | 54.1/69.0/76.5% | 4.3/13.6% | 3 |

> traceroute-per-hour=0.0: decode_failures 64

> traceroute-per-hour=1.0: decode_failures 48

> faster: 15.5 s per simulated hour against 36.9 over 64 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.386 | 0.367 | 0.020 | - | - | 0.695 | 0.726 | 0.000 | 0.85x | 8.0/17.9/21.9% | 1.9/5.4% | 3 |
| 60 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 90 | 1 | 0.852 | 0.848 | 0.004 | - | - | 0.968 | 0.969 | 0.605 | 1.81x | 15.3/25.2/28.1% | 1.7/5.0% | 3 |
| 120 | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.990 | 0.991 | 0.648 | 2.10x | 18.6/28.1/32.4% | 1.4/5.3% | 3 |
| 150 | 1 | 0.902 | 0.899 | 0.003 | - | - | 0.992 | 0.992 | 0.712 | 2.59x | 21.6/31.9/35.8% | 1.3/5.6% | 3 |

> nodes=40: decode_failures 12

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 120 | 1 | 0.463 | 0.447 | 0.016 | - | - | 0.634 | 0.637 | 0.082 | 2.39x | 11.1/19.1/24.7% | 1.8/4.9% | 3 |
| 250 | 1 | 0.296 | 0.290 | 0.006 | - | - | 0.522 | 0.538 | 0.092 | 4.60x | 13.0/20.0/25.9% | 1.6/5.5% | 3 |
| 500 | 1 | 0.188 | 0.183 | 0.005 | - | - | 0.470 | 0.479 | 0.000 | 9.46x | 12.2/22.2/34.2% | 1.7/6.2% | 3 |

> nodes=120: decode_failures 5

> nodes=250: decode_failures 50

> nodes=500: decode_failures 141

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.467 | 0.451 | 0.016 | - | - | 0.634 | 0.640 | 0.090 | 2.24x | 10.3/18.0/23.2% | 1.7/4.6% | 3 |
| 250 | 1 | 0.296 | 0.290 | 0.006 | - | - | 0.533 | 0.541 | 0.105 | 4.42x | 12.2/19.5/24.9% | 1.5/5.2% | 3 |
| 500 | 1 | 0.187 | 0.181 | 0.005 | - | - | 0.471 | 0.485 | 0.000 | 8.97x | 11.6/20.8/31.8% | 1.6/5.7% | 3 |

> nodes=250: decode_failures 55

> nodes=500: decode_failures 124

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.700 | 0.693 | 0.008 | - | - | 0.940 | 0.941 | 0.000 | 1.41x | 13.2/21.8/24.0% | 2.2/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.661 | 0.648 | 0.013 | - | - | 0.917 | 0.922 | 0.000 | 1.29x | 13.2/21.2/23.8% | 2.0/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.745 | 0.736 | 0.008 | - | - | 0.942 | 0.943 | 0.000 | 1.49x | 13.9/22.1/24.1% | 2.4/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.726 | 0.715 | 0.011 | - | - | 0.921 | 0.924 | 0.000 | 1.43x | 14.6/22.7/26.2% | 2.4/4.9% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.05 | 1 | 0.685 | 0.678 | 0.007 | - | - | 0.900 | 0.905 | 0.000 | 1.53x | 13.9/25.1/26.9% | 2.3/5.3% | 3 |
| 0.1 | 1 | 0.703 | 0.696 | 0.007 | - | - | 0.908 | 0.910 | 0.000 | 1.61x | 15.8/27.0/30.1% | 2.4/5.3% | 3 |
| 0.2 | 1 | 0.715 | 0.707 | 0.008 | - | - | 0.917 | 0.917 | 0.000 | 1.77x | 16.7/28.8/34.1% | 2.6/5.3% | 3 |

> router-late-fraction=0.2: decode_failures 1

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| local-typical | 1 | 0.509 | 0.498 | 0.012 | - | - | 0.720 | 0.769 | 0.000 | 1.34x | 11.0/22.7/28.8% | 2.0/5.6% | 3 |
| event | 1 | 0.143 | 0.135 | 0.008 | - | - | 0.327 | 0.355 | 0.000 | 1.00x | 5.1/10.0/19.4% | 1.7/3.7% | 3 |
| backbone | 1 | 0.956 | 0.953 | 0.002 | - | - | 1.000 | 1.000 | 0.683 | 1.32x | 21.3/33.5/36.5% | 1.9/5.6% | 3 |

> siting-mix=local-typical: decode_failures 13

> siting-mix=event: decode_failures 11

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.720 | 0.708 | 0.012 | - | - | 0.881 | 0.885 | 0.433 | 1.46x | 17.3/30.0/33.9% | 3.6/6.9% | 3 |
| 60 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 90 | 1 | 0.612 | 0.585 | 0.028 | - | - | 0.872 | 0.892 | 0.185 | 1.85x | 11.5/20.3/23.7% | 1.8/5.6% | 3 |
| 120 | 1 | 0.463 | 0.447 | 0.016 | - | - | 0.634 | 0.637 | 0.082 | 2.39x | 11.1/19.1/24.7% | 1.8/4.9% | 3 |
| 150 | 1 | 0.412 | 0.402 | 0.011 | - | - | 0.575 | 0.594 | 0.186 | 3.04x | 12.9/20.1/25.2% | 1.9/5.2% | 3 |

> nodes=90: decode_failures 51

> nodes=120: decode_failures 5

> nodes=150: decode_failures 84

> slower: 10.5 s per simulated hour against 3.38 over 64 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 1.25 | 1 | 0.361 | 0.350 | 0.011 | - | - | 0.516 | 0.552 | 0.000 | 1.41x | 9.8/15.6/22.3% | 2.3/4.6% | 3 |
| 1.5 | 1 | 0.178 | 0.170 | 0.008 | - | - | 0.374 | 0.385 | 0.000 | 1.22x | 6.8/12.7/15.6% | 2.0/4.2% | 3 |
| 2.0 | 1 | 0.065 | 0.065 | 0.000 | - | - | 0.085 | 0.115 | 0.000 | 0.56x | 2.1/4.5/7.3% | 0.7/2.2% | 3 |

> stretch=1.25: decode_failures 14

> stretch=1.5: decode_failures 1

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| clustered | 1 | 0.849 | 0.845 | 0.004 | - | - | 0.931 | 0.933 | 0.000 | 1.30x | 21.3/29.7/32.4% | 1.9/5.5% | 3 |
| corridor | 1 | 0.421 | 0.410 | 0.011 | - | - | 0.575 | 0.576 | 0.184 | 1.46x | 13.4/19.3/21.8% | 2.2/5.1% | 3 |
| hub | 1 | 0.895 | 0.895 | 0.000 | - | - | 0.951 | 0.951 | 0.732 | 1.27x | 24.0/35.8/37.4% | 1.8/5.4% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.649 | 0.649 | 0.000 | - | - | 0.860 | 0.910 | 0.000 | 1.62x | 15.1/25.6/27.5% | 2.6/6.4% | 3 |
| True | 1 | 0.660 | 0.660 | 0.000 | - | - | 0.892 | 0.909 | 0.000 | 1.65x | 15.4/25.6/28.1% | 2.6/6.6% | 3 |

> coding-rate-ladder=False: decode_failures 12

> coding-rate-ladder=True: decode_failures 1

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.660 | 0.660 | 0.000 | - | - | 0.892 | 0.909 | 0.000 | 1.65x | 15.4/25.6/28.1% | 2.6/6.6% | 3 |
| m4-early-flood | 1 | 0.663 | 0.663 | 0.000 | - | - | 0.871 | 0.915 | 0.000 | 1.64x | 15.2/25.5/27.7% | 2.6/6.5% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 1

> dm-mode=m4-early-flood: decode_failures 25

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.697 | 0.697 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.38x | 12.9/21.4/23.0% | 2.2/5.2% | 3 |
| chain | 1 | 0.667 | 0.665 | 0.002 | - | - | 0.813 | 0.908 | 0.000 | 1.61x | 15.2/24.8/27.1% | 2.6/6.1% | 3 |
| sr | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| True | 1 | 0.701 | 0.693 | 0.008 | - | - | 0.926 | 0.928 | 0.000 | 1.44x | 13.4/22.1/24.1% | 2.3/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.990 | 0.991 | 0.648 | 2.10x | 18.6/28.1/32.4% | 1.4/5.3% | 3 |
| True | 1 | 0.894 | 0.890 | 0.004 | - | - | 0.990 | 0.992 | 0.651 | 2.11x | 18.6/27.7/32.1% | 1.4/5.3% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.078 | 0.078 | 0.000 | - | - | 0.087 | 0.200 | 0.000 | 0.03x | 0.1/0.3/0.4% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.209 | 0.199 | 0.010 | - | - | 0.477 | 0.484 | 0.000 | 0.20x | 1.1/2.4/3.1% | 0.3/0.8% | 3 |
| LONG_TURBO | 1 | 0.547 | 0.537 | 0.010 | - | - | 0.802 | 0.817 | 0.000 | 1.34x | 9.9/16.7/21.4% | 2.2/4.7% | 3 |

> preset=SHORT_TURBO: decode_failures 1

> preset=MEDIUM_TURBO: decode_failures 2

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 0.25 | 1 | 0.724 | 0.711 | 0.013 | - | - | 0.930 | 0.931 | 0.102 | 1.34x | 14.6/22.8/25.1% | 2.0/5.4% | 3 |
| 1.0 | 1 | 0.827 | 0.812 | 0.015 | - | - | 0.961 | 0.961 | 0.386 | 1.02x | 18.2/23.8/26.0% | 1.3/5.0% | 3 |

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.128 | 0.125 | 0.003 | - | - | 0.247 | 0.248 | 0.000 | 0.09x | 0.5/0.9/1.1% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| LITE_FAST | 1 | 0.597 | 0.583 | 0.013 | - | - | 0.872 | 0.874 | 0.000 | 1.02x | 8.4/15.8/17.3% | 1.5/4.0% | 3 |
| NARROW_SLOW | 1 | 0.638 | 0.624 | 0.013 | - | - | 0.892 | 0.893 | 0.000 | 1.32x | 11.1/19.5/22.7% | 2.1/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| temporal | 1 | 0.542 | 0.531 | 0.012 | - | - | 0.819 | 0.846 | 0.000 | 1.37x | 12.4/21.3/23.0% | 2.1/5.1% | 3 |
| transient | 1 | 0.690 | 0.681 | 0.009 | - | - | 0.923 | 0.925 | 0.000 | 1.42x | 13.3/22.2/24.1% | 2.2/5.4% | 3 |
| periodic | 1 | 0.523 | 0.514 | 0.009 | - | - | 0.721 | 0.744 | 0.000 | 1.27x | 11.8/19.9/21.5% | 1.9/4.5% | 3 |

> noise-profile=temporal: decode_failures 18

> noise-profile=periodic: decode_failures 5

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.128 | 0.125 | 0.003 | - | - | 0.247 | 0.248 | 0.000 | 0.09x | 0.5/0.9/1.1% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| LONG_MODERATE | 1 | 0.721 | 0.704 | 0.017 | - | - | 0.916 | 0.926 | 0.431 | 3.45x | 40.8/53.0/57.7% | 5.4/12.3% | 3 |

> preset=LONG_MODERATE: decode_failures 4

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.031 | 0.031 | 0.000 | - | - | 0.155 | 0.158 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.078 | 0.078 | 0.000 | - | - | 0.087 | 0.200 | 0.000 | 0.03x | 0.1/0.3/0.4% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| LONG_TURBO | 1 | 0.547 | 0.537 | 0.010 | - | - | 0.802 | 0.817 | 0.000 | 1.34x | 9.9/16.7/21.4% | 2.2/4.7% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.684 | 0.669 | 0.015 | - | - | 0.890 | 0.893 | 0.000 | 1.97x | 16.9/27.0/30.8% | 3.1/7.1% | 3 |

> preset=SHORT_TURBO: decode_failures 1

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.642 | 0.633 | 0.009 | - | - | 0.863 | 0.866 | 0.000 | 1.37x | 13.0/21.6/23.4% | 2.1/5.0% | 3 |
| 10000 | 1 | 0.523 | 0.514 | 0.009 | - | - | 0.721 | 0.744 | 0.000 | 1.27x | 11.8/19.9/21.5% | 1.9/4.5% | 3 |
| 4000 | 1 | 0.278 | 0.275 | 0.003 | - | - | 0.355 | 0.463 | 0.000 | 1.04x | 9.9/16.4/17.6% | 1.6/3.3% | 3 |
| 2000 | 1 | 0.059 | 0.059 | 0.000 | - | - | 0.054 | 0.118 | 0.000 | 0.67x | 6.3/10.8/11.4% | 1.1/1.8% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 5

> noise-pulse-interval-ms=4000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.178 | 0.170 | 0.008 | - | - | 0.374 | 0.385 | 0.000 | 1.22x | 6.8/12.7/15.6% | 2.0/4.2% | 3 |
| 1.0 | 1 | 0.506 | 0.479 | 0.027 | - | - | 0.642 | 0.642 | 0.336 | 0.90x | 11.6/17.1/18.4% | 1.2/3.9% | 3 |

> duct-per-hour=0.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 22 | 1 | 0.177 | 0.169 | 0.008 | - | - | 0.367 | 0.374 | 0.000 | 1.24x | 6.9/12.6/15.8% | 2.1/4.1% | 3 |
| 17 | 1 | 0.073 | 0.073 | 0.000 | - | - | 0.081 | 0.189 | 0.000 | 0.62x | 2.6/5.2/7.7% | 0.9/2.4% | 3 |
| 14 | 1 | 0.047 | 0.047 | 0.000 | - | - | 0.067 | 0.074 | 0.000 | 0.46x | 1.5/3.3/6.7% | 0.6/2.1% | 3 |

> tx-power=17: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.990 | 0.991 | 0.648 | 2.10x | 18.6/28.1/32.4% | 1.4/5.3% | 3 |
| True | 1 | 0.887 | 0.883 | 0.004 | - | - | 0.988 | 0.988 | 0.621 | 2.39x | 21.0/30.4/35.3% | 1.7/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.707 | 0.701 | 0.006 | - | - | 0.924 | 0.928 | 0.000 | 1.48x | 13.9/23.8/25.9% | 2.2/5.3% | 3 |
| True | 1 | 0.761 | 0.756 | 0.005 | - | - | 0.920 | 0.920 | 0.000 | 1.60x | 15.2/24.2/26.3% | 2.6/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| random | 1 | 0.714 | 0.703 | 0.011 | - | - | 0.932 | 0.934 | 0.000 | 1.42x | 13.3/21.6/23.3% | 2.2/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.502 | 0.472 | 0.030 | - | - | 0.870 | 0.883 | 0.000 | 1.15x | 11.0/18.2/19.5% | 1.8/4.4% | 3 |
| 7 | 1 | 0.791 | 0.787 | 0.004 | - | - | 0.953 | 0.954 | 0.000 | 1.57x | 14.6/23.0/24.9% | 2.6/5.4% | 3 |
| 15 | 1 | 0.848 | 0.845 | 0.003 | - | - | 0.947 | 0.947 | 0.000 | 1.62x | 14.9/23.2/24.9% | 2.6/5.3% | 3 |
| 32 | 1 | 0.853 | 0.851 | 0.002 | - | - | 0.948 | 0.948 | 0.000 | 1.63x | 15.1/23.2/25.1% | 2.7/5.4% | 3 |

> hop-limit=3: decode_failures 11

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.502 | 0.472 | 0.030 | - | - | 0.870 | 0.883 | 0.000 | 1.15x | 11.0/18.2/19.5% | 1.8/4.4% | 3 |
| 5 | 1 | 0.692 | 0.683 | 0.010 | - | - | 0.954 | 0.957 | 0.000 | 1.39x | 13.0/21.8/23.5% | 2.2/5.2% | 3 |
| 7 | 1 | 0.791 | 0.787 | 0.004 | - | - | 0.953 | 0.954 | 0.000 | 1.57x | 14.6/23.0/24.9% | 2.6/5.4% | 3 |

> hop-limit=3: decode_failures 11

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.687 | 0.687 | 0.000 | - | - | 0.818 | 0.929 | 0.000 | 1.39x | 13.0/21.8/23.2% | 2.2/5.2% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 3

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.502 | 0.472 | 0.030 | - | - | 0.870 | 0.883 | 0.000 | 1.15x | 11.0/18.2/19.5% | 1.8/4.4% | 3 |
| True | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

> hop-spread=False: decode_failures 11

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| BALANCED | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| STRICT | 1 | 0.559 | 0.559 | 0.000 | - | - | 0.773 | 0.779 | 0.000 | 1.51x | 14.2/23.5/25.4% | 2.4/5.6% | 3 |

> signature-policy=STRICT: decode_failures 1

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| dm | 1 | 0.691 | 0.681 | 0.010 | - | - | 0.923 | 0.925 | 0.000 | 1.41x | 13.1/22.0/24.3% | 2.2/5.6% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.692 | 0.685 | 0.007 | - | - | 0.912 | 0.916 | 0.000 | 1.43x | 13.3/22.2/24.1% | 2.2/5.3% | 3 |
| local | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| time | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.915 | 0.923 | 0.000 | 1.44x | 13.5/22.5/24.4% | 2.3/5.5% | 3 |
| window | 1 | 0.695 | 0.686 | 0.009 | - | - | 0.923 | 0.926 | 0.000 | 1.43x | 13.3/22.2/24.2% | 2.2/5.4% | 3 |

> bucket-mode=global: misdecodes 21

> bucket-mode=time: misdecodes 13

> bucket-mode=window: misdecodes 9

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.688 | 0.678 | 0.010 | - | - | 0.920 | 0.925 | 0.000 | 1.57x | 14.6/24.3/26.5% | 2.5/6.2% | 3 |
| 1800 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.915 | 0.923 | 0.000 | 1.44x | 13.5/22.5/24.4% | 2.3/5.5% | 3 |
| 3600 | 1 | 0.687 | 0.681 | 0.007 | - | - | 0.912 | 0.919 | 0.000 | 1.44x | 13.4/22.4/24.2% | 2.2/5.3% | 3 |

> time-bucket-s=600: misdecodes 106

> time-bucket-s=1800: misdecodes 13

> time-bucket-s=3600: misdecodes 4

> time-bucket-s=3600: decode_failures 1

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| interval | 1 | 0.655 | 0.644 | 0.012 | - | - | 0.891 | 0.898 | 0.000 | 1.86x | 17.3/29.0/32.6% | 3.0/8.4% | 3 |
| aimd | 1 | 0.679 | 0.675 | 0.004 | - | - | 0.843 | 0.914 | 0.000 | 1.43x | 13.4/22.3/24.1% | 2.3/5.4% | 3 |
| bucket+interval | 1 | 0.658 | 0.645 | 0.013 | - | - | 0.904 | 0.908 | 0.000 | 1.89x | 17.6/29.2/32.8% | 3.0/8.3% | 3 |

> trigger=interval: misdecodes 12

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 13

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.690 | 0.682 | 0.008 | - | - | 0.909 | 0.931 | 0.000 | 1.42x | 13.3/22.2/24.5% | 2.2/5.6% | 3 |
| 8 | 1 | 0.686 | 0.678 | 0.008 | - | - | 0.903 | 0.916 | 0.000 | 1.41x | 13.1/21.8/24.2% | 2.2/5.5% | 3 |
| 16 | 1 | 0.689 | 0.680 | 0.009 | - | - | 0.909 | 0.913 | 0.000 | 1.40x | 13.1/21.9/23.8% | 2.2/5.3% | 3 |
| 32 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 50 | 1 | 0.699 | 0.691 | 0.008 | - | - | 0.931 | 0.935 | 0.000 | 1.43x | 13.4/22.4/24.4% | 2.2/5.5% | 3 |

> capacity=4: decode_failures 90

> capacity=8: decode_failures 84

> capacity=16: decode_failures 2

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.690 | 0.682 | 0.008 | - | - | 0.909 | 0.931 | 0.000 | 1.42x | 13.3/22.2/24.5% | 2.2/5.6% | 3 |
| 8 | 1 | 0.686 | 0.678 | 0.008 | - | - | 0.903 | 0.916 | 0.000 | 1.41x | 13.1/21.8/24.2% | 2.2/5.5% | 3 |
| 16 | 1 | 0.689 | 0.680 | 0.009 | - | - | 0.909 | 0.913 | 0.000 | 1.40x | 13.1/21.9/23.8% | 2.2/5.3% | 3 |
| 32 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 50 | 1 | 0.699 | 0.691 | 0.008 | - | - | 0.931 | 0.935 | 0.000 | 1.43x | 13.4/22.4/24.4% | 2.2/5.5% | 3 |

> capacity=4: decode_failures 90

> capacity=8: decode_failures 84

> capacity=16: decode_failures 2

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.680 | 0.675 | 0.004 | - | - | 0.855 | 0.913 | 0.000 | 1.41x | 13.1/21.9/23.6% | 2.2/5.3% | 3 |
| 16 | 1 | 0.695 | 0.685 | 0.009 | - | - | 0.923 | 0.931 | 0.000 | 1.42x | 13.3/22.1/24.1% | 2.2/5.4% | 3 |
| 32 | 1 | 0.695 | 0.686 | 0.009 | - | - | 0.923 | 0.926 | 0.000 | 1.43x | 13.3/22.2/24.2% | 2.2/5.4% | 3 |

> capacity=8: misdecodes 5

> capacity=8: decode_failures 84

> capacity=16: misdecodes 13

> capacity=16: decode_failures 10

> capacity=32: misdecodes 9

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.658 | 0.645 | 0.013 | - | - | 0.904 | 0.908 | 0.000 | 1.89x | 17.6/29.2/32.8% | 3.0/8.3% | 3 |
| 02-06 | 1 | 0.695 | 0.691 | 0.005 | - | - | 0.872 | 0.925 | 0.000 | 1.45x | 13.6/22.6/24.9% | 2.3/5.8% | 3 |
| 00-08 | 1 | 0.690 | 0.685 | 0.005 | - | - | 0.874 | 0.925 | 0.000 | 1.52x | 14.1/23.9/26.4% | 2.4/6.5% | 3 |

> catch-up-hours=: misdecodes 13

> catch-up-hours=02-06: decode_failures 41

> catch-up-hours=00-08: decode_failures 41

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.685 | 0.682 | 0.002 | - | - | 0.817 | 0.818 | 0.000 | 1.43x | 13.2/22.0/23.7% | 2.2/5.4% | 3 |
| 2 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 3 | 1 | 0.723 | 0.693 | 0.030 | - | - | 0.858 | 0.916 | 0.000 | 1.45x | 13.6/22.6/24.2% | 2.2/5.4% | 3 |
| 4 | 1 | 0.725 | 0.682 | 0.043 | - | - | 0.865 | 0.916 | 0.000 | 1.43x | 13.4/22.2/23.8% | 2.2/5.4% | 3 |

> hops-apart=3: decode_failures 31

> hops-apart=4: decode_failures 29

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.685 | 0.682 | 0.002 | - | - | 0.817 | 0.818 | 0.000 | 1.43x | 13.2/22.0/23.7% | 2.2/5.4% | 3 |
| 2 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 3 | 1 | 0.723 | 0.693 | 0.030 | - | - | 0.858 | 0.916 | 0.000 | 1.45x | 13.6/22.6/24.2% | 2.2/5.4% | 3 |
| 4 | 1 | 0.725 | 0.682 | 0.043 | - | - | 0.865 | 0.916 | 0.000 | 1.43x | 13.4/22.2/23.8% | 2.2/5.4% | 3 |
| 5 | 1 | 0.694 | 0.683 | 0.012 | - | - | 0.596 | 0.922 | 0.000 | 1.40x | 13.1/21.8/23.3% | 2.2/5.3% | 3 |

> hops-apart=3: decode_failures 31

> hops-apart=4: decode_failures 29

> hops-apart=5: decode_failures 15

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.686 | 0.677 | 0.009 | - | - | 0.916 | 0.921 | 0.000 | 1.43x | 13.3/22.1/24.2% | 2.3/5.4% | 3 |
| 30 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 120 | 1 | 0.690 | 0.682 | 0.009 | - | - | 0.921 | 0.922 | 0.000 | 1.44x | 13.4/22.3/24.4% | 2.3/5.4% | 3 |
| 600 | 1 | 0.689 | 0.682 | 0.007 | - | - | 0.909 | 0.913 | 0.000 | 1.42x | 13.2/22.0/24.0% | 2.2/5.3% | 3 |

> advert-jitter-s=1: decode_failures 1

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.686 | 0.677 | 0.009 | - | - | 0.916 | 0.921 | 0.000 | 1.43x | 13.3/22.1/24.2% | 2.3/5.4% | 3 |
| 30 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 120 | 1 | 0.690 | 0.682 | 0.009 | - | - | 0.921 | 0.922 | 0.000 | 1.44x | 13.4/22.3/24.4% | 2.3/5.4% | 3 |
| 600 | 1 | 0.689 | 0.682 | 0.007 | - | - | 0.909 | 0.913 | 0.000 | 1.42x | 13.2/22.0/24.0% | 2.2/5.3% | 3 |

> advert-jitter-s=1: decode_failures 1

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.701 | 0.680 | 0.022 | - | - | 0.671 | 0.893 | 0.000 | 1.42x | 13.2/21.8/23.7% | 2.2/5.3% | 3 |
| routers | 1 | 0.690 | 0.678 | 0.012 | - | - | 0.916 | 0.918 | 0.000 | 1.42x | 13.3/22.2/23.9% | 2.3/5.6% | 3 |
| alternate-routers | 1 | 0.694 | 0.685 | 0.009 | - | - | 0.929 | 0.934 | 0.000 | 1.42x | 13.1/22.2/24.0% | 2.2/5.5% | 3 |
| beside-router | 1 | 0.691 | 0.674 | 0.017 | - | - | 0.919 | 0.919 | 0.000 | 1.42x | 13.2/22.3/23.9% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.704 | 0.688 | 0.017 | - | - | 0.550 | 0.849 | 0.000 | 1.41x | 13.3/21.7/23.2% | 2.2/5.3% | 3 |
| hops-apart | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

> place=spread: decode_failures 8

> place=random-clients: decode_failures 18

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.701 | 0.680 | 0.022 | - | - | 0.671 | 0.893 | 0.000 | 1.42x | 13.2/21.8/23.7% | 2.2/5.3% | 3 |
| routers | 1 | 0.690 | 0.678 | 0.012 | - | - | 0.916 | 0.918 | 0.000 | 1.42x | 13.3/22.2/23.9% | 2.3/5.6% | 3 |
| alternate-routers | 1 | 0.694 | 0.685 | 0.009 | - | - | 0.929 | 0.934 | 0.000 | 1.42x | 13.1/22.2/24.0% | 2.2/5.5% | 3 |
| beside-router | 1 | 0.691 | 0.674 | 0.017 | - | - | 0.919 | 0.919 | 0.000 | 1.42x | 13.2/22.3/23.9% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.704 | 0.688 | 0.017 | - | - | 0.550 | 0.849 | 0.000 | 1.41x | 13.3/21.7/23.2% | 2.2/5.3% | 3 |
| hops-apart | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

> place=spread: decode_failures 8

> place=random-clients: decode_failures 18

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| broadcast | 1 | 0.755 | 0.675 | 0.081 | - | - | 0.913 | 0.918 | 0.000 | 1.55x | 14.4/24.1/25.7% | 2.4/5.7% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| heard | 1 | 0.687 | 0.679 | 0.008 | - | - | 0.921 | 0.924 | 0.000 | 1.42x | 13.2/22.1/24.0% | 2.2/5.4% | 3 |

> replay-ordering=heard: misdecodes 8

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.755 | 0.675 | 0.081 | - | - | 0.913 | 0.918 | 0.000 | 1.55x | 14.4/24.1/25.7% | 2.4/5.7% | 3 |
| heard | 1 | 0.753 | 0.672 | 0.081 | - | - | 0.906 | 0.915 | 0.000 | 1.55x | 14.3/24.0/25.6% | 2.5/5.8% | 3 |

> replay-ordering=heard: misdecodes 3

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| enum | 1 | 0.701 | 0.693 | 0.008 | - | - | 0.917 | 0.928 | 0.000 | 1.41x | 13.2/22.0/24.3% | 2.2/5.6% | 3 |
| hybrid | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.690 | 0.678 | 0.012 | - | - | 0.916 | 0.918 | 0.000 | 1.42x | 13.3/22.2/23.9% | 2.3/5.6% | 3 |
| 6 | 1 | 0.688 | 0.670 | 0.018 | - | - | 0.918 | 0.919 | 0.000 | 1.44x | 13.4/22.8/24.5% | 2.2/5.7% | 6 |

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.695 | 0.687 | 0.007 | - | - | 0.870 | 0.917 | 0.000 | 1.40x | 13.1/21.8/23.7% | 2.2/5.2% | 2 |
| 3 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 5 | 1 | 0.692 | 0.678 | 0.014 | - | - | 0.933 | 0.937 | 0.000 | 1.47x | 13.6/22.6/24.8% | 2.3/5.6% | 5 |
| 8 | 1 | 0.695 | 0.675 | 0.020 | - | - | 0.941 | 0.942 | 0.000 | 1.49x | 13.7/23.0/25.1% | 2.3/5.5% | 8 |

> servers=2: decode_failures 8

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.695 | 0.687 | 0.007 | - | - | 0.870 | 0.917 | 0.000 | 1.40x | 13.1/21.8/23.7% | 2.2/5.2% | 2 |
| 3 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 5 | 1 | 0.692 | 0.678 | 0.014 | - | - | 0.933 | 0.937 | 0.000 | 1.47x | 13.6/22.6/24.8% | 2.3/5.6% | 5 |
| 8 | 1 | 0.695 | 0.675 | 0.020 | - | - | 0.941 | 0.942 | 0.000 | 1.49x | 13.7/23.0/25.1% | 2.3/5.5% | 8 |

> servers=2: decode_failures 8

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| True | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.693 | 0.686 | 0.008 | - | - | 0.904 | 0.926 | 0.000 | 1.34x | 12.6/21.0/22.7% | 2.1/5.0% | 3 |
| 1 | 1 | 0.699 | 0.691 | 0.008 | - | - | 0.935 | 0.940 | 0.000 | 1.36x | 12.7/21.4/23.0% | 2.1/5.0% | 3 |
| 2 | 1 | 0.709 | 0.701 | 0.008 | - | - | 0.942 | 0.947 | 0.000 | 1.34x | 12.6/20.9/22.5% | 2.1/4.9% | 3 |
| 4 | 1 | 0.701 | 0.694 | 0.007 | - | - | 0.940 | 0.943 | 0.000 | 1.35x | 12.6/21.2/22.8% | 2.1/5.0% | 3 |

> sr-retries=0: decode_failures 8

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.690 | 0.682 | 0.008 | - | - | 0.920 | 0.923 | 0.000 | 1.41x | 13.2/22.0/24.0% | 2.2/5.3% | 3 |
| 24 | 1 | 0.694 | 0.685 | 0.009 | - | - | 0.927 | 0.928 | 0.000 | 1.42x | 13.3/22.1/24.3% | 2.2/5.4% | 3 |
| 32 | 1 | 0.691 | 0.683 | 0.009 | - | - | 0.919 | 0.919 | 0.000 | 1.44x | 13.4/22.3/24.3% | 2.2/5.4% | 3 |
| 64 | 1 | 0.680 | 0.670 | 0.011 | - | - | 0.914 | 0.914 | 0.000 | 1.44x | 13.4/22.4/24.2% | 2.3/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.692 | 0.683 | 0.009 | - | - | 0.918 | 0.924 | 0.000 | 1.51x | 14.1/23.1/25.4% | 2.4/5.7% | 3 |
| 16 | 1 | 0.693 | 0.684 | 0.009 | - | - | 0.924 | 0.927 | 0.000 | 1.47x | 13.6/22.6/24.7% | 2.3/5.5% | 3 |
| 32 | 1 | 0.695 | 0.686 | 0.009 | - | - | 0.923 | 0.926 | 0.000 | 1.43x | 13.3/22.2/24.2% | 2.2/5.4% | 3 |

> window-size=8: misdecodes 116

> window-size=16: misdecodes 47

> window-size=32: misdecodes 9

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.990 | 0.991 | 0.648 | 2.10x | 18.6/28.1/32.4% | 1.4/5.3% | 3 |
| True | 1 | 0.689 | 0.673 | 0.016 | - | - | 0.897 | 0.915 | 0.423 | 5.67x | 48.9/65.4/72.6% | 3.8/12.2% | 3 |

> no-congestion-scaling=True: decode_failures 75

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.296 | 0.290 | 0.006 | - | - | 0.533 | 0.541 | 0.105 | 4.42x | 12.2/19.5/24.9% | 1.5/5.2% | 3 |
| truesize | 1 | 0.328 | 0.322 | 0.006 | - | - | 0.583 | 0.593 | 0.100 | 2.41x | 6.6/11.0/14.9% | 0.8/3.4% | 3 |

> congestion-input=hotstore: decode_failures 55

> congestion-input=truesize: decode_failures 45

> slower: 21.7 s per simulated hour against 10.2 over 64 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.897 | 0.893 | 0.003 | - | - | 0.993 | 0.994 | 0.646 | 2.03x | 18.0/26.4/31.1% | 1.4/5.0% | 3 |
| adaptive | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.990 | 0.991 | 0.648 | 2.10x | 18.6/28.1/32.4% | 1.4/5.3% | 3 |

