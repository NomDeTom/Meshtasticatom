# Sweep blocks-2026-09-25-7228110

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 7228110 · seeds 7228110
- **blocks** 87 run
- **compute** 20.2 h of simulator time across every cell
- **generated** 2026-09-25T09:45:53+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>278 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 26
- AD-amplifiers: amplifier-mix=sprinkled: decode_failures 48
- AD-amplifiers: slower: 8.24 s per simulated hour against 1.65 over 35 prior run(s) - 5.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-amplify-worst: amplify-worst=0.0: decode_failures 26
- AD-amplify-worst: slower: 3.98 s per simulated hour against 1.76 over 35 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=degree: decode_failures 28
- AD-badrouters: role-placement=inverse: decode_failures 24
- AD-badrouters: role-placement=random: decode_failures 7
- AD-badrouters: slower: 5.18 s per simulated hour against 2.01 over 35 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 28
- AD-flooding: role-mix=all-routers: decode_failures 29
- AD-flooding: slower: 9.82 s per simulated hour against 2.57 over 35 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 28
- AD-nomute: role-mix=no-mute: decode_failures 27
- AD-nomute: role-mix=all-routers: decode_failures 29
- AD-nomute: slower: 9.38 s per simulated hour against 2.41 over 35 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 28
- AD-siting: siting-mix=basement-heavy: decode_failures 2
- AD-siting: slower: 3.75 s per simulated hour against 1.35 over 35 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=inverse: decode_failures 1
- BL-control: protocol=sr: decode_failures 16
- BL-control: slower: 3.61 s per simulated hour against 1.75 over 35 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 16
- DB-hotstore: max-num-nodes=100: decode_failures 30
- DB-hotstore: max-num-nodes=120: decode_failures 30
- DB-hotstore: max-num-nodes=250: decode_failures 30
- DB-hotstore: slower: 7.11 s per simulated hour against 2.42 over 35 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 104
- DB-platform: platform-mix=uniform: decode_failures 30
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 30
- DB-platform: platform-mix=constrained: decode_failures 16
- DB-platform: slower: 5.44 s per simulated hour against 2.51 over 35 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: decode_failures 95
- DB-warm: warm-num-nodes=25: decode_failures 95
- DB-warm: warm-num-nodes=100: decode_failures 95
- DB-warm: warm-num-nodes=2000: decode_failures 95
- DG-burst: burst-loss=0.0: decode_failures 26
- DG-burst: burst-loss=0.1: decode_failures 21
- DG-burst: burst-loss=0.2: decode_failures 21
- DG-burst: burst-loss=0.3: decode_failures 12
- DG-loss: extra-loss=0.0: decode_failures 26
- DG-loss: extra-loss=0.1: decode_failures 20
- DG-loss: extra-loss=0.2: decode_failures 15
- DG-loss: extra-loss=0.3: decode_failures 13
- DG-loss: slower: 5.09 s per simulated hour against 2.27 over 35 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 26
- DG-outage: burst-loss=0.1: decode_failures 33
- DG-outage: burst-loss=0.2: decode_failures 15
- DG-outage: burst-loss=0.3: decode_failures 20
- DM-mode: dm-mode=flood-only: decode_failures 16
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 10
- DM-mode: dm-mode=m4-early-flood: decode_failures 18
- FW-firmware: profile=2.8: decode_failures 26
- FW-firmware: slower: 5.04 s per simulated hour against 1.74 over 35 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.0: decode_failures 26
- FW-mixed: legacy-fraction=0.0: decode_failures 26
- FW-signing-cost: profile-flag=signing=false: decode_failures 28
- FW-signing-cost: profile-flag=signing=true: decode_failures 26
- FW-signing-cost: slower: 8.71 s per simulated hour against 1.61 over 35 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-versions: profile=2.8: decode_failures 26
- LD-chatty-hops: broadcast-interval-s=3600: decode_failures 25
- LD-chatty-hops: broadcast-interval-s=900: decode_failures 25
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 6
- LD-chatty: broadcast-interval-s=3600: decode_failures 24
- LD-chatty: broadcast-interval-s=900: decode_failures 8
- LD-chatty: broadcast-interval-s=300: decode_failures 2
- LD-diurnal: diurnal=flat: decode_failures 34
- LD-diurnal: diurnal=sinusoid: decode_failures 18
- LD-diurnal: diurnal=commuter: decode_failures 26
- LD-diurnal: slower: 6.14 s per simulated hour against 1.56 over 35 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 8
- LD-interval: broadcast-interval-s=3600: decode_failures 24
- LD-interval: broadcast-interval-s=10800: decode_failures 32
- LD-interval: broadcast-interval-s=43200: decode_failures 42
- LD-interval: slower: 8.24 s per simulated hour against 1.31 over 35 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 26
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 30
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 16
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 18
- LD-traceroute: slower: 7.62 s per simulated hour against 2.1 over 35 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 95
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 13.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 91
- MS-density: nodes=40: decode_failures 12
- MS-density: nodes=60: decode_failures 26
- MS-hopscale: nodes=60: decode_failures 26
- MS-hopscale: nodes=250: decode_failures 4
- MS-hopscale: nodes=500: decode_failures 222
- MS-oversubscribed: nodes=500: decode_failures 112
- MS-roles-fav: role-mix=legacy-default: decode_failures 34
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 18
- MS-roles-fav: slower: 8.33 s per simulated hour against 1.75 over 35 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-roles: role-mix=legacy-default: decode_failures 32
- MS-roles: role-mix=baymesh-2026-08: decode_failures 28
- MS-roles: slower: 5.34 s per simulated hour against 1.73 over 35 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 26
- MS-router-late: router-late-fraction=0.05: decode_failures 34
- MS-router-late: router-late-fraction=0.1: decode_failures 24
- MS-router-late: router-late-fraction=0.2: decode_failures 24
- MS-router-late: slower: 9.14 s per simulated hour against 1.74 over 35 prior run(s) - 5.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=uniform: decode_failures 26
- MS-size: nodes=40: decode_failures 1
- MS-size: nodes=60: decode_failures 26
- MS-size: nodes=150: decode_failures 7
- MS-stretch: stretch=1.0: decode_failures 26
- MS-stretch: stretch=1.25: decode_failures 20
- MS-stretch: stretch=1.5: 3 archives requested, 2 placed - group on the placed count
- MS-stretch: stretch=2.0: decode_failures 5
- MS-topology: topology=uniform: decode_failures 26
- PR-crladder: coding-rate-ladder=False: decode_failures 10
- PR-crladder: coding-rate-ladder=True: decode_failures 12
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 12
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 14
- PR-protocol: protocol=sr: decode_failures 26
- PR-protocol: slower: 3.52 s per simulated hour against 1.4 over 35 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats: extra-repeats=False: decode_failures 26
- PR-repeats: extra-repeats=True: decode_failures 34
- PR-repeats: slower: 7.84 s per simulated hour against 1.62 over 35 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-duct: duct-per-hour=0.0: decode_failures 26
- RF-duct: duct-per-hour=0.25: decode_failures 26
- RF-duct: duct-per-hour=1.0: decode_failures 51
- RF-duct: slower: 11.1 s per simulated hour against 1.76 over 35 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=SHORT_FAST: decode_failures 6
- RF-eu-presets: preset=LONG_FAST: decode_failures 26
- RF-noise: noise-profile=none: decode_failures 26
- RF-noise: noise-profile=temporal: decode_failures 6
- RF-noise: noise-profile=transient: decode_failures 20
- RF-noise: noise-profile=periodic: decode_failures 14
- RF-preset: preset=SHORT_FAST: decode_failures 6
- RF-preset: preset=LONG_FAST: decode_failures 26
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count
- RF-preset-turbo: preset=LONG_FAST: decode_failures 26
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 32
- RF-preset-turbo: slower: 4.23 s per simulated hour against 1.53 over 31 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 6
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 14
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-stretch-duct: duct-per-hour=0.0: 3 archives requested, 2 placed - group on the placed count
- RF-stretch-duct: duct-per-hour=1.0: 3 archives requested, 2 placed - group on the placed count
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 14
- RF-txpower: tx-power=30: decode_failures 26
- RF-txpower: tx-power=22: decode_failures 6
- RF-txpower: tx-power=17: decode_failures 9
- RF-txpower: tx-power=14: decode_failures 2
- RF-txpower: slower: 4.07 s per simulated hour against 1.59 over 35 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-favourites: favourite-routers=False: decode_failures 26
- RT-favourites: favourite-routers=True: decode_failures 32
- RT-favourites: slower: 7.64 s per simulated hour against 1.66 over 35 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 26
- RT-hopassign: hop-assign=random: decode_failures 16
- RT-hopassign: slower: 4.93 s per simulated hour against 1.88 over 35 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hoplimit: hop-limit=3: decode_failures 20
- RT-hoplimit: hop-limit=7: decode_failures 22
- RT-hoplimit: hop-limit=15: decode_failures 28
- RT-hoplimit: hop-limit=32: decode_failures 30
- RT-hoplimit: slower: 8.22 s per simulated hour against 1.76 over 35 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopspread: hop-limit=3: decode_failures 20
- RT-hopspread: hop-limit=5: decode_failures 36
- RT-hopspread: hop-limit=7: decode_failures 22
- RT-hopspread: slower: 8.4 s per simulated hour against 2.04 over 35 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 26
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 26
- RT-rebroadcast: slower: 3.5 s per simulated hour against 1.58 over 35 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-spread: hop-spread=False: decode_failures 20
- RT-spread: hop-spread=True: decode_failures 26
- RT-spread: slower: 7.37 s per simulated hour against 2.31 over 35 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 26
- SC-signing: signature-policy=BALANCED: decode_failures 26
- SC-signing: signature-policy=STRICT: decode_failures 18
- SC-signing: slower: 7.59 s per simulated hour against 1.8 over 35 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 26
- SF-advert-transport: slower: 4.59 s per simulated hour against 1.72 over 35 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 13
- SF-bucket-mode: bucket-mode=local: decode_failures 26
- SF-bucket-mode: bucket-mode=time: misdecodes 21
- SF-bucket-mode: bucket-mode=time: decode_failures 15
- SF-bucket-mode: bucket-mode=window: misdecodes 1
- SF-bucket-mode: bucket-mode=window: decode_failures 20
- SF-bucket-mode: slower: 5.73 s per simulated hour against 1.56 over 35 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-time: time-bucket-s=600: misdecodes 69
- SF-bucket-time: time-bucket-s=1800: misdecodes 21
- SF-bucket-time: time-bucket-s=1800: decode_failures 15
- SF-bucket-time: time-bucket-s=3600: misdecodes 2
- SF-bucket-time: time-bucket-s=3600: decode_failures 26
- SF-bucket-time: slower: 4.5 s per simulated hour against 1.57 over 35 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-cadence: trigger=bucket: decode_failures 26
- SF-cadence: trigger=interval: misdecodes 10
- SF-cadence: trigger=interval: decode_failures 28
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 18
- SF-cadence: trigger=bucket+interval: misdecodes 14
- SF-cadence: trigger=bucket+interval: decode_failures 17
- SF-cadence: slower: 8.22 s per simulated hour against 3.62 over 35 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 49
- SF-capacity-local: capacity=8: decode_failures 29
- SF-capacity-local: capacity=16: decode_failures 32
- SF-capacity-local: capacity=32: decode_failures 26
- SF-capacity-local: capacity=50: decode_failures 18
- SF-capacity-local: slower: 5.62 s per simulated hour against 1.77 over 35 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity: capacity=4: decode_failures 49
- SF-capacity: capacity=8: decode_failures 29
- SF-capacity: capacity=16: decode_failures 32
- SF-capacity: capacity=32: decode_failures 26
- SF-capacity: capacity=50: decode_failures 18
- SF-capacity: slower: 5.61 s per simulated hour against 1.7 over 35 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-window: capacity=8: misdecodes 3
- SF-capacity-window: capacity=8: decode_failures 51
- SF-capacity-window: capacity=16: misdecodes 1
- SF-capacity-window: capacity=16: decode_failures 20
- SF-capacity-window: capacity=32: misdecodes 1
- SF-capacity-window: capacity=32: decode_failures 20
- SF-capacity-window: slower: 3.8 s per simulated hour against 1.61 over 35 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 14
- SF-catchup: catch-up-hours=: decode_failures 17
- SF-catchup: catch-up-hours=02-06: decode_failures 43
- SF-catchup: catch-up-hours=00-08: decode_failures 47
- SF-hops-flat: hops-apart=2: decode_failures 26
- SF-hops-flat: hops-apart=3: decode_failures 16
- SF-hops-flat: hops-apart=4: decode_failures 25
- SF-hops-spread: hops-apart=2: decode_failures 26
- SF-hops-spread: hops-apart=3: decode_failures 16
- SF-hops-spread: hops-apart=4: decode_failures 25
- SF-hops-spread: hops-apart=5: decode_failures 20
- SF-jitter-global: advert-jitter-s=1: decode_failures 18
- SF-jitter-global: advert-jitter-s=30: decode_failures 26
- SF-jitter-global: advert-jitter-s=120: decode_failures 19
- SF-jitter-global: advert-jitter-s=600: decode_failures 24
- SF-jitter-global: slower: 4.38 s per simulated hour against 1.77 over 35 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 18
- SF-jitter-local: advert-jitter-s=30: decode_failures 26
- SF-jitter-local: advert-jitter-s=120: decode_failures 19
- SF-jitter-local: advert-jitter-s=600: decode_failures 24
- SF-jitter-local: slower: 7.42 s per simulated hour against 1.8 over 35 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 36
- SF-place-flat: place=hops-apart: decode_failures 26
- SF-place-spread: place=spread: decode_failures 36
- SF-place-spread: place=hops-apart: decode_failures 26
- SF-provide-transport: provide-transport=dm: decode_failures 26
- SF-provide-transport: provide-transport=broadcast: decode_failures 24
- SF-provide-transport: slower: 8.1 s per simulated hour against 1.79 over 35 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 24
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 1
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 23
- SF-replay-order-broadcast: slower: 4.73 s per simulated hour against 1.77 over 35 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 26
- SF-replay-order: replay-ordering=heard: misdecodes 8
- SF-replay-order: replay-ordering=heard: decode_failures 20
- SF-replay-order: slower: 7.5 s per simulated hour against 1.69 over 35 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-resolve: resolve=sketch: decode_failures 12
- SF-resolve: resolve=hybrid: decode_failures 26
- SF-resolve: slower: 4.59 s per simulated hour against 1.55 over 35 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=3: decode_failures 26
- SF-servers-flat: servers=5: decode_failures 47
- SF-servers-flat: servers=8: decode_failures 91
- SF-servers-flat: slower: 13.7 s per simulated hour against 2.56 over 35 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=3: decode_failures 26
- SF-servers-spread: servers=5: decode_failures 47
- SF-servers-spread: servers=8: decode_failures 91
- SF-servers-spread: slower: 13.8 s per simulated hour against 2.35 over 35 prior run(s) - 5.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 26
- SF-signed: signed=True: decode_failures 26
- SF-signed: slower: 8.12 s per simulated hour against 1.74 over 35 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 13
- SF-sr-retries: sr-retries=1: decode_failures 12
- SF-sr-retries: sr-retries=2: decode_failures 14
- SF-sr-retries: sr-retries=4: decode_failures 9
- SF-sr-retries: slower: 4.7 s per simulated hour against 1.58 over 35 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 32
- SF-width: short-id-bits=24: decode_failures 19
- SF-width: short-id-bits=32: decode_failures 26
- SF-width: short-id-bits=64: decode_failures 28
- SF-width: slower: 8.54 s per simulated hour against 1.68 over 35 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 32
- SF-window-size: window-size=16: misdecodes 9
- SF-window-size: window-size=32: misdecodes 1
- SF-window-size: window-size=32: decode_failures 20
- SF-window-size: slower: 3.61 s per simulated hour against 1.43 over 35 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: decode_failures 98

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-duct` | 11.1 | 1.76 | 6.34x | 35 |
| `LD-interval` | 8.24 | 1.31 | 6.29x | 35 |
| `SF-servers-spread` | 13.8 | 2.35 | 5.87x | 35 |
| `FW-signing-cost` | 8.71 | 1.61 | 5.41x | 35 |
| `SF-servers-flat` | 13.7 | 2.56 | 5.36x | 35 |
| `MS-router-late` | 9.14 | 1.74 | 5.25x | 35 |
| `SF-width` | 8.54 | 1.68 | 5.08x | 35 |
| `AD-amplifiers` | 8.24 | 1.65 | 4.98x | 35 |
| `PR-repeats` | 7.84 | 1.62 | 4.83x | 35 |
| `MS-roles-fav` | 8.33 | 1.75 | 4.75x | 35 |
| `RT-hoplimit` | 8.22 | 1.76 | 4.67x | 35 |
| `SF-signed` | 8.12 | 1.74 | 4.67x | 35 |
| `RT-favourites` | 7.64 | 1.66 | 4.60x | 35 |
| `SF-provide-transport` | 8.1 | 1.79 | 4.53x | 35 |
| `SF-replay-order` | 7.5 | 1.69 | 4.44x | 35 |
| `SC-signing` | 7.59 | 1.8 | 4.21x | 35 |
| `RT-hopspread` | 8.4 | 2.04 | 4.13x | 35 |
| `SF-jitter-local` | 7.42 | 1.8 | 4.12x | 35 |
| `LD-diurnal` | 6.14 | 1.56 | 3.92x | 35 |
| `AD-nomute` | 9.38 | 2.41 | 3.89x | 35 |
| `AD-flooding` | 9.82 | 2.57 | 3.82x | 35 |
| `SF-bucket-mode` | 5.73 | 1.56 | 3.66x | 35 |
| `LD-traceroute` | 7.62 | 2.1 | 3.64x | 35 |
| `SF-capacity` | 5.61 | 1.7 | 3.29x | 35 |
| `RT-spread` | 7.37 | 2.31 | 3.19x | 35 |
| `SF-capacity-local` | 5.62 | 1.77 | 3.18x | 35 |
| `MS-roles` | 5.34 | 1.73 | 3.08x | 35 |
| `SF-sr-retries` | 4.7 | 1.58 | 2.98x | 35 |
| `SF-resolve` | 4.59 | 1.55 | 2.97x | 35 |
| `DB-hotstore` | 7.11 | 2.42 | 2.94x | 35 |
| `FW-firmware` | 5.04 | 1.74 | 2.90x | 35 |
| `SF-bucket-time` | 4.5 | 1.57 | 2.87x | 35 |
| `AD-siting` | 3.75 | 1.35 | 2.77x | 35 |
| `RF-preset-turbo` | 4.23 | 1.53 | 2.77x | 31 |
| `SF-replay-order-broadcast` | 4.73 | 1.77 | 2.67x | 35 |
| `SF-advert-transport` | 4.59 | 1.72 | 2.67x | 35 |
| `RT-hopassign` | 4.93 | 1.88 | 2.62x | 35 |
| `AD-badrouters` | 5.18 | 2.01 | 2.57x | 35 |
| `RF-txpower` | 4.07 | 1.59 | 2.57x | 35 |
| `SF-window-size` | 3.61 | 1.43 | 2.53x | 35 |
| `PR-protocol` | 3.52 | 1.4 | 2.52x | 35 |
| `SF-jitter-global` | 4.38 | 1.77 | 2.48x | 35 |
| `SF-capacity-window` | 3.8 | 1.61 | 2.35x | 35 |
| `SF-cadence` | 8.22 | 3.62 | 2.27x | 35 |
| `AD-amplify-worst` | 3.98 | 1.76 | 2.26x | 35 |
| `DG-loss` | 5.09 | 2.27 | 2.24x | 35 |
| `RT-rebroadcast` | 3.5 | 1.58 | 2.22x | 35 |
| `DB-platform` | 5.44 | 2.51 | 2.16x | 35 |
| `BL-control` | 3.61 | 1.75 | 2.06x | 35 |
| `PR-dmmode-cr` | 5.14 | 2.6 | 1.98x | 35 |
| `FW-mixed-26` | 3.25 | 1.65 | 1.98x | 35 |
| `FW-versions` | 3.1 | 1.6 | 1.93x | 35 |
| `DM-mode` | 5.72 | 3.06 | 1.87x | 35 |
| `MS-stretch` | 3.69 | 2 | 1.84x | 35 |
| `RF-eu-presets` | 3.59 | 2 | 1.79x | 35 |
| `SF-hops-flat` | 6.47 | 3.65 | 1.77x | 35 |
| `LD-chatty-hops` | 7.61 | 4.32 | 1.76x | 35 |
| `RF-noise` | 8.51 | 4.91 | 1.73x | 35 |
| `PR-crladder` | 4.68 | 2.75 | 1.70x | 35 |
| `MS-hopscale` | 30.1 | 18.1 | 1.67x | 35 |
| `SF-place-flat` | 4.75 | 2.86 | 1.66x | 35 |
| `FW-mixed` | 2.77 | 1.67 | 1.65x | 35 |
| `SF-servers-allrouters` | 3.03 | 1.85 | 1.64x | 35 |
| `MS-topology` | 3.12 | 1.92 | 1.63x | 35 |
| `MS-density` | 5.39 | 3.38 | 1.59x | 35 |
| `RF-preset` | 4.65 | 2.98 | 1.56x | 35 |
| `MS-oversubscribed` | 30.4 | 19.7 | 1.54x | 35 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.932 | 0.932 | 0.744 → 0.757 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **text** | 0.075 → 0.972 | 0.897 | 0.075 → 0.972 | 38x sr_bytes | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.038 → 0.891 | 0.853 | 0.054 → 0.747 | 3.1e+02x sr_bytes | up | 5 |
| `PR-protocol` | protocol | **held** | 0 → 0.791 | 0.791 | 0.741 → 0.757 | 1.2x bytes_on_air | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.077 → 0.844 | 0.767 | 0.027 → 0.740 | 13x advert_bytes | down | 3 |
| `RF-txpower` | tx-power | **text** | 0.077 → 0.755 | 0.678 | 0.074 → 0.747 | 4.2x sr_bytes | down | 4 |
| `MS-stretch` | stretch | **held** | 0.133 → 0.791 | 0.658 | 0.113 → 0.747 | 61x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.062 → 0.714 | 0.652 | 0.072 → 0.690 | 2.3e+02x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.245 → 0.891 | 0.647 | 0.137 → 0.648 | 4.9x sr_bytes | up | 3 |
| `RF-preset` | preset | **text** | 0.238 → 0.760 | 0.521 | 0.232 → 0.749 | 3.6x sr_airtime | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.238 → 0.755 | 0.517 | 0.232 → 0.747 | 2.8x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.327 → 0.755 | 0.428 | 0.321 → 0.747 | 8.4x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.327 → 0.748 | 0.422 | 0.320 → 0.728 | 4.5x bytes_on_air | down | 3 |
| `MS-density` | nodes | **text** | 0.579 → 0.946 | 0.367 | 0.551 → 0.943 | 6.2x advert_bytes | up | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.508 → 0.861 | 0.352 | 0.502 → 0.858 | 11x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **held** | 0.133 → 0.475 | 0.343 | 0.248 → 0.541 | 7.9x sr_airtime | up | 2 |
| `DG-burst` | burst-loss | **text** | 0.439 → 0.755 | 0.316 | 0.423 → 0.747 | 1.8x sr_bytes | down | 4 |
| `DG-outage` | burst-loss | **text** | 0.444 → 0.755 | 0.312 | 0.429 → 0.747 | 1.5x advert_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.622 → 0.922 | 0.300 | 0.613 → 0.918 | 4.1x sr_bytes | up | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.573 → 0.868 | 0.295 | 0.546 → 0.866 | 1.6x bytes_on_air | up | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.502 → 0.792 | 0.290 | 0.493 → 0.785 | 11x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.587 → 0.869 | 0.281 | 0.312 → 0.526 | 6x sr_airtime | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.573 → 0.838 | 0.265 | 0.546 → 0.835 | 1.6x bytes_on_air | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.725 → 0.942 | 0.217 | 0.708 → 0.938 | 4.6x sr_airtime | down | 2 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.791 → 0.986 | 0.195 | 0.723 → 0.872 | 2.4x sr_bytes | up | 4 |
| `FW-versions` | profile | **held** | 0.791 → 0.985 | 0.193 | 0.747 → 0.840 | 3.2x bytes_on_air | down | 5 |
| `FW-mixed` | legacy-fraction | **held** | 0.791 → 0.983 | 0.192 | 0.722 → 0.869 | 2.6x sr_bytes | up | 4 |
| `RF-noise` | noise-profile | **held** | 0.604 → 0.791 | 0.188 | 0.582 → 0.747 | 1.7x sr_bytes | down | 4 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.791 → 0.974 | 0.183 | 0.747 → 0.887 | 2.3x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.573 → 0.755 | 0.182 | 0.546 → 0.747 | 1.5x sr_bytes | up | 2 |
| `FW-firmware` | profile | **held** | 0.791 → 0.971 | 0.179 | 0.747 → 0.788 | 3.2x bytes_on_air | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.626 → 0.791 | 0.165 | 0.747 → 0.755 | 34x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **held** | 0.791 → 0.948 | 0.157 | 0.747 → 0.880 | 2.9x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **held** | 0.705 → 0.862 | 0.157 | 0.696 → 0.820 | 7.1x sr_airtime | up | 4 |
| `SF-place-flat` | place | **held** | 0.791 → 0.943 | 0.152 | 0.742 → 0.760 | 2.6x sr_bytes | down | 6 |
| `SF-place-spread` | place | **held** | 0.791 → 0.943 | 0.152 | 0.742 → 0.760 | 2.6x sr_bytes | down | 6 |
| `MS-size` | nodes | **held** | 0.791 → 0.939 | 0.148 | 0.625 → 0.747 | 4.2x advert_bytes | up | 5 |
| `SF-cadence` | trigger | **held** | 0.675 → 0.821 | 0.146 | 0.731 → 0.747 | 15x advert_bytes | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.791 → 0.935 | 0.143 | 0.744 → 0.751 | 3.4x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.791 → 0.935 | 0.143 | 0.744 → 0.753 | 3.4x sr_bytes | up | 5 |
| `AD-badrouters` | role-placement | **text** | 0.609 → 0.746 | 0.137 | 0.601 → 0.740 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.618 → 0.755 | 0.137 | 0.605 → 0.747 | 1.6x sr_bytes | down | 4 |
| `SF-servers-flat` | servers | **held** | 0.791 → 0.927 | 0.136 | 0.743 → 0.752 | 15x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.791 → 0.927 | 0.136 | 0.743 → 0.752 | 15x sr_bytes | up | 4 |
| `SC-signing` | signature-policy | **held** | 0.664 → 0.791 | 0.128 | 0.656 → 0.747 | 1.7x sr_bytes | down | 3 |
| `RT-hopassign` | hop-assign | **held** | 0.672 → 0.791 | 0.120 | 0.703 → 0.747 | 1.9x sr_bytes | down | 2 |
| `DB-hotstore` | max-num-nodes | **text** | 0.711 → 0.822 | 0.112 | 0.702 → 0.817 | 2.3x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **held** | 0.791 → 0.902 | 0.110 | 0.747 → 0.855 | 1.4x sr_airtime | up | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.711 → 0.821 | 0.109 | 0.731 → 0.744 | 9.2x advert_bytes | down | 3 |
| `DB-platform` | platform-mix | **text** | 0.716 → 0.822 | 0.106 | 0.707 → 0.817 | 2.2x sr_airtime | down | 3 |
| `SF-resolve` | resolve | **held** | 0.685 → 0.791 | 0.106 | 0.747 → 0.755 | 5.9x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.702 → 0.806 | 0.104 | 0.747 → 0.753 | 3.8x sr_bytes | down | 4 |
| `SF-window-size` | window-size | **held** | 0.702 → 0.795 | 0.093 | 0.750 → 0.752 | 4.4x advert_bytes | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.746 → 0.837 | 0.091 | 0.740 → 0.828 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.746 → 0.837 | 0.091 | 0.740 → 0.828 | 2.3x bytes_on_air | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.791 → 0.881 | 0.090 | 0.747 → 0.800 | 1.3x bytes_on_air | up | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.791 → 0.867 | 0.076 | 0.747 → 0.757 | 2.2x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.720 → 0.791 | 0.072 | 0.694 → 0.747 | 1.6x sr_airtime | down | 4 |
| `SF-provide-transport` | provide-transport | **held** | 0.720 → 0.791 | 0.071 | 0.742 → 0.747 | 4.2x sr_airtime | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.670 → 0.723 | 0.053 | 0.656 → 0.706 | 1.3x sr_airtime | down | 2 |
| `MS-roles` | role-mix | **held** | 0.792 → 0.844 | 0.052 | 0.740 → 0.768 | 1.2x sr_bytes | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.755 → 0.807 | 0.052 | 0.747 → 0.800 | 3.2x bytes_on_air | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.739 → 0.784 | 0.045 | 0.745 → 0.753 | 1.4x sr_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.760 → 0.798 | 0.038 | 0.747 → 0.754 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.760 → 0.798 | 0.038 | 0.747 → 0.754 | 5.4x advert_bytes | up | 5 |
| `TH-congestion-input` | congestion-input | **held** | 0.851 → 0.887 | 0.036 | 0.518 → 0.555 | 1.4x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.638 → 0.671 | 0.033 | 0.711 → 0.733 | 1.2x sr_airtime | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.673 → 0.702 | 0.029 | 0.745 → 0.750 | 2.4x sr_bytes | up | 3 |
| `LD-diurnal` | diurnal | **held** | 0.791 → 0.819 | 0.027 | 0.747 → 0.771 | 1.5x sr_bytes | down | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.764 → 0.791 | 0.027 | 0.747 → 0.758 | 1.4x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.764 → 0.791 | 0.027 | 0.747 → 0.758 | 1.4x sr_bytes | down | 4 |
| `SF-width` | short-id-bits | **held** | 0.766 → 0.791 | 0.025 | 0.744 → 0.753 | 3.1x advert_bytes | down | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.780 → 0.799 | 0.019 | 0.771 → 0.792 | 1.1x sr_bytes | up | 2 |
| `AD-worst` | role-placement | **text** | 0.749 → 0.767 | 0.018 | 0.730 → 0.760 | 1.9x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.926 → 0.943 | 0.017 | 0.737 → 0.760 | 2.2x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.755 → 0.766 | 0.011 | 0.747 → 0.758 | 1.2x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.644 → 0.654 | 0.010 | 0.723 → 0.733 | 1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.644 → 0.654 | 0.010 | 0.717 → 0.723 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.755 → 0.764 | 0.009 | 0.747 → 0.756 | 1.2x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.934 → 0.942 | 0.007 | 0.929 → 0.938 | 1.2x sr_bytes | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.804 → 0.810 | 0.006 | 0.745 → 0.752 | 5x advert_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.776 → 0.780 | 0.004 | 0.772 → 0.774 | 1.4x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.942 → 0.945 | 0.003 | 0.938 → 0.942 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.718 → 0.720 | 0.002 | 0.736 → 0.742 | 1.2x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.942 → 0.943 | 0.001 | 0.938 → 0.939 | 1x bytes_on_air | up | 2 |

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
| none | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| sprinkled | 1 | 0.816 | 0.810 | 0.006 | - | - | 0.869 | 0.916 | 0.439 | 1.18x | 14.5/21.1/23.9% | 1.7/5.2% | 3 |
| arms-race | 1 | 0.885 | 0.880 | 0.005 | - | - | 0.948 | 0.949 | 0.639 | 1.18x | 16.5/25.1/29.2% | 1.5/5.2% | 3 |

> amplifier-mix=none: decode_failures 26

> amplifier-mix=sprinkled: decode_failures 48

> slower: 8.24 s per simulated hour against 1.65 over 35 prior run(s) - 5.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.824 | 0.800 | 0.023 | - | - | 0.939 | 0.942 | 0.439 | 1.28x | 15.5/20.8/25.9% | 1.8/4.8% | 3 |
| 0.3 | 1 | 0.895 | 0.887 | 0.009 | - | - | 0.974 | 0.976 | 0.742 | 1.17x | 17.2/23.6/28.7% | 1.6/5.3% | 3 |

> amplify-worst=0.0: decode_failures 26

> slower: 3.98 s per simulated hour against 1.76 over 35 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.746 | 0.740 | 0.007 | - | - | 0.844 | 0.886 | 0.000 | 1.16x | 13.6/20.1/24.6% | 1.8/4.8% | 3 |
| inverse | 1 | 0.609 | 0.601 | 0.009 | - | - | 0.719 | 0.774 | 0.159 | 1.19x | 13.8/19.0/23.6% | 2.1/4.2% | 3 |
| random | 1 | 0.735 | 0.729 | 0.005 | - | - | 0.744 | 0.830 | 0.269 | 1.17x | 12.5/19.9/23.7% | 2.0/4.3% | 3 |

> role-placement=degree: decode_failures 28

> role-placement=inverse: decode_failures 24

> role-placement=random: decode_failures 7

> slower: 5.18 s per simulated hour against 2.01 over 35 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.746 | 0.740 | 0.007 | - | - | 0.844 | 0.886 | 0.000 | 1.16x | 13.6/20.1/24.6% | 1.8/4.8% | 3 |
| all-routers | 1 | 0.837 | 0.828 | 0.009 | - | - | 0.892 | 0.926 | 0.529 | 2.65x | 26.2/35.7/38.1% | 4.4/5.2% | 3 |

> role-mix=baymesh-2026-08: decode_failures 28

> role-mix=all-routers: decode_failures 29

> slower: 9.82 s per simulated hour against 2.57 over 35 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.746 | 0.740 | 0.007 | - | - | 0.844 | 0.886 | 0.000 | 1.16x | 13.6/20.1/24.6% | 1.8/4.8% | 3 |
| no-mute | 1 | 0.750 | 0.742 | 0.008 | - | - | 0.831 | 0.886 | 0.183 | 1.22x | 13.2/19.9/22.1% | 1.8/4.7% | 3 |
| all-routers | 1 | 0.837 | 0.828 | 0.009 | - | - | 0.892 | 0.926 | 0.529 | 2.65x | 26.2/35.7/38.1% | 4.4/5.2% | 3 |

> role-mix=baymesh-2026-08: decode_failures 28

> role-mix=no-mute: decode_failures 27

> role-mix=all-routers: decode_failures 29

> slower: 9.38 s per simulated hour against 2.41 over 35 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.746 | 0.740 | 0.007 | - | - | 0.844 | 0.886 | 0.000 | 1.16x | 13.6/20.1/24.6% | 1.8/4.8% | 3 |
| local-typical | 1 | 0.456 | 0.451 | 0.004 | - | - | 0.659 | 0.659 | 0.000 | 1.20x | 10.5/20.6/27.3% | 1.7/5.6% | 3 |
| basement-heavy | 1 | 0.027 | 0.027 | 0.001 | - | - | 0.077 | 0.097 | 0.000 | 0.31x | 0.4/2.4/4.6% | 0.2/1.3% | 3 |

> siting-mix=uniform: decode_failures 28

> siting-mix=basement-heavy: decode_failures 2

> slower: 3.75 s per simulated hour against 1.35 over 35 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.767 | 0.760 | 0.007 | - | - | 0.931 | 0.932 | 0.000 | 2.37x | 14.4/25.4/32.1% | 1.8/5.4% | 3 |
| inverse | 1 | 0.749 | 0.730 | 0.019 | - | - | 0.928 | 0.929 | 0.000 | 2.30x | 13.9/23.4/31.3% | 1.9/3.0% | 3 |

> role-placement=inverse: decode_failures 1

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.757 | 0.757 | 0.000 | - | - | 0 | 0.000 | 0.204 | 1.24x | 13.9/20.8/24.2% | 1.8/4.7% | 3 |
| sr | 1 | 0.791 | 0.744 | 0.046 | - | - | 0.932 | 0.967 | 0.182 | 1.25x | 13.9/20.9/24.4% | 1.8/4.9% | 3 |

> protocol=sr: decode_failures 16

> slower: 3.61 s per simulated hour against 1.75 over 35 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.711 | 0.702 | 0.009 | - | - | 0.746 | 0.826 | 0.140 | 2.82x | 32.6/47.6/53.2% | 4.0/9.2% | 3 |
| 100 | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.838 | 0.919 | 0.157 | 1.54x | 17.9/27.0/30.8% | 2.1/5.1% | 3 |
| 120 | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.838 | 0.919 | 0.157 | 1.54x | 17.9/27.0/30.8% | 2.1/5.1% | 3 |
| 250 | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.838 | 0.919 | 0.157 | 1.54x | 17.9/27.0/30.8% | 2.1/5.1% | 3 |

> max-num-nodes=10: decode_failures 16

> max-num-nodes=100: decode_failures 30

> max-num-nodes=120: decode_failures 30

> max-num-nodes=250: decode_failures 30

> slower: 7.11 s per simulated hour against 2.42 over 35 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.319 | 0.312 | 0.007 | - | - | 0.587 | 0.616 | 0.132 | 11.96x | 40.0/67.2/78.4% | 4.2/11.1% | 3 |
| 120 | 1 | 0.527 | 0.518 | 0.009 | - | - | 0.851 | 0.851 | 0.213 | 4.74x | 15.2/34.8/46.9% | 1.5/5.8% | 3 |
| 250 | 1 | 0.536 | 0.526 | 0.010 | - | - | 0.869 | 0.869 | 0.208 | 4.54x | 14.6/32.9/44.4% | 1.4/5.4% | 3 |

> max-num-nodes=10: decode_failures 104

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.838 | 0.919 | 0.157 | 1.54x | 17.9/27.0/30.8% | 2.1/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.838 | 0.919 | 0.157 | 1.54x | 17.9/27.0/30.8% | 2.1/5.1% | 3 |
| constrained | 1 | 0.716 | 0.707 | 0.009 | - | - | 0.762 | 0.828 | 0.137 | 2.82x | 32.7/47.8/53.3% | 4.0/9.2% | 3 |

> platform-mix=uniform: decode_failures 30

> platform-mix=baymesh-2026-08: decode_failures 30

> platform-mix=constrained: decode_failures 16

> slower: 5.44 s per simulated hour against 2.51 over 35 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.723 | 0.706 | 0.017 | - | - | 0.870 | 0.932 | 0.395 | 5.97x | 57.0/71.3/76.7% | 4.1/12.2% | 3 |
| 25 | 1 | 0.723 | 0.706 | 0.017 | - | - | 0.870 | 0.932 | 0.395 | 5.97x | 57.0/71.3/76.7% | 4.1/12.2% | 3 |
| 100 | 1 | 0.723 | 0.706 | 0.017 | - | - | 0.870 | 0.932 | 0.395 | 5.97x | 57.0/71.3/76.7% | 4.1/12.2% | 3 |
| 2000 | 1 | 0.723 | 0.706 | 0.017 | - | - | 0.870 | 0.932 | 0.395 | 5.97x | 57.0/71.3/76.7% | 4.1/12.2% | 3 |

> warm-num-nodes=0: decode_failures 95

> warm-num-nodes=25: decode_failures 95

> warm-num-nodes=100: decode_failures 95

> warm-num-nodes=2000: decode_failures 95

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.656 | 0.642 | 0.014 | - | - | 0.706 | 0.825 | 0.160 | 1.16x | 13.3/19.7/23.1% | 1.7/4.4% | 3 |
| 0.2 | 1 | 0.554 | 0.538 | 0.016 | - | - | 0.633 | 0.753 | 0.146 | 1.09x | 12.6/18.4/22.0% | 1.6/4.0% | 3 |
| 0.3 | 1 | 0.439 | 0.423 | 0.017 | - | - | 0.500 | 0.654 | 0.130 | 0.96x | 11.1/16.8/20.0% | 1.4/3.3% | 3 |

> burst-loss=0.0: decode_failures 26

> burst-loss=0.1: decode_failures 21

> burst-loss=0.2: decode_failures 21

> burst-loss=0.3: decode_failures 12

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.721 | 0.711 | 0.010 | - | - | 0.733 | 0.829 | 0.198 | 1.31x | 14.8/21.5/25.3% | 2.0/4.7% | 3 |
| 0.2 | 1 | 0.674 | 0.664 | 0.010 | - | - | 0.689 | 0.803 | 0.186 | 1.32x | 14.8/21.8/25.6% | 2.0/4.5% | 3 |
| 0.3 | 1 | 0.618 | 0.605 | 0.013 | - | - | 0.662 | 0.788 | 0.162 | 1.33x | 14.8/22.0/26.0% | 2.1/4.2% | 3 |

> extra-loss=0.0: decode_failures 26

> extra-loss=0.1: decode_failures 20

> extra-loss=0.2: decode_failures 15

> extra-loss=0.3: decode_failures 13

> slower: 5.09 s per simulated hour against 2.27 over 35 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.643 | 0.631 | 0.012 | - | - | 0.691 | 0.812 | 0.162 | 1.17x | 13.5/19.8/23.2% | 1.7/4.5% | 3 |
| 0.2 | 1 | 0.541 | 0.526 | 0.016 | - | - | 0.638 | 0.768 | 0.152 | 1.08x | 12.7/18.6/22.2% | 1.6/4.4% | 3 |
| 0.3 | 1 | 0.444 | 0.429 | 0.014 | - | - | 0.521 | 0.661 | 0.138 | 1.01x | 11.7/17.5/20.7% | 1.5/3.5% | 3 |

> burst-loss=0.0: decode_failures 26

> burst-loss=0.1: decode_failures 33

> burst-loss=0.2: decode_failures 15

> burst-loss=0.3: decode_failures 20

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.711 | 0.711 | 0.000 | - | - | 0.638 | 0.820 | 0.174 | 1.60x | 18.2/26.6/31.2% | 2.3/5.9% | 3 |
| directed-with-late-flood | 1 | 0.717 | 0.717 | 0.000 | - | - | 0.654 | 0.826 | 0.188 | 1.48x | 17.0/25.1/29.4% | 2.1/5.8% | 3 |
| m4-early-flood | 1 | 0.733 | 0.733 | 0.000 | - | - | 0.671 | 0.847 | 0.196 | 1.47x | 16.8/24.7/29.1% | 2.1/5.8% | 3 |

> dm-mode=flood-only: decode_failures 16

> dm-mode=directed-with-late-flood: decode_failures 10

> dm-mode=m4-early-flood: decode_failures 18

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.797 | 0.788 | 0.010 | - | - | 0.971 | 0.972 | 0.453 | 0.70x | 7.3/10.7/11.8% | 1.2/2.1% | 3 |
| 2.8 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> profile=2.8: decode_failures 26

> slower: 5.04 s per simulated hour against 1.74 over 35 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.736 | 0.722 | 0.014 | - | - | 0.911 | 0.912 | 0.152 | 1.10x | 11.9/17.6/21.5% | 1.6/4.2% | 3 |
| 0.5 | 1 | 0.861 | 0.853 | 0.007 | - | - | 0.971 | 0.971 | 0.623 | 1.07x | 11.7/16.0/19.2% | 1.8/3.9% | 3 |
| 0.75 | 1 | 0.875 | 0.869 | 0.006 | - | - | 0.983 | 0.984 | 0.686 | 0.91x | 9.8/12.8/15.2% | 1.5/3.0% | 3 |

> legacy-fraction=0.0: decode_failures 26

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.736 | 0.723 | 0.013 | - | - | 0.919 | 0.921 | 0.151 | 1.12x | 12.0/17.7/21.6% | 1.7/4.2% | 3 |
| 0.5 | 1 | 0.848 | 0.838 | 0.010 | - | - | 0.967 | 0.969 | 0.639 | 1.06x | 11.7/16.4/19.6% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.877 | 0.872 | 0.006 | - | - | 0.986 | 0.987 | 0.650 | 0.88x | 9.9/12.6/15.2% | 1.4/3.1% | 3 |

> legacy-fraction=0.0: decode_failures 26

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.807 | 0.800 | 0.007 | - | - | 0.837 | 0.907 | 0.206 | 0.69x | 7.9/12.0/14.3% | 1.0/2.9% | 3 |
| signing=true | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> profile-flag=signing=false: decode_failures 28

> profile-flag=signing=true: decode_failures 26

> slower: 8.71 s per simulated hour against 1.61 over 35 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.830 | 0.822 | 0.008 | - | - | 0.980 | 0.984 | 0.502 | 0.72x | 7.9/11.1/12.9% | 1.1/2.6% | 3 |
| 2.5 | 1 | 0.829 | 0.819 | 0.009 | - | - | 0.985 | 0.985 | 0.537 | 0.73x | 7.8/11.1/12.6% | 1.1/2.6% | 3 |
| 2.6 | 1 | 0.826 | 0.816 | 0.010 | - | - | 0.980 | 0.980 | 0.511 | 0.70x | 7.6/11.0/12.9% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.847 | 0.840 | 0.007 | - | - | 0.983 | 0.985 | 0.500 | 0.70x | 7.9/11.7/13.5% | 1.0/2.9% | 3 |
| 2.8 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> profile=2.8: decode_failures 26

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.792 | 0.785 | 0.007 | - | - | 0.797 | 0.886 | 0.225 | 0.84x | 9.6/13.9/16.4% | 1.2/3.3% | 3 |
| 900 | 1 | 0.704 | 0.696 | 0.008 | - | - | 0.705 | 0.808 | 0.184 | 1.94x | 22.1/32.0/37.4% | 2.7/7.3% | 3 |
| 300 | 1 | 0.502 | 0.493 | 0.010 | - | - | 0.529 | 0.588 | 0.113 | 4.10x | 44.8/61.5/70.9% | 6.2/13.7% | 3 |

> broadcast-interval-s=3600: decode_failures 24

> broadcast-interval-s=900: decode_failures 8

> broadcast-interval-s=300: decode_failures 2

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.861 | 0.858 | 0.003 | - | - | 0.862 | 0.937 | 0.213 | 0.95x | 10.5/14.9/17.6% | 1.5/3.5% | 3 |
| 900 | 1 | 0.773 | 0.769 | 0.004 | - | - | 0.779 | 0.852 | 0.193 | 2.15x | 23.9/33.8/40.1% | 3.1/7.8% | 3 |
| 300 | 1 | 0.508 | 0.502 | 0.007 | - | - | 0.534 | 0.615 | 0.150 | 4.60x | 48.8/64.7/74.2% | 7.1/14.7% | 3 |

> broadcast-interval-s=3600: decode_failures 25

> broadcast-interval-s=900: decode_failures 25

> broadcast-interval-s=300: decode_failures 6

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.819 | 0.874 | 0.192 | 1.18x | 13.5/19.8/23.1% | 1.7/4.6% | 3 |
| sinusoid | 1 | 0.779 | 0.771 | 0.008 | - | - | 0.799 | 0.883 | 0.233 | 1.14x | 13.0/18.8/21.9% | 1.6/4.3% | 3 |
| commuter | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> diurnal=flat: decode_failures 34

> diurnal=sinusoid: decode_failures 18

> diurnal=commuter: decode_failures 26

> slower: 6.14 s per simulated hour against 1.56 over 35 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.704 | 0.696 | 0.008 | - | - | 0.705 | 0.808 | 0.184 | 1.94x | 22.1/32.0/37.4% | 2.7/7.3% | 3 |
| 3600 | 1 | 0.792 | 0.785 | 0.007 | - | - | 0.797 | 0.886 | 0.225 | 0.84x | 9.6/13.9/16.4% | 1.2/3.3% | 3 |
| 10800 | 1 | 0.821 | 0.813 | 0.008 | - | - | 0.862 | 0.931 | 0.235 | 0.56x | 6.4/9.2/11.0% | 0.8/2.2% | 3 |
| 43200 | 1 | 0.825 | 0.820 | 0.005 | - | - | 0.811 | 0.930 | 0.237 | 0.40x | 4.6/6.6/7.8% | 0.6/1.6% | 3 |

> broadcast-interval-s=900: decode_failures 8

> broadcast-interval-s=3600: decode_failures 24

> broadcast-interval-s=10800: decode_failures 32

> broadcast-interval-s=43200: decode_failures 42

> slower: 8.24 s per simulated hour against 1.31 over 35 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.749 | 0.741 | 0.008 | - | - | 0.746 | 0.850 | 0.174 | 1.32x | 14.9/21.9/25.6% | 1.9/5.1% | 3 |
| 1.0 | 1 | 0.738 | 0.731 | 0.007 | - | - | 0.750 | 0.840 | 0.177 | 1.42x | 16.3/24.1/28.1% | 2.0/5.5% | 3 |
| 4.0 | 1 | 0.703 | 0.694 | 0.009 | - | - | 0.720 | 0.804 | 0.170 | 1.72x | 20.0/29.8/34.8% | 2.4/6.8% | 3 |

> traceroute-per-hour=0.0: decode_failures 26

> traceroute-per-hour=0.25: decode_failures 30

> traceroute-per-hour=1.0: decode_failures 16

> traceroute-per-hour=4.0: decode_failures 18

> slower: 7.62 s per simulated hour against 2.1 over 35 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.706 | 0.017 | - | - | 0.870 | 0.932 | 0.395 | 5.97x | 57.0/71.3/76.7% | 4.1/12.2% | 3 |
| 1.0 | 1 | 0.670 | 0.656 | 0.014 | - | - | 0.833 | 0.912 | 0.357 | 6.50x | 60.6/73.3/78.6% | 4.5/13.2% | 3 |

> traceroute-per-hour=0.0: decode_failures 95

> traceroute-per-hour=1.0: queue drops 13.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 91

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.579 | 0.551 | 0.027 | - | - | 0.641 | 0.705 | 0.383 | 1.10x | 13.1/18.2/20.3% | 2.4/5.5% | 3 |
| 60 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 90 | 1 | 0.907 | 0.898 | 0.009 | - | - | 0.977 | 0.979 | 0.142 | 1.58x | 16.0/26.3/31.9% | 1.5/5.0% | 3 |
| 120 | 1 | 0.942 | 0.938 | 0.004 | - | - | 0.998 | 0.998 | 0.550 | 2.11x | 22.2/31.7/36.1% | 1.4/5.0% | 3 |
| 150 | 1 | 0.946 | 0.943 | 0.002 | - | - | 0.999 | 1.000 | 0.535 | 2.71x | 25.3/38.9/43.4% | 1.4/5.6% | 3 |

> nodes=40: decode_failures 12

> nodes=60: decode_failures 26

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 120 | 1 | 0.753 | 0.735 | 0.019 | - | - | 0.891 | 0.893 | 0.203 | 2.32x | 15.2/30.5/38.4% | 1.6/4.7% | 3 |
| 250 | 1 | 0.524 | 0.513 | 0.011 | - | - | 0.853 | 0.854 | 0.214 | 5.10x | 16.4/37.6/50.3% | 1.6/6.1% | 3 |
| 500 | 1 | 0.327 | 0.321 | 0.006 | - | - | 0.546 | 0.550 | 0.090 | 10.29x | 19.1/33.1/54.7% | 1.7/6.5% | 3 |

> nodes=60: decode_failures 26

> nodes=250: decode_failures 4

> nodes=500: decode_failures 222

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.748 | 0.728 | 0.021 | - | - | 0.897 | 0.899 | 0.210 | 2.16x | 14.2/28.8/36.3% | 1.5/4.3% | 3 |
| 250 | 1 | 0.527 | 0.518 | 0.009 | - | - | 0.851 | 0.851 | 0.213 | 4.74x | 15.2/34.8/46.9% | 1.5/5.8% | 3 |
| 500 | 1 | 0.327 | 0.320 | 0.006 | - | - | 0.546 | 0.548 | 0.089 | 9.68x | 17.8/30.7/51.1% | 1.6/5.7% | 3 |

> nodes=500: decode_failures 112

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.773 | 0.768 | 0.005 | - | - | 0.792 | 0.885 | 0.187 | 1.27x | 14.5/21.2/24.9% | 1.8/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.746 | 0.740 | 0.007 | - | - | 0.844 | 0.886 | 0.000 | 1.16x | 13.6/20.1/24.6% | 1.8/4.8% | 3 |

> role-mix=legacy-default: decode_failures 32

> role-mix=baymesh-2026-08: decode_failures 28

> slower: 5.34 s per simulated hour against 1.73 over 35 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.780 | 0.774 | 0.006 | - | - | 0.823 | 0.883 | 0.179 | 1.31x | 15.0/21.8/25.5% | 1.9/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.776 | 0.772 | 0.004 | - | - | 0.824 | 0.893 | 0.000 | 1.29x | 15.6/21.3/26.2% | 2.2/4.8% | 3 |

> role-mix=legacy-default: decode_failures 34

> role-mix=baymesh-2026-08: decode_failures 18

> slower: 8.33 s per simulated hour against 1.75 over 35 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.05 | 1 | 0.778 | 0.771 | 0.007 | - | - | 0.795 | 0.865 | 0.178 | 1.39x | 15.8/24.7/28.1% | 2.0/4.9% | 3 |
| 0.1 | 1 | 0.790 | 0.782 | 0.008 | - | - | 0.810 | 0.893 | 0.165 | 1.50x | 16.9/27.7/30.8% | 2.2/5.1% | 3 |
| 0.2 | 1 | 0.809 | 0.800 | 0.009 | - | - | 0.881 | 0.914 | 0.172 | 1.68x | 19.3/31.5/35.9% | 2.4/5.1% | 3 |

> router-late-fraction=0.0: decode_failures 26

> router-late-fraction=0.05: decode_failures 34

> router-late-fraction=0.1: decode_failures 24

> router-late-fraction=0.2: decode_failures 24

> slower: 9.14 s per simulated hour against 1.74 over 35 prior run(s) - 5.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| local-typical | 1 | 0.467 | 0.461 | 0.005 | - | - | 0.665 | 0.666 | 0.000 | 1.43x | 12.0/21.4/28.9% | 1.9/5.8% | 3 |
| event | 1 | 0.075 | 0.075 | 0.000 | - | - | 0.134 | 0.134 | 0.000 | 0.56x | 2.2/6.7/8.8% | 0.8/2.2% | 3 |
| backbone | 1 | 0.972 | 0.972 | 0.000 | - | - | 0.997 | 0.997 | 0.840 | 1.15x | 20.9/30.0/33.5% | 1.3/5.5% | 3 |

> siting-mix=uniform: decode_failures 26

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.746 | 0.710 | 0.036 | - | - | 0.859 | 0.878 | 0.614 | 1.22x | 17.4/24.6/26.2% | 2.7/6.8% | 3 |
| 60 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 90 | 1 | 0.737 | 0.728 | 0.010 | - | - | 0.939 | 0.940 | 0.000 | 1.53x | 14.0/22.0/26.1% | 1.3/4.9% | 3 |
| 120 | 1 | 0.753 | 0.735 | 0.019 | - | - | 0.891 | 0.893 | 0.203 | 2.32x | 15.2/30.5/38.4% | 1.6/4.7% | 3 |
| 150 | 1 | 0.640 | 0.625 | 0.015 | - | - | 0.899 | 0.900 | 0.170 | 2.81x | 14.9/30.2/36.5% | 1.5/5.1% | 3 |

> nodes=40: decode_failures 1

> nodes=60: decode_failures 26

> nodes=150: decode_failures 7

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 1.25 | 1 | 0.432 | 0.420 | 0.012 | - | - | 0.686 | 0.725 | 0.000 | 1.31x | 11.6/17.2/20.2% | 1.9/4.6% | 3 |
| 1.5 | 1 | 0.248 | 0.248 | 0.000 | - | - | 0.133 | 0.266 | 0.000 | 1.21x | 7.2/16.4/20.1% | 1.6/5.0% | 2 |
| 2.0 | 1 | 0.115 | 0.113 | 0.002 | - | - | 0.246 | 0.292 | 0.000 | 0.74x | 3.6/7.8/9.8% | 1.2/3.1% | 3 |

> stretch=1.0: decode_failures 26

> stretch=1.25: decode_failures 20

> stretch=1.5: 3 archives requested, 2 placed - group on the placed count

> stretch=2.0: decode_failures 5

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| clustered | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.982 | 0.982 | 0.171 | 1.08x | 22.2/28.1/32.4% | 1.3/5.5% | 3 |
| corridor | 1 | 0.622 | 0.613 | 0.009 | - | - | 0.811 | 0.813 | 0.244 | 1.34x | 16.1/26.1/30.0% | 1.8/5.7% | 3 |
| hub | 1 | 0.897 | 0.896 | 0.000 | - | - | 0.942 | 0.942 | 0.777 | 1.22x | 25.7/35.3/37.2% | 1.6/5.4% | 3 |

> topology=uniform: decode_failures 26

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.717 | 0.717 | 0.000 | - | - | 0.654 | 0.826 | 0.188 | 1.48x | 17.0/25.1/29.4% | 2.1/5.8% | 3 |
| True | 1 | 0.723 | 0.723 | 0.000 | - | - | 0.644 | 0.830 | 0.178 | 1.45x | 16.6/24.5/28.7% | 2.1/5.7% | 3 |

> coding-rate-ladder=False: decode_failures 10

> coding-rate-ladder=True: decode_failures 12

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.723 | 0.723 | 0.000 | - | - | 0.644 | 0.830 | 0.178 | 1.45x | 16.6/24.5/28.7% | 2.1/5.7% | 3 |
| m4-early-flood | 1 | 0.733 | 0.733 | 0.000 | - | - | 0.654 | 0.843 | 0.177 | 1.47x | 16.8/24.8/29.1% | 2.1/5.7% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 12

> dm-mode=m4-early-flood: decode_failures 14

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.757 | 0.757 | 0.000 | - | - | 0 | 0.000 | 0.204 | 1.24x | 13.9/20.8/24.2% | 1.8/4.7% | 3 |
| chain | 1 | 0.745 | 0.741 | 0.004 | - | - | 0.713 | 0.855 | 0.186 | 1.46x | 16.4/23.9/28.4% | 2.1/5.5% | 3 |
| sr | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> protocol=sr: decode_failures 26

> slower: 3.52 s per simulated hour against 1.4 over 35 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| True | 1 | 0.766 | 0.758 | 0.009 | - | - | 0.783 | 0.866 | 0.188 | 1.28x | 14.6/21.1/24.7% | 1.8/4.9% | 3 |

> extra-repeats=False: decode_failures 26

> extra-repeats=True: decode_failures 34

> slower: 7.84 s per simulated hour against 1.62 over 35 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.942 | 0.938 | 0.004 | - | - | 0.998 | 0.998 | 0.550 | 2.11x | 22.2/31.7/36.1% | 1.4/5.0% | 3 |
| True | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.998 | 0.999 | 0.540 | 2.15x | 22.4/32.1/36.7% | 1.5/5.1% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.138 | 0.137 | 0.001 | - | - | 0.245 | 0.246 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.339 | 0.331 | 0.008 | - | - | 0.529 | 0.531 | 0.000 | 0.25x | 1.7/2.9/3.4% | 0.4/0.9% | 3 |
| LONG_TURBO | 1 | 0.674 | 0.648 | 0.026 | - | - | 0.891 | 0.894 | 0.112 | 1.10x | 10.0/14.7/18.6% | 1.7/4.3% | 3 |

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.802 | 0.792 | 0.010 | - | - | 0.865 | 0.897 | 0.273 | 1.09x | 14.1/20.4/23.8% | 1.4/4.6% | 3 |
| 1.0 | 1 | 0.865 | 0.855 | 0.010 | - | - | 0.902 | 0.926 | 0.515 | 0.97x | 16.5/23.0/26.0% | 1.2/5.0% | 3 |

> duct-per-hour=0.0: decode_failures 26

> duct-per-hour=0.25: decode_failures 26

> duct-per-hour=1.0: decode_failures 51

> slower: 11.1 s per simulated hour against 1.76 over 35 prior run(s) - 6.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.238 | 0.232 | 0.007 | - | - | 0.390 | 0.394 | 0.000 | 0.12x | 0.8/1.3/1.5% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| LITE_FAST | 1 | 0.674 | 0.656 | 0.018 | - | - | 0.880 | 0.889 | 0.049 | 0.90x | 9.1/14.4/17.8% | 1.4/3.4% | 3 |
| NARROW_SLOW | 1 | 0.710 | 0.697 | 0.013 | - | - | 0.874 | 0.876 | 0.128 | 1.16x | 12.2/18.4/22.6% | 1.7/4.4% | 3 |

> preset=SHORT_FAST: decode_failures 6

> preset=LONG_FAST: decode_failures 26

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| temporal | 1 | 0.636 | 0.629 | 0.007 | - | - | 0.661 | 0.775 | 0.090 | 1.20x | 13.8/19.9/23.9% | 1.8/4.5% | 3 |
| transient | 1 | 0.745 | 0.736 | 0.009 | - | - | 0.769 | 0.849 | 0.190 | 1.25x | 14.1/20.5/24.0% | 1.8/4.8% | 3 |
| periodic | 1 | 0.591 | 0.582 | 0.009 | - | - | 0.604 | 0.684 | 0.148 | 1.15x | 13.2/19.2/22.4% | 1.7/4.2% | 3 |

> noise-profile=none: decode_failures 26

> noise-profile=temporal: decode_failures 6

> noise-profile=transient: decode_failures 20

> noise-profile=periodic: decode_failures 14

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.238 | 0.232 | 0.007 | - | - | 0.390 | 0.394 | 0.000 | 0.12x | 0.8/1.3/1.5% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| LONG_MODERATE | 1 | 0.760 | 0.749 | 0.010 | - | - | 0.817 | 0.821 | 0.398 | 3.33x | 40.5/55.1/64.0% | 4.8/11.9% | 3 |

> preset=SHORT_FAST: decode_failures 6

> preset=LONG_FAST: decode_failures 26

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.054 | 0.054 | 0.000 | - | - | 0.038 | 0.077 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 2 |
| SHORT_TURBO | 1 | 0.138 | 0.137 | 0.001 | - | - | 0.245 | 0.246 | 0.000 | 0.04x | 0.2/0.3/0.5% | 0.1/0.1% | 3 |
| LONG_FAST | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| LONG_TURBO | 1 | 0.674 | 0.648 | 0.026 | - | - | 0.891 | 0.894 | 0.112 | 1.10x | 10.0/14.7/18.6% | 1.7/4.3% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.795 | 0.852 | 0.262 | 1.69x | 18.1/25.8/31.1% | 2.5/6.6% | 3 |

> preset=EXTRA_SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count

> preset=LONG_FAST: decode_failures 26

> preset=EXTRA_LONG_TURBO: decode_failures 32

> slower: 4.23 s per simulated hour against 1.53 over 31 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.697 | 0.690 | 0.007 | - | - | 0.714 | 0.809 | 0.174 | 1.20x | 13.9/20.2/23.6% | 1.7/4.6% | 3 |
| 10000 | 1 | 0.591 | 0.582 | 0.009 | - | - | 0.604 | 0.684 | 0.148 | 1.15x | 13.2/19.2/22.4% | 1.7/4.2% | 3 |
| 4000 | 1 | 0.347 | 0.345 | 0.002 | - | - | 0.327 | 0.447 | 0.079 | 0.97x | 11.0/16.5/19.5% | 1.5/3.1% | 3 |
| 2000 | 1 | 0.072 | 0.072 | 0.000 | - | - | 0.062 | 0.119 | 0.016 | 0.67x | 7.5/12.2/13.7% | 1.0/2.1% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 6

> noise-pulse-interval-ms=10000: decode_failures 14

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.248 | 0.248 | 0.000 | - | - | 0.133 | 0.266 | 0.000 | 1.21x | 7.2/16.4/20.1% | 1.6/5.0% | 2 |
| 1.0 | 1 | 0.541 | 0.541 | 0.000 | - | - | 0.475 | 0.559 | 0.317 | 1.00x | 11.3/14.9/18.3% | 1.4/4.1% | 2 |

> duct-per-hour=0.0: 3 archives requested, 2 placed - group on the placed count

> duct-per-hour=1.0: 3 archives requested, 2 placed - group on the placed count

> duct-per-hour=1.0: decode_failures 14

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 22 | 1 | 0.310 | 0.301 | 0.009 | - | - | 0.479 | 0.481 | 0.000 | 1.32x | 8.7/13.9/15.2% | 2.0/4.3% | 3 |
| 17 | 1 | 0.144 | 0.140 | 0.004 | - | - | 0.276 | 0.334 | 0.000 | 0.89x | 4.6/9.0/10.9% | 1.4/3.4% | 3 |
| 14 | 1 | 0.077 | 0.074 | 0.003 | - | - | 0.238 | 0.246 | 0.000 | 0.54x | 2.3/5.4/7.6% | 0.8/2.5% | 3 |

> tx-power=30: decode_failures 26

> tx-power=22: decode_failures 6

> tx-power=17: decode_failures 9

> tx-power=14: decode_failures 2

> slower: 4.07 s per simulated hour against 1.59 over 35 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.942 | 0.938 | 0.004 | - | - | 0.998 | 0.998 | 0.550 | 2.11x | 22.2/31.7/36.1% | 1.4/5.0% | 3 |
| True | 1 | 0.934 | 0.929 | 0.005 | - | - | 0.999 | 0.999 | 0.511 | 2.42x | 25.1/35.3/39.8% | 1.7/5.5% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.808 | 0.873 | 0.145 | 1.38x | 15.7/23.5/27.0% | 1.9/5.0% | 3 |
| True | 1 | 0.799 | 0.792 | 0.006 | - | - | 0.811 | 0.889 | 0.174 | 1.47x | 16.7/25.0/28.1% | 2.0/5.0% | 3 |

> favourite-routers=False: decode_failures 26

> favourite-routers=True: decode_failures 32

> slower: 7.64 s per simulated hour against 1.66 over 35 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| random | 1 | 0.710 | 0.703 | 0.006 | - | - | 0.672 | 0.783 | 0.168 | 1.18x | 13.3/19.8/23.3% | 1.7/4.6% | 3 |

> hop-assign=centrality: decode_failures 26

> hop-assign=random: decode_failures 16

> slower: 4.93 s per simulated hour against 1.88 over 35 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.573 | 0.546 | 0.027 | - | - | 0.639 | 0.758 | 0.118 | 0.90x | 10.6/17.2/20.5% | 1.2/3.9% | 3 |
| 7 | 1 | 0.838 | 0.835 | 0.003 | - | - | 0.857 | 0.923 | 0.189 | 1.40x | 15.6/22.1/25.7% | 2.0/5.1% | 3 |
| 15 | 1 | 0.865 | 0.863 | 0.002 | - | - | 0.872 | 0.936 | 0.215 | 1.43x | 15.8/22.5/26.3% | 2.1/5.2% | 3 |
| 32 | 1 | 0.868 | 0.866 | 0.001 | - | - | 0.848 | 0.928 | 0.203 | 1.42x | 15.7/22.4/26.0% | 2.0/5.1% | 3 |

> hop-limit=3: decode_failures 20

> hop-limit=7: decode_failures 22

> hop-limit=15: decode_failures 28

> hop-limit=32: decode_failures 30

> slower: 8.22 s per simulated hour against 1.76 over 35 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.573 | 0.546 | 0.027 | - | - | 0.639 | 0.758 | 0.118 | 0.90x | 10.6/17.2/20.5% | 1.2/3.9% | 3 |
| 5 | 1 | 0.765 | 0.757 | 0.008 | - | - | 0.824 | 0.885 | 0.157 | 1.26x | 14.2/20.8/24.6% | 1.8/5.0% | 3 |
| 7 | 1 | 0.838 | 0.835 | 0.003 | - | - | 0.857 | 0.923 | 0.189 | 1.40x | 15.6/22.1/25.7% | 2.0/5.1% | 3 |

> hop-limit=3: decode_failures 20

> hop-limit=5: decode_failures 36

> hop-limit=7: decode_failures 22

> slower: 8.4 s per simulated hour against 2.04 over 35 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| KNOWN_ONLY | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.755 | 0.755 | 0.000 | - | - | 0.626 | 0.863 | 0.200 | 1.23x | 13.7/20.5/23.9% | 1.8/4.7% | 3 |

> rebroadcast-mode=ALL: decode_failures 26

> rebroadcast-mode=KNOWN_ONLY: decode_failures 26

> slower: 3.5 s per simulated hour against 1.58 over 35 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.573 | 0.546 | 0.027 | - | - | 0.639 | 0.758 | 0.118 | 0.90x | 10.6/17.2/20.5% | 1.2/3.9% | 3 |
| True | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> hop-spread=False: decode_failures 20

> hop-spread=True: decode_failures 26

> slower: 7.37 s per simulated hour against 2.31 over 35 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| BALANCED | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| STRICT | 1 | 0.656 | 0.656 | 0.000 | - | - | 0.664 | 0.762 | 0.145 | 1.35x | 15.5/22.2/26.4% | 2.0/5.2% | 3 |

> signature-policy=COMPATIBLE: decode_failures 26

> signature-policy=BALANCED: decode_failures 26

> signature-policy=STRICT: decode_failures 18

> slower: 7.59 s per simulated hour against 1.8 over 35 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| dm | 1 | 0.767 | 0.757 | 0.011 | - | - | 0.867 | 0.873 | 0.187 | 1.25x | 14.2/20.7/24.6% | 1.8/5.1% | 3 |

> advert-transport=broadcast: decode_failures 26

> slower: 4.59 s per simulated hour against 1.72 over 35 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.762 | 0.753 | 0.010 | - | - | 0.797 | 0.867 | 0.204 | 1.29x | 14.6/21.4/25.0% | 1.9/5.0% | 3 |
| local | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| time | 1 | 0.757 | 0.747 | 0.010 | - | - | 0.806 | 0.868 | 0.181 | 1.30x | 14.7/21.4/25.2% | 1.9/5.2% | 3 |
| window | 1 | 0.757 | 0.750 | 0.006 | - | - | 0.702 | 0.860 | 0.206 | 1.25x | 14.1/20.9/24.3% | 1.8/4.8% | 3 |

> bucket-mode=global: misdecodes 13

> bucket-mode=local: decode_failures 26

> bucket-mode=time: misdecodes 21

> bucket-mode=time: decode_failures 15

> bucket-mode=window: misdecodes 1

> bucket-mode=window: decode_failures 20

> slower: 5.73 s per simulated hour against 1.56 over 35 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.755 | 0.745 | 0.010 | - | - | 0.804 | 0.860 | 0.182 | 1.38x | 15.6/22.5/27.1% | 1.9/5.6% | 3 |
| 1800 | 1 | 0.757 | 0.747 | 0.010 | - | - | 0.806 | 0.868 | 0.181 | 1.30x | 14.7/21.4/25.2% | 1.9/5.2% | 3 |
| 3600 | 1 | 0.760 | 0.752 | 0.008 | - | - | 0.810 | 0.864 | 0.178 | 1.26x | 14.3/20.8/24.4% | 1.8/4.9% | 3 |

> time-bucket-s=600: misdecodes 69

> time-bucket-s=1800: misdecodes 21

> time-bucket-s=1800: decode_failures 15

> time-bucket-s=3600: misdecodes 2

> time-bucket-s=3600: decode_failures 26

> slower: 4.5 s per simulated hour against 1.57 over 35 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| interval | 1 | 0.747 | 0.736 | 0.011 | - | - | 0.802 | 0.838 | 0.187 | 1.68x | 18.5/28.3/33.4% | 2.6/7.1% | 3 |
| aimd | 1 | 0.743 | 0.741 | 0.002 | - | - | 0.675 | 0.842 | 0.190 | 1.29x | 14.6/21.2/24.8% | 1.8/4.9% | 3 |
| bucket+interval | 1 | 0.744 | 0.731 | 0.013 | - | - | 0.821 | 0.834 | 0.205 | 1.69x | 18.9/28.6/33.4% | 2.6/7.2% | 3 |

> trigger=bucket: decode_failures 26

> trigger=interval: misdecodes 10

> trigger=interval: decode_failures 28

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 18

> trigger=bucket+interval: misdecodes 14

> trigger=bucket+interval: decode_failures 17

> slower: 8.22 s per simulated hour against 3.62 over 35 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.760 | 0.752 | 0.009 | - | - | 0.780 | 0.870 | 0.184 | 1.27x | 14.4/21.0/24.5% | 1.8/5.0% | 3 |
| 8 | 1 | 0.757 | 0.750 | 0.008 | - | - | 0.760 | 0.859 | 0.174 | 1.26x | 14.3/20.9/24.5% | 1.8/4.9% | 3 |
| 16 | 1 | 0.762 | 0.754 | 0.008 | - | - | 0.783 | 0.860 | 0.208 | 1.26x | 14.3/20.9/24.5% | 1.8/4.9% | 3 |
| 32 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 50 | 1 | 0.762 | 0.754 | 0.008 | - | - | 0.798 | 0.865 | 0.191 | 1.26x | 14.3/20.9/24.6% | 1.8/4.9% | 3 |

> capacity=4: decode_failures 49

> capacity=8: decode_failures 29

> capacity=16: decode_failures 32

> capacity=32: decode_failures 26

> capacity=50: decode_failures 18

> slower: 5.61 s per simulated hour against 1.7 over 35 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.760 | 0.752 | 0.009 | - | - | 0.780 | 0.870 | 0.184 | 1.27x | 14.4/21.0/24.5% | 1.8/5.0% | 3 |
| 8 | 1 | 0.757 | 0.750 | 0.008 | - | - | 0.760 | 0.859 | 0.174 | 1.26x | 14.3/20.9/24.5% | 1.8/4.9% | 3 |
| 16 | 1 | 0.762 | 0.754 | 0.008 | - | - | 0.783 | 0.860 | 0.208 | 1.26x | 14.3/20.9/24.5% | 1.8/4.9% | 3 |
| 32 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 50 | 1 | 0.762 | 0.754 | 0.008 | - | - | 0.798 | 0.865 | 0.191 | 1.26x | 14.3/20.9/24.6% | 1.8/4.9% | 3 |

> capacity=4: decode_failures 49

> capacity=8: decode_failures 29

> capacity=16: decode_failures 32

> capacity=32: decode_failures 26

> capacity=50: decode_failures 18

> slower: 5.62 s per simulated hour against 1.77 over 35 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.754 | 0.749 | 0.005 | - | - | 0.673 | 0.865 | 0.195 | 1.24x | 14.0/20.7/24.1% | 1.8/4.7% | 3 |
| 16 | 1 | 0.751 | 0.745 | 0.005 | - | - | 0.676 | 0.860 | 0.183 | 1.23x | 13.9/20.6/24.0% | 1.8/4.7% | 3 |
| 32 | 1 | 0.757 | 0.750 | 0.006 | - | - | 0.702 | 0.860 | 0.206 | 1.25x | 14.1/20.9/24.3% | 1.8/4.8% | 3 |

> capacity=8: misdecodes 3

> capacity=8: decode_failures 51

> capacity=16: misdecodes 1

> capacity=16: decode_failures 20

> capacity=32: misdecodes 1

> capacity=32: decode_failures 20

> slower: 3.8 s per simulated hour against 1.61 over 35 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.744 | 0.731 | 0.013 | - | - | 0.821 | 0.834 | 0.205 | 1.69x | 18.9/28.6/33.4% | 2.6/7.2% | 3 |
| 02-06 | 1 | 0.749 | 0.744 | 0.005 | - | - | 0.711 | 0.855 | 0.174 | 1.28x | 14.6/21.2/25.0% | 1.8/5.0% | 3 |
| 00-08 | 1 | 0.745 | 0.739 | 0.006 | - | - | 0.740 | 0.843 | 0.180 | 1.35x | 15.3/22.1/26.5% | 1.9/5.4% | 3 |

> catch-up-hours=: misdecodes 14

> catch-up-hours=: decode_failures 17

> catch-up-hours=02-06: decode_failures 43

> catch-up-hours=00-08: decode_failures 47

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.755 | 0.751 | 0.004 | - | - | 0.858 | 0.858 | 0.200 | 1.26x | 14.3/21.1/24.6% | 1.8/4.9% | 3 |
| 2 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 3 | 1 | 0.791 | 0.744 | 0.046 | - | - | 0.932 | 0.967 | 0.182 | 1.25x | 13.9/20.9/24.4% | 1.8/4.9% | 3 |
| 4 | 1 | 0.792 | 0.749 | 0.043 | - | - | 0.935 | 0.969 | 0.279 | 1.30x | 14.5/21.6/25.3% | 1.9/5.0% | 3 |

> hops-apart=2: decode_failures 26

> hops-apart=3: decode_failures 16

> hops-apart=4: decode_failures 25

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.755 | 0.751 | 0.004 | - | - | 0.858 | 0.858 | 0.200 | 1.26x | 14.3/21.1/24.6% | 1.8/4.9% | 3 |
| 2 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 3 | 1 | 0.791 | 0.744 | 0.046 | - | - | 0.932 | 0.967 | 0.182 | 1.25x | 13.9/20.9/24.4% | 1.8/4.9% | 3 |
| 4 | 1 | 0.792 | 0.749 | 0.043 | - | - | 0.935 | 0.969 | 0.279 | 1.30x | 14.5/21.6/25.3% | 1.9/5.0% | 3 |
| 5 | 1 | 0.803 | 0.753 | 0.050 | - | - | 0.896 | 0.964 | 0.194 | 1.27x | 14.2/21.4/24.8% | 1.8/5.0% | 3 |

> hops-apart=2: decode_failures 26

> hops-apart=3: decode_failures 16

> hops-apart=4: decode_failures 25

> hops-apart=5: decode_failures 20

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.766 | 0.758 | 0.008 | - | - | 0.781 | 0.881 | 0.188 | 1.25x | 14.3/20.7/24.3% | 1.8/4.8% | 3 |
| 30 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 120 | 1 | 0.755 | 0.747 | 0.009 | - | - | 0.779 | 0.847 | 0.192 | 1.26x | 14.3/20.8/24.4% | 1.8/4.9% | 3 |
| 600 | 1 | 0.762 | 0.753 | 0.008 | - | - | 0.764 | 0.858 | 0.183 | 1.27x | 14.4/21.0/24.6% | 1.8/4.9% | 3 |

> advert-jitter-s=1: decode_failures 18

> advert-jitter-s=30: decode_failures 26

> advert-jitter-s=120: decode_failures 19

> advert-jitter-s=600: decode_failures 24

> slower: 4.38 s per simulated hour against 1.77 over 35 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.766 | 0.758 | 0.008 | - | - | 0.781 | 0.881 | 0.188 | 1.25x | 14.3/20.7/24.3% | 1.8/4.8% | 3 |
| 30 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 120 | 1 | 0.755 | 0.747 | 0.009 | - | - | 0.779 | 0.847 | 0.192 | 1.26x | 14.3/20.8/24.4% | 1.8/4.9% | 3 |
| 600 | 1 | 0.762 | 0.753 | 0.008 | - | - | 0.764 | 0.858 | 0.183 | 1.27x | 14.4/21.0/24.6% | 1.8/4.9% | 3 |

> advert-jitter-s=1: decode_failures 18

> advert-jitter-s=30: decode_failures 26

> advert-jitter-s=120: decode_failures 19

> advert-jitter-s=600: decode_failures 24

> slower: 7.42 s per simulated hour against 1.8 over 35 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.800 | 0.742 | 0.058 | - | - | 0.859 | 0.971 | 0.187 | 1.29x | 14.6/21.7/25.1% | 1.8/5.2% | 3 |
| routers | 1 | 0.773 | 0.760 | 0.013 | - | - | 0.943 | 0.946 | 0.225 | 1.26x | 14.0/21.1/24.6% | 1.8/4.9% | 3 |
| alternate-routers | 1 | 0.756 | 0.744 | 0.012 | - | - | 0.933 | 0.934 | 0.196 | 1.26x | 14.0/21.2/24.9% | 1.8/4.8% | 3 |
| beside-router | 1 | 0.759 | 0.742 | 0.017 | - | - | 0.923 | 0.926 | 0.181 | 1.26x | 14.2/21.2/24.6% | 1.8/4.8% | 3 |
| random-clients | 1 | 0.773 | 0.748 | 0.025 | - | - | 0.933 | 0.935 | 0.186 | 1.28x | 14.3/21.7/25.2% | 1.9/4.9% | 3 |
| hops-apart | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> place=spread: decode_failures 36

> place=hops-apart: decode_failures 26

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.800 | 0.742 | 0.058 | - | - | 0.859 | 0.971 | 0.187 | 1.29x | 14.6/21.7/25.1% | 1.8/5.2% | 3 |
| routers | 1 | 0.773 | 0.760 | 0.013 | - | - | 0.943 | 0.946 | 0.225 | 1.26x | 14.0/21.1/24.6% | 1.8/4.9% | 3 |
| alternate-routers | 1 | 0.756 | 0.744 | 0.012 | - | - | 0.933 | 0.934 | 0.196 | 1.26x | 14.0/21.2/24.9% | 1.8/4.8% | 3 |
| beside-router | 1 | 0.759 | 0.742 | 0.017 | - | - | 0.923 | 0.926 | 0.181 | 1.26x | 14.2/21.2/24.6% | 1.8/4.8% | 3 |
| random-clients | 1 | 0.773 | 0.748 | 0.025 | - | - | 0.933 | 0.935 | 0.186 | 1.28x | 14.3/21.7/25.2% | 1.9/4.9% | 3 |
| hops-apart | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> place=spread: decode_failures 36

> place=hops-apart: decode_failures 26

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| broadcast | 1 | 0.790 | 0.742 | 0.049 | - | - | 0.720 | 0.845 | 0.228 | 1.38x | 15.6/22.9/26.9% | 2.0/5.3% | 3 |

> provide-transport=dm: decode_failures 26

> provide-transport=broadcast: decode_failures 24

> slower: 8.1 s per simulated hour against 1.79 over 35 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| heard | 1 | 0.764 | 0.756 | 0.008 | - | - | 0.788 | 0.860 | 0.196 | 1.28x | 14.5/21.2/24.8% | 1.9/4.9% | 3 |

> replay-ordering=tip: decode_failures 26

> replay-ordering=heard: misdecodes 8

> replay-ordering=heard: decode_failures 20

> slower: 7.5 s per simulated hour against 1.69 over 35 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.790 | 0.742 | 0.049 | - | - | 0.720 | 0.845 | 0.228 | 1.38x | 15.6/22.9/26.9% | 2.0/5.3% | 3 |
| heard | 1 | 0.791 | 0.736 | 0.055 | - | - | 0.718 | 0.843 | 0.229 | 1.40x | 15.7/23.1/27.1% | 2.0/5.3% | 3 |

> replay-ordering=tip: decode_failures 24

> replay-ordering=heard: misdecodes 1

> replay-ordering=heard: decode_failures 23

> slower: 4.73 s per simulated hour against 1.77 over 35 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.761 | 0.755 | 0.006 | - | - | 0.685 | 0.871 | 0.177 | 1.26x | 14.3/21.1/24.6% | 1.8/4.9% | 3 |
| enum | 1 | 0.762 | 0.754 | 0.009 | - | - | 0.762 | 0.860 | 0.189 | 1.26x | 14.3/20.9/24.6% | 1.8/5.0% | 3 |
| hybrid | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> resolve=sketch: decode_failures 12

> resolve=hybrid: decode_failures 26

> slower: 4.59 s per simulated hour against 1.55 over 35 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.773 | 0.760 | 0.013 | - | - | 0.943 | 0.946 | 0.225 | 1.26x | 14.0/21.1/24.6% | 1.8/4.9% | 3 |
| 6 | 1 | 0.762 | 0.737 | 0.025 | - | - | 0.926 | 0.927 | 0.187 | 1.27x | 14.3/21.5/25.2% | 1.8/5.0% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.757 | 0.752 | 0.005 | - | - | 0.862 | 0.863 | 0.211 | 1.24x | 14.1/20.9/24.3% | 1.8/4.8% | 2 |
| 3 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 5 | 1 | 0.760 | 0.747 | 0.013 | - | - | 0.869 | 0.884 | 0.200 | 1.31x | 14.8/21.7/25.6% | 1.9/5.2% | 5 |
| 8 | 1 | 0.769 | 0.743 | 0.026 | - | - | 0.927 | 0.937 | 0.191 | 1.33x | 15.0/22.1/26.6% | 1.9/5.3% | 8 |

> servers=3: decode_failures 26

> servers=5: decode_failures 47

> servers=8: decode_failures 91

> slower: 13.7 s per simulated hour against 2.56 over 35 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.757 | 0.752 | 0.005 | - | - | 0.862 | 0.863 | 0.211 | 1.24x | 14.1/20.9/24.3% | 1.8/4.8% | 2 |
| 3 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 5 | 1 | 0.760 | 0.747 | 0.013 | - | - | 0.869 | 0.884 | 0.200 | 1.31x | 14.8/21.7/25.6% | 1.9/5.2% | 5 |
| 8 | 1 | 0.769 | 0.743 | 0.026 | - | - | 0.927 | 0.937 | 0.191 | 1.33x | 15.0/22.1/26.6% | 1.9/5.3% | 8 |

> servers=3: decode_failures 26

> servers=5: decode_failures 47

> servers=8: decode_failures 91

> slower: 13.8 s per simulated hour against 2.35 over 35 prior run(s) - 5.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| True | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |

> signed=False: decode_failures 26

> signed=True: decode_failures 26

> slower: 8.12 s per simulated hour against 1.74 over 35 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.762 | 0.753 | 0.009 | - | - | 0.739 | 0.871 | 0.176 | 1.17x | 13.5/19.5/22.8% | 1.7/4.5% | 3 |
| 1 | 1 | 0.761 | 0.752 | 0.009 | - | - | 0.784 | 0.857 | 0.216 | 1.16x | 13.4/19.5/22.8% | 1.7/4.5% | 3 |
| 2 | 1 | 0.752 | 0.745 | 0.007 | - | - | 0.765 | 0.833 | 0.210 | 1.16x | 13.3/19.4/22.6% | 1.7/4.4% | 3 |
| 4 | 1 | 0.758 | 0.750 | 0.008 | - | - | 0.769 | 0.854 | 0.213 | 1.17x | 13.4/19.5/22.8% | 1.7/4.4% | 3 |

> sr-retries=0: decode_failures 13

> sr-retries=1: decode_failures 12

> sr-retries=2: decode_failures 14

> sr-retries=4: decode_failures 9

> slower: 4.7 s per simulated hour against 1.58 over 35 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.776 | 0.868 | 0.191 | 1.26x | 14.3/20.8/24.4% | 1.8/4.9% | 3 |
| 24 | 1 | 0.756 | 0.747 | 0.008 | - | - | 0.766 | 0.856 | 0.190 | 1.26x | 14.2/20.9/24.3% | 1.8/4.9% | 3 |
| 32 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.791 | 0.864 | 0.204 | 1.27x | 14.4/21.0/24.7% | 1.8/5.0% | 3 |
| 64 | 1 | 0.752 | 0.744 | 0.008 | - | - | 0.775 | 0.849 | 0.194 | 1.27x | 14.5/21.1/24.7% | 1.8/4.9% | 3 |

> short-id-bits=16: decode_failures 32

> short-id-bits=24: decode_failures 19

> short-id-bits=32: decode_failures 26

> short-id-bits=64: decode_failures 28

> slower: 8.54 s per simulated hour against 1.68 over 35 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.762 | 0.752 | 0.010 | - | - | 0.795 | 0.866 | 0.183 | 1.31x | 14.9/21.7/25.4% | 1.9/5.1% | 3 |
| 16 | 1 | 0.761 | 0.751 | 0.011 | - | - | 0.791 | 0.872 | 0.179 | 1.29x | 14.8/21.5/25.2% | 1.8/5.1% | 3 |
| 32 | 1 | 0.757 | 0.750 | 0.006 | - | - | 0.702 | 0.860 | 0.206 | 1.25x | 14.1/20.9/24.3% | 1.8/4.8% | 3 |

> window-size=8: misdecodes 32

> window-size=16: misdecodes 9

> window-size=32: misdecodes 1

> window-size=32: decode_failures 20

> slower: 3.61 s per simulated hour against 1.43 over 35 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.942 | 0.938 | 0.004 | - | - | 0.998 | 0.998 | 0.550 | 2.11x | 22.2/31.7/36.1% | 1.4/5.0% | 3 |
| True | 1 | 0.725 | 0.708 | 0.017 | - | - | 0.866 | 0.938 | 0.390 | 5.97x | 56.9/71.0/76.6% | 4.1/12.3% | 3 |

> no-congestion-scaling=True: decode_failures 98

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.527 | 0.518 | 0.009 | - | - | 0.851 | 0.851 | 0.213 | 4.74x | 15.2/34.8/46.9% | 1.5/5.8% | 3 |
| truesize | 1 | 0.563 | 0.555 | 0.009 | - | - | 0.887 | 0.888 | 0.225 | 3.53x | 10.9/27.4/37.4% | 1.1/4.7% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.945 | 0.942 | 0.003 | - | - | 0.999 | 1.000 | 0.560 | 1.98x | 20.6/29.9/34.0% | 1.4/4.7% | 3 |
| adaptive | 1 | 0.942 | 0.938 | 0.004 | - | - | 0.998 | 0.998 | 0.550 | 2.11x | 22.2/31.7/36.1% | 1.4/5.0% | 3 |

