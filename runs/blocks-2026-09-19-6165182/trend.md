# Sweep blocks-2026-09-19-6165182

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 6165182 · seeds 6165182
- **blocks** 87 run
- **compute** 14.0 h of simulator time across every cell
- **generated** 2026-09-19T09:05:30+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>112 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 1
- AD-nomute: role-mix=no-mute: decode_failures 1
- AD-siting: siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count
- DB-hotstore: max-num-nodes=10: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 65
- DB-hotstore-stress: max-num-nodes=120: decode_failures 103
- DB-hotstore-stress: max-num-nodes=250: decode_failures 90
- DB-hotstore-stress: slower: 51 s per simulated hour against 22.6 over 29 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-platform: platform-mix=constrained: decode_failures 6
- DB-warm: warm-num-nodes=0: queue drops 13.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 111
- DB-warm: warm-num-nodes=25: queue drops 13.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 111
- DB-warm: warm-num-nodes=100: queue drops 13.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 111
- DB-warm: warm-num-nodes=2000: queue drops 13.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 111
- DG-burst: burst-loss=0.2: decode_failures 26
- DG-burst: burst-loss=0.3: decode_failures 27
- DG-loss: extra-loss=0.3: decode_failures 29
- DG-loss: slower: 4.84 s per simulated hour against 2.22 over 29 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DG-outage: burst-loss=0.1: decode_failures 21
- DG-outage: burst-loss=0.2: decode_failures 30
- DG-outage: burst-loss=0.3: decode_failures 29
- DM-mode: dm-mode=flood-only: decode_failures 33
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 31
- DM-mode: dm-mode=m4-early-flood: decode_failures 4
- DM-mode: slower: 7.59 s per simulated hour against 3.06 over 29 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed-26: legacy-fraction=0.5: decode_failures 17
- FW-mixed: legacy-fraction=0.5: decode_failures 27
- FW-mixed: slower: 3.59 s per simulated hour against 1.66 over 29 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 31
- LD-chatty: broadcast-interval-s=300: decode_failures 23
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 13.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 111
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 20.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 75
- MS-density: nodes=40: decode_failures 1
- MS-hopscale: nodes=250: decode_failures 150
- MS-hopscale: nodes=500: decode_failures 103
- MS-oversubscribed: nodes=250: decode_failures 103
- MS-oversubscribed: nodes=500: decode_failures 68
- MS-siting: siting-mix=event: decode_failures 1
- MS-stretch: stretch=1.5: decode_failures 6
- MS-stretch: stretch=2.0: decode_failures 6
- MS-topology: topology=clustered: decode_failures 52
- MS-topology: slower: 5.5 s per simulated hour against 1.92 over 29 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-crladder: coding-rate-ladder=False: decode_failures 31
- PR-crladder: coding-rate-ladder=True: decode_failures 30
- PR-crladder: slower: 11.3 s per simulated hour against 2.75 over 29 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 30
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 33
- PR-dmmode-cr: slower: 11.6 s per simulated hour against 2.54 over 29 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=SHORT_TURBO: decode_failures 18
- RF-bw500: preset=LONG_TURBO: decode_failures 1
- RF-bw500: slower: 3.88 s per simulated hour against 1.82 over 29 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 6
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 18
- RF-preset-turbo: preset=LONG_TURBO: decode_failures 1
- RF-preset-turbo: slower: 3.26 s per simulated hour against 1.54 over 25 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 7
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 6
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 36
- RF-stretch-duct: slower: 7.36 s per simulated hour against 2 over 29 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 1
- RF-txpower: tx-power=14: decode_failures 4
- RT-hopassign: hop-assign=random: decode_failures 1
- RT-hoplimit: hop-limit=3: decode_failures 3
- RT-hopspread: hop-limit=3: decode_failures 3
- RT-spread: hop-spread=False: decode_failures 3
- SF-bucket-mode: bucket-mode=global: misdecodes 34
- SF-bucket-mode: bucket-mode=time: misdecodes 16
- SF-bucket-mode: bucket-mode=window: misdecodes 13
- SF-bucket-time: time-bucket-s=600: misdecodes 95
- SF-bucket-time: time-bucket-s=1800: misdecodes 16
- SF-bucket-time: time-bucket-s=3600: misdecodes 4
- SF-bucket-time: time-bucket-s=3600: decode_failures 5
- SF-cadence: trigger=interval: misdecodes 7
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 2
- SF-cadence: trigger=bucket+interval: misdecodes 5
- SF-capacity-local: capacity=4: decode_failures 98
- SF-capacity-local: capacity=8: decode_failures 94
- SF-capacity-local: capacity=16: decode_failures 21
- SF-capacity: capacity=4: decode_failures 98
- SF-capacity: capacity=8: decode_failures 94
- SF-capacity: capacity=16: decode_failures 21
- SF-capacity-window: capacity=8: misdecodes 5
- SF-capacity-window: capacity=8: decode_failures 104
- SF-capacity-window: capacity=16: misdecodes 6
- SF-capacity-window: capacity=16: decode_failures 18
- SF-capacity-window: capacity=32: misdecodes 13
- SF-catchup: catch-up-hours=: misdecodes 5
- SF-catchup: catch-up-hours=02-06: decode_failures 25
- SF-catchup: catch-up-hours=00-08: decode_failures 26
- SF-hops-flat: hops-apart=4: decode_failures 11
- SF-hops-spread: hops-apart=4: decode_failures 11
- SF-hops-spread: hops-apart=5: decode_failures 16
- SF-place-flat: place=spread: decode_failures 21
- SF-place-spread: place=spread: decode_failures 21
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 2
- SF-replay-order: replay-ordering=heard: misdecodes 10
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-window-size: window-size=8: misdecodes 107
- SF-window-size: window-size=16: misdecodes 47
- SF-window-size: window-size=32: misdecodes 13
- TH-congestion-input: congestion-input=hotstore: decode_failures 103
- TH-congestion-input: congestion-input=truesize: decode_failures 63
- TH-congestion-input: slower: 47.5 s per simulated hour against 10.5 over 29 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: queue drops 13.3% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 16
- TH-congestion: faster: 8.06 s per simulated hour against 18.1 over 29 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `PR-dmmode-cr` | 11.6 | 2.54 | 4.58x | 29 |
| `TH-congestion-input` | 47.5 | 10.5 | 4.50x | 29 |
| `PR-crladder` | 11.3 | 2.75 | 4.11x | 29 |
| `RF-stretch-duct` | 7.36 | 2 | 3.69x | 29 |
| `MS-topology` | 5.5 | 1.92 | 2.87x | 29 |
| `DM-mode` | 7.59 | 3.06 | 2.48x | 29 |
| `DB-hotstore-stress` | 51 | 22.6 | 2.26x | 29 |
| `DG-loss` | 4.84 | 2.22 | 2.17x | 29 |
| `FW-mixed` | 3.59 | 1.66 | 2.17x | 29 |
| `RF-bw500` | 3.88 | 1.82 | 2.13x | 29 |
| `RF-preset-turbo` | 3.26 | 1.54 | 2.12x | 25 |
| `FW-mixed-26` | 2.86 | 1.65 | 1.73x | 29 |
| `SF-capacity-window` | 2.61 | 1.6 | 1.63x | 29 |
| `SF-bucket-time` | 2.52 | 1.61 | 1.56x | 29 |
| `SF-advert-transport` | 2.72 | 1.77 | 1.54x | 29 |
| `LD-chatty-hops` | 6.62 | 4.36 | 1.52x | 29 |
| `RT-spread` | 3.25 | 2.15 | 1.51x | 29 |
| `SF-catchup` | 6.29 | 9.68 | 0.65x | 29 |
| `TH-congestion` | 8.06 | 18.1 | 0.45x | 29 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.967 | 0.967 | 0.837 → 0.849 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.965 | 0.965 | 0.830 → 0.849 | 1.2x bytes_on_air | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.130 → 0.951 | 0.821 | 0.134 → 0.809 | 37x sr_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.101 → 0.908 | 0.807 | 0.095 → 0.791 | 1.8e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.175 → 0.965 | 0.790 | 0.073 → 0.842 | 6.2x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **text** | 0.100 → 0.855 | 0.755 | 0.099 → 0.842 | 6.2x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.146 → 0.855 | 0.709 | 0.145 → 0.842 | 5x sr_airtime | down | 4 |
| `RF-bw500` | preset | **text** | 0.248 → 0.787 | 0.538 | 0.242 → 0.778 | 2.2x sr_airtime | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.452 → 0.975 | 0.523 | 0.441 → 0.975 | 2.5x sr_bytes | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.344 → 0.855 | 0.511 | 0.339 → 0.842 | 8.4x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.346 → 0.822 | 0.476 | 0.341 → 0.815 | 4.5x bytes_on_air | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.420 → 0.855 | 0.435 | 0.412 → 0.842 | 2.9x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.420 → 0.855 | 0.435 | 0.412 → 0.842 | 2.9x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.535 → 0.963 | 0.428 | 0.523 → 0.962 | 2.6x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.480 → 0.858 | 0.378 | 0.319 → 0.528 | 7.4x sr_airtime | up | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.646 → 0.967 | 0.321 | 0.836 → 0.842 | 1.7x sr_bytes | down | 5 |
| `DG-outage` | burst-loss | **text** | 0.535 → 0.855 | 0.320 | 0.515 → 0.842 | 1.5x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.590 → 0.904 | 0.314 | 0.579 → 0.900 | 10x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.541 → 0.855 | 0.313 | 0.517 → 0.842 | 1.5x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.575 → 0.871 | 0.296 | 0.556 → 0.861 | 10x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.713 → 0.975 | 0.262 | 0.835 → 0.848 | 2.3x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.713 → 0.975 | 0.262 | 0.835 → 0.848 | 2.3x sr_bytes | up | 6 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.449 → 0.707 | 0.257 | 0.443 → 0.693 | 2.3x sr_airtime | up | 2 |
| `MS-density` | nodes | **text** | 0.716 → 0.960 | 0.244 | 0.683 → 0.959 | 4.8x sr_airtime | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.724 → 0.960 | 0.236 | 0.716 → 0.959 | 4.5x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.678 → 0.891 | 0.213 | 0.640 → 0.886 | 2x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.678 → 0.870 | 0.192 | 0.640 → 0.863 | 1.7x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.708 → 0.886 | 0.178 | 0.692 → 0.877 | 4.2x sr_bytes | down | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.788 → 0.967 | 0.178 | 0.836 → 0.842 | 1.7x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.678 → 0.855 | 0.177 | 0.640 → 0.842 | 1.4x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **held** | 0.790 → 0.965 | 0.175 | 0.673 → 0.842 | 1.2x advert_bytes | down | 4 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.821 → 0.984 | 0.163 | 0.835 → 0.884 | 2.2x bytes_on_air | up | 4 |
| `SC-signing` | signature-policy | **text** | 0.726 → 0.855 | 0.129 | 0.726 → 0.842 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.737 → 0.855 | 0.118 | 0.720 → 0.842 | 1.4x sr_bytes | down | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.848 → 0.965 | 0.117 | 0.842 → 0.852 | 36x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.855 → 0.967 | 0.113 | 0.842 → 0.966 | 3x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.855 → 0.957 | 0.102 | 0.842 → 0.956 | 2.3x sr_bytes | up | 3 |
| `FW-mixed` | legacy-fraction | **held** | 0.894 → 0.985 | 0.091 | 0.839 → 0.887 | 2.6x sr_bytes | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.822 → 0.913 | 0.091 | 0.809 → 0.910 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.822 → 0.913 | 0.091 | 0.809 → 0.910 | 2.5x bytes_on_air | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.813 → 0.902 | 0.089 | 0.797 → 0.897 | 2x sr_airtime | up | 4 |
| `SF-cadence` | trigger | **held** | 0.877 → 0.965 | 0.088 | 0.812 → 0.846 | 13x advert_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.819 → 0.902 | 0.083 | 0.802 → 0.897 | 2x sr_airtime | down | 3 |
| `SF-capacity-window` | capacity | **held** | 0.885 → 0.966 | 0.080 | 0.842 → 0.849 | 2.6x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.855 → 0.931 | 0.076 | 0.842 → 0.923 | 1.5x sr_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.826 → 0.896 | 0.069 | 0.518 → 0.554 | 1.5x sr_airtime | up | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.660 → 0.726 | 0.066 | 0.654 → 0.721 | 1.3x sr_airtime | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.827 → 0.887 | 0.060 | 0.812 → 0.881 | 4.7x bytes_on_air | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.800 → 0.855 | 0.054 | 0.782 → 0.842 | 1.4x sr_airtime | down | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.805 → 0.855 | 0.049 | 0.787 → 0.842 | 1.1x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **text** | 0.777 → 0.822 | 0.045 | 0.751 → 0.809 | 1.3x sr_bytes | down | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.910 → 0.949 | 0.039 | 0.812 → 0.847 | 9.3x advert_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.937 → 0.975 | 0.038 | 0.827 → 0.842 | 6.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.937 → 0.975 | 0.038 | 0.827 → 0.842 | 6.4x sr_bytes | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.855 → 0.886 | 0.031 | 0.827 → 0.842 | 3.6x sr_airtime | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.855 → 0.886 | 0.031 | 0.842 → 0.879 | 1.4x sr_bytes | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.855 → 0.884 | 0.029 | 0.842 → 0.876 | 3.2x bytes_on_air | down | 2 |
| `DM-mode` | dm-mode | **held** | 0.900 → 0.926 | 0.027 | 0.802 → 0.810 | 1.2x sr_airtime | up | 3 |
| `AD-worst` | role-placement | **text** | 0.825 → 0.849 | 0.025 | 0.812 → 0.843 | 1.3x sr_bytes | down | 2 |
| `FW-versions` | profile | **held** | 0.965 → 0.989 | 0.024 | 0.833 → 0.842 | 3.3x bytes_on_air | down | 5 |
| `RT-favourites` | favourite-routers | **text** | 0.860 → 0.882 | 0.022 | 0.849 → 0.876 | 1.2x sr_bytes | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.948 → 0.970 | 0.022 | 0.831 → 0.846 | 3x advert_bytes | down | 4 |
| `SF-capacity` | capacity | **held** | 0.944 → 0.965 | 0.022 | 0.835 → 0.842 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.944 → 0.965 | 0.022 | 0.835 → 0.842 | 5.4x advert_bytes | up | 5 |
| `FW-firmware` | profile | **held** | 0.965 → 0.985 | 0.020 | 0.842 → 0.851 | 3.2x bytes_on_air | down | 2 |
| `SF-resolve` | resolve | **held** | 0.948 → 0.965 | 0.017 | 0.842 → 0.842 | 5.9x advert_bytes | = | 3 |
| `SF-window-size` | window-size | **held** | 0.956 → 0.970 | 0.014 | 0.832 → 0.844 | 4.7x advert_bytes | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.855 → 0.868 | 0.013 | 0.842 → 0.859 | 1.3x sr_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.835 → 0.848 | 0.013 | 0.822 → 0.835 | 1.1x sr_airtime | down | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.955 → 0.965 | 0.010 | 0.839 → 0.842 | 2.7x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.950 → 0.960 | 0.010 | 0.949 → 0.959 | 1.2x bytes_on_air | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.955 → 0.966 | 0.010 | 0.837 → 0.842 | 3x advert_bytes | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.944 → 0.954 | 0.010 | 0.822 → 0.834 | 1.1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.900 → 0.909 | 0.009 | 0.810 → 0.810 | 1.1x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.958 → 0.967 | 0.009 | 0.836 → 0.846 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.958 → 0.967 | 0.009 | 0.836 → 0.846 | 1.1x sr_bytes | up | 4 |
| `SF-replay-order` | replay-ordering | **held** | 0.956 → 0.965 | 0.009 | 0.839 → 0.842 | 1.1x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.855 → 0.862 | 0.008 | 0.842 → 0.852 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.843 → 0.849 | 0.006 | 0.831 → 0.839 | 5.3x advert_bytes | up | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.909 → 0.914 | 0.005 | 0.809 → 0.810 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.883 → 0.886 | 0.004 | 0.825 → 0.827 | 1.1x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.970 → 0.974 | 0.004 | 0.840 → 0.845 | 2.3x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **held** | 0.947 → 0.951 | 0.003 | 0.809 → 0.810 | 1.1x bytes_on_air | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.958 → 0.960 | 0.002 | 0.957 → 0.959 | 1x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.960 → 0.962 | 0.002 | 0.959 → 0.962 | 1.1x sr_bytes | down | 2 |

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
| none | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| sprinkled | 1 | 0.928 | 0.925 | 0.004 | - | - | 0.983 | 0.983 | 0.653 | 1.04x | 15.7/21.7/26.1% | 1.3/5.2% | 3 |
| arms-race | 1 | 0.967 | 0.966 | 0.002 | - | - | 0.990 | 0.990 | 0.864 | 1.00x | 20.4/28.2/31.0% | 1.1/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.908 | 0.896 | 0.012 | - | - | 0.991 | 0.991 | 0.591 | 1.28x | 17.3/22.5/28.6% | 1.9/5.1% | 3 |
| 0.3 | 1 | 0.957 | 0.956 | 0.002 | - | - | 0.995 | 0.996 | 0.800 | 1.01x | 18.9/26.0/28.3% | 1.2/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.822 | 0.809 | 0.013 | - | - | 0.951 | 0.955 | 0.318 | 1.10x | 14.9/21.8/27.6% | 1.7/5.0% | 3 |
| inverse | 1 | 0.777 | 0.751 | 0.026 | - | - | 0.932 | 0.935 | 0.423 | 1.06x | 12.1/17.2/21.1% | 1.9/3.4% | 3 |
| random | 1 | 0.797 | 0.769 | 0.028 | - | - | 0.956 | 0.961 | 0.515 | 1.10x | 12.4/17.7/22.3% | 1.7/4.7% | 3 |

> role-placement=inverse: decode_failures 1

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.822 | 0.809 | 0.013 | - | - | 0.951 | 0.955 | 0.318 | 1.10x | 14.9/21.8/27.6% | 1.7/5.0% | 3 |
| all-routers | 1 | 0.913 | 0.910 | 0.003 | - | - | 0.969 | 0.970 | 0.756 | 2.80x | 31.7/39.0/43.3% | 4.5/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.822 | 0.809 | 0.013 | - | - | 0.951 | 0.955 | 0.318 | 1.10x | 14.9/21.8/27.6% | 1.7/5.0% | 3 |
| no-mute | 1 | 0.858 | 0.845 | 0.013 | - | - | 0.965 | 0.968 | 0.519 | 1.27x | 15.9/21.3/27.7% | 2.0/4.9% | 3 |
| all-routers | 1 | 0.913 | 0.910 | 0.003 | - | - | 0.969 | 0.970 | 0.756 | 2.80x | 31.7/39.0/43.3% | 4.5/5.2% | 3 |

> role-mix=no-mute: decode_failures 1

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.822 | 0.809 | 0.013 | - | - | 0.951 | 0.955 | 0.318 | 1.10x | 14.9/21.8/27.6% | 1.7/5.0% | 3 |
| local-typical | 1 | 0.727 | 0.718 | 0.009 | - | - | 0.883 | 0.884 | 0.000 | 1.28x | 12.8/23.0/27.4% | 2.2/5.0% | 3 |
| basement-heavy | 1 | 0.134 | 0.134 | 0.000 | - | - | 0.130 | 0.259 | 0.000 | 0.81x | 3.6/10.9/16.5% | 1.4/3.9% | 2 |

> siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.965 | 0.966 | 0.110 | 2.38x | 16.6/27.3/37.9% | 1.8/5.7% | 3 |
| inverse | 1 | 0.825 | 0.812 | 0.013 | - | - | 0.973 | 0.974 | 0.201 | 2.27x | 14.6/22.9/34.6% | 1.7/3.3% | 3 |

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.849 | 0.849 | 0.000 | - | - | 0 | 0.000 | 0.253 | 1.23x | 15.8/21.7/28.0% | 1.9/5.1% | 3 |
| sr | 1 | 0.855 | 0.837 | 0.017 | - | - | 0.967 | 0.968 | 0.244 | 1.29x | 16.4/22.8/29.2% | 1.9/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.813 | 0.797 | 0.017 | - | - | 0.942 | 0.944 | 0.339 | 2.98x | 38.3/52.1/60.9% | 3.7/10.1% | 3 |
| 100 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.972 | 0.973 | 0.365 | 1.50x | 20.0/27.4/33.5% | 2.0/5.3% | 3 |
| 120 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.972 | 0.973 | 0.365 | 1.50x | 20.0/27.4/33.5% | 2.0/5.3% | 3 |
| 250 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.972 | 0.973 | 0.365 | 1.50x | 20.0/27.4/33.5% | 2.0/5.3% | 3 |

> max-num-nodes=10: decode_failures 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.325 | 0.319 | 0.006 | - | - | 0.480 | 0.730 | 0.072 | 11.37x | 39.2/66.5/77.5% | 4.0/10.7% | 3 |
| 120 | 1 | 0.533 | 0.518 | 0.016 | - | - | 0.826 | 0.909 | 0.103 | 4.78x | 16.5/34.6/46.7% | 1.5/5.9% | 3 |
| 250 | 1 | 0.546 | 0.528 | 0.018 | - | - | 0.858 | 0.916 | 0.105 | 4.66x | 16.0/33.3/45.2% | 1.5/5.8% | 3 |

> max-num-nodes=10: decode_failures 65

> max-num-nodes=120: decode_failures 103

> max-num-nodes=250: decode_failures 90

> slower: 51 s per simulated hour against 22.6 over 29 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.972 | 0.973 | 0.365 | 1.50x | 20.0/27.4/33.5% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.972 | 0.973 | 0.365 | 1.50x | 20.0/27.4/33.5% | 2.0/5.3% | 3 |
| constrained | 1 | 0.819 | 0.802 | 0.017 | - | - | 0.931 | 0.938 | 0.362 | 2.98x | 38.3/52.3/61.0% | 3.7/10.1% | 3 |

> platform-mix=constrained: decode_failures 6

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.847 | 0.888 | 0.526 | 5.56x | 56.6/74.8/79.5% | 3.8/13.4% | 3 |
| 25 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.847 | 0.888 | 0.526 | 5.56x | 56.6/74.8/79.5% | 3.8/13.4% | 3 |
| 100 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.847 | 0.888 | 0.526 | 5.56x | 56.6/74.8/79.5% | 3.8/13.4% | 3 |
| 2000 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.847 | 0.888 | 0.526 | 5.56x | 56.6/74.8/79.5% | 3.8/13.4% | 3 |

> warm-num-nodes=0: queue drops 13.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 111

> warm-num-nodes=25: queue drops 13.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 111

> warm-num-nodes=100: queue drops 13.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 111

> warm-num-nodes=2000: queue drops 13.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 111

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.767 | 0.746 | 0.022 | - | - | 0.944 | 0.949 | 0.227 | 1.19x | 15.5/21.6/27.5% | 1.8/4.8% | 3 |
| 0.2 | 1 | 0.653 | 0.626 | 0.027 | - | - | 0.829 | 0.897 | 0.208 | 1.11x | 14.7/20.3/26.1% | 1.7/4.3% | 3 |
| 0.3 | 1 | 0.541 | 0.517 | 0.025 | - | - | 0.687 | 0.837 | 0.172 | 1.02x | 13.6/18.7/24.3% | 1.5/3.6% | 3 |

> burst-loss=0.2: decode_failures 26

> burst-loss=0.3: decode_failures 27

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.830 | 0.815 | 0.015 | - | - | 0.961 | 0.968 | 0.277 | 1.34x | 17.4/23.5/29.6% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.796 | 0.778 | 0.018 | - | - | 0.931 | 0.939 | 0.294 | 1.40x | 18.1/24.6/30.7% | 2.1/5.0% | 3 |
| 0.3 | 1 | 0.737 | 0.720 | 0.018 | - | - | 0.863 | 0.923 | 0.252 | 1.42x | 18.2/25.0/31.2% | 2.1/4.7% | 3 |

> extra-loss=0.3: decode_failures 29

> slower: 4.84 s per simulated hour against 2.22 over 29 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.750 | 0.731 | 0.020 | - | - | 0.900 | 0.926 | 0.243 | 1.19x | 15.4/21.5/27.5% | 1.8/5.1% | 3 |
| 0.2 | 1 | 0.636 | 0.616 | 0.019 | - | - | 0.777 | 0.905 | 0.205 | 1.13x | 15.1/20.8/26.6% | 1.6/4.5% | 3 |
| 0.3 | 1 | 0.535 | 0.515 | 0.020 | - | - | 0.677 | 0.835 | 0.180 | 1.09x | 14.2/20.1/26.0% | 1.6/4.1% | 3 |

> burst-loss=0.1: decode_failures 21

> burst-loss=0.2: decode_failures 30

> burst-loss=0.3: decode_failures 29

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.809 | 0.809 | 0.000 | - | - | 0.911 | 0.953 | 0.268 | 1.71x | 21.9/30.0/37.6% | 2.6/7.0% | 3 |
| directed-with-late-flood | 1 | 0.810 | 0.810 | 0.000 | - | - | 0.900 | 0.948 | 0.233 | 1.55x | 19.9/27.6/34.9% | 2.3/6.4% | 3 |
| m4-early-flood | 1 | 0.802 | 0.802 | 0.000 | - | - | 0.926 | 0.949 | 0.230 | 1.57x | 20.2/28.0/35.2% | 2.4/6.6% | 3 |

> dm-mode=flood-only: decode_failures 33

> dm-mode=directed-with-late-flood: decode_failures 31

> dm-mode=m4-early-flood: decode_failures 4

> slower: 7.59 s per simulated hour against 3.06 over 29 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.867 | 0.851 | 0.016 | - | - | 0.985 | 0.987 | 0.684 | 0.72x | 8.4/11.4/12.2% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.854 | 0.839 | 0.015 | - | - | 0.949 | 0.949 | 0.324 | 1.18x | 14.8/20.9/25.7% | 1.7/4.7% | 3 |
| 0.5 | 1 | 0.861 | 0.851 | 0.011 | - | - | 0.894 | 0.987 | 0.123 | 1.05x | 14.6/18.0/22.7% | 1.5/4.5% | 3 |
| 0.75 | 1 | 0.894 | 0.887 | 0.007 | - | - | 0.985 | 0.986 | 0.578 | 0.85x | 11.0/14.2/16.9% | 1.2/3.6% | 3 |

> legacy-fraction=0.5: decode_failures 27

> slower: 3.59 s per simulated hour against 1.66 over 29 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.849 | 0.835 | 0.013 | - | - | 0.949 | 0.950 | 0.349 | 1.13x | 14.3/20.5/24.9% | 1.6/4.5% | 3 |
| 0.5 | 1 | 0.859 | 0.853 | 0.006 | - | - | 0.821 | 0.981 | 0.180 | 1.01x | 14.3/17.4/22.4% | 1.4/4.5% | 3 |
| 0.75 | 1 | 0.890 | 0.884 | 0.006 | - | - | 0.984 | 0.984 | 0.574 | 0.82x | 10.8/14.0/16.5% | 1.2/3.6% | 3 |

> legacy-fraction=0.5: decode_failures 17

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.884 | 0.876 | 0.008 | - | - | 0.973 | 0.975 | 0.241 | 0.69x | 9.1/12.7/17.2% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.857 | 0.839 | 0.017 | - | - | 0.986 | 0.992 | 0.667 | 0.71x | 8.7/11.4/13.4% | 1.1/2.5% | 3 |
| 2.5 | 1 | 0.857 | 0.838 | 0.019 | - | - | 0.989 | 0.995 | 0.639 | 0.71x | 8.6/11.2/13.1% | 1.1/2.5% | 3 |
| 2.6 | 1 | 0.858 | 0.836 | 0.022 | - | - | 0.985 | 0.988 | 0.639 | 0.68x | 8.4/11.1/13.2% | 1.0/2.4% | 3 |
| 2.7 | 1 | 0.855 | 0.833 | 0.022 | - | - | 0.988 | 0.989 | 0.632 | 0.70x | 8.9/12.1/14.4% | 1.0/3.2% | 3 |
| 2.8 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.871 | 0.861 | 0.010 | - | - | 0.967 | 0.970 | 0.269 | 0.85x | 10.9/14.8/19.2% | 1.3/3.5% | 3 |
| 900 | 1 | 0.827 | 0.812 | 0.015 | - | - | 0.952 | 0.952 | 0.242 | 1.98x | 25.5/35.2/43.9% | 3.0/8.2% | 3 |
| 300 | 1 | 0.575 | 0.556 | 0.019 | - | - | 0.695 | 0.828 | 0.256 | 4.54x | 54.7/68.4/76.4% | 7.1/16.2% | 3 |

> broadcast-interval-s=300: decode_failures 23

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.904 | 0.900 | 0.004 | - | - | 0.976 | 0.978 | 0.253 | 0.92x | 11.7/15.4/19.8% | 1.4/3.5% | 3 |
| 900 | 1 | 0.855 | 0.844 | 0.011 | - | - | 0.955 | 0.957 | 0.249 | 2.24x | 28.4/37.9/46.8% | 3.5/8.6% | 3 |
| 300 | 1 | 0.590 | 0.579 | 0.011 | - | - | 0.705 | 0.850 | 0.275 | 5.15x | 58.8/71.7/78.1% | 8.3/17.5% | 3 |

> broadcast-interval-s=300: decode_failures 31

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.868 | 0.859 | 0.009 | - | - | 0.969 | 0.971 | 0.249 | 1.18x | 15.2/21.1/27.1% | 1.8/5.0% | 3 |
| sinusoid | 1 | 0.859 | 0.848 | 0.010 | - | - | 0.969 | 0.969 | 0.244 | 1.17x | 15.0/20.5/26.4% | 1.7/4.7% | 3 |
| commuter | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.827 | 0.812 | 0.015 | - | - | 0.952 | 0.952 | 0.242 | 1.98x | 25.5/35.2/43.9% | 3.0/8.2% | 3 |
| 3600 | 1 | 0.871 | 0.861 | 0.010 | - | - | 0.967 | 0.970 | 0.269 | 0.85x | 10.9/14.8/19.2% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.977 | 0.980 | 0.241 | 0.57x | 7.3/10.0/12.9% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.974 | 0.974 | 0.259 | 0.40x | 5.1/6.9/8.9% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.846 | 0.833 | 0.013 | - | - | 0.949 | 0.954 | 0.270 | 1.33x | 17.1/23.7/30.1% | 2.0/5.5% | 3 |
| 1.0 | 1 | 0.835 | 0.822 | 0.013 | - | - | 0.956 | 0.960 | 0.244 | 1.47x | 18.9/26.3/33.3% | 2.2/6.1% | 3 |
| 4.0 | 1 | 0.800 | 0.782 | 0.018 | - | - | 0.936 | 0.938 | 0.251 | 1.82x | 23.9/33.3/41.9% | 2.8/7.7% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.726 | 0.721 | 0.005 | - | - | 0.847 | 0.888 | 0.526 | 5.56x | 56.6/74.8/79.5% | 3.8/13.4% | 3 |
| 1.0 | 1 | 0.660 | 0.654 | 0.006 | - | - | 0.799 | 0.852 | 0.485 | 6.09x | 61.0/75.6/80.6% | 4.4/14.8% | 3 |

> traceroute-per-hour=0.0: queue drops 13.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 111

> traceroute-per-hour=1.0: queue drops 20.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 75

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.716 | 0.683 | 0.033 | - | - | 0.894 | 0.947 | 0.454 | 1.34x | 16.7/23.4/28.2% | 3.3/6.1% | 3 |
| 60 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 90 | 1 | 0.935 | 0.933 | 0.003 | - | - | 0.993 | 0.993 | 0.672 | 1.60x | 19.1/30.9/34.6% | 1.5/4.9% | 3 |
| 120 | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.999 | 1.000 | 0.764 | 1.99x | 21.5/39.5/43.0% | 1.3/4.9% | 3 |
| 150 | 1 | 0.955 | 0.953 | 0.002 | - | - | 1.000 | 1.000 | 0.824 | 2.60x | 28.2/45.5/52.3% | 1.3/5.7% | 3 |

> nodes=40: decode_failures 1

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 120 | 1 | 0.813 | 0.804 | 0.009 | - | - | 0.965 | 0.965 | 0.226 | 2.31x | 15.9/32.4/36.7% | 1.7/5.1% | 3 |
| 250 | 1 | 0.527 | 0.511 | 0.017 | - | - | 0.821 | 0.899 | 0.104 | 5.09x | 17.5/36.9/50.1% | 1.6/6.4% | 3 |
| 500 | 1 | 0.344 | 0.339 | 0.005 | - | - | 0.549 | 0.683 | 0.050 | 10.40x | 20.3/32.9/45.5% | 1.7/6.9% | 3 |

> nodes=250: decode_failures 150

> nodes=500: decode_failures 103

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.822 | 0.815 | 0.008 | - | - | 0.971 | 0.972 | 0.215 | 2.18x | 15.2/30.5/34.6% | 1.5/4.7% | 3 |
| 250 | 1 | 0.533 | 0.518 | 0.016 | - | - | 0.826 | 0.909 | 0.103 | 4.78x | 16.5/34.6/46.7% | 1.5/5.9% | 3 |
| 500 | 1 | 0.346 | 0.341 | 0.005 | - | - | 0.559 | 0.686 | 0.049 | 9.61x | 18.9/31.0/41.7% | 1.6/6.4% | 3 |

> nodes=250: decode_failures 103

> nodes=500: decode_failures 68

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.824 | 0.810 | 0.014 | - | - | 0.947 | 0.953 | 0.239 | 1.26x | 16.1/22.3/28.4% | 1.9/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.822 | 0.809 | 0.013 | - | - | 0.951 | 0.955 | 0.318 | 1.10x | 14.9/21.8/27.6% | 1.7/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.835 | 0.822 | 0.013 | - | - | 0.944 | 0.951 | 0.267 | 1.30x | 16.6/22.6/28.7% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.845 | 0.834 | 0.010 | - | - | 0.954 | 0.954 | 0.339 | 1.25x | 17.1/25.0/30.2% | 2.1/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.05 | 1 | 0.866 | 0.858 | 0.008 | - | - | 0.969 | 0.970 | 0.290 | 1.40x | 18.2/26.1/32.8% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.872 | 0.865 | 0.007 | - | - | 0.972 | 0.973 | 0.268 | 1.51x | 19.8/29.1/35.6% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.977 | 0.979 | 0.273 | 1.73x | 23.2/31.0/37.0% | 2.3/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| local-typical | 1 | 0.675 | 0.671 | 0.005 | - | - | 0.823 | 0.823 | 0.000 | 1.52x | 13.6/25.3/28.2% | 2.3/5.2% | 3 |
| event | 1 | 0.452 | 0.441 | 0.011 | - | - | 0.621 | 0.626 | 0.000 | 1.47x | 8.9/14.3/18.4% | 2.2/4.2% | 3 |
| backbone | 1 | 0.975 | 0.975 | 0.000 | - | - | 0.999 | 0.999 | 0.916 | 1.05x | 23.6/30.6/34.5% | 1.1/5.5% | 3 |

> siting-mix=event: decode_failures 1

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.807 | 0.785 | 0.023 | - | - | 0.966 | 0.977 | 0.652 | 1.41x | 22.0/27.6/32.2% | 3.5/6.7% | 3 |
| 60 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 90 | 1 | 0.886 | 0.877 | 0.009 | - | - | 0.989 | 0.991 | 0.188 | 1.80x | 16.8/30.3/36.6% | 1.7/5.0% | 3 |
| 120 | 1 | 0.813 | 0.804 | 0.009 | - | - | 0.965 | 0.965 | 0.226 | 2.31x | 15.9/32.4/36.7% | 1.7/5.1% | 3 |
| 150 | 1 | 0.708 | 0.692 | 0.016 | - | - | 0.937 | 0.939 | 0.134 | 2.90x | 15.9/31.4/38.9% | 1.6/5.2% | 3 |

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 1.25 | 1 | 0.682 | 0.667 | 0.015 | - | - | 0.882 | 0.885 | 0.000 | 1.34x | 12.6/18.4/22.1% | 1.9/5.1% | 3 |
| 1.5 | 1 | 0.449 | 0.443 | 0.006 | - | - | 0.554 | 0.577 | 0.000 | 1.32x | 10.1/15.1/16.1% | 2.0/4.4% | 3 |
| 2.0 | 1 | 0.146 | 0.145 | 0.002 | - | - | 0.278 | 0.300 | 0.000 | 0.89x | 4.8/9.0/12.7% | 1.5/3.1% | 3 |

> stretch=1.5: decode_failures 6

> stretch=2.0: decode_failures 6

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| clustered | 1 | 0.869 | 0.863 | 0.006 | - | - | 0.902 | 0.932 | 0.000 | 1.22x | 25.5/33.1/35.0% | 1.6/5.5% | 3 |
| corridor | 1 | 0.535 | 0.523 | 0.012 | - | - | 0.790 | 0.791 | 0.149 | 1.38x | 15.9/24.8/26.3% | 2.2/4.8% | 3 |
| hub | 1 | 0.963 | 0.962 | 0.001 | - | - | 0.992 | 0.992 | 0.894 | 1.23x | 25.6/35.4/37.1% | 1.9/5.5% | 3 |

> topology=clustered: decode_failures 52

> slower: 5.5 s per simulated hour against 1.92 over 29 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.810 | 0.810 | 0.000 | - | - | 0.900 | 0.948 | 0.233 | 1.55x | 19.9/27.6/34.9% | 2.3/6.4% | 3 |
| True | 1 | 0.810 | 0.810 | 0.000 | - | - | 0.909 | 0.950 | 0.250 | 1.56x | 20.0/27.9/35.1% | 2.3/6.5% | 3 |

> coding-rate-ladder=False: decode_failures 31

> coding-rate-ladder=True: decode_failures 30

> slower: 11.3 s per simulated hour against 2.75 over 29 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.810 | 0.810 | 0.000 | - | - | 0.909 | 0.950 | 0.250 | 1.56x | 20.0/27.9/35.1% | 2.3/6.5% | 3 |
| m4-early-flood | 1 | 0.809 | 0.809 | 0.000 | - | - | 0.914 | 0.950 | 0.244 | 1.56x | 20.1/27.9/35.0% | 2.3/6.5% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 30

> dm-mode=m4-early-flood: decode_failures 33

> slower: 11.6 s per simulated hour against 2.54 over 29 prior run(s) - 4.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.849 | 0.849 | 0.000 | - | - | 0 | 0.000 | 0.253 | 1.23x | 15.8/21.7/28.0% | 1.9/5.1% | 3 |
| chain | 1 | 0.834 | 0.830 | 0.004 | - | - | 0.873 | 0.963 | 0.256 | 1.49x | 19.1/26.2/33.3% | 2.3/6.1% | 3 |
| sr | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| True | 1 | 0.862 | 0.852 | 0.011 | - | - | 0.968 | 0.972 | 0.280 | 1.29x | 16.6/22.8/29.0% | 2.0/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.999 | 1.000 | 0.764 | 1.99x | 21.5/39.5/43.0% | 1.3/4.9% | 3 |
| True | 1 | 0.958 | 0.957 | 0.001 | - | - | 0.998 | 0.998 | 0.771 | 2.04x | 22.0/40.1/43.6% | 1.3/5.0% | 3 |

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.248 | 0.242 | 0.007 | - | - | 0.455 | 0.482 | 0.000 | 0.06x | 0.3/0.7/0.9% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.580 | 0.569 | 0.011 | - | - | 0.741 | 0.743 | 0.000 | 0.30x | 2.6/3.7/4.7% | 0.5/1.1% | 3 |
| LONG_TURBO | 1 | 0.787 | 0.778 | 0.009 | - | - | 0.918 | 0.920 | 0.268 | 1.28x | 14.7/19.4/22.4% | 1.9/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 18

> preset=LONG_TURBO: decode_failures 1

> slower: 3.88 s per simulated hour against 1.82 over 29 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.871 | 0.861 | 0.011 | - | - | 0.968 | 0.968 | 0.341 | 1.12x | 16.5/23.1/27.9% | 1.6/5.1% | 3 |
| 1.0 | 1 | 0.931 | 0.923 | 0.008 | - | - | 0.983 | 0.983 | 0.655 | 0.94x | 21.2/27.5/29.8% | 1.1/5.1% | 3 |

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.420 | 0.412 | 0.008 | - | - | 0.616 | 0.619 | 0.000 | 0.17x | 1.3/2.2/3.0% | 0.3/0.6% | 3 |
| LONG_FAST | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| LITE_FAST | 1 | 0.818 | 0.805 | 0.013 | - | - | 0.920 | 0.926 | 0.416 | 1.02x | 12.1/17.1/19.5% | 1.5/4.1% | 3 |
| NARROW_SLOW | 1 | 0.797 | 0.791 | 0.006 | - | - | 0.937 | 0.942 | 0.406 | 1.21x | 14.5/20.2/26.1% | 1.7/5.5% | 3 |

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| temporal | 1 | 0.790 | 0.775 | 0.014 | - | - | 0.936 | 0.938 | 0.169 | 1.31x | 16.5/22.2/27.9% | 2.0/5.1% | 3 |
| transient | 1 | 0.847 | 0.834 | 0.013 | - | - | 0.956 | 0.960 | 0.270 | 1.27x | 16.3/22.4/28.5% | 2.0/5.2% | 3 |
| periodic | 1 | 0.686 | 0.673 | 0.013 | - | - | 0.790 | 0.798 | 0.249 | 1.18x | 15.2/20.9/26.4% | 1.8/4.5% | 3 |

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.420 | 0.412 | 0.008 | - | - | 0.616 | 0.619 | 0.000 | 0.17x | 1.3/2.2/3.0% | 0.3/0.6% | 3 |
| LONG_FAST | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| LONG_MODERATE | 1 | 0.818 | 0.807 | 0.011 | - | - | 0.944 | 0.945 | 0.415 | 3.28x | 45.3/58.0/65.1% | 4.5/12.7% | 3 |

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.073 | 0.073 | 0.001 | - | - | 0.175 | 0.188 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.248 | 0.242 | 0.007 | - | - | 0.455 | 0.482 | 0.000 | 0.06x | 0.3/0.7/0.9% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| LONG_TURBO | 1 | 0.787 | 0.778 | 0.009 | - | - | 0.918 | 0.920 | 0.268 | 1.28x | 14.7/19.4/22.4% | 1.9/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.849 | 0.837 | 0.011 | - | - | 0.960 | 0.963 | 0.355 | 1.71x | 21.2/27.2/34.3% | 2.3/7.1% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 6

> preset=SHORT_TURBO: decode_failures 18

> preset=LONG_TURBO: decode_failures 1

> slower: 3.26 s per simulated hour against 1.54 over 25 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.804 | 0.791 | 0.013 | - | - | 0.908 | 0.912 | 0.258 | 1.25x | 16.3/22.3/28.4% | 1.9/5.0% | 3 |
| 10000 | 1 | 0.686 | 0.673 | 0.013 | - | - | 0.790 | 0.798 | 0.249 | 1.18x | 15.2/20.9/26.4% | 1.8/4.5% | 3 |
| 4000 | 1 | 0.459 | 0.453 | 0.006 | - | - | 0.498 | 0.583 | 0.175 | 1.02x | 13.3/18.4/23.4% | 1.5/3.5% | 3 |
| 2000 | 1 | 0.095 | 0.095 | 0.000 | - | - | 0.101 | 0.168 | 0.026 | 0.72x | 9.7/13.2/16.9% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 7

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.449 | 0.443 | 0.006 | - | - | 0.554 | 0.577 | 0.000 | 1.32x | 10.1/15.1/16.1% | 2.0/4.4% | 3 |
| 1.0 | 1 | 0.707 | 0.693 | 0.013 | - | - | 0.775 | 0.791 | 0.080 | 1.01x | 14.1/18.0/22.3% | 1.4/4.5% | 3 |

> duct-per-hour=0.0: decode_failures 6

> duct-per-hour=1.0: decode_failures 36

> slower: 7.36 s per simulated hour against 2 over 29 prior run(s) - 3.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 22 | 1 | 0.512 | 0.500 | 0.012 | - | - | 0.677 | 0.687 | 0.000 | 1.37x | 11.5/14.6/18.7% | 2.2/4.5% | 3 |
| 17 | 1 | 0.218 | 0.216 | 0.002 | - | - | 0.371 | 0.372 | 0.000 | 1.23x | 6.9/12.4/16.6% | 1.9/4.1% | 3 |
| 14 | 1 | 0.100 | 0.099 | 0.001 | - | - | 0.215 | 0.281 | 0.000 | 0.71x | 3.2/6.7/11.0% | 1.1/2.7% | 3 |

> tx-power=22: decode_failures 1

> tx-power=14: decode_failures 4

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.999 | 1.000 | 0.764 | 1.99x | 21.5/39.5/43.0% | 1.3/4.9% | 3 |
| True | 1 | 0.950 | 0.949 | 0.002 | - | - | 0.997 | 0.998 | 0.749 | 2.38x | 25.5/44.8/48.7% | 1.6/5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.860 | 0.849 | 0.011 | - | - | 0.967 | 0.968 | 0.298 | 1.31x | 17.1/24.6/30.2% | 1.7/5.4% | 3 |
| True | 1 | 0.882 | 0.876 | 0.007 | - | - | 0.968 | 0.970 | 0.304 | 1.36x | 17.3/24.8/30.3% | 1.8/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| random | 1 | 0.805 | 0.787 | 0.019 | - | - | 0.938 | 0.942 | 0.224 | 1.24x | 15.7/22.0/28.0% | 1.8/5.1% | 3 |

> hop-assign=random: decode_failures 1

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.678 | 0.640 | 0.038 | - | - | 0.894 | 0.908 | 0.136 | 0.94x | 12.8/19.0/24.4% | 1.3/4.6% | 3 |
| 7 | 1 | 0.870 | 0.863 | 0.007 | - | - | 0.951 | 0.953 | 0.235 | 1.36x | 17.5/23.4/29.8% | 2.1/5.3% | 3 |
| 15 | 1 | 0.891 | 0.886 | 0.004 | - | - | 0.958 | 0.959 | 0.275 | 1.39x | 17.8/23.6/30.2% | 2.1/5.4% | 3 |
| 32 | 1 | 0.891 | 0.886 | 0.004 | - | - | 0.958 | 0.959 | 0.275 | 1.39x | 17.8/23.6/30.2% | 2.1/5.4% | 3 |

> hop-limit=3: decode_failures 3

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.678 | 0.640 | 0.038 | - | - | 0.894 | 0.908 | 0.136 | 0.94x | 12.8/19.0/24.4% | 1.3/4.6% | 3 |
| 5 | 1 | 0.826 | 0.812 | 0.014 | - | - | 0.944 | 0.950 | 0.184 | 1.25x | 16.0/22.3/28.4% | 1.9/5.2% | 3 |
| 7 | 1 | 0.870 | 0.863 | 0.007 | - | - | 0.951 | 0.953 | 0.235 | 1.36x | 17.5/23.4/29.8% | 2.1/5.3% | 3 |

> hop-limit=3: decode_failures 3

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.852 | 0.852 | 0.000 | - | - | 0.848 | 0.969 | 0.275 | 1.24x | 15.9/21.9/28.1% | 1.9/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.678 | 0.640 | 0.038 | - | - | 0.894 | 0.908 | 0.136 | 0.94x | 12.8/19.0/24.4% | 1.3/4.6% | 3 |
| True | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

> hop-spread=False: decode_failures 3

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| BALANCED | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| STRICT | 1 | 0.726 | 0.726 | 0.000 | - | - | 0.858 | 0.865 | 0.145 | 1.37x | 17.7/24.0/30.6% | 2.1/5.6% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| dm | 1 | 0.852 | 0.839 | 0.012 | - | - | 0.955 | 0.957 | 0.258 | 1.25x | 16.1/22.5/28.6% | 1.9/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.850 | 0.838 | 0.013 | - | - | 0.955 | 0.961 | 0.257 | 1.28x | 16.5/22.7/29.0% | 1.9/5.3% | 3 |
| local | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| time | 1 | 0.849 | 0.837 | 0.012 | - | - | 0.960 | 0.964 | 0.248 | 1.30x | 16.7/23.0/29.2% | 2.0/5.3% | 3 |
| window | 1 | 0.854 | 0.842 | 0.012 | - | - | 0.966 | 0.969 | 0.251 | 1.27x | 16.4/22.6/28.9% | 1.9/5.3% | 3 |

> bucket-mode=global: misdecodes 34

> bucket-mode=time: misdecodes 16

> bucket-mode=window: misdecodes 13

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.843 | 0.831 | 0.012 | - | - | 0.959 | 0.963 | 0.263 | 1.44x | 18.4/25.4/31.7% | 2.2/5.9% | 3 |
| 1800 | 1 | 0.849 | 0.837 | 0.012 | - | - | 0.960 | 0.964 | 0.248 | 1.30x | 16.7/23.0/29.2% | 2.0/5.3% | 3 |
| 3600 | 1 | 0.849 | 0.839 | 0.011 | - | - | 0.957 | 0.969 | 0.252 | 1.29x | 16.6/22.9/29.1% | 2.0/5.3% | 3 |

> time-bucket-s=600: misdecodes 95

> time-bucket-s=1800: misdecodes 16

> time-bucket-s=3600: misdecodes 4

> time-bucket-s=3600: decode_failures 5

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| interval | 1 | 0.835 | 0.820 | 0.014 | - | - | 0.944 | 0.960 | 0.258 | 1.75x | 22.5/30.7/37.8% | 2.7/7.0% | 3 |
| aimd | 1 | 0.849 | 0.846 | 0.003 | - | - | 0.877 | 0.965 | 0.270 | 1.27x | 16.3/22.5/28.8% | 1.9/5.3% | 3 |
| bucket+interval | 1 | 0.827 | 0.812 | 0.015 | - | - | 0.949 | 0.951 | 0.275 | 1.79x | 23.1/31.5/38.7% | 2.7/7.3% | 3 |

> trigger=interval: misdecodes 7

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 2

> trigger=bucket+interval: misdecodes 5

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.851 | 0.841 | 0.010 | - | - | 0.950 | 0.962 | 0.251 | 1.27x | 16.3/22.8/28.7% | 1.9/5.3% | 3 |
| 8 | 1 | 0.844 | 0.835 | 0.009 | - | - | 0.944 | 0.956 | 0.248 | 1.26x | 16.1/22.6/28.6% | 1.9/5.2% | 3 |
| 16 | 1 | 0.849 | 0.837 | 0.013 | - | - | 0.953 | 0.957 | 0.269 | 1.28x | 16.3/22.8/28.9% | 1.9/5.3% | 3 |
| 32 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 50 | 1 | 0.854 | 0.842 | 0.012 | - | - | 0.961 | 0.962 | 0.236 | 1.27x | 16.3/22.4/28.6% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 98

> capacity=8: decode_failures 94

> capacity=16: decode_failures 21

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.851 | 0.841 | 0.010 | - | - | 0.950 | 0.962 | 0.251 | 1.27x | 16.3/22.8/28.7% | 1.9/5.3% | 3 |
| 8 | 1 | 0.844 | 0.835 | 0.009 | - | - | 0.944 | 0.956 | 0.248 | 1.26x | 16.1/22.6/28.6% | 1.9/5.2% | 3 |
| 16 | 1 | 0.849 | 0.837 | 0.013 | - | - | 0.953 | 0.957 | 0.269 | 1.28x | 16.3/22.8/28.9% | 1.9/5.3% | 3 |
| 32 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 50 | 1 | 0.854 | 0.842 | 0.012 | - | - | 0.961 | 0.962 | 0.236 | 1.27x | 16.3/22.4/28.6% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 98

> capacity=8: decode_failures 94

> capacity=16: decode_failures 21

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.849 | 0.845 | 0.004 | - | - | 0.885 | 0.965 | 0.252 | 1.25x | 15.9/22.1/28.4% | 1.9/5.2% | 3 |
| 16 | 1 | 0.860 | 0.849 | 0.011 | - | - | 0.962 | 0.971 | 0.245 | 1.27x | 16.2/22.5/28.8% | 1.9/5.2% | 3 |
| 32 | 1 | 0.854 | 0.842 | 0.012 | - | - | 0.966 | 0.969 | 0.251 | 1.27x | 16.4/22.6/28.9% | 1.9/5.3% | 3 |

> capacity=8: misdecodes 5

> capacity=8: decode_failures 104

> capacity=16: misdecodes 6

> capacity=16: decode_failures 18

> capacity=32: misdecodes 13

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.827 | 0.812 | 0.015 | - | - | 0.949 | 0.951 | 0.275 | 1.79x | 23.1/31.5/38.7% | 2.7/7.3% | 3 |
| 02-06 | 1 | 0.854 | 0.847 | 0.007 | - | - | 0.920 | 0.971 | 0.251 | 1.28x | 16.4/23.0/29.2% | 1.9/5.4% | 3 |
| 00-08 | 1 | 0.850 | 0.843 | 0.006 | - | - | 0.910 | 0.962 | 0.251 | 1.36x | 17.4/24.3/30.8% | 2.1/5.7% | 3 |

> catch-up-hours=: misdecodes 5

> catch-up-hours=02-06: decode_failures 25

> catch-up-hours=00-08: decode_failures 26

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.840 | 0.836 | 0.004 | - | - | 0.939 | 0.939 | 0.252 | 1.25x | 16.2/22.2/28.5% | 1.9/5.3% | 3 |
| 2 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 3 | 1 | 0.855 | 0.837 | 0.017 | - | - | 0.967 | 0.968 | 0.244 | 1.29x | 16.4/22.8/29.2% | 1.9/5.3% | 3 |
| 4 | 1 | 0.860 | 0.841 | 0.019 | - | - | 0.788 | 0.986 | 0.239 | 1.27x | 16.2/22.2/28.4% | 1.9/5.2% | 3 |

> hops-apart=4: decode_failures 11

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.840 | 0.836 | 0.004 | - | - | 0.939 | 0.939 | 0.252 | 1.25x | 16.2/22.2/28.5% | 1.9/5.3% | 3 |
| 2 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 3 | 1 | 0.855 | 0.837 | 0.017 | - | - | 0.967 | 0.968 | 0.244 | 1.29x | 16.4/22.8/29.2% | 1.9/5.3% | 3 |
| 4 | 1 | 0.860 | 0.841 | 0.019 | - | - | 0.788 | 0.986 | 0.239 | 1.27x | 16.2/22.2/28.4% | 1.9/5.2% | 3 |
| 5 | 1 | 0.846 | 0.838 | 0.009 | - | - | 0.646 | 0.957 | 0.260 | 1.25x | 16.0/21.9/28.1% | 1.9/5.2% | 3 |

> hops-apart=4: decode_failures 11

> hops-apart=5: decode_failures 16

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.852 | 0.841 | 0.011 | - | - | 0.958 | 0.961 | 0.252 | 1.30x | 16.6/23.1/29.3% | 1.9/5.3% | 3 |
| 30 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 120 | 1 | 0.849 | 0.836 | 0.013 | - | - | 0.965 | 0.967 | 0.260 | 1.27x | 16.3/22.6/28.7% | 1.9/5.3% | 3 |
| 600 | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.967 | 0.968 | 0.258 | 1.27x | 16.3/22.5/28.7% | 1.9/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.852 | 0.841 | 0.011 | - | - | 0.958 | 0.961 | 0.252 | 1.30x | 16.6/23.1/29.3% | 1.9/5.3% | 3 |
| 30 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 120 | 1 | 0.849 | 0.836 | 0.013 | - | - | 0.965 | 0.967 | 0.260 | 1.27x | 16.3/22.6/28.7% | 1.9/5.3% | 3 |
| 600 | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.967 | 0.968 | 0.258 | 1.27x | 16.3/22.5/28.7% | 1.9/5.2% | 3 |

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.860 | 0.848 | 0.013 | - | - | 0.713 | 0.965 | 0.254 | 1.26x | 16.1/22.1/28.5% | 1.9/5.2% | 3 |
| routers | 1 | 0.851 | 0.845 | 0.006 | - | - | 0.974 | 0.976 | 0.258 | 1.26x | 16.0/22.3/28.7% | 1.9/5.4% | 3 |
| alternate-routers | 1 | 0.838 | 0.835 | 0.003 | - | - | 0.948 | 0.949 | 0.264 | 1.25x | 16.0/22.0/28.3% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.852 | 0.845 | 0.007 | - | - | 0.975 | 0.977 | 0.279 | 1.27x | 16.1/22.3/28.6% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.861 | 0.844 | 0.017 | - | - | 0.971 | 0.974 | 0.267 | 1.27x | 16.2/22.3/28.6% | 1.9/5.2% | 3 |
| hops-apart | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

> place=spread: decode_failures 21

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.860 | 0.848 | 0.013 | - | - | 0.713 | 0.965 | 0.254 | 1.26x | 16.1/22.1/28.5% | 1.9/5.2% | 3 |
| routers | 1 | 0.851 | 0.845 | 0.006 | - | - | 0.974 | 0.976 | 0.258 | 1.26x | 16.0/22.3/28.7% | 1.9/5.4% | 3 |
| alternate-routers | 1 | 0.838 | 0.835 | 0.003 | - | - | 0.948 | 0.949 | 0.264 | 1.25x | 16.0/22.0/28.3% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.852 | 0.845 | 0.007 | - | - | 0.975 | 0.977 | 0.279 | 1.27x | 16.1/22.3/28.6% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.861 | 0.844 | 0.017 | - | - | 0.971 | 0.974 | 0.267 | 1.27x | 16.2/22.3/28.6% | 1.9/5.2% | 3 |
| hops-apart | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

> place=spread: decode_failures 21

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| broadcast | 1 | 0.886 | 0.827 | 0.059 | - | - | 0.952 | 0.962 | 0.333 | 1.42x | 18.1/24.7/31.0% | 2.2/5.8% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| heard | 1 | 0.850 | 0.839 | 0.011 | - | - | 0.956 | 0.964 | 0.269 | 1.27x | 16.4/22.7/28.8% | 1.9/5.3% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.886 | 0.827 | 0.059 | - | - | 0.952 | 0.962 | 0.333 | 1.42x | 18.1/24.7/31.0% | 2.2/5.8% | 3 |
| heard | 1 | 0.883 | 0.825 | 0.057 | - | - | 0.950 | 0.956 | 0.313 | 1.42x | 18.2/24.7/31.1% | 2.2/5.7% | 3 |

> replay-ordering=heard: misdecodes 2

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| enum | 1 | 0.852 | 0.842 | 0.010 | - | - | 0.948 | 0.966 | 0.276 | 1.26x | 16.1/22.5/28.6% | 1.9/5.2% | 3 |
| hybrid | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.851 | 0.845 | 0.006 | - | - | 0.974 | 0.976 | 0.258 | 1.26x | 16.0/22.3/28.7% | 1.9/5.4% | 3 |
| 6 | 1 | 0.850 | 0.840 | 0.010 | - | - | 0.970 | 0.972 | 0.277 | 1.28x | 16.2/22.8/29.1% | 1.9/5.5% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.846 | 0.841 | 0.006 | - | - | 0.937 | 0.946 | 0.252 | 1.25x | 16.2/22.1/28.4% | 1.9/5.2% | 2 |
| 3 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 5 | 1 | 0.853 | 0.837 | 0.015 | - | - | 0.974 | 0.976 | 0.256 | 1.31x | 16.9/23.3/29.4% | 2.0/5.3% | 5 |
| 8 | 1 | 0.849 | 0.827 | 0.022 | - | - | 0.975 | 0.978 | 0.249 | 1.33x | 16.9/23.9/29.9% | 2.0/5.4% | 8 |

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.846 | 0.841 | 0.006 | - | - | 0.937 | 0.946 | 0.252 | 1.25x | 16.2/22.1/28.4% | 1.9/5.2% | 2 |
| 3 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 5 | 1 | 0.853 | 0.837 | 0.015 | - | - | 0.974 | 0.976 | 0.256 | 1.31x | 16.9/23.3/29.4% | 2.0/5.3% | 5 |
| 8 | 1 | 0.849 | 0.827 | 0.022 | - | - | 0.975 | 0.978 | 0.249 | 1.33x | 16.9/23.9/29.9% | 2.0/5.4% | 8 |

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| True | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.842 | 0.830 | 0.013 | - | - | 0.941 | 0.958 | 0.228 | 1.21x | 15.5/21.1/27.0% | 1.8/4.9% | 3 |
| 1 | 1 | 0.848 | 0.835 | 0.013 | - | - | 0.951 | 0.955 | 0.240 | 1.21x | 15.5/21.2/27.0% | 1.8/4.9% | 3 |
| 2 | 1 | 0.835 | 0.822 | 0.014 | - | - | 0.942 | 0.951 | 0.232 | 1.20x | 15.3/20.9/26.7% | 1.8/4.9% | 3 |
| 4 | 1 | 0.841 | 0.825 | 0.015 | - | - | 0.944 | 0.949 | 0.253 | 1.19x | 15.2/21.0/26.7% | 1.8/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.858 | 0.846 | 0.011 | - | - | 0.970 | 0.971 | 0.257 | 1.27x | 16.4/22.7/28.9% | 1.9/5.3% | 3 |
| 24 | 1 | 0.842 | 0.831 | 0.011 | - | - | 0.952 | 0.954 | 0.231 | 1.26x | 16.2/22.3/28.5% | 1.9/5.2% | 3 |
| 32 | 1 | 0.855 | 0.842 | 0.013 | - | - | 0.965 | 0.966 | 0.254 | 1.28x | 16.5/22.8/29.0% | 1.9/5.3% | 3 |
| 64 | 1 | 0.844 | 0.833 | 0.011 | - | - | 0.948 | 0.953 | 0.271 | 1.30x | 16.7/22.9/29.3% | 2.0/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.847 | 0.832 | 0.015 | - | - | 0.956 | 0.959 | 0.264 | 1.39x | 17.8/24.5/30.9% | 2.1/5.7% | 3 |
| 16 | 1 | 0.855 | 0.844 | 0.011 | - | - | 0.970 | 0.973 | 0.263 | 1.29x | 16.7/23.0/29.2% | 2.0/5.3% | 3 |
| 32 | 1 | 0.854 | 0.842 | 0.012 | - | - | 0.966 | 0.969 | 0.251 | 1.27x | 16.4/22.6/28.9% | 1.9/5.3% | 3 |

> window-size=8: misdecodes 107

> window-size=16: misdecodes 47

> window-size=32: misdecodes 13

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.999 | 1.000 | 0.764 | 1.99x | 21.5/39.5/43.0% | 1.3/4.9% | 3 |
| True | 1 | 0.724 | 0.716 | 0.008 | - | - | 0.863 | 0.887 | 0.522 | 5.56x | 56.5/74.6/79.4% | 3.9/13.4% | 3 |

> no-congestion-scaling=True: queue drops 13.3% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 16

> faster: 8.06 s per simulated hour against 18.1 over 29 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.533 | 0.518 | 0.016 | - | - | 0.826 | 0.909 | 0.103 | 4.78x | 16.5/34.6/46.7% | 1.5/5.9% | 3 |
| truesize | 1 | 0.573 | 0.554 | 0.018 | - | - | 0.896 | 0.930 | 0.106 | 3.59x | 12.4/27.5/37.8% | 1.1/5.0% | 3 |

> congestion-input=hotstore: decode_failures 103

> congestion-input=truesize: decode_failures 63

> slower: 47.5 s per simulated hour against 10.5 over 29 prior run(s) - 4.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.962 | 0.962 | 0.001 | - | - | 0.998 | 0.998 | 0.771 | 1.87x | 20.3/37.4/40.8% | 1.2/4.6% | 3 |
| adaptive | 1 | 0.960 | 0.959 | 0.001 | - | - | 0.999 | 1.000 | 0.764 | 1.99x | 21.5/39.5/43.0% | 1.3/4.9% | 3 |

