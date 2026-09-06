# Sweep blocks-2026-09-06-6155294

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 6155294 · seeds 6155294
- **blocks** 87 run
- **compute** 15.3 h of simulator time across every cell
- **generated** 2026-09-06T08:37:46+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>238 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 3
- AD-amplify-worst: amplify-worst=0.0: decode_failures 3
- AD-amplify-worst: amplify-worst=0.1: decode_failures 7
- AD-amplify-worst: amplify-worst=0.3: decode_failures 4
- AD-amplify-worst: slower: 3.88 s per simulated hour against 1.79 over 16 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=degree: decode_failures 14
- AD-badrouters: role-placement=inverse: decode_failures 2
- AD-badrouters: role-placement=random: decode_failures 13
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 14
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 14
- AD-nomute: role-mix=no-mute: decode_failures 18
- AD-nomute: slower: 5.42 s per simulated hour against 2.33 over 16 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=uniform: decode_failures 14
- DB-hotstore: max-num-nodes=10: decode_failures 15
- DB-hotstore: max-num-nodes=100: decode_failures 16
- DB-hotstore: max-num-nodes=120: decode_failures 16
- DB-hotstore: max-num-nodes=250: decode_failures 16
- DB-hotstore: slower: 6.81 s per simulated hour against 2.81 over 16 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 46
- DB-hotstore-stress: max-num-nodes=120: decode_failures 44
- DB-hotstore-stress: max-num-nodes=250: decode_failures 64
- DB-platform: platform-mix=uniform: decode_failures 16
- DB-platform: platform-mix=baymesh-2026-08: decode_failures 16
- DB-platform: platform-mix=constrained: decode_failures 16
- DB-platform: slower: 6.92 s per simulated hour against 2.67 over 16 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: decode_failures 79
- DB-warm: warm-num-nodes=25: decode_failures 79
- DB-warm: warm-num-nodes=100: decode_failures 79
- DB-warm: warm-num-nodes=2000: decode_failures 79
- DG-burst: burst-loss=0.0: decode_failures 3
- DG-burst: burst-loss=0.1: decode_failures 18
- DG-burst: burst-loss=0.2: decode_failures 23
- DG-burst: burst-loss=0.3: decode_failures 12
- DG-loss: extra-loss=0.0: decode_failures 3
- DG-loss: extra-loss=0.1: decode_failures 16
- DG-loss: extra-loss=0.2: decode_failures 20
- DG-loss: extra-loss=0.3: decode_failures 15
- DG-loss: slower: 5.32 s per simulated hour against 2.22 over 16 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 3
- DG-outage: burst-loss=0.1: decode_failures 25
- DG-outage: burst-loss=0.2: decode_failures 15
- DG-outage: burst-loss=0.3: decode_failures 18
- DM-mode: dm-mode=flood-only: decode_failures 21
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 15
- DM-mode: dm-mode=m4-early-flood: decode_failures 23
- DM-mode: slower: 7.63 s per simulated hour against 2.88 over 16 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 3
- FW-mixed-26: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.5: decode_failures 3
- FW-signing-cost: profile-flag=signing=true: decode_failures 3
- FW-versions: profile=2.4: decode_failures 37
- FW-versions: profile=2.5: decode_failures 1
- FW-versions: profile=2.6: decode_failures 1
- FW-versions: profile=2.7: decode_failures 4
- FW-versions: profile=2.8: decode_failures 3
- FW-versions: slower: 4.66 s per simulated hour against 1.65 over 16 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 19
- LD-chatty: broadcast-interval-s=900: decode_failures 3
- LD-chatty: broadcast-interval-s=300: decode_failures 16
- LD-diurnal: diurnal=flat: decode_failures 1
- LD-diurnal: diurnal=sinusoid: decode_failures 8
- LD-diurnal: diurnal=commuter: decode_failures 3
- LD-interval: broadcast-interval-s=900: decode_failures 3
- LD-interval: broadcast-interval-s=10800: decode_failures 4
- LD-interval: broadcast-interval-s=43200: decode_failures 1
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 3
- LD-traceroute: traceroute-per-hour=0.25: decode_failures 3
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 1
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 20
- LD-traceroute: slower: 4.33 s per simulated hour against 2.14 over 16 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 79
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 105
- MS-density: nodes=40: decode_failures 9
- MS-density: nodes=60: decode_failures 3
- MS-hopscale: nodes=60: decode_failures 3
- MS-hopscale: nodes=120: decode_failures 51
- MS-hopscale: nodes=250: decode_failures 88
- MS-hopscale: nodes=500: decode_failures 127
- MS-oversubscribed: nodes=120: decode_failures 22
- MS-oversubscribed: nodes=250: decode_failures 44
- MS-oversubscribed: nodes=500: decode_failures 89
- MS-roles-fav: role-mix=legacy-default: decode_failures 1
- MS-roles: role-mix=legacy-default: decode_failures 5
- MS-roles: role-mix=baymesh-2026-08: decode_failures 14
- MS-roles: slower: 4.53 s per simulated hour against 1.8 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-router-late: router-late-fraction=0.0: decode_failures 3
- MS-router-late: router-late-fraction=0.05: decode_failures 3
- MS-siting: siting-mix=uniform: decode_failures 3
- MS-siting: siting-mix=local-typical: decode_failures 3
- MS-siting: siting-mix=event: decode_failures 3
- MS-size: nodes=40: decode_failures 1
- MS-size: nodes=60: decode_failures 3
- MS-size: nodes=90: decode_failures 3
- MS-size: nodes=120: decode_failures 51
- MS-size: nodes=150: decode_failures 24
- MS-size: slower: 8.32 s per simulated hour against 3.27 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.0: decode_failures 3
- MS-stretch: stretch=1.25: decode_failures 29
- MS-stretch: stretch=1.5: decode_failures 12
- MS-topology: topology=uniform: decode_failures 3
- MS-topology: topology=corridor: decode_failures 19
- PR-crladder: coding-rate-ladder=False: decode_failures 15
- PR-crladder: coding-rate-ladder=True: decode_failures 25
- PR-crladder: slower: 7.79 s per simulated hour against 2.77 over 16 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 25
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 28
- PR-dmmode-cr: slower: 8.67 s per simulated hour against 2.52 over 16 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 3
- PR-repeats: extra-repeats=False: decode_failures 3
- PR-repeats: extra-repeats=True: decode_failures 16
- PR-repeats: slower: 5.01 s per simulated hour against 1.75 over 16 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 10
- RF-duct: duct-per-hour=0.0: decode_failures 3
- RF-duct: duct-per-hour=0.25: decode_failures 4
- RF-duct: duct-per-hour=1.0: decode_failures 1
- RF-eu-presets: preset=LONG_FAST: decode_failures 3
- RF-noise: noise-profile=none: decode_failures 3
- RF-noise: noise-profile=temporal: decode_failures 13
- RF-noise: noise-profile=transient: decode_failures 2
- RF-noise: noise-profile=periodic: decode_failures 14
- RF-preset: preset=LONG_FAST: decode_failures 3
- RF-preset-turbo: preset=LONG_FAST: decode_failures 3
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 20
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 14
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 6
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 12
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 32
- RF-stretch-duct: slower: 7.04 s per simulated hour against 2.43 over 16 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=30: decode_failures 3
- RF-txpower: tx-power=22: decode_failures 8
- RT-favourites: favourite-routers=False: decode_failures 47
- RT-favourites: favourite-routers=True: decode_failures 10
- RT-favourites: slower: 9.53 s per simulated hour against 1.71 over 16 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-hopassign: hop-assign=centrality: decode_failures 3
- RT-hoplimit: hop-limit=3: decode_failures 14
- RT-hopspread: hop-limit=3: decode_failures 14
- RT-hopspread: hop-limit=5: decode_failures 28
- RT-hopspread: slower: 4.5 s per simulated hour against 2.03 over 16 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 3
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 14
- RT-spread: hop-spread=True: decode_failures 3
- RT-spread: slower: 4.34 s per simulated hour against 2.11 over 16 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SC-signing: signature-policy=COMPATIBLE: decode_failures 3
- SC-signing: signature-policy=BALANCED: decode_failures 3
- SC-signing: signature-policy=STRICT: decode_failures 11
- SF-advert-transport: advert-transport=broadcast: decode_failures 3
- SF-bucket-mode: bucket-mode=global: misdecodes 6
- SF-bucket-mode: bucket-mode=local: decode_failures 3
- SF-bucket-mode: bucket-mode=time: misdecodes 6
- SF-bucket-mode: bucket-mode=window: misdecodes 9
- SF-bucket-mode: bucket-mode=window: decode_failures 4
- SF-bucket-time: time-bucket-s=600: misdecodes 45
- SF-bucket-time: time-bucket-s=1800: misdecodes 6
- SF-bucket-time: time-bucket-s=3600: misdecodes 2
- SF-bucket-time: time-bucket-s=3600: decode_failures 6
- SF-cadence: trigger=bucket: decode_failures 3
- SF-cadence: trigger=interval: misdecodes 7
- SF-cadence: trigger=interval: decode_failures 12
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 35
- SF-cadence: trigger=bucket+interval: misdecodes 6
- SF-cadence: trigger=bucket+interval: decode_failures 1
- SF-cadence: slower: 8.25 s per simulated hour against 3.26 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 75
- SF-capacity-local: capacity=8: decode_failures 59
- SF-capacity-local: capacity=16: decode_failures 58
- SF-capacity-local: capacity=32: decode_failures 3
- SF-capacity: capacity=4: decode_failures 75
- SF-capacity: capacity=8: decode_failures 59
- SF-capacity: capacity=16: decode_failures 58
- SF-capacity: capacity=32: decode_failures 3
- SF-capacity-window: capacity=8: decode_failures 103
- SF-capacity-window: capacity=16: misdecodes 1
- SF-capacity-window: capacity=16: decode_failures 84
- SF-capacity-window: capacity=32: misdecodes 9
- SF-capacity-window: capacity=32: decode_failures 4
- SF-capacity-window: slower: 4.43 s per simulated hour against 1.67 over 16 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-catchup: catch-up-hours=: misdecodes 6
- SF-catchup: catch-up-hours=: decode_failures 1
- SF-catchup: catch-up-hours=02-06: decode_failures 40
- SF-catchup: catch-up-hours=00-08: decode_failures 39
- SF-hops-flat: hops-apart=2: decode_failures 3
- SF-hops-flat: hops-apart=4: decode_failures 21
- SF-hops-spread: hops-apart=2: decode_failures 3
- SF-hops-spread: hops-apart=4: decode_failures 21
- SF-hops-spread: hops-apart=5: decode_failures 17
- SF-jitter-global: advert-jitter-s=1: decode_failures 2
- SF-jitter-global: advert-jitter-s=30: decode_failures 3
- SF-jitter-global: advert-jitter-s=120: decode_failures 1
- SF-jitter-global: advert-jitter-s=600: decode_failures 39
- SF-jitter-global: slower: 5.34 s per simulated hour against 1.76 over 16 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 2
- SF-jitter-local: advert-jitter-s=30: decode_failures 3
- SF-jitter-local: advert-jitter-s=120: decode_failures 1
- SF-jitter-local: advert-jitter-s=600: decode_failures 39
- SF-jitter-local: slower: 4.51 s per simulated hour against 1.78 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 17
- SF-place-flat: place=hops-apart: decode_failures 3
- SF-place-spread: place=spread: decode_failures 17
- SF-place-spread: place=hops-apart: decode_failures 3
- SF-provide-transport: provide-transport=dm: decode_failures 3
- SF-provide-transport: provide-transport=broadcast: decode_failures 7
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 7
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 11
- SF-replay-order-broadcast: slower: 5.18 s per simulated hour against 1.73 over 16 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 3
- SF-replay-order: replay-ordering=heard: misdecodes 4
- SF-replay-order: replay-ordering=heard: decode_failures 1
- SF-resolve: resolve=sketch: decode_failures 18
- SF-resolve: resolve=hybrid: decode_failures 3
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=2: decode_failures 15
- SF-servers-flat: servers=3: decode_failures 3
- SF-servers-flat: servers=5: decode_failures 1
- SF-servers-flat: slower: 5.3 s per simulated hour against 2.63 over 16 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=2: decode_failures 15
- SF-servers-spread: servers=3: decode_failures 3
- SF-servers-spread: servers=5: decode_failures 1
- SF-signed: signed=False: decode_failures 3
- SF-signed: signed=True: decode_failures 3
- SF-sr-retries: sr-retries=0: decode_failures 4
- SF-sr-retries: sr-retries=1: decode_failures 1
- SF-sr-retries: sr-retries=2: decode_failures 4
- SF-width: short-id-bits=16: decode_failures 5
- SF-width: short-id-bits=24: decode_failures 6
- SF-width: short-id-bits=32: decode_failures 3
- SF-width: short-id-bits=64: decode_failures 12
- SF-width: slower: 4.09 s per simulated hour against 1.79 over 16 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 54
- SF-window-size: window-size=16: misdecodes 13
- SF-window-size: window-size=32: misdecodes 9
- SF-window-size: window-size=32: decode_failures 4
- TH-congestion-input: congestion-input=hotstore: decode_failures 44
- TH-congestion-input: congestion-input=truesize: decode_failures 29
- TH-congestion-input: slower: 25.1 s per simulated hour against 11.2 over 16 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: decode_failures 57

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RT-favourites` | 9.53 | 1.71 | 5.56x | 16 |
| `PR-dmmode-cr` | 8.67 | 2.52 | 3.45x | 16 |
| `SF-jitter-global` | 5.34 | 1.76 | 3.04x | 16 |
| `SF-replay-order-broadcast` | 5.18 | 1.73 | 3.00x | 16 |
| `RF-stretch-duct` | 7.04 | 2.43 | 2.89x | 16 |
| `PR-repeats` | 5.01 | 1.75 | 2.86x | 16 |
| `FW-versions` | 4.66 | 1.65 | 2.82x | 16 |
| `PR-crladder` | 7.79 | 2.77 | 2.81x | 16 |
| `SF-capacity-window` | 4.43 | 1.67 | 2.65x | 16 |
| `DM-mode` | 7.63 | 2.88 | 2.65x | 16 |
| `DB-platform` | 6.92 | 2.67 | 2.59x | 16 |
| `MS-size` | 8.32 | 3.27 | 2.54x | 16 |
| `SF-cadence` | 8.25 | 3.26 | 2.53x | 16 |
| `SF-jitter-local` | 4.51 | 1.78 | 2.53x | 16 |
| `MS-roles` | 4.53 | 1.8 | 2.52x | 16 |
| `DB-hotstore` | 6.81 | 2.81 | 2.42x | 16 |
| `DG-loss` | 5.32 | 2.22 | 2.39x | 16 |
| `AD-nomute` | 5.42 | 2.33 | 2.32x | 16 |
| `SF-width` | 4.09 | 1.79 | 2.28x | 16 |
| `TH-congestion-input` | 25.1 | 11.2 | 2.24x | 16 |
| `RT-hopspread` | 4.5 | 2.03 | 2.22x | 16 |
| `AD-amplify-worst` | 3.88 | 1.79 | 2.17x | 16 |
| `RT-spread` | 4.34 | 2.11 | 2.06x | 16 |
| `LD-traceroute` | 4.33 | 2.14 | 2.02x | 16 |
| `SF-servers-flat` | 5.3 | 2.63 | 2.02x | 16 |
| `SF-sr-retries` | 3.3 | 1.68 | 1.96x | 16 |
| `MS-stretch` | 3.88 | 1.99 | 1.95x | 16 |
| `AD-badrouters` | 4.32 | 2.26 | 1.91x | 16 |
| `AD-siting` | 2.49 | 1.32 | 1.88x | 16 |
| `SF-servers-allrouters` | 3.52 | 1.89 | 1.86x | 16 |
| `SF-resolve` | 2.84 | 1.53 | 1.85x | 16 |
| `RF-pulse` | 3.04 | 1.67 | 1.82x | 16 |
| `MS-oversubscribed` | 31.3 | 17.4 | 1.80x | 16 |
| `SF-servers-spread` | 4.16 | 2.32 | 1.79x | 16 |
| `MS-topology` | 3.31 | 1.87 | 1.77x | 16 |
| `SC-signing` | 3.51 | 1.99 | 1.76x | 16 |
| `SF-provide-transport` | 3.22 | 1.93 | 1.67x | 16 |
| `SF-bucket-time` | 2.77 | 1.67 | 1.66x | 16 |
| `AD-flooding` | 4.24 | 2.59 | 1.64x | 16 |
| `LD-interval` | 2.29 | 1.41 | 1.63x | 16 |
| `LD-diurnal` | 2.56 | 1.61 | 1.59x | 16 |
| `SF-capacity-local` | 2.79 | 1.79 | 1.56x | 16 |
| `SF-capacity` | 2.68 | 1.75 | 1.53x | 16 |
| `RF-duct` | 2.83 | 1.84 | 1.53x | 16 |
| `RF-preset` | 1.69 | 2.97 | 0.57x | 16 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.895 | 0.895 | 0.696 → 0.708 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.797 | 0.797 | 0.670 → 0.708 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.051 → 0.820 | 0.770 | 0.027 → 0.690 | 40x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.055 → 0.797 | 0.742 | 0.035 → 0.690 | 55x sr_bytes | down | 4 |
| `MS-stretch` | stretch | **held** | 0.078 → 0.797 | 0.719 | 0.055 → 0.690 | 33x sr_bytes | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.248 → 0.965 | 0.717 | 0.243 → 0.964 | 3.4x sr_airtime | up | 4 |
| `RF-bw500` | preset | **held** | 0.099 → 0.769 | 0.670 | 0.065 → 0.552 | 13x sr_bytes | up | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.058 → 0.701 | 0.643 | 0.064 → 0.635 | 2.5e+02x sr_airtime | down | 4 |
| `RF-preset` | preset | **held** | 0.229 → 0.834 | 0.605 | 0.116 → 0.715 | 5.5x sr_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.117 → 0.704 | 0.587 | 0.116 → 0.690 | 5.5x sr_bytes | up | 4 |
| `AD-siting` | siting-mix | **held** | 0.214 → 0.796 | 0.583 | 0.062 → 0.615 | 7.3x sr_bytes | down | 3 |
| `MS-topology` | topology | **text** | 0.387 → 0.936 | 0.549 | 0.371 → 0.934 | 3.4x sr_bytes | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.179 → 0.704 | 0.526 | 0.175 → 0.690 | 6.8x bytes_on_air | down | 4 |
| `MS-density` | nodes | **held** | 0.554 → 0.997 | 0.443 | 0.515 → 0.918 | 7.5x advert_bytes | up | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.500 → 0.935 | 0.435 | 0.511 → 0.853 | 13x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.429 → 0.844 | 0.416 | 0.409 → 0.745 | 14x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **held** | 0.402 → 0.797 | 0.396 | 0.357 → 0.690 | 2.1x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.320 → 0.698 | 0.379 | 0.177 → 0.450 | 4.3x bytes_on_air | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.145 → 0.511 | 0.365 | 0.144 → 0.506 | 4.1x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **held** | 0.432 → 0.797 | 0.365 | 0.363 → 0.690 | 1.9x advert_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.582 → 0.930 | 0.348 | 0.690 → 0.699 | 2.3x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.582 → 0.930 | 0.348 | 0.690 → 0.699 | 2.3x sr_bytes | up | 6 |
| `RT-hoplimit` | hop-limit | **text** | 0.538 → 0.874 | 0.336 | 0.518 → 0.870 | 1.7x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.538 → 0.821 | 0.283 | 0.518 → 0.812 | 1.5x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.538 → 0.811 | 0.273 | 0.518 → 0.696 | 1.9x sr_airtime | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.367 → 0.624 | 0.257 | 0.217 → 0.318 | 5.3x sr_airtime | up | 3 |
| `DG-loss` | extra-loss | **held** | 0.542 → 0.797 | 0.255 | 0.499 → 0.690 | 1.6x sr_airtime | down | 4 |
| `MS-size` | nodes | **text** | 0.463 → 0.704 | 0.241 | 0.451 → 0.690 | 3.7x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.675 → 0.892 | 0.217 | 0.664 → 0.888 | 3.4x sr_airtime | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.704 → 0.893 | 0.189 | 0.690 → 0.886 | 1.5x sr_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.623 → 0.808 | 0.184 | 0.695 → 0.698 | 15x sr_bytes | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.616 → 0.797 | 0.181 | 0.690 → 0.700 | 41x sr_airtime | down | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.715 → 0.895 | 0.180 | 0.690 → 0.700 | 1.3x sr_airtime | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.715 → 0.895 | 0.180 | 0.684 → 0.700 | 1.3x sr_airtime | down | 5 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.704 → 0.879 | 0.175 | 0.690 → 0.858 | 1.5x sr_airtime | up | 3 |
| `RT-spread` | hop-spread | **held** | 0.623 → 0.797 | 0.174 | 0.518 → 0.690 | 1.3x sr_airtime | up | 2 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.797 → 0.962 | 0.165 | 0.690 → 0.790 | 2.2x bytes_on_air | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.704 → 0.868 | 0.164 | 0.690 → 0.845 | 1.5x bytes_on_air | up | 3 |
| `FW-versions` | profile | **held** | 0.797 → 0.959 | 0.162 | 0.690 → 0.791 | 3.4x bytes_on_air | down | 5 |
| `FW-mixed` | legacy-fraction | **held** | 0.797 → 0.958 | 0.160 | 0.690 → 0.782 | 2.1x bytes_on_air | up | 4 |
| `FW-firmware` | profile | **held** | 0.797 → 0.953 | 0.156 | 0.690 → 0.787 | 3.3x bytes_on_air | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.765 → 0.914 | 0.149 | 0.687 → 0.701 | 6.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.765 → 0.914 | 0.149 | 0.687 → 0.701 | 6.4x sr_bytes | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.676 → 0.821 | 0.145 | 0.622 → 0.748 | 2.4x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **held** | 0.683 → 0.821 | 0.137 | 0.624 → 0.748 | 2.4x sr_airtime | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.664 → 0.798 | 0.135 | 0.648 → 0.789 | 6.3x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.631 → 0.763 | 0.132 | 0.615 → 0.755 | 2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.631 → 0.763 | 0.132 | 0.615 → 0.755 | 2x bytes_on_air | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.574 → 0.704 | 0.130 | 0.574 → 0.690 | 1.3x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **held** | 0.690 → 0.796 | 0.106 | 0.599 → 0.615 | 1.2x sr_airtime | down | 3 |
| `MS-roles` | role-mix | **text** | 0.631 → 0.729 | 0.098 | 0.615 → 0.715 | 1.2x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.707 → 0.797 | 0.091 | 0.660 → 0.694 | 16x advert_bytes | down | 4 |
| `MS-roles-fav` | role-mix | **text** | 0.686 → 0.763 | 0.077 | 0.671 → 0.753 | 1.2x sr_bytes | down | 2 |
| `FW-signing-cost` | profile-flag | **held** | 0.797 → 0.874 | 0.076 | 0.690 → 0.768 | 3.1x bytes_on_air | down | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.797 → 0.863 | 0.066 | 0.690 → 0.721 | 1.4x sr_bytes | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.804 → 0.869 | 0.065 | 0.604 → 0.655 | 1.3x sr_airtime | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.620 → 0.681 | 0.061 | 0.317 → 0.348 | 2x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.749 → 0.808 | 0.059 | 0.647 → 0.690 | 1.6x sr_airtime | down | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.726 → 0.775 | 0.048 | 0.660 → 0.700 | 8.9x advert_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.759 → 0.804 | 0.046 | 0.690 → 0.697 | 5.6x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.776 → 0.820 | 0.043 | 0.678 → 0.699 | 2.9x advert_bytes | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.704 → 0.747 | 0.042 | 0.690 → 0.734 | 1.2x sr_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **held** | 0.756 → 0.797 | 0.041 | 0.674 → 0.690 | 4x sr_airtime | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.789 → 0.824 | 0.035 | 0.693 → 0.712 | 1.2x sr_airtime | up | 4 |
| `DM-mode` | dm-mode | **held** | 0.668 → 0.703 | 0.035 | 0.660 → 0.671 | 1.3x sr_airtime | down | 3 |
| `SF-capacity` | capacity | **held** | 0.775 → 0.810 | 0.035 | 0.687 → 0.696 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.775 → 0.810 | 0.035 | 0.687 → 0.696 | 5.4x advert_bytes | up | 5 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.673 → 0.707 | 0.033 | 0.657 → 0.670 | 1.4x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.673 → 0.703 | 0.030 | 0.657 → 0.668 | 1.2x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.797 → 0.824 | 0.027 | 0.689 → 0.690 | 2.1x advert_bytes | up | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.728 → 0.754 | 0.026 | 0.715 → 0.743 | 1.3x sr_bytes | up | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.704 → 0.725 | 0.021 | 0.690 → 0.712 | 1.2x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.788 → 0.808 | 0.019 | 0.685 → 0.698 | 3.1x advert_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.789 → 0.808 | 0.019 | 0.685 → 0.694 | 4.9x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.875 → 0.892 | 0.017 | 0.870 → 0.888 | 1.2x bytes_on_air | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.797 → 0.814 | 0.017 | 0.688 → 0.698 | 1.4x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.797 → 0.814 | 0.017 | 0.688 → 0.698 | 1.4x sr_bytes | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.917 → 0.933 | 0.015 | 0.689 → 0.696 | 2.1x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.704 → 0.717 | 0.013 | 0.690 → 0.705 | 1x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.796 → 0.808 | 0.012 | 0.688 → 0.698 | 4.2x advert_bytes | up | 3 |
| `AD-worst` | role-placement | **held** | 0.920 → 0.930 | 0.010 | 0.762 → 0.767 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.742 → 0.745 | 0.004 | 0.674 → 0.677 | 1x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.701 → 0.704 | 0.003 | 0.688 → 0.690 | 1x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.892 → 0.895 | 0.003 | 0.888 → 0.890 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.984 → 0.987 | 0.003 | 0.888 → 0.890 | 1x bytes_on_air | up | 2 |

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
| none | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| sprinkled | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.947 | 0.951 | 0.483 | 1.45x | 15.3/18.9/22.1% | 2.2/5.1% | 3 |
| arms-race | 1 | 0.893 | 0.886 | 0.007 | - | - | 0.962 | 0.963 | 0.733 | 1.29x | 16.5/21.7/26.6% | 2.0/5.5% | 3 |

> amplifier-mix=none: decode_failures 3

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.776 | 0.755 | 0.021 | - | - | 0.886 | 0.893 | 0.457 | 1.36x | 15.8/20.5/21.8% | 2.1/4.8% | 3 |
| 0.3 | 1 | 0.879 | 0.858 | 0.021 | - | - | 0.956 | 0.962 | 0.478 | 1.21x | 18.0/23.9/26.5% | 1.8/4.3% | 3 |

> amplify-worst=0.0: decode_failures 3

> amplify-worst=0.1: decode_failures 7

> amplify-worst=0.3: decode_failures 4

> slower: 3.88 s per simulated hour against 1.79 over 16 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.631 | 0.615 | 0.016 | - | - | 0.796 | 0.824 | 0.027 | 1.18x | 11.6/19.2/21.1% | 2.0/4.6% | 3 |
| inverse | 1 | 0.627 | 0.612 | 0.015 | - | - | 0.760 | 0.766 | 0.041 | 1.12x | 11.2/15.3/19.8% | 2.0/3.6% | 3 |
| random | 1 | 0.611 | 0.599 | 0.012 | - | - | 0.690 | 0.795 | 0.000 | 1.16x | 11.7/17.0/21.4% | 2.0/4.9% | 3 |

> role-placement=degree: decode_failures 14

> role-placement=inverse: decode_failures 2

> role-placement=random: decode_failures 13

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.631 | 0.615 | 0.016 | - | - | 0.796 | 0.824 | 0.027 | 1.18x | 11.6/19.2/21.1% | 2.0/4.6% | 3 |
| all-routers | 1 | 0.763 | 0.755 | 0.007 | - | - | 0.884 | 0.887 | 0.472 | 2.40x | 21.4/30.3/32.2% | 4.0/5.0% | 3 |

> role-mix=baymesh-2026-08: decode_failures 14

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.631 | 0.615 | 0.016 | - | - | 0.796 | 0.824 | 0.027 | 1.18x | 11.6/19.2/21.1% | 2.0/4.6% | 3 |
| no-mute | 1 | 0.712 | 0.697 | 0.015 | - | - | 0.830 | 0.847 | 0.303 | 1.42x | 13.8/18.6/20.5% | 2.2/4.6% | 3 |
| all-routers | 1 | 0.763 | 0.755 | 0.007 | - | - | 0.884 | 0.887 | 0.472 | 2.40x | 21.4/30.3/32.2% | 4.0/5.0% | 3 |

> role-mix=baymesh-2026-08: decode_failures 14

> role-mix=no-mute: decode_failures 18

> slower: 5.42 s per simulated hour against 2.33 over 16 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.631 | 0.615 | 0.016 | - | - | 0.796 | 0.824 | 0.027 | 1.18x | 11.6/19.2/21.1% | 2.0/4.6% | 3 |
| local-typical | 1 | 0.468 | 0.461 | 0.007 | - | - | 0.700 | 0.703 | 0.000 | 1.28x | 10.4/21.1/31.4% | 2.3/5.6% | 3 |
| basement-heavy | 1 | 0.064 | 0.062 | 0.002 | - | - | 0.214 | 0.253 | 0.000 | 0.51x | 0.2/7.7/9.9% | 0.2/2.9% | 3 |

> siting-mix=uniform: decode_failures 14

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.777 | 0.767 | 0.010 | - | - | 0.920 | 0.921 | 0.143 | 2.39x | 16.1/26.8/34.3% | 2.0/5.5% | 3 |
| inverse | 1 | 0.779 | 0.762 | 0.016 | - | - | 0.930 | 0.932 | 0.196 | 2.31x | 15.2/22.9/29.4% | 1.9/3.3% | 3 |

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.708 | 0.708 | 0.000 | - | - | 0 | 0.000 | 0.326 | 1.36x | 12.7/18.9/21.5% | 2.1/4.8% | 3 |
| sr | 1 | 0.732 | 0.696 | 0.036 | - | - | 0.895 | 0.899 | 0.354 | 1.44x | 13.2/19.9/22.5% | 2.2/5.0% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.634 | 0.624 | 0.010 | - | - | 0.683 | 0.719 | 0.343 | 3.02x | 28.8/42.1/45.3% | 4.6/9.2% | 3 |
| 100 | 1 | 0.757 | 0.748 | 0.009 | - | - | 0.821 | 0.840 | 0.412 | 1.69x | 16.1/23.5/25.4% | 2.6/5.0% | 3 |
| 120 | 1 | 0.757 | 0.748 | 0.009 | - | - | 0.821 | 0.840 | 0.412 | 1.69x | 16.1/23.5/25.4% | 2.6/5.0% | 3 |
| 250 | 1 | 0.757 | 0.748 | 0.009 | - | - | 0.821 | 0.840 | 0.412 | 1.69x | 16.1/23.5/25.4% | 2.6/5.0% | 3 |

> max-num-nodes=10: decode_failures 15

> max-num-nodes=100: decode_failures 16

> max-num-nodes=120: decode_failures 16

> max-num-nodes=250: decode_failures 16

> slower: 6.81 s per simulated hour against 2.81 over 16 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.221 | 0.217 | 0.004 | - | - | 0.367 | 0.465 | 0.031 | 10.46x | 27.3/43.2/72.4% | 3.7/9.7% | 3 |
| 120 | 1 | 0.327 | 0.317 | 0.010 | - | - | 0.620 | 0.649 | 0.045 | 4.86x | 12.3/21.4/42.5% | 1.7/5.2% | 3 |
| 250 | 1 | 0.329 | 0.318 | 0.011 | - | - | 0.624 | 0.649 | 0.046 | 4.79x | 12.0/21.2/41.6% | 1.6/5.3% | 3 |

> max-num-nodes=10: decode_failures 46

> max-num-nodes=120: decode_failures 44

> max-num-nodes=250: decode_failures 64

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.757 | 0.748 | 0.009 | - | - | 0.821 | 0.840 | 0.412 | 1.69x | 16.1/23.5/25.4% | 2.6/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.757 | 0.748 | 0.009 | - | - | 0.821 | 0.840 | 0.412 | 1.69x | 16.1/23.5/25.4% | 2.6/5.0% | 3 |
| constrained | 1 | 0.632 | 0.622 | 0.010 | - | - | 0.676 | 0.713 | 0.335 | 3.02x | 28.8/42.0/45.3% | 4.6/9.2% | 3 |

> platform-mix=uniform: decode_failures 16

> platform-mix=baymesh-2026-08: decode_failures 16

> platform-mix=constrained: decode_failures 16

> slower: 6.92 s per simulated hour against 2.67 over 16 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.667 | 0.655 | 0.013 | - | - | 0.869 | 0.880 | 0.452 | 5.78x | 48.7/62.8/68.9% | 4.1/12.1% | 3 |
| 25 | 1 | 0.667 | 0.655 | 0.013 | - | - | 0.869 | 0.880 | 0.452 | 5.78x | 48.7/62.8/68.9% | 4.1/12.1% | 3 |
| 100 | 1 | 0.667 | 0.655 | 0.013 | - | - | 0.869 | 0.880 | 0.452 | 5.78x | 48.7/62.8/68.9% | 4.1/12.1% | 3 |
| 2000 | 1 | 0.667 | 0.655 | 0.013 | - | - | 0.869 | 0.880 | 0.452 | 5.78x | 48.7/62.8/68.9% | 4.1/12.1% | 3 |

> warm-num-nodes=0: decode_failures 79

> warm-num-nodes=25: decode_failures 79

> warm-num-nodes=100: decode_failures 79

> warm-num-nodes=2000: decode_failures 79

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.600 | 0.583 | 0.017 | - | - | 0.711 | 0.741 | 0.297 | 1.29x | 12.1/18.2/20.5% | 2.0/4.4% | 3 |
| 0.2 | 1 | 0.490 | 0.473 | 0.017 | - | - | 0.582 | 0.659 | 0.210 | 1.15x | 11.1/16.8/18.8% | 1.7/3.9% | 3 |
| 0.3 | 1 | 0.367 | 0.357 | 0.010 | - | - | 0.402 | 0.542 | 0.149 | 1.01x | 9.9/15.3/17.2% | 1.5/3.4% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 18

> burst-loss=0.2: decode_failures 23

> burst-loss=0.3: decode_failures 12

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.647 | 0.634 | 0.013 | - | - | 0.724 | 0.768 | 0.296 | 1.41x | 13.2/20.0/22.7% | 2.2/4.8% | 3 |
| 0.2 | 1 | 0.574 | 0.562 | 0.013 | - | - | 0.619 | 0.720 | 0.229 | 1.35x | 12.8/19.9/22.3% | 2.0/4.4% | 3 |
| 0.3 | 1 | 0.508 | 0.499 | 0.009 | - | - | 0.542 | 0.661 | 0.158 | 1.31x | 12.9/20.0/22.0% | 2.0/4.1% | 3 |

> extra-loss=0.0: decode_failures 3

> extra-loss=0.1: decode_failures 16

> extra-loss=0.2: decode_failures 20

> extra-loss=0.3: decode_failures 15

> slower: 5.32 s per simulated hour against 2.22 over 16 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.582 | 0.568 | 0.014 | - | - | 0.665 | 0.749 | 0.267 | 1.28x | 12.2/18.1/20.7% | 2.0/4.3% | 3 |
| 0.2 | 1 | 0.470 | 0.458 | 0.012 | - | - | 0.519 | 0.626 | 0.184 | 1.18x | 11.2/17.2/19.3% | 1.8/4.1% | 3 |
| 0.3 | 1 | 0.375 | 0.363 | 0.011 | - | - | 0.432 | 0.556 | 0.119 | 1.07x | 10.7/15.5/17.7% | 1.7/3.3% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 25

> burst-loss=0.2: decode_failures 15

> burst-loss=0.3: decode_failures 18

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.660 | 0.660 | 0.000 | - | - | 0.679 | 0.782 | 0.311 | 1.77x | 16.3/24.4/27.6% | 2.7/6.1% | 3 |
| directed-with-late-flood | 1 | 0.668 | 0.668 | 0.000 | - | - | 0.703 | 0.793 | 0.312 | 1.64x | 15.4/22.9/26.0% | 2.5/5.8% | 3 |
| m4-early-flood | 1 | 0.671 | 0.671 | 0.000 | - | - | 0.668 | 0.789 | 0.323 | 1.63x | 15.1/22.8/25.8% | 2.5/5.8% | 3 |

> dm-mode=flood-only: decode_failures 21

> dm-mode=directed-with-late-flood: decode_failures 15

> dm-mode=m4-early-flood: decode_failures 23

> slower: 7.63 s per simulated hour against 2.88 over 16 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.812 | 0.787 | 0.025 | - | - | 0.953 | 0.959 | 0.455 | 0.75x | 7.5/10.3/11.5% | 1.2/2.1% | 3 |
| 2.8 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> profile=2.8: decode_failures 3

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.785 | 0.778 | 0.008 | - | - | 0.945 | 0.946 | 0.275 | 1.25x | 12.8/18.3/19.9% | 2.0/4.7% | 3 |
| 0.5 | 1 | 0.764 | 0.752 | 0.012 | - | - | 0.931 | 0.941 | 0.291 | 1.11x | 12.4/16.9/19.6% | 1.7/3.8% | 3 |
| 0.75 | 1 | 0.800 | 0.782 | 0.017 | - | - | 0.958 | 0.961 | 0.380 | 0.92x | 9.7/13.2/15.1% | 1.4/3.2% | 3 |

> legacy-fraction=0.0: decode_failures 3

> legacy-fraction=0.5: decode_failures 3

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.782 | 0.774 | 0.008 | - | - | 0.942 | 0.942 | 0.215 | 1.24x | 12.8/18.5/19.7% | 1.9/4.8% | 3 |
| 0.5 | 1 | 0.775 | 0.762 | 0.012 | - | - | 0.946 | 0.950 | 0.377 | 1.10x | 12.4/16.8/19.2% | 1.8/3.7% | 3 |
| 0.75 | 1 | 0.806 | 0.790 | 0.016 | - | - | 0.962 | 0.963 | 0.367 | 0.89x | 9.6/13.4/15.3% | 1.4/3.2% | 3 |

> legacy-fraction=0.0: decode_failures 3

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.779 | 0.768 | 0.011 | - | - | 0.874 | 0.876 | 0.376 | 0.80x | 7.5/11.3/12.9% | 1.2/2.8% | 3 |
| signing=true | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> profile-flag=signing=true: decode_failures 3

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.796 | 0.772 | 0.025 | - | - | 0.921 | 0.958 | 0.340 | 0.76x | 8.1/11.6/13.5% | 1.2/3.0% | 3 |
| 2.5 | 1 | 0.810 | 0.784 | 0.026 | - | - | 0.959 | 0.964 | 0.331 | 0.78x | 8.2/11.6/13.5% | 1.3/3.0% | 3 |
| 2.6 | 1 | 0.802 | 0.774 | 0.028 | - | - | 0.956 | 0.963 | 0.355 | 0.74x | 8.0/11.5/13.4% | 1.2/2.9% | 3 |
| 2.7 | 1 | 0.814 | 0.791 | 0.023 | - | - | 0.948 | 0.966 | 0.336 | 0.73x | 7.9/11.4/13.5% | 1.2/3.1% | 3 |
| 2.8 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> profile=2.4: decode_failures 37

> profile=2.5: decode_failures 1

> profile=2.6: decode_failures 1

> profile=2.7: decode_failures 4

> profile=2.8: decode_failures 3

> slower: 4.66 s per simulated hour against 1.65 over 16 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.757 | 0.745 | 0.012 | - | - | 0.844 | 0.852 | 0.352 | 0.97x | 9.1/13.2/15.2% | 1.5/3.3% | 3 |
| 900 | 1 | 0.664 | 0.648 | 0.016 | - | - | 0.780 | 0.787 | 0.290 | 2.18x | 19.9/30.0/34.0% | 3.4/7.6% | 3 |
| 300 | 1 | 0.419 | 0.409 | 0.009 | - | - | 0.429 | 0.512 | 0.184 | 4.55x | 39.4/60.9/63.2% | 6.9/14.3% | 3 |

> broadcast-interval-s=900: decode_failures 3

> broadcast-interval-s=300: decode_failures 16

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.860 | 0.853 | 0.006 | - | - | 0.935 | 0.936 | 0.549 | 1.10x | 10.2/14.0/15.5% | 1.8/3.4% | 3 |
| 900 | 1 | 0.775 | 0.766 | 0.008 | - | - | 0.851 | 0.855 | 0.459 | 2.47x | 22.2/31.9/35.4% | 3.9/7.7% | 3 |
| 300 | 1 | 0.518 | 0.511 | 0.007 | - | - | 0.500 | 0.595 | 0.246 | 5.20x | 43.9/65.4/67.0% | 8.4/15.3% | 3 |

> broadcast-interval-s=300: decode_failures 19

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.747 | 0.734 | 0.012 | - | - | 0.835 | 0.838 | 0.365 | 1.33x | 12.3/18.3/20.8% | 2.0/4.6% | 3 |
| sinusoid | 1 | 0.728 | 0.715 | 0.013 | - | - | 0.811 | 0.821 | 0.329 | 1.31x | 12.0/18.0/20.4% | 2.0/4.5% | 3 |
| commuter | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> diurnal=flat: decode_failures 1

> diurnal=sinusoid: decode_failures 8

> diurnal=commuter: decode_failures 3

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.664 | 0.648 | 0.016 | - | - | 0.780 | 0.787 | 0.290 | 2.18x | 19.9/30.0/34.0% | 3.4/7.6% | 3 |
| 3600 | 1 | 0.757 | 0.745 | 0.012 | - | - | 0.844 | 0.852 | 0.352 | 0.97x | 9.1/13.2/15.2% | 1.5/3.3% | 3 |
| 10800 | 1 | 0.780 | 0.767 | 0.013 | - | - | 0.884 | 0.891 | 0.351 | 0.65x | 6.2/8.7/10.2% | 1.0/2.2% | 3 |
| 43200 | 1 | 0.798 | 0.789 | 0.010 | - | - | 0.892 | 0.898 | 0.381 | 0.45x | 4.3/6.1/7.0% | 0.7/1.7% | 3 |

> broadcast-interval-s=900: decode_failures 3

> broadcast-interval-s=10800: decode_failures 4

> broadcast-interval-s=43200: decode_failures 1

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.700 | 0.685 | 0.015 | - | - | 0.808 | 0.817 | 0.353 | 1.47x | 13.6/20.2/23.1% | 2.3/5.1% | 3 |
| 1.0 | 1 | 0.693 | 0.678 | 0.015 | - | - | 0.787 | 0.792 | 0.333 | 1.59x | 14.6/22.0/25.2% | 2.4/5.6% | 3 |
| 4.0 | 1 | 0.661 | 0.647 | 0.013 | - | - | 0.749 | 0.786 | 0.324 | 1.94x | 18.0/27.5/31.3% | 2.9/6.9% | 3 |

> traceroute-per-hour=0.0: decode_failures 3

> traceroute-per-hour=0.25: decode_failures 3

> traceroute-per-hour=1.0: decode_failures 1

> traceroute-per-hour=4.0: decode_failures 20

> slower: 4.33 s per simulated hour against 2.14 over 16 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.667 | 0.655 | 0.013 | - | - | 0.869 | 0.880 | 0.452 | 5.78x | 48.7/62.8/68.9% | 4.1/12.1% | 3 |
| 1.0 | 1 | 0.614 | 0.604 | 0.010 | - | - | 0.804 | 0.833 | 0.405 | 6.45x | 53.8/67.5/73.2% | 4.7/13.1% | 3 |

> traceroute-per-hour=0.0: decode_failures 79

> traceroute-per-hour=1.0: decode_failures 105

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.527 | 0.515 | 0.013 | - | - | 0.554 | 0.737 | 0.152 | 1.20x | 11.6/19.0/23.1% | 2.8/5.7% | 3 |
| 60 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 90 | 1 | 0.828 | 0.821 | 0.007 | - | - | 0.980 | 0.981 | 0.261 | 1.77x | 15.0/25.8/30.0% | 1.7/5.3% | 3 |
| 120 | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.984 | 0.985 | 0.638 | 2.07x | 18.0/25.5/29.7% | 1.5/4.8% | 3 |
| 150 | 1 | 0.920 | 0.918 | 0.003 | - | - | 0.997 | 0.998 | 0.680 | 2.67x | 23.9/34.1/38.4% | 1.5/5.7% | 3 |

> nodes=40: decode_failures 9

> nodes=60: decode_failures 3

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 120 | 1 | 0.463 | 0.451 | 0.013 | - | - | 0.690 | 0.699 | 0.000 | 2.29x | 12.3/18.2/21.4% | 1.7/4.5% | 3 |
| 250 | 1 | 0.322 | 0.312 | 0.009 | - | - | 0.594 | 0.634 | 0.037 | 5.13x | 12.9/22.5/45.0% | 1.8/5.6% | 3 |
| 500 | 1 | 0.179 | 0.175 | 0.003 | - | - | 0.311 | 0.336 | 0.033 | 9.45x | 12.9/19.9/32.5% | 1.7/4.7% | 3 |

> nodes=60: decode_failures 3

> nodes=120: decode_failures 51

> nodes=250: decode_failures 88

> nodes=500: decode_failures 127

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.462 | 0.450 | 0.012 | - | - | 0.698 | 0.714 | 0.000 | 2.13x | 11.4/16.5/19.7% | 1.6/4.1% | 3 |
| 250 | 1 | 0.327 | 0.317 | 0.010 | - | - | 0.620 | 0.649 | 0.045 | 4.86x | 12.3/21.4/42.5% | 1.7/5.2% | 3 |
| 500 | 1 | 0.180 | 0.177 | 0.004 | - | - | 0.320 | 0.334 | 0.034 | 8.93x | 12.2/19.2/30.8% | 1.6/4.4% | 3 |

> nodes=120: decode_failures 22

> nodes=250: decode_failures 44

> nodes=500: decode_failures 89

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.729 | 0.715 | 0.014 | - | - | 0.826 | 0.826 | 0.298 | 1.43x | 13.2/19.7/22.6% | 2.2/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.631 | 0.615 | 0.016 | - | - | 0.796 | 0.824 | 0.027 | 1.18x | 11.6/19.2/21.1% | 2.0/4.6% | 3 |

> role-mix=legacy-default: decode_failures 5

> role-mix=baymesh-2026-08: decode_failures 14

> slower: 4.53 s per simulated hour against 1.8 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.763 | 0.753 | 0.010 | - | - | 0.837 | 0.849 | 0.380 | 1.51x | 14.1/20.3/22.8% | 2.4/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.686 | 0.671 | 0.015 | - | - | 0.847 | 0.851 | 0.025 | 1.31x | 12.8/21.3/23.3% | 2.3/4.8% | 3 |

> role-mix=legacy-default: decode_failures 1

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.05 | 1 | 0.721 | 0.708 | 0.013 | - | - | 0.827 | 0.833 | 0.391 | 1.48x | 14.0/22.0/25.2% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.707 | 0.694 | 0.013 | - | - | 0.818 | 0.818 | 0.372 | 1.58x | 15.3/23.5/25.4% | 2.3/5.0% | 3 |
| 0.2 | 1 | 0.730 | 0.721 | 0.009 | - | - | 0.863 | 0.866 | 0.380 | 1.79x | 17.5/27.6/29.6% | 2.6/5.0% | 3 |

> router-late-fraction=0.0: decode_failures 3

> router-late-fraction=0.05: decode_failures 3

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| local-typical | 1 | 0.474 | 0.466 | 0.008 | - | - | 0.698 | 0.703 | 0.000 | 1.55x | 11.1/23.1/31.8% | 2.4/5.5% | 3 |
| event | 1 | 0.248 | 0.243 | 0.005 | - | - | 0.503 | 0.521 | 0.000 | 1.27x | 6.4/13.7/22.8% | 2.1/5.1% | 3 |
| backbone | 1 | 0.965 | 0.964 | 0.001 | - | - | 0.998 | 0.998 | 0.668 | 1.24x | 25.8/32.1/35.2% | 1.6/5.6% | 3 |

> siting-mix=uniform: decode_failures 3

> siting-mix=local-typical: decode_failures 3

> siting-mix=event: decode_failures 3

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.654 | 0.630 | 0.024 | - | - | 0.842 | 0.850 | 0.321 | 1.29x | 17.9/23.6/27.2% | 3.0/6.8% | 3 |
| 60 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 90 | 1 | 0.650 | 0.639 | 0.011 | - | - | 0.793 | 0.798 | 0.163 | 1.84x | 11.9/18.5/23.3% | 1.7/5.3% | 3 |
| 120 | 1 | 0.463 | 0.451 | 0.013 | - | - | 0.690 | 0.699 | 0.000 | 2.29x | 12.3/18.2/21.4% | 1.7/4.5% | 3 |
| 150 | 1 | 0.502 | 0.490 | 0.013 | - | - | 0.648 | 0.656 | 0.000 | 2.94x | 12.9/18.9/27.3% | 1.7/4.9% | 3 |

> nodes=40: decode_failures 1

> nodes=60: decode_failures 3

> nodes=90: decode_failures 3

> nodes=120: decode_failures 51

> nodes=150: decode_failures 24

> slower: 8.32 s per simulated hour against 3.27 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 1.25 | 1 | 0.311 | 0.291 | 0.020 | - | - | 0.485 | 0.516 | 0.000 | 1.22x | 7.7/15.5/20.2% | 1.8/4.3% | 3 |
| 1.5 | 1 | 0.145 | 0.144 | 0.002 | - | - | 0.243 | 0.362 | 0.000 | 0.95x | 4.7/12.7/16.9% | 1.5/4.1% | 3 |
| 2.0 | 1 | 0.055 | 0.055 | 0.000 | - | - | 0.078 | 0.118 | 0.000 | 0.48x | 1.8/3.6/5.7% | 0.7/2.0% | 3 |

> stretch=1.0: decode_failures 3

> stretch=1.25: decode_failures 29

> stretch=1.5: decode_failures 12

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| clustered | 1 | 0.839 | 0.835 | 0.004 | - | - | 0.924 | 0.924 | 0.314 | 1.21x | 18.5/28.8/31.1% | 1.6/5.3% | 3 |
| corridor | 1 | 0.387 | 0.371 | 0.016 | - | - | 0.538 | 0.560 | 0.000 | 1.41x | 12.6/23.0/26.8% | 2.1/5.3% | 3 |
| hub | 1 | 0.936 | 0.934 | 0.002 | - | - | 0.978 | 0.979 | 0.808 | 1.29x | 20.9/35.5/36.9% | 1.9/5.5% | 3 |

> topology=uniform: decode_failures 3

> topology=corridor: decode_failures 19

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.668 | 0.668 | 0.000 | - | - | 0.703 | 0.793 | 0.312 | 1.64x | 15.4/22.9/26.0% | 2.5/5.8% | 3 |
| True | 1 | 0.657 | 0.657 | 0.000 | - | - | 0.673 | 0.783 | 0.327 | 1.66x | 15.4/22.9/26.2% | 2.5/5.8% | 3 |

> coding-rate-ladder=False: decode_failures 15

> coding-rate-ladder=True: decode_failures 25

> slower: 7.79 s per simulated hour against 2.77 over 16 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.657 | 0.657 | 0.000 | - | - | 0.673 | 0.783 | 0.327 | 1.66x | 15.4/22.9/26.2% | 2.5/5.8% | 3 |
| m4-early-flood | 1 | 0.670 | 0.670 | 0.000 | - | - | 0.707 | 0.799 | 0.331 | 1.68x | 15.8/23.1/26.3% | 2.5/5.9% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 25

> dm-mode=m4-early-flood: decode_failures 28

> slower: 8.67 s per simulated hour against 2.52 over 16 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.708 | 0.708 | 0.000 | - | - | 0 | 0.000 | 0.326 | 1.36x | 12.7/18.9/21.5% | 2.1/4.8% | 3 |
| chain | 1 | 0.676 | 0.670 | 0.006 | - | - | 0.679 | 0.794 | 0.295 | 1.63x | 15.3/22.5/25.5% | 2.5/5.6% | 3 |
| sr | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> protocol=sr: decode_failures 3

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| True | 1 | 0.717 | 0.705 | 0.012 | - | - | 0.809 | 0.827 | 0.355 | 1.41x | 13.1/19.3/22.0% | 2.2/4.9% | 3 |

> extra-repeats=False: decode_failures 3

> extra-repeats=True: decode_failures 16

> slower: 5.01 s per simulated hour against 1.75 over 16 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.984 | 0.985 | 0.638 | 2.07x | 18.0/25.5/29.7% | 1.5/4.8% | 3 |
| True | 1 | 0.894 | 0.890 | 0.005 | - | - | 0.987 | 0.988 | 0.633 | 2.12x | 18.3/25.8/30.0% | 1.5/4.8% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.065 | 0.065 | 0.001 | - | - | 0.099 | 0.149 | 0.000 | 0.02x | 0.1/0.2/0.3% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.164 | 0.161 | 0.003 | - | - | 0.270 | 0.387 | 0.000 | 0.15x | 0.7/2.1/2.9% | 0.2/0.7% | 3 |
| LONG_TURBO | 1 | 0.564 | 0.552 | 0.011 | - | - | 0.769 | 0.772 | 0.000 | 1.25x | 9.7/14.9/17.0% | 2.0/4.3% | 3 |

> preset=MEDIUM_TURBO: decode_failures 10

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.736 | 0.721 | 0.015 | - | - | 0.815 | 0.827 | 0.419 | 1.34x | 14.7/20.7/23.2% | 2.0/4.9% | 3 |
| 1.0 | 1 | 0.868 | 0.845 | 0.024 | - | - | 0.921 | 0.926 | 0.662 | 0.96x | 19.2/23.8/25.8% | 1.3/4.8% | 3 |

> duct-per-hour=0.0: decode_failures 3

> duct-per-hour=0.25: decode_failures 4

> duct-per-hour=1.0: decode_failures 1

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.117 | 0.116 | 0.001 | - | - | 0.229 | 0.231 | 0.000 | 0.07x | 0.3/0.9/1.3% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| LITE_FAST | 1 | 0.549 | 0.538 | 0.011 | - | - | 0.766 | 0.767 | 0.000 | 0.94x | 7.9/13.2/14.4% | 1.4/3.5% | 3 |
| NARROW_SLOW | 1 | 0.626 | 0.613 | 0.013 | - | - | 0.798 | 0.800 | 0.052 | 1.29x | 11.5/16.8/19.3% | 2.0/4.6% | 3 |

> preset=LONG_FAST: decode_failures 3

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| temporal | 1 | 0.531 | 0.520 | 0.011 | - | - | 0.538 | 0.634 | 0.090 | 1.30x | 11.4/18.9/21.1% | 2.0/4.6% | 3 |
| transient | 1 | 0.708 | 0.696 | 0.012 | - | - | 0.811 | 0.817 | 0.347 | 1.41x | 12.9/19.3/22.1% | 2.2/4.9% | 3 |
| periodic | 1 | 0.527 | 0.518 | 0.009 | - | - | 0.564 | 0.643 | 0.222 | 1.26x | 11.8/17.9/20.1% | 1.9/4.2% | 3 |

> noise-profile=none: decode_failures 3

> noise-profile=temporal: decode_failures 13

> noise-profile=transient: decode_failures 2

> noise-profile=periodic: decode_failures 14

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.117 | 0.116 | 0.001 | - | - | 0.229 | 0.231 | 0.000 | 0.07x | 0.3/0.9/1.3% | 0.1/0.4% | 3 |
| LONG_FAST | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| LONG_MODERATE | 1 | 0.722 | 0.715 | 0.006 | - | - | 0.834 | 0.837 | 0.442 | 3.44x | 39.1/53.5/58.0% | 5.3/12.3% | 3 |

> preset=LONG_FAST: decode_failures 3

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.027 | 0.027 | 0.000 | - | - | 0.051 | 0.087 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.065 | 0.065 | 0.001 | - | - | 0.099 | 0.149 | 0.000 | 0.02x | 0.1/0.2/0.3% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| LONG_TURBO | 1 | 0.564 | 0.552 | 0.011 | - | - | 0.769 | 0.772 | 0.000 | 1.25x | 9.7/14.9/17.0% | 2.0/4.3% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.697 | 0.688 | 0.009 | - | - | 0.820 | 0.826 | 0.262 | 1.98x | 18.0/26.9/31.0% | 3.1/6.6% | 3 |

> preset=LONG_FAST: decode_failures 3

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.646 | 0.635 | 0.011 | - | - | 0.701 | 0.750 | 0.307 | 1.36x | 12.7/19.1/21.7% | 2.1/4.7% | 3 |
| 10000 | 1 | 0.527 | 0.518 | 0.009 | - | - | 0.564 | 0.643 | 0.222 | 1.26x | 11.8/17.9/20.1% | 1.9/4.2% | 3 |
| 4000 | 1 | 0.272 | 0.269 | 0.003 | - | - | 0.285 | 0.379 | 0.084 | 1.01x | 9.7/15.3/17.0% | 1.5/3.2% | 3 |
| 2000 | 1 | 0.064 | 0.064 | 0.000 | - | - | 0.058 | 0.109 | 0.017 | 0.65x | 6.7/10.0/11.1% | 1.0/1.7% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 20

> noise-pulse-interval-ms=10000: decode_failures 14

> noise-pulse-interval-ms=4000: decode_failures 6

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.145 | 0.144 | 0.002 | - | - | 0.243 | 0.362 | 0.000 | 0.95x | 4.7/12.7/16.9% | 1.5/4.1% | 3 |
| 1.0 | 1 | 0.511 | 0.506 | 0.004 | - | - | 0.584 | 0.657 | 0.360 | 0.84x | 12.9/17.9/19.1% | 1.2/3.9% | 3 |

> duct-per-hour=0.0: decode_failures 12

> duct-per-hour=1.0: decode_failures 32

> slower: 7.04 s per simulated hour against 2.43 over 16 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 22 | 1 | 0.146 | 0.144 | 0.002 | - | - | 0.245 | 0.359 | 0.000 | 0.96x | 4.8/12.9/17.1% | 1.4/4.2% | 3 |
| 17 | 1 | 0.066 | 0.065 | 0.001 | - | - | 0.098 | 0.147 | 0.000 | 0.52x | 2.2/5.0/7.2% | 0.9/2.2% | 3 |
| 14 | 1 | 0.035 | 0.035 | 0.000 | - | - | 0.055 | 0.087 | 0.000 | 0.38x | 1.2/3.3/5.3% | 0.7/1.6% | 3 |

> tx-power=30: decode_failures 3

> tx-power=22: decode_failures 8

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.984 | 0.985 | 0.638 | 2.07x | 18.0/25.5/29.7% | 1.5/4.8% | 3 |
| True | 1 | 0.875 | 0.870 | 0.005 | - | - | 0.976 | 0.977 | 0.624 | 2.42x | 20.6/29.6/33.7% | 1.7/5.4% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.728 | 0.715 | 0.013 | - | - | 0.820 | 0.840 | 0.385 | 1.49x | 14.2/21.9/24.8% | 2.2/4.9% | 3 |
| True | 1 | 0.754 | 0.743 | 0.010 | - | - | 0.827 | 0.839 | 0.405 | 1.62x | 14.8/23.0/25.3% | 2.7/5.0% | 3 |

> favourite-routers=False: decode_failures 47

> favourite-routers=True: decode_failures 10

> slower: 9.53 s per simulated hour against 1.71 over 16 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| random | 1 | 0.725 | 0.712 | 0.014 | - | - | 0.810 | 0.816 | 0.359 | 1.39x | 13.0/19.2/21.8% | 2.1/4.8% | 3 |

> hop-assign=centrality: decode_failures 3

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.538 | 0.518 | 0.020 | - | - | 0.623 | 0.656 | 0.084 | 1.08x | 10.3/15.6/18.1% | 1.5/4.2% | 3 |
| 7 | 1 | 0.821 | 0.812 | 0.008 | - | - | 0.888 | 0.889 | 0.503 | 1.57x | 14.4/20.4/22.8% | 2.5/4.9% | 3 |
| 15 | 1 | 0.871 | 0.867 | 0.004 | - | - | 0.917 | 0.920 | 0.568 | 1.68x | 15.5/21.3/23.7% | 2.7/5.1% | 3 |
| 32 | 1 | 0.874 | 0.870 | 0.004 | - | - | 0.919 | 0.921 | 0.569 | 1.66x | 15.4/21.1/23.4% | 2.7/5.0% | 3 |

> hop-limit=3: decode_failures 14

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.538 | 0.518 | 0.020 | - | - | 0.623 | 0.656 | 0.084 | 1.08x | 10.3/15.6/18.1% | 1.5/4.2% | 3 |
| 5 | 1 | 0.735 | 0.724 | 0.012 | - | - | 0.809 | 0.836 | 0.326 | 1.38x | 12.9/19.1/21.8% | 2.1/4.9% | 3 |
| 7 | 1 | 0.821 | 0.812 | 0.008 | - | - | 0.888 | 0.889 | 0.503 | 1.57x | 14.4/20.4/22.8% | 2.5/4.9% | 3 |

> hop-limit=3: decode_failures 14

> hop-limit=5: decode_failures 28

> slower: 4.5 s per simulated hour against 2.03 over 16 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| KNOWN_ONLY | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.700 | 0.700 | 0.000 | - | - | 0.616 | 0.820 | 0.338 | 1.38x | 12.8/19.1/21.7% | 2.2/4.9% | 3 |

> rebroadcast-mode=ALL: decode_failures 3

> rebroadcast-mode=KNOWN_ONLY: decode_failures 3

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.538 | 0.518 | 0.020 | - | - | 0.623 | 0.656 | 0.084 | 1.08x | 10.3/15.6/18.1% | 1.5/4.2% | 3 |
| True | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> hop-spread=False: decode_failures 14

> hop-spread=True: decode_failures 3

> slower: 4.34 s per simulated hour against 2.11 over 16 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| BALANCED | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| STRICT | 1 | 0.574 | 0.574 | 0.000 | - | - | 0.681 | 0.693 | 0.252 | 1.52x | 14.2/21.1/24.1% | 2.4/5.3% | 3 |

> signature-policy=COMPATIBLE: decode_failures 3

> signature-policy=BALANCED: decode_failures 3

> signature-policy=STRICT: decode_failures 11

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| dm | 1 | 0.704 | 0.689 | 0.015 | - | - | 0.824 | 0.829 | 0.340 | 1.40x | 13.0/19.4/22.0% | 2.1/4.9% | 3 |

> advert-transport=broadcast: decode_failures 3

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.710 | 0.697 | 0.013 | - | - | 0.788 | 0.813 | 0.348 | 1.42x | 13.0/19.5/22.3% | 2.2/4.9% | 3 |
| local | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| time | 1 | 0.700 | 0.685 | 0.015 | - | - | 0.808 | 0.819 | 0.314 | 1.46x | 13.5/20.0/22.9% | 2.3/5.0% | 3 |
| window | 1 | 0.711 | 0.698 | 0.014 | - | - | 0.808 | 0.821 | 0.340 | 1.41x | 13.0/19.4/22.3% | 2.2/5.0% | 3 |

> bucket-mode=global: misdecodes 6

> bucket-mode=local: decode_failures 3

> bucket-mode=time: misdecodes 6

> bucket-mode=window: misdecodes 9

> bucket-mode=window: decode_failures 4

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.699 | 0.685 | 0.014 | - | - | 0.789 | 0.804 | 0.323 | 1.57x | 14.7/21.3/24.4% | 2.4/5.3% | 3 |
| 1800 | 1 | 0.700 | 0.685 | 0.015 | - | - | 0.808 | 0.819 | 0.314 | 1.46x | 13.5/20.0/22.9% | 2.3/5.0% | 3 |
| 3600 | 1 | 0.707 | 0.694 | 0.013 | - | - | 0.797 | 0.816 | 0.329 | 1.43x | 13.1/19.7/22.6% | 2.2/5.0% | 3 |

> time-bucket-s=600: misdecodes 45

> time-bucket-s=1800: misdecodes 6

> time-bucket-s=3600: misdecodes 2

> time-bucket-s=3600: decode_failures 6

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| interval | 1 | 0.686 | 0.670 | 0.015 | - | - | 0.786 | 0.804 | 0.315 | 1.88x | 18.6/25.2/28.6% | 2.8/6.5% | 3 |
| aimd | 1 | 0.701 | 0.694 | 0.007 | - | - | 0.707 | 0.812 | 0.341 | 1.44x | 13.2/19.8/22.6% | 2.2/5.0% | 3 |
| bucket+interval | 1 | 0.676 | 0.660 | 0.015 | - | - | 0.775 | 0.776 | 0.313 | 1.90x | 18.8/25.4/29.0% | 2.8/6.6% | 3 |

> trigger=bucket: decode_failures 3

> trigger=interval: misdecodes 7

> trigger=interval: decode_failures 12

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 35

> trigger=bucket+interval: misdecodes 6

> trigger=bucket+interval: decode_failures 1

> slower: 8.25 s per simulated hour against 3.26 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.708 | 0.694 | 0.013 | - | - | 0.793 | 0.820 | 0.353 | 1.41x | 13.1/19.3/21.9% | 2.2/4.8% | 3 |
| 8 | 1 | 0.703 | 0.692 | 0.011 | - | - | 0.775 | 0.818 | 0.345 | 1.42x | 13.1/19.6/22.3% | 2.2/4.9% | 3 |
| 16 | 1 | 0.700 | 0.687 | 0.013 | - | - | 0.784 | 0.811 | 0.345 | 1.42x | 13.2/19.5/22.3% | 2.2/4.9% | 3 |
| 32 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 50 | 1 | 0.710 | 0.696 | 0.014 | - | - | 0.810 | 0.815 | 0.356 | 1.40x | 12.9/19.2/22.0% | 2.2/4.9% | 3 |

> capacity=4: decode_failures 75

> capacity=8: decode_failures 59

> capacity=16: decode_failures 58

> capacity=32: decode_failures 3

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.708 | 0.694 | 0.013 | - | - | 0.793 | 0.820 | 0.353 | 1.41x | 13.1/19.3/21.9% | 2.2/4.8% | 3 |
| 8 | 1 | 0.703 | 0.692 | 0.011 | - | - | 0.775 | 0.818 | 0.345 | 1.42x | 13.1/19.6/22.3% | 2.2/4.9% | 3 |
| 16 | 1 | 0.700 | 0.687 | 0.013 | - | - | 0.784 | 0.811 | 0.345 | 1.42x | 13.2/19.5/22.3% | 2.2/4.9% | 3 |
| 32 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 50 | 1 | 0.710 | 0.696 | 0.014 | - | - | 0.810 | 0.815 | 0.356 | 1.40x | 12.9/19.2/22.0% | 2.2/4.9% | 3 |

> capacity=4: decode_failures 75

> capacity=8: decode_failures 59

> capacity=16: decode_failures 58

> capacity=32: decode_failures 3

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.697 | 0.697 | 0.000 | - | - | 0.623 | 0.816 | 0.340 | 1.39x | 12.9/19.3/21.8% | 2.2/4.9% | 3 |
| 16 | 1 | 0.701 | 0.695 | 0.006 | - | - | 0.685 | 0.823 | 0.327 | 1.41x | 13.0/19.5/22.2% | 2.2/5.0% | 3 |
| 32 | 1 | 0.711 | 0.698 | 0.014 | - | - | 0.808 | 0.821 | 0.340 | 1.41x | 13.0/19.4/22.3% | 2.2/5.0% | 3 |

> capacity=8: decode_failures 103

> capacity=16: misdecodes 1

> capacity=16: decode_failures 84

> capacity=32: misdecodes 9

> capacity=32: decode_failures 4

> slower: 4.43 s per simulated hour against 1.67 over 16 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.676 | 0.660 | 0.015 | - | - | 0.775 | 0.776 | 0.313 | 1.90x | 18.8/25.4/29.0% | 2.8/6.6% | 3 |
| 02-06 | 1 | 0.703 | 0.696 | 0.007 | - | - | 0.726 | 0.815 | 0.353 | 1.44x | 13.5/19.8/22.5% | 2.2/5.0% | 3 |
| 00-08 | 1 | 0.708 | 0.700 | 0.008 | - | - | 0.737 | 0.822 | 0.363 | 1.51x | 14.3/20.5/23.5% | 2.3/5.2% | 3 |

> catch-up-hours=: misdecodes 6

> catch-up-hours=: decode_failures 1

> catch-up-hours=02-06: decode_failures 40

> catch-up-hours=00-08: decode_failures 39

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.706 | 0.700 | 0.006 | - | - | 0.857 | 0.858 | 0.354 | 1.42x | 13.2/19.7/22.4% | 2.2/5.0% | 3 |
| 2 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 3 | 1 | 0.732 | 0.696 | 0.036 | - | - | 0.895 | 0.899 | 0.354 | 1.44x | 13.2/19.9/22.5% | 2.2/5.0% | 3 |
| 4 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.715 | 0.900 | 0.331 | 1.42x | 13.2/19.7/22.5% | 2.2/5.1% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=4: decode_failures 21

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.706 | 0.700 | 0.006 | - | - | 0.857 | 0.858 | 0.354 | 1.42x | 13.2/19.7/22.4% | 2.2/5.0% | 3 |
| 2 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 3 | 1 | 0.732 | 0.696 | 0.036 | - | - | 0.895 | 0.899 | 0.354 | 1.44x | 13.2/19.9/22.5% | 2.2/5.0% | 3 |
| 4 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.715 | 0.900 | 0.331 | 1.42x | 13.2/19.7/22.5% | 2.2/5.1% | 3 |
| 5 | 1 | 0.702 | 0.684 | 0.018 | - | - | 0.724 | 0.896 | 0.342 | 1.43x | 13.4/20.0/22.6% | 2.2/5.2% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=4: decode_failures 21

> hops-apart=5: decode_failures 17

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.705 | 0.691 | 0.014 | - | - | 0.807 | 0.812 | 0.340 | 1.43x | 13.2/19.6/22.6% | 2.2/5.0% | 3 |
| 30 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 120 | 1 | 0.702 | 0.688 | 0.015 | - | - | 0.802 | 0.807 | 0.340 | 1.43x | 13.2/19.7/22.5% | 2.2/5.0% | 3 |
| 600 | 1 | 0.711 | 0.698 | 0.014 | - | - | 0.814 | 0.830 | 0.360 | 1.42x | 13.1/19.6/22.3% | 2.2/4.9% | 3 |

> advert-jitter-s=1: decode_failures 2

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 1

> advert-jitter-s=600: decode_failures 39

> slower: 5.34 s per simulated hour against 1.76 over 16 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.705 | 0.691 | 0.014 | - | - | 0.807 | 0.812 | 0.340 | 1.43x | 13.2/19.6/22.6% | 2.2/5.0% | 3 |
| 30 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 120 | 1 | 0.702 | 0.688 | 0.015 | - | - | 0.802 | 0.807 | 0.340 | 1.43x | 13.2/19.7/22.5% | 2.2/5.0% | 3 |
| 600 | 1 | 0.711 | 0.698 | 0.014 | - | - | 0.814 | 0.830 | 0.360 | 1.42x | 13.1/19.6/22.3% | 2.2/4.9% | 3 |

> advert-jitter-s=1: decode_failures 2

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 1

> advert-jitter-s=600: decode_failures 39

> slower: 4.51 s per simulated hour against 1.78 over 16 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.700 | 0.692 | 0.007 | - | - | 0.582 | 0.874 | 0.352 | 1.40x | 13.1/19.5/22.0% | 2.2/4.9% | 3 |
| routers | 1 | 0.722 | 0.696 | 0.026 | - | - | 0.917 | 0.924 | 0.350 | 1.42x | 13.2/19.9/22.7% | 2.2/5.0% | 3 |
| alternate-routers | 1 | 0.707 | 0.698 | 0.009 | - | - | 0.912 | 0.914 | 0.340 | 1.42x | 13.2/20.0/22.7% | 2.2/5.3% | 3 |
| beside-router | 1 | 0.707 | 0.698 | 0.009 | - | - | 0.930 | 0.930 | 0.346 | 1.41x | 13.0/19.7/22.3% | 2.2/5.0% | 3 |
| random-clients | 1 | 0.715 | 0.699 | 0.016 | - | - | 0.914 | 0.923 | 0.331 | 1.42x | 13.1/19.7/22.8% | 2.2/5.2% | 3 |
| hops-apart | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> place=spread: decode_failures 17

> place=hops-apart: decode_failures 3

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.700 | 0.692 | 0.007 | - | - | 0.582 | 0.874 | 0.352 | 1.40x | 13.1/19.5/22.0% | 2.2/4.9% | 3 |
| routers | 1 | 0.722 | 0.696 | 0.026 | - | - | 0.917 | 0.924 | 0.350 | 1.42x | 13.2/19.9/22.7% | 2.2/5.0% | 3 |
| alternate-routers | 1 | 0.707 | 0.698 | 0.009 | - | - | 0.912 | 0.914 | 0.340 | 1.42x | 13.2/20.0/22.7% | 2.2/5.3% | 3 |
| beside-router | 1 | 0.707 | 0.698 | 0.009 | - | - | 0.930 | 0.930 | 0.346 | 1.41x | 13.0/19.7/22.3% | 2.2/5.0% | 3 |
| random-clients | 1 | 0.715 | 0.699 | 0.016 | - | - | 0.914 | 0.923 | 0.331 | 1.42x | 13.1/19.7/22.8% | 2.2/5.2% | 3 |
| hops-apart | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> place=spread: decode_failures 17

> place=hops-apart: decode_failures 3

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| broadcast | 1 | 0.742 | 0.674 | 0.068 | - | - | 0.756 | 0.785 | 0.413 | 1.57x | 14.5/21.5/24.2% | 2.4/5.3% | 3 |

> provide-transport=dm: decode_failures 3

> provide-transport=broadcast: decode_failures 7

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| heard | 1 | 0.701 | 0.688 | 0.013 | - | - | 0.798 | 0.806 | 0.323 | 1.43x | 13.2/19.7/22.5% | 2.2/5.0% | 3 |

> replay-ordering=tip: decode_failures 3

> replay-ordering=heard: misdecodes 4

> replay-ordering=heard: decode_failures 1

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.742 | 0.674 | 0.068 | - | - | 0.756 | 0.785 | 0.413 | 1.57x | 14.5/21.5/24.2% | 2.4/5.3% | 3 |
| heard | 1 | 0.745 | 0.677 | 0.068 | - | - | 0.759 | 0.795 | 0.432 | 1.57x | 14.4/21.5/24.3% | 2.4/5.4% | 3 |

> replay-ordering=tip: decode_failures 7

> replay-ordering=heard: decode_failures 11

> slower: 5.18 s per simulated hour against 1.73 over 16 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.709 | 0.697 | 0.011 | - | - | 0.759 | 0.824 | 0.352 | 1.41x | 13.0/19.5/22.2% | 2.2/4.9% | 3 |
| enum | 1 | 0.708 | 0.694 | 0.014 | - | - | 0.804 | 0.825 | 0.327 | 1.40x | 12.9/19.4/22.0% | 2.2/4.8% | 3 |
| hybrid | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> resolve=sketch: decode_failures 18

> resolve=hybrid: decode_failures 3

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.722 | 0.696 | 0.026 | - | - | 0.917 | 0.924 | 0.350 | 1.42x | 13.2/19.9/22.7% | 2.2/5.0% | 3 |
| 6 | 1 | 0.717 | 0.689 | 0.029 | - | - | 0.933 | 0.935 | 0.325 | 1.47x | 13.8/20.7/23.5% | 2.2/5.5% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.708 | 0.701 | 0.007 | - | - | 0.765 | 0.812 | 0.335 | 1.39x | 12.9/19.2/21.9% | 2.2/4.9% | 2 |
| 3 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 5 | 1 | 0.717 | 0.698 | 0.019 | - | - | 0.891 | 0.896 | 0.352 | 1.44x | 13.3/19.8/22.4% | 2.3/5.0% | 5 |
| 8 | 1 | 0.713 | 0.687 | 0.026 | - | - | 0.914 | 0.917 | 0.356 | 1.49x | 13.5/20.1/23.1% | 2.3/5.0% | 8 |

> servers=2: decode_failures 15

> servers=3: decode_failures 3

> servers=5: decode_failures 1

> slower: 5.3 s per simulated hour against 2.63 over 16 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.708 | 0.701 | 0.007 | - | - | 0.765 | 0.812 | 0.335 | 1.39x | 12.9/19.2/21.9% | 2.2/4.9% | 2 |
| 3 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 5 | 1 | 0.717 | 0.698 | 0.019 | - | - | 0.891 | 0.896 | 0.352 | 1.44x | 13.3/19.8/22.4% | 2.3/5.0% | 5 |
| 8 | 1 | 0.713 | 0.687 | 0.026 | - | - | 0.914 | 0.917 | 0.356 | 1.49x | 13.5/20.1/23.1% | 2.3/5.0% | 8 |

> servers=2: decode_failures 15

> servers=3: decode_failures 3

> servers=5: decode_failures 1

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| True | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |

> signed=False: decode_failures 3

> signed=True: decode_failures 3

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.716 | 0.703 | 0.013 | - | - | 0.789 | 0.816 | 0.318 | 1.35x | 12.4/18.8/21.2% | 2.1/4.7% | 3 |
| 1 | 1 | 0.710 | 0.696 | 0.014 | - | - | 0.823 | 0.831 | 0.322 | 1.33x | 12.4/18.3/21.0% | 2.1/4.6% | 3 |
| 2 | 1 | 0.705 | 0.693 | 0.012 | - | - | 0.789 | 0.807 | 0.360 | 1.34x | 12.2/18.5/21.1% | 2.1/4.7% | 3 |
| 4 | 1 | 0.723 | 0.712 | 0.011 | - | - | 0.824 | 0.831 | 0.353 | 1.33x | 12.3/18.5/21.0% | 2.1/4.6% | 3 |

> sr-retries=0: decode_failures 4

> sr-retries=1: decode_failures 1

> sr-retries=2: decode_failures 4

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.714 | 0.699 | 0.015 | - | - | 0.820 | 0.831 | 0.332 | 1.41x | 13.0/19.5/22.2% | 2.2/4.9% | 3 |
| 24 | 1 | 0.698 | 0.683 | 0.015 | - | - | 0.815 | 0.821 | 0.343 | 1.41x | 13.0/19.6/22.4% | 2.2/4.9% | 3 |
| 32 | 1 | 0.704 | 0.690 | 0.014 | - | - | 0.797 | 0.807 | 0.350 | 1.41x | 13.0/19.4/22.3% | 2.2/4.9% | 3 |
| 64 | 1 | 0.690 | 0.678 | 0.011 | - | - | 0.776 | 0.798 | 0.344 | 1.42x | 13.1/19.5/22.3% | 2.2/4.9% | 3 |

> short-id-bits=16: decode_failures 5

> short-id-bits=24: decode_failures 6

> short-id-bits=32: decode_failures 3

> short-id-bits=64: decode_failures 12

> slower: 4.09 s per simulated hour against 1.79 over 16 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.703 | 0.689 | 0.014 | - | - | 0.799 | 0.811 | 0.328 | 1.49x | 13.9/20.3/23.2% | 2.2/5.1% | 3 |
| 16 | 1 | 0.703 | 0.688 | 0.015 | - | - | 0.796 | 0.806 | 0.346 | 1.41x | 13.0/19.4/22.2% | 2.2/4.9% | 3 |
| 32 | 1 | 0.711 | 0.698 | 0.014 | - | - | 0.808 | 0.821 | 0.340 | 1.41x | 13.0/19.4/22.3% | 2.2/5.0% | 3 |

> window-size=8: misdecodes 54

> window-size=16: misdecodes 13

> window-size=32: misdecodes 9

> window-size=32: decode_failures 4

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.984 | 0.985 | 0.638 | 2.07x | 18.0/25.5/29.7% | 1.5/4.8% | 3 |
| True | 1 | 0.675 | 0.664 | 0.012 | - | - | 0.864 | 0.876 | 0.461 | 5.68x | 48.0/62.3/68.4% | 4.0/11.9% | 3 |

> no-congestion-scaling=True: decode_failures 57

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.327 | 0.317 | 0.010 | - | - | 0.620 | 0.649 | 0.045 | 4.86x | 12.3/21.4/42.5% | 1.7/5.2% | 3 |
| truesize | 1 | 0.360 | 0.348 | 0.012 | - | - | 0.681 | 0.695 | 0.052 | 2.75x | 7.1/14.3/29.0% | 0.9/4.0% | 3 |

> congestion-input=hotstore: decode_failures 44

> congestion-input=truesize: decode_failures 29

> slower: 25.1 s per simulated hour against 11.2 over 16 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.895 | 0.890 | 0.005 | - | - | 0.987 | 0.988 | 0.630 | 1.98x | 17.1/24.6/28.4% | 1.4/4.6% | 3 |
| adaptive | 1 | 0.892 | 0.888 | 0.004 | - | - | 0.984 | 0.985 | 0.638 | 2.07x | 18.0/25.5/29.7% | 1.5/4.8% | 3 |

