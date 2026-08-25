# Sweep blocks-2026-08-21-1395205

- **sim version** `1.2.0`
- **transport** `17a0d62`
- **ground** rolling
- **seed base** 1395205 · seeds 1395205
- **blocks** 87 run
- **compute** 9.9 h of simulator time across every cell
- **generated** 2026-08-21T05:08:52+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>85 warnings</summary>

- SF-cadence: trigger=interval: misdecodes 16
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 8
- SF-cadence: trigger=bucket+interval: misdecodes 5
- SF-capacity: capacity=4: decode_failures 75
- SF-capacity: capacity=8: decode_failures 19
- DG-burst: burst-loss=0.2: decode_failures 7
- DG-burst: burst-loss=0.3: decode_failures 13
- DG-outage: burst-loss=0.1: decode_failures 24
- DG-outage: burst-loss=0.2: decode_failures 26
- DG-outage: burst-loss=0.3: decode_failures 24
- RF-txpower: tx-power=14: decode_failures 1
- SF-servers-allrouters: servers=3: decode_failures 24
- SF-servers-allrouters: servers=6: decode_failures 2
- SF-hops-flat: hops-apart=3: decode_failures 5
- SF-hops-flat: hops-apart=4: decode_failures 36
- SF-place-flat: place=spread: decode_failures 9
- SF-place-flat: place=routers: decode_failures 24
- SF-place-flat: place=beside-router: decode_failures 14
- SF-place-flat: place=random-clients: decode_failures 18
- SF-bucket-mode: bucket-mode=global: misdecodes 40
- SF-bucket-mode: bucket-mode=time: misdecodes 33
- SF-bucket-mode: bucket-mode=window: misdecodes 4
- SF-bucket-time: time-bucket-s=600: misdecodes 150
- SF-bucket-time: time-bucket-s=1800: misdecodes 33
- SF-bucket-time: time-bucket-s=3600: misdecodes 12
- SF-capacity-window: capacity=8: misdecodes 24
- SF-capacity-window: capacity=8: decode_failures 18
- SF-capacity-window: capacity=16: misdecodes 2
- SF-capacity-window: capacity=32: misdecodes 4
- SF-window-size: window-size=8: misdecodes 67
- SF-window-size: window-size=16: misdecodes 36
- SF-window-size: window-size=32: misdecodes 4
- MS-density: nodes=90: decode_failures 64
- MS-size: nodes=40: decode_failures 3
- MS-size: nodes=120: decode_failures 47
- SF-capacity-local: capacity=4: decode_failures 75
- SF-capacity-local: capacity=8: decode_failures 19
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 15
- SF-replay-order: replay-ordering=heard: misdecodes 19
- SF-hops-spread: hops-apart=3: decode_failures 5
- SF-hops-spread: hops-apart=4: decode_failures 36
- SF-hops-spread: hops-apart=5: decode_failures 19
- SF-place-spread: place=spread: decode_failures 9
- SF-place-spread: place=routers: decode_failures 24
- SF-place-spread: place=beside-router: decode_failures 14
- SF-place-spread: place=random-clients: decode_failures 18
- SF-catchup: catch-up-hours=: misdecodes 5
- SF-catchup: catch-up-hours=02-06: decode_failures 30
- SF-catchup: catch-up-hours=00-08: decode_failures 30
- TH-congestion: no-congestion-scaling=True: decode_failures 87
- RF-eu-presets: preset=SHORT_FAST: decode_failures 3
- RF-preset: preset=SHORT_FAST: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 8
- BL-control: protocol=sr: decode_failures 5
- TH-congestion-input: congestion-input=hotstore: decode_failures 43
- TH-congestion-input: congestion-input=truesize: decode_failures 21
- MS-hopscale: nodes=120: decode_failures 47
- MS-hopscale: nodes=250: decode_failures 80
- DB-hotstore: max-num-nodes=100: misdecodes 1
- DB-hotstore: max-num-nodes=120: misdecodes 1
- DB-hotstore: max-num-nodes=250: misdecodes 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 34
- DB-hotstore-stress: max-num-nodes=120: decode_failures 43
- DB-hotstore-stress: max-num-nodes=250: decode_failures 45
- FW-mixed-26: legacy-fraction=0.25: decode_failures 2
- FW-mixed: legacy-fraction=0.25: decode_failures 16
- MS-oversubscribed: nodes=120: decode_failures 20
- MS-oversubscribed: nodes=250: decode_failures 43
- DB-platform: platform-mix=uniform: misdecodes 1
- DB-platform: platform-mix=baymesh-2026-08: misdecodes 1
- RT-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 12
- MS-siting: siting-mix=event: decode_failures 1
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 93
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 78
- DB-warm: warm-num-nodes=0: decode_failures 93
- DB-warm: warm-num-nodes=25: decode_failures 93
- DB-warm: warm-num-nodes=100: decode_failures 93
- DB-warm: warm-num-nodes=2000: decode_failures 93
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 1
- RF-noise: noise-profile=periodic: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- AD-siting: siting-mix=local-typical: decode_failures 2
- MS-stretch: stretch=2.0: decode_failures 11

</details>

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.2) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.949 | 0.949 | 0.694 → 0.741 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **text** | 0.073 → 0.973 | 0.900 | 0.073 → 0.973 | 14x sr_airtime | up | 4 |
| `PR-protocol` | protocol | **held** | 0 → 0.832 | 0.832 | 0.671 → 0.694 | 1.1x bytes_on_air | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.119 → 0.867 | 0.748 | 0.039 → 0.579 | 20x sr_bytes | down | 3 |
| `RF-preset-turbo` | preset | **held** | 0.135 → 0.832 | 0.697 | 0.054 → 0.688 | 25x sr_bytes | up | 5 |
| `RF-preset` | preset | **held** | 0.253 → 0.923 | 0.669 | 0.196 → 0.739 | 6.8x sr_airtime | up | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.103 → 0.766 | 0.663 | 0.073 → 0.639 | 92x sr_airtime | down | 4 |
| `MS-hopscale` | nodes | **held** | 0.188 → 0.832 | 0.644 | 0.159 → 0.688 | 7.4x bytes_on_air | down | 4 |
| `RF-txpower` | tx-power | **text** | 0.058 → 0.688 | 0.629 | 0.058 → 0.688 | 3.8x advert_bytes | down | 4 |
| `MS-topology` | topology | **held** | 0.368 → 0.994 | 0.626 | 0.442 → 0.946 | 5.3x sr_airtime | up | 4 |
| `MS-stretch` | stretch | **text** | 0.098 → 0.688 | 0.589 | 0.098 → 0.688 | 3x advert_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.253 → 0.832 | 0.579 | 0.196 → 0.688 | 3.4x sr_airtime | up | 4 |
| `MS-size` | nodes | **held** | 0.409 → 0.916 | 0.507 | 0.327 → 0.719 | 2.9x sr_bytes | down | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **held** | 0.483 → 0.882 | 0.399 | 0.509 → 0.832 | 14x sr_airtime | down | 3 |
| `RF-bw500` | preset | **text** | 0.127 → 0.523 | 0.396 | 0.127 → 0.523 | 4.9x sr_bytes | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.187 → 0.577 | 0.390 | 0.187 → 0.577 | 2.5x sr_airtime | up | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.486 → 0.861 | 0.374 | 0.486 → 0.861 | 2.5x sr_airtime | up | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.195 → 0.554 | 0.359 | 0.160 → 0.410 | 3.6x bytes_on_air | down | 3 |
| `MS-density` | nodes | **text** | 0.524 → 0.870 | 0.345 | 0.524 → 0.870 | 6.5x sr_airtime | up | 5 |
| `AD-flooding` | role-mix | **text** | 0.475 → 0.798 | 0.323 | 0.475 → 0.798 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.475 → 0.798 | 0.323 | 0.475 → 0.798 | 2.3x bytes_on_air | up | 3 |
| `DG-outage` | burst-loss | **text** | 0.380 → 0.688 | 0.307 | 0.380 → 0.688 | 2.2x sr_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.486 → 0.787 | 0.301 | 0.486 → 0.787 | 2x sr_airtime | up | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.648 → 0.949 | 0.301 | 0.688 → 0.741 | 3.2x sr_bytes | down | 5 |
| `DG-burst` | burst-loss | **text** | 0.388 → 0.688 | 0.299 | 0.388 → 0.688 | 1.9x sr_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.573 → 0.871 | 0.298 | 0.680 → 0.726 | 3.1x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.573 → 0.871 | 0.298 | 0.680 → 0.726 | 3.1x sr_bytes | up | 6 |
| `AD-badrouters` | role-placement | **held** | 0.458 → 0.756 | 0.298 | 0.457 → 0.686 | 2.6x sr_bytes | up | 3 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.577 → 0.869 | 0.292 | 0.435 → 0.720 | 10x sr_airtime | down | 3 |
| `RT-spread` | hop-spread | **held** | 0.544 → 0.832 | 0.288 | 0.486 → 0.688 | 1.5x sr_airtime | up | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.688 → 0.924 | 0.237 | 0.688 → 0.924 | 2.6x sr_bytes | up | 3 |
| `MS-roles` | role-mix | **text** | 0.475 → 0.702 | 0.227 | 0.475 → 0.702 | 1.5x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.688 → 0.914 | 0.226 | 0.688 → 0.914 | 1.9x sr_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.488 → 0.708 | 0.219 | 0.488 → 0.708 | 1.4x sr_airtime | down | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.656 → 0.858 | 0.201 | 0.656 → 0.858 | 4.2x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **held** | 0.646 → 0.848 | 0.201 | 0.524 → 0.688 | 1.4x sr_airtime | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.688 → 0.849 | 0.162 | 0.688 → 0.849 | 1.3x sr_airtime | up | 3 |
| `FW-mixed` | legacy-fraction | **held** | 0.787 → 0.927 | 0.140 | 0.639 → 0.707 | 2.1x bytes_on_air | up | 4 |
| `DG-loss` | extra-loss | **text** | 0.550 → 0.688 | 0.137 | 0.550 → 0.688 | 1.2x sr_bytes | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.814 → 0.949 | 0.135 | 0.688 → 0.741 | 3.2x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.312 → 0.441 | 0.129 | 0.214 → 0.293 | 4x sr_airtime | up | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.812 → 0.931 | 0.120 | 0.637 → 0.706 | 2.1x bytes_on_air | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.638 → 0.751 | 0.113 | 0.638 → 0.751 | 7x sr_airtime | up | 4 |
| `DB-hotstore` | max-num-nodes | **held** | 0.760 → 0.856 | 0.096 | 0.645 → 0.730 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **held** | 0.760 → 0.856 | 0.096 | 0.645 → 0.730 | 2.2x sr_airtime | down | 3 |
| `FW-versions` | profile | **text** | 0.688 → 0.777 | 0.089 | 0.688 → 0.777 | 3.1x bytes_on_air | down | 5 |
| `SC-signing` | signature-policy | **text** | 0.601 → 0.688 | 0.087 | 0.601 → 0.688 | 1.3x sr_airtime | down | 3 |
| `FW-firmware` | profile | **text** | 0.688 → 0.771 | 0.084 | 0.688 → 0.771 | 3.1x bytes_on_air | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.871 → 0.947 | 0.076 | 0.704 → 0.744 | 2.2x advert_bytes | up | 2 |
| `FW-signing-cost` | profile-flag | **held** | 0.832 → 0.902 | 0.070 | 0.688 → 0.738 | 3.4x bytes_on_air | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.785 → 0.851 | 0.066 | 0.607 → 0.653 | 1.5x sr_airtime | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **held** | 0.792 → 0.832 | 0.040 | 0.648 → 0.688 | 1.5x sr_airtime | down | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.437 → 0.474 | 0.038 | 0.287 → 0.311 | 2.1x sr_airtime | up | 2 |
| `SF-cadence` | trigger | **held** | 0.795 → 0.832 | 0.037 | 0.673 → 0.688 | 15x advert_bytes | down | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.820 → 0.853 | 0.033 | 0.685 → 0.693 | 5.3x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.814 → 0.846 | 0.033 | 0.688 → 0.711 | 1.3x bytes_on_air | down | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.802 → 0.832 | 0.030 | 0.685 → 0.688 | 6.8x sr_airtime | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.829 → 0.859 | 0.030 | 0.682 → 0.688 | 6.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.829 → 0.859 | 0.030 | 0.682 → 0.688 | 6.4x sr_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.815 → 0.845 | 0.030 | 0.683 → 0.696 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.815 → 0.845 | 0.030 | 0.683 → 0.696 | 1.1x sr_airtime | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.803 → 0.832 | 0.029 | 0.688 → 0.703 | 1.2x sr_airtime | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.688 → 0.714 | 0.026 | 0.688 → 0.714 | 1.2x advert_bytes | down | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.676 → 0.702 | 0.026 | 0.676 → 0.702 | 1.2x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.787 → 0.813 | 0.025 | 0.645 → 0.663 | 1.4x sr_airtime | down | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.813 → 0.834 | 0.021 | 0.663 → 0.668 | 1.3x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.832 → 0.851 | 0.019 | 0.684 → 0.692 | 5x advert_bytes | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.688 → 0.706 | 0.018 | 0.688 → 0.706 | 2.9x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.834 → 0.851 | 0.018 | 0.688 → 0.691 | 6.3x advert_bytes | up | 3 |
| `SF-capacity` | capacity | **held** | 0.825 → 0.842 | 0.018 | 0.684 → 0.697 | 5.1x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.825 → 0.842 | 0.018 | 0.684 → 0.697 | 5.1x advert_bytes | down | 5 |
| `PR-repeats` | extra-repeats | **held** | 0.832 → 0.850 | 0.018 | 0.688 → 0.699 | 1x sr_bytes | up | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.661 → 0.676 | 0.015 | 0.661 → 0.676 | 1.1x sr_airtime | down | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.818 → 0.834 | 0.015 | 0.661 → 0.668 | 1.2x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.837 → 0.851 | 0.014 | 0.689 → 0.696 | 2.1x advert_bytes | up | 3 |
| `AD-worst` | role-placement | **text** | 0.704 → 0.718 | 0.014 | 0.704 → 0.718 | 1.1x sr_bytes | down | 2 |
| `SF-width` | short-id-bits | **text** | 0.681 → 0.694 | 0.012 | 0.681 → 0.694 | 3.1x advert_bytes | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.673 → 0.684 | 0.011 | 0.673 → 0.684 | 9.2x advert_bytes | up | 3 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.858 → 0.867 | 0.009 | 0.858 → 0.867 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.858 → 0.866 | 0.008 | 0.858 → 0.866 | 1x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.832 → 0.839 | 0.007 | 0.688 → 0.691 | 1.1x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **text** | 0.681 → 0.688 | 0.006 | 0.681 → 0.688 | 5.7x advert_bytes | = | 3 |
| `SF-advert-transport` | advert-transport | **held** | 0.832 → 0.838 | 0.006 | 0.688 → 0.690 | 2.3x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.834 → 0.839 | 0.005 | 0.706 → 0.708 | 1x sr_airtime | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.855 → 0.858 | 0.003 | 0.855 → 0.858 | 1.2x sr_airtime | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |
| `DB-warm` | warm-num-nodes | - | 4 |

## Every block

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| interval | 0.676 | - | - | 0.796 | 0.799 | 0.368 | 1.39x | 27.0/30.5% | 6.8% | 3 |
| aimd | 0.679 | - | - | 0.797 | 0.842 | 0.342 | 1.13x | 19.5/23.2% | 4.7% | 3 |
| bucket+interval | 0.673 | - | - | 0.795 | 0.797 | 0.381 | 1.37x | 26.7/30.6% | 6.5% | 3 |

> trigger=interval: misdecodes 16

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 8

> trigger=bucket+interval: misdecodes 5

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.684 | - | - | 0.822 | 0.822 | 0.369 | 1.10x | 18.8/22.4% | 4.5% | 3 |
| 30 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 120 | 0.696 | - | - | 0.845 | 0.846 | 0.359 | 1.12x | 19.2/22.9% | 4.6% | 3 |
| 600 | 0.683 | - | - | 0.815 | 0.816 | 0.364 | 1.12x | 19.1/22.8% | 4.6% | 3 |

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| enum | 0.681 | - | - | 0.833 | 0.834 | 0.367 | 1.13x | 19.6/23.1% | 4.6% | 3 |
| hybrid | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.692 | - | - | 0.842 | 0.843 | 0.361 | 1.11x | 19.1/22.5% | 4.5% | 3 |
| 8 | 0.687 | - | - | 0.842 | 0.845 | 0.354 | 1.12x | 19.0/22.7% | 4.6% | 3 |
| 16 | 0.697 | - | - | 0.842 | 0.843 | 0.357 | 1.11x | 18.8/22.4% | 4.5% | 3 |
| 32 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 50 | 0.684 | - | - | 0.825 | 0.827 | 0.363 | 1.11x | 18.9/22.6% | 4.6% | 3 |

> capacity=4: decode_failures 75

> capacity=8: decode_failures 19

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| True | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 0.689 | - | - | 0.834 | 0.834 | 0.349 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 24 | 0.681 | - | - | 0.840 | 0.840 | 0.348 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 32 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 64 | 0.694 | - | - | 0.838 | 0.840 | 0.370 | 1.12x | 19.1/22.8% | 4.6% | 3 |

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.1 | 0.591 | - | - | 0.781 | 0.783 | 0.301 | 1.05x | 17.9/21.2% | 4.2% | 3 |
| 0.2 | 0.489 | - | - | 0.733 | 0.739 | 0.238 | 0.97x | 16.8/19.4% | 3.6% | 3 |
| 0.3 | 0.388 | - | - | 0.628 | 0.644 | 0.170 | 0.90x | 15.2/17.8% | 3.1% | 3 |

> burst-loss=0.2: decode_failures 7

> burst-loss=0.3: decode_failures 13

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.475 | - | - | 0.646 | 0.648 | 0.303 | 1.09x | 17.7/20.2% | 4.7% | 3 |
| all-routers | 0.798 | - | - | 0.885 | 0.885 | 0.531 | 2.47x | 36.6/39.3% | 5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.486 | - | - | 0.544 | 0.550 | 0.288 | 1.01x | 17.6/20.9% | 4.3% | 3 |
| 7 | 0.787 | - | - | 0.837 | 0.837 | 0.649 | 1.24x | 20.3/23.5% | 4.6% | 3 |
| 15 | 0.861 | - | - | 0.908 | 0.908 | 0.764 | 1.32x | 21.2/24.2% | 4.8% | 3 |
| 32 | 0.852 | - | - | 0.894 | 0.894 | 0.750 | 1.30x | 20.9/24.0% | 4.8% | 3 |

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.1 | 0.656 | - | - | 0.805 | 0.805 | 0.345 | 1.18x | 19.8/23.0% | 4.4% | 3 |
| 0.2 | 0.607 | - | - | 0.769 | 0.771 | 0.318 | 1.23x | 20.3/23.4% | 4.3% | 3 |
| 0.3 | 0.550 | - | - | 0.721 | 0.721 | 0.280 | 1.24x | 20.4/23.9% | 4.0% | 3 |

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.1 | 0.594 | - | - | 0.790 | 0.810 | 0.300 | 1.07x | 18.3/21.2% | 4.2% | 3 |
| 0.2 | 0.459 | - | - | 0.640 | 0.708 | 0.225 | 0.97x | 16.4/18.8% | 3.5% | 3 |
| 0.3 | 0.380 | - | - | 0.575 | 0.636 | 0.185 | 0.93x | 16.1/18.9% | 3.5% | 3 |

> burst-loss=0.1: decode_failures 24

> burst-loss=0.2: decode_failures 26

> burst-loss=0.3: decode_failures 24

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 0.054 | - | - | 0.135 | 0.203 | 0.000 | 0.01x | 0.1/0.1% | 0.0% | 3 |
| SHORT_TURBO | 0.127 | - | - | 0.366 | 0.374 | 0.000 | 0.03x | 0.3/0.5% | 0.2% | 3 |
| LONG_FAST | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| LONG_TURBO | 0.523 | - | - | 0.686 | 0.688 | 0.337 | 1.11x | 16.4/19.1% | 3.8% | 3 |
| EXTRA_LONG_TURBO | 0.617 | - | - | 0.776 | 0.777 | 0.379 | 1.50x | 24.4/25.9% | 5.7% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 22 | 0.185 | - | - | 0.363 | 0.364 | 0.000 | 1.08x | 12.3/14.5% | 3.8% | 3 |
| 17 | 0.107 | - | - | 0.328 | 0.341 | 0.000 | 0.66x | 6.4/10.1% | 2.7% | 3 |
| 14 | 0.058 | - | - | 0.236 | 0.268 | 0.000 | 0.49x | 5.0/8.4% | 2.2% | 3 |

> tx-power=14: decode_failures 1

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.704 | - | - | 0.871 | 0.961 | 0.348 | 1.12x | 19.4/23.1% | 4.8% | 3 |
| 6 | 0.744 | - | - | 0.947 | 0.964 | 0.368 | 1.15x | 20.0/23.6% | 5.1% | 6 |

> servers=3: decode_failures 24

> servers=6: decode_failures 2

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.691 | - | - | 0.859 | 0.859 | 0.381 | 1.11x | 19.0/22.8% | 4.7% | 3 |
| 2 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 3 | 0.741 | - | - | 0.949 | 0.971 | 0.369 | 1.15x | 19.3/23.2% | 4.9% | 3 |
| 4 | 0.716 | - | - | 0.814 | 0.961 | 0.365 | 1.14x | 19.3/23.0% | 4.7% | 3 |

> hops-apart=3: decode_failures 5

> hops-apart=4: decode_failures 36

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.680 | - | - | 0.573 | 0.945 | 0.392 | 1.10x | 18.8/22.2% | 4.5% | 3 |
| routers | 0.704 | - | - | 0.871 | 0.961 | 0.348 | 1.12x | 19.4/23.1% | 4.8% | 3 |
| alternate-routers | 0.691 | - | - | 0.859 | 0.859 | 0.381 | 1.11x | 19.0/22.8% | 4.7% | 3 |
| beside-router | 0.695 | - | - | 0.837 | 0.955 | 0.367 | 1.13x | 19.2/22.7% | 4.6% | 3 |
| random-clients | 0.726 | - | - | 0.784 | 0.926 | 0.414 | 1.14x | 19.3/23.0% | 4.9% | 3 |
| hops-apart | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

> place=spread: decode_failures 9

> place=routers: decode_failures 24

> place=beside-router: decode_failures 14

> place=random-clients: decode_failures 18

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.685 | - | - | 0.829 | 0.829 | 0.369 | 1.10x | 18.6/22.3% | 4.5% | 2 |
| 3 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 5 | 0.682 | - | - | 0.854 | 0.856 | 0.343 | 1.14x | 19.8/23.5% | 4.8% | 5 |
| 8 | 0.683 | - | - | 0.859 | 0.859 | 0.366 | 1.17x | 20.8/24.4% | 5.0% | 8 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 0.684 | - | - | 0.844 | 0.845 | 0.349 | 1.14x | 19.5/23.2% | 4.7% | 3 |
| local | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| time | 0.692 | - | - | 0.842 | 0.844 | 0.367 | 1.15x | 19.9/23.5% | 4.8% | 3 |
| window | 0.691 | - | - | 0.851 | 0.854 | 0.358 | 1.11x | 18.9/22.6% | 4.6% | 3 |

> bucket-mode=global: misdecodes 40

> bucket-mode=time: misdecodes 33

> bucket-mode=window: misdecodes 4

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 0.685 | - | - | 0.820 | 0.822 | 0.374 | 1.23x | 22.1/25.7% | 5.3% | 3 |
| 1800 | 0.692 | - | - | 0.842 | 0.844 | 0.367 | 1.15x | 19.9/23.5% | 4.8% | 3 |
| 3600 | 0.693 | - | - | 0.853 | 0.853 | 0.387 | 1.12x | 19.2/22.9% | 4.7% | 3 |

> time-bucket-s=600: misdecodes 150

> time-bucket-s=1800: misdecodes 33

> time-bucket-s=3600: misdecodes 12

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.696 | - | - | 0.837 | 0.845 | 0.374 | 1.11x | 18.7/22.4% | 4.5% | 3 |
| 16 | 0.689 | - | - | 0.845 | 0.846 | 0.343 | 1.10x | 18.6/22.2% | 4.5% | 3 |
| 32 | 0.691 | - | - | 0.851 | 0.854 | 0.358 | 1.11x | 18.9/22.6% | 4.6% | 3 |

> capacity=8: misdecodes 24

> capacity=8: decode_failures 18

> capacity=16: misdecodes 2

> capacity=32: misdecodes 4

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.688 | - | - | 0.844 | 0.846 | 0.360 | 1.13x | 19.8/23.5% | 4.8% | 3 |
| 16 | 0.689 | - | - | 0.834 | 0.834 | 0.368 | 1.13x | 19.5/23.1% | 4.7% | 3 |
| 32 | 0.691 | - | - | 0.851 | 0.854 | 0.358 | 1.11x | 18.9/22.6% | 4.6% | 3 |

> window-size=8: misdecodes 67

> window-size=16: misdecodes 36

> window-size=32: misdecodes 4

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.524 | - | - | 0.680 | 0.682 | 0.174 | 0.95x | 23.1/24.9% | 5.5% | 3 |
| 60 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 90 | 0.778 | - | - | 0.801 | 0.851 | 0.370 | 1.28x | 19.5/22.2% | 4.4% | 3 |
| 120 | 0.858 | - | - | 0.990 | 0.991 | 0.608 | 1.68x | 30.4/34.4% | 5.4% | 3 |
| 150 | 0.870 | - | - | 0.994 | 0.994 | 0.625 | 1.94x | 30.8/34.6% | 5.1% | 3 |

> nodes=90: decode_failures 64

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.486 | - | - | 0.544 | 0.550 | 0.288 | 1.01x | 17.6/20.9% | 4.3% | 3 |
| 5 | 0.692 | - | - | 0.774 | 0.777 | 0.484 | 1.10x | 18.4/21.8% | 4.4% | 3 |
| 7 | 0.787 | - | - | 0.837 | 0.837 | 0.649 | 1.24x | 20.3/23.5% | 4.6% | 3 |

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.719 | - | - | 0.916 | 0.966 | 0.315 | 1.12x | 29.9/32.3% | 6.9% | 3 |
| 60 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 90 | 0.508 | - | - | 0.635 | 0.636 | 0.316 | 1.63x | 20.4/22.9% | 4.5% | 3 |
| 120 | 0.411 | - | - | 0.574 | 0.616 | 0.137 | 2.27x | 23.1/27.7% | 4.9% | 3 |
| 150 | 0.327 | - | - | 0.409 | 0.409 | 0.020 | 2.70x | 21.6/25.1% | 4.7% | 3 |

> nodes=40: decode_failures 3

> nodes=120: decode_failures 47

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.486 | - | - | 0.544 | 0.550 | 0.288 | 1.01x | 17.6/20.9% | 4.3% | 3 |
| True | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| dm | 0.690 | - | - | 0.838 | 0.839 | 0.354 | 1.11x | 18.9/22.4% | 4.5% | 3 |

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| broadcast | 0.706 | - | - | 0.834 | 0.834 | 0.361 | 1.17x | 20.4/24.2% | 5.0% | 3 |

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.692 | - | - | 0.842 | 0.843 | 0.361 | 1.11x | 19.1/22.5% | 4.5% | 3 |
| 8 | 0.687 | - | - | 0.842 | 0.845 | 0.354 | 1.12x | 19.0/22.7% | 4.6% | 3 |
| 16 | 0.697 | - | - | 0.842 | 0.843 | 0.357 | 1.11x | 18.8/22.4% | 4.5% | 3 |
| 32 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 50 | 0.684 | - | - | 0.825 | 0.827 | 0.363 | 1.11x | 18.9/22.6% | 4.6% | 3 |

> capacity=4: decode_failures 75

> capacity=8: decode_failures 19

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.706 | - | - | 0.834 | 0.834 | 0.361 | 1.17x | 20.4/24.2% | 5.0% | 3 |
| heard | 0.708 | - | - | 0.839 | 0.839 | 0.351 | 1.17x | 20.4/24.1% | 5.0% | 3 |

> replay-ordering=heard: misdecodes 15

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.684 | - | - | 0.822 | 0.822 | 0.369 | 1.10x | 18.8/22.4% | 4.5% | 3 |
| 30 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 120 | 0.696 | - | - | 0.845 | 0.846 | 0.359 | 1.12x | 19.2/22.9% | 4.6% | 3 |
| 600 | 0.683 | - | - | 0.815 | 0.816 | 0.364 | 1.12x | 19.1/22.8% | 4.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| heard | 0.691 | - | - | 0.839 | 0.840 | 0.369 | 1.12x | 19.1/22.8% | 4.6% | 3 |

> replay-ordering=heard: misdecodes 19

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.691 | - | - | 0.859 | 0.859 | 0.381 | 1.11x | 19.0/22.8% | 4.7% | 3 |
| 2 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 3 | 0.741 | - | - | 0.949 | 0.971 | 0.369 | 1.15x | 19.3/23.2% | 4.9% | 3 |
| 4 | 0.716 | - | - | 0.814 | 0.961 | 0.365 | 1.14x | 19.3/23.0% | 4.7% | 3 |
| 5 | 0.706 | - | - | 0.648 | 0.982 | 0.417 | 1.13x | 19.1/22.7% | 4.7% | 3 |

> hops-apart=3: decode_failures 5

> hops-apart=4: decode_failures 36

> hops-apart=5: decode_failures 19

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.680 | - | - | 0.573 | 0.945 | 0.392 | 1.10x | 18.8/22.2% | 4.5% | 3 |
| routers | 0.704 | - | - | 0.871 | 0.961 | 0.348 | 1.12x | 19.4/23.1% | 4.8% | 3 |
| alternate-routers | 0.691 | - | - | 0.859 | 0.859 | 0.381 | 1.11x | 19.0/22.8% | 4.7% | 3 |
| beside-router | 0.695 | - | - | 0.837 | 0.955 | 0.367 | 1.13x | 19.2/22.7% | 4.6% | 3 |
| random-clients | 0.726 | - | - | 0.784 | 0.926 | 0.414 | 1.14x | 19.3/23.0% | 4.9% | 3 |
| hops-apart | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

> place=spread: decode_failures 9

> place=routers: decode_failures 24

> place=beside-router: decode_failures 14

> place=random-clients: decode_failures 18

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.685 | - | - | 0.829 | 0.829 | 0.369 | 1.10x | 18.6/22.3% | 4.5% | 2 |
| 3 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 5 | 0.682 | - | - | 0.854 | 0.856 | 0.343 | 1.14x | 19.8/23.5% | 4.8% | 5 |
| 8 | 0.683 | - | - | 0.859 | 0.859 | 0.366 | 1.17x | 20.8/24.4% | 5.0% | 8 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 0.127 | - | - | 0.366 | 0.374 | 0.000 | 0.03x | 0.3/0.5% | 0.2% | 3 |
| MEDIUM_TURBO | 0.226 | - | - | 0.457 | 0.457 | 0.000 | 0.17x | 2.2/3.0% | 0.7% | 3 |
| LONG_TURBO | 0.523 | - | - | 0.686 | 0.688 | 0.337 | 1.11x | 16.4/19.1% | 3.8% | 3 |

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 0.673 | - | - | 0.795 | 0.797 | 0.381 | 1.37x | 26.7/30.6% | 6.5% | 3 |
| 02-06 | 0.684 | - | - | 0.804 | 0.836 | 0.356 | 1.14x | 19.7/23.2% | 4.7% | 3 |
| 00-08 | 0.684 | - | - | 0.802 | 0.834 | 0.349 | 1.18x | 21.0/24.4% | 5.2% | 3 |

> catch-up-hours=: misdecodes 5

> catch-up-hours=02-06: decode_failures 30

> catch-up-hours=00-08: decode_failures 30

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.858 | - | - | 0.990 | 0.991 | 0.608 | 1.68x | 30.4/34.4% | 5.4% | 3 |
| True | 0.656 | - | - | 0.845 | 0.940 | 0.452 | 4.78x | 69.3/74.9% | 12.4% | 3 |

> no-congestion-scaling=True: decode_failures 87

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 0.714 | - | - | 0.858 | 0.860 | 0.390 | 1.09x | 18.8/22.4% | 4.5% | 3 |
| sinusoid | 0.700 | - | - | 0.850 | 0.852 | 0.380 | 1.02x | 17.7/21.0% | 4.2% | 3 |
| commuter | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.196 | - | - | 0.253 | 0.255 | 0.000 | 0.10x | 1.0/1.2% | 0.4% | 3 |
| LONG_FAST | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| LITE_FAST | 0.637 | - | - | 0.779 | 0.780 | 0.381 | 0.91x | 18.6/19.9% | 3.5% | 3 |
| NARROW_SLOW | 0.663 | - | - | 0.794 | 0.798 | 0.372 | 1.17x | 23.4/25.6% | 4.6% | 3 |

> preset=SHORT_FAST: decode_failures 3

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.196 | - | - | 0.253 | 0.255 | 0.000 | 0.10x | 1.0/1.2% | 0.4% | 3 |
| LONG_FAST | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| LONG_MODERATE | 0.739 | - | - | 0.923 | 0.970 | 0.497 | 2.77x | 53.6/57.7% | 11.2% | 3 |

> preset=SHORT_FAST: decode_failures 3

> preset=LONG_MODERATE: decode_failures 8

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.694 | - | - | 0 | 0.000 | 0.366 | 1.10x | 18.6/22.1% | 4.5% | 3 |
| sr | 0.741 | - | - | 0.949 | 0.971 | 0.369 | 1.15x | 19.3/23.2% | 4.9% | 3 |

> protocol=sr: decode_failures 5

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| random | 0.703 | - | - | 0.803 | 0.805 | 0.500 | 1.13x | 19.0/22.2% | 4.5% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 0.638 | - | - | 0.814 | 0.814 | 0.311 | 1.74x | 29.2/34.1% | 6.9% | 3 |
| 3600 | 0.720 | - | - | 0.869 | 0.871 | 0.376 | 0.76x | 13.7/16.1% | 3.3% | 3 |
| 10800 | 0.739 | - | - | 0.889 | 0.891 | 0.398 | 0.47x | 8.8/10.3% | 2.2% | 3 |
| 43200 | 0.751 | - | - | 0.904 | 0.906 | 0.389 | 0.32x | 6.3/7.3% | 1.6% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.694 | - | - | 0 | 0.000 | 0.366 | 1.10x | 18.6/22.1% | 4.5% | 3 |
| chain | 0.671 | - | - | 0.776 | 0.816 | 0.360 | 1.23x | 22.3/26.3% | 5.4% | 3 |
| sr | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| clustered | 0.831 | - | - | 0.928 | 0.929 | 0.000 | 1.01x | 32.3/34.2% | 5.4% | 3 |
| corridor | 0.442 | - | - | 0.368 | 0.368 | 0.294 | 1.31x | 18.4/21.3% | 5.3% | 3 |
| hub | 0.946 | - | - | 0.994 | 0.994 | 0.701 | 1.12x | 29.8/34.4% | 5.6% | 3 |

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.858 | - | - | 0.990 | 0.991 | 0.608 | 1.68x | 30.4/34.4% | 5.4% | 3 |
| True | 0.855 | - | - | 0.991 | 0.992 | 0.613 | 1.93x | 34.6/38.9% | 5.9% | 3 |

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 0.287 | - | - | 0.437 | 0.455 | 0.000 | 3.74x | 22.7/30.2% | 4.9% | 3 |
| truesize | 0.311 | - | - | 0.474 | 0.483 | 0.000 | 1.96x | 13.5/18.5% | 3.2% | 3 |

> congestion-input=hotstore: decode_failures 43

> congestion-input=truesize: decode_failures 21

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 0.867 | - | - | 0.995 | 0.995 | 0.618 | 1.53x | 28.3/32.0% | 4.9% | 3 |
| adaptive | 0.858 | - | - | 0.990 | 0.991 | 0.608 | 1.68x | 30.4/34.4% | 5.4% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.663 | - | - | 0.813 | 0.815 | 0.342 | 1.31x | 23.1/27.3% | 5.6% | 3 |
| True | 0.668 | - | - | 0.834 | 0.834 | 0.344 | 1.32x | 23.9/28.0% | 5.8% | 3 |

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 0.645 | - | - | 0.791 | 0.792 | 0.349 | 1.38x | 24.5/28.9% | 6.0% | 3 |
| directed-with-late-flood | 0.663 | - | - | 0.813 | 0.815 | 0.342 | 1.31x | 23.1/27.3% | 5.6% | 3 |
| m4-early-flood | 0.655 | - | - | 0.787 | 0.789 | 0.354 | 1.29x | 22.9/27.1% | 5.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 0.668 | - | - | 0.834 | 0.834 | 0.344 | 1.32x | 23.9/28.0% | 5.8% | 3 |
| m4-early-flood | 0.661 | - | - | 0.818 | 0.820 | 0.361 | 1.31x | 23.5/27.6% | 5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.676 | - | - | 0.792 | 0.794 | 0.361 | 1.13x | 19.9/22.1% | 4.4% | 3 |
| True | 0.702 | - | - | 0.807 | 0.807 | 0.412 | 1.16x | 20.0/22.4% | 4.5% | 3 |

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 0.771 | - | - | 0.912 | 0.918 | 0.585 | 0.63x | 9.2/9.9% | 1.8% | 3 |
| 2.8 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 120 | 0.411 | - | - | 0.574 | 0.616 | 0.137 | 2.27x | 23.1/27.7% | 4.9% | 3 |
| 250 | 0.288 | - | - | 0.441 | 0.454 | 0.000 | 4.02x | 24.6/32.7% | 5.4% | 3 |
| 500 | 0.159 | - | - | 0.188 | 0.188 | 0.008 | 8.11x | 22.1/37.9% | 4.6% | 3 |

> nodes=120: decode_failures 47

> nodes=250: decode_failures 80

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.645 | - | - | 0.760 | 0.760 | 0.416 | 2.30x | 40.4/44.2% | 8.0% | 3 |
| 100 | 0.730 | - | - | 0.856 | 0.856 | 0.445 | 1.27x | 22.9/25.7% | 4.6% | 3 |
| 120 | 0.730 | - | - | 0.856 | 0.856 | 0.445 | 1.27x | 22.9/25.7% | 4.6% | 3 |
| 250 | 0.730 | - | - | 0.856 | 0.856 | 0.445 | 1.27x | 22.9/25.7% | 4.6% | 3 |

> max-num-nodes=100: misdecodes 1

> max-num-nodes=120: misdecodes 1

> max-num-nodes=250: misdecodes 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.214 | - | - | 0.312 | 0.353 | 0.000 | 8.97x | 48.4/62.1% | 9.9% | 3 |
| 120 | 0.287 | - | - | 0.437 | 0.455 | 0.000 | 3.74x | 22.7/30.2% | 4.9% | 3 |
| 250 | 0.293 | - | - | 0.441 | 0.458 | 0.000 | 3.73x | 22.6/30.5% | 4.9% | 3 |

> max-num-nodes=10: decode_failures 34

> max-num-nodes=120: decode_failures 43

> max-num-nodes=250: decode_failures 45

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.25 | 0.639 | - | - | 0.787 | 0.812 | 0.408 | 0.96x | 16.9/19.7% | 4.2% | 3 |
| 0.5 | 0.684 | - | - | 0.927 | 0.934 | 0.439 | 0.93x | 17.2/19.4% | 4.3% | 3 |
| 0.75 | 0.707 | - | - | 0.860 | 0.861 | 0.395 | 0.73x | 12.1/13.5% | 2.8% | 3 |

> legacy-fraction=0.25: decode_failures 16

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.25 | 0.637 | - | - | 0.812 | 0.825 | 0.414 | 0.96x | 17.2/20.0% | 4.3% | 3 |
| 0.5 | 0.683 | - | - | 0.931 | 0.938 | 0.448 | 0.92x | 17.0/19.4% | 4.3% | 3 |
| 0.75 | 0.706 | - | - | 0.842 | 0.846 | 0.422 | 0.72x | 11.9/14.0% | 2.8% | 3 |

> legacy-fraction=0.25: decode_failures 2

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 0.410 | - | - | 0.554 | 0.600 | 0.120 | 2.15x | 21.9/26.4% | 4.5% | 3 |
| 250 | 0.287 | - | - | 0.437 | 0.455 | 0.000 | 3.74x | 22.7/30.2% | 4.9% | 3 |
| 500 | 0.160 | - | - | 0.195 | 0.196 | 0.008 | 7.63x | 20.8/35.7% | 4.3% | 3 |

> nodes=120: decode_failures 20

> nodes=250: decode_failures 43

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.730 | - | - | 0.856 | 0.856 | 0.445 | 1.27x | 22.9/25.7% | 4.6% | 3 |
| baymesh-2026-08 | 0.730 | - | - | 0.856 | 0.856 | 0.445 | 1.27x | 22.9/25.7% | 4.6% | 3 |
| constrained | 0.645 | - | - | 0.760 | 0.760 | 0.416 | 2.30x | 40.4/44.2% | 8.0% | 3 |

> platform-mix=uniform: misdecodes 1

> platform-mix=baymesh-2026-08: misdecodes 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| KNOWN_ONLY | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| CORE_PORTNUMS_ONLY | 0.685 | - | - | 0.802 | 0.853 | 0.361 | 1.10x | 18.5/22.1% | 4.5% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 12

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| True | 0.699 | - | - | 0.850 | 0.850 | 0.387 | 1.13x | 19.3/22.9% | 4.6% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.858 | - | - | 0.990 | 0.991 | 0.608 | 1.68x | 30.4/34.4% | 5.4% | 3 |
| True | 0.866 | - | - | 0.995 | 0.995 | 0.628 | 1.73x | 30.7/34.7% | 5.3% | 3 |

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.702 | - | - | 0.842 | 0.844 | 0.490 | 1.14x | 19.9/23.5% | 4.8% | 3 |
| baymesh-2026-08 | 0.475 | - | - | 0.646 | 0.648 | 0.303 | 1.09x | 17.7/20.2% | 4.7% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.708 | - | - | 0.838 | 0.838 | 0.487 | 1.15x | 19.8/23.4% | 4.7% | 3 |
| baymesh-2026-08 | 0.488 | - | - | 0.655 | 0.657 | 0.317 | 1.17x | 20.3/22.6% | 4.7% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.05 | 0.693 | - | - | 0.825 | 0.828 | 0.354 | 1.21x | 21.7/24.3% | 4.6% | 3 |
| 0.1 | 0.706 | - | - | 0.846 | 0.847 | 0.373 | 1.26x | 23.4/26.3% | 4.5% | 3 |
| 0.2 | 0.711 | - | - | 0.814 | 0.815 | 0.382 | 1.49x | 30.3/35.1% | 4.6% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| BALANCED | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| STRICT | 0.601 | - | - | 0.747 | 0.747 | 0.318 | 1.23x | 20.8/24.7% | 5.0% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 0.738 | - | - | 0.902 | 0.902 | 0.385 | 0.60x | 11.1/13.3% | 2.7% | 3 |
| signing=true | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| local-typical | 0.561 | - | - | 0.805 | 0.819 | 0.000 | 1.22x | 21.0/26.5% | 5.1% | 3 |
| event | 0.073 | - | - | 0.109 | 0.230 | 0.000 | 0.55x | 5.0/10.5% | 2.3% | 3 |
| backbone | 0.973 | - | - | 0.998 | 0.998 | 0.914 | 1.00x | 30.4/33.2% | 5.5% | 3 |

> siting-mix=event: decode_failures 1

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.676 | - | - | 0.810 | 0.817 | 0.347 | 1.07x | 18.4/21.8% | 4.4% | 3 |
| 1 | 0.675 | - | - | 0.804 | 0.806 | 0.364 | 1.06x | 18.3/21.7% | 4.4% | 3 |
| 2 | 0.661 | - | - | 0.797 | 0.799 | 0.367 | 1.07x | 18.5/21.9% | 4.4% | 3 |
| 4 | 0.671 | - | - | 0.803 | 0.805 | 0.374 | 1.08x | 18.7/22.1% | 4.4% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.25 | 0.680 | - | - | 0.822 | 0.825 | 0.372 | 1.16x | 19.8/23.4% | 4.8% | 3 |
| 1.0 | 0.672 | - | - | 0.821 | 0.823 | 0.356 | 1.27x | 21.7/25.8% | 5.3% | 3 |
| 4.0 | 0.648 | - | - | 0.792 | 0.792 | 0.340 | 1.52x | 26.2/31.3% | 6.4% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.653 | - | - | 0.851 | 0.933 | 0.443 | 4.81x | 69.6/75.0% | 12.4% | 3 |
| 1.0 | 0.607 | - | - | 0.785 | 0.917 | 0.413 | 5.29x | 72.5/77.6% | 12.9% | 3 |

> traceroute-per-hour=0.0: decode_failures 93

> traceroute-per-hour=1.0: decode_failures 78

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 0.768 | - | - | 0.909 | 0.914 | 0.573 | 0.63x | 9.9/10.6% | 2.3% | 3 |
| 2.5 | 0.776 | - | - | 0.908 | 0.914 | 0.593 | 0.64x | 9.9/10.6% | 2.3% | 3 |
| 2.6 | 0.773 | - | - | 0.919 | 0.922 | 0.581 | 0.63x | 10.1/10.7% | 2.3% | 3 |
| 2.7 | 0.777 | - | - | 0.908 | 0.910 | 0.570 | 0.65x | 11.7/13.7% | 2.8% | 3 |
| 2.8 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.653 | - | - | 0.851 | 0.933 | 0.443 | 4.81x | 69.6/75.0% | 12.4% | 3 |
| 25 | 0.653 | - | - | 0.851 | 0.933 | 0.443 | 4.81x | 69.6/75.0% | 12.4% | 3 |
| 100 | 0.653 | - | - | 0.851 | 0.933 | 0.443 | 4.81x | 69.6/75.0% | 12.4% | 3 |
| 2000 | 0.653 | - | - | 0.851 | 0.933 | 0.443 | 4.81x | 69.6/75.0% | 12.4% | 3 |

> warm-num-nodes=0: decode_failures 93

> warm-num-nodes=25: decode_failures 93

> warm-num-nodes=100: decode_failures 93

> warm-num-nodes=2000: decode_failures 93

### `AD-amplifiers` - amplifier-mix  `--scenario rolling`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| sprinkled | 0.871 | - | - | 0.948 | 0.948 | 0.617 | 1.01x | 21.0/25.1% | 5.1% | 3 |
| arms-race | 0.924 | - | - | 0.959 | 0.959 | 0.675 | 0.88x | 25.0/28.4% | 5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.1 | 0.743 | - | - | 0.792 | 0.796 | 0.511 | 1.06x | 18.8/24.4% | 4.6% | 3 |
| 0.3 | 0.914 | - | - | 0.987 | 0.989 | 0.560 | 0.91x | 25.6/28.6% | 5.2% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.475 | - | - | 0.646 | 0.648 | 0.303 | 1.09x | 17.7/20.2% | 4.7% | 3 |
| inverse | 0.457 | - | - | 0.458 | 0.459 | 0.315 | 1.10x | 15.9/17.6% | 4.1% | 3 |
| random | 0.686 | - | - | 0.756 | 0.757 | 0.387 | 1.07x | 16.2/19.5% | 4.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.720 | - | - | 0.869 | 0.871 | 0.376 | 0.76x | 13.7/16.1% | 3.3% | 3 |
| 900 | 0.638 | - | - | 0.814 | 0.814 | 0.311 | 1.74x | 29.2/34.1% | 6.9% | 3 |
| 300 | 0.435 | - | - | 0.577 | 0.577 | 0.220 | 4.05x | 59.7/66.0% | 13.6% | 3 |

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.832 | - | - | 0.882 | 0.882 | 0.670 | 0.84x | 13.6/16.0% | 3.2% | 3 |
| 900 | 0.743 | - | - | 0.782 | 0.785 | 0.620 | 1.96x | 31.5/36.0% | 7.1% | 3 |
| 300 | 0.509 | - | - | 0.483 | 0.486 | 0.399 | 4.38x | 63.0/68.7% | 14.0% | 3 |

> broadcast-interval-s=300: decode_failures 1

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 0.25 | 0.722 | - | - | 0.868 | 0.870 | 0.415 | 1.06x | 20.1/23.3% | 4.6% | 3 |
| 1.0 | 0.849 | - | - | 0.932 | 0.932 | 0.669 | 0.92x | 26.2/27.9% | 5.1% | 3 |

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| temporal | 0.574 | - | - | 0.709 | 0.713 | 0.310 | 1.13x | 18.9/22.1% | 4.2% | 3 |
| transient | 0.687 | - | - | 0.848 | 0.849 | 0.343 | 1.10x | 19.0/22.6% | 4.6% | 3 |
| periodic | 0.524 | - | - | 0.646 | 0.650 | 0.258 | 1.03x | 17.4/20.3% | 3.9% | 3 |

> noise-profile=periodic: decode_failures 1

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.475 | - | - | 0.646 | 0.648 | 0.303 | 1.09x | 17.7/20.2% | 4.7% | 3 |
| no-mute | 0.685 | - | - | 0.844 | 0.845 | 0.495 | 1.12x | 17.5/20.8% | 4.7% | 3 |
| all-routers | 0.798 | - | - | 0.885 | 0.885 | 0.531 | 2.47x | 36.6/39.3% | 5.1% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 0.639 | - | - | 0.766 | 0.769 | 0.351 | 1.11x | 19.0/22.3% | 4.4% | 3 |
| 10000 | 0.524 | - | - | 0.646 | 0.650 | 0.258 | 1.03x | 17.4/20.3% | 3.9% | 3 |
| 4000 | 0.297 | - | - | 0.374 | 0.384 | 0.132 | 0.90x | 14.9/17.6% | 2.9% | 3 |
| 2000 | 0.073 | - | - | 0.103 | 0.136 | 0.016 | 0.67x | 11.6/13.5% | 1.9% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 1

> noise-pulse-interval-ms=4000: decode_failures 2

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.475 | - | - | 0.646 | 0.648 | 0.303 | 1.09x | 17.7/20.2% | 4.7% | 3 |
| local-typical | 0.579 | - | - | 0.867 | 0.885 | 0.000 | 1.01x | 19.1/25.9% | 5.1% | 3 |
| basement-heavy | 0.039 | - | - | 0.119 | 0.119 | 0.000 | 0.32x | 3.9/5.8% | 2.0% | 3 |

> siting-mix=local-typical: decode_failures 2

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 0.688 | - | - | 0.832 | 0.833 | 0.356 | 1.11x | 19.0/22.6% | 4.6% | 3 |
| 1.25 | 0.358 | - | - | 0.537 | 0.537 | 0.138 | 1.34x | 18.3/22.8% | 4.6% | 3 |
| 1.5 | 0.187 | - | - | 0.408 | 0.410 | 0.000 | 1.07x | 13.3/17.1% | 3.7% | 3 |
| 2.0 | 0.098 | - | - | 0.295 | 0.346 | 0.000 | 0.64x | 5.6/11.1% | 2.9% | 3 |

> stretch=2.0: decode_failures 11

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.187 | - | - | 0.408 | 0.410 | 0.000 | 1.07x | 13.3/17.1% | 3.7% | 3 |
| 1.0 | 0.577 | - | - | 0.713 | 0.714 | 0.424 | 0.89x | 19.1/21.9% | 4.0% | 3 |

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.718 | - | - | 0.878 | 0.878 | 0.000 | 2.12x | 24.7/30.3% | 5.3% | 3 |
| inverse | 0.704 | - | - | 0.883 | 0.884 | 0.000 | 2.06x | 21.5/28.7% | 3.1% | 3 |

