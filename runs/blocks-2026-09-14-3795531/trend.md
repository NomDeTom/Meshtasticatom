# Sweep blocks-2026-09-14-3795531

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 3795531 · seeds 3795531
- **blocks** 87 run
- **compute** 20.8 h of simulator time across every cell
- **generated** 2026-09-14T10:36:10+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>301 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 33
- AD-amplifiers: amplifier-mix=arms-race: decode_failures 34
- AD-amplifiers: slower: 7.86 s per simulated hour against 1.67 over 24 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-amplify-worst: amplify-worst=0.0: decode_failures 33
- AD-amplify-worst: slower: 4.82 s per simulated hour against 1.76 over 24 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=degree: decode_failures 36
- AD-badrouters: role-placement=inverse: decode_failures 14
- AD-badrouters: role-placement=random: decode_failures 24
- AD-badrouters: slower: 8.09 s per simulated hour against 1.98 over 24 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 36
- AD-flooding: role-mix=all-routers: decode_failures 26
- AD-flooding: slower: 9.25 s per simulated hour against 2.55 over 24 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 36
- AD-nomute: role-mix=no-mute: decode_failures 32
- AD-nomute: role-mix=all-routers: decode_failures 26
- AD-nomute: slower: 9.19 s per simulated hour against 2.38 over 24 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 36
- AD-siting: siting-mix=local-typical: decode_failures 10
- AD-siting: siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count
- AD-siting: slower: 4.42 s per simulated hour against 1.32 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=inverse: decode_failures 76
- AD-worst: slower: 13.5 s per simulated hour against 3.48 over 24 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 20
- BL-control: slower: 3.57 s per simulated hour against 1.72 over 24 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 21
- DB-hotstore: max-num-nodes=100: decode_failures 30
- DB-hotstore: max-num-nodes=120: decode_failures 30
- DB-hotstore: max-num-nodes=250: decode_failures 30
- DB-hotstore: slower: 8.37 s per simulated hour against 2.52 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 28
- DB-hotstore-stress: max-num-nodes=120: decode_failures 1
- DB-hotstore-stress: max-num-nodes=250: decode_failures 23
- DB-platform: platform-mix=uniform: decode_failures 30
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 30
- DB-platform: platform-mix=constrained: decode_failures 21
- DB-platform: slower: 9.28 s per simulated hour against 2.59 over 24 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: decode_failures 45
- DB-warm: warm-num-nodes=25: decode_failures 45
- DB-warm: warm-num-nodes=100: decode_failures 45
- DB-warm: warm-num-nodes=2000: decode_failures 45
- DG-burst: burst-loss=0.0: decode_failures 33
- DG-burst: burst-loss=0.1: decode_failures 25
- DG-burst: burst-loss=0.2: decode_failures 22
- DG-burst: burst-loss=0.3: decode_failures 15
- DG-loss: extra-loss=0.0: decode_failures 33
- DG-loss: extra-loss=0.1: decode_failures 31
- DG-loss: extra-loss=0.2: decode_failures 26
- DG-loss: extra-loss=0.3: decode_failures 18
- DG-loss: slower: 7.29 s per simulated hour against 2.2 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 33
- DG-outage: burst-loss=0.1: decode_failures 29
- DG-outage: burst-loss=0.2: decode_failures 16
- DG-outage: burst-loss=0.3: decode_failures 16
- DM-mode: dm-mode=flood-only: decode_failures 26
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 25
- DM-mode: dm-mode=m4-early-flood: decode_failures 27
- DM-mode: slower: 8.59 s per simulated hour against 2.88 over 24 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 33
- FW-firmware: slower: 5.57 s per simulated hour against 1.72 over 24 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.0: decode_failures 33
- FW-mixed-26: legacy-fraction=0.25: decode_failures 20
- FW-mixed-26: legacy-fraction=0.5: decode_failures 7
- FW-mixed-26: slower: 5.71 s per simulated hour against 1.69 over 24 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.0: decode_failures 33
- FW-mixed: legacy-fraction=0.25: decode_failures 13
- FW-mixed: legacy-fraction=0.5: decode_failures 39
- FW-mixed: slower: 6.26 s per simulated hour against 1.67 over 24 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-signing-cost: profile-flag=signing=false: decode_failures 44
- FW-signing-cost: profile-flag=signing=true: decode_failures 33
- FW-signing-cost: slower: 9.61 s per simulated hour against 1.6 over 24 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-versions: profile=2.8: decode_failures 33
- LD-chatty-hops: broadcast-interval-s=3600: decode_failures 24
- LD-chatty-hops: broadcast-interval-s=900: decode_failures 34
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 3
- LD-chatty: broadcast-interval-s=3600: decode_failures 37
- LD-chatty: broadcast-interval-s=900: decode_failures 26
- LD-chatty: broadcast-interval-s=300: decode_failures 6
- LD-diurnal: diurnal=flat: decode_failures 36
- LD-diurnal: diurnal=sinusoid: decode_failures 26
- LD-diurnal: diurnal=commuter: decode_failures 33
- LD-diurnal: slower: 9.92 s per simulated hour against 1.56 over 24 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 26
- LD-interval: broadcast-interval-s=3600: decode_failures 37
- LD-interval: broadcast-interval-s=10800: decode_failures 38
- LD-interval: broadcast-interval-s=43200: decode_failures 47
- LD-interval: slower: 11.2 s per simulated hour against 1.4 over 24 prior run(s) - 8.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 33
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 36
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 38
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 32
- LD-traceroute: slower: 11.2 s per simulated hour against 2.08 over 24 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 45
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 44
- MS-density: nodes=40: decode_failures 2
- MS-density: nodes=60: decode_failures 33
- MS-hopscale: nodes=60: decode_failures 33
- MS-hopscale: nodes=250: decode_failures 31
- MS-oversubscribed: nodes=250: decode_failures 1
- MS-oversubscribed: nodes=500: decode_failures 2
- MS-oversubscribed: faster: 9.5 s per simulated hour against 19.6 over 24 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-roles-fav: role-mix=legacy-default: decode_failures 37
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 24
- MS-roles-fav: slower: 9.79 s per simulated hour against 1.75 over 24 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-roles: role-mix=legacy-default: decode_failures 24
- MS-roles: role-mix=baymesh-2026-08: decode_failures 36
- MS-roles: slower: 7.38 s per simulated hour against 1.8 over 24 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 33
- MS-router-late: router-late-fraction=0.05: decode_failures 37
- MS-router-late: router-late-fraction=0.1: decode_failures 46
- MS-router-late: router-late-fraction=0.2: decode_failures 35
- MS-router-late: slower: 11.8 s per simulated hour against 1.76 over 24 prior run(s) - 6.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=uniform: decode_failures 33
- MS-siting: siting-mix=local-typical: decode_failures 15
- MS-siting: slower: 4.45 s per simulated hour against 1.97 over 24 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-size: nodes=60: decode_failures 33
- MS-stretch: stretch=1.0: decode_failures 33
- MS-stretch: stretch=1.5: decode_failures 5
- MS-topology: topology=uniform: decode_failures 33
- PR-crladder: coding-rate-ladder=False: decode_failures 25
- PR-crladder: coding-rate-ladder=True: decode_failures 26
- PR-crladder: slower: 8.37 s per simulated hour against 2.77 over 24 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 26
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 26
- PR-dmmode-cr: slower: 6.88 s per simulated hour against 2.52 over 24 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 33
- PR-protocol: slower: 4.1 s per simulated hour against 1.42 over 24 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats: extra-repeats=False: decode_failures 33
- PR-repeats: extra-repeats=True: decode_failures 34
- PR-repeats: slower: 7.65 s per simulated hour against 1.65 over 24 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 9
- RF-duct: duct-per-hour=0.0: decode_failures 33
- RF-duct: duct-per-hour=0.25: decode_failures 49
- RF-duct: duct-per-hour=1.0: decode_failures 39
- RF-duct: slower: 12.8 s per simulated hour against 1.76 over 24 prior run(s) - 7.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=LONG_FAST: decode_failures 33
- RF-eu-presets: preset=LITE_FAST: decode_failures 12
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 15
- RF-eu-presets: slower: 4.25 s per simulated hour against 2.03 over 24 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-noise: noise-profile=none: decode_failures 33
- RF-noise: noise-profile=temporal: decode_failures 10
- RF-noise: noise-profile=transient: decode_failures 36
- RF-noise: noise-profile=periodic: decode_failures 11
- RF-preset: preset=LONG_FAST: decode_failures 33
- RF-preset: preset=LONG_MODERATE: decode_failures 5
- RF-preset-turbo: preset=LONG_FAST: decode_failures 33
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 38
- RF-preset-turbo: slower: 5.04 s per simulated hour against 1.56 over 20 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 23
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 11
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 5
- RF-txpower: tx-power=30: decode_failures 33
- RF-txpower: tx-power=22: decode_failures 2
- RT-adopt: no-adopt-hop-recommendation=True: decode_failures 1
- RT-favourites: favourite-routers=False: decode_failures 33
- RT-favourites: favourite-routers=True: decode_failures 36
- RT-favourites: slower: 7.61 s per simulated hour against 1.68 over 24 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 33
- RT-hopassign: hop-assign=random: decode_failures 32
- RT-hopassign: slower: 10.1 s per simulated hour against 1.81 over 24 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hoplimit: hop-limit=3: decode_failures 21
- RT-hoplimit: hop-limit=7: decode_failures 16
- RT-hoplimit: slower: 4.26 s per simulated hour against 1.79 over 24 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopspread: hop-limit=3: decode_failures 21
- RT-hopspread: hop-limit=5: decode_failures 23
- RT-hopspread: hop-limit=7: decode_failures 16
- RT-hopspread: slower: 5.06 s per simulated hour against 2.03 over 24 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 33
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 33
- RT-rebroadcast: slower: 7.12 s per simulated hour against 1.59 over 24 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-spread: hop-spread=False: decode_failures 21
- RT-spread: hop-spread=True: decode_failures 33
- RT-spread: slower: 8.81 s per simulated hour against 2.11 over 24 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 33
- SC-signing: signature-policy=BALANCED: decode_failures 33
- SC-signing: signature-policy=STRICT: decode_failures 26
- SC-signing: slower: 7.04 s per simulated hour against 1.85 over 24 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 33
- SF-advert-transport: advert-transport=dm: decode_failures 5
- SF-advert-transport: slower: 7.94 s per simulated hour against 1.81 over 24 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 17
- SF-bucket-mode: bucket-mode=local: decode_failures 33
- SF-bucket-mode: bucket-mode=time: misdecodes 9
- SF-bucket-mode: bucket-mode=time: decode_failures 8
- SF-bucket-mode: bucket-mode=window: misdecodes 9
- SF-bucket-mode: bucket-mode=window: decode_failures 15
- SF-bucket-mode: slower: 5.39 s per simulated hour against 1.61 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-time: time-bucket-s=600: misdecodes 69
- SF-bucket-time: time-bucket-s=1800: misdecodes 9
- SF-bucket-time: time-bucket-s=1800: decode_failures 8
- SF-bucket-time: time-bucket-s=3600: misdecodes 6
- SF-bucket-time: time-bucket-s=3600: decode_failures 14
- SF-bucket-time: slower: 3.72 s per simulated hour against 1.67 over 24 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-cadence: trigger=bucket: decode_failures 33
- SF-cadence: trigger=interval: misdecodes 4
- SF-cadence: trigger=interval: decode_failures 21
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 29
- SF-cadence: trigger=bucket+interval: misdecodes 5
- SF-cadence: trigger=bucket+interval: decode_failures 35
- SF-cadence: slower: 11.2 s per simulated hour against 3.39 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 56
- SF-capacity-local: capacity=8: decode_failures 51
- SF-capacity-local: capacity=16: decode_failures 40
- SF-capacity-local: capacity=32: decode_failures 33
- SF-capacity-local: capacity=50: decode_failures 30
- SF-capacity-local: slower: 7.76 s per simulated hour against 1.79 over 24 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity: capacity=4: decode_failures 56
- SF-capacity: capacity=8: decode_failures 51
- SF-capacity: capacity=16: decode_failures 40
- SF-capacity: capacity=32: decode_failures 33
- SF-capacity: capacity=50: decode_failures 30
- SF-capacity: slower: 7.83 s per simulated hour against 1.7 over 24 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-window: capacity=8: misdecodes 6
- SF-capacity-window: capacity=8: decode_failures 58
- SF-capacity-window: capacity=16: misdecodes 2
- SF-capacity-window: capacity=16: decode_failures 38
- SF-capacity-window: capacity=32: misdecodes 9
- SF-capacity-window: capacity=32: decode_failures 15
- SF-catchup: catch-up-hours=: misdecodes 5
- SF-catchup: catch-up-hours=: decode_failures 35
- SF-catchup: catch-up-hours=02-06: decode_failures 42
- SF-catchup: catch-up-hours=00-08: decode_failures 47
- SF-hops-flat: hops-apart=2: decode_failures 33
- SF-hops-flat: hops-apart=3: decode_failures 20
- SF-hops-flat: hops-apart=4: decode_failures 18
- SF-hops-spread: hops-apart=2: decode_failures 33
- SF-hops-spread: hops-apart=3: decode_failures 20
- SF-hops-spread: hops-apart=4: decode_failures 18
- SF-hops-spread: hops-apart=5: decode_failures 22
- SF-jitter-global: advert-jitter-s=1: decode_failures 34
- SF-jitter-global: advert-jitter-s=30: decode_failures 33
- SF-jitter-global: advert-jitter-s=120: decode_failures 39
- SF-jitter-global: advert-jitter-s=600: decode_failures 38
- SF-jitter-global: slower: 9.06 s per simulated hour against 1.78 over 24 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 34
- SF-jitter-local: advert-jitter-s=30: decode_failures 33
- SF-jitter-local: advert-jitter-s=120: decode_failures 39
- SF-jitter-local: advert-jitter-s=600: decode_failures 38
- SF-jitter-local: slower: 11.2 s per simulated hour against 1.84 over 24 prior run(s) - 6.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 28
- SF-place-flat: place=routers: decode_failures 2
- SF-place-flat: place=alternate-routers: decode_failures 5
- SF-place-flat: place=beside-router: decode_failures 3
- SF-place-flat: place=random-clients: decode_failures 35
- SF-place-flat: place=hops-apart: decode_failures 33
- SF-place-flat: slower: 6.03 s per simulated hour against 3.01 over 24 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-spread: place=spread: decode_failures 28
- SF-place-spread: place=routers: decode_failures 2
- SF-place-spread: place=alternate-routers: decode_failures 5
- SF-place-spread: place=beside-router: decode_failures 3
- SF-place-spread: place=random-clients: decode_failures 35
- SF-place-spread: place=hops-apart: decode_failures 33
- SF-place-spread: slower: 6.06 s per simulated hour against 2.92 over 24 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-provide-transport: provide-transport=dm: decode_failures 33
- SF-provide-transport: provide-transport=broadcast: decode_failures 34
- SF-provide-transport: slower: 8.77 s per simulated hour against 1.86 over 24 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 34
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 1
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 22
- SF-replay-order-broadcast: slower: 8.77 s per simulated hour against 1.83 over 24 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 33
- SF-replay-order: replay-ordering=heard: misdecodes 4
- SF-replay-order: replay-ordering=heard: decode_failures 31
- SF-replay-order: slower: 10.1 s per simulated hour against 1.68 over 24 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-resolve: resolve=sketch: decode_failures 29
- SF-resolve: resolve=hybrid: decode_failures 33
- SF-resolve: slower: 6.96 s per simulated hour against 1.54 over 24 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-allrouters: servers=3: decode_failures 2
- SF-servers-allrouters: servers=6: decode_failures 37
- SF-servers-allrouters: slower: 7.28 s per simulated hour against 1.84 over 24 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=3: decode_failures 33
- SF-servers-flat: servers=5: decode_failures 2
- SF-servers-flat: servers=8: decode_failures 16
- SF-servers-flat: slower: 8.35 s per simulated hour against 2.55 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=3: decode_failures 33
- SF-servers-spread: servers=5: decode_failures 2
- SF-servers-spread: servers=8: decode_failures 16
- SF-servers-spread: slower: 8.49 s per simulated hour against 2.27 over 24 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 33
- SF-signed: signed=True: decode_failures 33
- SF-signed: slower: 10.1 s per simulated hour against 1.74 over 24 prior run(s) - 5.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 22
- SF-sr-retries: sr-retries=1: decode_failures 16
- SF-sr-retries: sr-retries=2: decode_failures 17
- SF-sr-retries: sr-retries=4: decode_failures 16
- SF-sr-retries: slower: 8.45 s per simulated hour against 1.61 over 24 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 31
- SF-width: short-id-bits=24: decode_failures 32
- SF-width: short-id-bits=32: decode_failures 33
- SF-width: short-id-bits=64: decode_failures 32
- SF-width: slower: 9.95 s per simulated hour against 1.74 over 24 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 67
- SF-window-size: window-size=16: misdecodes 18
- SF-window-size: window-size=32: misdecodes 9
- SF-window-size: window-size=32: decode_failures 15
- SF-window-size: slower: 3.14 s per simulated hour against 1.43 over 24 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion-input: congestion-input=hotstore: decode_failures 1
- TH-congestion-input: congestion-input=truesize: decode_failures 1
- TH-congestion: no-congestion-scaling=True: decode_failures 23
- TH-congestion: faster: 9.12 s per simulated hour against 18.6 over 24 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `LD-interval` | 11.2 | 1.4 | 7.97x | 24 |
| `RF-duct` | 12.8 | 1.76 | 7.26x | 24 |
| `MS-router-late` | 11.8 | 1.76 | 6.74x | 24 |
| `LD-diurnal` | 9.92 | 1.56 | 6.35x | 24 |
| `SF-jitter-local` | 11.2 | 1.84 | 6.09x | 24 |
| `FW-signing-cost` | 9.61 | 1.6 | 6.02x | 24 |
| `SF-replay-order` | 10.1 | 1.68 | 5.99x | 24 |
| `SF-signed` | 10.1 | 1.74 | 5.81x | 24 |
| `SF-width` | 9.95 | 1.74 | 5.73x | 24 |
| `MS-roles-fav` | 9.79 | 1.75 | 5.60x | 24 |
| `RT-hopassign` | 10.1 | 1.81 | 5.58x | 24 |
| `LD-traceroute` | 11.2 | 2.08 | 5.38x | 24 |
| `SF-sr-retries` | 8.45 | 1.61 | 5.26x | 24 |
| `SF-jitter-global` | 9.06 | 1.78 | 5.09x | 24 |
| `SF-replay-order-broadcast` | 8.77 | 1.83 | 4.80x | 24 |
| `SF-provide-transport` | 8.77 | 1.86 | 4.72x | 24 |
| `AD-amplifiers` | 7.86 | 1.67 | 4.71x | 24 |
| `PR-repeats` | 7.65 | 1.65 | 4.64x | 24 |
| `SF-capacity` | 7.83 | 1.7 | 4.62x | 24 |
| `RT-favourites` | 7.61 | 1.68 | 4.52x | 24 |
| `SF-resolve` | 6.96 | 1.54 | 4.52x | 24 |
| `RT-rebroadcast` | 7.12 | 1.59 | 4.48x | 24 |
| `SF-advert-transport` | 7.94 | 1.81 | 4.38x | 24 |
| `SF-capacity-local` | 7.76 | 1.79 | 4.34x | 24 |
| `RT-spread` | 8.81 | 2.11 | 4.17x | 24 |
| `MS-roles` | 7.38 | 1.8 | 4.11x | 24 |
| `AD-badrouters` | 8.09 | 1.98 | 4.09x | 24 |
| `SF-servers-allrouters` | 7.28 | 1.84 | 3.96x | 24 |
| `AD-worst` | 13.5 | 3.48 | 3.87x | 24 |
| `AD-nomute` | 9.19 | 2.38 | 3.85x | 24 |
| `SC-signing` | 7.04 | 1.85 | 3.81x | 24 |
| `FW-mixed` | 6.26 | 1.67 | 3.76x | 24 |
| `SF-servers-spread` | 8.49 | 2.27 | 3.74x | 24 |
| `AD-flooding` | 9.25 | 2.55 | 3.63x | 24 |
| `DB-platform` | 9.28 | 2.59 | 3.59x | 24 |
| `FW-mixed-26` | 5.71 | 1.69 | 3.38x | 24 |
| `AD-siting` | 4.42 | 1.32 | 3.35x | 24 |
| `SF-bucket-mode` | 5.39 | 1.61 | 3.34x | 24 |
| `DB-hotstore` | 8.37 | 2.52 | 3.33x | 24 |
| `DG-loss` | 7.29 | 2.2 | 3.31x | 24 |
| `SF-cadence` | 11.2 | 3.39 | 3.30x | 24 |
| `SF-servers-flat` | 8.35 | 2.55 | 3.27x | 24 |
| `FW-firmware` | 5.57 | 1.72 | 3.24x | 24 |
| `RF-preset-turbo` | 5.04 | 1.56 | 3.23x | 20 |
| `PR-crladder` | 8.37 | 2.77 | 3.02x | 24 |
| `DM-mode` | 8.59 | 2.88 | 2.98x | 24 |
| `PR-protocol` | 4.1 | 1.42 | 2.89x | 24 |
| `AD-amplify-worst` | 4.82 | 1.76 | 2.74x | 24 |
| `PR-dmmode-cr` | 6.88 | 2.52 | 2.73x | 24 |
| `RT-hopspread` | 5.06 | 2.03 | 2.50x | 24 |
| `RT-hoplimit` | 4.26 | 1.79 | 2.38x | 24 |
| `MS-siting` | 4.45 | 1.97 | 2.25x | 24 |
| `SF-bucket-time` | 3.72 | 1.67 | 2.23x | 24 |
| `SF-window-size` | 3.14 | 1.43 | 2.19x | 24 |
| `RF-eu-presets` | 4.25 | 2.03 | 2.09x | 24 |
| `BL-control` | 3.57 | 1.72 | 2.08x | 24 |
| `SF-place-spread` | 6.06 | 2.92 | 2.08x | 24 |
| `SF-place-flat` | 6.03 | 3.01 | 2.00x | 24 |
| `RF-pulse` | 3.29 | 1.66 | 1.98x | 24 |
| `RF-txpower` | 3.13 | 1.6 | 1.96x | 24 |
| `SF-capacity-window` | 3.26 | 1.67 | 1.95x | 24 |
| `LD-chatty` | 8.2 | 4.91 | 1.67x | 24 |
| `MS-topology` | 3.07 | 1.87 | 1.64x | 24 |
| `FW-versions` | 2.65 | 1.65 | 1.61x | 24 |
| `DG-burst` | 7.78 | 4.89 | 1.59x | 24 |
| `MS-stretch` | 3.4 | 2.21 | 1.54x | 24 |
| `MS-hopscale` | 11.8 | 18 | 0.66x | 24 |
| `TH-congestion` | 9.12 | 18.6 | 0.49x | 24 |
| `MS-oversubscribed` | 9.5 | 19.6 | 0.48x | 24 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `MS-siting` | siting-mix | **text** | 0.136 → 0.969 | 0.833 | 0.133 → 0.968 | 4.2x advert_bytes | up | 4 |
| `PR-protocol` | protocol | **held** | 0 → 0.815 | 0.815 | 0.602 → 0.623 | 1.1x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.000 → 0.815 | 0.815 | 0.031 → 0.617 | 4.7x bytes_on_air | up | 5 |
| `RF-preset` | preset | **held** | 0.056 → 0.858 | 0.801 | 0.114 → 0.676 | 89x sr_bytes | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.021 → 0.811 | 0.791 | 0.023 → 0.573 | 6.4e+02x sr_bytes | down | 3 |
| `RF-txpower` | tx-power | **held** | 0.039 → 0.815 | 0.776 | 0.047 → 0.617 | 1.1e+02x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.056 → 0.815 | 0.759 | 0.114 → 0.617 | 89x sr_bytes | up | 4 |
| `BL-control` | protocol | **held** | 0 → 0.670 | 0.670 | 0.611 → 0.623 | 1x bytes_on_air | up | 2 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.076 → 0.740 | 0.664 | 0.064 → 0.570 | 2.2e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.169 → 0.815 | 0.646 | 0.058 → 0.617 | 9.7x sr_bytes | down | 4 |
| `MS-hopscale` | nodes | **held** | 0.313 → 0.815 | 0.502 | 0.196 → 0.617 | 8.4x bytes_on_air | down | 4 |
| `MS-topology` | topology | **text** | 0.404 → 0.880 | 0.476 | 0.394 → 0.878 | 2.3x sr_airtime | up | 4 |
| `RF-bw500` | preset | **held** | 0.044 → 0.485 | 0.442 | 0.070 → 0.470 | 55x sr_bytes | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.478 → 0.901 | 0.424 | 0.412 → 0.735 | 15x sr_airtime | down | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.308 → 0.720 | 0.412 | 0.196 → 0.481 | 4.4x bytes_on_air | down | 3 |
| `MS-density` | nodes | **text** | 0.533 → 0.904 | 0.371 | 0.518 → 0.895 | 4.9x advert_bytes | up | 5 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.144 → 0.503 | 0.360 | 0.143 → 0.498 | 3.5x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.475 → 0.834 | 0.359 | 0.370 → 0.655 | 12x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.446 → 0.782 | 0.336 | 0.413 → 0.769 | 2x sr_airtime | up | 4 |
| `DG-outage` | burst-loss | **held** | 0.498 → 0.815 | 0.317 | 0.309 → 0.617 | 1.9x sr_airtime | down | 4 |
| `DG-burst` | burst-loss | **held** | 0.504 → 0.815 | 0.311 | 0.314 → 0.617 | 1.7x sr_airtime | down | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.641 → 0.936 | 0.295 | 0.617 → 0.925 | 2.1x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.641 → 0.929 | 0.288 | 0.617 → 0.916 | 1.8x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.468 → 0.744 | 0.275 | 0.458 → 0.732 | 3.3x sr_bytes | down | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.446 → 0.712 | 0.266 | 0.413 → 0.695 | 1.7x sr_airtime | up | 3 |
| `SF-place-flat` | place | **held** | 0.575 → 0.815 | 0.240 | 0.615 → 0.629 | 4.5x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.575 → 0.815 | 0.240 | 0.615 → 0.629 | 4.5x sr_bytes | up | 6 |
| `RT-spread` | hop-spread | **held** | 0.579 → 0.815 | 0.236 | 0.413 → 0.617 | 1.5x sr_airtime | up | 2 |
| `AD-badrouters` | role-placement | **held** | 0.577 → 0.811 | 0.235 | 0.420 → 0.573 | 2x sr_airtime | down | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.687 → 0.899 | 0.212 | 0.660 → 0.889 | 3.6x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **held** | 0.610 → 0.815 | 0.205 | 0.440 → 0.617 | 1.8x sr_airtime | down | 4 |
| `DG-loss` | extra-loss | **held** | 0.610 → 0.815 | 0.205 | 0.441 → 0.617 | 1.6x sr_airtime | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.615 → 0.815 | 0.200 | 0.611 → 0.619 | 2.7x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.615 → 0.815 | 0.200 | 0.608 → 0.619 | 2.7x sr_bytes | down | 5 |
| `SF-servers-allrouters` | servers | **held** | 0.681 → 0.856 | 0.175 | 0.616 → 0.621 | 6.6x sr_bytes | up | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.641 → 0.815 | 0.175 | 0.617 → 0.780 | 1.4x sr_airtime | up | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.733 → 0.900 | 0.167 | 0.617 → 0.748 | 2.4x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **held** | 0.650 → 0.815 | 0.165 | 0.494 → 0.617 | 1.5x sr_bytes | down | 3 |
| `DB-hotstore` | max-num-nodes | **held** | 0.710 → 0.863 | 0.153 | 0.562 → 0.679 | 2.6x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.710 → 0.863 | 0.153 | 0.562 → 0.679 | 2.6x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **held** | 0.732 → 0.883 | 0.151 | 0.563 → 0.685 | 7.6x sr_airtime | up | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.716 → 0.864 | 0.148 | 0.617 → 0.748 | 2.5x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.339 → 0.481 | 0.142 | 0.212 → 0.307 | 3.9x sr_airtime | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.674 → 0.815 | 0.141 | 0.617 → 0.621 | 32x sr_airtime | down | 3 |
| `FW-versions` | profile | **text** | 0.641 → 0.771 | 0.131 | 0.617 → 0.761 | 2.8x bytes_on_air | down | 5 |
| `SF-servers-flat` | servers | **held** | 0.814 → 0.944 | 0.130 | 0.608 → 0.631 | 14x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.814 → 0.944 | 0.130 | 0.608 → 0.631 | 14x sr_bytes | up | 4 |
| `FW-firmware` | profile | **text** | 0.641 → 0.755 | 0.114 | 0.617 → 0.744 | 2.8x bytes_on_air | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.609 → 0.721 | 0.112 | 0.573 → 0.708 | 2.1x sr_bytes | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.609 → 0.721 | 0.112 | 0.573 → 0.708 | 2.1x sr_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.705 → 0.807 | 0.101 | 0.606 → 0.615 | 4.9x sr_bytes | up | 3 |
| `SF-cadence` | trigger | **held** | 0.775 → 0.867 | 0.092 | 0.584 → 0.621 | 17x advert_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.815 → 0.898 | 0.083 | 0.617 → 0.623 | 2.2x advert_bytes | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.784 → 0.867 | 0.082 | 0.588 → 0.621 | 9.1x advert_bytes | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.608 → 0.687 | 0.079 | 0.584 → 0.662 | 1.4x sr_airtime | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.741 → 0.816 | 0.075 | 0.566 → 0.617 | 1.5x sr_airtime | down | 4 |
| `SF-resolve` | resolve | **held** | 0.745 → 0.815 | 0.070 | 0.617 → 0.628 | 5.8x advert_bytes | up | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.641 → 0.698 | 0.057 | 0.617 → 0.677 | 3.3x bytes_on_air | down | 2 |
| `SF-window-size` | window-size | **held** | 0.807 → 0.861 | 0.054 | 0.607 → 0.613 | 4.7x advert_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.807 → 0.860 | 0.053 | 0.607 → 0.618 | 3.3x advert_bytes | down | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.641 → 0.686 | 0.045 | 0.617 → 0.617 | 3.5x sr_airtime | up | 2 |
| `LD-diurnal` | diurnal | **held** | 0.805 → 0.842 | 0.036 | 0.615 → 0.632 | 1.2x advert_bytes | down | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.825 → 0.860 | 0.035 | 0.603 → 0.619 | 5.2x advert_bytes | down | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.309 → 0.343 | 0.034 | 0.305 → 0.339 | 2x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.796 → 0.831 | 0.034 | 0.611 → 0.620 | 1.2x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.796 → 0.831 | 0.034 | 0.611 → 0.620 | 1.2x sr_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.794 → 0.828 | 0.034 | 0.619 → 0.622 | 1.3x sr_bytes | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.805 → 0.838 | 0.033 | 0.598 → 0.626 | 1.3x sr_bytes | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.783 → 0.815 | 0.032 | 0.614 → 0.617 | 3.2x advert_bytes | up | 4 |
| `AD-worst` | role-placement | **text** | 0.679 → 0.710 | 0.031 | 0.662 → 0.702 | 2x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.798 → 0.826 | 0.028 | 0.617 → 0.641 | 1.3x bytes_on_air | down | 4 |
| `SF-capacity` | capacity | **held** | 0.812 → 0.840 | 0.028 | 0.608 → 0.620 | 5.5x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.812 → 0.840 | 0.028 | 0.608 → 0.620 | 5.5x advert_bytes | up | 5 |
| `MS-roles` | role-mix | **text** | 0.609 → 0.635 | 0.026 | 0.573 → 0.615 | 1.4x sr_bytes | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.791 → 0.815 | 0.023 | 0.596 → 0.617 | 1.1x sr_bytes | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.638 → 0.660 | 0.022 | 0.613 → 0.639 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.755 → 0.777 | 0.022 | 0.611 → 0.617 | 1.1x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.883 → 0.899 | 0.016 | 0.871 → 0.889 | 1.2x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.802 → 0.815 | 0.012 | 0.617 → 0.630 | 1.2x sr_airtime | down | 2 |
| `DM-mode` | dm-mode | **text** | 0.600 → 0.609 | 0.009 | 0.600 → 0.609 | 1.2x sr_airtime | up | 3 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.596 → 0.604 | 0.008 | 0.596 → 0.604 | 1.3x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.708 → 0.716 | 0.008 | 0.596 → 0.598 | 1.1x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.809 → 0.815 | 0.006 | 0.617 → 0.624 | 1.1x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.894 → 0.899 | 0.005 | 0.885 → 0.889 | 1.1x bytes_on_air | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.987 → 0.990 | 0.003 | 0.887 → 0.889 | 1.1x sr_airtime | up | 2 |

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
| none | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| sprinkled | 1 | 0.768 | 0.757 | 0.011 | - | - | 0.881 | 0.883 | 0.484 | 1.12x | 13.5/17.7/20.2% | 1.6/4.7% | 3 |
| arms-race | 1 | 0.929 | 0.916 | 0.013 | - | - | 0.964 | 0.981 | 0.639 | 0.97x | 16.2/19.6/24.1% | 1.2/4.8% | 3 |

> amplifier-mix=none: decode_failures 33

> amplifier-mix=arms-race: decode_failures 34

> slower: 7.86 s per simulated hour against 1.67 over 24 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.783 | 0.763 | 0.020 | - | - | 0.822 | 0.834 | 0.482 | 1.20x | 14.9/20.1/22.6% | 1.9/4.7% | 3 |
| 0.3 | 1 | 0.936 | 0.925 | 0.011 | - | - | 0.988 | 0.988 | 0.637 | 1.07x | 20.3/24.7/28.2% | 1.4/5.1% | 3 |

> amplify-worst=0.0: decode_failures 33

> slower: 4.82 s per simulated hour against 1.76 over 24 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.609 | 0.573 | 0.037 | - | - | 0.811 | 0.886 | 0.086 | 1.16x | 12.2/16.8/19.3% | 1.9/4.8% | 3 |
| inverse | 1 | 0.442 | 0.420 | 0.022 | - | - | 0.577 | 0.770 | 0.101 | 1.13x | 10.8/15.6/17.7% | 1.9/3.3% | 3 |
| random | 1 | 0.490 | 0.464 | 0.026 | - | - | 0.740 | 0.821 | 0.225 | 1.15x | 10.7/18.2/23.0% | 1.9/4.9% | 3 |

> role-placement=degree: decode_failures 36

> role-placement=inverse: decode_failures 14

> role-placement=random: decode_failures 24

> slower: 8.09 s per simulated hour against 1.98 over 24 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.609 | 0.573 | 0.037 | - | - | 0.811 | 0.886 | 0.086 | 1.16x | 12.2/16.8/19.3% | 1.9/4.8% | 3 |
| all-routers | 1 | 0.721 | 0.708 | 0.013 | - | - | 0.848 | 0.925 | 0.525 | 2.26x | 21.2/27.2/31.9% | 3.6/4.9% | 3 |

> role-mix=baymesh-2026-08: decode_failures 36

> role-mix=all-routers: decode_failures 26

> slower: 9.25 s per simulated hour against 2.55 over 24 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.609 | 0.573 | 0.037 | - | - | 0.811 | 0.886 | 0.086 | 1.16x | 12.2/16.8/19.3% | 1.9/4.8% | 3 |
| no-mute | 1 | 0.639 | 0.615 | 0.025 | - | - | 0.850 | 0.893 | 0.383 | 1.27x | 12.3/17.2/20.8% | 2.1/4.8% | 3 |
| all-routers | 1 | 0.721 | 0.708 | 0.013 | - | - | 0.848 | 0.925 | 0.525 | 2.26x | 21.2/27.2/31.9% | 3.6/4.9% | 3 |

> role-mix=baymesh-2026-08: decode_failures 36

> role-mix=no-mute: decode_failures 32

> role-mix=all-routers: decode_failures 26

> slower: 9.19 s per simulated hour against 2.38 over 24 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.609 | 0.573 | 0.037 | - | - | 0.811 | 0.886 | 0.086 | 1.16x | 12.2/16.8/19.3% | 1.9/4.8% | 3 |
| local-typical | 1 | 0.404 | 0.387 | 0.018 | - | - | 0.548 | 0.735 | 0.000 | 1.05x | 8.9/21.7/29.9% | 1.6/5.4% | 3 |
| basement-heavy | 1 | 0.023 | 0.023 | 0.000 | - | - | 0.021 | 0.042 | 0.000 | 0.28x | 0.6/2.3/3.6% | 0.3/1.2% | 2 |

> siting-mix=uniform: decode_failures 36

> siting-mix=local-typical: decode_failures 10

> siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count

> slower: 4.42 s per simulated hour against 1.32 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.710 | 0.702 | 0.008 | - | - | 0.883 | 0.884 | 0.000 | 2.31x | 14.0/24.6/33.4% | 1.9/5.2% | 3 |
| inverse | 1 | 0.679 | 0.662 | 0.017 | - | - | 0.857 | 0.886 | 0.000 | 2.25x | 13.6/23.2/29.4% | 1.8/3.2% | 3 |

> role-placement=inverse: decode_failures 76

> slower: 13.5 s per simulated hour against 3.48 over 24 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.623 | 0.623 | 0.000 | - | - | 0 | 0.000 | 0.397 | 1.19x | 11.8/16.4/19.8% | 1.9/4.3% | 3 |
| sr | 1 | 0.624 | 0.611 | 0.013 | - | - | 0.670 | 0.960 | 0.430 | 1.20x | 11.7/16.6/20.1% | 1.8/4.4% | 3 |

> protocol=sr: decode_failures 20

> slower: 3.57 s per simulated hour against 1.72 over 24 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.580 | 0.562 | 0.018 | - | - | 0.710 | 0.799 | 0.357 | 2.42x | 24.3/33.4/38.5% | 4.0/7.7% | 3 |
| 100 | 1 | 0.698 | 0.679 | 0.018 | - | - | 0.863 | 0.900 | 0.474 | 1.40x | 14.3/19.9/22.8% | 2.3/4.6% | 3 |
| 120 | 1 | 0.698 | 0.679 | 0.018 | - | - | 0.863 | 0.900 | 0.474 | 1.40x | 14.3/19.9/22.8% | 2.3/4.6% | 3 |
| 250 | 1 | 0.698 | 0.679 | 0.018 | - | - | 0.863 | 0.900 | 0.474 | 1.40x | 14.3/19.9/22.8% | 2.3/4.6% | 3 |

> max-num-nodes=10: decode_failures 21

> max-num-nodes=100: decode_failures 30

> max-num-nodes=120: decode_failures 30

> max-num-nodes=250: decode_failures 30

> slower: 8.37 s per simulated hour against 2.52 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.215 | 0.212 | 0.003 | - | - | 0.339 | 0.354 | 0.091 | 10.36x | 27.0/41.9/56.0% | 3.8/9.4% | 3 |
| 120 | 1 | 0.309 | 0.305 | 0.004 | - | - | 0.481 | 0.483 | 0.124 | 4.71x | 12.2/19.6/26.7% | 1.7/4.7% | 3 |
| 250 | 1 | 0.311 | 0.307 | 0.004 | - | - | 0.472 | 0.484 | 0.131 | 4.65x | 12.0/19.1/26.4% | 1.7/4.6% | 3 |

> max-num-nodes=10: decode_failures 28

> max-num-nodes=120: decode_failures 1

> max-num-nodes=250: decode_failures 23

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.698 | 0.679 | 0.018 | - | - | 0.863 | 0.900 | 0.474 | 1.40x | 14.3/19.9/22.8% | 2.3/4.6% | 3 |
| baymesh-2026-08 | 1 | 0.698 | 0.679 | 0.018 | - | - | 0.863 | 0.900 | 0.474 | 1.40x | 14.3/19.9/22.8% | 2.3/4.6% | 3 |
| constrained | 1 | 0.580 | 0.562 | 0.018 | - | - | 0.710 | 0.799 | 0.357 | 2.42x | 24.3/33.4/38.5% | 4.0/7.7% | 3 |

> platform-mix=uniform: decode_failures 30

> platform-mix=baymesh-2026-08: decode_failures 30

> platform-mix=constrained: decode_failures 21

> slower: 9.28 s per simulated hour against 2.59 over 24 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.687 | 0.662 | 0.025 | - | - | 0.846 | 0.870 | 0.440 | 5.52x | 49.0/62.6/67.8% | 3.7/12.2% | 3 |
| 25 | 1 | 0.687 | 0.662 | 0.025 | - | - | 0.846 | 0.870 | 0.440 | 5.52x | 49.0/62.6/67.8% | 3.7/12.2% | 3 |
| 100 | 1 | 0.687 | 0.662 | 0.025 | - | - | 0.846 | 0.870 | 0.440 | 5.52x | 49.0/62.6/67.8% | 3.7/12.2% | 3 |
| 2000 | 1 | 0.687 | 0.662 | 0.025 | - | - | 0.846 | 0.870 | 0.440 | 5.52x | 49.0/62.6/67.8% | 3.7/12.2% | 3 |

> warm-num-nodes=0: decode_failures 45

> warm-num-nodes=25: decode_failures 45

> warm-num-nodes=100: decode_failures 45

> warm-num-nodes=2000: decode_failures 45

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.545 | 0.521 | 0.024 | - | - | 0.757 | 0.858 | 0.302 | 1.12x | 11.0/16.3/19.2% | 1.8/4.1% | 3 |
| 0.2 | 1 | 0.427 | 0.407 | 0.020 | - | - | 0.608 | 0.763 | 0.213 | 1.05x | 10.5/15.4/18.4% | 1.7/3.7% | 3 |
| 0.3 | 1 | 0.332 | 0.314 | 0.018 | - | - | 0.504 | 0.678 | 0.146 | 0.97x | 10.0/14.2/16.9% | 1.5/3.2% | 3 |

> burst-loss=0.0: decode_failures 33

> burst-loss=0.1: decode_failures 25

> burst-loss=0.2: decode_failures 22

> burst-loss=0.3: decode_failures 15

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.583 | 0.557 | 0.026 | - | - | 0.766 | 0.864 | 0.350 | 1.23x | 12.1/17.7/20.6% | 1.9/4.3% | 3 |
| 0.2 | 1 | 0.526 | 0.504 | 0.022 | - | - | 0.689 | 0.830 | 0.279 | 1.24x | 12.3/18.2/21.3% | 2.0/4.2% | 3 |
| 0.3 | 1 | 0.458 | 0.441 | 0.017 | - | - | 0.610 | 0.758 | 0.184 | 1.26x | 12.6/18.5/21.9% | 1.9/4.0% | 3 |

> extra-loss=0.0: decode_failures 33

> extra-loss=0.1: decode_failures 31

> extra-loss=0.2: decode_failures 26

> extra-loss=0.3: decode_failures 18

> slower: 7.29 s per simulated hour against 2.2 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.1 | 1 | 0.540 | 0.516 | 0.024 | - | - | 0.712 | 0.854 | 0.288 | 1.15x | 11.4/16.6/19.6% | 1.8/3.9% | 3 |
| 0.2 | 1 | 0.446 | 0.427 | 0.018 | - | - | 0.616 | 0.775 | 0.229 | 1.08x | 10.7/15.6/18.6% | 1.6/3.9% | 3 |
| 0.3 | 1 | 0.328 | 0.309 | 0.018 | - | - | 0.498 | 0.664 | 0.151 | 1.00x | 10.1/14.3/17.1% | 1.5/3.2% | 3 |

> burst-loss=0.0: decode_failures 33

> burst-loss=0.1: decode_failures 29

> burst-loss=0.2: decode_failures 16

> burst-loss=0.3: decode_failures 16

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.600 | 0.600 | 0.000 | - | - | 0.693 | 0.890 | 0.378 | 1.43x | 14.2/20.6/24.3% | 2.3/5.4% | 3 |
| directed-with-late-flood | 1 | 0.604 | 0.604 | 0.000 | - | - | 0.700 | 0.895 | 0.363 | 1.34x | 13.1/19.2/22.8% | 2.1/5.1% | 3 |
| m4-early-flood | 1 | 0.609 | 0.609 | 0.000 | - | - | 0.702 | 0.888 | 0.384 | 1.35x | 13.3/19.3/22.9% | 2.1/5.1% | 3 |

> dm-mode=flood-only: decode_failures 26

> dm-mode=directed-with-late-flood: decode_failures 25

> dm-mode=m4-early-flood: decode_failures 27

> slower: 8.59 s per simulated hour against 2.88 over 24 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.755 | 0.744 | 0.011 | - | - | 0.927 | 0.931 | 0.234 | 0.76x | 7.7/9.9/10.9% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> profile=2.8: decode_failures 33

> slower: 5.57 s per simulated hour against 1.72 over 24 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.704 | 0.674 | 0.030 | - | - | 0.864 | 0.896 | 0.302 | 1.07x | 11.3/14.7/18.9% | 1.6/4.1% | 3 |
| 0.5 | 1 | 0.758 | 0.748 | 0.011 | - | - | 0.819 | 0.885 | 0.313 | 1.04x | 11.9/14.5/16.7% | 1.7/3.3% | 3 |
| 0.75 | 1 | 0.644 | 0.637 | 0.007 | - | - | 0.716 | 0.718 | 0.319 | 0.92x | 9.7/12.7/13.9% | 1.5/3.3% | 3 |

> legacy-fraction=0.0: decode_failures 33

> legacy-fraction=0.25: decode_failures 13

> legacy-fraction=0.5: decode_failures 39

> slower: 6.26 s per simulated hour against 1.67 over 24 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.697 | 0.678 | 0.019 | - | - | 0.839 | 0.903 | 0.336 | 1.09x | 11.7/15.0/19.2% | 1.6/4.3% | 3 |
| 0.5 | 1 | 0.761 | 0.748 | 0.013 | - | - | 0.900 | 0.903 | 0.362 | 1.01x | 11.7/15.1/17.1% | 1.6/3.3% | 3 |
| 0.75 | 1 | 0.658 | 0.650 | 0.008 | - | - | 0.733 | 0.736 | 0.309 | 0.92x | 9.6/12.9/14.5% | 1.5/3.4% | 3 |

> legacy-fraction=0.0: decode_failures 33

> legacy-fraction=0.25: decode_failures 20

> legacy-fraction=0.5: decode_failures 7

> slower: 5.71 s per simulated hour against 1.69 over 24 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.698 | 0.677 | 0.021 | - | - | 0.868 | 0.927 | 0.448 | 0.65x | 6.6/10.1/12.1% | 1.0/2.7% | 3 |
| signing=true | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> profile-flag=signing=false: decode_failures 44

> profile-flag=signing=true: decode_failures 33

> slower: 9.61 s per simulated hour against 1.6 over 24 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.757 | 0.746 | 0.011 | - | - | 0.929 | 0.930 | 0.285 | 0.77x | 8.1/11.2/12.0% | 1.2/2.5% | 3 |
| 2.5 | 1 | 0.750 | 0.738 | 0.012 | - | - | 0.925 | 0.928 | 0.243 | 0.78x | 8.2/11.2/12.1% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.753 | 0.741 | 0.012 | - | - | 0.929 | 0.933 | 0.259 | 0.76x | 8.1/11.1/12.0% | 1.1/2.5% | 3 |
| 2.7 | 1 | 0.771 | 0.761 | 0.011 | - | - | 0.934 | 0.935 | 0.258 | 0.76x | 8.2/11.8/13.4% | 1.1/2.7% | 3 |
| 2.8 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> profile=2.8: decode_failures 33

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.677 | 0.655 | 0.022 | - | - | 0.834 | 0.928 | 0.433 | 0.82x | 8.0/11.8/14.0% | 1.3/3.1% | 3 |
| 900 | 1 | 0.583 | 0.563 | 0.020 | - | - | 0.732 | 0.857 | 0.353 | 1.85x | 18.3/26.1/30.7% | 2.9/6.8% | 3 |
| 300 | 1 | 0.380 | 0.370 | 0.010 | - | - | 0.475 | 0.654 | 0.222 | 4.05x | 38.8/52.5/60.5% | 6.6/13.8% | 3 |

> broadcast-interval-s=3600: decode_failures 37

> broadcast-interval-s=900: decode_failures 26

> broadcast-interval-s=300: decode_failures 6

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.751 | 0.735 | 0.016 | - | - | 0.901 | 0.922 | 0.543 | 0.92x | 9.2/12.9/15.1% | 1.5/3.4% | 3 |
| 900 | 1 | 0.672 | 0.651 | 0.021 | - | - | 0.818 | 0.872 | 0.480 | 2.00x | 20.1/27.6/32.5% | 3.3/7.1% | 3 |
| 300 | 1 | 0.418 | 0.412 | 0.006 | - | - | 0.478 | 0.637 | 0.278 | 4.16x | 39.9/52.5/60.7% | 7.0/13.7% | 3 |

> broadcast-interval-s=3600: decode_failures 24

> broadcast-interval-s=900: decode_failures 34

> broadcast-interval-s=300: decode_failures 3

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.659 | 0.632 | 0.026 | - | - | 0.842 | 0.920 | 0.417 | 1.13x | 11.0/16.2/19.3% | 1.8/4.4% | 3 |
| sinusoid | 1 | 0.637 | 0.615 | 0.023 | - | - | 0.805 | 0.909 | 0.372 | 1.11x | 11.0/15.7/18.7% | 1.7/4.1% | 3 |
| commuter | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> diurnal=flat: decode_failures 36

> diurnal=sinusoid: decode_failures 26

> diurnal=commuter: decode_failures 33

> slower: 9.92 s per simulated hour against 1.56 over 24 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.583 | 0.563 | 0.020 | - | - | 0.732 | 0.857 | 0.353 | 1.85x | 18.3/26.1/30.7% | 2.9/6.8% | 3 |
| 3600 | 1 | 0.677 | 0.655 | 0.022 | - | - | 0.834 | 0.928 | 0.433 | 0.82x | 8.0/11.8/14.0% | 1.3/3.1% | 3 |
| 10800 | 1 | 0.700 | 0.680 | 0.020 | - | - | 0.865 | 0.948 | 0.455 | 0.54x | 5.3/8.0/9.3% | 0.8/2.1% | 3 |
| 43200 | 1 | 0.706 | 0.685 | 0.021 | - | - | 0.883 | 0.951 | 0.449 | 0.36x | 3.5/5.7/6.7% | 0.6/1.6% | 3 |

> broadcast-interval-s=900: decode_failures 26

> broadcast-interval-s=3600: decode_failures 37

> broadcast-interval-s=10800: decode_failures 38

> broadcast-interval-s=43200: decode_failures 47

> slower: 11.2 s per simulated hour against 1.4 over 24 prior run(s) - 8.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.628 | 0.605 | 0.024 | - | - | 0.805 | 0.875 | 0.404 | 1.26x | 12.3/18.0/21.4% | 1.9/4.8% | 3 |
| 1.0 | 1 | 0.632 | 0.602 | 0.030 | - | - | 0.816 | 0.891 | 0.379 | 1.34x | 13.2/19.2/22.8% | 2.1/5.0% | 3 |
| 4.0 | 1 | 0.589 | 0.566 | 0.023 | - | - | 0.741 | 0.851 | 0.352 | 1.61x | 16.0/23.3/27.5% | 2.6/6.1% | 3 |

> traceroute-per-hour=0.0: decode_failures 33

> traceroute-per-hour=0.25: decode_failures 36

> traceroute-per-hour=1.0: decode_failures 38

> traceroute-per-hour=4.0: decode_failures 32

> slower: 11.2 s per simulated hour against 2.08 over 24 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.687 | 0.662 | 0.025 | - | - | 0.846 | 0.870 | 0.440 | 5.52x | 49.0/62.6/67.8% | 3.7/12.2% | 3 |
| 1.0 | 1 | 0.608 | 0.584 | 0.024 | - | - | 0.778 | 0.796 | 0.387 | 6.41x | 55.2/68.6/73.0% | 4.5/13.7% | 3 |

> traceroute-per-hour=0.0: decode_failures 45

> traceroute-per-hour=1.0: decode_failures 44

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.533 | 0.518 | 0.015 | - | - | 0.715 | 0.720 | 0.000 | 1.17x | 13.9/19.4/24.8% | 2.6/5.5% | 3 |
| 60 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 90 | 1 | 0.834 | 0.826 | 0.008 | - | - | 0.950 | 0.951 | 0.554 | 1.61x | 16.1/21.9/25.5% | 1.5/4.7% | 3 |
| 120 | 1 | 0.899 | 0.889 | 0.011 | - | - | 0.987 | 0.987 | 0.649 | 1.93x | 18.1/24.7/28.7% | 1.3/5.1% | 3 |
| 150 | 1 | 0.904 | 0.895 | 0.009 | - | - | 0.993 | 0.993 | 0.686 | 2.41x | 21.3/28.9/33.7% | 1.2/5.2% | 3 |

> nodes=40: decode_failures 2

> nodes=60: decode_failures 33

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 120 | 1 | 0.490 | 0.479 | 0.012 | - | - | 0.724 | 0.726 | 0.151 | 2.32x | 12.0/19.4/25.8% | 1.7/5.2% | 3 |
| 250 | 1 | 0.309 | 0.305 | 0.004 | - | - | 0.449 | 0.456 | 0.126 | 4.89x | 12.5/20.4/27.9% | 1.8/5.0% | 3 |
| 500 | 1 | 0.197 | 0.196 | 0.002 | - | - | 0.313 | 0.314 | 0.034 | 9.84x | 13.2/21.4/37.9% | 1.7/5.2% | 3 |

> nodes=60: decode_failures 33

> nodes=250: decode_failures 31

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.491 | 0.481 | 0.011 | - | - | 0.720 | 0.724 | 0.149 | 2.17x | 11.4/18.2/24.3% | 1.6/4.9% | 3 |
| 250 | 1 | 0.309 | 0.305 | 0.004 | - | - | 0.481 | 0.483 | 0.124 | 4.71x | 12.2/19.6/26.7% | 1.7/4.7% | 3 |
| 500 | 1 | 0.197 | 0.196 | 0.002 | - | - | 0.308 | 0.309 | 0.038 | 9.38x | 12.6/20.6/36.6% | 1.6/4.9% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 2

> faster: 9.5 s per simulated hour against 19.6 over 24 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.635 | 0.615 | 0.020 | - | - | 0.789 | 0.896 | 0.402 | 1.21x | 11.8/17.2/20.4% | 1.9/4.5% | 3 |
| baymesh-2026-08 | 1 | 0.609 | 0.573 | 0.037 | - | - | 0.811 | 0.886 | 0.086 | 1.16x | 12.2/16.8/19.3% | 1.9/4.8% | 3 |

> role-mix=legacy-default: decode_failures 24

> role-mix=baymesh-2026-08: decode_failures 36

> slower: 7.38 s per simulated hour against 1.8 over 24 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.649 | 0.626 | 0.023 | - | - | 0.805 | 0.895 | 0.380 | 1.23x | 12.0/17.6/20.9% | 1.9/4.6% | 3 |
| baymesh-2026-08 | 1 | 0.634 | 0.598 | 0.036 | - | - | 0.838 | 0.889 | 0.066 | 1.18x | 12.2/17.8/19.6% | 1.9/4.6% | 3 |

> role-mix=legacy-default: decode_failures 37

> role-mix=baymesh-2026-08: decode_failures 24

> slower: 9.79 s per simulated hour against 1.75 over 24 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.05 | 1 | 0.646 | 0.619 | 0.027 | - | - | 0.822 | 0.896 | 0.423 | 1.27x | 13.3/18.7/20.4% | 2.0/4.5% | 3 |
| 0.1 | 1 | 0.667 | 0.641 | 0.025 | - | - | 0.826 | 0.888 | 0.432 | 1.39x | 14.4/20.5/23.4% | 2.2/4.6% | 3 |
| 0.2 | 1 | 0.660 | 0.638 | 0.022 | - | - | 0.798 | 0.882 | 0.426 | 1.53x | 15.5/23.7/29.3% | 2.4/4.4% | 3 |

> router-late-fraction=0.0: decode_failures 33

> router-late-fraction=0.05: decode_failures 37

> router-late-fraction=0.1: decode_failures 46

> router-late-fraction=0.2: decode_failures 35

> slower: 11.8 s per simulated hour against 1.76 over 24 prior run(s) - 6.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| local-typical | 1 | 0.392 | 0.375 | 0.017 | - | - | 0.528 | 0.684 | 0.000 | 1.24x | 9.7/25.1/32.0% | 1.9/5.2% | 3 |
| event | 1 | 0.136 | 0.133 | 0.002 | - | - | 0.247 | 0.255 | 0.000 | 0.90x | 4.7/9.7/14.2% | 1.5/3.2% | 3 |
| backbone | 1 | 0.969 | 0.968 | 0.001 | - | - | 0.997 | 0.998 | 0.869 | 1.11x | 21.6/30.6/32.3% | 1.4/5.3% | 3 |

> siting-mix=uniform: decode_failures 33

> siting-mix=local-typical: decode_failures 15

> slower: 4.45 s per simulated hour against 1.97 over 24 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.744 | 0.732 | 0.012 | - | - | 0.863 | 0.867 | 0.463 | 1.38x | 19.8/27.7/32.7% | 3.2/6.7% | 3 |
| 60 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 90 | 1 | 0.624 | 0.612 | 0.012 | - | - | 0.815 | 0.818 | 0.215 | 1.72x | 12.4/19.3/23.3% | 1.7/4.7% | 3 |
| 120 | 1 | 0.490 | 0.479 | 0.012 | - | - | 0.724 | 0.726 | 0.151 | 2.32x | 12.0/19.4/25.8% | 1.7/5.2% | 3 |
| 150 | 1 | 0.468 | 0.458 | 0.011 | - | - | 0.709 | 0.710 | 0.163 | 2.85x | 12.5/22.0/25.5% | 1.6/4.7% | 3 |

> nodes=60: decode_failures 33

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 1.25 | 1 | 0.263 | 0.262 | 0.001 | - | - | 0.248 | 0.248 | 0.035 | 1.32x | 9.8/15.3/19.3% | 2.0/4.9% | 3 |
| 1.5 | 1 | 0.144 | 0.143 | 0.001 | - | - | 0.216 | 0.237 | 0.000 | 0.93x | 4.8/9.3/10.8% | 1.5/3.2% | 3 |
| 2.0 | 1 | 0.060 | 0.058 | 0.002 | - | - | 0.169 | 0.176 | 0.000 | 0.49x | 1.9/4.3/7.5% | 0.7/2.1% | 3 |

> stretch=1.0: decode_failures 33

> stretch=1.5: decode_failures 5

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| clustered | 1 | 0.816 | 0.814 | 0.003 | - | - | 0.957 | 0.959 | 0.000 | 1.18x | 19.3/28.6/31.9% | 1.6/5.6% | 3 |
| corridor | 1 | 0.404 | 0.394 | 0.009 | - | - | 0.634 | 0.639 | 0.177 | 1.66x | 14.0/20.6/22.4% | 2.4/6.2% | 3 |
| hub | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.929 | 0.930 | 0.700 | 1.17x | 21.3/32.1/34.2% | 1.7/5.3% | 3 |

> topology=uniform: decode_failures 33

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.604 | 0.604 | 0.000 | - | - | 0.700 | 0.895 | 0.363 | 1.34x | 13.1/19.2/22.8% | 2.1/5.1% | 3 |
| True | 1 | 0.596 | 0.596 | 0.000 | - | - | 0.708 | 0.889 | 0.385 | 1.36x | 13.4/19.5/23.1% | 2.1/5.2% | 3 |

> coding-rate-ladder=False: decode_failures 25

> coding-rate-ladder=True: decode_failures 26

> slower: 8.37 s per simulated hour against 2.77 over 24 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.596 | 0.596 | 0.000 | - | - | 0.708 | 0.889 | 0.385 | 1.36x | 13.4/19.5/23.1% | 2.1/5.2% | 3 |
| m4-early-flood | 1 | 0.598 | 0.598 | 0.000 | - | - | 0.716 | 0.894 | 0.376 | 1.36x | 13.3/19.6/23.1% | 2.2/5.2% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 26

> dm-mode=m4-early-flood: decode_failures 26

> slower: 6.88 s per simulated hour against 2.52 over 24 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.623 | 0.623 | 0.000 | - | - | 0 | 0.000 | 0.397 | 1.19x | 11.8/16.4/19.8% | 1.9/4.3% | 3 |
| chain | 1 | 0.616 | 0.602 | 0.014 | - | - | 0.719 | 0.887 | 0.401 | 1.36x | 13.5/20.2/23.5% | 2.1/5.4% | 3 |
| sr | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> protocol=sr: decode_failures 33

> slower: 4.1 s per simulated hour against 1.42 over 24 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| True | 1 | 0.652 | 0.630 | 0.023 | - | - | 0.802 | 0.915 | 0.428 | 1.23x | 12.0/17.3/20.7% | 1.9/4.5% | 3 |

> extra-repeats=False: decode_failures 33

> extra-repeats=True: decode_failures 34

> slower: 7.65 s per simulated hour against 1.65 over 24 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.899 | 0.889 | 0.011 | - | - | 0.987 | 0.987 | 0.649 | 1.93x | 18.1/24.7/28.7% | 1.3/5.1% | 3 |
| True | 1 | 0.898 | 0.887 | 0.011 | - | - | 0.990 | 0.991 | 0.672 | 2.00x | 18.5/25.1/29.1% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.070 | 0.070 | 0.000 | - | - | 0.044 | 0.131 | 0.000 | 0.03x | 0.1/0.2/0.5% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.153 | 0.152 | 0.001 | - | - | 0.224 | 0.242 | 0.000 | 0.14x | 0.8/1.5/1.8% | 0.2/0.5% | 3 |
| LONG_TURBO | 1 | 0.481 | 0.470 | 0.010 | - | - | 0.485 | 0.492 | 0.182 | 1.22x | 10.6/13.5/16.1% | 2.0/4.1% | 3 |

> preset=MEDIUM_TURBO: decode_failures 9

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 0.25 | 1 | 0.687 | 0.652 | 0.035 | - | - | 0.855 | 0.901 | 0.459 | 1.12x | 13.0/17.8/21.0% | 1.7/4.6% | 3 |
| 1.0 | 1 | 0.815 | 0.780 | 0.035 | - | - | 0.928 | 0.948 | 0.653 | 0.94x | 17.1/20.6/23.5% | 1.3/4.9% | 3 |

> duct-per-hour=0.0: decode_failures 33

> duct-per-hour=0.25: decode_failures 49

> duct-per-hour=1.0: decode_failures 39

> slower: 12.8 s per simulated hour against 1.76 over 24 prior run(s) - 7.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.114 | 0.114 | 0.000 | - | - | 0.056 | 0.169 | 0.000 | 0.07x | 0.4/0.7/0.9% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| LITE_FAST | 1 | 0.483 | 0.472 | 0.011 | - | - | 0.544 | 0.781 | 0.274 | 0.87x | 8.0/11.2/12.5% | 1.4/3.2% | 3 |
| NARROW_SLOW | 1 | 0.536 | 0.524 | 0.012 | - | - | 0.561 | 0.693 | 0.287 | 1.14x | 10.6/14.4/17.8% | 1.9/4.1% | 3 |

> preset=LONG_FAST: decode_failures 33

> preset=LITE_FAST: decode_failures 12

> preset=NARROW_SLOW: decode_failures 15

> slower: 4.25 s per simulated hour against 2.03 over 24 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| temporal | 1 | 0.453 | 0.440 | 0.013 | - | - | 0.614 | 0.803 | 0.189 | 1.21x | 11.5/16.6/19.7% | 1.9/4.3% | 3 |
| transient | 1 | 0.634 | 0.608 | 0.026 | - | - | 0.808 | 0.889 | 0.388 | 1.20x | 11.7/17.0/20.3% | 1.8/4.5% | 3 |
| periodic | 1 | 0.470 | 0.455 | 0.015 | - | - | 0.610 | 0.719 | 0.236 | 1.10x | 10.8/15.8/18.6% | 1.8/3.8% | 3 |

> noise-profile=none: decode_failures 33

> noise-profile=temporal: decode_failures 10

> noise-profile=transient: decode_failures 36

> noise-profile=periodic: decode_failures 11

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.114 | 0.114 | 0.000 | - | - | 0.056 | 0.169 | 0.000 | 0.07x | 0.4/0.7/0.9% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| LONG_MODERATE | 1 | 0.700 | 0.676 | 0.025 | - | - | 0.858 | 0.888 | 0.475 | 3.18x | 37.1/47.5/54.7% | 4.9/11.4% | 3 |

> preset=LONG_FAST: decode_failures 33

> preset=LONG_MODERATE: decode_failures 5

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.031 | 0.031 | 0.000 | - | - | 0.000 | 0.000 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.070 | 0.070 | 0.000 | - | - | 0.044 | 0.131 | 0.000 | 0.03x | 0.1/0.2/0.5% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| LONG_TURBO | 1 | 0.481 | 0.470 | 0.010 | - | - | 0.485 | 0.492 | 0.182 | 1.22x | 10.6/13.5/16.1% | 2.0/4.1% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.625 | 0.600 | 0.025 | - | - | 0.807 | 0.884 | 0.361 | 1.66x | 15.7/21.4/26.7% | 2.6/6.1% | 3 |

> preset=LONG_FAST: decode_failures 33

> preset=EXTRA_LONG_TURBO: decode_failures 38

> slower: 5.04 s per simulated hour against 1.56 over 20 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.589 | 0.570 | 0.020 | - | - | 0.740 | 0.853 | 0.334 | 1.17x | 11.7/17.0/20.1% | 1.8/4.3% | 3 |
| 10000 | 1 | 0.470 | 0.455 | 0.015 | - | - | 0.610 | 0.719 | 0.236 | 1.10x | 10.8/15.8/18.6% | 1.8/3.8% | 3 |
| 4000 | 1 | 0.239 | 0.237 | 0.003 | - | - | 0.291 | 0.413 | 0.094 | 0.97x | 9.6/13.9/16.4% | 1.5/2.9% | 3 |
| 2000 | 1 | 0.064 | 0.064 | 0.000 | - | - | 0.076 | 0.144 | 0.024 | 0.68x | 7.0/10.0/12.7% | 1.1/1.8% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 23

> noise-pulse-interval-ms=10000: decode_failures 11

> noise-pulse-interval-ms=4000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.144 | 0.143 | 0.001 | - | - | 0.216 | 0.237 | 0.000 | 0.93x | 4.8/9.3/10.8% | 1.5/3.2% | 3 |
| 1.0 | 1 | 0.503 | 0.498 | 0.006 | - | - | 0.561 | 0.563 | 0.392 | 0.83x | 12.4/14.3/16.6% | 1.2/3.5% | 3 |

> duct-per-hour=0.0: decode_failures 5

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 22 | 1 | 0.152 | 0.151 | 0.001 | - | - | 0.199 | 0.231 | 0.000 | 0.95x | 5.1/9.3/10.6% | 1.5/3.2% | 3 |
| 17 | 1 | 0.071 | 0.071 | 0.000 | - | - | 0.039 | 0.117 | 0.000 | 0.56x | 2.2/4.6/8.4% | 0.8/2.4% | 3 |
| 14 | 1 | 0.047 | 0.047 | 0.000 | - | - | 0.089 | 0.137 | 0.000 | 0.44x | 1.5/3.5/5.1% | 0.6/1.7% | 3 |

> tx-power=30: decode_failures 33

> tx-power=22: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.899 | 0.889 | 0.011 | - | - | 0.987 | 0.987 | 0.649 | 1.93x | 18.1/24.7/28.7% | 1.3/5.1% | 3 |
| True | 1 | 0.883 | 0.871 | 0.012 | - | - | 0.980 | 0.983 | 0.631 | 2.28x | 20.8/27.8/31.9% | 1.6/5.7% | 3 |

> no-adopt-hop-recommendation=True: decode_failures 1

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.638 | 0.613 | 0.025 | - | - | 0.821 | 0.888 | 0.361 | 1.26x | 13.1/18.2/20.6% | 2.0/4.5% | 3 |
| True | 1 | 0.660 | 0.639 | 0.021 | - | - | 0.816 | 0.899 | 0.422 | 1.29x | 13.3/18.7/21.2% | 2.0/4.6% | 3 |

> favourite-routers=False: decode_failures 33

> favourite-routers=True: decode_failures 36

> slower: 7.61 s per simulated hour against 1.68 over 24 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| random | 1 | 0.620 | 0.596 | 0.025 | - | - | 0.791 | 0.881 | 0.383 | 1.16x | 11.5/16.8/20.3% | 1.7/4.4% | 3 |

> hop-assign=centrality: decode_failures 33

> hop-assign=random: decode_failures 32

> slower: 10.1 s per simulated hour against 1.81 over 24 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.446 | 0.413 | 0.033 | - | - | 0.579 | 0.733 | 0.280 | 1.08x | 11.1/15.5/18.2% | 1.7/4.3% | 3 |
| 7 | 1 | 0.712 | 0.695 | 0.017 | - | - | 0.836 | 0.876 | 0.494 | 1.31x | 13.2/18.4/21.5% | 2.2/4.7% | 3 |
| 15 | 1 | 0.782 | 0.768 | 0.015 | - | - | 0.899 | 0.900 | 0.571 | 1.35x | 13.7/18.9/22.0% | 2.3/4.8% | 3 |
| 32 | 1 | 0.780 | 0.769 | 0.011 | - | - | 0.882 | 0.890 | 0.555 | 1.37x | 13.9/19.0/22.2% | 2.3/4.9% | 3 |

> hop-limit=3: decode_failures 21

> hop-limit=7: decode_failures 16

> slower: 4.26 s per simulated hour against 1.79 over 24 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.446 | 0.413 | 0.033 | - | - | 0.579 | 0.733 | 0.280 | 1.08x | 11.1/15.5/18.2% | 1.7/4.3% | 3 |
| 5 | 1 | 0.628 | 0.603 | 0.025 | - | - | 0.785 | 0.882 | 0.411 | 1.16x | 11.6/16.4/20.0% | 1.8/4.4% | 3 |
| 7 | 1 | 0.712 | 0.695 | 0.017 | - | - | 0.836 | 0.876 | 0.494 | 1.31x | 13.2/18.4/21.5% | 2.2/4.7% | 3 |

> hop-limit=3: decode_failures 21

> hop-limit=5: decode_failures 23

> hop-limit=7: decode_failures 16

> slower: 5.06 s per simulated hour against 2.03 over 24 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| KNOWN_ONLY | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.621 | 0.621 | 0.000 | - | - | 0.674 | 0.897 | 0.418 | 1.19x | 11.7/16.6/20.1% | 1.8/4.4% | 3 |

> rebroadcast-mode=ALL: decode_failures 33

> rebroadcast-mode=KNOWN_ONLY: decode_failures 33

> slower: 7.12 s per simulated hour against 1.59 over 24 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.446 | 0.413 | 0.033 | - | - | 0.579 | 0.733 | 0.280 | 1.08x | 11.1/15.5/18.2% | 1.7/4.3% | 3 |
| True | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> hop-spread=False: decode_failures 21

> hop-spread=True: decode_failures 33

> slower: 8.81 s per simulated hour against 2.11 over 24 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| BALANCED | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| STRICT | 1 | 0.494 | 0.494 | 0.000 | - | - | 0.650 | 0.754 | 0.290 | 1.31x | 12.9/18.3/21.7% | 2.1/4.7% | 3 |

> signature-policy=COMPATIBLE: decode_failures 33

> signature-policy=BALANCED: decode_failures 33

> signature-policy=STRICT: decode_failures 26

> slower: 7.04 s per simulated hour against 1.85 over 24 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| dm | 1 | 0.655 | 0.623 | 0.033 | - | - | 0.898 | 0.898 | 0.419 | 1.19x | 11.6/17.3/20.5% | 1.8/4.7% | 3 |

> advert-transport=broadcast: decode_failures 33

> advert-transport=dm: decode_failures 5

> slower: 7.94 s per simulated hour against 1.81 over 24 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.638 | 0.618 | 0.020 | - | - | 0.813 | 0.896 | 0.413 | 1.21x | 11.7/17.2/20.5% | 1.9/4.6% | 3 |
| local | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| time | 1 | 0.638 | 0.610 | 0.028 | - | - | 0.860 | 0.899 | 0.400 | 1.25x | 12.3/18.2/21.3% | 1.9/4.8% | 3 |
| window | 1 | 0.628 | 0.607 | 0.020 | - | - | 0.807 | 0.895 | 0.374 | 1.21x | 11.8/17.2/20.6% | 1.9/4.6% | 3 |

> bucket-mode=global: misdecodes 17

> bucket-mode=local: decode_failures 33

> bucket-mode=time: misdecodes 9

> bucket-mode=time: decode_failures 8

> bucket-mode=window: misdecodes 9

> bucket-mode=window: decode_failures 15

> slower: 5.39 s per simulated hour against 1.61 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.628 | 0.603 | 0.026 | - | - | 0.832 | 0.885 | 0.392 | 1.31x | 12.7/19.5/22.6% | 2.0/5.3% | 3 |
| 1800 | 1 | 0.638 | 0.610 | 0.028 | - | - | 0.860 | 0.899 | 0.400 | 1.25x | 12.3/18.2/21.3% | 1.9/4.8% | 3 |
| 3600 | 1 | 0.641 | 0.619 | 0.022 | - | - | 0.825 | 0.897 | 0.399 | 1.21x | 11.7/17.3/20.7% | 1.9/4.6% | 3 |

> time-bucket-s=600: misdecodes 69

> time-bucket-s=1800: misdecodes 9

> time-bucket-s=1800: decode_failures 8

> time-bucket-s=3600: misdecodes 6

> time-bucket-s=3600: decode_failures 14

> slower: 3.72 s per simulated hour against 1.67 over 24 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| interval | 1 | 0.612 | 0.584 | 0.029 | - | - | 0.829 | 0.859 | 0.380 | 1.54x | 14.8/24.9/27.8% | 2.5/6.6% | 3 |
| aimd | 1 | 0.637 | 0.621 | 0.016 | - | - | 0.775 | 0.894 | 0.413 | 1.23x | 12.0/17.7/20.9% | 1.9/4.6% | 3 |
| bucket+interval | 1 | 0.627 | 0.588 | 0.039 | - | - | 0.867 | 0.873 | 0.415 | 1.56x | 15.0/25.2/28.4% | 2.5/6.7% | 3 |

> trigger=bucket: decode_failures 33

> trigger=interval: misdecodes 4

> trigger=interval: decode_failures 21

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 29

> trigger=bucket+interval: misdecodes 5

> trigger=bucket+interval: decode_failures 35

> slower: 11.2 s per simulated hour against 3.39 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.636 | 0.608 | 0.027 | - | - | 0.814 | 0.885 | 0.405 | 1.21x | 11.8/17.3/20.6% | 1.9/4.5% | 3 |
| 8 | 1 | 0.643 | 0.615 | 0.028 | - | - | 0.837 | 0.900 | 0.390 | 1.20x | 11.7/17.3/20.4% | 1.8/4.5% | 3 |
| 16 | 1 | 0.643 | 0.617 | 0.026 | - | - | 0.812 | 0.902 | 0.388 | 1.20x | 11.6/17.1/20.5% | 1.8/4.5% | 3 |
| 32 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 50 | 1 | 0.648 | 0.620 | 0.028 | - | - | 0.840 | 0.909 | 0.386 | 1.21x | 11.8/17.4/20.7% | 1.8/4.6% | 3 |

> capacity=4: decode_failures 56

> capacity=8: decode_failures 51

> capacity=16: decode_failures 40

> capacity=32: decode_failures 33

> capacity=50: decode_failures 30

> slower: 7.83 s per simulated hour against 1.7 over 24 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.636 | 0.608 | 0.027 | - | - | 0.814 | 0.885 | 0.405 | 1.21x | 11.8/17.3/20.6% | 1.9/4.5% | 3 |
| 8 | 1 | 0.643 | 0.615 | 0.028 | - | - | 0.837 | 0.900 | 0.390 | 1.20x | 11.7/17.3/20.4% | 1.8/4.5% | 3 |
| 16 | 1 | 0.643 | 0.617 | 0.026 | - | - | 0.812 | 0.902 | 0.388 | 1.20x | 11.6/17.1/20.5% | 1.8/4.5% | 3 |
| 32 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 50 | 1 | 0.648 | 0.620 | 0.028 | - | - | 0.840 | 0.909 | 0.386 | 1.21x | 11.8/17.4/20.7% | 1.8/4.6% | 3 |

> capacity=4: decode_failures 56

> capacity=8: decode_failures 51

> capacity=16: decode_failures 40

> capacity=32: decode_failures 33

> capacity=50: decode_failures 30

> slower: 7.76 s per simulated hour against 1.79 over 24 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.621 | 0.615 | 0.005 | - | - | 0.706 | 0.908 | 0.392 | 1.20x | 11.7/16.7/20.2% | 1.9/4.4% | 3 |
| 16 | 1 | 0.614 | 0.606 | 0.007 | - | - | 0.705 | 0.889 | 0.406 | 1.19x | 11.6/16.5/20.0% | 1.8/4.4% | 3 |
| 32 | 1 | 0.628 | 0.607 | 0.020 | - | - | 0.807 | 0.895 | 0.374 | 1.21x | 11.8/17.2/20.6% | 1.9/4.6% | 3 |

> capacity=8: misdecodes 6

> capacity=8: decode_failures 58

> capacity=16: misdecodes 2

> capacity=16: decode_failures 38

> capacity=32: misdecodes 9

> capacity=32: decode_failures 15

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.627 | 0.588 | 0.039 | - | - | 0.867 | 0.873 | 0.415 | 1.56x | 15.0/25.2/28.4% | 2.5/6.7% | 3 |
| 02-06 | 1 | 0.636 | 0.618 | 0.018 | - | - | 0.784 | 0.906 | 0.392 | 1.25x | 12.3/18.2/21.3% | 1.9/4.8% | 3 |
| 00-08 | 1 | 0.640 | 0.621 | 0.019 | - | - | 0.805 | 0.906 | 0.396 | 1.30x | 12.9/19.3/22.4% | 2.0/5.1% | 3 |

> catch-up-hours=: misdecodes 5

> catch-up-hours=: decode_failures 35

> catch-up-hours=02-06: decode_failures 42

> catch-up-hours=00-08: decode_failures 47

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.623 | 0.619 | 0.004 | - | - | 0.774 | 0.776 | 0.392 | 1.19x | 11.8/16.7/20.3% | 1.9/4.5% | 3 |
| 2 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 3 | 1 | 0.624 | 0.611 | 0.013 | - | - | 0.670 | 0.960 | 0.430 | 1.20x | 11.7/16.6/20.1% | 1.8/4.4% | 3 |
| 4 | 1 | 0.624 | 0.613 | 0.011 | - | - | 0.615 | 0.959 | 0.396 | 1.19x | 11.7/16.3/19.9% | 1.9/4.3% | 3 |

> hops-apart=2: decode_failures 33

> hops-apart=3: decode_failures 20

> hops-apart=4: decode_failures 18

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.623 | 0.619 | 0.004 | - | - | 0.774 | 0.776 | 0.392 | 1.19x | 11.8/16.7/20.3% | 1.9/4.5% | 3 |
| 2 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 3 | 1 | 0.624 | 0.611 | 0.013 | - | - | 0.670 | 0.960 | 0.430 | 1.20x | 11.7/16.6/20.1% | 1.8/4.4% | 3 |
| 4 | 1 | 0.624 | 0.613 | 0.011 | - | - | 0.615 | 0.959 | 0.396 | 1.19x | 11.7/16.3/19.9% | 1.9/4.3% | 3 |
| 5 | 1 | 0.636 | 0.608 | 0.029 | - | - | 0.671 | 0.959 | 0.415 | 1.20x | 11.8/16.6/20.1% | 1.8/4.3% | 3 |

> hops-apart=2: decode_failures 33

> hops-apart=3: decode_failures 20

> hops-apart=4: decode_failures 18

> hops-apart=5: decode_failures 22

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.640 | 0.619 | 0.022 | - | - | 0.811 | 0.914 | 0.406 | 1.21x | 11.8/17.3/20.6% | 1.8/4.6% | 3 |
| 30 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 120 | 1 | 0.647 | 0.620 | 0.026 | - | - | 0.831 | 0.909 | 0.406 | 1.21x | 11.8/17.4/20.6% | 1.9/4.6% | 3 |
| 600 | 1 | 0.637 | 0.611 | 0.026 | - | - | 0.796 | 0.880 | 0.407 | 1.21x | 11.8/17.2/20.6% | 1.8/4.5% | 3 |

> advert-jitter-s=1: decode_failures 34

> advert-jitter-s=30: decode_failures 33

> advert-jitter-s=120: decode_failures 39

> advert-jitter-s=600: decode_failures 38

> slower: 9.06 s per simulated hour against 1.78 over 24 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.640 | 0.619 | 0.022 | - | - | 0.811 | 0.914 | 0.406 | 1.21x | 11.8/17.3/20.6% | 1.8/4.6% | 3 |
| 30 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 120 | 1 | 0.647 | 0.620 | 0.026 | - | - | 0.831 | 0.909 | 0.406 | 1.21x | 11.8/17.4/20.6% | 1.9/4.6% | 3 |
| 600 | 1 | 0.637 | 0.611 | 0.026 | - | - | 0.796 | 0.880 | 0.407 | 1.21x | 11.8/17.2/20.6% | 1.8/4.5% | 3 |

> advert-jitter-s=1: decode_failures 34

> advert-jitter-s=30: decode_failures 33

> advert-jitter-s=120: decode_failures 39

> advert-jitter-s=600: decode_failures 38

> slower: 11.2 s per simulated hour against 1.84 over 24 prior run(s) - 6.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.647 | 0.629 | 0.018 | - | - | 0.575 | 0.793 | 0.396 | 1.21x | 12.1/16.7/20.3% | 1.9/4.5% | 3 |
| routers | 1 | 0.625 | 0.616 | 0.009 | - | - | 0.681 | 0.938 | 0.383 | 1.19x | 11.6/16.6/20.0% | 1.8/4.3% | 3 |
| alternate-routers | 1 | 0.626 | 0.622 | 0.004 | - | - | 0.740 | 0.950 | 0.387 | 1.19x | 11.5/16.6/20.0% | 1.8/4.4% | 3 |
| beside-router | 1 | 0.622 | 0.620 | 0.002 | - | - | 0.665 | 0.940 | 0.396 | 1.19x | 11.6/16.5/20.1% | 1.8/4.4% | 3 |
| random-clients | 1 | 0.642 | 0.615 | 0.028 | - | - | 0.802 | 0.905 | 0.411 | 1.22x | 11.9/17.4/20.8% | 1.9/4.6% | 3 |
| hops-apart | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> place=spread: decode_failures 28

> place=routers: decode_failures 2

> place=alternate-routers: decode_failures 5

> place=beside-router: decode_failures 3

> place=random-clients: decode_failures 35

> place=hops-apart: decode_failures 33

> slower: 6.03 s per simulated hour against 3.01 over 24 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.647 | 0.629 | 0.018 | - | - | 0.575 | 0.793 | 0.396 | 1.21x | 12.1/16.7/20.3% | 1.9/4.5% | 3 |
| routers | 1 | 0.625 | 0.616 | 0.009 | - | - | 0.681 | 0.938 | 0.383 | 1.19x | 11.6/16.6/20.0% | 1.8/4.3% | 3 |
| alternate-routers | 1 | 0.626 | 0.622 | 0.004 | - | - | 0.740 | 0.950 | 0.387 | 1.19x | 11.5/16.6/20.0% | 1.8/4.4% | 3 |
| beside-router | 1 | 0.622 | 0.620 | 0.002 | - | - | 0.665 | 0.940 | 0.396 | 1.19x | 11.6/16.5/20.1% | 1.8/4.4% | 3 |
| random-clients | 1 | 0.642 | 0.615 | 0.028 | - | - | 0.802 | 0.905 | 0.411 | 1.22x | 11.9/17.4/20.8% | 1.9/4.6% | 3 |
| hops-apart | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> place=spread: decode_failures 28

> place=routers: decode_failures 2

> place=alternate-routers: decode_failures 5

> place=beside-router: decode_failures 3

> place=random-clients: decode_failures 35

> place=hops-apart: decode_failures 33

> slower: 6.06 s per simulated hour against 2.92 over 24 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| broadcast | 1 | 0.686 | 0.617 | 0.069 | - | - | 0.777 | 0.890 | 0.439 | 1.29x | 12.6/18.6/21.9% | 2.0/4.9% | 3 |

> provide-transport=dm: decode_failures 33

> provide-transport=broadcast: decode_failures 34

> slower: 8.77 s per simulated hour against 1.86 over 24 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| heard | 1 | 0.646 | 0.624 | 0.023 | - | - | 0.809 | 0.900 | 0.415 | 1.22x | 11.9/17.3/20.8% | 1.9/4.6% | 3 |

> replay-ordering=tip: decode_failures 33

> replay-ordering=heard: misdecodes 4

> replay-ordering=heard: decode_failures 31

> slower: 10.1 s per simulated hour against 1.68 over 24 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.686 | 0.617 | 0.069 | - | - | 0.777 | 0.890 | 0.439 | 1.29x | 12.6/18.6/21.9% | 2.0/4.9% | 3 |
| heard | 1 | 0.671 | 0.611 | 0.060 | - | - | 0.755 | 0.890 | 0.441 | 1.29x | 12.6/18.8/22.0% | 2.0/5.0% | 3 |

> replay-ordering=tip: decode_failures 34

> replay-ordering=heard: misdecodes 1

> replay-ordering=heard: decode_failures 22

> slower: 8.77 s per simulated hour against 1.83 over 24 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.641 | 0.628 | 0.013 | - | - | 0.745 | 0.903 | 0.423 | 1.20x | 11.7/16.9/20.3% | 1.8/4.5% | 3 |
| enum | 1 | 0.646 | 0.619 | 0.027 | - | - | 0.810 | 0.902 | 0.382 | 1.19x | 11.5/17.1/20.1% | 1.8/4.6% | 3 |
| hybrid | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> resolve=sketch: decode_failures 29

> resolve=hybrid: decode_failures 33

> slower: 6.96 s per simulated hour against 1.54 over 24 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.625 | 0.616 | 0.009 | - | - | 0.681 | 0.938 | 0.383 | 1.19x | 11.6/16.6/20.0% | 1.8/4.3% | 3 |
| 6 | 1 | 0.695 | 0.621 | 0.074 | - | - | 0.856 | 0.976 | 0.430 | 1.24x | 12.2/17.3/20.8% | 1.9/4.6% | 6 |

> servers=3: decode_failures 2

> servers=6: decode_failures 37

> slower: 7.28 s per simulated hour against 1.84 over 24 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.638 | 0.631 | 0.008 | - | - | 0.814 | 0.815 | 0.417 | 1.19x | 11.7/16.7/20.1% | 1.8/4.5% | 2 |
| 3 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 5 | 1 | 0.654 | 0.619 | 0.034 | - | - | 0.910 | 0.924 | 0.425 | 1.23x | 11.9/17.9/21.3% | 1.9/4.7% | 5 |
| 8 | 1 | 0.669 | 0.608 | 0.061 | - | - | 0.944 | 0.960 | 0.407 | 1.27x | 12.5/18.7/22.5% | 2.0/4.8% | 8 |

> servers=3: decode_failures 33

> servers=5: decode_failures 2

> servers=8: decode_failures 16

> slower: 8.35 s per simulated hour against 2.55 over 24 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.638 | 0.631 | 0.008 | - | - | 0.814 | 0.815 | 0.417 | 1.19x | 11.7/16.7/20.1% | 1.8/4.5% | 2 |
| 3 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 5 | 1 | 0.654 | 0.619 | 0.034 | - | - | 0.910 | 0.924 | 0.425 | 1.23x | 11.9/17.9/21.3% | 1.9/4.7% | 5 |
| 8 | 1 | 0.669 | 0.608 | 0.061 | - | - | 0.944 | 0.960 | 0.407 | 1.27x | 12.5/18.7/22.5% | 2.0/4.8% | 8 |

> servers=3: decode_failures 33

> servers=5: decode_failures 2

> servers=8: decode_failures 16

> slower: 8.49 s per simulated hour against 2.27 over 24 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| True | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |

> signed=False: decode_failures 33

> signed=True: decode_failures 33

> slower: 10.1 s per simulated hour against 1.74 over 24 prior run(s) - 5.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.646 | 0.622 | 0.024 | - | - | 0.794 | 0.916 | 0.403 | 1.14x | 11.3/15.9/19.1% | 1.8/4.2% | 3 |
| 1 | 1 | 0.644 | 0.622 | 0.022 | - | - | 0.804 | 0.913 | 0.416 | 1.15x | 11.3/16.4/19.3% | 1.8/4.2% | 3 |
| 2 | 1 | 0.640 | 0.619 | 0.021 | - | - | 0.797 | 0.921 | 0.393 | 1.14x | 11.1/15.8/19.1% | 1.8/4.1% | 3 |
| 4 | 1 | 0.643 | 0.621 | 0.022 | - | - | 0.828 | 0.924 | 0.389 | 1.14x | 11.2/16.1/19.2% | 1.8/4.2% | 3 |

> sr-retries=0: decode_failures 22

> sr-retries=1: decode_failures 16

> sr-retries=2: decode_failures 17

> sr-retries=4: decode_failures 16

> slower: 8.45 s per simulated hour against 1.61 over 24 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.640 | 0.616 | 0.025 | - | - | 0.798 | 0.907 | 0.370 | 1.21x | 11.8/17.2/20.6% | 1.9/4.6% | 3 |
| 24 | 1 | 0.633 | 0.614 | 0.019 | - | - | 0.783 | 0.896 | 0.380 | 1.21x | 11.7/17.1/20.6% | 1.9/4.5% | 3 |
| 32 | 1 | 0.641 | 0.617 | 0.024 | - | - | 0.815 | 0.891 | 0.406 | 1.20x | 11.7/17.3/20.4% | 1.9/4.5% | 3 |
| 64 | 1 | 0.640 | 0.617 | 0.023 | - | - | 0.814 | 0.894 | 0.400 | 1.23x | 12.0/17.6/20.9% | 1.9/4.6% | 3 |

> short-id-bits=16: decode_failures 31

> short-id-bits=24: decode_failures 32

> short-id-bits=32: decode_failures 33

> short-id-bits=64: decode_failures 32

> slower: 9.95 s per simulated hour against 1.74 over 24 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.643 | 0.613 | 0.030 | - | - | 0.861 | 0.900 | 0.380 | 1.26x | 12.3/18.4/21.5% | 1.9/4.9% | 3 |
| 16 | 1 | 0.641 | 0.612 | 0.029 | - | - | 0.846 | 0.895 | 0.397 | 1.22x | 11.9/17.6/20.9% | 1.8/4.6% | 3 |
| 32 | 1 | 0.628 | 0.607 | 0.020 | - | - | 0.807 | 0.895 | 0.374 | 1.21x | 11.8/17.2/20.6% | 1.9/4.6% | 3 |

> window-size=8: misdecodes 67

> window-size=16: misdecodes 18

> window-size=32: misdecodes 9

> window-size=32: decode_failures 15

> slower: 3.14 s per simulated hour against 1.43 over 24 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.899 | 0.889 | 0.011 | - | - | 0.987 | 0.987 | 0.649 | 1.93x | 18.1/24.7/28.7% | 1.3/5.1% | 3 |
| True | 1 | 0.687 | 0.660 | 0.027 | - | - | 0.859 | 0.872 | 0.437 | 5.52x | 49.0/62.3/67.6% | 3.7/12.1% | 3 |

> no-congestion-scaling=True: decode_failures 23

> faster: 9.12 s per simulated hour against 18.6 over 24 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.309 | 0.305 | 0.004 | - | - | 0.481 | 0.483 | 0.124 | 4.71x | 12.2/19.6/26.7% | 1.7/4.7% | 3 |
| truesize | 1 | 0.343 | 0.339 | 0.004 | - | - | 0.511 | 0.512 | 0.139 | 2.58x | 6.7/12.3/16.0% | 0.8/2.9% | 3 |

> congestion-input=hotstore: decode_failures 1

> congestion-input=truesize: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.894 | 0.885 | 0.010 | - | - | 0.985 | 0.987 | 0.658 | 1.81x | 16.9/22.9/26.6% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.899 | 0.889 | 0.011 | - | - | 0.987 | 0.987 | 0.649 | 1.93x | 18.1/24.7/28.7% | 1.3/5.1% | 3 |

