# Sweep blocks-2026-08-29-3120871

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 3120871 · seeds 3120871
- **blocks** 87 run
- **compute** 8.6 h of simulator time across every cell
- **generated** 2026-08-29T09:54:04+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>89 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 38
- AD-amplify-worst: slower: 4.39 s per simulated hour against 1.67 over 8 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=inverse: decode_failures 9
- DB-hotstore: max-num-nodes=10: decode_failures 14
- DB-hotstore-stress: max-num-nodes=10: decode_failures 60
- DB-platform: platform-mix=constrained: decode_failures 3
- DB-warm: warm-num-nodes=0: decode_failures 33
- DB-warm: warm-num-nodes=25: decode_failures 33
- DB-warm: warm-num-nodes=100: decode_failures 33
- DB-warm: warm-num-nodes=2000: decode_failures 33
- DG-burst: burst-loss=0.1: decode_failures 2
- DG-burst: burst-loss=0.2: decode_failures 10
- DG-burst: burst-loss=0.3: decode_failures 31
- DG-outage: burst-loss=0.1: decode_failures 22
- DG-outage: burst-loss=0.2: decode_failures 22
- DG-outage: burst-loss=0.3: decode_failures 29
- DM-mode: dm-mode=flood-only: decode_failures 5
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 2
- DM-mode: dm-mode=m4-early-flood: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 7
- LD-chatty: broadcast-interval-s=300: decode_failures 10
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 33
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 20
- LD-traceroute-small: faster: 18 s per simulated hour against 37.2 over 8 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-density: nodes=40: decode_failures 6
- MS-density: nodes=150: misdecodes 1
- MS-hopscale: nodes=500: decode_failures 14
- MS-oversubscribed: nodes=120: decode_failures 2
- MS-oversubscribed: nodes=500: decode_failures 6
- MS-siting: siting-mix=event: decode_failures 4
- MS-size: nodes=90: decode_failures 76
- MS-size: slower: 7.48 s per simulated hour against 3.25 over 8 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.25: decode_failures 4
- MS-topology: topology=clustered: misdecodes 1
- PR-crladder: coding-rate-ladder=False: decode_failures 2
- PR-crladder: coding-rate-ladder=True: decode_failures 8
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 8
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 3
- RF-bw500: faster: 0.681 s per simulated hour against 2.04 over 8 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-eu-presets: preset=SHORT_FAST: decode_failures 1
- RF-noise: noise-profile=temporal: decode_failures 16
- RF-noise: noise-profile=periodic: decode_failures 2
- RF-preset: preset=SHORT_FAST: decode_failures 1
- RF-preset: preset=LONG_MODERATE: decode_failures 24
- RF-preset-turbo: faster: 0.823 s per simulated hour against 1.65 over 4 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 2
- RF-stretch-duct: faster: 1.13 s per simulated hour against 2.35 over 8 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=14: decode_failures 1
- RT-hoplimit: hop-limit=3: decode_failures 5
- RT-hopspread: hop-limit=3: decode_failures 5
- RT-spread: hop-spread=False: decode_failures 5
- SF-bucket-mode: bucket-mode=global: misdecodes 21
- SF-bucket-mode: bucket-mode=time: misdecodes 25
- SF-bucket-mode: bucket-mode=window: misdecodes 12
- SF-bucket-time: time-bucket-s=600: misdecodes 108
- SF-bucket-time: time-bucket-s=1800: misdecodes 25
- SF-bucket-time: time-bucket-s=3600: misdecodes 12
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 16
- SF-capacity-local: capacity=4: decode_failures 76
- SF-capacity-local: capacity=8: decode_failures 66
- SF-capacity-local: capacity=16: decode_failures 8
- SF-capacity: capacity=4: decode_failures 76
- SF-capacity: capacity=8: decode_failures 66
- SF-capacity: capacity=16: decode_failures 8
- SF-capacity-window: capacity=8: misdecodes 11
- SF-capacity-window: capacity=8: decode_failures 61
- SF-capacity-window: capacity=16: misdecodes 8
- SF-capacity-window: capacity=16: decode_failures 12
- SF-capacity-window: capacity=32: misdecodes 12
- SF-catchup: catch-up-hours=: misdecodes 16
- SF-catchup: catch-up-hours=02-06: decode_failures 6
- SF-catchup: catch-up-hours=00-08: decode_failures 6
- SF-catchup: faster: 4.27 s per simulated hour against 9.6 over 8 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: hops-apart=4: decode_failures 23
- SF-hops-spread: hops-apart=4: decode_failures 23
- SF-hops-spread: hops-apart=5: decode_failures 7
- SF-place-flat: place=spread: decode_failures 11
- SF-place-flat: place=random-clients: decode_failures 7
- SF-place-spread: place=spread: decode_failures 11
- SF-place-spread: place=random-clients: decode_failures 7
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 4
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-window-size: window-size=8: misdecodes 105
- SF-window-size: window-size=16: misdecodes 38
- SF-window-size: window-size=32: misdecodes 12
- TH-congestion: no-congestion-scaling=True: decode_failures 1
- TH-congestion: faster: 6.61 s per simulated hour against 20 over 8 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-amplify-worst` | 4.39 | 1.67 | 2.63x | 8 |
| `MS-size` | 7.48 | 3.25 | 2.30x | 8 |
| `PR-dmmode-cr` | 4.25 | 2.57 | 1.66x | 8 |
| `DB-warm` | 22.2 | 33.9 | 0.66x | 8 |
| `LD-chatty` | 2.95 | 4.57 | 0.65x | 8 |
| `DB-hotstore-stress` | 16.7 | 26.3 | 0.64x | 8 |
| `SF-place-flat` | 2.27 | 3.66 | 0.62x | 8 |
| `SF-replay-order-broadcast` | 1.19 | 1.99 | 0.60x | 8 |
| `TH-congestion-input` | 8.86 | 15.4 | 0.57x | 8 |
| `MS-hopscale` | 10.8 | 19.2 | 0.56x | 8 |
| `BL-control` | 1 | 1.83 | 0.55x | 8 |
| `RF-pulse` | 0.921 | 1.69 | 0.55x | 8 |
| `SF-hops-spread` | 2.59 | 4.83 | 0.54x | 8 |
| `SF-place-spread` | 1.86 | 3.52 | 0.53x | 8 |
| `RF-txpower` | 0.819 | 1.61 | 0.51x | 8 |
| `RF-preset-turbo` | 0.823 | 1.65 | 0.50x | 4 |
| `LD-traceroute-small` | 18 | 37.2 | 0.48x | 8 |
| `RF-stretch-duct` | 1.13 | 2.35 | 0.48x | 8 |
| `SF-catchup` | 4.27 | 9.6 | 0.44x | 8 |
| `RF-bw500` | 0.681 | 2.04 | 0.33x | 8 |
| `TH-congestion` | 6.61 | 19.9 | 0.33x | 8 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `MS-siting` | siting-mix | **text** | 0.075 → 0.960 | 0.886 | 0.074 → 0.955 | 8.8x sr_airtime | up | 4 |
| `PR-protocol` | protocol | **held** | 0 → 0.882 | 0.882 | 0.674 → 0.706 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.870 | 0.870 | 0.696 → 0.706 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.049 → 0.882 | 0.833 | 0.028 → 0.703 | 36x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.079 → 0.882 | 0.803 | 0.046 → 0.703 | 15x advert_bytes | down | 4 |
| `MS-stretch` | stretch | **held** | 0.102 → 0.882 | 0.780 | 0.070 → 0.703 | 26x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.149 → 0.882 | 0.733 | 0.132 → 0.703 | 5.9x advert_bytes | up | 4 |
| `RF-preset` | preset | **held** | 0.149 → 0.882 | 0.733 | 0.132 → 0.703 | 5.9x sr_airtime | up | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.081 → 0.810 | 0.729 | 0.065 → 0.633 | 2.5e+02x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.121 → 0.795 | 0.674 | 0.091 → 0.560 | 6.8x advert_bytes | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.213 → 0.867 | 0.654 | 0.071 → 0.680 | 6.7x sr_bytes | down | 3 |
| `MS-topology` | topology | **text** | 0.429 → 0.946 | 0.517 | 0.421 → 0.946 | 2.2x sr_airtime | up | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.178 → 0.643 | 0.464 | 0.176 → 0.637 | 4x sr_airtime | up | 2 |
| `MS-hopscale` | nodes | **held** | 0.448 → 0.882 | 0.433 | 0.309 → 0.703 | 9x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.451 → 0.853 | 0.402 | 0.313 → 0.578 | 4.7x bytes_on_air | down | 3 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.547 → 0.894 | 0.347 | 0.427 → 0.722 | 9.2x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.465 → 0.806 | 0.340 | 0.453 → 0.802 | 8.4x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.624 → 0.944 | 0.320 | 0.693 → 0.709 | 4.1x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.624 → 0.944 | 0.320 | 0.693 → 0.709 | 4.1x sr_bytes | up | 6 |
| `DG-burst` | burst-loss | **text** | 0.417 → 0.713 | 0.296 | 0.384 → 0.703 | 1.9x sr_bytes | down | 4 |
| `DG-outage` | burst-loss | **text** | 0.420 → 0.713 | 0.292 | 0.396 → 0.703 | 2.1x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.661 → 0.936 | 0.276 | 0.637 → 0.934 | 4.4x advert_bytes | up | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.453 → 0.719 | 0.266 | 0.306 → 0.505 | 6.3x sr_airtime | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.621 → 0.876 | 0.255 | 0.437 → 0.680 | 1.6x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.549 → 0.801 | 0.252 | 0.523 → 0.800 | 2.1x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.549 → 0.768 | 0.219 | 0.523 → 0.764 | 1.8x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.702 → 0.917 | 0.215 | 0.697 → 0.916 | 4.5x sr_airtime | down | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.678 → 0.882 | 0.204 | 0.689 → 0.703 | 3.8x sr_bytes | down | 5 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.713 → 0.906 | 0.193 | 0.703 → 0.898 | 1.2x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.689 → 0.882 | 0.193 | 0.535 → 0.703 | 1.5x sr_bytes | down | 4 |
| `MS-size` | nodes | **text** | 0.587 → 0.769 | 0.182 | 0.574 → 0.748 | 5x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.549 → 0.713 | 0.164 | 0.523 → 0.703 | 1.4x sr_bytes | up | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.713 → 0.870 | 0.157 | 0.703 → 0.860 | 1.4x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.713 → 0.865 | 0.152 | 0.703 → 0.855 | 2.2x sr_bytes | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.574 → 0.713 | 0.139 | 0.556 → 0.703 | 1.5x sr_bytes | down | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.613 → 0.748 | 0.135 | 0.604 → 0.743 | 2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.617 → 0.748 | 0.131 | 0.603 → 0.743 | 2.1x sr_airtime | down | 3 |
| `SC-signing` | signature-policy | **text** | 0.600 → 0.713 | 0.113 | 0.600 → 0.703 | 1.2x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.687 → 0.796 | 0.109 | 0.680 → 0.788 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.687 → 0.796 | 0.109 | 0.680 → 0.788 | 2.4x bytes_on_air | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.776 → 0.882 | 0.106 | 0.701 → 0.703 | 26x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.661 → 0.760 | 0.100 | 0.649 → 0.754 | 5x sr_airtime | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.713 → 0.800 | 0.087 | 0.703 → 0.792 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.713 → 0.800 | 0.087 | 0.700 → 0.793 | 2.1x bytes_on_air | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.814 → 0.896 | 0.082 | 0.685 → 0.705 | 11x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.814 → 0.896 | 0.082 | 0.685 → 0.705 | 11x sr_bytes | up | 4 |
| `FW-versions` | profile | **text** | 0.713 → 0.790 | 0.078 | 0.703 → 0.785 | 3.1x bytes_on_air | down | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.810 → 0.882 | 0.072 | 0.694 → 0.703 | 3.8x sr_bytes | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.840 → 0.911 | 0.071 | 0.689 → 0.742 | 1.2x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.816 → 0.883 | 0.068 | 0.694 → 0.697 | 3.8x sr_bytes | up | 2 |
| `FW-firmware` | profile | **text** | 0.713 → 0.780 | 0.067 | 0.703 → 0.774 | 3x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.816 → 0.882 | 0.066 | 0.658 → 0.703 | 16x advert_bytes | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.713 → 0.771 | 0.059 | 0.703 → 0.764 | 3.3x bytes_on_air | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.652 → 0.705 | 0.053 | 0.647 → 0.699 | 1.4x sr_airtime | down | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.835 → 0.882 | 0.047 | 0.685 → 0.720 | 1.3x bytes_on_air | down | 4 |
| `AD-worst` | role-placement | **text** | 0.735 → 0.780 | 0.045 | 0.712 → 0.765 | 1.1x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.841 → 0.886 | 0.044 | 0.698 → 0.708 | 1.9x sr_bytes | up | 3 |
| `MS-roles` | role-mix | **text** | 0.687 → 0.725 | 0.038 | 0.680 → 0.718 | 1.2x sr_bytes | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.732 → 0.769 | 0.037 | 0.725 → 0.766 | 1.2x sr_bytes | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.672 → 0.707 | 0.035 | 0.658 → 0.701 | 9x advert_bytes | up | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.680 → 0.715 | 0.034 | 0.667 → 0.705 | 1.3x sr_airtime | down | 4 |
| `TH-congestion-input` | congestion-input | **text** | 0.507 → 0.538 | 0.031 | 0.499 → 0.531 | 1.4x sr_airtime | up | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.851 → 0.882 | 0.031 | 0.678 → 0.703 | 3.5x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.857 → 0.885 | 0.027 | 0.688 → 0.702 | 5.1x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **held** | 0.819 → 0.841 | 0.022 | 0.662 → 0.681 | 1.2x sr_airtime | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.711 → 0.731 | 0.021 | 0.701 → 0.723 | 1.2x sr_airtime | down | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.851 → 0.871 | 0.020 | 0.678 → 0.700 | 1x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.824 → 0.841 | 0.017 | 0.670 → 0.681 | 1.1x sr_bytes | up | 2 |
| `SF-capacity` | capacity | **held** | 0.866 → 0.882 | 0.016 | 0.692 → 0.703 | 5.5x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.866 → 0.882 | 0.016 | 0.692 → 0.703 | 5.5x advert_bytes | up | 5 |
| `SF-resolve` | resolve | **held** | 0.867 → 0.882 | 0.015 | 0.689 → 0.703 | 5.8x advert_bytes | = | 3 |
| `SF-width` | short-id-bits | **held** | 0.868 → 0.883 | 0.014 | 0.689 → 0.703 | 3.1x advert_bytes | up | 4 |
| `SF-sr-retries` | sr-retries | **text** | 0.694 → 0.707 | 0.013 | 0.683 → 0.698 | 1.1x sr_bytes | down | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.874 → 0.886 | 0.012 | 0.698 → 0.707 | 3.8x advert_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.713 → 0.724 | 0.011 | 0.703 → 0.714 | 1.1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.670 → 0.680 | 0.011 | 0.670 → 0.680 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.882 → 0.892 | 0.010 | 0.703 → 0.709 | 1.1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.908 → 0.917 | 0.010 | 0.904 → 0.916 | 1.2x sr_airtime | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.704 → 0.713 | 0.009 | 0.695 → 0.703 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.704 → 0.713 | 0.009 | 0.695 → 0.703 | 1.1x sr_airtime | up | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.706 → 0.713 | 0.007 | 0.696 → 0.703 | 2.3x sr_airtime | down | 2 |
| `SF-window-size` | window-size | **held** | 0.880 → 0.887 | 0.007 | 0.696 → 0.707 | 5.8x advert_bytes | down | 3 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.995 → 0.998 | 0.004 | 0.916 → 0.917 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.991 → 0.995 | 0.004 | 0.914 → 0.916 | 1x sr_bytes | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.713 → 0.715 | 0.003 | 0.703 → 0.704 | 1.3x sr_bytes | up | 2 |

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
| none | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| sprinkled | 1 | 0.796 | 0.791 | 0.005 | - | - | 0.927 | 0.928 | 0.238 | 1.18x | 15.4/23.3/26.6% | 1.8/4.8% | 3 |
| arms-race | 1 | 0.906 | 0.898 | 0.008 | - | - | 0.978 | 0.978 | 0.359 | 1.10x | 16.6/22.3/27.2% | 1.5/4.8% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.1 | 1 | 0.812 | 0.808 | 0.005 | - | - | 0.836 | 0.911 | 0.291 | 1.15x | 14.0/19.2/25.1% | 1.7/4.7% | 3 |
| 0.3 | 1 | 0.865 | 0.855 | 0.011 | - | - | 0.978 | 0.979 | 0.281 | 1.12x | 17.0/22.9/27.1% | 1.6/5.0% | 3 |

> amplify-worst=0.1: decode_failures 38

> slower: 4.39 s per simulated hour against 1.67 over 8 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.687 | 0.680 | 0.006 | - | - | 0.867 | 0.869 | 0.000 | 1.01x | 12.8/17.7/19.7% | 1.7/4.5% | 3 |
| inverse | 1 | 0.459 | 0.437 | 0.023 | - | - | 0.621 | 0.679 | 0.168 | 0.94x | 9.6/14.3/16.6% | 1.6/3.3% | 3 |
| random | 1 | 0.656 | 0.641 | 0.016 | - | - | 0.876 | 0.879 | 0.046 | 1.05x | 11.7/16.6/19.2% | 1.8/4.2% | 3 |

> role-placement=inverse: decode_failures 9

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.687 | 0.680 | 0.006 | - | - | 0.867 | 0.869 | 0.000 | 1.01x | 12.8/17.7/19.7% | 1.7/4.5% | 3 |
| all-routers | 1 | 0.796 | 0.788 | 0.008 | - | - | 0.914 | 0.914 | 0.527 | 2.42x | 26.0/34.9/37.7% | 4.0/5.0% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.687 | 0.680 | 0.006 | - | - | 0.867 | 0.869 | 0.000 | 1.01x | 12.8/17.7/19.7% | 1.7/4.5% | 3 |
| no-mute | 1 | 0.716 | 0.706 | 0.009 | - | - | 0.891 | 0.894 | 0.217 | 1.18x | 13.3/18.5/21.1% | 1.8/4.6% | 3 |
| all-routers | 1 | 0.796 | 0.788 | 0.008 | - | - | 0.914 | 0.914 | 0.527 | 2.42x | 26.0/34.9/37.7% | 4.0/5.0% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.687 | 0.680 | 0.006 | - | - | 0.867 | 0.869 | 0.000 | 1.01x | 12.8/17.7/19.7% | 1.7/4.5% | 3 |
| local-typical | 1 | 0.273 | 0.272 | 0.001 | - | - | 0.325 | 0.488 | 0.000 | 1.29x | 8.8/21.5/28.1% | 1.6/5.9% | 3 |
| basement-heavy | 1 | 0.071 | 0.071 | 0.001 | - | - | 0.213 | 0.217 | 0.000 | 0.55x | 1.6/7.0/10.9% | 0.4/2.4% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.780 | 0.765 | 0.015 | - | - | 0.957 | 0.958 | 0.169 | 2.35x | 13.7/24.8/30.1% | 1.8/5.4% | 3 |
| inverse | 1 | 0.735 | 0.712 | 0.023 | - | - | 0.954 | 0.957 | 0.166 | 2.24x | 12.1/22.1/26.7% | 1.8/3.3% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.706 | 0.706 | 0.000 | - | - | 0 | 0.000 | 0.293 | 1.16x | 13.4/17.9/21.3% | 1.7/4.6% | 3 |
| sr | 1 | 0.710 | 0.696 | 0.015 | - | - | 0.870 | 0.874 | 0.300 | 1.18x | 13.8/18.2/21.9% | 1.7/4.7% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.613 | 0.604 | 0.009 | - | - | 0.742 | 0.772 | 0.211 | 2.65x | 28.9/49.5/55.5% | 3.7/9.4% | 3 |
| 100 | 1 | 0.748 | 0.743 | 0.005 | - | - | 0.874 | 0.875 | 0.318 | 1.47x | 15.7/29.5/33.3% | 2.1/5.1% | 3 |
| 120 | 1 | 0.748 | 0.743 | 0.005 | - | - | 0.874 | 0.875 | 0.318 | 1.47x | 15.7/29.5/33.3% | 2.1/5.1% | 3 |
| 250 | 1 | 0.748 | 0.743 | 0.005 | - | - | 0.874 | 0.875 | 0.318 | 1.47x | 15.7/29.5/33.3% | 2.1/5.1% | 3 |

> max-num-nodes=10: decode_failures 14

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.310 | 0.306 | 0.004 | - | - | 0.453 | 0.485 | 0.000 | 11.53x | 38.9/61.0/77.2% | 4.0/11.0% | 3 |
| 120 | 1 | 0.507 | 0.499 | 0.008 | - | - | 0.711 | 0.712 | 0.000 | 4.60x | 15.7/30.5/44.2% | 1.5/5.5% | 3 |
| 250 | 1 | 0.512 | 0.505 | 0.007 | - | - | 0.719 | 0.720 | 0.000 | 4.46x | 15.2/29.4/42.2% | 1.5/5.2% | 3 |

> max-num-nodes=10: decode_failures 60

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.748 | 0.743 | 0.005 | - | - | 0.874 | 0.875 | 0.318 | 1.47x | 15.7/29.5/33.3% | 2.1/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.748 | 0.743 | 0.005 | - | - | 0.874 | 0.875 | 0.318 | 1.47x | 15.7/29.5/33.3% | 2.1/5.1% | 3 |
| constrained | 1 | 0.617 | 0.603 | 0.014 | - | - | 0.754 | 0.757 | 0.235 | 2.66x | 29.0/49.7/55.7% | 3.7/9.4% | 3 |

> platform-mix=constrained: decode_failures 3

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.705 | 0.699 | 0.007 | - | - | 0.929 | 0.944 | 0.528 | 5.84x | 51.2/68.5/76.3% | 4.2/11.8% | 3 |
| 25 | 1 | 0.705 | 0.699 | 0.007 | - | - | 0.929 | 0.944 | 0.528 | 5.84x | 51.2/68.5/76.3% | 4.2/11.8% | 3 |
| 100 | 1 | 0.705 | 0.699 | 0.007 | - | - | 0.929 | 0.944 | 0.528 | 5.84x | 51.2/68.5/76.3% | 4.2/11.8% | 3 |
| 2000 | 1 | 0.705 | 0.699 | 0.007 | - | - | 0.929 | 0.944 | 0.528 | 5.84x | 51.2/68.5/76.3% | 4.2/11.8% | 3 |

> warm-num-nodes=0: decode_failures 33

> warm-num-nodes=25: decode_failures 33

> warm-num-nodes=100: decode_failures 33

> warm-num-nodes=2000: decode_failures 33

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.1 | 1 | 0.611 | 0.591 | 0.020 | - | - | 0.838 | 0.847 | 0.217 | 1.09x | 13.2/17.2/20.8% | 1.6/4.1% | 3 |
| 0.2 | 1 | 0.520 | 0.494 | 0.026 | - | - | 0.751 | 0.790 | 0.179 | 0.99x | 12.1/15.9/19.3% | 1.5/3.6% | 3 |
| 0.3 | 1 | 0.417 | 0.384 | 0.033 | - | - | 0.635 | 0.707 | 0.109 | 0.90x | 11.3/15.2/18.2% | 1.4/3.2% | 3 |

> burst-loss=0.1: decode_failures 2

> burst-loss=0.2: decode_failures 10

> burst-loss=0.3: decode_failures 31

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.1 | 1 | 0.683 | 0.670 | 0.014 | - | - | 0.868 | 0.871 | 0.249 | 1.22x | 14.5/18.9/22.5% | 1.9/4.5% | 3 |
| 0.2 | 1 | 0.630 | 0.614 | 0.015 | - | - | 0.835 | 0.836 | 0.191 | 1.24x | 15.1/19.8/23.4% | 1.8/4.4% | 3 |
| 0.3 | 1 | 0.574 | 0.556 | 0.018 | - | - | 0.800 | 0.809 | 0.151 | 1.24x | 15.3/20.4/23.4% | 1.8/4.1% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.1 | 1 | 0.614 | 0.598 | 0.016 | - | - | 0.823 | 0.855 | 0.231 | 1.11x | 13.2/17.3/20.9% | 1.6/4.0% | 3 |
| 0.2 | 1 | 0.492 | 0.471 | 0.020 | - | - | 0.677 | 0.770 | 0.179 | 1.02x | 12.4/16.4/19.7% | 1.5/4.0% | 3 |
| 0.3 | 1 | 0.420 | 0.396 | 0.025 | - | - | 0.647 | 0.727 | 0.110 | 0.94x | 11.5/15.6/18.9% | 1.4/3.7% | 3 |

> burst-loss=0.1: decode_failures 22

> burst-loss=0.2: decode_failures 22

> burst-loss=0.3: decode_failures 29

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.662 | 0.662 | 0.000 | - | - | 0.819 | 0.856 | 0.266 | 1.50x | 17.4/22.9/27.4% | 2.2/6.0% | 3 |
| directed-with-late-flood | 1 | 0.680 | 0.680 | 0.000 | - | - | 0.834 | 0.866 | 0.275 | 1.39x | 16.3/21.4/25.8% | 2.0/5.6% | 3 |
| m4-early-flood | 1 | 0.681 | 0.681 | 0.000 | - | - | 0.841 | 0.876 | 0.265 | 1.40x | 16.5/21.7/25.9% | 2.0/5.7% | 3 |

> dm-mode=flood-only: decode_failures 5

> dm-mode=directed-with-late-flood: decode_failures 2

> dm-mode=m4-early-flood: decode_failures 1

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.780 | 0.774 | 0.006 | - | - | 0.935 | 0.937 | 0.493 | 0.71x | 7.2/10.1/11.2% | 1.1/1.8% | 3 |
| 2.8 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.25 | 1 | 0.795 | 0.789 | 0.006 | - | - | 0.944 | 0.949 | 0.444 | 1.15x | 12.2/20.6/22.5% | 1.7/5.0% | 3 |
| 0.5 | 1 | 0.800 | 0.793 | 0.007 | - | - | 0.957 | 0.959 | 0.326 | 1.02x | 11.3/16.9/19.9% | 1.7/4.4% | 3 |
| 0.75 | 1 | 0.715 | 0.700 | 0.014 | - | - | 0.915 | 0.917 | 0.285 | 0.78x | 9.0/12.2/14.0% | 1.2/3.0% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.25 | 1 | 0.800 | 0.792 | 0.007 | - | - | 0.947 | 0.948 | 0.445 | 1.14x | 12.4/20.6/22.7% | 1.7/5.0% | 3 |
| 0.5 | 1 | 0.796 | 0.789 | 0.007 | - | - | 0.965 | 0.966 | 0.309 | 1.02x | 11.5/17.2/20.1% | 1.6/4.4% | 3 |
| 0.75 | 1 | 0.726 | 0.712 | 0.015 | - | - | 0.930 | 0.934 | 0.280 | 0.77x | 9.1/12.2/13.9% | 1.2/3.0% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.771 | 0.764 | 0.007 | - | - | 0.916 | 0.917 | 0.320 | 0.64x | 7.7/10.3/12.8% | 0.9/2.6% | 3 |
| signing=true | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.766 | 0.758 | 0.008 | - | - | 0.935 | 0.938 | 0.456 | 0.72x | 7.4/10.7/12.2% | 1.2/1.9% | 3 |
| 2.5 | 1 | 0.787 | 0.781 | 0.006 | - | - | 0.943 | 0.943 | 0.514 | 0.73x | 7.5/10.9/12.1% | 1.2/2.0% | 3 |
| 2.6 | 1 | 0.768 | 0.761 | 0.006 | - | - | 0.928 | 0.932 | 0.490 | 0.70x | 7.3/10.6/12.1% | 1.2/1.8% | 3 |
| 2.7 | 1 | 0.790 | 0.785 | 0.006 | - | - | 0.936 | 0.938 | 0.477 | 0.75x | 7.6/15.6/16.8% | 1.1/2.8% | 3 |
| 2.8 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.728 | 0.722 | 0.006 | - | - | 0.894 | 0.897 | 0.329 | 0.80x | 9.3/12.1/14.8% | 1.2/3.1% | 3 |
| 900 | 1 | 0.661 | 0.649 | 0.012 | - | - | 0.845 | 0.847 | 0.249 | 1.83x | 21.4/28.0/33.4% | 2.6/7.3% | 3 |
| 300 | 1 | 0.444 | 0.427 | 0.017 | - | - | 0.547 | 0.665 | 0.152 | 3.85x | 43.6/56.0/63.0% | 5.6/14.9% | 3 |

> broadcast-interval-s=300: decode_failures 10

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.806 | 0.802 | 0.003 | - | - | 0.890 | 0.891 | 0.435 | 0.92x | 10.1/13.4/15.9% | 1.4/3.4% | 3 |
| 900 | 1 | 0.713 | 0.707 | 0.006 | - | - | 0.826 | 0.828 | 0.360 | 2.02x | 22.5/29.9/34.9% | 3.0/7.7% | 3 |
| 300 | 1 | 0.465 | 0.453 | 0.012 | - | - | 0.577 | 0.605 | 0.217 | 4.42x | 49.0/62.0/66.6% | 6.4/16.2% | 3 |

> broadcast-interval-s=300: decode_failures 7

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.731 | 0.723 | 0.009 | - | - | 0.889 | 0.894 | 0.311 | 1.11x | 12.9/17.1/20.7% | 1.7/4.4% | 3 |
| sinusoid | 1 | 0.711 | 0.701 | 0.010 | - | - | 0.871 | 0.885 | 0.310 | 1.09x | 12.7/16.9/20.1% | 1.6/4.3% | 3 |
| commuter | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.661 | 0.649 | 0.012 | - | - | 0.845 | 0.847 | 0.249 | 1.83x | 21.4/28.0/33.4% | 2.6/7.3% | 3 |
| 3600 | 1 | 0.728 | 0.722 | 0.006 | - | - | 0.894 | 0.897 | 0.329 | 0.80x | 9.3/12.1/14.8% | 1.2/3.1% | 3 |
| 10800 | 1 | 0.745 | 0.738 | 0.007 | - | - | 0.890 | 0.891 | 0.325 | 0.55x | 6.4/8.5/10.3% | 0.8/2.1% | 3 |
| 43200 | 1 | 0.760 | 0.754 | 0.006 | - | - | 0.906 | 0.907 | 0.336 | 0.36x | 4.3/5.6/6.8% | 0.5/1.4% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.25 | 1 | 0.715 | 0.705 | 0.009 | - | - | 0.886 | 0.894 | 0.303 | 1.23x | 14.3/18.8/22.7% | 1.8/4.8% | 3 |
| 1.0 | 1 | 0.704 | 0.693 | 0.011 | - | - | 0.874 | 0.878 | 0.301 | 1.32x | 15.4/20.2/24.6% | 1.9/5.3% | 3 |
| 4.0 | 1 | 0.680 | 0.667 | 0.013 | - | - | 0.865 | 0.868 | 0.293 | 1.62x | 19.3/25.6/30.8% | 2.3/6.8% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.699 | 0.007 | - | - | 0.929 | 0.944 | 0.528 | 5.84x | 51.2/68.5/76.3% | 4.2/11.8% | 3 |
| 1.0 | 1 | 0.652 | 0.647 | 0.005 | - | - | 0.885 | 0.917 | 0.493 | 6.43x | 54.5/71.9/78.7% | 4.7/13.2% | 3 |

> traceroute-per-hour=0.0: decode_failures 33

> traceroute-per-hour=1.0: decode_failures 20

> faster: 18 s per simulated hour against 37.2 over 8 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.661 | 0.637 | 0.023 | - | - | 0.832 | 0.849 | 0.000 | 1.16x | 19.0/28.7/34.2% | 2.5/6.5% | 3 |
| 60 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 90 | 1 | 0.881 | 0.873 | 0.008 | - | - | 0.980 | 0.981 | 0.606 | 1.66x | 15.7/26.2/32.3% | 1.6/5.0% | 3 |
| 120 | 1 | 0.917 | 0.916 | 0.002 | - | - | 0.995 | 0.995 | 0.745 | 2.03x | 19.3/30.0/35.8% | 1.3/4.7% | 3 |
| 150 | 1 | 0.936 | 0.934 | 0.003 | - | - | 0.992 | 0.993 | 0.649 | 2.54x | 24.1/34.0/39.5% | 1.3/5.6% | 3 |

> nodes=40: decode_failures 6

> nodes=150: misdecodes 1

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 120 | 1 | 0.587 | 0.574 | 0.013 | - | - | 0.852 | 0.853 | 0.261 | 2.17x | 12.1/24.7/31.4% | 1.6/5.5% | 3 |
| 250 | 1 | 0.507 | 0.499 | 0.008 | - | - | 0.708 | 0.708 | 0.000 | 4.86x | 16.6/32.3/46.5% | 1.6/5.8% | 3 |
| 500 | 1 | 0.313 | 0.309 | 0.004 | - | - | 0.448 | 0.450 | 0.120 | 10.24x | 19.5/29.8/41.3% | 1.8/6.2% | 3 |

> nodes=500: decode_failures 14

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.591 | 0.578 | 0.013 | - | - | 0.853 | 0.855 | 0.263 | 2.07x | 11.6/22.9/29.4% | 1.5/5.2% | 3 |
| 250 | 1 | 0.507 | 0.499 | 0.008 | - | - | 0.711 | 0.712 | 0.000 | 4.60x | 15.7/30.5/44.2% | 1.5/5.5% | 3 |
| 500 | 1 | 0.317 | 0.313 | 0.004 | - | - | 0.451 | 0.453 | 0.122 | 9.54x | 18.1/27.7/39.9% | 1.6/5.6% | 3 |

> nodes=120: decode_failures 2

> nodes=500: decode_failures 6

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.725 | 0.718 | 0.007 | - | - | 0.902 | 0.906 | 0.316 | 1.17x | 13.7/18.1/21.7% | 1.7/4.6% | 3 |
| baymesh-2026-08 | 1 | 0.687 | 0.680 | 0.006 | - | - | 0.867 | 0.869 | 0.000 | 1.01x | 12.8/17.7/19.7% | 1.7/4.5% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.749 | 0.742 | 0.007 | - | - | 0.911 | 0.911 | 0.327 | 1.23x | 14.3/18.8/22.5% | 1.8/4.7% | 3 |
| baymesh-2026-08 | 1 | 0.694 | 0.689 | 0.005 | - | - | 0.840 | 0.840 | 0.000 | 1.16x | 14.4/21.3/24.5% | 1.9/4.4% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.05 | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.867 | 0.872 | 0.307 | 1.31x | 15.8/22.9/25.6% | 1.8/5.2% | 3 |
| 0.1 | 1 | 0.695 | 0.685 | 0.009 | - | - | 0.844 | 0.847 | 0.260 | 1.39x | 15.8/28.9/32.7% | 1.9/5.2% | 3 |
| 0.2 | 1 | 0.711 | 0.703 | 0.008 | - | - | 0.835 | 0.835 | 0.382 | 1.57x | 18.3/30.9/34.3% | 2.3/5.0% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| local-typical | 1 | 0.336 | 0.335 | 0.002 | - | - | 0.372 | 0.559 | 0.000 | 1.46x | 8.9/21.1/30.3% | 2.2/5.5% | 3 |
| event | 1 | 0.075 | 0.074 | 0.001 | - | - | 0.139 | 0.157 | 0.000 | 0.79x | 3.3/7.2/11.5% | 1.2/3.2% | 3 |
| backbone | 1 | 0.960 | 0.955 | 0.005 | - | - | 0.993 | 0.995 | 0.857 | 1.06x | 22.0/26.7/31.9% | 1.4/5.4% | 3 |

> siting-mix=event: decode_failures 4

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.764 | 0.745 | 0.019 | - | - | 0.906 | 0.907 | 0.000 | 1.18x | 22.9/31.6/35.0% | 2.4/7.0% | 3 |
| 60 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 90 | 1 | 0.769 | 0.748 | 0.020 | - | - | 0.926 | 0.950 | 0.446 | 1.90x | 14.1/30.2/34.7% | 1.8/5.2% | 3 |
| 120 | 1 | 0.587 | 0.574 | 0.013 | - | - | 0.852 | 0.853 | 0.261 | 2.17x | 12.1/24.7/31.4% | 1.6/5.5% | 3 |
| 150 | 1 | 0.617 | 0.604 | 0.013 | - | - | 0.801 | 0.802 | 0.218 | 2.73x | 14.1/27.7/35.7% | 1.6/4.5% | 3 |

> nodes=90: decode_failures 76

> slower: 7.48 s per simulated hour against 3.25 over 8 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 1.25 | 1 | 0.357 | 0.336 | 0.021 | - | - | 0.527 | 0.539 | 0.000 | 1.23x | 9.3/15.6/19.5% | 1.8/4.9% | 3 |
| 1.5 | 1 | 0.178 | 0.176 | 0.002 | - | - | 0.216 | 0.218 | 0.000 | 1.05x | 7.3/13.9/18.4% | 1.5/4.6% | 3 |
| 2.0 | 1 | 0.070 | 0.070 | 0.000 | - | - | 0.102 | 0.102 | 0.000 | 0.66x | 2.5/7.3/11.2% | 1.0/2.7% | 3 |

> stretch=1.25: decode_failures 4

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| clustered | 1 | 0.945 | 0.942 | 0.003 | - | - | 0.990 | 0.990 | 0.682 | 1.24x | 23.5/35.4/37.6% | 1.5/5.5% | 3 |
| corridor | 1 | 0.429 | 0.421 | 0.008 | - | - | 0.592 | 0.593 | 0.135 | 1.31x | 13.6/31.1/33.5% | 1.6/5.6% | 3 |
| hub | 1 | 0.946 | 0.946 | 0.000 | - | - | 0.978 | 0.978 | 0.861 | 1.23x | 24.6/34.6/36.8% | 1.7/5.4% | 3 |

> topology=clustered: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.680 | 0.680 | 0.000 | - | - | 0.834 | 0.866 | 0.275 | 1.39x | 16.3/21.4/25.8% | 2.0/5.6% | 3 |
| True | 1 | 0.670 | 0.670 | 0.000 | - | - | 0.824 | 0.868 | 0.281 | 1.40x | 16.4/21.7/26.0% | 2.0/5.7% | 3 |

> coding-rate-ladder=False: decode_failures 2

> coding-rate-ladder=True: decode_failures 8

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.670 | 0.670 | 0.000 | - | - | 0.824 | 0.868 | 0.281 | 1.40x | 16.4/21.7/26.0% | 2.0/5.7% | 3 |
| m4-early-flood | 1 | 0.681 | 0.681 | 0.000 | - | - | 0.841 | 0.871 | 0.288 | 1.42x | 16.7/22.1/26.4% | 2.0/5.7% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 8

> dm-mode=m4-early-flood: decode_failures 3

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.706 | 0.706 | 0.000 | - | - | 0 | 0.000 | 0.293 | 1.16x | 13.4/17.9/21.3% | 1.7/4.6% | 3 |
| chain | 1 | 0.680 | 0.674 | 0.006 | - | - | 0.786 | 0.860 | 0.281 | 1.35x | 16.0/20.9/25.4% | 2.0/5.3% | 3 |
| sr | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| True | 1 | 0.724 | 0.714 | 0.009 | - | - | 0.892 | 0.894 | 0.298 | 1.16x | 13.5/17.8/21.4% | 1.7/4.5% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.917 | 0.916 | 0.002 | - | - | 0.995 | 0.995 | 0.745 | 2.03x | 19.3/30.0/35.8% | 1.3/4.7% | 3 |
| True | 1 | 0.916 | 0.914 | 0.002 | - | - | 0.991 | 0.992 | 0.747 | 2.03x | 19.1/29.8/35.4% | 1.4/4.7% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.091 | 0.091 | 0.000 | - | - | 0.121 | 0.122 | 0.000 | 0.03x | 0.1/0.4/0.5% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.167 | 0.167 | 0.000 | - | - | 0.158 | 0.158 | 0.000 | 0.15x | 0.9/2.2/2.7% | 0.2/0.6% | 3 |
| LONG_TURBO | 1 | 0.577 | 0.560 | 0.016 | - | - | 0.795 | 0.795 | 0.115 | 1.06x | 9.9/17.2/20.0% | 1.4/4.7% | 3 |

> faster: 0.681 s per simulated hour against 2.04 over 8 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 0.25 | 1 | 0.749 | 0.739 | 0.010 | - | - | 0.888 | 0.893 | 0.387 | 1.09x | 14.4/18.4/22.6% | 1.6/4.6% | 3 |
| 1.0 | 1 | 0.870 | 0.860 | 0.011 | - | - | 0.937 | 0.938 | 0.691 | 0.91x | 17.2/21.8/27.4% | 1.3/4.8% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.134 | 0.132 | 0.002 | - | - | 0.149 | 0.149 | 0.000 | 0.08x | 0.5/1.1/1.4% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| LITE_FAST | 1 | 0.623 | 0.601 | 0.021 | - | - | 0.865 | 0.867 | 0.152 | 0.82x | 8.6/13.2/15.8% | 1.1/3.7% | 3 |
| NARROW_SLOW | 1 | 0.652 | 0.641 | 0.010 | - | - | 0.843 | 0.849 | 0.256 | 1.10x | 11.7/16.0/19.8% | 1.5/4.5% | 3 |

> preset=SHORT_FAST: decode_failures 1

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| temporal | 1 | 0.554 | 0.543 | 0.011 | - | - | 0.770 | 0.813 | 0.127 | 1.09x | 13.0/16.9/20.7% | 1.5/4.6% | 3 |
| transient | 1 | 0.702 | 0.691 | 0.011 | - | - | 0.874 | 0.878 | 0.278 | 1.18x | 13.8/18.1/21.8% | 1.7/4.7% | 3 |
| periodic | 1 | 0.545 | 0.535 | 0.010 | - | - | 0.689 | 0.710 | 0.197 | 1.05x | 12.5/16.4/19.7% | 1.6/3.9% | 3 |

> noise-profile=temporal: decode_failures 16

> noise-profile=periodic: decode_failures 2

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.134 | 0.132 | 0.002 | - | - | 0.149 | 0.149 | 0.000 | 0.08x | 0.5/1.1/1.4% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| LONG_MODERATE | 1 | 0.723 | 0.697 | 0.026 | - | - | 0.821 | 0.839 | 0.481 | 3.22x | 39.0/55.4/62.2% | 4.8/12.4% | 3 |

> preset=SHORT_FAST: decode_failures 1

> preset=LONG_MODERATE: decode_failures 24

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.028 | 0.028 | 0.000 | - | - | 0.049 | 0.051 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.091 | 0.091 | 0.000 | - | - | 0.121 | 0.122 | 0.000 | 0.03x | 0.1/0.4/0.5% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| LONG_TURBO | 1 | 0.577 | 0.560 | 0.016 | - | - | 0.795 | 0.795 | 0.115 | 1.06x | 9.9/17.2/20.0% | 1.4/4.7% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.706 | 0.693 | 0.013 | - | - | 0.862 | 0.864 | 0.327 | 1.67x | 18.1/25.3/28.1% | 2.6/6.0% | 3 |

> faster: 0.823 s per simulated hour against 1.65 over 4 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.643 | 0.633 | 0.010 | - | - | 0.810 | 0.811 | 0.243 | 1.14x | 13.6/17.8/21.4% | 1.7/4.4% | 3 |
| 10000 | 1 | 0.545 | 0.535 | 0.010 | - | - | 0.689 | 0.710 | 0.197 | 1.05x | 12.5/16.4/19.7% | 1.6/3.9% | 3 |
| 4000 | 1 | 0.297 | 0.292 | 0.005 | - | - | 0.362 | 0.438 | 0.082 | 0.89x | 10.7/14.3/16.8% | 1.3/3.0% | 3 |
| 2000 | 1 | 0.065 | 0.065 | 0.000 | - | - | 0.081 | 0.136 | 0.012 | 0.66x | 8.0/11.7/13.3% | 1.0/1.9% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.178 | 0.176 | 0.002 | - | - | 0.216 | 0.218 | 0.000 | 1.05x | 7.3/13.9/18.4% | 1.5/4.6% | 3 |
| 1.0 | 1 | 0.643 | 0.637 | 0.006 | - | - | 0.680 | 0.680 | 0.472 | 0.89x | 14.2/19.0/22.4% | 1.2/4.3% | 3 |

> faster: 1.13 s per simulated hour against 2.35 over 8 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 22 | 1 | 0.169 | 0.169 | 0.000 | - | - | 0.147 | 0.147 | 0.000 | 1.04x | 6.5/13.9/16.8% | 1.5/4.2% | 3 |
| 17 | 1 | 0.086 | 0.086 | 0.000 | - | - | 0.104 | 0.109 | 0.000 | 0.70x | 3.0/7.1/10.6% | 1.0/2.7% | 3 |
| 14 | 1 | 0.046 | 0.046 | 0.000 | - | - | 0.079 | 0.097 | 0.000 | 0.55x | 2.0/5.5/9.3% | 0.8/2.3% | 3 |

> tx-power=14: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.917 | 0.916 | 0.002 | - | - | 0.995 | 0.995 | 0.745 | 2.03x | 19.3/30.0/35.8% | 1.3/4.7% | 3 |
| True | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.997 | 0.998 | 0.724 | 2.35x | 22.1/34.3/40.5% | 1.5/5.3% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.732 | 0.725 | 0.006 | - | - | 0.877 | 0.878 | 0.353 | 1.29x | 15.2/22.2/24.6% | 1.8/5.2% | 3 |
| True | 1 | 0.769 | 0.766 | 0.003 | - | - | 0.873 | 0.875 | 0.462 | 1.38x | 15.8/23.1/25.5% | 2.1/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| random | 1 | 0.715 | 0.704 | 0.012 | - | - | 0.882 | 0.883 | 0.324 | 1.19x | 13.8/18.2/21.9% | 1.7/4.7% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.549 | 0.523 | 0.026 | - | - | 0.740 | 0.776 | 0.203 | 0.96x | 11.3/15.5/19.1% | 1.4/4.0% | 3 |
| 7 | 1 | 0.768 | 0.764 | 0.004 | - | - | 0.859 | 0.860 | 0.391 | 1.34x | 14.6/19.5/23.2% | 2.0/4.9% | 3 |
| 15 | 1 | 0.793 | 0.792 | 0.002 | - | - | 0.858 | 0.859 | 0.435 | 1.34x | 14.7/19.6/23.3% | 2.1/4.9% | 3 |
| 32 | 1 | 0.801 | 0.800 | 0.002 | - | - | 0.865 | 0.866 | 0.446 | 1.35x | 14.8/19.7/23.4% | 2.1/4.9% | 3 |

> hop-limit=3: decode_failures 5

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.549 | 0.523 | 0.026 | - | - | 0.740 | 0.776 | 0.203 | 0.96x | 11.3/15.5/19.1% | 1.4/4.0% | 3 |
| 5 | 1 | 0.703 | 0.692 | 0.011 | - | - | 0.854 | 0.855 | 0.340 | 1.18x | 13.5/17.9/21.6% | 1.7/4.6% | 3 |
| 7 | 1 | 0.768 | 0.764 | 0.004 | - | - | 0.859 | 0.860 | 0.391 | 1.34x | 14.6/19.5/23.2% | 2.0/4.9% | 3 |

> hop-limit=3: decode_failures 5

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| KNOWN_ONLY | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.701 | 0.701 | 0.000 | - | - | 0.776 | 0.881 | 0.278 | 1.17x | 13.5/17.9/21.4% | 1.7/4.6% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.549 | 0.523 | 0.026 | - | - | 0.740 | 0.776 | 0.203 | 0.96x | 11.3/15.5/19.1% | 1.4/4.0% | 3 |
| True | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

> hop-spread=False: decode_failures 5

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| BALANCED | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| STRICT | 1 | 0.600 | 0.600 | 0.000 | - | - | 0.773 | 0.778 | 0.206 | 1.25x | 14.5/19.2/23.0% | 1.8/4.9% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| dm | 1 | 0.706 | 0.696 | 0.009 | - | - | 0.881 | 0.881 | 0.285 | 1.16x | 13.6/17.9/21.7% | 1.7/4.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.714 | 0.698 | 0.016 | - | - | 0.874 | 0.882 | 0.287 | 1.17x | 13.6/17.9/21.5% | 1.7/4.6% | 3 |
| local | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| time | 1 | 0.712 | 0.702 | 0.011 | - | - | 0.885 | 0.890 | 0.295 | 1.20x | 14.2/18.5/22.4% | 1.8/4.8% | 3 |
| window | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.886 | 0.891 | 0.295 | 1.17x | 13.7/17.9/21.5% | 1.7/4.6% | 3 |

> bucket-mode=global: misdecodes 21

> bucket-mode=time: misdecodes 25

> bucket-mode=window: misdecodes 12

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.699 | 0.688 | 0.011 | - | - | 0.857 | 0.866 | 0.288 | 1.29x | 15.3/19.9/24.0% | 1.9/5.1% | 3 |
| 1800 | 1 | 0.712 | 0.702 | 0.011 | - | - | 0.885 | 0.890 | 0.295 | 1.20x | 14.2/18.5/22.4% | 1.8/4.8% | 3 |
| 3600 | 1 | 0.712 | 0.702 | 0.011 | - | - | 0.875 | 0.883 | 0.301 | 1.20x | 14.1/18.4/22.1% | 1.8/4.7% | 3 |

> time-bucket-s=600: misdecodes 108

> time-bucket-s=1800: misdecodes 25

> time-bucket-s=3600: misdecodes 12

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| interval | 1 | 0.683 | 0.670 | 0.013 | - | - | 0.861 | 0.867 | 0.287 | 1.56x | 18.7/25.5/30.4% | 2.2/7.0% | 3 |
| aimd | 1 | 0.697 | 0.690 | 0.007 | - | - | 0.816 | 0.877 | 0.298 | 1.19x | 13.9/18.3/22.2% | 1.8/4.7% | 3 |
| bucket+interval | 1 | 0.672 | 0.658 | 0.014 | - | - | 0.843 | 0.847 | 0.273 | 1.58x | 19.2/26.0/31.1% | 2.3/7.2% | 3 |

> trigger=interval: misdecodes 15

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 16

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.711 | 0.701 | 0.009 | - | - | 0.872 | 0.880 | 0.287 | 1.17x | 13.8/18.0/21.9% | 1.7/4.5% | 3 |
| 8 | 1 | 0.706 | 0.695 | 0.011 | - | - | 0.872 | 0.884 | 0.284 | 1.15x | 13.6/17.9/21.6% | 1.7/4.5% | 3 |
| 16 | 1 | 0.702 | 0.692 | 0.010 | - | - | 0.866 | 0.870 | 0.295 | 1.18x | 13.8/18.2/21.8% | 1.7/4.6% | 3 |
| 32 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 50 | 1 | 0.708 | 0.699 | 0.010 | - | - | 0.881 | 0.885 | 0.302 | 1.18x | 13.8/18.2/21.9% | 1.8/4.6% | 3 |

> capacity=4: decode_failures 76

> capacity=8: decode_failures 66

> capacity=16: decode_failures 8

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.711 | 0.701 | 0.009 | - | - | 0.872 | 0.880 | 0.287 | 1.17x | 13.8/18.0/21.9% | 1.7/4.5% | 3 |
| 8 | 1 | 0.706 | 0.695 | 0.011 | - | - | 0.872 | 0.884 | 0.284 | 1.15x | 13.6/17.9/21.6% | 1.7/4.5% | 3 |
| 16 | 1 | 0.702 | 0.692 | 0.010 | - | - | 0.866 | 0.870 | 0.295 | 1.18x | 13.8/18.2/21.8% | 1.7/4.6% | 3 |
| 32 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 50 | 1 | 0.708 | 0.699 | 0.010 | - | - | 0.881 | 0.885 | 0.302 | 1.18x | 13.8/18.2/21.9% | 1.8/4.6% | 3 |

> capacity=4: decode_failures 76

> capacity=8: decode_failures 66

> capacity=16: decode_failures 8

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.715 | 0.708 | 0.006 | - | - | 0.841 | 0.896 | 0.294 | 1.17x | 13.5/18.0/21.5% | 1.7/4.6% | 3 |
| 16 | 1 | 0.708 | 0.698 | 0.010 | - | - | 0.862 | 0.884 | 0.277 | 1.16x | 13.6/17.9/21.5% | 1.7/4.6% | 3 |
| 32 | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.886 | 0.891 | 0.295 | 1.17x | 13.7/17.9/21.5% | 1.7/4.6% | 3 |

> capacity=8: misdecodes 11

> capacity=8: decode_failures 61

> capacity=16: misdecodes 8

> capacity=16: decode_failures 12

> capacity=32: misdecodes 12

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.672 | 0.658 | 0.014 | - | - | 0.843 | 0.847 | 0.273 | 1.58x | 19.2/26.0/31.1% | 2.3/7.2% | 3 |
| 02-06 | 1 | 0.707 | 0.701 | 0.005 | - | - | 0.830 | 0.876 | 0.289 | 1.19x | 14.0/18.4/22.2% | 1.7/4.7% | 3 |
| 00-08 | 1 | 0.698 | 0.691 | 0.007 | - | - | 0.822 | 0.867 | 0.301 | 1.24x | 14.7/19.1/23.4% | 1.8/4.9% | 3 |

> catch-up-hours=: misdecodes 16

> catch-up-hours=02-06: decode_failures 6

> catch-up-hours=00-08: decode_failures 6

> faster: 4.27 s per simulated hour against 9.6 over 8 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.700 | 0.695 | 0.004 | - | - | 0.810 | 0.810 | 0.298 | 1.17x | 13.5/18.0/21.4% | 1.7/4.7% | 3 |
| 2 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 3 | 1 | 0.710 | 0.696 | 0.015 | - | - | 0.870 | 0.874 | 0.300 | 1.18x | 13.8/18.2/21.9% | 1.7/4.7% | 3 |
| 4 | 1 | 0.720 | 0.694 | 0.026 | - | - | 0.818 | 0.901 | 0.289 | 1.20x | 13.9/18.6/22.0% | 1.7/4.7% | 3 |

> hops-apart=4: decode_failures 23

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.700 | 0.695 | 0.004 | - | - | 0.810 | 0.810 | 0.298 | 1.17x | 13.5/18.0/21.4% | 1.7/4.7% | 3 |
| 2 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 3 | 1 | 0.710 | 0.696 | 0.015 | - | - | 0.870 | 0.874 | 0.300 | 1.18x | 13.8/18.2/21.9% | 1.7/4.7% | 3 |
| 4 | 1 | 0.720 | 0.694 | 0.026 | - | - | 0.818 | 0.901 | 0.289 | 1.20x | 13.9/18.6/22.0% | 1.7/4.7% | 3 |
| 5 | 1 | 0.702 | 0.689 | 0.013 | - | - | 0.678 | 0.899 | 0.278 | 1.17x | 13.4/17.8/21.4% | 1.7/4.7% | 3 |

> hops-apart=4: decode_failures 23

> hops-apart=5: decode_failures 7

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.708 | 0.698 | 0.010 | - | - | 0.876 | 0.881 | 0.285 | 1.18x | 13.9/18.2/22.0% | 1.7/4.7% | 3 |
| 30 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 120 | 1 | 0.704 | 0.695 | 0.009 | - | - | 0.876 | 0.880 | 0.283 | 1.18x | 13.8/18.2/21.8% | 1.7/4.7% | 3 |
| 600 | 1 | 0.710 | 0.700 | 0.009 | - | - | 0.884 | 0.888 | 0.286 | 1.18x | 13.7/18.1/21.7% | 1.7/4.6% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.708 | 0.698 | 0.010 | - | - | 0.876 | 0.881 | 0.285 | 1.18x | 13.9/18.2/22.0% | 1.7/4.7% | 3 |
| 30 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 120 | 1 | 0.704 | 0.695 | 0.009 | - | - | 0.876 | 0.880 | 0.283 | 1.18x | 13.8/18.2/21.8% | 1.7/4.7% | 3 |
| 600 | 1 | 0.710 | 0.700 | 0.009 | - | - | 0.884 | 0.888 | 0.286 | 1.18x | 13.7/18.1/21.7% | 1.7/4.6% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.716 | 0.698 | 0.018 | - | - | 0.624 | 0.900 | 0.287 | 1.19x | 13.8/18.1/21.3% | 1.8/4.7% | 3 |
| routers | 1 | 0.701 | 0.694 | 0.006 | - | - | 0.816 | 0.817 | 0.283 | 1.17x | 13.5/18.0/21.5% | 1.7/4.7% | 3 |
| alternate-routers | 1 | 0.713 | 0.709 | 0.004 | - | - | 0.814 | 0.816 | 0.307 | 1.15x | 13.2/17.8/21.1% | 1.7/4.6% | 3 |
| beside-router | 1 | 0.717 | 0.701 | 0.016 | - | - | 0.876 | 0.877 | 0.294 | 1.17x | 13.6/18.1/21.6% | 1.7/4.6% | 3 |
| random-clients | 1 | 0.756 | 0.693 | 0.063 | - | - | 0.944 | 0.957 | 0.326 | 1.19x | 13.6/18.3/21.4% | 1.7/4.6% | 3 |
| hops-apart | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

> place=spread: decode_failures 11

> place=random-clients: decode_failures 7

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.716 | 0.698 | 0.018 | - | - | 0.624 | 0.900 | 0.287 | 1.19x | 13.8/18.1/21.3% | 1.8/4.7% | 3 |
| routers | 1 | 0.701 | 0.694 | 0.006 | - | - | 0.816 | 0.817 | 0.283 | 1.17x | 13.5/18.0/21.5% | 1.7/4.7% | 3 |
| alternate-routers | 1 | 0.713 | 0.709 | 0.004 | - | - | 0.814 | 0.816 | 0.307 | 1.15x | 13.2/17.8/21.1% | 1.7/4.6% | 3 |
| beside-router | 1 | 0.717 | 0.701 | 0.016 | - | - | 0.876 | 0.877 | 0.294 | 1.17x | 13.6/18.1/21.6% | 1.7/4.6% | 3 |
| random-clients | 1 | 0.756 | 0.693 | 0.063 | - | - | 0.944 | 0.957 | 0.326 | 1.19x | 13.6/18.3/21.4% | 1.7/4.6% | 3 |
| hops-apart | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

> place=spread: decode_failures 11

> place=random-clients: decode_failures 7

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| broadcast | 1 | 0.740 | 0.678 | 0.062 | - | - | 0.851 | 0.863 | 0.362 | 1.27x | 14.8/19.4/23.2% | 1.9/5.1% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| heard | 1 | 0.719 | 0.709 | 0.010 | - | - | 0.892 | 0.893 | 0.298 | 1.17x | 13.7/18.0/21.7% | 1.7/4.6% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.740 | 0.678 | 0.062 | - | - | 0.851 | 0.863 | 0.362 | 1.27x | 14.8/19.4/23.2% | 1.9/5.1% | 3 |
| heard | 1 | 0.758 | 0.700 | 0.058 | - | - | 0.871 | 0.883 | 0.374 | 1.24x | 14.5/19.0/22.8% | 1.8/4.9% | 3 |

> replay-ordering=heard: misdecodes 4

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| enum | 1 | 0.698 | 0.689 | 0.009 | - | - | 0.867 | 0.876 | 0.298 | 1.17x | 13.8/18.0/21.9% | 1.7/4.6% | 3 |
| hybrid | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.701 | 0.694 | 0.006 | - | - | 0.816 | 0.817 | 0.283 | 1.17x | 13.5/18.0/21.5% | 1.7/4.7% | 3 |
| 6 | 1 | 0.718 | 0.697 | 0.021 | - | - | 0.883 | 0.884 | 0.288 | 1.20x | 14.1/18.6/22.3% | 1.7/5.1% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.703 | 0.699 | 0.004 | - | - | 0.814 | 0.815 | 0.269 | 1.16x | 13.5/18.0/21.4% | 1.7/4.6% | 2 |
| 3 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 5 | 1 | 0.725 | 0.705 | 0.019 | - | - | 0.896 | 0.899 | 0.327 | 1.21x | 14.2/18.7/22.5% | 1.7/4.9% | 5 |
| 8 | 1 | 0.712 | 0.685 | 0.026 | - | - | 0.890 | 0.891 | 0.300 | 1.25x | 14.9/19.2/23.4% | 1.8/5.1% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.703 | 0.699 | 0.004 | - | - | 0.814 | 0.815 | 0.269 | 1.16x | 13.5/18.0/21.4% | 1.7/4.6% | 2 |
| 3 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 5 | 1 | 0.725 | 0.705 | 0.019 | - | - | 0.896 | 0.899 | 0.327 | 1.21x | 14.2/18.7/22.5% | 1.7/4.9% | 5 |
| 8 | 1 | 0.712 | 0.685 | 0.026 | - | - | 0.890 | 0.891 | 0.300 | 1.25x | 14.9/19.2/23.4% | 1.8/5.1% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| True | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.703 | 0.694 | 0.009 | - | - | 0.871 | 0.875 | 0.271 | 1.12x | 13.1/17.3/20.8% | 1.7/4.4% | 3 |
| 1 | 1 | 0.707 | 0.698 | 0.008 | - | - | 0.876 | 0.882 | 0.302 | 1.10x | 13.0/17.0/20.5% | 1.6/4.4% | 3 |
| 2 | 1 | 0.694 | 0.683 | 0.011 | - | - | 0.878 | 0.878 | 0.271 | 1.09x | 12.9/16.8/20.3% | 1.6/4.3% | 3 |
| 4 | 1 | 0.702 | 0.694 | 0.008 | - | - | 0.877 | 0.878 | 0.312 | 1.12x | 13.2/17.2/20.9% | 1.7/4.4% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.705 | 0.696 | 0.009 | - | - | 0.868 | 0.871 | 0.278 | 1.17x | 13.7/18.1/21.7% | 1.7/4.6% | 3 |
| 24 | 1 | 0.699 | 0.689 | 0.010 | - | - | 0.870 | 0.873 | 0.278 | 1.18x | 13.7/18.2/21.8% | 1.7/4.6% | 3 |
| 32 | 1 | 0.713 | 0.703 | 0.010 | - | - | 0.882 | 0.883 | 0.294 | 1.18x | 13.8/18.2/21.7% | 1.7/4.7% | 3 |
| 64 | 1 | 0.710 | 0.699 | 0.011 | - | - | 0.883 | 0.885 | 0.290 | 1.19x | 13.9/18.2/22.0% | 1.8/4.7% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.712 | 0.701 | 0.011 | - | - | 0.887 | 0.888 | 0.301 | 1.22x | 14.4/18.9/22.8% | 1.8/4.9% | 3 |
| 16 | 1 | 0.710 | 0.696 | 0.014 | - | - | 0.880 | 0.881 | 0.286 | 1.19x | 13.9/18.2/22.2% | 1.7/4.7% | 3 |
| 32 | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.886 | 0.891 | 0.295 | 1.17x | 13.7/17.9/21.5% | 1.7/4.6% | 3 |

> window-size=8: misdecodes 105

> window-size=16: misdecodes 38

> window-size=32: misdecodes 12

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.917 | 0.916 | 0.002 | - | - | 0.995 | 0.995 | 0.745 | 2.03x | 19.3/30.0/35.8% | 1.3/4.7% | 3 |
| True | 1 | 0.702 | 0.697 | 0.006 | - | - | 0.936 | 0.944 | 0.533 | 5.84x | 51.1/68.3/76.3% | 4.2/11.8% | 3 |

> no-congestion-scaling=True: decode_failures 1

> faster: 6.61 s per simulated hour against 20 over 8 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.507 | 0.499 | 0.008 | - | - | 0.711 | 0.712 | 0.000 | 4.60x | 15.7/30.5/44.2% | 1.5/5.5% | 3 |
| truesize | 1 | 0.538 | 0.531 | 0.007 | - | - | 0.742 | 0.744 | 0.000 | 3.41x | 11.5/24.4/35.8% | 1.1/4.5% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.920 | 0.917 | 0.003 | - | - | 0.998 | 0.999 | 0.732 | 1.94x | 18.2/28.4/34.1% | 1.2/4.5% | 3 |
| adaptive | 1 | 0.917 | 0.916 | 0.002 | - | - | 0.995 | 0.995 | 0.745 | 2.03x | 19.3/30.0/35.8% | 1.3/4.7% | 3 |

