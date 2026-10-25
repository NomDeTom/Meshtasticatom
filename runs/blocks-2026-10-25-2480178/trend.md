# Sweep blocks-2026-10-25-2480178

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 2480178 · seeds 2480178
- **blocks** 87 run
- **compute** 9.7 h of simulator time across every cell
- **generated** 2026-10-25T09:02:18+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>76 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 1
- AD-nomute: faster: 1.07 s per simulated hour against 2.28 over 65 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-worst: role-placement=degree: decode_failures 64
- AD-worst: role-placement=inverse: decode_failures 58
- AD-worst: slower: 20.6 s per simulated hour against 3.41 over 65 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 46
- DB-warm: warm-num-nodes=0: decode_failures 95
- DB-warm: warm-num-nodes=25: decode_failures 95
- DB-warm: warm-num-nodes=100: decode_failures 95
- DB-warm: warm-num-nodes=2000: decode_failures 95
- DG-burst: burst-loss=0.3: decode_failures 14
- DG-burst: faster: 1.92 s per simulated hour against 5.02 over 65 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DG-outage: burst-loss=0.1: decode_failures 36
- DG-outage: burst-loss=0.2: decode_failures 9
- DG-outage: burst-loss=0.3: decode_failures 37
- DM-mode: faster: 1.16 s per simulated hour against 3.18 over 65 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- LD-diurnal: faster: 0.695 s per simulated hour against 1.51 over 65 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 95
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 80
- MS-density: nodes=40: decode_failures 1
- MS-hopscale: nodes=120: decode_failures 65
- MS-hopscale: nodes=250: decode_failures 1
- MS-hopscale: nodes=500: decode_failures 246
- MS-oversubscribed: nodes=120: decode_failures 4
- MS-oversubscribed: nodes=500: decode_failures 186
- MS-oversubscribed: slower: 39.1 s per simulated hour against 19.4 over 65 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-size: nodes=40: decode_failures 1
- MS-size: nodes=120: decode_failures 65
- MS-topology: topology=hub: misdecodes 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 2
- RF-preset: faster: 0.879 s per simulated hour against 2.84 over 65 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 2
- RF-stretch-duct: faster: 0.814 s per simulated hour against 1.84 over 65 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=14: decode_failures 1
- RT-hopassign: faster: 0.801 s per simulated hour against 1.76 over 65 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RT-hoplimit: hop-limit=32: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 42
- SF-bucket-mode: bucket-mode=time: misdecodes 45
- SF-bucket-mode: bucket-mode=window: misdecodes 18
- SF-bucket-time: time-bucket-s=600: misdecodes 122
- SF-bucket-time: time-bucket-s=1800: misdecodes 45
- SF-bucket-time: time-bucket-s=3600: misdecodes 20
- SF-cadence: trigger=interval: misdecodes 23
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 34
- SF-cadence: faster: 1.23 s per simulated hour against 3.62 over 65 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-capacity-local: capacity=4: decode_failures 41
- SF-capacity-local: capacity=8: decode_failures 3
- SF-capacity: capacity=4: decode_failures 41
- SF-capacity: capacity=8: decode_failures 3
- SF-capacity-window: capacity=8: misdecodes 17
- SF-capacity-window: capacity=8: decode_failures 6
- SF-capacity-window: capacity=16: misdecodes 36
- SF-capacity-window: capacity=32: misdecodes 18
- SF-catchup: catch-up-hours=: misdecodes 34
- SF-catchup: catch-up-hours=02-06: decode_failures 2
- SF-catchup: catch-up-hours=00-08: decode_failures 1
- SF-catchup: faster: 3.52 s per simulated hour against 8.85 over 65 prior run(s) - 2.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: hops-apart=3: decode_failures 1
- SF-hops-flat: hops-apart=4: decode_failures 19
- SF-hops-flat: faster: 1.85 s per simulated hour against 3.96 over 65 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: hops-apart=3: decode_failures 1
- SF-hops-spread: hops-apart=4: decode_failures 19
- SF-hops-spread: hops-apart=5: decode_failures 28
- SF-place-flat: place=spread: decode_failures 6
- SF-place-flat: place=random-clients: decode_failures 2
- SF-place-spread: place=spread: decode_failures 6
- SF-place-spread: place=random-clients: decode_failures 2
- SF-place-spread: faster: 1.38 s per simulated hour against 2.79 over 65 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 16
- SF-replay-order: replay-ordering=heard: misdecodes 32
- SF-window-size: window-size=8: misdecodes 93
- SF-window-size: window-size=16: misdecodes 59
- SF-window-size: window-size=32: misdecodes 18
- TH-congestion: no-congestion-scaling=True: decode_failures 75

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 20.6 | 3.41 | 6.05x | 65 |
| `MS-oversubscribed` | 39.1 | 19.4 | 2.02x | 65 |
| `MS-hopscale` | 33.1 | 17.3 | 1.91x | 65 |
| `MS-size` | 6.45 | 3.39 | 1.90x | 65 |
| `SF-replay-order-broadcast` | 1.13 | 1.69 | 0.67x | 65 |
| `DB-platform` | 1.61 | 2.42 | 0.67x | 65 |
| `RF-txpower` | 1.04 | 1.58 | 0.66x | 65 |
| `PR-protocol` | 0.898 | 1.38 | 0.65x | 65 |
| `TH-congestion` | 10.9 | 17 | 0.64x | 65 |
| `LD-traceroute-small` | 23.2 | 36.6 | 0.64x | 65 |
| `RF-pulse` | 0.99 | 1.61 | 0.61x | 65 |
| `AD-siting` | 0.887 | 1.45 | 0.61x | 65 |
| `TH-congestion-input` | 6.32 | 10.3 | 0.61x | 65 |
| `FW-versions` | 0.918 | 1.52 | 0.60x | 65 |
| `LD-chatty` | 2.79 | 4.64 | 0.60x | 65 |
| `PR-crladder` | 1.68 | 2.79 | 0.60x | 65 |
| `DG-loss` | 1.35 | 2.27 | 0.59x | 65 |
| `PR-dmmode-cr` | 1.54 | 2.6 | 0.59x | 65 |
| `SF-servers-flat` | 1.35 | 2.29 | 0.59x | 65 |
| `SF-replay-order` | 0.914 | 1.56 | 0.58x | 65 |
| `RT-hoplimit` | 1 | 1.74 | 0.58x | 65 |
| `PR-repeats` | 0.918 | 1.62 | 0.56x | 65 |
| `MS-density` | 1.8 | 3.23 | 0.56x | 65 |
| `SC-signing` | 0.995 | 1.79 | 0.56x | 65 |
| `SF-sr-retries` | 0.848 | 1.53 | 0.55x | 65 |
| `RF-eu-presets` | 1.01 | 1.85 | 0.55x | 65 |
| `MS-stretch` | 1.17 | 2.16 | 0.54x | 65 |
| `SF-capacity` | 0.918 | 1.7 | 0.54x | 65 |
| `SF-jitter-local` | 0.914 | 1.79 | 0.51x | 65 |
| `AD-badrouters` | 1 | 2 | 0.50x | 65 |
| `SF-resolve` | 0.767 | 1.53 | 0.50x | 65 |
| `SF-place-spread` | 1.38 | 2.79 | 0.49x | 65 |
| `AD-nomute` | 1.07 | 2.28 | 0.47x | 65 |
| `SF-hops-flat` | 1.85 | 3.96 | 0.47x | 65 |
| `LD-diurnal` | 0.695 | 1.51 | 0.46x | 65 |
| `RT-hopassign` | 0.801 | 1.76 | 0.46x | 65 |
| `RF-stretch-duct` | 0.814 | 1.84 | 0.44x | 65 |
| `SF-catchup` | 3.52 | 8.85 | 0.40x | 65 |
| `DG-burst` | 1.92 | 5.02 | 0.38x | 65 |
| `DM-mode` | 1.16 | 3.18 | 0.37x | 65 |
| `SF-cadence` | 1.23 | 3.62 | 0.34x | 65 |
| `RF-preset` | 0.879 | 2.84 | 0.31x | 65 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.912 | 0.912 | 0.706 → 0.717 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.812 | 0.812 | 0.692 → 0.717 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.192 → 0.914 | 0.722 | 0.188 → 0.913 | 4.5x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **text** | 0.058 → 0.723 | 0.664 | 0.057 → 0.716 | 5x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.149 → 0.812 | 0.663 | 0.072 → 0.716 | 6x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.101 → 0.760 | 0.659 | 0.101 → 0.665 | 1.3e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.083 → 0.731 | 0.648 | 0.080 → 0.727 | 3.6x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **held** | 0.199 → 0.812 | 0.613 | 0.120 → 0.716 | 6.3x sr_airtime | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.266 → 0.820 | 0.554 | 0.239 → 0.716 | 4.5x sr_airtime | up | 4 |
| `RF-bw500` | preset | **text** | 0.135 → 0.684 | 0.549 | 0.134 → 0.674 | 3.4x sr_airtime | up | 3 |
| `RF-preset` | preset | **held** | 0.266 → 0.812 | 0.546 | 0.239 → 0.716 | 6.2x sr_airtime | up | 3 |
| `SF-place-flat` | place | **held** | 0.453 → 0.912 | 0.460 | 0.703 → 0.716 | 3.2x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.453 → 0.912 | 0.460 | 0.703 → 0.716 | 3.2x sr_bytes | up | 6 |
| `MS-density` | nodes | **text** | 0.538 → 0.940 | 0.402 | 0.520 → 0.936 | 4.9x advert_bytes | up | 5 |
| `MS-oversubscribed` | nodes | **held** | 0.545 → 0.941 | 0.395 | 0.334 → 0.645 | 5.2x bytes_on_air | down | 3 |
| `MS-hopscale` | nodes | **held** | 0.536 → 0.930 | 0.394 | 0.331 → 0.716 | 19x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.493 → 0.837 | 0.344 | 0.451 → 0.739 | 9.8x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.586 → 0.909 | 0.323 | 0.504 → 0.821 | 12x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.314 → 0.636 | 0.322 | 0.309 → 0.632 | 3.2x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.635 → 0.950 | 0.316 | 0.616 → 0.950 | 2.5x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.426 → 0.723 | 0.296 | 0.407 → 0.716 | 2.6x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.454 → 0.723 | 0.268 | 0.423 → 0.716 | 2.6x sr_bytes | down | 4 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.685 → 0.953 | 0.268 | 0.716 → 0.874 | 2.1x sr_bytes | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.588 → 0.830 | 0.242 | 0.562 → 0.830 | 2.3x sr_bytes | up | 4 |
| `MS-size` | nodes | **held** | 0.697 → 0.930 | 0.233 | 0.612 → 0.750 | 6.6x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.655 → 0.878 | 0.223 | 0.641 → 0.874 | 3.4x sr_airtime | down | 2 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.372 → 0.588 | 0.216 | 0.332 → 0.519 | 5.8x sr_airtime | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.723 → 0.934 | 0.212 | 0.716 → 0.932 | 2x sr_bytes | up | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.704 → 0.912 | 0.208 | 0.704 → 0.716 | 6.1x sr_bytes | down | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.588 → 0.784 | 0.196 | 0.562 → 0.780 | 1.9x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.650 → 0.812 | 0.162 | 0.565 → 0.716 | 1.3x sr_airtime | down | 4 |
| `FW-firmware` | profile | **held** | 0.812 → 0.963 | 0.151 | 0.716 → 0.797 | 3.2x bytes_on_air | down | 2 |
| `FW-versions` | profile | **held** | 0.812 → 0.961 | 0.148 | 0.716 → 0.798 | 3.4x bytes_on_air | down | 5 |
| `DB-hotstore` | max-num-nodes | **held** | 0.656 → 0.799 | 0.143 | 0.637 → 0.747 | 2.2x sr_airtime | up | 4 |
| `RT-spread` | hop-spread | **text** | 0.588 → 0.723 | 0.134 | 0.562 → 0.716 | 1.9x sr_bytes | up | 2 |
| `AD-badrouters` | role-placement | **text** | 0.599 → 0.731 | 0.132 | 0.590 → 0.727 | 1.6x sr_bytes | down | 3 |
| `LD-interval` | broadcast-interval-s | **held** | 0.759 → 0.888 | 0.129 | 0.659 → 0.771 | 5.7x sr_airtime | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.790 → 0.912 | 0.122 | 0.704 → 0.716 | 4.3x sr_bytes | down | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.812 → 0.934 | 0.122 | 0.716 → 0.796 | 2.3x bytes_on_air | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.680 → 0.799 | 0.120 | 0.649 → 0.747 | 2x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.606 → 0.723 | 0.117 | 0.595 → 0.716 | 1.2x sr_bytes | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.723 → 0.832 | 0.109 | 0.716 → 0.827 | 1.2x bytes_on_air | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.624 → 0.723 | 0.099 | 0.624 → 0.716 | 1.2x sr_airtime | down | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.812 → 0.906 | 0.094 | 0.716 → 0.778 | 2.4x bytes_on_air | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.772 → 0.862 | 0.090 | 0.575 → 0.632 | 1.4x sr_airtime | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.731 → 0.820 | 0.089 | 0.727 → 0.812 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.731 → 0.820 | 0.089 | 0.727 → 0.812 | 2.4x bytes_on_air | up | 3 |
| `SF-cadence` | trigger | **held** | 0.749 → 0.812 | 0.063 | 0.672 → 0.716 | 26x sr_bytes | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.756 → 0.813 | 0.056 | 0.658 → 0.716 | 1.5x sr_airtime | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.812 → 0.861 | 0.049 | 0.716 → 0.734 | 1.2x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.751 → 0.800 | 0.049 | 0.672 → 0.715 | 17x sr_bytes | up | 3 |
| `FW-signing-cost` | profile-flag | **held** | 0.812 → 0.859 | 0.047 | 0.716 → 0.748 | 3.3x bytes_on_air | down | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.799 → 0.839 | 0.040 | 0.716 → 0.749 | 1.3x bytes_on_air | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.860 → 0.891 | 0.032 | 0.750 → 0.758 | 1.2x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **held** | 0.876 → 0.905 | 0.029 | 0.727 → 0.752 | 1.2x bytes_on_air | down | 2 |
| `LD-diurnal` | diurnal | **held** | 0.812 → 0.841 | 0.029 | 0.716 → 0.738 | 1.3x sr_bytes | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.784 → 0.812 | 0.028 | 0.715 → 0.716 | 25x sr_airtime | down | 3 |
| `SF-capacity-window` | capacity | **held** | 0.807 → 0.834 | 0.027 | 0.712 → 0.723 | 2.6x advert_bytes | down | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.588 → 0.614 | 0.026 | 0.519 → 0.543 | 1.5x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.783 → 0.807 | 0.024 | 0.767 → 0.796 | 1x sr_bytes | down | 2 |
| `SF-capacity` | capacity | **held** | 0.798 → 0.818 | 0.019 | 0.706 → 0.717 | 5.1x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.798 → 0.818 | 0.019 | 0.706 → 0.717 | 5.1x advert_bytes | down | 5 |
| `DM-mode` | dm-mode | **held** | 0.775 → 0.793 | 0.018 | 0.686 → 0.699 | 1.1x sr_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.794 → 0.812 | 0.018 | 0.693 → 0.716 | 9.6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.794 → 0.812 | 0.018 | 0.693 → 0.716 | 9.6x sr_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.727 → 0.742 | 0.014 | 0.720 → 0.736 | 1.1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.864 → 0.878 | 0.014 | 0.859 → 0.874 | 1.2x sr_airtime | down | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.798 → 0.812 | 0.014 | 0.707 → 0.716 | 1.8x sr_airtime | down | 2 |
| `SF-window-size` | window-size | **held** | 0.798 → 0.812 | 0.014 | 0.699 → 0.714 | 5.2x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **text** | 0.710 → 0.723 | 0.012 | 0.703 → 0.716 | 3.1x advert_bytes | up | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.803 → 0.814 | 0.010 | 0.707 → 0.716 | 3.2x advert_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.803 → 0.813 | 0.010 | 0.711 → 0.721 | 1.1x sr_bytes | down | 4 |
| `SF-resolve` | resolve | **held** | 0.803 → 0.812 | 0.009 | 0.710 → 0.716 | 5.9x advert_bytes | = | 3 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.691 → 0.699 | 0.009 | 0.691 → 0.699 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.798 → 0.805 | 0.008 | 0.704 → 0.707 | 5.3x advert_bytes | down | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.804 → 0.812 | 0.008 | 0.709 → 0.716 | 1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.804 → 0.812 | 0.008 | 0.709 → 0.716 | 1x sr_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.812 → 0.817 | 0.005 | 0.709 → 0.716 | 3.3x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.706 → 0.710 | 0.004 | 0.703 → 0.708 | 3.2x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.878 → 0.882 | 0.004 | 0.874 → 0.878 | 1x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.723 → 0.726 | 0.003 | 0.716 → 0.719 | 1x bytes_on_air | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.718 → 0.721 | 0.003 | 0.703 → 0.707 | 1.1x sr_bytes | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.812 → 0.813 | 0.001 | 0.713 → 0.716 | 1.4x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.691 → 0.691 | 0.001 | 0.691 → 0.691 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.982 → 0.982 | 0.001 | 0.874 → 0.874 | 1.1x bytes_on_air | down | 2 |

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
| none | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| sprinkled | 1 | 0.819 | 0.811 | 0.009 | - | - | 0.928 | 0.930 | 0.451 | 1.17x | 13.7/22.8/27.6% | 1.7/5.5% | 3 |
| arms-race | 1 | 0.934 | 0.932 | 0.002 | - | - | 0.979 | 0.979 | 0.505 | 1.11x | 18.5/26.0/30.3% | 1.5/5.5% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.800 | 0.791 | 0.009 | - | - | 0.685 | 0.689 | 0.000 | 1.31x | 18.2/26.7/30.3% | 1.8/5.0% | 3 |
| 0.3 | 1 | 0.884 | 0.874 | 0.009 | - | - | 0.953 | 0.954 | 0.000 | 1.20x | 19.2/25.0/27.8% | 1.6/5.5% | 3 |

> amplify-worst=0.1: decode_failures 1

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.731 | 0.727 | 0.005 | - | - | 0.876 | 0.878 | 0.000 | 1.12x | 13.5/24.7/27.4% | 1.7/5.0% | 3 |
| inverse | 1 | 0.599 | 0.590 | 0.009 | - | - | 0.805 | 0.805 | 0.000 | 0.97x | 11.3/16.9/20.9% | 1.6/3.3% | 3 |
| random | 1 | 0.626 | 0.617 | 0.009 | - | - | 0.787 | 0.788 | 0.000 | 1.07x | 12.4/17.6/20.9% | 1.7/4.6% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.731 | 0.727 | 0.005 | - | - | 0.876 | 0.878 | 0.000 | 1.12x | 13.5/24.7/27.4% | 1.7/5.0% | 3 |
| all-routers | 1 | 0.820 | 0.812 | 0.007 | - | - | 0.877 | 0.878 | 0.000 | 2.64x | 29.4/41.0/43.5% | 4.4/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.731 | 0.727 | 0.005 | - | - | 0.876 | 0.878 | 0.000 | 1.12x | 13.5/24.7/27.4% | 1.7/5.0% | 3 |
| no-mute | 1 | 0.771 | 0.764 | 0.007 | - | - | 0.922 | 0.922 | 0.000 | 1.25x | 15.0/21.7/25.5% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.820 | 0.812 | 0.007 | - | - | 0.877 | 0.878 | 0.000 | 2.64x | 29.4/41.0/43.5% | 4.4/5.2% | 3 |

> faster: 1.07 s per simulated hour against 2.28 over 65 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.731 | 0.727 | 0.005 | - | - | 0.876 | 0.878 | 0.000 | 1.12x | 13.5/24.7/27.4% | 1.7/5.0% | 3 |
| local-typical | 1 | 0.633 | 0.627 | 0.005 | - | - | 0.767 | 0.769 | 0.000 | 1.13x | 11.7/21.8/26.7% | 1.8/4.8% | 3 |
| basement-heavy | 1 | 0.083 | 0.080 | 0.003 | - | - | 0.254 | 0.271 | 0.000 | 0.67x | 1.9/6.7/10.0% | 0.6/3.0% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.807 | 0.796 | 0.011 | - | - | 0.905 | 0.922 | 0.234 | 2.26x | 15.9/25.2/32.2% | 1.8/4.9% | 3 |
| inverse | 1 | 0.783 | 0.767 | 0.015 | - | - | 0.911 | 0.927 | 0.231 | 2.20x | 14.6/23.0/29.4% | 1.8/3.5% | 3 |

> role-placement=degree: decode_failures 64

> role-placement=inverse: decode_failures 58

> slower: 20.6 s per simulated hour against 3.41 over 65 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.717 | 0.717 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 15.0/27.9/30.5% | 1.8/4.7% | 3 |
| sr | 1 | 0.739 | 0.706 | 0.033 | - | - | 0.912 | 0.919 | 0.000 | 1.29x | 15.5/28.2/30.8% | 1.8/4.9% | 3 |

> protocol=sr: decode_failures 1

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.644 | 0.637 | 0.007 | - | - | 0.656 | 0.657 | 0.000 | 2.75x | 32.4/56.2/59.6% | 3.6/9.2% | 3 |
| 100 | 1 | 0.750 | 0.747 | 0.003 | - | - | 0.799 | 0.799 | 0.000 | 1.49x | 17.6/32.2/34.5% | 1.9/5.0% | 3 |
| 120 | 1 | 0.750 | 0.747 | 0.003 | - | - | 0.799 | 0.799 | 0.000 | 1.49x | 17.6/32.2/34.5% | 1.9/5.0% | 3 |
| 250 | 1 | 0.750 | 0.747 | 0.003 | - | - | 0.799 | 0.799 | 0.000 | 1.49x | 17.6/32.2/34.5% | 1.9/5.0% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.335 | 0.332 | 0.003 | - | - | 0.372 | 0.414 | 0.147 | 11.87x | 40.4/59.9/74.7% | 4.2/10.5% | 3 |
| 120 | 1 | 0.524 | 0.519 | 0.005 | - | - | 0.588 | 0.590 | 0.184 | 4.49x | 15.7/26.5/37.9% | 1.5/5.1% | 3 |
| 250 | 1 | 0.522 | 0.517 | 0.005 | - | - | 0.584 | 0.587 | 0.188 | 4.37x | 15.3/26.0/37.1% | 1.5/4.9% | 3 |

> max-num-nodes=10: decode_failures 46

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.750 | 0.747 | 0.003 | - | - | 0.799 | 0.799 | 0.000 | 1.49x | 17.6/32.2/34.5% | 1.9/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.750 | 0.747 | 0.003 | - | - | 0.799 | 0.799 | 0.000 | 1.49x | 17.6/32.2/34.5% | 1.9/5.0% | 3 |
| constrained | 1 | 0.656 | 0.649 | 0.008 | - | - | 0.680 | 0.680 | 0.000 | 2.76x | 32.4/56.2/59.6% | 3.7/9.3% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.646 | 0.632 | 0.014 | - | - | 0.862 | 0.907 | 0.358 | 5.11x | 52.3/69.4/76.0% | 3.5/11.6% | 3 |
| 25 | 1 | 0.646 | 0.632 | 0.014 | - | - | 0.862 | 0.907 | 0.358 | 5.11x | 52.3/69.4/76.0% | 3.5/11.6% | 3 |
| 100 | 1 | 0.646 | 0.632 | 0.014 | - | - | 0.862 | 0.907 | 0.358 | 5.11x | 52.3/69.4/76.0% | 3.5/11.6% | 3 |
| 2000 | 1 | 0.646 | 0.632 | 0.014 | - | - | 0.862 | 0.907 | 0.358 | 5.11x | 52.3/69.4/76.0% | 3.5/11.6% | 3 |

> warm-num-nodes=0: decode_failures 95

> warm-num-nodes=25: decode_failures 95

> warm-num-nodes=100: decode_failures 95

> warm-num-nodes=2000: decode_failures 95

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.630 | 0.616 | 0.014 | - | - | 0.773 | 0.775 | 0.000 | 1.19x | 14.4/26.3/28.7% | 1.7/4.4% | 3 |
| 0.2 | 1 | 0.545 | 0.521 | 0.024 | - | - | 0.735 | 0.735 | 0.000 | 1.08x | 13.4/23.8/26.3% | 1.6/3.9% | 3 |
| 0.3 | 1 | 0.454 | 0.423 | 0.031 | - | - | 0.656 | 0.664 | 0.000 | 0.99x | 12.4/22.1/24.6% | 1.4/3.6% | 3 |

> burst-loss=0.3: decode_failures 14

> faster: 1.92 s per simulated hour against 5.02 over 65 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.697 | 0.686 | 0.011 | - | - | 0.802 | 0.803 | 0.000 | 1.32x | 15.8/28.2/30.8% | 1.9/4.6% | 3 |
| 0.2 | 1 | 0.659 | 0.648 | 0.011 | - | - | 0.768 | 0.769 | 0.000 | 1.35x | 16.3/28.1/30.8% | 2.0/4.5% | 3 |
| 0.3 | 1 | 0.606 | 0.595 | 0.011 | - | - | 0.732 | 0.733 | 0.000 | 1.35x | 16.7/27.7/30.7% | 2.1/4.4% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.617 | 0.605 | 0.013 | - | - | 0.768 | 0.785 | 0.000 | 1.19x | 14.5/26.2/28.6% | 1.7/4.5% | 3 |
| 0.2 | 1 | 0.523 | 0.505 | 0.018 | - | - | 0.698 | 0.723 | 0.000 | 1.10x | 13.6/24.5/27.0% | 1.7/4.1% | 3 |
| 0.3 | 1 | 0.426 | 0.407 | 0.019 | - | - | 0.599 | 0.637 | 0.000 | 1.03x | 13.3/22.7/25.2% | 1.6/4.1% | 3 |

> burst-loss=0.1: decode_failures 36

> burst-loss=0.2: decode_failures 9

> burst-loss=0.3: decode_failures 37

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.686 | 0.686 | 0.000 | - | - | 0.778 | 0.780 | 0.000 | 1.59x | 18.7/35.3/38.3% | 2.2/6.0% | 3 |
| directed-with-late-flood | 1 | 0.699 | 0.699 | 0.000 | - | - | 0.793 | 0.795 | 0.000 | 1.49x | 17.6/33.2/36.1% | 2.1/5.6% | 3 |
| m4-early-flood | 1 | 0.687 | 0.687 | 0.000 | - | - | 0.775 | 0.776 | 0.000 | 1.48x | 17.5/32.9/35.7% | 2.0/5.5% | 3 |

> faster: 1.16 s per simulated hour against 3.18 over 65 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.804 | 0.797 | 0.007 | - | - | 0.963 | 0.964 | 0.000 | 0.70x | 8.5/11.0/13.3% | 1.1/2.1% | 3 |
| 2.8 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.807 | 0.796 | 0.010 | - | - | 0.914 | 0.915 | 0.000 | 1.15x | 13.2/20.2/23.6% | 1.8/4.3% | 3 |
| 0.5 | 1 | 0.793 | 0.781 | 0.012 | - | - | 0.934 | 0.935 | 0.000 | 1.04x | 12.5/17.7/21.1% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.758 | 0.751 | 0.007 | - | - | 0.888 | 0.890 | 0.000 | 0.79x | 9.5/13.2/14.9% | 1.3/2.4% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.786 | 0.778 | 0.008 | - | - | 0.890 | 0.891 | 0.000 | 1.13x | 12.8/19.9/23.5% | 1.7/4.2% | 3 |
| 0.5 | 1 | 0.769 | 0.757 | 0.012 | - | - | 0.906 | 0.908 | 0.000 | 0.99x | 12.1/16.6/20.1% | 1.4/4.1% | 3 |
| 0.75 | 1 | 0.755 | 0.746 | 0.008 | - | - | 0.883 | 0.884 | 0.000 | 0.76x | 9.3/12.5/14.3% | 1.3/2.4% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.754 | 0.748 | 0.006 | - | - | 0.859 | 0.859 | 0.000 | 0.68x | 8.5/16.4/18.0% | 0.9/2.8% | 3 |
| signing=true | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.787 | 0.780 | 0.007 | - | - | 0.950 | 0.951 | 0.000 | 0.70x | 8.9/11.8/14.5% | 1.1/2.1% | 3 |
| 2.5 | 1 | 0.797 | 0.791 | 0.006 | - | - | 0.956 | 0.957 | 0.000 | 0.69x | 8.6/11.6/14.2% | 1.1/2.0% | 3 |
| 2.6 | 1 | 0.792 | 0.785 | 0.006 | - | - | 0.945 | 0.948 | 0.000 | 0.67x | 8.7/11.6/14.2% | 1.1/2.1% | 3 |
| 2.7 | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.961 | 0.961 | 0.000 | 0.73x | 9.3/16.6/18.8% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.744 | 0.739 | 0.005 | - | - | 0.837 | 0.837 | 0.000 | 0.84x | 10.0/18.6/20.3% | 1.2/3.2% | 3 |
| 900 | 1 | 0.670 | 0.659 | 0.011 | - | - | 0.759 | 0.759 | 0.000 | 2.00x | 23.6/42.8/46.4% | 2.8/7.2% | 3 |
| 300 | 1 | 0.462 | 0.451 | 0.011 | - | - | 0.493 | 0.494 | 0.000 | 4.43x | 48.9/74.6/79.1% | 6.7/14.7% | 3 |

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.824 | 0.821 | 0.003 | - | - | 0.909 | 0.910 | 0.000 | 0.94x | 11.4/19.8/21.6% | 1.3/3.3% | 3 |
| 900 | 1 | 0.762 | 0.757 | 0.005 | - | - | 0.854 | 0.854 | 0.000 | 2.25x | 27.0/45.4/49.0% | 3.3/7.6% | 3 |
| 300 | 1 | 0.511 | 0.504 | 0.007 | - | - | 0.586 | 0.587 | 0.000 | 4.85x | 53.4/76.4/80.3% | 7.5/15.3% | 3 |

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.745 | 0.738 | 0.007 | - | - | 0.841 | 0.841 | 0.000 | 1.21x | 14.3/26.8/29.1% | 1.7/4.6% | 3 |
| sinusoid | 1 | 0.732 | 0.725 | 0.007 | - | - | 0.824 | 0.825 | 0.000 | 1.15x | 13.6/25.7/27.9% | 1.6/4.3% | 3 |
| commuter | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

> faster: 0.695 s per simulated hour against 1.51 over 65 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.670 | 0.659 | 0.011 | - | - | 0.759 | 0.759 | 0.000 | 2.00x | 23.6/42.8/46.4% | 2.8/7.2% | 3 |
| 3600 | 1 | 0.744 | 0.739 | 0.005 | - | - | 0.837 | 0.837 | 0.000 | 0.84x | 10.0/18.6/20.3% | 1.2/3.2% | 3 |
| 10800 | 1 | 0.776 | 0.771 | 0.005 | - | - | 0.888 | 0.888 | 0.000 | 0.56x | 6.6/12.5/13.6% | 0.8/2.1% | 3 |
| 43200 | 1 | 0.761 | 0.757 | 0.004 | - | - | 0.862 | 0.862 | 0.000 | 0.38x | 4.5/8.5/9.3% | 0.5/1.5% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.717 | 0.707 | 0.010 | - | - | 0.813 | 0.813 | 0.000 | 1.35x | 15.8/29.9/32.5% | 1.9/5.1% | 3 |
| 1.0 | 1 | 0.702 | 0.694 | 0.008 | - | - | 0.789 | 0.789 | 0.000 | 1.44x | 17.2/31.9/34.7% | 2.0/5.4% | 3 |
| 4.0 | 1 | 0.669 | 0.658 | 0.011 | - | - | 0.756 | 0.756 | 0.000 | 1.76x | 21.4/38.7/42.5% | 2.5/6.7% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.646 | 0.632 | 0.014 | - | - | 0.862 | 0.907 | 0.358 | 5.11x | 52.3/69.4/76.0% | 3.5/11.6% | 3 |
| 1.0 | 1 | 0.587 | 0.575 | 0.012 | - | - | 0.772 | 0.874 | 0.324 | 5.83x | 57.9/72.9/78.3% | 4.1/13.6% | 3 |

> traceroute-per-hour=0.0: decode_failures 95

> traceroute-per-hour=1.0: decode_failures 80

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.538 | 0.520 | 0.018 | - | - | 0.745 | 0.749 | 0.000 | 1.04x | 12.5/18.9/23.5% | 2.4/6.2% | 3 |
| 60 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 90 | 1 | 0.849 | 0.838 | 0.010 | - | - | 0.968 | 0.969 | 0.604 | 1.49x | 15.8/27.7/30.2% | 1.4/4.5% | 3 |
| 120 | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.982 | 0.983 | 0.621 | 1.83x | 19.6/32.4/37.7% | 1.2/4.7% | 3 |
| 150 | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.998 | 0.998 | 0.321 | 2.38x | 24.5/35.0/41.5% | 1.2/5.1% | 3 |

> nodes=40: decode_failures 1

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 120 | 1 | 0.660 | 0.643 | 0.017 | - | - | 0.930 | 0.939 | 0.381 | 2.13x | 15.8/22.4/27.7% | 1.4/4.6% | 3 |
| 250 | 1 | 0.512 | 0.507 | 0.005 | - | - | 0.577 | 0.578 | 0.177 | 4.82x | 17.1/28.4/40.4% | 1.7/5.4% | 3 |
| 500 | 1 | 0.337 | 0.331 | 0.006 | - | - | 0.536 | 0.553 | 0.054 | 10.89x | 20.5/39.5/66.7% | 1.8/6.8% | 3 |

> nodes=120: decode_failures 65

> nodes=250: decode_failures 1

> nodes=500: decode_failures 246

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.661 | 0.645 | 0.016 | - | - | 0.941 | 0.949 | 0.395 | 1.97x | 14.5/21.1/26.3% | 1.3/4.4% | 3 |
| 250 | 1 | 0.524 | 0.519 | 0.005 | - | - | 0.588 | 0.590 | 0.184 | 4.49x | 15.7/26.5/37.9% | 1.5/5.1% | 3 |
| 500 | 1 | 0.340 | 0.334 | 0.006 | - | - | 0.545 | 0.560 | 0.052 | 10.03x | 18.7/36.6/62.9% | 1.6/6.5% | 3 |

> nodes=120: decode_failures 4

> nodes=500: decode_failures 186

> slower: 39.1 s per simulated hour against 19.4 over 65 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.755 | 0.752 | 0.003 | - | - | 0.905 | 0.905 | 0.000 | 1.30x | 15.2/29.2/31.7% | 1.9/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.731 | 0.727 | 0.005 | - | - | 0.876 | 0.878 | 0.000 | 1.12x | 13.5/24.7/27.4% | 1.7/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.763 | 0.758 | 0.005 | - | - | 0.891 | 0.891 | 0.000 | 1.32x | 15.4/28.8/31.4% | 1.9/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.754 | 0.750 | 0.003 | - | - | 0.860 | 0.860 | 0.000 | 1.27x | 15.3/28.6/31.1% | 2.1/5.0% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.05 | 1 | 0.726 | 0.720 | 0.006 | - | - | 0.802 | 0.803 | 0.000 | 1.41x | 15.9/30.3/34.1% | 1.9/4.8% | 3 |
| 0.1 | 1 | 0.727 | 0.723 | 0.004 | - | - | 0.799 | 0.799 | 0.000 | 1.45x | 16.3/31.3/34.9% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.757 | 0.749 | 0.008 | - | - | 0.839 | 0.839 | 0.000 | 1.68x | 19.9/36.2/40.4% | 2.5/4.8% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| local-typical | 1 | 0.655 | 0.641 | 0.014 | - | - | 0.763 | 0.763 | 0.000 | 1.39x | 12.8/25.5/30.3% | 2.1/5.1% | 3 |
| event | 1 | 0.192 | 0.188 | 0.004 | - | - | 0.364 | 0.373 | 0.000 | 1.21x | 6.2/17.6/27.3% | 1.5/5.0% | 3 |
| backbone | 1 | 0.914 | 0.913 | 0.001 | - | - | 0.956 | 0.957 | 0.000 | 1.10x | 25.1/32.4/35.8% | 1.4/5.5% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.693 | 0.683 | 0.010 | - | - | 0.867 | 0.876 | 0.000 | 1.19x | 19.1/24.6/26.0% | 2.6/6.9% | 3 |
| 60 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 90 | 1 | 0.775 | 0.750 | 0.025 | - | - | 0.856 | 0.858 | 0.413 | 1.56x | 14.2/19.2/23.2% | 1.6/4.3% | 3 |
| 120 | 1 | 0.660 | 0.643 | 0.017 | - | - | 0.930 | 0.939 | 0.381 | 2.13x | 15.8/22.4/27.7% | 1.4/4.6% | 3 |
| 150 | 1 | 0.622 | 0.612 | 0.011 | - | - | 0.697 | 0.698 | 0.195 | 2.58x | 15.2/22.7/28.0% | 1.4/4.5% | 3 |

> nodes=40: decode_failures 1

> nodes=120: decode_failures 65

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 1.25 | 1 | 0.471 | 0.467 | 0.004 | - | - | 0.610 | 0.611 | 0.107 | 1.27x | 12.6/23.5/27.3% | 1.8/4.8% | 3 |
| 1.5 | 1 | 0.314 | 0.309 | 0.004 | - | - | 0.372 | 0.373 | 0.127 | 1.65x | 11.7/24.9/32.7% | 2.5/5.6% | 3 |
| 2.0 | 1 | 0.121 | 0.120 | 0.001 | - | - | 0.199 | 0.199 | 0.000 | 0.98x | 4.5/14.3/19.3% | 1.4/4.2% | 3 |

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| clustered | 1 | 0.766 | 0.766 | 0.000 | - | - | 0.859 | 0.860 | 0.000 | 1.15x | 29.6/38.2/39.8% | 1.5/5.6% | 3 |
| corridor | 1 | 0.635 | 0.616 | 0.019 | - | - | 0.838 | 0.838 | 0.157 | 1.31x | 15.8/21.3/24.3% | 1.9/5.9% | 3 |
| hub | 1 | 0.950 | 0.950 | 0.000 | - | - | 0.981 | 0.981 | 0.759 | 1.24x | 27.5/36.8/39.5% | 1.9/5.6% | 3 |

> topology=hub: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.699 | 0.699 | 0.000 | - | - | 0.793 | 0.795 | 0.000 | 1.49x | 17.6/33.2/36.1% | 2.1/5.6% | 3 |
| True | 1 | 0.691 | 0.691 | 0.000 | - | - | 0.786 | 0.786 | 0.000 | 1.51x | 17.7/33.6/36.4% | 2.1/5.7% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.691 | 0.691 | 0.000 | - | - | 0.786 | 0.786 | 0.000 | 1.51x | 17.7/33.6/36.4% | 2.1/5.7% | 3 |
| m4-early-flood | 1 | 0.691 | 0.691 | 0.000 | - | - | 0.786 | 0.787 | 0.000 | 1.51x | 17.6/33.7/36.4% | 2.1/5.7% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.717 | 0.717 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 15.0/27.9/30.5% | 1.8/4.7% | 3 |
| chain | 1 | 0.695 | 0.692 | 0.004 | - | - | 0.765 | 0.787 | 0.000 | 1.48x | 17.2/33.2/35.6% | 2.1/5.6% | 3 |
| sr | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| True | 1 | 0.726 | 0.719 | 0.007 | - | - | 0.815 | 0.815 | 0.000 | 1.31x | 15.5/28.8/31.2% | 1.8/4.8% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.982 | 0.983 | 0.621 | 1.83x | 19.6/32.4/37.7% | 1.2/4.7% | 3 |
| True | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.984 | 0.985 | 0.631 | 1.88x | 20.0/32.8/38.2% | 1.2/4.8% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.135 | 0.134 | 0.002 | - | - | 0.258 | 0.262 | 0.000 | 0.04x | 0.2/0.8/1.0% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.322 | 0.319 | 0.003 | - | - | 0.372 | 0.373 | 0.000 | 0.25x | 1.9/4.4/5.0% | 0.4/0.9% | 3 |
| LONG_TURBO | 1 | 0.684 | 0.674 | 0.010 | - | - | 0.806 | 0.807 | 0.000 | 1.27x | 13.2/24.9/27.6% | 1.9/4.4% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.745 | 0.739 | 0.006 | - | - | 0.832 | 0.832 | 0.001 | 1.25x | 16.5/29.1/31.7% | 1.8/4.9% | 3 |
| 1.0 | 1 | 0.832 | 0.827 | 0.005 | - | - | 0.897 | 0.897 | 0.005 | 1.03x | 19.4/27.4/30.8% | 1.3/4.8% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.240 | 0.239 | 0.000 | - | - | 0.266 | 0.270 | 0.000 | 0.13x | 0.8/1.8/2.6% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| LITE_FAST | 1 | 0.706 | 0.698 | 0.008 | - | - | 0.820 | 0.820 | 0.000 | 0.96x | 10.9/19.0/21.1% | 1.5/3.7% | 3 |
| NARROW_SLOW | 1 | 0.708 | 0.701 | 0.007 | - | - | 0.806 | 0.808 | 0.000 | 1.23x | 13.8/23.9/27.2% | 1.8/4.7% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| temporal | 1 | 0.663 | 0.654 | 0.010 | - | - | 0.755 | 0.755 | 0.000 | 1.30x | 15.3/27.2/30.3% | 1.9/4.6% | 3 |
| transient | 1 | 0.713 | 0.708 | 0.005 | - | - | 0.807 | 0.808 | 0.000 | 1.28x | 15.0/28.2/30.6% | 1.8/4.8% | 3 |
| periodic | 1 | 0.572 | 0.565 | 0.007 | - | - | 0.650 | 0.650 | 0.000 | 1.16x | 13.9/24.9/27.3% | 1.7/4.1% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.240 | 0.239 | 0.000 | - | - | 0.266 | 0.270 | 0.000 | 0.13x | 0.8/1.8/2.6% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| LONG_MODERATE | 1 | 0.704 | 0.687 | 0.016 | - | - | 0.770 | 0.771 | 0.000 | 3.21x | 39.8/61.7/67.6% | 4.6/11.0% | 3 |

> faster: 0.879 s per simulated hour against 2.84 over 65 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.058 | 0.057 | 0.001 | - | - | 0.167 | 0.168 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.135 | 0.134 | 0.002 | - | - | 0.258 | 0.262 | 0.000 | 0.04x | 0.2/0.8/1.0% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| LONG_TURBO | 1 | 0.684 | 0.674 | 0.010 | - | - | 0.806 | 0.807 | 0.000 | 1.27x | 13.2/24.9/27.6% | 1.9/4.4% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.682 | 0.670 | 0.012 | - | - | 0.780 | 0.783 | 0.000 | 1.70x | 19.3/34.7/39.0% | 2.5/6.2% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.674 | 0.665 | 0.008 | - | - | 0.760 | 0.760 | 0.000 | 1.25x | 15.0/27.7/30.2% | 1.8/4.6% | 3 |
| 10000 | 1 | 0.572 | 0.565 | 0.007 | - | - | 0.650 | 0.650 | 0.000 | 1.16x | 13.9/24.9/27.3% | 1.7/4.1% | 3 |
| 4000 | 1 | 0.339 | 0.333 | 0.006 | - | - | 0.401 | 0.410 | 0.000 | 0.99x | 12.1/20.7/23.0% | 1.5/3.2% | 3 |
| 2000 | 1 | 0.101 | 0.101 | 0.000 | - | - | 0.101 | 0.144 | 0.000 | 0.72x | 9.0/15.0/17.4% | 1.2/2.0% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.314 | 0.309 | 0.004 | - | - | 0.372 | 0.373 | 0.127 | 1.65x | 11.7/24.9/32.7% | 2.5/5.6% | 3 |
| 1.0 | 1 | 0.636 | 0.632 | 0.003 | - | - | 0.681 | 0.681 | 0.371 | 1.11x | 13.7/23.8/26.8% | 1.6/4.3% | 3 |

> faster: 0.814 s per simulated hour against 1.84 over 65 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 22 | 1 | 0.299 | 0.296 | 0.003 | - | - | 0.345 | 0.346 | 0.000 | 1.64x | 11.7/25.8/29.9% | 2.4/5.4% | 3 |
| 17 | 1 | 0.129 | 0.127 | 0.002 | - | - | 0.239 | 0.242 | 0.000 | 0.99x | 4.2/16.3/19.4% | 1.5/4.2% | 3 |
| 14 | 1 | 0.074 | 0.072 | 0.002 | - | - | 0.149 | 0.186 | 0.000 | 0.67x | 2.5/8.5/12.4% | 0.9/3.1% | 3 |

> tx-power=14: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.982 | 0.983 | 0.621 | 1.83x | 19.6/32.4/37.7% | 1.2/4.7% | 3 |
| True | 1 | 0.864 | 0.859 | 0.005 | - | - | 0.980 | 0.981 | 0.595 | 2.14x | 22.6/36.6/42.2% | 1.4/5.3% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.818 | 0.818 | 0.000 | 1.34x | 15.5/29.2/32.2% | 1.8/4.8% | 3 |
| True | 1 | 0.742 | 0.736 | 0.006 | - | - | 0.814 | 0.814 | 0.000 | 1.41x | 16.4/29.9/33.0% | 1.9/4.9% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| random | 1 | 0.744 | 0.734 | 0.010 | - | - | 0.861 | 0.862 | 0.000 | 1.25x | 15.0/27.1/29.6% | 1.8/4.6% | 3 |

> faster: 0.801 s per simulated hour against 1.76 over 65 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.588 | 0.562 | 0.026 | - | - | 0.751 | 0.752 | 0.000 | 1.02x | 11.9/24.1/26.6% | 1.4/4.3% | 3 |
| 7 | 1 | 0.784 | 0.780 | 0.004 | - | - | 0.870 | 0.870 | 0.000 | 1.43x | 17.1/30.1/32.6% | 2.0/5.1% | 3 |
| 15 | 1 | 0.826 | 0.825 | 0.000 | - | - | 0.899 | 0.899 | 0.000 | 1.46x | 17.4/30.4/33.0% | 2.1/5.1% | 3 |
| 32 | 1 | 0.830 | 0.830 | 0.000 | - | - | 0.901 | 0.901 | 0.000 | 1.48x | 17.6/30.6/33.3% | 2.1/5.1% | 3 |

> hop-limit=32: misdecodes 1

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.588 | 0.562 | 0.026 | - | - | 0.751 | 0.752 | 0.000 | 1.02x | 11.9/24.1/26.6% | 1.4/4.3% | 3 |
| 5 | 1 | 0.736 | 0.725 | 0.010 | - | - | 0.838 | 0.839 | 0.000 | 1.30x | 15.7/28.1/30.7% | 1.9/4.7% | 3 |
| 7 | 1 | 0.784 | 0.780 | 0.004 | - | - | 0.870 | 0.870 | 0.000 | 1.43x | 17.1/30.1/32.6% | 2.0/5.1% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| KNOWN_ONLY | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.715 | 0.715 | 0.000 | - | - | 0.784 | 0.819 | 0.000 | 1.27x | 15.1/28.1/30.5% | 1.8/4.7% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.588 | 0.562 | 0.026 | - | - | 0.751 | 0.752 | 0.000 | 1.02x | 11.9/24.1/26.6% | 1.4/4.3% | 3 |
| True | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| BALANCED | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| STRICT | 1 | 0.624 | 0.624 | 0.000 | - | - | 0.729 | 0.729 | 0.000 | 1.35x | 16.0/29.8/32.4% | 1.9/5.0% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| dm | 1 | 0.718 | 0.709 | 0.009 | - | - | 0.817 | 0.818 | 0.000 | 1.24x | 14.7/27.9/30.2% | 1.8/4.8% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.719 | 0.712 | 0.007 | - | - | 0.814 | 0.814 | 0.000 | 1.28x | 15.0/28.4/30.9% | 1.8/4.8% | 3 |
| local | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| time | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.803 | 0.804 | 0.000 | 1.31x | 15.4/29.1/31.5% | 1.9/5.0% | 3 |
| window | 1 | 0.720 | 0.714 | 0.006 | - | - | 0.812 | 0.813 | 0.000 | 1.27x | 15.0/28.2/30.7% | 1.8/4.8% | 3 |

> bucket-mode=global: misdecodes 42

> bucket-mode=time: misdecodes 45

> bucket-mode=window: misdecodes 18

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.712 | 0.704 | 0.008 | - | - | 0.805 | 0.806 | 0.000 | 1.43x | 16.3/31.8/34.1% | 2.0/5.5% | 3 |
| 1800 | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.803 | 0.804 | 0.000 | 1.31x | 15.4/29.1/31.5% | 1.9/5.0% | 3 |
| 3600 | 1 | 0.711 | 0.704 | 0.007 | - | - | 0.798 | 0.799 | 0.000 | 1.28x | 15.1/28.5/30.9% | 1.8/4.8% | 3 |

> time-bucket-s=600: misdecodes 122

> time-bucket-s=1800: misdecodes 45

> time-bucket-s=3600: misdecodes 20

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| interval | 1 | 0.681 | 0.673 | 0.008 | - | - | 0.749 | 0.756 | 0.000 | 1.72x | 18.9/39.4/41.8% | 2.4/7.3% | 3 |
| aimd | 1 | 0.714 | 0.711 | 0.003 | - | - | 0.783 | 0.805 | 0.000 | 1.29x | 15.3/28.5/30.9% | 1.8/4.8% | 3 |
| bucket+interval | 1 | 0.682 | 0.672 | 0.011 | - | - | 0.751 | 0.751 | 0.000 | 1.79x | 19.2/41.6/44.0% | 2.5/7.9% | 3 |

> trigger=interval: misdecodes 23

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 34

> faster: 1.23 s per simulated hour against 3.62 over 65 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.721 | 0.714 | 0.007 | - | - | 0.817 | 0.817 | 0.000 | 1.26x | 15.0/28.1/30.6% | 1.8/4.8% | 3 |
| 8 | 1 | 0.725 | 0.717 | 0.008 | - | - | 0.818 | 0.819 | 0.000 | 1.27x | 15.0/28.1/30.7% | 1.8/4.8% | 3 |
| 16 | 1 | 0.715 | 0.706 | 0.009 | - | - | 0.798 | 0.800 | 0.000 | 1.26x | 15.0/28.0/30.4% | 1.8/4.8% | 3 |
| 32 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 50 | 1 | 0.717 | 0.709 | 0.008 | - | - | 0.808 | 0.809 | 0.000 | 1.26x | 14.8/27.8/30.3% | 1.8/4.7% | 3 |

> capacity=4: decode_failures 41

> capacity=8: decode_failures 3

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.721 | 0.714 | 0.007 | - | - | 0.817 | 0.817 | 0.000 | 1.26x | 15.0/28.1/30.6% | 1.8/4.8% | 3 |
| 8 | 1 | 0.725 | 0.717 | 0.008 | - | - | 0.818 | 0.819 | 0.000 | 1.27x | 15.0/28.1/30.7% | 1.8/4.8% | 3 |
| 16 | 1 | 0.715 | 0.706 | 0.009 | - | - | 0.798 | 0.800 | 0.000 | 1.26x | 15.0/28.0/30.4% | 1.8/4.8% | 3 |
| 32 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 50 | 1 | 0.717 | 0.709 | 0.008 | - | - | 0.808 | 0.809 | 0.000 | 1.26x | 14.8/27.8/30.3% | 1.8/4.7% | 3 |

> capacity=4: decode_failures 41

> capacity=8: decode_failures 3

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.732 | 0.723 | 0.009 | - | - | 0.834 | 0.836 | 0.000 | 1.27x | 15.1/28.1/30.6% | 1.8/4.7% | 3 |
| 16 | 1 | 0.719 | 0.712 | 0.007 | - | - | 0.807 | 0.808 | 0.000 | 1.28x | 15.2/28.5/31.1% | 1.8/4.8% | 3 |
| 32 | 1 | 0.720 | 0.714 | 0.006 | - | - | 0.812 | 0.813 | 0.000 | 1.27x | 15.0/28.2/30.7% | 1.8/4.8% | 3 |

> capacity=8: misdecodes 17

> capacity=8: decode_failures 6

> capacity=16: misdecodes 36

> capacity=32: misdecodes 18

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.682 | 0.672 | 0.011 | - | - | 0.751 | 0.751 | 0.000 | 1.79x | 19.2/41.6/44.0% | 2.5/7.9% | 3 |
| 02-06 | 1 | 0.717 | 0.712 | 0.005 | - | - | 0.799 | 0.818 | 0.000 | 1.30x | 15.4/28.9/31.4% | 1.9/4.9% | 3 |
| 00-08 | 1 | 0.720 | 0.715 | 0.005 | - | - | 0.800 | 0.813 | 0.000 | 1.35x | 15.8/30.2/32.6% | 2.0/5.2% | 3 |

> catch-up-hours=: misdecodes 34

> catch-up-hours=02-06: decode_failures 2

> catch-up-hours=00-08: decode_failures 1

> faster: 3.52 s per simulated hour against 8.85 over 65 prior run(s) - 2.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.708 | 0.704 | 0.005 | - | - | 0.796 | 0.797 | 0.000 | 1.26x | 14.9/28.0/30.5% | 1.8/4.7% | 3 |
| 2 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 3 | 1 | 0.739 | 0.706 | 0.033 | - | - | 0.912 | 0.919 | 0.000 | 1.29x | 15.5/28.2/30.8% | 1.8/4.9% | 3 |
| 4 | 1 | 0.735 | 0.708 | 0.027 | - | - | 0.790 | 0.927 | 0.000 | 1.29x | 15.3/28.0/30.6% | 1.7/4.8% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 19

> faster: 1.85 s per simulated hour against 3.96 over 65 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.708 | 0.704 | 0.005 | - | - | 0.796 | 0.797 | 0.000 | 1.26x | 14.9/28.0/30.5% | 1.8/4.7% | 3 |
| 2 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 3 | 1 | 0.739 | 0.706 | 0.033 | - | - | 0.912 | 0.919 | 0.000 | 1.29x | 15.5/28.2/30.8% | 1.8/4.9% | 3 |
| 4 | 1 | 0.735 | 0.708 | 0.027 | - | - | 0.790 | 0.927 | 0.000 | 1.29x | 15.3/28.0/30.6% | 1.7/4.8% | 3 |
| 5 | 1 | 0.740 | 0.715 | 0.025 | - | - | 0.704 | 0.897 | 0.000 | 1.31x | 15.3/28.7/31.5% | 1.8/5.1% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 19

> hops-apart=5: decode_failures 28

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.716 | 0.709 | 0.007 | - | - | 0.807 | 0.807 | 0.000 | 1.29x | 15.2/28.7/31.2% | 1.8/4.9% | 3 |
| 30 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 120 | 1 | 0.721 | 0.714 | 0.008 | - | - | 0.808 | 0.809 | 0.000 | 1.27x | 15.0/28.3/30.8% | 1.8/4.8% | 3 |
| 600 | 1 | 0.720 | 0.714 | 0.006 | - | - | 0.804 | 0.804 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.716 | 0.709 | 0.007 | - | - | 0.807 | 0.807 | 0.000 | 1.29x | 15.2/28.7/31.2% | 1.8/4.9% | 3 |
| 30 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 120 | 1 | 0.721 | 0.714 | 0.008 | - | - | 0.808 | 0.809 | 0.000 | 1.27x | 15.0/28.3/30.8% | 1.8/4.8% | 3 |
| 600 | 1 | 0.720 | 0.714 | 0.006 | - | - | 0.804 | 0.804 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.723 | 0.709 | 0.014 | - | - | 0.453 | 0.868 | 0.000 | 1.28x | 15.3/27.9/30.5% | 1.8/4.7% | 3 |
| routers | 1 | 0.710 | 0.708 | 0.003 | - | - | 0.793 | 0.793 | 0.000 | 1.28x | 15.1/28.5/31.0% | 1.8/4.8% | 3 |
| alternate-routers | 1 | 0.717 | 0.715 | 0.002 | - | - | 0.802 | 0.803 | 0.000 | 1.26x | 15.0/28.0/30.5% | 1.8/4.7% | 3 |
| beside-router | 1 | 0.711 | 0.704 | 0.007 | - | - | 0.801 | 0.802 | 0.000 | 1.29x | 15.2/28.7/31.2% | 1.8/4.8% | 3 |
| random-clients | 1 | 0.733 | 0.703 | 0.029 | - | - | 0.912 | 0.919 | 0.000 | 1.29x | 15.4/28.1/30.7% | 1.8/4.7% | 3 |
| hops-apart | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

> place=spread: decode_failures 6

> place=random-clients: decode_failures 2

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.723 | 0.709 | 0.014 | - | - | 0.453 | 0.868 | 0.000 | 1.28x | 15.3/27.9/30.5% | 1.8/4.7% | 3 |
| routers | 1 | 0.710 | 0.708 | 0.003 | - | - | 0.793 | 0.793 | 0.000 | 1.28x | 15.1/28.5/31.0% | 1.8/4.8% | 3 |
| alternate-routers | 1 | 0.717 | 0.715 | 0.002 | - | - | 0.802 | 0.803 | 0.000 | 1.26x | 15.0/28.0/30.5% | 1.8/4.7% | 3 |
| beside-router | 1 | 0.711 | 0.704 | 0.007 | - | - | 0.801 | 0.802 | 0.000 | 1.29x | 15.2/28.7/31.2% | 1.8/4.8% | 3 |
| random-clients | 1 | 0.733 | 0.703 | 0.029 | - | - | 0.912 | 0.919 | 0.000 | 1.29x | 15.4/28.1/30.7% | 1.8/4.7% | 3 |
| hops-apart | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

> place=spread: decode_failures 6

> place=random-clients: decode_failures 2

> faster: 1.38 s per simulated hour against 2.79 over 65 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| broadcast | 1 | 0.721 | 0.707 | 0.014 | - | - | 0.798 | 0.799 | 0.000 | 1.32x | 15.5/29.5/31.9% | 1.9/5.0% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| heard | 1 | 0.723 | 0.713 | 0.009 | - | - | 0.813 | 0.813 | 0.000 | 1.29x | 15.2/28.5/31.0% | 1.8/4.8% | 3 |

> replay-ordering=heard: misdecodes 32

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.721 | 0.707 | 0.014 | - | - | 0.798 | 0.799 | 0.000 | 1.32x | 15.5/29.5/31.9% | 1.9/5.0% | 3 |
| heard | 1 | 0.718 | 0.703 | 0.015 | - | - | 0.796 | 0.797 | 0.000 | 1.31x | 15.3/29.2/31.7% | 1.9/4.9% | 3 |

> replay-ordering=heard: misdecodes 16

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| enum | 1 | 0.718 | 0.710 | 0.009 | - | - | 0.803 | 0.804 | 0.000 | 1.27x | 15.0/28.5/30.9% | 1.8/4.9% | 3 |
| hybrid | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.710 | 0.708 | 0.003 | - | - | 0.793 | 0.793 | 0.000 | 1.28x | 15.1/28.5/31.0% | 1.8/4.8% | 3 |
| 6 | 1 | 0.706 | 0.703 | 0.003 | - | - | 0.790 | 0.790 | 0.000 | 1.31x | 15.4/29.1/31.6% | 1.8/5.0% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.713 | 0.708 | 0.004 | - | - | 0.794 | 0.794 | 0.000 | 1.26x | 14.9/28.1/30.5% | 1.8/4.8% | 2 |
| 3 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 5 | 1 | 0.715 | 0.708 | 0.007 | - | - | 0.808 | 0.811 | 0.000 | 1.31x | 15.3/29.2/31.6% | 1.9/5.0% | 5 |
| 8 | 1 | 0.712 | 0.693 | 0.020 | - | - | 0.810 | 0.811 | 0.000 | 1.34x | 15.4/29.9/32.4% | 1.9/5.1% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.713 | 0.708 | 0.004 | - | - | 0.794 | 0.794 | 0.000 | 1.26x | 14.9/28.1/30.5% | 1.8/4.8% | 2 |
| 3 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 5 | 1 | 0.715 | 0.708 | 0.007 | - | - | 0.808 | 0.811 | 0.000 | 1.31x | 15.3/29.2/31.6% | 1.9/5.0% | 5 |
| 8 | 1 | 0.712 | 0.693 | 0.020 | - | - | 0.810 | 0.811 | 0.000 | 1.34x | 15.4/29.9/32.4% | 1.9/5.1% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| True | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.728 | 0.719 | 0.009 | - | - | 0.812 | 0.813 | 0.000 | 1.20x | 14.2/26.4/28.6% | 1.7/4.5% | 3 |
| 1 | 1 | 0.728 | 0.721 | 0.008 | - | - | 0.813 | 0.816 | 0.000 | 1.19x | 14.1/26.3/28.7% | 1.7/4.4% | 3 |
| 2 | 1 | 0.721 | 0.711 | 0.010 | - | - | 0.803 | 0.804 | 0.000 | 1.19x | 14.2/26.3/28.6% | 1.7/4.5% | 3 |
| 4 | 1 | 0.721 | 0.711 | 0.010 | - | - | 0.803 | 0.804 | 0.000 | 1.19x | 14.2/26.3/28.6% | 1.7/4.5% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.710 | 0.703 | 0.007 | - | - | 0.805 | 0.809 | 0.000 | 1.27x | 15.2/28.3/30.8% | 1.8/4.8% | 3 |
| 24 | 1 | 0.718 | 0.711 | 0.007 | - | - | 0.813 | 0.813 | 0.000 | 1.28x | 15.2/28.4/30.9% | 1.8/4.8% | 3 |
| 32 | 1 | 0.723 | 0.716 | 0.007 | - | - | 0.812 | 0.812 | 0.000 | 1.27x | 15.1/28.3/30.7% | 1.8/4.8% | 3 |
| 64 | 1 | 0.716 | 0.708 | 0.008 | - | - | 0.806 | 0.807 | 0.000 | 1.28x | 15.1/28.4/30.8% | 1.8/4.8% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.707 | 0.699 | 0.009 | - | - | 0.798 | 0.798 | 0.000 | 1.35x | 15.8/29.9/32.3% | 2.0/5.0% | 3 |
| 16 | 1 | 0.713 | 0.706 | 0.007 | - | - | 0.806 | 0.806 | 0.000 | 1.31x | 15.5/29.0/31.4% | 1.9/4.9% | 3 |
| 32 | 1 | 0.720 | 0.714 | 0.006 | - | - | 0.812 | 0.813 | 0.000 | 1.27x | 15.0/28.2/30.7% | 1.8/4.8% | 3 |

> window-size=8: misdecodes 93

> window-size=16: misdecodes 59

> window-size=32: misdecodes 18

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.982 | 0.983 | 0.621 | 1.83x | 19.6/32.4/37.7% | 1.2/4.7% | 3 |
| True | 1 | 0.655 | 0.641 | 0.014 | - | - | 0.866 | 0.914 | 0.363 | 5.03x | 51.8/69.4/75.9% | 3.5/11.6% | 3 |

> no-congestion-scaling=True: decode_failures 75

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.524 | 0.519 | 0.005 | - | - | 0.588 | 0.590 | 0.184 | 4.49x | 15.7/26.5/37.9% | 1.5/5.1% | 3 |
| truesize | 1 | 0.548 | 0.543 | 0.005 | - | - | 0.614 | 0.614 | 0.199 | 3.33x | 11.6/20.6/29.7% | 1.1/4.1% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.982 | 0.983 | 0.629 | 1.69x | 17.9/30.0/34.7% | 1.1/4.3% | 3 |
| adaptive | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.982 | 0.983 | 0.621 | 1.83x | 19.6/32.4/37.7% | 1.2/4.7% | 3 |

