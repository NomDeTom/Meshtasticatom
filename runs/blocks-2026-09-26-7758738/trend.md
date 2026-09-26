# Sweep blocks-2026-09-26-7758738

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 7758738 · seeds 7758738
- **blocks** 87 run
- **compute** 15.3 h of simulator time across every cell
- **generated** 2026-09-26T09:34:06+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>237 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 2
- AD-amplify-worst: amplify-worst=0.0: decode_failures 2
- AD-amplify-worst: amplify-worst=0.1: decode_failures 30
- AD-amplify-worst: slower: 5.34 s per simulated hour against 1.79 over 36 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=degree: decode_failures 28
- AD-badrouters: role-placement=random: decode_failures 56
- AD-badrouters: slower: 8.52 s per simulated hour against 2.05 over 36 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 28
- AD-flooding: slower: 6.55 s per simulated hour against 2.59 over 36 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 28
- AD-nomute: slower: 5.04 s per simulated hour against 2.42 over 36 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 28
- AD-siting: siting-mix=local-typical: decode_failures 31
- AD-siting: slower: 3.88 s per simulated hour against 1.44 over 36 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=degree: decode_failures 18
- AD-worst: role-placement=inverse: decode_failures 28
- AD-worst: slower: 7.17 s per simulated hour against 3.48 over 36 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 38
- BL-control: slower: 6.73 s per simulated hour against 1.78 over 36 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 5
- DB-hotstore: max-num-nodes=100: decode_failures 1
- DB-hotstore: max-num-nodes=120: decode_failures 1
- DB-hotstore: max-num-nodes=250: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 46
- DB-platform: platform-mix=uniform: decode_failures 1
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 1
- DB-warm: warm-num-nodes=0: queue drops 11.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 130
- DB-warm: warm-num-nodes=25: queue drops 11.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 130
- DB-warm: warm-num-nodes=100: queue drops 11.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 130
- DB-warm: warm-num-nodes=2000: queue drops 11.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 130
- DG-burst: burst-loss=0.0: decode_failures 2
- DG-burst: burst-loss=0.1: decode_failures 37
- DG-burst: burst-loss=0.2: decode_failures 33
- DG-burst: burst-loss=0.3: decode_failures 18
- DG-loss: extra-loss=0.0: decode_failures 2
- DG-loss: extra-loss=0.2: decode_failures 7
- DG-loss: extra-loss=0.3: decode_failures 29
- DG-outage: burst-loss=0.0: decode_failures 2
- DG-outage: burst-loss=0.1: decode_failures 25
- DG-outage: burst-loss=0.2: decode_failures 34
- DG-outage: burst-loss=0.3: decode_failures 14
- DM-mode: dm-mode=flood-only: decode_failures 34
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 34
- DM-mode: dm-mode=m4-early-flood: decode_failures 39
- DM-mode: slower: 7.45 s per simulated hour against 3.17 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 2
- FW-mixed-26: legacy-fraction=0.0: decode_failures 2
- FW-mixed-26: legacy-fraction=0.5: decode_failures 2
- FW-mixed-26: legacy-fraction=0.75: decode_failures 24
- FW-mixed-26: slower: 3.33 s per simulated hour against 1.66 over 36 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.0: decode_failures 2
- FW-mixed: legacy-fraction=0.75: decode_failures 1
- FW-signing-cost: profile-flag=signing=true: decode_failures 2
- FW-versions: profile=2.8: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 26
- LD-chatty: broadcast-interval-s=3600: decode_failures 1
- LD-chatty: broadcast-interval-s=900: decode_failures 20
- LD-chatty: broadcast-interval-s=300: decode_failures 30
- LD-diurnal: diurnal=flat: decode_failures 1
- LD-diurnal: diurnal=commuter: decode_failures 2
- LD-interval: broadcast-interval-s=900: decode_failures 20
- LD-interval: broadcast-interval-s=3600: decode_failures 1
- LD-interval: broadcast-interval-s=43200: decode_failures 1
- LD-interval: slower: 3.39 s per simulated hour against 1.35 over 36 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 2
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 2
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 47
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 26
- LD-traceroute: slower: 7.11 s per simulated hour against 2.1 over 36 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 11.7% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 130
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 18.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 108
- MS-density: nodes=60: decode_failures 2
- MS-density: nodes=120: misdecodes 1
- MS-hopscale: nodes=60: decode_failures 2
- MS-hopscale: nodes=500: decode_failures 123
- MS-oversubscribed: nodes=500: decode_failures 29
- MS-roles: role-mix=legacy-default: decode_failures 2
- MS-roles: role-mix=baymesh-2026-08: decode_failures 28
- MS-roles: slower: 6.12 s per simulated hour against 1.78 over 36 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 2
- MS-router-late: router-late-fraction=0.05: decode_failures 1
- MS-router-late: router-late-fraction=0.1: decode_failures 1
- MS-router-late: router-late-fraction=0.2: decode_failures 10
- MS-siting: siting-mix=uniform: decode_failures 2
- MS-siting: siting-mix=local-typical: decode_failures 25
- MS-size: nodes=40: decode_failures 13
- MS-size: nodes=60: decode_failures 2
- MS-stretch: stretch=1.0: decode_failures 2
- MS-stretch: stretch=1.25: decode_failures 19
- MS-topology: topology=uniform: decode_failures 2
- MS-topology: topology=corridor: decode_failures 13
- PR-crladder: coding-rate-ladder=False: decode_failures 34
- PR-crladder: coding-rate-ladder=True: decode_failures 45
- PR-crladder: slower: 13.6 s per simulated hour against 2.77 over 36 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 45
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 43
- PR-dmmode-cr: slower: 11.8 s per simulated hour against 2.68 over 36 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 2
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- PR-repeats: extra-repeats=False: decode_failures 2
- PR-repeats: extra-repeats=True: decode_failures 2
- RF-duct: duct-per-hour=0.0: decode_failures 2
- RF-duct: duct-per-hour=0.25: decode_failures 1
- RF-duct: duct-per-hour=1.0: decode_failures 1
- RF-eu-presets: preset=LONG_FAST: decode_failures 2
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 22
- RF-noise: noise-profile=none: decode_failures 2
- RF-noise: noise-profile=temporal: decode_failures 2
- RF-noise: noise-profile=transient: decode_failures 4
- RF-noise: noise-profile=periodic: decode_failures 17
- RF-preset: preset=LONG_FAST: decode_failures 2
- RF-preset: preset=LONG_MODERATE: decode_failures 5
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 6
- RF-preset-turbo: preset=LONG_FAST: decode_failures 2
- RF-preset-turbo: preset=EXTRA_LONG_TURBO: decode_failures 35
- RF-preset-turbo: slower: 4.28 s per simulated hour against 1.53 over 32 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 22
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 17
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 1
- RF-pulse: slower: 4.09 s per simulated hour against 1.67 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: faster: 0.971 s per simulated hour against 1.96 over 36 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-txpower: tx-power=30: decode_failures 2
- RF-txpower: tx-power=14: decode_failures 2
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-adopt: no-adopt-hop-recommendation=True: misdecodes 1
- RT-favourites: favourite-routers=False: decode_failures 33
- RT-favourites: favourite-routers=True: decode_failures 1
- RT-favourites: slower: 4.75 s per simulated hour against 1.67 over 36 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 2
- RT-hopassign: hop-assign=random: decode_failures 1
- RT-hoplimit: hop-limit=3: decode_failures 37
- RT-hopspread: hop-limit=3: decode_failures 37
- RT-hopspread: hop-limit=5: decode_failures 2
- RT-hopspread: slower: 5.89 s per simulated hour against 2.04 over 36 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 2
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 2
- RT-spread: hop-spread=False: decode_failures 37
- RT-spread: hop-spread=True: decode_failures 2
- RT-spread: slower: 7.58 s per simulated hour against 2.33 over 36 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 2
- SC-signing: signature-policy=BALANCED: decode_failures 2
- SC-signing: signature-policy=STRICT: decode_failures 49
- SC-signing: slower: 6.18 s per simulated hour against 1.81 over 36 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-advert-transport: advert-transport=broadcast: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 24
- SF-bucket-mode: bucket-mode=local: decode_failures 2
- SF-bucket-mode: bucket-mode=time: misdecodes 8
- SF-bucket-mode: bucket-mode=window: misdecodes 9
- SF-bucket-mode: bucket-mode=window: decode_failures 2
- SF-bucket-time: time-bucket-s=600: misdecodes 70
- SF-bucket-time: time-bucket-s=1800: misdecodes 8
- SF-bucket-time: time-bucket-s=3600: misdecodes 5
- SF-bucket-time: time-bucket-s=3600: decode_failures 16
- SF-cadence: trigger=bucket: decode_failures 2
- SF-cadence: trigger=interval: misdecodes 17
- SF-cadence: trigger=interval: decode_failures 2
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 24
- SF-cadence: trigger=bucket+interval: misdecodes 19
- SF-capacity-local: capacity=4: decode_failures 71
- SF-capacity-local: capacity=8: decode_failures 62
- SF-capacity-local: capacity=16: decode_failures 43
- SF-capacity-local: capacity=32: decode_failures 2
- SF-capacity: capacity=4: decode_failures 71
- SF-capacity: capacity=8: decode_failures 62
- SF-capacity: capacity=16: decode_failures 43
- SF-capacity: capacity=32: decode_failures 2
- SF-capacity-window: capacity=8: misdecodes 8
- SF-capacity-window: capacity=8: decode_failures 94
- SF-capacity-window: capacity=16: misdecodes 6
- SF-capacity-window: capacity=16: decode_failures 64
- SF-capacity-window: capacity=32: misdecodes 9
- SF-capacity-window: capacity=32: decode_failures 2
- SF-capacity-window: slower: 3.9 s per simulated hour against 1.63 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 19
- SF-catchup: catch-up-hours=02-06: decode_failures 46
- SF-catchup: catch-up-hours=00-08: decode_failures 47
- SF-hops-flat: hops-apart=2: decode_failures 2
- SF-hops-flat: hops-apart=3: decode_failures 38
- SF-hops-flat: hops-apart=4: decode_failures 30
- SF-hops-spread: hops-apart=2: decode_failures 2
- SF-hops-spread: hops-apart=3: decode_failures 38
- SF-hops-spread: hops-apart=4: decode_failures 30
- SF-hops-spread: hops-apart=5: decode_failures 27
- SF-jitter-global: advert-jitter-s=1: decode_failures 3
- SF-jitter-global: advert-jitter-s=30: decode_failures 2
- SF-jitter-global: advert-jitter-s=120: decode_failures 3
- SF-jitter-global: advert-jitter-s=600: decode_failures 7
- SF-jitter-global: slower: 3.54 s per simulated hour against 1.77 over 36 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 3
- SF-jitter-local: advert-jitter-s=30: decode_failures 2
- SF-jitter-local: advert-jitter-s=120: decode_failures 3
- SF-jitter-local: advert-jitter-s=600: decode_failures 7
- SF-place-flat: place=spread: decode_failures 19
- SF-place-flat: place=random-clients: decode_failures 33
- SF-place-flat: place=hops-apart: decode_failures 2
- SF-place-spread: place=spread: decode_failures 19
- SF-place-spread: place=random-clients: decode_failures 33
- SF-place-spread: place=hops-apart: decode_failures 2
- SF-provide-transport: provide-transport=dm: decode_failures 2
- SF-provide-transport: provide-transport=broadcast: decode_failures 25
- SF-provide-transport: slower: 6.28 s per simulated hour against 1.79 over 36 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 25
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 2
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 49
- SF-replay-order-broadcast: slower: 12.3 s per simulated hour against 1.78 over 36 prior run(s) - 6.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 2
- SF-replay-order: replay-ordering=heard: misdecodes 4
- SF-resolve: resolve=sketch: decode_failures 15
- SF-resolve: resolve=hybrid: decode_failures 2
- SF-resolve: slower: 3.73 s per simulated hour against 1.55 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=3: decode_failures 2
- SF-servers-spread: servers=3: decode_failures 2
- SF-signed: signed=False: decode_failures 2
- SF-signed: signed=True: decode_failures 2
- SF-sr-retries: sr-retries=0: decode_failures 2
- SF-sr-retries: sr-retries=1: decode_failures 3
- SF-sr-retries: sr-retries=2: decode_failures 1
- SF-width: short-id-bits=16: decode_failures 1
- SF-width: short-id-bits=24: decode_failures 54
- SF-width: short-id-bits=32: decode_failures 2
- SF-width: short-id-bits=64: decode_failures 16
- SF-width: slower: 6.34 s per simulated hour against 1.7 over 36 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 122
- SF-window-size: window-size=16: misdecodes 49
- SF-window-size: window-size=32: misdecodes 9
- SF-window-size: window-size=32: decode_failures 2
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 10.8% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 102

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-replay-order-broadcast` | 12.3 | 1.78 | 6.93x | 36 |
| `PR-crladder` | 13.6 | 2.77 | 4.92x | 36 |
| `PR-dmmode-cr` | 11.8 | 2.68 | 4.39x | 36 |
| `AD-badrouters` | 8.52 | 2.05 | 4.15x | 36 |
| `BL-control` | 6.73 | 1.78 | 3.78x | 36 |
| `SF-width` | 6.34 | 1.7 | 3.72x | 36 |
| `SF-provide-transport` | 6.28 | 1.79 | 3.50x | 36 |
| `MS-roles` | 6.12 | 1.78 | 3.44x | 36 |
| `SC-signing` | 6.18 | 1.81 | 3.41x | 36 |
| `LD-traceroute` | 7.11 | 2.1 | 3.39x | 36 |
| `RT-spread` | 7.58 | 2.33 | 3.25x | 36 |
| `AD-amplify-worst` | 5.34 | 1.79 | 2.97x | 36 |
| `RT-hopspread` | 5.89 | 2.04 | 2.88x | 36 |
| `RT-favourites` | 4.75 | 1.67 | 2.85x | 36 |
| `RF-preset-turbo` | 4.28 | 1.53 | 2.79x | 32 |
| `AD-siting` | 3.88 | 1.44 | 2.69x | 36 |
| `AD-flooding` | 6.55 | 2.59 | 2.53x | 36 |
| `LD-interval` | 3.39 | 1.35 | 2.51x | 36 |
| `RF-pulse` | 4.09 | 1.67 | 2.45x | 36 |
| `SF-resolve` | 3.73 | 1.55 | 2.41x | 36 |
| `SF-capacity-window` | 3.9 | 1.63 | 2.39x | 36 |
| `DM-mode` | 7.45 | 3.17 | 2.35x | 36 |
| `AD-nomute` | 5.04 | 2.42 | 2.08x | 36 |
| `AD-worst` | 7.17 | 3.48 | 2.06x | 36 |
| `FW-mixed-26` | 3.33 | 1.66 | 2.01x | 36 |
| `SF-jitter-global` | 3.54 | 1.77 | 2.00x | 36 |
| `RF-eu-presets` | 3.97 | 2.02 | 1.97x | 36 |
| `SF-cadence` | 7.03 | 3.63 | 1.94x | 36 |
| `RT-hoplimit` | 3.41 | 1.77 | 1.93x | 36 |
| `SF-jitter-local` | 3.47 | 1.84 | 1.88x | 36 |
| `PR-repeats` | 2.96 | 1.65 | 1.79x | 36 |
| `SF-sr-retries` | 2.78 | 1.59 | 1.75x | 36 |
| `DG-loss` | 3.93 | 2.28 | 1.73x | 36 |
| `SF-signed` | 3.01 | 1.74 | 1.73x | 36 |
| `SF-capacity-local` | 2.86 | 1.78 | 1.61x | 36 |
| `SF-advert-transport` | 2.81 | 1.75 | 1.61x | 36 |
| `DG-burst` | 8.14 | 5.09 | 1.60x | 36 |
| `MS-siting` | 2.94 | 1.87 | 1.57x | 35 |
| `LD-chatty` | 7.97 | 5.09 | 1.57x | 36 |
| `SF-replay-order` | 2.56 | 1.7 | 1.51x | 36 |
| `SF-servers-flat` | 1.69 | 2.57 | 0.66x | 36 |
| `TH-congestion-input` | 6.11 | 10.8 | 0.56x | 36 |
| `RF-stretch-duct` | 0.971 | 1.96 | 0.49x | 36 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.941 | 0.941 | 0.751 → 0.777 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.879 | 0.879 | 0.776 → 0.777 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **text** | 0.161 → 0.972 | 0.811 | 0.161 → 0.971 | 5.8x sr_bytes | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.098 → 0.872 | 0.774 | 0.100 → 0.717 | 1.6e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.170 → 0.941 | 0.770 | 0.061 → 0.769 | 5.7x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.242 → 0.941 | 0.699 | 0.094 → 0.769 | 3.9x advert_bytes | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.076 → 0.761 | 0.685 | 0.075 → 0.753 | 4.9x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.126 → 0.781 | 0.655 | 0.124 → 0.769 | 4.1x sr_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.150 → 0.703 | 0.553 | 0.149 → 0.686 | 2.5x advert_bytes | up | 3 |
| `MS-topology` | topology | **held** | 0.447 → 0.986 | 0.539 | 0.480 → 0.950 | 4.2x sr_bytes | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.250 → 0.781 | 0.531 | 0.247 → 0.769 | 3.6x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.250 → 0.781 | 0.531 | 0.247 → 0.769 | 3.5x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.484 → 0.977 | 0.492 | 0.317 → 0.769 | 7.6x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.502 → 0.975 | 0.473 | 0.320 → 0.777 | 5x bytes_on_air | down | 3 |
| `SF-place-flat` | place | **held** | 0.508 → 0.950 | 0.442 | 0.769 → 0.777 | 3.8x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.508 → 0.950 | 0.442 | 0.769 → 0.777 | 3.8x sr_bytes | up | 6 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.566 → 0.973 | 0.406 | 0.457 → 0.807 | 10x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **held** | 0.543 → 0.941 | 0.398 | 0.411 → 0.769 | 1.8x advert_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.524 → 0.903 | 0.379 | 0.518 → 0.897 | 12x sr_airtime | down | 3 |
| `MS-density` | nodes | **text** | 0.614 → 0.961 | 0.347 | 0.600 → 0.961 | 4.5x sr_airtime | up | 5 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.266 → 0.600 | 0.334 | 0.263 → 0.598 | 2.8x sr_airtime | up | 2 |
| `DG-burst` | burst-loss | **text** | 0.463 → 0.781 | 0.318 | 0.442 → 0.769 | 1.5x advert_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.600 → 0.892 | 0.293 | 0.354 → 0.593 | 5.1x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.645 → 0.895 | 0.250 | 0.619 → 0.890 | 1.9x sr_bytes | up | 4 |
| `RF-noise` | noise-profile | **held** | 0.704 → 0.942 | 0.238 | 0.585 → 0.769 | 1.6x sr_airtime | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.715 → 0.941 | 0.226 | 0.764 → 0.777 | 5.1x sr_bytes | down | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.645 → 0.869 | 0.223 | 0.619 → 0.862 | 1.6x sr_bytes | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.724 → 0.941 | 0.217 | 0.764 → 0.777 | 5.1x sr_bytes | down | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.764 → 0.956 | 0.192 | 0.752 → 0.954 | 3.7x sr_airtime | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.778 → 0.941 | 0.162 | 0.769 → 0.782 | 34x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.629 → 0.781 | 0.151 | 0.615 → 0.769 | 1.3x sr_bytes | down | 4 |
| `MS-size` | nodes | **held** | 0.835 → 0.977 | 0.142 | 0.710 → 0.782 | 3.9x sr_airtime | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.645 → 0.781 | 0.136 | 0.619 → 0.769 | 1.5x sr_bytes | up | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.717 → 0.850 | 0.133 | 0.705 → 0.843 | 5.7x sr_airtime | up | 4 |
| `SC-signing` | signature-policy | **held** | 0.814 → 0.941 | 0.127 | 0.660 → 0.769 | 1.2x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.781 → 0.904 | 0.123 | 0.769 → 0.902 | 1.9x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.638 → 0.761 | 0.123 | 0.627 → 0.753 | 1.7x sr_bytes | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.781 → 0.899 | 0.119 | 0.769 → 0.890 | 1.5x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.705 → 0.820 | 0.115 | 0.691 → 0.810 | 2.1x sr_airtime | up | 4 |
| `SF-cadence` | trigger | **held** | 0.828 → 0.941 | 0.113 | 0.725 → 0.780 | 14x advert_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.710 → 0.820 | 0.110 | 0.697 → 0.810 | 2.2x sr_airtime | down | 3 |
| `SF-capacity-window` | capacity | **held** | 0.819 → 0.923 | 0.104 | 0.769 → 0.776 | 3.9x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.781 → 0.876 | 0.095 | 0.769 → 0.864 | 1.3x sr_airtime | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.761 → 0.853 | 0.092 | 0.753 → 0.846 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.761 → 0.853 | 0.092 | 0.753 → 0.846 | 2.2x bytes_on_air | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.685 → 0.754 | 0.069 | 0.674 → 0.744 | 1.4x sr_airtime | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.893 → 0.954 | 0.060 | 0.769 → 0.805 | 1.3x sr_bytes | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.724 → 0.782 | 0.057 | 0.710 → 0.770 | 1.5x sr_airtime | down | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.781 → 0.834 | 0.053 | 0.763 → 0.769 | 4.2x sr_airtime | up | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.779 → 0.830 | 0.051 | 0.768 → 0.822 | 2.4x bytes_on_air | down | 4 |
| `MS-roles` | role-mix | **held** | 0.902 → 0.952 | 0.050 | 0.753 → 0.778 | 1.1x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.781 → 0.828 | 0.047 | 0.769 → 0.821 | 2.3x bytes_on_air | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.781 → 0.826 | 0.045 | 0.769 → 0.817 | 3.2x bytes_on_air | down | 2 |
| `FW-versions` | profile | **text** | 0.781 → 0.826 | 0.045 | 0.769 → 0.822 | 3.6x bytes_on_air | down | 5 |
| `DM-mode` | dm-mode | **held** | 0.806 → 0.848 | 0.042 | 0.734 → 0.753 | 1.5x sr_airtime | down | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.865 → 0.907 | 0.042 | 0.725 → 0.774 | 9x advert_bytes | down | 3 |
| `AD-worst` | role-placement | **held** | 0.733 → 0.772 | 0.039 | 0.853 → 0.875 | 1.4x sr_bytes | up | 2 |
| `FW-firmware` | profile | **text** | 0.781 → 0.818 | 0.037 | 0.769 → 0.813 | 3.4x bytes_on_air | down | 2 |
| `SF-capacity` | capacity | **held** | 0.914 → 0.950 | 0.036 | 0.769 → 0.781 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.914 → 0.950 | 0.036 | 0.769 → 0.781 | 5.4x advert_bytes | up | 5 |
| `LD-diurnal` | diurnal | **text** | 0.781 → 0.814 | 0.033 | 0.769 → 0.803 | 1.2x sr_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.941 → 0.972 | 0.031 | 0.768 → 0.779 | 8.1x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.941 → 0.972 | 0.031 | 0.768 → 0.779 | 8.1x sr_bytes | up | 4 |
| `TH-congestion-input` | congestion-input | **text** | 0.594 → 0.624 | 0.030 | 0.586 → 0.617 | 1.3x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.923 → 0.950 | 0.027 | 0.769 → 0.774 | 4.7x advert_bytes | down | 3 |
| `SF-width` | short-id-bits | **held** | 0.918 → 0.941 | 0.022 | 0.766 → 0.772 | 3.1x advert_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.781 → 0.802 | 0.021 | 0.769 → 0.791 | 1.3x bytes_on_air | up | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.923 → 0.941 | 0.017 | 0.769 → 0.773 | 2.7x advert_bytes | down | 4 |
| `SF-resolve` | resolve | **held** | 0.925 → 0.941 | 0.016 | 0.769 → 0.772 | 5.8x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.928 → 0.944 | 0.016 | 0.772 → 0.781 | 1.2x sr_bytes | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.781 → 0.796 | 0.015 | 0.769 → 0.782 | 1.1x advert_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.806 → 0.821 | 0.014 | 0.741 → 0.748 | 1.4x sr_airtime | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.770 → 0.783 | 0.014 | 0.756 → 0.773 | 5.3x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.797 → 0.810 | 0.013 | 0.787 → 0.799 | 1.3x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.779 → 0.792 | 0.013 | 0.767 → 0.780 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.779 → 0.792 | 0.013 | 0.767 → 0.780 | 1.1x sr_airtime | down | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.781 → 0.792 | 0.011 | 0.769 → 0.781 | 1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.901 → 0.910 | 0.009 | 0.761 → 0.763 | 1.1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.948 → 0.956 | 0.008 | 0.946 → 0.954 | 1.2x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.908 → 0.913 | 0.005 | 0.772 → 0.772 | 3.1x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.936 → 0.941 | 0.004 | 0.769 → 0.772 | 2.7x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.781 → 0.785 | 0.004 | 0.769 → 0.775 | 1x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.818 → 0.821 | 0.003 | 0.738 → 0.741 | 1.1x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.956 → 0.958 | 0.002 | 0.954 → 0.956 | 1.1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.998 → 0.998 | 0.000 | 0.954 → 0.954 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| sprinkled | 1 | 0.836 | 0.828 | 0.007 | - | - | 0.956 | 0.956 | 0.305 | 1.12x | 14.7/20.2/24.7% | 1.8/5.0% | 3 |
| arms-race | 1 | 0.904 | 0.902 | 0.002 | - | - | 0.932 | 0.933 | 0.639 | 1.12x | 18.2/25.4/28.6% | 1.6/5.3% | 3 |

> amplifier-mix=none: decode_failures 2

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.1 | 1 | 0.817 | 0.803 | 0.013 | - | - | 0.955 | 0.967 | 0.310 | 1.26x | 14.6/24.5/28.7% | 1.9/4.9% | 3 |
| 0.3 | 1 | 0.876 | 0.864 | 0.013 | - | - | 0.974 | 0.976 | 0.496 | 1.17x | 16.4/24.1/29.1% | 1.6/4.6% | 3 |

> amplify-worst=0.0: decode_failures 2

> amplify-worst=0.1: decode_failures 30

> slower: 5.34 s per simulated hour against 1.79 over 36 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.902 | 0.912 | 0.319 | 1.18x | 12.9/25.5/30.0% | 1.9/5.1% | 3 |
| inverse | 1 | 0.638 | 0.627 | 0.011 | - | - | 0.830 | 0.833 | 0.024 | 1.02x | 11.7/17.8/21.5% | 1.8/3.6% | 3 |
| random | 1 | 0.719 | 0.704 | 0.015 | - | - | 0.875 | 0.904 | 0.259 | 1.14x | 13.1/19.9/25.0% | 1.9/4.8% | 3 |

> role-placement=degree: decode_failures 28

> role-placement=random: decode_failures 56

> slower: 8.52 s per simulated hour against 2.05 over 36 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.902 | 0.912 | 0.319 | 1.18x | 12.9/25.5/30.0% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.853 | 0.846 | 0.006 | - | - | 0.969 | 0.971 | 0.560 | 2.61x | 28.3/39.1/43.2% | 4.3/5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 28

> slower: 6.55 s per simulated hour against 2.59 over 36 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.902 | 0.912 | 0.319 | 1.18x | 12.9/25.5/30.0% | 1.9/5.1% | 3 |
| no-mute | 1 | 0.798 | 0.788 | 0.010 | - | - | 0.939 | 0.942 | 0.373 | 1.28x | 14.0/22.8/27.3% | 1.9/5.0% | 3 |
| all-routers | 1 | 0.853 | 0.846 | 0.006 | - | - | 0.969 | 0.971 | 0.560 | 2.61x | 28.3/39.1/43.2% | 4.3/5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 28

> slower: 5.04 s per simulated hour against 2.42 over 36 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.902 | 0.912 | 0.319 | 1.18x | 12.9/25.5/30.0% | 1.9/5.1% | 3 |
| local-typical | 1 | 0.516 | 0.494 | 0.023 | - | - | 0.703 | 0.747 | 0.000 | 1.19x | 10.8/18.5/27.4% | 2.0/4.6% | 3 |
| basement-heavy | 1 | 0.076 | 0.075 | 0.000 | - | - | 0.273 | 0.277 | 0.000 | 0.48x | 1.6/5.1/9.9% | 0.4/2.7% | 3 |

> siting-mix=uniform: decode_failures 28

> siting-mix=local-typical: decode_failures 31

> slower: 3.88 s per simulated hour against 1.44 over 36 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.878 | 0.875 | 0.002 | - | - | 0.733 | 0.984 | 0.000 | 2.18x | 19.0/28.9/36.0% | 1.7/5.5% | 3 |
| inverse | 1 | 0.859 | 0.853 | 0.006 | - | - | 0.772 | 0.988 | 0.000 | 2.04x | 16.9/24.9/31.2% | 1.6/3.1% | 3 |

> role-placement=degree: decode_failures 18

> role-placement=inverse: decode_failures 28

> slower: 7.17 s per simulated hour against 3.48 over 36 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.777 | 0.777 | 0.000 | - | - | 0 | 0.000 | 0.218 | 1.33x | 14.3/27.6/32.0% | 1.9/4.8% | 3 |
| sr | 1 | 0.817 | 0.776 | 0.041 | - | - | 0.879 | 0.974 | 0.245 | 1.38x | 14.7/28.2/32.6% | 2.0/5.0% | 3 |

> protocol=sr: decode_failures 38

> slower: 6.73 s per simulated hour against 1.78 over 36 prior run(s) - 3.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.705 | 0.691 | 0.014 | - | - | 0.853 | 0.864 | 0.251 | 2.80x | 30.5/56.2/61.2% | 4.4/9.4% | 3 |
| 100 | 1 | 0.820 | 0.810 | 0.010 | - | - | 0.946 | 0.949 | 0.332 | 1.55x | 16.5/33.4/37.0% | 2.4/5.1% | 3 |
| 120 | 1 | 0.820 | 0.810 | 0.010 | - | - | 0.946 | 0.949 | 0.332 | 1.55x | 16.5/33.4/37.0% | 2.4/5.1% | 3 |
| 250 | 1 | 0.820 | 0.810 | 0.010 | - | - | 0.946 | 0.949 | 0.332 | 1.55x | 16.5/33.4/37.0% | 2.4/5.1% | 3 |

> max-num-nodes=10: decode_failures 5

> max-num-nodes=100: decode_failures 1

> max-num-nodes=120: decode_failures 1

> max-num-nodes=250: decode_failures 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.361 | 0.354 | 0.007 | - | - | 0.600 | 0.627 | 0.100 | 11.54x | 41.9/60.5/71.7% | 4.0/11.6% | 3 |
| 120 | 1 | 0.594 | 0.586 | 0.008 | - | - | 0.884 | 0.885 | 0.141 | 4.60x | 17.3/28.6/38.7% | 1.5/6.0% | 3 |
| 250 | 1 | 0.601 | 0.593 | 0.008 | - | - | 0.892 | 0.893 | 0.140 | 4.42x | 16.8/26.8/36.6% | 1.4/5.6% | 3 |

> max-num-nodes=10: decode_failures 46

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.820 | 0.810 | 0.010 | - | - | 0.946 | 0.949 | 0.332 | 1.55x | 16.5/33.4/37.0% | 2.4/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.820 | 0.810 | 0.010 | - | - | 0.946 | 0.949 | 0.332 | 1.55x | 16.5/33.4/37.0% | 2.4/5.1% | 3 |
| constrained | 1 | 0.710 | 0.697 | 0.013 | - | - | 0.863 | 0.874 | 0.271 | 2.80x | 30.5/55.9/61.1% | 4.4/9.4% | 3 |

> platform-mix=uniform: decode_failures 1

> platform-mix=baymesh-2026-08: decode_failures 1

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.754 | 0.744 | 0.010 | - | - | 0.902 | 0.932 | 0.487 | 5.61x | 57.1/71.2/74.7% | 3.8/12.7% | 3 |
| 25 | 1 | 0.754 | 0.744 | 0.010 | - | - | 0.902 | 0.932 | 0.487 | 5.61x | 57.1/71.2/74.7% | 3.8/12.7% | 3 |
| 100 | 1 | 0.754 | 0.744 | 0.010 | - | - | 0.902 | 0.932 | 0.487 | 5.61x | 57.1/71.2/74.7% | 3.8/12.7% | 3 |
| 2000 | 1 | 0.754 | 0.744 | 0.010 | - | - | 0.902 | 0.932 | 0.487 | 5.61x | 57.1/71.2/74.7% | 3.8/12.7% | 3 |

> warm-num-nodes=0: queue drops 11.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 130

> warm-num-nodes=25: queue drops 11.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 130

> warm-num-nodes=100: queue drops 11.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 130

> warm-num-nodes=2000: queue drops 11.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 130

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.1 | 1 | 0.677 | 0.659 | 0.018 | - | - | 0.874 | 0.905 | 0.187 | 1.27x | 14.0/26.1/30.6% | 1.9/4.5% | 3 |
| 0.2 | 1 | 0.581 | 0.558 | 0.022 | - | - | 0.783 | 0.855 | 0.179 | 1.16x | 13.1/23.9/28.3% | 1.8/4.1% | 3 |
| 0.3 | 1 | 0.463 | 0.442 | 0.021 | - | - | 0.651 | 0.770 | 0.111 | 1.06x | 12.1/22.1/26.6% | 1.6/3.7% | 3 |

> burst-loss=0.0: decode_failures 2

> burst-loss=0.1: decode_failures 37

> burst-loss=0.2: decode_failures 33

> burst-loss=0.3: decode_failures 18

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.1 | 1 | 0.741 | 0.728 | 0.013 | - | - | 0.918 | 0.926 | 0.228 | 1.40x | 15.7/28.2/33.1% | 2.1/4.9% | 3 |
| 0.2 | 1 | 0.676 | 0.660 | 0.015 | - | - | 0.880 | 0.896 | 0.196 | 1.39x | 15.8/27.5/32.6% | 2.1/4.7% | 3 |
| 0.3 | 1 | 0.629 | 0.615 | 0.014 | - | - | 0.814 | 0.888 | 0.166 | 1.40x | 16.3/27.5/32.9% | 2.1/4.6% | 3 |

> extra-loss=0.0: decode_failures 2

> extra-loss=0.2: decode_failures 7

> extra-loss=0.3: decode_failures 29

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.1 | 1 | 0.654 | 0.636 | 0.018 | - | - | 0.827 | 0.877 | 0.182 | 1.26x | 13.9/26.4/30.8% | 1.9/4.6% | 3 |
| 0.2 | 1 | 0.531 | 0.512 | 0.019 | - | - | 0.739 | 0.846 | 0.146 | 1.16x | 13.1/24.4/28.8% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.424 | 0.411 | 0.013 | - | - | 0.543 | 0.715 | 0.089 | 1.05x | 12.4/21.6/26.3% | 1.6/3.6% | 3 |

> burst-loss=0.0: decode_failures 2

> burst-loss=0.1: decode_failures 25

> burst-loss=0.2: decode_failures 34

> burst-loss=0.3: decode_failures 14

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.734 | 0.734 | 0.000 | - | - | 0.848 | 0.927 | 0.227 | 1.76x | 18.8/36.4/42.0% | 2.5/6.5% | 3 |
| directed-with-late-flood | 1 | 0.748 | 0.748 | 0.000 | - | - | 0.806 | 0.926 | 0.209 | 1.58x | 17.1/32.7/37.9% | 2.3/5.8% | 3 |
| m4-early-flood | 1 | 0.753 | 0.753 | 0.000 | - | - | 0.819 | 0.936 | 0.222 | 1.59x | 17.0/33.1/38.3% | 2.3/5.9% | 3 |

> dm-mode=flood-only: decode_failures 34

> dm-mode=directed-with-late-flood: decode_failures 34

> dm-mode=m4-early-flood: decode_failures 39

> slower: 7.45 s per simulated hour against 3.17 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.818 | 0.813 | 0.005 | - | - | 0.963 | 0.964 | 0.380 | 0.72x | 8.0/10.6/11.9% | 1.1/2.0% | 3 |
| 2.8 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> profile=2.8: decode_failures 2

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.25 | 1 | 0.828 | 0.821 | 0.008 | - | - | 0.948 | 0.951 | 0.531 | 1.18x | 13.9/22.7/25.9% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.814 | 0.804 | 0.011 | - | - | 0.921 | 0.924 | 0.509 | 0.99x | 11.1/17.9/19.2% | 1.6/3.9% | 3 |
| 0.75 | 1 | 0.787 | 0.776 | 0.011 | - | - | 0.962 | 0.963 | 0.356 | 0.80x | 9.0/13.2/14.7% | 1.3/2.6% | 3 |

> legacy-fraction=0.0: decode_failures 2

> legacy-fraction=0.75: decode_failures 1

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.25 | 1 | 0.830 | 0.822 | 0.007 | - | - | 0.944 | 0.946 | 0.545 | 1.17x | 14.1/22.7/25.8% | 1.8/4.6% | 3 |
| 0.5 | 1 | 0.828 | 0.816 | 0.012 | - | - | 0.928 | 0.932 | 0.558 | 1.00x | 11.6/18.1/19.6% | 1.5/3.9% | 3 |
| 0.75 | 1 | 0.779 | 0.768 | 0.011 | - | - | 0.931 | 0.955 | 0.351 | 0.78x | 8.8/13.3/14.9% | 1.3/2.6% | 3 |

> legacy-fraction=0.0: decode_failures 2

> legacy-fraction=0.5: decode_failures 2

> legacy-fraction=0.75: decode_failures 24

> slower: 3.33 s per simulated hour against 1.66 over 36 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.826 | 0.817 | 0.009 | - | - | 0.965 | 0.968 | 0.267 | 0.74x | 8.2/16.7/19.4% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> profile-flag=signing=true: decode_failures 2

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.810 | 0.806 | 0.004 | - | - | 0.957 | 0.958 | 0.333 | 0.72x | 8.1/11.2/12.8% | 1.2/2.1% | 3 |
| 2.5 | 1 | 0.791 | 0.786 | 0.005 | - | - | 0.949 | 0.949 | 0.315 | 0.70x | 7.8/10.9/12.5% | 1.1/2.1% | 3 |
| 2.6 | 1 | 0.795 | 0.790 | 0.005 | - | - | 0.965 | 0.966 | 0.321 | 0.68x | 7.9/10.9/12.5% | 1.1/2.1% | 3 |
| 2.7 | 1 | 0.826 | 0.822 | 0.004 | - | - | 0.958 | 0.960 | 0.333 | 0.76x | 8.2/14.9/16.9% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> profile=2.8: decode_failures 2

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.817 | 0.807 | 0.010 | - | - | 0.973 | 0.975 | 0.279 | 0.94x | 10.1/19.8/22.9% | 1.4/3.6% | 3 |
| 900 | 1 | 0.717 | 0.705 | 0.013 | - | - | 0.884 | 0.897 | 0.208 | 2.12x | 22.7/42.1/48.8% | 3.2/7.4% | 3 |
| 300 | 1 | 0.467 | 0.457 | 0.009 | - | - | 0.566 | 0.701 | 0.144 | 4.34x | 45.7/72.3/79.2% | 6.5/12.6% | 3 |

> broadcast-interval-s=3600: decode_failures 1

> broadcast-interval-s=900: decode_failures 20

> broadcast-interval-s=300: decode_failures 30

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.975 | 0.978 | 0.513 | 1.05x | 10.8/19.9/22.9% | 1.6/3.6% | 3 |
| 900 | 1 | 0.826 | 0.817 | 0.009 | - | - | 0.920 | 0.926 | 0.447 | 2.35x | 24.8/43.2/50.0% | 3.6/7.5% | 3 |
| 300 | 1 | 0.524 | 0.518 | 0.006 | - | - | 0.596 | 0.696 | 0.319 | 4.85x | 49.1/73.9/80.4% | 7.4/13.3% | 3 |

> broadcast-interval-s=300: decode_failures 26

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.814 | 0.803 | 0.011 | - | - | 0.968 | 0.968 | 0.248 | 1.30x | 14.0/26.9/31.4% | 1.9/4.9% | 3 |
| sinusoid | 1 | 0.788 | 0.778 | 0.010 | - | - | 0.941 | 0.941 | 0.264 | 1.28x | 13.7/26.5/30.7% | 1.9/4.7% | 3 |
| commuter | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> diurnal=flat: decode_failures 1

> diurnal=commuter: decode_failures 2

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.717 | 0.705 | 0.013 | - | - | 0.884 | 0.897 | 0.208 | 2.12x | 22.7/42.1/48.8% | 3.2/7.4% | 3 |
| 3600 | 1 | 0.817 | 0.807 | 0.010 | - | - | 0.973 | 0.975 | 0.279 | 0.94x | 10.1/19.8/22.9% | 1.4/3.6% | 3 |
| 10800 | 1 | 0.839 | 0.831 | 0.008 | - | - | 0.973 | 0.974 | 0.291 | 0.64x | 6.8/13.7/15.7% | 0.9/2.6% | 3 |
| 43200 | 1 | 0.850 | 0.843 | 0.007 | - | - | 0.974 | 0.976 | 0.301 | 0.43x | 4.5/9.2/10.5% | 0.6/1.7% | 3 |

> broadcast-interval-s=900: decode_failures 20

> broadcast-interval-s=3600: decode_failures 1

> broadcast-interval-s=43200: decode_failures 1

> slower: 3.39 s per simulated hour against 1.35 over 36 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.25 | 1 | 0.782 | 0.770 | 0.011 | - | - | 0.942 | 0.945 | 0.244 | 1.41x | 15.3/29.3/33.9% | 2.1/5.2% | 3 |
| 1.0 | 1 | 0.762 | 0.750 | 0.012 | - | - | 0.918 | 0.932 | 0.229 | 1.52x | 16.5/31.4/36.7% | 2.2/5.6% | 3 |
| 4.0 | 1 | 0.724 | 0.710 | 0.014 | - | - | 0.900 | 0.916 | 0.227 | 1.92x | 21.3/39.2/46.2% | 2.9/6.9% | 3 |

> traceroute-per-hour=0.0: decode_failures 2

> traceroute-per-hour=0.25: decode_failures 2

> traceroute-per-hour=1.0: decode_failures 47

> traceroute-per-hour=4.0: decode_failures 26

> slower: 7.11 s per simulated hour against 2.1 over 36 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.754 | 0.744 | 0.010 | - | - | 0.902 | 0.932 | 0.487 | 5.61x | 57.1/71.2/74.7% | 3.8/12.7% | 3 |
| 1.0 | 1 | 0.685 | 0.674 | 0.011 | - | - | 0.844 | 0.895 | 0.430 | 6.21x | 61.4/73.7/77.1% | 4.4/14.1% | 3 |

> traceroute-per-hour=0.0: queue drops 11.7% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 130

> traceroute-per-hour=1.0: queue drops 18.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 108

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.614 | 0.600 | 0.014 | - | - | 0.810 | 0.812 | 0.000 | 1.26x | 16.6/23.4/25.6% | 3.0/6.5% | 3 |
| 60 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 90 | 1 | 0.947 | 0.945 | 0.002 | - | - | 0.990 | 0.992 | 0.694 | 1.53x | 18.2/23.7/25.9% | 1.4/5.1% | 3 |
| 120 | 1 | 0.956 | 0.954 | 0.001 | - | - | 0.998 | 0.998 | 0.780 | 1.96x | 21.7/30.5/34.1% | 1.2/5.2% | 3 |
| 150 | 1 | 0.961 | 0.961 | 0.001 | - | - | 0.999 | 0.999 | 0.740 | 2.44x | 27.1/37.5/43.7% | 1.2/5.5% | 3 |

> nodes=60: decode_failures 2

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 120 | 1 | 0.777 | 0.769 | 0.009 | - | - | 0.977 | 0.978 | 0.462 | 1.99x | 14.9/23.4/32.1% | 1.3/5.3% | 3 |
| 250 | 1 | 0.587 | 0.578 | 0.009 | - | - | 0.875 | 0.875 | 0.134 | 4.94x | 18.6/30.3/41.3% | 1.6/6.5% | 3 |
| 500 | 1 | 0.321 | 0.317 | 0.004 | - | - | 0.484 | 0.495 | 0.090 | 9.98x | 19.4/31.0/43.6% | 1.6/7.2% | 3 |

> nodes=60: decode_failures 2

> nodes=500: decode_failures 123

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.785 | 0.777 | 0.007 | - | - | 0.975 | 0.977 | 0.469 | 1.87x | 13.9/21.8/29.8% | 1.2/4.9% | 3 |
| 250 | 1 | 0.594 | 0.586 | 0.008 | - | - | 0.884 | 0.885 | 0.141 | 4.60x | 17.3/28.6/38.7% | 1.5/6.0% | 3 |
| 500 | 1 | 0.324 | 0.320 | 0.004 | - | - | 0.502 | 0.504 | 0.089 | 9.21x | 17.7/28.8/41.6% | 1.5/6.9% | 3 |

> nodes=500: decode_failures 29

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.789 | 0.778 | 0.011 | - | - | 0.952 | 0.955 | 0.340 | 1.33x | 14.4/27.9/32.3% | 1.9/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.761 | 0.753 | 0.008 | - | - | 0.902 | 0.912 | 0.319 | 1.18x | 12.9/25.5/30.0% | 1.9/5.1% | 3 |

> role-mix=legacy-default: decode_failures 2

> role-mix=baymesh-2026-08: decode_failures 28

> slower: 6.12 s per simulated hour against 1.78 over 36 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.816 | 0.805 | 0.011 | - | - | 0.954 | 0.956 | 0.396 | 1.38x | 14.9/28.1/32.5% | 2.0/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.776 | 0.769 | 0.007 | - | - | 0.893 | 0.898 | 0.401 | 1.25x | 13.7/27.7/32.7% | 2.1/4.8% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.05 | 1 | 0.790 | 0.779 | 0.011 | - | - | 0.940 | 0.942 | 0.279 | 1.46x | 16.8/31.1/34.0% | 2.1/5.0% | 3 |
| 0.1 | 1 | 0.792 | 0.781 | 0.011 | - | - | 0.942 | 0.946 | 0.268 | 1.55x | 16.9/33.7/37.7% | 2.2/5.0% | 3 |
| 0.2 | 1 | 0.802 | 0.791 | 0.011 | - | - | 0.946 | 0.955 | 0.268 | 1.72x | 18.9/37.8/42.6% | 2.3/5.3% | 3 |

> router-late-fraction=0.0: decode_failures 2

> router-late-fraction=0.05: decode_failures 1

> router-late-fraction=0.1: decode_failures 1

> router-late-fraction=0.2: decode_failures 10

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| local-typical | 1 | 0.569 | 0.548 | 0.021 | - | - | 0.732 | 0.801 | 0.000 | 1.36x | 10.8/21.2/29.2% | 2.1/4.7% | 3 |
| event | 1 | 0.161 | 0.161 | 0.000 | - | - | 0.383 | 0.383 | 0.000 | 0.95x | 3.6/17.8/23.5% | 1.1/4.4% | 3 |
| backbone | 1 | 0.972 | 0.971 | 0.001 | - | - | 0.998 | 0.999 | 0.739 | 1.05x | 21.6/29.8/35.7% | 1.2/5.5% | 3 |

> siting-mix=uniform: decode_failures 2

> siting-mix=local-typical: decode_failures 25

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.775 | 0.758 | 0.018 | - | - | 0.869 | 0.896 | 0.098 | 1.32x | 22.0/31.5/33.2% | 3.0/7.1% | 3 |
| 60 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 90 | 1 | 0.796 | 0.782 | 0.014 | - | - | 0.955 | 0.957 | 0.358 | 1.60x | 15.2/20.7/24.4% | 1.6/4.9% | 3 |
| 120 | 1 | 0.777 | 0.769 | 0.009 | - | - | 0.977 | 0.978 | 0.462 | 1.99x | 14.9/23.4/32.1% | 1.3/5.3% | 3 |
| 150 | 1 | 0.725 | 0.710 | 0.015 | - | - | 0.835 | 0.837 | 0.266 | 2.59x | 15.8/25.4/31.0% | 1.4/5.0% | 3 |

> nodes=40: decode_failures 13

> nodes=60: decode_failures 2

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 1.25 | 1 | 0.510 | 0.495 | 0.015 | - | - | 0.727 | 0.809 | 0.186 | 1.25x | 10.3/18.9/21.7% | 2.1/4.3% | 3 |
| 1.5 | 1 | 0.266 | 0.263 | 0.003 | - | - | 0.447 | 0.447 | 0.068 | 1.32x | 7.9/22.2/27.3% | 1.8/5.3% | 3 |
| 2.0 | 1 | 0.126 | 0.124 | 0.002 | - | - | 0.306 | 0.307 | 0.000 | 0.82x | 3.4/9.6/15.6% | 1.0/3.7% | 3 |

> stretch=1.0: decode_failures 2

> stretch=1.25: decode_failures 19

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| clustered | 1 | 0.861 | 0.861 | 0.000 | - | - | 0.943 | 0.943 | 0.000 | 1.13x | 31.2/39.7/41.0% | 1.2/5.6% | 3 |
| corridor | 1 | 0.490 | 0.480 | 0.010 | - | - | 0.447 | 0.477 | 0.000 | 1.29x | 15.4/19.3/23.0% | 1.9/5.1% | 3 |
| hub | 1 | 0.953 | 0.950 | 0.003 | - | - | 0.986 | 0.987 | 0.726 | 1.20x | 25.5/36.7/38.5% | 1.8/5.4% | 3 |

> topology=uniform: decode_failures 2

> topology=corridor: decode_failures 13

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.748 | 0.748 | 0.000 | - | - | 0.806 | 0.926 | 0.209 | 1.58x | 17.1/32.7/37.9% | 2.3/5.8% | 3 |
| True | 1 | 0.741 | 0.741 | 0.000 | - | - | 0.821 | 0.920 | 0.215 | 1.62x | 17.5/33.8/39.1% | 2.3/6.1% | 3 |

> coding-rate-ladder=False: decode_failures 34

> coding-rate-ladder=True: decode_failures 45

> slower: 13.6 s per simulated hour against 2.77 over 36 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.741 | 0.741 | 0.000 | - | - | 0.821 | 0.920 | 0.215 | 1.62x | 17.5/33.8/39.1% | 2.3/6.1% | 3 |
| m4-early-flood | 1 | 0.738 | 0.738 | 0.000 | - | - | 0.818 | 0.915 | 0.225 | 1.61x | 17.4/33.4/38.7% | 2.3/6.0% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 45

> dm-mode=m4-early-flood: decode_failures 43

> slower: 11.8 s per simulated hour against 2.68 over 36 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.777 | 0.777 | 0.000 | - | - | 0 | 0.000 | 0.218 | 1.33x | 14.3/27.6/32.0% | 1.9/4.8% | 3 |
| chain | 1 | 0.757 | 0.751 | 0.006 | - | - | 0.809 | 0.926 | 0.234 | 1.56x | 16.9/32.4/37.8% | 2.2/5.8% | 3 |
| sr | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> protocol=sr: decode_failures 2

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| True | 1 | 0.792 | 0.781 | 0.011 | - | - | 0.945 | 0.949 | 0.298 | 1.39x | 15.0/28.3/33.0% | 2.0/5.1% | 3 |

> extra-repeats=False: decode_failures 2

> extra-repeats=True: decode_failures 2

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.954 | 0.001 | - | - | 0.998 | 0.998 | 0.780 | 1.96x | 21.7/30.5/34.1% | 1.2/5.2% | 3 |
| True | 1 | 0.956 | 0.954 | 0.002 | - | - | 0.998 | 0.998 | 0.771 | 1.98x | 21.7/30.5/34.0% | 1.2/5.2% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.150 | 0.149 | 0.002 | - | - | 0.368 | 0.370 | 0.000 | 0.04x | 0.2/0.6/1.0% | 0.0/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.319 | 0.318 | 0.002 | - | - | 0.504 | 0.505 | 0.072 | 0.22x | 1.5/3.3/4.1% | 0.3/0.9% | 3 |
| LONG_TURBO | 1 | 0.703 | 0.686 | 0.017 | - | - | 0.919 | 0.922 | 0.256 | 1.26x | 12.0/20.9/24.3% | 1.8/4.4% | 3 |

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 0.25 | 1 | 0.816 | 0.803 | 0.013 | - | - | 0.948 | 0.953 | 0.388 | 1.27x | 16.1/28.8/32.9% | 1.8/5.0% | 3 |
| 1.0 | 1 | 0.899 | 0.890 | 0.010 | - | - | 0.974 | 0.979 | 0.642 | 0.99x | 20.7/28.6/32.4% | 1.3/4.8% | 3 |

> duct-per-hour=0.0: decode_failures 2

> duct-per-hour=0.25: decode_failures 1

> duct-per-hour=1.0: decode_failures 1

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.250 | 0.247 | 0.003 | - | - | 0.482 | 0.483 | 0.048 | 0.12x | 0.6/1.8/2.6% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| LITE_FAST | 1 | 0.725 | 0.709 | 0.015 | - | - | 0.943 | 0.946 | 0.233 | 0.98x | 10.8/18.0/20.5% | 1.5/3.7% | 3 |
| NARROW_SLOW | 1 | 0.762 | 0.739 | 0.023 | - | - | 0.937 | 0.951 | 0.189 | 1.28x | 13.7/23.9/25.4% | 1.9/4.9% | 3 |

> preset=LONG_FAST: decode_failures 2

> preset=NARROW_SLOW: decode_failures 22

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| temporal | 1 | 0.685 | 0.673 | 0.012 | - | - | 0.886 | 0.898 | 0.249 | 1.32x | 14.2/26.0/30.6% | 1.9/4.7% | 3 |
| transient | 1 | 0.780 | 0.768 | 0.013 | - | - | 0.942 | 0.946 | 0.232 | 1.36x | 14.6/28.1/32.6% | 2.0/5.0% | 3 |
| periodic | 1 | 0.592 | 0.585 | 0.008 | - | - | 0.704 | 0.759 | 0.170 | 1.23x | 13.5/24.9/29.2% | 1.9/4.3% | 3 |

> noise-profile=none: decode_failures 2

> noise-profile=temporal: decode_failures 2

> noise-profile=transient: decode_failures 4

> noise-profile=periodic: decode_failures 17

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.250 | 0.247 | 0.003 | - | - | 0.482 | 0.483 | 0.048 | 0.12x | 0.6/1.8/2.6% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| LONG_MODERATE | 1 | 0.760 | 0.741 | 0.018 | - | - | 0.911 | 0.913 | 0.370 | 3.31x | 42.6/59.0/61.3% | 4.6/12.4% | 3 |

> preset=LONG_FAST: decode_failures 2

> preset=LONG_MODERATE: decode_failures 5

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.061 | 0.061 | 0.000 | - | - | 0.170 | 0.171 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.150 | 0.149 | 0.002 | - | - | 0.368 | 0.370 | 0.000 | 0.04x | 0.2/0.6/1.0% | 0.0/0.2% | 3 |
| LONG_FAST | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| LONG_TURBO | 1 | 0.703 | 0.686 | 0.017 | - | - | 0.919 | 0.922 | 0.256 | 1.26x | 12.0/20.9/24.3% | 1.8/4.4% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.759 | 0.746 | 0.013 | - | - | 0.913 | 0.927 | 0.239 | 1.80x | 19.0/33.2/36.8% | 2.7/6.6% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 6

> preset=LONG_FAST: decode_failures 2

> preset=EXTRA_LONG_TURBO: decode_failures 35

> slower: 4.28 s per simulated hour against 1.53 over 32 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.728 | 0.717 | 0.011 | - | - | 0.872 | 0.893 | 0.228 | 1.31x | 14.4/27.1/31.6% | 1.9/4.7% | 3 |
| 10000 | 1 | 0.592 | 0.585 | 0.008 | - | - | 0.704 | 0.759 | 0.170 | 1.23x | 13.5/24.9/29.2% | 1.9/4.3% | 3 |
| 4000 | 1 | 0.356 | 0.354 | 0.002 | - | - | 0.404 | 0.520 | 0.082 | 1.01x | 11.3/19.8/23.8% | 1.6/3.1% | 3 |
| 2000 | 1 | 0.100 | 0.100 | 0.000 | - | - | 0.098 | 0.183 | 0.008 | 0.69x | 8.3/13.5/16.9% | 1.1/1.9% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 22

> noise-pulse-interval-ms=10000: decode_failures 17

> noise-pulse-interval-ms=4000: decode_failures 1

> slower: 4.09 s per simulated hour against 1.67 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.266 | 0.263 | 0.003 | - | - | 0.447 | 0.447 | 0.068 | 1.32x | 7.9/22.2/27.3% | 1.8/5.3% | 3 |
| 1.0 | 1 | 0.600 | 0.598 | 0.002 | - | - | 0.720 | 0.721 | 0.444 | 0.90x | 11.4/21.0/22.4% | 1.2/3.9% | 3 |

> faster: 0.971 s per simulated hour against 1.96 over 36 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 22 | 1 | 0.306 | 0.303 | 0.003 | - | - | 0.467 | 0.467 | 0.066 | 1.42x | 9.5/19.4/24.5% | 2.0/5.4% | 3 |
| 17 | 1 | 0.149 | 0.147 | 0.002 | - | - | 0.365 | 0.365 | 0.000 | 0.89x | 3.4/13.8/18.5% | 1.1/4.2% | 3 |
| 14 | 1 | 0.097 | 0.094 | 0.003 | - | - | 0.242 | 0.273 | 0.000 | 0.65x | 2.5/6.2/11.2% | 0.9/2.8% | 3 |

> tx-power=30: decode_failures 2

> tx-power=14: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.954 | 0.001 | - | - | 0.998 | 0.998 | 0.780 | 1.96x | 21.7/30.5/34.1% | 1.2/5.2% | 3 |
| True | 1 | 0.948 | 0.946 | 0.002 | - | - | 0.998 | 0.998 | 0.759 | 2.33x | 25.1/34.3/37.7% | 1.4/5.8% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

> no-adopt-hop-recommendation=True: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.797 | 0.787 | 0.010 | - | - | 0.943 | 0.963 | 0.213 | 1.40x | 15.7/30.1/33.2% | 2.1/5.1% | 3 |
| True | 1 | 0.810 | 0.799 | 0.011 | - | - | 0.939 | 0.942 | 0.292 | 1.43x | 16.4/30.1/33.1% | 2.1/5.0% | 3 |

> favourite-routers=False: decode_failures 33

> favourite-routers=True: decode_failures 1

> slower: 4.75 s per simulated hour against 1.67 over 36 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| random | 1 | 0.796 | 0.782 | 0.014 | - | - | 0.944 | 0.945 | 0.364 | 1.37x | 14.6/27.1/31.5% | 2.0/4.8% | 3 |

> hop-assign=centrality: decode_failures 2

> hop-assign=random: decode_failures 1

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.645 | 0.619 | 0.026 | - | - | 0.862 | 0.904 | 0.124 | 1.06x | 11.5/22.9/26.7% | 1.5/4.2% | 3 |
| 7 | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.950 | 0.950 | 0.482 | 1.55x | 16.3/29.2/33.8% | 2.3/5.1% | 3 |
| 15 | 1 | 0.887 | 0.883 | 0.005 | - | - | 0.942 | 0.943 | 0.571 | 1.59x | 16.5/29.7/34.4% | 2.4/5.2% | 3 |
| 32 | 1 | 0.895 | 0.890 | 0.005 | - | - | 0.953 | 0.954 | 0.580 | 1.59x | 16.6/29.7/34.3% | 2.4/5.2% | 3 |

> hop-limit=3: decode_failures 37

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.645 | 0.619 | 0.026 | - | - | 0.862 | 0.904 | 0.124 | 1.06x | 11.5/22.9/26.7% | 1.5/4.2% | 3 |
| 5 | 1 | 0.802 | 0.789 | 0.013 | - | - | 0.943 | 0.944 | 0.326 | 1.40x | 15.0/27.4/32.0% | 2.1/4.9% | 3 |
| 7 | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.950 | 0.950 | 0.482 | 1.55x | 16.3/29.2/33.8% | 2.3/5.1% | 3 |

> hop-limit=3: decode_failures 37

> hop-limit=5: decode_failures 2

> slower: 5.89 s per simulated hour against 2.04 over 36 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| KNOWN_ONLY | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.782 | 0.782 | 0.000 | - | - | 0.778 | 0.951 | 0.236 | 1.33x | 14.3/27.6/31.9% | 1.9/4.8% | 3 |

> rebroadcast-mode=ALL: decode_failures 2

> rebroadcast-mode=KNOWN_ONLY: decode_failures 2

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.645 | 0.619 | 0.026 | - | - | 0.862 | 0.904 | 0.124 | 1.06x | 11.5/22.9/26.7% | 1.5/4.2% | 3 |
| True | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> hop-spread=False: decode_failures 37

> hop-spread=True: decode_failures 2

> slower: 7.58 s per simulated hour against 2.33 over 36 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| BALANCED | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| STRICT | 1 | 0.660 | 0.660 | 0.000 | - | - | 0.814 | 0.837 | 0.146 | 1.51x | 16.3/31.0/36.0% | 2.3/5.5% | 3 |

> signature-policy=COMPATIBLE: decode_failures 2

> signature-policy=BALANCED: decode_failures 2

> signature-policy=STRICT: decode_failures 49

> slower: 6.18 s per simulated hour against 1.81 over 36 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| dm | 1 | 0.783 | 0.772 | 0.011 | - | - | 0.936 | 0.938 | 0.249 | 1.33x | 14.4/27.7/32.3% | 2.0/5.0% | 3 |

> advert-transport=broadcast: decode_failures 2

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.784 | 0.772 | 0.012 | - | - | 0.937 | 0.941 | 0.259 | 1.37x | 14.7/28.3/32.9% | 2.0/5.1% | 3 |
| local | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| time | 1 | 0.783 | 0.773 | 0.011 | - | - | 0.937 | 0.949 | 0.234 | 1.40x | 15.0/29.1/33.8% | 2.0/5.2% | 3 |
| window | 1 | 0.781 | 0.769 | 0.012 | - | - | 0.923 | 0.940 | 0.267 | 1.35x | 14.4/27.8/32.3% | 2.0/5.0% | 3 |

> bucket-mode=global: misdecodes 24

> bucket-mode=local: decode_failures 2

> bucket-mode=time: misdecodes 8

> bucket-mode=window: misdecodes 9

> bucket-mode=window: decode_failures 2

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.770 | 0.756 | 0.013 | - | - | 0.928 | 0.931 | 0.244 | 1.51x | 16.1/31.3/36.1% | 2.2/5.7% | 3 |
| 1800 | 1 | 0.783 | 0.773 | 0.011 | - | - | 0.937 | 0.949 | 0.234 | 1.40x | 15.0/29.1/33.8% | 2.0/5.2% | 3 |
| 3600 | 1 | 0.779 | 0.770 | 0.009 | - | - | 0.928 | 0.946 | 0.246 | 1.36x | 14.5/28.4/32.9% | 2.0/5.1% | 3 |

> time-bucket-s=600: misdecodes 70

> time-bucket-s=1800: misdecodes 8

> time-bucket-s=3600: misdecodes 5

> time-bucket-s=3600: decode_failures 16

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| interval | 1 | 0.741 | 0.726 | 0.015 | - | - | 0.897 | 0.908 | 0.243 | 1.82x | 19.3/37.9/43.7% | 2.6/7.2% | 3 |
| aimd | 1 | 0.784 | 0.780 | 0.003 | - | - | 0.828 | 0.957 | 0.271 | 1.38x | 14.9/28.4/33.1% | 2.0/5.0% | 3 |
| bucket+interval | 1 | 0.742 | 0.725 | 0.016 | - | - | 0.907 | 0.909 | 0.223 | 1.85x | 19.6/38.2/43.9% | 2.7/7.2% | 3 |

> trigger=bucket: decode_failures 2

> trigger=interval: misdecodes 17

> trigger=interval: decode_failures 2

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 24

> trigger=bucket+interval: misdecodes 19

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.788 | 0.778 | 0.010 | - | - | 0.928 | 0.952 | 0.263 | 1.35x | 14.5/28.0/32.5% | 2.0/5.0% | 3 |
| 8 | 1 | 0.783 | 0.773 | 0.010 | - | - | 0.914 | 0.943 | 0.262 | 1.34x | 14.5/27.8/32.4% | 1.9/4.9% | 3 |
| 16 | 1 | 0.789 | 0.778 | 0.011 | - | - | 0.950 | 0.958 | 0.240 | 1.37x | 14.6/28.2/32.7% | 2.0/5.0% | 3 |
| 32 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 50 | 1 | 0.791 | 0.781 | 0.010 | - | - | 0.944 | 0.948 | 0.276 | 1.37x | 14.7/28.3/32.9% | 2.0/5.0% | 3 |

> capacity=4: decode_failures 71

> capacity=8: decode_failures 62

> capacity=16: decode_failures 43

> capacity=32: decode_failures 2

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.788 | 0.778 | 0.010 | - | - | 0.928 | 0.952 | 0.263 | 1.35x | 14.5/28.0/32.5% | 2.0/5.0% | 3 |
| 8 | 1 | 0.783 | 0.773 | 0.010 | - | - | 0.914 | 0.943 | 0.262 | 1.34x | 14.5/27.8/32.4% | 1.9/4.9% | 3 |
| 16 | 1 | 0.789 | 0.778 | 0.011 | - | - | 0.950 | 0.958 | 0.240 | 1.37x | 14.6/28.2/32.7% | 2.0/5.0% | 3 |
| 32 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 50 | 1 | 0.791 | 0.781 | 0.010 | - | - | 0.944 | 0.948 | 0.276 | 1.37x | 14.7/28.3/32.9% | 2.0/5.0% | 3 |

> capacity=4: decode_failures 71

> capacity=8: decode_failures 62

> capacity=16: decode_failures 43

> capacity=32: decode_failures 2

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.778 | 0.775 | 0.003 | - | - | 0.819 | 0.953 | 0.227 | 1.34x | 14.4/27.8/32.2% | 2.0/4.8% | 3 |
| 16 | 1 | 0.780 | 0.776 | 0.004 | - | - | 0.845 | 0.942 | 0.254 | 1.34x | 14.3/27.6/32.0% | 2.0/4.8% | 3 |
| 32 | 1 | 0.781 | 0.769 | 0.012 | - | - | 0.923 | 0.940 | 0.267 | 1.35x | 14.4/27.8/32.3% | 2.0/5.0% | 3 |

> capacity=8: misdecodes 8

> capacity=8: decode_failures 94

> capacity=16: misdecodes 6

> capacity=16: decode_failures 64

> capacity=32: misdecodes 9

> capacity=32: decode_failures 2

> slower: 3.9 s per simulated hour against 1.63 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.742 | 0.725 | 0.016 | - | - | 0.907 | 0.909 | 0.223 | 1.85x | 19.6/38.2/43.9% | 2.7/7.2% | 3 |
| 02-06 | 1 | 0.780 | 0.774 | 0.006 | - | - | 0.867 | 0.939 | 0.252 | 1.41x | 15.1/29.2/33.8% | 2.1/5.2% | 3 |
| 00-08 | 1 | 0.771 | 0.765 | 0.007 | - | - | 0.865 | 0.939 | 0.250 | 1.46x | 15.7/30.6/35.3% | 2.1/5.5% | 3 |

> catch-up-hours=: misdecodes 19

> catch-up-hours=02-06: decode_failures 46

> catch-up-hours=00-08: decode_failures 47

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.779 | 0.777 | 0.002 | - | - | 0.899 | 0.899 | 0.253 | 1.34x | 14.3/28.0/32.3% | 2.0/4.9% | 3 |
| 2 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 3 | 1 | 0.817 | 0.776 | 0.041 | - | - | 0.879 | 0.974 | 0.245 | 1.38x | 14.7/28.2/32.6% | 2.0/5.0% | 3 |
| 4 | 1 | 0.770 | 0.764 | 0.005 | - | - | 0.724 | 0.960 | 0.227 | 1.34x | 14.4/27.6/32.0% | 2.0/4.8% | 3 |

> hops-apart=2: decode_failures 2

> hops-apart=3: decode_failures 38

> hops-apart=4: decode_failures 30

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.779 | 0.777 | 0.002 | - | - | 0.899 | 0.899 | 0.253 | 1.34x | 14.3/28.0/32.3% | 2.0/4.9% | 3 |
| 2 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 3 | 1 | 0.817 | 0.776 | 0.041 | - | - | 0.879 | 0.974 | 0.245 | 1.38x | 14.7/28.2/32.6% | 2.0/5.0% | 3 |
| 4 | 1 | 0.770 | 0.764 | 0.005 | - | - | 0.724 | 0.960 | 0.227 | 1.34x | 14.4/27.6/32.0% | 2.0/4.8% | 3 |
| 5 | 1 | 0.794 | 0.775 | 0.019 | - | - | 0.715 | 0.964 | 0.223 | 1.36x | 14.5/27.7/32.1% | 2.0/4.8% | 3 |

> hops-apart=2: decode_failures 2

> hops-apart=3: decode_failures 38

> hops-apart=4: decode_failures 30

> hops-apart=5: decode_failures 27

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.785 | 0.773 | 0.012 | - | - | 0.946 | 0.950 | 0.234 | 1.37x | 14.7/28.5/33.2% | 2.0/5.1% | 3 |
| 30 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 120 | 1 | 0.792 | 0.780 | 0.012 | - | - | 0.947 | 0.949 | 0.246 | 1.35x | 14.5/28.0/32.6% | 1.9/5.0% | 3 |
| 600 | 1 | 0.779 | 0.767 | 0.012 | - | - | 0.937 | 0.939 | 0.258 | 1.37x | 14.6/28.3/32.8% | 1.9/5.1% | 3 |

> advert-jitter-s=1: decode_failures 3

> advert-jitter-s=30: decode_failures 2

> advert-jitter-s=120: decode_failures 3

> advert-jitter-s=600: decode_failures 7

> slower: 3.54 s per simulated hour against 1.77 over 36 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.785 | 0.773 | 0.012 | - | - | 0.946 | 0.950 | 0.234 | 1.37x | 14.7/28.5/33.2% | 2.0/5.1% | 3 |
| 30 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 120 | 1 | 0.792 | 0.780 | 0.012 | - | - | 0.947 | 0.949 | 0.246 | 1.35x | 14.5/28.0/32.6% | 1.9/5.0% | 3 |
| 600 | 1 | 0.779 | 0.767 | 0.012 | - | - | 0.937 | 0.939 | 0.258 | 1.37x | 14.6/28.3/32.8% | 1.9/5.1% | 3 |

> advert-jitter-s=1: decode_failures 3

> advert-jitter-s=30: decode_failures 2

> advert-jitter-s=120: decode_failures 3

> advert-jitter-s=600: decode_failures 7

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.790 | 0.775 | 0.015 | - | - | 0.508 | 0.748 | 0.233 | 1.37x | 14.6/28.1/32.6% | 2.0/4.9% | 3 |
| routers | 1 | 0.775 | 0.772 | 0.003 | - | - | 0.908 | 0.908 | 0.244 | 1.35x | 14.5/27.9/32.2% | 2.0/4.9% | 3 |
| alternate-routers | 1 | 0.779 | 0.777 | 0.002 | - | - | 0.911 | 0.911 | 0.216 | 1.36x | 14.6/28.3/32.7% | 2.0/4.9% | 3 |
| beside-router | 1 | 0.787 | 0.774 | 0.013 | - | - | 0.950 | 0.951 | 0.262 | 1.36x | 14.6/28.4/32.7% | 2.0/4.9% | 3 |
| random-clients | 1 | 0.790 | 0.775 | 0.015 | - | - | 0.942 | 0.968 | 0.233 | 1.38x | 14.8/28.0/32.5% | 2.0/4.9% | 3 |
| hops-apart | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> place=spread: decode_failures 19

> place=random-clients: decode_failures 33

> place=hops-apart: decode_failures 2

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.790 | 0.775 | 0.015 | - | - | 0.508 | 0.748 | 0.233 | 1.37x | 14.6/28.1/32.6% | 2.0/4.9% | 3 |
| routers | 1 | 0.775 | 0.772 | 0.003 | - | - | 0.908 | 0.908 | 0.244 | 1.35x | 14.5/27.9/32.2% | 2.0/4.9% | 3 |
| alternate-routers | 1 | 0.779 | 0.777 | 0.002 | - | - | 0.911 | 0.911 | 0.216 | 1.36x | 14.6/28.3/32.7% | 2.0/4.9% | 3 |
| beside-router | 1 | 0.787 | 0.774 | 0.013 | - | - | 0.950 | 0.951 | 0.262 | 1.36x | 14.6/28.4/32.7% | 2.0/4.9% | 3 |
| random-clients | 1 | 0.790 | 0.775 | 0.015 | - | - | 0.942 | 0.968 | 0.233 | 1.38x | 14.8/28.0/32.5% | 2.0/4.9% | 3 |
| hops-apart | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> place=spread: decode_failures 19

> place=random-clients: decode_failures 33

> place=hops-apart: decode_failures 2

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| broadcast | 1 | 0.834 | 0.763 | 0.071 | - | - | 0.910 | 0.943 | 0.402 | 1.52x | 16.2/31.4/36.0% | 2.2/5.5% | 3 |

> provide-transport=dm: decode_failures 2

> provide-transport=broadcast: decode_failures 25

> slower: 6.28 s per simulated hour against 1.79 over 36 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| heard | 1 | 0.785 | 0.775 | 0.010 | - | - | 0.940 | 0.945 | 0.264 | 1.36x | 14.6/28.1/32.6% | 2.0/5.0% | 3 |

> replay-ordering=tip: decode_failures 2

> replay-ordering=heard: misdecodes 4

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.834 | 0.763 | 0.071 | - | - | 0.910 | 0.943 | 0.402 | 1.52x | 16.2/31.4/36.0% | 2.2/5.5% | 3 |
| heard | 1 | 0.831 | 0.761 | 0.070 | - | - | 0.901 | 0.943 | 0.418 | 1.51x | 16.1/31.4/36.0% | 2.2/5.4% | 3 |

> replay-ordering=tip: decode_failures 25

> replay-ordering=heard: misdecodes 2

> replay-ordering=heard: decode_failures 49

> slower: 12.3 s per simulated hour against 1.78 over 36 prior run(s) - 6.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.782 | 0.772 | 0.010 | - | - | 0.925 | 0.941 | 0.250 | 1.35x | 14.6/28.1/32.6% | 2.0/5.0% | 3 |
| enum | 1 | 0.784 | 0.772 | 0.012 | - | - | 0.933 | 0.940 | 0.256 | 1.35x | 14.5/27.9/32.5% | 1.9/5.0% | 3 |
| hybrid | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> resolve=sketch: decode_failures 15

> resolve=hybrid: decode_failures 2

> slower: 3.73 s per simulated hour against 1.55 over 36 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.775 | 0.772 | 0.003 | - | - | 0.908 | 0.908 | 0.244 | 1.35x | 14.5/27.9/32.2% | 2.0/4.9% | 3 |
| 6 | 1 | 0.776 | 0.772 | 0.003 | - | - | 0.913 | 0.914 | 0.252 | 1.37x | 14.7/29.0/33.2% | 2.0/5.1% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.783 | 0.779 | 0.005 | - | - | 0.949 | 0.951 | 0.230 | 1.35x | 14.5/28.1/32.4% | 2.0/4.9% | 2 |
| 3 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 5 | 1 | 0.785 | 0.768 | 0.017 | - | - | 0.968 | 0.972 | 0.243 | 1.37x | 14.9/28.4/32.9% | 2.0/5.0% | 5 |
| 8 | 1 | 0.790 | 0.770 | 0.020 | - | - | 0.972 | 0.974 | 0.246 | 1.41x | 15.2/29.4/34.0% | 2.0/5.2% | 8 |

> servers=3: decode_failures 2

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.783 | 0.779 | 0.005 | - | - | 0.949 | 0.951 | 0.230 | 1.35x | 14.5/28.1/32.4% | 2.0/4.9% | 2 |
| 3 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 5 | 1 | 0.785 | 0.768 | 0.017 | - | - | 0.968 | 0.972 | 0.243 | 1.37x | 14.9/28.4/32.9% | 2.0/5.0% | 5 |
| 8 | 1 | 0.790 | 0.770 | 0.020 | - | - | 0.972 | 0.974 | 0.246 | 1.41x | 15.2/29.4/34.0% | 2.0/5.2% | 8 |

> servers=3: decode_failures 2

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| True | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |

> signed=False: decode_failures 2

> signed=True: decode_failures 2

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.788 | 0.777 | 0.011 | - | - | 0.935 | 0.944 | 0.257 | 1.27x | 13.6/26.4/30.7% | 1.8/4.7% | 3 |
| 1 | 1 | 0.789 | 0.779 | 0.010 | - | - | 0.934 | 0.948 | 0.258 | 1.28x | 13.8/26.5/30.7% | 1.9/4.7% | 3 |
| 2 | 1 | 0.783 | 0.772 | 0.011 | - | - | 0.928 | 0.935 | 0.239 | 1.29x | 13.9/26.8/31.1% | 1.9/4.7% | 3 |
| 4 | 1 | 0.791 | 0.781 | 0.010 | - | - | 0.944 | 0.951 | 0.266 | 1.28x | 13.7/26.5/30.9% | 1.8/4.7% | 3 |

> sr-retries=0: decode_failures 2

> sr-retries=1: decode_failures 3

> sr-retries=2: decode_failures 1

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.778 | 0.766 | 0.011 | - | - | 0.934 | 0.940 | 0.250 | 1.36x | 14.7/28.3/32.9% | 2.0/5.0% | 3 |
| 24 | 1 | 0.782 | 0.772 | 0.011 | - | - | 0.918 | 0.949 | 0.241 | 1.38x | 14.8/28.4/33.1% | 2.0/5.0% | 3 |
| 32 | 1 | 0.781 | 0.769 | 0.011 | - | - | 0.941 | 0.943 | 0.250 | 1.36x | 14.5/28.3/32.8% | 2.0/5.0% | 3 |
| 64 | 1 | 0.783 | 0.772 | 0.011 | - | - | 0.938 | 0.946 | 0.272 | 1.37x | 14.7/28.2/32.8% | 2.0/5.0% | 3 |

> short-id-bits=16: decode_failures 1

> short-id-bits=24: decode_failures 54

> short-id-bits=32: decode_failures 2

> short-id-bits=64: decode_failures 16

> slower: 6.34 s per simulated hour against 1.7 over 36 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.787 | 0.774 | 0.013 | - | - | 0.950 | 0.952 | 0.272 | 1.45x | 15.5/29.7/34.4% | 2.1/5.3% | 3 |
| 16 | 1 | 0.783 | 0.772 | 0.011 | - | - | 0.927 | 0.946 | 0.265 | 1.39x | 15.0/28.8/33.4% | 2.0/5.1% | 3 |
| 32 | 1 | 0.781 | 0.769 | 0.012 | - | - | 0.923 | 0.940 | 0.267 | 1.35x | 14.4/27.8/32.3% | 2.0/5.0% | 3 |

> window-size=8: misdecodes 122

> window-size=16: misdecodes 49

> window-size=32: misdecodes 9

> window-size=32: decode_failures 2

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.956 | 0.954 | 0.001 | - | - | 0.998 | 0.998 | 0.780 | 1.96x | 21.7/30.5/34.1% | 1.2/5.2% | 3 |
| True | 1 | 0.764 | 0.752 | 0.012 | - | - | 0.923 | 0.940 | 0.499 | 5.56x | 56.6/70.9/74.3% | 3.8/12.5% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: queue drops 10.8% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 102

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.594 | 0.586 | 0.008 | - | - | 0.884 | 0.885 | 0.141 | 4.60x | 17.3/28.6/38.7% | 1.5/6.0% | 3 |
| truesize | 1 | 0.624 | 0.617 | 0.007 | - | - | 0.910 | 0.911 | 0.138 | 3.60x | 13.5/22.9/32.0% | 1.1/5.1% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.958 | 0.956 | 0.001 | - | - | 0.999 | 0.999 | 0.774 | 1.85x | 20.2/28.1/31.6% | 1.1/4.7% | 3 |
| adaptive | 1 | 0.956 | 0.954 | 0.001 | - | - | 0.998 | 0.998 | 0.780 | 1.96x | 21.7/30.5/34.1% | 1.2/5.2% | 3 |

> congestion-mode=adaptive: misdecodes 1

