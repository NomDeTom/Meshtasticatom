# Sweep blocks-2026-09-05-1196796

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 1196796 · seeds 1196796
- **blocks** 87 run
- **compute** 22.0 h of simulator time across every cell
- **generated** 2026-09-05T09:08:50+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>291 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 22
- AD-amplifiers: slower: 3.65 s per simulated hour against 1.68 over 15 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-amplify-worst: amplify-worst=0.0: decode_failures 22
- AD-amplify-worst: slower: 3.65 s per simulated hour against 1.69 over 15 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=degree: decode_failures 41
- AD-badrouters: role-placement=inverse: decode_failures 23
- AD-badrouters: slower: 7.39 s per simulated hour against 2.1 over 15 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 41
- AD-flooding: slower: 8.36 s per simulated hour against 2.57 over 15 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 41
- AD-nomute: slower: 6.27 s per simulated hour against 2.32 over 15 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 41
- AD-siting: siting-mix=local-typical: decode_failures 4
- AD-siting: siting-mix=basement-heavy: decode_failures 1
- AD-siting: slower: 5.05 s per simulated hour against 1.29 over 15 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=degree: decode_failures 74
- AD-worst: role-placement=inverse: decode_failures 69
- AD-worst: slower: 20.3 s per simulated hour against 3.86 over 15 prior run(s) - 5.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 27
- DB-hotstore: max-num-nodes=100: decode_failures 20
- DB-hotstore: max-num-nodes=120: decode_failures 20
- DB-hotstore: max-num-nodes=250: decode_failures 20
- DB-hotstore: slower: 8.62 s per simulated hour against 2.57 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 67
- DB-hotstore-stress: max-num-nodes=120: decode_failures 4
- DB-hotstore-stress: max-num-nodes=250: decode_failures 1
- DB-platform: platform-mix=uniform: decode_failures 20
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 20
- DB-platform: platform-mix=constrained: decode_failures 28
- DB-platform: slower: 8.72 s per simulated hour against 2.58 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: queue drops 16.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 122
- DB-warm: warm-num-nodes=25: queue drops 16.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 122
- DB-warm: warm-num-nodes=100: queue drops 16.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 122
- DB-warm: warm-num-nodes=2000: queue drops 16.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 122
- DG-burst: burst-loss=0.0: decode_failures 22
- DG-burst: burst-loss=0.1: decode_failures 23
- DG-burst: burst-loss=0.2: decode_failures 19
- DG-burst: burst-loss=0.3: decode_failures 32
- DG-loss: extra-loss=0.0: decode_failures 22
- DG-loss: extra-loss=0.1: decode_failures 34
- DG-loss: extra-loss=0.2: decode_failures 30
- DG-loss: extra-loss=0.3: decode_failures 14
- DG-loss: slower: 8.56 s per simulated hour against 2.18 over 15 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 22
- DG-outage: burst-loss=0.1: decode_failures 43
- DG-outage: burst-loss=0.2: decode_failures 26
- DG-outage: burst-loss=0.3: decode_failures 28
- DM-mode: dm-mode=flood-only: decode_failures 28
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 31
- DM-mode: dm-mode=m4-early-flood: decode_failures 32
- DM-mode: slower: 10.8 s per simulated hour against 2.7 over 15 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 22
- FW-firmware: slower: 4.75 s per simulated hour against 1.8 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.0: decode_failures 22
- FW-mixed-26: legacy-fraction=0.25: decode_failures 13
- FW-mixed-26: legacy-fraction=0.5: decode_failures 20
- FW-mixed-26: slower: 5.41 s per simulated hour against 1.71 over 15 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.0: decode_failures 22
- FW-mixed: legacy-fraction=0.25: decode_failures 46
- FW-mixed: legacy-fraction=0.5: decode_failures 2
- FW-mixed: slower: 6.43 s per simulated hour against 1.7 over 15 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-signing-cost: profile-flag=signing=false: decode_failures 41
- FW-signing-cost: profile-flag=signing=true: decode_failures 22
- FW-signing-cost: slower: 10.4 s per simulated hour against 1.58 over 15 prior run(s) - 6.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-versions: profile=2.8: decode_failures 22
- LD-chatty-hops: broadcast-interval-s=3600: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=900: decode_failures 22
- LD-chatty-hops: broadcast-interval-s=300: queue drops 14.7% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 29
- LD-chatty-hops: slower: 8.41 s per simulated hour against 3.72 over 15 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty: broadcast-interval-s=3600: decode_failures 45
- LD-chatty: broadcast-interval-s=900: decode_failures 35
- LD-chatty: broadcast-interval-s=300: queue drops 10.3% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 37
- LD-chatty: slower: 13.8 s per simulated hour against 4.58 over 15 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-diurnal: diurnal=flat: decode_failures 13
- LD-diurnal: diurnal=sinusoid: decode_failures 18
- LD-diurnal: diurnal=commuter: decode_failures 22
- LD-diurnal: slower: 7.04 s per simulated hour against 1.58 over 15 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 35
- LD-interval: broadcast-interval-s=3600: decode_failures 45
- LD-interval: broadcast-interval-s=10800: decode_failures 57
- LD-interval: broadcast-interval-s=43200: decode_failures 44
- LD-interval: slower: 13.8 s per simulated hour against 1.4 over 15 prior run(s) - 9.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 22
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 35
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 15
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 5
- LD-traceroute: slower: 7.6 s per simulated hour against 2.1 over 15 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 16.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 122
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 22.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 111
- MS-density: nodes=40: decode_failures 12
- MS-density: nodes=60: decode_failures 22
- MS-hopscale: nodes=60: decode_failures 22
- MS-hopscale: nodes=250: decode_failures 121
- MS-hopscale: nodes=500: decode_failures 21
- MS-oversubscribed: nodes=250: decode_failures 4
- MS-oversubscribed: nodes=500: decode_failures 5
- MS-roles-fav: role-mix=legacy-default: decode_failures 29
- MS-roles-fav: slower: 4.64 s per simulated hour against 1.75 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-roles: role-mix=legacy-default: decode_failures 39
- MS-roles: role-mix=baymesh-2026-08: decode_failures 41
- MS-roles: slower: 9.27 s per simulated hour against 1.73 over 15 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 22
- MS-router-late: router-late-fraction=0.05: decode_failures 37
- MS-router-late: router-late-fraction=0.1: decode_failures 32
- MS-router-late: slower: 8.05 s per simulated hour against 1.76 over 15 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=uniform: decode_failures 22
- MS-siting: siting-mix=local-typical: decode_failures 3
- MS-size: nodes=60: decode_failures 22
- MS-stretch: stretch=1.0: decode_failures 22
- MS-topology: topology=uniform: decode_failures 22
- MS-topology: topology=corridor: decode_failures 2
- PR-crladder: coding-rate-ladder=False: decode_failures 31
- PR-crladder: coding-rate-ladder=True: decode_failures 38
- PR-crladder: slower: 9.12 s per simulated hour against 2.75 over 15 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 38
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 34
- PR-dmmode-cr: slower: 12.1 s per simulated hour against 2.5 over 15 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 22
- PR-protocol: slower: 3.37 s per simulated hour against 1.42 over 15 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats: extra-repeats=False: decode_failures 22
- PR-repeats: extra-repeats=True: decode_failures 34
- PR-repeats: slower: 9.47 s per simulated hour against 1.68 over 15 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=SHORT_TURBO: decode_failures 3
- RF-bw500: preset=LONG_TURBO: decode_failures 12
- RF-duct: duct-per-hour=0.0: decode_failures 22
- RF-duct: duct-per-hour=0.25: decode_failures 29
- RF-duct: duct-per-hour=1.0: decode_failures 3
- RF-duct: slower: 6.17 s per simulated hour against 1.82 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=LONG_FAST: decode_failures 22
- RF-eu-presets: preset=LITE_FAST: decode_failures 27
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 33
- RF-eu-presets: slower: 7.74 s per simulated hour against 2.03 over 15 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-noise: noise-profile=none: decode_failures 22
- RF-noise: noise-profile=temporal: decode_failures 33
- RF-noise: noise-profile=transient: decode_failures 28
- RF-noise: noise-profile=periodic: decode_failures 26
- RF-noise: slower: 13.1 s per simulated hour against 4.91 over 15 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset: preset=LONG_FAST: decode_failures 22
- RF-preset: preset=LONG_MODERATE: decode_failures 3
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 3
- RF-preset-turbo: preset=LONG_FAST: decode_failures 22
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 12
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 2
- RF-preset-turbo: slower: 3.49 s per simulated hour against 1.59 over 11 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 12
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 26
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 4
- RF-pulse: slower: 4.16 s per simulated hour against 1.6 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=30: decode_failures 22
- RF-txpower: tx-power=17: decode_failures 4
- RF-txpower: tx-power=14: decode_failures 1
- RF-txpower: slower: 3.45 s per simulated hour against 1.59 over 15 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-favourites: favourite-routers=False: decode_failures 21
- RT-favourites: favourite-routers=True: decode_failures 30
- RT-favourites: slower: 9.31 s per simulated hour against 1.69 over 15 prior run(s) - 5.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 22
- RT-hopassign: hop-assign=random: decode_failures 44
- RT-hopassign: slower: 7.81 s per simulated hour against 1.77 over 15 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hoplimit: hop-limit=3: decode_failures 41
- RT-hoplimit: hop-limit=7: decode_failures 45
- RT-hoplimit: hop-limit=15: decode_failures 23
- RT-hoplimit: hop-limit=32: decode_failures 32
- RT-hoplimit: slower: 11.6 s per simulated hour against 1.82 over 15 prior run(s) - 6.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopspread: hop-limit=3: decode_failures 41
- RT-hopspread: hop-limit=5: decode_failures 52
- RT-hopspread: hop-limit=7: decode_failures 45
- RT-hopspread: slower: 14.7 s per simulated hour against 2.03 over 15 prior run(s) - 7.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 22
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 22
- RT-rebroadcast: slower: 5.61 s per simulated hour against 1.59 over 15 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-spread: hop-spread=False: decode_failures 41
- RT-spread: hop-spread=True: decode_failures 22
- RT-spread: slower: 8.42 s per simulated hour against 2.08 over 15 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 22
- SC-signing: signature-policy=BALANCED: decode_failures 22
- SC-signing: signature-policy=STRICT: decode_failures 36
- SC-signing: slower: 8.97 s per simulated hour against 1.87 over 15 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 22
- SF-advert-transport: slower: 5.06 s per simulated hour against 1.85 over 15 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 30
- SF-bucket-mode: bucket-mode=local: decode_failures 22
- SF-bucket-mode: bucket-mode=time: misdecodes 15
- SF-bucket-mode: bucket-mode=window: misdecodes 25
- SF-bucket-mode: bucket-mode=window: decode_failures 3
- SF-bucket-mode: slower: 4.05 s per simulated hour against 1.56 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-time: time-bucket-s=600: misdecodes 84
- SF-bucket-time: time-bucket-s=1800: misdecodes 15
- SF-bucket-time: time-bucket-s=3600: misdecodes 10
- SF-bucket-time: time-bucket-s=3600: decode_failures 16
- SF-bucket-time: slower: 3.99 s per simulated hour against 1.62 over 15 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-cadence: trigger=bucket: decode_failures 22
- SF-cadence: trigger=interval: misdecodes 14
- SF-cadence: trigger=interval: decode_failures 9
- SF-cadence: trigger=aimd: misdecodes 6
- SF-cadence: trigger=aimd: decode_failures 27
- SF-cadence: trigger=bucket+interval: misdecodes 20
- SF-cadence: trigger=bucket+interval: decode_failures 5
- SF-cadence: slower: 6.77 s per simulated hour against 2.9 over 15 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 64
- SF-capacity-local: capacity=8: decode_failures 41
- SF-capacity-local: capacity=16: decode_failures 47
- SF-capacity-local: capacity=32: decode_failures 22
- SF-capacity-local: capacity=50: decode_failures 15
- SF-capacity-local: slower: 5.66 s per simulated hour against 1.77 over 15 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity: capacity=4: decode_failures 64
- SF-capacity: capacity=8: decode_failures 41
- SF-capacity: capacity=16: decode_failures 47
- SF-capacity: capacity=32: decode_failures 22
- SF-capacity: capacity=50: decode_failures 15
- SF-capacity: slower: 5.71 s per simulated hour against 1.69 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-window: capacity=8: misdecodes 4
- SF-capacity-window: capacity=8: decode_failures 62
- SF-capacity-window: capacity=16: misdecodes 14
- SF-capacity-window: capacity=16: decode_failures 54
- SF-capacity-window: capacity=32: misdecodes 25
- SF-capacity-window: capacity=32: decode_failures 3
- SF-capacity-window: slower: 3.44 s per simulated hour against 1.61 over 15 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 20
- SF-catchup: catch-up-hours=: decode_failures 5
- SF-catchup: catch-up-hours=02-06: decode_failures 50
- SF-catchup: catch-up-hours=00-08: decode_failures 52
- SF-hops-flat: hops-apart=2: decode_failures 22
- SF-hops-flat: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=2: decode_failures 22
- SF-hops-spread: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=5: decode_failures 7
- SF-jitter-global: advert-jitter-s=1: decode_failures 28
- SF-jitter-global: advert-jitter-s=30: decode_failures 22
- SF-jitter-global: advert-jitter-s=120: decode_failures 32
- SF-jitter-global: advert-jitter-s=600: decode_failures 55
- SF-jitter-global: slower: 9.79 s per simulated hour against 1.74 over 15 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 28
- SF-jitter-local: advert-jitter-s=30: decode_failures 22
- SF-jitter-local: advert-jitter-s=120: decode_failures 32
- SF-jitter-local: advert-jitter-s=600: decode_failures 55
- SF-jitter-local: slower: 11.8 s per simulated hour against 1.77 over 15 prior run(s) - 6.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 28
- SF-place-flat: place=hops-apart: decode_failures 22
- SF-place-spread: place=spread: decode_failures 28
- SF-place-spread: place=hops-apart: decode_failures 22
- SF-provide-transport: provide-transport=dm: decode_failures 22
- SF-provide-transport: provide-transport=broadcast: decode_failures 37
- SF-provide-transport: slower: 9.85 s per simulated hour against 1.93 over 15 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 37
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 4
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 44
- SF-replay-order-broadcast: slower: 12.9 s per simulated hour against 1.57 over 15 prior run(s) - 8.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 22
- SF-replay-order: replay-ordering=heard: misdecodes 8
- SF-replay-order: replay-ordering=heard: decode_failures 28
- SF-replay-order: slower: 8.47 s per simulated hour against 1.79 over 15 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-resolve: resolve=sketch: decode_failures 24
- SF-resolve: resolve=hybrid: decode_failures 22
- SF-resolve: slower: 5.79 s per simulated hour against 1.53 over 15 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=2: decode_failures 20
- SF-servers-flat: servers=3: decode_failures 22
- SF-servers-flat: servers=5: decode_failures 44
- SF-servers-flat: slower: 6.68 s per simulated hour against 2.6 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=2: decode_failures 20
- SF-servers-spread: servers=3: decode_failures 22
- SF-servers-spread: servers=5: decode_failures 44
- SF-servers-spread: slower: 8.43 s per simulated hour against 2.29 over 15 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 22
- SF-signed: signed=True: decode_failures 22
- SF-signed: slower: 7.94 s per simulated hour against 1.74 over 15 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 19
- SF-sr-retries: sr-retries=1: decode_failures 10
- SF-sr-retries: sr-retries=2: decode_failures 19
- SF-sr-retries: sr-retries=4: decode_failures 25
- SF-sr-retries: slower: 9.44 s per simulated hour against 1.67 over 15 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 50
- SF-width: short-id-bits=24: decode_failures 41
- SF-width: short-id-bits=32: decode_failures 22
- SF-width: short-id-bits=64: decode_failures 53
- SF-width: slower: 13.4 s per simulated hour against 1.77 over 15 prior run(s) - 7.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 97
- SF-window-size: window-size=16: misdecodes 48
- SF-window-size: window-size=32: misdecodes 25
- SF-window-size: window-size=32: decode_failures 3
- TH-congestion-input: congestion-input=hotstore: decode_failures 4
- TH-congestion-input: congestion-input=truesize: decode_failures 1
- TH-congestion: no-congestion-scaling=True: queue drops 16.2% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 53

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `LD-interval` | 13.8 | 1.4 | 9.84x | 15 |
| `SF-replay-order-broadcast` | 12.9 | 1.57 | 8.23x | 15 |
| `SF-width` | 13.4 | 1.77 | 7.58x | 15 |
| `RT-hopspread` | 14.7 | 2.03 | 7.25x | 15 |
| `SF-jitter-local` | 11.8 | 1.77 | 6.69x | 15 |
| `FW-signing-cost` | 10.4 | 1.58 | 6.56x | 15 |
| `RT-hoplimit` | 11.6 | 1.82 | 6.36x | 15 |
| `PR-repeats` | 9.47 | 1.68 | 5.65x | 15 |
| `SF-sr-retries` | 9.44 | 1.67 | 5.65x | 15 |
| `SF-jitter-global` | 9.79 | 1.74 | 5.62x | 15 |
| `RT-favourites` | 9.31 | 1.69 | 5.50x | 15 |
| `MS-roles` | 9.27 | 1.73 | 5.34x | 15 |
| `AD-worst` | 20.3 | 3.86 | 5.25x | 15 |
| `SF-provide-transport` | 9.85 | 1.93 | 5.12x | 15 |
| `PR-dmmode-cr` | 12.1 | 2.5 | 4.85x | 15 |
| `SC-signing` | 8.97 | 1.87 | 4.79x | 15 |
| `SF-replay-order` | 8.47 | 1.79 | 4.72x | 15 |
| `MS-router-late` | 8.05 | 1.76 | 4.59x | 15 |
| `SF-signed` | 7.94 | 1.74 | 4.56x | 15 |
| `LD-diurnal` | 7.04 | 1.58 | 4.45x | 15 |
| `RT-hopassign` | 7.81 | 1.77 | 4.41x | 15 |
| `RT-spread` | 8.42 | 2.08 | 4.06x | 15 |
| `DM-mode` | 10.8 | 2.7 | 4.01x | 15 |
| `DG-loss` | 8.56 | 2.18 | 3.93x | 15 |
| `AD-siting` | 5.05 | 1.29 | 3.92x | 15 |
| `RF-eu-presets` | 7.74 | 2.03 | 3.81x | 15 |
| `SF-resolve` | 5.79 | 1.53 | 3.79x | 15 |
| `FW-mixed` | 6.43 | 1.7 | 3.77x | 15 |
| `SF-servers-spread` | 8.43 | 2.29 | 3.69x | 15 |
| `LD-traceroute` | 7.6 | 2.1 | 3.62x | 15 |
| `RT-rebroadcast` | 5.61 | 1.59 | 3.54x | 15 |
| `AD-badrouters` | 7.39 | 2.1 | 3.53x | 15 |
| `RF-duct` | 6.17 | 1.82 | 3.39x | 15 |
| `DB-platform` | 8.72 | 2.58 | 3.39x | 15 |
| `SF-capacity` | 5.71 | 1.69 | 3.39x | 15 |
| `DB-hotstore` | 8.62 | 2.57 | 3.35x | 15 |
| `PR-crladder` | 9.12 | 2.75 | 3.31x | 15 |
| `AD-flooding` | 8.36 | 2.57 | 3.25x | 15 |
| `SF-capacity-local` | 5.66 | 1.77 | 3.21x | 15 |
| `FW-mixed-26` | 5.41 | 1.71 | 3.17x | 15 |
| `LD-chatty` | 13.8 | 4.58 | 3.01x | 15 |
| `SF-advert-transport` | 5.06 | 1.85 | 2.73x | 15 |
| `AD-nomute` | 6.27 | 2.32 | 2.71x | 15 |
| `RF-noise` | 13.1 | 4.91 | 2.66x | 15 |
| `FW-firmware` | 4.75 | 1.8 | 2.65x | 15 |
| `MS-roles-fav` | 4.64 | 1.75 | 2.65x | 15 |
| `RF-pulse` | 4.16 | 1.6 | 2.59x | 15 |
| `SF-bucket-mode` | 4.05 | 1.56 | 2.59x | 15 |
| `SF-servers-flat` | 6.68 | 2.6 | 2.57x | 15 |
| `SF-bucket-time` | 3.99 | 1.62 | 2.45x | 15 |
| `PR-protocol` | 3.37 | 1.42 | 2.38x | 15 |
| `SF-cadence` | 6.77 | 2.9 | 2.34x | 15 |
| `LD-chatty-hops` | 8.41 | 3.72 | 2.26x | 15 |
| `RF-preset-turbo` | 3.49 | 1.59 | 2.20x | 11 |
| `RF-txpower` | 3.45 | 1.59 | 2.17x | 15 |
| `AD-amplifiers` | 3.65 | 1.68 | 2.17x | 15 |
| `AD-amplify-worst` | 3.65 | 1.69 | 2.16x | 15 |
| `SF-capacity-window` | 3.44 | 1.61 | 2.13x | 15 |
| `MS-topology` | 3.39 | 1.86 | 1.82x | 15 |
| `DG-burst` | 8.62 | 4.88 | 1.77x | 15 |
| `FW-versions` | 2.75 | 1.63 | 1.68x | 15 |
| `SF-place-flat` | 4.66 | 2.86 | 1.63x | 15 |
| `MS-siting` | 2.8 | 1.77 | 1.59x | 15 |
| `MS-stretch` | 3.11 | 1.99 | 1.56x | 15 |
| `BL-control` | 1.12 | 1.74 | 0.64x | 15 |
| `RF-stretch-duct` | 1.66 | 2.97 | 0.56x | 15 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.998 | 0.998 | 0.901 → 0.902 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.957 | 0.957 | 0.892 → 0.901 | 1.2x bytes_on_air | up | 3 |
| `AD-siting` | siting-mix | **text** | 0.039 → 0.850 | 0.812 | 0.038 → 0.843 | 20x sr_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.132 → 0.914 | 0.782 | 0.129 → 0.851 | 1.1e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.122 → 0.902 | 0.780 | 0.121 → 0.895 | 4.5x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **text** | 0.141 → 0.902 | 0.761 | 0.137 → 0.895 | 2.8x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **held** | 0.332 → 0.996 | 0.664 | 0.614 → 0.974 | 6.2x sr_bytes | up | 4 |
| `MS-stretch` | stretch | **text** | 0.240 → 0.902 | 0.662 | 0.235 → 0.895 | 3.1x sr_airtime | down | 4 |
| `MS-hopscale` | nodes | **text** | 0.314 → 0.902 | 0.587 | 0.311 → 0.895 | 8.1x bytes_on_air | down | 4 |
| `RF-bw500` | preset | **text** | 0.294 → 0.867 | 0.572 | 0.288 → 0.859 | 2.3x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.423 → 0.932 | 0.509 | 0.309 → 0.675 | 4.7x bytes_on_air | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.514 → 0.902 | 0.387 | 0.491 → 0.895 | 2x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.514 → 0.902 | 0.387 | 0.491 → 0.895 | 2.2x sr_airtime | up | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.605 → 0.924 | 0.319 | 0.593 → 0.920 | 9.2x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.647 → 0.951 | 0.303 | 0.640 → 0.948 | 8.8x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.600 → 0.902 | 0.302 | 0.577 → 0.895 | 1.3x advert_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.613 → 0.902 | 0.289 | 0.582 → 0.895 | 1.3x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.682 → 0.941 | 0.258 | 0.672 → 0.939 | 3.2x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.434 → 0.692 | 0.258 | 0.277 → 0.464 | 5.8x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.521 → 0.767 | 0.246 | 0.508 → 0.756 | 1.5x sr_airtime | up | 2 |
| `MS-size` | nodes | **text** | 0.658 → 0.902 | 0.244 | 0.642 → 0.895 | 5.1x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.717 → 0.950 | 0.232 | 0.710 → 0.947 | 4.8x sr_airtime | down | 2 |
| `MS-density` | nodes | **held** | 0.768 → 0.996 | 0.228 | 0.749 → 0.955 | 5.5x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.764 → 0.951 | 0.187 | 0.736 → 0.949 | 1.4x bytes_on_air | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.764 → 0.945 | 0.182 | 0.736 → 0.941 | 1.4x bytes_on_air | up | 3 |
| `SC-signing` | signature-policy | **held** | 0.803 → 0.957 | 0.154 | 0.762 → 0.895 | 1.4x sr_airtime | down | 3 |
| `RF-noise` | noise-profile | **held** | 0.804 → 0.957 | 0.153 | 0.747 → 0.895 | 1.2x sr_airtime | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.764 → 0.902 | 0.138 | 0.736 → 0.895 | 1.5x sr_bytes | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.827 → 0.957 | 0.130 | 0.895 → 0.903 | 32x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.864 → 0.985 | 0.122 | 0.882 → 0.897 | 13x advert_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.851 → 0.961 | 0.110 | 0.900 → 0.901 | 5.1x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **held** | 0.885 → 0.994 | 0.109 | 0.843 → 0.945 | 3.3x sr_bytes | up | 2 |
| `AD-nomute` | role-mix | **held** | 0.885 → 0.994 | 0.109 | 0.843 → 0.945 | 3.3x sr_bytes | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.883 → 0.989 | 0.106 | 0.891 → 0.905 | 4.5x advert_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.883 → 0.989 | 0.106 | 0.891 → 0.905 | 4.5x advert_bytes | up | 4 |
| `AD-badrouters` | role-placement | **held** | 0.885 → 0.982 | 0.097 | 0.843 → 0.865 | 1.7x sr_bytes | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.815 → 0.902 | 0.087 | 0.805 → 0.895 | 1.2x sr_airtime | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.916 → 0.998 | 0.082 | 0.895 → 0.904 | 3.2x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.916 → 0.998 | 0.082 | 0.895 → 0.904 | 3.2x sr_bytes | down | 5 |
| `SF-catchup` | catch-up-hours | **held** | 0.906 → 0.985 | 0.079 | 0.886 → 0.900 | 9.3x advert_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.882 → 0.957 | 0.075 | 0.895 → 0.902 | 5.8x advert_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.864 → 0.933 | 0.069 | 0.858 → 0.931 | 2.2x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.647 → 0.713 | 0.066 | 0.641 → 0.707 | 1.3x sr_airtime | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.870 → 0.933 | 0.064 | 0.863 → 0.931 | 2.2x sr_airtime | down | 3 |
| `MS-roles` | role-mix | **held** | 0.885 → 0.945 | 0.060 | 0.843 → 0.890 | 1.2x sr_bytes | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.875 → 0.932 | 0.057 | 0.867 → 0.929 | 5.2x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.902 → 0.957 | 0.055 | 0.895 → 0.957 | 3.7x sr_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.861 → 0.913 | 0.052 | 0.855 → 0.907 | 1.1x sr_bytes | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.902 → 0.949 | 0.047 | 0.895 → 0.944 | 1.6x sr_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.938 → 0.985 | 0.047 | 0.895 → 0.911 | 2.3x sr_bytes | up | 4 |
| `SF-place-flat` | place | **held** | 0.948 → 0.994 | 0.046 | 0.895 → 0.905 | 2.7x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.948 → 0.994 | 0.046 | 0.895 → 0.905 | 2.7x sr_bytes | up | 6 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.957 → 0.999 | 0.042 | 0.895 → 0.935 | 2x sr_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.890 → 0.931 | 0.041 | 0.884 → 0.926 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.957 → 0.996 | 0.039 | 0.891 → 0.927 | 2.2x sr_bytes | up | 4 |
| `FW-versions` | profile | **held** | 0.957 → 0.996 | 0.038 | 0.895 → 0.928 | 3.4x bytes_on_air | down | 5 |
| `SF-sr-retries` | sr-retries | **held** | 0.930 → 0.969 | 0.038 | 0.897 → 0.902 | 1.3x sr_bytes | up | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.684 → 0.722 | 0.038 | 0.459 → 0.493 | 1.5x sr_airtime | up | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.922 → 0.957 | 0.035 | 0.892 → 0.895 | 3.4x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.957 → 0.988 | 0.031 | 0.895 → 0.903 | 2.5x sr_airtime | up | 2 |
| `FW-firmware` | profile | **held** | 0.957 → 0.987 | 0.030 | 0.895 → 0.911 | 3.3x bytes_on_air | down | 2 |
| `AD-worst` | role-placement | **text** | 0.715 → 0.745 | 0.030 | 0.699 → 0.735 | 1.1x sr_bytes | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.901 → 0.930 | 0.029 | 0.896 → 0.927 | 1.1x bytes_on_air | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.873 → 0.902 | 0.029 | 0.864 → 0.895 | 1.8x sr_airtime | down | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.957 → 0.985 | 0.028 | 0.895 → 0.901 | 2.2x advert_bytes | down | 4 |
| `LD-diurnal` | diurnal | **held** | 0.952 → 0.978 | 0.027 | 0.895 → 0.912 | 1.3x sr_bytes | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.902 → 0.928 | 0.027 | 0.895 → 0.924 | 3.2x bytes_on_air | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.962 → 0.985 | 0.023 | 0.892 → 0.902 | 5.2x advert_bytes | down | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.880 → 0.902 | 0.022 | 0.869 → 0.895 | 1.3x sr_bytes | down | 2 |
| `SF-capacity` | capacity | **held** | 0.942 → 0.958 | 0.017 | 0.895 → 0.903 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.942 → 0.958 | 0.017 | 0.895 → 0.903 | 5.4x advert_bytes | up | 5 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.944 → 0.959 | 0.015 | 0.894 → 0.900 | 1.3x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.944 → 0.959 | 0.015 | 0.894 → 0.900 | 1.3x sr_airtime | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.871 → 0.883 | 0.012 | 0.871 → 0.883 | 1.1x sr_bytes | up | 3 |
| `SF-servers-allrouters` | servers | **held** | 0.986 → 0.997 | 0.011 | 0.900 → 0.901 | 2.3x sr_bytes | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.947 → 0.957 | 0.011 | 0.895 → 0.905 | 3.1x advert_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **held** | 0.948 → 0.957 | 0.009 | 0.895 → 0.901 | 1.1x sr_bytes | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.896 → 0.905 | 0.009 | 0.882 → 0.886 | 1.1x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **text** | 0.898 → 0.906 | 0.008 | 0.891 → 0.901 | 4x advert_bytes | up | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.950 → 0.957 | 0.007 | 0.895 → 0.901 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.922 → 0.928 | 0.007 | 0.886 → 0.892 | 1.1x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.944 → 0.950 | 0.005 | 0.942 → 0.947 | 1.2x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.950 → 0.955 | 0.005 | 0.947 → 0.953 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.950 → 0.952 | 0.003 | 0.947 → 0.950 | 1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.896 → 0.897 | 0.001 | 0.882 → 0.883 | 1.1x sr_airtime | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario rolling`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| sprinkled | 1 | 0.909 | 0.904 | 0.005 | - | - | 0.980 | 0.982 | 0.365 | 1.19x | 19.2/26.4/32.3% | 1.6/5.5% | 3 |
| arms-race | 1 | 0.957 | 0.957 | 0.000 | - | - | 0.978 | 0.978 | 0.896 | 0.94x | 22.2/27.3/29.1% | 1.1/5.3% | 3 |

> amplifier-mix=none: decode_failures 22

> slower: 3.65 s per simulated hour against 1.68 over 15 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.913 | 0.909 | 0.004 | - | - | 0.988 | 0.990 | 0.717 | 1.17x | 19.2/24.2/28.6% | 1.7/5.1% | 3 |
| 0.3 | 1 | 0.939 | 0.935 | 0.004 | - | - | 0.999 | 0.999 | 0.838 | 1.06x | 22.3/29.8/32.3% | 1.5/4.9% | 3 |

> amplify-worst=0.0: decode_failures 22

> slower: 3.65 s per simulated hour against 1.69 over 15 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.850 | 0.843 | 0.007 | - | - | 0.885 | 0.939 | 0.424 | 1.15x | 16.0/24.2/29.3% | 1.9/5.1% | 3 |
| inverse | 1 | 0.863 | 0.852 | 0.011 | - | - | 0.917 | 0.953 | 0.540 | 1.15x | 15.5/20.4/24.8% | 2.0/3.4% | 3 |
| random | 1 | 0.876 | 0.865 | 0.011 | - | - | 0.982 | 0.985 | 0.575 | 1.18x | 16.5/21.8/24.7% | 2.0/5.2% | 3 |

> role-placement=degree: decode_failures 41

> role-placement=inverse: decode_failures 23

> slower: 7.39 s per simulated hour against 2.1 over 15 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.850 | 0.843 | 0.007 | - | - | 0.885 | 0.939 | 0.424 | 1.15x | 16.0/24.2/29.3% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.946 | 0.945 | 0.000 | - | - | 0.994 | 0.994 | 0.781 | 2.93x | 38.0/48.6/52.4% | 4.7/5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 41

> slower: 8.36 s per simulated hour against 2.57 over 15 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.850 | 0.843 | 0.007 | - | - | 0.885 | 0.939 | 0.424 | 1.15x | 16.0/24.2/29.3% | 1.9/5.1% | 3 |
| no-mute | 1 | 0.892 | 0.885 | 0.008 | - | - | 0.964 | 0.971 | 0.617 | 1.25x | 17.6/24.0/26.4% | 1.9/5.3% | 3 |
| all-routers | 1 | 0.946 | 0.945 | 0.000 | - | - | 0.994 | 0.994 | 0.781 | 2.93x | 38.0/48.6/52.4% | 4.7/5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 41

> slower: 6.27 s per simulated hour against 2.32 over 15 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.850 | 0.843 | 0.007 | - | - | 0.885 | 0.939 | 0.424 | 1.15x | 16.0/24.2/29.3% | 1.9/5.1% | 3 |
| local-typical | 1 | 0.573 | 0.572 | 0.001 | - | - | 0.322 | 0.732 | 0.000 | 1.12x | 9.5/18.6/30.2% | 1.8/5.0% | 3 |
| basement-heavy | 1 | 0.039 | 0.038 | 0.000 | - | - | 0.078 | 0.118 | 0.000 | 0.37x | 0.7/3.4/6.3% | 0.3/2.1% | 3 |

> siting-mix=uniform: decode_failures 41

> siting-mix=local-typical: decode_failures 4

> siting-mix=basement-heavy: decode_failures 1

> slower: 5.05 s per simulated hour against 1.29 over 15 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.745 | 0.735 | 0.010 | - | - | 0.903 | 0.911 | 0.000 | 2.35x | 13.6/25.2/35.0% | 1.8/5.6% | 3 |
| inverse | 1 | 0.715 | 0.699 | 0.016 | - | - | 0.908 | 0.918 | 0.000 | 2.25x | 12.6/22.2/32.0% | 1.8/3.1% | 3 |

> role-placement=degree: decode_failures 74

> role-placement=inverse: decode_failures 69

> slower: 20.3 s per simulated hour against 3.86 over 15 prior run(s) - 5.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.901 | 0.901 | 0.000 | - | - | 0 | 0.000 | 0.585 | 1.27x | 18.1/24.6/28.9% | 1.8/5.2% | 3 |
| sr | 1 | 0.913 | 0.902 | 0.011 | - | - | 0.998 | 0.998 | 0.617 | 1.32x | 18.8/25.5/30.1% | 1.9/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.864 | 0.858 | 0.006 | - | - | 0.941 | 0.969 | 0.649 | 3.12x | 43.2/60.2/67.0% | 4.7/11.0% | 3 |
| 100 | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.957 | 0.992 | 0.596 | 1.54x | 22.2/32.4/36.9% | 2.2/5.7% | 3 |
| 120 | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.957 | 0.992 | 0.596 | 1.54x | 22.2/32.4/36.9% | 2.2/5.7% | 3 |
| 250 | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.957 | 0.992 | 0.596 | 1.54x | 22.2/32.4/36.9% | 2.2/5.7% | 3 |

> max-num-nodes=10: decode_failures 27

> max-num-nodes=100: decode_failures 20

> max-num-nodes=120: decode_failures 20

> max-num-nodes=250: decode_failures 20

> slower: 8.62 s per simulated hour against 2.57 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.282 | 0.277 | 0.005 | - | - | 0.434 | 0.505 | 0.157 | 11.04x | 37.0/56.1/75.0% | 3.9/11.2% | 3 |
| 120 | 1 | 0.469 | 0.459 | 0.010 | - | - | 0.684 | 0.686 | 0.222 | 4.37x | 14.5/27.9/41.7% | 1.5/5.1% | 3 |
| 250 | 1 | 0.475 | 0.464 | 0.012 | - | - | 0.692 | 0.695 | 0.225 | 4.24x | 14.1/26.9/40.4% | 1.5/5.0% | 3 |

> max-num-nodes=10: decode_failures 67

> max-num-nodes=120: decode_failures 4

> max-num-nodes=250: decode_failures 1

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.957 | 0.992 | 0.596 | 1.54x | 22.2/32.4/36.9% | 2.2/5.7% | 3 |
| baymesh-2026-08 | 1 | 0.933 | 0.931 | 0.002 | - | - | 0.957 | 0.992 | 0.596 | 1.54x | 22.2/32.4/36.9% | 2.2/5.7% | 3 |
| constrained | 1 | 0.870 | 0.863 | 0.006 | - | - | 0.947 | 0.970 | 0.660 | 3.12x | 43.3/60.3/67.1% | 4.7/11.0% | 3 |

> platform-mix=uniform: decode_failures 20

> platform-mix=baymesh-2026-08: decode_failures 20

> platform-mix=constrained: decode_failures 28

> slower: 8.72 s per simulated hour against 2.58 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.713 | 0.707 | 0.007 | - | - | 0.828 | 0.894 | 0.544 | 5.54x | 54.6/75.9/79.2% | 4.0/12.7% | 3 |
| 25 | 1 | 0.713 | 0.707 | 0.007 | - | - | 0.828 | 0.894 | 0.544 | 5.54x | 54.6/75.9/79.2% | 4.0/12.7% | 3 |
| 100 | 1 | 0.713 | 0.707 | 0.007 | - | - | 0.828 | 0.894 | 0.544 | 5.54x | 54.6/75.9/79.2% | 4.0/12.7% | 3 |
| 2000 | 1 | 0.713 | 0.707 | 0.007 | - | - | 0.828 | 0.894 | 0.544 | 5.54x | 54.6/75.9/79.2% | 4.0/12.7% | 3 |

> warm-num-nodes=0: queue drops 16.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 122

> warm-num-nodes=25: queue drops 16.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 122

> warm-num-nodes=100: queue drops 16.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 122

> warm-num-nodes=2000: queue drops 16.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 122

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.812 | 0.798 | 0.014 | - | - | 0.881 | 0.962 | 0.500 | 1.23x | 17.8/24.6/29.0% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.721 | 0.690 | 0.031 | - | - | 0.884 | 0.943 | 0.455 | 1.18x | 17.3/23.8/27.9% | 1.8/4.6% | 3 |
| 0.3 | 1 | 0.613 | 0.582 | 0.031 | - | - | 0.744 | 0.881 | 0.353 | 1.08x | 16.4/22.6/26.3% | 1.7/4.1% | 3 |

> burst-loss=0.0: decode_failures 22

> burst-loss=0.1: decode_failures 23

> burst-loss=0.2: decode_failures 19

> burst-loss=0.3: decode_failures 32

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.880 | 0.874 | 0.006 | - | - | 0.939 | 0.982 | 0.576 | 1.36x | 19.6/26.5/30.9% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.852 | 0.845 | 0.008 | - | - | 0.921 | 0.982 | 0.526 | 1.43x | 21.1/28.3/32.5% | 2.2/5.3% | 3 |
| 0.3 | 1 | 0.815 | 0.805 | 0.010 | - | - | 0.910 | 0.975 | 0.505 | 1.45x | 21.7/29.0/33.0% | 2.2/5.1% | 3 |

> extra-loss=0.0: decode_failures 22

> extra-loss=0.1: decode_failures 34

> extra-loss=0.2: decode_failures 30

> extra-loss=0.3: decode_failures 14

> slower: 8.56 s per simulated hour against 2.18 over 15 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.795 | 0.784 | 0.012 | - | - | 0.885 | 0.966 | 0.479 | 1.24x | 17.9/24.4/29.0% | 1.9/5.0% | 3 |
| 0.2 | 1 | 0.707 | 0.686 | 0.021 | - | - | 0.839 | 0.960 | 0.435 | 1.18x | 17.4/23.8/28.1% | 1.8/5.1% | 3 |
| 0.3 | 1 | 0.600 | 0.577 | 0.023 | - | - | 0.729 | 0.895 | 0.327 | 1.11x | 16.9/23.1/27.5% | 1.7/4.4% | 3 |

> burst-loss=0.0: decode_failures 22

> burst-loss=0.1: decode_failures 43

> burst-loss=0.2: decode_failures 26

> burst-loss=0.3: decode_failures 28

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.871 | 0.871 | 0.000 | - | - | 0.900 | 0.983 | 0.574 | 1.78x | 25.1/34.4/40.3% | 2.6/7.2% | 3 |
| directed-with-late-flood | 1 | 0.883 | 0.883 | 0.000 | - | - | 0.897 | 0.982 | 0.570 | 1.60x | 22.9/31.4/36.9% | 2.3/6.7% | 3 |
| m4-early-flood | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.895 | 0.982 | 0.585 | 1.59x | 22.8/31.3/36.8% | 2.3/6.7% | 3 |

> dm-mode=flood-only: decode_failures 28

> dm-mode=directed-with-late-flood: decode_failures 31

> dm-mode=m4-early-flood: decode_failures 32

> slower: 10.8 s per simulated hour against 2.7 over 15 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.913 | 0.911 | 0.003 | - | - | 0.987 | 0.987 | 0.549 | 0.71x | 9.5/11.7/13.2% | 1.1/2.2% | 3 |
| 2.8 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> profile=2.8: decode_failures 22

> slower: 4.75 s per simulated hour against 1.8 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.959 | 0.996 | 0.590 | 1.13x | 15.1/21.9/26.1% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.897 | 0.891 | 0.006 | - | - | 0.978 | 0.992 | 0.392 | 1.02x | 14.4/19.7/21.7% | 1.6/4.2% | 3 |
| 0.75 | 1 | 0.933 | 0.927 | 0.006 | - | - | 0.996 | 0.997 | 0.809 | 0.84x | 12.6/15.6/19.0% | 1.3/2.6% | 3 |

> legacy-fraction=0.0: decode_failures 22

> legacy-fraction=0.25: decode_failures 46

> legacy-fraction=0.5: decode_failures 2

> slower: 6.43 s per simulated hour against 1.7 over 15 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.983 | 0.996 | 0.619 | 1.15x | 15.2/22.2/26.2% | 1.8/4.9% | 3 |
| 0.5 | 1 | 0.890 | 0.884 | 0.007 | - | - | 0.963 | 0.994 | 0.346 | 1.00x | 14.1/19.5/21.5% | 1.5/4.3% | 3 |
| 0.75 | 1 | 0.931 | 0.926 | 0.005 | - | - | 0.997 | 0.997 | 0.800 | 0.84x | 12.7/15.6/19.3% | 1.3/2.6% | 3 |

> legacy-fraction=0.0: decode_failures 22

> legacy-fraction=0.25: decode_failures 13

> legacy-fraction=0.5: decode_failures 20

> slower: 5.41 s per simulated hour against 1.71 over 15 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.928 | 0.924 | 0.004 | - | - | 0.955 | 0.992 | 0.545 | 0.70x | 10.2/14.7/17.4% | 1.0/3.2% | 3 |
| signing=true | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> profile-flag=signing=false: decode_failures 41

> profile-flag=signing=true: decode_failures 22

> slower: 10.4 s per simulated hour against 1.58 over 15 prior run(s) - 6.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.910 | 0.906 | 0.003 | - | - | 0.991 | 0.992 | 0.559 | 0.71x | 9.9/12.7/14.6% | 1.2/2.3% | 3 |
| 2.5 | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.991 | 0.991 | 0.578 | 0.72x | 10.0/12.7/14.6% | 1.2/2.3% | 3 |
| 2.6 | 1 | 0.910 | 0.907 | 0.003 | - | - | 0.990 | 0.990 | 0.574 | 0.68x | 9.7/12.5/14.3% | 1.1/2.3% | 3 |
| 2.7 | 1 | 0.929 | 0.928 | 0.001 | - | - | 0.996 | 0.996 | 0.598 | 0.75x | 10.4/18.0/19.8% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> profile=2.8: decode_failures 22

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.947 | 0.991 | 0.574 | 0.88x | 12.3/16.9/19.8% | 1.2/3.7% | 3 |
| 900 | 1 | 0.875 | 0.867 | 0.008 | - | - | 0.950 | 0.985 | 0.619 | 2.14x | 30.2/41.4/48.1% | 3.2/8.8% | 3 |
| 300 | 1 | 0.605 | 0.593 | 0.012 | - | - | 0.769 | 0.869 | 0.357 | 4.52x | 60.1/72.8/79.3% | 7.0/17.8% | 3 |

> broadcast-interval-s=3600: decode_failures 45

> broadcast-interval-s=900: decode_failures 35

> broadcast-interval-s=300: queue drops 10.3% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 37

> slower: 13.8 s per simulated hour against 4.58 over 15 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.951 | 0.948 | 0.003 | - | - | 0.983 | 0.989 | 0.604 | 0.92x | 12.6/16.8/19.9% | 1.3/3.7% | 3 |
| 900 | 1 | 0.922 | 0.916 | 0.006 | - | - | 0.950 | 0.975 | 0.586 | 2.28x | 31.7/41.9/48.8% | 3.3/8.8% | 3 |
| 300 | 1 | 0.647 | 0.640 | 0.007 | - | - | 0.740 | 0.818 | 0.440 | 4.96x | 63.3/73.9/79.7% | 7.8/18.4% | 3 |

> broadcast-interval-s=3600: decode_failures 1

> broadcast-interval-s=900: decode_failures 22

> broadcast-interval-s=300: queue drops 14.7% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 29

> slower: 8.41 s per simulated hour against 3.72 over 15 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.917 | 0.912 | 0.006 | - | - | 0.978 | 0.989 | 0.560 | 1.22x | 17.1/24.1/28.1% | 1.8/5.2% | 3 |
| sinusoid | 1 | 0.915 | 0.909 | 0.005 | - | - | 0.952 | 0.992 | 0.582 | 1.19x | 16.7/22.9/26.9% | 1.7/4.8% | 3 |
| commuter | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> diurnal=flat: decode_failures 13

> diurnal=sinusoid: decode_failures 18

> diurnal=commuter: decode_failures 22

> slower: 7.04 s per simulated hour against 1.58 over 15 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.875 | 0.867 | 0.008 | - | - | 0.950 | 0.985 | 0.619 | 2.14x | 30.2/41.4/48.1% | 3.2/8.8% | 3 |
| 3600 | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.947 | 0.991 | 0.574 | 0.88x | 12.3/16.9/19.8% | 1.2/3.7% | 3 |
| 10800 | 1 | 0.930 | 0.926 | 0.004 | - | - | 0.950 | 0.993 | 0.570 | 0.60x | 8.3/11.6/13.3% | 0.8/2.5% | 3 |
| 43200 | 1 | 0.932 | 0.929 | 0.003 | - | - | 0.941 | 0.992 | 0.570 | 0.43x | 6.0/8.5/9.6% | 0.6/1.9% | 3 |

> broadcast-interval-s=900: decode_failures 35

> broadcast-interval-s=3600: decode_failures 45

> broadcast-interval-s=10800: decode_failures 57

> broadcast-interval-s=43200: decode_failures 44

> slower: 13.8 s per simulated hour against 1.4 over 15 prior run(s) - 9.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.947 | 0.982 | 0.571 | 1.36x | 19.4/26.6/31.4% | 2.0/5.7% | 3 |
| 1.0 | 1 | 0.901 | 0.893 | 0.008 | - | - | 0.964 | 0.989 | 0.570 | 1.53x | 21.9/30.0/35.3% | 2.2/6.4% | 3 |
| 4.0 | 1 | 0.873 | 0.864 | 0.009 | - | - | 0.972 | 0.987 | 0.617 | 1.96x | 28.4/39.0/45.9% | 2.9/8.4% | 3 |

> traceroute-per-hour=0.0: decode_failures 22

> traceroute-per-hour=0.25: decode_failures 35

> traceroute-per-hour=1.0: decode_failures 15

> traceroute-per-hour=4.0: decode_failures 5

> slower: 7.6 s per simulated hour against 2.1 over 15 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.707 | 0.007 | - | - | 0.828 | 0.894 | 0.544 | 5.54x | 54.6/75.9/79.2% | 4.0/12.7% | 3 |
| 1.0 | 1 | 0.647 | 0.641 | 0.006 | - | - | 0.769 | 0.846 | 0.463 | 6.01x | 58.0/77.0/80.0% | 4.4/13.8% | 3 |

> traceroute-per-hour=0.0: queue drops 16.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 122

> traceroute-per-hour=1.0: queue drops 22.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 111

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.763 | 0.749 | 0.014 | - | - | 0.768 | 0.871 | 0.251 | 1.30x | 21.4/25.4/31.7% | 2.8/6.8% | 3 |
| 60 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 90 | 1 | 0.932 | 0.930 | 0.002 | - | - | 0.986 | 0.986 | 0.736 | 1.58x | 19.2/30.2/34.8% | 1.5/5.0% | 3 |
| 120 | 1 | 0.950 | 0.947 | 0.002 | - | - | 0.996 | 0.996 | 0.814 | 2.05x | 21.0/40.2/43.9% | 1.4/5.1% | 3 |
| 150 | 1 | 0.957 | 0.955 | 0.002 | - | - | 0.996 | 0.996 | 0.861 | 2.57x | 27.6/47.3/55.0% | 1.3/5.5% | 3 |

> nodes=40: decode_failures 12

> nodes=60: decode_failures 22

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 120 | 1 | 0.703 | 0.683 | 0.020 | - | - | 0.944 | 0.946 | 0.243 | 2.24x | 15.3/35.7/40.3% | 1.6/4.7% | 3 |
| 250 | 1 | 0.474 | 0.462 | 0.012 | - | - | 0.686 | 0.698 | 0.227 | 4.74x | 15.8/30.6/46.1% | 1.6/6.0% | 3 |
| 500 | 1 | 0.314 | 0.311 | 0.003 | - | - | 0.429 | 0.430 | 0.056 | 10.17x | 19.4/31.6/42.4% | 1.8/5.9% | 3 |

> nodes=60: decode_failures 22

> nodes=250: decode_failures 121

> nodes=500: decode_failures 21

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.696 | 0.675 | 0.022 | - | - | 0.932 | 0.937 | 0.240 | 2.02x | 13.6/31.9/36.2% | 1.4/4.2% | 3 |
| 250 | 1 | 0.469 | 0.459 | 0.010 | - | - | 0.684 | 0.686 | 0.222 | 4.37x | 14.5/27.9/41.7% | 1.5/5.1% | 3 |
| 500 | 1 | 0.312 | 0.309 | 0.003 | - | - | 0.423 | 0.424 | 0.059 | 9.48x | 18.0/29.2/39.1% | 1.6/5.5% | 3 |

> nodes=250: decode_failures 4

> nodes=500: decode_failures 5

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.897 | 0.890 | 0.007 | - | - | 0.945 | 0.983 | 0.550 | 1.29x | 18.5/25.3/29.7% | 1.9/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.850 | 0.843 | 0.007 | - | - | 0.885 | 0.939 | 0.424 | 1.15x | 16.0/24.2/29.3% | 1.9/5.1% | 3 |

> role-mix=legacy-default: decode_failures 39

> role-mix=baymesh-2026-08: decode_failures 41

> slower: 9.27 s per simulated hour against 1.73 over 15 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.913 | 0.907 | 0.006 | - | - | 0.952 | 0.978 | 0.606 | 1.36x | 18.9/26.2/30.3% | 1.9/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.861 | 0.855 | 0.006 | - | - | 0.921 | 0.922 | 0.436 | 1.27x | 17.8/27.8/32.4% | 2.1/5.0% | 3 |

> role-mix=legacy-default: decode_failures 29

> slower: 4.64 s per simulated hour against 1.75 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.05 | 1 | 0.904 | 0.901 | 0.004 | - | - | 0.948 | 0.987 | 0.629 | 1.45x | 20.4/31.8/36.4% | 2.0/5.5% | 3 |
| 0.1 | 1 | 0.914 | 0.911 | 0.003 | - | - | 0.938 | 0.996 | 0.633 | 1.57x | 22.7/32.9/39.6% | 2.1/5.6% | 3 |
| 0.2 | 1 | 0.913 | 0.910 | 0.003 | - | - | 0.985 | 0.985 | 0.703 | 1.74x | 24.3/40.3/44.5% | 2.4/5.3% | 3 |

> router-late-fraction=0.0: decode_failures 22

> router-late-fraction=0.05: decode_failures 37

> router-late-fraction=0.1: decode_failures 32

> slower: 8.05 s per simulated hour against 1.76 over 15 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| local-typical | 1 | 0.680 | 0.680 | 0.000 | - | - | 0.332 | 0.821 | 0.000 | 1.34x | 12.1/20.6/29.9% | 1.8/5.2% | 3 |
| event | 1 | 0.623 | 0.614 | 0.008 | - | - | 0.846 | 0.846 | 0.000 | 1.49x | 11.4/20.6/25.3% | 2.4/5.3% | 3 |
| backbone | 1 | 0.974 | 0.974 | 0.000 | - | - | 0.996 | 0.996 | 0.891 | 1.08x | 26.5/36.3/38.6% | 1.3/5.5% | 3 |

> siting-mix=uniform: decode_failures 22

> siting-mix=local-typical: decode_failures 3

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.877 | 0.857 | 0.019 | - | - | 0.973 | 0.975 | 0.634 | 1.44x | 23.8/31.0/35.3% | 3.0/7.5% | 3 |
| 60 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 90 | 1 | 0.791 | 0.780 | 0.011 | - | - | 0.941 | 0.942 | 0.256 | 1.74x | 15.6/28.5/32.3% | 1.6/5.2% | 3 |
| 120 | 1 | 0.703 | 0.683 | 0.020 | - | - | 0.944 | 0.946 | 0.243 | 2.24x | 15.3/35.7/40.3% | 1.6/4.7% | 3 |
| 150 | 1 | 0.658 | 0.642 | 0.016 | - | - | 0.851 | 0.853 | 0.375 | 2.64x | 14.1/29.9/38.3% | 1.5/5.2% | 3 |

> nodes=60: decode_failures 22

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 1.25 | 1 | 0.763 | 0.753 | 0.011 | - | - | 0.975 | 0.976 | 0.336 | 1.43x | 14.5/23.7/25.8% | 2.2/4.9% | 3 |
| 1.5 | 1 | 0.521 | 0.508 | 0.013 | - | - | 0.748 | 0.750 | 0.000 | 1.37x | 10.9/18.8/23.2% | 2.2/4.7% | 3 |
| 2.0 | 1 | 0.240 | 0.235 | 0.005 | - | - | 0.434 | 0.435 | 0.000 | 1.22x | 7.1/16.2/21.1% | 1.8/4.0% | 3 |

> stretch=1.0: decode_failures 22

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| clustered | 1 | 0.864 | 0.863 | 0.000 | - | - | 0.937 | 0.938 | 0.000 | 1.18x | 27.1/35.1/36.8% | 1.4/5.6% | 3 |
| corridor | 1 | 0.682 | 0.672 | 0.010 | - | - | 0.783 | 0.785 | 0.149 | 1.29x | 17.5/26.8/28.5% | 1.8/5.0% | 3 |
| hub | 1 | 0.941 | 0.939 | 0.001 | - | - | 0.968 | 0.968 | 0.770 | 1.11x | 26.4/35.5/36.9% | 1.5/5.5% | 3 |

> topology=uniform: decode_failures 22

> topology=corridor: decode_failures 2

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.883 | 0.883 | 0.000 | - | - | 0.897 | 0.982 | 0.570 | 1.60x | 22.9/31.4/36.9% | 2.3/6.7% | 3 |
| True | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.896 | 0.987 | 0.565 | 1.59x | 22.8/31.4/36.8% | 2.4/6.8% | 3 |

> coding-rate-ladder=False: decode_failures 31

> coding-rate-ladder=True: decode_failures 38

> slower: 9.12 s per simulated hour against 2.75 over 15 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.896 | 0.987 | 0.565 | 1.59x | 22.8/31.4/36.8% | 2.4/6.8% | 3 |
| m4-early-flood | 1 | 0.886 | 0.886 | 0.000 | - | - | 0.905 | 0.987 | 0.591 | 1.61x | 23.1/31.5/37.1% | 2.4/6.7% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 38

> dm-mode=m4-early-flood: decode_failures 34

> slower: 12.1 s per simulated hour against 2.5 over 15 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.901 | 0.901 | 0.000 | - | - | 0 | 0.000 | 0.585 | 1.27x | 18.1/24.6/28.9% | 1.8/5.2% | 3 |
| chain | 1 | 0.894 | 0.892 | 0.002 | - | - | 0.877 | 0.985 | 0.585 | 1.48x | 21.1/29.0/34.0% | 2.2/6.3% | 3 |
| sr | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> protocol=sr: decode_failures 22

> slower: 3.37 s per simulated hour against 1.42 over 15 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| True | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.948 | 0.987 | 0.552 | 1.31x | 18.6/25.6/30.0% | 1.9/5.5% | 3 |

> extra-repeats=False: decode_failures 22

> extra-repeats=True: decode_failures 34

> slower: 9.47 s per simulated hour against 1.68 over 15 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.950 | 0.947 | 0.002 | - | - | 0.996 | 0.996 | 0.814 | 2.05x | 21.0/40.2/43.9% | 1.4/5.1% | 3 |
| True | 1 | 0.952 | 0.950 | 0.002 | - | - | 0.996 | 0.996 | 0.817 | 2.06x | 21.0/39.7/43.4% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.294 | 0.288 | 0.006 | - | - | 0.531 | 0.674 | 0.000 | 0.07x | 0.4/1.2/1.6% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.640 | 0.619 | 0.021 | - | - | 0.904 | 0.907 | 0.098 | 0.33x | 2.9/5.3/7.1% | 0.5/1.3% | 3 |
| LONG_TURBO | 1 | 0.867 | 0.859 | 0.008 | - | - | 0.963 | 0.977 | 0.394 | 1.35x | 15.9/22.0/27.4% | 2.0/5.1% | 3 |

> preset=SHORT_TURBO: decode_failures 3

> preset=LONG_TURBO: decode_failures 12

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.922 | 0.913 | 0.009 | - | - | 0.970 | 0.991 | 0.649 | 1.22x | 20.3/26.9/30.6% | 1.7/5.4% | 3 |
| 1.0 | 1 | 0.949 | 0.944 | 0.005 | - | - | 0.984 | 0.992 | 0.815 | 1.00x | 24.1/30.3/32.4% | 1.2/5.5% | 3 |

> duct-per-hour=0.0: decode_failures 22

> duct-per-hour=0.25: decode_failures 29

> duct-per-hour=1.0: decode_failures 3

> slower: 6.17 s per simulated hour against 1.82 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.514 | 0.491 | 0.023 | - | - | 0.824 | 0.827 | 0.000 | 0.19x | 1.4/3.2/3.9% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| LITE_FAST | 1 | 0.879 | 0.871 | 0.008 | - | - | 0.974 | 0.988 | 0.447 | 1.02x | 12.8/18.1/21.8% | 1.5/4.2% | 3 |
| NARROW_SLOW | 1 | 0.868 | 0.860 | 0.008 | - | - | 0.952 | 0.984 | 0.495 | 1.28x | 16.6/23.1/27.7% | 1.9/5.4% | 3 |

> preset=LONG_FAST: decode_failures 22

> preset=LITE_FAST: decode_failures 27

> preset=NARROW_SLOW: decode_failures 33

> slower: 7.74 s per simulated hour against 2.03 over 15 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| temporal | 1 | 0.849 | 0.841 | 0.007 | - | - | 0.912 | 0.981 | 0.482 | 1.34x | 18.7/25.2/30.7% | 1.9/5.4% | 3 |
| transient | 1 | 0.901 | 0.894 | 0.007 | - | - | 0.955 | 0.991 | 0.579 | 1.31x | 18.5/25.5/30.1% | 1.9/5.5% | 3 |
| periodic | 1 | 0.753 | 0.747 | 0.007 | - | - | 0.804 | 0.844 | 0.486 | 1.22x | 17.7/23.9/27.9% | 1.9/4.8% | 3 |

> noise-profile=none: decode_failures 22

> noise-profile=temporal: decode_failures 33

> noise-profile=transient: decode_failures 28

> noise-profile=periodic: decode_failures 26

> slower: 13.1 s per simulated hour against 4.91 over 15 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.514 | 0.491 | 0.023 | - | - | 0.824 | 0.827 | 0.000 | 0.19x | 1.4/3.2/3.9% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| LONG_MODERATE | 1 | 0.846 | 0.837 | 0.009 | - | - | 0.932 | 0.940 | 0.680 | 3.42x | 55.0/68.0/71.1% | 5.2/12.8% | 3 |

> preset=LONG_FAST: decode_failures 22

> preset=LONG_MODERATE: decode_failures 3

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.122 | 0.121 | 0.001 | - | - | 0.399 | 0.400 | 0.000 | 0.01x | 0.0/0.2/0.3% | 0.0/0.1% | 3 |
| SHORT_TURBO | 1 | 0.294 | 0.288 | 0.006 | - | - | 0.531 | 0.674 | 0.000 | 0.07x | 0.4/1.2/1.6% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| LONG_TURBO | 1 | 0.867 | 0.859 | 0.008 | - | - | 0.963 | 0.977 | 0.394 | 1.35x | 15.9/22.0/27.4% | 2.0/5.1% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.888 | 0.880 | 0.009 | - | - | 0.972 | 0.972 | 0.535 | 1.84x | 24.7/32.4/38.1% | 2.8/7.1% | 3 |

> preset=SHORT_TURBO: decode_failures 3

> preset=LONG_FAST: decode_failures 22

> preset=LONG_TURBO: decode_failures 12

> preset=EXTRA_LONG_TURBO: decode_failures 2

> slower: 3.49 s per simulated hour against 1.59 over 11 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.857 | 0.851 | 0.006 | - | - | 0.914 | 0.944 | 0.558 | 1.26x | 18.1/24.7/29.0% | 1.9/5.2% | 3 |
| 10000 | 1 | 0.753 | 0.747 | 0.007 | - | - | 0.804 | 0.844 | 0.486 | 1.22x | 17.7/23.9/27.9% | 1.9/4.8% | 3 |
| 4000 | 1 | 0.493 | 0.490 | 0.003 | - | - | 0.535 | 0.585 | 0.268 | 1.07x | 16.1/21.4/24.6% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.129 | 0.129 | 0.000 | - | - | 0.132 | 0.204 | 0.060 | 0.72x | 11.6/15.4/18.1% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 12

> noise-pulse-interval-ms=10000: decode_failures 26

> noise-pulse-interval-ms=4000: decode_failures 4

> slower: 4.16 s per simulated hour against 1.6 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.521 | 0.508 | 0.013 | - | - | 0.748 | 0.750 | 0.000 | 1.37x | 10.9/18.8/23.2% | 2.2/4.7% | 3 |
| 1.0 | 1 | 0.767 | 0.756 | 0.011 | - | - | 0.888 | 0.894 | 0.505 | 1.10x | 15.9/24.5/26.6% | 1.6/4.8% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 22 | 1 | 0.588 | 0.563 | 0.025 | - | - | 0.852 | 0.855 | 0.099 | 1.50x | 12.4/21.2/27.5% | 2.3/5.0% | 3 |
| 17 | 1 | 0.295 | 0.291 | 0.004 | - | - | 0.539 | 0.556 | 0.000 | 1.34x | 7.8/22.2/27.1% | 2.0/5.1% | 3 |
| 14 | 1 | 0.141 | 0.137 | 0.003 | - | - | 0.421 | 0.426 | 0.000 | 0.82x | 2.8/16.5/20.7% | 1.0/4.1% | 3 |

> tx-power=30: decode_failures 22

> tx-power=17: decode_failures 4

> tx-power=14: decode_failures 1

> slower: 3.45 s per simulated hour against 1.59 over 15 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.950 | 0.947 | 0.002 | - | - | 0.996 | 0.996 | 0.814 | 2.05x | 21.0/40.2/43.9% | 1.4/5.1% | 3 |
| True | 1 | 0.944 | 0.942 | 0.002 | - | - | 0.996 | 0.996 | 0.803 | 2.39x | 24.2/44.8/48.5% | 1.6/5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.901 | 0.896 | 0.005 | - | - | 0.958 | 0.990 | 0.545 | 1.39x | 19.8/29.3/32.8% | 1.9/5.6% | 3 |
| True | 1 | 0.930 | 0.927 | 0.003 | - | - | 0.957 | 0.992 | 0.580 | 1.47x | 20.8/30.1/33.8% | 2.0/5.7% | 3 |

> favourite-routers=False: decode_failures 21

> favourite-routers=True: decode_failures 30

> slower: 9.31 s per simulated hour against 1.69 over 15 prior run(s) - 5.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| random | 1 | 0.880 | 0.869 | 0.011 | - | - | 0.942 | 0.977 | 0.486 | 1.26x | 18.2/25.0/29.2% | 1.9/5.3% | 3 |

> hop-assign=centrality: decode_failures 22

> hop-assign=random: decode_failures 44

> slower: 7.81 s per simulated hour against 1.77 over 15 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.764 | 0.736 | 0.028 | - | - | 0.875 | 0.941 | 0.365 | 0.99x | 14.7/21.6/25.5% | 1.4/4.6% | 3 |
| 7 | 1 | 0.945 | 0.941 | 0.004 | - | - | 0.972 | 0.991 | 0.591 | 1.40x | 19.8/26.1/30.7% | 2.0/5.5% | 3 |
| 15 | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.962 | 0.980 | 0.605 | 1.36x | 19.0/25.7/30.2% | 1.9/5.5% | 3 |
| 32 | 1 | 0.951 | 0.949 | 0.002 | - | - | 0.953 | 0.985 | 0.617 | 1.37x | 19.1/25.8/30.4% | 1.9/5.4% | 3 |

> hop-limit=3: decode_failures 41

> hop-limit=7: decode_failures 45

> hop-limit=15: decode_failures 23

> hop-limit=32: decode_failures 32

> slower: 11.6 s per simulated hour against 1.82 over 15 prior run(s) - 6.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.764 | 0.736 | 0.028 | - | - | 0.875 | 0.941 | 0.365 | 0.99x | 14.7/21.6/25.5% | 1.4/4.6% | 3 |
| 5 | 1 | 0.913 | 0.903 | 0.010 | - | - | 0.960 | 0.986 | 0.533 | 1.29x | 18.5/25.0/29.4% | 1.9/5.4% | 3 |
| 7 | 1 | 0.945 | 0.941 | 0.004 | - | - | 0.972 | 0.991 | 0.591 | 1.40x | 19.8/26.1/30.7% | 2.0/5.5% | 3 |

> hop-limit=3: decode_failures 41

> hop-limit=5: decode_failures 52

> hop-limit=7: decode_failures 45

> slower: 14.7 s per simulated hour against 2.03 over 15 prior run(s) - 7.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.903 | 0.903 | 0.000 | - | - | 0.827 | 0.990 | 0.566 | 1.26x | 18.0/24.6/28.9% | 1.8/5.2% | 3 |

> rebroadcast-mode=ALL: decode_failures 22

> rebroadcast-mode=KNOWN_ONLY: decode_failures 22

> slower: 5.61 s per simulated hour against 1.59 over 15 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.764 | 0.736 | 0.028 | - | - | 0.875 | 0.941 | 0.365 | 0.99x | 14.7/21.6/25.5% | 1.4/4.6% | 3 |
| True | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> hop-spread=False: decode_failures 41

> hop-spread=True: decode_failures 22

> slower: 8.42 s per simulated hour against 2.08 over 15 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| BALANCED | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| STRICT | 1 | 0.762 | 0.762 | 0.000 | - | - | 0.803 | 0.852 | 0.458 | 1.39x | 19.6/26.7/31.1% | 2.0/5.6% | 3 |

> signature-policy=COMPATIBLE: decode_failures 22

> signature-policy=BALANCED: decode_failures 22

> signature-policy=STRICT: decode_failures 36

> slower: 8.97 s per simulated hour against 1.87 over 15 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| dm | 1 | 0.910 | 0.903 | 0.007 | - | - | 0.988 | 0.991 | 0.595 | 1.27x | 18.1/24.9/29.2% | 1.8/5.4% | 3 |

> advert-transport=broadcast: decode_failures 22

> slower: 5.06 s per simulated hour against 1.85 over 15 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.908 | 0.901 | 0.006 | - | - | 0.973 | 0.988 | 0.574 | 1.31x | 18.6/25.4/30.0% | 1.9/5.5% | 3 |
| local | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| time | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.985 | 0.990 | 0.574 | 1.34x | 19.0/26.1/30.6% | 2.0/5.6% | 3 |
| window | 1 | 0.906 | 0.901 | 0.006 | - | - | 0.961 | 0.992 | 0.565 | 1.29x | 18.4/25.0/29.4% | 1.9/5.4% | 3 |

> bucket-mode=global: misdecodes 30

> bucket-mode=local: decode_failures 22

> bucket-mode=time: misdecodes 15

> bucket-mode=window: misdecodes 25

> bucket-mode=window: decode_failures 3

> slower: 4.05 s per simulated hour against 1.56 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.900 | 0.892 | 0.007 | - | - | 0.968 | 0.987 | 0.581 | 1.44x | 20.4/27.9/32.6% | 2.1/6.1% | 3 |
| 1800 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.985 | 0.990 | 0.574 | 1.34x | 19.0/26.1/30.6% | 2.0/5.6% | 3 |
| 3600 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.962 | 0.994 | 0.568 | 1.30x | 18.6/25.4/29.8% | 1.9/5.4% | 3 |

> time-bucket-s=600: misdecodes 84

> time-bucket-s=1800: misdecodes 15

> time-bucket-s=3600: misdecodes 10

> time-bucket-s=3600: decode_failures 16

> slower: 3.99 s per simulated hour against 1.62 over 15 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| interval | 1 | 0.891 | 0.882 | 0.009 | - | - | 0.970 | 0.979 | 0.597 | 1.75x | 24.3/34.3/39.6% | 2.6/7.8% | 3 |
| aimd | 1 | 0.899 | 0.897 | 0.002 | - | - | 0.864 | 0.986 | 0.566 | 1.33x | 18.9/25.7/30.4% | 1.9/5.5% | 3 |
| bucket+interval | 1 | 0.896 | 0.886 | 0.009 | - | - | 0.985 | 0.990 | 0.597 | 1.78x | 24.6/34.7/40.0% | 2.6/8.0% | 3 |

> trigger=bucket: decode_failures 22

> trigger=interval: misdecodes 14

> trigger=interval: decode_failures 9

> trigger=aimd: misdecodes 6

> trigger=aimd: decode_failures 27

> trigger=bucket+interval: misdecodes 20

> trigger=bucket+interval: decode_failures 5

> slower: 6.77 s per simulated hour against 2.9 over 15 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.947 | 0.994 | 0.572 | 1.29x | 18.4/25.2/29.7% | 1.9/5.4% | 3 |
| 8 | 1 | 0.905 | 0.900 | 0.006 | - | - | 0.958 | 0.990 | 0.608 | 1.29x | 18.5/25.3/29.7% | 1.9/5.3% | 3 |
| 16 | 1 | 0.903 | 0.898 | 0.005 | - | - | 0.942 | 0.988 | 0.581 | 1.30x | 18.5/25.3/29.8% | 1.9/5.4% | 3 |
| 32 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 50 | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.958 | 0.992 | 0.589 | 1.32x | 18.7/25.6/30.1% | 1.9/5.4% | 3 |

> capacity=4: decode_failures 64

> capacity=8: decode_failures 41

> capacity=16: decode_failures 47

> capacity=32: decode_failures 22

> capacity=50: decode_failures 15

> slower: 5.71 s per simulated hour against 1.69 over 15 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.947 | 0.994 | 0.572 | 1.29x | 18.4/25.2/29.7% | 1.9/5.4% | 3 |
| 8 | 1 | 0.905 | 0.900 | 0.006 | - | - | 0.958 | 0.990 | 0.608 | 1.29x | 18.5/25.3/29.7% | 1.9/5.3% | 3 |
| 16 | 1 | 0.903 | 0.898 | 0.005 | - | - | 0.942 | 0.988 | 0.581 | 1.30x | 18.5/25.3/29.8% | 1.9/5.4% | 3 |
| 32 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 50 | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.958 | 0.992 | 0.589 | 1.32x | 18.7/25.6/30.1% | 1.9/5.4% | 3 |

> capacity=4: decode_failures 64

> capacity=8: decode_failures 41

> capacity=16: decode_failures 47

> capacity=32: decode_failures 22

> capacity=50: decode_failures 15

> slower: 5.66 s per simulated hour against 1.77 over 15 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.902 | 0.900 | 0.001 | - | - | 0.851 | 0.991 | 0.578 | 1.28x | 18.1/24.8/29.2% | 1.8/5.2% | 3 |
| 16 | 1 | 0.901 | 0.900 | 0.001 | - | - | 0.862 | 0.991 | 0.581 | 1.30x | 18.4/25.1/29.7% | 1.8/5.3% | 3 |
| 32 | 1 | 0.906 | 0.901 | 0.006 | - | - | 0.961 | 0.992 | 0.565 | 1.29x | 18.4/25.0/29.4% | 1.9/5.4% | 3 |

> capacity=8: misdecodes 4

> capacity=8: decode_failures 62

> capacity=16: misdecodes 14

> capacity=16: decode_failures 54

> capacity=32: misdecodes 25

> capacity=32: decode_failures 3

> slower: 3.44 s per simulated hour against 1.61 over 15 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.896 | 0.886 | 0.009 | - | - | 0.985 | 0.990 | 0.597 | 1.78x | 24.6/34.7/40.0% | 2.6/8.0% | 3 |
| 02-06 | 1 | 0.902 | 0.897 | 0.006 | - | - | 0.906 | 0.987 | 0.555 | 1.33x | 18.8/25.9/30.4% | 1.9/5.5% | 3 |
| 00-08 | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.920 | 0.993 | 0.553 | 1.39x | 19.5/27.1/31.7% | 2.0/5.9% | 3 |

> catch-up-hours=: misdecodes 20

> catch-up-hours=: decode_failures 5

> catch-up-hours=02-06: decode_failures 50

> catch-up-hours=00-08: decode_failures 52

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.906 | 0.904 | 0.001 | - | - | 0.990 | 0.991 | 0.561 | 1.30x | 18.4/25.2/29.7% | 1.8/5.3% | 3 |
| 2 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 3 | 1 | 0.913 | 0.902 | 0.011 | - | - | 0.998 | 0.998 | 0.617 | 1.32x | 18.8/25.5/30.1% | 1.9/5.4% | 3 |
| 4 | 1 | 0.921 | 0.901 | 0.019 | - | - | 0.916 | 0.991 | 0.573 | 1.32x | 18.9/25.6/29.9% | 1.9/5.6% | 3 |

> hops-apart=2: decode_failures 22

> hops-apart=4: decode_failures 28

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.906 | 0.904 | 0.001 | - | - | 0.990 | 0.991 | 0.561 | 1.30x | 18.4/25.2/29.7% | 1.8/5.3% | 3 |
| 2 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 3 | 1 | 0.913 | 0.902 | 0.011 | - | - | 0.998 | 0.998 | 0.617 | 1.32x | 18.8/25.5/30.1% | 1.9/5.4% | 3 |
| 4 | 1 | 0.921 | 0.901 | 0.019 | - | - | 0.916 | 0.991 | 0.573 | 1.32x | 18.9/25.6/29.9% | 1.9/5.6% | 3 |
| 5 | 1 | 0.927 | 0.901 | 0.027 | - | - | 0.985 | 0.995 | 0.583 | 1.33x | 18.7/25.6/30.2% | 1.9/5.6% | 3 |

> hops-apart=2: decode_failures 22

> hops-apart=4: decode_failures 28

> hops-apart=5: decode_failures 7

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.899 | 0.894 | 0.006 | - | - | 0.944 | 0.982 | 0.564 | 1.33x | 18.9/25.7/30.3% | 1.9/5.5% | 3 |
| 30 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 120 | 1 | 0.904 | 0.897 | 0.007 | - | - | 0.956 | 0.987 | 0.579 | 1.31x | 18.6/25.4/30.0% | 1.9/5.4% | 3 |
| 600 | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.959 | 0.989 | 0.580 | 1.32x | 18.8/25.7/30.2% | 1.9/5.5% | 3 |

> advert-jitter-s=1: decode_failures 28

> advert-jitter-s=30: decode_failures 22

> advert-jitter-s=120: decode_failures 32

> advert-jitter-s=600: decode_failures 55

> slower: 9.79 s per simulated hour against 1.74 over 15 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.899 | 0.894 | 0.006 | - | - | 0.944 | 0.982 | 0.564 | 1.33x | 18.9/25.7/30.3% | 1.9/5.5% | 3 |
| 30 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 120 | 1 | 0.904 | 0.897 | 0.007 | - | - | 0.956 | 0.987 | 0.579 | 1.31x | 18.6/25.4/30.0% | 1.9/5.4% | 3 |
| 600 | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.959 | 0.989 | 0.580 | 1.32x | 18.8/25.7/30.2% | 1.9/5.5% | 3 |

> advert-jitter-s=1: decode_failures 28

> advert-jitter-s=30: decode_failures 22

> advert-jitter-s=120: decode_failures 32

> advert-jitter-s=600: decode_failures 55

> slower: 11.8 s per simulated hour against 1.77 over 15 prior run(s) - 6.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.927 | 0.905 | 0.023 | - | - | 0.948 | 0.985 | 0.589 | 1.32x | 18.5/25.3/29.9% | 1.9/5.3% | 3 |
| routers | 1 | 0.903 | 0.901 | 0.002 | - | - | 0.986 | 0.987 | 0.580 | 1.29x | 18.3/25.3/29.6% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.904 | 0.903 | 0.001 | - | - | 0.983 | 0.983 | 0.558 | 1.30x | 18.4/25.3/29.7% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.994 | 0.995 | 0.575 | 1.30x | 18.3/25.2/29.6% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.907 | 0.897 | 0.010 | - | - | 0.985 | 0.987 | 0.569 | 1.32x | 18.7/25.5/30.1% | 1.9/5.4% | 3 |
| hops-apart | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> place=spread: decode_failures 28

> place=hops-apart: decode_failures 22

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.927 | 0.905 | 0.023 | - | - | 0.948 | 0.985 | 0.589 | 1.32x | 18.5/25.3/29.9% | 1.9/5.3% | 3 |
| routers | 1 | 0.903 | 0.901 | 0.002 | - | - | 0.986 | 0.987 | 0.580 | 1.29x | 18.3/25.3/29.6% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.904 | 0.903 | 0.001 | - | - | 0.983 | 0.983 | 0.558 | 1.30x | 18.4/25.3/29.7% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.994 | 0.995 | 0.575 | 1.30x | 18.3/25.2/29.6% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.907 | 0.897 | 0.010 | - | - | 0.985 | 0.987 | 0.569 | 1.32x | 18.7/25.5/30.1% | 1.9/5.4% | 3 |
| hops-apart | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> place=spread: decode_failures 28

> place=hops-apart: decode_failures 22

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| broadcast | 1 | 0.922 | 0.892 | 0.030 | - | - | 0.922 | 0.987 | 0.564 | 1.42x | 20.3/27.5/32.1% | 2.1/5.8% | 3 |

> provide-transport=dm: decode_failures 22

> provide-transport=broadcast: decode_failures 37

> slower: 9.85 s per simulated hour against 1.93 over 15 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| heard | 1 | 0.907 | 0.901 | 0.005 | - | - | 0.950 | 0.993 | 0.564 | 1.30x | 18.4/25.1/29.6% | 1.9/5.4% | 3 |

> replay-ordering=tip: decode_failures 22

> replay-ordering=heard: misdecodes 8

> replay-ordering=heard: decode_failures 28

> slower: 8.47 s per simulated hour against 1.79 over 15 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.922 | 0.892 | 0.030 | - | - | 0.922 | 0.987 | 0.564 | 1.42x | 20.3/27.5/32.1% | 2.1/5.8% | 3 |
| heard | 1 | 0.920 | 0.886 | 0.034 | - | - | 0.928 | 0.983 | 0.569 | 1.44x | 20.5/27.8/32.4% | 2.1/5.9% | 3 |

> replay-ordering=tip: decode_failures 37

> replay-ordering=heard: misdecodes 4

> replay-ordering=heard: decode_failures 44

> slower: 12.9 s per simulated hour against 1.57 over 15 prior run(s) - 8.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.904 | 0.902 | 0.002 | - | - | 0.882 | 0.988 | 0.570 | 1.29x | 18.4/25.2/29.7% | 1.9/5.3% | 3 |
| enum | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.951 | 0.987 | 0.577 | 1.31x | 18.7/25.5/30.0% | 1.9/5.5% | 3 |
| hybrid | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> resolve=sketch: decode_failures 24

> resolve=hybrid: decode_failures 22

> slower: 5.79 s per simulated hour against 1.53 over 15 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.903 | 0.901 | 0.002 | - | - | 0.986 | 0.987 | 0.580 | 1.29x | 18.3/25.3/29.6% | 1.9/5.3% | 3 |
| 6 | 1 | 0.903 | 0.900 | 0.003 | - | - | 0.997 | 0.997 | 0.608 | 1.33x | 18.8/26.0/30.4% | 2.0/5.5% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.883 | 0.968 | 0.579 | 1.29x | 18.3/25.0/29.4% | 1.9/5.4% | 2 |
| 3 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 5 | 1 | 0.917 | 0.905 | 0.012 | - | - | 0.987 | 0.993 | 0.576 | 1.35x | 19.2/25.8/30.3% | 2.0/5.6% | 5 |
| 8 | 1 | 0.907 | 0.891 | 0.016 | - | - | 0.989 | 0.992 | 0.580 | 1.38x | 19.6/26.2/30.6% | 2.0/5.6% | 8 |

> servers=2: decode_failures 20

> servers=3: decode_failures 22

> servers=5: decode_failures 44

> slower: 6.68 s per simulated hour against 2.6 over 15 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.883 | 0.968 | 0.579 | 1.29x | 18.3/25.0/29.4% | 1.9/5.4% | 2 |
| 3 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 5 | 1 | 0.917 | 0.905 | 0.012 | - | - | 0.987 | 0.993 | 0.576 | 1.35x | 19.2/25.8/30.3% | 2.0/5.6% | 5 |
| 8 | 1 | 0.907 | 0.891 | 0.016 | - | - | 0.989 | 0.992 | 0.580 | 1.38x | 19.6/26.2/30.6% | 2.0/5.6% | 8 |

> servers=2: decode_failures 20

> servers=3: decode_failures 22

> servers=5: decode_failures 44

> slower: 8.43 s per simulated hour against 2.29 over 15 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| True | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |

> signed=False: decode_failures 22

> signed=True: decode_failures 22

> slower: 7.94 s per simulated hour against 1.74 over 15 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.902 | 0.898 | 0.005 | - | - | 0.930 | 0.990 | 0.591 | 1.22x | 17.1/23.8/28.0% | 1.8/5.0% | 3 |
| 1 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.969 | 0.991 | 0.603 | 1.22x | 17.0/24.0/28.1% | 1.7/5.1% | 3 |
| 2 | 1 | 0.902 | 0.897 | 0.006 | - | - | 0.960 | 0.985 | 0.541 | 1.22x | 17.1/24.0/28.0% | 1.8/5.1% | 3 |
| 4 | 1 | 0.903 | 0.897 | 0.005 | - | - | 0.957 | 0.984 | 0.567 | 1.21x | 17.1/23.6/27.7% | 1.7/5.0% | 3 |

> sr-retries=0: decode_failures 19

> sr-retries=1: decode_failures 10

> sr-retries=2: decode_failures 19

> sr-retries=4: decode_failures 25

> slower: 9.44 s per simulated hour against 1.67 over 15 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.911 | 0.905 | 0.005 | - | - | 0.947 | 0.994 | 0.577 | 1.30x | 18.6/25.3/29.7% | 1.9/5.5% | 3 |
| 24 | 1 | 0.904 | 0.897 | 0.007 | - | - | 0.956 | 0.988 | 0.571 | 1.31x | 18.6/25.5/30.0% | 1.9/5.5% | 3 |
| 32 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.957 | 0.986 | 0.564 | 1.30x | 18.4/25.2/29.6% | 1.9/5.3% | 3 |
| 64 | 1 | 0.902 | 0.895 | 0.006 | - | - | 0.952 | 0.987 | 0.549 | 1.32x | 18.7/25.6/30.1% | 1.9/5.5% | 3 |

> short-id-bits=16: decode_failures 50

> short-id-bits=24: decode_failures 41

> short-id-bits=32: decode_failures 22

> short-id-bits=64: decode_failures 53

> slower: 13.4 s per simulated hour against 1.77 over 15 prior run(s) - 7.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.898 | 0.891 | 0.007 | - | - | 0.961 | 0.984 | 0.584 | 1.39x | 19.5/27.0/31.5% | 2.0/5.8% | 3 |
| 16 | 1 | 0.905 | 0.897 | 0.008 | - | - | 0.960 | 0.986 | 0.574 | 1.32x | 18.6/25.8/30.3% | 1.9/5.6% | 3 |
| 32 | 1 | 0.906 | 0.901 | 0.006 | - | - | 0.961 | 0.992 | 0.565 | 1.29x | 18.4/25.0/29.4% | 1.9/5.4% | 3 |

> window-size=8: misdecodes 97

> window-size=16: misdecodes 48

> window-size=32: misdecodes 25

> window-size=32: decode_failures 3

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.950 | 0.947 | 0.002 | - | - | 0.996 | 0.996 | 0.814 | 2.05x | 21.0/40.2/43.9% | 1.4/5.1% | 3 |
| True | 1 | 0.717 | 0.710 | 0.007 | - | - | 0.852 | 0.892 | 0.551 | 5.52x | 54.5/75.9/79.1% | 4.0/12.6% | 3 |

> no-congestion-scaling=True: queue drops 16.2% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 53

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.469 | 0.459 | 0.010 | - | - | 0.684 | 0.686 | 0.222 | 4.37x | 14.5/27.9/41.7% | 1.5/5.1% | 3 |
| truesize | 1 | 0.506 | 0.493 | 0.012 | - | - | 0.722 | 0.727 | 0.229 | 3.16x | 10.1/22.1/33.7% | 1.0/4.3% | 3 |

> congestion-input=hotstore: decode_failures 4

> congestion-input=truesize: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.997 | 0.998 | 0.830 | 1.91x | 19.5/37.3/40.9% | 1.3/4.7% | 3 |
| adaptive | 1 | 0.950 | 0.947 | 0.002 | - | - | 0.996 | 0.996 | 0.814 | 2.05x | 21.0/40.2/43.9% | 1.4/5.1% | 3 |

