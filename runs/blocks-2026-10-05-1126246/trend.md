# Sweep blocks-2026-10-05-1126246

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 1126246 · seeds 1126246
- **blocks** 87 run
- **compute** 14.4 h of simulator time across every cell
- **generated** 2026-10-05T10:39:37+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>200 warnings</summary>

- AD-amplifiers: amplifier-mix=none: decode_failures 3
- AD-amplifiers: amplifier-mix=sprinkled: decode_failures 3
- AD-amplify-worst: amplify-worst=0.0: decode_failures 3
- AD-amplify-worst: amplify-worst=0.1: decode_failures 44
- AD-amplify-worst: slower: 6.33 s per simulated hour against 1.86 over 45 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=inverse: decode_failures 61
- AD-worst: slower: 12.2 s per simulated hour against 3.41 over 45 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 99
- DB-platform: platform-mix=constrained: decode_failures 2
- DB-warm: warm-num-nodes=0: queue drops 13.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 109
- DB-warm: warm-num-nodes=25: queue drops 13.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 109
- DB-warm: warm-num-nodes=100: queue drops 13.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 109
- DB-warm: warm-num-nodes=2000: queue drops 13.5% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 109
- DG-burst: burst-loss=0.0: decode_failures 3
- DG-burst: burst-loss=0.1: decode_failures 4
- DG-burst: burst-loss=0.2: decode_failures 32
- DG-burst: burst-loss=0.3: decode_failures 29
- DG-loss: extra-loss=0.0: decode_failures 3
- DG-loss: extra-loss=0.1: decode_failures 37
- DG-loss: extra-loss=0.2: decode_failures 15
- DG-loss: extra-loss=0.3: decode_failures 27
- DG-loss: slower: 6.74 s per simulated hour against 2.27 over 45 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.0: decode_failures 3
- DG-outage: burst-loss=0.1: decode_failures 43
- DG-outage: burst-loss=0.2: decode_failures 23
- DG-outage: burst-loss=0.3: decode_failures 22
- DM-mode: dm-mode=flood-only: decode_failures 31
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 34
- DM-mode: dm-mode=m4-early-flood: decode_failures 30
- DM-mode: slower: 11.1 s per simulated hour against 3.27 over 45 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-firmware: profile=2.8: decode_failures 3
- FW-mixed-26: legacy-fraction=0.0: decode_failures 3
- FW-mixed: legacy-fraction=0.0: decode_failures 3
- FW-signing-cost: profile-flag=signing=true: decode_failures 3
- FW-versions: profile=2.8: decode_failures 3
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 17
- LD-chatty: broadcast-interval-s=900: decode_failures 11
- LD-chatty: broadcast-interval-s=300: decode_failures 13
- LD-diurnal: diurnal=flat: decode_failures 1
- LD-diurnal: diurnal=sinusoid: decode_failures 32
- LD-diurnal: diurnal=commuter: decode_failures 3
- LD-diurnal: slower: 4.22 s per simulated hour against 1.54 over 45 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-interval: broadcast-interval-s=900: decode_failures 11
- LD-interval: broadcast-interval-s=43200: decode_failures 1
- LD-traceroute: traceroute-per-hour=0.0: decode_failures 3
- LD-traceroute: traceroute-per-hour=1.0: decode_failures 7
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 31
- LD-traceroute: slower: 5.29 s per simulated hour against 2.1 over 45 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 13.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 109
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 20.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 84
- MS-density: nodes=60: decode_failures 3
- MS-hopscale: nodes=60: decode_failures 3
- MS-hopscale: nodes=250: decode_failures 4
- MS-hopscale: nodes=500: decode_failures 166
- MS-oversubscribed: nodes=500: decode_failures 98
- MS-router-late: router-late-fraction=0.0: decode_failures 3
- MS-siting: siting-mix=uniform: decode_failures 3
- MS-size: nodes=40: decode_failures 23
- MS-size: nodes=60: decode_failures 3
- MS-size: nodes=150: decode_failures 88
- MS-size: slower: 7.71 s per simulated hour against 3.39 over 45 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.0: decode_failures 3
- MS-stretch: stretch=1.25: decode_failures 3
- MS-stretch: stretch=1.5: decode_failures 33
- MS-topology: topology=uniform: decode_failures 3
- MS-topology: topology=clustered: decode_failures 5
- PR-crladder: coding-rate-ladder=False: decode_failures 34
- PR-crladder: coding-rate-ladder=True: decode_failures 33
- PR-crladder: slower: 11.6 s per simulated hour against 2.79 over 45 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 33
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 31
- PR-dmmode-cr: slower: 11.1 s per simulated hour against 2.77 over 45 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-protocol: protocol=sr: decode_failures 3
- PR-repeats: extra-repeats=False: decode_failures 3
- PR-repeats: extra-repeats=True: decode_failures 2
- RF-bw500: preset=SHORT_TURBO: decode_failures 8
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 23
- RF-duct: duct-per-hour=0.0: decode_failures 3
- RF-duct: duct-per-hour=0.25: decode_failures 3
- RF-eu-presets: preset=LONG_FAST: decode_failures 3
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 1
- RF-noise: noise-profile=none: decode_failures 3
- RF-noise: noise-profile=temporal: decode_failures 31
- RF-noise: noise-profile=transient: decode_failures 3
- RF-noise: noise-profile=periodic: decode_failures 26
- RF-preset: preset=LONG_FAST: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 3
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 6
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 8
- RF-preset-turbo: preset=LONG_FAST: decode_failures 3
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 3
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 26
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-pulse: slower: 3.43 s per simulated hour against 1.63 over 45 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 33
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 1
- RF-stretch-duct: slower: 6.19 s per simulated hour against 1.84 over 45 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=30: decode_failures 3
- RF-txpower: tx-power=22: decode_failures 17
- RF-txpower: tx-power=17: decode_failures 6
- RT-hopassign: hop-assign=centrality: decode_failures 3
- RT-hoplimit: hop-limit=3: decode_failures 4
- RT-hopspread: hop-limit=3: decode_failures 4
- RT-rebroadcast: rebroadcast-mode=ALL: decode_failures 3
- RT-rebroadcast: rebroadcast-mode=KNOWN_ONLY: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 4
- RT-spread: hop-spread=True: decode_failures 3
- SC-signing: signature-policy=COMPATIBLE: decode_failures 3
- SC-signing: signature-policy=BALANCED: decode_failures 3
- SC-signing: signature-policy=STRICT: decode_failures 4
- SF-advert-transport: advert-transport=broadcast: decode_failures 3
- SF-advert-transport: advert-transport=dm: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 18
- SF-bucket-mode: bucket-mode=local: decode_failures 3
- SF-bucket-mode: bucket-mode=time: misdecodes 19
- SF-bucket-mode: bucket-mode=window: misdecodes 12
- SF-bucket-time: time-bucket-s=600: misdecodes 74
- SF-bucket-time: time-bucket-s=1800: misdecodes 19
- SF-bucket-time: time-bucket-s=3600: misdecodes 8
- SF-bucket-time: time-bucket-s=3600: decode_failures 6
- SF-cadence: trigger=bucket: decode_failures 3
- SF-cadence: trigger=interval: misdecodes 6
- SF-cadence: trigger=interval: decode_failures 9
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 22
- SF-cadence: trigger=bucket+interval: misdecodes 10
- SF-capacity-local: capacity=4: decode_failures 71
- SF-capacity-local: capacity=8: decode_failures 52
- SF-capacity-local: capacity=16: decode_failures 49
- SF-capacity-local: capacity=32: decode_failures 3
- SF-capacity: capacity=4: decode_failures 71
- SF-capacity: capacity=8: decode_failures 52
- SF-capacity: capacity=16: decode_failures 49
- SF-capacity: capacity=32: decode_failures 3
- SF-capacity-window: capacity=8: misdecodes 3
- SF-capacity-window: capacity=8: decode_failures 78
- SF-capacity-window: capacity=16: misdecodes 17
- SF-capacity-window: capacity=16: decode_failures 33
- SF-capacity-window: capacity=32: misdecodes 12
- SF-catchup: catch-up-hours=: misdecodes 10
- SF-catchup: catch-up-hours=02-06: decode_failures 48
- SF-catchup: catch-up-hours=00-08: decode_failures 45
- SF-hops-flat: hops-apart=2: decode_failures 3
- SF-hops-flat: hops-apart=4: decode_failures 25
- SF-hops-spread: hops-apart=2: decode_failures 3
- SF-hops-spread: hops-apart=4: decode_failures 25
- SF-hops-spread: hops-apart=5: decode_failures 25
- SF-jitter-global: advert-jitter-s=1: decode_failures 2
- SF-jitter-global: advert-jitter-s=30: decode_failures 3
- SF-jitter-global: advert-jitter-s=120: decode_failures 2
- SF-jitter-global: advert-jitter-s=600: decode_failures 24
- SF-jitter-global: slower: 4.18 s per simulated hour against 1.77 over 45 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-jitter-local: advert-jitter-s=1: decode_failures 2
- SF-jitter-local: advert-jitter-s=30: decode_failures 3
- SF-jitter-local: advert-jitter-s=120: decode_failures 2
- SF-jitter-local: advert-jitter-s=600: decode_failures 24
- SF-jitter-local: slower: 4.18 s per simulated hour against 1.79 over 45 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-place-flat: place=spread: decode_failures 30
- SF-place-flat: place=hops-apart: decode_failures 3
- SF-place-spread: place=spread: decode_failures 30
- SF-place-spread: place=hops-apart: decode_failures 3
- SF-provide-transport: provide-transport=dm: decode_failures 3
- SF-provide-transport: provide-transport=broadcast: decode_failures 37
- SF-provide-transport: slower: 7.28 s per simulated hour against 1.75 over 45 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 37
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 3
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 31
- SF-replay-order-broadcast: slower: 9.68 s per simulated hour against 1.72 over 45 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=tip: decode_failures 3
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-resolve: resolve=sketch: decode_failures 29
- SF-resolve: resolve=hybrid: decode_failures 3
- SF-resolve: slower: 4.61 s per simulated hour against 1.54 over 45 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-flat: servers=3: decode_failures 3
- SF-servers-flat: servers=5: decode_failures 57
- SF-servers-flat: servers=8: decode_failures 109
- SF-servers-flat: slower: 13.7 s per simulated hour against 2.4 over 45 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-servers-spread: servers=3: decode_failures 3
- SF-servers-spread: servers=5: decode_failures 57
- SF-servers-spread: servers=8: decode_failures 109
- SF-servers-spread: slower: 13.9 s per simulated hour against 2.29 over 45 prior run(s) - 6.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-signed: signed=False: decode_failures 3
- SF-signed: signed=True: decode_failures 3
- SF-sr-retries: sr-retries=0: decode_failures 16
- SF-width: short-id-bits=16: decode_failures 1
- SF-width: short-id-bits=32: decode_failures 3
- SF-width: short-id-bits=64: decode_failures 34
- SF-width: slower: 3.63 s per simulated hour against 1.66 over 45 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 90
- SF-window-size: window-size=16: misdecodes 39
- SF-window-size: window-size=32: misdecodes 12
- TH-congestion-input: faster: 5.4 s per simulated hour against 11.2 over 45 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- TH-congestion: no-congestion-scaling=True: queue drops 12.4% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 106

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-servers-spread` | 13.9 | 2.29 | 6.07x | 45 |
| `SF-servers-flat` | 13.7 | 2.4 | 5.72x | 45 |
| `SF-replay-order-broadcast` | 9.68 | 1.72 | 5.64x | 45 |
| `SF-provide-transport` | 7.28 | 1.75 | 4.16x | 45 |
| `PR-crladder` | 11.6 | 2.79 | 4.15x | 45 |
| `PR-dmmode-cr` | 11.1 | 2.77 | 4.02x | 45 |
| `AD-worst` | 12.2 | 3.41 | 3.57x | 45 |
| `AD-amplify-worst` | 6.33 | 1.86 | 3.40x | 45 |
| `DM-mode` | 11.1 | 3.27 | 3.40x | 45 |
| `RF-stretch-duct` | 6.19 | 1.84 | 3.37x | 45 |
| `SF-resolve` | 4.61 | 1.54 | 3.00x | 45 |
| `DG-loss` | 6.74 | 2.27 | 2.97x | 45 |
| `LD-diurnal` | 4.22 | 1.54 | 2.73x | 45 |
| `LD-traceroute` | 5.29 | 2.1 | 2.52x | 45 |
| `SF-jitter-global` | 4.18 | 1.77 | 2.37x | 45 |
| `SF-jitter-local` | 4.18 | 1.79 | 2.34x | 45 |
| `MS-size` | 7.71 | 3.39 | 2.27x | 45 |
| `SF-width` | 3.63 | 1.66 | 2.19x | 45 |
| `RF-pulse` | 3.43 | 1.63 | 2.10x | 45 |
| `LD-interval` | 2.31 | 1.27 | 1.81x | 45 |
| `MS-stretch` | 3.59 | 2.03 | 1.77x | 45 |
| `SF-signed` | 2.97 | 1.74 | 1.71x | 45 |
| `SC-signing` | 3.08 | 1.8 | 1.71x | 45 |
| `SF-bucket-time` | 2.5 | 1.57 | 1.60x | 45 |
| `SF-capacity` | 2.75 | 1.75 | 1.57x | 45 |
| `RF-preset-turbo` | 2.32 | 1.54 | 1.51x | 41 |
| `SF-capacity-window` | 2.41 | 1.6 | 1.50x | 45 |
| `LD-traceroute-small` | 23.8 | 37.8 | 0.63x | 45 |
| `MS-density` | 2.04 | 3.38 | 0.60x | 45 |
| `TH-congestion-input` | 5.4 | 11.2 | 0.48x | 45 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.939 | 0.939 | 0.783 → 0.784 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.920 | 0.920 | 0.781 → 0.784 | 1.1x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.098 → 0.920 | 0.822 | 0.043 → 0.781 | 11x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.119 → 0.920 | 0.800 | 0.068 → 0.781 | 8.2x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.112 → 0.858 | 0.746 | 0.094 → 0.723 | 1.4e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.194 → 0.896 | 0.703 | 0.088 → 0.757 | 9.4x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.103 → 0.793 | 0.690 | 0.102 → 0.781 | 4.8x sr_bytes | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.277 → 0.965 | 0.688 | 0.270 → 0.965 | 3.6x sr_airtime | up | 4 |
| `RF-bw500` | preset | **held** | 0.266 → 0.906 | 0.640 | 0.154 → 0.744 | 4.1x sr_bytes | up | 3 |
| `RF-preset` | preset | **text** | 0.321 → 0.795 | 0.475 | 0.306 → 0.782 | 2.3x sr_airtime | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.321 → 0.793 | 0.472 | 0.306 → 0.781 | 1.6x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.324 → 0.793 | 0.469 | 0.319 → 0.781 | 8.2x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.574 → 0.955 | 0.382 | 0.571 → 0.951 | 5.5x sr_airtime | up | 5 |
| `MS-oversubscribed` | nodes | **text** | 0.326 → 0.701 | 0.375 | 0.321 → 0.695 | 6x sr_bytes | down | 3 |
| `MS-topology` | topology | **text** | 0.569 → 0.943 | 0.374 | 0.547 → 0.942 | 2.2x sr_bytes | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.515 → 0.886 | 0.371 | 0.501 → 0.882 | 9x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.293 → 0.658 | 0.365 | 0.288 → 0.623 | 1.4x sr_bytes | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.470 → 0.793 | 0.323 | 0.450 → 0.781 | 1.5x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.641 → 0.955 | 0.314 | 0.503 → 0.822 | 9.7x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.482 → 0.793 | 0.310 | 0.457 → 0.781 | 1.6x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.597 → 0.890 | 0.293 | 0.563 → 0.886 | 2.1x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.511 → 0.775 | 0.263 | 0.299 → 0.504 | 5.2x sr_airtime | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.597 → 0.850 | 0.253 | 0.563 → 0.843 | 1.7x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.700 → 0.943 | 0.243 | 0.689 → 0.937 | 5.9x sr_airtime | down | 2 |
| `SF-place-flat` | place | **held** | 0.703 → 0.941 | 0.238 | 0.775 → 0.790 | 4x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.703 → 0.941 | 0.238 | 0.775 → 0.790 | 4x sr_bytes | up | 6 |
| `RF-noise` | noise-profile | **held** | 0.712 → 0.920 | 0.208 | 0.603 → 0.781 | 1.4x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.597 → 0.793 | 0.196 | 0.563 → 0.781 | 1.5x sr_bytes | up | 2 |
| `MS-size` | nodes | **text** | 0.640 → 0.799 | 0.159 | 0.624 → 0.783 | 5.9x sr_bytes | down | 5 |
| `AD-flooding` | role-mix | **text** | 0.766 → 0.898 | 0.132 | 0.757 → 0.897 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.766 → 0.898 | 0.132 | 0.757 → 0.897 | 2.3x bytes_on_air | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.667 → 0.793 | 0.125 | 0.655 → 0.781 | 1.3x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.724 → 0.844 | 0.120 | 0.715 → 0.840 | 2.4x sr_airtime | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.793 → 0.911 | 0.118 | 0.781 → 0.895 | 2.2x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.745 → 0.864 | 0.118 | 0.734 → 0.857 | 5.6x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.793 → 0.906 | 0.114 | 0.781 → 0.903 | 1.6x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.731 → 0.844 | 0.113 | 0.723 → 0.840 | 2.4x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.716 → 0.819 | 0.103 | 0.608 → 0.693 | 1.6x sr_airtime | down | 2 |
| `SC-signing` | signature-policy | **text** | 0.691 → 0.793 | 0.101 | 0.691 → 0.781 | 1.2x sr_airtime | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.793 → 0.888 | 0.095 | 0.781 → 0.877 | 1.5x sr_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.793 → 0.882 | 0.090 | 0.781 → 0.878 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.793 → 0.882 | 0.089 | 0.781 → 0.877 | 2x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.831 → 0.920 | 0.089 | 0.781 → 0.794 | 26x sr_airtime | down | 3 |
| `SF-capacity-window` | capacity | **held** | 0.834 → 0.922 | 0.088 | 0.787 → 0.791 | 4.1x sr_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.793 → 0.874 | 0.081 | 0.781 → 0.871 | 3.1x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.793 → 0.872 | 0.080 | 0.781 → 0.869 | 3.1x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.849 → 0.928 | 0.079 | 0.760 → 0.790 | 14x advert_bytes | up | 4 |
| `AD-badrouters` | role-placement | **text** | 0.712 → 0.788 | 0.076 | 0.705 → 0.778 | 1.2x sr_bytes | up | 3 |
| `SF-resolve` | resolve | **held** | 0.861 → 0.920 | 0.059 | 0.781 → 0.789 | 5.7x advert_bytes | up | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.870 → 0.928 | 0.058 | 0.774 → 0.782 | 9.2x advert_bytes | down | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.883 → 0.940 | 0.057 | 0.784 → 0.825 | 1.1x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.793 → 0.846 | 0.053 | 0.781 → 0.844 | 2.2x sr_bytes | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.793 → 0.843 | 0.050 | 0.781 → 0.835 | 3.3x bytes_on_air | down | 2 |
| `MS-roles` | role-mix | **text** | 0.766 → 0.816 | 0.049 | 0.757 → 0.809 | 1.2x bytes_on_air | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.750 → 0.797 | 0.047 | 0.739 → 0.788 | 1.5x sr_airtime | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.898 → 0.939 | 0.041 | 0.781 → 0.796 | 3.3x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.898 → 0.939 | 0.041 | 0.781 → 0.796 | 3.3x sr_bytes | down | 5 |
| `AD-worst` | role-placement | **text** | 0.790 → 0.826 | 0.037 | 0.775 → 0.820 | 1.9x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.765 → 0.800 | 0.035 | 0.498 → 0.531 | 1.4x sr_airtime | up | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.888 → 0.920 | 0.032 | 0.781 → 0.781 | 3.1x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.920 → 0.951 | 0.031 | 0.781 → 0.785 | 1.2x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.829 → 0.860 | 0.031 | 0.750 → 0.762 | 1.2x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.793 → 0.821 | 0.029 | 0.781 → 0.814 | 1.2x sr_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.893 → 0.920 | 0.027 | 0.778 → 0.790 | 16x sr_bytes | down | 4 |
| `SF-servers-spread` | servers | **held** | 0.893 → 0.920 | 0.027 | 0.778 → 0.790 | 16x sr_bytes | down | 4 |
| `DM-mode` | dm-mode | **held** | 0.837 → 0.860 | 0.023 | 0.746 → 0.762 | 1.1x sr_bytes | up | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.829 → 0.851 | 0.022 | 0.750 → 0.766 | 1.2x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.906 → 0.926 | 0.019 | 0.779 → 0.782 | 3x advert_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.917 → 0.935 | 0.018 | 0.787 → 0.798 | 1.5x sr_bytes | up | 4 |
| `SF-window-size` | window-size | **text** | 0.782 → 0.799 | 0.017 | 0.773 → 0.791 | 5.2x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **held** | 0.913 → 0.929 | 0.016 | 0.797 → 0.809 | 1.1x sr_bytes | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.905 → 0.920 | 0.015 | 0.779 → 0.786 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.905 → 0.920 | 0.015 | 0.779 → 0.786 | 1.1x sr_bytes | down | 4 |
| `SF-capacity` | capacity | **held** | 0.906 → 0.920 | 0.014 | 0.777 → 0.783 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.906 → 0.920 | 0.014 | 0.777 → 0.783 | 5.4x advert_bytes | up | 5 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.777 → 0.790 | 0.014 | 0.766 → 0.782 | 5.4x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.788 → 0.799 | 0.012 | 0.779 → 0.791 | 3.1x advert_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.920 → 0.929 | 0.009 | 0.781 → 0.788 | 2.2x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.793 → 0.802 | 0.009 | 0.781 → 0.794 | 1.1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.934 → 0.943 | 0.008 | 0.928 → 0.937 | 1.2x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.943 → 0.950 | 0.007 | 0.937 → 0.945 | 1.1x bytes_on_air | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.909 → 0.915 | 0.006 | 0.777 → 0.781 | 2.7x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.787 → 0.793 | 0.005 | 0.779 → 0.781 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.815 → 0.820 | 0.005 | 0.772 → 0.781 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.943 → 0.946 | 0.003 | 0.937 → 0.941 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| sprinkled | 1 | 0.807 | 0.800 | 0.008 | - | - | 0.928 | 0.931 | 0.310 | 1.26x | 15.5/22.9/28.5% | 1.8/5.5% | 3 |
| arms-race | 1 | 0.906 | 0.903 | 0.003 | - | - | 0.935 | 0.936 | 0.827 | 1.08x | 18.0/24.8/29.0% | 1.6/5.1% | 3 |

> amplifier-mix=none: decode_failures 3

> amplifier-mix=sprinkled: decode_failures 3

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.857 | 0.835 | 0.022 | - | - | 0.921 | 0.954 | 0.543 | 1.34x | 14.7/25.7/29.0% | 1.9/5.4% | 3 |
| 0.3 | 1 | 0.911 | 0.895 | 0.016 | - | - | 0.985 | 0.986 | 0.676 | 1.21x | 18.0/22.4/29.3% | 1.7/5.2% | 3 |

> amplify-worst=0.0: decode_failures 3

> amplify-worst=0.1: decode_failures 44

> slower: 6.33 s per simulated hour against 1.86 over 45 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.766 | 0.757 | 0.009 | - | - | 0.896 | 0.897 | 0.352 | 1.17x | 13.6/24.0/28.1% | 1.8/5.3% | 3 |
| inverse | 1 | 0.712 | 0.705 | 0.007 | - | - | 0.861 | 0.863 | 0.407 | 1.08x | 12.0/17.2/19.6% | 1.9/3.5% | 3 |
| random | 1 | 0.788 | 0.778 | 0.010 | - | - | 0.921 | 0.927 | 0.413 | 1.15x | 12.5/18.8/20.1% | 1.9/4.9% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.766 | 0.757 | 0.009 | - | - | 0.896 | 0.897 | 0.352 | 1.17x | 13.6/24.0/28.1% | 1.8/5.3% | 3 |
| all-routers | 1 | 0.898 | 0.897 | 0.001 | - | - | 0.961 | 0.962 | 0.724 | 2.73x | 26.6/39.5/41.6% | 4.4/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.766 | 0.757 | 0.009 | - | - | 0.896 | 0.897 | 0.352 | 1.17x | 13.6/24.0/28.1% | 1.8/5.3% | 3 |
| no-mute | 1 | 0.827 | 0.821 | 0.006 | - | - | 0.932 | 0.934 | 0.550 | 1.29x | 13.8/21.5/24.4% | 1.9/5.3% | 3 |
| all-routers | 1 | 0.898 | 0.897 | 0.001 | - | - | 0.961 | 0.962 | 0.724 | 2.73x | 26.6/39.5/41.6% | 4.4/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.766 | 0.757 | 0.009 | - | - | 0.896 | 0.897 | 0.352 | 1.17x | 13.6/24.0/28.1% | 1.8/5.3% | 3 |
| local-typical | 1 | 0.443 | 0.435 | 0.008 | - | - | 0.638 | 0.640 | 0.000 | 1.25x | 9.6/21.5/28.8% | 2.0/5.5% | 3 |
| basement-heavy | 1 | 0.089 | 0.088 | 0.000 | - | - | 0.194 | 0.274 | 0.000 | 0.64x | 1.1/12.6/19.3% | 0.4/3.9% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.826 | 0.820 | 0.006 | - | - | 0.936 | 0.936 | 0.000 | 2.36x | 17.9/28.4/39.3% | 1.8/5.8% | 3 |
| inverse | 1 | 0.790 | 0.775 | 0.014 | - | - | 0.929 | 0.936 | 0.000 | 2.19x | 15.3/25.3/32.7% | 1.7/3.2% | 3 |

> role-placement=inverse: decode_failures 61

> slower: 12.2 s per simulated hour against 3.41 over 45 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.784 | 0.784 | 0.000 | - | - | 0 | 0.000 | 0.215 | 1.32x | 13.1/23.6/26.5% | 2.0/5.2% | 3 |
| sr | 1 | 0.801 | 0.783 | 0.019 | - | - | 0.939 | 0.944 | 0.215 | 1.33x | 13.2/23.8/26.7% | 2.0/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.731 | 0.723 | 0.008 | - | - | 0.837 | 0.838 | 0.376 | 3.16x | 30.8/59.8/62.8% | 4.4/9.8% | 3 |
| 100 | 1 | 0.844 | 0.840 | 0.004 | - | - | 0.927 | 0.928 | 0.338 | 1.64x | 15.8/32.6/34.7% | 2.2/5.2% | 3 |
| 120 | 1 | 0.844 | 0.840 | 0.004 | - | - | 0.927 | 0.928 | 0.338 | 1.64x | 15.8/32.6/34.7% | 2.2/5.2% | 3 |
| 250 | 1 | 0.844 | 0.840 | 0.004 | - | - | 0.927 | 0.928 | 0.338 | 1.64x | 15.8/32.6/34.7% | 2.2/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.304 | 0.299 | 0.005 | - | - | 0.511 | 0.533 | 0.142 | 11.22x | 36.9/64.1/76.4% | 3.9/10.9% | 3 |
| 120 | 1 | 0.505 | 0.498 | 0.007 | - | - | 0.765 | 0.766 | 0.179 | 4.57x | 14.8/29.8/44.6% | 1.5/5.8% | 3 |
| 250 | 1 | 0.511 | 0.504 | 0.008 | - | - | 0.775 | 0.775 | 0.176 | 4.43x | 14.5/28.8/43.2% | 1.5/5.6% | 3 |

> max-num-nodes=10: decode_failures 99

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.844 | 0.840 | 0.004 | - | - | 0.927 | 0.928 | 0.338 | 1.64x | 15.8/32.6/34.7% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.844 | 0.840 | 0.004 | - | - | 0.927 | 0.928 | 0.338 | 1.64x | 15.8/32.6/34.7% | 2.2/5.2% | 3 |
| constrained | 1 | 0.724 | 0.715 | 0.009 | - | - | 0.825 | 0.827 | 0.343 | 3.15x | 30.7/59.5/62.5% | 4.4/9.8% | 3 |

> platform-mix=constrained: decode_failures 2

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.819 | 0.908 | 0.447 | 5.79x | 56.7/72.9/77.1% | 4.2/13.3% | 3 |
| 25 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.819 | 0.908 | 0.447 | 5.79x | 56.7/72.9/77.1% | 4.2/13.3% | 3 |
| 100 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.819 | 0.908 | 0.447 | 5.79x | 56.7/72.9/77.1% | 4.2/13.3% | 3 |
| 2000 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.819 | 0.908 | 0.447 | 5.79x | 56.7/72.9/77.1% | 4.2/13.3% | 3 |

> warm-num-nodes=0: queue drops 13.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 109

> warm-num-nodes=25: queue drops 13.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 109

> warm-num-nodes=100: queue drops 13.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 109

> warm-num-nodes=2000: queue drops 13.5% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 109

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.695 | 0.677 | 0.018 | - | - | 0.890 | 0.896 | 0.341 | 1.23x | 12.2/22.8/25.4% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.597 | 0.572 | 0.025 | - | - | 0.802 | 0.855 | 0.275 | 1.13x | 11.5/21.2/23.9% | 1.6/4.4% | 3 |
| 0.3 | 1 | 0.482 | 0.457 | 0.025 | - | - | 0.671 | 0.779 | 0.209 | 1.03x | 10.6/19.9/22.6% | 1.5/3.8% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 4

> burst-loss=0.2: decode_failures 32

> burst-loss=0.3: decode_failures 29

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.765 | 0.755 | 0.010 | - | - | 0.900 | 0.916 | 0.338 | 1.39x | 13.8/25.0/27.8% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.714 | 0.703 | 0.011 | - | - | 0.870 | 0.885 | 0.324 | 1.37x | 14.0/25.0/27.8% | 2.0/5.0% | 3 |
| 0.3 | 1 | 0.667 | 0.655 | 0.012 | - | - | 0.839 | 0.875 | 0.326 | 1.41x | 14.5/26.3/29.2% | 2.0/5.0% | 3 |

> extra-loss=0.0: decode_failures 3

> extra-loss=0.1: decode_failures 37

> extra-loss=0.2: decode_failures 15

> extra-loss=0.3: decode_failures 27

> slower: 6.74 s per simulated hour against 2.27 over 45 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.674 | 0.662 | 0.012 | - | - | 0.811 | 0.898 | 0.342 | 1.23x | 12.3/22.5/25.0% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.573 | 0.555 | 0.018 | - | - | 0.758 | 0.854 | 0.290 | 1.13x | 11.5/21.2/23.8% | 1.6/4.6% | 3 |
| 0.3 | 1 | 0.470 | 0.450 | 0.019 | - | - | 0.671 | 0.787 | 0.183 | 1.08x | 11.0/21.0/23.8% | 1.5/4.3% | 3 |

> burst-loss=0.0: decode_failures 3

> burst-loss=0.1: decode_failures 43

> burst-loss=0.2: decode_failures 23

> burst-loss=0.3: decode_failures 22

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.746 | 0.746 | 0.000 | - | - | 0.837 | 0.897 | 0.191 | 1.69x | 16.4/30.9/34.1% | 2.4/6.8% | 3 |
| directed-with-late-flood | 1 | 0.762 | 0.762 | 0.000 | - | - | 0.860 | 0.914 | 0.214 | 1.56x | 15.3/28.6/31.7% | 2.2/6.3% | 3 |
| m4-early-flood | 1 | 0.762 | 0.762 | 0.000 | - | - | 0.856 | 0.910 | 0.210 | 1.56x | 15.4/28.7/31.8% | 2.2/6.3% | 3 |

> dm-mode=flood-only: decode_failures 31

> dm-mode=directed-with-late-flood: decode_failures 34

> dm-mode=m4-early-flood: decode_failures 30

> slower: 11.1 s per simulated hour against 3.27 over 45 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.872 | 0.869 | 0.003 | - | - | 0.968 | 0.971 | 0.427 | 0.75x | 8.1/11.4/12.7% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> profile=2.8: decode_failures 3

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.944 | 0.947 | 0.410 | 1.25x | 14.0/21.7/25.1% | 1.9/4.7% | 3 |
| 0.5 | 1 | 0.882 | 0.877 | 0.004 | - | - | 0.979 | 0.980 | 0.542 | 1.00x | 11.2/18.1/22.2% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.851 | 0.844 | 0.007 | - | - | 0.972 | 0.976 | 0.494 | 0.95x | 10.6/16.3/18.6% | 1.5/3.7% | 3 |

> legacy-fraction=0.0: decode_failures 3

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.835 | 0.825 | 0.010 | - | - | 0.946 | 0.950 | 0.406 | 1.24x | 13.7/21.3/25.0% | 1.9/4.7% | 3 |
| 0.5 | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.980 | 0.982 | 0.518 | 1.00x | 11.6/18.2/22.3% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.853 | 0.846 | 0.007 | - | - | 0.975 | 0.977 | 0.465 | 0.91x | 10.2/15.5/18.0% | 1.4/3.6% | 3 |

> legacy-fraction=0.0: decode_failures 3

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.843 | 0.835 | 0.008 | - | - | 0.962 | 0.964 | 0.364 | 0.71x | 7.0/13.6/15.5% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> profile-flag=signing=true: decode_failures 3

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.874 | 0.871 | 0.003 | - | - | 0.967 | 0.969 | 0.411 | 0.78x | 8.6/12.8/14.6% | 1.2/2.6% | 3 |
| 2.5 | 1 | 0.862 | 0.859 | 0.003 | - | - | 0.956 | 0.956 | 0.489 | 0.78x | 8.6/12.7/14.3% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.866 | 0.863 | 0.003 | - | - | 0.960 | 0.961 | 0.459 | 0.76x | 8.6/12.8/14.9% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.873 | 0.870 | 0.003 | - | - | 0.966 | 0.968 | 0.416 | 0.78x | 8.6/13.6/15.8% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> profile=2.8: decode_failures 3

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.830 | 0.822 | 0.008 | - | - | 0.955 | 0.956 | 0.396 | 0.91x | 8.9/16.3/18.1% | 1.4/3.7% | 3 |
| 900 | 1 | 0.745 | 0.734 | 0.012 | - | - | 0.885 | 0.904 | 0.349 | 2.07x | 20.6/37.2/40.9% | 3.0/8.1% | 3 |
| 300 | 1 | 0.517 | 0.503 | 0.014 | - | - | 0.641 | 0.735 | 0.276 | 4.38x | 43.0/70.8/74.7% | 6.3/16.3% | 3 |

> broadcast-interval-s=900: decode_failures 11

> broadcast-interval-s=300: decode_failures 13

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.886 | 0.882 | 0.003 | - | - | 0.970 | 0.971 | 0.369 | 1.00x | 10.0/16.7/18.5% | 1.5/3.7% | 3 |
| 900 | 1 | 0.805 | 0.798 | 0.008 | - | - | 0.916 | 0.917 | 0.363 | 2.32x | 23.5/38.8/42.7% | 3.4/8.3% | 3 |
| 300 | 1 | 0.515 | 0.501 | 0.014 | - | - | 0.636 | 0.709 | 0.293 | 5.01x | 49.3/73.3/76.3% | 7.5/17.1% | 3 |

> broadcast-interval-s=300: decode_failures 17

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.821 | 0.814 | 0.008 | - | - | 0.946 | 0.947 | 0.364 | 1.26x | 12.5/22.8/25.4% | 1.9/5.1% | 3 |
| sinusoid | 1 | 0.803 | 0.795 | 0.008 | - | - | 0.920 | 0.934 | 0.348 | 1.23x | 12.1/22.0/24.6% | 1.8/4.9% | 3 |
| commuter | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> diurnal=flat: decode_failures 1

> diurnal=sinusoid: decode_failures 32

> diurnal=commuter: decode_failures 3

> slower: 4.22 s per simulated hour against 1.54 over 45 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.745 | 0.734 | 0.012 | - | - | 0.885 | 0.904 | 0.349 | 2.07x | 20.6/37.2/40.9% | 3.0/8.1% | 3 |
| 3600 | 1 | 0.830 | 0.822 | 0.008 | - | - | 0.955 | 0.956 | 0.396 | 0.91x | 8.9/16.3/18.1% | 1.4/3.7% | 3 |
| 10800 | 1 | 0.856 | 0.849 | 0.007 | - | - | 0.964 | 0.967 | 0.353 | 0.61x | 6.0/10.8/12.0% | 0.9/2.5% | 3 |
| 43200 | 1 | 0.864 | 0.857 | 0.006 | - | - | 0.970 | 0.972 | 0.368 | 0.42x | 4.1/7.5/8.3% | 0.6/1.8% | 3 |

> broadcast-interval-s=900: decode_failures 11

> broadcast-interval-s=43200: decode_failures 1

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.797 | 0.788 | 0.009 | - | - | 0.927 | 0.931 | 0.358 | 1.38x | 13.6/25.1/28.0% | 2.0/5.7% | 3 |
| 1.0 | 1 | 0.773 | 0.761 | 0.011 | - | - | 0.906 | 0.915 | 0.386 | 1.50x | 15.0/27.4/30.5% | 2.2/6.1% | 3 |
| 4.0 | 1 | 0.750 | 0.739 | 0.011 | - | - | 0.886 | 0.905 | 0.366 | 1.86x | 19.1/34.3/38.5% | 2.7/7.5% | 3 |

> traceroute-per-hour=0.0: decode_failures 3

> traceroute-per-hour=1.0: decode_failures 7

> traceroute-per-hour=4.0: decode_failures 31

> slower: 5.29 s per simulated hour against 2.1 over 45 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.819 | 0.908 | 0.447 | 5.79x | 56.7/72.9/77.1% | 4.2/13.3% | 3 |
| 1.0 | 1 | 0.615 | 0.608 | 0.007 | - | - | 0.716 | 0.858 | 0.378 | 6.38x | 61.2/75.1/78.6% | 4.7/14.2% | 3 |

> traceroute-per-hour=0.0: queue drops 13.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 109

> traceroute-per-hour=1.0: queue drops 20.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 84

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.574 | 0.571 | 0.003 | - | - | 0.733 | 0.738 | 0.248 | 1.29x | 13.9/24.5/29.0% | 3.2/6.0% | 3 |
| 60 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 90 | 1 | 0.919 | 0.914 | 0.005 | - | - | 0.993 | 0.995 | 0.593 | 1.62x | 17.9/27.7/31.3% | 1.5/4.9% | 3 |
| 120 | 1 | 0.943 | 0.937 | 0.006 | - | - | 0.996 | 0.997 | 0.689 | 2.01x | 21.5/32.6/35.9% | 1.4/5.2% | 3 |
| 150 | 1 | 0.955 | 0.951 | 0.005 | - | - | 1.000 | 1.000 | 0.817 | 2.56x | 25.9/37.7/42.7% | 1.3/5.7% | 3 |

> nodes=60: decode_failures 3

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 120 | 1 | 0.699 | 0.693 | 0.006 | - | - | 0.816 | 0.816 | 0.118 | 2.19x | 13.5/28.9/35.3% | 1.5/4.6% | 3 |
| 250 | 1 | 0.506 | 0.499 | 0.007 | - | - | 0.764 | 0.765 | 0.185 | 4.74x | 15.5/30.8/46.2% | 1.6/6.0% | 3 |
| 500 | 1 | 0.324 | 0.319 | 0.005 | - | - | 0.478 | 0.504 | 0.090 | 10.05x | 18.3/29.2/53.3% | 1.7/6.6% | 3 |

> nodes=60: decode_failures 3

> nodes=250: decode_failures 4

> nodes=500: decode_failures 166

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.701 | 0.695 | 0.006 | - | - | 0.829 | 0.830 | 0.101 | 2.07x | 12.8/27.9/34.0% | 1.4/4.4% | 3 |
| 250 | 1 | 0.505 | 0.498 | 0.007 | - | - | 0.765 | 0.766 | 0.179 | 4.57x | 14.8/29.8/44.6% | 1.5/5.8% | 3 |
| 500 | 1 | 0.326 | 0.321 | 0.005 | - | - | 0.488 | 0.517 | 0.097 | 9.37x | 16.9/27.6/50.8% | 1.6/6.1% | 3 |

> nodes=500: decode_failures 98

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.816 | 0.809 | 0.006 | - | - | 0.935 | 0.937 | 0.364 | 1.35x | 13.1/24.4/26.9% | 2.0/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.766 | 0.757 | 0.009 | - | - | 0.896 | 0.897 | 0.352 | 1.17x | 13.6/24.0/28.1% | 1.8/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.831 | 0.825 | 0.006 | - | - | 0.940 | 0.943 | 0.330 | 1.41x | 14.1/25.1/27.5% | 2.1/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.791 | 0.784 | 0.007 | - | - | 0.883 | 0.884 | 0.427 | 1.32x | 14.9/27.3/31.6% | 2.2/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.05 | 1 | 0.802 | 0.797 | 0.005 | - | - | 0.916 | 0.919 | 0.265 | 1.44x | 14.7/29.3/31.2% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.800 | 0.794 | 0.006 | - | - | 0.911 | 0.912 | 0.296 | 1.60x | 15.8/35.1/38.3% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.846 | 0.844 | 0.002 | - | - | 0.913 | 0.913 | 0.573 | 1.80x | 17.6/37.6/41.1% | 2.3/5.0% | 3 |

> router-late-fraction=0.0: decode_failures 3

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| local-typical | 1 | 0.508 | 0.503 | 0.006 | - | - | 0.702 | 0.704 | 0.000 | 1.53x | 10.9/23.0/31.1% | 2.5/5.3% | 3 |
| event | 1 | 0.277 | 0.270 | 0.007 | - | - | 0.511 | 0.515 | 0.000 | 1.34x | 6.9/14.9/23.4% | 2.1/4.9% | 3 |
| backbone | 1 | 0.965 | 0.965 | 0.000 | - | - | 0.989 | 0.990 | 0.854 | 1.28x | 21.5/30.3/34.3% | 1.7/5.6% | 3 |

> siting-mix=uniform: decode_failures 3

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.799 | 0.783 | 0.016 | - | - | 0.909 | 0.937 | 0.516 | 1.42x | 21.1/32.4/34.3% | 3.5/7.4% | 3 |
| 60 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 90 | 1 | 0.778 | 0.763 | 0.015 | - | - | 0.907 | 0.909 | 0.415 | 1.68x | 14.6/25.4/29.7% | 1.4/5.4% | 3 |
| 120 | 1 | 0.699 | 0.693 | 0.006 | - | - | 0.816 | 0.816 | 0.118 | 2.19x | 13.5/28.9/35.3% | 1.5/4.6% | 3 |
| 150 | 1 | 0.640 | 0.624 | 0.017 | - | - | 0.862 | 0.872 | 0.333 | 2.69x | 13.4/31.1/36.4% | 1.4/6.0% | 3 |

> nodes=40: decode_failures 23

> nodes=60: decode_failures 3

> nodes=150: decode_failures 88

> slower: 7.71 s per simulated hour against 3.39 over 45 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 1.25 | 1 | 0.598 | 0.588 | 0.010 | - | - | 0.863 | 0.866 | 0.264 | 1.31x | 10.6/20.7/24.6% | 1.9/5.5% | 3 |
| 1.5 | 1 | 0.293 | 0.288 | 0.006 | - | - | 0.626 | 0.649 | 0.000 | 1.11x | 7.0/14.9/19.7% | 1.5/5.5% | 3 |
| 2.0 | 1 | 0.103 | 0.102 | 0.001 | - | - | 0.261 | 0.264 | 0.000 | 0.82x | 3.1/9.1/15.1% | 1.0/3.8% | 3 |

> stretch=1.0: decode_failures 3

> stretch=1.25: decode_failures 3

> stretch=1.5: decode_failures 33

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| clustered | 1 | 0.905 | 0.899 | 0.005 | - | - | 0.925 | 0.981 | 0.341 | 1.12x | 22.3/28.3/30.5% | 1.5/5.5% | 3 |
| corridor | 1 | 0.569 | 0.547 | 0.022 | - | - | 0.667 | 0.669 | 0.337 | 1.24x | 15.6/22.1/25.6% | 1.8/5.6% | 3 |
| hub | 1 | 0.943 | 0.942 | 0.001 | - | - | 0.993 | 0.993 | 0.416 | 1.14x | 24.5/36.0/37.8% | 1.5/5.7% | 3 |

> topology=uniform: decode_failures 3

> topology=clustered: decode_failures 5

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.762 | 0.762 | 0.000 | - | - | 0.860 | 0.914 | 0.214 | 1.56x | 15.3/28.6/31.7% | 2.2/6.3% | 3 |
| True | 1 | 0.750 | 0.750 | 0.000 | - | - | 0.829 | 0.898 | 0.219 | 1.54x | 15.3/28.1/31.4% | 2.2/6.3% | 3 |

> coding-rate-ladder=False: decode_failures 34

> coding-rate-ladder=True: decode_failures 33

> slower: 11.6 s per simulated hour against 2.79 over 45 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.750 | 0.750 | 0.000 | - | - | 0.829 | 0.898 | 0.219 | 1.54x | 15.3/28.1/31.4% | 2.2/6.3% | 3 |
| m4-early-flood | 1 | 0.766 | 0.766 | 0.000 | - | - | 0.851 | 0.924 | 0.190 | 1.57x | 15.5/28.9/32.1% | 2.2/6.4% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 33

> dm-mode=m4-early-flood: decode_failures 31

> slower: 11.1 s per simulated hour against 2.77 over 45 prior run(s) - 4.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.784 | 0.784 | 0.000 | - | - | 0 | 0.000 | 0.215 | 1.32x | 13.1/23.6/26.5% | 2.0/5.2% | 3 |
| chain | 1 | 0.785 | 0.782 | 0.003 | - | - | 0.847 | 0.931 | 0.299 | 1.47x | 14.2/27.2/30.1% | 2.1/6.0% | 3 |
| sr | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> protocol=sr: decode_failures 3

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| True | 1 | 0.802 | 0.794 | 0.008 | - | - | 0.919 | 0.922 | 0.333 | 1.33x | 13.1/23.9/26.6% | 2.0/5.4% | 3 |

> extra-repeats=False: decode_failures 3

> extra-repeats=True: decode_failures 2

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.937 | 0.006 | - | - | 0.996 | 0.997 | 0.689 | 2.01x | 21.5/32.6/35.9% | 1.4/5.2% | 3 |
| True | 1 | 0.946 | 0.941 | 0.006 | - | - | 0.997 | 0.998 | 0.707 | 2.05x | 21.9/33.1/36.4% | 1.4/5.3% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.157 | 0.154 | 0.003 | - | - | 0.266 | 0.311 | 0.000 | 0.05x | 0.2/0.5/0.7% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.372 | 0.350 | 0.023 | - | - | 0.582 | 0.612 | 0.004 | 0.26x | 1.5/4.7/5.8% | 0.3/1.1% | 3 |
| LONG_TURBO | 1 | 0.753 | 0.744 | 0.009 | - | - | 0.906 | 0.907 | 0.406 | 1.25x | 11.9/20.5/24.1% | 1.9/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 8

> preset=MEDIUM_TURBO: decode_failures 23

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.814 | 0.801 | 0.012 | - | - | 0.933 | 0.941 | 0.423 | 1.31x | 13.8/24.8/27.7% | 1.9/5.4% | 3 |
| 1.0 | 1 | 0.888 | 0.877 | 0.011 | - | - | 0.962 | 0.964 | 0.657 | 1.20x | 18.6/29.5/32.2% | 1.6/5.5% | 3 |

> duct-per-hour=0.0: decode_failures 3

> duct-per-hour=0.25: decode_failures 3

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.321 | 0.306 | 0.014 | - | - | 0.694 | 0.698 | 0.000 | 0.15x | 0.8/2.2/3.1% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| LITE_FAST | 1 | 0.751 | 0.742 | 0.009 | - | - | 0.936 | 0.941 | 0.237 | 1.00x | 10.1/18.5/20.5% | 1.5/4.2% | 3 |
| NARROW_SLOW | 1 | 0.746 | 0.736 | 0.010 | - | - | 0.909 | 0.913 | 0.249 | 1.25x | 13.3/23.1/25.0% | 1.9/5.3% | 3 |

> preset=LONG_FAST: decode_failures 3

> preset=NARROW_SLOW: decode_failures 1

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| temporal | 1 | 0.706 | 0.697 | 0.009 | - | - | 0.843 | 0.881 | 0.325 | 1.31x | 12.9/24.4/27.3% | 1.9/5.2% | 3 |
| transient | 1 | 0.777 | 0.767 | 0.010 | - | - | 0.908 | 0.915 | 0.356 | 1.31x | 12.8/23.8/26.6% | 1.9/5.3% | 3 |
| periodic | 1 | 0.611 | 0.603 | 0.008 | - | - | 0.712 | 0.739 | 0.251 | 1.22x | 12.2/22.0/24.3% | 1.8/4.7% | 3 |

> noise-profile=none: decode_failures 3

> noise-profile=temporal: decode_failures 31

> noise-profile=transient: decode_failures 3

> noise-profile=periodic: decode_failures 26

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.321 | 0.306 | 0.014 | - | - | 0.694 | 0.698 | 0.000 | 0.15x | 0.8/2.2/3.1% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| LONG_MODERATE | 1 | 0.795 | 0.782 | 0.013 | - | - | 0.892 | 0.896 | 0.538 | 3.45x | 39.8/59.6/64.7% | 4.7/12.0% | 3 |

> preset=LONG_FAST: decode_failures 3

> preset=LONG_MODERATE: decode_failures 3

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.044 | 0.043 | 0.001 | - | - | 0.098 | 0.103 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.157 | 0.154 | 0.003 | - | - | 0.266 | 0.311 | 0.000 | 0.05x | 0.2/0.5/0.7% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| LONG_TURBO | 1 | 0.753 | 0.744 | 0.009 | - | - | 0.906 | 0.907 | 0.406 | 1.25x | 11.9/20.5/24.1% | 1.9/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.777 | 0.767 | 0.010 | - | - | 0.909 | 0.911 | 0.304 | 1.82x | 18.2/30.8/32.0% | 2.6/7.1% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 6

> preset=SHORT_TURBO: decode_failures 8

> preset=LONG_FAST: decode_failures 3

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.733 | 0.723 | 0.009 | - | - | 0.858 | 0.861 | 0.357 | 1.29x | 12.9/23.4/26.1% | 1.9/5.1% | 3 |
| 10000 | 1 | 0.611 | 0.603 | 0.008 | - | - | 0.712 | 0.739 | 0.251 | 1.22x | 12.2/22.0/24.3% | 1.8/4.7% | 3 |
| 4000 | 1 | 0.384 | 0.380 | 0.004 | - | - | 0.458 | 0.500 | 0.196 | 1.03x | 10.7/18.9/21.2% | 1.5/3.5% | 3 |
| 2000 | 1 | 0.094 | 0.094 | 0.000 | - | - | 0.112 | 0.172 | 0.026 | 0.72x | 7.7/13.4/15.5% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 3

> noise-pulse-interval-ms=10000: decode_failures 26

> noise-pulse-interval-ms=4000: decode_failures 3

> slower: 3.43 s per simulated hour against 1.63 over 45 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.293 | 0.288 | 0.006 | - | - | 0.626 | 0.649 | 0.000 | 1.11x | 7.0/14.9/19.7% | 1.5/5.5% | 3 |
| 1.0 | 1 | 0.658 | 0.623 | 0.036 | - | - | 0.829 | 0.834 | 0.459 | 1.05x | 14.2/21.9/26.1% | 1.5/5.1% | 3 |

> duct-per-hour=0.0: decode_failures 33

> duct-per-hour=1.0: decode_failures 1

> slower: 6.19 s per simulated hour against 1.84 over 45 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 22 | 1 | 0.343 | 0.324 | 0.018 | - | - | 0.517 | 0.551 | 0.003 | 1.29x | 8.1/20.0/25.3% | 1.9/4.8% | 3 |
| 17 | 1 | 0.153 | 0.150 | 0.003 | - | - | 0.262 | 0.291 | 0.000 | 0.99x | 4.8/8.4/13.9% | 1.6/3.8% | 3 |
| 14 | 1 | 0.069 | 0.068 | 0.000 | - | - | 0.119 | 0.120 | 0.000 | 0.65x | 2.6/6.2/10.1% | 1.0/2.8% | 3 |

> tx-power=30: decode_failures 3

> tx-power=22: decode_failures 17

> tx-power=17: decode_failures 6

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.937 | 0.006 | - | - | 0.996 | 0.997 | 0.689 | 2.01x | 21.5/32.6/35.9% | 1.4/5.2% | 3 |
| True | 1 | 0.934 | 0.928 | 0.007 | - | - | 0.995 | 0.995 | 0.664 | 2.37x | 25.3/36.6/40.3% | 1.7/5.9% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.803 | 0.797 | 0.006 | - | - | 0.929 | 0.930 | 0.183 | 1.42x | 14.5/26.8/29.3% | 2.0/5.4% | 3 |
| True | 1 | 0.814 | 0.809 | 0.005 | - | - | 0.913 | 0.913 | 0.177 | 1.48x | 15.6/27.0/29.3% | 2.0/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| random | 1 | 0.796 | 0.785 | 0.011 | - | - | 0.951 | 0.953 | 0.368 | 1.33x | 13.0/23.9/26.4% | 1.9/5.2% | 3 |

> hop-assign=centrality: decode_failures 3

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.597 | 0.563 | 0.034 | - | - | 0.865 | 0.871 | 0.265 | 1.00x | 9.8/20.2/22.3% | 1.4/4.6% | 3 |
| 7 | 1 | 0.850 | 0.843 | 0.006 | - | - | 0.950 | 0.950 | 0.410 | 1.46x | 14.4/24.8/27.2% | 2.1/5.4% | 3 |
| 15 | 1 | 0.883 | 0.879 | 0.004 | - | - | 0.948 | 0.949 | 0.345 | 1.50x | 15.1/25.2/27.7% | 2.2/5.5% | 3 |
| 32 | 1 | 0.890 | 0.886 | 0.003 | - | - | 0.955 | 0.957 | 0.363 | 1.55x | 15.5/25.8/28.4% | 2.3/5.6% | 3 |

> hop-limit=3: decode_failures 4

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.597 | 0.563 | 0.034 | - | - | 0.865 | 0.871 | 0.265 | 1.00x | 9.8/20.2/22.3% | 1.4/4.6% | 3 |
| 5 | 1 | 0.779 | 0.770 | 0.009 | - | - | 0.941 | 0.941 | 0.354 | 1.30x | 12.7/23.4/26.1% | 1.9/5.3% | 3 |
| 7 | 1 | 0.850 | 0.843 | 0.006 | - | - | 0.950 | 0.950 | 0.410 | 1.46x | 14.4/24.8/27.2% | 2.1/5.4% | 3 |

> hop-limit=3: decode_failures 4

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.794 | 0.794 | 0.000 | - | - | 0.831 | 0.935 | 0.200 | 1.29x | 12.9/23.2/26.0% | 1.9/5.1% | 3 |

> rebroadcast-mode=ALL: decode_failures 3

> rebroadcast-mode=KNOWN_ONLY: decode_failures 3

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.597 | 0.563 | 0.034 | - | - | 0.865 | 0.871 | 0.265 | 1.00x | 9.8/20.2/22.3% | 1.4/4.6% | 3 |
| True | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> hop-spread=False: decode_failures 4

> hop-spread=True: decode_failures 3

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| BALANCED | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| STRICT | 1 | 0.691 | 0.691 | 0.000 | - | - | 0.840 | 0.844 | 0.091 | 1.46x | 14.5/26.0/29.0% | 2.1/5.8% | 3 |

> signature-policy=COMPATIBLE: decode_failures 3

> signature-policy=BALANCED: decode_failures 3

> signature-policy=STRICT: decode_failures 4

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| dm | 1 | 0.798 | 0.788 | 0.009 | - | - | 0.929 | 0.930 | 0.364 | 1.31x | 12.8/23.8/26.6% | 1.9/5.4% | 3 |

> advert-transport=broadcast: decode_failures 3

> advert-transport=dm: decode_failures 1

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.789 | 0.779 | 0.010 | - | - | 0.910 | 0.917 | 0.399 | 1.34x | 13.2/24.2/27.0% | 2.0/5.5% | 3 |
| local | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| time | 1 | 0.788 | 0.779 | 0.009 | - | - | 0.919 | 0.926 | 0.367 | 1.34x | 13.0/24.3/26.8% | 2.0/5.5% | 3 |
| window | 1 | 0.799 | 0.791 | 0.008 | - | - | 0.922 | 0.939 | 0.347 | 1.33x | 13.1/23.9/26.7% | 1.9/5.3% | 3 |

> bucket-mode=global: misdecodes 18

> bucket-mode=local: decode_failures 3

> bucket-mode=time: misdecodes 19

> bucket-mode=window: misdecodes 12

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.777 | 0.766 | 0.010 | - | - | 0.908 | 0.914 | 0.366 | 1.46x | 14.1/26.7/29.2% | 2.1/6.0% | 3 |
| 1800 | 1 | 0.788 | 0.779 | 0.009 | - | - | 0.919 | 0.926 | 0.367 | 1.34x | 13.0/24.3/26.8% | 2.0/5.5% | 3 |
| 3600 | 1 | 0.790 | 0.782 | 0.008 | - | - | 0.912 | 0.924 | 0.352 | 1.33x | 13.2/23.9/26.7% | 1.9/5.3% | 3 |

> time-bucket-s=600: misdecodes 74

> time-bucket-s=1800: misdecodes 19

> time-bucket-s=3600: misdecodes 8

> time-bucket-s=3600: decode_failures 6

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| interval | 1 | 0.772 | 0.760 | 0.012 | - | - | 0.908 | 0.915 | 0.395 | 1.71x | 16.2/32.6/35.4% | 2.4/7.7% | 3 |
| aimd | 1 | 0.794 | 0.790 | 0.003 | - | - | 0.849 | 0.933 | 0.282 | 1.33x | 13.0/24.3/26.9% | 2.0/5.4% | 3 |
| bucket+interval | 1 | 0.786 | 0.774 | 0.012 | - | - | 0.928 | 0.929 | 0.375 | 1.73x | 16.5/33.0/36.0% | 2.4/7.7% | 3 |

> trigger=bucket: decode_failures 3

> trigger=interval: misdecodes 6

> trigger=interval: decode_failures 9

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 22

> trigger=bucket+interval: misdecodes 10

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.793 | 0.783 | 0.010 | - | - | 0.906 | 0.935 | 0.352 | 1.31x | 12.9/23.8/26.3% | 1.9/5.3% | 3 |
| 8 | 1 | 0.791 | 0.781 | 0.009 | - | - | 0.914 | 0.927 | 0.350 | 1.32x | 13.0/23.8/26.4% | 1.9/5.3% | 3 |
| 16 | 1 | 0.785 | 0.777 | 0.008 | - | - | 0.906 | 0.922 | 0.321 | 1.34x | 13.3/24.2/27.0% | 1.9/5.5% | 3 |
| 32 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 50 | 1 | 0.793 | 0.783 | 0.009 | - | - | 0.920 | 0.927 | 0.357 | 1.33x | 13.1/24.1/26.7% | 1.9/5.4% | 3 |

> capacity=4: decode_failures 71

> capacity=8: decode_failures 52

> capacity=16: decode_failures 49

> capacity=32: decode_failures 3

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.793 | 0.783 | 0.010 | - | - | 0.906 | 0.935 | 0.352 | 1.31x | 12.9/23.8/26.3% | 1.9/5.3% | 3 |
| 8 | 1 | 0.791 | 0.781 | 0.009 | - | - | 0.914 | 0.927 | 0.350 | 1.32x | 13.0/23.8/26.4% | 1.9/5.3% | 3 |
| 16 | 1 | 0.785 | 0.777 | 0.008 | - | - | 0.906 | 0.922 | 0.321 | 1.34x | 13.3/24.2/27.0% | 1.9/5.5% | 3 |
| 32 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 50 | 1 | 0.793 | 0.783 | 0.009 | - | - | 0.920 | 0.927 | 0.357 | 1.33x | 13.1/24.1/26.7% | 1.9/5.4% | 3 |

> capacity=4: decode_failures 71

> capacity=8: decode_failures 52

> capacity=16: decode_failures 49

> capacity=32: decode_failures 3

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.790 | 0.787 | 0.003 | - | - | 0.834 | 0.928 | 0.221 | 1.30x | 13.0/23.4/26.2% | 1.9/5.2% | 3 |
| 16 | 1 | 0.793 | 0.787 | 0.006 | - | - | 0.870 | 0.922 | 0.303 | 1.31x | 13.0/23.7/26.4% | 1.9/5.3% | 3 |
| 32 | 1 | 0.799 | 0.791 | 0.008 | - | - | 0.922 | 0.939 | 0.347 | 1.33x | 13.1/23.9/26.7% | 1.9/5.3% | 3 |

> capacity=8: misdecodes 3

> capacity=8: decode_failures 78

> capacity=16: misdecodes 17

> capacity=16: decode_failures 33

> capacity=32: misdecodes 12

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.786 | 0.774 | 0.012 | - | - | 0.928 | 0.929 | 0.375 | 1.73x | 16.5/33.0/36.0% | 2.4/7.7% | 3 |
| 02-06 | 1 | 0.787 | 0.782 | 0.006 | - | - | 0.870 | 0.929 | 0.300 | 1.35x | 13.1/24.7/27.2% | 2.0/5.6% | 3 |
| 00-08 | 1 | 0.789 | 0.782 | 0.007 | - | - | 0.881 | 0.930 | 0.323 | 1.41x | 13.5/26.0/28.4% | 2.1/6.0% | 3 |

> catch-up-hours=: misdecodes 10

> catch-up-hours=02-06: decode_failures 48

> catch-up-hours=00-08: decode_failures 45

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.788 | 0.787 | 0.001 | - | - | 0.911 | 0.913 | 0.202 | 1.34x | 13.3/23.9/26.8% | 2.0/5.3% | 3 |
| 2 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 3 | 1 | 0.801 | 0.783 | 0.019 | - | - | 0.939 | 0.944 | 0.215 | 1.33x | 13.2/23.8/26.7% | 2.0/5.4% | 3 |
| 4 | 1 | 0.819 | 0.796 | 0.023 | - | - | 0.898 | 0.947 | 0.213 | 1.35x | 13.8/24.0/27.1% | 2.0/5.4% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=4: decode_failures 25

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.788 | 0.787 | 0.001 | - | - | 0.911 | 0.913 | 0.202 | 1.34x | 13.3/23.9/26.8% | 2.0/5.3% | 3 |
| 2 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 3 | 1 | 0.801 | 0.783 | 0.019 | - | - | 0.939 | 0.944 | 0.215 | 1.33x | 13.2/23.8/26.7% | 2.0/5.4% | 3 |
| 4 | 1 | 0.819 | 0.796 | 0.023 | - | - | 0.898 | 0.947 | 0.213 | 1.35x | 13.8/24.0/27.1% | 2.0/5.4% | 3 |
| 5 | 1 | 0.819 | 0.796 | 0.023 | - | - | 0.898 | 0.947 | 0.213 | 1.35x | 13.8/24.0/27.1% | 2.0/5.4% | 3 |

> hops-apart=2: decode_failures 3

> hops-apart=4: decode_failures 25

> hops-apart=5: decode_failures 25

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.788 | 0.779 | 0.009 | - | - | 0.919 | 0.922 | 0.370 | 1.34x | 13.0/24.1/26.8% | 1.9/5.4% | 3 |
| 30 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 120 | 1 | 0.792 | 0.784 | 0.008 | - | - | 0.917 | 0.922 | 0.346 | 1.32x | 13.0/23.8/26.5% | 2.0/5.3% | 3 |
| 600 | 1 | 0.795 | 0.786 | 0.008 | - | - | 0.905 | 0.922 | 0.342 | 1.32x | 12.9/24.0/26.5% | 1.9/5.4% | 3 |

> advert-jitter-s=1: decode_failures 2

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 2

> advert-jitter-s=600: decode_failures 24

> slower: 4.18 s per simulated hour against 1.77 over 45 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.788 | 0.779 | 0.009 | - | - | 0.919 | 0.922 | 0.370 | 1.34x | 13.0/24.1/26.8% | 1.9/5.4% | 3 |
| 30 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 120 | 1 | 0.792 | 0.784 | 0.008 | - | - | 0.917 | 0.922 | 0.346 | 1.32x | 13.0/23.8/26.5% | 2.0/5.3% | 3 |
| 600 | 1 | 0.795 | 0.786 | 0.008 | - | - | 0.905 | 0.922 | 0.342 | 1.32x | 12.9/24.0/26.5% | 1.9/5.4% | 3 |

> advert-jitter-s=1: decode_failures 2

> advert-jitter-s=30: decode_failures 3

> advert-jitter-s=120: decode_failures 2

> advert-jitter-s=600: decode_failures 24

> slower: 4.18 s per simulated hour against 1.79 over 45 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.798 | 0.775 | 0.023 | - | - | 0.703 | 0.886 | 0.196 | 1.35x | 13.8/23.8/26.9% | 2.0/5.3% | 3 |
| routers | 1 | 0.782 | 0.781 | 0.001 | - | - | 0.909 | 0.909 | 0.209 | 1.33x | 13.1/23.9/26.7% | 2.0/5.3% | 3 |
| alternate-routers | 1 | 0.791 | 0.790 | 0.001 | - | - | 0.919 | 0.921 | 0.212 | 1.33x | 13.2/23.7/26.6% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.791 | 0.788 | 0.003 | - | - | 0.931 | 0.931 | 0.236 | 1.33x | 13.1/24.0/26.7% | 2.0/5.3% | 3 |
| random-clients | 1 | 0.818 | 0.787 | 0.031 | - | - | 0.941 | 0.947 | 0.219 | 1.35x | 13.5/23.9/26.8% | 2.0/5.3% | 3 |
| hops-apart | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> place=spread: decode_failures 30

> place=hops-apart: decode_failures 3

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.798 | 0.775 | 0.023 | - | - | 0.703 | 0.886 | 0.196 | 1.35x | 13.8/23.8/26.9% | 2.0/5.3% | 3 |
| routers | 1 | 0.782 | 0.781 | 0.001 | - | - | 0.909 | 0.909 | 0.209 | 1.33x | 13.1/23.9/26.7% | 2.0/5.3% | 3 |
| alternate-routers | 1 | 0.791 | 0.790 | 0.001 | - | - | 0.919 | 0.921 | 0.212 | 1.33x | 13.2/23.7/26.6% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.791 | 0.788 | 0.003 | - | - | 0.931 | 0.931 | 0.236 | 1.33x | 13.1/24.0/26.7% | 2.0/5.3% | 3 |
| random-clients | 1 | 0.818 | 0.787 | 0.031 | - | - | 0.941 | 0.947 | 0.219 | 1.35x | 13.5/23.9/26.8% | 2.0/5.3% | 3 |
| hops-apart | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> place=spread: decode_failures 30

> place=hops-apart: decode_failures 3

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| broadcast | 1 | 0.820 | 0.781 | 0.039 | - | - | 0.888 | 0.922 | 0.316 | 1.40x | 13.6/25.3/28.0% | 2.1/5.6% | 3 |

> provide-transport=dm: decode_failures 3

> provide-transport=broadcast: decode_failures 37

> slower: 7.28 s per simulated hour against 1.75 over 45 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| heard | 1 | 0.787 | 0.779 | 0.009 | - | - | 0.918 | 0.919 | 0.349 | 1.33x | 13.1/24.2/26.9% | 1.9/5.4% | 3 |

> replay-ordering=tip: decode_failures 3

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.820 | 0.781 | 0.039 | - | - | 0.888 | 0.922 | 0.316 | 1.40x | 13.6/25.3/28.0% | 2.1/5.6% | 3 |
| heard | 1 | 0.815 | 0.772 | 0.043 | - | - | 0.886 | 0.913 | 0.324 | 1.42x | 13.8/25.5/28.3% | 2.1/5.6% | 3 |

> replay-ordering=tip: decode_failures 37

> replay-ordering=heard: misdecodes 3

> replay-ordering=heard: decode_failures 31

> slower: 9.68 s per simulated hour against 1.72 over 45 prior run(s) - 5.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.788 | 0.783 | 0.005 | - | - | 0.861 | 0.927 | 0.271 | 1.32x | 13.0/23.7/26.6% | 1.9/5.3% | 3 |
| enum | 1 | 0.796 | 0.789 | 0.008 | - | - | 0.898 | 0.924 | 0.344 | 1.32x | 12.9/23.9/26.5% | 1.9/5.4% | 3 |
| hybrid | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> resolve=sketch: decode_failures 29

> resolve=hybrid: decode_failures 3

> slower: 4.61 s per simulated hour against 1.54 over 45 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.782 | 0.781 | 0.001 | - | - | 0.909 | 0.909 | 0.209 | 1.33x | 13.1/23.9/26.7% | 2.0/5.3% | 3 |
| 6 | 1 | 0.780 | 0.777 | 0.002 | - | - | 0.915 | 0.916 | 0.233 | 1.34x | 13.2/24.3/27.1% | 2.0/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.780 | 0.778 | 0.002 | - | - | 0.914 | 0.914 | 0.227 | 1.33x | 13.2/23.8/26.7% | 2.0/5.3% | 2 |
| 3 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 5 | 1 | 0.798 | 0.790 | 0.008 | - | - | 0.893 | 0.932 | 0.220 | 1.36x | 13.2/24.7/27.3% | 2.0/5.5% | 5 |
| 8 | 1 | 0.800 | 0.783 | 0.017 | - | - | 0.910 | 0.925 | 0.218 | 1.39x | 13.3/25.1/27.5% | 2.0/5.7% | 8 |

> servers=3: decode_failures 3

> servers=5: decode_failures 57

> servers=8: decode_failures 109

> slower: 13.7 s per simulated hour against 2.4 over 45 prior run(s) - 5.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.780 | 0.778 | 0.002 | - | - | 0.914 | 0.914 | 0.227 | 1.33x | 13.2/23.8/26.7% | 2.0/5.3% | 2 |
| 3 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 5 | 1 | 0.798 | 0.790 | 0.008 | - | - | 0.893 | 0.932 | 0.220 | 1.36x | 13.2/24.7/27.3% | 2.0/5.5% | 5 |
| 8 | 1 | 0.800 | 0.783 | 0.017 | - | - | 0.910 | 0.925 | 0.218 | 1.39x | 13.3/25.1/27.5% | 2.0/5.7% | 8 |

> servers=3: decode_failures 3

> servers=5: decode_failures 57

> servers=8: decode_failures 109

> slower: 13.9 s per simulated hour against 2.29 over 45 prior run(s) - 6.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| True | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |

> signed=False: decode_failures 3

> signed=True: decode_failures 3

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.806 | 0.798 | 0.008 | - | - | 0.917 | 0.947 | 0.357 | 1.25x | 12.3/22.4/25.0% | 1.9/5.0% | 3 |
| 1 | 1 | 0.798 | 0.787 | 0.011 | - | - | 0.925 | 0.934 | 0.390 | 1.24x | 12.3/22.4/25.0% | 1.8/5.0% | 3 |
| 2 | 1 | 0.802 | 0.794 | 0.008 | - | - | 0.935 | 0.937 | 0.316 | 1.24x | 12.1/22.3/24.9% | 1.8/5.0% | 3 |
| 4 | 1 | 0.795 | 0.788 | 0.007 | - | - | 0.920 | 0.924 | 0.310 | 1.25x | 12.4/22.7/25.2% | 1.8/5.1% | 3 |

> sr-retries=0: decode_failures 16

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.793 | 0.782 | 0.011 | - | - | 0.926 | 0.926 | 0.390 | 1.32x | 13.0/23.8/26.5% | 1.9/5.3% | 3 |
| 24 | 1 | 0.789 | 0.779 | 0.010 | - | - | 0.915 | 0.919 | 0.395 | 1.32x | 13.0/23.7/26.5% | 1.9/5.3% | 3 |
| 32 | 1 | 0.793 | 0.781 | 0.011 | - | - | 0.920 | 0.924 | 0.393 | 1.33x | 13.1/23.9/26.8% | 1.9/5.4% | 3 |
| 64 | 1 | 0.789 | 0.782 | 0.007 | - | - | 0.906 | 0.919 | 0.304 | 1.34x | 13.2/24.4/27.1% | 2.0/5.5% | 3 |

> short-id-bits=16: decode_failures 1

> short-id-bits=32: decode_failures 3

> short-id-bits=64: decode_failures 34

> slower: 3.63 s per simulated hour against 1.66 over 45 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.782 | 0.773 | 0.009 | - | - | 0.910 | 0.917 | 0.348 | 1.38x | 13.5/25.0/27.7% | 2.0/5.6% | 3 |
| 16 | 1 | 0.799 | 0.790 | 0.009 | - | - | 0.926 | 0.934 | 0.352 | 1.34x | 13.1/24.4/27.1% | 2.0/5.6% | 3 |
| 32 | 1 | 0.799 | 0.791 | 0.008 | - | - | 0.922 | 0.939 | 0.347 | 1.33x | 13.1/23.9/26.7% | 1.9/5.3% | 3 |

> window-size=8: misdecodes 90

> window-size=16: misdecodes 39

> window-size=32: misdecodes 12

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.937 | 0.006 | - | - | 0.996 | 0.997 | 0.689 | 2.01x | 21.5/32.6/35.9% | 1.4/5.2% | 3 |
| True | 1 | 0.700 | 0.689 | 0.011 | - | - | 0.817 | 0.913 | 0.429 | 5.77x | 56.4/72.7/77.0% | 4.1/13.3% | 3 |

> no-congestion-scaling=True: queue drops 12.4% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 106

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.505 | 0.498 | 0.007 | - | - | 0.765 | 0.766 | 0.179 | 4.57x | 14.8/29.8/44.6% | 1.5/5.8% | 3 |
| truesize | 1 | 0.538 | 0.531 | 0.007 | - | - | 0.800 | 0.801 | 0.186 | 3.41x | 11.1/23.8/37.1% | 1.1/5.0% | 3 |

> faster: 5.4 s per simulated hour against 11.2 over 45 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.950 | 0.945 | 0.005 | - | - | 0.997 | 0.997 | 0.717 | 1.79x | 19.3/29.1/32.2% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.943 | 0.937 | 0.006 | - | - | 0.996 | 0.997 | 0.689 | 2.01x | 21.5/32.6/35.9% | 1.4/5.2% | 3 |

