# Sweep blocks-2026-09-28-9995428

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 9995428 · seeds 9995428
- **blocks** 87 run
- **compute** 12.3 h of simulator time across every cell
- **generated** 2026-09-28T10:00:06+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>121 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 27
- AD-badrouters: slower: 4.42 s per simulated hour against 2.13 over 38 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-siting: siting-mix=basement-heavy: decode_failures 3
- AD-worst: role-placement=degree: decode_failures 43
- AD-worst: role-placement=inverse: decode_failures 18
- AD-worst: slower: 12.6 s per simulated hour against 3.48 over 38 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 29
- BL-control: slower: 5.44 s per simulated hour against 1.82 over 38 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: decode_failures 23
- DB-hotstore-stress: max-num-nodes=10: decode_failures 37
- DB-hotstore-stress: max-num-nodes=120: decode_failures 25
- DB-hotstore-stress: max-num-nodes=250: decode_failures 12
- DB-platform: platform-mix=constrained: decode_failures 35
- DB-warm: warm-num-nodes=0: decode_failures 83
- DB-warm: warm-num-nodes=25: decode_failures 83
- DB-warm: warm-num-nodes=100: decode_failures 83
- DB-warm: warm-num-nodes=2000: decode_failures 83
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 39
- DG-burst: burst-loss=0.3: decode_failures 21
- DG-loss: extra-loss=0.1: decode_failures 37
- DG-loss: extra-loss=0.2: decode_failures 30
- DG-loss: extra-loss=0.3: decode_failures 31
- DG-loss: slower: 8.81 s per simulated hour against 2.28 over 38 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.1: decode_failures 4
- DG-outage: burst-loss=0.2: decode_failures 31
- DG-outage: burst-loss=0.3: decode_failures 23
- DM-mode: dm-mode=flood-only: decode_failures 2
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 15
- DM-mode: dm-mode=m4-early-flood: decode_failures 15
- FW-mixed: legacy-fraction=0.75: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 24
- LD-chatty: broadcast-interval-s=300: decode_failures 29
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 83
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 74
- MS-density: nodes=40: decode_failures 8
- MS-hopscale: nodes=250: decode_failures 55
- MS-hopscale: nodes=500: decode_failures 94
- MS-oversubscribed: nodes=250: decode_failures 25
- MS-oversubscribed: nodes=500: decode_failures 74
- MS-siting: siting-mix=local-typical: decode_failures 8
- MS-siting: siting-mix=event: decode_failures 20
- MS-size: nodes=40: decode_failures 8
- MS-size: nodes=150: decode_failures 23
- MS-stretch: stretch=1.25: decode_failures 23
- MS-stretch: stretch=1.5: decode_failures 2
- MS-topology: topology=corridor: decode_failures 34
- PR-crladder: coding-rate-ladder=False: decode_failures 15
- PR-crladder: coding-rate-ladder=True: decode_failures 30
- PR-crladder: slower: 9.47 s per simulated hour against 2.79 over 38 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 30
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 41
- PR-dmmode-cr: slower: 12.5 s per simulated hour against 2.85 over 38 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=SHORT_TURBO: decode_failures 6
- RF-bw500: preset=LONG_TURBO: decode_failures 1
- RF-noise: noise-profile=temporal: decode_failures 17
- RF-noise: noise-profile=periodic: decode_failures 14
- RF-preset: preset=LONG_MODERATE: decode_failures 32
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 6
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 14
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 2
- RF-txpower: tx-power=22: decode_failures 1
- RF-txpower: tx-power=17: decode_failures 2
- RF-txpower: tx-power=14: decode_failures 5
- RT-hoplimit: hop-limit=3: decode_failures 11
- RT-hopspread: hop-limit=3: decode_failures 11
- RT-spread: hop-spread=False: decode_failures 11
- SC-signing: signature-policy=STRICT: decode_failures 14
- SF-bucket-mode: bucket-mode=global: misdecodes 23
- SF-bucket-mode: bucket-mode=time: misdecodes 6
- SF-bucket-mode: bucket-mode=window: misdecodes 16
- SF-bucket-time: time-bucket-s=600: misdecodes 92
- SF-bucket-time: time-bucket-s=1800: misdecodes 6
- SF-bucket-time: time-bucket-s=3600: misdecodes 5
- SF-bucket-time: time-bucket-s=3600: decode_failures 1
- SF-cadence: trigger=interval: misdecodes 12
- SF-cadence: trigger=interval: decode_failures 23
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 6
- SF-cadence: trigger=bucket+interval: misdecodes 9
- SF-cadence: slower: 7.3 s per simulated hour against 3.63 over 38 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 91
- SF-capacity-local: capacity=8: decode_failures 103
- SF-capacity-local: capacity=16: decode_failures 13
- SF-capacity: capacity=4: decode_failures 91
- SF-capacity: capacity=8: decode_failures 103
- SF-capacity: capacity=16: decode_failures 13
- SF-capacity-window: capacity=8: misdecodes 4
- SF-capacity-window: capacity=8: decode_failures 95
- SF-capacity-window: capacity=16: misdecodes 9
- SF-capacity-window: capacity=16: decode_failures 7
- SF-capacity-window: capacity=32: misdecodes 16
- SF-catchup: catch-up-hours=: misdecodes 9
- SF-catchup: catch-up-hours=02-06: decode_failures 46
- SF-catchup: catch-up-hours=00-08: decode_failures 46
- SF-hops-flat: hops-apart=3: decode_failures 29
- SF-hops-flat: hops-apart=4: decode_failures 22
- SF-hops-spread: hops-apart=3: decode_failures 29
- SF-hops-spread: hops-apart=4: decode_failures 22
- SF-hops-spread: hops-apart=5: decode_failures 18
- SF-place-flat: place=spread: decode_failures 9
- SF-place-spread: place=spread: decode_failures 9
- SF-provide-transport: provide-transport=broadcast: decode_failures 4
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 4
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 1
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 4
- SF-replay-order: replay-ordering=heard: misdecodes 8
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-sr-retries: sr-retries=0: decode_failures 15
- SF-sr-retries: slower: 3.64 s per simulated hour against 1.59 over 38 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-width: short-id-bits=16: decode_failures 1
- SF-window-size: window-size=8: misdecodes 113
- SF-window-size: window-size=16: misdecodes 64
- SF-window-size: window-size=32: misdecodes 16
- TH-congestion-input: congestion-input=hotstore: decode_failures 25
- TH-congestion-input: congestion-input=truesize: decode_failures 19
- TH-congestion: no-congestion-scaling=True: decode_failures 65

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `PR-dmmode-cr` | 12.5 | 2.85 | 4.38x | 38 |
| `DG-loss` | 8.81 | 2.28 | 3.87x | 38 |
| `AD-worst` | 12.6 | 3.48 | 3.61x | 38 |
| `PR-crladder` | 9.47 | 2.79 | 3.39x | 38 |
| `BL-control` | 5.44 | 1.82 | 2.98x | 38 |
| `SF-sr-retries` | 3.64 | 1.59 | 2.29x | 38 |
| `AD-badrouters` | 4.42 | 2.13 | 2.07x | 38 |
| `SF-cadence` | 7.3 | 3.63 | 2.01x | 38 |
| `MS-topology` | 3.88 | 1.95 | 1.99x | 38 |
| `MS-siting` | 3.75 | 1.92 | 1.96x | 37 |
| `DM-mode` | 6.41 | 3.29 | 1.95x | 38 |
| `DB-platform` | 4.88 | 2.52 | 1.94x | 38 |
| `SC-signing` | 3.43 | 1.81 | 1.89x | 38 |
| `SF-replay-order-broadcast` | 3.25 | 1.78 | 1.83x | 38 |
| `RT-spread` | 3.91 | 2.33 | 1.68x | 38 |
| `RT-hoplimit` | 2.71 | 1.79 | 1.52x | 38 |
| `LD-diurnal` | 1.02 | 1.57 | 0.65x | 38 |
| `SF-servers-spread` | 1.45 | 2.35 | 0.62x | 38 |
| `PR-repeats-busy` | 2.31 | 3.77 | 0.61x | 38 |
| `SF-place-spread` | 1.66 | 2.82 | 0.59x | 38 |
| `SF-place-flat` | 1.7 | 2.89 | 0.59x | 38 |
| `PR-protocol` | 0.819 | 1.41 | 0.58x | 38 |
| `SF-servers-flat` | 1.44 | 2.55 | 0.56x | 38 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.964 | 0.964 | 0.730 → 0.745 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.072 → 0.964 | 0.892 | 0.029 → 0.740 | 18x advert_bytes | up | 5 |
| `BL-control` | protocol | **held** | 0 → 0.862 | 0.862 | 0.743 → 0.745 | 1x bytes_on_air | up | 2 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.104 → 0.892 | 0.788 | 0.079 → 0.681 | 99x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.179 → 0.964 | 0.785 | 0.046 → 0.737 | 9x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.191 → 0.920 | 0.729 | 0.127 → 0.608 | 10x sr_bytes | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.238 → 0.964 | 0.726 | 0.194 → 0.737 | 6.8x bytes_on_air | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.099 → 0.825 | 0.725 | 0.042 → 0.649 | 9x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.090 → 0.760 | 0.670 | 0.088 → 0.737 | 3.7x sr_airtime | down | 4 |
| `MS-size` | nodes | **held** | 0.341 → 0.964 | 0.624 | 0.488 → 0.737 | 2.5x sr_bytes | down | 5 |
| `MS-siting` | siting-mix | **text** | 0.336 → 0.950 | 0.614 | 0.315 → 0.949 | 2.2x sr_airtime | up | 4 |
| `SF-place-flat` | place | **held** | 0.420 → 0.970 | 0.550 | 0.737 → 0.752 | 2.4x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.420 → 0.970 | 0.550 | 0.737 → 0.752 | 2.4x sr_bytes | up | 6 |
| `RF-preset` | preset | **text** | 0.251 → 0.779 | 0.528 | 0.250 → 0.765 | 2.8x sr_airtime | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.251 → 0.760 | 0.509 | 0.250 → 0.737 | 2.2x sr_airtime | up | 4 |
| `MS-topology` | topology | **text** | 0.426 → 0.921 | 0.495 | 0.407 → 0.920 | 3.8x sr_bytes | up | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.246 → 0.656 | 0.411 | 0.195 → 0.521 | 4.2x bytes_on_air | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.567 → 0.948 | 0.382 | 0.454 → 0.834 | 14x sr_airtime | down | 3 |
| `MS-density` | nodes | **text** | 0.566 → 0.894 | 0.328 | 0.557 → 0.890 | 4.3x advert_bytes | up | 5 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.668 → 0.985 | 0.317 | 0.479 → 0.785 | 9.7x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.455 → 0.760 | 0.305 | 0.427 → 0.737 | 1.6x sr_bytes | down | 4 |
| `DG-outage` | burst-loss | **text** | 0.462 → 0.760 | 0.298 | 0.440 → 0.737 | 1.6x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.270 → 0.567 | 0.297 | 0.266 → 0.554 | 2.9x sr_airtime | up | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.570 → 0.836 | 0.267 | 0.515 → 0.829 | 2.4x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.721 → 0.964 | 0.244 | 0.737 → 0.748 | 2.7x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.638 → 0.869 | 0.231 | 0.631 → 0.864 | 3.6x sr_airtime | down | 2 |
| `RT-hopspread` | hop-limit | **text** | 0.570 → 0.796 | 0.227 | 0.515 → 0.785 | 2.2x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.768 → 0.966 | 0.198 | 0.570 → 0.737 | 1.5x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.570 → 0.760 | 0.190 | 0.515 → 0.737 | 1.8x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **held** | 0.781 → 0.964 | 0.183 | 0.592 → 0.737 | 1.9x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.357 → 0.525 | 0.168 | 0.217 → 0.313 | 4.2x sr_airtime | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.693 → 0.857 | 0.164 | 0.684 → 0.856 | 2.2x sr_bytes | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.601 → 0.760 | 0.159 | 0.580 → 0.737 | 1.4x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.664 → 0.817 | 0.153 | 0.649 → 0.805 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.664 → 0.817 | 0.153 | 0.649 → 0.805 | 2.2x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.760 → 0.906 | 0.146 | 0.737 → 0.875 | 1.3x sr_airtime | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.831 → 0.964 | 0.134 | 0.737 → 0.748 | 2.7x sr_bytes | down | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.703 → 0.819 | 0.116 | 0.673 → 0.809 | 5.4x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.852 → 0.964 | 0.112 | 0.737 → 0.748 | 30x sr_airtime | down | 3 |
| `FW-mixed` | legacy-fraction | **held** | 0.855 → 0.964 | 0.110 | 0.663 → 0.737 | 2.3x bytes_on_air | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.760 → 0.869 | 0.109 | 0.737 → 0.845 | 1.3x bytes_on_air | up | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.866 → 0.964 | 0.098 | 0.671 → 0.737 | 2.4x bytes_on_air | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.705 → 0.803 | 0.098 | 0.673 → 0.786 | 2x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.708 → 0.803 | 0.095 | 0.682 → 0.786 | 2.1x sr_airtime | up | 4 |
| `SF-cadence` | trigger | **held** | 0.880 → 0.964 | 0.084 | 0.709 → 0.739 | 13x advert_bytes | down | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.812 → 0.895 | 0.082 | 0.665 → 0.734 | 1.2x sr_bytes | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.770 → 0.851 | 0.081 | 0.574 → 0.634 | 1.3x sr_airtime | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.890 → 0.971 | 0.081 | 0.740 → 0.751 | 2.6x advert_bytes | up | 3 |
| `MS-roles` | role-mix | **held** | 0.825 → 0.897 | 0.073 | 0.649 → 0.707 | 1.2x bytes_on_air | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.914 → 0.976 | 0.062 | 0.736 → 0.753 | 1.2x sr_airtime | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.913 → 0.970 | 0.057 | 0.735 → 0.744 | 6.5x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.913 → 0.970 | 0.057 | 0.735 → 0.744 | 6.5x sr_bytes | up | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.908 → 0.964 | 0.056 | 0.676 → 0.737 | 1.1x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.760 → 0.807 | 0.047 | 0.737 → 0.794 | 3.2x bytes_on_air | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.760 → 0.801 | 0.041 | 0.737 → 0.737 | 2.9x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.721 → 0.760 | 0.039 | 0.692 → 0.739 | 1.4x sr_airtime | down | 4 |
| `FW-versions` | profile | **held** | 0.926 → 0.964 | 0.038 | 0.737 → 0.759 | 3.3x bytes_on_air | up | 5 |
| `SF-catchup` | catch-up-hours | **held** | 0.918 → 0.955 | 0.037 | 0.709 → 0.757 | 9.3x advert_bytes | down | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.510 → 0.546 | 0.035 | 0.313 → 0.341 | 2x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **text** | 0.695 → 0.730 | 0.035 | 0.695 → 0.730 | 1.2x sr_airtime | up | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.878 → 0.909 | 0.031 | 0.721 → 0.726 | 1.2x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **held** | 0.825 → 0.853 | 0.028 | 0.600 → 0.649 | 1.6x sr_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.769 → 0.795 | 0.026 | 0.749 → 0.778 | 1.1x bytes_on_air | up | 2 |
| `AD-worst` | role-placement | **text** | 0.799 → 0.824 | 0.025 | 0.790 → 0.819 | 1.1x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.935 → 0.960 | 0.024 | 0.743 → 0.747 | 3.6x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.748 → 0.771 | 0.023 | 0.727 → 0.751 | 5.3x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.943 → 0.964 | 0.021 | 0.737 → 0.754 | 1.2x bytes_on_air | down | 4 |
| `FW-firmware` | profile | **text** | 0.760 → 0.779 | 0.020 | 0.737 → 0.772 | 3.2x bytes_on_air | down | 2 |
| `SF-capacity` | capacity | **held** | 0.946 → 0.964 | 0.018 | 0.736 → 0.748 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.946 → 0.964 | 0.018 | 0.736 → 0.748 | 5.4x advert_bytes | up | 5 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.709 → 0.726 | 0.017 | 0.709 → 0.726 | 1x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **text** | 0.758 → 0.775 | 0.017 | 0.734 → 0.751 | 4.3x advert_bytes | up | 3 |
| `SF-resolve` | resolve | **held** | 0.948 → 0.964 | 0.016 | 0.737 → 0.742 | 5.8x advert_bytes | = | 3 |
| `LD-diurnal` | diurnal | **text** | 0.760 → 0.776 | 0.016 | 0.737 → 0.758 | 1.5x sr_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.760 → 0.775 | 0.015 | 0.737 → 0.751 | 2.1x advert_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.760 → 0.772 | 0.012 | 0.737 → 0.754 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.869 → 0.880 | 0.011 | 0.864 → 0.876 | 1.1x bytes_on_air | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.959 → 0.970 | 0.011 | 0.729 → 0.740 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.959 → 0.970 | 0.011 | 0.729 → 0.740 | 1.1x sr_airtime | up | 4 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.869 → 0.879 | 0.010 | 0.864 → 0.875 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.760 → 0.768 | 0.008 | 0.737 → 0.743 | 1.1x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.941 → 0.947 | 0.007 | 0.736 → 0.737 | 1.1x sr_airtime | up | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.760 → 0.766 | 0.006 | 0.737 → 0.747 | 2.2x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **text** | 0.760 → 0.766 | 0.006 | 0.737 → 0.744 | 3.1x advert_bytes | up | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.866 → 0.869 | 0.003 | 0.861 → 0.864 | 1.1x sr_airtime | down | 2 |

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
| none | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| sprinkled | 1 | 0.693 | 0.684 | 0.009 | - | - | 0.847 | 0.848 | 0.311 | 1.25x | 13.1/21.0/25.7% | 1.9/4.9% | 3 |
| arms-race | 1 | 0.857 | 0.856 | 0.001 | - | - | 0.892 | 0.892 | 0.638 | 1.06x | 18.0/23.7/26.5% | 1.5/5.0% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.1 | 1 | 0.826 | 0.789 | 0.037 | - | - | 0.897 | 0.899 | 0.160 | 1.24x | 17.7/22.8/26.3% | 1.8/5.4% | 3 |
| 0.3 | 1 | 0.906 | 0.875 | 0.031 | - | - | 0.954 | 0.957 | 0.598 | 1.11x | 18.9/25.0/29.2% | 1.4/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.664 | 0.649 | 0.015 | - | - | 0.825 | 0.827 | 0.131 | 1.15x | 13.4/22.6/26.2% | 1.9/5.1% | 3 |
| inverse | 1 | 0.640 | 0.600 | 0.040 | - | - | 0.825 | 0.862 | 0.140 | 1.07x | 11.1/17.8/19.6% | 2.0/3.3% | 3 |
| random | 1 | 0.648 | 0.613 | 0.035 | - | - | 0.853 | 0.857 | 0.145 | 1.11x | 12.3/19.0/22.2% | 1.9/3.4% | 3 |

> role-placement=inverse: decode_failures 27

> slower: 4.42 s per simulated hour against 2.13 over 38 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.664 | 0.649 | 0.015 | - | - | 0.825 | 0.827 | 0.131 | 1.15x | 13.4/22.6/26.2% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.817 | 0.805 | 0.012 | - | - | 0.958 | 0.959 | 0.331 | 2.53x | 26.4/38.0/42.8% | 4.3/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.664 | 0.649 | 0.015 | - | - | 0.825 | 0.827 | 0.131 | 1.15x | 13.4/22.6/26.2% | 1.9/5.1% | 3 |
| no-mute | 1 | 0.727 | 0.704 | 0.023 | - | - | 0.897 | 0.904 | 0.135 | 1.35x | 13.5/23.4/27.3% | 2.2/5.4% | 3 |
| all-routers | 1 | 0.817 | 0.805 | 0.012 | - | - | 0.958 | 0.959 | 0.331 | 2.53x | 26.4/38.0/42.8% | 4.3/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.664 | 0.649 | 0.015 | - | - | 0.825 | 0.827 | 0.131 | 1.15x | 13.4/22.6/26.2% | 1.9/5.1% | 3 |
| local-typical | 1 | 0.415 | 0.405 | 0.010 | - | - | 0.619 | 0.625 | 0.000 | 1.24x | 9.9/22.9/34.8% | 1.9/5.1% | 3 |
| basement-heavy | 1 | 0.042 | 0.042 | 0.000 | - | - | 0.099 | 0.192 | 0.000 | 0.37x | 0.3/4.4/6.0% | 0.2/1.9% | 3 |

> siting-mix=basement-heavy: decode_failures 3

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.824 | 0.819 | 0.005 | - | - | 0.960 | 0.966 | 0.000 | 2.29x | 15.8/28.3/36.3% | 1.8/5.9% | 3 |
| inverse | 1 | 0.799 | 0.790 | 0.009 | - | - | 0.957 | 0.964 | 0.000 | 2.23x | 15.2/24.6/29.9% | 1.8/3.1% | 3 |

> role-placement=degree: decode_failures 43

> role-placement=inverse: decode_failures 18

> slower: 12.6 s per simulated hour against 3.48 over 38 prior run(s) - 3.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.745 | 0.745 | 0.000 | - | - | 0 | 0.000 | 0.148 | 1.38x | 14.6/24.8/28.9% | 2.1/5.2% | 3 |
| sr | 1 | 0.764 | 0.743 | 0.021 | - | - | 0.862 | 0.973 | 0.154 | 1.43x | 15.0/25.6/30.0% | 2.2/5.6% | 3 |

> protocol=sr: decode_failures 29

> slower: 5.44 s per simulated hour against 1.82 over 38 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.708 | 0.682 | 0.026 | - | - | 0.892 | 0.932 | 0.123 | 2.87x | 29.0/51.2/61.7% | 4.4/9.0% | 3 |
| 100 | 1 | 0.803 | 0.786 | 0.017 | - | - | 0.967 | 0.967 | 0.160 | 1.62x | 16.8/29.9/36.7% | 2.4/5.3% | 3 |
| 120 | 1 | 0.803 | 0.786 | 0.017 | - | - | 0.967 | 0.967 | 0.160 | 1.62x | 16.8/29.9/36.7% | 2.4/5.3% | 3 |
| 250 | 1 | 0.803 | 0.786 | 0.017 | - | - | 0.967 | 0.967 | 0.160 | 1.62x | 16.8/29.9/36.7% | 2.4/5.3% | 3 |

> max-num-nodes=10: decode_failures 23

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.221 | 0.217 | 0.004 | - | - | 0.357 | 0.409 | 0.072 | 10.25x | 28.4/40.1/52.8% | 3.7/8.7% | 3 |
| 120 | 1 | 0.319 | 0.313 | 0.006 | - | - | 0.510 | 0.526 | 0.083 | 4.39x | 12.2/17.8/23.9% | 1.6/4.0% | 3 |
| 250 | 1 | 0.319 | 0.313 | 0.006 | - | - | 0.525 | 0.533 | 0.091 | 4.40x | 12.3/17.6/23.9% | 1.6/4.0% | 3 |

> max-num-nodes=10: decode_failures 37

> max-num-nodes=120: decode_failures 25

> max-num-nodes=250: decode_failures 12

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.803 | 0.786 | 0.017 | - | - | 0.967 | 0.967 | 0.160 | 1.62x | 16.8/29.9/36.7% | 2.4/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.803 | 0.786 | 0.017 | - | - | 0.967 | 0.967 | 0.160 | 1.62x | 16.8/29.9/36.7% | 2.4/5.3% | 3 |
| constrained | 1 | 0.705 | 0.673 | 0.032 | - | - | 0.912 | 0.935 | 0.117 | 2.87x | 29.1/51.2/61.6% | 4.4/9.1% | 3 |

> platform-mix=constrained: decode_failures 35

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.641 | 0.634 | 0.007 | - | - | 0.851 | 0.909 | 0.362 | 5.60x | 45.6/67.4/76.2% | 3.9/12.3% | 3 |
| 25 | 1 | 0.641 | 0.634 | 0.007 | - | - | 0.851 | 0.909 | 0.362 | 5.60x | 45.6/67.4/76.2% | 3.9/12.3% | 3 |
| 100 | 1 | 0.641 | 0.634 | 0.007 | - | - | 0.851 | 0.909 | 0.362 | 5.60x | 45.6/67.4/76.2% | 3.9/12.3% | 3 |
| 2000 | 1 | 0.641 | 0.634 | 0.007 | - | - | 0.851 | 0.909 | 0.362 | 5.60x | 45.6/67.4/76.2% | 3.9/12.3% | 3 |

> warm-num-nodes=0: decode_failures 83

> warm-num-nodes=25: decode_failures 83

> warm-num-nodes=100: decode_failures 83

> warm-num-nodes=2000: decode_failures 83

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.1 | 1 | 0.672 | 0.640 | 0.032 | - | - | 0.931 | 0.945 | 0.120 | 1.29x | 14.0/24.1/28.5% | 1.9/5.2% | 3 |
| 0.2 | 1 | 0.561 | 0.532 | 0.029 | - | - | 0.796 | 0.916 | 0.102 | 1.15x | 12.7/21.7/26.1% | 1.8/4.3% | 3 |
| 0.3 | 1 | 0.455 | 0.427 | 0.028 | - | - | 0.664 | 0.846 | 0.069 | 1.03x | 11.4/20.0/24.2% | 1.6/3.8% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 39

> burst-loss=0.3: decode_failures 21

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.1 | 1 | 0.708 | 0.688 | 0.020 | - | - | 0.914 | 0.952 | 0.115 | 1.42x | 15.3/25.9/30.6% | 2.2/5.5% | 3 |
| 0.2 | 1 | 0.665 | 0.638 | 0.027 | - | - | 0.902 | 0.943 | 0.121 | 1.40x | 15.3/26.0/30.9% | 2.1/5.4% | 3 |
| 0.3 | 1 | 0.601 | 0.580 | 0.021 | - | - | 0.820 | 0.916 | 0.112 | 1.36x | 15.1/25.4/30.6% | 2.1/5.0% | 3 |

> extra-loss=0.1: decode_failures 37

> extra-loss=0.2: decode_failures 30

> extra-loss=0.3: decode_failures 31

> slower: 8.81 s per simulated hour against 2.28 over 38 prior run(s) - 3.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.1 | 1 | 0.665 | 0.638 | 0.027 | - | - | 0.934 | 0.950 | 0.119 | 1.31x | 14.3/24.5/28.6% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.548 | 0.525 | 0.024 | - | - | 0.786 | 0.912 | 0.092 | 1.18x | 13.0/22.8/26.9% | 1.8/4.8% | 3 |
| 0.3 | 1 | 0.462 | 0.440 | 0.022 | - | - | 0.677 | 0.857 | 0.068 | 1.07x | 11.8/20.7/24.7% | 1.6/3.9% | 3 |

> burst-loss=0.1: decode_failures 4

> burst-loss=0.2: decode_failures 31

> burst-loss=0.3: decode_failures 23

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.695 | 0.695 | 0.000 | - | - | 0.918 | 0.957 | 0.120 | 1.79x | 19.2/32.7/38.0% | 2.8/7.0% | 3 |
| directed-with-late-flood | 1 | 0.709 | 0.709 | 0.000 | - | - | 0.900 | 0.961 | 0.143 | 1.67x | 17.7/30.8/35.7% | 2.5/6.5% | 3 |
| m4-early-flood | 1 | 0.730 | 0.730 | 0.000 | - | - | 0.923 | 0.970 | 0.141 | 1.67x | 17.8/30.9/36.0% | 2.5/6.6% | 3 |

> dm-mode=flood-only: decode_failures 2

> dm-mode=directed-with-late-flood: decode_failures 15

> dm-mode=m4-early-flood: decode_failures 15

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.779 | 0.772 | 0.007 | - | - | 0.945 | 0.949 | 0.000 | 0.78x | 7.4/11.6/13.3% | 1.2/2.1% | 3 |
| 2.8 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.25 | 1 | 0.723 | 0.708 | 0.015 | - | - | 0.910 | 0.914 | 0.109 | 1.21x | 12.8/19.9/23.7% | 1.7/4.8% | 3 |
| 0.5 | 1 | 0.673 | 0.663 | 0.010 | - | - | 0.855 | 0.857 | 0.178 | 1.06x | 11.0/15.7/18.3% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.737 | 0.722 | 0.015 | - | - | 0.899 | 0.906 | 0.000 | 0.86x | 9.2/13.2/16.7% | 1.4/3.3% | 3 |

> legacy-fraction=0.75: decode_failures 2

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.25 | 1 | 0.716 | 0.702 | 0.014 | - | - | 0.917 | 0.922 | 0.094 | 1.18x | 12.5/19.3/23.3% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.681 | 0.671 | 0.010 | - | - | 0.866 | 0.873 | 0.192 | 1.06x | 11.1/15.8/18.4% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.715 | 0.701 | 0.014 | - | - | 0.875 | 0.877 | 0.000 | 0.84x | 9.2/13.4/16.8% | 1.3/3.4% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.807 | 0.794 | 0.012 | - | - | 0.979 | 0.981 | 0.185 | 0.78x | 8.7/15.2/17.7% | 1.1/3.4% | 3 |
| signing=true | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.755 | 0.747 | 0.008 | - | - | 0.926 | 0.928 | 0.000 | 0.77x | 7.3/12.2/14.9% | 1.2/2.5% | 3 |
| 2.5 | 1 | 0.767 | 0.759 | 0.008 | - | - | 0.928 | 0.936 | 0.000 | 0.80x | 7.5/12.4/15.1% | 1.3/2.6% | 3 |
| 2.6 | 1 | 0.760 | 0.751 | 0.009 | - | - | 0.939 | 0.940 | 0.000 | 0.78x | 7.5/12.6/15.5% | 1.3/2.6% | 3 |
| 2.7 | 1 | 0.766 | 0.759 | 0.007 | - | - | 0.935 | 0.939 | 0.000 | 0.80x | 7.4/13.8/17.9% | 1.2/3.2% | 3 |
| 2.8 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.801 | 0.785 | 0.016 | - | - | 0.985 | 0.987 | 0.148 | 0.94x | 10.0/17.0/19.8% | 1.4/3.8% | 3 |
| 900 | 1 | 0.703 | 0.673 | 0.030 | - | - | 0.935 | 0.943 | 0.135 | 2.12x | 22.5/38.3/44.5% | 3.3/8.3% | 3 |
| 300 | 1 | 0.498 | 0.479 | 0.019 | - | - | 0.668 | 0.881 | 0.104 | 4.42x | 45.3/69.3/76.4% | 7.0/15.2% | 3 |

> broadcast-interval-s=300: decode_failures 29

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.840 | 0.834 | 0.006 | - | - | 0.948 | 0.948 | 0.217 | 1.04x | 10.7/17.7/19.9% | 1.7/3.6% | 3 |
| 900 | 1 | 0.749 | 0.732 | 0.017 | - | - | 0.896 | 0.899 | 0.172 | 2.41x | 25.0/40.3/45.3% | 3.8/8.2% | 3 |
| 300 | 1 | 0.462 | 0.454 | 0.008 | - | - | 0.567 | 0.727 | 0.096 | 5.05x | 50.4/73.0/77.7% | 8.3/15.7% | 3 |

> broadcast-interval-s=300: decode_failures 24

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.776 | 0.758 | 0.018 | - | - | 0.969 | 0.973 | 0.171 | 1.31x | 14.0/23.7/27.8% | 2.1/5.2% | 3 |
| sinusoid | 1 | 0.772 | 0.753 | 0.018 | - | - | 0.957 | 0.963 | 0.144 | 1.25x | 13.3/22.8/26.6% | 1.9/4.9% | 3 |
| commuter | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.703 | 0.673 | 0.030 | - | - | 0.935 | 0.943 | 0.135 | 2.12x | 22.5/38.3/44.5% | 3.3/8.3% | 3 |
| 3600 | 1 | 0.801 | 0.785 | 0.016 | - | - | 0.985 | 0.987 | 0.148 | 0.94x | 10.0/17.0/19.8% | 1.4/3.8% | 3 |
| 10800 | 1 | 0.817 | 0.805 | 0.012 | - | - | 0.989 | 0.989 | 0.178 | 0.60x | 6.4/11.0/12.8% | 0.9/2.5% | 3 |
| 43200 | 1 | 0.819 | 0.809 | 0.010 | - | - | 0.987 | 0.989 | 0.160 | 0.42x | 4.5/7.8/9.1% | 0.6/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.25 | 1 | 0.759 | 0.739 | 0.020 | - | - | 0.959 | 0.972 | 0.150 | 1.47x | 15.6/26.7/31.1% | 2.3/5.8% | 3 |
| 1.0 | 1 | 0.750 | 0.725 | 0.024 | - | - | 0.963 | 0.964 | 0.147 | 1.61x | 17.2/29.3/34.2% | 2.5/6.4% | 3 |
| 4.0 | 1 | 0.721 | 0.692 | 0.029 | - | - | 0.949 | 0.957 | 0.145 | 1.94x | 20.6/36.4/42.3% | 2.9/8.1% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.641 | 0.634 | 0.007 | - | - | 0.851 | 0.909 | 0.362 | 5.60x | 45.6/67.4/76.2% | 3.9/12.3% | 3 |
| 1.0 | 1 | 0.580 | 0.574 | 0.005 | - | - | 0.770 | 0.871 | 0.322 | 6.28x | 51.1/70.2/78.3% | 4.6/13.6% | 3 |

> traceroute-per-hour=0.0: decode_failures 83

> traceroute-per-hour=1.0: decode_failures 74

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.566 | 0.557 | 0.009 | - | - | 0.786 | 0.814 | 0.000 | 1.12x | 13.6/26.6/30.2% | 2.6/6.0% | 3 |
| 60 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 90 | 1 | 0.894 | 0.890 | 0.004 | - | - | 0.992 | 0.993 | 0.640 | 1.77x | 16.3/25.3/31.4% | 1.7/5.3% | 3 |
| 120 | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.986 | 0.987 | 0.519 | 2.16x | 18.5/32.3/39.5% | 1.5/5.2% | 3 |
| 150 | 1 | 0.888 | 0.881 | 0.007 | - | - | 0.976 | 0.977 | 0.636 | 2.41x | 20.4/30.3/34.5% | 1.3/5.0% | 3 |

> nodes=40: decode_failures 8

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 120 | 1 | 0.523 | 0.514 | 0.009 | - | - | 0.654 | 0.655 | 0.061 | 2.22x | 10.8/19.3/24.5% | 1.6/5.2% | 3 |
| 250 | 1 | 0.317 | 0.311 | 0.006 | - | - | 0.506 | 0.516 | 0.085 | 4.67x | 13.1/18.7/25.4% | 1.7/4.4% | 3 |
| 500 | 1 | 0.196 | 0.194 | 0.002 | - | - | 0.238 | 0.266 | 0.020 | 9.40x | 12.9/20.1/28.9% | 1.7/4.7% | 3 |

> nodes=250: decode_failures 55

> nodes=500: decode_failures 94

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.531 | 0.521 | 0.010 | - | - | 0.656 | 0.660 | 0.054 | 2.13x | 10.2/18.3/23.5% | 1.5/5.0% | 3 |
| 250 | 1 | 0.319 | 0.313 | 0.006 | - | - | 0.510 | 0.526 | 0.083 | 4.39x | 12.2/17.8/23.9% | 1.6/4.0% | 3 |
| 500 | 1 | 0.197 | 0.195 | 0.002 | - | - | 0.246 | 0.275 | 0.017 | 8.81x | 12.1/18.8/27.0% | 1.6/4.3% | 3 |

> nodes=250: decode_failures 25

> nodes=500: decode_failures 74

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.727 | 0.707 | 0.020 | - | - | 0.897 | 0.902 | 0.145 | 1.39x | 14.9/24.8/28.9% | 2.1/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.664 | 0.649 | 0.015 | - | - | 0.825 | 0.827 | 0.131 | 1.15x | 13.4/22.6/26.2% | 1.9/5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.752 | 0.734 | 0.019 | - | - | 0.895 | 0.902 | 0.198 | 1.43x | 15.1/25.1/28.8% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.674 | 0.665 | 0.010 | - | - | 0.812 | 0.815 | 0.124 | 1.33x | 15.4/25.5/29.3% | 2.4/5.0% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.05 | 1 | 0.759 | 0.743 | 0.016 | - | - | 0.948 | 0.959 | 0.150 | 1.51x | 16.8/28.6/34.2% | 2.3/5.5% | 3 |
| 0.1 | 1 | 0.774 | 0.754 | 0.020 | - | - | 0.959 | 0.961 | 0.153 | 1.60x | 17.0/30.6/39.1% | 2.3/5.4% | 3 |
| 0.2 | 1 | 0.769 | 0.753 | 0.016 | - | - | 0.943 | 0.946 | 0.110 | 1.75x | 20.4/34.4/40.4% | 2.5/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| local-typical | 1 | 0.544 | 0.535 | 0.009 | - | - | 0.813 | 0.821 | 0.000 | 1.52x | 11.8/24.6/35.6% | 2.5/5.3% | 3 |
| event | 1 | 0.336 | 0.315 | 0.021 | - | - | 0.624 | 0.656 | 0.000 | 1.41x | 8.6/16.5/26.2% | 2.0/6.0% | 3 |
| backbone | 1 | 0.950 | 0.949 | 0.001 | - | - | 0.997 | 0.998 | 0.214 | 1.25x | 25.9/34.8/38.3% | 1.9/5.5% | 3 |

> siting-mix=local-typical: decode_failures 8

> siting-mix=event: decode_failures 20

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.711 | 0.698 | 0.013 | - | - | 0.883 | 0.896 | 0.098 | 1.31x | 22.2/34.5/38.0% | 2.6/7.2% | 3 |
| 60 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 90 | 1 | 0.642 | 0.632 | 0.011 | - | - | 0.884 | 0.886 | 0.000 | 1.78x | 12.2/21.9/27.8% | 1.7/5.4% | 3 |
| 120 | 1 | 0.523 | 0.514 | 0.009 | - | - | 0.654 | 0.655 | 0.061 | 2.22x | 10.8/19.3/24.5% | 1.6/5.2% | 3 |
| 150 | 1 | 0.489 | 0.488 | 0.001 | - | - | 0.341 | 0.575 | 0.031 | 2.71x | 12.2/19.0/26.5% | 1.5/5.0% | 3 |

> nodes=40: decode_failures 8

> nodes=150: decode_failures 23

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 1.25 | 1 | 0.450 | 0.438 | 0.011 | - | - | 0.742 | 0.751 | 0.000 | 1.37x | 10.7/19.7/23.3% | 2.3/5.7% | 3 |
| 1.5 | 1 | 0.270 | 0.266 | 0.004 | - | - | 0.384 | 0.390 | 0.000 | 1.26x | 6.7/16.9/21.1% | 2.2/5.0% | 3 |
| 2.0 | 1 | 0.090 | 0.088 | 0.003 | - | - | 0.322 | 0.333 | 0.000 | 0.59x | 2.1/6.5/8.5% | 0.9/2.4% | 3 |

> stretch=1.25: decode_failures 23

> stretch=1.5: decode_failures 2

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| clustered | 1 | 0.870 | 0.860 | 0.010 | - | - | 0.986 | 0.988 | 0.000 | 1.22x | 21.3/32.0/33.9% | 1.8/5.5% | 3 |
| corridor | 1 | 0.426 | 0.407 | 0.018 | - | - | 0.646 | 0.694 | 0.106 | 1.47x | 13.7/23.2/29.4% | 1.9/6.3% | 3 |
| hub | 1 | 0.921 | 0.920 | 0.001 | - | - | 0.976 | 0.976 | 0.426 | 1.31x | 22.9/34.5/35.8% | 2.0/5.4% | 3 |

> topology=corridor: decode_failures 34

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.709 | 0.709 | 0.000 | - | - | 0.900 | 0.961 | 0.143 | 1.67x | 17.7/30.8/35.7% | 2.5/6.5% | 3 |
| True | 1 | 0.726 | 0.726 | 0.000 | - | - | 0.909 | 0.963 | 0.146 | 1.66x | 17.7/30.5/35.5% | 2.5/6.5% | 3 |

> coding-rate-ladder=False: decode_failures 15

> coding-rate-ladder=True: decode_failures 30

> slower: 9.47 s per simulated hour against 2.79 over 38 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.726 | 0.726 | 0.000 | - | - | 0.909 | 0.963 | 0.146 | 1.66x | 17.7/30.5/35.5% | 2.5/6.5% | 3 |
| m4-early-flood | 1 | 0.721 | 0.721 | 0.000 | - | - | 0.878 | 0.958 | 0.152 | 1.65x | 17.5/30.3/35.3% | 2.5/6.4% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 30

> dm-mode=m4-early-flood: decode_failures 41

> slower: 12.5 s per simulated hour against 2.85 over 38 prior run(s) - 4.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.745 | 0.745 | 0.000 | - | - | 0 | 0.000 | 0.148 | 1.38x | 14.6/24.8/28.9% | 2.1/5.2% | 3 |
| chain | 1 | 0.731 | 0.730 | 0.001 | - | - | 0.838 | 0.970 | 0.145 | 1.60x | 17.0/28.7/33.3% | 2.5/6.1% | 3 |
| sr | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| True | 1 | 0.772 | 0.754 | 0.019 | - | - | 0.968 | 0.976 | 0.168 | 1.43x | 15.1/25.8/30.1% | 2.2/5.6% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.986 | 0.987 | 0.519 | 2.16x | 18.5/32.3/39.5% | 1.5/5.2% | 3 |
| True | 1 | 0.879 | 0.875 | 0.004 | - | - | 0.990 | 0.990 | 0.535 | 2.18x | 18.4/32.0/39.1% | 1.5/5.2% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.128 | 0.127 | 0.001 | - | - | 0.191 | 0.316 | 0.000 | 0.03x | 0.1/0.4/0.5% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.315 | 0.312 | 0.003 | - | - | 0.354 | 0.359 | 0.000 | 0.22x | 1.2/3.3/4.2% | 0.3/1.0% | 3 |
| LONG_TURBO | 1 | 0.622 | 0.608 | 0.015 | - | - | 0.920 | 0.924 | 0.000 | 1.20x | 11.9/17.7/20.9% | 1.8/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 6

> preset=LONG_TURBO: decode_failures 1

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 0.25 | 1 | 0.790 | 0.764 | 0.026 | - | - | 0.972 | 0.974 | 0.237 | 1.35x | 16.5/26.5/30.4% | 2.1/5.6% | 3 |
| 1.0 | 1 | 0.869 | 0.845 | 0.024 | - | - | 0.983 | 0.986 | 0.511 | 1.07x | 21.0/29.0/31.5% | 1.5/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.251 | 0.250 | 0.001 | - | - | 0.571 | 0.574 | 0.000 | 0.11x | 0.5/1.5/2.0% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| LITE_FAST | 1 | 0.652 | 0.641 | 0.011 | - | - | 0.925 | 0.928 | 0.000 | 0.94x | 9.2/15.2/19.0% | 1.5/4.0% | 3 |
| NARROW_SLOW | 1 | 0.691 | 0.681 | 0.010 | - | - | 0.950 | 0.951 | 0.069 | 1.24x | 12.9/20.4/24.5% | 2.0/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| temporal | 1 | 0.633 | 0.600 | 0.034 | - | - | 0.898 | 0.932 | 0.045 | 1.31x | 14.0/24.7/28.9% | 2.0/5.4% | 3 |
| transient | 1 | 0.752 | 0.726 | 0.026 | - | - | 0.966 | 0.968 | 0.144 | 1.38x | 14.7/25.1/29.4% | 2.1/5.5% | 3 |
| periodic | 1 | 0.588 | 0.570 | 0.019 | - | - | 0.768 | 0.800 | 0.120 | 1.27x | 13.8/23.5/27.7% | 1.9/4.9% | 3 |

> noise-profile=temporal: decode_failures 17

> noise-profile=periodic: decode_failures 14

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.251 | 0.250 | 0.001 | - | - | 0.571 | 0.574 | 0.000 | 0.11x | 0.5/1.5/2.0% | 0.1/0.5% | 3 |
| LONG_FAST | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| LONG_MODERATE | 1 | 0.779 | 0.765 | 0.014 | - | - | 0.924 | 0.948 | 0.364 | 3.52x | 43.0/61.8/68.3% | 5.1/13.1% | 3 |

> preset=LONG_MODERATE: decode_failures 32

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.029 | 0.029 | 0.000 | - | - | 0.072 | 0.076 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.128 | 0.127 | 0.001 | - | - | 0.191 | 0.316 | 0.000 | 0.03x | 0.1/0.4/0.5% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| LONG_TURBO | 1 | 0.622 | 0.608 | 0.015 | - | - | 0.920 | 0.924 | 0.000 | 1.20x | 11.9/17.7/20.9% | 1.8/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.760 | 0.740 | 0.020 | - | - | 0.958 | 0.963 | 0.173 | 1.87x | 18.8/30.8/36.5% | 2.8/7.3% | 3 |

> preset=SHORT_TURBO: decode_failures 6

> preset=LONG_TURBO: decode_failures 1

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.701 | 0.681 | 0.020 | - | - | 0.892 | 0.909 | 0.137 | 1.36x | 14.7/25.0/29.2% | 2.1/5.3% | 3 |
| 10000 | 1 | 0.588 | 0.570 | 0.019 | - | - | 0.768 | 0.800 | 0.120 | 1.27x | 13.8/23.5/27.7% | 1.9/4.9% | 3 |
| 4000 | 1 | 0.353 | 0.351 | 0.002 | - | - | 0.450 | 0.590 | 0.054 | 1.03x | 11.2/19.3/22.9% | 1.6/3.5% | 3 |
| 2000 | 1 | 0.079 | 0.079 | 0.000 | - | - | 0.104 | 0.220 | 0.019 | 0.68x | 7.6/12.9/16.2% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 14

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.270 | 0.266 | 0.004 | - | - | 0.384 | 0.390 | 0.000 | 1.26x | 6.7/16.9/21.1% | 2.2/5.0% | 3 |
| 1.0 | 1 | 0.567 | 0.554 | 0.013 | - | - | 0.659 | 0.661 | 0.329 | 0.92x | 13.0/18.6/20.9% | 1.3/4.1% | 3 |

> duct-per-hour=0.0: decode_failures 2

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 22 | 1 | 0.276 | 0.271 | 0.004 | - | - | 0.373 | 0.374 | 0.000 | 1.30x | 7.0/17.1/21.6% | 2.2/5.1% | 3 |
| 17 | 1 | 0.118 | 0.117 | 0.001 | - | - | 0.179 | 0.300 | 0.000 | 0.70x | 2.5/7.6/11.8% | 0.9/2.9% | 3 |
| 14 | 1 | 0.048 | 0.046 | 0.002 | - | - | 0.211 | 0.241 | 0.000 | 0.43x | 1.5/3.7/5.7% | 0.7/1.8% | 3 |

> tx-power=22: decode_failures 1

> tx-power=17: decode_failures 2

> tx-power=14: decode_failures 5

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.986 | 0.987 | 0.519 | 2.16x | 18.5/32.3/39.5% | 1.5/5.2% | 3 |
| True | 1 | 0.866 | 0.861 | 0.006 | - | - | 0.985 | 0.986 | 0.515 | 2.41x | 20.7/34.6/42.3% | 1.6/5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.769 | 0.749 | 0.019 | - | - | 0.971 | 0.974 | 0.108 | 1.43x | 15.5/28.0/32.1% | 2.1/5.5% | 3 |
| True | 1 | 0.795 | 0.778 | 0.017 | - | - | 0.969 | 0.969 | 0.140 | 1.55x | 16.7/28.5/32.7% | 2.2/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| random | 1 | 0.707 | 0.676 | 0.031 | - | - | 0.908 | 0.910 | 0.143 | 1.37x | 14.7/24.3/28.3% | 2.1/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.570 | 0.515 | 0.055 | - | - | 0.870 | 0.891 | 0.062 | 1.05x | 11.2/21.3/25.1% | 1.5/5.1% | 3 |
| 7 | 1 | 0.796 | 0.785 | 0.012 | - | - | 0.925 | 0.927 | 0.185 | 1.52x | 16.0/26.0/29.5% | 2.4/5.3% | 3 |
| 15 | 1 | 0.824 | 0.816 | 0.008 | - | - | 0.916 | 0.917 | 0.221 | 1.58x | 16.3/26.6/29.9% | 2.6/5.3% | 3 |
| 32 | 1 | 0.836 | 0.829 | 0.007 | - | - | 0.925 | 0.927 | 0.225 | 1.59x | 16.5/26.8/30.1% | 2.5/5.4% | 3 |

> hop-limit=3: decode_failures 11

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.570 | 0.515 | 0.055 | - | - | 0.870 | 0.891 | 0.062 | 1.05x | 11.2/21.3/25.1% | 1.5/5.1% | 3 |
| 5 | 1 | 0.714 | 0.690 | 0.024 | - | - | 0.919 | 0.924 | 0.122 | 1.39x | 14.8/24.7/28.9% | 2.2/5.4% | 3 |
| 7 | 1 | 0.796 | 0.785 | 0.012 | - | - | 0.925 | 0.927 | 0.185 | 1.52x | 16.0/26.0/29.5% | 2.4/5.3% | 3 |

> hop-limit=3: decode_failures 11

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| KNOWN_ONLY | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.748 | 0.748 | 0.000 | - | - | 0.852 | 0.974 | 0.154 | 1.37x | 14.6/24.9/29.0% | 2.2/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.570 | 0.515 | 0.055 | - | - | 0.870 | 0.891 | 0.062 | 1.05x | 11.2/21.3/25.1% | 1.5/5.1% | 3 |
| True | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

> hop-spread=False: decode_failures 11

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| BALANCED | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| STRICT | 1 | 0.592 | 0.592 | 0.000 | - | - | 0.781 | 0.811 | 0.087 | 1.47x | 15.6/26.7/31.2% | 2.2/5.7% | 3 |

> signature-policy=STRICT: decode_failures 14

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| dm | 1 | 0.766 | 0.747 | 0.019 | - | - | 0.970 | 0.972 | 0.151 | 1.38x | 14.8/25.4/29.7% | 2.1/5.6% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.767 | 0.747 | 0.021 | - | - | 0.960 | 0.973 | 0.142 | 1.43x | 15.3/26.0/30.3% | 2.2/5.6% | 3 |
| local | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| time | 1 | 0.771 | 0.751 | 0.020 | - | - | 0.968 | 0.983 | 0.160 | 1.44x | 15.4/26.2/30.5% | 2.2/5.8% | 3 |
| window | 1 | 0.775 | 0.751 | 0.024 | - | - | 0.971 | 0.978 | 0.164 | 1.40x | 14.8/25.4/29.6% | 2.1/5.6% | 3 |

> bucket-mode=global: misdecodes 23

> bucket-mode=time: misdecodes 6

> bucket-mode=window: misdecodes 16

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.748 | 0.727 | 0.021 | - | - | 0.951 | 0.960 | 0.136 | 1.53x | 16.4/27.8/32.2% | 2.3/6.2% | 3 |
| 1800 | 1 | 0.771 | 0.751 | 0.020 | - | - | 0.968 | 0.983 | 0.160 | 1.44x | 15.4/26.2/30.5% | 2.2/5.8% | 3 |
| 3600 | 1 | 0.754 | 0.736 | 0.018 | - | - | 0.952 | 0.961 | 0.146 | 1.41x | 15.0/25.6/29.8% | 2.2/5.5% | 3 |

> time-bucket-s=600: misdecodes 92

> time-bucket-s=1800: misdecodes 6

> time-bucket-s=3600: misdecodes 5

> time-bucket-s=3600: decode_failures 1

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| interval | 1 | 0.740 | 0.718 | 0.022 | - | - | 0.953 | 0.967 | 0.167 | 1.83x | 19.5/33.3/38.3% | 2.9/8.0% | 3 |
| aimd | 1 | 0.744 | 0.739 | 0.005 | - | - | 0.880 | 0.972 | 0.158 | 1.42x | 15.2/25.6/29.9% | 2.2/5.5% | 3 |
| bucket+interval | 1 | 0.735 | 0.709 | 0.027 | - | - | 0.955 | 0.959 | 0.145 | 1.86x | 19.9/33.8/38.8% | 2.9/7.9% | 3 |

> trigger=interval: misdecodes 12

> trigger=interval: decode_failures 23

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 6

> trigger=bucket+interval: misdecodes 9

> slower: 7.3 s per simulated hour against 3.63 over 38 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.763 | 0.748 | 0.015 | - | - | 0.946 | 0.977 | 0.158 | 1.41x | 15.0/25.6/30.1% | 2.1/5.7% | 3 |
| 8 | 1 | 0.758 | 0.737 | 0.021 | - | - | 0.954 | 0.972 | 0.119 | 1.42x | 15.2/25.9/30.2% | 2.2/5.7% | 3 |
| 16 | 1 | 0.758 | 0.738 | 0.020 | - | - | 0.959 | 0.968 | 0.143 | 1.43x | 15.2/26.1/30.4% | 2.2/5.7% | 3 |
| 32 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 50 | 1 | 0.758 | 0.736 | 0.022 | - | - | 0.964 | 0.965 | 0.159 | 1.41x | 15.1/25.7/30.0% | 2.2/5.6% | 3 |

> capacity=4: decode_failures 91

> capacity=8: decode_failures 103

> capacity=16: decode_failures 13

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.763 | 0.748 | 0.015 | - | - | 0.946 | 0.977 | 0.158 | 1.41x | 15.0/25.6/30.1% | 2.1/5.7% | 3 |
| 8 | 1 | 0.758 | 0.737 | 0.021 | - | - | 0.954 | 0.972 | 0.119 | 1.42x | 15.2/25.9/30.2% | 2.2/5.7% | 3 |
| 16 | 1 | 0.758 | 0.738 | 0.020 | - | - | 0.959 | 0.968 | 0.143 | 1.43x | 15.2/26.1/30.4% | 2.2/5.7% | 3 |
| 32 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 50 | 1 | 0.758 | 0.736 | 0.022 | - | - | 0.964 | 0.965 | 0.159 | 1.41x | 15.1/25.7/30.0% | 2.2/5.6% | 3 |

> capacity=4: decode_failures 91

> capacity=8: decode_failures 103

> capacity=16: decode_failures 13

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.748 | 0.740 | 0.008 | - | - | 0.890 | 0.963 | 0.149 | 1.38x | 14.6/25.1/29.3% | 2.1/5.4% | 3 |
| 16 | 1 | 0.767 | 0.743 | 0.024 | - | - | 0.965 | 0.974 | 0.150 | 1.41x | 15.0/25.7/29.9% | 2.2/5.6% | 3 |
| 32 | 1 | 0.775 | 0.751 | 0.024 | - | - | 0.971 | 0.978 | 0.164 | 1.40x | 14.8/25.4/29.6% | 2.1/5.6% | 3 |

> capacity=8: misdecodes 4

> capacity=8: decode_failures 95

> capacity=16: misdecodes 9

> capacity=16: decode_failures 7

> capacity=32: misdecodes 16

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.735 | 0.709 | 0.027 | - | - | 0.955 | 0.959 | 0.145 | 1.86x | 19.9/33.8/38.8% | 2.9/7.9% | 3 |
| 02-06 | 1 | 0.768 | 0.757 | 0.011 | - | - | 0.919 | 0.979 | 0.133 | 1.44x | 15.5/26.4/30.7% | 2.2/5.8% | 3 |
| 00-08 | 1 | 0.761 | 0.748 | 0.013 | - | - | 0.918 | 0.972 | 0.143 | 1.49x | 16.0/27.1/31.7% | 2.3/6.1% | 3 |

> catch-up-hours=: misdecodes 9

> catch-up-hours=02-06: decode_failures 46

> catch-up-hours=00-08: decode_failures 46

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.751 | 0.748 | 0.003 | - | - | 0.956 | 0.959 | 0.150 | 1.40x | 14.8/25.4/29.6% | 2.2/5.4% | 3 |
| 2 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 3 | 1 | 0.764 | 0.743 | 0.021 | - | - | 0.862 | 0.973 | 0.154 | 1.43x | 15.0/25.6/30.0% | 2.2/5.6% | 3 |
| 4 | 1 | 0.778 | 0.737 | 0.042 | - | - | 0.831 | 0.968 | 0.145 | 1.41x | 14.9/25.4/29.6% | 2.2/5.5% | 3 |

> hops-apart=3: decode_failures 29

> hops-apart=4: decode_failures 22

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.751 | 0.748 | 0.003 | - | - | 0.956 | 0.959 | 0.150 | 1.40x | 14.8/25.4/29.6% | 2.2/5.4% | 3 |
| 2 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 3 | 1 | 0.764 | 0.743 | 0.021 | - | - | 0.862 | 0.973 | 0.154 | 1.43x | 15.0/25.6/30.0% | 2.2/5.6% | 3 |
| 4 | 1 | 0.778 | 0.737 | 0.042 | - | - | 0.831 | 0.968 | 0.145 | 1.41x | 14.9/25.4/29.6% | 2.2/5.5% | 3 |
| 5 | 1 | 0.760 | 0.740 | 0.020 | - | - | 0.721 | 0.969 | 0.154 | 1.41x | 14.9/25.2/29.5% | 2.2/5.4% | 3 |

> hops-apart=3: decode_failures 29

> hops-apart=4: decode_failures 22

> hops-apart=5: decode_failures 18

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.754 | 0.729 | 0.025 | - | - | 0.959 | 0.963 | 0.149 | 1.41x | 14.9/25.6/29.8% | 2.2/5.6% | 3 |
| 30 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 120 | 1 | 0.761 | 0.740 | 0.021 | - | - | 0.968 | 0.972 | 0.150 | 1.44x | 15.3/25.9/30.4% | 2.2/5.7% | 3 |
| 600 | 1 | 0.763 | 0.740 | 0.023 | - | - | 0.970 | 0.972 | 0.145 | 1.42x | 15.0/25.7/30.0% | 2.2/5.6% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.754 | 0.729 | 0.025 | - | - | 0.959 | 0.963 | 0.149 | 1.41x | 14.9/25.6/29.8% | 2.2/5.6% | 3 |
| 30 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 120 | 1 | 0.761 | 0.740 | 0.021 | - | - | 0.968 | 0.972 | 0.150 | 1.44x | 15.3/25.9/30.4% | 2.2/5.7% | 3 |
| 600 | 1 | 0.763 | 0.740 | 0.023 | - | - | 0.970 | 0.972 | 0.145 | 1.42x | 15.0/25.7/30.0% | 2.2/5.6% | 3 |

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.761 | 0.752 | 0.009 | - | - | 0.420 | 0.794 | 0.158 | 1.40x | 14.9/25.3/29.6% | 2.2/5.3% | 3 |
| routers | 1 | 0.750 | 0.747 | 0.002 | - | - | 0.935 | 0.936 | 0.142 | 1.40x | 14.9/25.6/29.7% | 2.1/5.4% | 3 |
| alternate-routers | 1 | 0.748 | 0.746 | 0.002 | - | - | 0.929 | 0.929 | 0.129 | 1.41x | 14.9/25.7/29.8% | 2.2/5.4% | 3 |
| beside-router | 1 | 0.747 | 0.745 | 0.002 | - | - | 0.924 | 0.925 | 0.165 | 1.42x | 15.0/25.7/29.9% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.759 | 0.742 | 0.017 | - | - | 0.970 | 0.972 | 0.128 | 1.41x | 15.0/25.3/29.6% | 2.2/5.3% | 3 |
| hops-apart | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

> place=spread: decode_failures 9

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.761 | 0.752 | 0.009 | - | - | 0.420 | 0.794 | 0.158 | 1.40x | 14.9/25.3/29.6% | 2.2/5.3% | 3 |
| routers | 1 | 0.750 | 0.747 | 0.002 | - | - | 0.935 | 0.936 | 0.142 | 1.40x | 14.9/25.6/29.7% | 2.1/5.4% | 3 |
| alternate-routers | 1 | 0.748 | 0.746 | 0.002 | - | - | 0.929 | 0.929 | 0.129 | 1.41x | 14.9/25.7/29.8% | 2.2/5.4% | 3 |
| beside-router | 1 | 0.747 | 0.745 | 0.002 | - | - | 0.924 | 0.925 | 0.165 | 1.42x | 15.0/25.7/29.9% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.759 | 0.742 | 0.017 | - | - | 0.970 | 0.972 | 0.128 | 1.41x | 15.0/25.3/29.6% | 2.2/5.3% | 3 |
| hops-apart | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

> place=spread: decode_failures 9

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| broadcast | 1 | 0.801 | 0.737 | 0.063 | - | - | 0.941 | 0.964 | 0.198 | 1.52x | 16.2/27.4/31.8% | 2.3/5.8% | 3 |

> provide-transport=broadcast: decode_failures 4

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| heard | 1 | 0.768 | 0.743 | 0.026 | - | - | 0.965 | 0.969 | 0.168 | 1.43x | 15.3/26.0/30.3% | 2.2/5.7% | 3 |

> replay-ordering=heard: misdecodes 8

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.801 | 0.737 | 0.063 | - | - | 0.941 | 0.964 | 0.198 | 1.52x | 16.2/27.4/31.8% | 2.3/5.8% | 3 |
| heard | 1 | 0.802 | 0.736 | 0.066 | - | - | 0.947 | 0.969 | 0.185 | 1.51x | 16.0/27.2/31.4% | 2.3/5.8% | 3 |

> replay-ordering=tip: decode_failures 4

> replay-ordering=heard: misdecodes 1

> replay-ordering=heard: decode_failures 4

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| enum | 1 | 0.760 | 0.742 | 0.019 | - | - | 0.948 | 0.970 | 0.155 | 1.41x | 15.1/25.7/30.1% | 2.2/5.6% | 3 |
| hybrid | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.750 | 0.747 | 0.002 | - | - | 0.935 | 0.936 | 0.142 | 1.40x | 14.9/25.6/29.7% | 2.1/5.4% | 3 |
| 6 | 1 | 0.756 | 0.743 | 0.013 | - | - | 0.960 | 0.961 | 0.151 | 1.41x | 14.9/26.1/30.3% | 2.1/5.6% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.752 | 0.744 | 0.007 | - | - | 0.913 | 0.915 | 0.129 | 1.40x | 14.9/25.5/29.7% | 2.1/5.5% | 2 |
| 3 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 5 | 1 | 0.756 | 0.735 | 0.021 | - | - | 0.968 | 0.969 | 0.163 | 1.44x | 15.4/26.3/30.4% | 2.2/5.7% | 5 |
| 8 | 1 | 0.778 | 0.738 | 0.040 | - | - | 0.970 | 0.972 | 0.137 | 1.49x | 15.9/27.0/31.4% | 2.3/5.8% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.752 | 0.744 | 0.007 | - | - | 0.913 | 0.915 | 0.129 | 1.40x | 14.9/25.5/29.7% | 2.1/5.5% | 2 |
| 3 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 5 | 1 | 0.756 | 0.735 | 0.021 | - | - | 0.968 | 0.969 | 0.163 | 1.44x | 15.4/26.3/30.4% | 2.2/5.7% | 5 |
| 8 | 1 | 0.778 | 0.738 | 0.040 | - | - | 0.970 | 0.972 | 0.137 | 1.49x | 15.9/27.0/31.4% | 2.3/5.8% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| True | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.751 | 0.738 | 0.013 | - | - | 0.914 | 0.968 | 0.162 | 1.34x | 14.3/24.5/28.5% | 2.1/5.2% | 3 |
| 1 | 1 | 0.758 | 0.736 | 0.022 | - | - | 0.957 | 0.971 | 0.118 | 1.31x | 13.9/24.1/28.0% | 2.0/5.2% | 3 |
| 2 | 1 | 0.769 | 0.749 | 0.019 | - | - | 0.970 | 0.970 | 0.141 | 1.33x | 14.1/24.4/28.3% | 2.0/5.3% | 3 |
| 4 | 1 | 0.772 | 0.753 | 0.019 | - | - | 0.976 | 0.977 | 0.132 | 1.33x | 14.3/24.4/28.5% | 2.1/5.3% | 3 |

> sr-retries=0: decode_failures 15

> slower: 3.64 s per simulated hour against 1.59 over 38 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.761 | 0.738 | 0.023 | - | - | 0.965 | 0.967 | 0.145 | 1.41x | 15.0/25.7/30.0% | 2.2/5.6% | 3 |
| 24 | 1 | 0.762 | 0.739 | 0.023 | - | - | 0.962 | 0.968 | 0.157 | 1.42x | 15.1/25.8/30.2% | 2.2/5.7% | 3 |
| 32 | 1 | 0.760 | 0.737 | 0.023 | - | - | 0.964 | 0.972 | 0.135 | 1.42x | 15.0/25.7/30.0% | 2.2/5.7% | 3 |
| 64 | 1 | 0.766 | 0.744 | 0.022 | - | - | 0.967 | 0.970 | 0.142 | 1.44x | 15.3/26.2/30.6% | 2.2/5.8% | 3 |

> short-id-bits=16: decode_failures 1

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.762 | 0.743 | 0.019 | - | - | 0.963 | 0.975 | 0.153 | 1.49x | 15.9/27.0/31.3% | 2.3/5.9% | 3 |
| 16 | 1 | 0.758 | 0.734 | 0.024 | - | - | 0.959 | 0.965 | 0.149 | 1.44x | 15.3/26.2/30.5% | 2.2/5.8% | 3 |
| 32 | 1 | 0.775 | 0.751 | 0.024 | - | - | 0.971 | 0.978 | 0.164 | 1.40x | 14.8/25.4/29.6% | 2.1/5.6% | 3 |

> window-size=8: misdecodes 113

> window-size=16: misdecodes 64

> window-size=32: misdecodes 16

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.986 | 0.987 | 0.519 | 2.16x | 18.5/32.3/39.5% | 1.5/5.2% | 3 |
| True | 1 | 0.638 | 0.631 | 0.007 | - | - | 0.848 | 0.905 | 0.357 | 5.60x | 45.5/67.5/76.1% | 3.9/12.2% | 3 |

> no-congestion-scaling=True: decode_failures 65

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.319 | 0.313 | 0.006 | - | - | 0.510 | 0.526 | 0.083 | 4.39x | 12.2/17.8/23.9% | 1.6/4.0% | 3 |
| truesize | 1 | 0.347 | 0.341 | 0.006 | - | - | 0.546 | 0.556 | 0.100 | 2.50x | 6.9/11.2/15.1% | 0.9/3.0% | 3 |

> congestion-input=hotstore: decode_failures 25

> congestion-input=truesize: decode_failures 19

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.880 | 0.876 | 0.004 | - | - | 0.988 | 0.988 | 0.520 | 1.96x | 17.0/29.4/36.3% | 1.3/4.7% | 3 |
| adaptive | 1 | 0.869 | 0.864 | 0.005 | - | - | 0.986 | 0.987 | 0.519 | 2.16x | 18.5/32.3/39.5% | 1.5/5.2% | 3 |

