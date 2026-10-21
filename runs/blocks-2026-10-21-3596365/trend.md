# Sweep blocks-2026-10-21-3596365

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** flat
- **seed base** 3596365 · seeds 3596365
- **blocks** 87 run
- **compute** 10.6 h of simulator time across every cell
- **generated** 2026-10-21T08:45:47+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>118 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 9
- AD-badrouters: role-placement=inverse: decode_failures 22
- AD-badrouters: role-placement=random: decode_failures 14
- AD-siting: siting-mix=local-typical: decode_failures 5
- BL-control: protocol=sr: decode_failures 22
- BL-control: slower: 4.49 s per simulated hour against 1.81 over 61 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 37
- DB-hotstore-stress: max-num-nodes=120: decode_failures 19
- DB-hotstore-stress: max-num-nodes=250: decode_failures 4
- DB-warm: warm-num-nodes=0: decode_failures 86
- DB-warm: warm-num-nodes=25: decode_failures 86
- DB-warm: warm-num-nodes=100: decode_failures 86
- DB-warm: warm-num-nodes=2000: decode_failures 86
- DG-burst: burst-loss=0.1: decode_failures 7
- DG-burst: burst-loss=0.2: decode_failures 20
- DG-burst: burst-loss=0.3: decode_failures 17
- DG-loss: extra-loss=0.1: decode_failures 28
- DG-loss: extra-loss=0.2: decode_failures 25
- DG-loss: extra-loss=0.3: decode_failures 24
- DG-loss: slower: 6.23 s per simulated hour against 2.27 over 61 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.1: decode_failures 28
- DG-outage: burst-loss=0.2: decode_failures 22
- DG-outage: burst-loss=0.3: decode_failures 19
- DM-mode: dm-mode=flood-only: decode_failures 27
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 28
- DM-mode: dm-mode=m4-early-flood: decode_failures 26
- DM-mode: slower: 9.99 s per simulated hour against 3.06 over 61 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.25: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 14
- LD-chatty: broadcast-interval-s=900: decode_failures 22
- LD-chatty: broadcast-interval-s=300: decode_failures 20
- LD-diurnal: diurnal=sinusoid: decode_failures 1
- LD-interval: broadcast-interval-s=900: decode_failures 22
- LD-traceroute: traceroute-per-hour=4.0: decode_failures 26
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 86
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 90
- MS-density: nodes=40: decode_failures 14
- MS-hopscale: nodes=250: decode_failures 12
- MS-hopscale: nodes=500: decode_failures 53
- MS-oversubscribed: nodes=250: decode_failures 19
- MS-oversubscribed: nodes=500: decode_failures 12
- MS-oversubscribed: faster: 9.19 s per simulated hour against 19.7 over 61 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-siting: siting-mix=local-typical: decode_failures 12
- MS-siting: siting-mix=event: decode_failures 4
- MS-size: nodes=150: decode_failures 43
- MS-stretch: stretch=1.25: decode_failures 30
- MS-stretch: stretch=1.5: decode_failures 1
- PR-crladder: coding-rate-ladder=False: decode_failures 28
- PR-crladder: coding-rate-ladder=True: decode_failures 20
- PR-crladder: slower: 8.91 s per simulated hour against 2.75 over 61 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 20
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 27
- PR-dmmode-cr: slower: 7.4 s per simulated hour against 2.55 over 61 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-repeats: extra-repeats=True: decode_failures 4
- RF-noise: noise-profile=temporal: decode_failures 23
- RF-noise: noise-profile=transient: decode_failures 14
- RF-noise: noise-profile=periodic: decode_failures 12
- RF-preset: preset=LONG_MODERATE: decode_failures 48
- RF-preset: slower: 5.98 s per simulated hour against 2.85 over 61 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 8
- RF-pulse: noise-pulse-interval-ms=30000: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 12
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 1
- RF-txpower: tx-power=22: decode_failures 6
- RT-hoplimit: hop-limit=3: decode_failures 6
- RT-hopspread: hop-limit=3: decode_failures 6
- RT-spread: hop-spread=False: decode_failures 6
- SC-signing: signature-policy=STRICT: decode_failures 17
- SF-bucket-mode: bucket-mode=global: misdecodes 16
- SF-bucket-mode: bucket-mode=time: misdecodes 11
- SF-bucket-mode: bucket-mode=window: misdecodes 5
- SF-bucket-time: time-bucket-s=600: misdecodes 71
- SF-bucket-time: time-bucket-s=1800: misdecodes 11
- SF-bucket-time: time-bucket-s=3600: misdecodes 2
- SF-cadence: trigger=interval: misdecodes 2
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 11
- SF-cadence: trigger=bucket+interval: misdecodes 3
- SF-capacity-local: capacity=4: decode_failures 71
- SF-capacity-local: capacity=8: decode_failures 72
- SF-capacity-local: capacity=16: decode_failures 57
- SF-capacity: capacity=4: decode_failures 71
- SF-capacity: capacity=8: decode_failures 72
- SF-capacity: capacity=16: decode_failures 57
- SF-capacity-window: capacity=8: misdecodes 1
- SF-capacity-window: capacity=8: decode_failures 88
- SF-capacity-window: capacity=16: misdecodes 4
- SF-capacity-window: capacity=16: decode_failures 25
- SF-capacity-window: capacity=32: misdecodes 5
- SF-catchup: catch-up-hours=: misdecodes 3
- SF-catchup: catch-up-hours=02-06: decode_failures 45
- SF-catchup: catch-up-hours=00-08: decode_failures 43
- SF-hops-flat: hops-apart=3: decode_failures 22
- SF-hops-flat: hops-apart=4: decode_failures 39
- SF-hops-spread: hops-apart=3: decode_failures 22
- SF-hops-spread: hops-apart=4: decode_failures 39
- SF-hops-spread: hops-apart=5: decode_failures 34
- SF-jitter-global: advert-jitter-s=120: decode_failures 1
- SF-jitter-local: advert-jitter-s=120: decode_failures 1
- SF-place-flat: place=routers: decode_failures 16
- SF-place-spread: place=routers: decode_failures 16
- SF-provide-transport: provide-transport=broadcast: decode_failures 13
- SF-replay-order-broadcast: replay-ordering=tip: decode_failures 13
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 15
- SF-replay-order-broadcast: slower: 5.87 s per simulated hour against 1.69 over 61 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-replay-order: replay-ordering=heard: misdecodes 4
- SF-replay-order: replay-ordering=heard: decode_failures 6
- SF-servers-allrouters: servers=3: decode_failures 16
- SF-servers-allrouters: slower: 3.96 s per simulated hour against 1.83 over 61 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-sr-retries: sr-retries=0: decode_failures 8
- SF-window-size: window-size=8: misdecodes 89
- SF-window-size: window-size=16: misdecodes 24
- SF-window-size: window-size=32: misdecodes 5
- TH-congestion-input: congestion-input=hotstore: decode_failures 19
- TH-congestion-input: congestion-input=truesize: decode_failures 1
- TH-congestion: no-congestion-scaling=True: decode_failures 93

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `SF-replay-order-broadcast` | 5.87 | 1.69 | 3.48x | 61 |
| `DM-mode` | 9.99 | 3.06 | 3.26x | 61 |
| `PR-crladder` | 8.91 | 2.75 | 3.24x | 61 |
| `PR-dmmode-cr` | 7.4 | 2.55 | 2.91x | 61 |
| `DG-loss` | 6.23 | 2.27 | 2.74x | 61 |
| `BL-control` | 4.49 | 1.81 | 2.48x | 61 |
| `SF-servers-allrouters` | 3.96 | 1.83 | 2.16x | 61 |
| `RF-preset` | 5.98 | 2.85 | 2.10x | 61 |
| `SF-provide-transport` | 3.49 | 1.77 | 1.97x | 61 |
| `LD-traceroute` | 4.06 | 2.1 | 1.93x | 61 |
| `RT-spread` | 3.66 | 2.16 | 1.70x | 61 |
| `AD-badrouters` | 2.98 | 1.86 | 1.60x | 61 |
| `AD-amplify-worst` | 2.84 | 1.83 | 1.55x | 61 |
| `SF-hops-spread` | 6.99 | 4.52 | 1.55x | 61 |
| `SF-hops-flat` | 6.12 | 3.96 | 1.55x | 61 |
| `SC-signing` | 2.74 | 1.79 | 1.53x | 61 |
| `MS-size` | 5.14 | 3.38 | 1.52x | 61 |
| `SF-capacity` | 2.58 | 1.7 | 1.51x | 61 |
| `PR-repeats` | 2.5 | 1.65 | 1.51x | 61 |
| `MS-roles` | 1.12 | 1.7 | 0.66x | 61 |
| `LD-chatty-hops` | 2.62 | 4.05 | 0.65x | 61 |
| `RF-stretch-duct` | 1.12 | 1.84 | 0.61x | 61 |
| `RT-adopt` | 2.21 | 3.91 | 0.56x | 61 |
| `RT-favourites` | 0.901 | 1.66 | 0.54x | 61 |
| `SF-place-flat` | 1.55 | 2.86 | 0.54x | 61 |
| `RF-bw500` | 1.04 | 1.95 | 0.53x | 61 |
| `DG-outage` | 3.73 | 7.08 | 0.53x | 61 |
| `MS-oversubscribed` | 9.19 | 19.7 | 0.47x | 61 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `MS-siting` | siting-mix | **held** | 0.073 → 0.998 | 0.925 | 0.063 → 0.967 | 14x advert_bytes | up | 4 |
| `PR-protocol` | protocol | **held** | 0 → 0.871 | 0.871 | 0.612 → 0.614 | 1.1x bytes_on_air | up | 3 |
| `MS-stretch` | stretch | **held** | 0.034 → 0.871 | 0.837 | 0.049 → 0.614 | 51x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.059 → 0.871 | 0.812 | 0.036 → 0.614 | 16x advert_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.063 → 0.871 | 0.808 | 0.029 → 0.632 | 16x advert_bytes | up | 5 |
| `BL-control` | protocol | **held** | 0 → 0.791 | 0.791 | 0.612 → 0.614 | 1x bytes_on_air | up | 2 |
| `AD-siting` | siting-mix | **held** | 0.033 → 0.813 | 0.780 | 0.013 → 0.575 | 45x advert_bytes | down | 3 |
| `RF-eu-presets` | preset | **held** | 0.092 → 0.871 | 0.778 | 0.131 → 0.614 | 11x advert_bytes | up | 4 |
| `RF-preset` | preset | **held** | 0.092 → 0.871 | 0.778 | 0.131 → 0.625 | 16x sr_airtime | up | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.065 → 0.803 | 0.738 | 0.057 → 0.563 | 2.2e+02x sr_airtime | down | 4 |
| `SF-place-flat` | place | **held** | 0.167 → 0.871 | 0.704 | 0.614 → 0.624 | 22x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.167 → 0.871 | 0.704 | 0.614 → 0.624 | 22x sr_bytes | up | 6 |
| `RF-bw500` | preset | **held** | 0.063 → 0.765 | 0.702 | 0.062 → 0.495 | 14x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.294 → 0.871 | 0.577 | 0.185 → 0.614 | 7.7x bytes_on_air | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **held** | 0.133 → 0.650 | 0.517 | 0.171 → 0.632 | 7.8x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.391 → 0.889 | 0.498 | 0.378 → 0.888 | 2.7x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.428 → 0.922 | 0.494 | 0.419 → 0.919 | 7.4x advert_bytes | up | 5 |
| `MS-size` | nodes | **held** | 0.573 → 0.931 | 0.358 | 0.422 → 0.614 | 8.3x sr_bytes | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.500 → 0.837 | 0.337 | 0.462 → 0.834 | 2.6x sr_bytes | up | 4 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.563 → 0.894 | 0.331 | 0.368 → 0.669 | 7.9x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **held** | 0.543 → 0.871 | 0.328 | 0.326 → 0.614 | 1.6x advert_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.188 → 0.503 | 0.315 | 0.186 → 0.497 | 4.4x bytes_on_air | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.516 → 0.823 | 0.307 | 0.495 → 0.819 | 6.2x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **held** | 0.575 → 0.871 | 0.296 | 0.341 → 0.614 | 1.5x advert_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.500 → 0.785 | 0.285 | 0.462 → 0.779 | 2.1x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.635 → 0.907 | 0.272 | 0.614 → 0.897 | 1.6x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.643 → 0.880 | 0.238 | 0.635 → 0.878 | 3.8x sr_airtime | down | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.635 → 0.862 | 0.227 | 0.614 → 0.842 | 1.6x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.660 → 0.871 | 0.210 | 0.455 → 0.614 | 1.4x sr_bytes | down | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.635 → 0.844 | 0.209 | 0.614 → 0.839 | 2x sr_bytes | up | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.669 → 0.871 | 0.202 | 0.612 → 0.625 | 1.9x sr_bytes | down | 5 |
| `DG-loss` | extra-loss | **held** | 0.678 → 0.871 | 0.192 | 0.462 → 0.614 | 1.3x advert_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.350 → 0.528 | 0.178 | 0.201 → 0.293 | 3.6x sr_airtime | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.588 → 0.748 | 0.160 | 0.575 → 0.736 | 2.1x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.588 → 0.748 | 0.160 | 0.575 → 0.736 | 2.1x bytes_on_air | up | 3 |
| `AD-badrouters` | role-placement | **held** | 0.688 → 0.840 | 0.152 | 0.440 → 0.575 | 1.8x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.500 → 0.635 | 0.135 | 0.462 → 0.614 | 1.5x sr_bytes | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.738 → 0.871 | 0.133 | 0.614 → 0.629 | 25x sr_airtime | down | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.617 → 0.742 | 0.124 | 0.606 → 0.728 | 2.2x bytes_on_air | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.579 → 0.703 | 0.124 | 0.557 → 0.693 | 5.4x sr_airtime | up | 4 |
| `SC-signing` | signature-policy | **held** | 0.748 → 0.871 | 0.122 | 0.523 → 0.614 | 1.4x sr_airtime | down | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.750 → 0.871 | 0.121 | 0.612 → 0.624 | 1.9x sr_bytes | down | 4 |
| `FW-versions` | profile | **text** | 0.635 → 0.747 | 0.111 | 0.614 → 0.735 | 3.1x bytes_on_air | down | 5 |
| `SF-capacity-window` | capacity | **held** | 0.770 → 0.879 | 0.109 | 0.622 → 0.627 | 3.5x sr_bytes | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.623 → 0.728 | 0.105 | 0.605 → 0.718 | 1.9x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.626 → 0.728 | 0.103 | 0.607 → 0.718 | 1.8x sr_airtime | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.629 → 0.726 | 0.098 | 0.614 → 0.709 | 2.2x bytes_on_air | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.812 → 0.906 | 0.094 | 0.635 → 0.695 | 1.1x sr_airtime | down | 2 |
| `FW-firmware` | profile | **text** | 0.635 → 0.721 | 0.086 | 0.614 → 0.709 | 3x bytes_on_air | down | 2 |
| `MS-roles` | role-mix | **held** | 0.813 → 0.898 | 0.085 | 0.575 → 0.653 | 1.1x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.791 → 0.871 | 0.080 | 0.590 → 0.623 | 14x advert_bytes | down | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.660 → 0.725 | 0.065 | 0.643 → 0.714 | 1.2x sr_bytes | up | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.841 → 0.899 | 0.058 | 0.576 → 0.628 | 1.4x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.635 → 0.692 | 0.057 | 0.614 → 0.681 | 3.3x bytes_on_air | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.635 → 0.690 | 0.055 | 0.614 → 0.614 | 3.3x sr_airtime | up | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.511 → 0.566 | 0.054 | 0.290 → 0.322 | 2x sr_airtime | up | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.871 → 0.924 | 0.053 | 0.614 → 0.666 | 1.4x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.818 → 0.871 | 0.053 | 0.573 → 0.614 | 1.3x sr_airtime | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.829 → 0.874 | 0.045 | 0.615 → 0.617 | 2.1x advert_bytes | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.635 → 0.675 | 0.040 | 0.614 → 0.662 | 1.2x sr_bytes | up | 4 |
| `SF-resolve` | resolve | **held** | 0.831 → 0.871 | 0.040 | 0.614 → 0.618 | 6x advert_bytes | = | 3 |
| `LD-diurnal` | diurnal | **text** | 0.635 → 0.669 | 0.033 | 0.614 → 0.652 | 1.4x sr_bytes | down | 3 |
| `AD-worst` | role-placement | **text** | 0.730 → 0.761 | 0.031 | 0.711 → 0.749 | 1.3x sr_bytes | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.858 → 0.888 | 0.030 | 0.612 → 0.627 | 6.9x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.858 → 0.888 | 0.030 | 0.612 → 0.627 | 6.9x sr_bytes | up | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.815 → 0.845 | 0.030 | 0.590 → 0.627 | 9.1x advert_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.848 → 0.874 | 0.026 | 0.614 → 0.629 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.848 → 0.874 | 0.026 | 0.614 → 0.629 | 5.4x advert_bytes | up | 5 |
| `SF-sr-retries` | sr-retries | **held** | 0.846 → 0.871 | 0.025 | 0.628 → 0.642 | 1.1x sr_bytes | up | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.857 → 0.879 | 0.022 | 0.614 → 0.626 | 3x advert_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.857 → 0.879 | 0.021 | 0.618 → 0.626 | 4.8x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **text** | 0.584 → 0.599 | 0.016 | 0.584 → 0.599 | 1.2x sr_airtime | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.865 → 0.880 | 0.015 | 0.862 → 0.878 | 1.2x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.625 → 0.640 | 0.015 | 0.606 → 0.625 | 5.3x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.635 → 0.648 | 0.013 | 0.614 → 0.631 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.635 → 0.648 | 0.013 | 0.614 → 0.631 | 1.1x sr_airtime | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.635 → 0.646 | 0.011 | 0.614 → 0.630 | 1.1x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.861 → 0.872 | 0.010 | 0.614 → 0.625 | 3.1x advert_bytes | down | 4 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.777 → 0.787 | 0.010 | 0.594 → 0.596 | 1.1x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.768 → 0.777 | 0.009 | 0.596 → 0.604 | 1.3x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.880 → 0.889 | 0.009 | 0.878 → 0.888 | 1.1x bytes_on_air | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.635 → 0.644 | 0.009 | 0.614 → 0.625 | 2x advert_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.864 → 0.871 | 0.007 | 0.614 → 0.626 | 1.1x sr_bytes | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.684 → 0.690 | 0.006 | 0.612 → 0.614 | 1.1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.880 → 0.884 | 0.003 | 0.878 → 0.882 | 1.1x sr_airtime | up | 2 |

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
| none | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| sprinkled | 1 | 0.681 | 0.666 | 0.015 | - | - | 0.846 | 0.849 | 0.116 | 1.13x | 13.2/17.8/21.1% | 1.8/4.7% | 3 |
| arms-race | 1 | 0.844 | 0.839 | 0.005 | - | - | 0.902 | 0.902 | 0.106 | 1.03x | 17.3/22.7/25.3% | 1.1/5.1% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario flat`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.750 | 0.724 | 0.027 | - | - | 0.786 | 0.803 | 0.479 | 1.36x | 14.9/21.6/26.5% | 2.2/5.0% | 3 |
| 0.3 | 1 | 0.907 | 0.897 | 0.010 | - | - | 0.981 | 0.983 | 0.707 | 1.18x | 18.9/24.5/28.5% | 1.7/4.9% | 3 |

> amplify-worst=0.1: decode_failures 9

### `AD-badrouters` - role-placement  `--scenario flat`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.588 | 0.575 | 0.013 | - | - | 0.813 | 0.816 | 0.000 | 1.16x | 11.1/18.1/22.5% | 1.9/5.0% | 3 |
| inverse | 1 | 0.459 | 0.440 | 0.019 | - | - | 0.688 | 0.733 | 0.000 | 1.03x | 9.6/14.6/19.0% | 1.8/3.4% | 3 |
| random | 1 | 0.591 | 0.570 | 0.022 | - | - | 0.840 | 0.864 | 0.000 | 1.08x | 10.2/17.3/20.0% | 1.7/3.7% | 3 |

> role-placement=inverse: decode_failures 22

> role-placement=random: decode_failures 14

### `AD-flooding` - role-mix  `--scenario flat`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.588 | 0.575 | 0.013 | - | - | 0.813 | 0.816 | 0.000 | 1.16x | 11.1/18.1/22.5% | 1.9/5.0% | 3 |
| all-routers | 1 | 0.748 | 0.736 | 0.011 | - | - | 0.913 | 0.917 | 0.000 | 2.38x | 20.2/28.1/34.1% | 3.9/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario flat`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.588 | 0.575 | 0.013 | - | - | 0.813 | 0.816 | 0.000 | 1.16x | 11.1/18.1/22.5% | 1.9/5.0% | 3 |
| no-mute | 1 | 0.628 | 0.611 | 0.017 | - | - | 0.849 | 0.854 | 0.000 | 1.24x | 11.7/17.1/21.7% | 2.0/4.2% | 3 |
| all-routers | 1 | 0.748 | 0.736 | 0.011 | - | - | 0.913 | 0.917 | 0.000 | 2.38x | 20.2/28.1/34.1% | 3.9/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario flat`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.588 | 0.575 | 0.013 | - | - | 0.813 | 0.816 | 0.000 | 1.16x | 11.1/18.1/22.5% | 1.9/5.0% | 3 |
| local-typical | 1 | 0.244 | 0.240 | 0.004 | - | - | 0.303 | 0.496 | 0.000 | 1.03x | 5.7/16.5/22.5% | 1.3/5.0% | 3 |
| basement-heavy | 1 | 0.013 | 0.013 | 0.000 | - | - | 0.033 | 0.036 | 0.000 | 0.25x | 0.2/1.9/3.4% | 0.2/1.2% | 3 |

> siting-mix=local-typical: decode_failures 5

### `AD-worst` - role-placement  `--scenario flat`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.761 | 0.749 | 0.012 | - | - | 0.914 | 0.915 | 0.000 | 2.52x | 15.3/27.9/36.1% | 2.0/6.0% | 3 |
| inverse | 1 | 0.730 | 0.711 | 0.019 | - | - | 0.915 | 0.917 | 0.000 | 2.44x | 13.5/24.0/30.7% | 1.9/3.5% | 3 |

### `BL-control` - protocol  `--scenario flat`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.614 | 0.614 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 11.7/18.7/24.8% | 1.9/4.9% | 3 |
| sr | 1 | 0.640 | 0.612 | 0.028 | - | - | 0.791 | 0.850 | 0.000 | 1.30x | 12.3/19.1/25.3% | 1.9/5.0% | 3 |

> protocol=sr: decode_failures 22

> slower: 4.49 s per simulated hour against 1.81 over 61 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario flat`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.626 | 0.607 | 0.019 | - | - | 0.779 | 0.781 | 0.000 | 2.77x | 25.2/39.5/48.8% | 4.1/9.2% | 3 |
| 100 | 1 | 0.728 | 0.718 | 0.011 | - | - | 0.865 | 0.866 | 0.000 | 1.55x | 14.1/22.5/27.8% | 2.2/5.2% | 3 |
| 120 | 1 | 0.728 | 0.718 | 0.011 | - | - | 0.865 | 0.866 | 0.000 | 1.55x | 14.1/22.5/27.8% | 2.2/5.2% | 3 |
| 250 | 1 | 0.728 | 0.718 | 0.011 | - | - | 0.865 | 0.866 | 0.000 | 1.55x | 14.1/22.5/27.8% | 2.2/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario flat`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.205 | 0.201 | 0.005 | - | - | 0.350 | 0.377 | 0.065 | 10.15x | 24.9/40.8/60.3% | 3.6/9.3% | 3 |
| 120 | 1 | 0.298 | 0.290 | 0.007 | - | - | 0.511 | 0.526 | 0.076 | 4.58x | 11.2/19.5/32.6% | 1.6/5.2% | 3 |
| 250 | 1 | 0.300 | 0.293 | 0.008 | - | - | 0.528 | 0.530 | 0.078 | 4.51x | 11.0/19.4/31.9% | 1.6/5.1% | 3 |

> max-num-nodes=10: decode_failures 37

> max-num-nodes=120: decode_failures 19

> max-num-nodes=250: decode_failures 4

### `DB-platform` - platform-mix  `--scenario flat`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.728 | 0.718 | 0.011 | - | - | 0.865 | 0.866 | 0.000 | 1.55x | 14.1/22.5/27.8% | 2.2/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.728 | 0.718 | 0.011 | - | - | 0.865 | 0.866 | 0.000 | 1.55x | 14.1/22.5/27.8% | 2.2/5.2% | 3 |
| constrained | 1 | 0.623 | 0.605 | 0.018 | - | - | 0.776 | 0.786 | 0.000 | 2.76x | 25.1/39.2/48.7% | 4.0/9.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario flat`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.637 | 0.628 | 0.009 | - | - | 0.899 | 0.921 | 0.095 | 5.75x | 49.7/68.2/73.6% | 3.9/12.8% | 3 |
| 25 | 1 | 0.637 | 0.628 | 0.009 | - | - | 0.899 | 0.921 | 0.095 | 5.75x | 49.7/68.2/73.6% | 3.9/12.8% | 3 |
| 100 | 1 | 0.637 | 0.628 | 0.009 | - | - | 0.899 | 0.921 | 0.095 | 5.75x | 49.7/68.2/73.6% | 3.9/12.8% | 3 |
| 2000 | 1 | 0.637 | 0.628 | 0.009 | - | - | 0.899 | 0.921 | 0.095 | 5.75x | 49.7/68.2/73.6% | 3.9/12.8% | 3 |

> warm-num-nodes=0: decode_failures 86

> warm-num-nodes=25: decode_failures 86

> warm-num-nodes=100: decode_failures 86

> warm-num-nodes=2000: decode_failures 86

### `DG-burst` - burst-loss  `--scenario flat`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.543 | 0.519 | 0.024 | - | - | 0.802 | 0.829 | 0.000 | 1.19x | 10.9/18.1/24.1% | 1.7/4.8% | 3 |
| 0.2 | 1 | 0.452 | 0.429 | 0.022 | - | - | 0.669 | 0.765 | 0.000 | 1.08x | 10.0/16.9/22.5% | 1.6/4.2% | 3 |
| 0.3 | 1 | 0.365 | 0.341 | 0.024 | - | - | 0.575 | 0.684 | 0.000 | 1.00x | 9.3/15.6/21.2% | 1.5/3.8% | 3 |

> burst-loss=0.1: decode_failures 7

> burst-loss=0.2: decode_failures 20

> burst-loss=0.3: decode_failures 17

### `DG-loss` - extra-loss  `--scenario flat`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.584 | 0.566 | 0.018 | - | - | 0.813 | 0.841 | 0.000 | 1.30x | 11.9/19.6/25.6% | 1.9/5.1% | 3 |
| 0.2 | 1 | 0.545 | 0.527 | 0.018 | - | - | 0.776 | 0.826 | 0.000 | 1.31x | 12.0/19.7/25.7% | 1.9/4.9% | 3 |
| 0.3 | 1 | 0.477 | 0.462 | 0.016 | - | - | 0.678 | 0.787 | 0.000 | 1.28x | 11.8/19.4/25.5% | 1.9/4.6% | 3 |

> extra-loss=0.1: decode_failures 28

> extra-loss=0.2: decode_failures 25

> extra-loss=0.3: decode_failures 24

> slower: 6.23 s per simulated hour against 2.27 over 61 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario flat`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.538 | 0.519 | 0.019 | - | - | 0.738 | 0.831 | 0.000 | 1.23x | 11.1/18.3/24.7% | 1.8/4.7% | 3 |
| 0.2 | 1 | 0.426 | 0.411 | 0.015 | - | - | 0.607 | 0.751 | 0.000 | 1.10x | 10.1/17.0/23.2% | 1.6/4.6% | 3 |
| 0.3 | 1 | 0.342 | 0.326 | 0.016 | - | - | 0.543 | 0.671 | 0.000 | 1.02x | 9.7/15.8/21.7% | 1.6/4.0% | 3 |

> burst-loss=0.1: decode_failures 28

> burst-loss=0.2: decode_failures 22

> burst-loss=0.3: decode_failures 19

### `DM-mode` - dm-mode  `--scenario flat`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.584 | 0.584 | 0.000 | - | - | 0.776 | 0.843 | 0.000 | 1.56x | 14.1/23.8/31.0% | 2.3/6.3% | 3 |
| directed-with-late-flood | 1 | 0.594 | 0.594 | 0.000 | - | - | 0.787 | 0.861 | 0.000 | 1.46x | 13.4/22.4/29.8% | 2.1/6.1% | 3 |
| m4-early-flood | 1 | 0.599 | 0.599 | 0.000 | - | - | 0.779 | 0.864 | 0.000 | 1.46x | 13.4/22.3/29.5% | 2.1/6.1% | 3 |

> dm-mode=flood-only: decode_failures 27

> dm-mode=directed-with-late-flood: decode_failures 28

> dm-mode=m4-early-flood: decode_failures 26

> slower: 9.99 s per simulated hour against 3.06 over 61 prior run(s) - 3.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario flat`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.721 | 0.709 | 0.011 | - | - | 0.902 | 0.904 | 0.168 | 0.75x | 6.8/9.7/10.8% | 1.2/2.5% | 3 |
| 2.8 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario flat`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.617 | 0.606 | 0.012 | - | - | 0.912 | 0.917 | 0.000 | 1.22x | 11.7/17.7/23.2% | 1.8/5.1% | 3 |
| 0.5 | 1 | 0.742 | 0.728 | 0.013 | - | - | 0.920 | 0.921 | 0.380 | 1.04x | 9.0/14.7/18.6% | 1.6/4.1% | 3 |
| 0.75 | 1 | 0.689 | 0.675 | 0.013 | - | - | 0.897 | 0.900 | 0.053 | 0.85x | 8.2/12.2/14.1% | 1.4/3.2% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario flat`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.629 | 0.618 | 0.011 | - | - | 0.904 | 0.918 | 0.000 | 1.21x | 11.5/17.5/23.1% | 1.8/5.1% | 3 |
| 0.5 | 1 | 0.726 | 0.709 | 0.017 | - | - | 0.917 | 0.922 | 0.397 | 1.02x | 9.1/14.5/18.5% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.708 | 0.694 | 0.014 | - | - | 0.912 | 0.914 | 0.045 | 0.83x | 8.2/12.1/14.4% | 1.3/3.3% | 3 |

> legacy-fraction=0.25: decode_failures 1

### `FW-signing-cost` - profile-flag  `--scenario flat`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.692 | 0.681 | 0.011 | - | - | 0.899 | 0.904 | 0.000 | 0.71x | 6.5/11.5/15.5% | 1.0/3.2% | 3 |
| signing=true | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

### `FW-versions` - profile  `--scenario flat`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.715 | 0.703 | 0.013 | - | - | 0.875 | 0.878 | 0.187 | 0.75x | 7.1/9.9/11.6% | 1.2/3.0% | 3 |
| 2.5 | 1 | 0.723 | 0.710 | 0.013 | - | - | 0.891 | 0.891 | 0.175 | 0.75x | 6.9/9.8/11.3% | 1.3/2.9% | 3 |
| 2.6 | 1 | 0.731 | 0.720 | 0.011 | - | - | 0.906 | 0.907 | 0.167 | 0.74x | 7.0/9.8/11.6% | 1.2/2.9% | 3 |
| 2.7 | 1 | 0.747 | 0.735 | 0.011 | - | - | 0.911 | 0.912 | 0.193 | 0.76x | 7.3/11.1/12.1% | 1.2/3.2% | 3 |
| 2.8 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.683 | 0.669 | 0.014 | - | - | 0.894 | 0.900 | 0.000 | 0.83x | 7.6/12.4/16.6% | 1.2/3.5% | 3 |
| 900 | 1 | 0.579 | 0.557 | 0.022 | - | - | 0.796 | 0.816 | 0.000 | 1.95x | 18.0/29.5/38.3% | 2.9/7.9% | 3 |
| 300 | 1 | 0.389 | 0.368 | 0.021 | - | - | 0.563 | 0.659 | 0.000 | 4.25x | 37.4/57.7/69.2% | 6.5/14.5% | 3 |

> broadcast-interval-s=900: decode_failures 22

> broadcast-interval-s=300: decode_failures 20

### `LD-chatty-hops` - broadcast-interval-s  `--scenario flat`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.823 | 0.819 | 0.004 | - | - | 0.947 | 0.949 | 0.000 | 1.00x | 8.8/13.4/17.8% | 1.5/3.5% | 3 |
| 900 | 1 | 0.744 | 0.733 | 0.011 | - | - | 0.900 | 0.903 | 0.000 | 2.31x | 20.5/31.9/41.1% | 3.6/8.2% | 3 |
| 300 | 1 | 0.516 | 0.495 | 0.021 | - | - | 0.739 | 0.764 | 0.000 | 4.91x | 42.6/63.5/72.5% | 7.7/15.9% | 3 |

> broadcast-interval-s=300: decode_failures 14

### `LD-diurnal` - diurnal  `--scenario flat`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.669 | 0.652 | 0.017 | - | - | 0.888 | 0.897 | 0.000 | 1.19x | 11.0/17.8/23.7% | 1.8/5.0% | 3 |
| sinusoid | 1 | 0.653 | 0.636 | 0.018 | - | - | 0.867 | 0.872 | 0.000 | 1.15x | 10.6/17.2/23.0% | 1.7/4.7% | 3 |
| commuter | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

> diurnal=sinusoid: decode_failures 1

### `LD-interval` - broadcast-interval-s  `--scenario flat`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.579 | 0.557 | 0.022 | - | - | 0.796 | 0.816 | 0.000 | 1.95x | 18.0/29.5/38.3% | 2.9/7.9% | 3 |
| 3600 | 1 | 0.683 | 0.669 | 0.014 | - | - | 0.894 | 0.900 | 0.000 | 0.83x | 7.6/12.4/16.6% | 1.2/3.5% | 3 |
| 10800 | 1 | 0.693 | 0.680 | 0.013 | - | - | 0.906 | 0.907 | 0.000 | 0.54x | 5.0/8.3/11.0% | 0.8/2.4% | 3 |
| 43200 | 1 | 0.703 | 0.693 | 0.010 | - | - | 0.912 | 0.914 | 0.000 | 0.36x | 3.3/5.5/7.4% | 0.5/1.7% | 3 |

> broadcast-interval-s=900: decode_failures 22

### `LD-traceroute` - traceroute-per-hour  `--scenario flat`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.631 | 0.613 | 0.018 | - | - | 0.860 | 0.863 | 0.000 | 1.33x | 12.3/20.2/26.6% | 2.0/5.5% | 3 |
| 1.0 | 1 | 0.622 | 0.602 | 0.020 | - | - | 0.858 | 0.859 | 0.000 | 1.44x | 13.3/21.8/28.9% | 2.1/6.0% | 3 |
| 4.0 | 1 | 0.594 | 0.573 | 0.021 | - | - | 0.818 | 0.841 | 0.000 | 1.71x | 16.0/26.6/35.2% | 2.5/7.2% | 3 |

> traceroute-per-hour=4.0: decode_failures 26

### `LD-traceroute-small` - traceroute-per-hour  `--scenario flat`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.637 | 0.628 | 0.009 | - | - | 0.899 | 0.921 | 0.095 | 5.75x | 49.7/68.2/73.6% | 3.9/12.8% | 3 |
| 1.0 | 1 | 0.583 | 0.576 | 0.008 | - | - | 0.841 | 0.891 | 0.095 | 6.29x | 53.6/70.9/76.0% | 4.3/13.6% | 3 |

> traceroute-per-hour=0.0: decode_failures 86

> traceroute-per-hour=1.0: decode_failures 90

### `MS-density` - nodes  `--scenario flat`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.428 | 0.419 | 0.009 | - | - | 0.551 | 0.599 | 0.000 | 0.93x | 11.1/17.6/18.9% | 2.5/5.0% | 3 |
| 60 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 90 | 1 | 0.805 | 0.801 | 0.004 | - | - | 0.939 | 0.940 | 0.573 | 1.65x | 12.7/25.1/26.6% | 1.6/5.0% | 3 |
| 120 | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.981 | 0.981 | 0.095 | 2.11x | 19.5/29.7/33.9% | 1.4/5.4% | 3 |
| 150 | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.997 | 0.997 | 0.692 | 2.63x | 23.3/34.5/39.6% | 1.4/5.6% | 3 |

> nodes=40: decode_failures 14

### `MS-hopscale` - nodes  `--scenario flat`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 120 | 1 | 0.507 | 0.502 | 0.005 | - | - | 0.573 | 0.573 | 0.065 | 2.26x | 11.1/20.5/25.8% | 1.6/5.3% | 3 |
| 250 | 1 | 0.296 | 0.289 | 0.007 | - | - | 0.520 | 0.525 | 0.074 | 4.86x | 11.9/21.0/34.5% | 1.7/5.5% | 3 |
| 500 | 1 | 0.187 | 0.185 | 0.002 | - | - | 0.294 | 0.299 | 0.052 | 9.71x | 12.5/20.6/39.2% | 1.8/4.9% | 3 |

> nodes=250: decode_failures 12

> nodes=500: decode_failures 53

### `MS-oversubscribed` - nodes  `--scenario flat`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.503 | 0.497 | 0.006 | - | - | 0.566 | 0.567 | 0.069 | 2.10x | 10.3/18.5/23.1% | 1.5/4.8% | 3 |
| 250 | 1 | 0.298 | 0.290 | 0.007 | - | - | 0.511 | 0.526 | 0.076 | 4.58x | 11.2/19.5/32.6% | 1.6/5.2% | 3 |
| 500 | 1 | 0.188 | 0.186 | 0.002 | - | - | 0.305 | 0.306 | 0.052 | 9.21x | 11.9/19.6/37.1% | 1.7/4.5% | 3 |

> nodes=250: decode_failures 19

> nodes=500: decode_failures 12

> faster: 9.19 s per simulated hour against 19.7 over 61 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-roles` - role-mix  `--scenario flat`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.665 | 0.653 | 0.013 | - | - | 0.898 | 0.901 | 0.000 | 1.28x | 11.6/19.4/25.6% | 1.9/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.588 | 0.575 | 0.013 | - | - | 0.813 | 0.816 | 0.000 | 1.16x | 11.1/18.1/22.5% | 1.9/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario flat`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.708 | 0.695 | 0.013 | - | - | 0.906 | 0.906 | 0.000 | 1.34x | 11.8/19.7/25.8% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.646 | 0.635 | 0.011 | - | - | 0.812 | 0.812 | 0.000 | 1.28x | 12.5/20.2/24.8% | 2.2/4.9% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario flat`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.05 | 1 | 0.653 | 0.635 | 0.017 | - | - | 0.857 | 0.858 | 0.000 | 1.37x | 12.1/20.1/29.8% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.658 | 0.644 | 0.014 | - | - | 0.869 | 0.875 | 0.000 | 1.43x | 12.9/22.0/30.8% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.675 | 0.662 | 0.013 | - | - | 0.868 | 0.871 | 0.000 | 1.57x | 15.0/22.7/31.0% | 2.4/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario flat`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| local-typical | 1 | 0.274 | 0.262 | 0.012 | - | - | 0.498 | 0.544 | 0.000 | 1.32x | 8.5/16.6/22.0% | 2.2/5.3% | 3 |
| event | 1 | 0.064 | 0.063 | 0.000 | - | - | 0.073 | 0.081 | 0.000 | 0.58x | 2.3/4.7/7.9% | 1.0/2.3% | 3 |
| backbone | 1 | 0.967 | 0.967 | 0.001 | - | - | 0.998 | 0.998 | 0.791 | 1.23x | 23.6/30.4/33.4% | 1.6/5.4% | 3 |

> siting-mix=local-typical: decode_failures 12

> siting-mix=event: decode_failures 4

### `MS-size` - nodes  `--scenario flat`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.623 | 0.612 | 0.011 | - | - | 0.843 | 0.845 | 0.000 | 1.13x | 17.4/24.6/31.3% | 2.5/6.6% | 3 |
| 60 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 90 | 1 | 0.625 | 0.609 | 0.016 | - | - | 0.931 | 0.936 | 0.160 | 1.73x | 11.0/23.4/31.6% | 1.5/5.4% | 3 |
| 120 | 1 | 0.507 | 0.502 | 0.005 | - | - | 0.573 | 0.573 | 0.065 | 2.26x | 11.1/20.5/25.8% | 1.6/5.3% | 3 |
| 150 | 1 | 0.430 | 0.422 | 0.008 | - | - | 0.654 | 0.673 | 0.000 | 2.83x | 12.0/19.2/27.6% | 1.7/4.1% | 3 |

> nodes=150: decode_failures 43

### `MS-stretch` - stretch  `--scenario flat`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 1.25 | 1 | 0.369 | 0.356 | 0.013 | - | - | 0.587 | 0.603 | 0.000 | 1.27x | 8.8/15.4/21.6% | 1.9/5.0% | 3 |
| 1.5 | 1 | 0.172 | 0.171 | 0.001 | - | - | 0.133 | 0.134 | 0.000 | 1.05x | 6.1/10.4/13.5% | 1.7/3.5% | 3 |
| 2.0 | 1 | 0.050 | 0.049 | 0.000 | - | - | 0.034 | 0.045 | 0.000 | 0.48x | 2.1/3.4/4.6% | 0.8/1.7% | 3 |

> stretch=1.25: decode_failures 30

> stretch=1.5: decode_failures 1

### `MS-topology` - topology  `--scenario flat`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| clustered | 1 | 0.856 | 0.856 | 0.000 | - | - | 0.971 | 0.971 | 0.000 | 1.14x | 25.9/32.2/35.3% | 1.4/5.8% | 3 |
| corridor | 1 | 0.391 | 0.378 | 0.013 | - | - | 0.526 | 0.530 | 0.251 | 1.40x | 12.3/17.2/23.2% | 2.3/4.4% | 3 |
| hub | 1 | 0.889 | 0.888 | 0.001 | - | - | 0.951 | 0.952 | 0.717 | 1.27x | 20.4/34.6/37.2% | 1.9/5.4% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario flat`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.594 | 0.594 | 0.000 | - | - | 0.787 | 0.861 | 0.000 | 1.46x | 13.4/22.4/29.8% | 2.1/6.1% | 3 |
| True | 1 | 0.596 | 0.596 | 0.000 | - | - | 0.777 | 0.858 | 0.000 | 1.47x | 13.5/22.7/29.7% | 2.1/6.2% | 3 |

> coding-rate-ladder=False: decode_failures 28

> coding-rate-ladder=True: decode_failures 20

> slower: 8.91 s per simulated hour against 2.75 over 61 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario flat`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.596 | 0.596 | 0.000 | - | - | 0.777 | 0.858 | 0.000 | 1.47x | 13.5/22.7/29.7% | 2.1/6.2% | 3 |
| m4-early-flood | 1 | 0.604 | 0.604 | 0.000 | - | - | 0.768 | 0.859 | 0.000 | 1.46x | 13.4/22.4/29.5% | 2.2/6.1% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 20

> dm-mode=m4-early-flood: decode_failures 27

> slower: 7.4 s per simulated hour against 2.55 over 61 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario flat`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.614 | 0.614 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 11.7/18.7/24.8% | 1.9/4.9% | 3 |
| chain | 1 | 0.618 | 0.612 | 0.006 | - | - | 0.755 | 0.869 | 0.000 | 1.39x | 12.4/21.7/28.2% | 2.0/5.9% | 3 |
| sr | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario flat`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| True | 1 | 0.646 | 0.630 | 0.016 | - | - | 0.869 | 0.880 | 0.000 | 1.30x | 12.0/19.3/25.5% | 1.9/5.3% | 3 |

> extra-repeats=True: decode_failures 4

### `PR-repeats-busy` - extra-repeats  `--scenario flat`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.981 | 0.981 | 0.095 | 2.11x | 19.5/29.7/33.9% | 1.4/5.4% | 3 |
| True | 1 | 0.884 | 0.882 | 0.002 | - | - | 0.981 | 0.981 | 0.127 | 2.13x | 19.4/29.8/33.9% | 1.4/5.4% | 3 |

### `RF-bw500` - preset  `--scenario flat`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.062 | 0.062 | 0.000 | - | - | 0.063 | 0.068 | 0.000 | 0.02x | 0.1/0.2/0.3% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.188 | 0.187 | 0.001 | - | - | 0.159 | 0.161 | 0.000 | 0.16x | 1.0/1.7/2.2% | 0.3/0.6% | 3 |
| LONG_TURBO | 1 | 0.505 | 0.495 | 0.009 | - | - | 0.765 | 0.768 | 0.000 | 1.17x | 8.6/15.1/21.3% | 1.6/4.7% | 3 |

### `RF-duct` - duct-per-hour  `--scenario flat`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.660 | 0.641 | 0.020 | - | - | 0.873 | 0.881 | 0.083 | 1.23x | 13.0/20.1/25.9% | 1.8/5.2% | 3 |
| 1.0 | 1 | 0.862 | 0.842 | 0.021 | - | - | 0.951 | 0.952 | 0.609 | 0.91x | 20.9/26.5/29.5% | 1.2/5.1% | 3 |

### `RF-eu-presets` - preset  `--scenario flat`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.131 | 0.131 | 0.000 | - | - | 0.092 | 0.096 | 0.000 | 0.08x | 0.4/0.7/1.0% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| LITE_FAST | 1 | 0.525 | 0.515 | 0.010 | - | - | 0.798 | 0.805 | 0.000 | 0.94x | 7.7/12.7/17.9% | 1.5/3.6% | 3 |
| NARROW_SLOW | 1 | 0.579 | 0.558 | 0.021 | - | - | 0.835 | 0.836 | 0.000 | 1.20x | 10.3/16.3/23.5% | 1.7/4.8% | 3 |

### `RF-noise` - noise-profile  `--scenario flat`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| temporal | 1 | 0.499 | 0.481 | 0.018 | - | - | 0.760 | 0.792 | 0.000 | 1.25x | 11.0/18.7/25.9% | 1.8/5.2% | 3 |
| transient | 1 | 0.630 | 0.609 | 0.020 | - | - | 0.853 | 0.867 | 0.000 | 1.27x | 11.7/19.1/25.2% | 1.9/5.3% | 3 |
| periodic | 1 | 0.471 | 0.455 | 0.016 | - | - | 0.660 | 0.689 | 0.000 | 1.17x | 10.8/17.5/23.2% | 1.8/4.5% | 3 |

> noise-profile=temporal: decode_failures 23

> noise-profile=transient: decode_failures 14

> noise-profile=periodic: decode_failures 12

### `RF-preset` - preset  `--scenario flat`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.131 | 0.131 | 0.000 | - | - | 0.092 | 0.096 | 0.000 | 0.08x | 0.4/0.7/1.0% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| LONG_MODERATE | 1 | 0.651 | 0.625 | 0.026 | - | - | 0.856 | 0.873 | 0.194 | 3.43x | 35.2/52.5/57.2% | 4.6/13.3% | 3 |

> preset=LONG_MODERATE: decode_failures 48

> slower: 5.98 s per simulated hour against 2.85 over 61 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-preset-turbo` - preset  `--scenario flat`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.029 | 0.029 | 0.000 | - | - | 0.122 | 0.146 | 0.000 | 0.01x | 0.0/0.0/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.062 | 0.062 | 0.000 | - | - | 0.063 | 0.068 | 0.000 | 0.02x | 0.1/0.2/0.3% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| LONG_TURBO | 1 | 0.505 | 0.495 | 0.009 | - | - | 0.765 | 0.768 | 0.000 | 1.17x | 8.6/15.1/21.3% | 1.6/4.7% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.650 | 0.632 | 0.018 | - | - | 0.849 | 0.858 | 0.000 | 1.79x | 15.9/24.2/30.4% | 2.7/6.9% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 8

### `RF-pulse` - noise-pulse-interval-ms  `--scenario flat`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.580 | 0.563 | 0.018 | - | - | 0.803 | 0.809 | 0.000 | 1.26x | 11.8/19.1/25.3% | 1.8/5.1% | 3 |
| 10000 | 1 | 0.471 | 0.455 | 0.016 | - | - | 0.660 | 0.689 | 0.000 | 1.17x | 10.8/17.5/23.2% | 1.8/4.5% | 3 |
| 4000 | 1 | 0.264 | 0.262 | 0.002 | - | - | 0.340 | 0.469 | 0.000 | 0.98x | 9.0/14.7/19.3% | 1.5/3.2% | 3 |
| 2000 | 1 | 0.057 | 0.057 | 0.000 | - | - | 0.065 | 0.144 | 0.000 | 0.64x | 6.2/9.6/12.8% | 1.0/1.8% | 3 |

> noise-pulse-interval-ms=30000: decode_failures 1

> noise-pulse-interval-ms=10000: decode_failures 12

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario flat`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.172 | 0.171 | 0.001 | - | - | 0.133 | 0.134 | 0.000 | 1.05x | 6.1/10.4/13.5% | 1.7/3.5% | 3 |
| 1.0 | 1 | 0.637 | 0.632 | 0.005 | - | - | 0.650 | 0.651 | 0.407 | 0.88x | 13.8/17.9/19.7% | 1.2/3.9% | 3 |

> duct-per-hour=0.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario flat`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 22 | 1 | 0.188 | 0.180 | 0.007 | - | - | 0.303 | 0.325 | 0.000 | 1.09x | 6.7/11.2/14.1% | 1.8/3.8% | 3 |
| 17 | 1 | 0.068 | 0.068 | 0.000 | - | - | 0.059 | 0.061 | 0.000 | 0.56x | 2.5/4.1/5.1% | 1.0/1.8% | 3 |
| 14 | 1 | 0.036 | 0.036 | 0.000 | - | - | 0.088 | 0.090 | 0.000 | 0.36x | 1.2/2.5/3.5% | 0.6/1.3% | 3 |

> tx-power=22: decode_failures 6

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario flat`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.981 | 0.981 | 0.095 | 2.11x | 19.5/29.7/33.9% | 1.4/5.4% | 3 |
| True | 1 | 0.865 | 0.862 | 0.003 | - | - | 0.974 | 0.974 | 0.105 | 2.45x | 22.2/33.2/37.1% | 1.7/5.9% | 3 |

### `RT-favourites` - favourite-routers  `--scenario flat`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.660 | 0.643 | 0.017 | - | - | 0.867 | 0.868 | 0.000 | 1.31x | 11.6/20.0/26.3% | 1.9/5.1% | 3 |
| True | 1 | 0.725 | 0.714 | 0.011 | - | - | 0.867 | 0.869 | 0.000 | 1.46x | 13.2/21.7/27.0% | 2.1/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario flat`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| random | 1 | 0.686 | 0.666 | 0.020 | - | - | 0.924 | 0.925 | 0.000 | 1.32x | 12.3/19.3/25.7% | 2.0/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario flat`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.500 | 0.462 | 0.038 | - | - | 0.851 | 0.867 | 0.000 | 1.11x | 10.2/17.0/23.8% | 1.7/4.8% | 3 |
| 7 | 1 | 0.785 | 0.779 | 0.006 | - | - | 0.917 | 0.919 | 0.000 | 1.52x | 13.5/20.8/27.2% | 2.4/5.4% | 3 |
| 15 | 1 | 0.837 | 0.834 | 0.003 | - | - | 0.927 | 0.928 | 0.000 | 1.55x | 13.8/20.8/27.2% | 2.5/5.3% | 3 |
| 32 | 1 | 0.827 | 0.822 | 0.005 | - | - | 0.921 | 0.923 | 0.000 | 1.56x | 13.9/20.9/27.4% | 2.5/5.4% | 3 |

> hop-limit=3: decode_failures 6

### `RT-hopspread` - hop-limit  `--scenario flat`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.500 | 0.462 | 0.038 | - | - | 0.851 | 0.867 | 0.000 | 1.11x | 10.2/17.0/23.8% | 1.7/4.8% | 3 |
| 5 | 1 | 0.688 | 0.673 | 0.014 | - | - | 0.912 | 0.917 | 0.000 | 1.31x | 11.9/19.6/26.0% | 2.0/5.2% | 3 |
| 7 | 1 | 0.785 | 0.779 | 0.006 | - | - | 0.917 | 0.919 | 0.000 | 1.52x | 13.5/20.8/27.2% | 2.4/5.4% | 3 |

> hop-limit=3: decode_failures 6

### `RT-rebroadcast` - rebroadcast-mode  `--scenario flat`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.629 | 0.629 | 0.000 | - | - | 0.738 | 0.878 | 0.000 | 1.27x | 11.8/18.7/24.9% | 1.9/5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario flat`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.500 | 0.462 | 0.038 | - | - | 0.851 | 0.867 | 0.000 | 1.11x | 10.2/17.0/23.8% | 1.7/4.8% | 3 |
| True | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

> hop-spread=False: decode_failures 6

### `SC-signing` - signature-policy  `--scenario flat`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| BALANCED | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| STRICT | 1 | 0.523 | 0.523 | 0.000 | - | - | 0.748 | 0.782 | 0.000 | 1.41x | 13.0/21.3/28.3% | 2.1/5.8% | 3 |

> signature-policy=STRICT: decode_failures 17

### `SF-advert-transport` - advert-transport  `--scenario flat`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| dm | 1 | 0.644 | 0.625 | 0.019 | - | - | 0.868 | 0.871 | 0.000 | 1.28x | 11.7/19.5/25.6% | 1.9/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario flat`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.632 | 0.616 | 0.016 | - | - | 0.857 | 0.870 | 0.000 | 1.29x | 11.9/19.3/25.4% | 1.9/5.3% | 3 |
| local | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| time | 1 | 0.636 | 0.619 | 0.017 | - | - | 0.861 | 0.879 | 0.000 | 1.29x | 11.7/19.3/25.5% | 1.9/5.3% | 3 |
| window | 1 | 0.645 | 0.626 | 0.019 | - | - | 0.879 | 0.885 | 0.000 | 1.29x | 11.8/19.3/25.5% | 1.9/5.3% | 3 |

> bucket-mode=global: misdecodes 16

> bucket-mode=time: misdecodes 11

> bucket-mode=window: misdecodes 5

### `SF-bucket-time` - time-bucket-s  `--scenario flat`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.625 | 0.606 | 0.019 | - | - | 0.854 | 0.862 | 0.000 | 1.37x | 12.4/21.1/27.4% | 2.0/5.8% | 3 |
| 1800 | 1 | 0.636 | 0.619 | 0.017 | - | - | 0.861 | 0.879 | 0.000 | 1.29x | 11.7/19.3/25.5% | 1.9/5.3% | 3 |
| 3600 | 1 | 0.640 | 0.625 | 0.015 | - | - | 0.856 | 0.866 | 0.000 | 1.29x | 11.8/19.2/25.5% | 1.9/5.3% | 3 |

> time-bucket-s=600: misdecodes 71

> time-bucket-s=1800: misdecodes 11

> time-bucket-s=3600: misdecodes 2

### `SF-cadence` - trigger  `--scenario flat`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| interval | 1 | 0.621 | 0.601 | 0.019 | - | - | 0.852 | 0.855 | 0.000 | 1.54x | 13.2/24.9/31.9% | 2.1/7.1% | 3 |
| aimd | 1 | 0.632 | 0.623 | 0.009 | - | - | 0.791 | 0.870 | 0.000 | 1.28x | 11.8/19.2/25.4% | 1.9/5.2% | 3 |
| bucket+interval | 1 | 0.613 | 0.590 | 0.023 | - | - | 0.845 | 0.850 | 0.000 | 1.55x | 13.4/24.8/31.7% | 2.1/7.1% | 3 |

> trigger=interval: misdecodes 2

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 11

> trigger=bucket+interval: misdecodes 3

### `SF-capacity` - capacity  `--scenario flat`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.640 | 0.624 | 0.016 | - | - | 0.850 | 0.879 | 0.000 | 1.30x | 11.9/19.8/25.9% | 1.9/5.4% | 3 |
| 8 | 1 | 0.636 | 0.620 | 0.016 | - | - | 0.848 | 0.869 | 0.000 | 1.30x | 11.9/19.6/25.8% | 1.9/5.4% | 3 |
| 16 | 1 | 0.640 | 0.624 | 0.016 | - | - | 0.853 | 0.877 | 0.000 | 1.30x | 11.9/19.5/25.8% | 1.9/5.3% | 3 |
| 32 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 50 | 1 | 0.645 | 0.629 | 0.016 | - | - | 0.874 | 0.878 | 0.000 | 1.28x | 11.7/19.2/25.4% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 71

> capacity=8: decode_failures 72

> capacity=16: decode_failures 57

### `SF-capacity-local` - capacity  `--scenario flat`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.640 | 0.624 | 0.016 | - | - | 0.850 | 0.879 | 0.000 | 1.30x | 11.9/19.8/25.9% | 1.9/5.4% | 3 |
| 8 | 1 | 0.636 | 0.620 | 0.016 | - | - | 0.848 | 0.869 | 0.000 | 1.30x | 11.9/19.6/25.8% | 1.9/5.4% | 3 |
| 16 | 1 | 0.640 | 0.624 | 0.016 | - | - | 0.853 | 0.877 | 0.000 | 1.30x | 11.9/19.5/25.8% | 1.9/5.3% | 3 |
| 32 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 50 | 1 | 0.645 | 0.629 | 0.016 | - | - | 0.874 | 0.878 | 0.000 | 1.28x | 11.7/19.2/25.4% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 71

> capacity=8: decode_failures 72

> capacity=16: decode_failures 57

### `SF-capacity-window` - capacity  `--scenario flat`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.632 | 0.627 | 0.005 | - | - | 0.770 | 0.883 | 0.000 | 1.28x | 11.7/18.9/25.3% | 1.9/5.1% | 3 |
| 16 | 1 | 0.636 | 0.622 | 0.015 | - | - | 0.842 | 0.875 | 0.000 | 1.28x | 11.8/19.2/25.3% | 1.9/5.2% | 3 |
| 32 | 1 | 0.645 | 0.626 | 0.019 | - | - | 0.879 | 0.885 | 0.000 | 1.29x | 11.8/19.3/25.5% | 1.9/5.3% | 3 |

> capacity=8: misdecodes 1

> capacity=8: decode_failures 88

> capacity=16: misdecodes 4

> capacity=16: decode_failures 25

> capacity=32: misdecodes 5

### `SF-catchup` - catch-up-hours  `--scenario flat`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.613 | 0.590 | 0.023 | - | - | 0.845 | 0.850 | 0.000 | 1.55x | 13.4/24.8/31.7% | 2.1/7.1% | 3 |
| 02-06 | 1 | 0.638 | 0.627 | 0.011 | - | - | 0.815 | 0.879 | 0.000 | 1.30x | 12.0/19.9/26.2% | 1.9/5.5% | 3 |
| 00-08 | 1 | 0.640 | 0.627 | 0.013 | - | - | 0.826 | 0.884 | 0.000 | 1.34x | 12.2/21.1/27.3% | 1.9/5.9% | 3 |

> catch-up-hours=: misdecodes 3

> catch-up-hours=02-06: decode_failures 45

> catch-up-hours=00-08: decode_failures 43

### `SF-hops-flat` - hops-apart  `--scenario flat`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.634 | 0.624 | 0.010 | - | - | 0.839 | 0.840 | 0.000 | 1.30x | 12.2/19.4/25.6% | 2.0/5.2% | 3 |
| 2 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 3 | 1 | 0.640 | 0.612 | 0.028 | - | - | 0.791 | 0.850 | 0.000 | 1.30x | 12.3/19.1/25.3% | 1.9/5.0% | 3 |
| 4 | 1 | 0.659 | 0.622 | 0.036 | - | - | 0.750 | 0.860 | 0.000 | 1.32x | 12.4/19.3/25.6% | 2.0/5.1% | 3 |

> hops-apart=3: decode_failures 22

> hops-apart=4: decode_failures 39

### `SF-hops-spread` - hops-apart  `--scenario flat`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.634 | 0.624 | 0.010 | - | - | 0.839 | 0.840 | 0.000 | 1.30x | 12.2/19.4/25.6% | 2.0/5.2% | 3 |
| 2 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 3 | 1 | 0.640 | 0.612 | 0.028 | - | - | 0.791 | 0.850 | 0.000 | 1.30x | 12.3/19.1/25.3% | 1.9/5.0% | 3 |
| 4 | 1 | 0.659 | 0.622 | 0.036 | - | - | 0.750 | 0.860 | 0.000 | 1.32x | 12.4/19.3/25.6% | 2.0/5.1% | 3 |
| 5 | 1 | 0.643 | 0.625 | 0.018 | - | - | 0.669 | 0.830 | 0.000 | 1.31x | 12.2/19.1/25.3% | 2.0/5.0% | 3 |

> hops-apart=3: decode_failures 22

> hops-apart=4: decode_failures 39

> hops-apart=5: decode_failures 34

### `SF-jitter-global` - advert-jitter-s  `--scenario flat`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.641 | 0.623 | 0.018 | - | - | 0.867 | 0.871 | 0.000 | 1.29x | 11.8/19.3/25.7% | 2.0/5.3% | 3 |
| 30 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 120 | 1 | 0.648 | 0.631 | 0.017 | - | - | 0.877 | 0.881 | 0.000 | 1.28x | 11.8/19.2/25.3% | 1.9/5.3% | 3 |
| 600 | 1 | 0.642 | 0.624 | 0.018 | - | - | 0.875 | 0.878 | 0.000 | 1.30x | 11.9/19.6/25.8% | 1.9/5.4% | 3 |

> advert-jitter-s=120: decode_failures 1

### `SF-jitter-local` - advert-jitter-s  `--scenario flat`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.641 | 0.623 | 0.018 | - | - | 0.867 | 0.871 | 0.000 | 1.29x | 11.8/19.3/25.7% | 2.0/5.3% | 3 |
| 30 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 120 | 1 | 0.648 | 0.631 | 0.017 | - | - | 0.877 | 0.881 | 0.000 | 1.28x | 11.8/19.2/25.3% | 1.9/5.3% | 3 |
| 600 | 1 | 0.642 | 0.624 | 0.018 | - | - | 0.875 | 0.878 | 0.000 | 1.30x | 11.9/19.6/25.8% | 1.9/5.4% | 3 |

> advert-jitter-s=120: decode_failures 1

### `SF-place-flat` - place  `--scenario flat`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.622 | 0.622 | 0.000 | - | - | 0.167 | 0.464 | 0.000 | 1.27x | 11.8/18.7/25.0% | 1.9/5.0% | 3 |
| routers | 1 | 0.626 | 0.615 | 0.011 | - | - | 0.829 | 0.852 | 0.000 | 1.28x | 11.8/19.2/25.4% | 1.9/5.1% | 3 |
| alternate-routers | 1 | 0.630 | 0.623 | 0.007 | - | - | 0.851 | 0.852 | 0.000 | 1.28x | 11.9/19.0/25.2% | 1.9/5.0% | 3 |
| beside-router | 1 | 0.627 | 0.617 | 0.010 | - | - | 0.870 | 0.872 | 0.000 | 1.30x | 12.0/19.3/25.5% | 2.0/5.1% | 3 |
| random-clients | 1 | 0.634 | 0.624 | 0.010 | - | - | 0.776 | 0.782 | 0.000 | 1.30x | 11.9/18.9/25.2% | 2.0/5.0% | 3 |
| hops-apart | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

> place=routers: decode_failures 16

### `SF-place-spread` - place  `--scenario flat`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.622 | 0.622 | 0.000 | - | - | 0.167 | 0.464 | 0.000 | 1.27x | 11.8/18.7/25.0% | 1.9/5.0% | 3 |
| routers | 1 | 0.626 | 0.615 | 0.011 | - | - | 0.829 | 0.852 | 0.000 | 1.28x | 11.8/19.2/25.4% | 1.9/5.1% | 3 |
| alternate-routers | 1 | 0.630 | 0.623 | 0.007 | - | - | 0.851 | 0.852 | 0.000 | 1.28x | 11.9/19.0/25.2% | 1.9/5.0% | 3 |
| beside-router | 1 | 0.627 | 0.617 | 0.010 | - | - | 0.870 | 0.872 | 0.000 | 1.30x | 12.0/19.3/25.5% | 2.0/5.1% | 3 |
| random-clients | 1 | 0.634 | 0.624 | 0.010 | - | - | 0.776 | 0.782 | 0.000 | 1.30x | 11.9/18.9/25.2% | 2.0/5.0% | 3 |
| hops-apart | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

> place=routers: decode_failures 16

### `SF-provide-transport` - provide-transport  `--scenario flat`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| broadcast | 1 | 0.690 | 0.614 | 0.076 | - | - | 0.841 | 0.867 | 0.000 | 1.35x | 12.3/20.6/26.7% | 1.9/5.5% | 3 |

> provide-transport=broadcast: decode_failures 13

### `SF-replay-order` - replay-ordering  `--scenario flat`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| heard | 1 | 0.642 | 0.626 | 0.016 | - | - | 0.864 | 0.872 | 0.000 | 1.29x | 11.9/19.3/25.6% | 1.9/5.3% | 3 |

> replay-ordering=heard: misdecodes 4

> replay-ordering=heard: decode_failures 6

### `SF-replay-order-broadcast` - replay-ordering  `--scenario flat`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.690 | 0.614 | 0.076 | - | - | 0.841 | 0.867 | 0.000 | 1.35x | 12.3/20.6/26.7% | 1.9/5.5% | 3 |
| heard | 1 | 0.684 | 0.612 | 0.073 | - | - | 0.835 | 0.865 | 0.000 | 1.36x | 12.4/20.9/27.0% | 2.0/5.5% | 3 |

> replay-ordering=tip: decode_failures 13

> replay-ordering=heard: decode_failures 15

> slower: 5.87 s per simulated hour against 1.69 over 61 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-resolve` - resolve  `--scenario flat`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| enum | 1 | 0.633 | 0.618 | 0.015 | - | - | 0.831 | 0.866 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| hybrid | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario flat`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.626 | 0.615 | 0.011 | - | - | 0.829 | 0.852 | 0.000 | 1.28x | 11.8/19.2/25.4% | 1.9/5.1% | 3 |
| 6 | 1 | 0.636 | 0.617 | 0.019 | - | - | 0.874 | 0.879 | 0.000 | 1.32x | 12.1/19.9/26.3% | 2.0/5.4% | 6 |

> servers=3: decode_failures 16

> slower: 3.96 s per simulated hour against 1.83 over 61 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-flat` - servers  `--scenario flat`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.634 | 0.627 | 0.007 | - | - | 0.858 | 0.858 | 0.000 | 1.29x | 11.9/19.2/25.5% | 1.9/5.2% | 2 |
| 3 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 5 | 1 | 0.646 | 0.617 | 0.029 | - | - | 0.888 | 0.890 | 0.000 | 1.31x | 11.9/19.6/26.2% | 2.0/5.4% | 5 |
| 8 | 1 | 0.648 | 0.612 | 0.037 | - | - | 0.885 | 0.886 | 0.000 | 1.33x | 12.2/20.2/26.6% | 2.0/5.5% | 8 |

### `SF-servers-spread` - servers  `--scenario flat`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.634 | 0.627 | 0.007 | - | - | 0.858 | 0.858 | 0.000 | 1.29x | 11.9/19.2/25.5% | 1.9/5.2% | 2 |
| 3 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 5 | 1 | 0.646 | 0.617 | 0.029 | - | - | 0.888 | 0.890 | 0.000 | 1.31x | 11.9/19.6/26.2% | 2.0/5.4% | 5 |
| 8 | 1 | 0.648 | 0.612 | 0.037 | - | - | 0.885 | 0.886 | 0.000 | 1.33x | 12.2/20.2/26.6% | 2.0/5.5% | 8 |

### `SF-signed` - signed  `--scenario flat`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| True | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario flat`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.655 | 0.642 | 0.013 | - | - | 0.846 | 0.882 | 0.000 | 1.21x | 11.2/18.3/24.2% | 1.8/4.9% | 3 |
| 1 | 1 | 0.649 | 0.633 | 0.015 | - | - | 0.855 | 0.861 | 0.000 | 1.20x | 11.0/18.2/24.1% | 1.8/5.0% | 3 |
| 2 | 1 | 0.649 | 0.630 | 0.018 | - | - | 0.871 | 0.874 | 0.000 | 1.21x | 11.2/18.2/24.1% | 1.8/5.0% | 3 |
| 4 | 1 | 0.643 | 0.628 | 0.015 | - | - | 0.848 | 0.857 | 0.000 | 1.20x | 11.1/18.0/23.9% | 1.8/4.9% | 3 |

> sr-retries=0: decode_failures 8

### `SF-width` - short-id-bits  `--scenario flat`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.642 | 0.625 | 0.017 | - | - | 0.872 | 0.876 | 0.000 | 1.28x | 11.8/19.2/25.4% | 1.9/5.3% | 3 |
| 24 | 1 | 0.636 | 0.618 | 0.018 | - | - | 0.861 | 0.865 | 0.000 | 1.26x | 11.6/19.0/25.0% | 1.9/5.2% | 3 |
| 32 | 1 | 0.635 | 0.614 | 0.021 | - | - | 0.871 | 0.875 | 0.000 | 1.28x | 11.8/19.3/25.4% | 1.9/5.3% | 3 |
| 64 | 1 | 0.634 | 0.614 | 0.020 | - | - | 0.864 | 0.867 | 0.000 | 1.29x | 11.8/19.2/25.5% | 1.9/5.3% | 3 |

### `SF-window-size` - window-size  `--scenario flat`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.635 | 0.618 | 0.017 | - | - | 0.863 | 0.870 | 0.000 | 1.32x | 12.0/20.1/26.4% | 1.9/5.5% | 3 |
| 16 | 1 | 0.639 | 0.622 | 0.017 | - | - | 0.857 | 0.868 | 0.000 | 1.29x | 11.9/19.4/25.6% | 1.9/5.3% | 3 |
| 32 | 1 | 0.645 | 0.626 | 0.019 | - | - | 0.879 | 0.885 | 0.000 | 1.29x | 11.8/19.3/25.5% | 1.9/5.3% | 3 |

> window-size=8: misdecodes 89

> window-size=16: misdecodes 24

> window-size=32: misdecodes 5

### `TH-congestion` - no-congestion-scaling  `--scenario flat`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.981 | 0.981 | 0.095 | 2.11x | 19.5/29.7/33.9% | 1.4/5.4% | 3 |
| True | 1 | 0.643 | 0.635 | 0.008 | - | - | 0.891 | 0.926 | 0.092 | 5.68x | 49.2/68.0/73.4% | 3.8/12.7% | 3 |

> no-congestion-scaling=True: decode_failures 93

### `TH-congestion-input` - congestion-input  `--scenario flat`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.298 | 0.290 | 0.007 | - | - | 0.511 | 0.526 | 0.076 | 4.58x | 11.2/19.5/32.6% | 1.6/5.2% | 3 |
| truesize | 1 | 0.330 | 0.322 | 0.007 | - | - | 0.566 | 0.569 | 0.081 | 2.53x | 6.1/11.9/19.9% | 0.8/3.3% | 3 |

> congestion-input=hotstore: decode_failures 19

> congestion-input=truesize: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario flat`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.889 | 0.888 | 0.002 | - | - | 0.985 | 0.985 | 0.104 | 1.98x | 18.2/28.0/31.5% | 1.3/5.1% | 3 |
| adaptive | 1 | 0.880 | 0.878 | 0.002 | - | - | 0.981 | 0.981 | 0.095 | 2.11x | 19.5/29.7/33.9% | 1.4/5.4% | 3 |

