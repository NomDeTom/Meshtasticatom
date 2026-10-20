# Sweep blocks-2026-10-20-3250205

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 3250205 · seeds 3250205
- **blocks** 87 run
- **compute** 19.5 h of simulator time across every cell
- **generated** 2026-10-20T09:30:04+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>278 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 30
- AD-amplifiers: slower: 4.26 s per simulated hour against 1.6 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-amplify-worst: amplify-worst=0.0: decode_failures 30
- AD-amplify-worst: slower: 4.01 s per simulated hour against 1.79 over 60 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=degree: decode_failures 14
- AD-badrouters: role-placement=inverse: decode_failures 33
- AD-badrouters: role-placement=random: decode_failures 20
- AD-badrouters: slower: 4.9 s per simulated hour against 1.83 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 14
- AD-flooding: role-mix=all-routers: decode_failures 14
- AD-flooding: slower: 5.92 s per simulated hour against 2.5 over 60 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 14
- AD-nomute: role-mix=no-mute: decode_failures 29
- AD-nomute: role-mix=all-routers: decode_failures 14
- AD-nomute: slower: 7.96 s per simulated hour against 2.28 over 60 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 14
- AD-worst: role-placement=degree: misdecodes 1
- AD-worst: faster: 1.59 s per simulated hour against 3.37 over 60 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DB-hotstore: max-num-nodes=10: decode_failures 19
- DB-hotstore: max-num-nodes=100: decode_failures 47
- DB-hotstore: max-num-nodes=120: decode_failures 47
- DB-hotstore: max-num-nodes=250: decode_failures 47
- DB-hotstore: slower: 12.9 s per simulated hour against 2.37 over 60 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 51
- DB-hotstore-stress: max-num-nodes=120: decode_failures 1
- DB-platform: platform-mix=uniform: decode_failures 47
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 47
- DB-platform: platform-mix=constrained: decode_failures 21
- DB-platform: slower: 12.4 s per simulated hour against 2.45 over 60 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: queue drops 15.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 74
- DB-warm: warm-num-nodes=25: queue drops 15.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 74
- DB-warm: warm-num-nodes=100: queue drops 15.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 74
- DB-warm: warm-num-nodes=2000: queue drops 15.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 74
- DG-burst: burst-loss=0.0: decode_failures 30
- DG-burst: burst-loss=0.1: decode_failures 32
- DG-burst: burst-loss=0.2: decode_failures 34
- DG-burst: burst-loss=0.3: decode_failures 23
- DG-loss: extra-loss=0.0: decode_failures 30
- DG-loss: extra-loss=0.1: decode_failures 33
- DG-loss: extra-loss=0.2: decode_failures 31
- DG-loss: extra-loss=0.3: decode_failures 24
- DG-loss: slower: 6.13 s per simulated hour against 2.25 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 30
- DG-outage: burst-loss=0.1: decode_failures 22
- DG-outage: burst-loss=0.2: decode_failures 24
- DG-outage: burst-loss=0.3: decode_failures 17
- DM-mode: dm-mode=flood-only: decode_failures 29
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 33
- DM-mode: dm-mode=m4-early-flood: decode_failures 31
- DM-mode: slower: 8.49 s per simulated hour against 2.89 over 60 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 30
- FW-firmware: slower: 3.76 s per simulated hour against 1.63 over 60 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.0: decode_failures 30
- FW-mixed-26: slower: 3.77 s per simulated hour against 1.68 over 60 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.0: decode_failures 30
- FW-mixed: slower: 3.68 s per simulated hour against 1.65 over 60 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-signing-cost: profile-flag=signing=false: decode_failures 42
- FW-signing-cost: profile-flag=signing=true: decode_failures 30
- FW-signing-cost: slower: 9.35 s per simulated hour against 1.58 over 60 prior run(s) - 5.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-versions: profile=2.8: decode_failures 30
- LD-chatty-hops: broadcast-interval-s=3600: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=900: decode_failures 22
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 12
- LD-chatty: broadcast-interval-s=3600: decode_failures 14
- LD-chatty: broadcast-interval-s=900: decode_failures 18
- LD-chatty: broadcast-interval-s=300: decode_failures 17
- LD-diurnal: diurnal=flat: decode_failures 27
- LD-diurnal: diurnal=sinusoid: decode_failures 32
- LD-diurnal: diurnal=commuter: decode_failures 30
- LD-diurnal: slower: 5.67 s per simulated hour against 1.52 over 60 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 18
- LD-interval: broadcast-interval-s=3600: decode_failures 14
- LD-interval: broadcast-interval-s=43200: decode_failures 30
- LD-interval: slower: 3.79 s per simulated hour against 1.31 over 60 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 30
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 32
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 13
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 26
- LD-traceroute: slower: 9.24 s per simulated hour against 2.1 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 15.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 74
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 20.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 90
- MS-density: nodes=60: decode_failures 30
- MS-density: nodes=150: misdecodes 1
- MS-hopscale: nodes=60: decode_failures 30
- MS-hopscale: nodes=250: decode_failures 3
- MS-hopscale: nodes=500: decode_failures 15
- MS-oversubscribed: nodes=250: decode_failures 1
- MS-oversubscribed: nodes=500: decode_failures 2
- MS-roles-fav: role-mix=legacy-default: decode_failures 35
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 7
- MS-roles-fav: slower: 7.83 s per simulated hour against 1.7 over 60 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-roles: role-mix=legacy-default: decode_failures 38
- MS-roles: role-mix=baymesh-2026-08: decode_failures 14
- MS-roles: slower: 5.45 s per simulated hour against 1.69 over 60 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 30
- MS-router-late: router-late-fraction=0.05: decode_failures 29
- MS-router-late: router-late-fraction=0.1: decode_failures 24
- MS-router-late: router-late-fraction=0.2: decode_failures 34
- MS-router-late: slower: 6.59 s per simulated hour against 1.72 over 60 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=uniform: decode_failures 30
- MS-siting: siting-mix=event: decode_failures 1
- MS-size: nodes=60: decode_failures 30
- MS-stretch: stretch=1.0: decode_failures 30
- MS-stretch: stretch=1.5: decode_failures 9
- MS-topology: topology=uniform: decode_failures 30
- MS-topology: topology=clustered: decode_failures 1
- MS-topology: topology=corridor: decode_failures 2
- MS-topology: slower: 4.44 s per simulated hour against 1.91 over 60 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-crladder: coding-rate-ladder=False: decode_failures 33
- PR-crladder: coding-rate-ladder=True: decode_failures 36
- PR-crladder: slower: 11.8 s per simulated hour against 2.74 over 60 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 36
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 28
- PR-dmmode-cr: slower: 11.1 s per simulated hour against 2.54 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 30
- PR-protocol: slower: 4.16 s per simulated hour against 1.39 over 60 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats-busy: extra-repeats=True: misdecodes 1
- PR-repeats: extra-repeats=False: decode_failures 30
- PR-repeats: extra-repeats=True: decode_failures 37
- PR-repeats: slower: 9.38 s per simulated hour against 1.64 over 60 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=SHORT_TURBO: decode_failures 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 3
- RF-duct: duct-per-hour=0.0: decode_failures 30
- RF-duct: duct-per-hour=0.25: decode_failures 33
- RF-duct: duct-per-hour=1.0: decode_failures 1
- RF-duct: slower: 5.53 s per simulated hour against 1.75 over 60 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=LONG_FAST: decode_failures 30
- RF-noise: noise-profile=none: decode_failures 30
- RF-noise: noise-profile=temporal: decode_failures 17
- RF-noise: noise-profile=transient: decode_failures 44
- RF-noise: noise-profile=periodic: decode_failures 18
- RF-noise: slower: 12.1 s per simulated hour against 4.92 over 60 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset: preset=LONG_FAST: decode_failures 30
- RF-preset: preset=LONG_MODERATE: decode_failures 23
- RF-preset: slower: 6.76 s per simulated hour against 2.84 over 60 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 1
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 1
- RF-preset-turbo: preset=LONG_FAST: decode_failures 30
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 26
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 18
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-pulse: slower: 4.3 s per simulated hour against 1.61 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 9
- RF-txpower: tx-power=30: decode_failures 30
- RF-txpower: tx-power=22: decode_failures 1
- RF-txpower: slower: 3.25 s per simulated hour against 1.58 over 60 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-favourites: favourite-routers=False: decode_failures 30
- RT-favourites: favourite-routers=True: decode_failures 30
- RT-favourites: slower: 9.85 s per simulated hour against 1.66 over 60 prior run(s) - 5.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 30
- RT-hopassign: hop-assign=random: decode_failures 36
- RT-hopassign: slower: 8.55 s per simulated hour against 1.76 over 60 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hoplimit: hop-limit=3: decode_failures 27
- RT-hoplimit: hop-limit=7: decode_failures 16
- RT-hoplimit: hop-limit=15: decode_failures 48
- RT-hoplimit: hop-limit=32: decode_failures 42
- RT-hoplimit: slower: 10.8 s per simulated hour against 1.75 over 60 prior run(s) - 6.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopspread: hop-limit=3: decode_failures 27
- RT-hopspread: hop-limit=5: decode_failures 43
- RT-hopspread: hop-limit=7: decode_failures 16
- RT-hopspread: slower: 9.71 s per simulated hour against 2.03 over 60 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 30
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 30
- RT-rebroadcast: slower: 6.93 s per simulated hour against 1.56 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-spread: hop-spread=False: decode_failures 27
- RT-spread: hop-spread=True: decode_failures 30
- RT-spread: slower: 9.4 s per simulated hour against 2.15 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 30
- SC-signing: signature-policy=BALANCED: decode_failures 30
- SC-signing: signature-policy=STRICT: decode_failures 22
- SC-signing: slower: 9.06 s per simulated hour against 1.78 over 60 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 30
- SF-advert-transport: slower: 6.54 s per simulated hour against 1.71 over 60 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-mode: bucket-mode=global: misdecodes 18
- SF-bucket-mode: bucket-mode=local: decode_failures 30
- SF-bucket-mode: bucket-mode=time: misdecodes 14
- SF-bucket-mode: bucket-mode=window: misdecodes 6
- SF-bucket-mode: slower: 4.05 s per simulated hour against 1.45 over 60 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-bucket-time: time-bucket-s=600: misdecodes 65
- SF-bucket-time: time-bucket-s=1800: misdecodes 14
- SF-bucket-time: time-bucket-s=3600: misdecodes 4
- SF-bucket-time: time-bucket-s=3600: decode_failures 8
- SF-cadence: trigger=bucket: decode_failures 30
- SF-cadence: trigger=interval: misdecodes 5
- SF-cadence: trigger=interval: decode_failures 37
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 18
- SF-cadence: trigger=bucket+interval: misdecodes 5
- SF-cadence: trigger=bucket+interval: decode_failures 22
- SF-cadence: slower: 11.7 s per simulated hour against 3.54 over 60 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 72
- SF-capacity-local: capacity=8: decode_failures 61
- SF-capacity-local: capacity=16: decode_failures 51
- SF-capacity-local: capacity=32: decode_failures 30
- SF-capacity-local: capacity=50: decode_failures 31
- SF-capacity-local: slower: 7.12 s per simulated hour against 1.73 over 60 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity: capacity=4: decode_failures 72
- SF-capacity: capacity=8: decode_failures 61
- SF-capacity: capacity=16: decode_failures 51
- SF-capacity: capacity=32: decode_failures 30
- SF-capacity: capacity=50: decode_failures 31
- SF-capacity: slower: 6.94 s per simulated hour against 1.7 over 60 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-window: capacity=8: misdecodes 5
- SF-capacity-window: capacity=8: decode_failures 75
- SF-capacity-window: capacity=16: misdecodes 3
- SF-capacity-window: capacity=16: decode_failures 47
- SF-capacity-window: capacity=32: misdecodes 6
- SF-catchup: catch-up-hours=: misdecodes 5
- SF-catchup: catch-up-hours=: decode_failures 22
- SF-catchup: catch-up-hours=02-06: decode_failures 50
- SF-catchup: catch-up-hours=00-08: decode_failures 55
- SF-hops-flat: hops-apart=2: decode_failures 30
- SF-hops-spread: hops-apart=2: decode_failures 30
- SF-hops-spread: hops-apart=5: decode_failures 1
- SF-jitter-global: advert-jitter-s=1: decode_failures 29
- SF-jitter-global: advert-jitter-s=30: decode_failures 30
- SF-jitter-global: advert-jitter-s=120: decode_failures 25
- SF-jitter-global: advert-jitter-s=600: decode_failures 41
- SF-jitter-global: slower: 8.27 s per simulated hour against 1.75 over 60 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 29
- SF-jitter-local: advert-jitter-s=30: decode_failures 30
- SF-jitter-local: advert-jitter-s=120: decode_failures 25
- SF-jitter-local: advert-jitter-s=600: decode_failures 41
- SF-jitter-local: slower: 6.15 s per simulated hour against 1.78 over 60 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 37
- SF-place-flat: place=random-clients: decode_failures 19
- SF-place-flat: place=hops-apart: decode_failures 30
- SF-place-spread: place=spread: decode_failures 37
- SF-place-spread: place=random-clients: decode_failures 19
- SF-place-spread: place=hops-apart: decode_failures 30
- SF-place-spread: slower: 5.57 s per simulated hour against 2.77 over 60 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-provide-transport: provide-transport=dm: decode_failures 30
- SF-provide-transport: provide-transport=broadcast: decode_failures 42
- SF-provide-transport: slower: 11.5 s per simulated hour against 1.76 over 60 prior run(s) - 6.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 42
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 23
- SF-replay-order-broadcast: slower: 10.4 s per simulated hour against 1.68 over 60 prior run(s) - 6.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 30
- SF-replay-order: replay-ordering=heard: misdecodes 3
- SF-replay-order: replay-ordering=heard: decode_failures 39
- SF-replay-order: slower: 6.48 s per simulated hour against 1.56 over 60 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-resolve: resolve=sketch: decode_failures 29
- SF-resolve: resolve=hybrid: decode_failures 30
- SF-resolve: slower: 4.32 s per simulated hour against 1.52 over 60 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=3: decode_failures 30
- SF-servers-flat: servers=5: decode_failures 21
- SF-servers-flat: servers=8: decode_failures 41
- SF-servers-flat: slower: 5.55 s per simulated hour against 2.29 over 60 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=3: decode_failures 30
- SF-servers-spread: servers=5: decode_failures 21
- SF-servers-spread: servers=8: decode_failures 41
- SF-servers-spread: slower: 5.86 s per simulated hour against 2.22 over 60 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 30
- SF-signed: signed=True: decode_failures 30
- SF-signed: slower: 10 s per simulated hour against 1.66 over 60 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 9
- SF-sr-retries: sr-retries=1: decode_failures 7
- SF-sr-retries: sr-retries=2: decode_failures 16
- SF-sr-retries: sr-retries=4: decode_failures 11
- SF-sr-retries: slower: 6.12 s per simulated hour against 1.51 over 60 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 45
- SF-width: short-id-bits=24: decode_failures 31
- SF-width: short-id-bits=32: decode_failures 30
- SF-width: short-id-bits=64: decode_failures 44
- SF-width: slower: 12 s per simulated hour against 1.65 over 60 prior run(s) - 7.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 94
- SF-window-size: window-size=16: misdecodes 36
- SF-window-size: window-size=32: misdecodes 6
- TH-congestion-input: congestion-input=hotstore: decode_failures 1
- TH-congestion: no-congestion-scaling=True: queue drops 12.5% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 20

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-width` | 12 | 1.65 | 7.29x | 60 |
| `SF-provide-transport` | 11.5 | 1.76 | 6.52x | 60 |
| `SF-replay-order-broadcast` | 10.4 | 1.68 | 6.19x | 60 |
| `RT-hoplimit` | 10.8 | 1.75 | 6.16x | 60 |
| `SF-signed` | 10 | 1.66 | 6.02x | 60 |
| `RT-favourites` | 9.85 | 1.66 | 5.93x | 60 |
| `FW-signing-cost` | 9.35 | 1.58 | 5.92x | 60 |
| `PR-repeats` | 9.38 | 1.64 | 5.72x | 60 |
| `DB-hotstore` | 12.9 | 2.37 | 5.45x | 60 |
| `SC-signing` | 9.06 | 1.78 | 5.08x | 60 |
| `DB-platform` | 12.4 | 2.45 | 5.07x | 60 |
| `RT-hopassign` | 8.55 | 1.76 | 4.87x | 60 |
| `RT-hopspread` | 9.71 | 2.03 | 4.78x | 60 |
| `SF-jitter-global` | 8.27 | 1.75 | 4.72x | 60 |
| `MS-roles-fav` | 7.83 | 1.7 | 4.59x | 60 |
| `RT-rebroadcast` | 6.93 | 1.56 | 4.43x | 60 |
| `LD-traceroute` | 9.24 | 2.1 | 4.41x | 60 |
| `PR-dmmode-cr` | 11.1 | 2.54 | 4.38x | 60 |
| `RT-spread` | 9.4 | 2.15 | 4.36x | 60 |
| `PR-crladder` | 11.8 | 2.74 | 4.30x | 60 |
| `SF-replay-order` | 6.48 | 1.56 | 4.15x | 60 |
| `SF-capacity-local` | 7.12 | 1.73 | 4.11x | 60 |
| `SF-capacity` | 6.94 | 1.7 | 4.09x | 60 |
| `SF-sr-retries` | 6.12 | 1.51 | 4.04x | 60 |
| `SF-advert-transport` | 6.54 | 1.71 | 3.83x | 60 |
| `MS-router-late` | 6.59 | 1.72 | 3.82x | 60 |
| `LD-diurnal` | 5.67 | 1.52 | 3.75x | 60 |
| `AD-nomute` | 7.96 | 2.28 | 3.49x | 60 |
| `SF-jitter-local` | 6.15 | 1.78 | 3.46x | 60 |
| `SF-cadence` | 11.7 | 3.54 | 3.30x | 60 |
| `MS-roles` | 5.45 | 1.69 | 3.23x | 60 |
| `RF-duct` | 5.53 | 1.75 | 3.16x | 60 |
| `PR-protocol` | 4.16 | 1.39 | 3.00x | 60 |
| `DM-mode` | 8.49 | 2.89 | 2.94x | 60 |
| `LD-interval` | 3.79 | 1.31 | 2.88x | 60 |
| `SF-resolve` | 4.32 | 1.52 | 2.85x | 60 |
| `SF-bucket-mode` | 4.05 | 1.45 | 2.79x | 60 |
| `DG-loss` | 6.13 | 2.25 | 2.73x | 60 |
| `AD-badrouters` | 4.9 | 1.83 | 2.68x | 60 |
| `RF-pulse` | 4.3 | 1.61 | 2.68x | 60 |
| `AD-amplifiers` | 4.26 | 1.6 | 2.67x | 60 |
| `SF-servers-spread` | 5.86 | 2.22 | 2.64x | 60 |
| `RF-noise` | 12.1 | 4.92 | 2.47x | 60 |
| `SF-servers-flat` | 5.55 | 2.29 | 2.42x | 60 |
| `RF-preset` | 6.76 | 2.84 | 2.38x | 60 |
| `AD-flooding` | 5.92 | 2.5 | 2.37x | 60 |
| `MS-topology` | 4.44 | 1.91 | 2.33x | 60 |
| `FW-firmware` | 3.76 | 1.63 | 2.31x | 60 |
| `FW-mixed-26` | 3.77 | 1.68 | 2.24x | 60 |
| `AD-amplify-worst` | 4.01 | 1.79 | 2.23x | 60 |
| `FW-mixed` | 3.68 | 1.65 | 2.22x | 60 |
| `RF-txpower` | 3.25 | 1.58 | 2.06x | 60 |
| `SF-place-spread` | 5.57 | 2.77 | 2.01x | 60 |
| `SF-place-flat` | 5.61 | 2.83 | 1.98x | 60 |
| `LD-chatty-hops` | 7.14 | 3.95 | 1.81x | 60 |
| `RF-eu-presets` | 3.3 | 1.86 | 1.78x | 60 |
| `SF-catchup` | 15.4 | 8.76 | 1.76x | 60 |
| `MS-siting` | 3.17 | 1.81 | 1.76x | 59 |
| `SF-bucket-time` | 2.69 | 1.57 | 1.71x | 60 |
| `RF-preset-turbo` | 2.61 | 1.53 | 1.70x | 56 |
| `SF-capacity-window` | 2.66 | 1.6 | 1.67x | 60 |
| `AD-siting` | 2.27 | 1.42 | 1.60x | 60 |
| `FW-versions` | 2.41 | 1.52 | 1.59x | 60 |
| `MS-density` | 5.08 | 3.23 | 1.57x | 60 |
| `MS-stretch` | 3.1 | 2.02 | 1.54x | 60 |
| `TH-congestion` | 11.5 | 17.2 | 0.67x | 60 |
| `MS-oversubscribed` | 12.7 | 19.9 | 0.64x | 60 |
| `AD-worst` | 1.59 | 3.37 | 0.47x | 60 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.981 | 0.981 | 0.809 → 0.819 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.919 | 0.919 | 0.792 → 0.819 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **held** | 0.141 → 0.999 | 0.858 | 0.230 → 0.976 | 16x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.152 → 0.939 | 0.786 | 0.063 → 0.811 | 8.7x sr_airtime | up | 5 |
| `AD-siting` | siting-mix | **text** | 0.050 → 0.832 | 0.783 | 0.050 → 0.809 | 9.3x sr_bytes | down | 3 |
| `RF-txpower` | tx-power | **held** | 0.145 → 0.919 | 0.774 | 0.081 → 0.811 | 9.9x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.112 → 0.855 | 0.744 | 0.105 → 0.739 | 1.7e+02x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.152 → 0.889 | 0.737 | 0.149 → 0.629 | 6.6x advert_bytes | up | 3 |
| `MS-stretch` | stretch | **text** | 0.125 → 0.834 | 0.710 | 0.124 → 0.811 | 6x sr_airtime | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.260 → 0.925 | 0.665 | 0.223 → 0.811 | 4.4x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.260 → 0.919 | 0.659 | 0.223 → 0.811 | 5.4x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.418 → 0.973 | 0.555 | 0.305 → 0.811 | 8.3x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.425 → 0.970 | 0.545 | 0.307 → 0.735 | 4.7x bytes_on_air | down | 3 |
| `MS-topology` | topology | **text** | 0.605 → 0.958 | 0.353 | 0.588 → 0.953 | 1.9x sr_bytes | up | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.620 → 0.964 | 0.344 | 0.505 → 0.847 | 11x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.493 → 0.834 | 0.341 | 0.458 → 0.811 | 1.5x advert_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.355 → 0.684 | 0.329 | 0.342 → 0.648 | 1.6x sr_airtime | up | 2 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.607 → 0.924 | 0.317 | 0.591 → 0.913 | 10x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.528 → 0.834 | 0.307 | 0.498 → 0.811 | 1.6x sr_bytes | down | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.730 → 0.963 | 0.234 | 0.716 → 0.959 | 4.5x sr_airtime | down | 2 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.527 → 0.760 | 0.233 | 0.309 → 0.522 | 5.1x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.719 → 0.930 | 0.211 | 0.683 → 0.923 | 1.5x bytes_on_air | up | 4 |
| `RF-noise` | noise-profile | **held** | 0.718 → 0.919 | 0.202 | 0.644 → 0.811 | 1.9x sr_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.719 → 0.915 | 0.196 | 0.683 → 0.902 | 1.4x sr_bytes | up | 3 |
| `MS-density` | nodes | **text** | 0.771 → 0.963 | 0.192 | 0.742 → 0.959 | 4.4x sr_airtime | up | 5 |
| `MS-size` | nodes | **text** | 0.712 → 0.889 | 0.177 | 0.704 → 0.875 | 5.1x sr_bytes | down | 5 |
| `SC-signing` | signature-policy | **held** | 0.761 → 0.919 | 0.158 | 0.695 → 0.811 | 1.3x sr_bytes | down | 3 |
| `SF-place-flat` | place | **held** | 0.821 → 0.953 | 0.132 | 0.804 → 0.816 | 4.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.821 → 0.953 | 0.132 | 0.804 → 0.816 | 4.6x sr_bytes | up | 6 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.834 → 0.960 | 0.126 | 0.811 → 0.959 | 2.7x sr_bytes | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.709 → 0.834 | 0.125 | 0.682 → 0.811 | 1.4x sr_bytes | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.845 → 0.963 | 0.118 | 0.813 → 0.820 | 4.6x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.719 → 0.834 | 0.115 | 0.683 → 0.811 | 1.4x sr_bytes | up | 2 |
| `DB-platform` | platform-mix | **text** | 0.761 → 0.873 | 0.112 | 0.737 → 0.858 | 2.4x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.763 → 0.873 | 0.110 | 0.739 → 0.858 | 2.4x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.810 → 0.919 | 0.109 | 0.811 → 0.820 | 29x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.844 → 0.953 | 0.109 | 0.779 → 0.811 | 14x advert_bytes | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.834 → 0.936 | 0.102 | 0.811 → 0.928 | 1.5x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.785 → 0.883 | 0.098 | 0.753 → 0.871 | 5.8x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.834 → 0.928 | 0.094 | 0.811 → 0.902 | 1.5x sr_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.834 → 0.918 | 0.084 | 0.811 → 0.914 | 3x bytes_on_air | down | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.742 → 0.824 | 0.083 | 0.629 → 0.683 | 1.3x sr_airtime | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.869 → 0.946 | 0.077 | 0.745 → 0.811 | 1.6x sr_airtime | down | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.868 → 0.944 | 0.076 | 0.805 → 0.830 | 1.5x sr_bytes | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.909 → 0.981 | 0.073 | 0.804 → 0.811 | 2.5x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.909 → 0.981 | 0.073 | 0.802 → 0.811 | 2.5x sr_bytes | up | 5 |
| `FW-firmware` | profile | **text** | 0.834 → 0.906 | 0.072 | 0.811 → 0.901 | 2.9x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **held** | 0.919 → 0.990 | 0.071 | 0.811 → 0.901 | 2x bytes_on_air | up | 4 |
| `AD-nomute` | role-mix | **held** | 0.902 → 0.970 | 0.068 | 0.809 → 0.878 | 2.3x bytes_on_air | up | 3 |
| `SF-resolve` | resolve | **held** | 0.867 → 0.935 | 0.068 | 0.808 → 0.811 | 5.6x advert_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.919 → 0.986 | 0.067 | 0.811 → 0.892 | 2x bytes_on_air | up | 4 |
| `AD-flooding` | role-mix | **held** | 0.904 → 0.970 | 0.066 | 0.809 → 0.878 | 2.3x bytes_on_air | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.892 → 0.953 | 0.062 | 0.783 → 0.818 | 9.3x advert_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.919 → 0.975 | 0.055 | 0.796 → 0.811 | 9.6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.919 → 0.975 | 0.055 | 0.796 → 0.811 | 9.6x sr_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.919 → 0.972 | 0.052 | 0.806 → 0.811 | 2.1x advert_bytes | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.912 → 0.963 | 0.050 | 0.805 → 0.814 | 2.4x advert_bytes | up | 4 |
| `RT-favourites` | favourite-routers | **held** | 0.872 → 0.921 | 0.049 | 0.808 → 0.842 | 1.3x sr_bytes | up | 2 |
| `FW-signing-cost` | profile-flag | **held** | 0.919 → 0.962 | 0.043 | 0.811 → 0.853 | 3.2x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.526 → 0.561 | 0.035 | 0.517 → 0.552 | 1.5x sr_airtime | up | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.888 → 0.919 | 0.031 | 0.796 → 0.811 | 3.9x sr_airtime | down | 2 |
| `SF-width` | short-id-bits | **held** | 0.919 → 0.948 | 0.028 | 0.802 → 0.813 | 3x advert_bytes | down | 4 |
| `MS-roles` | role-mix | **held** | 0.904 → 0.930 | 0.026 | 0.809 → 0.833 | 1.1x bytes_on_air | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.834 → 0.858 | 0.024 | 0.811 → 0.842 | 1.2x advert_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.912 → 0.935 | 0.023 | 0.810 → 0.817 | 5.1x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.912 → 0.935 | 0.023 | 0.810 → 0.817 | 5.1x advert_bytes | down | 5 |
| `MS-router-late` | router-late-fraction | **text** | 0.834 → 0.857 | 0.023 | 0.811 → 0.842 | 1.4x bytes_on_air | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.763 → 0.786 | 0.022 | 0.763 → 0.786 | 1.3x sr_airtime | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.812 → 0.832 | 0.020 | 0.787 → 0.809 | 1.2x sr_bytes | down | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.928 → 0.947 | 0.019 | 0.838 → 0.853 | 1.1x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.946 → 0.963 | 0.017 | 0.796 → 0.813 | 4.4x advert_bytes | up | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.872 → 0.888 | 0.016 | 0.795 → 0.796 | 1.2x sr_bytes | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.919 → 0.932 | 0.013 | 0.809 → 0.811 | 1.2x sr_bytes | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.924 → 0.936 | 0.012 | 0.800 → 0.816 | 3.2x sr_bytes | up | 2 |
| `AD-worst` | role-placement | **held** | 0.942 → 0.953 | 0.010 | 0.803 → 0.811 | 1.2x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.917 → 0.926 | 0.009 | 0.809 → 0.817 | 1.2x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.917 → 0.926 | 0.009 | 0.809 → 0.817 | 1.2x sr_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.930 → 0.939 | 0.009 | 0.801 → 0.811 | 5.1x advert_bytes | down | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.819 → 0.827 | 0.008 | 0.779 → 0.779 | 1.2x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.957 → 0.963 | 0.007 | 0.952 → 0.959 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.914 → 0.919 | 0.005 | 0.810 → 0.811 | 1.2x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.915 → 0.919 | 0.004 | 0.811 → 0.812 | 1.1x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.997 → 0.999 | 0.001 | 0.959 → 0.961 | 1.1x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.779 → 0.780 | 0.001 | 0.779 → 0.780 | 1x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.998 → 0.999 | 0.001 | 0.959 → 0.959 | 1x sr_bytes | down | 2 |

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
| none | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| sprinkled | 1 | 0.887 | 0.882 | 0.006 | - | - | 0.978 | 0.979 | 0.594 | 1.18x | 16.1/24.7/28.4% | 1.5/5.4% | 3 |
| arms-race | 1 | 0.960 | 0.959 | 0.002 | - | - | 0.989 | 0.989 | 0.904 | 1.03x | 19.6/25.9/28.7% | 1.4/5.2% | 3 |

> amplifier-mix=none: decode_failures 30

> slower: 4.26 s per simulated hour against 1.6 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.1 | 1 | 0.878 | 0.867 | 0.011 | - | - | 0.982 | 0.983 | 0.601 | 1.21x | 17.7/25.1/29.2% | 1.6/5.1% | 3 |
| 0.3 | 1 | 0.936 | 0.928 | 0.007 | - | - | 0.991 | 0.993 | 0.779 | 1.05x | 19.4/25.7/27.9% | 1.3/5.0% | 3 |

> amplify-worst=0.0: decode_failures 30

> slower: 4.01 s per simulated hour against 1.79 over 60 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.832 | 0.809 | 0.023 | - | - | 0.904 | 0.959 | 0.519 | 1.14x | 15.9/23.2/27.3% | 1.9/4.8% | 3 |
| inverse | 1 | 0.812 | 0.787 | 0.025 | - | - | 0.907 | 0.949 | 0.465 | 1.08x | 13.7/17.8/21.4% | 1.9/3.5% | 3 |
| random | 1 | 0.828 | 0.801 | 0.027 | - | - | 0.918 | 0.970 | 0.470 | 1.11x | 14.4/19.6/21.9% | 1.9/4.4% | 3 |

> role-placement=degree: decode_failures 14

> role-placement=inverse: decode_failures 33

> role-placement=random: decode_failures 20

> slower: 4.9 s per simulated hour against 1.83 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.832 | 0.809 | 0.023 | - | - | 0.904 | 0.959 | 0.519 | 1.14x | 15.9/23.2/27.3% | 1.9/4.8% | 3 |
| all-routers | 1 | 0.893 | 0.878 | 0.014 | - | - | 0.970 | 0.990 | 0.719 | 2.67x | 32.3/39.4/41.9% | 4.4/5.1% | 3 |

> role-mix=baymesh-2026-08: decode_failures 14

> role-mix=all-routers: decode_failures 14

> slower: 5.92 s per simulated hour against 2.5 over 60 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.832 | 0.809 | 0.023 | - | - | 0.904 | 0.959 | 0.519 | 1.14x | 15.9/23.2/27.3% | 1.9/4.8% | 3 |
| no-mute | 1 | 0.838 | 0.816 | 0.021 | - | - | 0.902 | 0.961 | 0.606 | 1.27x | 16.2/22.9/25.7% | 2.0/5.0% | 3 |
| all-routers | 1 | 0.893 | 0.878 | 0.014 | - | - | 0.970 | 0.990 | 0.719 | 2.67x | 32.3/39.4/41.9% | 4.4/5.1% | 3 |

> role-mix=baymesh-2026-08: decode_failures 14

> role-mix=no-mute: decode_failures 29

> role-mix=all-routers: decode_failures 14

> slower: 7.96 s per simulated hour against 2.28 over 60 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.832 | 0.809 | 0.023 | - | - | 0.904 | 0.959 | 0.519 | 1.14x | 15.9/23.2/27.3% | 1.9/4.8% | 3 |
| local-typical | 1 | 0.737 | 0.732 | 0.004 | - | - | 0.886 | 0.887 | 0.000 | 1.27x | 12.8/22.0/26.0% | 2.1/5.0% | 3 |
| basement-heavy | 1 | 0.050 | 0.050 | 0.000 | - | - | 0.152 | 0.156 | 0.000 | 0.46x | 0.7/6.0/9.6% | 0.2/2.2% | 3 |

> siting-mix=uniform: decode_failures 14

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.815 | 0.811 | 0.004 | - | - | 0.942 | 0.943 | 0.054 | 2.29x | 18.5/29.7/35.3% | 1.7/5.5% | 3 |
| inverse | 1 | 0.810 | 0.803 | 0.007 | - | - | 0.953 | 0.954 | 0.104 | 2.24x | 15.3/25.5/31.5% | 1.7/3.2% | 3 |

> role-placement=degree: misdecodes 1

> faster: 1.59 s per simulated hour against 3.37 over 60 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.819 | 0.819 | 0.000 | - | - | 0 | 0.000 | 0.575 | 1.21x | 16.1/22.5/25.8% | 1.7/4.8% | 3 |
| sr | 1 | 0.835 | 0.809 | 0.026 | - | - | 0.981 | 0.982 | 0.594 | 1.25x | 16.8/23.3/26.6% | 1.7/5.2% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.763 | 0.739 | 0.024 | - | - | 0.814 | 0.917 | 0.524 | 2.80x | 36.0/51.5/55.7% | 3.6/9.6% | 3 |
| 100 | 1 | 0.873 | 0.858 | 0.015 | - | - | 0.904 | 0.955 | 0.635 | 1.48x | 19.5/28.0/30.9% | 2.0/5.2% | 3 |
| 120 | 1 | 0.873 | 0.858 | 0.015 | - | - | 0.904 | 0.955 | 0.635 | 1.48x | 19.5/28.0/30.9% | 2.0/5.2% | 3 |
| 250 | 1 | 0.873 | 0.858 | 0.015 | - | - | 0.904 | 0.955 | 0.635 | 1.48x | 19.5/28.0/30.9% | 2.0/5.2% | 3 |

> max-num-nodes=10: decode_failures 19

> max-num-nodes=100: decode_failures 47

> max-num-nodes=120: decode_failures 47

> max-num-nodes=250: decode_failures 47

> slower: 12.9 s per simulated hour against 2.37 over 60 prior run(s) - 5.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.316 | 0.309 | 0.007 | - | - | 0.527 | 0.556 | 0.147 | 11.63x | 40.5/57.8/72.5% | 4.2/10.9% | 3 |
| 120 | 1 | 0.526 | 0.517 | 0.009 | - | - | 0.757 | 0.757 | 0.194 | 4.53x | 16.0/27.2/37.8% | 1.5/5.5% | 3 |
| 250 | 1 | 0.531 | 0.522 | 0.009 | - | - | 0.760 | 0.762 | 0.201 | 4.38x | 15.6/25.9/36.7% | 1.5/5.3% | 3 |

> max-num-nodes=10: decode_failures 51

> max-num-nodes=120: decode_failures 1

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.873 | 0.858 | 0.015 | - | - | 0.904 | 0.955 | 0.635 | 1.48x | 19.5/28.0/30.9% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.873 | 0.858 | 0.015 | - | - | 0.904 | 0.955 | 0.635 | 1.48x | 19.5/28.0/30.9% | 2.0/5.2% | 3 |
| constrained | 1 | 0.761 | 0.737 | 0.024 | - | - | 0.811 | 0.914 | 0.517 | 2.80x | 36.0/51.5/55.6% | 3.6/9.6% | 3 |

> platform-mix=uniform: decode_failures 47

> platform-mix=baymesh-2026-08: decode_failures 47

> platform-mix=constrained: decode_failures 21

> slower: 12.4 s per simulated hour against 2.45 over 60 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.695 | 0.683 | 0.012 | - | - | 0.824 | 0.871 | 0.516 | 5.67x | 60.8/75.3/79.7% | 4.2/13.2% | 3 |
| 25 | 1 | 0.695 | 0.683 | 0.012 | - | - | 0.824 | 0.871 | 0.516 | 5.67x | 60.8/75.3/79.7% | 4.2/13.2% | 3 |
| 100 | 1 | 0.695 | 0.683 | 0.012 | - | - | 0.824 | 0.871 | 0.516 | 5.67x | 60.8/75.3/79.7% | 4.2/13.2% | 3 |
| 2000 | 1 | 0.695 | 0.683 | 0.012 | - | - | 0.824 | 0.871 | 0.516 | 5.67x | 60.8/75.3/79.7% | 4.2/13.2% | 3 |

> warm-num-nodes=0: queue drops 15.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 74

> warm-num-nodes=25: queue drops 15.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 74

> warm-num-nodes=100: queue drops 15.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 74

> warm-num-nodes=2000: queue drops 15.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 74

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.1 | 1 | 0.738 | 0.704 | 0.034 | - | - | 0.883 | 0.954 | 0.479 | 1.19x | 16.2/22.5/25.7% | 1.7/4.6% | 3 |
| 0.2 | 1 | 0.643 | 0.597 | 0.046 | - | - | 0.813 | 0.899 | 0.379 | 1.10x | 15.0/20.8/24.0% | 1.6/4.1% | 3 |
| 0.3 | 1 | 0.528 | 0.498 | 0.030 | - | - | 0.647 | 0.840 | 0.298 | 0.99x | 13.7/19.4/22.0% | 1.4/3.6% | 3 |

> burst-loss=0.0: decode_failures 30

> burst-loss=0.1: decode_failures 32

> burst-loss=0.2: decode_failures 34

> burst-loss=0.3: decode_failures 23

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.1 | 1 | 0.793 | 0.765 | 0.028 | - | - | 0.897 | 0.954 | 0.524 | 1.30x | 17.4/24.3/27.4% | 1.9/5.0% | 3 |
| 0.2 | 1 | 0.755 | 0.734 | 0.021 | - | - | 0.840 | 0.951 | 0.472 | 1.36x | 18.2/25.3/28.2% | 2.0/4.8% | 3 |
| 0.3 | 1 | 0.709 | 0.682 | 0.027 | - | - | 0.823 | 0.932 | 0.434 | 1.36x | 18.2/25.3/28.1% | 2.0/4.5% | 3 |

> extra-loss=0.0: decode_failures 30

> extra-loss=0.1: decode_failures 33

> extra-loss=0.2: decode_failures 31

> extra-loss=0.3: decode_failures 24

> slower: 6.13 s per simulated hour against 2.25 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.1 | 1 | 0.734 | 0.709 | 0.025 | - | - | 0.837 | 0.939 | 0.470 | 1.19x | 16.0/22.1/25.4% | 1.7/4.5% | 3 |
| 0.2 | 1 | 0.606 | 0.577 | 0.029 | - | - | 0.713 | 0.898 | 0.384 | 1.13x | 15.4/21.6/24.8% | 1.6/4.4% | 3 |
| 0.3 | 1 | 0.493 | 0.458 | 0.036 | - | - | 0.610 | 0.826 | 0.293 | 1.03x | 14.2/19.6/22.5% | 1.5/3.5% | 3 |

> burst-loss=0.0: decode_failures 30

> burst-loss=0.1: decode_failures 22

> burst-loss=0.2: decode_failures 24

> burst-loss=0.3: decode_failures 17

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.763 | 0.763 | 0.000 | - | - | 0.818 | 0.953 | 0.537 | 1.64x | 21.7/30.2/34.3% | 2.3/6.3% | 3 |
| directed-with-late-flood | 1 | 0.779 | 0.779 | 0.000 | - | - | 0.819 | 0.961 | 0.532 | 1.47x | 19.5/27.6/31.4% | 2.0/5.8% | 3 |
| m4-early-flood | 1 | 0.786 | 0.786 | 0.000 | - | - | 0.815 | 0.966 | 0.551 | 1.46x | 19.3/27.2/31.1% | 2.0/5.7% | 3 |

> dm-mode=flood-only: decode_failures 29

> dm-mode=directed-with-late-flood: decode_failures 33

> dm-mode=m4-early-flood: decode_failures 31

> slower: 8.49 s per simulated hour against 2.89 over 60 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.906 | 0.901 | 0.004 | - | - | 0.989 | 0.991 | 0.710 | 0.77x | 9.1/12.9/14.8% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> profile=2.8: decode_failures 30

> slower: 3.76 s per simulated hour against 1.63 over 60 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.25 | 1 | 0.891 | 0.887 | 0.004 | - | - | 0.969 | 0.972 | 0.684 | 1.19x | 14.8/23.9/27.0% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.964 | 0.967 | 0.547 | 1.05x | 13.4/19.7/21.9% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.990 | 0.991 | 0.742 | 0.90x | 11.7/16.4/19.4% | 1.5/3.5% | 3 |

> legacy-fraction=0.0: decode_failures 30

> slower: 3.68 s per simulated hour against 1.65 over 60 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.25 | 1 | 0.890 | 0.885 | 0.005 | - | - | 0.969 | 0.971 | 0.637 | 1.16x | 14.5/23.6/26.5% | 1.6/4.7% | 3 |
| 0.5 | 1 | 0.867 | 0.862 | 0.004 | - | - | 0.960 | 0.962 | 0.623 | 1.03x | 13.2/19.8/21.7% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.895 | 0.892 | 0.004 | - | - | 0.986 | 0.988 | 0.714 | 0.87x | 11.6/16.2/19.5% | 1.4/3.6% | 3 |

> legacy-fraction=0.0: decode_failures 30

> slower: 3.77 s per simulated hour against 1.68 over 60 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.868 | 0.853 | 0.015 | - | - | 0.962 | 0.984 | 0.612 | 0.69x | 9.6/13.5/15.8% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> profile-flag=signing=false: decode_failures 42

> profile-flag=signing=true: decode_failures 30

> slower: 9.35 s per simulated hour against 1.58 over 60 prior run(s) - 5.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.898 | 0.891 | 0.006 | - | - | 0.987 | 0.988 | 0.714 | 0.76x | 9.2/13.6/16.4% | 1.2/2.4% | 3 |
| 2.5 | 1 | 0.897 | 0.892 | 0.005 | - | - | 0.993 | 0.994 | 0.703 | 0.76x | 9.1/13.5/16.1% | 1.2/2.3% | 3 |
| 2.6 | 1 | 0.893 | 0.889 | 0.004 | - | - | 0.989 | 0.990 | 0.681 | 0.74x | 9.1/13.5/16.3% | 1.2/2.4% | 3 |
| 2.7 | 1 | 0.918 | 0.914 | 0.004 | - | - | 0.990 | 0.990 | 0.706 | 0.81x | 9.5/17.9/20.8% | 1.2/3.2% | 3 |
| 2.8 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> profile=2.8: decode_failures 30

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.866 | 0.847 | 0.019 | - | - | 0.964 | 0.981 | 0.625 | 0.84x | 11.4/15.8/18.3% | 1.2/3.5% | 3 |
| 900 | 1 | 0.785 | 0.753 | 0.032 | - | - | 0.887 | 0.953 | 0.528 | 1.95x | 25.7/35.7/40.5% | 2.8/7.6% | 3 |
| 300 | 1 | 0.526 | 0.505 | 0.021 | - | - | 0.620 | 0.840 | 0.318 | 4.23x | 51.2/70.2/75.1% | 6.1/14.2% | 3 |

> broadcast-interval-s=3600: decode_failures 14

> broadcast-interval-s=900: decode_failures 18

> broadcast-interval-s=300: decode_failures 17

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.924 | 0.913 | 0.011 | - | - | 0.975 | 0.983 | 0.747 | 0.95x | 12.7/16.9/19.4% | 1.4/3.5% | 3 |
| 900 | 1 | 0.881 | 0.864 | 0.017 | - | - | 0.942 | 0.970 | 0.654 | 2.23x | 29.0/38.7/43.5% | 3.2/8.1% | 3 |
| 300 | 1 | 0.607 | 0.591 | 0.016 | - | - | 0.670 | 0.841 | 0.301 | 4.76x | 55.8/73.4/78.1% | 7.2/15.2% | 3 |

> broadcast-interval-s=3600: decode_failures 2

> broadcast-interval-s=900: decode_failures 22

> broadcast-interval-s=300: decode_failures 12

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.858 | 0.842 | 0.017 | - | - | 0.934 | 0.975 | 0.622 | 1.14x | 15.5/21.2/24.4% | 1.6/4.6% | 3 |
| sinusoid | 1 | 0.842 | 0.823 | 0.019 | - | - | 0.921 | 0.970 | 0.600 | 1.14x | 15.2/21.1/24.2% | 1.6/4.5% | 3 |
| commuter | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> diurnal=flat: decode_failures 27

> diurnal=sinusoid: decode_failures 32

> diurnal=commuter: decode_failures 30

> slower: 5.67 s per simulated hour against 1.52 over 60 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.785 | 0.753 | 0.032 | - | - | 0.887 | 0.953 | 0.528 | 1.95x | 25.7/35.7/40.5% | 2.8/7.6% | 3 |
| 3600 | 1 | 0.866 | 0.847 | 0.019 | - | - | 0.964 | 0.981 | 0.625 | 0.84x | 11.4/15.8/18.3% | 1.2/3.5% | 3 |
| 10800 | 1 | 0.879 | 0.862 | 0.018 | - | - | 0.979 | 0.984 | 0.612 | 0.56x | 7.6/10.4/12.1% | 0.8/2.3% | 3 |
| 43200 | 1 | 0.883 | 0.871 | 0.013 | - | - | 0.955 | 0.988 | 0.633 | 0.40x | 5.3/7.3/8.5% | 0.5/1.6% | 3 |

> broadcast-interval-s=900: decode_failures 18

> broadcast-interval-s=3600: decode_failures 14

> broadcast-interval-s=43200: decode_failures 30

> slower: 3.79 s per simulated hour against 1.31 over 60 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.25 | 1 | 0.829 | 0.806 | 0.023 | - | - | 0.918 | 0.975 | 0.556 | 1.32x | 17.6/24.4/28.1% | 1.8/5.3% | 3 |
| 1.0 | 1 | 0.821 | 0.785 | 0.036 | - | - | 0.946 | 0.969 | 0.542 | 1.42x | 19.1/26.8/30.6% | 2.0/5.8% | 3 |
| 4.0 | 1 | 0.773 | 0.745 | 0.029 | - | - | 0.869 | 0.947 | 0.510 | 1.80x | 24.4/33.9/38.9% | 2.5/7.1% | 3 |

> traceroute-per-hour=0.0: decode_failures 30

> traceroute-per-hour=0.25: decode_failures 32

> traceroute-per-hour=1.0: decode_failures 13

> traceroute-per-hour=4.0: decode_failures 26

> slower: 9.24 s per simulated hour against 2.1 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.695 | 0.683 | 0.012 | - | - | 0.824 | 0.871 | 0.516 | 5.67x | 60.8/75.3/79.7% | 4.2/13.2% | 3 |
| 1.0 | 1 | 0.638 | 0.629 | 0.009 | - | - | 0.742 | 0.823 | 0.463 | 6.10x | 63.7/76.6/80.4% | 4.5/14.2% | 3 |

> traceroute-per-hour=0.0: queue drops 15.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 74

> traceroute-per-hour=1.0: queue drops 20.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 90

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.771 | 0.742 | 0.030 | - | - | 0.927 | 0.948 | 0.559 | 1.34x | 18.7/30.5/34.0% | 3.1/6.6% | 3 |
| 60 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 90 | 1 | 0.951 | 0.946 | 0.004 | - | - | 0.990 | 0.992 | 0.844 | 1.61x | 18.8/27.5/32.9% | 1.4/4.7% | 3 |
| 120 | 1 | 0.963 | 0.959 | 0.004 | - | - | 0.999 | 0.999 | 0.877 | 2.01x | 23.0/38.8/42.5% | 1.3/4.9% | 3 |
| 150 | 1 | 0.961 | 0.959 | 0.001 | - | - | 0.999 | 1.000 | 0.826 | 2.47x | 27.7/40.7/45.0% | 1.2/5.8% | 3 |

> nodes=60: decode_failures 30

> nodes=150: misdecodes 1

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 120 | 1 | 0.758 | 0.744 | 0.015 | - | - | 0.973 | 0.973 | 0.448 | 2.08x | 15.3/22.5/26.1% | 1.5/4.5% | 3 |
| 250 | 1 | 0.521 | 0.511 | 0.009 | - | - | 0.758 | 0.759 | 0.189 | 4.82x | 17.2/28.9/40.3% | 1.6/5.9% | 3 |
| 500 | 1 | 0.311 | 0.305 | 0.006 | - | - | 0.418 | 0.418 | 0.088 | 10.03x | 19.1/29.3/49.9% | 1.7/6.6% | 3 |

> nodes=60: decode_failures 30

> nodes=250: decode_failures 3

> nodes=500: decode_failures 15

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.751 | 0.735 | 0.016 | - | - | 0.970 | 0.971 | 0.436 | 1.96x | 14.6/21.1/24.3% | 1.4/4.2% | 3 |
| 250 | 1 | 0.526 | 0.517 | 0.009 | - | - | 0.757 | 0.757 | 0.194 | 4.53x | 16.0/27.2/37.8% | 1.5/5.5% | 3 |
| 500 | 1 | 0.313 | 0.307 | 0.006 | - | - | 0.425 | 0.425 | 0.089 | 9.11x | 17.3/26.7/44.8% | 1.5/5.8% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 2

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.854 | 0.833 | 0.021 | - | - | 0.930 | 0.970 | 0.630 | 1.27x | 17.0/23.5/26.8% | 1.8/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.832 | 0.809 | 0.023 | - | - | 0.904 | 0.959 | 0.519 | 1.14x | 15.9/23.2/27.3% | 1.9/4.8% | 3 |

> role-mix=legacy-default: decode_failures 38

> role-mix=baymesh-2026-08: decode_failures 14

> slower: 5.45 s per simulated hour against 1.69 over 60 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.872 | 0.853 | 0.019 | - | - | 0.928 | 0.973 | 0.656 | 1.29x | 17.3/23.6/26.7% | 1.8/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.861 | 0.838 | 0.024 | - | - | 0.947 | 0.963 | 0.586 | 1.28x | 17.2/25.8/29.3% | 2.2/4.8% | 3 |

> role-mix=legacy-default: decode_failures 35

> role-mix=baymesh-2026-08: decode_failures 7

> slower: 7.83 s per simulated hour against 1.7 over 60 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.05 | 1 | 0.838 | 0.819 | 0.018 | - | - | 0.919 | 0.967 | 0.569 | 1.34x | 18.1/25.3/29.5% | 1.8/5.0% | 3 |
| 0.1 | 1 | 0.852 | 0.833 | 0.018 | - | - | 0.939 | 0.970 | 0.575 | 1.47x | 20.8/29.2/33.0% | 1.9/5.1% | 3 |
| 0.2 | 1 | 0.857 | 0.842 | 0.015 | - | - | 0.921 | 0.963 | 0.648 | 1.69x | 24.1/34.2/36.8% | 2.3/5.0% | 3 |

> router-late-fraction=0.0: decode_failures 30

> router-late-fraction=0.05: decode_failures 29

> router-late-fraction=0.1: decode_failures 24

> router-late-fraction=0.2: decode_failures 34

> slower: 6.59 s per simulated hour against 1.72 over 60 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| local-typical | 1 | 0.719 | 0.712 | 0.007 | - | - | 0.866 | 0.869 | 0.000 | 1.36x | 14.7/21.7/23.8% | 2.3/5.0% | 3 |
| event | 1 | 0.232 | 0.230 | 0.002 | - | - | 0.141 | 0.190 | 0.000 | 1.30x | 7.3/14.1/16.0% | 2.2/4.4% | 3 |
| backbone | 1 | 0.976 | 0.976 | 0.001 | - | - | 0.999 | 0.999 | 0.881 | 1.12x | 26.6/35.7/38.7% | 1.3/5.6% | 3 |

> siting-mix=uniform: decode_failures 30

> siting-mix=event: decode_failures 1

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.866 | 0.848 | 0.017 | - | - | 0.939 | 0.945 | 0.618 | 1.33x | 25.2/32.9/41.0% | 3.0/7.6% | 3 |
| 60 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 90 | 1 | 0.889 | 0.875 | 0.014 | - | - | 0.969 | 0.971 | 0.598 | 1.59x | 15.4/22.3/25.0% | 1.5/5.2% | 3 |
| 120 | 1 | 0.758 | 0.744 | 0.015 | - | - | 0.973 | 0.973 | 0.448 | 2.08x | 15.3/22.5/26.1% | 1.5/4.5% | 3 |
| 150 | 1 | 0.712 | 0.704 | 0.008 | - | - | 0.965 | 0.966 | 0.352 | 2.81x | 16.5/25.0/31.9% | 1.6/5.0% | 3 |

> nodes=60: decode_failures 30

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 1.25 | 1 | 0.618 | 0.607 | 0.011 | - | - | 0.850 | 0.853 | 0.079 | 1.30x | 12.7/20.8/22.3% | 2.0/4.8% | 3 |
| 1.5 | 1 | 0.355 | 0.342 | 0.014 | - | - | 0.570 | 0.614 | 0.000 | 1.38x | 9.8/15.7/21.0% | 2.2/4.7% | 3 |
| 2.0 | 1 | 0.125 | 0.124 | 0.001 | - | - | 0.274 | 0.277 | 0.000 | 0.84x | 4.5/7.3/10.0% | 1.4/2.5% | 3 |

> stretch=1.0: decode_failures 30

> stretch=1.5: decode_failures 9

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| clustered | 1 | 0.948 | 0.945 | 0.003 | - | - | 0.994 | 0.996 | 0.000 | 1.16x | 31.8/37.4/39.2% | 1.4/5.7% | 3 |
| corridor | 1 | 0.605 | 0.588 | 0.017 | - | - | 0.855 | 0.874 | 0.247 | 1.23x | 14.3/22.3/26.6% | 1.7/5.0% | 3 |
| hub | 1 | 0.958 | 0.953 | 0.005 | - | - | 0.995 | 0.996 | 0.849 | 1.15x | 29.7/37.4/38.2% | 1.5/5.6% | 3 |

> topology=uniform: decode_failures 30

> topology=clustered: decode_failures 1

> topology=corridor: decode_failures 2

> slower: 4.44 s per simulated hour against 1.91 over 60 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.779 | 0.779 | 0.000 | - | - | 0.819 | 0.961 | 0.532 | 1.47x | 19.5/27.6/31.4% | 2.0/5.8% | 3 |
| True | 1 | 0.779 | 0.779 | 0.000 | - | - | 0.827 | 0.965 | 0.542 | 1.48x | 19.6/27.9/31.7% | 2.0/5.8% | 3 |

> coding-rate-ladder=False: decode_failures 33

> coding-rate-ladder=True: decode_failures 36

> slower: 11.8 s per simulated hour against 2.74 over 60 prior run(s) - 4.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.779 | 0.779 | 0.000 | - | - | 0.827 | 0.965 | 0.542 | 1.48x | 19.6/27.9/31.7% | 2.0/5.8% | 3 |
| m4-early-flood | 1 | 0.780 | 0.780 | 0.000 | - | - | 0.827 | 0.973 | 0.562 | 1.47x | 19.6/27.7/31.4% | 2.0/5.8% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 36

> dm-mode=m4-early-flood: decode_failures 28

> slower: 11.1 s per simulated hour against 2.54 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.819 | 0.819 | 0.000 | - | - | 0 | 0.000 | 0.575 | 1.21x | 16.1/22.5/25.8% | 1.7/4.8% | 3 |
| chain | 1 | 0.798 | 0.792 | 0.005 | - | - | 0.819 | 0.969 | 0.546 | 1.44x | 19.1/26.7/30.2% | 2.1/5.6% | 3 |
| sr | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> protocol=sr: decode_failures 30

> slower: 4.16 s per simulated hour against 1.39 over 60 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| True | 1 | 0.833 | 0.812 | 0.021 | - | - | 0.915 | 0.975 | 0.582 | 1.29x | 17.2/23.9/27.3% | 1.9/5.1% | 3 |

> extra-repeats=False: decode_failures 30

> extra-repeats=True: decode_failures 37

> slower: 9.38 s per simulated hour against 1.64 over 60 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.963 | 0.959 | 0.004 | - | - | 0.999 | 0.999 | 0.877 | 2.01x | 23.0/38.8/42.5% | 1.3/4.9% | 3 |
| True | 1 | 0.964 | 0.959 | 0.005 | - | - | 0.998 | 0.998 | 0.879 | 2.03x | 23.2/39.0/42.6% | 1.4/4.9% | 3 |

> extra-repeats=True: misdecodes 1

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.149 | 0.149 | 0.001 | - | - | 0.152 | 0.157 | 0.000 | 0.04x | 0.2/0.4/0.6% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.387 | 0.371 | 0.015 | - | - | 0.600 | 0.618 | 0.000 | 0.26x | 2.0/3.3/4.9% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.636 | 0.629 | 0.007 | - | - | 0.889 | 0.890 | 0.249 | 1.22x | 10.7/21.2/23.4% | 1.7/5.1% | 3 |

> preset=SHORT_TURBO: decode_failures 1

> preset=MEDIUM_TURBO: decode_failures 3

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 0.25 | 1 | 0.858 | 0.826 | 0.031 | - | - | 0.943 | 0.982 | 0.620 | 1.21x | 18.3/25.1/28.3% | 1.7/5.1% | 3 |
| 1.0 | 1 | 0.928 | 0.902 | 0.026 | - | - | 0.985 | 0.989 | 0.783 | 0.98x | 23.3/30.1/31.3% | 1.3/5.3% | 3 |

> duct-per-hour=0.0: decode_failures 30

> duct-per-hour=0.25: decode_failures 33

> duct-per-hour=1.0: decode_failures 1

> slower: 5.53 s per simulated hour against 1.75 over 60 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.224 | 0.223 | 0.002 | - | - | 0.260 | 0.264 | 0.000 | 0.12x | 0.8/1.3/1.8% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| LITE_FAST | 1 | 0.741 | 0.721 | 0.020 | - | - | 0.909 | 0.914 | 0.357 | 0.90x | 9.9/16.6/17.8% | 1.2/3.9% | 3 |
| NARROW_SLOW | 1 | 0.771 | 0.746 | 0.025 | - | - | 0.925 | 0.926 | 0.446 | 1.16x | 13.4/20.8/23.8% | 1.7/5.0% | 3 |

> preset=LONG_FAST: decode_failures 30

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| temporal | 1 | 0.720 | 0.702 | 0.018 | - | - | 0.747 | 0.935 | 0.348 | 1.23x | 15.9/22.2/25.9% | 1.8/4.6% | 3 |
| transient | 1 | 0.829 | 0.806 | 0.023 | - | - | 0.915 | 0.970 | 0.589 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| periodic | 1 | 0.660 | 0.644 | 0.016 | - | - | 0.718 | 0.812 | 0.440 | 1.15x | 15.4/21.5/24.5% | 1.6/4.3% | 3 |

> noise-profile=none: decode_failures 30

> noise-profile=temporal: decode_failures 17

> noise-profile=transient: decode_failures 44

> noise-profile=periodic: decode_failures 18

> slower: 12.1 s per simulated hour against 4.92 over 60 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.224 | 0.223 | 0.002 | - | - | 0.260 | 0.264 | 0.000 | 0.12x | 0.8/1.3/1.8% | 0.2/0.4% | 3 |
| LONG_FAST | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| LONG_MODERATE | 1 | 0.799 | 0.781 | 0.018 | - | - | 0.913 | 0.947 | 0.624 | 3.18x | 45.7/58.2/63.3% | 4.7/11.6% | 3 |

> preset=LONG_FAST: decode_failures 30

> preset=LONG_MODERATE: decode_failures 23

> slower: 6.76 s per simulated hour against 2.84 over 60 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.064 | 0.063 | 0.001 | - | - | 0.153 | 0.235 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.149 | 0.149 | 0.001 | - | - | 0.152 | 0.157 | 0.000 | 0.04x | 0.2/0.4/0.6% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| LONG_TURBO | 1 | 0.636 | 0.629 | 0.007 | - | - | 0.889 | 0.890 | 0.249 | 1.22x | 10.7/21.2/23.4% | 1.7/5.1% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.828 | 0.803 | 0.025 | - | - | 0.939 | 0.942 | 0.581 | 1.72x | 21.5/29.7/34.3% | 2.3/6.7% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 1

> preset=SHORT_TURBO: decode_failures 1

> preset=LONG_FAST: decode_failures 30

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.762 | 0.739 | 0.022 | - | - | 0.855 | 0.904 | 0.509 | 1.22x | 16.4/23.0/26.2% | 1.7/4.8% | 3 |
| 10000 | 1 | 0.660 | 0.644 | 0.016 | - | - | 0.718 | 0.812 | 0.440 | 1.15x | 15.4/21.5/24.5% | 1.6/4.3% | 3 |
| 4000 | 1 | 0.409 | 0.403 | 0.006 | - | - | 0.446 | 0.587 | 0.245 | 1.02x | 13.8/18.9/21.3% | 1.5/3.3% | 3 |
| 2000 | 1 | 0.105 | 0.105 | 0.000 | - | - | 0.112 | 0.203 | 0.055 | 0.73x | 10.1/14.3/15.7% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 26

> noise-pulse-interval-ms=10000: decode_failures 18

> noise-pulse-interval-ms=4000: decode_failures 3

> slower: 4.3 s per simulated hour against 1.61 over 60 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.355 | 0.342 | 0.014 | - | - | 0.570 | 0.614 | 0.000 | 1.38x | 9.8/15.7/21.0% | 2.2/4.7% | 3 |
| 1.0 | 1 | 0.684 | 0.648 | 0.035 | - | - | 0.786 | 0.798 | 0.443 | 1.01x | 15.6/21.6/23.7% | 1.4/4.6% | 3 |

> duct-per-hour=0.0: decode_failures 9

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 22 | 1 | 0.347 | 0.331 | 0.016 | - | - | 0.540 | 0.588 | 0.000 | 1.36x | 10.2/17.3/20.7% | 2.1/4.6% | 3 |
| 17 | 1 | 0.140 | 0.139 | 0.001 | - | - | 0.145 | 0.147 | 0.000 | 0.95x | 5.2/8.4/11.9% | 1.5/3.1% | 3 |
| 14 | 1 | 0.081 | 0.081 | 0.001 | - | - | 0.231 | 0.236 | 0.000 | 0.61x | 2.8/5.4/7.9% | 0.9/2.2% | 3 |

> tx-power=30: decode_failures 30

> tx-power=22: decode_failures 1

> slower: 3.25 s per simulated hour against 1.58 over 60 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.963 | 0.959 | 0.004 | - | - | 0.999 | 0.999 | 0.877 | 2.01x | 23.0/38.8/42.5% | 1.3/4.9% | 3 |
| True | 1 | 0.957 | 0.952 | 0.005 | - | - | 0.998 | 0.998 | 0.860 | 2.34x | 26.3/43.3/47.2% | 1.6/5.4% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.827 | 0.808 | 0.018 | - | - | 0.872 | 0.962 | 0.556 | 1.32x | 17.7/24.8/28.5% | 1.8/5.0% | 3 |
| True | 1 | 0.859 | 0.842 | 0.018 | - | - | 0.921 | 0.962 | 0.593 | 1.39x | 18.4/25.3/29.0% | 1.9/5.2% | 3 |

> favourite-routers=False: decode_failures 30

> favourite-routers=True: decode_failures 30

> slower: 9.85 s per simulated hour against 1.66 over 60 prior run(s) - 5.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| random | 1 | 0.838 | 0.810 | 0.028 | - | - | 0.914 | 0.959 | 0.616 | 1.28x | 17.0/23.6/26.7% | 1.8/5.0% | 3 |

> hop-assign=centrality: decode_failures 30

> hop-assign=random: decode_failures 36

> slower: 8.55 s per simulated hour against 1.76 over 60 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.719 | 0.683 | 0.036 | - | - | 0.828 | 0.954 | 0.338 | 1.00x | 13.7/20.9/23.6% | 1.3/4.6% | 3 |
| 7 | 1 | 0.915 | 0.902 | 0.013 | - | - | 0.964 | 0.980 | 0.728 | 1.41x | 18.7/24.9/28.2% | 2.0/5.2% | 3 |
| 15 | 1 | 0.930 | 0.923 | 0.007 | - | - | 0.963 | 0.983 | 0.751 | 1.43x | 19.0/25.2/28.7% | 2.1/5.2% | 3 |
| 32 | 1 | 0.929 | 0.921 | 0.008 | - | - | 0.967 | 0.984 | 0.766 | 1.44x | 19.0/25.3/28.8% | 2.1/5.3% | 3 |

> hop-limit=3: decode_failures 27

> hop-limit=7: decode_failures 16

> hop-limit=15: decode_failures 48

> hop-limit=32: decode_failures 42

> slower: 10.8 s per simulated hour against 1.75 over 60 prior run(s) - 6.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.719 | 0.683 | 0.036 | - | - | 0.828 | 0.954 | 0.338 | 1.00x | 13.7/20.9/23.6% | 1.3/4.6% | 3 |
| 5 | 1 | 0.860 | 0.842 | 0.018 | - | - | 0.927 | 0.974 | 0.587 | 1.27x | 17.0/23.3/26.6% | 1.8/5.0% | 3 |
| 7 | 1 | 0.915 | 0.902 | 0.013 | - | - | 0.964 | 0.980 | 0.728 | 1.41x | 18.7/24.9/28.2% | 2.0/5.2% | 3 |

> hop-limit=3: decode_failures 27

> hop-limit=5: decode_failures 43

> hop-limit=7: decode_failures 16

> slower: 9.71 s per simulated hour against 2.03 over 60 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| KNOWN_ONLY | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.820 | 0.820 | 0.000 | - | - | 0.810 | 0.975 | 0.578 | 1.21x | 16.2/22.5/25.9% | 1.7/4.9% | 3 |

> rebroadcast-mode=ALL: decode_failures 30

> rebroadcast-mode=KNOWN_ONLY: decode_failures 30

> slower: 6.93 s per simulated hour against 1.56 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.719 | 0.683 | 0.036 | - | - | 0.828 | 0.954 | 0.338 | 1.00x | 13.7/20.9/23.6% | 1.3/4.6% | 3 |
| True | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> hop-spread=False: decode_failures 27

> hop-spread=True: decode_failures 30

> slower: 9.4 s per simulated hour against 2.15 over 60 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| BALANCED | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| STRICT | 1 | 0.695 | 0.695 | 0.000 | - | - | 0.761 | 0.847 | 0.467 | 1.35x | 17.9/24.7/28.2% | 2.0/5.2% | 3 |

> signature-policy=COMPATIBLE: decode_failures 30

> signature-policy=BALANCED: decode_failures 30

> signature-policy=STRICT: decode_failures 22

> slower: 9.06 s per simulated hour against 1.78 over 60 prior run(s) - 5.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| dm | 1 | 0.835 | 0.806 | 0.029 | - | - | 0.972 | 0.976 | 0.578 | 1.22x | 16.4/23.2/26.5% | 1.7/5.1% | 3 |

> advert-transport=broadcast: decode_failures 30

> slower: 6.54 s per simulated hour against 1.71 over 60 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.834 | 0.814 | 0.020 | - | - | 0.912 | 0.974 | 0.560 | 1.25x | 16.7/23.3/26.7% | 1.8/5.0% | 3 |
| local | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| time | 1 | 0.830 | 0.805 | 0.025 | - | - | 0.930 | 0.964 | 0.575 | 1.27x | 16.9/23.8/27.0% | 1.8/5.1% | 3 |
| window | 1 | 0.841 | 0.813 | 0.028 | - | - | 0.963 | 0.981 | 0.565 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> bucket-mode=global: misdecodes 18

> bucket-mode=local: decode_failures 30

> bucket-mode=time: misdecodes 14

> bucket-mode=window: misdecodes 6

> slower: 4.05 s per simulated hour against 1.45 over 60 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.831 | 0.801 | 0.030 | - | - | 0.939 | 0.973 | 0.538 | 1.37x | 18.3/25.4/29.0% | 1.9/5.5% | 3 |
| 1800 | 1 | 0.830 | 0.805 | 0.025 | - | - | 0.930 | 0.964 | 0.575 | 1.27x | 16.9/23.8/27.0% | 1.8/5.1% | 3 |
| 3600 | 1 | 0.838 | 0.811 | 0.026 | - | - | 0.938 | 0.976 | 0.585 | 1.24x | 16.5/23.1/26.4% | 1.7/5.0% | 3 |

> time-bucket-s=600: misdecodes 65

> time-bucket-s=1800: misdecodes 14

> time-bucket-s=3600: misdecodes 4

> time-bucket-s=3600: decode_failures 8

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| interval | 1 | 0.811 | 0.779 | 0.032 | - | - | 0.942 | 0.957 | 0.537 | 1.69x | 22.2/31.5/36.0% | 2.3/7.0% | 3 |
| aimd | 1 | 0.815 | 0.807 | 0.009 | - | - | 0.844 | 0.967 | 0.580 | 1.25x | 16.7/23.3/26.8% | 1.7/5.0% | 3 |
| bucket+interval | 1 | 0.824 | 0.783 | 0.040 | - | - | 0.953 | 0.969 | 0.550 | 1.70x | 22.4/31.1/35.7% | 2.4/6.9% | 3 |

> trigger=bucket: decode_failures 30

> trigger=interval: misdecodes 5

> trigger=interval: decode_failures 37

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 18

> trigger=bucket+interval: misdecodes 5

> trigger=bucket+interval: decode_failures 22

> slower: 11.7 s per simulated hour against 3.54 over 60 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.830 | 0.810 | 0.020 | - | - | 0.935 | 0.975 | 0.560 | 1.24x | 16.7/23.7/27.1% | 1.7/5.2% | 3 |
| 8 | 1 | 0.837 | 0.817 | 0.021 | - | - | 0.935 | 0.979 | 0.575 | 1.22x | 16.3/23.0/26.4% | 1.7/5.0% | 3 |
| 16 | 1 | 0.839 | 0.816 | 0.023 | - | - | 0.926 | 0.979 | 0.574 | 1.23x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 32 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 50 | 1 | 0.833 | 0.812 | 0.021 | - | - | 0.912 | 0.970 | 0.575 | 1.24x | 16.6/23.1/26.5% | 1.7/5.0% | 3 |

> capacity=4: decode_failures 72

> capacity=8: decode_failures 61

> capacity=16: decode_failures 51

> capacity=32: decode_failures 30

> capacity=50: decode_failures 31

> slower: 6.94 s per simulated hour against 1.7 over 60 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.830 | 0.810 | 0.020 | - | - | 0.935 | 0.975 | 0.560 | 1.24x | 16.7/23.7/27.1% | 1.7/5.2% | 3 |
| 8 | 1 | 0.837 | 0.817 | 0.021 | - | - | 0.935 | 0.979 | 0.575 | 1.22x | 16.3/23.0/26.4% | 1.7/5.0% | 3 |
| 16 | 1 | 0.839 | 0.816 | 0.023 | - | - | 0.926 | 0.979 | 0.574 | 1.23x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 32 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 50 | 1 | 0.833 | 0.812 | 0.021 | - | - | 0.912 | 0.970 | 0.575 | 1.24x | 16.6/23.1/26.5% | 1.7/5.0% | 3 |

> capacity=4: decode_failures 72

> capacity=8: decode_failures 61

> capacity=16: decode_failures 51

> capacity=32: decode_failures 30

> capacity=50: decode_failures 31

> slower: 7.12 s per simulated hour against 1.73 over 60 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.821 | 0.815 | 0.006 | - | - | 0.845 | 0.975 | 0.552 | 1.22x | 16.3/22.8/26.1% | 1.7/4.9% | 3 |
| 16 | 1 | 0.829 | 0.820 | 0.009 | - | - | 0.860 | 0.976 | 0.565 | 1.22x | 16.3/22.7/26.0% | 1.7/4.9% | 3 |
| 32 | 1 | 0.841 | 0.813 | 0.028 | - | - | 0.963 | 0.981 | 0.565 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> capacity=8: misdecodes 5

> capacity=8: decode_failures 75

> capacity=16: misdecodes 3

> capacity=16: decode_failures 47

> capacity=32: misdecodes 6

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.824 | 0.783 | 0.040 | - | - | 0.953 | 0.969 | 0.550 | 1.70x | 22.4/31.1/35.7% | 2.4/6.9% | 3 |
| 02-06 | 1 | 0.829 | 0.814 | 0.015 | - | - | 0.892 | 0.976 | 0.575 | 1.26x | 17.0/23.6/27.0% | 1.7/5.2% | 3 |
| 00-08 | 1 | 0.838 | 0.818 | 0.020 | - | - | 0.912 | 0.978 | 0.580 | 1.32x | 17.9/24.8/28.5% | 1.8/5.5% | 3 |

> catch-up-hours=: misdecodes 5

> catch-up-hours=: decode_failures 22

> catch-up-hours=02-06: decode_failures 50

> catch-up-hours=00-08: decode_failures 55

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.806 | 0.804 | 0.002 | - | - | 0.909 | 0.909 | 0.555 | 1.23x | 16.5/22.9/26.1% | 1.7/4.9% | 3 |
| 2 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 3 | 1 | 0.835 | 0.809 | 0.026 | - | - | 0.981 | 0.982 | 0.594 | 1.25x | 16.8/23.3/26.6% | 1.7/5.2% | 3 |
| 4 | 1 | 0.856 | 0.807 | 0.049 | - | - | 0.981 | 0.985 | 0.639 | 1.26x | 16.9/23.7/26.7% | 1.7/5.2% | 3 |

> hops-apart=2: decode_failures 30

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.806 | 0.804 | 0.002 | - | - | 0.909 | 0.909 | 0.555 | 1.23x | 16.5/22.9/26.1% | 1.7/4.9% | 3 |
| 2 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 3 | 1 | 0.835 | 0.809 | 0.026 | - | - | 0.981 | 0.982 | 0.594 | 1.25x | 16.8/23.3/26.6% | 1.7/5.2% | 3 |
| 4 | 1 | 0.856 | 0.807 | 0.049 | - | - | 0.981 | 0.985 | 0.639 | 1.26x | 16.9/23.7/26.7% | 1.7/5.2% | 3 |
| 5 | 1 | 0.857 | 0.802 | 0.054 | - | - | 0.978 | 0.987 | 0.605 | 1.26x | 16.8/23.6/26.7% | 1.8/5.3% | 3 |

> hops-apart=2: decode_failures 30

> hops-apart=5: decode_failures 1

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.839 | 0.817 | 0.022 | - | - | 0.917 | 0.986 | 0.584 | 1.23x | 16.4/23.0/26.4% | 1.7/5.0% | 3 |
| 30 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 120 | 1 | 0.833 | 0.809 | 0.024 | - | - | 0.926 | 0.972 | 0.550 | 1.24x | 16.6/23.2/26.6% | 1.7/5.0% | 3 |
| 600 | 1 | 0.838 | 0.816 | 0.022 | - | - | 0.921 | 0.979 | 0.569 | 1.24x | 16.6/23.2/26.6% | 1.7/5.0% | 3 |

> advert-jitter-s=1: decode_failures 29

> advert-jitter-s=30: decode_failures 30

> advert-jitter-s=120: decode_failures 25

> advert-jitter-s=600: decode_failures 41

> slower: 8.27 s per simulated hour against 1.75 over 60 prior run(s) - 4.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.839 | 0.817 | 0.022 | - | - | 0.917 | 0.986 | 0.584 | 1.23x | 16.4/23.0/26.4% | 1.7/5.0% | 3 |
| 30 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 120 | 1 | 0.833 | 0.809 | 0.024 | - | - | 0.926 | 0.972 | 0.550 | 1.24x | 16.6/23.2/26.6% | 1.7/5.0% | 3 |
| 600 | 1 | 0.838 | 0.816 | 0.022 | - | - | 0.921 | 0.979 | 0.569 | 1.24x | 16.6/23.2/26.6% | 1.7/5.0% | 3 |

> advert-jitter-s=1: decode_failures 29

> advert-jitter-s=30: decode_failures 30

> advert-jitter-s=120: decode_failures 25

> advert-jitter-s=600: decode_failures 41

> slower: 6.15 s per simulated hour against 1.78 over 60 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.863 | 0.815 | 0.048 | - | - | 0.899 | 0.993 | 0.603 | 1.29x | 17.5/23.5/26.5% | 1.8/4.9% | 3 |
| routers | 1 | 0.819 | 0.816 | 0.003 | - | - | 0.924 | 0.924 | 0.566 | 1.24x | 16.6/23.3/26.4% | 1.7/5.0% | 3 |
| alternate-routers | 1 | 0.810 | 0.804 | 0.006 | - | - | 0.931 | 0.932 | 0.574 | 1.25x | 16.7/23.5/26.9% | 1.7/5.1% | 3 |
| beside-router | 1 | 0.823 | 0.816 | 0.006 | - | - | 0.953 | 0.953 | 0.557 | 1.23x | 16.4/23.1/26.4% | 1.7/4.9% | 3 |
| random-clients | 1 | 0.828 | 0.807 | 0.021 | - | - | 0.821 | 0.941 | 0.558 | 1.25x | 16.9/23.4/26.6% | 1.7/4.9% | 3 |
| hops-apart | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> place=spread: decode_failures 37

> place=random-clients: decode_failures 19

> place=hops-apart: decode_failures 30

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.863 | 0.815 | 0.048 | - | - | 0.899 | 0.993 | 0.603 | 1.29x | 17.5/23.5/26.5% | 1.8/4.9% | 3 |
| routers | 1 | 0.819 | 0.816 | 0.003 | - | - | 0.924 | 0.924 | 0.566 | 1.24x | 16.6/23.3/26.4% | 1.7/5.0% | 3 |
| alternate-routers | 1 | 0.810 | 0.804 | 0.006 | - | - | 0.931 | 0.932 | 0.574 | 1.25x | 16.7/23.5/26.9% | 1.7/5.1% | 3 |
| beside-router | 1 | 0.823 | 0.816 | 0.006 | - | - | 0.953 | 0.953 | 0.557 | 1.23x | 16.4/23.1/26.4% | 1.7/4.9% | 3 |
| random-clients | 1 | 0.828 | 0.807 | 0.021 | - | - | 0.821 | 0.941 | 0.558 | 1.25x | 16.9/23.4/26.6% | 1.7/4.9% | 3 |
| hops-apart | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> place=spread: decode_failures 37

> place=random-clients: decode_failures 19

> place=hops-apart: decode_failures 30

> slower: 5.57 s per simulated hour against 2.77 over 60 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| broadcast | 1 | 0.862 | 0.796 | 0.067 | - | - | 0.888 | 0.965 | 0.619 | 1.36x | 17.9/25.1/28.6% | 1.9/5.3% | 3 |

> provide-transport=dm: decode_failures 30

> provide-transport=broadcast: decode_failures 42

> slower: 11.5 s per simulated hour against 1.76 over 60 prior run(s) - 6.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| heard | 1 | 0.831 | 0.809 | 0.022 | - | - | 0.932 | 0.976 | 0.581 | 1.25x | 16.8/23.2/26.8% | 1.7/5.0% | 3 |

> replay-ordering=tip: decode_failures 30

> replay-ordering=heard: misdecodes 3

> replay-ordering=heard: decode_failures 39

> slower: 6.48 s per simulated hour against 1.56 over 60 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.862 | 0.796 | 0.067 | - | - | 0.888 | 0.965 | 0.619 | 1.36x | 17.9/25.1/28.6% | 1.9/5.3% | 3 |
| heard | 1 | 0.850 | 0.795 | 0.055 | - | - | 0.872 | 0.965 | 0.619 | 1.32x | 17.4/24.5/27.9% | 1.8/5.2% | 3 |

> replay-ordering=tip: decode_failures 42

> replay-ordering=heard: decode_failures 23

> slower: 10.4 s per simulated hour against 1.68 over 60 prior run(s) - 6.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.819 | 0.808 | 0.011 | - | - | 0.867 | 0.978 | 0.579 | 1.24x | 16.5/23.2/26.5% | 1.7/5.0% | 3 |
| enum | 1 | 0.835 | 0.809 | 0.026 | - | - | 0.935 | 0.972 | 0.568 | 1.24x | 16.7/23.4/26.8% | 1.7/5.1% | 3 |
| hybrid | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> resolve=sketch: decode_failures 29

> resolve=hybrid: decode_failures 30

> slower: 4.32 s per simulated hour against 1.52 over 60 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.819 | 0.816 | 0.003 | - | - | 0.924 | 0.924 | 0.566 | 1.24x | 16.6/23.3/26.4% | 1.7/5.0% | 3 |
| 6 | 1 | 0.810 | 0.800 | 0.010 | - | - | 0.936 | 0.937 | 0.570 | 1.28x | 17.0/24.4/27.6% | 1.8/5.2% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.817 | 0.810 | 0.007 | - | - | 0.948 | 0.949 | 0.565 | 1.24x | 16.5/23.0/26.3% | 1.7/4.9% | 2 |
| 3 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 5 | 1 | 0.839 | 0.805 | 0.034 | - | - | 0.964 | 0.978 | 0.575 | 1.28x | 17.0/23.9/27.5% | 1.8/5.2% | 5 |
| 8 | 1 | 0.839 | 0.796 | 0.044 | - | - | 0.975 | 0.980 | 0.574 | 1.30x | 17.3/24.5/28.2% | 1.8/5.2% | 8 |

> servers=3: decode_failures 30

> servers=5: decode_failures 21

> servers=8: decode_failures 41

> slower: 5.55 s per simulated hour against 2.29 over 60 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.817 | 0.810 | 0.007 | - | - | 0.948 | 0.949 | 0.565 | 1.24x | 16.5/23.0/26.3% | 1.7/4.9% | 2 |
| 3 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 5 | 1 | 0.839 | 0.805 | 0.034 | - | - | 0.964 | 0.978 | 0.575 | 1.28x | 17.0/23.9/27.5% | 1.8/5.2% | 5 |
| 8 | 1 | 0.839 | 0.796 | 0.044 | - | - | 0.975 | 0.980 | 0.574 | 1.30x | 17.3/24.5/28.2% | 1.8/5.2% | 8 |

> servers=3: decode_failures 30

> servers=5: decode_failures 21

> servers=8: decode_failures 41

> slower: 5.86 s per simulated hour against 2.22 over 60 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| True | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> signed=False: decode_failures 30

> signed=True: decode_failures 30

> slower: 10 s per simulated hour against 1.66 over 60 prior run(s) - 6.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.827 | 0.814 | 0.013 | - | - | 0.868 | 0.960 | 0.591 | 1.15x | 15.4/21.2/24.3% | 1.6/4.5% | 3 |
| 1 | 1 | 0.851 | 0.830 | 0.021 | - | - | 0.944 | 0.981 | 0.588 | 1.13x | 15.2/21.0/24.0% | 1.6/4.5% | 3 |
| 2 | 1 | 0.831 | 0.810 | 0.021 | - | - | 0.923 | 0.968 | 0.601 | 1.15x | 15.5/21.5/24.6% | 1.6/4.6% | 3 |
| 4 | 1 | 0.832 | 0.805 | 0.027 | - | - | 0.933 | 0.969 | 0.588 | 1.14x | 15.3/21.2/24.3% | 1.6/4.5% | 3 |

> sr-retries=0: decode_failures 9

> sr-retries=1: decode_failures 7

> sr-retries=2: decode_failures 16

> sr-retries=4: decode_failures 11

> slower: 6.12 s per simulated hour against 1.51 over 60 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.838 | 0.813 | 0.025 | - | - | 0.948 | 0.979 | 0.584 | 1.24x | 16.5/23.1/26.5% | 1.7/5.1% | 3 |
| 24 | 1 | 0.836 | 0.810 | 0.025 | - | - | 0.933 | 0.976 | 0.573 | 1.25x | 16.8/23.4/26.8% | 1.7/5.1% | 3 |
| 32 | 1 | 0.834 | 0.811 | 0.023 | - | - | 0.919 | 0.971 | 0.551 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |
| 64 | 1 | 0.826 | 0.802 | 0.024 | - | - | 0.919 | 0.972 | 0.575 | 1.25x | 16.6/23.3/26.7% | 1.7/5.0% | 3 |

> short-id-bits=16: decode_failures 45

> short-id-bits=24: decode_failures 31

> short-id-bits=32: decode_failures 30

> short-id-bits=64: decode_failures 44

> slower: 12 s per simulated hour against 1.65 over 60 prior run(s) - 7.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.828 | 0.796 | 0.032 | - | - | 0.946 | 0.973 | 0.580 | 1.32x | 17.6/24.4/27.9% | 1.8/5.3% | 3 |
| 16 | 1 | 0.838 | 0.807 | 0.032 | - | - | 0.952 | 0.974 | 0.551 | 1.27x | 17.0/23.8/27.2% | 1.8/5.1% | 3 |
| 32 | 1 | 0.841 | 0.813 | 0.028 | - | - | 0.963 | 0.981 | 0.565 | 1.24x | 16.6/23.2/26.5% | 1.7/5.0% | 3 |

> window-size=8: misdecodes 94

> window-size=16: misdecodes 36

> window-size=32: misdecodes 6

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.963 | 0.959 | 0.004 | - | - | 0.999 | 0.999 | 0.877 | 2.01x | 23.0/38.8/42.5% | 1.3/4.9% | 3 |
| True | 1 | 0.730 | 0.716 | 0.013 | - | - | 0.855 | 0.888 | 0.548 | 5.45x | 59.1/74.2/79.0% | 4.0/12.7% | 3 |

> no-congestion-scaling=True: queue drops 12.5% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 20

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.526 | 0.517 | 0.009 | - | - | 0.757 | 0.757 | 0.194 | 4.53x | 16.0/27.2/37.8% | 1.5/5.5% | 3 |
| truesize | 1 | 0.561 | 0.552 | 0.009 | - | - | 0.787 | 0.789 | 0.205 | 3.30x | 11.8/20.4/29.5% | 1.1/4.5% | 3 |

> congestion-input=hotstore: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.964 | 0.961 | 0.003 | - | - | 0.997 | 0.998 | 0.881 | 1.91x | 21.8/37.0/40.4% | 1.3/4.7% | 3 |
| adaptive | 1 | 0.963 | 0.959 | 0.004 | - | - | 0.999 | 0.999 | 0.877 | 2.01x | 23.0/38.8/42.5% | 1.3/4.9% | 3 |

