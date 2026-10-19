# Sweep blocks-2026-10-19-4886225

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 4886225 · seeds 4886225
- **blocks** 87 run
- **compute** 11.2 h of simulator time across every cell
- **generated** 2026-10-19T09:09:15+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>128 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 1
- AD-badrouters: role-placement=degree: decode_failures 15
- AD-badrouters: role-placement=inverse: decode_failures 20
- AD-badrouters: role-placement=random: decode_failures 7
- AD-badrouters: slower: 5.94 s per simulated hour against 1.79 over 59 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 15
- AD-flooding: role-mix=all-routers: decode_failures 1
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 15
- AD-nomute: role-mix=all-routers: decode_failures 1
- AD-siting: siting-mix=uniform: decode_failures 15
- BL-control: protocol=sr: decode_failures 37
- BL-control: slower: 5.25 s per simulated hour against 1.81 over 59 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 17
- DB-hotstore-stress: max-num-nodes=10: decode_failures 26
- DB-platform: platform-mix=constrained: decode_failures 17
- DB-warm: warm-num-nodes=0: decode_failures 116
- DB-warm: warm-num-nodes=25: decode_failures 116
- DB-warm: warm-num-nodes=100: decode_failures 116
- DB-warm: warm-num-nodes=2000: decode_failures 116
- DG-burst: burst-loss=0.1: decode_failures 11
- DG-burst: burst-loss=0.2: decode_failures 13
- DG-burst: burst-loss=0.3: decode_failures 34
- DG-loss: extra-loss=0.1: decode_failures 3
- DG-loss: extra-loss=0.2: decode_failures 2
- DG-loss: extra-loss=0.3: decode_failures 17
- DG-outage: burst-loss=0.1: decode_failures 20
- DG-outage: burst-loss=0.2: decode_failures 34
- DG-outage: burst-loss=0.3: decode_failures 24
- DM-mode: dm-mode=flood-only: decode_failures 21
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 26
- DM-mode: dm-mode=m4-early-flood: decode_failures 22
- DM-mode: slower: 8.53 s per simulated hour against 2.71 over 59 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty-hops: broadcast-interval-s=900: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 12
- LD-chatty: broadcast-interval-s=900: decode_failures 1
- LD-chatty: broadcast-interval-s=300: decode_failures 15
- LD-interval: broadcast-interval-s=900: decode_failures 1
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 1
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 1
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 116
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 10.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 120
- MS-oversubscribed: faster: 6.86 s per simulated hour against 20.1 over 59 prior run(s) - 2.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 25
- MS-roles-fav: slower: 5.06 s per simulated hour against 1.7 over 59 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-roles: role-mix=baymesh-2026-08: decode_failures 15
- MS-roles: slower: 3.79 s per simulated hour against 1.68 over 59 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.1: decode_failures 21
- MS-router-late: router-late-fraction=0.2: decode_failures 18
- MS-router-late: slower: 4.71 s per simulated hour against 1.72 over 59 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=event: decode_failures 3
- MS-siting: siting-mix=backbone: misdecodes 1
- MS-stretch: stretch=1.25: decode_failures 4
- PR-crladder: coding-rate-ladder=False: decode_failures 26
- PR-crladder: coding-rate-ladder=True: decode_failures 23
- PR-crladder: slower: 9.25 s per simulated hour against 2.72 over 59 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 23
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 23
- PR-dmmode-cr: slower: 8.47 s per simulated hour against 2.54 over 59 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats: extra-repeats=True: decode_failures 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 14
- RF-eu-presets: preset=SHORT_FAST: decode_failures 10
- RF-noise: noise-profile=temporal: decode_failures 13
- RF-noise: noise-profile=transient: decode_failures 1
- RF-noise: noise-profile=periodic: decode_failures 3
- RF-preset: preset=SHORT_FAST: decode_failures 10
- RF-preset: preset=LONG_MODERATE: decode_failures 29
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 2
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 14
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 16
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 3
- RF-stretch-duct: faster: 0.624 s per simulated hour against 1.84 over 59 prior run(s) - 2.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=17: decode_failures 6
- RF-txpower: tx-power=14: decode_failures 1
- RT-favourites: favourite-routers=True: decode_failures 18
- RT-hoplimit: hop-limit=3: decode_failures 21
- RT-hopspread: hop-limit=3: decode_failures 21
- RT-spread: hop-spread=False: decode_failures 21
- RT-spread: slower: 4.79 s per simulated hour against 2.15 over 59 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 15
- SF-bucket-mode: bucket-mode=time: misdecodes 23
- SF-bucket-mode: bucket-mode=window: misdecodes 5
- SF-bucket-time: time-bucket-s=600: misdecodes 100
- SF-bucket-time: time-bucket-s=1800: misdecodes 23
- SF-bucket-time: time-bucket-s=3600: misdecodes 6
- SF-bucket-time: time-bucket-s=3600: decode_failures 1
- SF-cadence: trigger=interval: misdecodes 3
- SF-cadence: trigger=interval: decode_failures 4
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 2
- SF-cadence: trigger=bucket+interval: misdecodes 8
- SF-capacity-local: capacity=4: decode_failures 59
- SF-capacity-local: capacity=8: decode_failures 75
- SF-capacity-local: capacity=16: decode_failures 46
- SF-capacity: capacity=4: decode_failures 59
- SF-capacity: capacity=8: decode_failures 75
- SF-capacity: capacity=16: decode_failures 46
- SF-capacity-window: capacity=8: misdecodes 10
- SF-capacity-window: capacity=8: decode_failures 49
- SF-capacity-window: capacity=16: misdecodes 9
- SF-capacity-window: capacity=16: decode_failures 9
- SF-capacity-window: capacity=32: misdecodes 5
- SF-catchup: catch-up-hours=: misdecodes 8
- SF-catchup: catch-up-hours=02-06: misdecodes 2
- SF-catchup: catch-up-hours=02-06: decode_failures 40
- SF-catchup: catch-up-hours=00-08: decode_failures 43
- SF-hops-flat: hops-apart=3: decode_failures 37
- SF-hops-flat: hops-apart=4: decode_failures 23
- SF-hops-spread: hops-apart=3: decode_failures 37
- SF-hops-spread: hops-apart=4: decode_failures 23
- SF-hops-spread: hops-apart=5: decode_failures 29
- SF-jitter-global: advert-jitter-s=600: decode_failures 2
- SF-jitter-local: advert-jitter-s=600: decode_failures 2
- SF-place-flat: place=spread: decode_failures 31
- SF-place-flat: place=beside-router: decode_failures 16
- SF-place-spread: place=spread: decode_failures 31
- SF-place-spread: place=beside-router: decode_failures 16
- SF-provide-transport: provide-transport=broadcast: decode_failures 22
- SF-provide-transport: slower: 4.56 s per simulated hour against 1.75 over 59 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 22
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 22
- SF-replay-order-broadcast: slower: 6.39 s per simulated hour against 1.68 over 59 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-window-size: window-size=8: misdecodes 87
- SF-window-size: window-size=16: misdecodes 37
- SF-window-size: window-size=32: misdecodes 5
- TH-congestion: no-congestion-scaling=True: decode_failures 93

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-replay-order-broadcast` | 6.39 | 1.68 | 3.81x | 59 |
| `PR-crladder` | 9.25 | 2.72 | 3.40x | 59 |
| `PR-dmmode-cr` | 8.47 | 2.54 | 3.34x | 59 |
| `AD-badrouters` | 5.94 | 1.79 | 3.31x | 59 |
| `DM-mode` | 8.53 | 2.71 | 3.15x | 59 |
| `MS-roles-fav` | 5.06 | 1.7 | 2.97x | 59 |
| `BL-control` | 5.25 | 1.81 | 2.90x | 59 |
| `MS-router-late` | 4.71 | 1.72 | 2.73x | 59 |
| `SF-provide-transport` | 4.56 | 1.75 | 2.60x | 59 |
| `MS-roles` | 3.79 | 1.68 | 2.27x | 59 |
| `RT-spread` | 4.79 | 2.15 | 2.23x | 59 |
| `RF-preset-turbo` | 2.82 | 1.53 | 1.84x | 55 |
| `RT-hoplimit` | 3.03 | 1.74 | 1.75x | 59 |
| `RT-favourites` | 2.84 | 1.66 | 1.71x | 59 |
| `SF-cadence` | 5.84 | 3.48 | 1.68x | 59 |
| `SF-servers-flat` | 3.77 | 2.28 | 1.65x | 59 |
| `AD-siting` | 2.23 | 1.39 | 1.61x | 59 |
| `AD-nomute` | 3.66 | 2.28 | 1.61x | 59 |
| `SF-place-flat` | 4.2 | 2.79 | 1.50x | 59 |
| `AD-amplify-worst` | 1.21 | 1.83 | 0.66x | 59 |
| `FW-firmware` | 1.08 | 1.65 | 0.65x | 59 |
| `TH-congestion-input` | 6.6 | 11.1 | 0.60x | 59 |
| `PR-repeats-busy` | 2.06 | 3.75 | 0.55x | 59 |
| `MS-hopscale` | 9.16 | 17.6 | 0.52x | 59 |
| `MS-oversubscribed` | 6.86 | 20.1 | 0.34x | 59 |
| `RF-stretch-duct` | 0.624 | 1.84 | 0.34x | 59 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.939 | 0.939 | 0.738 → 0.754 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.902 | 0.902 | 0.741 → 0.742 | 1x bytes_on_air | up | 2 |
| `AD-siting` | siting-mix | **held** | 0.018 → 0.839 | 0.821 | 0.066 → 0.719 | 3.4e+02x sr_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.100 → 0.877 | 0.776 | 0.081 → 0.669 | 1.4e+02x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.190 → 0.965 | 0.775 | 0.190 → 0.965 | 3.5x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.173 → 0.939 | 0.766 | 0.053 → 0.754 | 5.8x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.233 → 0.939 | 0.706 | 0.077 → 0.754 | 4.1x advert_bytes | down | 4 |
| `MS-stretch` | stretch | **text** | 0.131 → 0.772 | 0.641 | 0.129 → 0.754 | 4.6x sr_airtime | down | 4 |
| `MS-density` | nodes | **held** | 0.400 → 0.998 | 0.598 | 0.362 → 0.936 | 9.9x advert_bytes | up | 5 |
| `RF-eu-presets` | preset | **held** | 0.349 → 0.945 | 0.596 | 0.218 → 0.754 | 3.5x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.349 → 0.939 | 0.590 | 0.218 → 0.754 | 4.5x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.405 → 0.939 | 0.533 | 0.314 → 0.754 | 7.8x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.399 → 0.893 | 0.494 | 0.316 → 0.711 | 4.4x bytes_on_air | down | 3 |
| `RF-bw500` | preset | **text** | 0.138 → 0.630 | 0.492 | 0.136 → 0.617 | 2.7x sr_airtime | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.538 → 0.964 | 0.425 | 0.477 → 0.862 | 11x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.554 → 0.960 | 0.407 | 0.435 → 0.786 | 11x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.544 → 0.890 | 0.346 | 0.530 → 0.888 | 2.1x sr_airtime | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.435 → 0.772 | 0.338 | 0.414 → 0.754 | 1.7x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.224 → 0.553 | 0.329 | 0.224 → 0.550 | 3.1x sr_airtime | up | 2 |
| `DG-burst` | burst-loss | **text** | 0.452 → 0.772 | 0.320 | 0.419 → 0.754 | 1.7x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.575 → 0.894 | 0.320 | 0.536 → 0.887 | 3.6x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.575 → 0.839 | 0.265 | 0.536 → 0.826 | 2.5x sr_bytes | up | 3 |
| `MS-size` | nodes | **held** | 0.692 → 0.939 | 0.246 | 0.590 → 0.754 | 6.8x sr_bytes | up | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.708 → 0.939 | 0.231 | 0.741 → 0.754 | 2.2x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.708 → 0.939 | 0.231 | 0.741 → 0.754 | 2.2x sr_bytes | down | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.334 → 0.546 | 0.212 | 0.322 → 0.517 | 4.7x sr_airtime | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.575 → 0.772 | 0.198 | 0.536 → 0.754 | 1.9x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.726 → 0.913 | 0.188 | 0.714 → 0.910 | 3.6x sr_airtime | down | 2 |
| `DG-loss` | extra-loss | **text** | 0.599 → 0.772 | 0.173 | 0.585 → 0.754 | 1.4x sr_bytes | down | 4 |
| `RF-noise` | noise-profile | **text** | 0.604 → 0.772 | 0.168 | 0.584 → 0.754 | 1.3x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.606 → 0.772 | 0.166 | 0.606 → 0.754 | 1.2x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.772 → 0.924 | 0.152 | 0.754 → 0.922 | 1.5x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **held** | 0.810 → 0.955 | 0.144 | 0.657 → 0.792 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.810 → 0.955 | 0.144 | 0.657 → 0.792 | 2.2x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **held** | 0.839 → 0.966 | 0.128 | 0.719 → 0.821 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **held** | 0.839 → 0.966 | 0.128 | 0.719 → 0.821 | 2.3x bytes_on_air | up | 3 |
| `MS-roles` | role-mix | **held** | 0.839 → 0.963 | 0.125 | 0.719 → 0.778 | 1.2x bytes_on_air | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.837 → 0.959 | 0.122 | 0.727 → 0.754 | 12x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.837 → 0.959 | 0.122 | 0.727 → 0.754 | 12x sr_bytes | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.719 → 0.836 | 0.117 | 0.696 → 0.823 | 5.2x sr_airtime | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.826 → 0.939 | 0.113 | 0.726 → 0.793 | 1.4x sr_bytes | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.826 → 0.939 | 0.113 | 0.754 → 0.757 | 26x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **text** | 0.631 → 0.741 | 0.110 | 0.606 → 0.719 | 1.5x sr_bytes | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.772 → 0.875 | 0.103 | 0.754 → 0.854 | 1.3x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.772 → 0.874 | 0.102 | 0.754 → 0.861 | 1.7x sr_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.844 → 0.939 | 0.094 | 0.730 → 0.754 | 3.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.844 → 0.939 | 0.094 | 0.730 → 0.754 | 3.6x sr_bytes | up | 6 |
| `SF-cadence` | trigger | **held** | 0.853 → 0.939 | 0.086 | 0.709 → 0.754 | 14x advert_bytes | down | 4 |
| `FW-versions` | profile | **text** | 0.772 → 0.854 | 0.082 | 0.754 → 0.841 | 3.2x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.772 → 0.841 | 0.069 | 0.754 → 0.827 | 3.1x bytes_on_air | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.647 → 0.714 | 0.067 | 0.636 → 0.703 | 1.3x sr_airtime | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.772 → 0.839 | 0.067 | 0.754 → 0.826 | 2.2x bytes_on_air | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.772 → 0.838 | 0.066 | 0.754 → 0.825 | 2.2x bytes_on_air | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.710 → 0.772 | 0.062 | 0.681 → 0.754 | 1.4x sr_airtime | down | 4 |
| `SF-provide-transport` | provide-transport | **held** | 0.884 → 0.939 | 0.054 | 0.732 → 0.754 | 3.3x sr_airtime | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.878 → 0.932 | 0.054 | 0.739 → 0.753 | 2x advert_bytes | up | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.882 → 0.931 | 0.049 | 0.709 → 0.739 | 9.1x advert_bytes | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.772 → 0.814 | 0.042 | 0.754 → 0.796 | 3.3x bytes_on_air | down | 2 |
| `RT-favourites` | favourite-routers | **held** | 0.928 → 0.964 | 0.036 | 0.766 → 0.771 | 1.2x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.533 → 0.569 | 0.036 | 0.511 → 0.544 | 1.4x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.850 → 0.885 | 0.035 | 0.734 → 0.743 | 3.1x sr_bytes | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.772 → 0.807 | 0.035 | 0.754 → 0.790 | 1.4x sr_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.904 → 0.939 | 0.034 | 0.731 → 0.754 | 5.5x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.904 → 0.939 | 0.034 | 0.731 → 0.754 | 5.5x advert_bytes | up | 5 |
| `DM-mode` | dm-mode | **held** | 0.809 → 0.838 | 0.029 | 0.702 → 0.725 | 1.2x sr_airtime | up | 3 |
| `AD-worst` | role-placement | **text** | 0.750 → 0.777 | 0.027 | 0.730 → 0.765 | 1.2x sr_bytes | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.925 → 0.952 | 0.027 | 0.739 → 0.754 | 1.1x sr_bytes | up | 4 |
| `LD-diurnal` | diurnal | **held** | 0.936 → 0.957 | 0.021 | 0.751 → 0.770 | 1.2x sr_bytes | down | 3 |
| `SF-window-size` | window-size | **held** | 0.932 → 0.946 | 0.014 | 0.739 → 0.743 | 5.6x advert_bytes | down | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.939 → 0.952 | 0.013 | 0.754 → 0.756 | 1.1x sr_bytes | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.932 → 0.946 | 0.013 | 0.740 → 0.754 | 3.1x advert_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.939 → 0.951 | 0.012 | 0.754 → 0.755 | 2.2x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.760 → 0.772 | 0.012 | 0.738 → 0.754 | 3.5x advert_bytes | down | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.760 → 0.772 | 0.012 | 0.736 → 0.751 | 5.6x advert_bytes | up | 3 |
| `SF-resolve` | resolve | **text** | 0.763 → 0.772 | 0.010 | 0.742 → 0.754 | 5.9x advert_bytes | = | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.939 → 0.948 | 0.009 | 0.742 → 0.754 | 1.1x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.763 → 0.772 | 0.009 | 0.739 → 0.754 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.763 → 0.772 | 0.009 | 0.739 → 0.754 | 1.1x sr_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.832 → 0.840 | 0.008 | 0.721 → 0.726 | 1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.913 → 0.919 | 0.006 | 0.910 → 0.917 | 1x bytes_on_air | up | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.720 → 0.726 | 0.006 | 0.720 → 0.726 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.913 → 0.919 | 0.006 | 0.910 → 0.915 | 1.1x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.909 → 0.913 | 0.004 | 0.904 → 0.910 | 1.2x bytes_on_air | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.935 → 0.939 | 0.003 | 0.750 → 0.754 | 1.2x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.788 → 0.791 | 0.003 | 0.722 → 0.732 | 1.1x sr_airtime | down | 2 |

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
| none | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| sprinkled | 1 | 0.900 | 0.896 | 0.004 | - | - | 0.967 | 0.968 | 0.740 | 1.16x | 15.5/22.7/25.6% | 1.8/5.2% | 3 |
| arms-race | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.954 | 0.954 | 0.823 | 1.15x | 17.7/25.2/29.0% | 1.4/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.1 | 1 | 0.798 | 0.767 | 0.031 | - | - | 0.911 | 0.915 | 0.513 | 1.21x | 14.5/19.7/23.3% | 1.6/4.7% | 3 |
| 0.3 | 1 | 0.874 | 0.861 | 0.013 | - | - | 0.993 | 0.994 | 0.570 | 1.13x | 15.6/21.9/24.5% | 1.6/4.2% | 3 |

> amplify-worst=0.1: decode_failures 1

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.741 | 0.719 | 0.022 | - | - | 0.839 | 0.902 | 0.447 | 1.10x | 12.2/17.7/22.7% | 2.1/4.6% | 3 |
| inverse | 1 | 0.631 | 0.606 | 0.025 | - | - | 0.794 | 0.847 | 0.283 | 1.04x | 10.6/14.5/19.4% | 1.8/3.7% | 3 |
| random | 1 | 0.647 | 0.609 | 0.038 | - | - | 0.882 | 0.913 | 0.040 | 1.09x | 11.3/16.3/20.9% | 1.9/4.1% | 3 |

> role-placement=degree: decode_failures 15

> role-placement=inverse: decode_failures 20

> role-placement=random: decode_failures 7

> slower: 5.94 s per simulated hour against 1.79 over 59 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.741 | 0.719 | 0.022 | - | - | 0.839 | 0.902 | 0.447 | 1.10x | 12.2/17.7/22.7% | 2.1/4.6% | 3 |
| all-routers | 1 | 0.842 | 0.821 | 0.021 | - | - | 0.966 | 0.969 | 0.642 | 2.50x | 24.8/31.6/36.7% | 4.0/4.9% | 3 |

> role-mix=baymesh-2026-08: decode_failures 15

> role-mix=all-routers: decode_failures 1

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.741 | 0.719 | 0.022 | - | - | 0.839 | 0.902 | 0.447 | 1.10x | 12.2/17.7/22.7% | 2.1/4.6% | 3 |
| no-mute | 1 | 0.782 | 0.758 | 0.024 | - | - | 0.960 | 0.963 | 0.517 | 1.25x | 12.9/18.5/23.4% | 1.9/4.7% | 3 |
| all-routers | 1 | 0.842 | 0.821 | 0.021 | - | - | 0.966 | 0.969 | 0.642 | 2.50x | 24.8/31.6/36.7% | 4.0/4.9% | 3 |

> role-mix=baymesh-2026-08: decode_failures 15

> role-mix=all-routers: decode_failures 1

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.741 | 0.719 | 0.022 | - | - | 0.839 | 0.902 | 0.447 | 1.10x | 12.2/17.7/22.7% | 2.1/4.6% | 3 |
| local-typical | 1 | 0.385 | 0.383 | 0.002 | - | - | 0.627 | 0.628 | 0.000 | 1.08x | 9.4/18.7/26.4% | 1.6/4.8% | 3 |
| basement-heavy | 1 | 0.066 | 0.066 | 0.000 | - | - | 0.018 | 0.051 | 0.000 | 0.58x | 2.6/7.0/10.2% | 0.7/2.7% | 3 |

> siting-mix=uniform: decode_failures 15

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.777 | 0.765 | 0.012 | - | - | 0.938 | 0.938 | 0.000 | 2.34x | 13.7/24.8/31.7% | 1.8/5.7% | 3 |
| inverse | 1 | 0.750 | 0.730 | 0.020 | - | - | 0.938 | 0.940 | 0.000 | 2.22x | 13.0/21.0/29.0% | 1.8/3.2% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.741 | 0.741 | 0.000 | - | - | 0 | 0.000 | 0.502 | 1.27x | 13.5/20.5/25.8% | 1.8/4.6% | 3 |
| sr | 1 | 0.782 | 0.742 | 0.040 | - | - | 0.902 | 0.964 | 0.515 | 1.31x | 14.0/21.0/26.5% | 1.9/4.6% | 3 |

> protocol=sr: decode_failures 37

> slower: 5.25 s per simulated hour against 1.81 over 59 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.674 | 0.657 | 0.017 | - | - | 0.810 | 0.905 | 0.481 | 2.82x | 30.7/43.9/54.8% | 4.3/8.9% | 3 |
| 100 | 1 | 0.814 | 0.792 | 0.022 | - | - | 0.955 | 0.958 | 0.567 | 1.50x | 16.1/25.1/31.6% | 2.2/4.9% | 3 |
| 120 | 1 | 0.814 | 0.792 | 0.022 | - | - | 0.955 | 0.958 | 0.567 | 1.50x | 16.1/25.1/31.6% | 2.2/4.9% | 3 |
| 250 | 1 | 0.814 | 0.792 | 0.022 | - | - | 0.955 | 0.958 | 0.567 | 1.50x | 16.1/25.1/31.6% | 2.2/4.9% | 3 |

> max-num-nodes=10: decode_failures 17

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.326 | 0.322 | 0.004 | - | - | 0.334 | 0.363 | 0.146 | 11.04x | 38.6/53.5/66.7% | 3.9/10.4% | 3 |
| 120 | 1 | 0.517 | 0.511 | 0.006 | - | - | 0.533 | 0.534 | 0.209 | 4.15x | 14.7/22.7/30.4% | 1.4/4.8% | 3 |
| 250 | 1 | 0.523 | 0.517 | 0.005 | - | - | 0.546 | 0.548 | 0.214 | 4.07x | 14.5/22.0/29.4% | 1.4/4.6% | 3 |

> max-num-nodes=10: decode_failures 26

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.814 | 0.792 | 0.022 | - | - | 0.955 | 0.958 | 0.567 | 1.50x | 16.1/25.1/31.6% | 2.2/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.814 | 0.792 | 0.022 | - | - | 0.955 | 0.958 | 0.567 | 1.50x | 16.1/25.1/31.6% | 2.2/4.9% | 3 |
| constrained | 1 | 0.674 | 0.657 | 0.017 | - | - | 0.810 | 0.905 | 0.481 | 2.82x | 30.7/43.9/54.8% | 4.3/8.9% | 3 |

> platform-mix=constrained: decode_failures 17

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.714 | 0.703 | 0.011 | - | - | 0.872 | 0.906 | 0.432 | 5.79x | 52.2/70.0/77.6% | 4.2/12.5% | 3 |
| 25 | 1 | 0.714 | 0.703 | 0.011 | - | - | 0.872 | 0.906 | 0.432 | 5.79x | 52.2/70.0/77.6% | 4.2/12.5% | 3 |
| 100 | 1 | 0.714 | 0.703 | 0.011 | - | - | 0.872 | 0.906 | 0.432 | 5.79x | 52.2/70.0/77.6% | 4.2/12.5% | 3 |
| 2000 | 1 | 0.714 | 0.703 | 0.011 | - | - | 0.872 | 0.906 | 0.432 | 5.79x | 52.2/70.0/77.6% | 4.2/12.5% | 3 |

> warm-num-nodes=0: decode_failures 116

> warm-num-nodes=25: decode_failures 116

> warm-num-nodes=100: decode_failures 116

> warm-num-nodes=2000: decode_failures 116

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.1 | 1 | 0.647 | 0.627 | 0.020 | - | - | 0.851 | 0.905 | 0.427 | 1.20x | 13.1/19.9/25.2% | 1.7/4.3% | 3 |
| 0.2 | 1 | 0.564 | 0.533 | 0.030 | - | - | 0.784 | 0.855 | 0.344 | 1.10x | 12.1/18.1/23.1% | 1.6/3.8% | 3 |
| 0.3 | 1 | 0.452 | 0.419 | 0.033 | - | - | 0.663 | 0.779 | 0.246 | 0.99x | 11.3/16.8/22.0% | 1.5/3.4% | 3 |

> burst-loss=0.1: decode_failures 11

> burst-loss=0.2: decode_failures 13

> burst-loss=0.3: decode_failures 34

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.1 | 1 | 0.724 | 0.700 | 0.024 | - | - | 0.932 | 0.937 | 0.454 | 1.32x | 14.3/21.4/27.0% | 1.9/4.6% | 3 |
| 0.2 | 1 | 0.670 | 0.643 | 0.026 | - | - | 0.892 | 0.913 | 0.403 | 1.34x | 14.6/21.5/27.0% | 2.0/4.4% | 3 |
| 0.3 | 1 | 0.599 | 0.585 | 0.014 | - | - | 0.770 | 0.883 | 0.351 | 1.32x | 14.6/21.2/26.8% | 2.0/4.1% | 3 |

> extra-loss=0.1: decode_failures 3

> extra-loss=0.2: decode_failures 2

> extra-loss=0.3: decode_failures 17

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.1 | 1 | 0.667 | 0.642 | 0.025 | - | - | 0.883 | 0.916 | 0.377 | 1.20x | 13.2/19.8/25.3% | 1.8/4.4% | 3 |
| 0.2 | 1 | 0.521 | 0.497 | 0.024 | - | - | 0.721 | 0.832 | 0.326 | 1.11x | 12.2/18.3/23.7% | 1.7/3.9% | 3 |
| 0.3 | 1 | 0.435 | 0.414 | 0.021 | - | - | 0.621 | 0.779 | 0.266 | 1.04x | 11.8/17.2/22.4% | 1.6/3.6% | 3 |

> burst-loss=0.1: decode_failures 20

> burst-loss=0.2: decode_failures 34

> burst-loss=0.3: decode_failures 24

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.702 | 0.702 | 0.000 | - | - | 0.809 | 0.921 | 0.476 | 1.61x | 17.3/26.2/32.8% | 2.3/5.7% | 3 |
| directed-with-late-flood | 1 | 0.720 | 0.720 | 0.000 | - | - | 0.838 | 0.945 | 0.462 | 1.47x | 15.8/24.2/30.5% | 2.1/5.4% | 3 |
| m4-early-flood | 1 | 0.725 | 0.725 | 0.000 | - | - | 0.833 | 0.939 | 0.488 | 1.49x | 16.0/24.2/30.8% | 2.1/5.4% | 3 |

> dm-mode=flood-only: decode_failures 21

> dm-mode=directed-with-late-flood: decode_failures 26

> dm-mode=m4-early-flood: decode_failures 22

> slower: 8.53 s per simulated hour against 2.71 over 59 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.841 | 0.827 | 0.014 | - | - | 0.955 | 0.955 | 0.452 | 0.75x | 7.7/10.4/11.6% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.25 | 1 | 0.774 | 0.767 | 0.007 | - | - | 0.940 | 0.941 | 0.330 | 1.20x | 12.4/19.0/22.1% | 1.9/4.4% | 3 |
| 0.5 | 1 | 0.839 | 0.826 | 0.014 | - | - | 0.974 | 0.976 | 0.551 | 1.01x | 11.6/15.3/17.0% | 1.5/3.7% | 3 |
| 0.75 | 1 | 0.798 | 0.790 | 0.008 | - | - | 0.956 | 0.956 | 0.544 | 0.83x | 9.1/12.8/14.3% | 1.3/2.9% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.25 | 1 | 0.785 | 0.777 | 0.007 | - | - | 0.946 | 0.947 | 0.336 | 1.19x | 12.3/18.5/22.0% | 1.8/4.4% | 3 |
| 0.5 | 1 | 0.838 | 0.825 | 0.013 | - | - | 0.966 | 0.970 | 0.602 | 1.00x | 11.4/15.3/17.0% | 1.6/3.8% | 3 |
| 0.75 | 1 | 0.800 | 0.794 | 0.006 | - | - | 0.964 | 0.965 | 0.584 | 0.83x | 9.2/13.3/14.9% | 1.2/2.9% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.814 | 0.796 | 0.018 | - | - | 0.960 | 0.962 | 0.556 | 0.70x | 7.6/12.1/15.4% | 1.0/2.8% | 3 |
| signing=true | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.847 | 0.832 | 0.015 | - | - | 0.963 | 0.963 | 0.451 | 0.74x | 7.9/11.0/12.4% | 1.2/2.6% | 3 |
| 2.5 | 1 | 0.841 | 0.827 | 0.014 | - | - | 0.954 | 0.954 | 0.460 | 0.76x | 8.0/11.2/12.5% | 1.3/2.6% | 3 |
| 2.6 | 1 | 0.841 | 0.826 | 0.015 | - | - | 0.963 | 0.966 | 0.456 | 0.73x | 7.9/11.2/12.7% | 1.2/2.6% | 3 |
| 2.7 | 1 | 0.854 | 0.841 | 0.013 | - | - | 0.962 | 0.964 | 0.465 | 0.75x | 8.1/13.2/14.7% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.802 | 0.786 | 0.016 | - | - | 0.960 | 0.965 | 0.536 | 0.87x | 9.3/14.4/18.3% | 1.2/3.2% | 3 |
| 900 | 1 | 0.719 | 0.696 | 0.023 | - | - | 0.905 | 0.925 | 0.434 | 2.00x | 21.5/32.0/40.1% | 2.8/7.1% | 3 |
| 300 | 1 | 0.442 | 0.435 | 0.007 | - | - | 0.554 | 0.759 | 0.299 | 4.37x | 45.0/62.3/72.9% | 6.4/14.3% | 3 |

> broadcast-interval-s=900: decode_failures 1

> broadcast-interval-s=300: decode_failures 15

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.874 | 0.862 | 0.012 | - | - | 0.964 | 0.964 | 0.629 | 1.02x | 10.6/15.6/19.2% | 1.5/3.3% | 3 |
| 900 | 1 | 0.781 | 0.761 | 0.021 | - | - | 0.907 | 0.916 | 0.561 | 2.31x | 24.1/34.9/43.4% | 3.3/7.6% | 3 |
| 300 | 1 | 0.481 | 0.477 | 0.004 | - | - | 0.538 | 0.736 | 0.373 | 4.95x | 49.2/64.9/74.9% | 7.5/15.0% | 3 |

> broadcast-interval-s=900: decode_failures 1

> broadcast-interval-s=300: decode_failures 12

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.788 | 0.770 | 0.017 | - | - | 0.957 | 0.958 | 0.522 | 1.17x | 12.4/19.2/24.3% | 1.7/4.2% | 3 |
| sinusoid | 1 | 0.771 | 0.751 | 0.020 | - | - | 0.936 | 0.940 | 0.494 | 1.17x | 12.4/19.0/24.0% | 1.7/4.2% | 3 |
| commuter | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.719 | 0.696 | 0.023 | - | - | 0.905 | 0.925 | 0.434 | 2.00x | 21.5/32.0/40.1% | 2.8/7.1% | 3 |
| 3600 | 1 | 0.802 | 0.786 | 0.016 | - | - | 0.960 | 0.965 | 0.536 | 0.87x | 9.3/14.4/18.3% | 1.2/3.2% | 3 |
| 10800 | 1 | 0.821 | 0.803 | 0.018 | - | - | 0.980 | 0.980 | 0.547 | 0.60x | 6.3/10.1/12.7% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.836 | 0.823 | 0.013 | - | - | 0.975 | 0.977 | 0.558 | 0.43x | 4.5/7.3/9.4% | 0.6/1.8% | 3 |

> broadcast-interval-s=900: decode_failures 1

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.25 | 1 | 0.753 | 0.734 | 0.020 | - | - | 0.930 | 0.948 | 0.486 | 1.33x | 14.2/21.9/27.4% | 1.9/4.8% | 3 |
| 1.0 | 1 | 0.754 | 0.728 | 0.025 | - | - | 0.940 | 0.944 | 0.479 | 1.44x | 15.4/23.8/30.0% | 2.1/5.3% | 3 |
| 4.0 | 1 | 0.710 | 0.681 | 0.029 | - | - | 0.912 | 0.918 | 0.402 | 1.80x | 19.2/29.2/37.4% | 2.6/6.8% | 3 |

> traceroute-per-hour=0.25: decode_failures 1

> traceroute-per-hour=4.0: decode_failures 1

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.714 | 0.703 | 0.011 | - | - | 0.872 | 0.906 | 0.432 | 5.79x | 52.2/70.0/77.6% | 4.2/12.5% | 3 |
| 1.0 | 1 | 0.647 | 0.636 | 0.011 | - | - | 0.805 | 0.851 | 0.380 | 6.48x | 57.2/73.6/80.0% | 4.7/14.0% | 3 |

> traceroute-per-hour=0.0: decode_failures 116

> traceroute-per-hour=1.0: queue drops 10.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 120

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.367 | 0.362 | 0.005 | - | - | 0.400 | 0.406 | 0.000 | 0.85x | 12.3/16.5/17.0% | 2.0/4.5% | 3 |
| 60 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 90 | 1 | 0.916 | 0.913 | 0.003 | - | - | 0.994 | 0.994 | 0.483 | 1.66x | 17.5/25.6/31.8% | 1.4/5.0% | 3 |
| 120 | 1 | 0.913 | 0.910 | 0.004 | - | - | 0.976 | 0.976 | 0.582 | 2.03x | 19.4/30.5/37.9% | 1.4/5.1% | 3 |
| 150 | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.998 | 0.998 | 0.743 | 2.53x | 23.1/34.8/39.4% | 1.3/5.5% | 3 |

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 120 | 1 | 0.729 | 0.717 | 0.012 | - | - | 0.878 | 0.880 | 0.177 | 2.22x | 14.7/25.4/31.8% | 1.6/5.3% | 3 |
| 250 | 1 | 0.521 | 0.516 | 0.006 | - | - | 0.547 | 0.548 | 0.220 | 4.53x | 16.1/25.0/32.7% | 1.6/5.1% | 3 |
| 500 | 1 | 0.317 | 0.314 | 0.002 | - | - | 0.405 | 0.406 | 0.072 | 9.87x | 19.2/30.2/40.0% | 1.6/6.1% | 3 |

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.725 | 0.711 | 0.014 | - | - | 0.893 | 0.893 | 0.176 | 2.10x | 13.9/24.1/30.0% | 1.5/5.0% | 3 |
| 250 | 1 | 0.517 | 0.511 | 0.006 | - | - | 0.533 | 0.534 | 0.209 | 4.15x | 14.7/22.7/30.4% | 1.4/4.8% | 3 |
| 500 | 1 | 0.318 | 0.316 | 0.002 | - | - | 0.399 | 0.399 | 0.078 | 9.15x | 17.8/27.7/36.7% | 1.5/5.5% | 3 |

> faster: 6.86 s per simulated hour against 20.1 over 59 prior run(s) - 2.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.800 | 0.778 | 0.022 | - | - | 0.963 | 0.967 | 0.528 | 1.32x | 14.0/21.6/27.1% | 1.9/4.7% | 3 |
| baymesh-2026-08 | 1 | 0.741 | 0.719 | 0.022 | - | - | 0.839 | 0.902 | 0.447 | 1.10x | 12.2/17.7/22.7% | 2.1/4.6% | 3 |

> role-mix=baymesh-2026-08: decode_failures 15

> slower: 3.79 s per simulated hour against 1.68 over 59 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.815 | 0.793 | 0.022 | - | - | 0.939 | 0.943 | 0.527 | 1.36x | 14.6/21.9/27.4% | 1.9/4.7% | 3 |
| baymesh-2026-08 | 1 | 0.744 | 0.726 | 0.018 | - | - | 0.826 | 0.890 | 0.469 | 1.21x | 13.7/19.3/25.0% | 2.1/4.6% | 3 |

> role-mix=baymesh-2026-08: decode_failures 25

> slower: 5.06 s per simulated hour against 1.7 over 59 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.05 | 1 | 0.777 | 0.755 | 0.022 | - | - | 0.944 | 0.949 | 0.542 | 1.41x | 15.2/24.0/31.1% | 2.0/4.8% | 3 |
| 0.1 | 1 | 0.787 | 0.769 | 0.018 | - | - | 0.923 | 0.962 | 0.547 | 1.51x | 16.6/25.4/32.7% | 2.1/4.8% | 3 |
| 0.2 | 1 | 0.807 | 0.790 | 0.017 | - | - | 0.924 | 0.961 | 0.533 | 1.62x | 18.1/26.9/34.7% | 2.5/4.7% | 3 |

> router-late-fraction=0.1: decode_failures 21

> router-late-fraction=0.2: decode_failures 18

> slower: 4.71 s per simulated hour against 1.72 over 59 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| local-typical | 1 | 0.476 | 0.474 | 0.002 | - | - | 0.731 | 0.731 | 0.000 | 1.29x | 10.3/19.7/26.7% | 1.8/5.2% | 3 |
| event | 1 | 0.190 | 0.190 | 0.001 | - | - | 0.351 | 0.437 | 0.000 | 0.90x | 4.0/14.3/18.6% | 1.0/4.4% | 3 |
| backbone | 1 | 0.965 | 0.965 | 0.001 | - | - | 0.996 | 0.997 | 0.862 | 1.18x | 21.0/29.2/31.4% | 1.6/5.4% | 3 |

> siting-mix=event: decode_failures 3

> siting-mix=backbone: misdecodes 1

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.638 | 0.633 | 0.006 | - | - | 0.692 | 0.697 | 0.319 | 1.21x | 18.1/24.2/27.0% | 2.7/6.3% | 3 |
| 60 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 90 | 1 | 0.685 | 0.669 | 0.016 | - | - | 0.870 | 0.870 | 0.273 | 1.51x | 12.4/19.1/21.5% | 1.5/4.1% | 3 |
| 120 | 1 | 0.729 | 0.717 | 0.012 | - | - | 0.878 | 0.880 | 0.177 | 2.22x | 14.7/25.4/31.8% | 1.6/5.3% | 3 |
| 150 | 1 | 0.605 | 0.590 | 0.014 | - | - | 0.825 | 0.828 | 0.118 | 2.69x | 14.4/23.5/28.7% | 1.5/4.8% | 3 |

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 1.25 | 1 | 0.471 | 0.462 | 0.009 | - | - | 0.689 | 0.745 | 0.234 | 1.38x | 11.3/20.6/24.0% | 2.3/4.4% | 3 |
| 1.5 | 1 | 0.224 | 0.224 | 0.000 | - | - | 0.358 | 0.360 | 0.045 | 1.29x | 7.7/17.6/24.2% | 1.9/4.2% | 3 |
| 2.0 | 1 | 0.131 | 0.129 | 0.002 | - | - | 0.330 | 0.334 | 0.000 | 0.79x | 2.8/11.2/15.2% | 0.9/3.4% | 3 |

> stretch=1.25: decode_failures 4

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| clustered | 1 | 0.890 | 0.887 | 0.003 | - | - | 0.997 | 0.997 | 0.000 | 1.16x | 26.3/35.5/37.1% | 1.7/5.5% | 3 |
| corridor | 1 | 0.544 | 0.530 | 0.014 | - | - | 0.662 | 0.664 | 0.188 | 1.33x | 15.5/23.3/24.8% | 2.1/5.0% | 3 |
| hub | 1 | 0.888 | 0.888 | 0.000 | - | - | 0.946 | 0.948 | 0.000 | 1.25x | 26.6/34.5/37.3% | 1.8/5.7% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.720 | 0.720 | 0.000 | - | - | 0.838 | 0.945 | 0.462 | 1.47x | 15.8/24.2/30.5% | 2.1/5.4% | 3 |
| True | 1 | 0.726 | 0.726 | 0.000 | - | - | 0.840 | 0.942 | 0.476 | 1.48x | 15.8/24.2/30.6% | 2.1/5.3% | 3 |

> coding-rate-ladder=False: decode_failures 26

> coding-rate-ladder=True: decode_failures 23

> slower: 9.25 s per simulated hour against 2.72 over 59 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.726 | 0.726 | 0.000 | - | - | 0.840 | 0.942 | 0.476 | 1.48x | 15.8/24.2/30.6% | 2.1/5.3% | 3 |
| m4-early-flood | 1 | 0.721 | 0.721 | 0.000 | - | - | 0.832 | 0.936 | 0.463 | 1.48x | 15.9/24.2/30.6% | 2.1/5.4% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 23

> dm-mode=m4-early-flood: decode_failures 23

> slower: 8.47 s per simulated hour against 2.54 over 59 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.741 | 0.741 | 0.000 | - | - | 0 | 0.000 | 0.502 | 1.27x | 13.5/20.5/25.8% | 1.8/4.6% | 3 |
| chain | 1 | 0.745 | 0.738 | 0.006 | - | - | 0.834 | 0.940 | 0.497 | 1.46x | 15.7/24.0/30.4% | 2.1/5.2% | 3 |
| sr | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| True | 1 | 0.777 | 0.756 | 0.022 | - | - | 0.952 | 0.956 | 0.507 | 1.31x | 13.8/21.5/26.8% | 1.9/4.7% | 3 |

> extra-repeats=True: decode_failures 1

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.913 | 0.910 | 0.004 | - | - | 0.976 | 0.976 | 0.582 | 2.03x | 19.4/30.5/37.9% | 1.4/5.1% | 3 |
| True | 1 | 0.919 | 0.917 | 0.003 | - | - | 0.979 | 0.979 | 0.594 | 2.08x | 19.7/30.8/38.3% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.138 | 0.136 | 0.002 | - | - | 0.321 | 0.359 | 0.000 | 0.04x | 0.2/0.6/0.8% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.273 | 0.271 | 0.002 | - | - | 0.453 | 0.453 | 0.000 | 0.21x | 1.3/3.0/5.0% | 0.3/0.8% | 3 |
| LONG_TURBO | 1 | 0.630 | 0.617 | 0.013 | - | - | 0.749 | 0.751 | 0.270 | 1.23x | 11.3/18.0/21.2% | 1.8/3.9% | 3 |

> preset=SHORT_TURBO: decode_failures 14

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 0.25 | 1 | 0.807 | 0.787 | 0.020 | - | - | 0.963 | 0.966 | 0.574 | 1.26x | 14.4/22.5/27.4% | 1.8/4.8% | 3 |
| 1.0 | 1 | 0.875 | 0.854 | 0.021 | - | - | 0.973 | 0.976 | 0.738 | 1.17x | 17.2/26.0/29.0% | 1.6/5.1% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.222 | 0.218 | 0.004 | - | - | 0.349 | 0.451 | 0.000 | 0.11x | 0.6/1.8/2.9% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| LITE_FAST | 1 | 0.658 | 0.645 | 0.013 | - | - | 0.830 | 0.835 | 0.289 | 0.95x | 9.4/15.0/17.1% | 1.4/3.3% | 3 |
| NARROW_SLOW | 1 | 0.746 | 0.727 | 0.018 | - | - | 0.945 | 0.953 | 0.409 | 1.21x | 12.0/17.9/22.8% | 1.8/4.5% | 3 |

> preset=SHORT_FAST: decode_failures 10

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| temporal | 1 | 0.633 | 0.609 | 0.025 | - | - | 0.852 | 0.924 | 0.310 | 1.27x | 13.4/20.2/25.7% | 1.8/4.3% | 3 |
| transient | 1 | 0.751 | 0.729 | 0.023 | - | - | 0.930 | 0.939 | 0.500 | 1.29x | 13.7/21.1/26.4% | 1.8/4.6% | 3 |
| periodic | 1 | 0.604 | 0.584 | 0.021 | - | - | 0.778 | 0.795 | 0.360 | 1.18x | 12.9/19.2/24.3% | 1.7/4.1% | 3 |

> noise-profile=temporal: decode_failures 13

> noise-profile=transient: decode_failures 1

> noise-profile=periodic: decode_failures 3

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.222 | 0.218 | 0.004 | - | - | 0.349 | 0.451 | 0.000 | 0.11x | 0.6/1.8/2.9% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| LONG_MODERATE | 1 | 0.759 | 0.737 | 0.022 | - | - | 0.871 | 0.940 | 0.455 | 3.18x | 36.4/50.7/57.5% | 4.7/11.6% | 3 |

> preset=SHORT_FAST: decode_failures 10

> preset=LONG_MODERATE: decode_failures 29

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.053 | 0.053 | 0.000 | - | - | 0.173 | 0.215 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.138 | 0.136 | 0.002 | - | - | 0.321 | 0.359 | 0.000 | 0.04x | 0.2/0.6/0.8% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| LONG_TURBO | 1 | 0.630 | 0.617 | 0.013 | - | - | 0.749 | 0.751 | 0.270 | 1.23x | 11.3/18.0/21.2% | 1.8/3.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.758 | 0.742 | 0.016 | - | - | 0.899 | 0.938 | 0.501 | 1.76x | 17.9/25.8/33.5% | 2.6/6.4% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 2

> preset=SHORT_TURBO: decode_failures 14

> preset=EXTRA_LONG_TURBO: decode_failures 16

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.690 | 0.669 | 0.021 | - | - | 0.877 | 0.890 | 0.455 | 1.26x | 13.6/20.9/26.2% | 1.8/4.5% | 3 |
| 10000 | 1 | 0.604 | 0.584 | 0.021 | - | - | 0.778 | 0.795 | 0.360 | 1.18x | 12.9/19.2/24.3% | 1.7/4.1% | 3 |
| 4000 | 1 | 0.340 | 0.333 | 0.007 | - | - | 0.436 | 0.543 | 0.189 | 1.00x | 10.9/15.7/20.4% | 1.5/3.1% | 3 |
| 2000 | 1 | 0.081 | 0.081 | 0.000 | - | - | 0.100 | 0.180 | 0.031 | 0.73x | 8.2/12.1/16.0% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 1

> noise-pulse-interval-ms=10000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.224 | 0.224 | 0.000 | - | - | 0.358 | 0.360 | 0.045 | 1.29x | 7.7/17.6/24.2% | 1.9/4.2% | 3 |
| 1.0 | 1 | 0.553 | 0.550 | 0.002 | - | - | 0.630 | 0.631 | 0.413 | 1.03x | 11.9/20.5/23.3% | 1.5/3.9% | 3 |

> faster: 0.624 s per simulated hour against 1.84 over 59 prior run(s) - 2.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 22 | 1 | 0.273 | 0.269 | 0.004 | - | - | 0.453 | 0.453 | 0.000 | 1.41x | 8.7/19.3/27.9% | 2.1/4.7% | 3 |
| 17 | 1 | 0.131 | 0.130 | 0.001 | - | - | 0.295 | 0.330 | 0.000 | 0.85x | 4.1/11.3/16.0% | 1.2/3.6% | 3 |
| 14 | 1 | 0.078 | 0.077 | 0.001 | - | - | 0.233 | 0.241 | 0.000 | 0.58x | 2.5/7.1/11.3% | 0.9/2.5% | 3 |

> tx-power=17: decode_failures 6

> tx-power=14: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.913 | 0.910 | 0.004 | - | - | 0.976 | 0.976 | 0.582 | 2.03x | 19.4/30.5/37.9% | 1.4/5.1% | 3 |
| True | 1 | 0.909 | 0.904 | 0.005 | - | - | 0.978 | 0.978 | 0.559 | 2.44x | 23.1/35.4/42.9% | 1.6/5.9% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.787 | 0.766 | 0.022 | - | - | 0.964 | 0.970 | 0.535 | 1.38x | 14.4/23.5/30.5% | 2.0/4.9% | 3 |
| True | 1 | 0.788 | 0.771 | 0.016 | - | - | 0.928 | 0.957 | 0.558 | 1.39x | 14.8/23.5/30.5% | 2.0/4.9% | 3 |

> favourite-routers=True: decode_failures 18

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| random | 1 | 0.770 | 0.750 | 0.020 | - | - | 0.935 | 0.941 | 0.499 | 1.34x | 14.2/21.8/27.3% | 1.9/4.7% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.575 | 0.536 | 0.039 | - | - | 0.797 | 0.857 | 0.293 | 1.04x | 11.6/18.2/23.6% | 1.5/4.5% | 3 |
| 7 | 1 | 0.839 | 0.826 | 0.014 | - | - | 0.936 | 0.938 | 0.633 | 1.51x | 15.9/23.3/28.7% | 2.2/4.9% | 3 |
| 15 | 1 | 0.894 | 0.887 | 0.008 | - | - | 0.957 | 0.958 | 0.675 | 1.55x | 16.3/23.6/29.2% | 2.2/5.0% | 3 |
| 32 | 1 | 0.888 | 0.881 | 0.006 | - | - | 0.943 | 0.944 | 0.652 | 1.53x | 16.2/23.2/28.7% | 2.2/4.9% | 3 |

> hop-limit=3: decode_failures 21

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.575 | 0.536 | 0.039 | - | - | 0.797 | 0.857 | 0.293 | 1.04x | 11.6/18.2/23.6% | 1.5/4.5% | 3 |
| 5 | 1 | 0.759 | 0.736 | 0.024 | - | - | 0.933 | 0.935 | 0.497 | 1.36x | 14.3/21.5/26.9% | 2.0/4.7% | 3 |
| 7 | 1 | 0.839 | 0.826 | 0.014 | - | - | 0.936 | 0.938 | 0.633 | 1.51x | 15.9/23.3/28.7% | 2.2/4.9% | 3 |

> hop-limit=3: decode_failures 21

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| KNOWN_ONLY | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.757 | 0.757 | 0.000 | - | - | 0.826 | 0.956 | 0.519 | 1.25x | 13.3/20.2/25.5% | 1.9/4.5% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.575 | 0.536 | 0.039 | - | - | 0.797 | 0.857 | 0.293 | 1.04x | 11.6/18.2/23.6% | 1.5/4.5% | 3 |
| True | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

> hop-spread=False: decode_failures 21

> slower: 4.79 s per simulated hour against 2.15 over 59 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| BALANCED | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| STRICT | 1 | 0.606 | 0.606 | 0.000 | - | - | 0.799 | 0.818 | 0.360 | 1.41x | 15.2/23.0/28.9% | 2.1/4.9% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| dm | 1 | 0.775 | 0.755 | 0.019 | - | - | 0.951 | 0.955 | 0.512 | 1.27x | 13.5/20.9/26.3% | 1.8/4.8% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.765 | 0.739 | 0.026 | - | - | 0.940 | 0.953 | 0.496 | 1.29x | 13.7/21.2/26.5% | 1.9/4.6% | 3 |
| local | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| time | 1 | 0.760 | 0.738 | 0.023 | - | - | 0.935 | 0.945 | 0.500 | 1.32x | 14.1/21.6/27.1% | 1.9/4.8% | 3 |
| window | 1 | 0.762 | 0.739 | 0.024 | - | - | 0.932 | 0.941 | 0.472 | 1.31x | 13.9/21.3/26.8% | 1.9/4.7% | 3 |

> bucket-mode=global: misdecodes 15

> bucket-mode=time: misdecodes 23

> bucket-mode=window: misdecodes 5

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.762 | 0.736 | 0.026 | - | - | 0.933 | 0.948 | 0.487 | 1.42x | 15.2/23.3/29.3% | 2.0/5.2% | 3 |
| 1800 | 1 | 0.760 | 0.738 | 0.023 | - | - | 0.935 | 0.945 | 0.500 | 1.32x | 14.1/21.6/27.1% | 1.9/4.8% | 3 |
| 3600 | 1 | 0.772 | 0.751 | 0.021 | - | - | 0.937 | 0.953 | 0.521 | 1.28x | 13.6/20.7/26.1% | 1.8/4.5% | 3 |

> time-bucket-s=600: misdecodes 100

> time-bucket-s=1800: misdecodes 23

> time-bucket-s=3600: misdecodes 6

> time-bucket-s=3600: decode_failures 1

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| interval | 1 | 0.740 | 0.720 | 0.020 | - | - | 0.891 | 0.933 | 0.457 | 1.67x | 17.9/27.7/35.6% | 2.4/6.7% | 3 |
| aimd | 1 | 0.752 | 0.745 | 0.006 | - | - | 0.853 | 0.952 | 0.494 | 1.29x | 13.8/21.0/26.6% | 1.8/4.6% | 3 |
| bucket+interval | 1 | 0.736 | 0.709 | 0.027 | - | - | 0.931 | 0.934 | 0.453 | 1.71x | 18.2/28.5/36.7% | 2.4/7.2% | 3 |

> trigger=interval: misdecodes 3

> trigger=interval: decode_failures 4

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 2

> trigger=bucket+interval: misdecodes 8

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.760 | 0.743 | 0.017 | - | - | 0.904 | 0.942 | 0.503 | 1.30x | 13.9/21.6/27.1% | 1.9/4.9% | 3 |
| 8 | 1 | 0.761 | 0.742 | 0.019 | - | - | 0.919 | 0.945 | 0.503 | 1.31x | 14.0/21.6/27.3% | 1.9/4.9% | 3 |
| 16 | 1 | 0.760 | 0.744 | 0.016 | - | - | 0.909 | 0.948 | 0.493 | 1.30x | 13.9/21.4/27.0% | 1.9/4.9% | 3 |
| 32 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 50 | 1 | 0.752 | 0.731 | 0.022 | - | - | 0.937 | 0.939 | 0.495 | 1.29x | 13.8/21.2/26.6% | 1.8/4.7% | 3 |

> capacity=4: decode_failures 59

> capacity=8: decode_failures 75

> capacity=16: decode_failures 46

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.760 | 0.743 | 0.017 | - | - | 0.904 | 0.942 | 0.503 | 1.30x | 13.9/21.6/27.1% | 1.9/4.9% | 3 |
| 8 | 1 | 0.761 | 0.742 | 0.019 | - | - | 0.919 | 0.945 | 0.503 | 1.31x | 14.0/21.6/27.3% | 1.9/4.9% | 3 |
| 16 | 1 | 0.760 | 0.744 | 0.016 | - | - | 0.909 | 0.948 | 0.493 | 1.30x | 13.9/21.4/27.0% | 1.9/4.9% | 3 |
| 32 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 50 | 1 | 0.752 | 0.731 | 0.022 | - | - | 0.937 | 0.939 | 0.495 | 1.29x | 13.8/21.2/26.6% | 1.8/4.7% | 3 |

> capacity=4: decode_failures 59

> capacity=8: decode_failures 75

> capacity=16: decode_failures 46

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.754 | 0.743 | 0.011 | - | - | 0.878 | 0.946 | 0.492 | 1.29x | 13.8/20.8/26.4% | 1.9/4.6% | 3 |
| 16 | 1 | 0.772 | 0.753 | 0.019 | - | - | 0.925 | 0.948 | 0.479 | 1.28x | 13.6/20.9/26.2% | 1.9/4.5% | 3 |
| 32 | 1 | 0.762 | 0.739 | 0.024 | - | - | 0.932 | 0.941 | 0.472 | 1.31x | 13.9/21.3/26.8% | 1.9/4.7% | 3 |

> capacity=8: misdecodes 10

> capacity=8: decode_failures 49

> capacity=16: misdecodes 9

> capacity=16: decode_failures 9

> capacity=32: misdecodes 5

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.736 | 0.709 | 0.027 | - | - | 0.931 | 0.934 | 0.453 | 1.71x | 18.2/28.5/36.7% | 2.4/7.2% | 3 |
| 02-06 | 1 | 0.750 | 0.738 | 0.013 | - | - | 0.882 | 0.949 | 0.465 | 1.32x | 14.1/21.9/27.6% | 1.9/5.1% | 3 |
| 00-08 | 1 | 0.755 | 0.739 | 0.016 | - | - | 0.892 | 0.951 | 0.481 | 1.38x | 14.6/23.1/29.4% | 2.0/5.7% | 3 |

> catch-up-hours=: misdecodes 8

> catch-up-hours=02-06: misdecodes 2

> catch-up-hours=02-06: decode_failures 40

> catch-up-hours=00-08: decode_failures 43

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.833 | 0.835 | 0.508 | 1.29x | 13.8/20.8/26.4% | 1.8/4.6% | 3 |
| 2 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 3 | 1 | 0.782 | 0.742 | 0.040 | - | - | 0.902 | 0.964 | 0.515 | 1.31x | 14.0/21.0/26.5% | 1.9/4.6% | 3 |
| 4 | 1 | 0.758 | 0.741 | 0.017 | - | - | 0.708 | 0.933 | 0.486 | 1.28x | 13.7/20.7/26.1% | 1.8/4.5% | 3 |

> hops-apart=3: decode_failures 37

> hops-apart=4: decode_failures 23

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.833 | 0.835 | 0.508 | 1.29x | 13.8/20.8/26.4% | 1.8/4.6% | 3 |
| 2 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 3 | 1 | 0.782 | 0.742 | 0.040 | - | - | 0.902 | 0.964 | 0.515 | 1.31x | 14.0/21.0/26.5% | 1.9/4.6% | 3 |
| 4 | 1 | 0.758 | 0.741 | 0.017 | - | - | 0.708 | 0.933 | 0.486 | 1.28x | 13.7/20.7/26.1% | 1.8/4.5% | 3 |
| 5 | 1 | 0.771 | 0.743 | 0.028 | - | - | 0.772 | 0.953 | 0.497 | 1.28x | 13.7/20.5/25.9% | 1.9/4.5% | 3 |

> hops-apart=3: decode_failures 37

> hops-apart=4: decode_failures 23

> hops-apart=5: decode_failures 29

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.768 | 0.745 | 0.023 | - | - | 0.940 | 0.948 | 0.477 | 1.28x | 13.6/21.0/26.3% | 1.8/4.5% | 3 |
| 30 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 120 | 1 | 0.763 | 0.740 | 0.023 | - | - | 0.940 | 0.944 | 0.519 | 1.29x | 13.6/21.0/26.3% | 1.9/4.6% | 3 |
| 600 | 1 | 0.764 | 0.739 | 0.025 | - | - | 0.947 | 0.955 | 0.478 | 1.30x | 13.8/21.2/26.5% | 1.9/4.6% | 3 |

> advert-jitter-s=600: decode_failures 2

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.768 | 0.745 | 0.023 | - | - | 0.940 | 0.948 | 0.477 | 1.28x | 13.6/21.0/26.3% | 1.8/4.5% | 3 |
| 30 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 120 | 1 | 0.763 | 0.740 | 0.023 | - | - | 0.940 | 0.944 | 0.519 | 1.29x | 13.6/21.0/26.3% | 1.9/4.6% | 3 |
| 600 | 1 | 0.764 | 0.739 | 0.025 | - | - | 0.947 | 0.955 | 0.478 | 1.30x | 13.8/21.2/26.5% | 1.9/4.6% | 3 |

> advert-jitter-s=600: decode_failures 2

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.813 | 0.740 | 0.073 | - | - | 0.872 | 0.955 | 0.556 | 1.32x | 14.1/21.3/26.7% | 1.9/4.6% | 3 |
| routers | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.850 | 0.850 | 0.493 | 1.28x | 13.8/20.7/26.3% | 1.8/4.5% | 3 |
| alternate-routers | 1 | 0.738 | 0.730 | 0.007 | - | - | 0.844 | 0.844 | 0.492 | 1.30x | 14.0/21.0/26.5% | 1.9/4.6% | 3 |
| beside-router | 1 | 0.761 | 0.735 | 0.026 | - | - | 0.923 | 0.942 | 0.492 | 1.29x | 13.8/21.2/26.8% | 1.8/4.8% | 3 |
| random-clients | 1 | 0.766 | 0.746 | 0.020 | - | - | 0.884 | 0.886 | 0.493 | 1.30x | 14.1/20.8/26.4% | 1.9/4.8% | 3 |
| hops-apart | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

> place=spread: decode_failures 31

> place=beside-router: decode_failures 16

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.813 | 0.740 | 0.073 | - | - | 0.872 | 0.955 | 0.556 | 1.32x | 14.1/21.3/26.7% | 1.9/4.6% | 3 |
| routers | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.850 | 0.850 | 0.493 | 1.28x | 13.8/20.7/26.3% | 1.8/4.5% | 3 |
| alternate-routers | 1 | 0.738 | 0.730 | 0.007 | - | - | 0.844 | 0.844 | 0.492 | 1.30x | 14.0/21.0/26.5% | 1.9/4.6% | 3 |
| beside-router | 1 | 0.761 | 0.735 | 0.026 | - | - | 0.923 | 0.942 | 0.492 | 1.29x | 13.8/21.2/26.8% | 1.8/4.8% | 3 |
| random-clients | 1 | 0.766 | 0.746 | 0.020 | - | - | 0.884 | 0.886 | 0.493 | 1.30x | 14.1/20.8/26.4% | 1.9/4.8% | 3 |
| hops-apart | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

> place=spread: decode_failures 31

> place=beside-router: decode_failures 16

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| broadcast | 1 | 0.791 | 0.732 | 0.059 | - | - | 0.884 | 0.942 | 0.568 | 1.37x | 14.6/22.3/28.1% | 2.0/4.9% | 3 |

> provide-transport=broadcast: decode_failures 22

> slower: 4.56 s per simulated hour against 1.75 over 59 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| heard | 1 | 0.766 | 0.742 | 0.025 | - | - | 0.948 | 0.951 | 0.501 | 1.29x | 13.8/21.1/26.7% | 1.8/4.6% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.791 | 0.732 | 0.059 | - | - | 0.884 | 0.942 | 0.568 | 1.37x | 14.6/22.3/28.1% | 2.0/4.9% | 3 |
| heard | 1 | 0.788 | 0.722 | 0.067 | - | - | 0.887 | 0.948 | 0.560 | 1.39x | 15.0/22.7/28.6% | 2.0/5.0% | 3 |

> replay-ordering=tip: decode_failures 22

> replay-ordering=heard: decode_failures 22

> slower: 6.39 s per simulated hour against 1.68 over 59 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| enum | 1 | 0.763 | 0.742 | 0.021 | - | - | 0.929 | 0.951 | 0.486 | 1.30x | 13.8/21.6/27.2% | 1.9/5.0% | 3 |
| hybrid | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.749 | 0.743 | 0.006 | - | - | 0.850 | 0.850 | 0.493 | 1.28x | 13.8/20.7/26.3% | 1.8/4.5% | 3 |
| 6 | 1 | 0.747 | 0.734 | 0.013 | - | - | 0.885 | 0.890 | 0.483 | 1.32x | 14.3/21.3/27.4% | 1.9/5.0% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.750 | 0.745 | 0.004 | - | - | 0.837 | 0.839 | 0.492 | 1.28x | 13.8/20.6/26.1% | 1.8/4.6% | 2 |
| 3 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 5 | 1 | 0.761 | 0.737 | 0.024 | - | - | 0.938 | 0.941 | 0.514 | 1.32x | 14.1/21.7/27.4% | 1.9/4.8% | 5 |
| 8 | 1 | 0.766 | 0.727 | 0.039 | - | - | 0.959 | 0.961 | 0.497 | 1.36x | 14.7/22.2/28.2% | 1.9/5.0% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.750 | 0.745 | 0.004 | - | - | 0.837 | 0.839 | 0.492 | 1.28x | 13.8/20.6/26.1% | 1.8/4.6% | 2 |
| 3 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 5 | 1 | 0.761 | 0.737 | 0.024 | - | - | 0.938 | 0.941 | 0.514 | 1.32x | 14.1/21.7/27.4% | 1.9/4.8% | 5 |
| 8 | 1 | 0.766 | 0.727 | 0.039 | - | - | 0.959 | 0.961 | 0.497 | 1.36x | 14.7/22.2/28.2% | 1.9/5.0% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| True | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.757 | 0.739 | 0.019 | - | - | 0.925 | 0.938 | 0.492 | 1.20x | 12.8/19.7/24.8% | 1.7/4.2% | 3 |
| 1 | 1 | 0.770 | 0.749 | 0.021 | - | - | 0.944 | 0.951 | 0.498 | 1.20x | 12.7/19.7/24.8% | 1.7/4.3% | 3 |
| 2 | 1 | 0.772 | 0.752 | 0.020 | - | - | 0.946 | 0.951 | 0.504 | 1.20x | 12.9/19.9/24.9% | 1.7/4.3% | 3 |
| 4 | 1 | 0.773 | 0.754 | 0.019 | - | - | 0.952 | 0.960 | 0.498 | 1.20x | 12.7/19.7/24.8% | 1.7/4.3% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.765 | 0.742 | 0.024 | - | - | 0.946 | 0.950 | 0.520 | 1.30x | 13.9/21.2/26.7% | 1.9/4.7% | 3 |
| 24 | 1 | 0.762 | 0.740 | 0.022 | - | - | 0.942 | 0.947 | 0.501 | 1.29x | 13.7/21.2/26.6% | 1.9/4.6% | 3 |
| 32 | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.939 | 0.952 | 0.479 | 1.30x | 13.9/21.3/26.8% | 1.8/4.6% | 3 |
| 64 | 1 | 0.761 | 0.740 | 0.021 | - | - | 0.932 | 0.937 | 0.511 | 1.31x | 14.0/21.4/27.0% | 1.8/4.7% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.767 | 0.741 | 0.026 | - | - | 0.946 | 0.954 | 0.482 | 1.36x | 14.6/22.3/28.1% | 1.9/5.0% | 3 |
| 16 | 1 | 0.766 | 0.743 | 0.023 | - | - | 0.932 | 0.941 | 0.502 | 1.31x | 13.8/21.4/26.8% | 1.9/4.7% | 3 |
| 32 | 1 | 0.762 | 0.739 | 0.024 | - | - | 0.932 | 0.941 | 0.472 | 1.31x | 13.9/21.3/26.8% | 1.9/4.7% | 3 |

> window-size=8: misdecodes 87

> window-size=16: misdecodes 37

> window-size=32: misdecodes 5

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.913 | 0.910 | 0.004 | - | - | 0.976 | 0.976 | 0.582 | 2.03x | 19.4/30.5/37.9% | 1.4/5.1% | 3 |
| True | 1 | 0.726 | 0.714 | 0.012 | - | - | 0.892 | 0.911 | 0.424 | 5.69x | 51.3/69.5/77.4% | 4.1/12.4% | 3 |

> no-congestion-scaling=True: decode_failures 93

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.517 | 0.511 | 0.006 | - | - | 0.533 | 0.534 | 0.209 | 4.15x | 14.7/22.7/30.4% | 1.4/4.8% | 3 |
| truesize | 1 | 0.549 | 0.544 | 0.005 | - | - | 0.569 | 0.571 | 0.224 | 3.06x | 10.9/17.3/23.2% | 1.0/3.7% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.919 | 0.915 | 0.004 | - | - | 0.980 | 0.980 | 0.575 | 1.93x | 18.3/29.0/36.0% | 1.3/4.9% | 3 |
| adaptive | 1 | 0.913 | 0.910 | 0.004 | - | - | 0.976 | 0.976 | 0.582 | 2.03x | 19.4/30.5/37.9% | 1.4/5.1% | 3 |

