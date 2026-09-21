# Sweep blocks-2026-09-21-9201645

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 9201645 · seeds 9201645
- **blocks** 87 run
- **compute** 13.7 h of simulator time across every cell
- **generated** 2026-09-21T09:23:48+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>227 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 3
- AD-amplify-worst: amplify-worst=0.0: decode_failures 3
- AD-amplify-worst: amplify-worst=0.1: decode_failures 3
- AD-badrouters: role-placement=degree: decode_failures 13
- AD-badrouters: role-placement=inverse: decode_failures 3
- AD-badrouters: role-placement=random: decode_failures 2
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 13
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 13
- AD-nomute: role-mix=no-mute: decode_failures 24
- AD-nomute: slower: 5.48 s per simulated hour against 2.35 over 31 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 13
- AD-siting: siting-mix=basement-heavy: decode_failures 2
- BL-control: protocol=sr: decode_failures 23
- BL-control: slower: 4.58 s per simulated hour against 1.7 over 31 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 10
- DB-warm: warm-num-nodes=0: decode_failures 90
- DB-warm: warm-num-nodes=25: decode_failures 90
- DB-warm: warm-num-nodes=100: decode_failures 90
- DB-warm: warm-num-nodes=2000: decode_failures 90
- DG-burst: burst-loss=0.0: decode_failures 3
- DG-burst: burst-loss=0.1: decode_failures 16
- DG-burst: burst-loss=0.2: decode_failures 19
- DG-burst: burst-loss=0.3: decode_failures 14
- DG-loss: extra-loss=0.0: decode_failures 3
- DG-loss: extra-loss=0.1: decode_failures 14
- DG-loss: extra-loss=0.2: decode_failures 23
- DG-loss: extra-loss=0.3: decode_failures 10
- DG-loss: slower: 5.22 s per simulated hour against 2.22 over 31 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 3
- DG-outage: burst-loss=0.1: decode_failures 29
- DG-outage: burst-loss=0.2: decode_failures 25
- DG-outage: burst-loss=0.3: decode_failures 18
- DM-mode: dm-mode=flood-only: decode_failures 27
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 19
- DM-mode: dm-mode=m4-early-flood: decode_failures 24
- DM-mode: slower: 8.06 s per simulated hour against 3.06 over 31 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 3
- FW-mixed-26: legacy-fraction=0.0: decode_failures 3
- FW-mixed-26: legacy-fraction=0.5: decode_failures 1
- FW-mixed-26: legacy-fraction=0.75: decode_failures 21
- FW-mixed-26: slower: 3.35 s per simulated hour against 1.67 over 31 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.75: decode_failures 30
- FW-signing-cost: profile-flag=signing=false: decode_failures 2
- FW-signing-cost: profile-flag=signing=true: decode_failures 3
- FW-versions: profile=2.8: decode_failures 3
- LD-chatty-hops: broadcast-interval-s=3600: decode_failures 22
- LD-chatty: broadcast-interval-s=3600: decode_failures 1
- LD-chatty: broadcast-interval-s=900: decode_failures 34
- LD-chatty: broadcast-interval-s=300: decode_failures 3
- LD-diurnal: diurnal=flat: decode_failures 15
- LD-diurnal: diurnal=sinusoid: decode_failures 23
- LD-diurnal: diurnal=commuter: decode_failures 3
- LD-diurnal: slower: 4.46 s per simulated hour against 1.58 over 31 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 34
- LD-interval: broadcast-interval-s=3600: decode_failures 1
- LD-interval: broadcast-interval-s=10800: decode_failures 2
- LD-interval: broadcast-interval-s=43200: decode_failures 4
- LD-interval: slower: 4.61 s per simulated hour against 1.31 over 31 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 3
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 1
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 34
- LD-traceroute: slower: 4.55 s per simulated hour against 2.06 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 90
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 93
- MS-density: nodes=60: decode_failures 3
- MS-hopscale: nodes=60: decode_failures 3
- MS-hopscale: nodes=500: decode_failures 12
- MS-oversubscribed: nodes=500: decode_failures 4
- MS-roles-fav: role-mix=legacy-default: decode_failures 14
- MS-roles-fav: slower: 3.75 s per simulated hour against 1.74 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-roles: role-mix=legacy-default: decode_failures 7
- MS-roles: role-mix=baymesh-2026-08: decode_failures 13
- MS-roles: slower: 4.63 s per simulated hour against 1.73 over 31 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 3
- MS-siting: siting-mix=uniform: decode_failures 3
- MS-siting: siting-mix=event: decode_failures 2
- MS-size: nodes=60: decode_failures 3
- MS-size: nodes=150: decode_failures 93
- MS-stretch: stretch=1.0: decode_failures 3
- MS-stretch: stretch=1.5: decode_failures 2
- MS-stretch: stretch=2.0: decode_failures 3
- MS-topology: topology=uniform: decode_failures 3
- MS-topology: topology=clustered: decode_failures 2
- MS-topology: topology=corridor: decode_failures 9
- PR-crladder: coding-rate-ladder=False: decode_failures 19
- PR-crladder: coding-rate-ladder=True: decode_failures 29
- PR-crladder: slower: 6.92 s per simulated hour against 2.75 over 31 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 29
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 20
- PR-dmmode-cr: slower: 8.66 s per simulated hour against 2.6 over 31 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 3
- PR-repeats: extra-repeats=False: decode_failures 3
- PR-repeats: extra-repeats=True: decode_failures 29
- PR-repeats: slower: 6.47 s per simulated hour against 1.62 over 31 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-duct: duct-per-hour=0.0: decode_failures 3
- RF-eu-presets: preset=SHORT_FAST: decode_failures 2
- RF-eu-presets: preset=LONG_FAST: decode_failures 3
- RF-noise: noise-profile=none: decode_failures 3
- RF-noise: noise-profile=temporal: decode_failures 13
- RF-noise: noise-profile=transient: decode_failures 10
- RF-noise: noise-profile=periodic: decode_failures 17
- RF-preset: preset=SHORT_FAST: decode_failures 2
- RF-preset: preset=LONG_FAST: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 17
- RF-preset-turbo: preset=LONG_FAST: decode_failures 3
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 14
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 17
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-pulse: slower: 3.41 s per simulated hour against 1.63 over 31 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 2
- RF-stretch-duct: faster: 1.25 s per simulated hour against 2.56 over 31 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=30: decode_failures 3
- RF-txpower: tx-power=14: decode_failures 5
- RT-favourites: favourite-routers=False: decode_failures 1
- RT-hopassign: hop-assign=centrality: decode_failures 3
- RT-hopassign: hop-assign=random: decode_failures 1
- RT-hoplimit: hop-limit=3: decode_failures 18
- RT-hoplimit: hop-limit=7: decode_failures 9
- RT-hoplimit: slower: 3.74 s per simulated hour against 1.76 over 31 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopspread: hop-limit=3: decode_failures 18
- RT-hopspread: hop-limit=5: decode_failures 16
- RT-hopspread: hop-limit=7: decode_failures 9
- RT-hopspread: slower: 5.77 s per simulated hour against 2.03 over 31 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 3
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 18
- RT-spread: hop-spread=True: decode_failures 3
- SC-signing: signature-policy=COMPATIBLE: decode_failures 3
- SC-signing: signature-policy=BALANCED: decode_failures 3
- SC-signing: signature-policy=STRICT: decode_failures 22
- SC-signing: slower: 4.18 s per simulated hour against 1.8 over 31 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 3
- SF-advert-transport: advert-transport=dm: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 12
- SF-bucket-mode: bucket-mode=local: decode_failures 3
- SF-bucket-mode: bucket-mode=time: misdecodes 10
- SF-bucket-mode: bucket-mode=window: misdecodes 9
- SF-bucket-mode: bucket-mode=window: decode_failures 2
- SF-bucket-time: time-bucket-s=600: misdecodes 67
- SF-bucket-time: time-bucket-s=1800: misdecodes 10
- SF-bucket-time: time-bucket-s=3600: misdecodes 2
- SF-bucket-time: time-bucket-s=3600: decode_failures 10
- SF-cadence: trigger=bucket: decode_failures 3
- SF-cadence: trigger=interval: misdecodes 6
- SF-cadence: trigger=aimd: decode_failures 27
- SF-cadence: trigger=bucket+interval: misdecodes 2
- SF-capacity-local: capacity=4: decode_failures 81
- SF-capacity-local: capacity=8: decode_failures 71
- SF-capacity-local: capacity=16: decode_failures 67
- SF-capacity-local: capacity=32: decode_failures 3
- SF-capacity-local: capacity=50: decode_failures 23
- SF-capacity-local: slower: 4.29 s per simulated hour against 1.77 over 31 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity: capacity=4: decode_failures 81
- SF-capacity: capacity=8: decode_failures 71
- SF-capacity: capacity=16: decode_failures 67
- SF-capacity: capacity=32: decode_failures 3
- SF-capacity: capacity=50: decode_failures 23
- SF-capacity: slower: 5.97 s per simulated hour against 1.7 over 31 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-window: capacity=8: misdecodes 1
- SF-capacity-window: capacity=8: decode_failures 84
- SF-capacity-window: capacity=16: misdecodes 1
- SF-capacity-window: capacity=16: decode_failures 61
- SF-capacity-window: capacity=32: misdecodes 9
- SF-capacity-window: capacity=32: decode_failures 2
- SF-capacity-window: slower: 3.35 s per simulated hour against 1.61 over 31 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 2
- SF-catchup: catch-up-hours=02-06: decode_failures 33
- SF-catchup: catch-up-hours=00-08: decode_failures 32
- SF-hops-flat: hops-apart=2: decode_failures 3
- SF-hops-flat: hops-apart=3: decode_failures 23
- SF-hops-flat: hops-apart=4: decode_failures 26
- SF-hops-spread: hops-apart=2: decode_failures 3
- SF-hops-spread: hops-apart=3: decode_failures 23
- SF-hops-spread: hops-apart=4: decode_failures 26
- SF-hops-spread: hops-apart=5: decode_failures 24
- SF-jitter-global: advert-jitter-s=1: decode_failures 26
- SF-jitter-global: advert-jitter-s=30: decode_failures 3
- SF-jitter-global: advert-jitter-s=120: decode_failures 31
- SF-jitter-global: advert-jitter-s=600: decode_failures 31
- SF-jitter-global: slower: 8.25 s per simulated hour against 1.77 over 31 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 26
- SF-jitter-local: advert-jitter-s=30: decode_failures 3
- SF-jitter-local: advert-jitter-s=120: decode_failures 31
- SF-jitter-local: advert-jitter-s=600: decode_failures 31
- SF-jitter-local: slower: 5.81 s per simulated hour against 1.77 over 31 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 2
- SF-place-flat: place=random-clients: decode_failures 16
- SF-place-flat: place=hops-apart: decode_failures 3
- SF-place-spread: place=spread: decode_failures 2
- SF-place-spread: place=random-clients: decode_failures 16
- SF-place-spread: place=hops-apart: decode_failures 3
- SF-provide-transport: provide-transport=dm: decode_failures 3
- SF-provide-transport: provide-transport=broadcast: decode_failures 19
- SF-provide-transport: slower: 3.9 s per simulated hour against 1.8 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 19
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 15
- SF-replay-order-broadcast: slower: 6.7 s per simulated hour against 1.77 over 31 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 3
- SF-replay-order: replay-ordering=heard: misdecodes 4
- SF-replay-order: replay-ordering=heard: decode_failures 27
- SF-replay-order: slower: 4.94 s per simulated hour against 1.69 over 31 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-resolve: resolve=sketch: decode_failures 16
- SF-resolve: resolve=hybrid: decode_failures 3
- SF-resolve: slower: 3.38 s per simulated hour against 1.53 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=3: decode_failures 3
- SF-servers-flat: servers=8: decode_failures 30
- SF-servers-flat: slower: 6.61 s per simulated hour against 2.54 over 31 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=3: decode_failures 3
- SF-servers-spread: servers=8: decode_failures 30
- SF-servers-spread: slower: 6.71 s per simulated hour against 2.35 over 31 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 3
- SF-signed: signed=True: decode_failures 3
- SF-sr-retries: sr-retries=0: decode_failures 10
- SF-sr-retries: sr-retries=1: decode_failures 14
- SF-sr-retries: sr-retries=4: decode_failures 4
- SF-sr-retries: slower: 4.15 s per simulated hour against 1.58 over 31 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 17
- SF-width: short-id-bits=24: decode_failures 16
- SF-width: short-id-bits=32: decode_failures 3
- SF-width: short-id-bits=64: decode_failures 9
- SF-width: slower: 5.13 s per simulated hour against 1.73 over 31 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 80
- SF-window-size: window-size=16: misdecodes 19
- SF-window-size: window-size=32: misdecodes 9
- SF-window-size: window-size=32: decode_failures 2
- TH-congestion: no-congestion-scaling=True: decode_failures 75

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-jitter-global` | 8.25 | 1.77 | 4.66x | 31 |
| `PR-repeats` | 6.47 | 1.62 | 3.98x | 31 |
| `SF-replay-order-broadcast` | 6.7 | 1.77 | 3.78x | 31 |
| `LD-interval` | 4.61 | 1.31 | 3.52x | 31 |
| `SF-capacity` | 5.97 | 1.7 | 3.50x | 31 |
| `PR-dmmode-cr` | 8.66 | 2.6 | 3.33x | 31 |
| `SF-jitter-local` | 5.81 | 1.77 | 3.29x | 31 |
| `SF-width` | 5.13 | 1.73 | 2.97x | 31 |
| `SF-replay-order` | 4.94 | 1.69 | 2.92x | 31 |
| `SF-servers-spread` | 6.71 | 2.35 | 2.86x | 31 |
| `RT-hopspread` | 5.77 | 2.03 | 2.85x | 31 |
| `LD-diurnal` | 4.46 | 1.58 | 2.82x | 31 |
| `BL-control` | 4.58 | 1.7 | 2.70x | 31 |
| `MS-roles` | 4.63 | 1.73 | 2.67x | 31 |
| `DM-mode` | 8.06 | 3.06 | 2.63x | 31 |
| `SF-sr-retries` | 4.15 | 1.58 | 2.63x | 31 |
| `SF-servers-flat` | 6.61 | 2.54 | 2.60x | 31 |
| `PR-crladder` | 6.92 | 2.75 | 2.51x | 31 |
| `SF-capacity-local` | 4.29 | 1.77 | 2.43x | 31 |
| `DG-loss` | 5.22 | 2.22 | 2.35x | 31 |
| `AD-nomute` | 5.48 | 2.35 | 2.33x | 31 |
| `SC-signing` | 4.18 | 1.8 | 2.32x | 31 |
| `LD-traceroute` | 4.55 | 2.06 | 2.21x | 31 |
| `SF-resolve` | 3.38 | 1.53 | 2.21x | 31 |
| `SF-provide-transport` | 3.9 | 1.8 | 2.17x | 31 |
| `MS-roles-fav` | 3.75 | 1.74 | 2.15x | 31 |
| `RT-hoplimit` | 3.74 | 1.76 | 2.12x | 31 |
| `RF-pulse` | 3.41 | 1.63 | 2.09x | 31 |
| `SF-capacity-window` | 3.35 | 1.61 | 2.07x | 31 |
| `FW-mixed-26` | 3.35 | 1.67 | 2.01x | 31 |
| `FW-mixed` | 3.32 | 1.67 | 1.99x | 31 |
| `FW-signing-cost` | 3.09 | 1.58 | 1.95x | 31 |
| `MS-size` | 6.51 | 3.38 | 1.93x | 31 |
| `AD-siting` | 2.56 | 1.35 | 1.90x | 31 |
| `SF-signed` | 3.18 | 1.74 | 1.82x | 31 |
| `RT-spread` | 3.82 | 2.15 | 1.78x | 31 |
| `SF-advert-transport` | 3.12 | 1.77 | 1.77x | 31 |
| `AD-amplify-worst` | 2.96 | 1.76 | 1.69x | 31 |
| `SF-hops-flat` | 5.3 | 3.25 | 1.63x | 31 |
| `AD-flooding` | 4.12 | 2.52 | 1.63x | 31 |
| `RT-rebroadcast` | 2.4 | 1.58 | 1.52x | 31 |
| `AD-badrouters` | 3.17 | 2.1 | 1.51x | 31 |
| `DB-hotstore-stress` | 14.3 | 22.6 | 0.63x | 31 |
| `MS-hopscale` | 10.7 | 18.1 | 0.59x | 31 |
| `MS-oversubscribed` | 11.3 | 19.7 | 0.57x | 31 |
| `RF-bw500` | 1.08 | 1.88 | 0.57x | 31 |
| `RF-stretch-duct` | 1.25 | 2.56 | 0.49x | 31 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `MS-siting` | siting-mix | **text** | 0.086 → 0.969 | 0.883 | 0.085 → 0.969 | 3.8x advert_bytes | up | 4 |
| `BL-control` | protocol | **held** | 0 → 0.821 | 0.821 | 0.592 → 0.601 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.778 | 0.778 | 0.592 → 0.601 | 1.1x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.061 → 0.778 | 0.716 | 0.031 → 0.608 | 16x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.101 → 0.778 | 0.677 | 0.046 → 0.592 | 13x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.069 → 0.729 | 0.660 | 0.071 → 0.550 | 1.2e+02x sr_airtime | down | 4 |
| `MS-topology` | topology | **held** | 0.380 → 0.983 | 0.603 | 0.425 → 0.949 | 3.4x sr_airtime | up | 4 |
| `AD-siting` | siting-mix | **held** | 0.189 → 0.776 | 0.587 | 0.058 → 0.544 | 4.6x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **held** | 0.218 → 0.778 | 0.559 | 0.077 → 0.592 | 4x sr_bytes | down | 4 |
| `RF-preset` | preset | **text** | 0.183 → 0.688 | 0.506 | 0.180 → 0.669 | 3x sr_airtime | up | 3 |
| `SF-place-flat` | place | **held** | 0.329 → 0.793 | 0.464 | 0.589 → 0.603 | 8.9x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.329 → 0.793 | 0.464 | 0.589 → 0.603 | 8.9x sr_bytes | up | 6 |
| `RF-eu-presets` | preset | **text** | 0.183 → 0.604 | 0.422 | 0.180 → 0.592 | 2.8x sr_bytes | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.198 → 0.604 | 0.406 | 0.195 → 0.592 | 8.1x bytes_on_air | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.199 → 0.583 | 0.384 | 0.192 → 0.560 | 2.4x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.465 → 0.826 | 0.361 | 0.353 → 0.637 | 13x sr_airtime | down | 3 |
| `RF-bw500` | preset | **held** | 0.195 → 0.549 | 0.354 | 0.099 → 0.404 | 2.9x advert_bytes | up | 3 |
| `MS-density` | nodes | **text** | 0.561 → 0.907 | 0.346 | 0.546 → 0.905 | 5.2x advert_bytes | up | 5 |
| `MS-oversubscribed` | nodes | **text** | 0.197 → 0.520 | 0.323 | 0.194 → 0.513 | 3.8x sr_bytes | down | 3 |
| `DG-outage` | burst-loss | **held** | 0.460 → 0.778 | 0.318 | 0.308 → 0.592 | 1.7x advert_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.451 → 0.768 | 0.317 | 0.427 → 0.766 | 1.6x sr_bytes | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.604 → 0.915 | 0.310 | 0.592 → 0.906 | 1.9x sr_bytes | up | 3 |
| `DG-burst` | burst-loss | **held** | 0.476 → 0.778 | 0.301 | 0.325 → 0.592 | 1.6x advert_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.427 → 0.727 | 0.300 | 0.415 → 0.721 | 10x sr_airtime | down | 3 |
| `MS-size` | nodes | **text** | 0.478 → 0.751 | 0.273 | 0.468 → 0.722 | 5.6x sr_bytes | down | 5 |
| `RF-noise` | noise-profile | **held** | 0.515 → 0.779 | 0.264 | 0.440 → 0.592 | 2x sr_airtime | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.451 → 0.704 | 0.253 | 0.427 → 0.698 | 1.3x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.604 → 0.842 | 0.237 | 0.592 → 0.835 | 2x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.646 → 0.875 | 0.229 | 0.631 → 0.869 | 3.3x sr_airtime | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.604 → 0.822 | 0.217 | 0.592 → 0.800 | 1.5x sr_airtime | up | 3 |
| `DG-loss` | extra-loss | **held** | 0.581 → 0.778 | 0.197 | 0.455 → 0.592 | 1.6x sr_airtime | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.530 → 0.713 | 0.183 | 0.519 → 0.702 | 2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.530 → 0.713 | 0.183 | 0.519 → 0.702 | 2x bytes_on_air | up | 3 |
| `SC-signing` | signature-policy | **held** | 0.613 → 0.778 | 0.164 | 0.490 → 0.592 | 1.4x sr_airtime | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.762 → 0.923 | 0.161 | 0.586 → 0.598 | 12x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.762 → 0.923 | 0.161 | 0.586 → 0.598 | 12x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.547 → 0.707 | 0.160 | 0.233 → 0.339 | 3.2x sr_airtime | up | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.666 → 0.821 | 0.155 | 0.582 → 0.594 | 2.7x sr_bytes | down | 5 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.604 → 0.759 | 0.155 | 0.592 → 0.748 | 2.1x sr_bytes | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.604 → 0.759 | 0.155 | 0.592 → 0.747 | 2x sr_bytes | up | 4 |
| `RT-spread` | hop-spread | **text** | 0.451 → 0.604 | 0.154 | 0.427 → 0.592 | 1.2x advert_bytes | up | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.677 → 0.821 | 0.144 | 0.586 → 0.594 | 2.7x sr_bytes | down | 4 |
| `LD-interval` | broadcast-interval-s | **held** | 0.718 → 0.854 | 0.136 | 0.557 → 0.660 | 6.3x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.642 → 0.778 | 0.135 | 0.592 → 0.594 | 15x sr_airtime | down | 3 |
| `SF-capacity-window` | capacity | **held** | 0.666 → 0.793 | 0.126 | 0.590 → 0.603 | 4.6x sr_bytes | up | 3 |
| `MS-roles` | role-mix | **held** | 0.656 → 0.781 | 0.125 | 0.519 → 0.601 | 1.2x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.669 → 0.791 | 0.121 | 0.558 → 0.613 | 1.4x sr_bytes | down | 2 |
| `DB-hotstore` | max-num-nodes | **held** | 0.661 → 0.770 | 0.109 | 0.534 → 0.634 | 2.3x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.672 → 0.770 | 0.099 | 0.538 → 0.634 | 2.2x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **held** | 0.597 → 0.672 | 0.075 | 0.474 → 0.519 | 1.2x sr_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.736 → 0.811 | 0.075 | 0.589 → 0.606 | 1.3x sr_bytes | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.718 → 0.791 | 0.073 | 0.549 → 0.599 | 1.4x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **held** | 0.778 → 0.850 | 0.073 | 0.592 → 0.651 | 3.3x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.715 → 0.778 | 0.063 | 0.575 → 0.593 | 16x advert_bytes | down | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.587 → 0.643 | 0.056 | 0.575 → 0.629 | 1.3x sr_airtime | down | 2 |
| `FW-versions` | profile | **held** | 0.778 → 0.832 | 0.054 | 0.592 → 0.624 | 3.2x bytes_on_air | down | 5 |
| `SF-resolve` | resolve | **held** | 0.725 → 0.778 | 0.053 | 0.584 → 0.601 | 5.9x advert_bytes | up | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.711 → 0.762 | 0.051 | 0.575 → 0.592 | 9x advert_bytes | down | 3 |
| `FW-firmware` | profile | **held** | 0.778 → 0.818 | 0.040 | 0.592 → 0.621 | 3.1x bytes_on_air | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.612 → 0.652 | 0.040 | 0.601 → 0.643 | 1.2x sr_bytes | up | 2 |
| `SF-capacity` | capacity | **held** | 0.742 → 0.780 | 0.038 | 0.579 → 0.605 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.742 → 0.780 | 0.038 | 0.579 → 0.605 | 5.3x advert_bytes | up | 5 |
| `LD-diurnal` | diurnal | **text** | 0.604 → 0.641 | 0.036 | 0.592 → 0.628 | 1.3x advert_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.604 → 0.639 | 0.034 | 0.586 → 0.592 | 3.9x sr_airtime | up | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.342 → 0.374 | 0.033 | 0.337 → 0.370 | 2x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.761 → 0.793 | 0.031 | 0.584 → 0.592 | 4.4x advert_bytes | up | 3 |
| `RT-hopassign` | hop-assign | **held** | 0.747 → 0.778 | 0.030 | 0.592 → 0.610 | 1.1x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.604 → 0.631 | 0.026 | 0.592 → 0.621 | 1.3x sr_bytes | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.559 → 0.582 | 0.022 | 0.559 → 0.582 | 1.1x sr_airtime | up | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.771 → 0.793 | 0.021 | 0.592 → 0.598 | 2.8x advert_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.604 → 0.623 | 0.019 | 0.592 → 0.612 | 1.2x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.760 → 0.778 | 0.018 | 0.586 → 0.592 | 1.2x sr_bytes | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.760 → 0.778 | 0.017 | 0.591 → 0.603 | 1.2x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.760 → 0.778 | 0.017 | 0.591 → 0.603 | 1.2x sr_bytes | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.760 → 0.775 | 0.016 | 0.582 → 0.598 | 2.2x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.689 → 0.705 | 0.015 | 0.578 → 0.580 | 1.3x sr_airtime | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.762 → 0.777 | 0.015 | 0.585 → 0.595 | 5.1x advert_bytes | down | 3 |
| `AD-worst` | role-placement | **held** | 0.878 → 0.892 | 0.014 | 0.656 → 0.659 | 1x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.763 → 0.778 | 0.014 | 0.590 → 0.597 | 3.1x advert_bytes | up | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.691 → 0.705 | 0.014 | 0.577 → 0.578 | 1.3x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.863 → 0.875 | 0.013 | 0.856 → 0.869 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.778 → 0.783 | 0.006 | 0.592 → 0.596 | 2x advert_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.744 → 0.748 | 0.004 | 0.581 → 0.586 | 1x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.875 → 0.878 | 0.002 | 0.869 → 0.871 | 1x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.978 → 0.978 | 0.000 | 0.869 → 0.869 | 1.1x sr_bytes | down | 2 |

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
| none | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| sprinkled | 1 | 0.701 | 0.690 | 0.012 | - | - | 0.850 | 0.854 | 0.305 | 1.27x | 12.9/21.0/23.3% | 2.0/4.5% | 3 |
| arms-race | 1 | 0.842 | 0.835 | 0.007 | - | - | 0.940 | 0.942 | 0.343 | 1.19x | 17.1/22.8/25.1% | 1.8/5.4% | 3 |

> amplifier-mix=none: decode_failures 3

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.720 | 0.698 | 0.022 | - | - | 0.776 | 0.776 | 0.517 | 1.23x | 13.9/19.1/23.0% | 1.8/4.7% | 3 |
| 0.3 | 1 | 0.915 | 0.906 | 0.009 | - | - | 0.956 | 0.957 | 0.707 | 1.12x | 21.6/26.6/29.4% | 1.5/5.1% | 3 |

> amplify-worst=0.0: decode_failures 3

> amplify-worst=0.1: decode_failures 3

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.530 | 0.519 | 0.011 | - | - | 0.656 | 0.687 | 0.180 | 1.14x | 11.6/18.6/21.9% | 2.0/4.3% | 3 |
| inverse | 1 | 0.486 | 0.474 | 0.013 | - | - | 0.672 | 0.673 | 0.180 | 1.09x | 10.9/18.5/21.0% | 1.9/3.7% | 3 |
| random | 1 | 0.491 | 0.481 | 0.010 | - | - | 0.597 | 0.599 | 0.041 | 1.09x | 11.2/19.7/21.6% | 1.9/4.6% | 3 |

> role-placement=degree: decode_failures 13

> role-placement=inverse: decode_failures 3

> role-placement=random: decode_failures 2

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.530 | 0.519 | 0.011 | - | - | 0.656 | 0.687 | 0.180 | 1.14x | 11.6/18.6/21.9% | 2.0/4.3% | 3 |
| all-routers | 1 | 0.713 | 0.702 | 0.011 | - | - | 0.836 | 0.844 | 0.331 | 2.27x | 21.1/30.5/32.6% | 3.7/4.7% | 3 |

> role-mix=baymesh-2026-08: decode_failures 13

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.530 | 0.519 | 0.011 | - | - | 0.656 | 0.687 | 0.180 | 1.14x | 11.6/18.6/21.9% | 2.0/4.3% | 3 |
| no-mute | 1 | 0.651 | 0.637 | 0.014 | - | - | 0.797 | 0.825 | 0.238 | 1.21x | 12.0/17.9/19.7% | 1.9/4.9% | 3 |
| all-routers | 1 | 0.713 | 0.702 | 0.011 | - | - | 0.836 | 0.844 | 0.331 | 2.27x | 21.1/30.5/32.6% | 3.7/4.7% | 3 |

> role-mix=baymesh-2026-08: decode_failures 13

> role-mix=no-mute: decode_failures 24

> slower: 5.48 s per simulated hour against 2.35 over 31 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.530 | 0.519 | 0.011 | - | - | 0.656 | 0.687 | 0.180 | 1.14x | 11.6/18.6/21.9% | 2.0/4.3% | 3 |
| local-typical | 1 | 0.562 | 0.544 | 0.017 | - | - | 0.776 | 0.778 | 0.000 | 1.16x | 11.1/22.0/23.8% | 1.9/5.4% | 3 |
| basement-heavy | 1 | 0.060 | 0.058 | 0.002 | - | - | 0.189 | 0.238 | 0.000 | 0.45x | 1.3/5.1/6.5% | 0.3/2.2% | 3 |

> siting-mix=uniform: decode_failures 13

> siting-mix=basement-heavy: decode_failures 2

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.672 | 0.659 | 0.013 | - | - | 0.878 | 0.881 | 0.000 | 2.36x | 15.3/27.0/32.8% | 1.9/6.1% | 3 |
| inverse | 1 | 0.670 | 0.656 | 0.015 | - | - | 0.892 | 0.894 | 0.000 | 2.31x | 14.8/23.4/29.2% | 1.9/3.3% | 3 |

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.601 | 0.601 | 0.000 | - | - | 0 | 0.000 | 0.093 | 1.17x | 11.8/18.7/20.8% | 1.8/4.4% | 3 |
| sr | 1 | 0.626 | 0.592 | 0.034 | - | - | 0.821 | 0.920 | 0.087 | 1.19x | 12.2/18.8/20.7% | 1.7/4.5% | 3 |

> protocol=sr: decode_failures 23

> slower: 4.58 s per simulated hour against 1.7 over 31 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.544 | 0.534 | 0.010 | - | - | 0.661 | 0.667 | 0.106 | 2.42x | 23.0/41.4/46.0% | 3.6/7.5% | 3 |
| 100 | 1 | 0.643 | 0.634 | 0.009 | - | - | 0.770 | 0.771 | 0.114 | 1.39x | 13.0/24.4/27.3% | 2.1/4.5% | 3 |
| 120 | 1 | 0.643 | 0.634 | 0.009 | - | - | 0.770 | 0.771 | 0.114 | 1.39x | 13.0/24.4/27.3% | 2.1/4.5% | 3 |
| 250 | 1 | 0.643 | 0.634 | 0.009 | - | - | 0.770 | 0.771 | 0.114 | 1.39x | 13.0/24.4/27.3% | 2.1/4.5% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.238 | 0.233 | 0.005 | - | - | 0.547 | 0.548 | 0.060 | 10.23x | 26.3/47.6/62.9% | 3.5/10.4% | 3 |
| 120 | 1 | 0.342 | 0.337 | 0.004 | - | - | 0.707 | 0.708 | 0.065 | 4.66x | 11.5/23.9/34.3% | 1.6/5.4% | 3 |
| 250 | 1 | 0.343 | 0.339 | 0.004 | - | - | 0.702 | 0.704 | 0.065 | 4.60x | 11.5/23.5/33.8% | 1.6/5.2% | 3 |

> max-num-nodes=10: decode_failures 10

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.643 | 0.634 | 0.009 | - | - | 0.770 | 0.771 | 0.114 | 1.39x | 13.0/24.4/27.3% | 2.1/4.5% | 3 |
| baymesh-2026-08 | 1 | 0.643 | 0.634 | 0.009 | - | - | 0.770 | 0.771 | 0.114 | 1.39x | 13.0/24.4/27.3% | 2.1/4.5% | 3 |
| constrained | 1 | 0.548 | 0.538 | 0.010 | - | - | 0.672 | 0.673 | 0.128 | 2.42x | 23.1/41.5/46.1% | 3.7/7.5% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.817 | 0.859 | 0.365 | 5.62x | 47.0/64.7/72.6% | 4.1/12.1% | 3 |
| 25 | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.817 | 0.859 | 0.365 | 5.62x | 47.0/64.7/72.6% | 4.1/12.1% | 3 |
| 100 | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.817 | 0.859 | 0.365 | 5.62x | 47.0/64.7/72.6% | 4.1/12.1% | 3 |
| 2000 | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.817 | 0.859 | 0.365 | 5.62x | 47.0/64.7/72.6% | 4.1/12.1% | 3 |

> warm-num-nodes=0: decode_failures 90

> warm-num-nodes=25: decode_failures 90

> warm-num-nodes=100: decode_failures 90

> warm-num-nodes=2000: decode_failures 90

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.520 | 0.500 | 0.020 | - | - | 0.711 | 0.743 | 0.067 | 1.11x | 11.3/18.1/20.2% | 1.7/4.3% | 3 |
| 0.2 | 1 | 0.430 | 0.414 | 0.017 | - | - | 0.589 | 0.675 | 0.051 | 1.02x | 10.6/16.7/18.5% | 1.5/3.7% | 3 |
| 0.3 | 1 | 0.340 | 0.325 | 0.015 | - | - | 0.476 | 0.599 | 0.036 | 0.93x | 9.7/15.4/16.8% | 1.4/3.3% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 16

> burst-loss=0.2: decode_failures 19

> burst-loss=0.3: decode_failures 14

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.567 | 0.554 | 0.013 | - | - | 0.733 | 0.760 | 0.087 | 1.20x | 12.3/19.3/21.4% | 1.8/4.6% | 3 |
| 0.2 | 1 | 0.519 | 0.505 | 0.014 | - | - | 0.685 | 0.733 | 0.058 | 1.23x | 12.5/19.5/21.6% | 1.9/4.4% | 3 |
| 0.3 | 1 | 0.465 | 0.455 | 0.010 | - | - | 0.581 | 0.690 | 0.051 | 1.25x | 13.1/19.3/21.3% | 1.9/4.1% | 3 |

> extra-loss=0.0: decode_failures 3

> extra-loss=0.1: decode_failures 14

> extra-loss=0.2: decode_failures 23

> extra-loss=0.3: decode_failures 10

> slower: 5.22 s per simulated hour against 2.22 over 31 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.1 | 1 | 0.505 | 0.491 | 0.014 | - | - | 0.672 | 0.725 | 0.064 | 1.11x | 11.2/18.1/20.3% | 1.6/4.3% | 3 |
| 0.2 | 1 | 0.413 | 0.400 | 0.013 | - | - | 0.553 | 0.650 | 0.055 | 1.04x | 10.8/17.3/18.9% | 1.6/4.0% | 3 |
| 0.3 | 1 | 0.322 | 0.308 | 0.014 | - | - | 0.460 | 0.595 | 0.026 | 0.98x | 10.2/16.1/18.0% | 1.5/3.5% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 29

> burst-loss=0.2: decode_failures 25

> burst-loss=0.3: decode_failures 18

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.559 | 0.559 | 0.000 | - | - | 0.667 | 0.743 | 0.092 | 1.44x | 14.4/23.8/26.7% | 2.1/5.6% | 3 |
| directed-with-late-flood | 1 | 0.580 | 0.580 | 0.000 | - | - | 0.689 | 0.764 | 0.099 | 1.37x | 13.9/22.8/25.6% | 2.0/5.5% | 3 |
| m4-early-flood | 1 | 0.582 | 0.582 | 0.000 | - | - | 0.689 | 0.766 | 0.099 | 1.37x | 13.8/22.7/25.5% | 2.0/5.4% | 3 |

> dm-mode=flood-only: decode_failures 27

> dm-mode=directed-with-late-flood: decode_failures 19

> dm-mode=m4-early-flood: decode_failures 24

> slower: 8.06 s per simulated hour against 3.06 over 31 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.633 | 0.621 | 0.012 | - | - | 0.818 | 0.820 | 0.126 | 0.71x | 7.4/9.6/12.1% | 1.1/2.1% | 3 |
| 2.8 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> profile=2.8: decode_failures 3

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.637 | 0.629 | 0.007 | - | - | 0.801 | 0.806 | 0.000 | 1.08x | 10.0/21.5/25.1% | 1.6/4.4% | 3 |
| 0.5 | 1 | 0.759 | 0.747 | 0.013 | - | - | 0.881 | 0.884 | 0.401 | 1.05x | 10.3/15.5/16.7% | 1.7/3.8% | 3 |
| 0.75 | 1 | 0.698 | 0.687 | 0.010 | - | - | 0.805 | 0.863 | 0.236 | 0.86x | 8.9/13.5/15.7% | 1.4/3.6% | 3 |

> legacy-fraction=0.0: decode_failures 3

> legacy-fraction=0.75: decode_failures 30

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.625 | 0.618 | 0.007 | - | - | 0.763 | 0.766 | 0.000 | 1.08x | 10.2/20.7/24.4% | 1.6/4.2% | 3 |
| 0.5 | 1 | 0.759 | 0.748 | 0.011 | - | - | 0.884 | 0.888 | 0.398 | 1.04x | 10.6/15.3/16.4% | 1.6/3.8% | 3 |
| 0.75 | 1 | 0.697 | 0.686 | 0.011 | - | - | 0.783 | 0.854 | 0.255 | 0.84x | 8.7/13.4/15.4% | 1.3/3.6% | 3 |

> legacy-fraction=0.0: decode_failures 3

> legacy-fraction=0.5: decode_failures 1

> legacy-fraction=0.75: decode_failures 21

> slower: 3.35 s per simulated hour against 1.67 over 31 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.663 | 0.651 | 0.012 | - | - | 0.850 | 0.851 | 0.083 | 0.66x | 6.7/11.5/12.9% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> profile-flag=signing=false: decode_failures 2

> profile-flag=signing=true: decode_failures 3

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.625 | 0.614 | 0.011 | - | - | 0.819 | 0.821 | 0.121 | 0.71x | 7.7/10.2/13.1% | 1.2/2.4% | 3 |
| 2.5 | 1 | 0.631 | 0.619 | 0.012 | - | - | 0.807 | 0.809 | 0.141 | 0.72x | 7.6/10.0/12.8% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.632 | 0.620 | 0.012 | - | - | 0.832 | 0.833 | 0.130 | 0.70x | 7.6/10.1/13.1% | 1.1/2.5% | 3 |
| 2.7 | 1 | 0.633 | 0.624 | 0.010 | - | - | 0.829 | 0.829 | 0.146 | 0.71x | 7.7/11.7/14.6% | 1.0/3.0% | 3 |
| 2.8 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> profile=2.8: decode_failures 3

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.650 | 0.637 | 0.013 | - | - | 0.826 | 0.836 | 0.076 | 0.79x | 8.0/13.2/14.8% | 1.2/3.3% | 3 |
| 900 | 1 | 0.571 | 0.557 | 0.014 | - | - | 0.718 | 0.747 | 0.086 | 1.85x | 18.3/29.5/32.9% | 2.8/7.1% | 3 |
| 300 | 1 | 0.361 | 0.353 | 0.008 | - | - | 0.465 | 0.522 | 0.081 | 4.38x | 41.6/61.9/67.2% | 6.5/14.9% | 3 |

> broadcast-interval-s=3600: decode_failures 1

> broadcast-interval-s=900: decode_failures 34

> broadcast-interval-s=300: decode_failures 3

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.727 | 0.721 | 0.005 | - | - | 0.838 | 0.853 | 0.180 | 0.91x | 9.4/14.3/15.8% | 1.4/3.4% | 3 |
| 900 | 1 | 0.648 | 0.640 | 0.008 | - | - | 0.770 | 0.779 | 0.179 | 2.07x | 20.9/31.5/35.0% | 3.3/7.4% | 3 |
| 300 | 1 | 0.427 | 0.415 | 0.011 | - | - | 0.560 | 0.576 | 0.176 | 4.50x | 43.4/61.9/67.8% | 7.1/14.4% | 3 |

> broadcast-interval-s=3600: decode_failures 22

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.641 | 0.628 | 0.013 | - | - | 0.805 | 0.831 | 0.086 | 1.12x | 11.2/18.4/20.6% | 1.7/4.5% | 3 |
| sinusoid | 1 | 0.619 | 0.607 | 0.013 | - | - | 0.772 | 0.804 | 0.101 | 1.06x | 10.7/17.5/19.5% | 1.6/4.3% | 3 |
| commuter | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> diurnal=flat: decode_failures 15

> diurnal=sinusoid: decode_failures 23

> diurnal=commuter: decode_failures 3

> slower: 4.46 s per simulated hour against 1.58 over 31 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.571 | 0.557 | 0.014 | - | - | 0.718 | 0.747 | 0.086 | 1.85x | 18.3/29.5/32.9% | 2.8/7.1% | 3 |
| 3600 | 1 | 0.650 | 0.637 | 0.013 | - | - | 0.826 | 0.836 | 0.076 | 0.79x | 8.0/13.2/14.8% | 1.2/3.3% | 3 |
| 10800 | 1 | 0.665 | 0.652 | 0.013 | - | - | 0.848 | 0.850 | 0.089 | 0.52x | 5.3/9.0/10.0% | 0.7/2.4% | 3 |
| 43200 | 1 | 0.671 | 0.660 | 0.011 | - | - | 0.854 | 0.862 | 0.105 | 0.34x | 3.3/6.1/6.9% | 0.4/1.7% | 3 |

> broadcast-interval-s=900: decode_failures 34

> broadcast-interval-s=3600: decode_failures 1

> broadcast-interval-s=10800: decode_failures 2

> broadcast-interval-s=43200: decode_failures 4

> slower: 4.61 s per simulated hour against 1.31 over 31 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.613 | 0.599 | 0.014 | - | - | 0.791 | 0.801 | 0.090 | 1.24x | 12.5/20.4/22.6% | 1.8/5.0% | 3 |
| 1.0 | 1 | 0.590 | 0.575 | 0.015 | - | - | 0.775 | 0.776 | 0.096 | 1.32x | 13.2/21.8/24.5% | 1.9/5.4% | 3 |
| 4.0 | 1 | 0.562 | 0.549 | 0.013 | - | - | 0.718 | 0.756 | 0.093 | 1.64x | 16.7/27.0/30.3% | 2.5/6.7% | 3 |

> traceroute-per-hour=0.0: decode_failures 3

> traceroute-per-hour=0.25: decode_failures 1

> traceroute-per-hour=4.0: decode_failures 34

> slower: 4.55 s per simulated hour against 2.06 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.817 | 0.859 | 0.365 | 5.62x | 47.0/64.7/72.6% | 4.1/12.1% | 3 |
| 1.0 | 1 | 0.587 | 0.575 | 0.012 | - | - | 0.768 | 0.828 | 0.326 | 6.32x | 52.2/68.7/76.0% | 4.7/13.5% | 3 |

> traceroute-per-hour=0.0: decode_failures 90

> traceroute-per-hour=1.0: decode_failures 93

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.561 | 0.546 | 0.015 | - | - | 0.783 | 0.792 | 0.000 | 1.04x | 11.2/18.1/20.3% | 2.6/5.3% | 3 |
| 60 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 90 | 1 | 0.840 | 0.830 | 0.010 | - | - | 0.950 | 0.951 | 0.592 | 1.73x | 14.9/24.9/31.2% | 1.7/4.7% | 3 |
| 120 | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.978 | 0.978 | 0.510 | 2.05x | 17.8/27.4/33.9% | 1.5/5.1% | 3 |
| 150 | 1 | 0.907 | 0.905 | 0.002 | - | - | 0.990 | 0.991 | 0.586 | 2.69x | 21.5/38.2/44.8% | 1.5/5.4% | 3 |

> nodes=60: decode_failures 3

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 120 | 1 | 0.521 | 0.513 | 0.008 | - | - | 0.717 | 0.719 | 0.210 | 2.46x | 12.0/24.3/31.7% | 1.8/5.0% | 3 |
| 250 | 1 | 0.338 | 0.334 | 0.004 | - | - | 0.690 | 0.691 | 0.068 | 4.93x | 12.2/25.5/36.7% | 1.7/5.8% | 3 |
| 500 | 1 | 0.198 | 0.195 | 0.004 | - | - | 0.404 | 0.404 | 0.037 | 9.38x | 12.3/22.5/38.9% | 1.7/5.4% | 3 |

> nodes=60: decode_failures 3

> nodes=500: decode_failures 12

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.520 | 0.513 | 0.007 | - | - | 0.722 | 0.724 | 0.212 | 2.38x | 11.4/23.6/30.6% | 1.7/4.8% | 3 |
| 250 | 1 | 0.342 | 0.337 | 0.004 | - | - | 0.707 | 0.708 | 0.065 | 4.66x | 11.5/23.9/34.3% | 1.6/5.4% | 3 |
| 500 | 1 | 0.197 | 0.194 | 0.004 | - | - | 0.404 | 0.406 | 0.038 | 8.81x | 11.6/21.2/36.3% | 1.5/5.1% | 3 |

> nodes=500: decode_failures 4

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.615 | 0.601 | 0.014 | - | - | 0.781 | 0.796 | 0.122 | 1.19x | 11.8/19.4/21.7% | 1.8/4.8% | 3 |
| baymesh-2026-08 | 1 | 0.530 | 0.519 | 0.011 | - | - | 0.656 | 0.687 | 0.180 | 1.14x | 11.6/18.6/21.9% | 2.0/4.3% | 3 |

> role-mix=legacy-default: decode_failures 7

> role-mix=baymesh-2026-08: decode_failures 13

> slower: 4.63 s per simulated hour against 1.73 over 31 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.628 | 0.613 | 0.014 | - | - | 0.791 | 0.807 | 0.135 | 1.21x | 12.2/19.6/21.6% | 1.8/4.7% | 3 |
| baymesh-2026-08 | 1 | 0.565 | 0.558 | 0.007 | - | - | 0.669 | 0.673 | 0.224 | 1.25x | 12.7/23.2/26.1% | 2.3/4.3% | 3 |

> role-mix=legacy-default: decode_failures 14

> slower: 3.75 s per simulated hour against 1.74 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.05 | 1 | 0.619 | 0.607 | 0.011 | - | - | 0.785 | 0.789 | 0.099 | 1.25x | 12.2/21.6/25.2% | 1.8/4.7% | 3 |
| 0.1 | 1 | 0.616 | 0.604 | 0.013 | - | - | 0.776 | 0.776 | 0.122 | 1.32x | 12.4/24.9/28.8% | 1.9/4.5% | 3 |
| 0.2 | 1 | 0.631 | 0.621 | 0.010 | - | - | 0.774 | 0.778 | 0.099 | 1.48x | 14.2/28.3/31.3% | 2.2/4.5% | 3 |

> router-late-fraction=0.0: decode_failures 3

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| local-typical | 1 | 0.738 | 0.732 | 0.007 | - | - | 0.934 | 0.935 | 0.000 | 1.49x | 13.0/23.3/27.9% | 2.5/5.5% | 3 |
| event | 1 | 0.086 | 0.085 | 0.001 | - | - | 0.271 | 0.281 | 0.000 | 0.61x | 1.4/6.1/10.7% | 0.6/2.7% | 3 |
| backbone | 1 | 0.969 | 0.969 | 0.000 | - | - | 0.998 | 0.998 | 0.835 | 1.14x | 25.1/31.1/34.5% | 1.4/5.5% | 3 |

> siting-mix=uniform: decode_failures 3

> siting-mix=event: decode_failures 2

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.751 | 0.722 | 0.029 | - | - | 0.875 | 0.877 | 0.450 | 1.33x | 18.3/27.9/29.9% | 3.1/6.8% | 3 |
| 60 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 90 | 1 | 0.547 | 0.540 | 0.008 | - | - | 0.798 | 0.799 | 0.177 | 1.78x | 11.1/25.0/32.1% | 1.7/4.6% | 3 |
| 120 | 1 | 0.521 | 0.513 | 0.008 | - | - | 0.717 | 0.719 | 0.210 | 2.46x | 12.0/24.3/31.7% | 1.8/5.0% | 3 |
| 150 | 1 | 0.478 | 0.468 | 0.010 | - | - | 0.703 | 0.759 | 0.000 | 2.99x | 12.4/24.2/30.2% | 1.7/5.0% | 3 |

> nodes=60: decode_failures 3

> nodes=150: decode_failures 93

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 1.25 | 1 | 0.307 | 0.301 | 0.006 | - | - | 0.462 | 0.466 | 0.000 | 1.44x | 10.0/18.6/22.1% | 2.2/4.8% | 3 |
| 1.5 | 1 | 0.199 | 0.192 | 0.007 | - | - | 0.396 | 0.402 | 0.000 | 1.10x | 5.9/12.1/14.7% | 2.0/4.3% | 3 |
| 2.0 | 1 | 0.078 | 0.077 | 0.001 | - | - | 0.218 | 0.238 | 0.000 | 0.64x | 2.6/5.4/9.9% | 0.9/2.7% | 3 |

> stretch=1.0: decode_failures 3

> stretch=1.5: decode_failures 2

> stretch=2.0: decode_failures 3

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| clustered | 1 | 0.788 | 0.787 | 0.001 | - | - | 0.709 | 0.877 | 0.025 | 1.10x | 28.8/37.4/39.4% | 1.5/5.6% | 3 |
| corridor | 1 | 0.428 | 0.425 | 0.003 | - | - | 0.380 | 0.394 | 0.148 | 1.45x | 14.0/22.0/24.5% | 2.2/4.6% | 3 |
| hub | 1 | 0.949 | 0.949 | 0.000 | - | - | 0.983 | 0.983 | 0.824 | 1.27x | 23.7/31.6/33.1% | 1.8/5.5% | 3 |

> topology=uniform: decode_failures 3

> topology=clustered: decode_failures 2

> topology=corridor: decode_failures 9

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.580 | 0.580 | 0.000 | - | - | 0.689 | 0.764 | 0.099 | 1.37x | 13.9/22.8/25.6% | 2.0/5.5% | 3 |
| True | 1 | 0.578 | 0.578 | 0.000 | - | - | 0.705 | 0.767 | 0.093 | 1.38x | 13.8/23.0/25.8% | 2.0/5.5% | 3 |

> coding-rate-ladder=False: decode_failures 19

> coding-rate-ladder=True: decode_failures 29

> slower: 6.92 s per simulated hour against 2.75 over 31 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.578 | 0.578 | 0.000 | - | - | 0.705 | 0.767 | 0.093 | 1.38x | 13.8/23.0/25.8% | 2.0/5.5% | 3 |
| m4-early-flood | 1 | 0.577 | 0.577 | 0.000 | - | - | 0.691 | 0.772 | 0.093 | 1.37x | 13.8/22.8/25.6% | 1.9/5.5% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 29

> dm-mode=m4-early-flood: decode_failures 20

> slower: 8.66 s per simulated hour against 2.6 over 31 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.601 | 0.601 | 0.000 | - | - | 0 | 0.000 | 0.093 | 1.17x | 11.8/18.7/20.8% | 1.8/4.4% | 3 |
| chain | 1 | 0.600 | 0.596 | 0.005 | - | - | 0.683 | 0.795 | 0.076 | 1.30x | 13.0/22.6/25.2% | 1.8/5.6% | 3 |
| sr | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> protocol=sr: decode_failures 3

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| True | 1 | 0.623 | 0.612 | 0.011 | - | - | 0.778 | 0.811 | 0.113 | 1.20x | 12.0/19.6/21.8% | 1.8/4.8% | 3 |

> extra-repeats=False: decode_failures 3

> extra-repeats=True: decode_failures 29

> slower: 6.47 s per simulated hour against 1.62 over 31 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.978 | 0.978 | 0.510 | 2.05x | 17.8/27.4/33.9% | 1.5/5.1% | 3 |
| True | 1 | 0.878 | 0.871 | 0.006 | - | - | 0.978 | 0.979 | 0.545 | 2.09x | 18.2/27.5/34.1% | 1.5/5.1% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.100 | 0.099 | 0.000 | - | - | 0.195 | 0.197 | 0.000 | 0.03x | 0.1/0.3/0.6% | 0.1/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.216 | 0.209 | 0.008 | - | - | 0.440 | 0.445 | 0.000 | 0.17x | 0.9/2.0/2.3% | 0.3/0.7% | 3 |
| LONG_TURBO | 1 | 0.416 | 0.404 | 0.011 | - | - | 0.549 | 0.553 | 0.085 | 1.24x | 10.3/16.8/18.8% | 1.8/3.9% | 3 |

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 0.25 | 1 | 0.629 | 0.614 | 0.015 | - | - | 0.787 | 0.797 | 0.153 | 1.15x | 13.0/20.5/22.4% | 1.7/4.8% | 3 |
| 1.0 | 1 | 0.822 | 0.800 | 0.021 | - | - | 0.911 | 0.914 | 0.581 | 0.82x | 18.9/23.6/24.5% | 1.1/4.6% | 3 |

> duct-per-hour=0.0: decode_failures 3

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.183 | 0.180 | 0.003 | - | - | 0.386 | 0.394 | 0.000 | 0.10x | 0.5/1.0/1.3% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| LITE_FAST | 1 | 0.454 | 0.452 | 0.002 | - | - | 0.502 | 0.503 | 0.043 | 0.92x | 8.3/13.8/15.8% | 1.4/3.2% | 3 |
| NARROW_SLOW | 1 | 0.506 | 0.498 | 0.008 | - | - | 0.619 | 0.621 | 0.036 | 1.10x | 11.0/16.1/18.1% | 1.7/3.8% | 3 |

> preset=SHORT_FAST: decode_failures 2

> preset=LONG_FAST: decode_failures 3

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| temporal | 1 | 0.447 | 0.440 | 0.006 | - | - | 0.515 | 0.627 | 0.084 | 1.19x | 11.9/18.5/20.7% | 1.7/4.3% | 3 |
| transient | 1 | 0.603 | 0.588 | 0.015 | - | - | 0.779 | 0.788 | 0.092 | 1.19x | 12.0/19.4/21.5% | 1.7/4.8% | 3 |
| periodic | 1 | 0.453 | 0.444 | 0.008 | - | - | 0.572 | 0.624 | 0.056 | 1.08x | 11.0/17.5/19.4% | 1.6/4.0% | 3 |

> noise-profile=none: decode_failures 3

> noise-profile=temporal: decode_failures 13

> noise-profile=transient: decode_failures 10

> noise-profile=periodic: decode_failures 17

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.183 | 0.180 | 0.003 | - | - | 0.386 | 0.394 | 0.000 | 0.10x | 0.5/1.0/1.3% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| LONG_MODERATE | 1 | 0.688 | 0.669 | 0.019 | - | - | 0.803 | 0.897 | 0.370 | 3.23x | 40.2/53.6/61.7% | 4.6/11.1% | 3 |

> preset=SHORT_FAST: decode_failures 2

> preset=LONG_FAST: decode_failures 3

> preset=LONG_MODERATE: decode_failures 17

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.031 | 0.031 | 0.000 | - | - | 0.061 | 0.065 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.100 | 0.099 | 0.000 | - | - | 0.195 | 0.197 | 0.000 | 0.03x | 0.1/0.3/0.6% | 0.1/0.1% | 3 |
| LONG_FAST | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| LONG_TURBO | 1 | 0.416 | 0.404 | 0.011 | - | - | 0.549 | 0.553 | 0.085 | 1.24x | 10.3/16.8/18.8% | 1.8/3.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.611 | 0.608 | 0.003 | - | - | 0.663 | 0.663 | 0.102 | 1.64x | 16.2/23.6/26.1% | 2.4/6.0% | 3 |

> preset=LONG_FAST: decode_failures 3

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.564 | 0.550 | 0.013 | - | - | 0.729 | 0.748 | 0.075 | 1.17x | 11.9/19.4/21.5% | 1.7/4.6% | 3 |
| 10000 | 1 | 0.453 | 0.444 | 0.008 | - | - | 0.572 | 0.624 | 0.056 | 1.08x | 11.0/17.5/19.4% | 1.6/4.0% | 3 |
| 4000 | 1 | 0.252 | 0.250 | 0.003 | - | - | 0.311 | 0.378 | 0.029 | 0.96x | 9.9/15.3/16.7% | 1.5/3.0% | 3 |
| 2000 | 1 | 0.071 | 0.071 | 0.000 | - | - | 0.069 | 0.130 | 0.003 | 0.68x | 7.1/11.6/13.5% | 1.1/1.9% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 14

> noise-pulse-interval-ms=10000: decode_failures 17

> noise-pulse-interval-ms=4000: decode_failures 3

> slower: 3.41 s per simulated hour against 1.63 over 31 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.199 | 0.192 | 0.007 | - | - | 0.396 | 0.402 | 0.000 | 1.10x | 5.9/12.1/14.7% | 2.0/4.3% | 3 |
| 1.0 | 1 | 0.583 | 0.560 | 0.022 | - | - | 0.696 | 0.698 | 0.377 | 0.77x | 12.7/15.9/17.2% | 1.1/3.8% | 3 |

> duct-per-hour=0.0: decode_failures 2

> faster: 1.25 s per simulated hour against 2.56 over 31 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 22 | 1 | 0.195 | 0.195 | 0.000 | - | - | 0.233 | 0.237 | 0.000 | 1.10x | 5.9/12.2/14.4% | 2.0/4.1% | 3 |
| 17 | 1 | 0.097 | 0.097 | 0.001 | - | - | 0.101 | 0.184 | 0.000 | 0.73x | 3.0/6.1/10.6% | 1.1/2.9% | 3 |
| 14 | 1 | 0.047 | 0.046 | 0.000 | - | - | 0.117 | 0.146 | 0.000 | 0.47x | 1.5/3.3/5.2% | 0.7/1.7% | 3 |

> tx-power=30: decode_failures 3

> tx-power=14: decode_failures 5

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.978 | 0.978 | 0.510 | 2.05x | 17.8/27.4/33.9% | 1.5/5.1% | 3 |
| True | 1 | 0.863 | 0.856 | 0.007 | - | - | 0.977 | 0.977 | 0.502 | 2.42x | 21.0/31.7/38.7% | 1.8/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.612 | 0.601 | 0.011 | - | - | 0.779 | 0.782 | 0.108 | 1.25x | 12.3/20.6/23.7% | 1.8/4.7% | 3 |
| True | 1 | 0.652 | 0.643 | 0.009 | - | - | 0.787 | 0.794 | 0.145 | 1.28x | 12.7/20.6/24.0% | 1.8/4.7% | 3 |

> favourite-routers=False: decode_failures 1

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| random | 1 | 0.624 | 0.610 | 0.014 | - | - | 0.747 | 0.754 | 0.131 | 1.23x | 12.3/20.0/22.4% | 1.8/4.8% | 3 |

> hop-assign=centrality: decode_failures 3

> hop-assign=random: decode_failures 1

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.451 | 0.427 | 0.024 | - | - | 0.632 | 0.658 | 0.091 | 1.07x | 10.6/18.6/20.7% | 1.5/4.6% | 3 |
| 7 | 1 | 0.704 | 0.698 | 0.006 | - | - | 0.813 | 0.827 | 0.170 | 1.34x | 13.8/20.8/23.2% | 2.1/4.9% | 3 |
| 15 | 1 | 0.768 | 0.766 | 0.002 | - | - | 0.861 | 0.864 | 0.271 | 1.40x | 14.3/21.5/23.8% | 2.1/5.0% | 3 |
| 32 | 1 | 0.761 | 0.760 | 0.002 | - | - | 0.857 | 0.860 | 0.262 | 1.38x | 14.2/21.2/23.5% | 2.1/4.9% | 3 |

> hop-limit=3: decode_failures 18

> hop-limit=7: decode_failures 9

> slower: 3.74 s per simulated hour against 1.76 over 31 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.451 | 0.427 | 0.024 | - | - | 0.632 | 0.658 | 0.091 | 1.07x | 10.6/18.6/20.7% | 1.5/4.6% | 3 |
| 5 | 1 | 0.619 | 0.608 | 0.011 | - | - | 0.767 | 0.784 | 0.121 | 1.19x | 11.8/19.6/21.7% | 1.7/4.8% | 3 |
| 7 | 1 | 0.704 | 0.698 | 0.006 | - | - | 0.813 | 0.827 | 0.170 | 1.34x | 13.8/20.8/23.2% | 2.1/4.9% | 3 |

> hop-limit=3: decode_failures 18

> hop-limit=5: decode_failures 16

> hop-limit=7: decode_failures 9

> slower: 5.77 s per simulated hour against 2.03 over 31 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| KNOWN_ONLY | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.595 | 0.594 | 0.001 | - | - | 0.642 | 0.792 | 0.087 | 1.17x | 11.9/19.0/21.0% | 1.8/4.5% | 3 |

> rebroadcast-mode=ALL: decode_failures 3

> rebroadcast-mode=KNOWN_ONLY: decode_failures 3

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.451 | 0.427 | 0.024 | - | - | 0.632 | 0.658 | 0.091 | 1.07x | 10.6/18.6/20.7% | 1.5/4.6% | 3 |
| True | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> hop-spread=False: decode_failures 18

> hop-spread=True: decode_failures 3

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| BALANCED | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| STRICT | 1 | 0.490 | 0.490 | 0.000 | - | - | 0.613 | 0.700 | 0.052 | 1.32x | 13.5/21.8/23.9% | 2.0/5.3% | 3 |

> signature-policy=COMPATIBLE: decode_failures 3

> signature-policy=BALANCED: decode_failures 3

> signature-policy=STRICT: decode_failures 22

> slower: 4.18 s per simulated hour against 1.8 over 31 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| dm | 1 | 0.609 | 0.596 | 0.012 | - | - | 0.783 | 0.786 | 0.095 | 1.18x | 11.9/19.5/21.6% | 1.7/4.9% | 3 |

> advert-transport=broadcast: decode_failures 3

> advert-transport=dm: decode_failures 1

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.612 | 0.598 | 0.014 | - | - | 0.771 | 0.790 | 0.087 | 1.18x | 11.9/19.3/21.4% | 1.8/4.7% | 3 |
| local | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| time | 1 | 0.607 | 0.595 | 0.012 | - | - | 0.777 | 0.794 | 0.103 | 1.21x | 12.2/20.0/22.2% | 1.8/5.0% | 3 |
| window | 1 | 0.606 | 0.592 | 0.013 | - | - | 0.793 | 0.811 | 0.094 | 1.18x | 11.8/19.4/21.6% | 1.8/4.8% | 3 |

> bucket-mode=global: misdecodes 12

> bucket-mode=local: decode_failures 3

> bucket-mode=time: misdecodes 10

> bucket-mode=window: misdecodes 9

> bucket-mode=window: decode_failures 2

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.597 | 0.585 | 0.012 | - | - | 0.764 | 0.778 | 0.081 | 1.25x | 12.6/21.1/23.6% | 1.8/5.5% | 3 |
| 1800 | 1 | 0.607 | 0.595 | 0.012 | - | - | 0.777 | 0.794 | 0.103 | 1.21x | 12.2/20.0/22.2% | 1.8/5.0% | 3 |
| 3600 | 1 | 0.603 | 0.592 | 0.011 | - | - | 0.762 | 0.787 | 0.099 | 1.19x | 11.8/19.5/21.5% | 1.7/4.8% | 3 |

> time-bucket-s=600: misdecodes 67

> time-bucket-s=1800: misdecodes 10

> time-bucket-s=3600: misdecodes 2

> time-bucket-s=3600: decode_failures 10

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| interval | 1 | 0.595 | 0.581 | 0.015 | - | - | 0.755 | 0.767 | 0.084 | 1.45x | 14.1/27.0/29.8% | 1.9/7.1% | 3 |
| aimd | 1 | 0.600 | 0.593 | 0.008 | - | - | 0.715 | 0.804 | 0.083 | 1.19x | 12.1/19.6/22.1% | 1.8/4.8% | 3 |
| bucket+interval | 1 | 0.589 | 0.575 | 0.014 | - | - | 0.762 | 0.768 | 0.092 | 1.45x | 14.1/27.1/30.0% | 1.9/7.0% | 3 |

> trigger=bucket: decode_failures 3

> trigger=interval: misdecodes 6

> trigger=aimd: decode_failures 27

> trigger=bucket+interval: misdecodes 2

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.608 | 0.595 | 0.013 | - | - | 0.768 | 0.784 | 0.096 | 1.18x | 11.8/19.5/21.6% | 1.7/4.8% | 3 |
| 8 | 1 | 0.592 | 0.579 | 0.013 | - | - | 0.742 | 0.771 | 0.087 | 1.18x | 11.7/19.4/21.7% | 1.7/4.8% | 3 |
| 16 | 1 | 0.614 | 0.600 | 0.014 | - | - | 0.779 | 0.797 | 0.092 | 1.18x | 11.7/19.5/21.7% | 1.7/4.8% | 3 |
| 32 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 50 | 1 | 0.617 | 0.605 | 0.012 | - | - | 0.780 | 0.813 | 0.091 | 1.19x | 11.9/19.6/22.0% | 1.8/4.8% | 3 |

> capacity=4: decode_failures 81

> capacity=8: decode_failures 71

> capacity=16: decode_failures 67

> capacity=32: decode_failures 3

> capacity=50: decode_failures 23

> slower: 5.97 s per simulated hour against 1.7 over 31 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.608 | 0.595 | 0.013 | - | - | 0.768 | 0.784 | 0.096 | 1.18x | 11.8/19.5/21.6% | 1.7/4.8% | 3 |
| 8 | 1 | 0.592 | 0.579 | 0.013 | - | - | 0.742 | 0.771 | 0.087 | 1.18x | 11.7/19.4/21.7% | 1.7/4.8% | 3 |
| 16 | 1 | 0.614 | 0.600 | 0.014 | - | - | 0.779 | 0.797 | 0.092 | 1.18x | 11.7/19.5/21.7% | 1.7/4.8% | 3 |
| 32 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 50 | 1 | 0.617 | 0.605 | 0.012 | - | - | 0.780 | 0.813 | 0.091 | 1.19x | 11.9/19.6/22.0% | 1.8/4.8% | 3 |

> capacity=4: decode_failures 81

> capacity=8: decode_failures 71

> capacity=16: decode_failures 67

> capacity=32: decode_failures 3

> capacity=50: decode_failures 23

> slower: 4.29 s per simulated hour against 1.77 over 31 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.605 | 0.603 | 0.002 | - | - | 0.666 | 0.786 | 0.094 | 1.17x | 11.9/18.9/21.1% | 1.8/4.5% | 3 |
| 16 | 1 | 0.595 | 0.590 | 0.005 | - | - | 0.698 | 0.801 | 0.096 | 1.18x | 11.9/19.2/21.2% | 1.8/4.7% | 3 |
| 32 | 1 | 0.606 | 0.592 | 0.013 | - | - | 0.793 | 0.811 | 0.094 | 1.18x | 11.8/19.4/21.6% | 1.8/4.8% | 3 |

> capacity=8: misdecodes 1

> capacity=8: decode_failures 84

> capacity=16: misdecodes 1

> capacity=16: decode_failures 61

> capacity=32: misdecodes 9

> capacity=32: decode_failures 2

> slower: 3.35 s per simulated hour against 1.61 over 31 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.589 | 0.575 | 0.014 | - | - | 0.762 | 0.768 | 0.092 | 1.45x | 14.1/27.1/30.0% | 1.9/7.0% | 3 |
| 02-06 | 1 | 0.598 | 0.591 | 0.007 | - | - | 0.717 | 0.793 | 0.105 | 1.22x | 12.1/20.0/22.4% | 1.8/4.9% | 3 |
| 00-08 | 1 | 0.600 | 0.592 | 0.009 | - | - | 0.711 | 0.781 | 0.103 | 1.26x | 12.7/21.4/23.9% | 1.8/5.4% | 3 |

> catch-up-hours=: misdecodes 2

> catch-up-hours=02-06: decode_failures 33

> catch-up-hours=00-08: decode_failures 32

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.597 | 0.594 | 0.003 | - | - | 0.783 | 0.785 | 0.097 | 1.18x | 11.8/19.1/21.1% | 1.8/4.5% | 3 |
| 2 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 3 | 1 | 0.626 | 0.592 | 0.034 | - | - | 0.821 | 0.920 | 0.087 | 1.19x | 12.2/18.8/20.7% | 1.7/4.5% | 3 |
| 4 | 1 | 0.613 | 0.586 | 0.027 | - | - | 0.677 | 0.915 | 0.093 | 1.20x | 12.3/18.9/20.9% | 1.8/4.5% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=3: decode_failures 23

> hops-apart=4: decode_failures 26

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.597 | 0.594 | 0.003 | - | - | 0.783 | 0.785 | 0.097 | 1.18x | 11.8/19.1/21.1% | 1.8/4.5% | 3 |
| 2 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 3 | 1 | 0.626 | 0.592 | 0.034 | - | - | 0.821 | 0.920 | 0.087 | 1.19x | 12.2/18.8/20.7% | 1.7/4.5% | 3 |
| 4 | 1 | 0.613 | 0.586 | 0.027 | - | - | 0.677 | 0.915 | 0.093 | 1.20x | 12.3/18.9/20.9% | 1.8/4.5% | 3 |
| 5 | 1 | 0.610 | 0.582 | 0.028 | - | - | 0.666 | 0.916 | 0.089 | 1.22x | 12.5/19.2/21.2% | 1.9/4.6% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=3: decode_failures 23

> hops-apart=4: decode_failures 26

> hops-apart=5: decode_failures 24

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.609 | 0.597 | 0.012 | - | - | 0.760 | 0.796 | 0.077 | 1.20x | 11.9/19.7/21.9% | 1.8/4.8% | 3 |
| 30 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 120 | 1 | 0.614 | 0.603 | 0.011 | - | - | 0.773 | 0.797 | 0.107 | 1.20x | 12.0/19.7/21.9% | 1.7/4.8% | 3 |
| 600 | 1 | 0.604 | 0.591 | 0.013 | - | - | 0.772 | 0.788 | 0.099 | 1.18x | 11.8/19.3/21.7% | 1.7/4.7% | 3 |

> advert-jitter-s=1: decode_failures 26

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 31

> advert-jitter-s=600: decode_failures 31

> slower: 8.25 s per simulated hour against 1.77 over 31 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.609 | 0.597 | 0.012 | - | - | 0.760 | 0.796 | 0.077 | 1.20x | 11.9/19.7/21.9% | 1.8/4.8% | 3 |
| 30 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 120 | 1 | 0.614 | 0.603 | 0.011 | - | - | 0.773 | 0.797 | 0.107 | 1.20x | 12.0/19.7/21.9% | 1.7/4.8% | 3 |
| 600 | 1 | 0.604 | 0.591 | 0.013 | - | - | 0.772 | 0.788 | 0.099 | 1.18x | 11.8/19.3/21.7% | 1.7/4.7% | 3 |

> advert-jitter-s=1: decode_failures 26

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 31

> advert-jitter-s=600: decode_failures 31

> slower: 5.81 s per simulated hour against 1.77 over 31 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.604 | 0.603 | 0.001 | - | - | 0.329 | 0.736 | 0.093 | 1.17x | 11.8/18.7/20.6% | 1.8/4.3% | 3 |
| routers | 1 | 0.611 | 0.598 | 0.014 | - | - | 0.760 | 0.764 | 0.084 | 1.19x | 11.9/19.4/21.4% | 1.8/4.8% | 3 |
| alternate-routers | 1 | 0.608 | 0.597 | 0.011 | - | - | 0.793 | 0.795 | 0.106 | 1.18x | 11.8/19.3/21.3% | 1.8/4.6% | 3 |
| beside-router | 1 | 0.595 | 0.589 | 0.006 | - | - | 0.744 | 0.744 | 0.093 | 1.19x | 11.9/19.3/21.3% | 1.8/4.5% | 3 |
| random-clients | 1 | 0.607 | 0.593 | 0.014 | - | - | 0.666 | 0.739 | 0.101 | 1.19x | 12.0/19.0/20.7% | 1.7/4.4% | 3 |
| hops-apart | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> place=spread: decode_failures 2

> place=random-clients: decode_failures 16

> place=hops-apart: decode_failures 3

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.604 | 0.603 | 0.001 | - | - | 0.329 | 0.736 | 0.093 | 1.17x | 11.8/18.7/20.6% | 1.8/4.3% | 3 |
| routers | 1 | 0.611 | 0.598 | 0.014 | - | - | 0.760 | 0.764 | 0.084 | 1.19x | 11.9/19.4/21.4% | 1.8/4.8% | 3 |
| alternate-routers | 1 | 0.608 | 0.597 | 0.011 | - | - | 0.793 | 0.795 | 0.106 | 1.18x | 11.8/19.3/21.3% | 1.8/4.6% | 3 |
| beside-router | 1 | 0.595 | 0.589 | 0.006 | - | - | 0.744 | 0.744 | 0.093 | 1.19x | 11.9/19.3/21.3% | 1.8/4.5% | 3 |
| random-clients | 1 | 0.607 | 0.593 | 0.014 | - | - | 0.666 | 0.739 | 0.101 | 1.19x | 12.0/19.0/20.7% | 1.7/4.4% | 3 |
| hops-apart | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> place=spread: decode_failures 2

> place=random-clients: decode_failures 16

> place=hops-apart: decode_failures 3

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| broadcast | 1 | 0.639 | 0.586 | 0.053 | - | - | 0.744 | 0.782 | 0.136 | 1.25x | 12.3/21.0/23.5% | 1.8/5.1% | 3 |

> provide-transport=dm: decode_failures 3

> provide-transport=broadcast: decode_failures 19

> slower: 3.9 s per simulated hour against 1.8 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| heard | 1 | 0.598 | 0.586 | 0.012 | - | - | 0.760 | 0.781 | 0.084 | 1.20x | 12.0/19.5/21.7% | 1.8/4.7% | 3 |

> replay-ordering=tip: decode_failures 3

> replay-ordering=heard: misdecodes 4

> replay-ordering=heard: decode_failures 27

> slower: 4.94 s per simulated hour against 1.69 over 31 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.639 | 0.586 | 0.053 | - | - | 0.744 | 0.782 | 0.136 | 1.25x | 12.3/21.0/23.5% | 1.8/5.1% | 3 |
| heard | 1 | 0.640 | 0.581 | 0.059 | - | - | 0.748 | 0.781 | 0.144 | 1.28x | 12.7/21.4/23.9% | 1.8/5.1% | 3 |

> replay-ordering=tip: decode_failures 19

> replay-ordering=heard: decode_failures 15

> slower: 6.7 s per simulated hour against 1.77 over 31 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.608 | 0.601 | 0.007 | - | - | 0.725 | 0.794 | 0.084 | 1.19x | 11.8/19.5/21.6% | 1.7/4.8% | 3 |
| enum | 1 | 0.597 | 0.584 | 0.013 | - | - | 0.766 | 0.789 | 0.080 | 1.18x | 11.8/19.4/21.8% | 1.8/4.8% | 3 |
| hybrid | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> resolve=sketch: decode_failures 16

> resolve=hybrid: decode_failures 3

> slower: 3.38 s per simulated hour against 1.53 over 31 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.611 | 0.598 | 0.014 | - | - | 0.760 | 0.764 | 0.084 | 1.19x | 11.9/19.4/21.4% | 1.8/4.8% | 3 |
| 6 | 1 | 0.597 | 0.582 | 0.015 | - | - | 0.775 | 0.776 | 0.088 | 1.21x | 12.1/20.0/22.1% | 1.8/4.7% | 6 |

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.602 | 0.598 | 0.004 | - | - | 0.762 | 0.764 | 0.096 | 1.17x | 11.8/19.0/20.9% | 1.8/4.6% | 2 |
| 3 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 5 | 1 | 0.606 | 0.587 | 0.019 | - | - | 0.810 | 0.816 | 0.087 | 1.21x | 12.1/19.9/22.1% | 1.8/4.8% | 5 |
| 8 | 1 | 0.636 | 0.586 | 0.050 | - | - | 0.923 | 0.945 | 0.089 | 1.27x | 12.6/20.9/23.5% | 1.9/5.1% | 8 |

> servers=3: decode_failures 3

> servers=8: decode_failures 30

> slower: 6.61 s per simulated hour against 2.54 over 31 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.602 | 0.598 | 0.004 | - | - | 0.762 | 0.764 | 0.096 | 1.17x | 11.8/19.0/20.9% | 1.8/4.6% | 2 |
| 3 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 5 | 1 | 0.606 | 0.587 | 0.019 | - | - | 0.810 | 0.816 | 0.087 | 1.21x | 12.1/19.9/22.1% | 1.8/4.8% | 5 |
| 8 | 1 | 0.636 | 0.586 | 0.050 | - | - | 0.923 | 0.945 | 0.089 | 1.27x | 12.6/20.9/23.5% | 1.9/5.1% | 8 |

> servers=3: decode_failures 3

> servers=8: decode_failures 30

> slower: 6.71 s per simulated hour against 2.35 over 31 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| True | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |

> signed=False: decode_failures 3

> signed=True: decode_failures 3

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.615 | 0.606 | 0.009 | - | - | 0.759 | 0.805 | 0.052 | 1.10x | 11.1/18.1/20.1% | 1.6/4.4% | 3 |
| 1 | 1 | 0.599 | 0.589 | 0.010 | - | - | 0.736 | 0.778 | 0.093 | 1.08x | 10.9/17.8/19.7% | 1.6/4.3% | 3 |
| 2 | 1 | 0.607 | 0.596 | 0.011 | - | - | 0.789 | 0.805 | 0.070 | 1.11x | 11.1/18.2/20.3% | 1.6/4.5% | 3 |
| 4 | 1 | 0.619 | 0.606 | 0.013 | - | - | 0.811 | 0.823 | 0.100 | 1.11x | 11.2/18.4/20.5% | 1.6/4.5% | 3 |

> sr-retries=0: decode_failures 10

> sr-retries=1: decode_failures 14

> sr-retries=4: decode_failures 4

> slower: 4.15 s per simulated hour against 1.58 over 31 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.602 | 0.591 | 0.012 | - | - | 0.763 | 0.785 | 0.080 | 1.19x | 11.9/19.6/21.7% | 1.7/4.8% | 3 |
| 24 | 1 | 0.609 | 0.597 | 0.012 | - | - | 0.774 | 0.795 | 0.095 | 1.18x | 11.8/19.5/21.6% | 1.8/4.7% | 3 |
| 32 | 1 | 0.604 | 0.592 | 0.012 | - | - | 0.778 | 0.782 | 0.100 | 1.19x | 12.0/19.4/21.7% | 1.8/4.8% | 3 |
| 64 | 1 | 0.604 | 0.590 | 0.013 | - | - | 0.776 | 0.799 | 0.098 | 1.19x | 11.9/19.5/21.8% | 1.7/4.8% | 3 |

> short-id-bits=16: decode_failures 17

> short-id-bits=24: decode_failures 16

> short-id-bits=32: decode_failures 3

> short-id-bits=64: decode_failures 9

> slower: 5.13 s per simulated hour against 1.73 over 31 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.595 | 0.584 | 0.011 | - | - | 0.761 | 0.769 | 0.083 | 1.23x | 12.3/20.4/22.9% | 1.7/5.1% | 3 |
| 16 | 1 | 0.601 | 0.589 | 0.012 | - | - | 0.762 | 0.778 | 0.096 | 1.18x | 11.8/19.6/21.7% | 1.7/4.8% | 3 |
| 32 | 1 | 0.606 | 0.592 | 0.013 | - | - | 0.793 | 0.811 | 0.094 | 1.18x | 11.8/19.4/21.6% | 1.8/4.8% | 3 |

> window-size=8: misdecodes 80

> window-size=16: misdecodes 19

> window-size=32: misdecodes 9

> window-size=32: decode_failures 2

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.978 | 0.978 | 0.510 | 2.05x | 17.8/27.4/33.9% | 1.5/5.1% | 3 |
| True | 1 | 0.646 | 0.631 | 0.015 | - | - | 0.835 | 0.865 | 0.369 | 5.63x | 46.9/64.5/72.4% | 4.2/12.0% | 3 |

> no-congestion-scaling=True: decode_failures 75

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.342 | 0.337 | 0.004 | - | - | 0.707 | 0.708 | 0.065 | 4.66x | 11.5/23.9/34.3% | 1.6/5.4% | 3 |
| truesize | 1 | 0.374 | 0.370 | 0.004 | - | - | 0.739 | 0.739 | 0.070 | 2.59x | 6.1/16.2/23.8% | 0.8/4.2% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.978 | 0.979 | 0.542 | 2.10x | 18.2/27.7/34.1% | 1.5/5.1% | 3 |
| adaptive | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.978 | 0.978 | 0.510 | 2.05x | 17.8/27.4/33.9% | 1.5/5.1% | 3 |

