# Sweep blocks-2026-10-03-2996430

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 2996430 · seeds 2996430
- **blocks** 87 run
- **compute** 8.8 h of simulator time across every cell
- **generated** 2026-10-03T08:58:12+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>91 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 55
- AD-amplify-worst: slower: 5.46 s per simulated hour against 1.86 over 43 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=local-typical: decode_failures 1
- BL-control: protocol=sr: decode_failures 28
- BL-control: slower: 5.26 s per simulated hour against 1.94 over 43 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 73
- DB-hotstore-stress: max-num-nodes=120: decode_failures 8
- DB-hotstore-stress: max-num-nodes=250: decode_failures 4
- DB-warm: warm-num-nodes=0: decode_failures 31
- DB-warm: warm-num-nodes=25: decode_failures 31
- DB-warm: warm-num-nodes=100: decode_failures 31
- DB-warm: warm-num-nodes=2000: decode_failures 31
- DG-burst: burst-loss=0.2: decode_failures 1
- DG-burst: burst-loss=0.3: decode_failures 19
- DG-outage: burst-loss=0.1: decode_failures 13
- DG-outage: burst-loss=0.2: decode_failures 29
- DG-outage: burst-loss=0.3: decode_failures 24
- DM-mode: faster: 1.23 s per simulated hour against 3.31 over 43 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- FW-mixed-26: legacy-fraction=0.25: decode_failures 25
- FW-mixed-26: legacy-fraction=0.5: decode_failures 35
- FW-mixed-26: slower: 5.88 s per simulated hour against 1.71 over 43 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.25: decode_failures 19
- FW-mixed: legacy-fraction=0.5: decode_failures 37
- FW-mixed: slower: 5.83 s per simulated hour against 1.67 over 43 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 4
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 31
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 14.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 48
- MS-density: nodes=40: decode_failures 20
- MS-density: nodes=120: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 3
- MS-hopscale: nodes=500: decode_failures 41
- MS-oversubscribed: nodes=250: decode_failures 8
- MS-oversubscribed: nodes=500: decode_failures 83
- MS-router-late: faster: 0.841 s per simulated hour against 1.74 over 43 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-siting: siting-mix=local-typical: decode_failures 43
- MS-siting: siting-mix=event: decode_failures 5
- MS-siting: slower: 4.71 s per simulated hour against 1.92 over 42 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-size: nodes=150: decode_failures 4
- MS-stretch: stretch=2.0: decode_failures 1
- MS-topology: topology=corridor: decode_failures 17
- MS-topology: topology=hub: misdecodes 1
- PR-dmmode-cr: faster: 1.28 s per simulated hour against 2.82 over 43 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 13
- RF-eu-presets: preset=SHORT_FAST: decode_failures 2
- RF-preset: preset=SHORT_FAST: decode_failures 2
- RF-preset: preset=LONG_MODERATE: decode_failures 6
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 6
- RF-txpower: tx-power=22: decode_failures 12
- RF-txpower: tx-power=17: decode_failures 1
- RF-txpower: tx-power=14: decode_failures 2
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 44
- SF-bucket-mode: bucket-mode=time: misdecodes 33
- SF-bucket-mode: bucket-mode=window: misdecodes 14
- SF-bucket-time: time-bucket-s=600: misdecodes 139
- SF-bucket-time: time-bucket-s=1800: misdecodes 33
- SF-bucket-time: time-bucket-s=3600: misdecodes 8
- SF-cadence: trigger=interval: misdecodes 4
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 4
- SF-cadence: trigger=bucket+interval: misdecodes 16
- SF-capacity-local: capacity=4: decode_failures 87
- SF-capacity-local: capacity=8: decode_failures 34
- SF-capacity: capacity=4: decode_failures 87
- SF-capacity: capacity=8: decode_failures 34
- SF-capacity-window: capacity=8: misdecodes 24
- SF-capacity-window: capacity=8: decode_failures 13
- SF-capacity-window: capacity=16: misdecodes 6
- SF-capacity-window: capacity=32: misdecodes 14
- SF-catchup: catch-up-hours=: misdecodes 16
- SF-catchup: catch-up-hours=02-06: decode_failures 32
- SF-catchup: catch-up-hours=00-08: decode_failures 31
- SF-hops-flat: hops-apart=3: decode_failures 28
- SF-hops-flat: hops-apart=4: decode_failures 24
- SF-hops-spread: hops-apart=3: decode_failures 28
- SF-hops-spread: hops-apart=4: decode_failures 24
- SF-hops-spread: hops-apart=5: decode_failures 23
- SF-place-flat: place=spread: decode_failures 23
- SF-place-spread: place=spread: decode_failures 23
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 9
- SF-replay-order: replay-ordering=heard: misdecodes 8
- SF-window-size: window-size=8: misdecodes 128
- SF-window-size: window-size=16: misdecodes 56
- SF-window-size: window-size=32: misdecodes 14
- TH-congestion-input: congestion-input=hotstore: decode_failures 8
- TH-congestion-input: congestion-input=truesize: decode_failures 3
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: decode_failures 50

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `FW-mixed` | 5.83 | 1.67 | 3.49x | 43 |
| `FW-mixed-26` | 5.88 | 1.71 | 3.45x | 43 |
| `AD-amplify-worst` | 5.46 | 1.86 | 2.93x | 43 |
| `BL-control` | 5.26 | 1.94 | 2.71x | 43 |
| `MS-siting` | 4.71 | 1.92 | 2.45x | 42 |
| `AD-worst` | 2.33 | 3.48 | 0.67x | 43 |
| `FW-firmware` | 1.17 | 1.74 | 0.67x | 43 |
| `RF-preset` | 1.95 | 2.94 | 0.66x | 43 |
| `LD-traceroute-small` | 25 | 37.8 | 0.66x | 43 |
| `TH-congestion` | 10.9 | 17 | 0.65x | 43 |
| `DG-burst` | 3.24 | 5.11 | 0.64x | 43 |
| `MS-stretch` | 1.29 | 2.03 | 0.63x | 43 |
| `PR-crladder` | 1.74 | 2.79 | 0.62x | 43 |
| `SF-capacity-window` | 0.997 | 1.61 | 0.62x | 43 |
| `MS-hopscale` | 10.7 | 18 | 0.59x | 43 |
| `DB-platform` | 1.46 | 2.51 | 0.58x | 43 |
| `SF-replay-order-broadcast` | 0.975 | 1.77 | 0.55x | 43 |
| `RF-stretch-duct` | 1 | 1.84 | 0.55x | 43 |
| `AD-badrouters` | 1.12 | 2.1 | 0.54x | 43 |
| `AD-siting` | 0.814 | 1.53 | 0.53x | 43 |
| `SC-signing` | 0.947 | 1.82 | 0.52x | 43 |
| `LD-chatty` | 2.62 | 5.04 | 0.52x | 43 |
| `LD-traceroute` | 1.07 | 2.1 | 0.51x | 43 |
| `DB-warm` | 16.9 | 33.5 | 0.50x | 43 |
| `MS-router-late` | 0.841 | 1.74 | 0.48x | 43 |
| `PR-dmmode-cr` | 1.28 | 2.82 | 0.46x | 43 |
| `DM-mode` | 1.23 | 3.31 | 0.37x | 43 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.899 | 0.899 | 0.739 → 0.765 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.887 | 0.887 | 0.765 → 0.774 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **text** | 0.178 → 0.971 | 0.793 | 0.170 → 0.970 | 4.4x sr_airtime | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.095 → 0.850 | 0.755 | 0.070 → 0.693 | 1.4e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.167 → 0.899 | 0.732 | 0.081 → 0.753 | 6.8x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.191 → 0.899 | 0.708 | 0.063 → 0.753 | 5.2x advert_bytes | up | 5 |
| `AD-siting` | siting-mix | **held** | 0.116 → 0.813 | 0.697 | 0.034 → 0.663 | 7.6x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.107 → 0.760 | 0.653 | 0.106 → 0.753 | 3.4x advert_bytes | down | 4 |
| `MS-hopscale` | nodes | **held** | 0.318 → 0.931 | 0.614 | 0.319 → 0.753 | 8.4x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.325 → 0.934 | 0.609 | 0.322 → 0.711 | 4.9x bytes_on_air | down | 3 |
| `RF-bw500` | preset | **held** | 0.291 → 0.835 | 0.544 | 0.137 → 0.660 | 2.9x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.235 → 0.760 | 0.526 | 0.232 → 0.753 | 3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.235 → 0.760 | 0.526 | 0.232 → 0.753 | 3.9x sr_airtime | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.508 → 0.877 | 0.369 | 0.498 → 0.873 | 9x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.260 → 0.618 | 0.358 | 0.250 → 0.608 | 2.2x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.427 → 0.760 | 0.334 | 0.407 → 0.753 | 1.9x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.468 → 0.801 | 0.333 | 0.451 → 0.795 | 8.1x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.486 → 0.790 | 0.304 | 0.305 → 0.502 | 6x sr_airtime | up | 3 |
| `DG-burst` | burst-loss | **text** | 0.458 → 0.760 | 0.302 | 0.433 → 0.753 | 2x sr_bytes | down | 4 |
| `MS-topology` | topology | **held** | 0.670 → 0.955 | 0.285 | 0.613 → 0.902 | 2.8x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.684 → 0.953 | 0.269 | 0.667 → 0.949 | 5.6x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.602 → 0.858 | 0.256 | 0.573 → 0.856 | 2.6x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.602 → 0.842 | 0.240 | 0.573 → 0.838 | 2.1x sr_bytes | up | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.696 → 0.899 | 0.203 | 0.746 → 0.774 | 2.1x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.742 → 0.944 | 0.202 | 0.729 → 0.942 | 3.7x sr_airtime | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.760 → 0.953 | 0.193 | 0.753 → 0.947 | 1.3x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.732 → 0.913 | 0.181 | 0.589 → 0.756 | 1.4x sr_airtime | down | 4 |
| `SF-place-flat` | place | **held** | 0.759 → 0.938 | 0.179 | 0.752 → 0.771 | 2.4x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.759 → 0.938 | 0.179 | 0.752 → 0.771 | 2.4x sr_bytes | up | 6 |
| `MS-size` | nodes | **text** | 0.667 → 0.839 | 0.171 | 0.651 → 0.823 | 4.4x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.602 → 0.760 | 0.159 | 0.573 → 0.753 | 1.8x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.603 → 0.760 | 0.158 | 0.588 → 0.753 | 1.5x sr_bytes | down | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.705 → 0.848 | 0.143 | 0.696 → 0.844 | 5.5x sr_airtime | up | 4 |
| `SC-signing` | signature-policy | **text** | 0.619 → 0.760 | 0.142 | 0.619 → 0.753 | 1.6x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.682 → 0.823 | 0.141 | 0.677 → 0.819 | 2.4x sr_airtime | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.760 → 0.898 | 0.138 | 0.753 → 0.885 | 2.6x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.672 → 0.808 | 0.136 | 0.663 → 0.804 | 2.1x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.672 → 0.808 | 0.136 | 0.663 → 0.804 | 2.1x bytes_on_air | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.695 → 0.823 | 0.128 | 0.689 → 0.819 | 2.2x sr_airtime | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.760 → 0.887 | 0.127 | 0.753 → 0.881 | 1.3x bytes_on_air | up | 3 |
| `FW-versions` | profile | **text** | 0.760 → 0.877 | 0.116 | 0.753 → 0.871 | 3x bytes_on_air | down | 5 |
| `MS-roles-fav` | role-mix | **held** | 0.786 → 0.888 | 0.102 | 0.699 → 0.762 | 1.2x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **text** | 0.672 → 0.769 | 0.098 | 0.663 → 0.760 | 1.1x sr_bytes | down | 2 |
| `FW-firmware` | profile | **text** | 0.760 → 0.857 | 0.097 | 0.753 → 0.846 | 3.1x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.760 → 0.852 | 0.091 | 0.753 → 0.844 | 2.5x sr_bytes | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.810 → 0.899 | 0.090 | 0.666 → 0.734 | 1.4x sr_airtime | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.760 → 0.844 | 0.083 | 0.753 → 0.834 | 2.3x sr_bytes | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.760 → 0.824 | 0.064 | 0.753 → 0.821 | 3.2x bytes_on_air | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.837 → 0.899 | 0.062 | 0.753 → 0.774 | 2.1x sr_bytes | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.701 → 0.760 | 0.060 | 0.693 → 0.753 | 1.5x sr_airtime | down | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.846 → 0.899 | 0.053 | 0.753 → 0.766 | 28x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **text** | 0.627 → 0.672 | 0.045 | 0.604 → 0.663 | 1.5x sr_bytes | down | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.789 → 0.827 | 0.037 | 0.497 → 0.529 | 1.5x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.753 → 0.788 | 0.035 | 0.742 → 0.783 | 1.2x sr_bytes | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.734 → 0.768 | 0.034 | 0.726 → 0.765 | 9.4x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.868 → 0.899 | 0.032 | 0.753 → 0.774 | 1.5x sr_bytes | down | 4 |
| `SF-cadence` | trigger | **held** | 0.870 → 0.899 | 0.029 | 0.726 → 0.756 | 15x advert_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.874 → 0.899 | 0.026 | 0.734 → 0.753 | 1.3x sr_bytes | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.760 → 0.785 | 0.025 | 0.747 → 0.753 | 2.5x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.907 → 0.931 | 0.025 | 0.752 → 0.757 | 2.5x sr_bytes | up | 2 |
| `SF-servers-flat` | servers | **held** | 0.892 → 0.915 | 0.024 | 0.753 → 0.761 | 5.1x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.892 → 0.915 | 0.024 | 0.753 → 0.761 | 5.1x sr_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.899 → 0.922 | 0.023 | 0.752 → 0.762 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.899 → 0.922 | 0.023 | 0.752 → 0.762 | 5.4x advert_bytes | up | 5 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.899 → 0.921 | 0.022 | 0.753 → 0.765 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.899 → 0.921 | 0.022 | 0.753 → 0.765 | 1.1x sr_airtime | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.776 → 0.797 | 0.020 | 0.773 → 0.793 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.899 → 0.916 | 0.017 | 0.753 → 0.758 | 1x advert_bytes | up | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.748 → 0.764 | 0.016 | 0.740 → 0.757 | 3.4x advert_bytes | up | 4 |
| `LD-diurnal` | diurnal | **text** | 0.760 → 0.776 | 0.015 | 0.753 → 0.769 | 1.2x advert_bytes | down | 3 |
| `SF-width` | short-id-bits | **held** | 0.899 → 0.913 | 0.014 | 0.753 → 0.762 | 3.1x advert_bytes | down | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.760 → 0.773 | 0.013 | 0.753 → 0.765 | 1x advert_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.899 → 0.912 | 0.013 | 0.753 → 0.760 | 2.6x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.901 → 0.912 | 0.011 | 0.747 → 0.755 | 1.1x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.877 → 0.888 | 0.011 | 0.721 → 0.730 | 1.2x sr_airtime | up | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.882 → 0.892 | 0.010 | 0.727 → 0.731 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.748 → 0.758 | 0.010 | 0.740 → 0.752 | 5.5x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.901 → 0.911 | 0.009 | 0.758 → 0.768 | 1.3x sr_bytes | down | 4 |
| `SF-capacity-window` | capacity | **text** | 0.764 → 0.772 | 0.008 | 0.757 → 0.766 | 2x advert_bytes | down | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.940 → 0.944 | 0.005 | 0.937 → 0.942 | 1.3x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.944 → 0.949 | 0.004 | 0.942 → 0.947 | 1.1x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.888 → 0.892 | 0.004 | 0.730 → 0.731 | 1.1x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.910 → 0.912 | 0.002 | 0.755 → 0.758 | 5.5x advert_bytes | down | 3 |
| `SF-resolve` | resolve | **text** | 0.760 → 0.762 | 0.002 | 0.753 → 0.757 | 5.7x advert_bytes | = | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.944 → 0.945 | 0.001 | 0.942 → 0.943 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| sprinkled | 1 | 0.919 | 0.910 | 0.009 | - | - | 0.980 | 0.981 | 0.522 | 1.16x | 16.3/23.0/27.3% | 1.6/5.1% | 3 |
| arms-race | 1 | 0.953 | 0.947 | 0.006 | - | - | 0.987 | 0.989 | 0.812 | 1.12x | 19.1/24.3/28.2% | 1.4/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.836 | 0.828 | 0.008 | - | - | 0.883 | 0.961 | 0.397 | 1.25x | 15.7/22.2/26.6% | 1.9/4.9% | 3 |
| 0.3 | 1 | 0.898 | 0.885 | 0.013 | - | - | 0.947 | 0.948 | 0.686 | 1.09x | 17.2/23.3/27.4% | 1.7/4.7% | 3 |

> amplify-worst=0.1: decode_failures 55

> slower: 5.46 s per simulated hour against 1.86 over 43 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.672 | 0.663 | 0.009 | - | - | 0.813 | 0.814 | 0.325 | 1.21x | 13.0/20.4/22.8% | 2.1/4.8% | 3 |
| inverse | 1 | 0.627 | 0.604 | 0.022 | - | - | 0.854 | 0.859 | 0.345 | 1.10x | 11.8/16.9/18.4% | 2.0/3.6% | 3 |
| random | 1 | 0.638 | 0.629 | 0.009 | - | - | 0.813 | 0.816 | 0.314 | 1.16x | 12.9/17.9/20.4% | 2.0/4.7% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.672 | 0.663 | 0.009 | - | - | 0.813 | 0.814 | 0.325 | 1.21x | 13.0/20.4/22.8% | 2.1/4.8% | 3 |
| all-routers | 1 | 0.808 | 0.804 | 0.004 | - | - | 0.904 | 0.905 | 0.605 | 2.56x | 25.0/33.5/35.3% | 4.2/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.672 | 0.663 | 0.009 | - | - | 0.813 | 0.814 | 0.325 | 1.21x | 13.0/20.4/22.8% | 2.1/4.8% | 3 |
| no-mute | 1 | 0.725 | 0.714 | 0.011 | - | - | 0.871 | 0.874 | 0.311 | 1.28x | 13.5/20.6/22.1% | 2.0/4.9% | 3 |
| all-routers | 1 | 0.808 | 0.804 | 0.004 | - | - | 0.904 | 0.905 | 0.605 | 2.56x | 25.0/33.5/35.3% | 4.2/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.672 | 0.663 | 0.009 | - | - | 0.813 | 0.814 | 0.325 | 1.21x | 13.0/20.4/22.8% | 2.1/4.8% | 3 |
| local-typical | 1 | 0.512 | 0.507 | 0.004 | - | - | 0.686 | 0.688 | 0.000 | 1.27x | 11.8/23.9/29.8% | 2.2/5.3% | 3 |
| basement-heavy | 1 | 0.034 | 0.034 | 0.001 | - | - | 0.116 | 0.182 | 0.000 | 0.36x | 0.8/3.5/6.8% | 0.3/2.1% | 3 |

> siting-mix=local-typical: decode_failures 1

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.788 | 0.783 | 0.005 | - | - | 0.935 | 0.935 | 0.000 | 2.42x | 15.6/25.6/33.4% | 1.9/5.6% | 3 |
| inverse | 1 | 0.753 | 0.742 | 0.011 | - | - | 0.935 | 0.936 | 0.000 | 2.32x | 13.6/21.9/30.3% | 1.9/3.2% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.765 | 0.765 | 0.000 | - | - | 0 | 0.000 | 0.277 | 1.25x | 13.9/20.3/22.0% | 1.8/4.8% | 3 |
| sr | 1 | 0.792 | 0.774 | 0.018 | - | - | 0.887 | 0.953 | 0.281 | 1.26x | 14.0/20.5/22.4% | 1.8/4.9% | 3 |

> protocol=sr: decode_failures 28

> slower: 5.26 s per simulated hour against 1.94 over 43 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.682 | 0.677 | 0.005 | - | - | 0.762 | 0.763 | 0.475 | 2.87x | 31.2/46.7/51.8% | 4.1/9.3% | 3 |
| 100 | 1 | 0.823 | 0.819 | 0.004 | - | - | 0.899 | 0.900 | 0.559 | 1.49x | 16.4/25.0/28.0% | 2.2/4.9% | 3 |
| 120 | 1 | 0.823 | 0.819 | 0.004 | - | - | 0.899 | 0.900 | 0.559 | 1.49x | 16.4/25.0/28.0% | 2.2/4.9% | 3 |
| 250 | 1 | 0.823 | 0.819 | 0.004 | - | - | 0.899 | 0.900 | 0.559 | 1.49x | 16.4/25.0/28.0% | 2.2/4.9% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.314 | 0.305 | 0.008 | - | - | 0.486 | 0.533 | 0.000 | 11.44x | 41.6/58.3/72.5% | 3.9/10.8% | 3 |
| 120 | 1 | 0.509 | 0.497 | 0.012 | - | - | 0.789 | 0.790 | 0.000 | 4.39x | 16.0/26.8/36.5% | 1.5/5.2% | 3 |
| 250 | 1 | 0.513 | 0.502 | 0.011 | - | - | 0.790 | 0.793 | 0.000 | 4.25x | 15.5/25.8/35.2% | 1.4/5.1% | 3 |

> max-num-nodes=10: decode_failures 73

> max-num-nodes=120: decode_failures 8

> max-num-nodes=250: decode_failures 4

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.823 | 0.819 | 0.004 | - | - | 0.899 | 0.900 | 0.559 | 1.49x | 16.4/25.0/28.0% | 2.2/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.823 | 0.819 | 0.004 | - | - | 0.899 | 0.900 | 0.559 | 1.49x | 16.4/25.0/28.0% | 2.2/4.9% | 3 |
| constrained | 1 | 0.695 | 0.689 | 0.006 | - | - | 0.789 | 0.789 | 0.471 | 2.87x | 31.3/46.8/51.8% | 4.1/9.3% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.745 | 0.734 | 0.011 | - | - | 0.899 | 0.940 | 0.567 | 5.65x | 53.1/69.5/74.4% | 3.8/12.4% | 3 |
| 25 | 1 | 0.745 | 0.734 | 0.011 | - | - | 0.899 | 0.940 | 0.567 | 5.65x | 53.1/69.5/74.4% | 3.8/12.4% | 3 |
| 100 | 1 | 0.745 | 0.734 | 0.011 | - | - | 0.899 | 0.940 | 0.567 | 5.65x | 53.1/69.5/74.4% | 3.8/12.4% | 3 |
| 2000 | 1 | 0.745 | 0.734 | 0.011 | - | - | 0.899 | 0.940 | 0.567 | 5.65x | 53.1/69.5/74.4% | 3.8/12.4% | 3 |

> warm-num-nodes=0: decode_failures 31

> warm-num-nodes=25: decode_failures 31

> warm-num-nodes=100: decode_failures 31

> warm-num-nodes=2000: decode_failures 31

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.667 | 0.653 | 0.014 | - | - | 0.867 | 0.872 | 0.220 | 1.19x | 13.7/20.1/21.7% | 1.7/4.4% | 3 |
| 0.2 | 1 | 0.551 | 0.529 | 0.022 | - | - | 0.796 | 0.807 | 0.175 | 1.11x | 12.6/19.3/20.8% | 1.6/3.9% | 3 |
| 0.3 | 1 | 0.458 | 0.433 | 0.025 | - | - | 0.715 | 0.756 | 0.164 | 1.00x | 11.3/17.7/19.2% | 1.5/3.5% | 3 |

> burst-loss=0.2: decode_failures 1

> burst-loss=0.3: decode_failures 19

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.725 | 0.717 | 0.009 | - | - | 0.898 | 0.900 | 0.258 | 1.30x | 14.6/21.4/23.2% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.679 | 0.668 | 0.010 | - | - | 0.862 | 0.864 | 0.274 | 1.33x | 14.7/22.1/23.9% | 2.0/4.5% | 3 |
| 0.3 | 1 | 0.603 | 0.588 | 0.014 | - | - | 0.809 | 0.818 | 0.205 | 1.33x | 14.5/22.4/24.1% | 2.0/4.3% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.651 | 0.639 | 0.013 | - | - | 0.845 | 0.861 | 0.183 | 1.20x | 13.7/19.8/21.8% | 1.8/4.6% | 3 |
| 0.2 | 1 | 0.549 | 0.534 | 0.016 | - | - | 0.759 | 0.814 | 0.153 | 1.13x | 12.8/19.1/20.9% | 1.7/4.2% | 3 |
| 0.3 | 1 | 0.427 | 0.407 | 0.020 | - | - | 0.672 | 0.752 | 0.139 | 1.02x | 11.8/18.0/19.5% | 1.6/3.7% | 3 |

> burst-loss=0.1: decode_failures 13

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 24

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.721 | 0.721 | 0.000 | - | - | 0.877 | 0.878 | 0.260 | 1.61x | 18.2/26.5/28.7% | 2.3/6.3% | 3 |
| directed-with-late-flood | 1 | 0.730 | 0.730 | 0.000 | - | - | 0.888 | 0.890 | 0.270 | 1.48x | 16.9/24.7/26.8% | 2.1/5.8% | 3 |
| m4-early-flood | 1 | 0.722 | 0.722 | 0.000 | - | - | 0.886 | 0.890 | 0.234 | 1.49x | 16.9/24.8/27.0% | 2.1/5.9% | 3 |

> faster: 1.23 s per simulated hour against 3.31 over 43 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.857 | 0.846 | 0.011 | - | - | 0.981 | 0.983 | 0.644 | 0.73x | 7.9/11.3/13.7% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.852 | 0.844 | 0.007 | - | - | 0.958 | 0.978 | 0.256 | 1.14x | 13.0/21.0/23.3% | 1.7/4.9% | 3 |
| 0.5 | 1 | 0.840 | 0.814 | 0.026 | - | - | 0.931 | 0.954 | 0.486 | 1.04x | 10.8/16.4/20.5% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.845 | 0.836 | 0.008 | - | - | 0.976 | 0.979 | 0.281 | 0.89x | 10.1/14.3/16.9% | 1.3/3.5% | 3 |

> legacy-fraction=0.25: decode_failures 19

> legacy-fraction=0.5: decode_failures 37

> slower: 5.83 s per simulated hour against 1.67 over 43 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.844 | 0.834 | 0.009 | - | - | 0.951 | 0.972 | 0.150 | 1.12x | 13.1/20.8/23.4% | 1.7/5.0% | 3 |
| 0.5 | 1 | 0.841 | 0.815 | 0.025 | - | - | 0.938 | 0.959 | 0.442 | 1.04x | 11.0/16.6/20.2% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.822 | 0.812 | 0.009 | - | - | 0.953 | 0.955 | 0.238 | 0.87x | 10.2/14.3/17.2% | 1.3/3.5% | 3 |

> legacy-fraction=0.25: decode_failures 25

> legacy-fraction=0.5: decode_failures 35

> slower: 5.88 s per simulated hour against 1.71 over 43 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.824 | 0.821 | 0.004 | - | - | 0.951 | 0.951 | 0.290 | 0.69x | 7.9/12.1/13.0% | 1.0/2.8% | 3 |
| signing=true | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.855 | 0.846 | 0.009 | - | - | 0.984 | 0.986 | 0.646 | 0.74x | 8.3/12.4/15.4% | 1.2/2.2% | 3 |
| 2.5 | 1 | 0.853 | 0.842 | 0.011 | - | - | 0.980 | 0.982 | 0.637 | 0.75x | 8.2/12.4/15.3% | 1.2/2.1% | 3 |
| 2.6 | 1 | 0.848 | 0.837 | 0.010 | - | - | 0.983 | 0.985 | 0.633 | 0.74x | 8.3/12.7/15.7% | 1.2/2.2% | 3 |
| 2.7 | 1 | 0.877 | 0.871 | 0.006 | - | - | 0.976 | 0.978 | 0.685 | 0.79x | 8.5/16.3/18.4% | 1.2/3.0% | 3 |
| 2.8 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.801 | 0.795 | 0.006 | - | - | 0.931 | 0.933 | 0.272 | 0.91x | 10.3/15.0/16.1% | 1.3/3.5% | 3 |
| 900 | 1 | 0.705 | 0.696 | 0.009 | - | - | 0.851 | 0.852 | 0.250 | 1.96x | 22.2/31.9/34.8% | 2.7/7.6% | 3 |
| 300 | 1 | 0.468 | 0.451 | 0.016 | - | - | 0.674 | 0.680 | 0.170 | 4.14x | 43.9/61.4/66.6% | 6.1/15.4% | 3 |

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.949 | 0.950 | 0.314 | 0.96x | 10.6/14.9/16.0% | 1.5/3.4% | 3 |
| 900 | 1 | 0.778 | 0.773 | 0.005 | - | - | 0.871 | 0.872 | 0.332 | 2.24x | 24.6/34.4/37.0% | 3.4/8.0% | 3 |
| 300 | 1 | 0.508 | 0.498 | 0.009 | - | - | 0.679 | 0.683 | 0.261 | 4.67x | 48.4/65.7/69.8% | 6.9/16.3% | 3 |

> broadcast-interval-s=300: decode_failures 4

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.909 | 0.911 | 0.279 | 1.22x | 13.7/20.1/21.8% | 1.8/4.8% | 3 |
| sinusoid | 1 | 0.776 | 0.769 | 0.007 | - | - | 0.910 | 0.912 | 0.262 | 1.16x | 13.0/19.0/20.5% | 1.7/4.4% | 3 |
| commuter | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.705 | 0.696 | 0.009 | - | - | 0.851 | 0.852 | 0.250 | 1.96x | 22.2/31.9/34.8% | 2.7/7.6% | 3 |
| 3600 | 1 | 0.801 | 0.795 | 0.006 | - | - | 0.931 | 0.933 | 0.272 | 0.91x | 10.3/15.0/16.1% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.948 | 0.948 | 0.285 | 0.60x | 6.8/9.9/10.7% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.848 | 0.844 | 0.004 | - | - | 0.965 | 0.966 | 0.310 | 0.41x | 4.6/6.8/7.4% | 0.6/1.5% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.758 | 0.750 | 0.009 | - | - | 0.904 | 0.906 | 0.256 | 1.34x | 15.1/22.0/23.9% | 1.9/5.2% | 3 |
| 1.0 | 1 | 0.737 | 0.729 | 0.008 | - | - | 0.890 | 0.892 | 0.266 | 1.44x | 16.4/24.0/26.0% | 2.0/5.6% | 3 |
| 4.0 | 1 | 0.701 | 0.693 | 0.008 | - | - | 0.862 | 0.862 | 0.240 | 1.77x | 20.2/30.0/32.7% | 2.5/7.2% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.745 | 0.734 | 0.011 | - | - | 0.899 | 0.940 | 0.567 | 5.65x | 53.1/69.5/74.4% | 3.8/12.4% | 3 |
| 1.0 | 1 | 0.677 | 0.666 | 0.011 | - | - | 0.810 | 0.903 | 0.484 | 6.22x | 57.5/72.0/76.9% | 4.3/13.3% | 3 |

> traceroute-per-hour=0.0: decode_failures 31

> traceroute-per-hour=1.0: queue drops 14.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 48

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.684 | 0.667 | 0.017 | - | - | 0.847 | 0.897 | 0.000 | 1.31x | 16.4/23.8/27.5% | 3.2/6.2% | 3 |
| 60 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 90 | 1 | 0.918 | 0.914 | 0.004 | - | - | 0.979 | 0.980 | 0.702 | 1.61x | 16.4/24.9/28.9% | 1.4/4.9% | 3 |
| 120 | 1 | 0.944 | 0.942 | 0.003 | - | - | 0.999 | 0.999 | 0.775 | 1.98x | 19.7/28.7/32.7% | 1.2/5.0% | 3 |
| 150 | 1 | 0.953 | 0.949 | 0.004 | - | - | 0.995 | 0.995 | 0.518 | 2.58x | 24.7/38.0/43.9% | 1.3/6.0% | 3 |

> nodes=40: decode_failures 20

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 120 | 1 | 0.719 | 0.709 | 0.011 | - | - | 0.931 | 0.932 | 0.267 | 2.12x | 14.0/26.1/32.6% | 1.4/5.9% | 3 |
| 250 | 1 | 0.500 | 0.489 | 0.011 | - | - | 0.770 | 0.773 | 0.000 | 4.72x | 17.3/28.8/39.8% | 1.6/5.6% | 3 |
| 500 | 1 | 0.322 | 0.319 | 0.003 | - | - | 0.318 | 0.319 | 0.059 | 10.24x | 20.0/33.6/42.9% | 1.8/5.7% | 3 |

> nodes=250: decode_failures 3

> nodes=500: decode_failures 41

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.721 | 0.711 | 0.010 | - | - | 0.934 | 0.936 | 0.260 | 1.95x | 12.8/23.9/30.0% | 1.3/5.4% | 3 |
| 250 | 1 | 0.509 | 0.497 | 0.012 | - | - | 0.789 | 0.790 | 0.000 | 4.39x | 16.0/26.8/36.5% | 1.5/5.2% | 3 |
| 500 | 1 | 0.324 | 0.322 | 0.003 | - | - | 0.325 | 0.328 | 0.064 | 9.46x | 18.4/31.5/39.8% | 1.6/5.3% | 3 |

> nodes=250: decode_failures 8

> nodes=500: decode_failures 83

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.769 | 0.760 | 0.009 | - | - | 0.902 | 0.904 | 0.263 | 1.27x | 14.1/20.7/22.5% | 1.8/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.672 | 0.663 | 0.009 | - | - | 0.813 | 0.814 | 0.325 | 1.21x | 13.0/20.4/22.8% | 2.1/4.8% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.772 | 0.762 | 0.010 | - | - | 0.888 | 0.888 | 0.290 | 1.32x | 14.7/21.3/22.8% | 1.9/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.707 | 0.699 | 0.008 | - | - | 0.786 | 0.787 | 0.409 | 1.39x | 15.2/23.3/25.9% | 2.5/4.8% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.05 | 1 | 0.764 | 0.760 | 0.004 | - | - | 0.888 | 0.888 | 0.255 | 1.37x | 14.6/24.1/28.8% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.769 | 0.765 | 0.004 | - | - | 0.869 | 0.870 | 0.559 | 1.46x | 15.6/26.6/30.1% | 2.2/4.7% | 3 |
| 0.2 | 1 | 0.778 | 0.774 | 0.004 | - | - | 0.868 | 0.869 | 0.550 | 1.64x | 17.3/29.9/35.7% | 2.2/4.8% | 3 |

> faster: 0.841 s per simulated hour against 1.74 over 43 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| local-typical | 1 | 0.668 | 0.664 | 0.004 | - | - | 0.783 | 0.831 | 0.000 | 1.44x | 12.9/22.7/29.1% | 2.1/5.0% | 3 |
| event | 1 | 0.178 | 0.170 | 0.009 | - | - | 0.338 | 0.383 | 0.000 | 1.21x | 5.7/12.9/19.2% | 1.9/4.0% | 3 |
| backbone | 1 | 0.971 | 0.970 | 0.001 | - | - | 1.000 | 1.000 | 0.763 | 1.10x | 22.6/30.7/33.4% | 1.3/5.4% | 3 |

> siting-mix=local-typical: decode_failures 43

> siting-mix=event: decode_failures 5

> slower: 4.71 s per simulated hour against 1.92 over 42 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.839 | 0.823 | 0.016 | - | - | 0.956 | 0.962 | 0.547 | 1.47x | 22.8/31.4/34.4% | 3.2/7.5% | 3 |
| 60 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 90 | 1 | 0.802 | 0.793 | 0.009 | - | - | 0.962 | 0.962 | 0.434 | 1.60x | 14.8/20.8/22.9% | 1.6/4.9% | 3 |
| 120 | 1 | 0.719 | 0.709 | 0.011 | - | - | 0.931 | 0.932 | 0.267 | 2.12x | 14.0/26.1/32.6% | 1.4/5.9% | 3 |
| 150 | 1 | 0.667 | 0.651 | 0.016 | - | - | 0.790 | 0.791 | 0.108 | 2.72x | 15.8/23.8/30.0% | 1.5/5.6% | 3 |

> nodes=150: decode_failures 4

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 1.25 | 1 | 0.477 | 0.468 | 0.009 | - | - | 0.730 | 0.733 | 0.150 | 1.27x | 9.7/17.5/20.6% | 1.9/5.0% | 3 |
| 1.5 | 1 | 0.260 | 0.250 | 0.010 | - | - | 0.504 | 0.509 | 0.000 | 1.22x | 6.7/15.4/22.7% | 1.6/4.8% | 3 |
| 2.0 | 1 | 0.107 | 0.106 | 0.001 | - | - | 0.267 | 0.277 | 0.000 | 0.76x | 3.4/6.8/8.3% | 1.2/2.5% | 3 |

> stretch=2.0: decode_failures 1

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| clustered | 1 | 0.865 | 0.864 | 0.001 | - | - | 0.915 | 0.916 | 0.458 | 1.14x | 22.9/34.2/35.5% | 1.4/5.3% | 3 |
| corridor | 1 | 0.628 | 0.613 | 0.015 | - | - | 0.670 | 0.782 | 0.343 | 1.30x | 14.3/25.7/28.3% | 1.9/5.4% | 3 |
| hub | 1 | 0.902 | 0.902 | 0.001 | - | - | 0.955 | 0.955 | 0.708 | 1.20x | 27.3/36.2/37.5% | 1.7/5.4% | 3 |

> topology=corridor: decode_failures 17

> topology=hub: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.730 | 0.730 | 0.000 | - | - | 0.888 | 0.890 | 0.270 | 1.48x | 16.9/24.7/26.8% | 2.1/5.8% | 3 |
| True | 1 | 0.731 | 0.731 | 0.000 | - | - | 0.892 | 0.893 | 0.268 | 1.49x | 16.9/24.8/26.8% | 2.1/5.9% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.731 | 0.731 | 0.000 | - | - | 0.892 | 0.893 | 0.268 | 1.49x | 16.9/24.8/26.8% | 2.1/5.9% | 3 |
| m4-early-flood | 1 | 0.727 | 0.727 | 0.000 | - | - | 0.882 | 0.885 | 0.282 | 1.48x | 16.9/24.8/26.8% | 2.1/6.0% | 3 |

> faster: 1.28 s per simulated hour against 2.82 over 43 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.765 | 0.765 | 0.000 | - | - | 0 | 0.000 | 0.277 | 1.25x | 13.9/20.3/22.0% | 1.8/4.8% | 3 |
| chain | 1 | 0.740 | 0.739 | 0.001 | - | - | 0.835 | 0.892 | 0.248 | 1.45x | 16.5/24.2/26.3% | 2.1/5.7% | 3 |
| sr | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| True | 1 | 0.773 | 0.765 | 0.008 | - | - | 0.912 | 0.912 | 0.288 | 1.28x | 14.4/21.0/22.7% | 1.8/4.9% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.944 | 0.942 | 0.003 | - | - | 0.999 | 0.999 | 0.775 | 1.98x | 19.7/28.7/32.7% | 1.2/5.0% | 3 |
| True | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.999 | 0.999 | 0.786 | 1.99x | 19.7/28.9/32.9% | 1.3/5.0% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.138 | 0.137 | 0.001 | - | - | 0.291 | 0.293 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.288 | 0.285 | 0.004 | - | - | 0.474 | 0.576 | 0.000 | 0.21x | 1.1/3.0/3.7% | 0.3/0.9% | 3 |
| LONG_TURBO | 1 | 0.666 | 0.660 | 0.006 | - | - | 0.835 | 0.836 | 0.197 | 1.23x | 11.1/16.7/18.8% | 1.7/4.5% | 3 |

> preset=MEDIUM_TURBO: decode_failures 13

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.772 | 0.764 | 0.008 | - | - | 0.901 | 0.903 | 0.294 | 1.22x | 15.2/21.6/23.3% | 1.8/4.9% | 3 |
| 1.0 | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.962 | 0.963 | 0.628 | 0.94x | 19.8/24.4/27.6% | 1.2/4.9% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.235 | 0.232 | 0.003 | - | - | 0.470 | 0.479 | 0.000 | 0.11x | 0.6/1.3/1.9% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| LITE_FAST | 1 | 0.660 | 0.654 | 0.006 | - | - | 0.857 | 0.857 | 0.164 | 0.94x | 9.3/13.6/18.7% | 1.4/3.7% | 3 |
| NARROW_SLOW | 1 | 0.709 | 0.704 | 0.005 | - | - | 0.864 | 0.865 | 0.438 | 1.23x | 12.0/18.4/23.2% | 1.8/4.7% | 3 |

> preset=SHORT_FAST: decode_failures 2

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| temporal | 1 | 0.631 | 0.621 | 0.010 | - | - | 0.831 | 0.833 | 0.229 | 1.22x | 13.0/19.7/22.1% | 1.8/4.6% | 3 |
| transient | 1 | 0.763 | 0.756 | 0.007 | - | - | 0.913 | 0.914 | 0.278 | 1.27x | 14.3/20.9/22.6% | 1.8/4.9% | 3 |
| periodic | 1 | 0.597 | 0.589 | 0.008 | - | - | 0.732 | 0.742 | 0.198 | 1.19x | 13.5/19.5/21.4% | 1.8/4.3% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.235 | 0.232 | 0.003 | - | - | 0.470 | 0.479 | 0.000 | 0.11x | 0.6/1.3/1.9% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| LONG_MODERATE | 1 | 0.754 | 0.742 | 0.011 | - | - | 0.874 | 0.885 | 0.244 | 3.29x | 42.7/55.9/59.2% | 4.9/12.3% | 3 |

> preset=SHORT_FAST: decode_failures 2

> preset=LONG_MODERATE: decode_failures 6

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.064 | 0.063 | 0.001 | - | - | 0.191 | 0.194 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.138 | 0.137 | 0.001 | - | - | 0.291 | 0.293 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| LONG_TURBO | 1 | 0.666 | 0.660 | 0.006 | - | - | 0.835 | 0.836 | 0.197 | 1.23x | 11.1/16.7/18.8% | 1.7/4.5% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.758 | 0.751 | 0.007 | - | - | 0.891 | 0.891 | 0.202 | 1.79x | 18.3/24.8/31.4% | 2.6/6.6% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.701 | 0.693 | 0.007 | - | - | 0.850 | 0.854 | 0.240 | 1.25x | 14.3/20.7/22.4% | 1.8/4.7% | 3 |
| 10000 | 1 | 0.597 | 0.589 | 0.008 | - | - | 0.732 | 0.742 | 0.198 | 1.19x | 13.5/19.5/21.4% | 1.8/4.3% | 3 |
| 4000 | 1 | 0.339 | 0.336 | 0.004 | - | - | 0.449 | 0.510 | 0.118 | 1.00x | 11.3/16.9/18.5% | 1.5/3.2% | 3 |
| 2000 | 1 | 0.070 | 0.070 | 0.000 | - | - | 0.095 | 0.147 | 0.022 | 0.69x | 8.0/11.8/13.1% | 1.1/1.8% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 6

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.260 | 0.250 | 0.010 | - | - | 0.504 | 0.509 | 0.000 | 1.22x | 6.7/15.4/22.7% | 1.6/4.8% | 3 |
| 1.0 | 1 | 0.618 | 0.608 | 0.009 | - | - | 0.779 | 0.780 | 0.369 | 0.94x | 11.7/19.7/22.1% | 1.3/4.1% | 3 |

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 22 | 1 | 0.273 | 0.264 | 0.009 | - | - | 0.449 | 0.533 | 0.000 | 1.24x | 7.9/15.0/18.8% | 1.9/4.8% | 3 |
| 17 | 1 | 0.128 | 0.127 | 0.001 | - | - | 0.264 | 0.264 | 0.000 | 0.82x | 4.3/7.4/9.8% | 1.2/3.2% | 3 |
| 14 | 1 | 0.083 | 0.081 | 0.002 | - | - | 0.167 | 0.203 | 0.000 | 0.64x | 2.9/5.5/6.4% | 0.9/1.9% | 3 |

> tx-power=22: decode_failures 12

> tx-power=17: decode_failures 1

> tx-power=14: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.944 | 0.942 | 0.003 | - | - | 0.999 | 0.999 | 0.775 | 1.98x | 19.7/28.7/32.7% | 1.2/5.0% | 3 |
| True | 1 | 0.940 | 0.937 | 0.002 | - | - | 0.998 | 0.998 | 0.764 | 2.36x | 23.6/32.9/37.0% | 1.5/5.6% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.776 | 0.773 | 0.004 | - | - | 0.917 | 0.917 | 0.232 | 1.32x | 14.4/22.7/26.8% | 1.8/5.0% | 3 |
| True | 1 | 0.797 | 0.793 | 0.003 | - | - | 0.900 | 0.900 | 0.230 | 1.38x | 15.4/23.2/27.1% | 1.8/5.0% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| random | 1 | 0.747 | 0.734 | 0.013 | - | - | 0.874 | 0.879 | 0.240 | 1.28x | 14.3/20.8/22.5% | 1.8/4.8% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.602 | 0.573 | 0.029 | - | - | 0.876 | 0.883 | 0.198 | 0.94x | 11.0/17.0/18.8% | 1.3/4.0% | 3 |
| 7 | 1 | 0.842 | 0.838 | 0.004 | - | - | 0.920 | 0.921 | 0.332 | 1.42x | 15.8/22.1/23.8% | 2.2/5.1% | 3 |
| 15 | 1 | 0.858 | 0.854 | 0.003 | - | - | 0.915 | 0.915 | 0.340 | 1.43x | 15.9/22.0/23.7% | 2.2/5.0% | 3 |
| 32 | 1 | 0.858 | 0.856 | 0.002 | - | - | 0.908 | 0.910 | 0.364 | 1.43x | 15.8/22.1/23.7% | 2.2/5.0% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.602 | 0.573 | 0.029 | - | - | 0.876 | 0.883 | 0.198 | 0.94x | 11.0/17.0/18.8% | 1.3/4.0% | 3 |
| 5 | 1 | 0.782 | 0.773 | 0.009 | - | - | 0.916 | 0.916 | 0.288 | 1.27x | 14.1/20.6/22.3% | 1.8/4.8% | 3 |
| 7 | 1 | 0.842 | 0.838 | 0.004 | - | - | 0.920 | 0.921 | 0.332 | 1.42x | 15.8/22.1/23.8% | 2.2/5.1% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| KNOWN_ONLY | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.766 | 0.766 | 0.000 | - | - | 0.846 | 0.911 | 0.260 | 1.23x | 13.7/19.8/21.7% | 1.8/4.7% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.602 | 0.573 | 0.029 | - | - | 0.876 | 0.883 | 0.198 | 0.94x | 11.0/17.0/18.8% | 1.3/4.0% | 3 |
| True | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| BALANCED | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| STRICT | 1 | 0.619 | 0.619 | 0.000 | - | - | 0.761 | 0.764 | 0.180 | 1.38x | 15.6/22.6/24.4% | 2.1/5.3% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| dm | 1 | 0.766 | 0.760 | 0.007 | - | - | 0.912 | 0.912 | 0.276 | 1.25x | 14.0/20.5/22.4% | 1.9/4.8% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.757 | 0.751 | 0.006 | - | - | 0.895 | 0.896 | 0.275 | 1.28x | 14.5/21.1/22.8% | 1.8/5.0% | 3 |
| local | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| time | 1 | 0.748 | 0.740 | 0.008 | - | - | 0.896 | 0.899 | 0.271 | 1.30x | 14.7/21.3/23.1% | 1.9/5.0% | 3 |
| window | 1 | 0.764 | 0.757 | 0.007 | - | - | 0.910 | 0.913 | 0.253 | 1.25x | 14.1/20.5/22.3% | 1.8/4.8% | 3 |

> bucket-mode=global: misdecodes 44

> bucket-mode=time: misdecodes 33

> bucket-mode=window: misdecodes 14

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.751 | 0.743 | 0.008 | - | - | 0.898 | 0.901 | 0.258 | 1.42x | 16.0/23.5/25.6% | 2.1/5.5% | 3 |
| 1800 | 1 | 0.748 | 0.740 | 0.008 | - | - | 0.896 | 0.899 | 0.271 | 1.30x | 14.7/21.3/23.1% | 1.9/5.0% | 3 |
| 3600 | 1 | 0.758 | 0.752 | 0.006 | - | - | 0.900 | 0.904 | 0.250 | 1.28x | 14.5/21.0/22.9% | 1.8/5.0% | 3 |

> time-bucket-s=600: misdecodes 139

> time-bucket-s=1800: misdecodes 33

> time-bucket-s=3600: misdecodes 8

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| interval | 1 | 0.737 | 0.728 | 0.009 | - | - | 0.891 | 0.893 | 0.257 | 1.70x | 19.5/28.9/31.4% | 2.5/6.7% | 3 |
| aimd | 1 | 0.759 | 0.756 | 0.003 | - | - | 0.870 | 0.916 | 0.267 | 1.29x | 14.5/21.1/22.8% | 1.9/4.9% | 3 |
| bucket+interval | 1 | 0.734 | 0.726 | 0.009 | - | - | 0.879 | 0.880 | 0.257 | 1.72x | 19.8/29.5/32.1% | 2.5/7.0% | 3 |

> trigger=interval: misdecodes 4

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 4

> trigger=bucket+interval: misdecodes 16

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.762 | 0.756 | 0.006 | - | - | 0.904 | 0.913 | 0.281 | 1.26x | 14.1/20.8/22.6% | 1.9/4.8% | 3 |
| 8 | 1 | 0.768 | 0.762 | 0.006 | - | - | 0.911 | 0.913 | 0.256 | 1.26x | 14.2/20.7/22.6% | 1.8/4.9% | 3 |
| 16 | 1 | 0.759 | 0.752 | 0.007 | - | - | 0.902 | 0.904 | 0.273 | 1.26x | 14.0/20.5/22.2% | 1.8/4.8% | 3 |
| 32 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 50 | 1 | 0.768 | 0.760 | 0.008 | - | - | 0.922 | 0.924 | 0.266 | 1.27x | 14.3/20.9/22.6% | 1.8/4.9% | 3 |

> capacity=4: decode_failures 87

> capacity=8: decode_failures 34

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.762 | 0.756 | 0.006 | - | - | 0.904 | 0.913 | 0.281 | 1.26x | 14.1/20.8/22.6% | 1.9/4.8% | 3 |
| 8 | 1 | 0.768 | 0.762 | 0.006 | - | - | 0.911 | 0.913 | 0.256 | 1.26x | 14.2/20.7/22.6% | 1.8/4.9% | 3 |
| 16 | 1 | 0.759 | 0.752 | 0.007 | - | - | 0.902 | 0.904 | 0.273 | 1.26x | 14.0/20.5/22.2% | 1.8/4.8% | 3 |
| 32 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 50 | 1 | 0.768 | 0.760 | 0.008 | - | - | 0.922 | 0.924 | 0.266 | 1.27x | 14.3/20.9/22.6% | 1.8/4.9% | 3 |

> capacity=4: decode_failures 87

> capacity=8: decode_failures 34

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.771 | 0.765 | 0.006 | - | - | 0.912 | 0.916 | 0.246 | 1.26x | 14.1/20.6/22.4% | 1.8/4.9% | 3 |
| 16 | 1 | 0.772 | 0.766 | 0.006 | - | - | 0.916 | 0.917 | 0.286 | 1.25x | 14.1/20.4/22.2% | 1.8/4.8% | 3 |
| 32 | 1 | 0.764 | 0.757 | 0.007 | - | - | 0.910 | 0.913 | 0.253 | 1.25x | 14.1/20.5/22.3% | 1.8/4.8% | 3 |

> capacity=8: misdecodes 24

> capacity=8: decode_failures 13

> capacity=16: misdecodes 6

> capacity=32: misdecodes 14

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.734 | 0.726 | 0.009 | - | - | 0.879 | 0.880 | 0.257 | 1.72x | 19.8/29.5/32.1% | 2.5/7.0% | 3 |
| 02-06 | 1 | 0.768 | 0.765 | 0.004 | - | - | 0.884 | 0.918 | 0.291 | 1.30x | 14.7/21.5/23.3% | 1.9/5.0% | 3 |
| 00-08 | 1 | 0.752 | 0.747 | 0.005 | - | - | 0.873 | 0.901 | 0.266 | 1.37x | 15.5/23.0/25.1% | 2.0/5.4% | 3 |

> catch-up-hours=: misdecodes 16

> catch-up-hours=02-06: decode_failures 32

> catch-up-hours=00-08: decode_failures 31

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.761 | 0.758 | 0.003 | - | - | 0.896 | 0.897 | 0.250 | 1.26x | 14.3/20.8/22.6% | 1.8/4.9% | 3 |
| 2 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 3 | 1 | 0.792 | 0.774 | 0.018 | - | - | 0.887 | 0.953 | 0.281 | 1.26x | 14.0/20.5/22.4% | 1.8/4.9% | 3 |
| 4 | 1 | 0.789 | 0.760 | 0.029 | - | - | 0.837 | 0.930 | 0.275 | 1.28x | 14.1/20.8/22.8% | 1.9/5.0% | 3 |

> hops-apart=3: decode_failures 28

> hops-apart=4: decode_failures 24

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.761 | 0.758 | 0.003 | - | - | 0.896 | 0.897 | 0.250 | 1.26x | 14.3/20.8/22.6% | 1.8/4.9% | 3 |
| 2 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 3 | 1 | 0.792 | 0.774 | 0.018 | - | - | 0.887 | 0.953 | 0.281 | 1.26x | 14.0/20.5/22.4% | 1.8/4.9% | 3 |
| 4 | 1 | 0.789 | 0.760 | 0.029 | - | - | 0.837 | 0.930 | 0.275 | 1.28x | 14.1/20.8/22.8% | 1.9/5.0% | 3 |
| 5 | 1 | 0.763 | 0.746 | 0.017 | - | - | 0.696 | 0.911 | 0.281 | 1.26x | 14.0/20.5/22.4% | 1.9/5.0% | 3 |

> hops-apart=3: decode_failures 28

> hops-apart=4: decode_failures 24

> hops-apart=5: decode_failures 23

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.908 | 0.909 | 0.255 | 1.29x | 14.4/21.1/22.9% | 1.8/5.0% | 3 |
| 30 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 120 | 1 | 0.771 | 0.765 | 0.006 | - | - | 0.921 | 0.923 | 0.257 | 1.27x | 14.2/20.7/22.5% | 1.8/4.9% | 3 |
| 600 | 1 | 0.770 | 0.764 | 0.006 | - | - | 0.919 | 0.919 | 0.270 | 1.25x | 14.1/20.5/22.2% | 1.8/4.8% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.908 | 0.909 | 0.255 | 1.29x | 14.4/21.1/22.9% | 1.8/5.0% | 3 |
| 30 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 120 | 1 | 0.771 | 0.765 | 0.006 | - | - | 0.921 | 0.923 | 0.257 | 1.27x | 14.2/20.7/22.5% | 1.8/4.9% | 3 |
| 600 | 1 | 0.770 | 0.764 | 0.006 | - | - | 0.919 | 0.919 | 0.270 | 1.25x | 14.1/20.5/22.2% | 1.8/4.8% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.787 | 0.754 | 0.033 | - | - | 0.759 | 0.936 | 0.280 | 1.30x | 14.6/20.9/23.1% | 1.9/5.0% | 3 |
| routers | 1 | 0.759 | 0.752 | 0.007 | - | - | 0.907 | 0.911 | 0.263 | 1.26x | 14.2/20.7/22.5% | 1.8/4.9% | 3 |
| alternate-routers | 1 | 0.779 | 0.768 | 0.011 | - | - | 0.927 | 0.932 | 0.298 | 1.26x | 14.3/20.6/22.5% | 1.8/4.8% | 3 |
| beside-router | 1 | 0.786 | 0.771 | 0.015 | - | - | 0.938 | 0.939 | 0.275 | 1.27x | 14.3/20.7/22.8% | 1.8/4.9% | 3 |
| random-clients | 1 | 0.789 | 0.759 | 0.031 | - | - | 0.926 | 0.929 | 0.285 | 1.27x | 14.4/20.9/22.9% | 1.8/5.0% | 3 |
| hops-apart | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

> place=spread: decode_failures 23

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.787 | 0.754 | 0.033 | - | - | 0.759 | 0.936 | 0.280 | 1.30x | 14.6/20.9/23.1% | 1.9/5.0% | 3 |
| routers | 1 | 0.759 | 0.752 | 0.007 | - | - | 0.907 | 0.911 | 0.263 | 1.26x | 14.2/20.7/22.5% | 1.8/4.9% | 3 |
| alternate-routers | 1 | 0.779 | 0.768 | 0.011 | - | - | 0.927 | 0.932 | 0.298 | 1.26x | 14.3/20.6/22.5% | 1.8/4.8% | 3 |
| beside-router | 1 | 0.786 | 0.771 | 0.015 | - | - | 0.938 | 0.939 | 0.275 | 1.27x | 14.3/20.7/22.8% | 1.8/4.9% | 3 |
| random-clients | 1 | 0.789 | 0.759 | 0.031 | - | - | 0.926 | 0.929 | 0.285 | 1.27x | 14.4/20.9/22.9% | 1.8/5.0% | 3 |
| hops-apart | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

> place=spread: decode_failures 23

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| broadcast | 1 | 0.785 | 0.747 | 0.038 | - | - | 0.901 | 0.904 | 0.319 | 1.33x | 15.1/21.8/23.6% | 1.9/5.2% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| heard | 1 | 0.765 | 0.758 | 0.007 | - | - | 0.916 | 0.917 | 0.274 | 1.26x | 14.2/20.6/22.4% | 1.8/4.9% | 3 |

> replay-ordering=heard: misdecodes 8

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.785 | 0.747 | 0.038 | - | - | 0.901 | 0.904 | 0.319 | 1.33x | 15.1/21.8/23.6% | 1.9/5.2% | 3 |
| heard | 1 | 0.793 | 0.755 | 0.039 | - | - | 0.912 | 0.912 | 0.338 | 1.32x | 14.9/21.5/23.3% | 1.9/5.1% | 3 |

> replay-ordering=heard: misdecodes 9

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| enum | 1 | 0.762 | 0.757 | 0.005 | - | - | 0.898 | 0.901 | 0.258 | 1.26x | 14.3/20.9/22.8% | 1.9/4.8% | 3 |
| hybrid | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.759 | 0.752 | 0.007 | - | - | 0.907 | 0.911 | 0.263 | 1.26x | 14.2/20.7/22.5% | 1.8/4.9% | 3 |
| 6 | 1 | 0.774 | 0.757 | 0.017 | - | - | 0.931 | 0.934 | 0.258 | 1.28x | 14.3/21.1/22.9% | 1.8/5.2% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.762 | 0.758 | 0.004 | - | - | 0.892 | 0.893 | 0.273 | 1.26x | 14.1/20.6/22.3% | 1.8/4.9% | 2 |
| 3 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 5 | 1 | 0.768 | 0.761 | 0.006 | - | - | 0.915 | 0.916 | 0.277 | 1.30x | 14.7/21.3/23.1% | 1.9/5.0% | 5 |
| 8 | 1 | 0.763 | 0.754 | 0.009 | - | - | 0.903 | 0.906 | 0.293 | 1.32x | 15.0/21.7/23.5% | 1.9/5.1% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.762 | 0.758 | 0.004 | - | - | 0.892 | 0.893 | 0.273 | 1.26x | 14.1/20.6/22.3% | 1.8/4.9% | 2 |
| 3 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 5 | 1 | 0.768 | 0.761 | 0.006 | - | - | 0.915 | 0.916 | 0.277 | 1.30x | 14.7/21.3/23.1% | 1.9/5.0% | 5 |
| 8 | 1 | 0.763 | 0.754 | 0.009 | - | - | 0.903 | 0.906 | 0.293 | 1.32x | 15.0/21.7/23.5% | 1.9/5.1% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| True | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.767 | 0.759 | 0.008 | - | - | 0.911 | 0.917 | 0.258 | 1.19x | 13.3/19.4/21.0% | 1.7/4.5% | 3 |
| 1 | 1 | 0.766 | 0.759 | 0.007 | - | - | 0.906 | 0.907 | 0.283 | 1.19x | 13.5/19.6/21.2% | 1.7/4.6% | 3 |
| 2 | 1 | 0.774 | 0.768 | 0.007 | - | - | 0.908 | 0.912 | 0.290 | 1.19x | 13.4/19.5/21.1% | 1.7/4.6% | 3 |
| 4 | 1 | 0.766 | 0.758 | 0.007 | - | - | 0.901 | 0.903 | 0.265 | 1.21x | 13.6/19.8/21.4% | 1.7/4.6% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.913 | 0.913 | 0.270 | 1.25x | 14.1/20.6/22.3% | 1.8/4.8% | 3 |
| 24 | 1 | 0.763 | 0.757 | 0.005 | - | - | 0.900 | 0.903 | 0.274 | 1.27x | 14.3/20.8/22.5% | 1.9/4.9% | 3 |
| 32 | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.899 | 0.902 | 0.268 | 1.25x | 14.0/20.4/22.3% | 1.8/4.8% | 3 |
| 64 | 1 | 0.763 | 0.756 | 0.007 | - | - | 0.911 | 0.911 | 0.261 | 1.26x | 14.1/20.6/22.2% | 1.8/4.8% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.764 | 0.755 | 0.008 | - | - | 0.912 | 0.914 | 0.264 | 1.33x | 15.0/21.8/23.6% | 1.9/5.1% | 3 |
| 16 | 1 | 0.765 | 0.758 | 0.007 | - | - | 0.911 | 0.914 | 0.258 | 1.28x | 14.5/20.9/22.8% | 1.8/5.0% | 3 |
| 32 | 1 | 0.764 | 0.757 | 0.007 | - | - | 0.910 | 0.913 | 0.253 | 1.25x | 14.1/20.5/22.3% | 1.8/4.8% | 3 |

> window-size=8: misdecodes 128

> window-size=16: misdecodes 56

> window-size=32: misdecodes 14

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.944 | 0.942 | 0.003 | - | - | 0.999 | 0.999 | 0.775 | 1.98x | 19.7/28.7/32.7% | 1.2/5.0% | 3 |
| True | 1 | 0.742 | 0.729 | 0.013 | - | - | 0.895 | 0.938 | 0.564 | 5.68x | 53.3/69.6/74.6% | 3.8/12.4% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: decode_failures 50

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.509 | 0.497 | 0.012 | - | - | 0.789 | 0.790 | 0.000 | 4.39x | 16.0/26.8/36.5% | 1.5/5.2% | 3 |
| truesize | 1 | 0.540 | 0.529 | 0.011 | - | - | 0.827 | 0.829 | 0.000 | 3.31x | 11.9/20.6/28.5% | 1.1/4.1% | 3 |

> congestion-input=hotstore: decode_failures 8

> congestion-input=truesize: decode_failures 3

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.949 | 0.947 | 0.002 | - | - | 0.997 | 0.998 | 0.771 | 1.86x | 18.6/27.1/30.8% | 1.2/4.6% | 3 |
| adaptive | 1 | 0.944 | 0.942 | 0.003 | - | - | 0.999 | 0.999 | 0.775 | 1.98x | 19.7/28.7/32.7% | 1.2/5.0% | 3 |

> congestion-mode=adaptive: misdecodes 1

