# Sweep blocks-2026-08-27-3444599

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 3444599 · seeds 3444599
- **blocks** 87 run
- **compute** 11.0 h of simulator time across every cell
- **generated** 2026-08-27T14:04:36+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>109 warnings</summary>

- AD-amplifiers: amplifier-mix=sprinkled: decode_failures 24
- AD-amplifiers: slower: 4.05 s per simulated hour against 1.81 over 6 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-amplify-worst: amplify-worst=0.1: decode_failures 2
- AD-badrouters: role-placement=inverse: decode_failures 13
- AD-badrouters: role-placement=random: decode_failures 15
- AD-badrouters: slower: 4.71 s per simulated hour against 2.06 over 6 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 19
- DB-hotstore-stress: max-num-nodes=10: decode_failures 14
- DB-hotstore-stress: faster: 9.43 s per simulated hour against 28.9 over 6 prior run(s) - 3.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DB-platform: platform-mix=constrained: decode_failures 19
- DB-warm: warm-num-nodes=0: decode_failures 32
- DB-warm: warm-num-nodes=25: decode_failures 32
- DB-warm: warm-num-nodes=100: decode_failures 32
- DB-warm: warm-num-nodes=2000: decode_failures 32
- DG-burst: burst-loss=0.1: decode_failures 4
- DG-burst: burst-loss=0.2: decode_failures 27
- DG-burst: burst-loss=0.3: decode_failures 14
- DG-loss: extra-loss=0.3: decode_failures 32
- DG-loss: slower: 4.55 s per simulated hour against 2.13 over 6 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.1: decode_failures 25
- DG-outage: burst-loss=0.2: decode_failures 29
- DG-outage: burst-loss=0.3: decode_failures 23
- DM-mode: dm-mode=flood-only: decode_failures 10
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 22
- DM-mode: dm-mode=m4-early-flood: decode_failures 15
- DM-mode: slower: 6.07 s per simulated hour against 2.58 over 6 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.75: decode_failures 45
- FW-mixed: slower: 4.55 s per simulated hour against 1.86 over 6 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-versions: profile=2.5: decode_failures 1
- FW-versions: profile=2.6: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 19
- LD-chatty: broadcast-interval-s=900: decode_failures 2
- LD-chatty: broadcast-interval-s=300: decode_failures 19
- LD-interval: broadcast-interval-s=900: decode_failures 2
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 3
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 32
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 61
- MS-density: nodes=40: decode_failures 5
- MS-density: nodes=90: decode_failures 2
- MS-hopscale: nodes=500: decode_failures 104
- MS-oversubscribed: nodes=500: decode_failures 65
- MS-roles-fav: role-mix=legacy-default: decode_failures 1
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 6
- MS-router-late: router-late-fraction=0.1: decode_failures 2
- MS-size: nodes=90: decode_failures 3
- MS-stretch: stretch=1.25: decode_failures 4
- PR-crladder: coding-rate-ladder=False: decode_failures 22
- PR-crladder: coding-rate-ladder=True: decode_failures 21
- PR-crladder: slower: 8.89 s per simulated hour against 2.76 over 6 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 21
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 19
- PR-dmmode-cr: slower: 8.55 s per simulated hour against 2.27 over 6 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: faster: 1.25 s per simulated hour against 2.73 over 6 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-noise: noise-profile=temporal: decode_failures 27
- RF-noise: noise-profile=periodic: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 28
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 3
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 7
- RF-stretch-duct: faster: 1.05 s per simulated hour against 3.11 over 6 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RT-hoplimit: hop-limit=3: decode_failures 14
- RT-hopspread: hop-limit=3: decode_failures 14
- RT-spread: hop-spread=False: decode_failures 14
- SF-bucket-mode: bucket-mode=global: misdecodes 24
- SF-bucket-mode: bucket-mode=time: misdecodes 13
- SF-bucket-mode: bucket-mode=window: misdecodes 12
- SF-bucket-time: time-bucket-s=600: misdecodes 92
- SF-bucket-time: time-bucket-s=1800: misdecodes 13
- SF-bucket-time: time-bucket-s=3600: misdecodes 4
- SF-bucket-time: time-bucket-s=3600: decode_failures 4
- SF-cadence: trigger=interval: misdecodes 9
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 1
- SF-cadence: trigger=bucket+interval: misdecodes 4
- SF-cadence: slower: 6.11 s per simulated hour against 2.73 over 6 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 94
- SF-capacity-local: capacity=8: decode_failures 68
- SF-capacity-local: capacity=16: decode_failures 63
- SF-capacity: capacity=4: decode_failures 94
- SF-capacity: capacity=8: decode_failures 68
- SF-capacity: capacity=16: decode_failures 63
- SF-capacity-window: capacity=8: misdecodes 4
- SF-capacity-window: capacity=8: decode_failures 102
- SF-capacity-window: capacity=16: misdecodes 8
- SF-capacity-window: capacity=16: decode_failures 28
- SF-capacity-window: capacity=32: misdecodes 12
- SF-catchup: catch-up-hours=: misdecodes 4
- SF-catchup: catch-up-hours=02-06: decode_failures 30
- SF-catchup: catch-up-hours=00-08: decode_failures 26
- SF-hops-flat: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=5: decode_failures 34
- SF-jitter-global: advert-jitter-s=600: decode_failures 2
- SF-jitter-local: advert-jitter-s=600: decode_failures 2
- SF-place-flat: place=spread: decode_failures 15
- SF-place-spread: place=spread: decode_failures 15
- SF-place-spread: faster: 1.79 s per simulated hour against 3.84 over 6 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-provide-transport: provide-transport=broadcast: decode_failures 1
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 1
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 16
- SF-replay-order-broadcast: slower: 4.87 s per simulated hour against 1.73 over 6 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=heard: misdecodes 18
- SF-width: short-id-bits=16: decode_failures 1
- SF-window-size: window-size=8: misdecodes 105
- SF-window-size: window-size=16: misdecodes 41
- SF-window-size: window-size=32: misdecodes 12
- TH-congestion-input: faster: 4.75 s per simulated hour against 18.5 over 6 prior run(s) - 3.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- TH-congestion: no-congestion-scaling=True: decode_failures 109

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `PR-dmmode-cr` | 8.55 | 2.27 | 3.77x | 6 |
| `PR-crladder` | 8.89 | 2.76 | 3.22x | 6 |
| `SF-replay-order-broadcast` | 4.87 | 1.73 | 2.82x | 6 |
| `FW-mixed` | 4.55 | 1.86 | 2.44x | 6 |
| `DM-mode` | 6.07 | 2.58 | 2.35x | 6 |
| `AD-badrouters` | 4.71 | 2.06 | 2.28x | 6 |
| `SF-cadence` | 6.11 | 2.73 | 2.24x | 6 |
| `AD-amplifiers` | 4.05 | 1.81 | 2.23x | 6 |
| `DG-loss` | 4.55 | 2.13 | 2.13x | 6 |
| `DB-hotstore` | 4.38 | 2.33 | 1.88x | 6 |
| `SF-servers-spread` | 3.67 | 2.19 | 1.67x | 6 |
| `SF-capacity-window` | 2.59 | 1.55 | 1.67x | 6 |
| `MS-roles-fav` | 2.72 | 1.63 | 1.67x | 6 |
| `RT-hopspread` | 3.38 | 2.03 | 1.67x | 6 |
| `SF-advert-transport` | 3 | 1.85 | 1.62x | 6 |
| `DB-platform` | 4.66 | 2.89 | 1.61x | 6 |
| `SF-provide-transport` | 3.09 | 1.93 | 1.60x | 6 |
| `SF-jitter-global` | 2.8 | 1.78 | 1.57x | 6 |
| `SF-sr-retries` | 2.34 | 1.49 | 1.57x | 6 |
| `LD-interval` | 2.08 | 1.35 | 1.54x | 6 |
| `SF-capacity-local` | 2.94 | 1.93 | 1.52x | 6 |
| `RT-hoplimit` | 2.68 | 1.76 | 1.52x | 6 |
| `MS-hopscale` | 13.2 | 20.2 | 0.65x | 6 |
| `DB-warm` | 21.1 | 33.9 | 0.62x | 6 |
| `SF-servers-allrouters` | 1.22 | 2.1 | 0.58x | 6 |
| `MS-stretch` | 1.55 | 2.74 | 0.56x | 6 |
| `LD-traceroute-small` | 20.7 | 38 | 0.55x | 6 |
| `SF-place-flat` | 2.11 | 3.91 | 0.54x | 6 |
| `RF-txpower` | 0.987 | 1.97 | 0.50x | 6 |
| `SF-place-spread` | 1.79 | 3.84 | 0.47x | 6 |
| `RF-bw500` | 1.25 | 2.73 | 0.46x | 6 |
| `RF-stretch-duct` | 1.05 | 3.11 | 0.34x | 6 |
| `DB-hotstore-stress` | 9.43 | 28.9 | 0.33x | 6 |
| `TH-congestion-input` | 4.75 | 18.5 | 0.26x | 6 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.933 | 0.933 | 0.694 → 0.697 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.923 | 0.923 | 0.688 → 0.694 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.097 → 0.969 | 0.872 | 0.096 → 0.968 | 4x advert_bytes | up | 4 |
| `AD-siting` | siting-mix | **held** | 0.132 → 0.912 | 0.781 | 0.044 → 0.672 | 8x advert_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.107 → 0.869 | 0.763 | 0.090 → 0.645 | 1.6e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.233 → 0.923 | 0.690 | 0.068 → 0.690 | 7x sr_bytes | down | 4 |
| `MS-hopscale` | nodes | **held** | 0.237 → 0.923 | 0.686 | 0.186 → 0.690 | 7.1x bytes_on_air | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.239 → 0.923 | 0.684 | 0.059 → 0.690 | 8x sr_bytes | up | 5 |
| `MS-stretch` | stretch | **held** | 0.289 → 0.923 | 0.634 | 0.095 → 0.690 | 5x sr_airtime | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.246 → 0.858 | 0.612 | 0.189 → 0.610 | 3.9x bytes_on_air | down | 3 |
| `RF-eu-presets` | preset | **held** | 0.350 → 0.923 | 0.573 | 0.184 → 0.690 | 5.5x sr_bytes | up | 4 |
| `RF-preset` | preset | **held** | 0.350 → 0.923 | 0.573 | 0.184 → 0.690 | 7.9x sr_bytes | up | 3 |
| `RF-bw500` | preset | **text** | 0.116 → 0.665 | 0.549 | 0.116 → 0.652 | 8x sr_bytes | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.240 → 0.668 | 0.428 | 0.240 → 0.666 | 3.4x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.519 → 0.938 | 0.419 | 0.515 → 0.938 | 2.6x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.550 → 0.918 | 0.368 | 0.523 → 0.909 | 4.5x advert_bytes | up | 5 |
| `SF-place-flat` | place | **held** | 0.562 → 0.923 | 0.361 | 0.690 → 0.705 | 3.1x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.562 → 0.923 | 0.361 | 0.690 → 0.705 | 3.1x sr_bytes | up | 6 |
| `DG-outage` | burst-loss | **held** | 0.573 → 0.923 | 0.350 | 0.364 → 0.690 | 1.6x sr_airtime | down | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.598 → 0.943 | 0.346 | 0.421 → 0.734 | 9.6x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.522 → 0.852 | 0.330 | 0.503 → 0.832 | 7.9x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.426 → 0.727 | 0.301 | 0.388 → 0.690 | 1.6x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.571 → 0.863 | 0.292 | 0.534 → 0.853 | 2.2x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.571 → 0.820 | 0.248 | 0.534 → 0.797 | 1.7x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.619 → 0.833 | 0.213 | 0.568 → 0.806 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.619 → 0.833 | 0.213 | 0.568 → 0.806 | 2.4x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.789 → 0.990 | 0.201 | 0.690 → 0.900 | 1.6x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.727 → 0.926 | 0.199 | 0.690 → 0.925 | 2.5x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.528 → 0.727 | 0.199 | 0.520 → 0.690 | 6x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.731 → 0.918 | 0.187 | 0.710 → 0.909 | 3.4x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **held** | 0.751 → 0.923 | 0.172 | 0.537 → 0.690 | 1.6x sr_bytes | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.727 → 0.896 | 0.168 | 0.690 → 0.873 | 1.6x sr_bytes | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.568 → 0.727 | 0.159 | 0.534 → 0.690 | 1.4x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.775 → 0.933 | 0.158 | 0.690 → 0.704 | 3.5x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.571 → 0.727 | 0.156 | 0.534 → 0.690 | 1.2x sr_bytes | up | 2 |
| `DB-hotstore` | max-num-nodes | **text** | 0.640 → 0.778 | 0.138 | 0.610 → 0.735 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.642 → 0.778 | 0.137 | 0.608 → 0.735 | 2.2x sr_airtime | down | 3 |
| `FW-versions` | profile | **text** | 0.727 → 0.863 | 0.136 | 0.690 → 0.851 | 3x bytes_on_air | down | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.799 → 0.933 | 0.134 | 0.690 → 0.704 | 3.1x sr_bytes | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.789 → 0.923 | 0.134 | 0.690 → 0.698 | 35x sr_airtime | down | 3 |
| `SC-signing` | signature-policy | **text** | 0.601 → 0.727 | 0.126 | 0.601 → 0.690 | 1.3x sr_airtime | down | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.791 → 0.914 | 0.124 | 0.572 → 0.699 | 1.2x advert_bytes | down | 2 |
| `MS-roles` | role-mix | **held** | 0.808 → 0.928 | 0.120 | 0.568 → 0.696 | 1.3x bytes_on_air | down | 2 |
| `FW-firmware` | profile | **text** | 0.727 → 0.846 | 0.119 | 0.690 → 0.830 | 2.9x bytes_on_air | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.677 → 0.793 | 0.115 | 0.634 → 0.766 | 5.1x sr_airtime | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.837 → 0.940 | 0.103 | 0.690 → 0.704 | 9x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.837 → 0.940 | 0.103 | 0.690 → 0.704 | 9x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.832 → 0.935 | 0.103 | 0.690 → 0.700 | 3.7x sr_bytes | up | 3 |
| `DB-hotstore-stress` | max-num-nodes | **text** | 0.232 → 0.333 | 0.101 | 0.229 → 0.330 | 3.6x sr_airtime | up | 3 |
| `SF-cadence` | trigger | **held** | 0.852 → 0.932 | 0.080 | 0.668 → 0.699 | 14x advert_bytes | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.640 → 0.717 | 0.077 | 0.620 → 0.697 | 1.3x sr_bytes | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.723 → 0.791 | 0.067 | 0.690 → 0.779 | 2.1x bytes_on_air | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.727 → 0.789 | 0.062 | 0.689 → 0.690 | 4.2x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.727 → 0.781 | 0.054 | 0.690 → 0.751 | 3.2x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.727 → 0.780 | 0.052 | 0.690 → 0.769 | 2x bytes_on_air | up | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.881 → 0.932 | 0.051 | 0.679 → 0.714 | 8.9x advert_bytes | down | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.684 → 0.729 | 0.045 | 0.636 → 0.690 | 1.4x sr_airtime | down | 4 |
| `AD-badrouters` | role-placement | **held** | 0.808 → 0.848 | 0.040 | 0.557 → 0.571 | 1.4x sr_bytes | up | 3 |
| `SF-capacity` | capacity | **held** | 0.898 → 0.935 | 0.037 | 0.690 → 0.704 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.898 → 0.935 | 0.037 | 0.690 → 0.704 | 5.4x advert_bytes | up | 5 |
| `MS-router-late` | router-late-fraction | **text** | 0.727 → 0.762 | 0.035 | 0.690 → 0.725 | 1.3x bytes_on_air | up | 4 |
| `DM-mode` | dm-mode | **held** | 0.832 → 0.866 | 0.034 | 0.664 → 0.676 | 1.2x sr_bytes | up | 3 |
| `LD-diurnal` | diurnal | **held** | 0.923 → 0.952 | 0.029 | 0.690 → 0.715 | 1.3x sr_bytes | down | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.727 → 0.755 | 0.028 | 0.690 → 0.714 | 1.1x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.840 → 0.867 | 0.027 | 0.667 → 0.684 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.330 → 0.357 | 0.027 | 0.328 → 0.354 | 2.1x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.727 → 0.752 | 0.025 | 0.690 → 0.716 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.914 → 0.932 | 0.019 | 0.683 → 0.696 | 5.4x advert_bytes | down | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.923 → 0.940 | 0.017 | 0.690 → 0.695 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.910 → 0.924 | 0.014 | 0.678 → 0.689 | 1.1x sr_bytes | down | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.726 → 0.740 | 0.014 | 0.689 → 0.706 | 1.2x sr_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.727 → 0.741 | 0.013 | 0.690 → 0.701 | 2.2x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.706 → 0.717 | 0.012 | 0.695 → 0.711 | 1.1x sr_bytes | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.923 → 0.935 | 0.011 | 0.690 → 0.697 | 3.2x advert_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.758 → 0.769 | 0.010 | 0.720 → 0.729 | 1.1x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **text** | 0.727 → 0.737 | 0.010 | 0.690 → 0.699 | 3.1x advert_bytes | down | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.923 → 0.932 | 0.009 | 0.690 → 0.701 | 1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.923 → 0.932 | 0.009 | 0.690 → 0.701 | 1x sr_bytes | down | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.667 → 0.676 | 0.009 | 0.667 → 0.676 | 1.1x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.910 → 0.918 | 0.008 | 0.901 → 0.909 | 1.2x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.918 → 0.925 | 0.007 | 0.909 → 0.917 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.982 → 0.987 | 0.005 | 0.909 → 0.912 | 1x sr_bytes | down | 2 |
| `SF-resolve` | resolve | **text** | 0.727 → 0.731 | 0.004 | 0.690 → 0.692 | 5.7x advert_bytes | = | 3 |
| `SF-window-size` | window-size | **text** | 0.732 → 0.736 | 0.004 | 0.690 → 0.701 | 4.8x advert_bytes | down | 3 |
| `SF-servers-allrouters` | servers | **text** | 0.702 → 0.705 | 0.004 | 0.699 → 0.702 | 2.6x sr_bytes | up | 2 |

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
| none | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| sprinkled | 1 | 0.814 | 0.788 | 0.026 | - | - | 0.955 | 0.972 | 0.614 | 1.34x | 14.7/26.0/27.8% | 2.0/5.2% | 3 |
| arms-race | 1 | 0.926 | 0.925 | 0.002 | - | - | 0.975 | 0.976 | 0.692 | 1.09x | 18.0/22.9/26.9% | 1.4/5.2% | 3 |

> amplifier-mix=sprinkled: decode_failures 24

> slower: 4.05 s per simulated hour against 1.81 over 6 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.1 | 1 | 0.770 | 0.756 | 0.013 | - | - | 0.789 | 0.794 | 0.496 | 1.14x | 14.7/20.0/21.2% | 1.7/4.8% | 3 |
| 0.3 | 1 | 0.910 | 0.900 | 0.011 | - | - | 0.990 | 0.991 | 0.568 | 1.06x | 20.2/25.2/29.1% | 1.2/4.9% | 3 |

> amplify-worst=0.1: decode_failures 2

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.619 | 0.568 | 0.051 | - | - | 0.808 | 0.815 | 0.200 | 1.04x | 11.7/19.6/21.5% | 1.7/4.1% | 3 |
| inverse | 1 | 0.618 | 0.557 | 0.060 | - | - | 0.834 | 0.884 | 0.270 | 1.07x | 11.7/14.4/15.6% | 1.8/3.3% | 3 |
| random | 1 | 0.612 | 0.571 | 0.040 | - | - | 0.848 | 0.888 | 0.051 | 1.01x | 11.3/15.9/18.8% | 1.6/4.3% | 3 |

> role-placement=inverse: decode_failures 13

> role-placement=random: decode_failures 15

> slower: 4.71 s per simulated hour against 2.06 over 6 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.619 | 0.568 | 0.051 | - | - | 0.808 | 0.815 | 0.200 | 1.04x | 11.7/19.6/21.5% | 1.7/4.1% | 3 |
| all-routers | 1 | 0.833 | 0.806 | 0.027 | - | - | 0.964 | 0.966 | 0.331 | 2.47x | 24.4/37.7/40.8% | 4.1/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.619 | 0.568 | 0.051 | - | - | 0.808 | 0.815 | 0.200 | 1.04x | 11.7/19.6/21.5% | 1.7/4.1% | 3 |
| no-mute | 1 | 0.722 | 0.690 | 0.032 | - | - | 0.926 | 0.930 | 0.369 | 1.24x | 13.5/18.7/20.8% | 1.9/4.6% | 3 |
| all-routers | 1 | 0.833 | 0.806 | 0.027 | - | - | 0.964 | 0.966 | 0.331 | 2.47x | 24.4/37.7/40.8% | 4.1/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.619 | 0.568 | 0.051 | - | - | 0.808 | 0.815 | 0.200 | 1.04x | 11.7/19.6/21.5% | 1.7/4.1% | 3 |
| local-typical | 1 | 0.682 | 0.672 | 0.011 | - | - | 0.912 | 0.917 | 0.000 | 1.15x | 12.2/21.6/26.5% | 1.8/5.3% | 3 |
| basement-heavy | 1 | 0.046 | 0.044 | 0.002 | - | - | 0.132 | 0.137 | 0.000 | 0.39x | 0.7/4.8/5.9% | 0.3/1.8% | 3 |

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.717 | 0.711 | 0.006 | - | - | 0.904 | 0.904 | 0.000 | 2.32x | 14.1/26.8/34.7% | 1.9/5.5% | 3 |
| inverse | 1 | 0.706 | 0.695 | 0.011 | - | - | 0.907 | 0.908 | 0.000 | 2.27x | 13.3/23.7/29.3% | 1.8/3.4% | 3 |

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.694 | 0.694 | 0.000 | - | - | 0 | 0.000 | 0.367 | 1.25x | 12.9/25.1/26.4% | 2.0/4.3% | 3 |
| sr | 1 | 0.743 | 0.697 | 0.047 | - | - | 0.933 | 0.938 | 0.395 | 1.31x | 13.6/26.3/27.7% | 2.1/4.5% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.640 | 0.610 | 0.029 | - | - | 0.808 | 0.855 | 0.272 | 2.77x | 26.4/58.6/60.7% | 4.3/8.1% | 3 |
| 100 | 1 | 0.778 | 0.735 | 0.044 | - | - | 0.932 | 0.934 | 0.363 | 1.53x | 14.3/35.3/36.7% | 2.3/4.5% | 3 |
| 120 | 1 | 0.778 | 0.735 | 0.044 | - | - | 0.932 | 0.934 | 0.363 | 1.53x | 14.3/35.3/36.7% | 2.3/4.5% | 3 |
| 250 | 1 | 0.778 | 0.735 | 0.044 | - | - | 0.932 | 0.934 | 0.363 | 1.53x | 14.3/35.3/36.7% | 2.3/4.5% | 3 |

> max-num-nodes=10: decode_failures 19

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.232 | 0.229 | 0.002 | - | - | 0.262 | 0.271 | 0.025 | 10.35x | 28.9/40.8/48.7% | 3.8/9.5% | 3 |
| 120 | 1 | 0.330 | 0.328 | 0.003 | - | - | 0.351 | 0.351 | 0.034 | 4.43x | 12.2/17.7/23.9% | 1.6/4.2% | 3 |
| 250 | 1 | 0.333 | 0.330 | 0.003 | - | - | 0.354 | 0.355 | 0.028 | 4.42x | 12.2/17.7/24.4% | 1.6/4.3% | 3 |

> max-num-nodes=10: decode_failures 14

> faster: 9.43 s per simulated hour against 28.9 over 6 prior run(s) - 3.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.778 | 0.735 | 0.044 | - | - | 0.932 | 0.934 | 0.363 | 1.53x | 14.3/35.3/36.7% | 2.3/4.5% | 3 |
| baymesh-2026-08 | 1 | 0.778 | 0.735 | 0.044 | - | - | 0.932 | 0.934 | 0.363 | 1.53x | 14.3/35.3/36.7% | 2.3/4.5% | 3 |
| constrained | 1 | 0.642 | 0.608 | 0.034 | - | - | 0.815 | 0.862 | 0.262 | 2.77x | 26.4/58.6/60.6% | 4.3/8.1% | 3 |

> platform-mix=constrained: decode_failures 19

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.717 | 0.697 | 0.020 | - | - | 0.829 | 0.839 | 0.466 | 5.71x | 51.9/68.0/73.1% | 4.0/13.1% | 3 |
| 25 | 1 | 0.717 | 0.697 | 0.020 | - | - | 0.829 | 0.839 | 0.466 | 5.71x | 51.9/68.0/73.1% | 4.0/13.1% | 3 |
| 100 | 1 | 0.717 | 0.697 | 0.020 | - | - | 0.829 | 0.839 | 0.466 | 5.71x | 51.9/68.0/73.1% | 4.0/13.1% | 3 |
| 2000 | 1 | 0.717 | 0.697 | 0.020 | - | - | 0.829 | 0.839 | 0.466 | 5.71x | 51.9/68.0/73.1% | 4.0/13.1% | 3 |

> warm-num-nodes=0: decode_failures 32

> warm-num-nodes=25: decode_failures 32

> warm-num-nodes=100: decode_failures 32

> warm-num-nodes=2000: decode_failures 32

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.1 | 1 | 0.637 | 0.592 | 0.045 | - | - | 0.893 | 0.904 | 0.295 | 1.20x | 12.4/23.8/25.4% | 1.8/4.0% | 3 |
| 0.2 | 1 | 0.528 | 0.487 | 0.041 | - | - | 0.799 | 0.839 | 0.216 | 1.10x | 11.5/22.0/23.8% | 1.7/3.7% | 3 |
| 0.3 | 1 | 0.426 | 0.388 | 0.039 | - | - | 0.673 | 0.749 | 0.179 | 1.00x | 10.7/20.1/22.0% | 1.6/3.3% | 3 |

> burst-loss=0.1: decode_failures 4

> burst-loss=0.2: decode_failures 27

> burst-loss=0.3: decode_failures 14

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.1 | 1 | 0.700 | 0.665 | 0.035 | - | - | 0.922 | 0.927 | 0.310 | 1.33x | 13.8/26.2/27.8% | 2.1/4.5% | 3 |
| 0.2 | 1 | 0.637 | 0.604 | 0.032 | - | - | 0.871 | 0.877 | 0.255 | 1.31x | 13.8/25.6/27.5% | 2.1/4.3% | 3 |
| 0.3 | 1 | 0.568 | 0.534 | 0.034 | - | - | 0.806 | 0.842 | 0.181 | 1.32x | 14.3/25.2/27.5% | 2.0/4.2% | 3 |

> extra-loss=0.3: decode_failures 32

> slower: 4.55 s per simulated hour against 2.13 over 6 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.1 | 1 | 0.628 | 0.594 | 0.034 | - | - | 0.854 | 0.904 | 0.308 | 1.22x | 12.6/23.6/25.2% | 1.9/4.0% | 3 |
| 0.2 | 1 | 0.502 | 0.468 | 0.033 | - | - | 0.731 | 0.808 | 0.187 | 1.11x | 11.7/22.3/23.9% | 1.6/3.7% | 3 |
| 0.3 | 1 | 0.387 | 0.364 | 0.023 | - | - | 0.573 | 0.712 | 0.093 | 1.02x | 11.0/20.5/22.5% | 1.5/3.5% | 3 |

> burst-loss=0.1: decode_failures 25

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 23

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.664 | 0.664 | 0.000 | - | - | 0.847 | 0.915 | 0.363 | 1.67x | 17.1/33.1/35.0% | 2.6/5.7% | 3 |
| directed-with-late-flood | 1 | 0.676 | 0.676 | 0.000 | - | - | 0.832 | 0.929 | 0.360 | 1.54x | 15.9/31.3/33.0% | 2.4/5.4% | 3 |
| m4-early-flood | 1 | 0.668 | 0.668 | 0.000 | - | - | 0.866 | 0.931 | 0.357 | 1.57x | 16.1/31.6/33.3% | 2.5/5.5% | 3 |

> dm-mode=flood-only: decode_failures 10

> dm-mode=directed-with-late-flood: decode_failures 22

> dm-mode=m4-early-flood: decode_failures 15

> slower: 6.07 s per simulated hour against 2.58 over 6 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.846 | 0.830 | 0.016 | - | - | 0.978 | 0.978 | 0.460 | 0.79x | 8.1/11.4/12.2% | 1.3/2.1% | 3 |
| 2.8 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.25 | 1 | 0.757 | 0.734 | 0.023 | - | - | 0.931 | 0.940 | 0.485 | 1.17x | 11.8/19.7/21.5% | 1.9/4.0% | 3 |
| 0.5 | 1 | 0.732 | 0.724 | 0.009 | - | - | 0.908 | 0.911 | 0.117 | 1.08x | 10.6/18.3/20.2% | 1.6/4.1% | 3 |
| 0.75 | 1 | 0.780 | 0.769 | 0.011 | - | - | 0.934 | 0.970 | 0.231 | 0.90x | 9.5/12.9/14.4% | 1.5/3.0% | 3 |

> legacy-fraction=0.75: decode_failures 45

> slower: 4.55 s per simulated hour against 1.86 over 6 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.25 | 1 | 0.740 | 0.718 | 0.022 | - | - | 0.919 | 0.922 | 0.484 | 1.16x | 11.8/19.4/21.2% | 1.8/4.0% | 3 |
| 0.5 | 1 | 0.723 | 0.714 | 0.009 | - | - | 0.904 | 0.906 | 0.127 | 1.06x | 10.6/17.7/19.6% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.791 | 0.779 | 0.011 | - | - | 0.963 | 0.971 | 0.312 | 0.86x | 9.2/12.5/14.1% | 1.5/3.0% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.781 | 0.751 | 0.030 | - | - | 0.971 | 0.975 | 0.463 | 0.72x | 7.5/15.2/16.1% | 1.1/2.6% | 3 |
| signing=true | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.851 | 0.829 | 0.021 | - | - | 0.986 | 0.987 | 0.451 | 0.80x | 8.2/12.3/13.6% | 1.4/2.3% | 3 |
| 2.5 | 1 | 0.851 | 0.834 | 0.018 | - | - | 0.976 | 0.977 | 0.461 | 0.81x | 8.1/12.1/13.5% | 1.3/2.3% | 3 |
| 2.6 | 1 | 0.848 | 0.826 | 0.021 | - | - | 0.972 | 0.974 | 0.444 | 0.79x | 8.2/12.2/13.5% | 1.3/2.3% | 3 |
| 2.7 | 1 | 0.863 | 0.851 | 0.012 | - | - | 0.976 | 0.977 | 0.438 | 0.84x | 8.5/16.2/17.3% | 1.4/3.1% | 3 |
| 2.8 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

> profile=2.5: decode_failures 1

> profile=2.6: decode_failures 2

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.763 | 0.734 | 0.029 | - | - | 0.943 | 0.949 | 0.415 | 0.90x | 9.2/18.3/19.2% | 1.4/3.1% | 3 |
| 900 | 1 | 0.677 | 0.634 | 0.043 | - | - | 0.889 | 0.910 | 0.326 | 2.00x | 20.8/38.6/40.8% | 3.2/6.6% | 3 |
| 300 | 1 | 0.435 | 0.421 | 0.014 | - | - | 0.598 | 0.763 | 0.163 | 4.33x | 42.4/71.1/74.9% | 6.7/12.5% | 3 |

> broadcast-interval-s=900: decode_failures 2

> broadcast-interval-s=300: decode_failures 19

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.852 | 0.832 | 0.020 | - | - | 0.964 | 0.965 | 0.538 | 1.00x | 10.0/18.8/19.5% | 1.6/3.2% | 3 |
| 900 | 1 | 0.773 | 0.739 | 0.033 | - | - | 0.931 | 0.933 | 0.430 | 2.31x | 23.1/41.2/43.3% | 3.9/7.0% | 3 |
| 300 | 1 | 0.522 | 0.503 | 0.019 | - | - | 0.711 | 0.826 | 0.241 | 4.88x | 47.1/72.9/76.8% | 8.3/12.7% | 3 |

> broadcast-interval-s=300: decode_failures 19

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.754 | 0.715 | 0.038 | - | - | 0.952 | 0.957 | 0.399 | 1.23x | 12.5/24.7/26.0% | 1.9/4.3% | 3 |
| sinusoid | 1 | 0.747 | 0.715 | 0.032 | - | - | 0.939 | 0.942 | 0.418 | 1.18x | 12.0/23.6/24.9% | 1.8/4.1% | 3 |
| commuter | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.677 | 0.634 | 0.043 | - | - | 0.889 | 0.910 | 0.326 | 2.00x | 20.8/38.6/40.8% | 3.2/6.6% | 3 |
| 3600 | 1 | 0.763 | 0.734 | 0.029 | - | - | 0.943 | 0.949 | 0.415 | 0.90x | 9.2/18.3/19.2% | 1.4/3.1% | 3 |
| 10800 | 1 | 0.785 | 0.760 | 0.025 | - | - | 0.958 | 0.961 | 0.455 | 0.62x | 6.3/12.6/13.2% | 0.9/2.2% | 3 |
| 43200 | 1 | 0.793 | 0.766 | 0.027 | - | - | 0.966 | 0.966 | 0.466 | 0.40x | 4.0/8.2/8.6% | 0.6/1.4% | 3 |

> broadcast-interval-s=900: decode_failures 2

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.25 | 1 | 0.728 | 0.687 | 0.042 | - | - | 0.935 | 0.939 | 0.362 | 1.34x | 13.7/26.9/28.3% | 2.1/4.6% | 3 |
| 1.0 | 1 | 0.729 | 0.690 | 0.039 | - | - | 0.934 | 0.939 | 0.396 | 1.48x | 15.3/29.6/31.3% | 2.3/5.1% | 3 |
| 4.0 | 1 | 0.684 | 0.636 | 0.048 | - | - | 0.902 | 0.910 | 0.327 | 1.81x | 18.9/36.1/38.4% | 2.8/6.3% | 3 |

> traceroute-per-hour=4.0: decode_failures 3

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.717 | 0.697 | 0.020 | - | - | 0.829 | 0.839 | 0.466 | 5.71x | 51.9/68.0/73.1% | 4.0/13.1% | 3 |
| 1.0 | 1 | 0.640 | 0.620 | 0.020 | - | - | 0.758 | 0.780 | 0.406 | 6.45x | 58.1/71.8/76.5% | 4.6/14.2% | 3 |

> traceroute-per-hour=0.0: decode_failures 32

> traceroute-per-hour=1.0: decode_failures 61

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.550 | 0.523 | 0.027 | - | - | 0.792 | 0.817 | 0.350 | 1.10x | 13.5/20.9/22.6% | 2.5/5.2% | 3 |
| 60 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 90 | 1 | 0.861 | 0.851 | 0.010 | - | - | 0.951 | 0.951 | 0.455 | 1.49x | 16.0/21.9/24.8% | 1.5/4.7% | 3 |
| 120 | 1 | 0.918 | 0.909 | 0.009 | - | - | 0.987 | 0.988 | 0.660 | 1.98x | 19.3/28.5/32.2% | 1.3/5.1% | 3 |
| 150 | 1 | 0.914 | 0.907 | 0.006 | - | - | 0.985 | 0.986 | 0.391 | 2.58x | 22.2/35.6/41.0% | 1.4/5.4% | 3 |

> nodes=40: decode_failures 5

> nodes=90: decode_failures 2

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 120 | 1 | 0.619 | 0.608 | 0.010 | - | - | 0.852 | 0.855 | 0.000 | 2.32x | 13.8/25.3/32.7% | 1.7/5.2% | 3 |
| 250 | 1 | 0.328 | 0.325 | 0.003 | - | - | 0.348 | 0.349 | 0.028 | 4.81x | 13.3/19.4/26.8% | 1.7/4.7% | 3 |
| 500 | 1 | 0.187 | 0.186 | 0.001 | - | - | 0.237 | 0.257 | 0.030 | 9.03x | 12.6/18.0/23.9% | 1.6/4.6% | 3 |

> nodes=500: decode_failures 104

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.621 | 0.610 | 0.011 | - | - | 0.858 | 0.859 | 0.000 | 2.20x | 13.1/24.1/31.1% | 1.6/4.9% | 3 |
| 250 | 1 | 0.330 | 0.328 | 0.003 | - | - | 0.351 | 0.351 | 0.034 | 4.43x | 12.2/17.7/23.9% | 1.6/4.2% | 3 |
| 500 | 1 | 0.190 | 0.189 | 0.001 | - | - | 0.246 | 0.266 | 0.031 | 8.51x | 11.8/17.1/23.1% | 1.5/4.4% | 3 |

> nodes=500: decode_failures 65

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.736 | 0.696 | 0.040 | - | - | 0.928 | 0.934 | 0.352 | 1.31x | 13.5/25.8/27.1% | 2.1/4.4% | 3 |
| baymesh-2026-08 | 1 | 0.619 | 0.568 | 0.051 | - | - | 0.808 | 0.815 | 0.200 | 1.04x | 11.7/19.6/21.5% | 1.7/4.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.737 | 0.699 | 0.038 | - | - | 0.914 | 0.922 | 0.393 | 1.36x | 14.0/26.6/27.9% | 2.1/4.5% | 3 |
| baymesh-2026-08 | 1 | 0.625 | 0.572 | 0.053 | - | - | 0.791 | 0.808 | 0.201 | 1.17x | 12.6/23.9/26.5% | 1.9/4.0% | 3 |

> role-mix=legacy-default: decode_failures 1

> role-mix=baymesh-2026-08: decode_failures 6

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.05 | 1 | 0.762 | 0.725 | 0.038 | - | - | 0.932 | 0.940 | 0.386 | 1.42x | 14.0/31.6/33.2% | 2.2/4.2% | 3 |
| 0.1 | 1 | 0.762 | 0.719 | 0.043 | - | - | 0.938 | 0.939 | 0.359 | 1.51x | 14.2/34.5/37.3% | 2.3/4.3% | 3 |
| 0.2 | 1 | 0.762 | 0.722 | 0.040 | - | - | 0.918 | 0.919 | 0.285 | 1.66x | 15.8/35.7/40.1% | 2.3/4.5% | 3 |

> router-late-fraction=0.1: decode_failures 2

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| local-typical | 1 | 0.726 | 0.715 | 0.011 | - | - | 0.910 | 0.915 | 0.000 | 1.40x | 13.1/22.6/26.0% | 2.2/5.2% | 3 |
| event | 1 | 0.097 | 0.096 | 0.001 | - | - | 0.273 | 0.276 | 0.000 | 0.72x | 1.6/10.7/18.6% | 0.8/3.3% | 3 |
| backbone | 1 | 0.969 | 0.968 | 0.001 | - | - | 0.999 | 0.999 | 0.763 | 1.11x | 25.3/32.9/36.7% | 1.5/5.3% | 3 |

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.637 | 0.628 | 0.009 | - | - | 0.733 | 0.734 | 0.357 | 1.28x | 18.5/27.9/31.3% | 3.1/6.5% | 3 |
| 60 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 90 | 1 | 0.671 | 0.657 | 0.014 | - | - | 0.786 | 0.787 | 0.331 | 1.81x | 13.6/21.8/28.0% | 1.8/4.4% | 3 |
| 120 | 1 | 0.619 | 0.608 | 0.010 | - | - | 0.852 | 0.855 | 0.000 | 2.32x | 13.8/25.3/32.7% | 1.7/5.2% | 3 |
| 150 | 1 | 0.528 | 0.520 | 0.008 | - | - | 0.803 | 0.803 | 0.127 | 2.88x | 14.6/21.4/24.8% | 1.7/5.2% | 3 |

> nodes=90: decode_failures 3

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 1.25 | 1 | 0.458 | 0.450 | 0.008 | - | - | 0.632 | 0.677 | 0.000 | 1.39x | 10.4/20.7/25.7% | 2.2/4.3% | 3 |
| 1.5 | 1 | 0.240 | 0.240 | 0.001 | - | - | 0.367 | 0.368 | 0.000 | 1.29x | 7.4/19.0/23.3% | 1.8/4.2% | 3 |
| 2.0 | 1 | 0.096 | 0.095 | 0.001 | - | - | 0.289 | 0.290 | 0.000 | 0.72x | 2.2/9.2/16.1% | 1.0/3.3% | 3 |

> stretch=1.25: decode_failures 4

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| clustered | 1 | 0.816 | 0.814 | 0.002 | - | - | 0.912 | 0.912 | 0.000 | 1.25x | 22.5/31.5/35.3% | 1.7/5.5% | 3 |
| corridor | 1 | 0.519 | 0.515 | 0.004 | - | - | 0.677 | 0.678 | 0.000 | 1.39x | 13.2/23.5/26.1% | 2.2/4.7% | 3 |
| hub | 1 | 0.938 | 0.938 | 0.001 | - | - | 0.979 | 0.980 | 0.797 | 1.30x | 21.7/34.3/36.6% | 2.0/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.676 | 0.676 | 0.000 | - | - | 0.832 | 0.929 | 0.360 | 1.54x | 15.9/31.3/33.0% | 2.4/5.4% | 3 |
| True | 1 | 0.667 | 0.667 | 0.000 | - | - | 0.840 | 0.931 | 0.350 | 1.54x | 15.9/31.1/32.8% | 2.4/5.4% | 3 |

> coding-rate-ladder=False: decode_failures 22

> coding-rate-ladder=True: decode_failures 21

> slower: 8.89 s per simulated hour against 2.76 over 6 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.667 | 0.667 | 0.000 | - | - | 0.840 | 0.931 | 0.350 | 1.54x | 15.9/31.1/32.8% | 2.4/5.4% | 3 |
| m4-early-flood | 1 | 0.684 | 0.684 | 0.000 | - | - | 0.867 | 0.933 | 0.370 | 1.54x | 15.8/31.3/32.9% | 2.4/5.4% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 21

> dm-mode=m4-early-flood: decode_failures 19

> slower: 8.55 s per simulated hour against 2.27 over 6 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.694 | 0.694 | 0.000 | - | - | 0 | 0.000 | 0.367 | 1.25x | 12.9/25.1/26.4% | 2.0/4.3% | 3 |
| chain | 1 | 0.694 | 0.688 | 0.006 | - | - | 0.814 | 0.930 | 0.350 | 1.50x | 15.3/30.1/31.7% | 2.3/5.2% | 3 |
| sr | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| True | 1 | 0.752 | 0.716 | 0.037 | - | - | 0.948 | 0.952 | 0.401 | 1.32x | 13.4/26.2/27.6% | 2.1/4.5% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.918 | 0.909 | 0.009 | - | - | 0.987 | 0.988 | 0.660 | 1.98x | 19.3/28.5/32.2% | 1.3/5.1% | 3 |
| True | 1 | 0.920 | 0.912 | 0.007 | - | - | 0.982 | 0.982 | 0.677 | 2.01x | 19.3/28.4/31.9% | 1.3/5.1% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.116 | 0.116 | 0.000 | - | - | 0.318 | 0.318 | 0.000 | 0.04x | 0.1/0.5/0.9% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.262 | 0.261 | 0.001 | - | - | 0.408 | 0.409 | 0.000 | 0.20x | 1.1/3.2/3.8% | 0.3/0.7% | 3 |
| LONG_TURBO | 1 | 0.665 | 0.652 | 0.014 | - | - | 0.829 | 0.832 | 0.244 | 1.27x | 10.9/20.8/24.0% | 1.9/4.3% | 3 |

> faster: 1.25 s per simulated hour against 2.73 over 6 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 0.25 | 1 | 0.785 | 0.748 | 0.037 | - | - | 0.955 | 0.956 | 0.513 | 1.14x | 14.5/26.2/27.4% | 1.8/4.4% | 3 |
| 1.0 | 1 | 0.896 | 0.873 | 0.022 | - | - | 0.978 | 0.979 | 0.787 | 0.94x | 23.0/31.2/32.5% | 1.3/4.8% | 3 |

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.184 | 0.184 | 0.000 | - | - | 0.350 | 0.351 | 0.000 | 0.10x | 0.5/1.6/2.1% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| LITE_FAST | 1 | 0.688 | 0.677 | 0.011 | - | - | 0.848 | 0.851 | 0.265 | 0.99x | 8.9/18.7/20.2% | 1.5/3.3% | 3 |
| NARROW_SLOW | 1 | 0.689 | 0.670 | 0.019 | - | - | 0.869 | 0.872 | 0.366 | 1.27x | 12.0/25.1/26.5% | 1.9/4.3% | 3 |

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| temporal | 1 | 0.614 | 0.589 | 0.026 | - | - | 0.832 | 0.900 | 0.211 | 1.29x | 13.0/24.9/26.5% | 2.0/4.3% | 3 |
| transient | 1 | 0.720 | 0.683 | 0.037 | - | - | 0.920 | 0.921 | 0.377 | 1.29x | 13.0/25.7/27.1% | 2.0/4.4% | 3 |
| periodic | 1 | 0.565 | 0.537 | 0.028 | - | - | 0.751 | 0.776 | 0.238 | 1.19x | 12.2/23.5/25.0% | 1.8/4.0% | 3 |

> noise-profile=temporal: decode_failures 27

> noise-profile=periodic: decode_failures 3

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.184 | 0.184 | 0.000 | - | - | 0.350 | 0.351 | 0.000 | 0.10x | 0.5/1.6/2.1% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| LONG_MODERATE | 1 | 0.720 | 0.672 | 0.048 | - | - | 0.910 | 0.944 | 0.464 | 3.37x | 39.2/61.7/64.6% | 5.2/10.5% | 3 |

> preset=LONG_MODERATE: decode_failures 28

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.059 | 0.059 | 0.000 | - | - | 0.239 | 0.240 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.116 | 0.116 | 0.000 | - | - | 0.318 | 0.318 | 0.000 | 0.04x | 0.1/0.5/0.9% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| LONG_TURBO | 1 | 0.665 | 0.652 | 0.014 | - | - | 0.829 | 0.832 | 0.244 | 1.27x | 10.9/20.8/24.0% | 1.9/4.3% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.711 | 0.687 | 0.024 | - | - | 0.865 | 0.866 | 0.406 | 1.75x | 17.0/33.1/34.5% | 2.9/5.7% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.678 | 0.645 | 0.033 | - | - | 0.869 | 0.882 | 0.325 | 1.26x | 13.1/25.6/27.0% | 2.0/4.3% | 3 |
| 10000 | 1 | 0.565 | 0.537 | 0.028 | - | - | 0.751 | 0.776 | 0.238 | 1.19x | 12.2/23.5/25.0% | 1.8/4.0% | 3 |
| 4000 | 1 | 0.336 | 0.329 | 0.007 | - | - | 0.430 | 0.519 | 0.107 | 0.99x | 10.6/18.8/20.4% | 1.5/3.0% | 3 |
| 2000 | 1 | 0.090 | 0.090 | 0.000 | - | - | 0.107 | 0.164 | 0.022 | 0.69x | 7.5/13.3/15.2% | 1.1/1.8% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 1

> noise-pulse-interval-ms=10000: decode_failures 3

> noise-pulse-interval-ms=4000: decode_failures 7

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.240 | 0.240 | 0.001 | - | - | 0.367 | 0.368 | 0.000 | 1.29x | 7.4/19.0/23.3% | 1.8/4.2% | 3 |
| 1.0 | 1 | 0.668 | 0.666 | 0.002 | - | - | 0.728 | 0.728 | 0.567 | 0.97x | 15.9/25.0/26.5% | 1.4/4.2% | 3 |

> faster: 1.05 s per simulated hour against 3.11 over 6 prior run(s) - 3.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 22 | 1 | 0.256 | 0.255 | 0.001 | - | - | 0.375 | 0.376 | 0.000 | 1.29x | 7.4/19.3/23.4% | 1.9/4.3% | 3 |
| 17 | 1 | 0.118 | 0.118 | 0.001 | - | - | 0.294 | 0.296 | 0.000 | 0.82x | 2.9/10.6/17.5% | 1.1/3.4% | 3 |
| 14 | 1 | 0.068 | 0.068 | 0.001 | - | - | 0.233 | 0.234 | 0.000 | 0.53x | 1.6/4.7/9.0% | 0.6/2.4% | 3 |

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.918 | 0.909 | 0.009 | - | - | 0.987 | 0.988 | 0.660 | 1.98x | 19.3/28.5/32.2% | 1.3/5.1% | 3 |
| True | 1 | 0.910 | 0.901 | 0.009 | - | - | 0.982 | 0.982 | 0.655 | 2.37x | 22.5/32.3/35.8% | 1.5/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.758 | 0.720 | 0.038 | - | - | 0.928 | 0.935 | 0.386 | 1.43x | 13.9/31.5/32.5% | 2.2/4.2% | 3 |
| True | 1 | 0.769 | 0.729 | 0.039 | - | - | 0.935 | 0.939 | 0.426 | 1.47x | 14.3/31.7/32.8% | 2.3/4.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| random | 1 | 0.755 | 0.714 | 0.041 | - | - | 0.926 | 0.926 | 0.375 | 1.32x | 13.5/24.8/26.2% | 2.2/4.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.571 | 0.534 | 0.037 | - | - | 0.842 | 0.892 | 0.218 | 1.08x | 11.1/23.3/24.9% | 1.6/4.0% | 3 |
| 7 | 1 | 0.820 | 0.797 | 0.023 | - | - | 0.952 | 0.952 | 0.498 | 1.50x | 14.9/27.8/28.9% | 2.4/4.7% | 3 |
| 15 | 1 | 0.863 | 0.853 | 0.010 | - | - | 0.952 | 0.952 | 0.569 | 1.53x | 15.1/28.2/29.2% | 2.5/4.7% | 3 |
| 32 | 1 | 0.859 | 0.846 | 0.013 | - | - | 0.949 | 0.949 | 0.595 | 1.54x | 15.2/28.4/29.4% | 2.5/4.7% | 3 |

> hop-limit=3: decode_failures 14

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.571 | 0.534 | 0.037 | - | - | 0.842 | 0.892 | 0.218 | 1.08x | 11.1/23.3/24.9% | 1.6/4.0% | 3 |
| 5 | 1 | 0.748 | 0.714 | 0.035 | - | - | 0.935 | 0.940 | 0.418 | 1.29x | 13.4/25.2/26.5% | 2.1/4.3% | 3 |
| 7 | 1 | 0.820 | 0.797 | 0.023 | - | - | 0.952 | 0.952 | 0.498 | 1.50x | 14.9/27.8/28.9% | 2.4/4.7% | 3 |

> hop-limit=3: decode_failures 14

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| KNOWN_ONLY | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.698 | 0.698 | 0.000 | - | - | 0.789 | 0.936 | 0.381 | 1.27x | 13.0/25.3/26.6% | 2.0/4.3% | 3 |

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.571 | 0.534 | 0.037 | - | - | 0.842 | 0.892 | 0.218 | 1.08x | 11.1/23.3/24.9% | 1.6/4.0% | 3 |
| True | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

> hop-spread=False: decode_failures 14

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| BALANCED | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| STRICT | 1 | 0.601 | 0.601 | 0.000 | - | - | 0.830 | 0.835 | 0.267 | 1.45x | 14.8/28.7/30.2% | 2.3/4.9% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| dm | 1 | 0.741 | 0.701 | 0.040 | - | - | 0.935 | 0.939 | 0.375 | 1.26x | 13.0/25.4/26.9% | 2.0/4.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.733 | 0.697 | 0.035 | - | - | 0.931 | 0.938 | 0.385 | 1.31x | 13.5/26.3/27.7% | 2.0/4.5% | 3 |
| local | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| time | 1 | 0.730 | 0.695 | 0.035 | - | - | 0.932 | 0.949 | 0.388 | 1.34x | 13.7/26.7/28.1% | 2.1/4.6% | 3 |
| window | 1 | 0.732 | 0.690 | 0.042 | - | - | 0.935 | 0.939 | 0.380 | 1.29x | 13.3/25.9/27.2% | 2.0/4.4% | 3 |

> bucket-mode=global: misdecodes 24

> bucket-mode=time: misdecodes 13

> bucket-mode=window: misdecodes 12

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.717 | 0.683 | 0.033 | - | - | 0.914 | 0.926 | 0.355 | 1.46x | 14.9/28.9/30.3% | 2.3/5.0% | 3 |
| 1800 | 1 | 0.730 | 0.695 | 0.035 | - | - | 0.932 | 0.949 | 0.388 | 1.34x | 13.7/26.7/28.1% | 2.1/4.6% | 3 |
| 3600 | 1 | 0.728 | 0.696 | 0.032 | - | - | 0.914 | 0.940 | 0.393 | 1.30x | 13.2/26.1/27.4% | 2.0/4.4% | 3 |

> time-bucket-s=600: misdecodes 92

> time-bucket-s=1800: misdecodes 13

> time-bucket-s=3600: misdecodes 4

> time-bucket-s=3600: decode_failures 4

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| interval | 1 | 0.713 | 0.668 | 0.045 | - | - | 0.916 | 0.925 | 0.364 | 1.73x | 17.4/34.8/36.7% | 2.7/6.4% | 3 |
| aimd | 1 | 0.713 | 0.699 | 0.014 | - | - | 0.852 | 0.946 | 0.397 | 1.32x | 13.5/26.6/27.9% | 2.1/4.5% | 3 |
| bucket+interval | 1 | 0.721 | 0.679 | 0.042 | - | - | 0.932 | 0.933 | 0.369 | 1.77x | 17.9/35.4/37.1% | 2.8/6.3% | 3 |

> trigger=interval: misdecodes 9

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 1

> trigger=bucket+interval: misdecodes 4

> slower: 6.11 s per simulated hour against 2.73 over 6 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.729 | 0.694 | 0.035 | - | - | 0.919 | 0.939 | 0.391 | 1.29x | 13.2/26.0/27.4% | 2.0/4.5% | 3 |
| 8 | 1 | 0.721 | 0.694 | 0.027 | - | - | 0.898 | 0.933 | 0.380 | 1.32x | 13.5/26.6/28.0% | 2.1/4.7% | 3 |
| 16 | 1 | 0.731 | 0.696 | 0.035 | - | - | 0.927 | 0.935 | 0.391 | 1.30x | 13.3/26.2/27.6% | 2.0/4.5% | 3 |
| 32 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 50 | 1 | 0.741 | 0.704 | 0.037 | - | - | 0.935 | 0.938 | 0.389 | 1.29x | 13.2/26.0/27.4% | 2.0/4.4% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 68

> capacity=16: decode_failures 63

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.729 | 0.694 | 0.035 | - | - | 0.919 | 0.939 | 0.391 | 1.29x | 13.2/26.0/27.4% | 2.0/4.5% | 3 |
| 8 | 1 | 0.721 | 0.694 | 0.027 | - | - | 0.898 | 0.933 | 0.380 | 1.32x | 13.5/26.6/28.0% | 2.1/4.7% | 3 |
| 16 | 1 | 0.731 | 0.696 | 0.035 | - | - | 0.927 | 0.935 | 0.391 | 1.30x | 13.3/26.2/27.6% | 2.0/4.5% | 3 |
| 32 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 50 | 1 | 0.741 | 0.704 | 0.037 | - | - | 0.935 | 0.938 | 0.389 | 1.29x | 13.2/26.0/27.4% | 2.0/4.4% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 68

> capacity=16: decode_failures 63

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.706 | 0.699 | 0.007 | - | - | 0.832 | 0.945 | 0.390 | 1.29x | 13.3/25.8/27.2% | 2.0/4.4% | 3 |
| 16 | 1 | 0.731 | 0.700 | 0.030 | - | - | 0.923 | 0.950 | 0.396 | 1.29x | 13.2/25.6/26.9% | 2.0/4.4% | 3 |
| 32 | 1 | 0.732 | 0.690 | 0.042 | - | - | 0.935 | 0.939 | 0.380 | 1.29x | 13.3/25.9/27.2% | 2.0/4.4% | 3 |

> capacity=8: misdecodes 4

> capacity=8: decode_failures 102

> capacity=16: misdecodes 8

> capacity=16: decode_failures 28

> capacity=32: misdecodes 12

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.721 | 0.679 | 0.042 | - | - | 0.932 | 0.933 | 0.369 | 1.77x | 17.9/35.4/37.1% | 2.8/6.3% | 3 |
| 02-06 | 1 | 0.735 | 0.714 | 0.021 | - | - | 0.881 | 0.942 | 0.399 | 1.33x | 13.5/26.6/27.9% | 2.1/4.6% | 3 |
| 00-08 | 1 | 0.732 | 0.708 | 0.023 | - | - | 0.885 | 0.939 | 0.406 | 1.39x | 14.2/27.9/29.4% | 2.2/5.0% | 3 |

> catch-up-hours=: misdecodes 4

> catch-up-hours=02-06: decode_failures 30

> catch-up-hours=00-08: decode_failures 26

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.704 | 0.701 | 0.002 | - | - | 0.799 | 0.800 | 0.387 | 1.28x | 13.2/25.9/27.2% | 2.0/4.4% | 3 |
| 2 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 3 | 1 | 0.743 | 0.697 | 0.047 | - | - | 0.933 | 0.938 | 0.395 | 1.31x | 13.6/26.3/27.7% | 2.1/4.5% | 3 |
| 4 | 1 | 0.735 | 0.704 | 0.030 | - | - | 0.817 | 0.963 | 0.387 | 1.31x | 13.5/26.0/27.4% | 2.0/4.4% | 3 |

> hops-apart=4: decode_failures 28

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.704 | 0.701 | 0.002 | - | - | 0.799 | 0.800 | 0.387 | 1.28x | 13.2/25.9/27.2% | 2.0/4.4% | 3 |
| 2 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 3 | 1 | 0.743 | 0.697 | 0.047 | - | - | 0.933 | 0.938 | 0.395 | 1.31x | 13.6/26.3/27.7% | 2.1/4.5% | 3 |
| 4 | 1 | 0.735 | 0.704 | 0.030 | - | - | 0.817 | 0.963 | 0.387 | 1.31x | 13.5/26.0/27.4% | 2.0/4.4% | 3 |
| 5 | 1 | 0.737 | 0.697 | 0.041 | - | - | 0.775 | 0.958 | 0.378 | 1.32x | 13.7/26.3/27.7% | 2.0/4.5% | 3 |

> hops-apart=4: decode_failures 28

> hops-apart=5: decode_failures 34

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.735 | 0.701 | 0.034 | - | - | 0.931 | 0.936 | 0.388 | 1.31x | 13.3/26.2/27.6% | 2.1/4.5% | 3 |
| 30 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 120 | 1 | 0.735 | 0.697 | 0.038 | - | - | 0.932 | 0.934 | 0.392 | 1.31x | 13.4/26.2/27.6% | 2.0/4.5% | 3 |
| 600 | 1 | 0.735 | 0.699 | 0.035 | - | - | 0.927 | 0.935 | 0.408 | 1.30x | 13.3/26.2/27.6% | 2.0/4.5% | 3 |

> advert-jitter-s=600: decode_failures 2

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.735 | 0.701 | 0.034 | - | - | 0.931 | 0.936 | 0.388 | 1.31x | 13.3/26.2/27.6% | 2.1/4.5% | 3 |
| 30 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 120 | 1 | 0.735 | 0.697 | 0.038 | - | - | 0.932 | 0.934 | 0.392 | 1.31x | 13.4/26.2/27.6% | 2.0/4.5% | 3 |
| 600 | 1 | 0.735 | 0.699 | 0.035 | - | - | 0.927 | 0.935 | 0.408 | 1.30x | 13.3/26.2/27.6% | 2.0/4.5% | 3 |

> advert-jitter-s=600: decode_failures 2

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.720 | 0.696 | 0.023 | - | - | 0.562 | 0.867 | 0.382 | 1.30x | 13.4/25.7/27.1% | 2.0/4.3% | 3 |
| routers | 1 | 0.702 | 0.699 | 0.003 | - | - | 0.797 | 0.798 | 0.367 | 1.31x | 13.4/26.3/27.6% | 2.0/4.5% | 3 |
| alternate-routers | 1 | 0.702 | 0.699 | 0.002 | - | - | 0.796 | 0.796 | 0.376 | 1.27x | 13.2/25.8/27.1% | 2.0/4.4% | 3 |
| beside-router | 1 | 0.696 | 0.693 | 0.003 | - | - | 0.793 | 0.793 | 0.347 | 1.29x | 13.2/26.0/27.3% | 2.0/4.4% | 3 |
| random-clients | 1 | 0.737 | 0.705 | 0.032 | - | - | 0.877 | 0.914 | 0.389 | 1.28x | 13.3/25.8/27.3% | 2.0/4.4% | 3 |
| hops-apart | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

> place=spread: decode_failures 15

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.720 | 0.696 | 0.023 | - | - | 0.562 | 0.867 | 0.382 | 1.30x | 13.4/25.7/27.1% | 2.0/4.3% | 3 |
| routers | 1 | 0.702 | 0.699 | 0.003 | - | - | 0.797 | 0.798 | 0.367 | 1.31x | 13.4/26.3/27.6% | 2.0/4.5% | 3 |
| alternate-routers | 1 | 0.702 | 0.699 | 0.002 | - | - | 0.796 | 0.796 | 0.376 | 1.27x | 13.2/25.8/27.1% | 2.0/4.4% | 3 |
| beside-router | 1 | 0.696 | 0.693 | 0.003 | - | - | 0.793 | 0.793 | 0.347 | 1.29x | 13.2/26.0/27.3% | 2.0/4.4% | 3 |
| random-clients | 1 | 0.737 | 0.705 | 0.032 | - | - | 0.877 | 0.914 | 0.389 | 1.28x | 13.3/25.8/27.3% | 2.0/4.4% | 3 |
| hops-apart | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

> place=spread: decode_failures 15

> faster: 1.79 s per simulated hour against 3.84 over 6 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| broadcast | 1 | 0.789 | 0.689 | 0.101 | - | - | 0.924 | 0.936 | 0.509 | 1.47x | 15.1/28.6/30.0% | 2.3/4.9% | 3 |

> provide-transport=broadcast: decode_failures 1

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| heard | 1 | 0.737 | 0.695 | 0.042 | - | - | 0.940 | 0.945 | 0.390 | 1.31x | 13.4/26.3/27.7% | 2.0/4.5% | 3 |

> replay-ordering=heard: misdecodes 18

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.789 | 0.689 | 0.101 | - | - | 0.924 | 0.936 | 0.509 | 1.47x | 15.1/28.6/30.0% | 2.3/4.9% | 3 |
| heard | 1 | 0.781 | 0.678 | 0.103 | - | - | 0.910 | 0.931 | 0.513 | 1.44x | 14.8/28.2/29.7% | 2.3/4.8% | 3 |

> replay-ordering=tip: decode_failures 1

> replay-ordering=heard: decode_failures 16

> slower: 4.87 s per simulated hour against 1.73 over 6 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| enum | 1 | 0.731 | 0.692 | 0.039 | - | - | 0.923 | 0.932 | 0.388 | 1.30x | 13.4/26.3/27.6% | 2.0/4.6% | 3 |
| hybrid | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.702 | 0.699 | 0.003 | - | - | 0.797 | 0.798 | 0.367 | 1.31x | 13.4/26.3/27.6% | 2.0/4.5% | 3 |
| 6 | 1 | 0.705 | 0.702 | 0.003 | - | - | 0.800 | 0.802 | 0.360 | 1.32x | 13.5/27.0/28.3% | 2.0/4.6% | 6 |

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.708 | 0.704 | 0.004 | - | - | 0.837 | 0.837 | 0.397 | 1.28x | 13.1/25.4/26.8% | 2.0/4.4% | 2 |
| 3 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 5 | 1 | 0.740 | 0.694 | 0.047 | - | - | 0.938 | 0.941 | 0.386 | 1.33x | 13.7/26.7/28.1% | 2.1/4.6% | 5 |
| 8 | 1 | 0.734 | 0.696 | 0.038 | - | - | 0.940 | 0.944 | 0.380 | 1.35x | 14.0/27.0/28.4% | 2.1/4.6% | 8 |

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.708 | 0.704 | 0.004 | - | - | 0.837 | 0.837 | 0.397 | 1.28x | 13.1/25.4/26.8% | 2.0/4.4% | 2 |
| 3 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 5 | 1 | 0.740 | 0.694 | 0.047 | - | - | 0.938 | 0.941 | 0.386 | 1.33x | 13.7/26.7/28.1% | 2.1/4.6% | 5 |
| 8 | 1 | 0.734 | 0.696 | 0.038 | - | - | 0.940 | 0.944 | 0.380 | 1.35x | 14.0/27.0/28.4% | 2.1/4.6% | 8 |

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| True | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.737 | 0.703 | 0.034 | - | - | 0.925 | 0.936 | 0.368 | 1.23x | 12.6/24.6/25.9% | 1.9/4.2% | 3 |
| 1 | 1 | 0.726 | 0.689 | 0.037 | - | - | 0.930 | 0.933 | 0.390 | 1.22x | 12.5/24.5/25.8% | 1.8/4.2% | 3 |
| 2 | 1 | 0.732 | 0.694 | 0.038 | - | - | 0.933 | 0.938 | 0.382 | 1.23x | 12.5/24.7/26.0% | 1.9/4.2% | 3 |
| 4 | 1 | 0.740 | 0.706 | 0.035 | - | - | 0.928 | 0.930 | 0.384 | 1.22x | 12.6/24.3/25.6% | 1.9/4.1% | 3 |

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.737 | 0.699 | 0.038 | - | - | 0.929 | 0.933 | 0.384 | 1.30x | 13.3/26.0/27.4% | 2.0/4.4% | 3 |
| 24 | 1 | 0.734 | 0.691 | 0.043 | - | - | 0.930 | 0.934 | 0.380 | 1.30x | 13.3/25.7/27.1% | 2.0/4.4% | 3 |
| 32 | 1 | 0.727 | 0.690 | 0.037 | - | - | 0.923 | 0.925 | 0.376 | 1.30x | 13.4/25.9/27.3% | 2.0/4.4% | 3 |
| 64 | 1 | 0.733 | 0.698 | 0.036 | - | - | 0.929 | 0.931 | 0.380 | 1.30x | 13.2/26.0/27.3% | 2.0/4.4% | 3 |

> short-id-bits=16: decode_failures 1

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.736 | 0.701 | 0.035 | - | - | 0.932 | 0.939 | 0.393 | 1.36x | 13.8/27.2/28.6% | 2.1/4.7% | 3 |
| 16 | 1 | 0.735 | 0.699 | 0.036 | - | - | 0.935 | 0.939 | 0.380 | 1.32x | 13.5/26.5/27.8% | 2.1/4.6% | 3 |
| 32 | 1 | 0.732 | 0.690 | 0.042 | - | - | 0.935 | 0.939 | 0.380 | 1.29x | 13.3/25.9/27.2% | 2.0/4.4% | 3 |

> window-size=8: misdecodes 105

> window-size=16: misdecodes 41

> window-size=32: misdecodes 12

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.918 | 0.909 | 0.009 | - | - | 0.987 | 0.988 | 0.660 | 1.98x | 19.3/28.5/32.2% | 1.3/5.1% | 3 |
| True | 1 | 0.731 | 0.710 | 0.021 | - | - | 0.835 | 0.855 | 0.477 | 5.50x | 50.6/66.8/71.9% | 3.9/12.9% | 3 |

> no-congestion-scaling=True: decode_failures 109

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.330 | 0.328 | 0.003 | - | - | 0.351 | 0.351 | 0.034 | 4.43x | 12.2/17.7/23.9% | 1.6/4.2% | 3 |
| truesize | 1 | 0.357 | 0.354 | 0.003 | - | - | 0.375 | 0.376 | 0.032 | 2.44x | 6.7/11.5/13.3% | 0.8/2.8% | 3 |

> faster: 4.75 s per simulated hour against 18.5 over 6 prior run(s) - 3.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.925 | 0.917 | 0.007 | - | - | 0.987 | 0.988 | 0.666 | 1.90x | 18.3/27.1/30.2% | 1.2/4.8% | 3 |
| adaptive | 1 | 0.918 | 0.909 | 0.009 | - | - | 0.987 | 0.988 | 0.660 | 1.98x | 19.3/28.5/32.2% | 1.3/5.1% | 3 |

