# Sweep blocks-2026-10-31-7782257

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 7782257 · seeds 7782257
- **blocks** 87 run
- **compute** 18.3 h of simulator time across every cell
- **generated** 2026-10-31T10:02:03+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>284 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 20
- AD-amplifiers: amplifier-mix=sprinkled: decode_failures 6
- AD-amplifiers: slower: 4.76 s per simulated hour against 1.57 over 71 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-amplify-worst: amplify-worst=0.0: decode_failures 20
- AD-amplify-worst: amplify-worst=0.3: decode_failures 1
- AD-badrouters: role-placement=degree: decode_failures 41
- AD-badrouters: role-placement=inverse: decode_failures 31
- AD-badrouters: role-placement=random: decode_failures 30
- AD-badrouters: slower: 10.8 s per simulated hour against 1.79 over 71 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 41
- AD-flooding: slower: 8.14 s per simulated hour against 2.42 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 41
- AD-nomute: role-mix=no-mute: decode_failures 21
- AD-nomute: slower: 8.17 s per simulated hour against 2.21 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 41
- AD-siting: slower: 4.56 s per simulated hour against 1.45 over 71 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=inverse: decode_failures 1
- BL-control: protocol=sr: decode_failures 28
- BL-control: slower: 5.38 s per simulated hour against 1.81 over 71 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 22
- DB-hotstore: max-num-nodes=100: decode_failures 25
- DB-hotstore: max-num-nodes=120: decode_failures 25
- DB-hotstore: max-num-nodes=250: decode_failures 25
- DB-hotstore: slower: 8.48 s per simulated hour against 2.3 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 32
- DB-hotstore-stress: max-num-nodes=120: decode_failures 1
- DB-hotstore-stress: max-num-nodes=250: decode_failures 4
- DB-platform: platform-mix=uniform: decode_failures 25
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 25
- DB-platform: platform-mix=constrained: decode_failures 23
- DB-platform: slower: 7.96 s per simulated hour against 2.4 over 71 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: decode_failures 55
- DB-warm: warm-num-nodes=25: decode_failures 55
- DB-warm: warm-num-nodes=100: decode_failures 55
- DB-warm: warm-num-nodes=2000: decode_failures 55
- DB-warm: faster: 15.7 s per simulated hour against 34.3 over 71 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DG-burst: burst-loss=0.0: decode_failures 20
- DG-burst: burst-loss=0.1: decode_failures 43
- DG-burst: burst-loss=0.2: decode_failures 29
- DG-burst: burst-loss=0.3: decode_failures 20
- DG-loss: extra-loss=0.0: decode_failures 20
- DG-loss: extra-loss=0.1: decode_failures 25
- DG-loss: extra-loss=0.2: decode_failures 37
- DG-loss: extra-loss=0.3: decode_failures 30
- DG-loss: slower: 9.76 s per simulated hour against 2.22 over 71 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 20
- DG-outage: burst-loss=0.1: decode_failures 36
- DG-outage: burst-loss=0.2: decode_failures 23
- DG-outage: burst-loss=0.3: decode_failures 19
- DM-mode: dm-mode=flood-only: decode_failures 30
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 24
- DM-mode: dm-mode=m4-early-flood: decode_failures 26
- DM-mode: slower: 5.75 s per simulated hour against 2.71 over 71 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 20
- FW-firmware: slower: 5.33 s per simulated hour against 1.62 over 71 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.0: decode_failures 20
- FW-mixed-26: slower: 3.57 s per simulated hour against 1.69 over 71 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.0: decode_failures 20
- FW-signing-cost: profile-flag=signing=false: decode_failures 29
- FW-signing-cost: profile-flag=signing=true: decode_failures 20
- FW-signing-cost: slower: 9.51 s per simulated hour against 1.52 over 71 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-versions: profile=2.8: decode_failures 20
- FW-versions: slower: 3.17 s per simulated hour against 1.52 over 71 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 20
- LD-chatty: broadcast-interval-s=3600: decode_failures 15
- LD-chatty: broadcast-interval-s=900: decode_failures 37
- LD-chatty: broadcast-interval-s=300: decode_failures 19
- LD-diurnal: diurnal=flat: decode_failures 27
- LD-diurnal: diurnal=sinusoid: decode_failures 18
- LD-diurnal: diurnal=commuter: decode_failures 20
- LD-diurnal: slower: 5.06 s per simulated hour against 1.49 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 37
- LD-interval: broadcast-interval-s=3600: decode_failures 15
- LD-interval: broadcast-interval-s=10800: decode_failures 21
- LD-interval: broadcast-interval-s=43200: decode_failures 32
- LD-interval: slower: 8.11 s per simulated hour against 1.27 over 71 prior run(s) - 6.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 20
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 31
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 35
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 36
- LD-traceroute: slower: 11.1 s per simulated hour against 2.1 over 71 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 55
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 63
- MS-density: nodes=40: decode_failures 5
- MS-density: nodes=60: decode_failures 20
- MS-hopscale: nodes=60: decode_failures 20
- MS-hopscale: nodes=120: decode_failures 65
- MS-hopscale: nodes=250: decode_failures 6
- MS-hopscale: nodes=500: decode_failures 117
- MS-oversubscribed: nodes=120: decode_failures 23
- MS-oversubscribed: nodes=250: decode_failures 1
- MS-oversubscribed: nodes=500: decode_failures 42
- MS-roles-fav: role-mix=legacy-default: decode_failures 15
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 7
- MS-roles-fav: slower: 4.47 s per simulated hour against 1.7 over 71 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-roles: role-mix=legacy-default: decode_failures 26
- MS-roles: role-mix=baymesh-2026-08: decode_failures 41
- MS-roles: slower: 8.85 s per simulated hour against 1.68 over 71 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 20
- MS-router-late: router-late-fraction=0.05: decode_failures 29
- MS-router-late: router-late-fraction=0.1: decode_failures 23
- MS-router-late: router-late-fraction=0.2: decode_failures 4
- MS-router-late: slower: 8.32 s per simulated hour against 1.73 over 71 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=uniform: decode_failures 20
- MS-siting: siting-mix=event: 3 archives requested, 2 placed - group on the placed count
- MS-size: nodes=60: decode_failures 20
- MS-size: nodes=90: decode_failures 27
- MS-size: nodes=120: decode_failures 65
- MS-size: nodes=150: decode_failures 94
- MS-size: slower: 14.7 s per simulated hour against 3.42 over 71 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.0: decode_failures 20
- MS-stretch: stretch=1.25: decode_failures 24
- MS-stretch: stretch=1.5: decode_failures 14
- MS-stretch: stretch=2.0: decode_failures 1
- MS-stretch: slower: 4.4 s per simulated hour against 2.04 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-topology: topology=uniform: decode_failures 20
- MS-topology: topology=corridor: decode_failures 1
- PR-crladder: coding-rate-ladder=False: decode_failures 24
- PR-crladder: coding-rate-ladder=True: decode_failures 30
- PR-crladder: slower: 8.63 s per simulated hour against 2.79 over 71 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: inert: every value of `dm-mode` produced identical numbers - either the flag is not read, or it needs a second flag before it does anything (README §10.4)
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 30
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 30
- PR-dmmode-cr: slower: 10.6 s per simulated hour against 2.6 over 71 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 20
- PR-repeats: extra-repeats=False: decode_failures 20
- PR-repeats: extra-repeats=True: decode_failures 22
- PR-repeats: slower: 8.67 s per simulated hour against 1.58 over 71 prior run(s) - 5.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 1
- RF-bw500: preset=LONG_TURBO: decode_failures 28
- RF-bw500: slower: 4.15 s per simulated hour against 1.9 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-duct: duct-per-hour=0.0: decode_failures 20
- RF-duct: duct-per-hour=0.25: decode_failures 19
- RF-duct: slower: 5.67 s per simulated hour against 1.73 over 71 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=SHORT_FAST: decode_failures 5
- RF-eu-presets: preset=LONG_FAST: decode_failures 20
- RF-eu-presets: preset=LITE_FAST: decode_failures 33
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 33
- RF-eu-presets: slower: 6.61 s per simulated hour against 1.8 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-noise: noise-profile=none: decode_failures 20
- RF-noise: noise-profile=temporal: decode_failures 27
- RF-noise: noise-profile=transient: decode_failures 32
- RF-noise: noise-profile=periodic: decode_failures 20
- RF-noise: slower: 11.4 s per simulated hour against 4.92 over 71 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset: preset=SHORT_FAST: decode_failures 5
- RF-preset: preset=LONG_FAST: decode_failures 20
- RF-preset: preset=LONG_MODERATE: decode_failures 21
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 5
- RF-preset-turbo: preset=LONG_FAST: decode_failures 20
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 28
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 30
- RF-preset-turbo: slower: 3.87 s per simulated hour against 1.48 over 67 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 28
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 20
- RF-pulse: slower: 4 s per simulated hour against 1.6 over 71 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 14
- RF-txpower: tx-power=30: decode_failures 20
- RF-txpower: tx-power=22: decode_failures 11
- RF-txpower: tx-power=14: decode_failures 1
- RF-txpower: slower: 3.5 s per simulated hour against 1.58 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-favourites: favourite-routers=False: decode_failures 30
- RT-favourites: favourite-routers=True: decode_failures 6
- RT-favourites: slower: 6.66 s per simulated hour against 1.63 over 71 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 20
- RT-hopassign: slower: 5.96 s per simulated hour against 1.74 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hoplimit: hop-limit=3: decode_failures 22
- RT-hopspread: hop-limit=3: decode_failures 22
- RT-hopspread: slower: 4.08 s per simulated hour against 2.03 over 71 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 20
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 20
- RT-rebroadcast: slower: 5.88 s per simulated hour against 1.55 over 71 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-spread: hop-spread=False: decode_failures 22
- RT-spread: hop-spread=True: decode_failures 20
- RT-spread: slower: 7.98 s per simulated hour against 2.16 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 20
- SC-signing: signature-policy=BALANCED: decode_failures 20
- SC-signing: signature-policy=STRICT: decode_failures 23
- SC-signing: slower: 8.38 s per simulated hour against 1.7 over 71 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 20
- SF-advert-transport: advert-transport=dm: decode_failures 13
- SF-advert-transport: slower: 8.22 s per simulated hour against 1.68 over 71 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 3
- SF-bucket-mode: bucket-mode=local: decode_failures 20
- SF-bucket-mode: bucket-mode=time: misdecodes 7
- SF-bucket-mode: bucket-mode=time: decode_failures 1
- SF-bucket-mode: bucket-mode=window: misdecodes 1
- SF-bucket-mode: bucket-mode=window: decode_failures 3
- SF-bucket-mode: slower: 4.15 s per simulated hour against 1.41 over 71 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-time: time-bucket-s=600: misdecodes 33
- SF-bucket-time: time-bucket-s=1800: misdecodes 7
- SF-bucket-time: time-bucket-s=1800: decode_failures 1
- SF-bucket-time: time-bucket-s=3600: decode_failures 18
- SF-bucket-time: slower: 3.56 s per simulated hour against 1.6 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-cadence: trigger=bucket: decode_failures 20
- SF-cadence: trigger=interval: misdecodes 7
- SF-cadence: trigger=interval: decode_failures 13
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 11
- SF-cadence: trigger=bucket+interval: misdecodes 2
- SF-cadence: trigger=bucket+interval: decode_failures 16
- SF-cadence: slower: 8.45 s per simulated hour against 3.62 over 71 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 81
- SF-capacity-local: capacity=8: decode_failures 70
- SF-capacity-local: capacity=16: decode_failures 73
- SF-capacity-local: capacity=32: decode_failures 20
- SF-capacity-local: capacity=50: decode_failures 1
- SF-capacity-local: slower: 4.48 s per simulated hour against 1.72 over 71 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity: capacity=4: decode_failures 81
- SF-capacity: capacity=8: decode_failures 70
- SF-capacity: capacity=16: decode_failures 73
- SF-capacity: capacity=32: decode_failures 20
- SF-capacity: capacity=50: decode_failures 1
- SF-capacity-window: capacity=8: decode_failures 91
- SF-capacity-window: capacity=16: decode_failures 68
- SF-capacity-window: capacity=32: misdecodes 1
- SF-capacity-window: capacity=32: decode_failures 3
- SF-capacity-window: slower: 4.13 s per simulated hour against 1.59 over 71 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 2
- SF-catchup: catch-up-hours=: decode_failures 16
- SF-catchup: catch-up-hours=02-06: decode_failures 34
- SF-catchup: catch-up-hours=00-08: decode_failures 41
- SF-hops-flat: hops-apart=2: decode_failures 20
- SF-hops-flat: hops-apart=3: decode_failures 28
- SF-hops-flat: hops-apart=4: decode_failures 20
- SF-hops-spread: hops-apart=2: decode_failures 20
- SF-hops-spread: hops-apart=3: decode_failures 28
- SF-hops-spread: hops-apart=4: decode_failures 20
- SF-hops-spread: hops-apart=5: decode_failures 12
- SF-jitter-global: advert-jitter-s=1: decode_failures 27
- SF-jitter-global: advert-jitter-s=30: decode_failures 20
- SF-jitter-global: advert-jitter-s=120: decode_failures 31
- SF-jitter-global: advert-jitter-s=600: decode_failures 27
- SF-jitter-global: slower: 5.96 s per simulated hour against 1.75 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 27
- SF-jitter-local: advert-jitter-s=30: decode_failures 20
- SF-jitter-local: advert-jitter-s=120: decode_failures 31
- SF-jitter-local: advert-jitter-s=600: decode_failures 27
- SF-jitter-local: slower: 9.87 s per simulated hour against 1.76 over 71 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 25
- SF-place-flat: place=routers: decode_failures 4
- SF-place-flat: place=random-clients: decode_failures 27
- SF-place-flat: place=hops-apart: decode_failures 20
- SF-place-spread: place=spread: decode_failures 25
- SF-place-spread: place=routers: decode_failures 4
- SF-place-spread: place=random-clients: decode_failures 27
- SF-place-spread: place=hops-apart: decode_failures 20
- SF-provide-transport: provide-transport=dm: decode_failures 20
- SF-provide-transport: provide-transport=broadcast: decode_failures 42
- SF-provide-transport: slower: 11.2 s per simulated hour against 1.75 over 71 prior run(s) - 6.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 42
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 29
- SF-replay-order-broadcast: slower: 11.7 s per simulated hour against 1.63 over 71 prior run(s) - 7.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 20
- SF-replay-order: replay-ordering=heard: decode_failures 30
- SF-replay-order: slower: 9.27 s per simulated hour against 1.54 over 71 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-resolve: resolve=sketch: decode_failures 38
- SF-resolve: resolve=hybrid: decode_failures 20
- SF-resolve: slower: 7.47 s per simulated hour against 1.51 over 71 prior run(s) - 5.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-allrouters: servers=3: decode_failures 4
- SF-servers-flat: servers=2: decode_failures 20
- SF-servers-flat: servers=3: decode_failures 20
- SF-servers-flat: slower: 6.08 s per simulated hour against 2.27 over 71 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=2: decode_failures 20
- SF-servers-spread: servers=3: decode_failures 20
- SF-servers-spread: slower: 6.2 s per simulated hour against 2.17 over 71 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 20
- SF-signed: signed=True: decode_failures 20
- SF-signed: slower: 8.39 s per simulated hour against 1.62 over 71 prior run(s) - 5.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 21
- SF-sr-retries: sr-retries=1: decode_failures 5
- SF-sr-retries: sr-retries=2: decode_failures 13
- SF-sr-retries: sr-retries=4: decode_failures 14
- SF-sr-retries: slower: 6.11 s per simulated hour against 1.51 over 71 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 30
- SF-width: short-id-bits=24: decode_failures 24
- SF-width: short-id-bits=32: decode_failures 20
- SF-width: short-id-bits=64: decode_failures 29
- SF-width: slower: 5.96 s per simulated hour against 1.66 over 71 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 53
- SF-window-size: window-size=16: misdecodes 10
- SF-window-size: window-size=32: misdecodes 1
- SF-window-size: window-size=32: decode_failures 3
- TH-congestion-input: congestion-input=hotstore: decode_failures 1
- TH-congestion: no-congestion-scaling=True: decode_failures 63

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-replay-order-broadcast` | 11.7 | 1.63 | 7.14x | 71 |
| `SF-provide-transport` | 11.2 | 1.75 | 6.38x | 71 |
| `LD-interval` | 8.11 | 1.27 | 6.38x | 71 |
| `FW-signing-cost` | 9.51 | 1.52 | 6.26x | 71 |
| `AD-badrouters` | 10.8 | 1.79 | 6.04x | 71 |
| `SF-replay-order` | 9.27 | 1.54 | 6.02x | 71 |
| `SF-jitter-local` | 9.87 | 1.76 | 5.62x | 71 |
| `PR-repeats` | 8.67 | 1.58 | 5.50x | 71 |
| `LD-traceroute` | 11.1 | 2.1 | 5.30x | 71 |
| `MS-roles` | 8.85 | 1.68 | 5.28x | 71 |
| `SF-signed` | 8.39 | 1.62 | 5.19x | 71 |
| `SF-resolve` | 7.47 | 1.51 | 4.96x | 71 |
| `SC-signing` | 8.38 | 1.7 | 4.93x | 71 |
| `SF-advert-transport` | 8.22 | 1.68 | 4.89x | 71 |
| `MS-router-late` | 8.32 | 1.73 | 4.82x | 71 |
| `DG-loss` | 9.76 | 2.22 | 4.39x | 71 |
| `MS-size` | 14.7 | 3.42 | 4.30x | 71 |
| `RT-favourites` | 6.66 | 1.63 | 4.08x | 71 |
| `PR-dmmode-cr` | 10.6 | 2.6 | 4.08x | 71 |
| `SF-sr-retries` | 6.11 | 1.51 | 4.05x | 71 |
| `RT-rebroadcast` | 5.88 | 1.55 | 3.78x | 71 |
| `RT-spread` | 7.98 | 2.16 | 3.69x | 71 |
| `AD-nomute` | 8.17 | 2.21 | 3.69x | 71 |
| `DB-hotstore` | 8.48 | 2.3 | 3.68x | 71 |
| `RF-eu-presets` | 6.61 | 1.8 | 3.68x | 71 |
| `SF-width` | 5.96 | 1.66 | 3.60x | 71 |
| `RT-hopassign` | 5.96 | 1.74 | 3.43x | 71 |
| `SF-jitter-global` | 5.96 | 1.75 | 3.41x | 71 |
| `LD-diurnal` | 5.06 | 1.49 | 3.39x | 71 |
| `AD-flooding` | 8.14 | 2.42 | 3.37x | 71 |
| `DB-platform` | 7.96 | 2.4 | 3.31x | 71 |
| `FW-firmware` | 5.33 | 1.62 | 3.29x | 71 |
| `RF-duct` | 5.67 | 1.73 | 3.28x | 71 |
| `AD-siting` | 4.56 | 1.45 | 3.15x | 71 |
| `PR-crladder` | 8.63 | 2.79 | 3.10x | 71 |
| `AD-amplifiers` | 4.76 | 1.57 | 3.03x | 71 |
| `BL-control` | 5.38 | 1.81 | 2.97x | 71 |
| `SF-bucket-mode` | 4.15 | 1.41 | 2.95x | 71 |
| `SF-servers-spread` | 6.2 | 2.17 | 2.86x | 71 |
| `SF-servers-flat` | 6.08 | 2.27 | 2.67x | 71 |
| `MS-roles-fav` | 4.47 | 1.7 | 2.63x | 71 |
| `RF-preset-turbo` | 3.87 | 1.48 | 2.61x | 67 |
| `SF-capacity-local` | 4.48 | 1.72 | 2.60x | 71 |
| `SF-capacity-window` | 4.13 | 1.59 | 2.59x | 71 |
| `RF-pulse` | 4 | 1.6 | 2.51x | 71 |
| `SF-cadence` | 8.45 | 3.62 | 2.33x | 71 |
| `RF-noise` | 11.4 | 4.92 | 2.32x | 71 |
| `SF-bucket-time` | 3.56 | 1.6 | 2.23x | 71 |
| `RF-txpower` | 3.5 | 1.58 | 2.22x | 71 |
| `RF-bw500` | 4.15 | 1.9 | 2.18x | 71 |
| `MS-stretch` | 4.4 | 2.04 | 2.16x | 71 |
| `DM-mode` | 5.75 | 2.71 | 2.12x | 71 |
| `FW-mixed-26` | 3.57 | 1.69 | 2.11x | 71 |
| `FW-versions` | 3.17 | 1.52 | 2.08x | 71 |
| `RT-hopspread` | 4.08 | 2.03 | 2.01x | 71 |
| `SF-window-size` | 2.53 | 1.37 | 1.85x | 71 |
| `SF-capacity` | 3.12 | 1.7 | 1.83x | 71 |
| `RF-stretch-duct` | 3.3 | 1.81 | 1.82x | 71 |
| `MS-topology` | 3.09 | 1.92 | 1.61x | 71 |
| `LD-chatty` | 7.29 | 4.55 | 1.60x | 71 |
| `SF-place-spread` | 4.32 | 2.75 | 1.57x | 71 |
| `PR-protocol` | 2.11 | 1.36 | 1.55x | 71 |
| `SF-catchup` | 13.6 | 8.85 | 1.54x | 71 |
| `DG-burst` | 7.57 | 5.02 | 1.51x | 71 |
| `DB-hotstore-stress` | 14 | 21.2 | 0.66x | 71 |
| `MS-oversubscribed` | 11.6 | 19.4 | 0.60x | 71 |
| `TH-congestion` | 9.41 | 17 | 0.55x | 71 |
| `DB-warm` | 15.7 | 34.3 | 0.46x | 71 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `MS-siting` | siting-mix | **held** | 0.051 → 0.995 | 0.944 | 0.043 → 0.951 | 1.6e+02x sr_bytes | up | 4 |
| `PR-protocol` | protocol | **held** | 0 → 0.866 | 0.866 | 0.677 → 0.695 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.835 | 0.835 | 0.695 → 0.696 | 1x bytes_on_air | up | 2 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.061 → 0.797 | 0.737 | 0.059 → 0.642 | 3.2e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.161 → 0.866 | 0.705 | 0.035 → 0.695 | 5.6x advert_bytes | up | 5 |
| `RF-preset` | preset | **held** | 0.239 → 0.899 | 0.660 | 0.168 → 0.698 | 10x sr_airtime | up | 3 |
| `RF-txpower` | tx-power | **text** | 0.052 → 0.705 | 0.653 | 0.050 → 0.688 | 4x sr_bytes | down | 4 |
| `MS-stretch` | stretch | **text** | 0.065 → 0.705 | 0.641 | 0.062 → 0.688 | 3.1x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.239 → 0.866 | 0.627 | 0.168 → 0.688 | 8.9x sr_bytes | up | 4 |
| `AD-siting` | siting-mix | **text** | 0.030 → 0.627 | 0.598 | 0.029 → 0.615 | 17x sr_bytes | down | 3 |
| `RF-bw500` | preset | **text** | 0.075 → 0.622 | 0.547 | 0.073 → 0.614 | 3.4x bytes_on_air | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.329 → 0.866 | 0.537 | 0.179 → 0.688 | 7.1x bytes_on_air | down | 4 |
| `MS-topology` | topology | **text** | 0.393 → 0.924 | 0.531 | 0.385 → 0.923 | 4.1x sr_bytes | up | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.236 → 0.719 | 0.483 | 0.226 → 0.692 | 2.9x sr_airtime | up | 2 |
| `MS-density` | nodes | **text** | 0.476 → 0.914 | 0.438 | 0.455 → 0.908 | 5.1x advert_bytes | up | 5 |
| `DG-outage` | burst-loss | **held** | 0.438 → 0.866 | 0.428 | 0.361 → 0.688 | 2.2x sr_airtime | down | 4 |
| `DG-burst` | burst-loss | **held** | 0.462 → 0.866 | 0.404 | 0.374 → 0.688 | 2x sr_airtime | down | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.521 → 0.922 | 0.401 | 0.431 → 0.744 | 14x sr_airtime | down | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.524 → 0.916 | 0.393 | 0.682 → 0.696 | 2.7x sr_bytes | down | 5 |
| `MS-size` | nodes | **held** | 0.560 → 0.942 | 0.382 | 0.451 → 0.728 | 6.1x sr_bytes | down | 5 |
| `MS-oversubscribed` | nodes | **held** | 0.325 → 0.688 | 0.363 | 0.179 → 0.507 | 4x bytes_on_air | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.494 → 0.845 | 0.351 | 0.478 → 0.839 | 7.7x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.524 → 0.848 | 0.324 | 0.502 → 0.845 | 1.9x sr_bytes | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.608 → 0.916 | 0.309 | 0.682 → 0.696 | 2.4x sr_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.524 → 0.805 | 0.281 | 0.502 → 0.798 | 1.8x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.605 → 0.866 | 0.261 | 0.520 → 0.688 | 1.7x sr_airtime | down | 4 |
| `DG-loss` | extra-loss | **held** | 0.612 → 0.866 | 0.254 | 0.518 → 0.688 | 1.6x sr_airtime | down | 4 |
| `AD-flooding` | role-mix | **held** | 0.722 → 0.973 | 0.251 | 0.615 → 0.817 | 2.1x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **held** | 0.722 → 0.973 | 0.251 | 0.615 → 0.817 | 2.1x bytes_on_air | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.647 → 0.890 | 0.242 | 0.636 → 0.886 | 3.6x sr_airtime | down | 2 |
| `SF-place-flat` | place | **held** | 0.703 → 0.942 | 0.239 | 0.682 → 0.692 | 4.2x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.703 → 0.942 | 0.239 | 0.682 → 0.692 | 4.2x sr_bytes | up | 6 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.705 → 0.934 | 0.228 | 0.688 → 0.920 | 2.2x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.705 → 0.915 | 0.210 | 0.688 → 0.893 | 1.6x sr_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.716 → 0.907 | 0.191 | 0.685 → 0.695 | 14x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.445 → 0.633 | 0.187 | 0.426 → 0.621 | 1.2x sr_airtime | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.524 → 0.705 | 0.181 | 0.502 → 0.688 | 1.4x sr_airtime | up | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.705 → 0.885 | 0.180 | 0.688 → 0.871 | 1.4x sr_bytes | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.795 → 0.967 | 0.172 | 0.676 → 0.691 | 15x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.795 → 0.967 | 0.172 | 0.676 → 0.691 | 15x sr_bytes | up | 4 |
| `SC-signing` | signature-policy | **held** | 0.699 → 0.866 | 0.167 | 0.580 → 0.688 | 1.6x sr_airtime | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.709 → 0.866 | 0.156 | 0.688 → 0.693 | 39x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **held** | 0.785 → 0.935 | 0.150 | 0.645 → 0.770 | 7.2x sr_airtime | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.345 → 0.495 | 0.150 | 0.217 → 0.306 | 3.9x sr_airtime | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.785 → 0.920 | 0.135 | 0.684 → 0.694 | 1.7x sr_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.798 → 0.922 | 0.124 | 0.677 → 0.692 | 5.8x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.798 → 0.922 | 0.124 | 0.677 → 0.692 | 5.8x advert_bytes | up | 5 |
| `SF-cadence` | trigger | **held** | 0.778 → 0.878 | 0.100 | 0.660 → 0.691 | 14x advert_bytes | up | 4 |
| `MS-roles` | role-mix | **held** | 0.722 → 0.820 | 0.098 | 0.615 → 0.663 | 1.2x bytes_on_air | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.706 → 0.802 | 0.096 | 0.686 → 0.790 | 2.2x sr_airtime | down | 3 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.779 → 0.866 | 0.087 | 0.629 → 0.688 | 1.9x sr_airtime | down | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.717 → 0.802 | 0.086 | 0.698 → 0.790 | 2.2x sr_airtime | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.693 → 0.778 | 0.086 | 0.687 → 0.763 | 2.1x bytes_on_air | up | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.866 → 0.951 | 0.086 | 0.688 → 0.754 | 1.2x bytes_on_air | up | 4 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.866 → 0.942 | 0.076 | 0.688 → 0.760 | 2.1x bytes_on_air | up | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.866 → 0.940 | 0.074 | 0.688 → 0.688 | 1.4x sr_airtime | up | 2 |
| `RT-favourites` | favourite-routers | **held** | 0.876 → 0.941 | 0.065 | 0.723 → 0.755 | 1.2x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.814 → 0.878 | 0.064 | 0.664 → 0.703 | 9x advert_bytes | down | 3 |
| `FW-versions` | profile | **held** | 0.866 → 0.927 | 0.061 | 0.688 → 0.727 | 3.2x bytes_on_air | down | 5 |
| `TH-congestion-input` | congestion-input | **held** | 0.492 → 0.547 | 0.055 | 0.306 → 0.335 | 2.2x sr_airtime | up | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.705 → 0.759 | 0.053 | 0.678 → 0.688 | 3.4x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.705 → 0.758 | 0.053 | 0.688 → 0.745 | 3.2x bytes_on_air | down | 2 |
| `FW-firmware` | profile | **held** | 0.866 → 0.917 | 0.051 | 0.688 → 0.716 | 3.2x bytes_on_air | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.588 → 0.639 | 0.051 | 0.577 → 0.628 | 1.2x sr_airtime | down | 2 |
| `AD-worst` | role-placement | **text** | 0.710 → 0.751 | 0.041 | 0.691 → 0.743 | 1.4x sr_bytes | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.866 → 0.907 | 0.041 | 0.685 → 0.690 | 2.3x advert_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.866 → 0.905 | 0.039 | 0.688 → 0.689 | 2.1x advert_bytes | up | 2 |
| `SF-resolve` | resolve | **held** | 0.827 → 0.866 | 0.038 | 0.688 → 0.694 | 6x advert_bytes | up | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.874 → 0.903 | 0.029 | 0.684 → 0.690 | 5.2x advert_bytes | down | 3 |
| `SF-width` | short-id-bits | **held** | 0.838 → 0.866 | 0.028 | 0.687 → 0.695 | 3.1x advert_bytes | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.705 → 0.733 | 0.027 | 0.688 → 0.719 | 1.2x sr_bytes | down | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.676 → 0.702 | 0.026 | 0.659 → 0.686 | 1.1x bytes_on_air | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.845 → 0.866 | 0.021 | 0.687 → 0.694 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.845 → 0.866 | 0.021 | 0.687 → 0.694 | 1.1x sr_airtime | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.705 → 0.725 | 0.020 | 0.688 → 0.706 | 1x sr_bytes | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.939 → 0.959 | 0.020 | 0.687 → 0.690 | 2.1x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.891 → 0.907 | 0.016 | 0.678 → 0.685 | 3.9x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **held** | 0.760 → 0.769 | 0.010 | 0.659 → 0.666 | 1.1x sr_airtime | down | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.856 → 0.866 | 0.010 | 0.688 → 0.695 | 1x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.661 → 0.669 | 0.009 | 0.661 → 0.669 | 1x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.882 → 0.890 | 0.008 | 0.878 → 0.886 | 1.2x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.988 → 0.992 | 0.004 | 0.886 → 0.888 | 1x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.989 → 0.992 | 0.003 | 0.886 → 0.889 | 1.1x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.809 → 0.812 | 0.003 | 0.678 → 0.678 | 1.1x sr_bytes | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `PR-dmmode-cr` | dm-mode | - | 2 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario flat`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| sprinkled | 1 | 0.794 | 0.766 | 0.027 | - | - | 0.942 | 0.963 | 0.427 | 1.32x | 14.6/20.5/26.0% | 2.1/4.8% | 3 |
| arms-race | 1 | 0.934 | 0.920 | 0.013 | - | - | 0.988 | 0.988 | 0.818 | 1.28x | 20.2/24.9/30.0% | 1.9/4.8% | 3 |

> amplifier-mix=none: decode_failures 20

> amplifier-mix=sprinkled: decode_failures 6

> slower: 4.76 s per simulated hour against 1.57 over 71 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.1 | 1 | 0.757 | 0.745 | 0.011 | - | - | 0.796 | 0.796 | 0.147 | 1.34x | 15.5/20.0/24.8% | 2.1/4.9% | 3 |
| 0.3 | 1 | 0.885 | 0.871 | 0.014 | - | - | 0.927 | 0.927 | 0.645 | 1.16x | 19.7/23.8/29.6% | 1.7/5.1% | 3 |

> amplify-worst=0.0: decode_failures 20

> amplify-worst=0.3: decode_failures 1

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.627 | 0.615 | 0.012 | - | - | 0.722 | 0.834 | 0.000 | 1.21x | 11.5/21.1/26.8% | 2.0/4.9% | 3 |
| inverse | 1 | 0.445 | 0.426 | 0.019 | - | - | 0.672 | 0.807 | 0.120 | 1.18x | 11.1/14.5/17.2% | 2.1/3.6% | 3 |
| random | 1 | 0.633 | 0.621 | 0.012 | - | - | 0.678 | 0.891 | 0.224 | 1.19x | 11.2/18.1/22.4% | 2.1/3.8% | 3 |

> role-placement=degree: decode_failures 41

> role-placement=inverse: decode_failures 31

> role-placement=random: decode_failures 30

> slower: 10.8 s per simulated hour against 1.79 over 71 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.627 | 0.615 | 0.012 | - | - | 0.722 | 0.834 | 0.000 | 1.21x | 11.5/21.1/26.8% | 2.0/4.9% | 3 |
| all-routers | 1 | 0.831 | 0.817 | 0.015 | - | - | 0.973 | 0.979 | 0.409 | 2.49x | 22.3/32.2/37.4% | 4.1/5.1% | 3 |

> role-mix=baymesh-2026-08: decode_failures 41

> slower: 8.14 s per simulated hour against 2.42 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.627 | 0.615 | 0.012 | - | - | 0.722 | 0.834 | 0.000 | 1.21x | 11.5/21.1/26.8% | 2.0/4.9% | 3 |
| no-mute | 1 | 0.694 | 0.676 | 0.018 | - | - | 0.851 | 0.904 | 0.176 | 1.38x | 12.9/18.7/24.2% | 2.2/5.0% | 3 |
| all-routers | 1 | 0.831 | 0.817 | 0.015 | - | - | 0.973 | 0.979 | 0.409 | 2.49x | 22.3/32.2/37.4% | 4.1/5.1% | 3 |

> role-mix=baymesh-2026-08: decode_failures 41

> role-mix=no-mute: decode_failures 21

> slower: 8.17 s per simulated hour against 2.21 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.627 | 0.615 | 0.012 | - | - | 0.722 | 0.834 | 0.000 | 1.21x | 11.5/21.1/26.8% | 2.0/4.9% | 3 |
| local-typical | 1 | 0.569 | 0.565 | 0.004 | - | - | 0.735 | 0.737 | 0.000 | 1.26x | 10.8/20.4/28.3% | 2.3/5.0% | 3 |
| basement-heavy | 1 | 0.030 | 0.029 | 0.000 | - | - | 0.163 | 0.163 | 0.000 | 0.35x | 0.2/3.9/6.7% | 0.2/1.9% | 3 |

> siting-mix=uniform: decode_failures 41

> slower: 4.56 s per simulated hour against 1.45 over 71 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.751 | 0.743 | 0.008 | - | - | 0.904 | 0.904 | 0.000 | 2.42x | 14.1/24.2/32.3% | 1.8/5.6% | 3 |
| inverse | 1 | 0.710 | 0.691 | 0.018 | - | - | 0.912 | 0.913 | 0.000 | 2.30x | 12.7/22.1/28.6% | 1.9/3.0% | 3 |

> role-placement=inverse: decode_failures 1

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.695 | 0.695 | 0.000 | - | - | 0 | 0.000 | 0.197 | 1.35x | 11.8/20.8/26.0% | 2.0/4.9% | 3 |
| sr | 1 | 0.728 | 0.696 | 0.033 | - | - | 0.835 | 0.927 | 0.174 | 1.38x | 12.0/21.1/26.2% | 2.1/5.0% | 3 |

> protocol=sr: decode_failures 28

> slower: 5.38 s per simulated hour against 1.81 over 71 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.717 | 0.698 | 0.019 | - | - | 0.884 | 0.921 | 0.215 | 2.93x | 28.4/42.1/51.7% | 4.1/9.5% | 3 |
| 100 | 1 | 0.802 | 0.790 | 0.013 | - | - | 0.944 | 0.966 | 0.228 | 1.58x | 16.0/23.0/28.9% | 2.2/5.3% | 3 |
| 120 | 1 | 0.802 | 0.790 | 0.013 | - | - | 0.944 | 0.966 | 0.228 | 1.58x | 16.0/23.0/28.9% | 2.2/5.3% | 3 |
| 250 | 1 | 0.802 | 0.790 | 0.013 | - | - | 0.944 | 0.966 | 0.228 | 1.58x | 16.0/23.0/28.9% | 2.2/5.3% | 3 |

> max-num-nodes=10: decode_failures 22

> max-num-nodes=100: decode_failures 25

> max-num-nodes=120: decode_failures 25

> max-num-nodes=250: decode_failures 25

> slower: 8.48 s per simulated hour against 2.3 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.220 | 0.217 | 0.004 | - | - | 0.345 | 0.355 | 0.023 | 9.92x | 25.6/39.2/59.1% | 3.4/9.4% | 3 |
| 120 | 1 | 0.310 | 0.306 | 0.004 | - | - | 0.492 | 0.494 | 0.029 | 4.47x | 11.5/18.7/28.9% | 1.6/4.4% | 3 |
| 250 | 1 | 0.310 | 0.306 | 0.004 | - | - | 0.495 | 0.496 | 0.028 | 4.41x | 11.2/18.3/28.6% | 1.5/4.4% | 3 |

> max-num-nodes=10: decode_failures 32

> max-num-nodes=120: decode_failures 1

> max-num-nodes=250: decode_failures 4

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.802 | 0.790 | 0.013 | - | - | 0.944 | 0.966 | 0.228 | 1.58x | 16.0/23.0/28.9% | 2.2/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.802 | 0.790 | 0.013 | - | - | 0.944 | 0.966 | 0.228 | 1.58x | 16.0/23.0/28.9% | 2.2/5.3% | 3 |
| constrained | 1 | 0.706 | 0.686 | 0.020 | - | - | 0.875 | 0.916 | 0.208 | 2.93x | 28.4/41.9/51.4% | 4.1/9.5% | 3 |

> platform-mix=uniform: decode_failures 25

> platform-mix=baymesh-2026-08: decode_failures 25

> platform-mix=constrained: decode_failures 23

> slower: 7.96 s per simulated hour against 2.4 over 71 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.639 | 0.628 | 0.011 | - | - | 0.816 | 0.826 | 0.409 | 5.90x | 50.7/65.3/69.7% | 4.4/12.8% | 3 |
| 25 | 1 | 0.639 | 0.628 | 0.011 | - | - | 0.816 | 0.826 | 0.409 | 5.90x | 50.7/65.3/69.7% | 4.4/12.8% | 3 |
| 100 | 1 | 0.639 | 0.628 | 0.011 | - | - | 0.816 | 0.826 | 0.409 | 5.90x | 50.7/65.3/69.7% | 4.4/12.8% | 3 |
| 2000 | 1 | 0.639 | 0.628 | 0.011 | - | - | 0.816 | 0.826 | 0.409 | 5.90x | 50.7/65.3/69.7% | 4.4/12.8% | 3 |

> warm-num-nodes=0: decode_failures 55

> warm-num-nodes=25: decode_failures 55

> warm-num-nodes=100: decode_failures 55

> warm-num-nodes=2000: decode_failures 55

> faster: 15.7 s per simulated hour against 34.3 over 71 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.1 | 1 | 0.598 | 0.583 | 0.015 | - | - | 0.723 | 0.888 | 0.163 | 1.27x | 11.3/19.9/25.3% | 1.9/4.5% | 3 |
| 0.2 | 1 | 0.499 | 0.484 | 0.016 | - | - | 0.613 | 0.809 | 0.137 | 1.13x | 10.0/17.8/22.9% | 1.8/3.8% | 3 |
| 0.3 | 1 | 0.385 | 0.374 | 0.011 | - | - | 0.462 | 0.724 | 0.065 | 1.03x | 9.4/16.6/21.7% | 1.6/3.4% | 3 |

> burst-loss=0.0: decode_failures 20

> burst-loss=0.1: decode_failures 43

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 20

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.1 | 1 | 0.655 | 0.640 | 0.014 | - | - | 0.791 | 0.920 | 0.172 | 1.38x | 12.2/21.3/26.8% | 2.1/4.8% | 3 |
| 0.2 | 1 | 0.605 | 0.597 | 0.008 | - | - | 0.699 | 0.899 | 0.124 | 1.38x | 12.6/21.4/27.3% | 2.1/4.6% | 3 |
| 0.3 | 1 | 0.526 | 0.518 | 0.007 | - | - | 0.612 | 0.850 | 0.097 | 1.33x | 12.5/20.7/26.5% | 2.1/4.2% | 3 |

> extra-loss=0.0: decode_failures 20

> extra-loss=0.1: decode_failures 25

> extra-loss=0.2: decode_failures 37

> extra-loss=0.3: decode_failures 30

> slower: 9.76 s per simulated hour against 2.22 over 71 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.1 | 1 | 0.587 | 0.575 | 0.012 | - | - | 0.717 | 0.898 | 0.120 | 1.26x | 11.3/19.7/25.1% | 2.0/4.6% | 3 |
| 0.2 | 1 | 0.486 | 0.474 | 0.012 | - | - | 0.607 | 0.829 | 0.115 | 1.19x | 10.8/18.3/23.9% | 1.9/4.2% | 3 |
| 0.3 | 1 | 0.368 | 0.361 | 0.007 | - | - | 0.438 | 0.677 | 0.089 | 1.08x | 9.9/17.4/22.8% | 1.7/3.9% | 3 |

> burst-loss=0.0: decode_failures 20

> burst-loss=0.1: decode_failures 36

> burst-loss=0.2: decode_failures 23

> burst-loss=0.3: decode_failures 19

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.666 | 0.666 | 0.000 | - | - | 0.769 | 0.935 | 0.186 | 1.69x | 14.7/26.0/32.2% | 2.5/6.0% | 3 |
| directed-with-late-flood | 1 | 0.661 | 0.661 | 0.000 | - | - | 0.760 | 0.918 | 0.181 | 1.62x | 14.2/25.0/31.0% | 2.4/5.8% | 3 |
| m4-early-flood | 1 | 0.659 | 0.659 | 0.000 | - | - | 0.766 | 0.922 | 0.171 | 1.62x | 14.2/24.9/31.0% | 2.4/5.9% | 3 |

> dm-mode=flood-only: decode_failures 30

> dm-mode=directed-with-late-flood: decode_failures 24

> dm-mode=m4-early-flood: decode_failures 26

> slower: 5.75 s per simulated hour against 2.71 over 71 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.729 | 0.716 | 0.013 | - | - | 0.917 | 0.918 | 0.000 | 0.79x | 7.0/9.8/11.8% | 1.3/2.0% | 3 |
| 2.8 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> profile=2.8: decode_failures 20

> slower: 5.33 s per simulated hour against 1.62 over 71 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.25 | 1 | 0.693 | 0.687 | 0.005 | - | - | 0.890 | 0.893 | 0.324 | 1.27x | 10.9/18.5/23.1% | 2.0/4.7% | 3 |
| 0.5 | 1 | 0.718 | 0.700 | 0.018 | - | - | 0.860 | 0.867 | 0.000 | 1.05x | 9.4/14.9/16.5% | 1.8/3.7% | 3 |
| 0.75 | 1 | 0.778 | 0.763 | 0.015 | - | - | 0.939 | 0.942 | 0.396 | 0.95x | 9.0/14.0/16.3% | 1.5/3.4% | 3 |

> legacy-fraction=0.0: decode_failures 20

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.25 | 1 | 0.700 | 0.694 | 0.006 | - | - | 0.907 | 0.908 | 0.345 | 1.27x | 11.0/18.7/23.5% | 2.1/4.7% | 3 |
| 0.5 | 1 | 0.710 | 0.688 | 0.021 | - | - | 0.870 | 0.870 | 0.000 | 1.02x | 9.4/14.7/16.1% | 1.7/3.7% | 3 |
| 0.75 | 1 | 0.776 | 0.760 | 0.016 | - | - | 0.942 | 0.950 | 0.359 | 0.92x | 8.7/13.9/16.4% | 1.5/3.4% | 3 |

> legacy-fraction=0.0: decode_failures 20

> slower: 3.57 s per simulated hour against 1.69 over 71 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.758 | 0.745 | 0.013 | - | - | 0.903 | 0.970 | 0.165 | 0.76x | 6.7/12.0/15.5% | 1.1/3.0% | 3 |
| signing=true | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> profile-flag=signing=false: decode_failures 29

> profile-flag=signing=true: decode_failures 20

> slower: 9.51 s per simulated hour against 1.52 over 71 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.724 | 0.713 | 0.011 | - | - | 0.907 | 0.912 | 0.000 | 0.80x | 7.4/10.9/12.8% | 1.3/2.3% | 3 |
| 2.5 | 1 | 0.732 | 0.722 | 0.010 | - | - | 0.919 | 0.923 | 0.000 | 0.78x | 7.3/10.7/12.5% | 1.3/2.3% | 3 |
| 2.6 | 1 | 0.733 | 0.721 | 0.013 | - | - | 0.927 | 0.929 | 0.000 | 0.78x | 7.3/11.0/12.8% | 1.3/2.4% | 3 |
| 2.7 | 1 | 0.736 | 0.727 | 0.009 | - | - | 0.922 | 0.925 | 0.000 | 0.79x | 7.2/12.3/14.3% | 1.2/3.1% | 3 |
| 2.8 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> profile=2.8: decode_failures 20

> slower: 3.17 s per simulated hour against 1.52 over 71 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.760 | 0.744 | 0.017 | - | - | 0.922 | 0.965 | 0.199 | 0.91x | 8.1/14.0/17.6% | 1.4/3.4% | 3 |
| 900 | 1 | 0.655 | 0.645 | 0.010 | - | - | 0.785 | 0.921 | 0.171 | 2.11x | 18.2/32.2/39.8% | 3.2/7.5% | 3 |
| 300 | 1 | 0.440 | 0.431 | 0.009 | - | - | 0.521 | 0.731 | 0.112 | 4.38x | 37.5/59.1/69.8% | 6.9/13.6% | 3 |

> broadcast-interval-s=3600: decode_failures 15

> broadcast-interval-s=900: decode_failures 37

> broadcast-interval-s=300: decode_failures 19

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.845 | 0.839 | 0.006 | - | - | 0.957 | 0.959 | 0.270 | 1.03x | 9.0/14.2/18.0% | 1.6/3.4% | 3 |
| 900 | 1 | 0.762 | 0.747 | 0.015 | - | - | 0.911 | 0.916 | 0.233 | 2.43x | 21.2/34.5/42.5% | 3.8/8.0% | 3 |
| 300 | 1 | 0.494 | 0.478 | 0.016 | - | - | 0.672 | 0.783 | 0.173 | 4.98x | 42.6/63.6/73.9% | 8.0/14.7% | 3 |

> broadcast-interval-s=300: decode_failures 20

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.733 | 0.719 | 0.014 | - | - | 0.886 | 0.958 | 0.182 | 1.30x | 11.3/20.2/25.2% | 2.0/4.9% | 3 |
| sinusoid | 1 | 0.721 | 0.704 | 0.017 | - | - | 0.875 | 0.945 | 0.172 | 1.27x | 11.2/19.6/24.5% | 1.9/4.7% | 3 |
| commuter | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> diurnal=flat: decode_failures 27

> diurnal=sinusoid: decode_failures 18

> diurnal=commuter: decode_failures 20

> slower: 5.06 s per simulated hour against 1.49 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.655 | 0.645 | 0.010 | - | - | 0.785 | 0.921 | 0.171 | 2.11x | 18.2/32.2/39.8% | 3.2/7.5% | 3 |
| 3600 | 1 | 0.760 | 0.744 | 0.017 | - | - | 0.922 | 0.965 | 0.199 | 0.91x | 8.1/14.0/17.6% | 1.4/3.4% | 3 |
| 10800 | 1 | 0.776 | 0.760 | 0.016 | - | - | 0.935 | 0.973 | 0.218 | 0.62x | 5.6/9.7/12.1% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.782 | 0.770 | 0.012 | - | - | 0.923 | 0.984 | 0.200 | 0.43x | 3.9/6.7/8.4% | 0.6/1.7% | 3 |

> broadcast-interval-s=900: decode_failures 37

> broadcast-interval-s=3600: decode_failures 15

> broadcast-interval-s=10800: decode_failures 21

> broadcast-interval-s=43200: decode_failures 32

> slower: 8.11 s per simulated hour against 1.27 over 71 prior run(s) - 6.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.25 | 1 | 0.697 | 0.683 | 0.014 | - | - | 0.836 | 0.932 | 0.191 | 1.45x | 12.7/22.5/28.0% | 2.2/5.3% | 3 |
| 1.0 | 1 | 0.688 | 0.675 | 0.013 | - | - | 0.825 | 0.926 | 0.189 | 1.56x | 13.6/24.1/30.1% | 2.3/5.7% | 3 |
| 4.0 | 1 | 0.640 | 0.629 | 0.011 | - | - | 0.779 | 0.911 | 0.181 | 1.92x | 16.8/29.7/37.0% | 2.9/7.0% | 3 |

> traceroute-per-hour=0.0: decode_failures 20

> traceroute-per-hour=0.25: decode_failures 31

> traceroute-per-hour=1.0: decode_failures 35

> traceroute-per-hour=4.0: decode_failures 36

> slower: 11.1 s per simulated hour against 2.1 over 71 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.639 | 0.628 | 0.011 | - | - | 0.816 | 0.826 | 0.409 | 5.90x | 50.7/65.3/69.7% | 4.4/12.8% | 3 |
| 1.0 | 1 | 0.588 | 0.577 | 0.010 | - | - | 0.767 | 0.778 | 0.398 | 6.42x | 53.8/68.2/72.1% | 4.8/13.7% | 3 |

> traceroute-per-hour=0.0: decode_failures 55

> traceroute-per-hour=1.0: decode_failures 63

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.476 | 0.455 | 0.021 | - | - | 0.746 | 0.770 | 0.000 | 1.03x | 10.5/18.3/23.7% | 2.5/6.0% | 3 |
| 60 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 90 | 1 | 0.840 | 0.834 | 0.006 | - | - | 0.989 | 0.990 | 0.221 | 1.62x | 14.4/23.7/29.1% | 1.6/5.1% | 3 |
| 120 | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.992 | 0.993 | 0.653 | 2.13x | 19.5/27.3/30.4% | 1.6/5.3% | 3 |
| 150 | 1 | 0.914 | 0.908 | 0.006 | - | - | 0.994 | 0.995 | 0.610 | 2.59x | 21.4/35.7/41.9% | 1.4/5.4% | 3 |

> nodes=40: decode_failures 5

> nodes=60: decode_failures 20

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 120 | 1 | 0.526 | 0.506 | 0.020 | - | - | 0.711 | 0.757 | 0.106 | 2.42x | 11.6/19.1/27.0% | 1.8/5.2% | 3 |
| 250 | 1 | 0.308 | 0.304 | 0.004 | - | - | 0.489 | 0.491 | 0.030 | 4.79x | 12.1/20.0/31.8% | 1.7/4.9% | 3 |
| 500 | 1 | 0.182 | 0.179 | 0.003 | - | - | 0.329 | 0.337 | 0.044 | 9.73x | 12.8/21.7/35.6% | 1.8/5.4% | 3 |

> nodes=60: decode_failures 20

> nodes=120: decode_failures 65

> nodes=250: decode_failures 6

> nodes=500: decode_failures 117

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.526 | 0.507 | 0.019 | - | - | 0.688 | 0.735 | 0.112 | 2.28x | 11.0/18.0/25.5% | 1.7/4.9% | 3 |
| 250 | 1 | 0.310 | 0.306 | 0.004 | - | - | 0.492 | 0.494 | 0.029 | 4.47x | 11.5/18.7/28.9% | 1.6/4.4% | 3 |
| 500 | 1 | 0.182 | 0.179 | 0.003 | - | - | 0.325 | 0.333 | 0.049 | 9.12x | 12.0/20.0/32.7% | 1.6/4.5% | 3 |

> nodes=120: decode_failures 23

> nodes=250: decode_failures 1

> nodes=500: decode_failures 42

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.677 | 0.663 | 0.013 | - | - | 0.820 | 0.893 | 0.227 | 1.39x | 11.9/21.2/26.4% | 2.1/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.627 | 0.615 | 0.012 | - | - | 0.722 | 0.834 | 0.000 | 1.21x | 11.5/21.1/26.8% | 2.0/4.9% | 3 |

> role-mix=legacy-default: decode_failures 26

> role-mix=baymesh-2026-08: decode_failures 41

> slower: 8.85 s per simulated hour against 1.68 over 71 prior run(s) - 5.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.702 | 0.686 | 0.016 | - | - | 0.837 | 0.887 | 0.222 | 1.43x | 12.6/21.2/26.9% | 2.2/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.676 | 0.659 | 0.018 | - | - | 0.826 | 0.848 | 0.000 | 1.33x | 13.3/22.9/28.8% | 2.2/5.1% | 3 |

> role-mix=legacy-default: decode_failures 15

> role-mix=baymesh-2026-08: decode_failures 7

> slower: 4.47 s per simulated hour against 1.7 over 71 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.05 | 1 | 0.738 | 0.723 | 0.015 | - | - | 0.903 | 0.965 | 0.192 | 1.44x | 12.9/21.9/26.7% | 2.1/5.0% | 3 |
| 0.1 | 1 | 0.753 | 0.734 | 0.019 | - | - | 0.921 | 0.968 | 0.205 | 1.54x | 15.1/23.2/29.7% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.771 | 0.754 | 0.017 | - | - | 0.951 | 0.969 | 0.196 | 1.70x | 17.1/25.6/31.9% | 2.6/5.2% | 3 |

> router-late-fraction=0.0: decode_failures 20

> router-late-fraction=0.05: decode_failures 29

> router-late-fraction=0.1: decode_failures 23

> router-late-fraction=0.2: decode_failures 4

> slower: 8.32 s per simulated hour against 1.73 over 71 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| local-typical | 1 | 0.556 | 0.547 | 0.009 | - | - | 0.723 | 0.724 | 0.000 | 1.33x | 11.8/20.8/26.8% | 2.2/5.0% | 3 |
| event | 1 | 0.043 | 0.043 | 0.000 | - | - | 0.051 | 0.102 | 0.000 | 0.40x | 0.8/4.1/7.7% | 0.4/2.0% | 2 |
| backbone | 1 | 0.952 | 0.951 | 0.001 | - | - | 0.995 | 0.995 | 0.144 | 1.21x | 24.6/32.6/34.5% | 1.5/5.5% | 3 |

> siting-mix=uniform: decode_failures 20

> siting-mix=event: 3 archives requested, 2 placed - group on the placed count

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.746 | 0.728 | 0.018 | - | - | 0.942 | 0.947 | 0.000 | 1.42x | 19.7/27.5/29.6% | 3.1/6.8% | 3 |
| 60 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 90 | 1 | 0.482 | 0.473 | 0.009 | - | - | 0.560 | 0.625 | 0.049 | 1.75x | 10.7/17.7/23.6% | 1.7/4.9% | 3 |
| 120 | 1 | 0.526 | 0.506 | 0.020 | - | - | 0.711 | 0.757 | 0.106 | 2.42x | 11.6/19.1/27.0% | 1.8/5.2% | 3 |
| 150 | 1 | 0.468 | 0.451 | 0.017 | - | - | 0.724 | 0.766 | 0.114 | 2.96x | 12.5/19.7/25.1% | 1.6/4.8% | 3 |

> nodes=60: decode_failures 20

> nodes=90: decode_failures 27

> nodes=120: decode_failures 65

> nodes=150: decode_failures 94

> slower: 14.7 s per simulated hour against 3.42 over 71 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 1.25 | 1 | 0.453 | 0.449 | 0.004 | - | - | 0.602 | 0.690 | 0.000 | 1.46x | 11.1/16.6/18.2% | 2.2/4.8% | 3 |
| 1.5 | 1 | 0.236 | 0.226 | 0.010 | - | - | 0.414 | 0.523 | 0.000 | 1.35x | 7.6/13.7/17.9% | 2.2/4.2% | 3 |
| 2.0 | 1 | 0.065 | 0.062 | 0.002 | - | - | 0.326 | 0.328 | 0.000 | 0.48x | 1.6/3.7/6.8% | 0.7/2.2% | 3 |

> stretch=1.0: decode_failures 20

> stretch=1.25: decode_failures 24

> stretch=1.5: decode_failures 14

> stretch=2.0: decode_failures 1

> slower: 4.4 s per simulated hour against 2.04 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| clustered | 1 | 0.846 | 0.845 | 0.001 | - | - | 0.903 | 0.904 | 0.000 | 1.10x | 22.2/33.5/34.5% | 1.1/5.3% | 3 |
| corridor | 1 | 0.393 | 0.385 | 0.008 | - | - | 0.494 | 0.497 | 0.071 | 1.40x | 12.6/18.1/20.4% | 2.3/4.8% | 3 |
| hub | 1 | 0.924 | 0.923 | 0.001 | - | - | 0.973 | 0.973 | 0.773 | 1.23x | 21.1/34.5/37.0% | 1.7/5.4% | 3 |

> topology=uniform: decode_failures 20

> topology=corridor: decode_failures 1

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.661 | 0.661 | 0.000 | - | - | 0.760 | 0.918 | 0.181 | 1.62x | 14.2/25.0/31.0% | 2.4/5.8% | 3 |
| True | 1 | 0.669 | 0.669 | 0.000 | - | - | 0.768 | 0.922 | 0.187 | 1.62x | 14.2/24.9/31.0% | 2.4/5.8% | 3 |

> coding-rate-ladder=False: decode_failures 24

> coding-rate-ladder=True: decode_failures 30

> slower: 8.63 s per simulated hour against 2.79 over 71 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.669 | 0.669 | 0.000 | - | - | 0.768 | 0.922 | 0.187 | 1.62x | 14.2/24.9/31.0% | 2.4/5.8% | 3 |
| m4-early-flood | 1 | 0.669 | 0.669 | 0.000 | - | - | 0.768 | 0.922 | 0.187 | 1.62x | 14.2/24.9/31.0% | 2.4/5.8% | 3 |

> inert: every value of `dm-mode` produced identical numbers - either the flag is not read, or it needs a second flag before it does anything (README §10.4)

> dm-mode=directed-with-late-flood: decode_failures 30

> dm-mode=m4-early-flood: decode_failures 30

> slower: 10.6 s per simulated hour against 2.6 over 71 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.695 | 0.695 | 0.000 | - | - | 0 | 0.000 | 0.197 | 1.35x | 11.8/20.8/26.0% | 2.0/4.9% | 3 |
| chain | 1 | 0.678 | 0.677 | 0.001 | - | - | 0.705 | 0.921 | 0.177 | 1.55x | 13.4/23.8/29.6% | 2.3/5.6% | 3 |
| sr | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> protocol=sr: decode_failures 20

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| True | 1 | 0.725 | 0.706 | 0.019 | - | - | 0.885 | 0.948 | 0.217 | 1.40x | 12.2/21.4/26.7% | 2.1/5.1% | 3 |

> extra-repeats=False: decode_failures 20

> extra-repeats=True: decode_failures 22

> slower: 8.67 s per simulated hour against 1.58 over 71 prior run(s) - 5.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.992 | 0.993 | 0.653 | 2.13x | 19.5/27.3/30.4% | 1.6/5.3% | 3 |
| True | 1 | 0.892 | 0.888 | 0.003 | - | - | 0.988 | 0.988 | 0.652 | 2.16x | 19.7/27.4/30.4% | 1.6/5.3% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.075 | 0.073 | 0.002 | - | - | 0.340 | 0.343 | 0.000 | 0.02x | 0.1/0.2/0.5% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.270 | 0.252 | 0.019 | - | - | 0.534 | 0.563 | 0.000 | 0.22x | 1.3/2.3/3.2% | 0.3/0.8% | 3 |
| LONG_TURBO | 1 | 0.622 | 0.614 | 0.008 | - | - | 0.727 | 0.791 | 0.000 | 1.34x | 10.8/14.9/17.9% | 2.1/4.4% | 3 |

> preset=MEDIUM_TURBO: decode_failures 1

> preset=LONG_TURBO: decode_failures 28

> slower: 4.15 s per simulated hour against 1.9 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 0.25 | 1 | 0.788 | 0.761 | 0.027 | - | - | 0.920 | 0.951 | 0.391 | 1.28x | 15.9/24.2/28.2% | 1.8/5.3% | 3 |
| 1.0 | 1 | 0.915 | 0.893 | 0.022 | - | - | 0.986 | 0.990 | 0.730 | 0.88x | 19.9/26.4/27.1% | 1.1/4.9% | 3 |

> duct-per-hour=0.0: decode_failures 20

> duct-per-hour=0.25: decode_failures 19

> slower: 5.67 s per simulated hour against 1.73 over 71 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.169 | 0.168 | 0.001 | - | - | 0.239 | 0.446 | 0.000 | 0.10x | 0.5/1.0/1.5% | 0.2/0.3% | 3 |
| LONG_FAST | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| LITE_FAST | 1 | 0.610 | 0.591 | 0.019 | - | - | 0.765 | 0.844 | 0.099 | 0.99x | 8.4/12.1/15.4% | 1.5/3.4% | 3 |
| NARROW_SLOW | 1 | 0.626 | 0.608 | 0.018 | - | - | 0.771 | 0.867 | 0.188 | 1.30x | 10.9/17.1/20.3% | 2.1/4.5% | 3 |

> preset=SHORT_FAST: decode_failures 5

> preset=LONG_FAST: decode_failures 20

> preset=LITE_FAST: decode_failures 33

> preset=NARROW_SLOW: decode_failures 33

> slower: 6.61 s per simulated hour against 1.8 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| temporal | 1 | 0.565 | 0.558 | 0.007 | - | - | 0.686 | 0.871 | 0.073 | 1.33x | 11.3/20.3/24.9% | 2.0/4.7% | 3 |
| transient | 1 | 0.700 | 0.687 | 0.013 | - | - | 0.842 | 0.938 | 0.191 | 1.36x | 11.8/21.0/26.0% | 2.0/4.9% | 3 |
| periodic | 1 | 0.530 | 0.520 | 0.010 | - | - | 0.605 | 0.751 | 0.132 | 1.23x | 10.9/18.8/24.0% | 1.9/4.2% | 3 |

> noise-profile=none: decode_failures 20

> noise-profile=temporal: decode_failures 27

> noise-profile=transient: decode_failures 32

> noise-profile=periodic: decode_failures 20

> slower: 11.4 s per simulated hour against 4.92 over 71 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.169 | 0.168 | 0.001 | - | - | 0.239 | 0.446 | 0.000 | 0.10x | 0.5/1.0/1.5% | 0.2/0.3% | 3 |
| LONG_FAST | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| LONG_MODERATE | 1 | 0.725 | 0.698 | 0.027 | - | - | 0.899 | 0.925 | 0.277 | 3.33x | 37.1/54.9/60.8% | 4.9/11.8% | 3 |

> preset=SHORT_FAST: decode_failures 5

> preset=LONG_FAST: decode_failures 20

> preset=LONG_MODERATE: decode_failures 21

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.035 | 0.035 | 0.000 | - | - | 0.161 | 0.254 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.075 | 0.073 | 0.002 | - | - | 0.340 | 0.343 | 0.000 | 0.02x | 0.1/0.2/0.5% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| LONG_TURBO | 1 | 0.622 | 0.614 | 0.008 | - | - | 0.727 | 0.791 | 0.000 | 1.34x | 10.8/14.9/17.9% | 2.1/4.4% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.706 | 0.695 | 0.011 | - | - | 0.830 | 0.939 | 0.229 | 1.91x | 16.2/27.9/34.4% | 2.9/6.7% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 5

> preset=LONG_FAST: decode_failures 20

> preset=LONG_TURBO: decode_failures 28

> preset=EXTRA_LONG_TURBO: decode_failures 30

> slower: 3.87 s per simulated hour against 1.48 over 67 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.655 | 0.642 | 0.013 | - | - | 0.797 | 0.894 | 0.175 | 1.33x | 11.9/20.8/26.1% | 2.0/4.8% | 3 |
| 10000 | 1 | 0.530 | 0.520 | 0.010 | - | - | 0.605 | 0.751 | 0.132 | 1.23x | 10.9/18.8/24.0% | 1.9/4.2% | 3 |
| 4000 | 1 | 0.295 | 0.295 | 0.001 | - | - | 0.301 | 0.502 | 0.038 | 1.02x | 9.7/16.1/21.0% | 1.6/3.2% | 3 |
| 2000 | 1 | 0.059 | 0.059 | 0.000 | - | - | 0.061 | 0.150 | 0.003 | 0.67x | 6.6/10.4/13.8% | 1.1/1.8% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 28

> noise-pulse-interval-ms=10000: decode_failures 20

> slower: 4 s per simulated hour against 1.6 over 71 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.236 | 0.226 | 0.010 | - | - | 0.414 | 0.523 | 0.000 | 1.35x | 7.6/13.7/17.9% | 2.2/4.2% | 3 |
| 1.0 | 1 | 0.719 | 0.692 | 0.027 | - | - | 0.833 | 0.837 | 0.456 | 0.98x | 15.4/18.6/20.7% | 1.4/4.3% | 3 |

> duct-per-hour=0.0: decode_failures 14

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 22 | 1 | 0.247 | 0.237 | 0.010 | - | - | 0.431 | 0.546 | 0.000 | 1.38x | 8.1/14.0/18.7% | 2.2/4.3% | 3 |
| 17 | 1 | 0.080 | 0.080 | 0.000 | - | - | 0.334 | 0.337 | 0.000 | 0.58x | 2.1/5.2/9.3% | 0.9/2.3% | 3 |
| 14 | 1 | 0.052 | 0.050 | 0.002 | - | - | 0.277 | 0.280 | 0.000 | 0.41x | 1.2/3.3/6.4% | 0.5/2.0% | 3 |

> tx-power=30: decode_failures 20

> tx-power=22: decode_failures 11

> tx-power=14: decode_failures 1

> slower: 3.5 s per simulated hour against 1.58 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.992 | 0.993 | 0.653 | 2.13x | 19.5/27.3/30.4% | 1.6/5.3% | 3 |
| True | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.985 | 0.987 | 0.641 | 2.40x | 21.8/29.9/33.2% | 1.8/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.734 | 0.723 | 0.011 | - | - | 0.876 | 0.967 | 0.220 | 1.39x | 12.5/21.7/26.2% | 2.1/5.0% | 3 |
| True | 1 | 0.772 | 0.755 | 0.017 | - | - | 0.941 | 0.959 | 0.221 | 1.46x | 13.4/22.3/27.3% | 2.2/5.2% | 3 |

> favourite-routers=False: decode_failures 30

> favourite-routers=True: decode_failures 6

> slower: 6.66 s per simulated hour against 1.63 over 71 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| random | 1 | 0.726 | 0.688 | 0.037 | - | - | 0.940 | 0.947 | 0.213 | 1.38x | 12.0/21.0/26.0% | 2.1/5.2% | 3 |

> hop-assign=centrality: decode_failures 20

> slower: 5.96 s per simulated hour against 1.74 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.524 | 0.502 | 0.022 | - | - | 0.712 | 0.911 | 0.128 | 1.12x | 9.8/17.1/21.8% | 1.7/4.3% | 3 |
| 7 | 1 | 0.805 | 0.798 | 0.007 | - | - | 0.925 | 0.929 | 0.267 | 1.57x | 13.7/21.9/27.5% | 2.4/5.2% | 3 |
| 15 | 1 | 0.848 | 0.845 | 0.003 | - | - | 0.935 | 0.935 | 0.263 | 1.63x | 14.2/22.1/27.8% | 2.5/5.2% | 3 |
| 32 | 1 | 0.843 | 0.839 | 0.004 | - | - | 0.924 | 0.925 | 0.258 | 1.61x | 14.1/22.1/27.9% | 2.5/5.2% | 3 |

> hop-limit=3: decode_failures 22

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.524 | 0.502 | 0.022 | - | - | 0.712 | 0.911 | 0.128 | 1.12x | 9.8/17.1/21.8% | 1.7/4.3% | 3 |
| 5 | 1 | 0.719 | 0.691 | 0.029 | - | - | 0.922 | 0.927 | 0.236 | 1.38x | 11.9/20.8/25.9% | 2.1/5.1% | 3 |
| 7 | 1 | 0.805 | 0.798 | 0.007 | - | - | 0.925 | 0.929 | 0.267 | 1.57x | 13.7/21.9/27.5% | 2.4/5.2% | 3 |

> hop-limit=3: decode_failures 22

> slower: 4.08 s per simulated hour against 2.03 over 71 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| KNOWN_ONLY | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.693 | 0.693 | 0.000 | - | - | 0.709 | 0.936 | 0.198 | 1.34x | 11.8/20.5/25.7% | 2.0/4.9% | 3 |

> rebroadcast-mode=ALL: decode_failures 20

> rebroadcast-mode=KNOWN_ONLY: decode_failures 20

> slower: 5.88 s per simulated hour against 1.55 over 71 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.524 | 0.502 | 0.022 | - | - | 0.712 | 0.911 | 0.128 | 1.12x | 9.8/17.1/21.8% | 1.7/4.3% | 3 |
| True | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> hop-spread=False: decode_failures 22

> hop-spread=True: decode_failures 20

> slower: 7.98 s per simulated hour against 2.16 over 71 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| BALANCED | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| STRICT | 1 | 0.580 | 0.580 | 0.000 | - | - | 0.699 | 0.821 | 0.113 | 1.48x | 12.8/22.8/28.4% | 2.2/5.3% | 3 |

> signature-policy=COMPATIBLE: decode_failures 20

> signature-policy=BALANCED: decode_failures 20

> signature-policy=STRICT: decode_failures 23

> slower: 8.38 s per simulated hour against 1.7 over 71 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| dm | 1 | 0.717 | 0.689 | 0.028 | - | - | 0.905 | 0.937 | 0.181 | 1.38x | 11.9/21.4/26.6% | 2.1/5.3% | 3 |

> advert-transport=broadcast: decode_failures 20

> advert-transport=dm: decode_failures 13

> slower: 8.22 s per simulated hour against 1.68 over 71 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.712 | 0.687 | 0.025 | - | - | 0.882 | 0.932 | 0.172 | 1.39x | 12.2/21.6/26.8% | 2.1/5.2% | 3 |
| local | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| time | 1 | 0.718 | 0.690 | 0.028 | - | - | 0.903 | 0.936 | 0.181 | 1.42x | 12.3/22.0/27.3% | 2.1/5.4% | 3 |
| window | 1 | 0.715 | 0.685 | 0.030 | - | - | 0.907 | 0.938 | 0.195 | 1.39x | 12.0/21.5/26.7% | 2.1/5.3% | 3 |

> bucket-mode=global: misdecodes 3

> bucket-mode=local: decode_failures 20

> bucket-mode=time: misdecodes 7

> bucket-mode=time: decode_failures 1

> bucket-mode=window: misdecodes 1

> bucket-mode=window: decode_failures 3

> slower: 4.15 s per simulated hour against 1.41 over 71 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.715 | 0.684 | 0.031 | - | - | 0.899 | 0.935 | 0.186 | 1.53x | 13.2/23.7/29.2% | 2.3/5.8% | 3 |
| 1800 | 1 | 0.718 | 0.690 | 0.028 | - | - | 0.903 | 0.936 | 0.181 | 1.42x | 12.3/22.0/27.3% | 2.1/5.4% | 3 |
| 3600 | 1 | 0.710 | 0.689 | 0.021 | - | - | 0.874 | 0.940 | 0.182 | 1.39x | 12.2/21.4/26.7% | 2.1/5.2% | 3 |

> time-bucket-s=600: misdecodes 33

> time-bucket-s=1800: misdecodes 7

> time-bucket-s=1800: decode_failures 1

> time-bucket-s=3600: decode_failures 18

> slower: 3.56 s per simulated hour against 1.6 over 71 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| interval | 1 | 0.683 | 0.660 | 0.023 | - | - | 0.856 | 0.918 | 0.192 | 1.81x | 15.5/27.7/34.5% | 2.7/7.0% | 3 |
| aimd | 1 | 0.698 | 0.691 | 0.007 | - | - | 0.778 | 0.947 | 0.183 | 1.39x | 12.2/21.4/26.6% | 2.1/5.0% | 3 |
| bucket+interval | 1 | 0.692 | 0.664 | 0.028 | - | - | 0.878 | 0.922 | 0.186 | 1.84x | 15.8/28.0/34.8% | 2.7/7.1% | 3 |

> trigger=bucket: decode_failures 20

> trigger=interval: misdecodes 7

> trigger=interval: decode_failures 13

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 11

> trigger=bucket+interval: misdecodes 2

> trigger=bucket+interval: decode_failures 16

> slower: 8.45 s per simulated hour against 3.62 over 71 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.705 | 0.692 | 0.013 | - | - | 0.840 | 0.943 | 0.183 | 1.38x | 12.1/21.1/26.3% | 2.1/5.0% | 3 |
| 8 | 1 | 0.685 | 0.677 | 0.009 | - | - | 0.798 | 0.932 | 0.177 | 1.38x | 12.1/21.1/26.5% | 2.1/5.0% | 3 |
| 16 | 1 | 0.701 | 0.690 | 0.011 | - | - | 0.831 | 0.936 | 0.153 | 1.38x | 12.2/21.1/26.4% | 2.1/5.0% | 3 |
| 32 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 50 | 1 | 0.720 | 0.690 | 0.029 | - | - | 0.922 | 0.948 | 0.189 | 1.40x | 12.1/21.6/26.8% | 2.1/5.2% | 3 |

> capacity=4: decode_failures 81

> capacity=8: decode_failures 70

> capacity=16: decode_failures 73

> capacity=32: decode_failures 20

> capacity=50: decode_failures 1

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.705 | 0.692 | 0.013 | - | - | 0.840 | 0.943 | 0.183 | 1.38x | 12.1/21.1/26.3% | 2.1/5.0% | 3 |
| 8 | 1 | 0.685 | 0.677 | 0.009 | - | - | 0.798 | 0.932 | 0.177 | 1.38x | 12.1/21.1/26.5% | 2.1/5.0% | 3 |
| 16 | 1 | 0.701 | 0.690 | 0.011 | - | - | 0.831 | 0.936 | 0.153 | 1.38x | 12.2/21.1/26.4% | 2.1/5.0% | 3 |
| 32 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 50 | 1 | 0.720 | 0.690 | 0.029 | - | - | 0.922 | 0.948 | 0.189 | 1.40x | 12.1/21.6/26.8% | 2.1/5.2% | 3 |

> capacity=4: decode_failures 81

> capacity=8: decode_failures 70

> capacity=16: decode_failures 73

> capacity=32: decode_failures 20

> capacity=50: decode_failures 1

> slower: 4.48 s per simulated hour against 1.72 over 71 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.694 | 0.694 | 0.000 | - | - | 0.716 | 0.936 | 0.187 | 1.37x | 11.9/20.9/26.2% | 2.1/4.9% | 3 |
| 16 | 1 | 0.703 | 0.695 | 0.007 | - | - | 0.761 | 0.940 | 0.185 | 1.36x | 11.9/20.9/26.2% | 2.0/5.0% | 3 |
| 32 | 1 | 0.715 | 0.685 | 0.030 | - | - | 0.907 | 0.938 | 0.195 | 1.39x | 12.0/21.5/26.7% | 2.1/5.3% | 3 |

> capacity=8: decode_failures 91

> capacity=16: decode_failures 68

> capacity=32: misdecodes 1

> capacity=32: decode_failures 3

> slower: 4.13 s per simulated hour against 1.59 over 71 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.692 | 0.664 | 0.028 | - | - | 0.878 | 0.922 | 0.186 | 1.84x | 15.8/28.0/34.8% | 2.7/7.1% | 3 |
| 02-06 | 1 | 0.712 | 0.703 | 0.009 | - | - | 0.814 | 0.954 | 0.181 | 1.41x | 12.3/21.7/27.1% | 2.1/5.1% | 3 |
| 00-08 | 1 | 0.711 | 0.699 | 0.012 | - | - | 0.832 | 0.955 | 0.188 | 1.47x | 12.8/22.6/28.2% | 2.2/5.4% | 3 |

> catch-up-hours=: misdecodes 2

> catch-up-hours=: decode_failures 16

> catch-up-hours=02-06: decode_failures 34

> catch-up-hours=00-08: decode_failures 41

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.697 | 0.694 | 0.004 | - | - | 0.916 | 0.918 | 0.207 | 1.38x | 12.2/21.6/26.9% | 2.1/5.1% | 3 |
| 2 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 3 | 1 | 0.728 | 0.696 | 0.033 | - | - | 0.835 | 0.927 | 0.174 | 1.38x | 12.0/21.1/26.2% | 2.1/5.0% | 3 |
| 4 | 1 | 0.692 | 0.682 | 0.010 | - | - | 0.608 | 0.903 | 0.164 | 1.37x | 11.9/21.0/26.2% | 2.0/5.0% | 3 |

> hops-apart=2: decode_failures 20

> hops-apart=3: decode_failures 28

> hops-apart=4: decode_failures 20

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.697 | 0.694 | 0.004 | - | - | 0.916 | 0.918 | 0.207 | 1.38x | 12.2/21.6/26.9% | 2.1/5.1% | 3 |
| 2 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 3 | 1 | 0.728 | 0.696 | 0.033 | - | - | 0.835 | 0.927 | 0.174 | 1.38x | 12.0/21.1/26.2% | 2.1/5.0% | 3 |
| 4 | 1 | 0.692 | 0.682 | 0.010 | - | - | 0.608 | 0.903 | 0.164 | 1.37x | 11.9/21.0/26.2% | 2.0/5.0% | 3 |
| 5 | 1 | 0.691 | 0.687 | 0.004 | - | - | 0.524 | 0.895 | 0.183 | 1.37x | 12.0/21.0/26.3% | 2.1/5.0% | 3 |

> hops-apart=2: decode_failures 20

> hops-apart=3: decode_failures 28

> hops-apart=4: decode_failures 20

> hops-apart=5: decode_failures 12

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.700 | 0.687 | 0.013 | - | - | 0.845 | 0.946 | 0.188 | 1.39x | 12.3/21.3/26.6% | 2.1/5.1% | 3 |
| 30 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 120 | 1 | 0.705 | 0.692 | 0.013 | - | - | 0.848 | 0.936 | 0.176 | 1.40x | 12.2/21.5/26.8% | 2.1/5.1% | 3 |
| 600 | 1 | 0.706 | 0.694 | 0.013 | - | - | 0.847 | 0.933 | 0.181 | 1.40x | 12.1/21.4/26.7% | 2.1/5.1% | 3 |

> advert-jitter-s=1: decode_failures 27

> advert-jitter-s=30: decode_failures 20

> advert-jitter-s=120: decode_failures 31

> advert-jitter-s=600: decode_failures 27

> slower: 5.96 s per simulated hour against 1.75 over 71 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.700 | 0.687 | 0.013 | - | - | 0.845 | 0.946 | 0.188 | 1.39x | 12.3/21.3/26.6% | 2.1/5.1% | 3 |
| 30 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 120 | 1 | 0.705 | 0.692 | 0.013 | - | - | 0.848 | 0.936 | 0.176 | 1.40x | 12.2/21.5/26.8% | 2.1/5.1% | 3 |
| 600 | 1 | 0.706 | 0.694 | 0.013 | - | - | 0.847 | 0.933 | 0.181 | 1.40x | 12.1/21.4/26.7% | 2.1/5.1% | 3 |

> advert-jitter-s=1: decode_failures 27

> advert-jitter-s=30: decode_failures 20

> advert-jitter-s=120: decode_failures 31

> advert-jitter-s=600: decode_failures 27

> slower: 9.87 s per simulated hour against 1.76 over 71 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.720 | 0.682 | 0.038 | - | - | 0.703 | 0.929 | 0.184 | 1.41x | 12.3/21.2/26.4% | 2.1/5.0% | 3 |
| routers | 1 | 0.713 | 0.687 | 0.026 | - | - | 0.939 | 0.948 | 0.191 | 1.37x | 12.2/21.4/26.7% | 2.1/5.2% | 3 |
| alternate-routers | 1 | 0.697 | 0.692 | 0.005 | - | - | 0.903 | 0.903 | 0.187 | 1.37x | 12.0/21.4/26.6% | 2.0/5.0% | 3 |
| beside-router | 1 | 0.701 | 0.689 | 0.013 | - | - | 0.942 | 0.946 | 0.172 | 1.38x | 12.2/21.2/26.5% | 2.1/5.0% | 3 |
| random-clients | 1 | 0.707 | 0.683 | 0.024 | - | - | 0.715 | 0.866 | 0.180 | 1.40x | 12.3/21.1/26.5% | 2.1/5.0% | 3 |
| hops-apart | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> place=spread: decode_failures 25

> place=routers: decode_failures 4

> place=random-clients: decode_failures 27

> place=hops-apart: decode_failures 20

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.720 | 0.682 | 0.038 | - | - | 0.703 | 0.929 | 0.184 | 1.41x | 12.3/21.2/26.4% | 2.1/5.0% | 3 |
| routers | 1 | 0.713 | 0.687 | 0.026 | - | - | 0.939 | 0.948 | 0.191 | 1.37x | 12.2/21.4/26.7% | 2.1/5.2% | 3 |
| alternate-routers | 1 | 0.697 | 0.692 | 0.005 | - | - | 0.903 | 0.903 | 0.187 | 1.37x | 12.0/21.4/26.6% | 2.0/5.0% | 3 |
| beside-router | 1 | 0.701 | 0.689 | 0.013 | - | - | 0.942 | 0.946 | 0.172 | 1.38x | 12.2/21.2/26.5% | 2.1/5.0% | 3 |
| random-clients | 1 | 0.707 | 0.683 | 0.024 | - | - | 0.715 | 0.866 | 0.180 | 1.40x | 12.3/21.1/26.5% | 2.1/5.0% | 3 |
| hops-apart | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> place=spread: decode_failures 25

> place=routers: decode_failures 4

> place=random-clients: decode_failures 27

> place=hops-apart: decode_failures 20

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| broadcast | 1 | 0.759 | 0.678 | 0.080 | - | - | 0.812 | 0.940 | 0.242 | 1.52x | 13.2/23.1/28.6% | 2.3/5.4% | 3 |

> provide-transport=dm: decode_failures 20

> provide-transport=broadcast: decode_failures 42

> slower: 11.2 s per simulated hour against 1.75 over 71 prior run(s) - 6.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| heard | 1 | 0.711 | 0.695 | 0.015 | - | - | 0.856 | 0.946 | 0.189 | 1.40x | 12.3/21.4/26.7% | 2.1/5.1% | 3 |

> replay-ordering=tip: decode_failures 20

> replay-ordering=heard: decode_failures 30

> slower: 9.27 s per simulated hour against 1.54 over 71 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.759 | 0.678 | 0.080 | - | - | 0.812 | 0.940 | 0.242 | 1.52x | 13.2/23.1/28.6% | 2.3/5.4% | 3 |
| heard | 1 | 0.756 | 0.678 | 0.079 | - | - | 0.809 | 0.931 | 0.269 | 1.50x | 13.0/22.8/28.1% | 2.3/5.3% | 3 |

> replay-ordering=tip: decode_failures 42

> replay-ordering=heard: decode_failures 29

> slower: 11.7 s per simulated hour against 1.63 over 71 prior run(s) - 7.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.704 | 0.693 | 0.011 | - | - | 0.834 | 0.931 | 0.175 | 1.38x | 12.0/21.1/26.3% | 2.1/5.0% | 3 |
| enum | 1 | 0.705 | 0.694 | 0.010 | - | - | 0.827 | 0.941 | 0.196 | 1.37x | 12.0/21.1/26.3% | 2.0/5.0% | 3 |
| hybrid | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> resolve=sketch: decode_failures 38

> resolve=hybrid: decode_failures 20

> slower: 7.47 s per simulated hour against 1.51 over 71 prior run(s) - 5.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.713 | 0.687 | 0.026 | - | - | 0.939 | 0.948 | 0.191 | 1.37x | 12.2/21.4/26.7% | 2.1/5.2% | 3 |
| 6 | 1 | 0.716 | 0.690 | 0.026 | - | - | 0.959 | 0.960 | 0.174 | 1.41x | 12.3/22.4/27.6% | 2.1/5.4% | 6 |

> servers=3: decode_failures 4

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.695 | 0.691 | 0.003 | - | - | 0.795 | 0.920 | 0.191 | 1.37x | 12.0/21.2/26.3% | 2.0/5.0% | 2 |
| 3 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 5 | 1 | 0.719 | 0.688 | 0.031 | - | - | 0.943 | 0.948 | 0.179 | 1.43x | 12.4/21.7/27.2% | 2.2/5.3% | 5 |
| 8 | 1 | 0.736 | 0.676 | 0.061 | - | - | 0.967 | 0.971 | 0.172 | 1.47x | 12.7/22.6/28.1% | 2.3/5.6% | 8 |

> servers=2: decode_failures 20

> servers=3: decode_failures 20

> slower: 6.08 s per simulated hour against 2.27 over 71 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.695 | 0.691 | 0.003 | - | - | 0.795 | 0.920 | 0.191 | 1.37x | 12.0/21.2/26.3% | 2.0/5.0% | 2 |
| 3 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 5 | 1 | 0.719 | 0.688 | 0.031 | - | - | 0.943 | 0.948 | 0.179 | 1.43x | 12.4/21.7/27.2% | 2.2/5.3% | 5 |
| 8 | 1 | 0.736 | 0.676 | 0.061 | - | - | 0.967 | 0.971 | 0.172 | 1.47x | 12.7/22.6/28.1% | 2.3/5.6% | 8 |

> servers=2: decode_failures 20

> servers=3: decode_failures 20

> slower: 6.2 s per simulated hour against 2.17 over 71 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| True | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |

> signed=False: decode_failures 20

> signed=True: decode_failures 20

> slower: 8.39 s per simulated hour against 1.62 over 71 prior run(s) - 5.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.694 | 0.686 | 0.008 | - | - | 0.785 | 0.945 | 0.207 | 1.29x | 11.2/19.8/24.6% | 1.9/4.6% | 3 |
| 1 | 1 | 0.726 | 0.694 | 0.032 | - | - | 0.920 | 0.959 | 0.179 | 1.32x | 11.4/20.5/25.5% | 2.0/5.0% | 3 |
| 2 | 1 | 0.701 | 0.684 | 0.016 | - | - | 0.850 | 0.941 | 0.169 | 1.30x | 11.3/20.0/24.8% | 1.9/4.7% | 3 |
| 4 | 1 | 0.701 | 0.688 | 0.013 | - | - | 0.847 | 0.947 | 0.176 | 1.31x | 11.3/19.8/24.8% | 2.0/4.7% | 3 |

> sr-retries=0: decode_failures 21

> sr-retries=1: decode_failures 5

> sr-retries=2: decode_failures 13

> sr-retries=4: decode_failures 14

> slower: 6.11 s per simulated hour against 1.51 over 71 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.707 | 0.695 | 0.012 | - | - | 0.844 | 0.946 | 0.191 | 1.38x | 11.9/21.2/26.5% | 2.1/5.0% | 3 |
| 24 | 1 | 0.708 | 0.694 | 0.015 | - | - | 0.861 | 0.941 | 0.195 | 1.38x | 12.1/21.1/26.5% | 2.1/5.1% | 3 |
| 32 | 1 | 0.705 | 0.688 | 0.018 | - | - | 0.866 | 0.944 | 0.184 | 1.39x | 12.1/21.5/26.9% | 2.1/5.1% | 3 |
| 64 | 1 | 0.700 | 0.687 | 0.013 | - | - | 0.838 | 0.938 | 0.172 | 1.40x | 12.2/21.5/26.8% | 2.1/5.1% | 3 |

> short-id-bits=16: decode_failures 30

> short-id-bits=24: decode_failures 24

> short-id-bits=32: decode_failures 20

> short-id-bits=64: decode_failures 29

> slower: 5.96 s per simulated hour against 1.66 over 71 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.713 | 0.684 | 0.029 | - | - | 0.891 | 0.927 | 0.176 | 1.46x | 12.7/22.7/28.1% | 2.2/5.5% | 3 |
| 16 | 1 | 0.709 | 0.678 | 0.032 | - | - | 0.902 | 0.928 | 0.190 | 1.41x | 12.2/21.8/27.0% | 2.1/5.4% | 3 |
| 32 | 1 | 0.715 | 0.685 | 0.030 | - | - | 0.907 | 0.938 | 0.195 | 1.39x | 12.0/21.5/26.7% | 2.1/5.3% | 3 |

> window-size=8: misdecodes 53

> window-size=16: misdecodes 10

> window-size=32: misdecodes 1

> window-size=32: decode_failures 3

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.992 | 0.993 | 0.653 | 2.13x | 19.5/27.3/30.4% | 1.6/5.3% | 3 |
| True | 1 | 0.647 | 0.636 | 0.011 | - | - | 0.830 | 0.835 | 0.430 | 5.85x | 50.3/65.0/69.5% | 4.3/12.7% | 3 |

> no-congestion-scaling=True: decode_failures 63

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.310 | 0.306 | 0.004 | - | - | 0.492 | 0.494 | 0.029 | 4.47x | 11.5/18.7/28.9% | 1.6/4.4% | 3 |
| truesize | 1 | 0.339 | 0.335 | 0.005 | - | - | 0.547 | 0.548 | 0.033 | 2.47x | 6.5/11.0/17.1% | 0.8/2.7% | 3 |

> congestion-input=hotstore: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.892 | 0.889 | 0.003 | - | - | 0.989 | 0.989 | 0.650 | 2.01x | 18.4/25.7/28.8% | 1.5/5.1% | 3 |
| adaptive | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.992 | 0.993 | 0.653 | 2.13x | 19.5/27.3/30.4% | 1.6/5.3% | 3 |

