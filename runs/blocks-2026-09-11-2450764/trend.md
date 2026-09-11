# Sweep blocks-2026-09-11-2450764

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 2450764 · seeds 2450764
- **blocks** 87 run
- **compute** 16.8 h of simulator time across every cell
- **generated** 2026-09-11T08:57:15+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>250 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 3
- AD-amplify-worst: amplify-worst=0.0: decode_failures 3
- AD-badrouters: role-placement=degree: decode_failures 2
- AD-badrouters: role-placement=inverse: decode_failures 22
- AD-badrouters: role-placement=random: decode_failures 1
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 2
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 2
- AD-siting: siting-mix=uniform: decode_failures 2
- AD-siting: siting-mix=basement-heavy: decode_failures 1
- DB-hotstore: max-num-nodes=10: decode_failures 7
- DB-hotstore: max-num-nodes=100: decode_failures 47
- DB-hotstore: max-num-nodes=120: decode_failures 47
- DB-hotstore: max-num-nodes=250: decode_failures 47
- DB-hotstore: slower: 12 s per simulated hour against 2.54 over 21 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 26
- DB-hotstore-stress: max-num-nodes=120: decode_failures 1
- DB-hotstore-stress: max-num-nodes=250: decode_failures 4
- DB-platform: platform-mix=uniform: decode_failures 47
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 47
- DB-platform: platform-mix=constrained: decode_failures 17
- DB-platform: slower: 13.3 s per simulated hour against 2.6 over 21 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: decode_failures 89
- DB-warm: warm-num-nodes=25: decode_failures 89
- DB-warm: warm-num-nodes=100: decode_failures 89
- DB-warm: warm-num-nodes=2000: decode_failures 89
- DG-burst: burst-loss=0.0: decode_failures 3
- DG-burst: burst-loss=0.1: decode_failures 15
- DG-burst: burst-loss=0.2: decode_failures 26
- DG-burst: burst-loss=0.3: decode_failures 22
- DG-loss: extra-loss=0.0: decode_failures 3
- DG-loss: extra-loss=0.1: decode_failures 30
- DG-loss: extra-loss=0.2: decode_failures 21
- DG-loss: extra-loss=0.3: decode_failures 24
- DG-loss: slower: 7.51 s per simulated hour against 2.22 over 21 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 3
- DG-outage: burst-loss=0.1: decode_failures 33
- DG-outage: burst-loss=0.2: decode_failures 20
- DG-outage: burst-loss=0.3: decode_failures 17
- DM-mode: dm-mode=flood-only: decode_failures 27
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 33
- DM-mode: dm-mode=m4-early-flood: decode_failures 33
- DM-mode: slower: 9 s per simulated hour against 3.06 over 21 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 3
- FW-mixed-26: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.5: decode_failures 54
- FW-mixed: slower: 5.9 s per simulated hour against 1.67 over 21 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-signing-cost: profile-flag=signing=false: decode_failures 3
- FW-signing-cost: profile-flag=signing=true: decode_failures 3
- FW-versions: profile=2.8: decode_failures 3
- LD-chatty-hops: broadcast-interval-s=3600: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 23
- LD-chatty: broadcast-interval-s=3600: decode_failures 5
- LD-chatty: broadcast-interval-s=900: decode_failures 25
- LD-chatty: broadcast-interval-s=300: decode_failures 18
- LD-diurnal: diurnal=flat: decode_failures 35
- LD-diurnal: diurnal=sinusoid: decode_failures 18
- LD-diurnal: diurnal=commuter: decode_failures 3
- LD-diurnal: slower: 6.33 s per simulated hour against 1.58 over 21 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 25
- LD-interval: broadcast-interval-s=3600: decode_failures 5
- LD-interval: broadcast-interval-s=43200: decode_failures 31
- LD-interval: slower: 6.18 s per simulated hour against 1.4 over 21 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 3
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 31
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 20
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 8
- LD-traceroute: slower: 7.37 s per simulated hour against 2.1 over 21 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 89
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 12.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 92
- MS-density: nodes=60: decode_failures 3
- MS-density: nodes=120: misdecodes 1
- MS-hopscale: nodes=60: decode_failures 3
- MS-hopscale: nodes=250: decode_failures 10
- MS-hopscale: nodes=500: decode_failures 213
- MS-oversubscribed: nodes=250: decode_failures 1
- MS-oversubscribed: nodes=500: decode_failures 182
- MS-roles-fav: role-mix=legacy-default: decode_failures 2
- MS-roles: role-mix=legacy-default: decode_failures 11
- MS-roles: role-mix=baymesh-2026-08: decode_failures 2
- MS-roles: slower: 3.89 s per simulated hour against 1.86 over 21 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 3
- MS-router-late: router-late-fraction=0.05: decode_failures 1
- MS-router-late: router-late-fraction=0.1: decode_failures 18
- MS-router-late: router-late-fraction=0.2: decode_failures 37
- MS-router-late: slower: 5.46 s per simulated hour against 1.76 over 21 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=uniform: decode_failures 3
- MS-size: nodes=60: decode_failures 3
- MS-stretch: stretch=1.0: decode_failures 3
- MS-stretch: stretch=1.5: decode_failures 1
- MS-topology: topology=uniform: decode_failures 3
- MS-topology: topology=corridor: decode_failures 28
- MS-topology: slower: 4.11 s per simulated hour against 1.86 over 21 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-crladder: coding-rate-ladder=False: decode_failures 33
- PR-crladder: coding-rate-ladder=True: decode_failures 33
- PR-crladder: slower: 11 s per simulated hour against 2.79 over 21 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 33
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 30
- PR-dmmode-cr: slower: 10.4 s per simulated hour against 2.54 over 21 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 3
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- PR-repeats-busy: extra-repeats=True: misdecodes 1
- PR-repeats: extra-repeats=False: decode_failures 3
- PR-repeats: extra-repeats=True: decode_failures 26
- PR-repeats: slower: 6.84 s per simulated hour against 1.68 over 21 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=SHORT_TURBO: decode_failures 5
- RF-duct: duct-per-hour=0.0: decode_failures 3
- RF-duct: duct-per-hour=0.25: decode_failures 13
- RF-duct: slower: 4.08 s per simulated hour against 1.76 over 21 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=SHORT_FAST: decode_failures 11
- RF-eu-presets: preset=LONG_FAST: decode_failures 3
- RF-noise: noise-profile=none: decode_failures 3
- RF-noise: noise-profile=temporal: decode_failures 17
- RF-noise: noise-profile=transient: decode_failures 26
- RF-noise: noise-profile=periodic: decode_failures 18
- RF-preset: preset=SHORT_FAST: decode_failures 11
- RF-preset: preset=LONG_FAST: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 5
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 5
- RF-preset-turbo: preset=LONG_FAST: decode_failures 3
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 26
- RF-preset-turbo: slower: 3.34 s per simulated hour against 1.59 over 17 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 10
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 18
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-pulse: slower: 3.52 s per simulated hour against 1.6 over 21 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 1
- RF-txpower: tx-power=30: decode_failures 3
- RF-txpower: tx-power=22: decode_failures 2
- RF-txpower: tx-power=17: decode_failures 4
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-adopt: no-adopt-hop-recommendation=True: misdecodes 1
- RT-favourites: favourite-routers=True: decode_failures 1
- RT-hopassign: hop-assign=centrality: decode_failures 3
- RT-hopassign: hop-assign=random: decode_failures 19
- RT-hopassign: slower: 4.48 s per simulated hour against 1.85 over 21 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hoplimit: hop-limit=3: decode_failures 26
- RT-hoplimit: hop-limit=7: decode_failures 2
- RT-hopspread: hop-limit=3: decode_failures 26
- RT-hopspread: hop-limit=5: decode_failures 11
- RT-hopspread: hop-limit=7: decode_failures 2
- RT-hopspread: slower: 4.72 s per simulated hour against 2.03 over 21 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 3
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 26
- RT-spread: hop-spread=True: decode_failures 3
- RT-spread: slower: 6 s per simulated hour against 2.15 over 21 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 3
- SC-signing: signature-policy=BALANCED: decode_failures 3
- SC-signing: signature-policy=STRICT: decode_failures 28
- SC-signing: slower: 5.63 s per simulated hour against 1.87 over 21 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 3
- SF-bucket-mode: bucket-mode=global: misdecodes 14
- SF-bucket-mode: bucket-mode=local: decode_failures 3
- SF-bucket-mode: bucket-mode=time: misdecodes 8
- SF-bucket-mode: bucket-mode=time: decode_failures 1
- SF-bucket-mode: bucket-mode=window: misdecodes 3
- SF-bucket-mode: bucket-mode=window: decode_failures 4
- SF-bucket-time: time-bucket-s=600: misdecodes 70
- SF-bucket-time: time-bucket-s=1800: misdecodes 8
- SF-bucket-time: time-bucket-s=1800: decode_failures 1
- SF-bucket-time: time-bucket-s=3600: misdecodes 3
- SF-bucket-time: time-bucket-s=3600: decode_failures 18
- SF-bucket-time: slower: 4.34 s per simulated hour against 1.62 over 21 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-cadence: trigger=bucket: decode_failures 3
- SF-cadence: trigger=interval: misdecodes 8
- SF-cadence: trigger=interval: decode_failures 9
- SF-cadence: trigger=aimd: decode_failures 31
- SF-cadence: trigger=bucket+interval: misdecodes 7
- SF-cadence: trigger=bucket+interval: decode_failures 1
- SF-cadence: slower: 9.45 s per simulated hour against 3.62 over 21 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 63
- SF-capacity-local: capacity=8: decode_failures 64
- SF-capacity-local: capacity=16: decode_failures 46
- SF-capacity-local: capacity=32: decode_failures 3
- SF-capacity: capacity=4: decode_failures 63
- SF-capacity: capacity=8: decode_failures 64
- SF-capacity: capacity=16: decode_failures 46
- SF-capacity: capacity=32: decode_failures 3
- SF-capacity-window: capacity=8: decode_failures 111
- SF-capacity-window: capacity=16: misdecodes 1
- SF-capacity-window: capacity=16: decode_failures 69
- SF-capacity-window: capacity=32: misdecodes 3
- SF-capacity-window: capacity=32: decode_failures 4
- SF-capacity-window: slower: 4.3 s per simulated hour against 1.73 over 21 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 7
- SF-catchup: catch-up-hours=: decode_failures 1
- SF-catchup: catch-up-hours=02-06: decode_failures 48
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 45
- SF-hops-flat: hops-apart=2: decode_failures 3
- SF-hops-flat: hops-apart=4: decode_failures 24
- SF-hops-spread: hops-apart=2: decode_failures 3
- SF-hops-spread: hops-apart=4: decode_failures 24
- SF-hops-spread: hops-apart=5: decode_failures 36
- SF-jitter-global: advert-jitter-s=1: decode_failures 21
- SF-jitter-global: advert-jitter-s=30: decode_failures 3
- SF-jitter-global: advert-jitter-s=120: decode_failures 3
- SF-jitter-global: advert-jitter-s=600: decode_failures 4
- SF-jitter-global: slower: 5 s per simulated hour against 1.79 over 21 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 21
- SF-jitter-local: advert-jitter-s=30: decode_failures 3
- SF-jitter-local: advert-jitter-s=120: decode_failures 3
- SF-jitter-local: advert-jitter-s=600: decode_failures 4
- SF-jitter-local: slower: 4.88 s per simulated hour against 1.88 over 21 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 20
- SF-place-flat: place=random-clients: decode_failures 7
- SF-place-flat: place=hops-apart: decode_failures 3
- SF-place-spread: place=spread: decode_failures 20
- SF-place-spread: place=random-clients: decode_failures 7
- SF-place-spread: place=hops-apart: decode_failures 3
- SF-provide-transport: provide-transport=dm: decode_failures 3
- SF-provide-transport: provide-transport=broadcast: decode_failures 45
- SF-provide-transport: slower: 9.29 s per simulated hour against 1.91 over 21 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 45
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 21
- SF-replay-order-broadcast: slower: 9.92 s per simulated hour against 1.77 over 21 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 3
- SF-replay-order: replay-ordering=heard: decode_failures 29
- SF-replay-order: slower: 6.9 s per simulated hour against 1.69 over 21 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-resolve: resolve=sketch: decode_failures 30
- SF-resolve: resolve=hybrid: decode_failures 3
- SF-resolve: slower: 5.03 s per simulated hour against 1.53 over 21 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=2: decode_failures 23
- SF-servers-flat: servers=3: decode_failures 3
- SF-servers-spread: servers=2: decode_failures 23
- SF-servers-spread: servers=3: decode_failures 3
- SF-servers-spread: slower: 4.73 s per simulated hour against 2.29 over 21 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 3
- SF-signed: signed=True: decode_failures 3
- SF-signed: slower: 3.86 s per simulated hour against 1.74 over 21 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 10
- SF-sr-retries: sr-retries=1: decode_failures 15
- SF-sr-retries: sr-retries=2: decode_failures 3
- SF-sr-retries: sr-retries=4: decode_failures 3
- SF-sr-retries: slower: 5.34 s per simulated hour against 1.64 over 21 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 40
- SF-width: short-id-bits=24: decode_failures 19
- SF-width: short-id-bits=32: decode_failures 3
- SF-width: short-id-bits=64: decode_failures 2
- SF-width: slower: 4.2 s per simulated hour against 1.75 over 21 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 91
- SF-window-size: window-size=16: misdecodes 19
- SF-window-size: window-size=32: misdecodes 3
- SF-window-size: window-size=32: decode_failures 4
- TH-congestion-input: congestion-input=hotstore: decode_failures 1
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: decode_failures 82

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-replay-order-broadcast` | 9.92 | 1.77 | 5.59x | 21 |
| `DB-platform` | 13.3 | 2.6 | 5.13x | 21 |
| `SF-provide-transport` | 9.29 | 1.91 | 4.86x | 21 |
| `DB-hotstore` | 12 | 2.54 | 4.73x | 21 |
| `LD-interval` | 6.18 | 1.4 | 4.40x | 21 |
| `PR-dmmode-cr` | 10.4 | 2.54 | 4.09x | 21 |
| `PR-repeats` | 6.84 | 1.68 | 4.08x | 21 |
| `SF-replay-order` | 6.9 | 1.69 | 4.08x | 21 |
| `LD-diurnal` | 6.33 | 1.58 | 4.00x | 21 |
| `PR-crladder` | 11 | 2.79 | 3.94x | 21 |
| `FW-mixed` | 5.9 | 1.67 | 3.52x | 21 |
| `LD-traceroute` | 7.37 | 2.1 | 3.51x | 21 |
| `DG-loss` | 7.51 | 2.22 | 3.38x | 21 |
| `SF-resolve` | 5.03 | 1.53 | 3.28x | 21 |
| `SF-sr-retries` | 5.34 | 1.64 | 3.26x | 21 |
| `MS-router-late` | 5.46 | 1.76 | 3.11x | 21 |
| `SC-signing` | 5.63 | 1.87 | 3.01x | 21 |
| `DM-mode` | 9 | 3.06 | 2.94x | 21 |
| `RT-spread` | 6 | 2.15 | 2.80x | 21 |
| `SF-jitter-global` | 5 | 1.79 | 2.79x | 21 |
| `SF-bucket-time` | 4.34 | 1.62 | 2.67x | 21 |
| `SF-cadence` | 9.45 | 3.62 | 2.61x | 21 |
| `SF-jitter-local` | 4.88 | 1.88 | 2.59x | 21 |
| `SF-capacity-window` | 4.3 | 1.73 | 2.49x | 21 |
| `RT-hopassign` | 4.48 | 1.85 | 2.42x | 21 |
| `SF-width` | 4.2 | 1.75 | 2.40x | 21 |
| `RT-hopspread` | 4.72 | 2.03 | 2.33x | 21 |
| `RF-duct` | 4.08 | 1.76 | 2.32x | 21 |
| `SF-signed` | 3.86 | 1.74 | 2.22x | 21 |
| `MS-topology` | 4.11 | 1.86 | 2.21x | 21 |
| `RF-pulse` | 3.52 | 1.6 | 2.19x | 21 |
| `RF-preset-turbo` | 3.34 | 1.59 | 2.10x | 17 |
| `MS-roles` | 3.89 | 1.86 | 2.10x | 21 |
| `SF-servers-spread` | 4.73 | 2.29 | 2.07x | 21 |
| `SF-capacity` | 3.33 | 1.7 | 1.95x | 21 |
| `SF-bucket-mode` | 3.07 | 1.63 | 1.89x | 21 |
| `SF-capacity-local` | 3.33 | 1.81 | 1.84x | 21 |
| `AD-badrouters` | 3.84 | 2.1 | 1.83x | 21 |
| `SF-servers-flat` | 4.67 | 2.56 | 1.82x | 21 |
| `FW-signing-cost` | 2.83 | 1.61 | 1.76x | 21 |
| `LD-chatty` | 7.78 | 4.78 | 1.63x | 21 |
| `RF-noise` | 7.86 | 4.91 | 1.60x | 21 |
| `FW-firmware` | 2.76 | 1.74 | 1.58x | 21 |
| `SF-window-size` | 2.26 | 1.44 | 1.57x | 21 |
| `RT-hoplimit` | 2.84 | 1.82 | 1.56x | 21 |
| `RT-favourites` | 2.61 | 1.69 | 1.54x | 21 |
| `RT-rebroadcast` | 2.42 | 1.59 | 1.52x | 21 |
| `RF-stretch-duct` | 1.64 | 2.97 | 0.55x | 21 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.953 | 0.953 | 0.803 → 0.807 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **held** | 0.056 → 0.997 | 0.941 | 0.060 → 0.963 | 28x sr_airtime | up | 4 |
| `PR-protocol` | protocol | **held** | 0 → 0.923 | 0.923 | 0.768 → 0.807 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.065 → 0.923 | 0.858 | 0.054 → 0.795 | 16x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.066 → 0.923 | 0.857 | 0.075 → 0.795 | 23x sr_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.067 → 0.923 | 0.856 | 0.038 → 0.795 | 19x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.068 → 0.843 | 0.775 | 0.076 → 0.738 | 3.1e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.173 → 0.884 | 0.711 | 0.043 → 0.735 | 5.5x sr_bytes | down | 3 |
| `RF-bw500` | preset | **held** | 0.219 → 0.887 | 0.668 | 0.109 → 0.714 | 4.1x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.244 → 0.806 | 0.563 | 0.241 → 0.795 | 3.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.244 → 0.806 | 0.563 | 0.241 → 0.795 | 3.8x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.418 → 0.952 | 0.534 | 0.410 → 0.951 | 3.5x sr_bytes | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.329 → 0.806 | 0.477 | 0.321 → 0.795 | 9.5x sr_bytes | down | 4 |
| `DG-outage` | burst-loss | **held** | 0.496 → 0.923 | 0.427 | 0.441 → 0.795 | 2x sr_airtime | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.330 → 0.748 | 0.418 | 0.320 → 0.732 | 7.2x sr_bytes | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.239 → 0.611 | 0.372 | 0.231 → 0.601 | 2.4x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.587 → 0.944 | 0.357 | 0.485 → 0.834 | 12x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **held** | 0.588 → 0.923 | 0.335 | 0.477 → 0.795 | 1.6x advert_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.600 → 0.898 | 0.298 | 0.590 → 0.894 | 9.8x sr_airtime | down | 3 |
| `RF-noise` | noise-profile | **held** | 0.638 → 0.923 | 0.285 | 0.620 → 0.795 | 1.9x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.669 → 0.952 | 0.282 | 0.651 → 0.950 | 4.6x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.639 → 0.901 | 0.262 | 0.622 → 0.898 | 1.7x sr_bytes | up | 4 |
| `SF-place-flat` | place | **held** | 0.708 → 0.964 | 0.255 | 0.789 → 0.811 | 2x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.708 → 0.964 | 0.255 | 0.789 → 0.811 | 2x sr_bytes | up | 6 |
| `RT-hopspread` | hop-limit | **text** | 0.639 → 0.881 | 0.242 | 0.622 → 0.877 | 1.6x sr_bytes | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.695 → 0.923 | 0.228 | 0.795 → 0.802 | 37x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **held** | 0.713 → 0.933 | 0.221 | 0.683 → 0.761 | 1.3x advert_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.736 → 0.946 | 0.210 | 0.724 → 0.943 | 3.6x sr_airtime | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.714 → 0.916 | 0.201 | 0.792 → 0.807 | 11x sr_bytes | up | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.371 → 0.570 | 0.199 | 0.297 → 0.467 | 5x sr_airtime | up | 3 |
| `RT-spread` | hop-spread | **held** | 0.727 → 0.923 | 0.196 | 0.622 → 0.795 | 1.5x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **held** | 0.729 → 0.923 | 0.194 | 0.656 → 0.795 | 1.3x advert_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.770 → 0.953 | 0.183 | 0.795 → 0.803 | 3.3x sr_bytes | down | 5 |
| `SC-signing` | signature-policy | **held** | 0.755 → 0.923 | 0.168 | 0.705 → 0.795 | 1.4x sr_airtime | down | 3 |
| `MS-size` | nodes | **text** | 0.656 → 0.813 | 0.157 | 0.642 → 0.808 | 7.2x sr_bytes | down | 5 |
| `AD-flooding` | role-mix | **text** | 0.749 → 0.899 | 0.150 | 0.735 → 0.890 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.749 → 0.899 | 0.150 | 0.735 → 0.890 | 2.3x bytes_on_air | up | 3 |
| `SF-cadence` | trigger | **held** | 0.781 → 0.923 | 0.142 | 0.764 → 0.795 | 15x advert_bytes | down | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.806 → 0.938 | 0.132 | 0.795 → 0.932 | 3x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.749 → 0.874 | 0.125 | 0.737 → 0.866 | 5.7x sr_airtime | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.751 → 0.870 | 0.119 | 0.736 → 0.860 | 2.4x sr_airtime | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.815 → 0.933 | 0.118 | 0.789 → 0.803 | 4.6x advert_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.815 → 0.933 | 0.118 | 0.789 → 0.803 | 4.6x advert_bytes | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.806 → 0.919 | 0.113 | 0.795 → 0.913 | 2.2x sr_bytes | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.763 → 0.870 | 0.107 | 0.750 → 0.860 | 2.4x sr_airtime | down | 3 |
| `RT-hopassign` | hop-assign | **held** | 0.822 → 0.923 | 0.100 | 0.736 → 0.795 | 1.1x advert_bytes | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.806 → 0.899 | 0.093 | 0.795 → 0.891 | 1.5x sr_bytes | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.665 → 0.748 | 0.083 | 0.656 → 0.737 | 1.3x sr_airtime | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.859 → 0.939 | 0.080 | 0.795 → 0.817 | 1.2x sr_bytes | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.884 → 0.953 | 0.069 | 0.795 → 0.803 | 3.3x sr_bytes | down | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.839 → 0.904 | 0.065 | 0.770 → 0.804 | 8.8x advert_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.861 → 0.923 | 0.061 | 0.795 → 0.805 | 5.9x advert_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.923 → 0.982 | 0.060 | 0.795 → 0.840 | 2x bytes_on_air | up | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.806 → 0.859 | 0.052 | 0.795 → 0.850 | 1.4x bytes_on_air | up | 4 |
| `FW-firmware` | profile | **held** | 0.923 → 0.973 | 0.050 | 0.795 → 0.829 | 3.2x bytes_on_air | down | 2 |
| `MS-roles` | role-mix | **text** | 0.749 → 0.798 | 0.049 | 0.735 → 0.791 | 1.1x bytes_on_air | down | 2 |
| `SF-capacity` | capacity | **held** | 0.873 → 0.923 | 0.049 | 0.794 → 0.802 | 5.5x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.873 → 0.923 | 0.049 | 0.794 → 0.802 | 5.5x advert_bytes | up | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.774 → 0.823 | 0.049 | 0.766 → 0.813 | 1.5x sr_bytes | down | 2 |
| `SF-width` | short-id-bits | **held** | 0.893 → 0.941 | 0.048 | 0.795 → 0.805 | 3.3x advert_bytes | up | 4 |
| `FW-versions` | profile | **held** | 0.923 → 0.968 | 0.045 | 0.795 → 0.831 | 3.2x bytes_on_air | down | 5 |
| `SF-provide-transport` | provide-transport | **held** | 0.879 → 0.923 | 0.043 | 0.795 → 0.795 | 3.9x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.806 → 0.850 | 0.043 | 0.795 → 0.841 | 3.3x bytes_on_air | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.765 → 0.806 | 0.042 | 0.750 → 0.795 | 1.5x sr_airtime | down | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.923 → 0.964 | 0.041 | 0.795 → 0.831 | 2.1x sr_bytes | up | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.553 → 0.592 | 0.039 | 0.464 → 0.491 | 1.6x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.889 → 0.927 | 0.038 | 0.782 → 0.806 | 1.2x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.889 → 0.927 | 0.038 | 0.782 → 0.806 | 1.2x sr_airtime | up | 4 |
| `DM-mode` | dm-mode | **held** | 0.737 → 0.775 | 0.037 | 0.760 → 0.788 | 1.8x sr_airtime | down | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.891 → 0.923 | 0.032 | 0.795 → 0.804 | 1x advert_bytes | down | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.897 → 0.924 | 0.028 | 0.787 → 0.804 | 5.3x advert_bytes | down | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.895 → 0.923 | 0.027 | 0.790 → 0.795 | 1.1x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.806 → 0.831 | 0.025 | 0.795 → 0.822 | 1.2x sr_bytes | down | 3 |
| `SF-window-size` | window-size | **held** | 0.900 → 0.922 | 0.022 | 0.794 → 0.806 | 4.4x advert_bytes | down | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.846 → 0.865 | 0.019 | 0.834 → 0.856 | 1.1x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.732 → 0.747 | 0.015 | 0.776 → 0.781 | 1.2x sr_bytes | down | 2 |
| `AD-worst` | role-placement | **text** | 0.822 → 0.837 | 0.014 | 0.814 → 0.831 | 1.1x sr_bytes | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.867 → 0.879 | 0.013 | 0.777 → 0.795 | 1.1x sr_bytes | down | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.805 → 0.818 | 0.013 | 0.794 → 0.806 | 2.8x advert_bytes | up | 4 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.737 → 0.747 | 0.010 | 0.776 → 0.781 | 1.3x sr_airtime | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.923 → 0.930 | 0.007 | 0.795 → 0.800 | 2x advert_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.940 → 0.946 | 0.007 | 0.936 → 0.943 | 1.2x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.946 → 0.953 | 0.006 | 0.943 → 0.951 | 1.1x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.795 → 0.797 | 0.003 | 0.787 → 0.789 | 2.2x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.946 → 0.947 | 0.001 | 0.943 → 0.945 | 1x sr_bytes | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario valleys`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| sprinkled | 1 | 0.902 | 0.899 | 0.003 | - | - | 0.952 | 0.952 | 0.613 | 1.26x | 16.9/24.7/26.2% | 1.9/5.1% | 3 |
| arms-race | 1 | 0.938 | 0.932 | 0.006 | - | - | 0.984 | 0.984 | 0.785 | 1.15x | 20.7/28.0/30.3% | 1.5/5.2% | 3 |

> amplifier-mix=none: decode_failures 3

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.848 | 0.836 | 0.012 | - | - | 0.961 | 0.963 | 0.376 | 1.21x | 15.5/20.4/23.9% | 1.7/4.9% | 3 |
| 0.3 | 1 | 0.919 | 0.913 | 0.006 | - | - | 0.993 | 0.994 | 0.666 | 1.15x | 17.4/23.6/26.7% | 1.7/5.0% | 3 |

> amplify-worst=0.0: decode_failures 3

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.884 | 0.888 | 0.487 | 1.15x | 13.3/20.7/23.9% | 1.9/4.9% | 3 |
| inverse | 1 | 0.699 | 0.683 | 0.016 | - | - | 0.713 | 0.829 | 0.384 | 1.08x | 11.7/17.0/19.4% | 2.0/3.3% | 3 |
| random | 1 | 0.775 | 0.761 | 0.015 | - | - | 0.933 | 0.942 | 0.437 | 1.16x | 13.1/20.0/23.6% | 1.9/4.8% | 3 |

> role-placement=degree: decode_failures 2

> role-placement=inverse: decode_failures 22

> role-placement=random: decode_failures 1

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.884 | 0.888 | 0.487 | 1.15x | 13.3/20.7/23.9% | 1.9/4.9% | 3 |
| all-routers | 1 | 0.899 | 0.890 | 0.009 | - | - | 0.975 | 0.977 | 0.676 | 2.64x | 26.0/36.8/41.1% | 4.4/5.2% | 3 |

> role-mix=baymesh-2026-08: decode_failures 2

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.884 | 0.888 | 0.487 | 1.15x | 13.3/20.7/23.9% | 1.9/4.9% | 3 |
| no-mute | 1 | 0.787 | 0.776 | 0.011 | - | - | 0.883 | 0.888 | 0.466 | 1.28x | 14.1/21.1/24.2% | 2.0/4.9% | 3 |
| all-routers | 1 | 0.899 | 0.890 | 0.009 | - | - | 0.975 | 0.977 | 0.676 | 2.64x | 26.0/36.8/41.1% | 4.4/5.2% | 3 |

> role-mix=baymesh-2026-08: decode_failures 2

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.884 | 0.888 | 0.487 | 1.15x | 13.3/20.7/23.9% | 1.9/4.9% | 3 |
| local-typical | 1 | 0.661 | 0.651 | 0.011 | - | - | 0.777 | 0.777 | 0.000 | 1.27x | 11.2/19.1/24.6% | 2.1/4.7% | 3 |
| basement-heavy | 1 | 0.045 | 0.043 | 0.002 | - | - | 0.173 | 0.239 | 0.000 | 0.40x | 0.5/4.8/7.3% | 0.2/2.0% | 3 |

> siting-mix=uniform: decode_failures 2

> siting-mix=basement-heavy: decode_failures 1

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.837 | 0.831 | 0.006 | - | - | 0.954 | 0.954 | 0.187 | 2.27x | 15.8/27.3/32.0% | 1.7/5.3% | 3 |
| inverse | 1 | 0.822 | 0.814 | 0.009 | - | - | 0.957 | 0.958 | 0.208 | 2.16x | 13.8/23.1/26.9% | 1.7/3.1% | 3 |

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.807 | 0.807 | 0.000 | - | - | 0 | 0.000 | 0.472 | 1.25x | 14.8/21.7/24.8% | 1.7/4.8% | 3 |
| sr | 1 | 0.822 | 0.803 | 0.018 | - | - | 0.953 | 0.955 | 0.494 | 1.28x | 15.1/22.4/25.7% | 1.7/5.1% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.751 | 0.736 | 0.015 | - | - | 0.851 | 0.869 | 0.421 | 3.06x | 33.6/52.2/57.5% | 4.2/9.9% | 3 |
| 100 | 1 | 0.870 | 0.860 | 0.009 | - | - | 0.935 | 0.958 | 0.534 | 1.57x | 17.3/27.8/30.8% | 2.3/5.1% | 3 |
| 120 | 1 | 0.870 | 0.860 | 0.009 | - | - | 0.935 | 0.958 | 0.534 | 1.57x | 17.3/27.8/30.8% | 2.3/5.1% | 3 |
| 250 | 1 | 0.870 | 0.860 | 0.009 | - | - | 0.935 | 0.958 | 0.534 | 1.57x | 17.3/27.8/30.8% | 2.3/5.1% | 3 |

> max-num-nodes=10: decode_failures 7

> max-num-nodes=100: decode_failures 47

> max-num-nodes=120: decode_failures 47

> max-num-nodes=250: decode_failures 47

> slower: 12 s per simulated hour against 2.54 over 21 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.301 | 0.297 | 0.004 | - | - | 0.371 | 0.381 | 0.174 | 11.36x | 38.2/51.4/59.7% | 4.0/10.2% | 3 |
| 120 | 1 | 0.470 | 0.464 | 0.006 | - | - | 0.553 | 0.553 | 0.249 | 4.39x | 15.3/21.6/26.3% | 1.5/4.5% | 3 |
| 250 | 1 | 0.473 | 0.467 | 0.006 | - | - | 0.570 | 0.573 | 0.257 | 4.27x | 15.0/20.6/24.6% | 1.5/4.3% | 3 |

> max-num-nodes=10: decode_failures 26

> max-num-nodes=120: decode_failures 1

> max-num-nodes=250: decode_failures 4

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.870 | 0.860 | 0.009 | - | - | 0.935 | 0.958 | 0.534 | 1.57x | 17.3/27.8/30.8% | 2.3/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.870 | 0.860 | 0.009 | - | - | 0.935 | 0.958 | 0.534 | 1.57x | 17.3/27.8/30.8% | 2.3/5.1% | 3 |
| constrained | 1 | 0.763 | 0.750 | 0.013 | - | - | 0.853 | 0.885 | 0.409 | 3.07x | 33.6/52.3/57.6% | 4.3/9.9% | 3 |

> platform-mix=uniform: decode_failures 47

> platform-mix=baymesh-2026-08: decode_failures 47

> platform-mix=constrained: decode_failures 17

> slower: 13.3 s per simulated hour against 2.6 over 21 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.748 | 0.737 | 0.010 | - | - | 0.902 | 0.932 | 0.560 | 5.45x | 54.6/68.2/73.2% | 3.6/12.2% | 3 |
| 25 | 1 | 0.748 | 0.737 | 0.010 | - | - | 0.902 | 0.932 | 0.560 | 5.45x | 54.6/68.2/73.2% | 3.6/12.2% | 3 |
| 100 | 1 | 0.748 | 0.737 | 0.010 | - | - | 0.902 | 0.932 | 0.560 | 5.45x | 54.6/68.2/73.2% | 3.6/12.2% | 3 |
| 2000 | 1 | 0.748 | 0.737 | 0.010 | - | - | 0.902 | 0.932 | 0.560 | 5.45x | 54.6/68.2/73.2% | 3.6/12.2% | 3 |

> warm-num-nodes=0: decode_failures 89

> warm-num-nodes=25: decode_failures 89

> warm-num-nodes=100: decode_failures 89

> warm-num-nodes=2000: decode_failures 89

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.694 | 0.683 | 0.011 | - | - | 0.764 | 0.866 | 0.410 | 1.19x | 13.9/21.1/24.1% | 1.6/4.4% | 3 |
| 0.2 | 1 | 0.600 | 0.580 | 0.021 | - | - | 0.711 | 0.837 | 0.323 | 1.11x | 13.0/20.0/23.0% | 1.5/4.1% | 3 |
| 0.3 | 1 | 0.495 | 0.477 | 0.018 | - | - | 0.588 | 0.749 | 0.239 | 1.01x | 11.9/18.2/21.1% | 1.4/3.4% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 15

> burst-loss=0.2: decode_failures 26

> burst-loss=0.3: decode_failures 22

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.766 | 0.755 | 0.011 | - | - | 0.864 | 0.905 | 0.425 | 1.35x | 15.6/23.5/26.7% | 1.9/4.9% | 3 |
| 0.2 | 1 | 0.731 | 0.721 | 0.010 | - | - | 0.811 | 0.899 | 0.408 | 1.38x | 15.9/24.2/27.6% | 2.0/4.7% | 3 |
| 0.3 | 1 | 0.666 | 0.656 | 0.011 | - | - | 0.729 | 0.854 | 0.336 | 1.36x | 15.6/24.0/27.5% | 2.0/4.4% | 3 |

> extra-loss=0.0: decode_failures 3

> extra-loss=0.1: decode_failures 30

> extra-loss=0.2: decode_failures 21

> extra-loss=0.3: decode_failures 24

> slower: 7.51 s per simulated hour against 2.22 over 21 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.696 | 0.683 | 0.013 | - | - | 0.788 | 0.875 | 0.365 | 1.21x | 14.1/21.2/24.3% | 1.6/4.6% | 3 |
| 0.2 | 1 | 0.565 | 0.554 | 0.011 | - | - | 0.608 | 0.791 | 0.295 | 1.12x | 12.9/20.0/23.4% | 1.6/4.1% | 3 |
| 0.3 | 1 | 0.451 | 0.441 | 0.011 | - | - | 0.496 | 0.718 | 0.198 | 1.02x | 12.2/18.4/21.6% | 1.5/3.5% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 33

> burst-loss=0.2: decode_failures 20

> burst-loss=0.3: decode_failures 17

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.760 | 0.760 | 0.000 | - | - | 0.775 | 0.904 | 0.454 | 1.69x | 19.7/29.6/34.1% | 2.3/6.5% | 3 |
| directed-with-late-flood | 1 | 0.781 | 0.781 | 0.000 | - | - | 0.737 | 0.930 | 0.474 | 1.53x | 17.7/26.8/30.6% | 2.1/5.9% | 3 |
| m4-early-flood | 1 | 0.788 | 0.788 | 0.000 | - | - | 0.753 | 0.922 | 0.464 | 1.54x | 17.9/26.9/30.9% | 2.1/5.9% | 3 |

> dm-mode=flood-only: decode_failures 27

> dm-mode=directed-with-late-flood: decode_failures 33

> dm-mode=m4-early-flood: decode_failures 33

> slower: 9 s per simulated hour against 3.06 over 21 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.973 | 0.973 | 0.408 | 0.73x | 7.7/10.8/12.5% | 1.2/2.1% | 3 |
| 2.8 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> profile=2.8: decode_failures 3

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.814 | 0.806 | 0.008 | - | - | 0.961 | 0.965 | 0.377 | 1.15x | 13.1/18.1/21.9% | 1.6/4.6% | 3 |
| 0.5 | 1 | 0.841 | 0.831 | 0.011 | - | - | 0.959 | 0.978 | 0.487 | 1.05x | 11.3/17.2/20.3% | 1.6/4.3% | 3 |
| 0.75 | 1 | 0.831 | 0.824 | 0.007 | - | - | 0.964 | 0.965 | 0.516 | 0.93x | 10.9/15.6/16.5% | 1.5/3.6% | 3 |

> legacy-fraction=0.0: decode_failures 3

> legacy-fraction=0.5: decode_failures 54

> slower: 5.9 s per simulated hour against 1.67 over 21 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.812 | 0.803 | 0.009 | - | - | 0.957 | 0.959 | 0.381 | 1.14x | 13.0/18.1/22.1% | 1.5/4.6% | 3 |
| 0.5 | 1 | 0.835 | 0.825 | 0.010 | - | - | 0.964 | 0.971 | 0.436 | 1.01x | 11.0/16.9/20.2% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.847 | 0.840 | 0.007 | - | - | 0.982 | 0.982 | 0.470 | 0.92x | 10.9/15.5/16.8% | 1.5/3.6% | 3 |

> legacy-fraction=0.0: decode_failures 3

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.850 | 0.841 | 0.009 | - | - | 0.949 | 0.951 | 0.460 | 0.70x | 8.4/12.9/14.8% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> profile-flag=signing=false: decode_failures 3

> profile-flag=signing=true: decode_failures 3

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.827 | 0.820 | 0.007 | - | - | 0.968 | 0.970 | 0.417 | 0.73x | 8.1/11.8/13.8% | 1.1/2.5% | 3 |
| 2.5 | 1 | 0.826 | 0.818 | 0.008 | - | - | 0.959 | 0.961 | 0.398 | 0.75x | 8.2/11.9/13.7% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.828 | 0.819 | 0.010 | - | - | 0.968 | 0.968 | 0.423 | 0.72x | 8.0/11.9/14.0% | 1.1/2.5% | 3 |
| 2.7 | 1 | 0.836 | 0.831 | 0.006 | - | - | 0.958 | 0.960 | 0.409 | 0.74x | 8.5/12.9/15.2% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> profile=2.8: decode_failures 3

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.843 | 0.834 | 0.010 | - | - | 0.944 | 0.950 | 0.461 | 0.89x | 10.1/15.4/17.6% | 1.3/3.6% | 3 |
| 900 | 1 | 0.749 | 0.737 | 0.012 | - | - | 0.843 | 0.884 | 0.406 | 2.06x | 23.9/35.3/40.6% | 2.8/7.9% | 3 |
| 300 | 1 | 0.497 | 0.485 | 0.013 | - | - | 0.587 | 0.673 | 0.237 | 4.50x | 48.8/68.2/75.9% | 6.6/14.9% | 3 |

> broadcast-interval-s=3600: decode_failures 5

> broadcast-interval-s=900: decode_failures 25

> broadcast-interval-s=300: decode_failures 18

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.960 | 0.960 | 0.568 | 1.00x | 11.7/15.9/18.3% | 1.5/3.6% | 3 |
| 900 | 1 | 0.847 | 0.841 | 0.006 | - | - | 0.933 | 0.936 | 0.596 | 2.36x | 26.3/38.4/43.6% | 3.4/8.3% | 3 |
| 300 | 1 | 0.600 | 0.590 | 0.010 | - | - | 0.695 | 0.759 | 0.417 | 5.04x | 51.8/70.1/77.9% | 7.7/15.3% | 3 |

> broadcast-interval-s=3600: decode_failures 2

> broadcast-interval-s=300: decode_failures 23

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.831 | 0.822 | 0.009 | - | - | 0.913 | 0.943 | 0.495 | 1.23x | 14.3/21.2/24.4% | 1.7/4.8% | 3 |
| sinusoid | 1 | 0.821 | 0.812 | 0.009 | - | - | 0.901 | 0.935 | 0.487 | 1.21x | 13.9/20.9/23.9% | 1.7/4.6% | 3 |
| commuter | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> diurnal=flat: decode_failures 35

> diurnal=sinusoid: decode_failures 18

> diurnal=commuter: decode_failures 3

> slower: 6.33 s per simulated hour against 1.58 over 21 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.749 | 0.737 | 0.012 | - | - | 0.843 | 0.884 | 0.406 | 2.06x | 23.9/35.3/40.6% | 2.8/7.9% | 3 |
| 3600 | 1 | 0.843 | 0.834 | 0.010 | - | - | 0.944 | 0.950 | 0.461 | 0.89x | 10.1/15.4/17.6% | 1.3/3.6% | 3 |
| 10800 | 1 | 0.865 | 0.857 | 0.008 | - | - | 0.960 | 0.969 | 0.533 | 0.61x | 6.8/10.3/11.9% | 0.8/2.5% | 3 |
| 43200 | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.952 | 0.972 | 0.506 | 0.44x | 5.0/7.4/8.5% | 0.6/1.9% | 3 |

> broadcast-interval-s=900: decode_failures 25

> broadcast-interval-s=3600: decode_failures 5

> broadcast-interval-s=43200: decode_failures 31

> slower: 6.18 s per simulated hour against 1.4 over 21 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.801 | 0.791 | 0.010 | - | - | 0.881 | 0.924 | 0.459 | 1.34x | 15.6/23.3/26.5% | 1.8/5.1% | 3 |
| 1.0 | 1 | 0.786 | 0.773 | 0.013 | - | - | 0.902 | 0.923 | 0.450 | 1.51x | 17.6/26.4/30.2% | 2.1/5.8% | 3 |
| 4.0 | 1 | 0.765 | 0.750 | 0.015 | - | - | 0.888 | 0.896 | 0.429 | 1.90x | 22.3/33.5/38.7% | 2.6/7.3% | 3 |

> traceroute-per-hour=0.0: decode_failures 3

> traceroute-per-hour=0.25: decode_failures 31

> traceroute-per-hour=1.0: decode_failures 20

> traceroute-per-hour=4.0: decode_failures 8

> slower: 7.37 s per simulated hour against 2.1 over 21 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.748 | 0.737 | 0.010 | - | - | 0.902 | 0.932 | 0.560 | 5.45x | 54.6/68.2/73.2% | 3.6/12.2% | 3 |
| 1.0 | 1 | 0.665 | 0.656 | 0.009 | - | - | 0.835 | 0.890 | 0.487 | 6.13x | 59.8/71.7/76.7% | 4.1/13.3% | 3 |

> traceroute-per-hour=0.0: decode_failures 89

> traceroute-per-hour=1.0: queue drops 12.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 92

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.669 | 0.651 | 0.018 | - | - | 0.865 | 0.867 | 0.399 | 1.28x | 14.9/22.5/29.4% | 3.2/6.1% | 3 |
| 60 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 90 | 1 | 0.923 | 0.919 | 0.004 | - | - | 0.995 | 0.995 | 0.665 | 1.62x | 17.8/25.0/30.3% | 1.5/5.0% | 3 |
| 120 | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.997 | 0.997 | 0.763 | 1.89x | 20.5/28.0/31.5% | 1.2/5.0% | 3 |
| 150 | 1 | 0.952 | 0.950 | 0.002 | - | - | 0.997 | 0.997 | 0.791 | 2.58x | 26.7/38.3/43.4% | 1.3/5.6% | 3 |

> nodes=60: decode_failures 3

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 120 | 1 | 0.747 | 0.734 | 0.012 | - | - | 0.908 | 0.908 | 0.412 | 2.11x | 15.0/21.8/26.6% | 1.5/4.9% | 3 |
| 250 | 1 | 0.469 | 0.463 | 0.006 | - | - | 0.576 | 0.577 | 0.232 | 4.70x | 16.4/23.1/27.4% | 1.6/4.9% | 3 |
| 500 | 1 | 0.329 | 0.321 | 0.008 | - | - | 0.556 | 0.626 | 0.121 | 10.42x | 19.7/31.0/42.4% | 1.8/5.8% | 3 |

> nodes=60: decode_failures 3

> nodes=250: decode_failures 10

> nodes=500: decode_failures 213

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.748 | 0.732 | 0.015 | - | - | 0.909 | 0.911 | 0.407 | 1.96x | 13.8/20.3/24.9% | 1.5/4.5% | 3 |
| 250 | 1 | 0.470 | 0.464 | 0.006 | - | - | 0.553 | 0.553 | 0.249 | 4.39x | 15.3/21.6/26.3% | 1.5/4.5% | 3 |
| 500 | 1 | 0.330 | 0.320 | 0.009 | - | - | 0.574 | 0.631 | 0.128 | 9.94x | 18.7/29.6/41.0% | 1.7/5.5% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 182

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.798 | 0.791 | 0.007 | - | - | 0.868 | 0.898 | 0.477 | 1.30x | 15.0/22.5/25.9% | 1.8/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.749 | 0.735 | 0.014 | - | - | 0.884 | 0.888 | 0.487 | 1.15x | 13.3/20.7/23.9% | 1.9/4.9% | 3 |

> role-mix=legacy-default: decode_failures 11

> role-mix=baymesh-2026-08: decode_failures 2

> slower: 3.89 s per simulated hour against 1.86 over 21 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.823 | 0.813 | 0.010 | - | - | 0.909 | 0.921 | 0.516 | 1.32x | 15.5/22.4/25.5% | 1.8/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.774 | 0.766 | 0.008 | - | - | 0.867 | 0.873 | 0.545 | 1.30x | 15.3/22.8/26.4% | 2.2/4.7% | 3 |

> role-mix=legacy-default: decode_failures 2

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.05 | 1 | 0.845 | 0.834 | 0.012 | - | - | 0.947 | 0.947 | 0.483 | 1.44x | 17.3/24.7/28.7% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.846 | 0.835 | 0.011 | - | - | 0.936 | 0.948 | 0.492 | 1.53x | 17.5/28.8/32.1% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.859 | 0.850 | 0.009 | - | - | 0.934 | 0.954 | 0.487 | 1.76x | 18.7/34.0/39.4% | 2.4/5.1% | 3 |

> router-late-fraction=0.0: decode_failures 3

> router-late-fraction=0.05: decode_failures 1

> router-late-fraction=0.1: decode_failures 18

> router-late-fraction=0.2: decode_failures 37

> slower: 5.46 s per simulated hour against 1.76 over 21 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| local-typical | 1 | 0.698 | 0.684 | 0.014 | - | - | 0.816 | 0.818 | 0.000 | 1.42x | 11.9/19.8/25.8% | 2.1/4.9% | 3 |
| event | 1 | 0.060 | 0.060 | 0.000 | - | - | 0.056 | 0.097 | 0.000 | 0.56x | 2.0/6.2/7.5% | 0.9/2.1% | 3 |
| backbone | 1 | 0.963 | 0.963 | 0.001 | - | - | 0.997 | 0.999 | 0.814 | 1.11x | 22.9/31.1/34.7% | 1.4/5.4% | 3 |

> siting-mix=uniform: decode_failures 3

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.813 | 0.808 | 0.005 | - | - | 0.908 | 0.909 | 0.439 | 1.37x | 21.2/27.9/31.6% | 3.0/7.3% | 3 |
| 60 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 90 | 1 | 0.765 | 0.758 | 0.007 | - | - | 0.950 | 0.951 | 0.431 | 1.67x | 13.9/21.4/27.4% | 1.7/4.7% | 3 |
| 120 | 1 | 0.747 | 0.734 | 0.012 | - | - | 0.908 | 0.908 | 0.412 | 2.11x | 15.0/21.8/26.6% | 1.5/4.9% | 3 |
| 150 | 1 | 0.656 | 0.642 | 0.015 | - | - | 0.960 | 0.962 | 0.332 | 2.77x | 16.0/26.6/31.6% | 1.6/5.6% | 3 |

> nodes=60: decode_failures 3

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 1.25 | 1 | 0.541 | 0.527 | 0.013 | - | - | 0.772 | 0.772 | 0.137 | 1.25x | 10.8/14.8/19.6% | 2.0/4.5% | 3 |
| 1.5 | 1 | 0.239 | 0.231 | 0.008 | - | - | 0.439 | 0.444 | 0.000 | 1.16x | 8.0/12.7/15.6% | 1.8/3.7% | 3 |
| 2.0 | 1 | 0.075 | 0.075 | 0.000 | - | - | 0.066 | 0.067 | 0.000 | 0.56x | 2.4/4.4/6.5% | 1.0/2.3% | 3 |

> stretch=1.0: decode_failures 3

> stretch=1.5: decode_failures 1

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| clustered | 1 | 0.886 | 0.882 | 0.003 | - | - | 0.938 | 0.938 | 0.000 | 1.15x | 21.6/33.5/36.1% | 1.5/5.5% | 3 |
| corridor | 1 | 0.418 | 0.410 | 0.009 | - | - | 0.591 | 0.624 | 0.128 | 1.53x | 15.0/24.9/27.1% | 2.0/5.7% | 3 |
| hub | 1 | 0.952 | 0.951 | 0.001 | - | - | 0.988 | 0.988 | 0.855 | 1.20x | 24.6/30.8/32.7% | 1.4/5.6% | 3 |

> topology=uniform: decode_failures 3

> topology=corridor: decode_failures 28

> slower: 4.11 s per simulated hour against 1.86 over 21 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.781 | 0.781 | 0.000 | - | - | 0.737 | 0.930 | 0.474 | 1.53x | 17.7/26.8/30.6% | 2.1/5.9% | 3 |
| True | 1 | 0.776 | 0.776 | 0.000 | - | - | 0.747 | 0.914 | 0.466 | 1.56x | 18.1/27.3/31.3% | 2.1/5.9% | 3 |

> coding-rate-ladder=False: decode_failures 33

> coding-rate-ladder=True: decode_failures 33

> slower: 11 s per simulated hour against 2.79 over 21 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.776 | 0.776 | 0.000 | - | - | 0.747 | 0.914 | 0.466 | 1.56x | 18.1/27.3/31.3% | 2.1/5.9% | 3 |
| m4-early-flood | 1 | 0.781 | 0.781 | 0.000 | - | - | 0.732 | 0.917 | 0.470 | 1.52x | 17.6/26.6/30.5% | 2.1/5.8% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 33

> dm-mode=m4-early-flood: decode_failures 30

> slower: 10.4 s per simulated hour against 2.54 over 21 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.807 | 0.807 | 0.000 | - | - | 0 | 0.000 | 0.472 | 1.25x | 14.8/21.7/24.8% | 1.7/4.8% | 3 |
| chain | 1 | 0.771 | 0.768 | 0.004 | - | - | 0.726 | 0.894 | 0.451 | 1.49x | 17.2/25.7/29.6% | 2.1/5.7% | 3 |
| sr | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> protocol=sr: decode_failures 3

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| True | 1 | 0.813 | 0.804 | 0.009 | - | - | 0.891 | 0.933 | 0.488 | 1.31x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> extra-repeats=False: decode_failures 3

> extra-repeats=True: decode_failures 26

> slower: 6.84 s per simulated hour against 1.68 over 21 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.997 | 0.997 | 0.763 | 1.89x | 20.5/28.0/31.5% | 1.2/5.0% | 3 |
| True | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.998 | 0.998 | 0.789 | 1.92x | 20.6/28.2/31.6% | 1.3/5.0% | 3 |

> extra-repeats=False: misdecodes 1

> extra-repeats=True: misdecodes 1

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.111 | 0.109 | 0.002 | - | - | 0.219 | 0.238 | 0.000 | 0.03x | 0.1/0.3/0.4% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.351 | 0.343 | 0.008 | - | - | 0.543 | 0.546 | 0.000 | 0.24x | 1.4/2.9/4.1% | 0.3/0.9% | 3 |
| LONG_TURBO | 1 | 0.726 | 0.714 | 0.013 | - | - | 0.887 | 0.897 | 0.269 | 1.30x | 11.1/18.1/23.7% | 2.1/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 5

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 0.25 | 1 | 0.851 | 0.840 | 0.011 | - | - | 0.945 | 0.954 | 0.557 | 1.19x | 17.5/23.8/26.2% | 1.7/5.0% | 3 |
| 1.0 | 1 | 0.899 | 0.891 | 0.008 | - | - | 0.964 | 0.968 | 0.690 | 1.12x | 21.4/28.4/29.1% | 1.6/5.2% | 3 |

> duct-per-hour=0.0: decode_failures 3

> duct-per-hour=0.25: decode_failures 13

> slower: 4.08 s per simulated hour against 1.76 over 21 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.244 | 0.241 | 0.003 | - | - | 0.362 | 0.425 | 0.000 | 0.12x | 0.7/1.3/1.9% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| LITE_FAST | 1 | 0.729 | 0.721 | 0.008 | - | - | 0.888 | 0.888 | 0.300 | 1.01x | 9.5/15.7/19.5% | 1.7/3.7% | 3 |
| NARROW_SLOW | 1 | 0.757 | 0.749 | 0.008 | - | - | 0.881 | 0.887 | 0.407 | 1.27x | 12.7/19.8/23.7% | 1.9/4.6% | 3 |

> preset=SHORT_FAST: decode_failures 11

> preset=LONG_FAST: decode_failures 3

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| temporal | 1 | 0.693 | 0.679 | 0.014 | - | - | 0.813 | 0.846 | 0.332 | 1.26x | 13.9/21.6/24.5% | 1.8/4.7% | 3 |
| transient | 1 | 0.801 | 0.789 | 0.012 | - | - | 0.902 | 0.921 | 0.496 | 1.30x | 15.0/22.3/25.7% | 1.8/4.9% | 3 |
| periodic | 1 | 0.626 | 0.620 | 0.006 | - | - | 0.638 | 0.749 | 0.363 | 1.19x | 13.8/20.6/23.6% | 1.6/4.2% | 3 |

> noise-profile=none: decode_failures 3

> noise-profile=temporal: decode_failures 17

> noise-profile=transient: decode_failures 26

> noise-profile=periodic: decode_failures 18

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.244 | 0.241 | 0.003 | - | - | 0.362 | 0.425 | 0.000 | 0.12x | 0.7/1.3/1.9% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| LONG_MODERATE | 1 | 0.764 | 0.732 | 0.033 | - | - | 0.863 | 0.864 | 0.563 | 3.27x | 42.4/57.6/65.7% | 4.8/12.0% | 3 |

> preset=SHORT_FAST: decode_failures 11

> preset=LONG_FAST: decode_failures 3

> preset=LONG_MODERATE: decode_failures 5

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.038 | 0.038 | 0.000 | - | - | 0.067 | 0.069 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.111 | 0.109 | 0.002 | - | - | 0.219 | 0.238 | 0.000 | 0.03x | 0.1/0.3/0.4% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| LONG_TURBO | 1 | 0.726 | 0.714 | 0.013 | - | - | 0.887 | 0.897 | 0.269 | 1.30x | 11.1/18.1/23.7% | 2.1/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.800 | 0.789 | 0.011 | - | - | 0.864 | 0.912 | 0.418 | 1.77x | 20.5/27.4/30.4% | 2.8/6.5% | 3 |

> preset=SHORT_TURBO: decode_failures 5

> preset=LONG_FAST: decode_failures 3

> preset=EXTRA_LONG_TURBO: decode_failures 26

> slower: 3.34 s per simulated hour against 1.59 over 17 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.748 | 0.738 | 0.010 | - | - | 0.843 | 0.868 | 0.437 | 1.28x | 15.0/22.4/25.7% | 1.8/4.8% | 3 |
| 10000 | 1 | 0.626 | 0.620 | 0.006 | - | - | 0.638 | 0.749 | 0.363 | 1.19x | 13.8/20.6/23.6% | 1.6/4.2% | 3 |
| 4000 | 1 | 0.376 | 0.374 | 0.003 | - | - | 0.361 | 0.498 | 0.187 | 1.01x | 11.8/17.4/20.3% | 1.5/3.2% | 3 |
| 2000 | 1 | 0.076 | 0.076 | 0.000 | - | - | 0.068 | 0.141 | 0.036 | 0.68x | 7.8/12.0/14.5% | 1.0/1.8% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 10

> noise-pulse-interval-ms=10000: decode_failures 18

> noise-pulse-interval-ms=4000: decode_failures 3

> slower: 3.52 s per simulated hour against 1.6 over 21 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.239 | 0.231 | 0.008 | - | - | 0.439 | 0.444 | 0.000 | 1.16x | 8.0/12.7/15.6% | 1.8/3.7% | 3 |
| 1.0 | 1 | 0.611 | 0.601 | 0.010 | - | - | 0.712 | 0.713 | 0.464 | 0.89x | 12.8/16.8/18.7% | 1.3/3.9% | 3 |

> duct-per-hour=0.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 22 | 1 | 0.329 | 0.319 | 0.010 | - | - | 0.516 | 0.545 | 0.000 | 1.32x | 8.2/15.0/18.1% | 2.0/4.5% | 3 |
| 17 | 1 | 0.113 | 0.111 | 0.002 | - | - | 0.189 | 0.223 | 0.000 | 0.74x | 3.3/6.3/9.3% | 1.1/2.5% | 3 |
| 14 | 1 | 0.054 | 0.054 | 0.000 | - | - | 0.065 | 0.069 | 0.000 | 0.45x | 1.8/3.6/4.5% | 0.6/1.5% | 3 |

> tx-power=30: decode_failures 3

> tx-power=22: decode_failures 2

> tx-power=17: decode_failures 4

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.997 | 0.997 | 0.763 | 1.89x | 20.5/28.0/31.5% | 1.2/5.0% | 3 |
| True | 1 | 0.940 | 0.936 | 0.003 | - | - | 0.995 | 0.996 | 0.777 | 2.24x | 23.8/32.3/36.3% | 1.5/5.6% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

> no-adopt-hop-recommendation=True: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.846 | 0.834 | 0.012 | - | - | 0.947 | 0.951 | 0.403 | 1.39x | 16.2/23.8/28.3% | 2.0/5.1% | 3 |
| True | 1 | 0.865 | 0.856 | 0.010 | - | - | 0.949 | 0.955 | 0.520 | 1.46x | 16.8/24.1/28.4% | 2.2/5.0% | 3 |

> favourite-routers=True: decode_failures 1

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| random | 1 | 0.745 | 0.736 | 0.010 | - | - | 0.822 | 0.872 | 0.443 | 1.27x | 14.7/21.7/24.9% | 1.7/4.7% | 3 |

> hop-assign=centrality: decode_failures 3

> hop-assign=random: decode_failures 19

> slower: 4.48 s per simulated hour against 1.85 over 21 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.639 | 0.622 | 0.017 | - | - | 0.727 | 0.803 | 0.285 | 1.01x | 12.0/19.0/22.0% | 1.4/4.2% | 3 |
| 7 | 1 | 0.881 | 0.877 | 0.004 | - | - | 0.950 | 0.950 | 0.583 | 1.47x | 16.9/24.2/27.4% | 2.2/5.3% | 3 |
| 15 | 1 | 0.901 | 0.898 | 0.003 | - | - | 0.950 | 0.950 | 0.597 | 1.52x | 17.5/25.0/28.3% | 2.3/5.5% | 3 |
| 32 | 1 | 0.900 | 0.897 | 0.004 | - | - | 0.945 | 0.950 | 0.588 | 1.52x | 17.6/25.0/28.3% | 2.3/5.5% | 3 |

> hop-limit=3: decode_failures 26

> hop-limit=7: decode_failures 2

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.639 | 0.622 | 0.017 | - | - | 0.727 | 0.803 | 0.285 | 1.01x | 12.0/19.0/22.0% | 1.4/4.2% | 3 |
| 5 | 1 | 0.826 | 0.816 | 0.010 | - | - | 0.917 | 0.937 | 0.488 | 1.34x | 15.6/23.2/26.3% | 1.8/5.1% | 3 |
| 7 | 1 | 0.881 | 0.877 | 0.004 | - | - | 0.950 | 0.950 | 0.583 | 1.47x | 16.9/24.2/27.4% | 2.2/5.3% | 3 |

> hop-limit=3: decode_failures 26

> hop-limit=5: decode_failures 11

> hop-limit=7: decode_failures 2

> slower: 4.72 s per simulated hour against 2.03 over 21 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| KNOWN_ONLY | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.802 | 0.802 | 0.000 | - | - | 0.695 | 0.929 | 0.466 | 1.25x | 14.7/21.7/24.8% | 1.7/4.8% | 3 |

> rebroadcast-mode=ALL: decode_failures 3

> rebroadcast-mode=KNOWN_ONLY: decode_failures 3

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.639 | 0.622 | 0.017 | - | - | 0.727 | 0.803 | 0.285 | 1.01x | 12.0/19.0/22.0% | 1.4/4.2% | 3 |
| True | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> hop-spread=False: decode_failures 26

> hop-spread=True: decode_failures 3

> slower: 6 s per simulated hour against 2.15 over 21 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| BALANCED | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| STRICT | 1 | 0.705 | 0.705 | 0.000 | - | - | 0.755 | 0.850 | 0.396 | 1.41x | 16.2/24.5/27.8% | 2.0/5.3% | 3 |

> signature-policy=COMPATIBLE: decode_failures 3

> signature-policy=BALANCED: decode_failures 3

> signature-policy=STRICT: decode_failures 28

> slower: 5.63 s per simulated hour against 1.87 over 21 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| dm | 1 | 0.812 | 0.800 | 0.012 | - | - | 0.930 | 0.932 | 0.475 | 1.27x | 14.7/22.0/25.4% | 1.7/5.0% | 3 |

> advert-transport=broadcast: decode_failures 3

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.805 | 0.794 | 0.012 | - | - | 0.919 | 0.923 | 0.456 | 1.30x | 15.2/22.6/25.9% | 1.8/5.0% | 3 |
| local | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| time | 1 | 0.813 | 0.801 | 0.012 | - | - | 0.924 | 0.934 | 0.470 | 1.35x | 15.8/23.4/26.9% | 1.9/5.3% | 3 |
| window | 1 | 0.818 | 0.806 | 0.012 | - | - | 0.916 | 0.942 | 0.478 | 1.28x | 14.9/22.3/25.6% | 1.8/5.0% | 3 |

> bucket-mode=global: misdecodes 14

> bucket-mode=local: decode_failures 3

> bucket-mode=time: misdecodes 8

> bucket-mode=time: decode_failures 1

> bucket-mode=window: misdecodes 3

> bucket-mode=window: decode_failures 4

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.801 | 0.787 | 0.013 | - | - | 0.898 | 0.908 | 0.459 | 1.44x | 16.4/24.8/28.5% | 2.0/5.7% | 3 |
| 1800 | 1 | 0.813 | 0.801 | 0.012 | - | - | 0.924 | 0.934 | 0.470 | 1.35x | 15.8/23.4/26.9% | 1.9/5.3% | 3 |
| 3600 | 1 | 0.813 | 0.804 | 0.009 | - | - | 0.897 | 0.935 | 0.471 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> time-bucket-s=600: misdecodes 70

> time-bucket-s=1800: misdecodes 8

> time-bucket-s=1800: decode_failures 1

> time-bucket-s=3600: misdecodes 3

> time-bucket-s=3600: decode_failures 18

> slower: 4.34 s per simulated hour against 1.62 over 21 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| interval | 1 | 0.776 | 0.764 | 0.012 | - | - | 0.867 | 0.890 | 0.467 | 1.74x | 19.3/29.8/34.8% | 2.4/7.3% | 3 |
| aimd | 1 | 0.795 | 0.790 | 0.005 | - | - | 0.781 | 0.918 | 0.475 | 1.34x | 15.4/23.1/26.2% | 1.9/5.1% | 3 |
| bucket+interval | 1 | 0.785 | 0.770 | 0.015 | - | - | 0.904 | 0.913 | 0.457 | 1.77x | 19.6/30.4/35.4% | 2.5/7.4% | 3 |

> trigger=bucket: decode_failures 3

> trigger=interval: misdecodes 8

> trigger=interval: decode_failures 9

> trigger=aimd: decode_failures 31

> trigger=bucket+interval: misdecodes 7

> trigger=bucket+interval: decode_failures 1

> slower: 9.45 s per simulated hour against 3.62 over 21 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.811 | 0.800 | 0.011 | - | - | 0.894 | 0.937 | 0.471 | 1.28x | 14.9/22.2/25.6% | 1.8/4.9% | 3 |
| 8 | 1 | 0.812 | 0.802 | 0.010 | - | - | 0.894 | 0.935 | 0.475 | 1.28x | 14.9/22.2/25.5% | 1.7/4.9% | 3 |
| 16 | 1 | 0.804 | 0.794 | 0.010 | - | - | 0.873 | 0.923 | 0.467 | 1.28x | 14.8/22.2/25.6% | 1.7/5.0% | 3 |
| 32 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 50 | 1 | 0.812 | 0.801 | 0.012 | - | - | 0.921 | 0.934 | 0.477 | 1.28x | 15.1/22.4/25.8% | 1.8/5.0% | 3 |

> capacity=4: decode_failures 63

> capacity=8: decode_failures 64

> capacity=16: decode_failures 46

> capacity=32: decode_failures 3

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.811 | 0.800 | 0.011 | - | - | 0.894 | 0.937 | 0.471 | 1.28x | 14.9/22.2/25.6% | 1.8/4.9% | 3 |
| 8 | 1 | 0.812 | 0.802 | 0.010 | - | - | 0.894 | 0.935 | 0.475 | 1.28x | 14.9/22.2/25.5% | 1.7/4.9% | 3 |
| 16 | 1 | 0.804 | 0.794 | 0.010 | - | - | 0.873 | 0.923 | 0.467 | 1.28x | 14.8/22.2/25.6% | 1.7/5.0% | 3 |
| 32 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 50 | 1 | 0.812 | 0.801 | 0.012 | - | - | 0.921 | 0.934 | 0.477 | 1.28x | 15.1/22.4/25.8% | 1.8/5.0% | 3 |

> capacity=4: decode_failures 63

> capacity=8: decode_failures 64

> capacity=16: decode_failures 46

> capacity=32: decode_failures 3

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.793 | 0.792 | 0.001 | - | - | 0.714 | 0.931 | 0.482 | 1.26x | 14.9/22.0/25.1% | 1.7/4.9% | 3 |
| 16 | 1 | 0.812 | 0.807 | 0.006 | - | - | 0.797 | 0.934 | 0.482 | 1.27x | 14.9/22.2/25.3% | 1.7/4.9% | 3 |
| 32 | 1 | 0.818 | 0.806 | 0.012 | - | - | 0.916 | 0.942 | 0.478 | 1.28x | 14.9/22.3/25.6% | 1.8/5.0% | 3 |

> capacity=8: decode_failures 111

> capacity=16: misdecodes 1

> capacity=16: decode_failures 69

> capacity=32: misdecodes 3

> capacity=32: decode_failures 4

> slower: 4.3 s per simulated hour against 1.73 over 21 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.785 | 0.770 | 0.015 | - | - | 0.904 | 0.913 | 0.457 | 1.77x | 19.6/30.4/35.4% | 2.5/7.4% | 3 |
| 02-06 | 1 | 0.812 | 0.804 | 0.008 | - | - | 0.839 | 0.940 | 0.464 | 1.34x | 15.6/23.2/26.7% | 1.8/5.1% | 3 |
| 00-08 | 1 | 0.802 | 0.794 | 0.008 | - | - | 0.842 | 0.927 | 0.470 | 1.40x | 16.0/23.9/27.6% | 1.9/5.5% | 3 |

> catch-up-hours=: misdecodes 7

> catch-up-hours=: decode_failures 1

> catch-up-hours=02-06: decode_failures 48

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 45

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.805 | 0.803 | 0.003 | - | - | 0.923 | 0.924 | 0.477 | 1.28x | 15.1/22.3/25.6% | 1.8/4.9% | 3 |
| 2 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 3 | 1 | 0.822 | 0.803 | 0.018 | - | - | 0.953 | 0.955 | 0.494 | 1.28x | 15.1/22.4/25.7% | 1.7/5.1% | 3 |
| 4 | 1 | 0.825 | 0.797 | 0.028 | - | - | 0.884 | 0.971 | 0.462 | 1.29x | 15.5/22.5/25.7% | 1.8/5.2% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=4: decode_failures 24

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.805 | 0.803 | 0.003 | - | - | 0.923 | 0.924 | 0.477 | 1.28x | 15.1/22.3/25.6% | 1.8/4.9% | 3 |
| 2 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 3 | 1 | 0.822 | 0.803 | 0.018 | - | - | 0.953 | 0.955 | 0.494 | 1.28x | 15.1/22.4/25.7% | 1.7/5.1% | 3 |
| 4 | 1 | 0.825 | 0.797 | 0.028 | - | - | 0.884 | 0.971 | 0.462 | 1.29x | 15.5/22.5/25.7% | 1.8/5.2% | 3 |
| 5 | 1 | 0.819 | 0.801 | 0.018 | - | - | 0.770 | 0.965 | 0.473 | 1.29x | 15.4/22.3/25.5% | 1.8/5.0% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=4: decode_failures 24

> hops-apart=5: decode_failures 36

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.814 | 0.804 | 0.010 | - | - | 0.889 | 0.932 | 0.477 | 1.29x | 15.1/22.4/25.7% | 1.8/5.0% | 3 |
| 30 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 120 | 1 | 0.793 | 0.782 | 0.012 | - | - | 0.908 | 0.917 | 0.481 | 1.30x | 15.1/22.7/26.1% | 1.8/5.1% | 3 |
| 600 | 1 | 0.818 | 0.806 | 0.012 | - | - | 0.927 | 0.936 | 0.470 | 1.29x | 15.2/22.6/25.9% | 1.8/5.1% | 3 |

> advert-jitter-s=1: decode_failures 21

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 3

> advert-jitter-s=600: decode_failures 4

> slower: 5 s per simulated hour against 1.79 over 21 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.814 | 0.804 | 0.010 | - | - | 0.889 | 0.932 | 0.477 | 1.29x | 15.1/22.4/25.7% | 1.8/5.0% | 3 |
| 30 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 120 | 1 | 0.793 | 0.782 | 0.012 | - | - | 0.908 | 0.917 | 0.481 | 1.30x | 15.1/22.7/26.1% | 1.8/5.1% | 3 |
| 600 | 1 | 0.818 | 0.806 | 0.012 | - | - | 0.927 | 0.936 | 0.470 | 1.29x | 15.2/22.6/25.9% | 1.8/5.1% | 3 |

> advert-jitter-s=1: decode_failures 21

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 3

> advert-jitter-s=600: decode_failures 4

> slower: 4.88 s per simulated hour against 1.88 over 21 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.819 | 0.801 | 0.018 | - | - | 0.708 | 0.919 | 0.480 | 1.28x | 15.0/21.7/24.8% | 1.7/4.9% | 3 |
| routers | 1 | 0.797 | 0.789 | 0.009 | - | - | 0.923 | 0.923 | 0.469 | 1.28x | 15.2/22.4/25.6% | 1.8/5.1% | 3 |
| alternate-routers | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.927 | 0.929 | 0.464 | 1.29x | 15.4/22.4/25.7% | 1.8/5.2% | 3 |
| beside-router | 1 | 0.824 | 0.811 | 0.013 | - | - | 0.964 | 0.967 | 0.488 | 1.30x | 15.4/22.7/25.8% | 1.8/5.0% | 3 |
| random-clients | 1 | 0.822 | 0.798 | 0.024 | - | - | 0.891 | 0.947 | 0.468 | 1.30x | 15.4/22.3/25.5% | 1.8/5.0% | 3 |
| hops-apart | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> place=spread: decode_failures 20

> place=random-clients: decode_failures 7

> place=hops-apart: decode_failures 3

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.819 | 0.801 | 0.018 | - | - | 0.708 | 0.919 | 0.480 | 1.28x | 15.0/21.7/24.8% | 1.7/4.9% | 3 |
| routers | 1 | 0.797 | 0.789 | 0.009 | - | - | 0.923 | 0.923 | 0.469 | 1.28x | 15.2/22.4/25.6% | 1.8/5.1% | 3 |
| alternate-routers | 1 | 0.804 | 0.798 | 0.006 | - | - | 0.927 | 0.929 | 0.464 | 1.29x | 15.4/22.4/25.7% | 1.8/5.2% | 3 |
| beside-router | 1 | 0.824 | 0.811 | 0.013 | - | - | 0.964 | 0.967 | 0.488 | 1.30x | 15.4/22.7/25.8% | 1.8/5.0% | 3 |
| random-clients | 1 | 0.822 | 0.798 | 0.024 | - | - | 0.891 | 0.947 | 0.468 | 1.30x | 15.4/22.3/25.5% | 1.8/5.0% | 3 |
| hops-apart | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> place=spread: decode_failures 20

> place=random-clients: decode_failures 7

> place=hops-apart: decode_failures 3

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| broadcast | 1 | 0.843 | 0.795 | 0.048 | - | - | 0.879 | 0.927 | 0.487 | 1.43x | 16.3/24.9/28.5% | 2.0/5.5% | 3 |

> provide-transport=dm: decode_failures 3

> provide-transport=broadcast: decode_failures 45

> slower: 9.29 s per simulated hour against 1.91 over 21 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| heard | 1 | 0.801 | 0.790 | 0.012 | - | - | 0.895 | 0.921 | 0.456 | 1.29x | 15.1/22.5/25.8% | 1.8/5.0% | 3 |

> replay-ordering=tip: decode_failures 3

> replay-ordering=heard: decode_failures 29

> slower: 6.9 s per simulated hour against 1.69 over 21 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.843 | 0.795 | 0.048 | - | - | 0.879 | 0.927 | 0.487 | 1.43x | 16.3/24.9/28.5% | 2.0/5.5% | 3 |
| heard | 1 | 0.830 | 0.777 | 0.053 | - | - | 0.867 | 0.914 | 0.453 | 1.44x | 16.5/25.1/28.8% | 2.0/5.5% | 3 |

> replay-ordering=tip: decode_failures 45

> replay-ordering=heard: decode_failures 21

> slower: 9.92 s per simulated hour against 1.77 over 21 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.814 | 0.805 | 0.008 | - | - | 0.861 | 0.936 | 0.473 | 1.29x | 15.1/22.5/25.6% | 1.8/5.0% | 3 |
| enum | 1 | 0.808 | 0.797 | 0.012 | - | - | 0.895 | 0.929 | 0.482 | 1.28x | 14.8/22.2/25.5% | 1.7/5.0% | 3 |
| hybrid | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> resolve=sketch: decode_failures 30

> resolve=hybrid: decode_failures 3

> slower: 5.03 s per simulated hour against 1.53 over 21 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.797 | 0.789 | 0.009 | - | - | 0.923 | 0.923 | 0.469 | 1.28x | 15.2/22.4/25.6% | 1.8/5.1% | 3 |
| 6 | 1 | 0.795 | 0.787 | 0.008 | - | - | 0.924 | 0.925 | 0.468 | 1.30x | 15.5/22.9/26.2% | 1.8/5.3% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.808 | 0.803 | 0.004 | - | - | 0.815 | 0.910 | 0.490 | 1.27x | 14.9/22.2/25.4% | 1.8/4.9% | 2 |
| 3 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 5 | 1 | 0.814 | 0.800 | 0.014 | - | - | 0.933 | 0.938 | 0.458 | 1.30x | 15.1/22.9/26.2% | 1.8/5.0% | 5 |
| 8 | 1 | 0.802 | 0.789 | 0.012 | - | - | 0.933 | 0.937 | 0.457 | 1.35x | 15.4/23.4/27.0% | 1.8/5.1% | 8 |

> servers=2: decode_failures 23

> servers=3: decode_failures 3

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.808 | 0.803 | 0.004 | - | - | 0.815 | 0.910 | 0.490 | 1.27x | 14.9/22.2/25.4% | 1.8/4.9% | 2 |
| 3 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 5 | 1 | 0.814 | 0.800 | 0.014 | - | - | 0.933 | 0.938 | 0.458 | 1.30x | 15.1/22.9/26.2% | 1.8/5.0% | 5 |
| 8 | 1 | 0.802 | 0.789 | 0.012 | - | - | 0.933 | 0.937 | 0.457 | 1.35x | 15.4/23.4/27.0% | 1.8/5.1% | 8 |

> servers=2: decode_failures 23

> servers=3: decode_failures 3

> slower: 4.73 s per simulated hour against 2.29 over 21 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| True | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |

> signed=False: decode_failures 3

> signed=True: decode_failures 3

> slower: 3.86 s per simulated hour against 1.74 over 21 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.812 | 0.805 | 0.007 | - | - | 0.859 | 0.928 | 0.463 | 1.20x | 13.9/20.8/23.9% | 1.6/4.6% | 3 |
| 1 | 1 | 0.804 | 0.795 | 0.009 | - | - | 0.864 | 0.930 | 0.480 | 1.20x | 13.9/20.8/24.0% | 1.6/4.6% | 3 |
| 2 | 1 | 0.828 | 0.817 | 0.011 | - | - | 0.939 | 0.941 | 0.486 | 1.21x | 14.2/21.2/24.4% | 1.7/4.7% | 3 |
| 4 | 1 | 0.807 | 0.795 | 0.011 | - | - | 0.916 | 0.929 | 0.454 | 1.22x | 14.2/21.2/24.3% | 1.7/4.7% | 3 |

> sr-retries=0: decode_failures 10

> sr-retries=1: decode_failures 15

> sr-retries=2: decode_failures 3

> sr-retries=4: decode_failures 3

> slower: 5.34 s per simulated hour against 1.64 over 21 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.805 | 0.795 | 0.010 | - | - | 0.893 | 0.936 | 0.461 | 1.28x | 14.8/22.1/25.4% | 1.8/4.9% | 3 |
| 24 | 1 | 0.809 | 0.798 | 0.011 | - | - | 0.903 | 0.930 | 0.460 | 1.29x | 15.0/22.3/25.7% | 1.7/5.0% | 3 |
| 32 | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.923 | 0.932 | 0.469 | 1.29x | 15.2/22.7/25.8% | 1.8/5.0% | 3 |
| 64 | 1 | 0.818 | 0.805 | 0.013 | - | - | 0.941 | 0.946 | 0.470 | 1.28x | 15.0/22.3/25.6% | 1.8/5.0% | 3 |

> short-id-bits=16: decode_failures 40

> short-id-bits=24: decode_failures 19

> short-id-bits=32: decode_failures 3

> short-id-bits=64: decode_failures 2

> slower: 4.2 s per simulated hour against 1.75 over 21 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.809 | 0.794 | 0.014 | - | - | 0.922 | 0.942 | 0.466 | 1.36x | 15.7/23.8/27.3% | 1.9/5.4% | 3 |
| 16 | 1 | 0.807 | 0.795 | 0.012 | - | - | 0.900 | 0.927 | 0.467 | 1.32x | 15.4/23.1/26.5% | 1.8/5.2% | 3 |
| 32 | 1 | 0.818 | 0.806 | 0.012 | - | - | 0.916 | 0.942 | 0.478 | 1.28x | 14.9/22.3/25.6% | 1.8/5.0% | 3 |

> window-size=8: misdecodes 91

> window-size=16: misdecodes 19

> window-size=32: misdecodes 3

> window-size=32: decode_failures 4

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.997 | 0.997 | 0.763 | 1.89x | 20.5/28.0/31.5% | 1.2/5.0% | 3 |
| True | 1 | 0.736 | 0.724 | 0.012 | - | - | 0.904 | 0.926 | 0.557 | 5.51x | 55.0/68.4/73.3% | 3.6/12.3% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: decode_failures 82

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.470 | 0.464 | 0.006 | - | - | 0.553 | 0.553 | 0.249 | 4.39x | 15.3/21.6/26.3% | 1.5/4.5% | 3 |
| truesize | 1 | 0.497 | 0.491 | 0.006 | - | - | 0.592 | 0.594 | 0.267 | 3.13x | 11.0/15.9/19.1% | 1.1/3.3% | 3 |

> congestion-input=hotstore: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.953 | 0.951 | 0.002 | - | - | 0.997 | 0.997 | 0.788 | 1.81x | 19.5/26.7/30.1% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.946 | 0.943 | 0.003 | - | - | 0.997 | 0.997 | 0.763 | 1.89x | 20.5/28.0/31.5% | 1.2/5.0% | 3 |

> congestion-mode=adaptive: misdecodes 1

