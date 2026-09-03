# Sweep blocks-2026-09-03-5856432

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 5856432 · seeds 5856432
- **blocks** 87 run
- **compute** 14.9 h of simulator time across every cell
- **generated** 2026-09-03T08:38:45+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>254 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 3
- AD-amplify-worst: amplify-worst=0.0: decode_failures 3
- AD-badrouters: role-placement=degree: decode_failures 7
- AD-badrouters: role-placement=inverse: decode_failures 14
- AD-badrouters: role-placement=random: decode_failures 18
- AD-badrouters: slower: 5.86 s per simulated hour against 2.1 over 13 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 7
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 7
- AD-nomute: role-mix=no-mute: decode_failures 2
- AD-siting: siting-mix=uniform: decode_failures 7
- AD-siting: siting-mix=local-typical: decode_failures 23
- AD-siting: slower: 3.75 s per simulated hour against 1.29 over 13 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=degree: decode_failures 60
- AD-worst: role-placement=inverse: decode_failures 75
- AD-worst: slower: 22.3 s per simulated hour against 3.86 over 13 prior run(s) - 5.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 29
- BL-control: slower: 4.71 s per simulated hour against 1.74 over 13 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 17
- DB-hotstore-stress: max-num-nodes=10: decode_failures 2
- DB-hotstore-stress: faster: 9.34 s per simulated hour against 22.6 over 13 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DB-platform: platform-mix=constrained: decode_failures 24
- DB-warm: warm-num-nodes=0: decode_failures 46
- DB-warm: warm-num-nodes=25: decode_failures 46
- DB-warm: warm-num-nodes=100: decode_failures 46
- DB-warm: warm-num-nodes=2000: decode_failures 46
- DG-burst: burst-loss=0.0: decode_failures 3
- DG-burst: burst-loss=0.1: decode_failures 37
- DG-burst: burst-loss=0.2: decode_failures 27
- DG-burst: burst-loss=0.3: decode_failures 29
- DG-loss: extra-loss=0.0: decode_failures 3
- DG-loss: extra-loss=0.1: decode_failures 4
- DG-loss: extra-loss=0.2: decode_failures 23
- DG-loss: extra-loss=0.3: decode_failures 26
- DG-loss: slower: 6.67 s per simulated hour against 2.18 over 13 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 3
- DG-outage: burst-loss=0.1: decode_failures 17
- DG-outage: burst-loss=0.2: decode_failures 21
- DG-outage: burst-loss=0.3: decode_failures 26
- DM-mode: dm-mode=flood-only: decode_failures 39
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 10
- DM-mode: dm-mode=m4-early-flood: decode_failures 10
- DM-mode: slower: 7.97 s per simulated hour against 2.7 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 3
- FW-mixed-26: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.5: decode_failures 1
- FW-signing-cost: profile-flag=signing=true: decode_failures 3
- FW-versions: profile=2.8: decode_failures 3
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 26
- LD-chatty: broadcast-interval-s=3600: decode_failures 1
- LD-chatty: broadcast-interval-s=900: decode_failures 14
- LD-chatty: broadcast-interval-s=300: decode_failures 30
- LD-diurnal: diurnal=sinusoid: decode_failures 3
- LD-diurnal: diurnal=commuter: decode_failures 3
- LD-diurnal: slower: 3.44 s per simulated hour against 1.58 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 14
- LD-interval: broadcast-interval-s=3600: decode_failures 1
- LD-interval: broadcast-interval-s=43200: decode_failures 1
- LD-interval: slower: 3.72 s per simulated hour against 1.4 over 13 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 3
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 29
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 8
- LD-traceroute: slower: 5.08 s per simulated hour against 2.1 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 46
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 50
- MS-density: nodes=40: decode_failures 5
- MS-density: nodes=60: decode_failures 3
- MS-density: nodes=150: decode_failures 2
- MS-hopscale: nodes=60: decode_failures 3
- MS-hopscale: nodes=500: decode_failures 66
- MS-oversubscribed: nodes=500: decode_failures 27
- MS-roles-fav: role-mix=legacy-default: decode_failures 2
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 1
- MS-roles: role-mix=legacy-default: decode_failures 2
- MS-roles: role-mix=baymesh-2026-08: decode_failures 7
- MS-roles: slower: 4.15 s per simulated hour against 1.73 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 3
- MS-router-late: router-late-fraction=0.05: decode_failures 3
- MS-router-late: router-late-fraction=0.2: decode_failures 1
- MS-router-late: slower: 3.54 s per simulated hour against 1.76 over 13 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=uniform: decode_failures 3
- MS-siting: siting-mix=local-typical: decode_failures 14
- MS-size: nodes=40: decode_failures 14
- MS-size: nodes=60: decode_failures 3
- MS-size: nodes=150: decode_failures 2
- MS-stretch: stretch=1.0: decode_failures 3
- MS-stretch: stretch=1.25: decode_failures 26
- MS-stretch: stretch=1.5: decode_failures 17
- MS-stretch: stretch=2.0: decode_failures 5
- MS-stretch: slower: 5 s per simulated hour against 1.89 over 13 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-topology: topology=uniform: decode_failures 3
- PR-crladder: coding-rate-ladder=False: decode_failures 10
- PR-crladder: coding-rate-ladder=True: decode_failures 20
- PR-crladder: slower: 7.79 s per simulated hour against 2.75 over 13 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 20
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 15
- PR-dmmode-cr: slower: 7.6 s per simulated hour against 2.5 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 3
- PR-repeats: extra-repeats=False: decode_failures 3
- PR-repeats: extra-repeats=True: decode_failures 4
- PR-repeats: slower: 3.77 s per simulated hour against 1.68 over 13 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=SHORT_TURBO: decode_failures 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 14
- RF-bw500: preset=LONG_TURBO: decode_failures 6
- RF-bw500: slower: 3.82 s per simulated hour against 1.88 over 13 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-duct: duct-per-hour=0.0: decode_failures 3
- RF-duct: duct-per-hour=0.25: decode_failures 6
- RF-duct: slower: 3.69 s per simulated hour against 1.76 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=SHORT_FAST: decode_failures 1
- RF-eu-presets: preset=LONG_FAST: decode_failures 3
- RF-eu-presets: preset=LITE_FAST: decode_failures 14
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 2
- RF-noise: noise-profile=none: decode_failures 3
- RF-noise: noise-profile=temporal: decode_failures 25
- RF-noise: noise-profile=transient: decode_failures 3
- RF-noise: noise-profile=periodic: decode_failures 20
- RF-preset: preset=SHORT_FAST: decode_failures 1
- RF-preset: preset=LONG_FAST: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 22
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 1
- RF-preset-turbo: preset=LONG_FAST: decode_failures 3
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 6
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 7
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 5
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 20
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 7
- RF-pulse: slower: 3.61 s per simulated hour against 1.6 over 13 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 17
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 1
- RF-stretch-duct: slower: 4.12 s per simulated hour against 1.9 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=30: decode_failures 3
- RF-txpower: tx-power=17: decode_failures 1
- RT-favourites: favourite-routers=False: decode_failures 1
- RT-favourites: favourite-routers=True: decode_failures 3
- RT-favourites: slower: 3.83 s per simulated hour against 1.69 over 13 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 3
- RT-hopassign: hop-assign=random: decode_failures 7
- RT-hopassign: slower: 4.52 s per simulated hour against 1.77 over 13 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hoplimit: hop-limit=3: decode_failures 25
- RT-hopspread: hop-limit=3: decode_failures 25
- RT-hopspread: hop-limit=5: decode_failures 1
- RT-hopspread: slower: 5.25 s per simulated hour against 2.03 over 13 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 3
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 25
- RT-spread: hop-spread=True: decode_failures 3
- RT-spread: slower: 6.84 s per simulated hour against 2.08 over 13 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 3
- SC-signing: signature-policy=BALANCED: decode_failures 3
- SC-signing: signature-policy=STRICT: decode_failures 26
- SC-signing: slower: 5.97 s per simulated hour against 1.87 over 13 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 3
- SF-advert-transport: slower: 4.16 s per simulated hour against 1.85 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 8
- SF-bucket-mode: bucket-mode=local: decode_failures 3
- SF-bucket-mode: bucket-mode=time: misdecodes 6
- SF-bucket-mode: bucket-mode=time: decode_failures 5
- SF-bucket-mode: bucket-mode=window: misdecodes 7
- SF-bucket-mode: slower: 3.29 s per simulated hour against 1.56 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-time: time-bucket-s=600: misdecodes 68
- SF-bucket-time: time-bucket-s=1800: misdecodes 6
- SF-bucket-time: time-bucket-s=1800: decode_failures 5
- SF-bucket-time: time-bucket-s=3600: misdecodes 2
- SF-bucket-time: time-bucket-s=3600: decode_failures 12
- SF-bucket-time: slower: 3.98 s per simulated hour against 1.62 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-cadence: trigger=bucket: decode_failures 3
- SF-cadence: trigger=interval: misdecodes 6
- SF-cadence: trigger=interval: decode_failures 25
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 23
- SF-cadence: trigger=bucket+interval: misdecodes 8
- SF-cadence: slower: 8.98 s per simulated hour against 2.75 over 13 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 94
- SF-capacity-local: capacity=8: decode_failures 98
- SF-capacity-local: capacity=16: decode_failures 91
- SF-capacity-local: capacity=32: decode_failures 3
- SF-capacity-local: slower: 3.94 s per simulated hour against 1.77 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity: capacity=4: decode_failures 94
- SF-capacity: capacity=8: decode_failures 98
- SF-capacity: capacity=16: decode_failures 91
- SF-capacity: capacity=32: decode_failures 3
- SF-capacity: slower: 4.01 s per simulated hour against 1.69 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-window: capacity=8: decode_failures 127
- SF-capacity-window: capacity=16: misdecodes 1
- SF-capacity-window: capacity=16: decode_failures 74
- SF-capacity-window: capacity=32: misdecodes 7
- SF-capacity-window: slower: 4.06 s per simulated hour against 1.61 over 13 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 8
- SF-catchup: catch-up-hours=02-06: decode_failures 46
- SF-catchup: catch-up-hours=00-08: decode_failures 47
- SF-hops-flat: hops-apart=2: decode_failures 3
- SF-hops-flat: hops-apart=3: decode_failures 29
- SF-hops-flat: hops-apart=4: decode_failures 27
- SF-hops-spread: hops-apart=2: decode_failures 3
- SF-hops-spread: hops-apart=3: decode_failures 29
- SF-hops-spread: hops-apart=4: decode_failures 27
- SF-hops-spread: hops-apart=5: decode_failures 34
- SF-jitter-global: advert-jitter-s=1: decode_failures 3
- SF-jitter-global: advert-jitter-s=30: decode_failures 3
- SF-jitter-global: advert-jitter-s=120: decode_failures 9
- SF-jitter-global: advert-jitter-s=600: decode_failures 39
- SF-jitter-global: slower: 7.28 s per simulated hour against 1.74 over 13 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 3
- SF-jitter-local: advert-jitter-s=30: decode_failures 3
- SF-jitter-local: advert-jitter-s=120: decode_failures 9
- SF-jitter-local: advert-jitter-s=600: decode_failures 39
- SF-jitter-local: slower: 6.94 s per simulated hour against 1.77 over 13 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 23
- SF-place-flat: place=routers: decode_failures 17
- SF-place-flat: place=beside-router: decode_failures 5
- SF-place-flat: place=random-clients: decode_failures 29
- SF-place-flat: place=hops-apart: decode_failures 3
- SF-place-flat: slower: 5.42 s per simulated hour against 2.56 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-spread: place=spread: decode_failures 23
- SF-place-spread: place=routers: decode_failures 17
- SF-place-spread: place=beside-router: decode_failures 5
- SF-place-spread: place=random-clients: decode_failures 29
- SF-place-spread: place=hops-apart: decode_failures 3
- SF-provide-transport: provide-transport=dm: decode_failures 3
- SF-provide-transport: provide-transport=broadcast: decode_failures 15
- SF-provide-transport: slower: 5.72 s per simulated hour against 1.93 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 15
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 4
- SF-replay-order-broadcast: slower: 5.86 s per simulated hour against 1.57 over 13 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 3
- SF-replay-order: replay-ordering=heard: misdecodes 4
- SF-resolve: resolve=sketch: decode_failures 4
- SF-resolve: resolve=hybrid: decode_failures 3
- SF-servers-allrouters: servers=3: decode_failures 17
- SF-servers-allrouters: servers=6: decode_failures 7
- SF-servers-allrouters: slower: 6.94 s per simulated hour against 1.85 over 13 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=2: decode_failures 2
- SF-servers-flat: servers=3: decode_failures 3
- SF-servers-flat: servers=8: decode_failures 1
- SF-servers-flat: slower: 6.5 s per simulated hour against 2.6 over 13 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=2: decode_failures 2
- SF-servers-spread: servers=3: decode_failures 3
- SF-servers-spread: servers=8: decode_failures 1
- SF-servers-spread: slower: 6.49 s per simulated hour against 2.29 over 13 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 3
- SF-signed: signed=True: decode_failures 3
- SF-signed: slower: 3.51 s per simulated hour against 1.74 over 13 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 16
- SF-sr-retries: sr-retries=1: decode_failures 7
- SF-sr-retries: slower: 5 s per simulated hour against 1.67 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 2
- SF-width: short-id-bits=24: decode_failures 3
- SF-width: short-id-bits=32: decode_failures 3
- SF-width: short-id-bits=64: decode_failures 1
- SF-width: slower: 3.79 s per simulated hour against 1.77 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 83
- SF-window-size: window-size=16: misdecodes 31
- SF-window-size: window-size=32: misdecodes 7
- TH-congestion: no-congestion-scaling=True: decode_failures 60

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 22.3 | 3.86 | 5.77x | 13 |
| `SF-jitter-global` | 7.28 | 1.74 | 4.18x | 13 |
| `SF-jitter-local` | 6.94 | 1.77 | 3.93x | 13 |
| `SF-servers-allrouters` | 6.94 | 1.85 | 3.75x | 13 |
| `SF-replay-order-broadcast` | 5.86 | 1.57 | 3.74x | 13 |
| `RT-spread` | 6.84 | 2.08 | 3.29x | 13 |
| `SF-cadence` | 8.98 | 2.75 | 3.26x | 13 |
| `SC-signing` | 5.97 | 1.87 | 3.19x | 13 |
| `DG-loss` | 6.67 | 2.18 | 3.06x | 13 |
| `PR-dmmode-cr` | 7.6 | 2.5 | 3.04x | 13 |
| `SF-sr-retries` | 5 | 1.67 | 2.99x | 13 |
| `SF-provide-transport` | 5.72 | 1.93 | 2.97x | 13 |
| `DM-mode` | 7.97 | 2.7 | 2.95x | 13 |
| `AD-siting` | 3.75 | 1.29 | 2.91x | 13 |
| `SF-servers-spread` | 6.49 | 2.29 | 2.84x | 13 |
| `PR-crladder` | 7.79 | 2.75 | 2.83x | 13 |
| `AD-badrouters` | 5.86 | 2.1 | 2.80x | 13 |
| `BL-control` | 4.71 | 1.74 | 2.71x | 13 |
| `LD-interval` | 3.72 | 1.4 | 2.66x | 13 |
| `MS-stretch` | 5 | 1.89 | 2.65x | 13 |
| `RT-hopspread` | 5.25 | 2.03 | 2.59x | 13 |
| `RT-hopassign` | 4.52 | 1.77 | 2.55x | 13 |
| `SF-capacity-window` | 4.06 | 1.61 | 2.52x | 13 |
| `SF-servers-flat` | 6.5 | 2.6 | 2.50x | 13 |
| `SF-bucket-time` | 3.98 | 1.62 | 2.45x | 13 |
| `LD-traceroute` | 5.08 | 2.1 | 2.42x | 13 |
| `MS-roles` | 4.15 | 1.73 | 2.39x | 13 |
| `SF-capacity` | 4.01 | 1.69 | 2.38x | 13 |
| `RT-favourites` | 3.83 | 1.69 | 2.26x | 13 |
| `RF-pulse` | 3.61 | 1.6 | 2.25x | 13 |
| `PR-repeats` | 3.77 | 1.68 | 2.25x | 13 |
| `SF-advert-transport` | 4.16 | 1.85 | 2.25x | 13 |
| `SF-capacity-local` | 3.94 | 1.77 | 2.23x | 13 |
| `LD-diurnal` | 3.44 | 1.58 | 2.18x | 13 |
| `RF-stretch-duct` | 4.12 | 1.9 | 2.17x | 13 |
| `SF-width` | 3.79 | 1.77 | 2.14x | 13 |
| `SF-place-flat` | 5.42 | 2.56 | 2.12x | 13 |
| `SF-bucket-mode` | 3.29 | 1.56 | 2.10x | 13 |
| `RF-duct` | 3.69 | 1.76 | 2.09x | 13 |
| `RF-bw500` | 3.82 | 1.88 | 2.04x | 13 |
| `MS-router-late` | 3.54 | 1.76 | 2.02x | 13 |
| `SF-signed` | 3.51 | 1.74 | 2.01x | 13 |
| `RF-eu-presets` | 3.9 | 2.03 | 1.92x | 13 |
| `SF-hops-flat` | 6.18 | 3.23 | 1.91x | 13 |
| `DB-platform` | 4.92 | 2.58 | 1.91x | 13 |
| `SF-place-spread` | 5.36 | 2.84 | 1.89x | 13 |
| `FW-signing-cost` | 2.97 | 1.58 | 1.87x | 13 |
| `SF-resolve` | 2.85 | 1.53 | 1.87x | 13 |
| `RT-rebroadcast` | 2.85 | 1.59 | 1.80x | 13 |
| `MS-siting` | 2.81 | 1.62 | 1.73x | 13 |
| `FW-mixed` | 2.82 | 1.66 | 1.70x | 13 |
| `RT-hoplimit` | 3.09 | 1.82 | 1.70x | 13 |
| `RF-noise` | 8.25 | 4.91 | 1.68x | 13 |
| `MS-roles-fav` | 2.93 | 1.75 | 1.67x | 13 |
| `SF-replay-order` | 2.98 | 1.79 | 1.67x | 13 |
| `LD-chatty` | 7.42 | 4.58 | 1.62x | 13 |
| `AD-amplify-worst` | 2.68 | 1.69 | 1.58x | 13 |
| `AD-nomute` | 3.6 | 2.32 | 1.55x | 13 |
| `DB-hotstore` | 3.95 | 2.57 | 1.54x | 13 |
| `AD-flooding` | 3.94 | 2.57 | 1.53x | 13 |
| `RF-preset` | 4.51 | 2.94 | 1.53x | 13 |
| `MS-hopscale` | 11.7 | 18.1 | 0.65x | 13 |
| `LD-traceroute-small` | 22.6 | 36.6 | 0.62x | 13 |
| `MS-oversubscribed` | 10.4 | 18.6 | 0.56x | 13 |
| `TH-congestion-input` | 6.24 | 11.2 | 0.56x | 13 |
| `DB-hotstore-stress` | 9.34 | 22.6 | 0.41x | 13 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.940 | 0.940 | 0.668 → 0.678 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.038 → 0.940 | 0.902 | 0.024 → 0.675 | 52x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.040 → 0.940 | 0.900 | 0.038 → 0.675 | 52x advert_bytes | down | 4 |
| `BL-control` | protocol | **held** | 0 → 0.884 | 0.884 | 0.678 → 0.682 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **text** | 0.152 → 0.973 | 0.821 | 0.150 → 0.972 | 7.1x sr_bytes | up | 4 |
| `MS-stretch` | stretch | **held** | 0.121 → 0.940 | 0.819 | 0.060 → 0.675 | 8.8x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.065 → 0.867 | 0.802 | 0.071 → 0.614 | 3.4e+02x sr_airtime | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.261 → 0.940 | 0.679 | 0.146 → 0.675 | 4.9x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.261 → 0.940 | 0.679 | 0.146 → 0.695 | 5.3x sr_airtime | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.225 → 0.848 | 0.623 | 0.062 → 0.570 | 7.6x sr_bytes | down | 3 |
| `MS-hopscale` | nodes | **held** | 0.351 → 0.940 | 0.589 | 0.189 → 0.675 | 7.2x bytes_on_air | down | 4 |
| `RF-bw500` | preset | **held** | 0.207 → 0.742 | 0.535 | 0.082 → 0.556 | 3.9x advert_bytes | up | 3 |
| `MS-topology` | topology | **text** | 0.427 → 0.925 | 0.498 | 0.419 → 0.924 | 4.3x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.475 → 0.905 | 0.430 | 0.467 → 0.899 | 7.6x sr_airtime | up | 5 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.210 → 0.640 | 0.430 | 0.205 → 0.614 | 2.5x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **held** | 0.531 → 0.940 | 0.409 | 0.350 → 0.675 | 1.8x advert_bytes | down | 4 |
| `DG-burst` | burst-loss | **held** | 0.556 → 0.940 | 0.385 | 0.353 → 0.675 | 1.7x advert_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.193 → 0.555 | 0.362 | 0.191 → 0.544 | 4.3x bytes_on_air | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.535 → 0.878 | 0.343 | 0.501 → 0.873 | 2.7x sr_bytes | up | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.629 → 0.968 | 0.339 | 0.423 → 0.725 | 8.5x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.500 → 0.837 | 0.336 | 0.490 → 0.828 | 9.2x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.617 → 0.940 | 0.323 | 0.675 → 0.685 | 3.5x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.617 → 0.940 | 0.323 | 0.675 → 0.685 | 3.5x sr_bytes | up | 6 |
| `RF-noise` | noise-profile | **held** | 0.651 → 0.940 | 0.289 | 0.498 → 0.675 | 1.5x advert_bytes | down | 4 |
| `MS-size` | nodes | **held** | 0.655 → 0.940 | 0.285 | 0.459 → 0.714 | 3.9x sr_bytes | down | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.535 → 0.805 | 0.269 | 0.501 → 0.793 | 1.9x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.701 → 0.953 | 0.251 | 0.675 → 0.947 | 2.9x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.653 → 0.891 | 0.238 | 0.640 → 0.880 | 4.6x sr_airtime | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.725 → 0.940 | 0.215 | 0.675 → 0.679 | 38x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.599 → 0.813 | 0.214 | 0.570 → 0.805 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.599 → 0.813 | 0.214 | 0.570 → 0.805 | 2.2x bytes_on_air | up | 3 |
| `DG-loss` | extra-loss | **held** | 0.732 → 0.940 | 0.208 | 0.507 → 0.675 | 1.3x advert_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.736 → 0.940 | 0.204 | 0.675 → 0.683 | 3.1x sr_bytes | down | 5 |
| `SF-servers-flat` | servers | **held** | 0.766 → 0.965 | 0.199 | 0.666 → 0.676 | 9.3x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.766 → 0.965 | 0.199 | 0.666 → 0.676 | 9.3x sr_bytes | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.701 → 0.900 | 0.199 | 0.675 → 0.892 | 2.5x sr_bytes | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.753 → 0.940 | 0.187 | 0.675 → 0.683 | 3.1x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.751 → 0.937 | 0.185 | 0.682 → 0.692 | 8.5x sr_bytes | up | 3 |
| `SC-signing` | signature-policy | **held** | 0.759 → 0.940 | 0.181 | 0.523 → 0.675 | 1.4x sr_airtime | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.701 → 0.880 | 0.179 | 0.675 → 0.850 | 1.7x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.535 → 0.701 | 0.166 | 0.501 → 0.675 | 1.4x sr_bytes | up | 2 |
| `DB-hotstore` | max-num-nodes | **held** | 0.780 → 0.937 | 0.157 | 0.607 → 0.737 | 2.1x sr_airtime | up | 4 |
| `SF-cadence` | trigger | **held** | 0.788 → 0.940 | 0.152 | 0.644 → 0.686 | 13x advert_bytes | down | 4 |
| `DB-platform` | platform-mix | **held** | 0.805 → 0.937 | 0.132 | 0.609 → 0.737 | 2x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.308 → 0.421 | 0.113 | 0.216 → 0.317 | 3.9x sr_airtime | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.701 → 0.807 | 0.106 | 0.675 → 0.797 | 2x bytes_on_air | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.668 → 0.772 | 0.104 | 0.639 → 0.754 | 5.9x sr_airtime | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.701 → 0.804 | 0.103 | 0.675 → 0.795 | 2.1x bytes_on_air | up | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.827 → 0.918 | 0.091 | 0.650 → 0.677 | 8.7x advert_bytes | down | 3 |
| `MS-roles` | role-mix | **text** | 0.599 → 0.689 | 0.090 | 0.570 → 0.668 | 1.2x bytes_on_air | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.861 → 0.944 | 0.083 | 0.668 → 0.685 | 2.4x sr_bytes | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.701 → 0.783 | 0.082 | 0.668 → 0.675 | 4.1x sr_airtime | up | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.863 → 0.940 | 0.078 | 0.663 → 0.674 | 1.2x sr_bytes | up | 4 |
| `FW-versions` | profile | **text** | 0.701 → 0.773 | 0.072 | 0.675 → 0.766 | 3.4x bytes_on_air | down | 5 |
| `DM-mode` | dm-mode | **held** | 0.794 → 0.865 | 0.071 | 0.638 → 0.647 | 1.3x sr_bytes | up | 3 |
| `FW-firmware` | profile | **text** | 0.701 → 0.770 | 0.069 | 0.675 → 0.761 | 3.3x bytes_on_air | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.641 → 0.710 | 0.069 | 0.618 → 0.691 | 1.1x advert_bytes | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.601 → 0.663 | 0.063 | 0.590 → 0.651 | 1.3x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.701 → 0.760 | 0.059 | 0.675 → 0.739 | 3.2x bytes_on_air | down | 2 |
| `AD-badrouters` | role-placement | **text** | 0.599 → 0.655 | 0.056 | 0.570 → 0.628 | 1.3x sr_bytes | up | 3 |
| `RT-hopassign` | hop-assign | **held** | 0.885 → 0.940 | 0.055 | 0.645 → 0.675 | 1.1x sr_bytes | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.889 → 0.940 | 0.051 | 0.633 → 0.683 | 1.4x sr_airtime | down | 4 |
| `AD-worst` | role-placement | **text** | 0.697 → 0.745 | 0.048 | 0.680 → 0.734 | 1.1x bytes_on_air | down | 2 |
| `SF-capacity` | capacity | **held** | 0.894 → 0.940 | 0.046 | 0.667 → 0.685 | 5.5x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.894 → 0.940 | 0.046 | 0.667 → 0.685 | 5.5x advert_bytes | up | 5 |
| `TH-congestion-input` | congestion-input | **held** | 0.418 → 0.456 | 0.038 | 0.315 → 0.348 | 2x sr_airtime | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.700 → 0.732 | 0.032 | 0.675 → 0.713 | 1.3x bytes_on_air | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.925 → 0.950 | 0.025 | 0.674 → 0.685 | 3x advert_bytes | down | 4 |
| `SF-resolve` | resolve | **held** | 0.918 → 0.940 | 0.022 | 0.675 → 0.680 | 5.9x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **held** | 0.919 → 0.938 | 0.019 | 0.685 → 0.686 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.915 → 0.933 | 0.018 | 0.671 → 0.684 | 5.2x advert_bytes | down | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.893 → 0.910 | 0.017 | 0.660 → 0.668 | 1x sr_airtime | up | 2 |
| `LD-diurnal` | diurnal | **text** | 0.701 → 0.718 | 0.017 | 0.675 → 0.697 | 1.4x sr_bytes | down | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.847 → 0.863 | 0.016 | 0.648 → 0.652 | 1.1x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.875 → 0.891 | 0.016 | 0.862 → 0.880 | 1.2x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.701 → 0.717 | 0.015 | 0.675 → 0.695 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.925 → 0.940 | 0.015 | 0.675 → 0.682 | 2.6x advert_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.926 → 0.940 | 0.014 | 0.675 → 0.682 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.926 → 0.940 | 0.014 | 0.675 → 0.682 | 1.1x sr_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.694 → 0.701 | 0.007 | 0.673 → 0.675 | 2.1x sr_airtime | down | 2 |
| `SF-window-size` | window-size | **text** | 0.706 → 0.712 | 0.006 | 0.680 → 0.685 | 4x advert_bytes | down | 3 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.948 → 0.952 | 0.004 | 0.880 → 0.880 | 1x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.647 → 0.652 | 0.004 | 0.647 → 0.652 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.891 → 0.894 | 0.003 | 0.880 → 0.881 | 1x bytes_on_air | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.701 → 0.704 | 0.003 | 0.675 → 0.680 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| sprinkled | 1 | 0.870 | 0.862 | 0.007 | - | - | 0.947 | 0.947 | 0.539 | 1.27x | 16.7/21.5/23.0% | 2.1/5.4% | 3 |
| arms-race | 1 | 0.953 | 0.947 | 0.006 | - | - | 0.982 | 0.982 | 0.873 | 1.17x | 23.4/29.4/32.5% | 1.5/5.2% | 3 |

> amplifier-mix=none: decode_failures 3

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.1 | 1 | 0.804 | 0.793 | 0.011 | - | - | 0.924 | 0.928 | 0.616 | 1.30x | 15.2/20.1/24.5% | 2.0/4.2% | 3 |
| 0.3 | 1 | 0.900 | 0.892 | 0.008 | - | - | 0.955 | 0.958 | 0.703 | 1.05x | 18.1/22.1/26.1% | 1.4/4.9% | 3 |

> amplify-worst=0.0: decode_failures 3

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.599 | 0.570 | 0.029 | - | - | 0.848 | 0.868 | 0.191 | 1.14x | 10.9/19.4/23.5% | 1.9/4.4% | 3 |
| inverse | 1 | 0.609 | 0.585 | 0.024 | - | - | 0.853 | 0.883 | 0.247 | 1.09x | 10.2/14.3/16.5% | 2.0/3.4% | 3 |
| random | 1 | 0.655 | 0.628 | 0.027 | - | - | 0.858 | 0.884 | 0.427 | 1.18x | 11.0/16.0/19.9% | 2.0/4.3% | 3 |

> role-placement=degree: decode_failures 7

> role-placement=inverse: decode_failures 14

> role-placement=random: decode_failures 18

> slower: 5.86 s per simulated hour against 2.1 over 13 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.599 | 0.570 | 0.029 | - | - | 0.848 | 0.868 | 0.191 | 1.14x | 10.9/19.4/23.5% | 1.9/4.4% | 3 |
| all-routers | 1 | 0.813 | 0.805 | 0.008 | - | - | 0.955 | 0.958 | 0.607 | 2.51x | 22.7/31.2/34.6% | 4.1/5.3% | 3 |

> role-mix=baymesh-2026-08: decode_failures 7

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.599 | 0.570 | 0.029 | - | - | 0.848 | 0.868 | 0.191 | 1.14x | 10.9/19.4/23.5% | 1.9/4.4% | 3 |
| no-mute | 1 | 0.721 | 0.702 | 0.019 | - | - | 0.932 | 0.944 | 0.362 | 1.31x | 12.5/17.7/20.8% | 2.1/4.3% | 3 |
| all-routers | 1 | 0.813 | 0.805 | 0.008 | - | - | 0.955 | 0.958 | 0.607 | 2.51x | 22.7/31.2/34.6% | 4.1/5.3% | 3 |

> role-mix=baymesh-2026-08: decode_failures 7

> role-mix=no-mute: decode_failures 2

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.599 | 0.570 | 0.029 | - | - | 0.848 | 0.868 | 0.191 | 1.14x | 10.9/19.4/23.5% | 1.9/4.4% | 3 |
| local-typical | 1 | 0.542 | 0.527 | 0.015 | - | - | 0.793 | 0.843 | 0.000 | 1.21x | 9.4/16.0/21.5% | 2.1/5.3% | 3 |
| basement-heavy | 1 | 0.063 | 0.062 | 0.001 | - | - | 0.225 | 0.226 | 0.000 | 0.52x | 0.6/9.8/15.1% | 0.3/3.1% | 3 |

> siting-mix=uniform: decode_failures 7

> siting-mix=local-typical: decode_failures 23

> slower: 3.75 s per simulated hour against 1.29 over 13 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.745 | 0.734 | 0.011 | - | - | 0.889 | 0.912 | 0.000 | 2.49x | 14.5/25.1/31.5% | 1.9/5.6% | 3 |
| inverse | 1 | 0.697 | 0.680 | 0.017 | - | - | 0.853 | 0.905 | 0.000 | 2.32x | 13.4/21.9/29.5% | 1.9/3.6% | 3 |

> role-placement=degree: decode_failures 60

> role-placement=inverse: decode_failures 75

> slower: 22.3 s per simulated hour against 3.86 over 13 prior run(s) - 5.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.678 | 0.678 | 0.000 | - | - | 0 | 0.000 | 0.446 | 1.30x | 12.3/18.8/22.3% | 2.0/4.6% | 3 |
| sr | 1 | 0.725 | 0.682 | 0.043 | - | - | 0.884 | 0.968 | 0.470 | 1.35x | 12.7/19.3/23.1% | 2.1/4.9% | 3 |

> protocol=sr: decode_failures 29

> slower: 4.71 s per simulated hour against 1.74 over 13 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.624 | 0.607 | 0.017 | - | - | 0.780 | 0.870 | 0.418 | 2.84x | 26.7/44.8/52.7% | 4.2/8.5% | 3 |
| 100 | 1 | 0.754 | 0.737 | 0.017 | - | - | 0.937 | 0.939 | 0.500 | 1.56x | 14.6/24.9/29.8% | 2.3/4.7% | 3 |
| 120 | 1 | 0.754 | 0.737 | 0.017 | - | - | 0.937 | 0.939 | 0.500 | 1.56x | 14.6/24.9/29.8% | 2.3/4.7% | 3 |
| 250 | 1 | 0.754 | 0.737 | 0.017 | - | - | 0.937 | 0.939 | 0.500 | 1.56x | 14.6/24.9/29.8% | 2.3/4.7% | 3 |

> max-num-nodes=10: decode_failures 17

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.219 | 0.216 | 0.003 | - | - | 0.308 | 0.310 | 0.018 | 10.15x | 27.3/38.9/57.0% | 3.7/9.2% | 3 |
| 120 | 1 | 0.318 | 0.315 | 0.003 | - | - | 0.418 | 0.418 | 0.029 | 4.31x | 11.8/17.2/25.4% | 1.5/4.1% | 3 |
| 250 | 1 | 0.320 | 0.317 | 0.003 | - | - | 0.421 | 0.422 | 0.028 | 4.27x | 11.6/16.9/25.4% | 1.5/4.0% | 3 |

> max-num-nodes=10: decode_failures 2

> faster: 9.34 s per simulated hour against 22.6 over 13 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.754 | 0.737 | 0.017 | - | - | 0.937 | 0.939 | 0.500 | 1.56x | 14.6/24.9/29.8% | 2.3/4.7% | 3 |
| baymesh-2026-08 | 1 | 0.754 | 0.737 | 0.017 | - | - | 0.937 | 0.939 | 0.500 | 1.56x | 14.6/24.9/29.8% | 2.3/4.7% | 3 |
| constrained | 1 | 0.632 | 0.609 | 0.023 | - | - | 0.805 | 0.867 | 0.399 | 2.84x | 26.7/44.7/52.5% | 4.2/8.5% | 3 |

> platform-mix=constrained: decode_failures 24

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.663 | 0.651 | 0.012 | - | - | 0.735 | 0.782 | 0.449 | 5.41x | 44.1/70.5/77.0% | 3.9/10.6% | 3 |
| 25 | 1 | 0.663 | 0.651 | 0.012 | - | - | 0.735 | 0.782 | 0.449 | 5.41x | 44.1/70.5/77.0% | 3.9/10.6% | 3 |
| 100 | 1 | 0.663 | 0.651 | 0.012 | - | - | 0.735 | 0.782 | 0.449 | 5.41x | 44.1/70.5/77.0% | 3.9/10.6% | 3 |
| 2000 | 1 | 0.663 | 0.651 | 0.012 | - | - | 0.735 | 0.782 | 0.449 | 5.41x | 44.1/70.5/77.0% | 3.9/10.6% | 3 |

> warm-num-nodes=0: decode_failures 46

> warm-num-nodes=25: decode_failures 46

> warm-num-nodes=100: decode_failures 46

> warm-num-nodes=2000: decode_failures 46

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.1 | 1 | 0.584 | 0.560 | 0.024 | - | - | 0.800 | 0.877 | 0.373 | 1.22x | 11.4/17.6/21.1% | 1.9/3.9% | 3 |
| 0.2 | 1 | 0.475 | 0.451 | 0.024 | - | - | 0.685 | 0.771 | 0.264 | 1.10x | 10.4/16.1/19.0% | 1.7/3.4% | 3 |
| 0.3 | 1 | 0.375 | 0.353 | 0.022 | - | - | 0.556 | 0.685 | 0.208 | 1.01x | 9.7/15.1/17.7% | 1.5/3.0% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 37

> burst-loss=0.2: decode_failures 27

> burst-loss=0.3: decode_failures 29

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.1 | 1 | 0.648 | 0.624 | 0.024 | - | - | 0.885 | 0.892 | 0.398 | 1.36x | 12.8/19.5/23.2% | 2.1/4.3% | 3 |
| 0.2 | 1 | 0.590 | 0.566 | 0.024 | - | - | 0.803 | 0.866 | 0.333 | 1.35x | 12.7/19.8/22.4% | 2.0/4.1% | 3 |
| 0.3 | 1 | 0.528 | 0.507 | 0.021 | - | - | 0.732 | 0.829 | 0.284 | 1.32x | 12.5/19.5/22.0% | 2.0/3.8% | 3 |

> extra-loss=0.0: decode_failures 3

> extra-loss=0.1: decode_failures 4

> extra-loss=0.2: decode_failures 23

> extra-loss=0.3: decode_failures 26

> slower: 6.67 s per simulated hour against 2.18 over 13 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.1 | 1 | 0.582 | 0.556 | 0.026 | - | - | 0.829 | 0.900 | 0.324 | 1.24x | 11.6/17.8/21.3% | 1.9/4.2% | 3 |
| 0.2 | 1 | 0.462 | 0.442 | 0.020 | - | - | 0.637 | 0.756 | 0.275 | 1.14x | 10.7/16.9/19.8% | 1.8/3.6% | 3 |
| 0.3 | 1 | 0.368 | 0.350 | 0.018 | - | - | 0.531 | 0.659 | 0.186 | 1.05x | 10.2/15.3/18.1% | 1.6/3.1% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 17

> burst-loss=0.2: decode_failures 21

> burst-loss=0.3: decode_failures 26

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.638 | 0.638 | 0.000 | - | - | 0.794 | 0.916 | 0.395 | 1.72x | 15.9/25.7/30.5% | 2.6/5.8% | 3 |
| directed-with-late-flood | 1 | 0.647 | 0.647 | 0.000 | - | - | 0.843 | 0.921 | 0.423 | 1.59x | 14.7/24.0/28.7% | 2.4/5.4% | 3 |
| m4-early-flood | 1 | 0.641 | 0.641 | 0.000 | - | - | 0.865 | 0.912 | 0.404 | 1.60x | 14.7/24.3/29.1% | 2.4/5.5% | 3 |

> dm-mode=flood-only: decode_failures 39

> dm-mode=directed-with-late-flood: decode_failures 10

> dm-mode=m4-early-flood: decode_failures 10

> slower: 7.97 s per simulated hour against 2.7 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.770 | 0.761 | 0.010 | - | - | 0.926 | 0.928 | 0.402 | 0.74x | 7.4/10.3/11.4% | 1.2/1.8% | 3 |
| 2.8 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> profile=2.8: decode_failures 3

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.25 | 1 | 0.781 | 0.756 | 0.024 | - | - | 0.895 | 0.897 | 0.481 | 1.20x | 12.0/16.3/19.8% | 1.8/4.5% | 3 |
| 0.5 | 1 | 0.767 | 0.734 | 0.033 | - | - | 0.961 | 0.967 | 0.347 | 1.02x | 10.4/13.8/15.8% | 1.6/3.6% | 3 |
| 0.75 | 1 | 0.807 | 0.797 | 0.010 | - | - | 0.975 | 0.978 | 0.560 | 0.96x | 10.2/13.2/15.5% | 1.6/3.5% | 3 |

> legacy-fraction=0.0: decode_failures 3

> legacy-fraction=0.5: decode_failures 1

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.25 | 1 | 0.780 | 0.753 | 0.027 | - | - | 0.908 | 0.912 | 0.497 | 1.19x | 12.1/16.2/19.8% | 1.8/4.4% | 3 |
| 0.5 | 1 | 0.762 | 0.730 | 0.032 | - | - | 0.955 | 0.959 | 0.366 | 1.03x | 10.5/13.9/16.1% | 1.5/3.6% | 3 |
| 0.75 | 1 | 0.804 | 0.795 | 0.009 | - | - | 0.971 | 0.977 | 0.519 | 0.91x | 10.0/12.9/15.2% | 1.5/3.5% | 3 |

> legacy-fraction=0.0: decode_failures 3

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.760 | 0.739 | 0.020 | - | - | 0.966 | 0.968 | 0.525 | 0.74x | 7.0/10.8/13.5% | 1.1/2.6% | 3 |
| signing=true | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> profile-flag=signing=true: decode_failures 3

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.754 | 0.743 | 0.011 | - | - | 0.924 | 0.925 | 0.396 | 0.74x | 7.4/10.9/12.3% | 1.2/2.3% | 3 |
| 2.5 | 1 | 0.750 | 0.738 | 0.012 | - | - | 0.916 | 0.916 | 0.427 | 0.73x | 7.3/10.8/11.9% | 1.1/2.3% | 3 |
| 2.6 | 1 | 0.769 | 0.759 | 0.010 | - | - | 0.925 | 0.925 | 0.445 | 0.71x | 7.3/10.6/12.1% | 1.1/2.3% | 3 |
| 2.7 | 1 | 0.773 | 0.766 | 0.007 | - | - | 0.925 | 0.928 | 0.405 | 0.73x | 7.6/11.7/13.3% | 1.1/2.9% | 3 |
| 2.8 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> profile=2.8: decode_failures 3

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.745 | 0.725 | 0.020 | - | - | 0.968 | 0.970 | 0.492 | 0.92x | 8.6/13.0/15.7% | 1.4/3.1% | 3 |
| 900 | 1 | 0.668 | 0.639 | 0.029 | - | - | 0.900 | 0.924 | 0.415 | 2.06x | 19.2/29.9/35.3% | 3.2/6.9% | 3 |
| 300 | 1 | 0.447 | 0.423 | 0.023 | - | - | 0.629 | 0.754 | 0.263 | 4.41x | 39.5/58.8/68.1% | 6.8/13.8% | 3 |

> broadcast-interval-s=3600: decode_failures 1

> broadcast-interval-s=900: decode_failures 14

> broadcast-interval-s=300: decode_failures 30

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.837 | 0.828 | 0.009 | - | - | 0.972 | 0.976 | 0.590 | 1.05x | 9.8/14.7/17.7% | 1.6/3.3% | 3 |
| 900 | 1 | 0.761 | 0.747 | 0.015 | - | - | 0.946 | 0.949 | 0.500 | 2.37x | 21.8/32.9/39.1% | 3.7/7.4% | 3 |
| 300 | 1 | 0.500 | 0.490 | 0.009 | - | - | 0.638 | 0.829 | 0.312 | 4.94x | 44.5/62.4/72.1% | 7.7/14.3% | 3 |

> broadcast-interval-s=300: decode_failures 26

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.717 | 0.697 | 0.020 | - | - | 0.956 | 0.960 | 0.471 | 1.26x | 11.9/18.3/22.1% | 1.9/4.3% | 3 |
| sinusoid | 1 | 0.718 | 0.693 | 0.025 | - | - | 0.949 | 0.956 | 0.437 | 1.22x | 11.4/17.6/21.3% | 1.9/4.1% | 3 |
| commuter | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> diurnal=sinusoid: decode_failures 3

> diurnal=commuter: decode_failures 3

> slower: 3.44 s per simulated hour against 1.58 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.668 | 0.639 | 0.029 | - | - | 0.900 | 0.924 | 0.415 | 2.06x | 19.2/29.9/35.3% | 3.2/6.9% | 3 |
| 3600 | 1 | 0.745 | 0.725 | 0.020 | - | - | 0.968 | 0.970 | 0.492 | 0.92x | 8.6/13.0/15.7% | 1.4/3.1% | 3 |
| 10800 | 1 | 0.761 | 0.742 | 0.019 | - | - | 0.969 | 0.973 | 0.492 | 0.60x | 5.6/8.5/10.4% | 1.0/2.0% | 3 |
| 43200 | 1 | 0.772 | 0.754 | 0.018 | - | - | 0.977 | 0.981 | 0.483 | 0.42x | 3.9/6.1/7.5% | 0.6/1.5% | 3 |

> broadcast-interval-s=900: decode_failures 14

> broadcast-interval-s=3600: decode_failures 1

> broadcast-interval-s=43200: decode_failures 1

> slower: 3.72 s per simulated hour against 1.4 over 13 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.25 | 1 | 0.705 | 0.683 | 0.022 | - | - | 0.939 | 0.944 | 0.437 | 1.40x | 13.0/20.2/24.2% | 2.2/4.8% | 3 |
| 1.0 | 1 | 0.678 | 0.654 | 0.024 | - | - | 0.889 | 0.924 | 0.459 | 1.51x | 14.1/21.7/26.4% | 2.3/5.2% | 3 |
| 4.0 | 1 | 0.662 | 0.633 | 0.029 | - | - | 0.899 | 0.922 | 0.422 | 1.86x | 17.4/27.7/33.4% | 2.8/6.4% | 3 |

> traceroute-per-hour=0.0: decode_failures 3

> traceroute-per-hour=1.0: decode_failures 29

> traceroute-per-hour=4.0: decode_failures 8

> slower: 5.08 s per simulated hour against 2.1 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.663 | 0.651 | 0.012 | - | - | 0.735 | 0.782 | 0.449 | 5.41x | 44.1/70.5/77.0% | 3.9/10.6% | 3 |
| 1.0 | 1 | 0.601 | 0.590 | 0.011 | - | - | 0.684 | 0.741 | 0.389 | 6.10x | 49.6/72.5/79.0% | 4.5/11.6% | 3 |

> traceroute-per-hour=0.0: decode_failures 46

> traceroute-per-hour=1.0: decode_failures 50

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.475 | 0.467 | 0.008 | - | - | 0.600 | 0.625 | 0.206 | 0.98x | 11.2/15.5/17.9% | 2.2/4.7% | 3 |
| 60 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 90 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.975 | 0.976 | 0.505 | 1.67x | 14.6/22.6/30.0% | 1.6/4.8% | 3 |
| 120 | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.952 | 0.952 | 0.714 | 2.10x | 17.3/34.7/40.0% | 1.4/5.2% | 3 |
| 150 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.978 | 0.979 | 0.622 | 2.62x | 22.3/39.8/46.4% | 1.3/5.6% | 3 |

> nodes=40: decode_failures 5

> nodes=60: decode_failures 3

> nodes=150: decode_failures 2

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 120 | 1 | 0.560 | 0.548 | 0.013 | - | - | 0.706 | 0.707 | 0.000 | 2.22x | 12.5/18.9/22.2% | 1.7/4.4% | 3 |
| 250 | 1 | 0.321 | 0.317 | 0.003 | - | - | 0.427 | 0.427 | 0.032 | 4.58x | 12.5/18.4/26.3% | 1.7/4.5% | 3 |
| 500 | 1 | 0.191 | 0.189 | 0.002 | - | - | 0.351 | 0.470 | 0.025 | 9.50x | 12.9/20.0/28.4% | 1.7/4.9% | 3 |

> nodes=60: decode_failures 3

> nodes=500: decode_failures 66

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.555 | 0.544 | 0.011 | - | - | 0.695 | 0.696 | 0.000 | 2.11x | 11.9/17.6/20.7% | 1.6/4.1% | 3 |
| 250 | 1 | 0.318 | 0.315 | 0.003 | - | - | 0.418 | 0.418 | 0.029 | 4.31x | 11.8/17.2/25.4% | 1.5/4.1% | 3 |
| 500 | 1 | 0.193 | 0.191 | 0.002 | - | - | 0.355 | 0.477 | 0.025 | 8.96x | 12.2/19.0/27.0% | 1.6/4.7% | 3 |

> nodes=500: decode_failures 27

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.689 | 0.668 | 0.021 | - | - | 0.937 | 0.943 | 0.339 | 1.31x | 12.2/19.2/23.2% | 2.0/4.4% | 3 |
| baymesh-2026-08 | 1 | 0.599 | 0.570 | 0.029 | - | - | 0.848 | 0.868 | 0.191 | 1.14x | 10.9/19.4/23.5% | 1.9/4.4% | 3 |

> role-mix=legacy-default: decode_failures 2

> role-mix=baymesh-2026-08: decode_failures 7

> slower: 4.15 s per simulated hour against 1.73 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.710 | 0.691 | 0.019 | - | - | 0.930 | 0.936 | 0.383 | 1.33x | 12.4/19.4/23.4% | 2.0/4.4% | 3 |
| baymesh-2026-08 | 1 | 0.641 | 0.618 | 0.023 | - | - | 0.863 | 0.869 | 0.229 | 1.24x | 12.5/21.1/26.1% | 2.1/4.5% | 3 |

> role-mix=legacy-default: decode_failures 2

> role-mix=baymesh-2026-08: decode_failures 1

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.05 | 1 | 0.700 | 0.676 | 0.024 | - | - | 0.919 | 0.932 | 0.446 | 1.44x | 13.4/22.8/28.1% | 2.2/4.5% | 3 |
| 0.1 | 1 | 0.732 | 0.713 | 0.019 | - | - | 0.939 | 0.941 | 0.459 | 1.52x | 14.2/24.8/30.3% | 2.2/4.7% | 3 |
| 0.2 | 1 | 0.723 | 0.707 | 0.016 | - | - | 0.912 | 0.918 | 0.505 | 1.70x | 16.2/26.8/30.1% | 2.5/4.6% | 3 |

> router-late-fraction=0.0: decode_failures 3

> router-late-fraction=0.05: decode_failures 3

> router-late-fraction=0.2: decode_failures 1

> slower: 3.54 s per simulated hour against 1.76 over 13 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| local-typical | 1 | 0.525 | 0.512 | 0.013 | - | - | 0.782 | 0.841 | 0.000 | 1.38x | 9.4/18.5/23.4% | 2.1/5.3% | 3 |
| event | 1 | 0.152 | 0.150 | 0.002 | - | - | 0.441 | 0.441 | 0.000 | 0.97x | 1.7/11.6/21.9% | 0.8/4.2% | 3 |
| backbone | 1 | 0.973 | 0.972 | 0.001 | - | - | 0.998 | 0.998 | 0.909 | 1.18x | 24.9/32.8/35.0% | 1.7/5.6% | 3 |

> siting-mix=uniform: decode_failures 3

> siting-mix=local-typical: decode_failures 14

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.729 | 0.714 | 0.015 | - | - | 0.839 | 0.857 | 0.471 | 1.36x | 19.4/25.8/31.9% | 3.2/7.0% | 3 |
| 60 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 90 | 1 | 0.641 | 0.635 | 0.006 | - | - | 0.904 | 0.906 | 0.315 | 1.80x | 11.7/21.0/26.4% | 1.6/5.0% | 3 |
| 120 | 1 | 0.560 | 0.548 | 0.013 | - | - | 0.706 | 0.707 | 0.000 | 2.22x | 12.5/18.9/22.2% | 1.7/4.4% | 3 |
| 150 | 1 | 0.476 | 0.459 | 0.017 | - | - | 0.655 | 0.658 | 0.120 | 2.70x | 11.8/18.8/24.3% | 1.6/5.3% | 3 |

> nodes=40: decode_failures 14

> nodes=60: decode_failures 3

> nodes=150: decode_failures 2

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 1.25 | 1 | 0.372 | 0.351 | 0.020 | - | - | 0.498 | 0.534 | 0.000 | 1.33x | 9.5/17.3/19.6% | 2.1/4.8% | 3 |
| 1.5 | 1 | 0.210 | 0.205 | 0.005 | - | - | 0.414 | 0.428 | 0.000 | 1.20x | 6.9/13.5/15.9% | 2.0/4.5% | 3 |
| 2.0 | 1 | 0.060 | 0.060 | 0.000 | - | - | 0.121 | 0.174 | 0.000 | 0.58x | 2.2/4.2/6.1% | 0.9/2.3% | 3 |

> stretch=1.0: decode_failures 3

> stretch=1.25: decode_failures 26

> stretch=1.5: decode_failures 17

> stretch=2.0: decode_failures 5

> slower: 5 s per simulated hour against 1.89 over 13 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| clustered | 1 | 0.867 | 0.865 | 0.001 | - | - | 0.946 | 0.946 | 0.000 | 1.23x | 22.8/33.7/35.7% | 1.6/5.4% | 3 |
| corridor | 1 | 0.427 | 0.419 | 0.008 | - | - | 0.519 | 0.520 | 0.155 | 1.41x | 14.0/18.2/21.0% | 2.2/5.1% | 3 |
| hub | 1 | 0.925 | 0.924 | 0.001 | - | - | 0.969 | 0.970 | 0.831 | 1.32x | 22.8/35.5/36.9% | 2.0/5.4% | 3 |

> topology=uniform: decode_failures 3

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.647 | 0.647 | 0.000 | - | - | 0.843 | 0.921 | 0.423 | 1.59x | 14.7/24.0/28.7% | 2.4/5.4% | 3 |
| True | 1 | 0.652 | 0.652 | 0.000 | - | - | 0.847 | 0.921 | 0.432 | 1.60x | 14.9/23.8/28.6% | 2.4/5.4% | 3 |

> coding-rate-ladder=False: decode_failures 10

> coding-rate-ladder=True: decode_failures 20

> slower: 7.79 s per simulated hour against 2.75 over 13 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.652 | 0.652 | 0.000 | - | - | 0.847 | 0.921 | 0.432 | 1.60x | 14.9/23.8/28.6% | 2.4/5.4% | 3 |
| m4-early-flood | 1 | 0.648 | 0.648 | 0.000 | - | - | 0.863 | 0.918 | 0.430 | 1.62x | 15.1/24.7/29.5% | 2.4/5.7% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 20

> dm-mode=m4-early-flood: decode_failures 15

> slower: 7.6 s per simulated hour against 2.5 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.678 | 0.678 | 0.000 | - | - | 0 | 0.000 | 0.446 | 1.30x | 12.3/18.8/22.3% | 2.0/4.6% | 3 |
| chain | 1 | 0.669 | 0.668 | 0.001 | - | - | 0.722 | 0.942 | 0.438 | 1.51x | 14.3/22.3/27.0% | 2.3/5.1% | 3 |
| sr | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> protocol=sr: decode_failures 3

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| True | 1 | 0.717 | 0.695 | 0.022 | - | - | 0.939 | 0.941 | 0.472 | 1.35x | 12.6/19.3/23.2% | 2.1/4.6% | 3 |

> extra-repeats=False: decode_failures 3

> extra-repeats=True: decode_failures 4

> slower: 3.77 s per simulated hour against 1.68 over 13 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.952 | 0.952 | 0.714 | 2.10x | 17.3/34.7/40.0% | 1.4/5.2% | 3 |
| True | 1 | 0.893 | 0.880 | 0.013 | - | - | 0.948 | 0.949 | 0.713 | 2.16x | 17.7/35.2/40.6% | 1.5/5.3% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.083 | 0.082 | 0.001 | - | - | 0.207 | 0.216 | 0.000 | 0.03x | 0.1/0.3/0.3% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.245 | 0.233 | 0.012 | - | - | 0.433 | 0.444 | 0.000 | 0.19x | 1.2/2.3/2.9% | 0.3/0.8% | 3 |
| LONG_TURBO | 1 | 0.576 | 0.556 | 0.020 | - | - | 0.742 | 0.753 | 0.000 | 1.25x | 9.7/15.5/18.9% | 1.9/4.4% | 3 |

> preset=SHORT_TURBO: decode_failures 1

> preset=MEDIUM_TURBO: decode_failures 14

> preset=LONG_TURBO: decode_failures 6

> slower: 3.82 s per simulated hour against 1.88 over 13 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 0.25 | 1 | 0.746 | 0.721 | 0.024 | - | - | 0.931 | 0.944 | 0.519 | 1.11x | 13.2/19.1/22.5% | 1.6/4.3% | 3 |
| 1.0 | 1 | 0.880 | 0.850 | 0.030 | - | - | 0.976 | 0.979 | 0.750 | 0.91x | 20.7/24.3/27.8% | 1.2/4.7% | 3 |

> duct-per-hour=0.0: decode_failures 3

> duct-per-hour=0.25: decode_failures 6

> slower: 3.69 s per simulated hour against 1.76 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.148 | 0.146 | 0.002 | - | - | 0.261 | 0.264 | 0.000 | 0.10x | 0.6/1.0/1.3% | 0.2/0.3% | 3 |
| LONG_FAST | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| LITE_FAST | 1 | 0.578 | 0.554 | 0.024 | - | - | 0.853 | 0.888 | 0.000 | 0.94x | 8.0/13.2/16.7% | 1.3/3.7% | 3 |
| NARROW_SLOW | 1 | 0.620 | 0.603 | 0.017 | - | - | 0.810 | 0.812 | 0.153 | 1.26x | 10.8/16.9/23.0% | 1.8/4.7% | 3 |

> preset=SHORT_FAST: decode_failures 1

> preset=LONG_FAST: decode_failures 3

> preset=LITE_FAST: decode_failures 14

> preset=NARROW_SLOW: decode_failures 2

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| temporal | 1 | 0.550 | 0.530 | 0.019 | - | - | 0.753 | 0.873 | 0.131 | 1.27x | 11.8/18.7/22.0% | 1.9/4.3% | 3 |
| transient | 1 | 0.697 | 0.673 | 0.024 | - | - | 0.935 | 0.943 | 0.447 | 1.35x | 12.5/19.2/23.0% | 2.1/4.6% | 3 |
| periodic | 1 | 0.515 | 0.498 | 0.016 | - | - | 0.651 | 0.743 | 0.305 | 1.21x | 11.3/17.5/20.2% | 1.8/3.9% | 3 |

> noise-profile=none: decode_failures 3

> noise-profile=temporal: decode_failures 25

> noise-profile=transient: decode_failures 3

> noise-profile=periodic: decode_failures 20

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.148 | 0.146 | 0.002 | - | - | 0.261 | 0.264 | 0.000 | 0.10x | 0.6/1.0/1.3% | 0.2/0.3% | 3 |
| LONG_FAST | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| LONG_MODERATE | 1 | 0.721 | 0.695 | 0.027 | - | - | 0.838 | 0.922 | 0.558 | 3.32x | 37.8/50.5/57.0% | 5.1/12.3% | 3 |

> preset=SHORT_FAST: decode_failures 1

> preset=LONG_FAST: decode_failures 3

> preset=LONG_MODERATE: decode_failures 22

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.024 | 0.024 | 0.000 | - | - | 0.038 | 0.047 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.083 | 0.082 | 0.001 | - | - | 0.207 | 0.216 | 0.000 | 0.03x | 0.1/0.3/0.3% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| LONG_TURBO | 1 | 0.576 | 0.556 | 0.020 | - | - | 0.742 | 0.753 | 0.000 | 1.25x | 9.7/15.5/18.9% | 1.9/4.4% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.671 | 0.646 | 0.024 | - | - | 0.912 | 0.918 | 0.332 | 1.91x | 17.0/25.1/30.6% | 2.9/6.2% | 3 |

> preset=SHORT_TURBO: decode_failures 1

> preset=LONG_FAST: decode_failures 3

> preset=LONG_TURBO: decode_failures 6

> preset=EXTRA_LONG_TURBO: decode_failures 7

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.637 | 0.614 | 0.024 | - | - | 0.867 | 0.881 | 0.397 | 1.29x | 12.1/18.8/22.4% | 2.0/4.3% | 3 |
| 10000 | 1 | 0.515 | 0.498 | 0.016 | - | - | 0.651 | 0.743 | 0.305 | 1.21x | 11.3/17.5/20.2% | 1.8/3.9% | 3 |
| 4000 | 1 | 0.296 | 0.291 | 0.004 | - | - | 0.330 | 0.481 | 0.160 | 0.99x | 9.3/14.4/16.4% | 1.5/2.8% | 3 |
| 2000 | 1 | 0.071 | 0.071 | 0.000 | - | - | 0.065 | 0.131 | 0.030 | 0.70x | 6.9/10.5/12.1% | 1.1/1.7% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 5

> noise-pulse-interval-ms=10000: decode_failures 20

> noise-pulse-interval-ms=4000: decode_failures 7

> slower: 3.61 s per simulated hour against 1.6 over 13 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.210 | 0.205 | 0.005 | - | - | 0.414 | 0.428 | 0.000 | 1.20x | 6.9/13.5/15.9% | 2.0/4.5% | 3 |
| 1.0 | 1 | 0.640 | 0.614 | 0.026 | - | - | 0.738 | 0.738 | 0.504 | 0.86x | 15.0/18.3/21.2% | 1.2/4.2% | 3 |

> duct-per-hour=0.0: decode_failures 17

> duct-per-hour=1.0: decode_failures 1

> slower: 4.12 s per simulated hour against 1.9 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 22 | 1 | 0.224 | 0.217 | 0.006 | - | - | 0.434 | 0.440 | 0.000 | 1.26x | 7.3/13.3/17.1% | 2.1/4.2% | 3 |
| 17 | 1 | 0.081 | 0.080 | 0.001 | - | - | 0.199 | 0.201 | 0.000 | 0.67x | 3.0/5.5/6.8% | 1.2/2.5% | 3 |
| 14 | 1 | 0.038 | 0.038 | 0.000 | - | - | 0.040 | 0.047 | 0.000 | 0.44x | 1.4/3.1/4.7% | 0.7/1.8% | 3 |

> tx-power=30: decode_failures 3

> tx-power=17: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.952 | 0.952 | 0.714 | 2.10x | 17.3/34.7/40.0% | 1.4/5.2% | 3 |
| True | 1 | 0.875 | 0.862 | 0.013 | - | - | 0.938 | 0.938 | 0.695 | 2.46x | 20.2/38.4/44.1% | 1.7/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.708 | 0.686 | 0.022 | - | - | 0.938 | 0.945 | 0.449 | 1.41x | 13.1/21.9/26.4% | 2.2/4.5% | 3 |
| True | 1 | 0.706 | 0.685 | 0.021 | - | - | 0.919 | 0.930 | 0.449 | 1.45x | 13.5/22.5/27.2% | 2.2/4.5% | 3 |

> favourite-routers=False: decode_failures 1

> favourite-routers=True: decode_failures 3

> slower: 3.83 s per simulated hour against 1.69 over 13 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| random | 1 | 0.665 | 0.645 | 0.021 | - | - | 0.885 | 0.904 | 0.372 | 1.32x | 12.4/19.2/23.1% | 2.1/4.4% | 3 |

> hop-assign=centrality: decode_failures 3

> hop-assign=random: decode_failures 7

> slower: 4.52 s per simulated hour against 1.77 over 13 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.535 | 0.501 | 0.035 | - | - | 0.857 | 0.899 | 0.273 | 1.17x | 10.7/18.3/23.0% | 1.6/4.3% | 3 |
| 7 | 1 | 0.805 | 0.793 | 0.012 | - | - | 0.971 | 0.975 | 0.572 | 1.53x | 14.2/21.3/25.4% | 2.4/4.8% | 3 |
| 15 | 1 | 0.878 | 0.873 | 0.005 | - | - | 0.979 | 0.981 | 0.623 | 1.57x | 14.6/21.9/26.0% | 2.5/4.9% | 3 |
| 32 | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.970 | 0.973 | 0.629 | 1.57x | 14.6/21.8/25.8% | 2.5/4.9% | 3 |

> hop-limit=3: decode_failures 25

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.535 | 0.501 | 0.035 | - | - | 0.857 | 0.899 | 0.273 | 1.17x | 10.7/18.3/23.0% | 1.6/4.3% | 3 |
| 5 | 1 | 0.725 | 0.703 | 0.022 | - | - | 0.962 | 0.967 | 0.480 | 1.33x | 12.3/19.1/23.1% | 2.0/4.5% | 3 |
| 7 | 1 | 0.805 | 0.793 | 0.012 | - | - | 0.971 | 0.975 | 0.572 | 1.53x | 14.2/21.3/25.4% | 2.4/4.8% | 3 |

> hop-limit=3: decode_failures 25

> hop-limit=5: decode_failures 1

> slower: 5.25 s per simulated hour against 2.03 over 13 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| KNOWN_ONLY | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.679 | 0.679 | 0.000 | - | - | 0.725 | 0.945 | 0.441 | 1.31x | 12.4/18.8/22.3% | 2.1/4.5% | 3 |

> rebroadcast-mode=ALL: decode_failures 3

> rebroadcast-mode=KNOWN_ONLY: decode_failures 3

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.535 | 0.501 | 0.035 | - | - | 0.857 | 0.899 | 0.273 | 1.17x | 10.7/18.3/23.0% | 1.6/4.3% | 3 |
| True | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> hop-spread=False: decode_failures 25

> hop-spread=True: decode_failures 3

> slower: 6.84 s per simulated hour against 2.08 over 13 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| BALANCED | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| STRICT | 1 | 0.523 | 0.523 | 0.000 | - | - | 0.759 | 0.778 | 0.301 | 1.45x | 13.6/21.2/25.5% | 2.2/4.9% | 3 |

> signature-policy=COMPATIBLE: decode_failures 3

> signature-policy=BALANCED: decode_failures 3

> signature-policy=STRICT: decode_failures 26

> slower: 5.97 s per simulated hour against 1.87 over 13 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| dm | 1 | 0.694 | 0.673 | 0.020 | - | - | 0.937 | 0.938 | 0.441 | 1.33x | 12.4/19.1/23.0% | 2.1/4.6% | 3 |

> advert-transport=broadcast: decode_failures 3

> slower: 4.16 s per simulated hour against 1.85 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.706 | 0.680 | 0.026 | - | - | 0.925 | 0.954 | 0.466 | 1.34x | 12.5/19.3/23.1% | 2.1/4.5% | 3 |
| local | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| time | 1 | 0.703 | 0.681 | 0.023 | - | - | 0.933 | 0.941 | 0.457 | 1.38x | 12.9/20.0/23.9% | 2.1/4.7% | 3 |
| window | 1 | 0.706 | 0.682 | 0.024 | - | - | 0.937 | 0.949 | 0.436 | 1.35x | 12.6/19.3/23.3% | 2.1/4.6% | 3 |

> bucket-mode=global: misdecodes 8

> bucket-mode=local: decode_failures 3

> bucket-mode=time: misdecodes 6

> bucket-mode=time: decode_failures 5

> bucket-mode=window: misdecodes 7

> slower: 3.29 s per simulated hour against 1.56 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.695 | 0.671 | 0.024 | - | - | 0.922 | 0.940 | 0.446 | 1.47x | 13.6/21.3/25.8% | 2.3/5.0% | 3 |
| 1800 | 1 | 0.703 | 0.681 | 0.023 | - | - | 0.933 | 0.941 | 0.457 | 1.38x | 12.9/20.0/23.9% | 2.1/4.7% | 3 |
| 3600 | 1 | 0.704 | 0.684 | 0.019 | - | - | 0.915 | 0.949 | 0.454 | 1.35x | 12.6/19.3/23.3% | 2.1/4.6% | 3 |

> time-bucket-s=600: misdecodes 68

> time-bucket-s=1800: misdecodes 6

> time-bucket-s=1800: decode_failures 5

> time-bucket-s=3600: misdecodes 2

> time-bucket-s=3600: decode_failures 12

> slower: 3.98 s per simulated hour against 1.62 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| interval | 1 | 0.671 | 0.644 | 0.027 | - | - | 0.898 | 0.922 | 0.439 | 1.76x | 16.1/26.1/32.5% | 2.5/6.8% | 3 |
| aimd | 1 | 0.695 | 0.686 | 0.009 | - | - | 0.788 | 0.938 | 0.438 | 1.34x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| bucket+interval | 1 | 0.677 | 0.650 | 0.027 | - | - | 0.918 | 0.925 | 0.413 | 1.78x | 16.2/26.3/32.5% | 2.6/6.6% | 3 |

> trigger=bucket: decode_failures 3

> trigger=interval: misdecodes 6

> trigger=interval: decode_failures 25

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 23

> trigger=bucket+interval: misdecodes 8

> slower: 8.98 s per simulated hour against 2.75 over 13 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.704 | 0.683 | 0.021 | - | - | 0.905 | 0.949 | 0.444 | 1.33x | 12.5/19.1/23.2% | 2.1/4.5% | 3 |
| 8 | 1 | 0.708 | 0.685 | 0.022 | - | - | 0.912 | 0.943 | 0.456 | 1.34x | 12.5/19.3/23.3% | 2.1/4.6% | 3 |
| 16 | 1 | 0.691 | 0.667 | 0.024 | - | - | 0.894 | 0.936 | 0.451 | 1.36x | 12.6/19.4/23.5% | 2.1/4.6% | 3 |
| 32 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 50 | 1 | 0.706 | 0.680 | 0.025 | - | - | 0.936 | 0.942 | 0.449 | 1.35x | 12.7/19.5/23.5% | 2.1/4.6% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 98

> capacity=16: decode_failures 91

> capacity=32: decode_failures 3

> slower: 4.01 s per simulated hour against 1.69 over 13 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.704 | 0.683 | 0.021 | - | - | 0.905 | 0.949 | 0.444 | 1.33x | 12.5/19.1/23.2% | 2.1/4.5% | 3 |
| 8 | 1 | 0.708 | 0.685 | 0.022 | - | - | 0.912 | 0.943 | 0.456 | 1.34x | 12.5/19.3/23.3% | 2.1/4.6% | 3 |
| 16 | 1 | 0.691 | 0.667 | 0.024 | - | - | 0.894 | 0.936 | 0.451 | 1.36x | 12.6/19.4/23.5% | 2.1/4.6% | 3 |
| 32 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 50 | 1 | 0.706 | 0.680 | 0.025 | - | - | 0.936 | 0.942 | 0.449 | 1.35x | 12.7/19.5/23.5% | 2.1/4.6% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 98

> capacity=16: decode_failures 91

> capacity=32: decode_failures 3

> slower: 3.94 s per simulated hour against 1.77 over 13 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.693 | 0.692 | 0.001 | - | - | 0.751 | 0.954 | 0.450 | 1.33x | 12.5/19.0/22.7% | 2.1/4.6% | 3 |
| 16 | 1 | 0.699 | 0.684 | 0.014 | - | - | 0.840 | 0.945 | 0.458 | 1.32x | 12.4/19.0/22.7% | 2.1/4.5% | 3 |
| 32 | 1 | 0.706 | 0.682 | 0.024 | - | - | 0.937 | 0.949 | 0.436 | 1.35x | 12.6/19.3/23.3% | 2.1/4.6% | 3 |

> capacity=8: decode_failures 127

> capacity=16: misdecodes 1

> capacity=16: decode_failures 74

> capacity=32: misdecodes 7

> slower: 4.06 s per simulated hour against 1.61 over 13 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.677 | 0.650 | 0.027 | - | - | 0.918 | 0.925 | 0.413 | 1.78x | 16.2/26.3/32.5% | 2.6/6.6% | 3 |
| 02-06 | 1 | 0.692 | 0.677 | 0.015 | - | - | 0.827 | 0.926 | 0.451 | 1.36x | 12.7/19.5/23.7% | 2.1/4.7% | 3 |
| 00-08 | 1 | 0.689 | 0.674 | 0.015 | - | - | 0.834 | 0.926 | 0.451 | 1.43x | 13.2/20.5/25.2% | 2.2/5.0% | 3 |

> catch-up-hours=: misdecodes 8

> catch-up-hours=02-06: decode_failures 46

> catch-up-hours=00-08: decode_failures 47

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.688 | 0.683 | 0.004 | - | - | 0.753 | 0.754 | 0.450 | 1.32x | 12.3/19.3/23.0% | 2.1/4.5% | 3 |
| 2 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 3 | 1 | 0.725 | 0.682 | 0.043 | - | - | 0.884 | 0.968 | 0.470 | 1.35x | 12.7/19.3/23.1% | 2.1/4.9% | 3 |
| 4 | 1 | 0.723 | 0.677 | 0.046 | - | - | 0.849 | 0.948 | 0.453 | 1.34x | 12.8/19.6/23.2% | 2.1/4.9% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=3: decode_failures 29

> hops-apart=4: decode_failures 27

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.688 | 0.683 | 0.004 | - | - | 0.753 | 0.754 | 0.450 | 1.32x | 12.3/19.3/23.0% | 2.1/4.5% | 3 |
| 2 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 3 | 1 | 0.725 | 0.682 | 0.043 | - | - | 0.884 | 0.968 | 0.470 | 1.35x | 12.7/19.3/23.1% | 2.1/4.9% | 3 |
| 4 | 1 | 0.723 | 0.677 | 0.046 | - | - | 0.849 | 0.948 | 0.453 | 1.34x | 12.8/19.6/23.2% | 2.1/4.9% | 3 |
| 5 | 1 | 0.700 | 0.682 | 0.018 | - | - | 0.736 | 0.966 | 0.440 | 1.33x | 12.4/19.1/22.8% | 2.0/4.8% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=3: decode_failures 29

> hops-apart=4: decode_failures 27

> hops-apart=5: decode_failures 34

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.707 | 0.682 | 0.025 | - | - | 0.940 | 0.942 | 0.450 | 1.34x | 12.5/19.3/23.3% | 2.1/4.5% | 3 |
| 30 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 120 | 1 | 0.698 | 0.675 | 0.022 | - | - | 0.928 | 0.942 | 0.448 | 1.35x | 12.6/19.3/23.3% | 2.1/4.6% | 3 |
| 600 | 1 | 0.702 | 0.677 | 0.025 | - | - | 0.926 | 0.944 | 0.433 | 1.35x | 12.6/19.2/23.3% | 2.1/4.6% | 3 |

> advert-jitter-s=1: decode_failures 3

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 9

> advert-jitter-s=600: decode_failures 39

> slower: 7.28 s per simulated hour against 1.74 over 13 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.707 | 0.682 | 0.025 | - | - | 0.940 | 0.942 | 0.450 | 1.34x | 12.5/19.3/23.3% | 2.1/4.5% | 3 |
| 30 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 120 | 1 | 0.698 | 0.675 | 0.022 | - | - | 0.928 | 0.942 | 0.448 | 1.35x | 12.6/19.3/23.3% | 2.1/4.6% | 3 |
| 600 | 1 | 0.702 | 0.677 | 0.025 | - | - | 0.926 | 0.944 | 0.433 | 1.35x | 12.6/19.2/23.3% | 2.1/4.6% | 3 |

> advert-jitter-s=1: decode_failures 3

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 9

> advert-jitter-s=600: decode_failures 39

> slower: 6.94 s per simulated hour against 1.77 over 13 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.699 | 0.677 | 0.022 | - | - | 0.617 | 0.908 | 0.444 | 1.34x | 12.6/19.5/23.2% | 2.1/4.7% | 3 |
| routers | 1 | 0.700 | 0.685 | 0.015 | - | - | 0.861 | 0.960 | 0.446 | 1.34x | 12.5/19.5/23.3% | 2.1/4.8% | 3 |
| alternate-routers | 1 | 0.686 | 0.682 | 0.004 | - | - | 0.746 | 0.746 | 0.441 | 1.32x | 12.4/19.2/23.0% | 2.1/4.6% | 3 |
| beside-router | 1 | 0.712 | 0.675 | 0.037 | - | - | 0.884 | 0.902 | 0.441 | 1.35x | 12.9/19.8/23.5% | 2.1/4.6% | 3 |
| random-clients | 1 | 0.722 | 0.677 | 0.045 | - | - | 0.850 | 0.942 | 0.446 | 1.37x | 12.9/20.1/23.7% | 2.1/4.9% | 3 |
| hops-apart | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> place=spread: decode_failures 23

> place=routers: decode_failures 17

> place=beside-router: decode_failures 5

> place=random-clients: decode_failures 29

> place=hops-apart: decode_failures 3

> slower: 5.42 s per simulated hour against 2.56 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.699 | 0.677 | 0.022 | - | - | 0.617 | 0.908 | 0.444 | 1.34x | 12.6/19.5/23.2% | 2.1/4.7% | 3 |
| routers | 1 | 0.700 | 0.685 | 0.015 | - | - | 0.861 | 0.960 | 0.446 | 1.34x | 12.5/19.5/23.3% | 2.1/4.8% | 3 |
| alternate-routers | 1 | 0.686 | 0.682 | 0.004 | - | - | 0.746 | 0.746 | 0.441 | 1.32x | 12.4/19.2/23.0% | 2.1/4.6% | 3 |
| beside-router | 1 | 0.712 | 0.675 | 0.037 | - | - | 0.884 | 0.902 | 0.441 | 1.35x | 12.9/19.8/23.5% | 2.1/4.6% | 3 |
| random-clients | 1 | 0.722 | 0.677 | 0.045 | - | - | 0.850 | 0.942 | 0.446 | 1.37x | 12.9/20.1/23.7% | 2.1/4.9% | 3 |
| hops-apart | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> place=spread: decode_failures 23

> place=routers: decode_failures 17

> place=beside-router: decode_failures 5

> place=random-clients: decode_failures 29

> place=hops-apart: decode_failures 3

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| broadcast | 1 | 0.783 | 0.668 | 0.115 | - | - | 0.893 | 0.935 | 0.530 | 1.50x | 14.0/22.1/26.3% | 2.3/5.0% | 3 |

> provide-transport=dm: decode_failures 3

> provide-transport=broadcast: decode_failures 15

> slower: 5.72 s per simulated hour against 1.93 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| heard | 1 | 0.704 | 0.680 | 0.024 | - | - | 0.941 | 0.951 | 0.444 | 1.35x | 12.6/19.3/23.3% | 2.1/4.6% | 3 |

> replay-ordering=tip: decode_failures 3

> replay-ordering=heard: misdecodes 4

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.783 | 0.668 | 0.115 | - | - | 0.893 | 0.935 | 0.530 | 1.50x | 14.0/22.1/26.3% | 2.3/5.0% | 3 |
| heard | 1 | 0.788 | 0.660 | 0.128 | - | - | 0.910 | 0.937 | 0.519 | 1.53x | 14.0/22.7/26.9% | 2.3/5.0% | 3 |

> replay-ordering=tip: decode_failures 15

> replay-ordering=heard: decode_failures 4

> slower: 5.86 s per simulated hour against 1.57 over 13 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.700 | 0.675 | 0.024 | - | - | 0.928 | 0.939 | 0.445 | 1.34x | 12.6/19.4/23.4% | 2.1/4.5% | 3 |
| enum | 1 | 0.705 | 0.680 | 0.025 | - | - | 0.918 | 0.944 | 0.447 | 1.34x | 12.6/19.1/23.0% | 2.1/4.6% | 3 |
| hybrid | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> resolve=sketch: decode_failures 4

> resolve=hybrid: decode_failures 3

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.700 | 0.685 | 0.015 | - | - | 0.861 | 0.960 | 0.446 | 1.34x | 12.5/19.5/23.3% | 2.1/4.8% | 3 |
| 6 | 1 | 0.717 | 0.668 | 0.048 | - | - | 0.944 | 0.949 | 0.445 | 1.38x | 12.9/20.4/24.2% | 2.1/5.0% | 6 |

> servers=3: decode_failures 17

> servers=6: decode_failures 7

> slower: 6.94 s per simulated hour against 1.85 over 13 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.685 | 0.676 | 0.009 | - | - | 0.766 | 0.788 | 0.424 | 1.33x | 12.6/19.3/23.1% | 2.1/4.6% | 2 |
| 3 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 5 | 1 | 0.707 | 0.671 | 0.036 | - | - | 0.948 | 0.954 | 0.451 | 1.38x | 12.7/19.9/24.0% | 2.1/4.6% | 5 |
| 8 | 1 | 0.703 | 0.666 | 0.037 | - | - | 0.965 | 0.968 | 0.425 | 1.41x | 13.0/20.8/24.9% | 2.2/4.7% | 8 |

> servers=2: decode_failures 2

> servers=3: decode_failures 3

> servers=8: decode_failures 1

> slower: 6.5 s per simulated hour against 2.6 over 13 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.685 | 0.676 | 0.009 | - | - | 0.766 | 0.788 | 0.424 | 1.33x | 12.6/19.3/23.1% | 2.1/4.6% | 2 |
| 3 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 5 | 1 | 0.707 | 0.671 | 0.036 | - | - | 0.948 | 0.954 | 0.451 | 1.38x | 12.7/19.9/24.0% | 2.1/4.6% | 5 |
| 8 | 1 | 0.703 | 0.666 | 0.037 | - | - | 0.965 | 0.968 | 0.425 | 1.41x | 13.0/20.8/24.9% | 2.2/4.7% | 8 |

> servers=2: decode_failures 2

> servers=3: decode_failures 3

> servers=8: decode_failures 1

> slower: 6.49 s per simulated hour against 2.29 over 13 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| True | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |

> signed=False: decode_failures 3

> signed=True: decode_failures 3

> slower: 3.51 s per simulated hour against 1.74 over 13 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.687 | 0.668 | 0.019 | - | - | 0.863 | 0.935 | 0.410 | 1.24x | 11.6/18.1/21.7% | 1.9/4.2% | 3 |
| 1 | 1 | 0.698 | 0.673 | 0.026 | - | - | 0.920 | 0.945 | 0.431 | 1.23x | 11.6/18.0/21.6% | 1.9/4.2% | 3 |
| 2 | 1 | 0.697 | 0.674 | 0.022 | - | - | 0.940 | 0.944 | 0.447 | 1.25x | 11.6/18.2/21.7% | 1.9/4.2% | 3 |
| 4 | 1 | 0.684 | 0.663 | 0.021 | - | - | 0.915 | 0.933 | 0.410 | 1.24x | 11.6/18.1/21.7% | 1.9/4.3% | 3 |

> sr-retries=0: decode_failures 16

> sr-retries=1: decode_failures 7

> slower: 5 s per simulated hour against 1.67 over 13 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.706 | 0.683 | 0.023 | - | - | 0.939 | 0.949 | 0.470 | 1.33x | 12.6/19.3/23.2% | 2.1/4.5% | 3 |
| 24 | 1 | 0.709 | 0.685 | 0.024 | - | - | 0.950 | 0.958 | 0.454 | 1.35x | 12.5/19.2/23.2% | 2.1/4.6% | 3 |
| 32 | 1 | 0.701 | 0.675 | 0.026 | - | - | 0.940 | 0.943 | 0.454 | 1.35x | 12.6/19.4/23.2% | 2.1/4.6% | 3 |
| 64 | 1 | 0.698 | 0.674 | 0.024 | - | - | 0.925 | 0.940 | 0.445 | 1.35x | 12.7/19.7/23.7% | 2.1/4.6% | 3 |

> short-id-bits=16: decode_failures 2

> short-id-bits=24: decode_failures 3

> short-id-bits=32: decode_failures 3

> short-id-bits=64: decode_failures 1

> slower: 3.79 s per simulated hour against 1.77 over 13 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.707 | 0.680 | 0.027 | - | - | 0.934 | 0.940 | 0.466 | 1.42x | 13.3/20.5/24.7% | 2.2/4.8% | 3 |
| 16 | 1 | 0.712 | 0.685 | 0.026 | - | - | 0.938 | 0.949 | 0.431 | 1.38x | 12.8/19.7/23.7% | 2.1/4.7% | 3 |
| 32 | 1 | 0.706 | 0.682 | 0.024 | - | - | 0.937 | 0.949 | 0.436 | 1.35x | 12.6/19.3/23.3% | 2.1/4.6% | 3 |

> window-size=8: misdecodes 83

> window-size=16: misdecodes 31

> window-size=32: misdecodes 7

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.952 | 0.952 | 0.714 | 2.10x | 17.3/34.7/40.0% | 1.4/5.2% | 3 |
| True | 1 | 0.653 | 0.640 | 0.014 | - | - | 0.737 | 0.773 | 0.433 | 5.51x | 45.0/70.8/77.2% | 4.0/10.6% | 3 |

> no-congestion-scaling=True: decode_failures 60

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.318 | 0.315 | 0.003 | - | - | 0.418 | 0.418 | 0.029 | 4.31x | 11.8/17.2/25.4% | 1.5/4.1% | 3 |
| truesize | 1 | 0.351 | 0.348 | 0.003 | - | - | 0.456 | 0.458 | 0.032 | 2.47x | 6.4/11.2/15.1% | 0.9/2.8% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.894 | 0.881 | 0.013 | - | - | 0.953 | 0.955 | 0.713 | 2.02x | 16.5/32.8/37.8% | 1.4/4.9% | 3 |
| adaptive | 1 | 0.891 | 0.880 | 0.011 | - | - | 0.952 | 0.952 | 0.714 | 2.10x | 17.3/34.7/40.0% | 1.4/5.2% | 3 |

