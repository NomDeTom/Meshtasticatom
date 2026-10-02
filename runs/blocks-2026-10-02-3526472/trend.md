# Sweep blocks-2026-10-02-3526472

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 3526472 · seeds 3526472
- **blocks** 87 run
- **compute** 10.4 h of simulator time across every cell
- **generated** 2026-10-02T09:51:39+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>101 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 4
- AD-amplify-worst: amplify-worst=0.3: decode_failures 1
- AD-badrouters: role-placement=random: decode_failures 21
- AD-siting: siting-mix=basement-heavy: decode_failures 1
- BL-control: protocol=sr: decode_failures 31
- BL-control: slower: 6.07 s per simulated hour against 1.93 over 42 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 8
- DB-hotstore-stress: max-num-nodes=10: decode_failures 58
- DB-platform: platform-mix=constrained: decode_failures 8
- DB-warm: warm-num-nodes=0: decode_failures 81
- DB-warm: warm-num-nodes=25: decode_failures 81
- DB-warm: warm-num-nodes=100: decode_failures 81
- DB-warm: warm-num-nodes=2000: decode_failures 81
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 27
- DG-burst: burst-loss=0.3: decode_failures 19
- DG-loss: extra-loss=0.1: decode_failures 9
- DG-loss: extra-loss=0.2: decode_failures 19
- DG-loss: extra-loss=0.3: decode_failures 15
- DG-outage: burst-loss=0.1: decode_failures 4
- DG-outage: burst-loss=0.2: decode_failures 25
- DG-outage: burst-loss=0.3: decode_failures 17
- DM-mode: dm-mode=flood-only: decode_failures 19
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 1
- DM-mode: dm-mode=m4-early-flood: decode_failures 15
- LD-chatty-hops: broadcast-interval-s=900: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 2
- LD-chatty: broadcast-interval-s=900: decode_failures 1
- LD-chatty: broadcast-interval-s=300: decode_failures 1
- LD-interval: broadcast-interval-s=900: decode_failures 1
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 25
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 81
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 10.0% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 64
- MS-hopscale: nodes=250: decode_failures 26
- MS-hopscale: nodes=500: decode_failures 7
- MS-oversubscribed: nodes=500: decode_failures 20
- MS-size: nodes=150: decode_failures 2
- MS-stretch: stretch=1.5: decode_failures 9
- MS-stretch: stretch=2.0: decode_failures 3
- PR-crladder: coding-rate-ladder=False: decode_failures 1
- PR-crladder: coding-rate-ladder=True: decode_failures 22
- PR-crladder: slower: 5.73 s per simulated hour against 2.79 over 42 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 22
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 8
- PR-dmmode-cr: slower: 6.58 s per simulated hour against 2.79 over 42 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-noise: noise-profile=temporal: decode_failures 6
- RF-noise: noise-profile=transient: decode_failures 2
- RF-noise: noise-profile=periodic: decode_failures 2
- RF-preset: preset=LONG_MODERATE: decode_failures 11
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 1
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 9
- RT-hoplimit: hop-limit=3: decode_failures 1
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SC-signing: signature-policy=STRICT: decode_failures 26
- SF-bucket-mode: bucket-mode=global: misdecodes 19
- SF-bucket-mode: bucket-mode=time: misdecodes 22
- SF-bucket-mode: bucket-mode=window: misdecodes 12
- SF-bucket-time: time-bucket-s=600: misdecodes 89
- SF-bucket-time: time-bucket-s=1800: misdecodes 22
- SF-bucket-time: time-bucket-s=3600: misdecodes 4
- SF-bucket-time: time-bucket-s=3600: decode_failures 1
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 8
- SF-cadence: trigger=bucket+interval: misdecodes 19
- SF-capacity-local: capacity=4: decode_failures 87
- SF-capacity-local: capacity=8: decode_failures 75
- SF-capacity-local: capacity=16: decode_failures 33
- SF-capacity: capacity=4: decode_failures 87
- SF-capacity: capacity=8: decode_failures 75
- SF-capacity: capacity=16: decode_failures 33
- SF-capacity-window: capacity=8: misdecodes 13
- SF-capacity-window: capacity=8: decode_failures 52
- SF-capacity-window: capacity=16: misdecodes 8
- SF-capacity-window: capacity=16: decode_failures 3
- SF-capacity-window: capacity=32: misdecodes 12
- SF-catchup: catch-up-hours=: misdecodes 19
- SF-catchup: catch-up-hours=02-06: decode_failures 35
- SF-catchup: catch-up-hours=00-08: decode_failures 31
- SF-hops-flat: hops-apart=3: decode_failures 31
- SF-hops-flat: hops-apart=4: decode_failures 31
- SF-hops-spread: hops-apart=3: decode_failures 31
- SF-hops-spread: hops-apart=4: decode_failures 31
- SF-hops-spread: hops-apart=5: decode_failures 31
- SF-jitter-global: advert-jitter-s=1: decode_failures 9
- SF-jitter-local: advert-jitter-s=1: decode_failures 9
- SF-place-flat: place=spread: decode_failures 14
- SF-place-flat: place=random-clients: decode_failures 25
- SF-place-spread: place=spread: decode_failures 14
- SF-place-spread: place=random-clients: decode_failures 25
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 2
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 21
- SF-replay-order-broadcast: slower: 4.02 s per simulated hour against 1.75 over 42 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=heard: misdecodes 10
- SF-window-size: window-size=8: misdecodes 128
- SF-window-size: window-size=16: misdecodes 44
- SF-window-size: window-size=32: misdecodes 12
- TH-congestion: no-congestion-scaling=True: decode_failures 43

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 6.07 | 1.93 | 3.15x | 42 |
| `PR-dmmode-cr` | 6.58 | 2.79 | 2.35x | 42 |
| `SF-replay-order-broadcast` | 4.02 | 1.75 | 2.30x | 42 |
| `PR-crladder` | 5.73 | 2.79 | 2.05x | 42 |
| `SC-signing` | 3.52 | 1.81 | 1.94x | 42 |
| `AD-badrouters` | 3.8 | 2.05 | 1.85x | 42 |
| `DG-loss` | 3.8 | 2.28 | 1.67x | 42 |
| `RF-stretch-duct` | 3.02 | 1.82 | 1.66x | 42 |
| `RT-favourites` | 1.1 | 1.66 | 0.66x | 42 |
| `SF-width` | 1.13 | 1.7 | 0.66x | 42 |
| `LD-chatty-hops` | 2.76 | 4.28 | 0.65x | 42 |
| `AD-amplifiers` | 1.02 | 1.64 | 0.62x | 42 |
| `LD-chatty` | 3.16 | 5.09 | 0.62x | 42 |
| `RF-bw500` | 1.12 | 1.81 | 0.62x | 42 |
| `SF-servers-allrouters` | 0.94 | 1.85 | 0.51x | 42 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.875 | 0.875 | 0.661 → 0.673 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.867 | 0.867 | 0.661 → 0.671 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.028 → 0.867 | 0.839 | 0.083 → 0.671 | 60x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.082 → 0.822 | 0.739 | 0.045 → 0.571 | 16x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.228 → 0.951 | 0.723 | 0.222 → 0.948 | 3.3x sr_airtime | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.088 → 0.802 | 0.714 | 0.076 → 0.615 | 1.4e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.192 → 0.867 | 0.675 | 0.067 → 0.671 | 4.7x advert_bytes | up | 5 |
| `MS-stretch` | stretch | **text** | 0.140 → 0.679 | 0.539 | 0.139 → 0.671 | 2.5x sr_airtime | down | 4 |
| `RF-preset` | preset | **text** | 0.224 → 0.736 | 0.512 | 0.216 → 0.718 | 2.2x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.481 → 0.955 | 0.474 | 0.477 → 0.955 | 2x sr_airtime | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.224 → 0.679 | 0.456 | 0.216 → 0.671 | 1.9x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **held** | 0.488 → 0.919 | 0.431 | 0.332 → 0.687 | 9.2x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.488 → 0.919 | 0.430 | 0.332 → 0.695 | 4.7x sr_bytes | down | 3 |
| `MS-density` | nodes | **text** | 0.515 → 0.944 | 0.429 | 0.507 → 0.941 | 5.9x sr_airtime | up | 5 |
| `RF-bw500` | preset | **text** | 0.111 → 0.537 | 0.426 | 0.111 → 0.524 | 3.2x sr_bytes | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.307 → 0.700 | 0.393 | 0.298 → 0.689 | 2.3x sr_airtime | up | 2 |
| `SF-place-flat` | place | **held** | 0.513 → 0.867 | 0.355 | 0.661 → 0.679 | 2.7x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.513 → 0.867 | 0.355 | 0.661 → 0.679 | 2.7x sr_bytes | up | 6 |
| `DG-outage` | burst-loss | **held** | 0.521 → 0.867 | 0.346 | 0.350 → 0.671 | 1.7x advert_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.535 → 0.856 | 0.320 | 0.430 → 0.744 | 13x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.490 → 0.789 | 0.300 | 0.454 → 0.784 | 1.8x sr_bytes | up | 4 |
| `DG-burst` | burst-loss | **text** | 0.384 → 0.679 | 0.295 | 0.361 → 0.671 | 1.7x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.530 → 0.811 | 0.281 | 0.306 → 0.486 | 5.2x sr_airtime | up | 3 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.616 → 0.891 | 0.275 | 0.442 → 0.713 | 10x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.679 → 0.926 | 0.247 | 0.671 → 0.924 | 1.7x sr_bytes | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.490 → 0.729 | 0.239 | 0.454 → 0.717 | 1.4x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.674 → 0.893 | 0.219 | 0.671 → 0.828 | 1.7x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.665 → 0.867 | 0.202 | 0.498 → 0.671 | 1.7x sr_bytes | down | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.727 → 0.925 | 0.198 | 0.708 → 0.920 | 3.8x sr_airtime | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.589 → 0.786 | 0.197 | 0.571 → 0.777 | 2.1x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.589 → 0.786 | 0.197 | 0.571 → 0.777 | 2.1x bytes_on_air | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.679 → 0.874 | 0.194 | 0.671 → 0.863 | 1.3x sr_airtime | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.490 → 0.679 | 0.190 | 0.454 → 0.671 | 1.5x sr_bytes | up | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.679 → 0.839 | 0.160 | 0.671 → 0.830 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.679 → 0.828 | 0.149 | 0.671 → 0.815 | 2x bytes_on_air | up | 4 |
| `DG-loss` | extra-loss | **text** | 0.532 → 0.679 | 0.147 | 0.521 → 0.671 | 1.3x sr_bytes | down | 4 |
| `AD-badrouters` | role-placement | **held** | 0.682 → 0.822 | 0.139 | 0.498 → 0.580 | 1.3x sr_bytes | down | 3 |
| `MS-size` | nodes | **held** | 0.803 → 0.937 | 0.135 | 0.604 → 0.736 | 5.1x sr_bytes | down | 5 |
| `SC-signing` | signature-policy | **held** | 0.733 → 0.867 | 0.134 | 0.571 → 0.671 | 1.4x sr_airtime | down | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.747 → 0.875 | 0.129 | 0.666 → 0.673 | 3.4x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.747 → 0.875 | 0.129 | 0.661 → 0.673 | 3.4x sr_bytes | down | 5 |
| `MS-roles` | role-mix | **text** | 0.589 → 0.703 | 0.114 | 0.571 → 0.692 | 1.2x sr_bytes | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.611 → 0.716 | 0.105 | 0.599 → 0.708 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.612 → 0.716 | 0.104 | 0.603 → 0.708 | 2.1x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.772 → 0.867 | 0.095 | 0.671 → 0.676 | 30x sr_airtime | down | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.619 → 0.712 | 0.092 | 0.606 → 0.702 | 1.1x bytes_on_air | down | 2 |
| `FW-versions` | profile | **text** | 0.679 → 0.767 | 0.087 | 0.671 → 0.760 | 3.6x bytes_on_air | down | 5 |
| `LD-interval` | broadcast-interval-s | **text** | 0.653 → 0.740 | 0.086 | 0.642 → 0.733 | 5.9x sr_airtime | up | 4 |
| `FW-firmware` | profile | **text** | 0.679 → 0.747 | 0.068 | 0.671 → 0.736 | 3.5x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.803 → 0.867 | 0.065 | 0.644 → 0.671 | 15x advert_bytes | down | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.817 → 0.878 | 0.061 | 0.640 → 0.699 | 1.3x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.679 → 0.734 | 0.054 | 0.671 → 0.726 | 3.2x bytes_on_air | down | 2 |
| `DM-mode` | dm-mode | **held** | 0.785 → 0.837 | 0.052 | 0.637 → 0.656 | 1.3x sr_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.679 → 0.727 | 0.048 | 0.671 → 0.719 | 1.3x bytes_on_air | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.832 → 0.876 | 0.044 | 0.671 → 0.680 | 1.9x advert_bytes | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.645 → 0.680 | 0.035 | 0.634 → 0.671 | 1.4x sr_airtime | down | 4 |
| `SF-provide-transport` | provide-transport | **held** | 0.833 → 0.867 | 0.034 | 0.654 → 0.671 | 3x sr_airtime | down | 2 |
| `SF-capacity` | capacity | **held** | 0.847 → 0.878 | 0.032 | 0.670 → 0.683 | 5.5x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.847 → 0.878 | 0.032 | 0.670 → 0.683 | 5.5x advert_bytes | up | 5 |
| `RT-favourites` | favourite-routers | **text** | 0.694 → 0.725 | 0.030 | 0.685 → 0.716 | 1.1x sr_bytes | up | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.838 → 0.867 | 0.029 | 0.638 → 0.671 | 1.1x advert_bytes | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.679 → 0.708 | 0.028 | 0.671 → 0.700 | 1.2x sr_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.834 → 0.860 | 0.026 | 0.660 → 0.684 | 1.2x sr_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.679 → 0.704 | 0.024 | 0.671 → 0.693 | 1.1x sr_airtime | up | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.498 → 0.521 | 0.023 | 0.486 → 0.511 | 1.5x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.791 → 0.813 | 0.022 | 0.779 → 0.806 | 1.3x sr_bytes | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.663 → 0.684 | 0.021 | 0.653 → 0.679 | 9.1x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.851 → 0.870 | 0.019 | 0.669 → 0.678 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.851 → 0.870 | 0.019 | 0.669 → 0.678 | 1.2x sr_airtime | up | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.857 → 0.876 | 0.019 | 0.671 → 0.681 | 3.5x advert_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.857 → 0.876 | 0.019 | 0.669 → 0.680 | 5.7x advert_bytes | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.860 → 0.878 | 0.018 | 0.669 → 0.678 | 6.2x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.860 → 0.878 | 0.018 | 0.669 → 0.678 | 6.2x sr_bytes | up | 4 |
| `SF-width` | short-id-bits | **text** | 0.679 → 0.692 | 0.013 | 0.671 → 0.683 | 3.1x advert_bytes | up | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.818 → 0.830 | 0.012 | 0.654 → 0.665 | 1.1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.913 → 0.925 | 0.012 | 0.907 → 0.920 | 1.2x bytes_on_air | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.847 → 0.857 | 0.011 | 0.667 → 0.671 | 2.7x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.673 → 0.683 | 0.010 | 0.662 → 0.675 | 5.4x advert_bytes | up | 3 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.656 → 0.665 | 0.009 | 0.656 → 0.665 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.833 → 0.840 | 0.007 | 0.654 → 0.662 | 1.2x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.861 → 0.867 | 0.006 | 0.671 → 0.676 | 1.1x sr_bytes | down | 2 |
| `SF-resolve` | resolve | **held** | 0.861 → 0.867 | 0.006 | 0.664 → 0.671 | 5.7x advert_bytes | = | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.925 → 0.929 | 0.004 | 0.920 → 0.924 | 1x bytes_on_air | up | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.679 → 0.683 | 0.004 | 0.671 → 0.672 | 2.3x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.925 → 0.925 | 0.000 | 0.920 → 0.921 | 1.1x sr_airtime | down | 2 |

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
| none | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| sprinkled | 1 | 0.811 | 0.803 | 0.009 | - | - | 0.971 | 0.972 | 0.478 | 1.33x | 13.7/25.8/28.1% | 1.8/5.0% | 3 |
| arms-race | 1 | 0.926 | 0.924 | 0.002 | - | - | 0.972 | 0.972 | 0.750 | 1.21x | 18.4/24.7/26.9% | 1.9/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.730 | 0.707 | 0.023 | - | - | 0.674 | 0.676 | 0.230 | 1.28x | 12.4/24.7/26.8% | 2.0/5.1% | 3 |
| 0.3 | 1 | 0.870 | 0.828 | 0.042 | - | - | 0.893 | 0.896 | 0.612 | 1.31x | 15.4/25.2/27.8% | 1.8/5.4% | 3 |

> amplify-worst=0.1: decode_failures 4

> amplify-worst=0.3: decode_failures 1

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.589 | 0.571 | 0.018 | - | - | 0.822 | 0.828 | 0.000 | 1.18x | 10.0/23.8/27.6% | 2.1/5.0% | 3 |
| inverse | 1 | 0.513 | 0.498 | 0.015 | - | - | 0.682 | 0.685 | 0.000 | 1.08x | 10.2/17.4/20.5% | 2.0/3.2% | 3 |
| random | 1 | 0.598 | 0.580 | 0.018 | - | - | 0.819 | 0.852 | 0.000 | 1.17x | 10.8/19.8/24.0% | 2.0/4.9% | 3 |

> role-placement=random: decode_failures 21

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.589 | 0.571 | 0.018 | - | - | 0.822 | 0.828 | 0.000 | 1.18x | 10.0/23.8/27.6% | 2.1/5.0% | 3 |
| all-routers | 1 | 0.786 | 0.777 | 0.009 | - | - | 0.927 | 0.930 | 0.000 | 2.42x | 20.8/37.3/40.7% | 4.1/4.9% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.589 | 0.571 | 0.018 | - | - | 0.822 | 0.828 | 0.000 | 1.18x | 10.0/23.8/27.6% | 2.1/5.0% | 3 |
| no-mute | 1 | 0.674 | 0.658 | 0.016 | - | - | 0.865 | 0.867 | 0.000 | 1.29x | 11.7/22.1/23.8% | 2.2/4.9% | 3 |
| all-routers | 1 | 0.786 | 0.777 | 0.009 | - | - | 0.927 | 0.930 | 0.000 | 2.42x | 20.8/37.3/40.7% | 4.1/4.9% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.589 | 0.571 | 0.018 | - | - | 0.822 | 0.828 | 0.000 | 1.18x | 10.0/23.8/27.6% | 2.1/5.0% | 3 |
| local-typical | 1 | 0.503 | 0.495 | 0.008 | - | - | 0.745 | 0.750 | 0.000 | 1.26x | 9.6/21.2/29.5% | 2.2/5.2% | 3 |
| basement-heavy | 1 | 0.045 | 0.045 | 0.000 | - | - | 0.082 | 0.193 | 0.000 | 0.37x | 0.2/4.3/9.6% | 0.2/2.5% | 3 |

> siting-mix=basement-heavy: decode_failures 1

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.813 | 0.806 | 0.007 | - | - | 0.945 | 0.946 | 0.000 | 2.27x | 15.5/26.6/32.3% | 1.7/5.4% | 3 |
| inverse | 1 | 0.791 | 0.779 | 0.012 | - | - | 0.942 | 0.943 | 0.000 | 2.21x | 14.3/23.5/29.3% | 1.7/3.2% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.661 | 0.661 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.29x | 11.5/23.3/25.7% | 2.0/4.6% | 3 |
| sr | 1 | 0.723 | 0.673 | 0.050 | - | - | 0.875 | 0.934 | 0.000 | 1.36x | 12.1/24.6/26.8% | 2.2/4.9% | 3 |

> protocol=sr: decode_failures 31

> slower: 6.07 s per simulated hour against 1.93 over 42 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.612 | 0.603 | 0.009 | - | - | 0.771 | 0.789 | 0.000 | 2.96x | 26.5/58.7/64.2% | 4.4/8.4% | 3 |
| 100 | 1 | 0.716 | 0.708 | 0.009 | - | - | 0.870 | 0.871 | 0.000 | 1.65x | 14.9/34.9/38.5% | 2.6/4.8% | 3 |
| 120 | 1 | 0.716 | 0.708 | 0.009 | - | - | 0.870 | 0.871 | 0.000 | 1.65x | 14.9/34.9/38.5% | 2.6/4.8% | 3 |
| 250 | 1 | 0.716 | 0.708 | 0.009 | - | - | 0.870 | 0.871 | 0.000 | 1.65x | 14.9/34.9/38.5% | 2.6/4.8% | 3 |

> max-num-nodes=10: decode_failures 8

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.316 | 0.306 | 0.009 | - | - | 0.530 | 0.593 | 0.091 | 11.43x | 38.6/59.5/72.8% | 3.9/11.6% | 3 |
| 120 | 1 | 0.498 | 0.486 | 0.012 | - | - | 0.811 | 0.812 | 0.150 | 4.34x | 14.7/27.3/36.1% | 1.4/5.5% | 3 |
| 250 | 1 | 0.496 | 0.485 | 0.011 | - | - | 0.801 | 0.802 | 0.155 | 4.22x | 14.4/26.1/34.3% | 1.4/5.2% | 3 |

> max-num-nodes=10: decode_failures 58

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.716 | 0.708 | 0.009 | - | - | 0.870 | 0.871 | 0.000 | 1.65x | 14.9/34.9/38.5% | 2.6/4.8% | 3 |
| baymesh-2026-08 | 1 | 0.716 | 0.708 | 0.009 | - | - | 0.870 | 0.871 | 0.000 | 1.65x | 14.9/34.9/38.5% | 2.6/4.8% | 3 |
| constrained | 1 | 0.611 | 0.599 | 0.011 | - | - | 0.770 | 0.781 | 0.000 | 2.96x | 26.5/58.8/64.3% | 4.5/8.4% | 3 |

> platform-mix=constrained: decode_failures 8

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.878 | 0.943 | 0.417 | 5.81x | 51.1/71.4/77.2% | 4.1/11.9% | 3 |
| 25 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.878 | 0.943 | 0.417 | 5.81x | 51.1/71.4/77.2% | 4.1/11.9% | 3 |
| 100 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.878 | 0.943 | 0.417 | 5.81x | 51.1/71.4/77.2% | 4.1/11.9% | 3 |
| 2000 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.878 | 0.943 | 0.417 | 5.81x | 51.1/71.4/77.2% | 4.1/11.9% | 3 |

> warm-num-nodes=0: decode_failures 81

> warm-num-nodes=25: decode_failures 81

> warm-num-nodes=100: decode_failures 81

> warm-num-nodes=2000: decode_failures 81

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.587 | 0.570 | 0.017 | - | - | 0.816 | 0.831 | 0.000 | 1.22x | 10.7/23.0/25.2% | 1.9/4.5% | 3 |
| 0.2 | 1 | 0.483 | 0.461 | 0.022 | - | - | 0.740 | 0.784 | 0.000 | 1.11x | 9.9/21.4/23.4% | 1.7/4.1% | 3 |
| 0.3 | 1 | 0.384 | 0.361 | 0.023 | - | - | 0.599 | 0.692 | 0.000 | 1.00x | 9.3/19.6/21.7% | 1.6/3.6% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 27

> burst-loss=0.3: decode_failures 19

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.652 | 0.643 | 0.009 | - | - | 0.854 | 0.864 | 0.000 | 1.36x | 11.9/25.0/27.3% | 2.1/4.7% | 3 |
| 0.2 | 1 | 0.590 | 0.579 | 0.011 | - | - | 0.801 | 0.831 | 0.000 | 1.34x | 12.0/25.1/27.4% | 2.2/4.6% | 3 |
| 0.3 | 1 | 0.532 | 0.521 | 0.011 | - | - | 0.738 | 0.799 | 0.000 | 1.30x | 12.0/24.7/27.3% | 2.0/4.4% | 3 |

> extra-loss=0.1: decode_failures 9

> extra-loss=0.2: decode_failures 19

> extra-loss=0.3: decode_failures 15

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.576 | 0.562 | 0.014 | - | - | 0.803 | 0.825 | 0.000 | 1.24x | 10.7/23.4/25.8% | 2.0/4.5% | 3 |
| 0.2 | 1 | 0.480 | 0.467 | 0.013 | - | - | 0.712 | 0.804 | 0.000 | 1.13x | 10.0/22.0/24.0% | 1.8/4.2% | 3 |
| 0.3 | 1 | 0.363 | 0.350 | 0.013 | - | - | 0.521 | 0.685 | 0.000 | 1.07x | 10.2/20.7/23.4% | 1.6/4.0% | 3 |

> burst-loss=0.1: decode_failures 4

> burst-loss=0.2: decode_failures 25

> burst-loss=0.3: decode_failures 17

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.637 | 0.637 | 0.000 | - | - | 0.785 | 0.834 | 0.000 | 1.65x | 14.6/30.2/33.2% | 2.6/6.1% | 3 |
| directed-with-late-flood | 1 | 0.656 | 0.656 | 0.000 | - | - | 0.837 | 0.854 | 0.000 | 1.57x | 14.0/29.0/31.8% | 2.5/5.8% | 3 |
| m4-early-flood | 1 | 0.651 | 0.651 | 0.000 | - | - | 0.817 | 0.849 | 0.000 | 1.57x | 14.1/29.0/31.8% | 2.5/5.9% | 3 |

> dm-mode=flood-only: decode_failures 19

> dm-mode=directed-with-late-flood: decode_failures 1

> dm-mode=m4-early-flood: decode_failures 15

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.747 | 0.736 | 0.011 | - | - | 0.931 | 0.933 | 0.437 | 0.69x | 6.3/10.3/12.1% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.693 | 0.684 | 0.009 | - | - | 0.904 | 0.907 | 0.308 | 1.26x | 11.0/21.4/24.0% | 2.0/4.5% | 3 |
| 0.5 | 1 | 0.828 | 0.815 | 0.013 | - | - | 0.956 | 0.964 | 0.383 | 1.06x | 10.5/17.1/19.0% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.726 | 0.716 | 0.010 | - | - | 0.947 | 0.948 | 0.285 | 0.91x | 9.0/13.6/15.3% | 1.6/3.2% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.698 | 0.685 | 0.013 | - | - | 0.917 | 0.918 | 0.276 | 1.23x | 11.0/21.1/23.8% | 2.0/4.4% | 3 |
| 0.5 | 1 | 0.839 | 0.830 | 0.009 | - | - | 0.952 | 0.965 | 0.388 | 1.03x | 10.4/17.0/19.0% | 1.5/4.0% | 3 |
| 0.75 | 1 | 0.712 | 0.704 | 0.008 | - | - | 0.930 | 0.935 | 0.254 | 0.87x | 8.6/13.3/15.1% | 1.4/3.2% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.734 | 0.726 | 0.007 | - | - | 0.905 | 0.909 | 0.000 | 0.73x | 7.0/14.3/15.8% | 1.2/2.9% | 3 |
| signing=true | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.740 | 0.730 | 0.010 | - | - | 0.930 | 0.931 | 0.402 | 0.68x | 6.6/11.1/12.6% | 1.1/2.5% | 3 |
| 2.5 | 1 | 0.744 | 0.733 | 0.011 | - | - | 0.934 | 0.935 | 0.397 | 0.71x | 6.7/11.3/12.8% | 1.2/2.6% | 3 |
| 2.6 | 1 | 0.755 | 0.745 | 0.011 | - | - | 0.948 | 0.949 | 0.434 | 0.66x | 6.6/10.9/12.5% | 1.1/2.5% | 3 |
| 2.7 | 1 | 0.767 | 0.760 | 0.006 | - | - | 0.942 | 0.942 | 0.340 | 0.69x | 6.8/12.5/14.4% | 1.0/3.0% | 3 |
| 2.8 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.721 | 0.713 | 0.008 | - | - | 0.891 | 0.896 | 0.000 | 0.88x | 7.8/16.2/17.6% | 1.4/3.2% | 3 |
| 900 | 1 | 0.653 | 0.642 | 0.011 | - | - | 0.851 | 0.859 | 0.000 | 2.10x | 18.3/37.5/41.0% | 3.3/7.5% | 3 |
| 300 | 1 | 0.449 | 0.442 | 0.007 | - | - | 0.616 | 0.683 | 0.000 | 4.48x | 38.7/69.2/75.2% | 7.1/14.5% | 3 |

> broadcast-interval-s=900: decode_failures 1

> broadcast-interval-s=300: decode_failures 1

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.751 | 0.744 | 0.007 | - | - | 0.856 | 0.858 | 0.000 | 0.99x | 8.9/16.6/17.9% | 1.6/3.3% | 3 |
| 900 | 1 | 0.669 | 0.654 | 0.015 | - | - | 0.793 | 0.804 | 0.000 | 2.33x | 20.8/38.4/41.6% | 3.6/7.5% | 3 |
| 300 | 1 | 0.436 | 0.430 | 0.005 | - | - | 0.535 | 0.635 | 0.000 | 5.01x | 42.6/70.8/76.1% | 8.3/14.7% | 3 |

> broadcast-interval-s=900: decode_failures 1

> broadcast-interval-s=300: decode_failures 2

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.708 | 0.700 | 0.008 | - | - | 0.887 | 0.888 | 0.000 | 1.26x | 11.3/23.1/25.3% | 2.0/4.6% | 3 |
| sinusoid | 1 | 0.688 | 0.680 | 0.009 | - | - | 0.861 | 0.862 | 0.000 | 1.22x | 11.0/22.2/24.0% | 1.9/4.4% | 3 |
| commuter | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.653 | 0.642 | 0.011 | - | - | 0.851 | 0.859 | 0.000 | 2.10x | 18.3/37.5/41.0% | 3.3/7.5% | 3 |
| 3600 | 1 | 0.721 | 0.713 | 0.008 | - | - | 0.891 | 0.896 | 0.000 | 0.88x | 7.8/16.2/17.6% | 1.4/3.2% | 3 |
| 10800 | 1 | 0.722 | 0.715 | 0.006 | - | - | 0.890 | 0.891 | 0.000 | 0.60x | 5.4/11.2/12.1% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.740 | 0.733 | 0.006 | - | - | 0.910 | 0.912 | 0.000 | 0.41x | 3.7/7.7/8.3% | 0.6/1.6% | 3 |

> broadcast-interval-s=900: decode_failures 1

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.680 | 0.670 | 0.009 | - | - | 0.866 | 0.872 | 0.000 | 1.39x | 12.2/25.4/27.8% | 2.1/5.1% | 3 |
| 1.0 | 1 | 0.674 | 0.666 | 0.008 | - | - | 0.856 | 0.872 | 0.000 | 1.50x | 13.3/27.7/30.2% | 2.3/5.5% | 3 |
| 4.0 | 1 | 0.645 | 0.634 | 0.011 | - | - | 0.843 | 0.849 | 0.000 | 1.85x | 16.3/34.4/37.9% | 2.9/6.9% | 3 |

> traceroute-per-hour=1.0: decode_failures 25

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.878 | 0.943 | 0.417 | 5.81x | 51.1/71.4/77.2% | 4.1/11.9% | 3 |
| 1.0 | 1 | 0.655 | 0.640 | 0.015 | - | - | 0.817 | 0.915 | 0.385 | 6.43x | 55.5/75.0/79.3% | 4.6/12.9% | 3 |

> traceroute-per-hour=0.0: decode_failures 81

> traceroute-per-hour=1.0: queue drops 10.0% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 64

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.515 | 0.507 | 0.008 | - | - | 0.727 | 0.730 | 0.000 | 1.04x | 11.3/17.8/19.7% | 2.4/5.5% | 3 |
| 60 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 90 | 1 | 0.874 | 0.869 | 0.004 | - | - | 0.982 | 0.982 | 0.592 | 1.67x | 16.1/26.1/30.4% | 1.5/4.8% | 3 |
| 120 | 1 | 0.925 | 0.920 | 0.004 | - | - | 0.994 | 0.995 | 0.548 | 2.06x | 20.1/31.8/37.5% | 1.4/5.1% | 3 |
| 150 | 1 | 0.944 | 0.941 | 0.003 | - | - | 0.998 | 0.998 | 0.720 | 2.63x | 23.6/39.8/45.2% | 1.4/5.5% | 3 |

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 120 | 1 | 0.696 | 0.687 | 0.009 | - | - | 0.919 | 0.919 | 0.116 | 2.25x | 13.9/26.2/31.7% | 1.6/4.7% | 3 |
| 250 | 1 | 0.489 | 0.478 | 0.011 | - | - | 0.793 | 0.796 | 0.149 | 4.59x | 15.6/29.0/38.6% | 1.5/6.0% | 3 |
| 500 | 1 | 0.337 | 0.332 | 0.004 | - | - | 0.488 | 0.489 | 0.104 | 9.86x | 18.8/29.8/47.0% | 1.6/5.9% | 3 |

> nodes=250: decode_failures 26

> nodes=500: decode_failures 7

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.702 | 0.695 | 0.007 | - | - | 0.919 | 0.919 | 0.121 | 2.19x | 13.6/25.5/30.6% | 1.6/4.5% | 3 |
| 250 | 1 | 0.498 | 0.486 | 0.012 | - | - | 0.811 | 0.812 | 0.150 | 4.34x | 14.7/27.3/36.1% | 1.4/5.5% | 3 |
| 500 | 1 | 0.337 | 0.332 | 0.005 | - | - | 0.488 | 0.490 | 0.104 | 9.21x | 17.6/27.8/44.6% | 1.5/5.6% | 3 |

> nodes=500: decode_failures 20

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.703 | 0.692 | 0.011 | - | - | 0.862 | 0.868 | 0.000 | 1.36x | 12.2/24.7/26.9% | 2.1/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.589 | 0.571 | 0.018 | - | - | 0.822 | 0.828 | 0.000 | 1.18x | 10.0/23.8/27.6% | 2.1/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.712 | 0.702 | 0.009 | - | - | 0.856 | 0.859 | 0.000 | 1.41x | 12.8/24.9/27.0% | 2.3/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.619 | 0.606 | 0.014 | - | - | 0.807 | 0.810 | 0.000 | 1.29x | 11.5/26.4/29.7% | 2.4/4.7% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.05 | 1 | 0.686 | 0.676 | 0.010 | - | - | 0.861 | 0.867 | 0.000 | 1.48x | 13.6/32.1/35.3% | 2.2/4.8% | 3 |
| 0.1 | 1 | 0.681 | 0.672 | 0.009 | - | - | 0.849 | 0.859 | 0.000 | 1.57x | 14.3/35.5/40.2% | 2.3/4.8% | 3 |
| 0.2 | 1 | 0.727 | 0.719 | 0.008 | - | - | 0.876 | 0.884 | 0.000 | 1.78x | 16.7/38.1/41.4% | 2.7/4.9% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| local-typical | 1 | 0.579 | 0.573 | 0.006 | - | - | 0.822 | 0.825 | 0.000 | 1.41x | 10.5/23.7/30.5% | 2.3/5.1% | 3 |
| event | 1 | 0.228 | 0.222 | 0.005 | - | - | 0.482 | 0.492 | 0.000 | 1.30x | 5.8/19.4/25.0% | 1.7/5.4% | 3 |
| backbone | 1 | 0.951 | 0.948 | 0.003 | - | - | 0.985 | 0.987 | 0.753 | 1.28x | 21.2/30.9/34.3% | 2.0/5.4% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.746 | 0.736 | 0.010 | - | - | 0.937 | 0.939 | 0.341 | 1.40x | 19.4/28.1/31.7% | 3.3/7.1% | 3 |
| 60 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 90 | 1 | 0.630 | 0.621 | 0.009 | - | - | 0.803 | 0.804 | 0.270 | 1.68x | 13.1/20.8/27.9% | 1.7/4.8% | 3 |
| 120 | 1 | 0.696 | 0.687 | 0.009 | - | - | 0.919 | 0.919 | 0.116 | 2.25x | 13.9/26.2/31.7% | 1.6/4.7% | 3 |
| 150 | 1 | 0.618 | 0.604 | 0.014 | - | - | 0.928 | 0.930 | 0.227 | 2.73x | 14.0/24.6/31.3% | 1.5/5.3% | 3 |

> nodes=150: decode_failures 2

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 1.25 | 1 | 0.430 | 0.420 | 0.010 | - | - | 0.683 | 0.692 | 0.000 | 1.41x | 11.6/23.4/29.6% | 2.1/5.5% | 3 |
| 1.5 | 1 | 0.307 | 0.298 | 0.008 | - | - | 0.562 | 0.581 | 0.000 | 1.58x | 9.3/24.6/32.6% | 2.4/6.1% | 3 |
| 2.0 | 1 | 0.140 | 0.139 | 0.002 | - | - | 0.398 | 0.400 | 0.000 | 0.91x | 3.4/11.0/16.1% | 1.5/4.5% | 3 |

> stretch=1.5: decode_failures 9

> stretch=2.0: decode_failures 3

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| clustered | 1 | 0.939 | 0.935 | 0.004 | - | - | 0.996 | 0.996 | 0.695 | 1.27x | 21.7/30.2/32.9% | 1.8/5.4% | 3 |
| corridor | 1 | 0.481 | 0.477 | 0.004 | - | - | 0.691 | 0.692 | 0.000 | 1.42x | 21.0/32.4/37.8% | 1.9/6.7% | 3 |
| hub | 1 | 0.955 | 0.955 | 0.000 | - | - | 0.986 | 0.986 | 0.777 | 1.27x | 23.2/35.7/37.1% | 1.7/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.656 | 0.656 | 0.000 | - | - | 0.837 | 0.854 | 0.000 | 1.57x | 14.0/29.0/31.8% | 2.5/5.8% | 3 |
| True | 1 | 0.665 | 0.665 | 0.000 | - | - | 0.830 | 0.873 | 0.000 | 1.56x | 13.9/28.9/31.5% | 2.5/5.8% | 3 |

> coding-rate-ladder=False: decode_failures 1

> coding-rate-ladder=True: decode_failures 22

> slower: 5.73 s per simulated hour against 2.79 over 42 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.665 | 0.665 | 0.000 | - | - | 0.830 | 0.873 | 0.000 | 1.56x | 13.9/28.9/31.5% | 2.5/5.8% | 3 |
| m4-early-flood | 1 | 0.654 | 0.654 | 0.000 | - | - | 0.818 | 0.845 | 0.000 | 1.56x | 13.8/28.7/31.5% | 2.5/5.8% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 22

> dm-mode=m4-early-flood: decode_failures 8

> slower: 6.58 s per simulated hour against 2.79 over 42 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.661 | 0.661 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.29x | 11.5/23.3/25.7% | 2.0/4.6% | 3 |
| chain | 1 | 0.669 | 0.668 | 0.001 | - | - | 0.783 | 0.868 | 0.000 | 1.56x | 13.9/28.5/31.0% | 2.5/5.6% | 3 |
| sr | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| True | 1 | 0.704 | 0.693 | 0.011 | - | - | 0.885 | 0.888 | 0.000 | 1.36x | 12.0/24.5/26.8% | 2.1/4.9% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.925 | 0.920 | 0.004 | - | - | 0.994 | 0.995 | 0.548 | 2.06x | 20.1/31.8/37.5% | 1.4/5.1% | 3 |
| True | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.997 | 0.997 | 0.579 | 2.11x | 20.3/32.2/37.9% | 1.5/5.1% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.111 | 0.111 | 0.000 | - | - | 0.361 | 0.361 | 0.000 | 0.03x | 0.1/0.6/0.8% | 0.0/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.282 | 0.274 | 0.007 | - | - | 0.574 | 0.582 | 0.000 | 0.20x | 1.1/3.4/4.6% | 0.2/0.9% | 3 |
| LONG_TURBO | 1 | 0.537 | 0.524 | 0.013 | - | - | 0.772 | 0.773 | 0.000 | 1.32x | 9.3/22.9/26.3% | 2.1/4.8% | 3 |

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 0.25 | 1 | 0.750 | 0.738 | 0.012 | - | - | 0.894 | 0.894 | 0.232 | 1.27x | 15.1/27.0/27.8% | 1.9/4.9% | 3 |
| 1.0 | 1 | 0.874 | 0.863 | 0.011 | - | - | 0.956 | 0.957 | 0.571 | 1.06x | 18.7/27.8/30.4% | 1.4/5.0% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.224 | 0.216 | 0.007 | - | - | 0.494 | 0.498 | 0.000 | 0.11x | 0.5/1.7/2.1% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| LITE_FAST | 1 | 0.585 | 0.572 | 0.012 | - | - | 0.838 | 0.839 | 0.000 | 0.92x | 7.8/15.7/19.2% | 1.5/3.6% | 3 |
| NARROW_SLOW | 1 | 0.626 | 0.623 | 0.003 | - | - | 0.837 | 0.837 | 0.000 | 1.23x | 10.7/21.1/24.3% | 2.0/4.6% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| temporal | 1 | 0.553 | 0.546 | 0.007 | - | - | 0.747 | 0.801 | 0.000 | 1.23x | 10.8/22.4/24.6% | 2.0/4.5% | 3 |
| transient | 1 | 0.669 | 0.660 | 0.009 | - | - | 0.856 | 0.864 | 0.000 | 1.35x | 11.8/24.6/26.9% | 2.1/4.8% | 3 |
| periodic | 1 | 0.506 | 0.498 | 0.008 | - | - | 0.665 | 0.682 | 0.000 | 1.19x | 10.4/21.9/24.0% | 1.9/4.1% | 3 |

> noise-profile=temporal: decode_failures 6

> noise-profile=transient: decode_failures 2

> noise-profile=periodic: decode_failures 2

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.224 | 0.216 | 0.007 | - | - | 0.494 | 0.498 | 0.000 | 0.11x | 0.5/1.7/2.1% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| LONG_MODERATE | 1 | 0.736 | 0.718 | 0.018 | - | - | 0.878 | 0.927 | 0.233 | 3.72x | 38.8/63.3/66.0% | 5.8/12.1% | 3 |

> preset=LONG_MODERATE: decode_failures 11

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.067 | 0.067 | 0.000 | - | - | 0.192 | 0.290 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.111 | 0.111 | 0.000 | - | - | 0.361 | 0.361 | 0.000 | 0.03x | 0.1/0.6/0.8% | 0.0/0.2% | 3 |
| LONG_FAST | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| LONG_TURBO | 1 | 0.537 | 0.524 | 0.013 | - | - | 0.772 | 0.773 | 0.000 | 1.32x | 9.3/22.9/26.3% | 2.1/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.671 | 0.664 | 0.007 | - | - | 0.855 | 0.861 | 0.000 | 1.85x | 15.7/31.9/34.1% | 2.9/6.4% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.624 | 0.615 | 0.009 | - | - | 0.802 | 0.806 | 0.000 | 1.30x | 11.5/24.3/26.5% | 2.0/4.7% | 3 |
| 10000 | 1 | 0.506 | 0.498 | 0.008 | - | - | 0.665 | 0.682 | 0.000 | 1.19x | 10.4/21.9/24.0% | 1.9/4.1% | 3 |
| 4000 | 1 | 0.307 | 0.304 | 0.003 | - | - | 0.416 | 0.499 | 0.000 | 1.00x | 9.4/18.7/20.7% | 1.6/3.2% | 3 |
| 2000 | 1 | 0.076 | 0.076 | 0.000 | - | - | 0.088 | 0.172 | 0.000 | 0.69x | 7.0/14.7/16.5% | 1.1/2.2% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 2

> noise-pulse-interval-ms=4000: decode_failures 1

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.307 | 0.298 | 0.008 | - | - | 0.562 | 0.581 | 0.000 | 1.58x | 9.3/24.6/32.6% | 2.4/6.1% | 3 |
| 1.0 | 1 | 0.700 | 0.689 | 0.011 | - | - | 0.839 | 0.840 | 0.451 | 1.03x | 14.5/24.5/27.6% | 1.4/4.5% | 3 |

> duct-per-hour=0.0: decode_failures 9

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 22 | 1 | 0.260 | 0.251 | 0.009 | - | - | 0.512 | 0.518 | 0.000 | 1.38x | 7.0/20.6/28.1% | 2.0/5.5% | 3 |
| 17 | 1 | 0.106 | 0.105 | 0.001 | - | - | 0.348 | 0.352 | 0.000 | 0.73x | 3.1/11.1/14.9% | 1.0/3.8% | 3 |
| 14 | 1 | 0.083 | 0.083 | 0.000 | - | - | 0.028 | 0.028 | 0.000 | 0.66x | 2.2/7.9/12.5% | 0.8/3.1% | 3 |

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.925 | 0.920 | 0.004 | - | - | 0.994 | 0.995 | 0.548 | 2.06x | 20.1/31.8/37.5% | 1.4/5.1% | 3 |
| True | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.993 | 0.994 | 0.543 | 2.49x | 23.4/37.8/43.2% | 1.8/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.694 | 0.685 | 0.009 | - | - | 0.872 | 0.874 | 0.000 | 1.50x | 13.7/31.9/34.6% | 2.2/4.9% | 3 |
| True | 1 | 0.725 | 0.716 | 0.008 | - | - | 0.869 | 0.870 | 0.000 | 1.59x | 14.5/32.8/35.5% | 2.5/4.9% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| random | 1 | 0.654 | 0.638 | 0.016 | - | - | 0.838 | 0.849 | 0.000 | 1.29x | 11.7/23.3/25.2% | 2.0/4.6% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.490 | 0.454 | 0.036 | - | - | 0.727 | 0.740 | 0.000 | 1.12x | 10.3/22.3/24.5% | 1.7/4.6% | 3 |
| 7 | 1 | 0.729 | 0.717 | 0.013 | - | - | 0.851 | 0.854 | 0.000 | 1.51x | 13.5/25.4/27.7% | 2.4/5.0% | 3 |
| 15 | 1 | 0.787 | 0.781 | 0.005 | - | - | 0.870 | 0.873 | 0.000 | 1.55x | 13.8/25.8/28.1% | 2.4/5.0% | 3 |
| 32 | 1 | 0.789 | 0.784 | 0.005 | - | - | 0.876 | 0.880 | 0.000 | 1.54x | 13.7/25.6/28.0% | 2.4/5.0% | 3 |

> hop-limit=3: decode_failures 1

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.490 | 0.454 | 0.036 | - | - | 0.727 | 0.740 | 0.000 | 1.12x | 10.3/22.3/24.5% | 1.7/4.6% | 3 |
| 5 | 1 | 0.641 | 0.627 | 0.014 | - | - | 0.801 | 0.804 | 0.000 | 1.31x | 12.1/23.5/25.4% | 2.1/4.7% | 3 |
| 7 | 1 | 0.729 | 0.717 | 0.013 | - | - | 0.851 | 0.854 | 0.000 | 1.51x | 13.5/25.4/27.7% | 2.4/5.0% | 3 |

> hop-limit=3: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| KNOWN_ONLY | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.676 | 0.676 | 0.000 | - | - | 0.772 | 0.867 | 0.000 | 1.32x | 11.6/23.9/26.4% | 2.1/4.7% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.490 | 0.454 | 0.036 | - | - | 0.727 | 0.740 | 0.000 | 1.12x | 10.3/22.3/24.5% | 1.7/4.6% | 3 |
| True | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

> hop-spread=False: decode_failures 1

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| BALANCED | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| STRICT | 1 | 0.571 | 0.571 | 0.000 | - | - | 0.733 | 0.767 | 0.000 | 1.43x | 12.6/26.4/28.7% | 2.2/5.3% | 3 |

> signature-policy=STRICT: decode_failures 26

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| dm | 1 | 0.683 | 0.672 | 0.011 | - | - | 0.870 | 0.873 | 0.000 | 1.33x | 11.9/24.5/26.5% | 2.0/5.0% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.689 | 0.681 | 0.008 | - | - | 0.868 | 0.875 | 0.000 | 1.34x | 12.0/24.4/26.6% | 2.1/4.8% | 3 |
| local | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| time | 1 | 0.682 | 0.674 | 0.008 | - | - | 0.857 | 0.866 | 0.000 | 1.36x | 12.1/24.9/27.2% | 2.1/5.0% | 3 |
| window | 1 | 0.690 | 0.680 | 0.010 | - | - | 0.876 | 0.885 | 0.000 | 1.33x | 11.7/24.3/26.6% | 2.1/4.8% | 3 |

> bucket-mode=global: misdecodes 19

> bucket-mode=time: misdecodes 22

> bucket-mode=window: misdecodes 12

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.673 | 0.662 | 0.011 | - | - | 0.852 | 0.860 | 0.000 | 1.50x | 13.3/27.5/29.9% | 2.3/5.6% | 3 |
| 1800 | 1 | 0.682 | 0.674 | 0.008 | - | - | 0.857 | 0.866 | 0.000 | 1.36x | 12.1/24.9/27.2% | 2.1/5.0% | 3 |
| 3600 | 1 | 0.683 | 0.675 | 0.008 | - | - | 0.859 | 0.865 | 0.000 | 1.36x | 12.0/24.8/27.1% | 2.2/4.9% | 3 |

> time-bucket-s=600: misdecodes 89

> time-bucket-s=1800: misdecodes 22

> time-bucket-s=3600: misdecodes 4

> time-bucket-s=3600: decode_failures 1

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| interval | 1 | 0.655 | 0.644 | 0.011 | - | - | 0.836 | 0.840 | 0.000 | 1.81x | 16.4/34.0/35.6% | 2.8/7.5% | 3 |
| aimd | 1 | 0.672 | 0.668 | 0.005 | - | - | 0.803 | 0.866 | 0.000 | 1.36x | 11.9/24.8/27.1% | 2.1/4.9% | 3 |
| bucket+interval | 1 | 0.663 | 0.653 | 0.010 | - | - | 0.841 | 0.844 | 0.000 | 1.83x | 16.5/34.1/35.8% | 2.9/7.2% | 3 |

> trigger=interval: misdecodes 15

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 8

> trigger=bucket+interval: misdecodes 19

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.678 | 0.670 | 0.007 | - | - | 0.847 | 0.867 | 0.000 | 1.34x | 11.8/24.6/26.6% | 2.0/5.0% | 3 |
| 8 | 1 | 0.691 | 0.683 | 0.007 | - | - | 0.878 | 0.888 | 0.000 | 1.34x | 12.1/24.7/26.6% | 2.1/5.0% | 3 |
| 16 | 1 | 0.684 | 0.674 | 0.010 | - | - | 0.866 | 0.874 | 0.000 | 1.35x | 11.9/24.8/26.9% | 2.1/4.9% | 3 |
| 32 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 50 | 1 | 0.682 | 0.673 | 0.008 | - | - | 0.867 | 0.872 | 0.000 | 1.35x | 12.1/24.7/26.9% | 2.1/4.9% | 3 |

> capacity=4: decode_failures 87

> capacity=8: decode_failures 75

> capacity=16: decode_failures 33

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.678 | 0.670 | 0.007 | - | - | 0.847 | 0.867 | 0.000 | 1.34x | 11.8/24.6/26.6% | 2.0/5.0% | 3 |
| 8 | 1 | 0.691 | 0.683 | 0.007 | - | - | 0.878 | 0.888 | 0.000 | 1.34x | 12.1/24.7/26.6% | 2.1/5.0% | 3 |
| 16 | 1 | 0.684 | 0.674 | 0.010 | - | - | 0.866 | 0.874 | 0.000 | 1.35x | 11.9/24.8/26.9% | 2.1/4.9% | 3 |
| 32 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 50 | 1 | 0.682 | 0.673 | 0.008 | - | - | 0.867 | 0.872 | 0.000 | 1.35x | 12.1/24.7/26.9% | 2.1/4.9% | 3 |

> capacity=4: decode_failures 87

> capacity=8: decode_failures 75

> capacity=16: decode_failures 33

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.676 | 0.671 | 0.005 | - | - | 0.832 | 0.867 | 0.000 | 1.33x | 11.7/24.1/26.4% | 2.0/4.7% | 3 |
| 16 | 1 | 0.681 | 0.671 | 0.010 | - | - | 0.857 | 0.864 | 0.000 | 1.33x | 11.8/24.2/26.4% | 2.1/4.8% | 3 |
| 32 | 1 | 0.690 | 0.680 | 0.010 | - | - | 0.876 | 0.885 | 0.000 | 1.33x | 11.7/24.3/26.6% | 2.1/4.8% | 3 |

> capacity=8: misdecodes 13

> capacity=8: decode_failures 52

> capacity=16: misdecodes 8

> capacity=16: decode_failures 3

> capacity=32: misdecodes 12

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.663 | 0.653 | 0.010 | - | - | 0.841 | 0.844 | 0.000 | 1.83x | 16.5/34.1/35.8% | 2.9/7.2% | 3 |
| 02-06 | 1 | 0.684 | 0.679 | 0.005 | - | - | 0.826 | 0.871 | 0.000 | 1.39x | 12.3/25.6/27.7% | 2.1/5.1% | 3 |
| 00-08 | 1 | 0.683 | 0.676 | 0.007 | - | - | 0.824 | 0.864 | 0.000 | 1.47x | 13.2/27.4/29.4% | 2.2/5.6% | 3 |

> catch-up-hours=: misdecodes 19

> catch-up-hours=02-06: decode_failures 35

> catch-up-hours=00-08: decode_failures 31

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.669 | 0.667 | 0.002 | - | - | 0.845 | 0.846 | 0.000 | 1.34x | 11.8/24.1/26.5% | 2.1/4.8% | 3 |
| 2 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 3 | 1 | 0.723 | 0.673 | 0.050 | - | - | 0.875 | 0.934 | 0.000 | 1.36x | 12.1/24.6/26.8% | 2.2/4.9% | 3 |
| 4 | 1 | 0.688 | 0.666 | 0.022 | - | - | 0.747 | 0.919 | 0.000 | 1.36x | 12.2/24.6/26.8% | 2.0/4.9% | 3 |

> hops-apart=3: decode_failures 31

> hops-apart=4: decode_failures 31

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.669 | 0.667 | 0.002 | - | - | 0.845 | 0.846 | 0.000 | 1.34x | 11.8/24.1/26.5% | 2.1/4.8% | 3 |
| 2 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 3 | 1 | 0.723 | 0.673 | 0.050 | - | - | 0.875 | 0.934 | 0.000 | 1.36x | 12.1/24.6/26.8% | 2.2/4.9% | 3 |
| 4 | 1 | 0.688 | 0.666 | 0.022 | - | - | 0.747 | 0.919 | 0.000 | 1.36x | 12.2/24.6/26.8% | 2.0/4.9% | 3 |
| 5 | 1 | 0.715 | 0.661 | 0.053 | - | - | 0.845 | 0.938 | 0.000 | 1.36x | 11.9/24.7/27.1% | 2.1/5.0% | 3 |

> hops-apart=3: decode_failures 31

> hops-apart=4: decode_failures 31

> hops-apart=5: decode_failures 31

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.677 | 0.669 | 0.008 | - | - | 0.851 | 0.865 | 0.000 | 1.34x | 11.9/24.5/26.6% | 2.1/4.8% | 3 |
| 30 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 120 | 1 | 0.689 | 0.678 | 0.011 | - | - | 0.870 | 0.875 | 0.000 | 1.35x | 12.0/24.7/26.8% | 2.1/4.9% | 3 |
| 600 | 1 | 0.683 | 0.674 | 0.009 | - | - | 0.863 | 0.868 | 0.000 | 1.37x | 12.1/24.9/27.1% | 2.1/4.9% | 3 |

> advert-jitter-s=1: decode_failures 9

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.677 | 0.669 | 0.008 | - | - | 0.851 | 0.865 | 0.000 | 1.34x | 11.9/24.5/26.6% | 2.1/4.8% | 3 |
| 30 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 120 | 1 | 0.689 | 0.678 | 0.011 | - | - | 0.870 | 0.875 | 0.000 | 1.35x | 12.0/24.7/26.8% | 2.1/4.9% | 3 |
| 600 | 1 | 0.683 | 0.674 | 0.009 | - | - | 0.863 | 0.868 | 0.000 | 1.37x | 12.1/24.9/27.1% | 2.1/4.9% | 3 |

> advert-jitter-s=1: decode_failures 9

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.678 | 0.669 | 0.009 | - | - | 0.513 | 0.863 | 0.000 | 1.34x | 11.9/24.2/26.6% | 2.1/4.8% | 3 |
| routers | 1 | 0.673 | 0.671 | 0.002 | - | - | 0.847 | 0.848 | 0.000 | 1.32x | 11.6/23.9/26.3% | 2.1/4.8% | 3 |
| alternate-routers | 1 | 0.683 | 0.679 | 0.004 | - | - | 0.855 | 0.855 | 0.000 | 1.36x | 11.9/24.7/27.1% | 2.1/5.0% | 3 |
| beside-router | 1 | 0.665 | 0.664 | 0.001 | - | - | 0.828 | 0.828 | 0.000 | 1.34x | 11.7/24.3/26.8% | 2.1/4.8% | 3 |
| random-clients | 1 | 0.683 | 0.661 | 0.022 | - | - | 0.781 | 0.923 | 0.000 | 1.34x | 11.9/24.5/27.2% | 2.1/5.0% | 3 |
| hops-apart | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

> place=spread: decode_failures 14

> place=random-clients: decode_failures 25

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.678 | 0.669 | 0.009 | - | - | 0.513 | 0.863 | 0.000 | 1.34x | 11.9/24.2/26.6% | 2.1/4.8% | 3 |
| routers | 1 | 0.673 | 0.671 | 0.002 | - | - | 0.847 | 0.848 | 0.000 | 1.32x | 11.6/23.9/26.3% | 2.1/4.8% | 3 |
| alternate-routers | 1 | 0.683 | 0.679 | 0.004 | - | - | 0.855 | 0.855 | 0.000 | 1.36x | 11.9/24.7/27.1% | 2.1/5.0% | 3 |
| beside-router | 1 | 0.665 | 0.664 | 0.001 | - | - | 0.828 | 0.828 | 0.000 | 1.34x | 11.7/24.3/26.8% | 2.1/4.8% | 3 |
| random-clients | 1 | 0.683 | 0.661 | 0.022 | - | - | 0.781 | 0.923 | 0.000 | 1.34x | 11.9/24.5/27.2% | 2.1/5.0% | 3 |
| hops-apart | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

> place=spread: decode_failures 14

> place=random-clients: decode_failures 25

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| broadcast | 1 | 0.702 | 0.654 | 0.048 | - | - | 0.833 | 0.846 | 0.000 | 1.43x | 12.6/25.8/28.2% | 2.3/5.1% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| heard | 1 | 0.683 | 0.676 | 0.007 | - | - | 0.861 | 0.863 | 0.000 | 1.35x | 12.1/24.6/26.8% | 2.1/4.9% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.702 | 0.654 | 0.048 | - | - | 0.833 | 0.846 | 0.000 | 1.43x | 12.6/25.8/28.2% | 2.3/5.1% | 3 |
| heard | 1 | 0.707 | 0.662 | 0.044 | - | - | 0.840 | 0.852 | 0.000 | 1.43x | 12.5/25.7/28.0% | 2.3/5.1% | 3 |

> replay-ordering=heard: misdecodes 2

> replay-ordering=heard: decode_failures 21

> slower: 4.02 s per simulated hour against 1.75 over 42 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| enum | 1 | 0.674 | 0.664 | 0.011 | - | - | 0.861 | 0.869 | 0.000 | 1.34x | 11.9/24.9/26.9% | 2.1/5.0% | 3 |
| hybrid | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.673 | 0.671 | 0.002 | - | - | 0.847 | 0.848 | 0.000 | 1.32x | 11.6/23.9/26.3% | 2.1/4.8% | 3 |
| 6 | 1 | 0.672 | 0.667 | 0.005 | - | - | 0.857 | 0.857 | 0.000 | 1.39x | 12.1/25.5/27.9% | 2.2/5.2% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.681 | 0.678 | 0.003 | - | - | 0.860 | 0.861 | 0.000 | 1.33x | 11.7/24.1/26.4% | 2.1/4.7% | 2 |
| 3 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 5 | 1 | 0.688 | 0.676 | 0.011 | - | - | 0.878 | 0.880 | 0.000 | 1.35x | 11.9/24.7/26.9% | 2.1/4.9% | 5 |
| 8 | 1 | 0.680 | 0.669 | 0.011 | - | - | 0.868 | 0.869 | 0.000 | 1.39x | 12.1/25.5/27.8% | 2.2/5.1% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.681 | 0.678 | 0.003 | - | - | 0.860 | 0.861 | 0.000 | 1.33x | 11.7/24.1/26.4% | 2.1/4.7% | 2 |
| 3 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 5 | 1 | 0.688 | 0.676 | 0.011 | - | - | 0.878 | 0.880 | 0.000 | 1.35x | 11.9/24.7/26.9% | 2.1/4.9% | 5 |
| 8 | 1 | 0.680 | 0.669 | 0.011 | - | - | 0.868 | 0.869 | 0.000 | 1.39x | 12.1/25.5/27.8% | 2.2/5.1% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| True | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.685 | 0.679 | 0.006 | - | - | 0.843 | 0.872 | 0.000 | 1.27x | 11.3/23.3/25.5% | 2.0/4.6% | 3 |
| 1 | 1 | 0.691 | 0.684 | 0.008 | - | - | 0.860 | 0.871 | 0.000 | 1.26x | 11.3/23.1/25.1% | 1.9/4.5% | 3 |
| 2 | 1 | 0.667 | 0.660 | 0.007 | - | - | 0.834 | 0.839 | 0.000 | 1.26x | 11.1/23.1/25.2% | 2.0/4.6% | 3 |
| 4 | 1 | 0.691 | 0.682 | 0.009 | - | - | 0.859 | 0.867 | 0.000 | 1.25x | 11.1/22.9/24.8% | 2.0/4.4% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.685 | 0.677 | 0.009 | - | - | 0.864 | 0.866 | 0.000 | 1.36x | 12.1/24.9/27.0% | 2.1/4.9% | 3 |
| 24 | 1 | 0.682 | 0.673 | 0.009 | - | - | 0.874 | 0.877 | 0.000 | 1.36x | 12.0/24.9/27.1% | 2.1/4.9% | 3 |
| 32 | 1 | 0.679 | 0.671 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.33x | 11.9/24.2/26.3% | 2.0/4.8% | 3 |
| 64 | 1 | 0.692 | 0.683 | 0.009 | - | - | 0.872 | 0.876 | 0.000 | 1.35x | 11.9/24.7/27.0% | 2.1/4.9% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.682 | 0.673 | 0.009 | - | - | 0.867 | 0.871 | 0.000 | 1.42x | 12.5/26.0/28.2% | 2.2/5.2% | 3 |
| 16 | 1 | 0.678 | 0.669 | 0.009 | - | - | 0.857 | 0.860 | 0.000 | 1.34x | 11.9/24.5/26.7% | 2.1/4.9% | 3 |
| 32 | 1 | 0.690 | 0.680 | 0.010 | - | - | 0.876 | 0.885 | 0.000 | 1.33x | 11.7/24.3/26.6% | 2.1/4.8% | 3 |

> window-size=8: misdecodes 128

> window-size=16: misdecodes 44

> window-size=32: misdecodes 12

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.925 | 0.920 | 0.004 | - | - | 0.994 | 0.995 | 0.548 | 2.06x | 20.1/31.8/37.5% | 1.4/5.1% | 3 |
| True | 1 | 0.727 | 0.708 | 0.019 | - | - | 0.904 | 0.951 | 0.422 | 5.68x | 50.4/70.9/76.7% | 4.0/11.6% | 3 |

> no-congestion-scaling=True: decode_failures 43

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.498 | 0.486 | 0.012 | - | - | 0.811 | 0.812 | 0.150 | 4.34x | 14.7/27.3/36.1% | 1.4/5.5% | 3 |
| truesize | 1 | 0.521 | 0.511 | 0.011 | - | - | 0.830 | 0.831 | 0.170 | 3.12x | 10.5/21.2/27.8% | 1.0/4.4% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.925 | 0.921 | 0.005 | - | - | 0.994 | 0.995 | 0.555 | 2.00x | 19.1/31.4/36.4% | 1.4/4.9% | 3 |
| adaptive | 1 | 0.925 | 0.920 | 0.004 | - | - | 0.994 | 0.995 | 0.548 | 2.06x | 20.1/31.8/37.5% | 1.4/5.1% | 3 |

