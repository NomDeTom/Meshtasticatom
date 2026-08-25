# Sweep blocks-2026-08-25-6335397

- **sim version** `1.4.0`
- **transport** `591429c`
- **ground** rolling
- **seed base** 6335397 · seeds 6335397
- **blocks** 86 run, 1 missing
- **compute** 12.2 h of simulator time across every cell
- **generated** 2026-08-25T05:55:18+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>98 warnings</summary>

- SF-cadence: trigger=interval: misdecodes 26
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=bucket+interval: misdecodes 32
- SF-capacity: capacity=4: decode_failures 78
- SF-capacity: capacity=8: decode_failures 55
- SF-capacity: capacity=16: decode_failures 3
- DG-burst: burst-loss=0.2: decode_failures 3
- DG-burst: burst-loss=0.3: decode_failures 20
- DG-outage: burst-loss=0.1: decode_failures 30
- DG-outage: burst-loss=0.2: decode_failures 46
- DG-outage: burst-loss=0.3: decode_failures 33
- RF-txpower: tx-power=22: decode_failures 22
- RF-txpower: tx-power=14: decode_failures 4
- SF-servers-allrouters: servers=6: misdecodes 2
- SF-hops-flat: hops-apart=3: decode_failures 11
- SF-hops-flat: hops-apart=4: decode_failures 20
- SF-place-flat: place=spread: decode_failures 34
- SF-place-flat: place=random-clients: decode_failures 34
- SF-servers-flat: servers=8: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 42
- SF-bucket-mode: bucket-mode=time: misdecodes 44
- SF-bucket-mode: bucket-mode=window: misdecodes 20
- SF-bucket-time: time-bucket-s=600: misdecodes 106
- SF-bucket-time: time-bucket-s=1800: misdecodes 44
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-capacity-window: capacity=8: misdecodes 18
- SF-capacity-window: capacity=8: decode_failures 21
- SF-capacity-window: capacity=16: misdecodes 24
- SF-capacity-window: capacity=16: decode_failures 1
- SF-capacity-window: capacity=32: misdecodes 20
- SF-window-size: window-size=8: misdecodes 149
- SF-window-size: window-size=16: misdecodes 72
- SF-window-size: window-size=32: misdecodes 20
- MS-size: nodes=120: decode_failures 68
- MS-size: nodes=150: decode_failures 9
- MS-size: slower: 8.61 s per simulated hour against 3.4 over 4 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-capacity-local: capacity=4: decode_failures 78
- SF-capacity-local: capacity=8: decode_failures 55
- SF-capacity-local: capacity=16: decode_failures 3
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 14
- SF-replay-order: replay-ordering=heard: misdecodes 21
- SF-hops-spread: hops-apart=3: decode_failures 11
- SF-hops-spread: hops-apart=4: decode_failures 20
- SF-hops-spread: hops-apart=5: decode_failures 19
- SF-place-spread: place=spread: decode_failures 34
- SF-place-spread: place=random-clients: decode_failures 34
- SF-servers-spread: servers=8: misdecodes 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 13
- SF-catchup: catch-up-hours=: misdecodes 32
- SF-catchup: catch-up-hours=02-06: decode_failures 5
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 5
- SF-catchup: faster: 4.79 s per simulated hour against 10.1 over 4 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- TH-congestion: no-congestion-scaling=True: queue drops 11.5% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 83
- RF-eu-presets: preset=SHORT_FAST: decode_failures 14
- RF-preset: preset=SHORT_FAST: decode_failures 14
- RF-preset: preset=LONG_MODERATE: decode_failures 3
- BL-control: protocol=sr: decode_failures 11
- MS-topology: topology=clustered: misdecodes 1
- TH-congestion-input: faster: 9.11 s per simulated hour against 18.5 over 4 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-hopscale: nodes=120: decode_failures 68
- MS-hopscale: nodes=500: decode_failures 55
- DB-hotstore: max-num-nodes=10: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 3
- FW-mixed: legacy-fraction=0.75: misdecodes 1
- MS-oversubscribed: nodes=120: decode_failures 34
- MS-oversubscribed: nodes=500: decode_failures 76
- DB-platform: platform-mix=constrained: decode_failures 1
- MS-siting: siting-mix=backbone: misdecodes 1
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 12.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 111
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 20.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 85
- DB-warm: warm-num-nodes=0: queue drops 12.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 111
- DB-warm: warm-num-nodes=25: queue drops 12.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 111
- DB-warm: warm-num-nodes=100: queue drops 12.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 111
- DB-warm: warm-num-nodes=2000: queue drops 12.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 111
- AD-amplifiers: amplifier-mix=sprinkled: misdecodes 1
- AD-amplify-worst: amplify-worst=0.1: decode_failures 3
- AD-badrouters: role-placement=inverse: decode_failures 5
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 4
- LD-chatty: broadcast-interval-s=300: decode_failures 13
- RF-noise: noise-profile=transient: misdecodes 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- AD-siting: siting-mix=local-typical: decode_failures 13
- AD-siting: slower: 2.72 s per simulated hour against 1.3 over 4 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 8
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 1
- MS-stretch: stretch=1.25: decode_failures 40
- MS-stretch: stretch=1.5: decode_failures 8
- MS-stretch: stretch=2.0: decode_failures 1
- AD-worst: role-placement=inverse: decode_failures 3
- AD-worst: faster: 4.84 s per simulated hour against 10.7 over 4 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

</details>

Blocks that produced no JSON (their job failed, timed out, or was cancelled): `RF-preset-turbo`

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `MS-size` | 8.61 | 3.4 | 2.53x | 4 |
| `AD-siting` | 2.72 | 1.3 | 2.09x | 4 |
| `BL-control` | 3.79 | 1.93 | 1.96x | 4 |
| `RF-txpower` | 3.2 | 1.7 | 1.89x | 4 |
| `SF-place-flat` | 5.02 | 2.97 | 1.69x | 4 |
| `RF-bw500` | 3.37 | 2.04 | 1.65x | 4 |
| `SF-place-spread` | 4.85 | 2.96 | 1.64x | 4 |
| `AD-amplify-worst` | 2.59 | 1.67 | 1.55x | 4 |
| `MS-oversubscribed` | 30 | 19.8 | 1.52x | 4 |
| `PR-dmmode-cr` | 1.75 | 2.83 | 0.62x | 4 |
| `LD-chatty-hops` | 2.39 | 4.21 | 0.57x | 4 |
| `DB-hotstore-stress` | 15.7 | 28.9 | 0.54x | 4 |
| `TH-congestion-input` | 9.11 | 18.5 | 0.49x | 4 |
| `SF-catchup` | 4.79 | 10.1 | 0.47x | 4 |
| `AD-worst` | 4.84 | 10.7 | 0.45x | 4 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.936 | 0.936 | 0.742 → 0.805 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.915 | 0.915 | 0.738 → 0.760 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.135 → 0.960 | 0.825 | 0.135 → 0.960 | 5x sr_airtime | up | 4 |
| `AD-siting` | siting-mix | **held** | 0.151 → 0.928 | 0.777 | 0.113 → 0.692 | 6.4x advert_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.104 → 0.861 | 0.756 | 0.095 → 0.708 | 1.4e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.260 → 0.915 | 0.655 | 0.106 → 0.760 | 3.8x advert_bytes | down | 4 |
| `MS-stretch` | stretch | **text** | 0.139 → 0.760 | 0.621 | 0.139 → 0.760 | 3.4x sr_airtime | down | 4 |
| `MS-density` | nodes | **text** | 0.378 → 0.959 | 0.581 | 0.378 → 0.959 | 8.9x sr_airtime | up | 5 |
| `MS-hopscale` | nodes | **held** | 0.394 → 0.915 | 0.521 | 0.312 → 0.760 | 8.9x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.456 → 0.956 | 0.500 | 0.456 → 0.956 | 2.6x sr_airtime | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.269 → 0.760 | 0.491 | 0.269 → 0.760 | 2.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.269 → 0.760 | 0.491 | 0.269 → 0.760 | 3.2x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.400 → 0.860 | 0.461 | 0.316 → 0.756 | 4.6x bytes_on_air | down | 3 |
| `RF-bw500` | preset | **text** | 0.200 → 0.632 | 0.432 | 0.200 → 0.632 | 1.9x sr_bytes | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.502 → 0.829 | 0.326 | 0.502 → 0.829 | 9.4x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.334 → 0.658 | 0.324 | 0.334 → 0.658 | 2x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.481 → 0.791 | 0.310 | 0.481 → 0.791 | 7.5x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.463 → 0.760 | 0.297 | 0.463 → 0.760 | 2.6x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.470 → 0.760 | 0.290 | 0.470 → 0.760 | 2.3x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.409 → 0.660 | 0.251 | 0.308 → 0.506 | 5.1x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.574 → 0.820 | 0.245 | 0.574 → 0.820 | 1.4x bytes_on_air | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.574 → 0.808 | 0.234 | 0.574 → 0.808 | 1.3x bytes_on_air | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.760 → 0.966 | 0.206 | 0.760 → 0.966 | 1.3x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.762 → 0.959 | 0.197 | 0.762 → 0.959 | 4.8x sr_airtime | down | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.746 → 0.936 | 0.191 | 0.749 → 0.805 | 2.9x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.574 → 0.760 | 0.186 | 0.574 → 0.760 | 1.3x advert_bytes | up | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.760 → 0.930 | 0.170 | 0.760 → 0.930 | 2x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.692 → 0.862 | 0.169 | 0.692 → 0.862 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.692 → 0.862 | 0.169 | 0.692 → 0.862 | 2.5x bytes_on_air | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.749 → 0.915 | 0.166 | 0.598 → 0.760 | 1.4x sr_airtime | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.604 → 0.760 | 0.156 | 0.604 → 0.760 | 1.3x sr_airtime | down | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.791 → 0.936 | 0.145 | 0.749 → 0.805 | 2.9x sr_bytes | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.627 → 0.760 | 0.133 | 0.627 → 0.760 | 1.5x sr_bytes | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.760 → 0.891 | 0.130 | 0.760 → 0.891 | 1.4x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.701 → 0.830 | 0.128 | 0.701 → 0.830 | 5.6x sr_airtime | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.645 → 0.773 | 0.128 | 0.645 → 0.773 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.649 → 0.773 | 0.124 | 0.649 → 0.773 | 2.2x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.792 → 0.915 | 0.123 | 0.746 → 0.799 | 5.8x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.792 → 0.915 | 0.123 | 0.746 → 0.799 | 5.8x sr_bytes | up | 6 |
| `MS-size` | nodes | **text** | 0.714 → 0.808 | 0.094 | 0.714 → 0.808 | 7.5x sr_bytes | down | 5 |
| `AD-badrouters` | role-placement | **text** | 0.611 → 0.692 | 0.081 | 0.611 → 0.692 | 1.2x sr_bytes | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.673 → 0.746 | 0.073 | 0.673 → 0.746 | 1.3x sr_airtime | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.750 → 0.822 | 0.072 | 0.750 → 0.822 | 2x bytes_on_air | up | 4 |
| `MS-roles` | role-mix | **text** | 0.692 → 0.763 | 0.071 | 0.692 → 0.763 | 1.4x sr_bytes | down | 2 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.915 → 0.985 | 0.070 | 0.757 → 0.817 | 2.1x bytes_on_air | up | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.735 → 0.798 | 0.063 | 0.735 → 0.798 | 1.4x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.857 → 0.915 | 0.058 | 0.749 → 0.760 | 22x sr_airtime | down | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.715 → 0.772 | 0.057 | 0.715 → 0.772 | 1.3x sr_bytes | down | 2 |
| `FW-firmware` | profile | **text** | 0.760 → 0.815 | 0.055 | 0.760 → 0.815 | 3.4x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.863 → 0.915 | 0.052 | 0.729 → 0.760 | 18x sr_bytes | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.708 → 0.760 | 0.052 | 0.708 → 0.760 | 1.4x sr_airtime | down | 4 |
| `FW-versions` | profile | **text** | 0.760 → 0.812 | 0.052 | 0.760 → 0.812 | 3.4x bytes_on_air | down | 5 |
| `TH-congestion-input` | congestion-input | **held** | 0.641 → 0.687 | 0.045 | 0.500 → 0.536 | 1.5x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **held** | 0.915 → 0.959 | 0.044 | 0.760 → 0.803 | 3.2x bytes_on_air | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.876 → 0.915 | 0.039 | 0.750 → 0.760 | 1.1x sr_airtime | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.892 → 0.924 | 0.032 | 0.748 → 0.758 | 1.2x sr_bytes | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.889 → 0.919 | 0.030 | 0.758 → 0.766 | 1.9x advert_bytes | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.898 → 0.927 | 0.029 | 0.754 → 0.763 | 6.9x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.898 → 0.927 | 0.029 | 0.754 → 0.763 | 6.9x sr_bytes | up | 4 |
| `AD-worst` | role-placement | **text** | 0.819 → 0.847 | 0.028 | 0.819 → 0.847 | 1.6x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **held** | 0.915 → 0.941 | 0.025 | 0.760 → 0.785 | 1.4x sr_bytes | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.697 → 0.722 | 0.024 | 0.697 → 0.722 | 1.3x sr_airtime | up | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.760 → 0.784 | 0.024 | 0.760 → 0.784 | 2.5x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.732 → 0.755 | 0.023 | 0.732 → 0.755 | 13x sr_bytes | up | 3 |
| `SF-window-size` | window-size | **text** | 0.749 → 0.765 | 0.016 | 0.749 → 0.765 | 6.3x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.911 → 0.925 | 0.014 | 0.757 → 0.768 | 3.2x advert_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.903 → 0.915 | 0.012 | 0.751 → 0.760 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.903 → 0.915 | 0.012 | 0.751 → 0.760 | 5.3x advert_bytes | up | 5 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.711 → 0.722 | 0.011 | 0.711 → 0.722 | 1.1x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **held** | 0.904 → 0.915 | 0.011 | 0.753 → 0.760 | 5.7x advert_bytes | = | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.755 → 0.765 | 0.010 | 0.755 → 0.765 | 3.3x advert_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.751 → 0.760 | 0.009 | 0.751 → 0.760 | 2.7x sr_airtime | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.751 → 0.760 | 0.009 | 0.751 → 0.760 | 1.1x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.912 → 0.920 | 0.007 | 0.759 → 0.765 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.912 → 0.920 | 0.007 | 0.759 → 0.765 | 1.1x sr_airtime | up | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.908 → 0.913 | 0.006 | 0.752 → 0.755 | 5.4x advert_bytes | down | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.915 → 0.920 | 0.005 | 0.760 → 0.764 | 1.1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.954 → 0.959 | 0.005 | 0.954 → 0.959 | 1.2x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.760 → 0.764 | 0.004 | 0.760 → 0.764 | 1.2x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.784 → 0.787 | 0.003 | 0.784 → 0.787 | 1.1x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.711 → 0.714 | 0.003 | 0.711 → 0.714 | 1.1x sr_bytes | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.873 → 0.874 | 0.001 | 0.748 → 0.749 | 2.8x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.959 → 0.959 | 0.001 | 0.959 → 0.959 | 1x bytes_on_air | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.959 → 0.959 | 0.001 | 0.959 → 0.959 | 1x sr_bytes | up | 2 |

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
| bucket | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| interval | 0.729 | - | - | 0.882 | 0.889 | 0.349 | 1.57x | 38.3/40.5% | 8.5% | 3 |
| aimd | 0.743 | - | - | 0.863 | 0.914 | 0.370 | 1.20x | 26.4/29.2% | 5.3% | 3 |
| bucket+interval | 0.732 | - | - | 0.888 | 0.890 | 0.370 | 1.61x | 39.1/41.2% | 8.7% | 3 |

> trigger=interval: misdecodes 26

> trigger=aimd: misdecodes 1

> trigger=bucket+interval: misdecodes 32

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.759 | - | - | 0.912 | 0.913 | 0.379 | 1.20x | 26.6/29.3% | 5.3% | 3 |
| 30 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 120 | 0.760 | - | - | 0.916 | 0.918 | 0.381 | 1.21x | 26.6/29.4% | 5.3% | 3 |
| 600 | 0.765 | - | - | 0.920 | 0.921 | 0.366 | 1.21x | 26.5/29.3% | 5.3% | 3 |

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| enum | 0.753 | - | - | 0.904 | 0.906 | 0.380 | 1.21x | 26.9/29.5% | 5.5% | 3 |
| hybrid | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.753 | - | - | 0.909 | 0.915 | 0.359 | 1.20x | 26.6/29.4% | 5.4% | 3 |
| 8 | 0.757 | - | - | 0.908 | 0.911 | 0.371 | 1.20x | 26.5/29.2% | 5.4% | 3 |
| 16 | 0.751 | - | - | 0.903 | 0.904 | 0.364 | 1.19x | 26.1/28.9% | 5.2% | 3 |
| 32 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 50 | 0.760 | - | - | 0.914 | 0.916 | 0.374 | 1.20x | 26.4/29.2% | 5.3% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 55

> capacity=16: decode_failures 3

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| True | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 0.768 | - | - | 0.923 | 0.925 | 0.383 | 1.19x | 26.2/28.9% | 5.2% | 3 |
| 24 | 0.757 | - | - | 0.911 | 0.913 | 0.362 | 1.21x | 26.5/29.2% | 5.3% | 3 |
| 32 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 64 | 0.767 | - | - | 0.925 | 0.925 | 0.389 | 1.23x | 26.9/29.7% | 5.4% | 3 |

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.1 | 0.661 | - | - | 0.879 | 0.881 | 0.300 | 1.15x | 25.7/28.4% | 4.9% | 3 |
| 0.2 | 0.564 | - | - | 0.828 | 0.835 | 0.240 | 1.08x | 24.4/27.0% | 4.5% | 3 |
| 0.3 | 0.470 | - | - | 0.737 | 0.783 | 0.181 | 0.98x | 22.4/25.0% | 4.0% | 3 |

> burst-loss=0.2: decode_failures 3

> burst-loss=0.3: decode_failures 20

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.692 | - | - | 0.928 | 0.929 | 0.122 | 1.05x | 24.0/26.8% | 5.1% | 3 |
| all-routers | 0.862 | - | - | 0.967 | 0.969 | 0.547 | 2.63x | 48.5/51.8% | 5.4% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.574 | - | - | 0.748 | 0.748 | 0.187 | 0.94x | 21.4/24.1% | 4.5% | 3 |
| 7 | 0.808 | - | - | 0.908 | 0.908 | 0.470 | 1.25x | 26.3/29.1% | 5.2% | 3 |
| 15 | 0.820 | - | - | 0.904 | 0.904 | 0.558 | 1.27x | 26.4/29.2% | 5.2% | 3 |
| 32 | 0.819 | - | - | 0.908 | 0.908 | 0.573 | 1.29x | 26.6/29.5% | 5.3% | 3 |

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.1 | 0.724 | - | - | 0.903 | 0.904 | 0.335 | 1.26x | 27.4/30.2% | 5.2% | 3 |
| 0.2 | 0.681 | - | - | 0.889 | 0.893 | 0.303 | 1.30x | 28.1/31.3% | 5.1% | 3 |
| 0.3 | 0.627 | - | - | 0.853 | 0.858 | 0.260 | 1.34x | 29.4/32.9% | 5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.1 | 0.640 | - | - | 0.848 | 0.869 | 0.303 | 1.14x | 25.2/27.9% | 5.0% | 3 |
| 0.2 | 0.562 | - | - | 0.824 | 0.861 | 0.225 | 1.09x | 24.3/26.7% | 4.5% | 3 |
| 0.3 | 0.463 | - | - | 0.721 | 0.789 | 0.193 | 1.02x | 23.7/26.0% | 4.7% | 3 |

> burst-loss=0.1: decode_failures 30

> burst-loss=0.2: decode_failures 46

> burst-loss=0.3: decode_failures 33

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 22 | 0.337 | - | - | 0.547 | 0.581 | 0.000 | 1.30x | 20.9/26.3% | 5.4% | 3 |
| 17 | 0.174 | - | - | 0.399 | 0.403 | 0.000 | 1.10x | 15.2/22.8% | 5.2% | 3 |
| 14 | 0.106 | - | - | 0.260 | 0.260 | 0.000 | 0.86x | 10.1/15.0% | 3.7% | 3 |

> tx-power=22: decode_failures 22

> tx-power=14: decode_failures 4

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.749 | - | - | 0.874 | 0.874 | 0.362 | 1.20x | 26.2/29.0% | 5.3% | 3 |
| 6 | 0.748 | - | - | 0.873 | 0.873 | 0.377 | 1.24x | 27.4/30.2% | 5.6% | 6 |

> servers=6: misdecodes 2

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.749 | - | - | 0.874 | 0.874 | 0.362 | 1.20x | 26.2/29.0% | 5.3% | 3 |
| 2 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 3 | 0.805 | - | - | 0.936 | 0.951 | 0.379 | 1.22x | 27.0/29.7% | 5.4% | 3 |
| 4 | 0.768 | - | - | 0.791 | 0.948 | 0.377 | 1.21x | 26.0/28.9% | 5.2% | 3 |

> hops-apart=3: decode_failures 11

> hops-apart=4: decode_failures 20

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.799 | - | - | 0.864 | 0.938 | 0.391 | 1.23x | 27.0/29.6% | 5.4% | 3 |
| routers | 0.749 | - | - | 0.874 | 0.874 | 0.362 | 1.20x | 26.2/29.0% | 5.3% | 3 |
| alternate-routers | 0.746 | - | - | 0.876 | 0.877 | 0.384 | 1.20x | 26.3/29.0% | 5.4% | 3 |
| beside-router | 0.750 | - | - | 0.875 | 0.875 | 0.375 | 1.20x | 26.3/29.2% | 5.2% | 3 |
| random-clients | 0.777 | - | - | 0.792 | 0.948 | 0.417 | 1.20x | 26.2/29.2% | 5.3% | 3 |
| hops-apart | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

> place=spread: decode_failures 34

> place=random-clients: decode_failures 34

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.754 | - | - | 0.898 | 0.902 | 0.392 | 1.20x | 26.1/29.0% | 5.2% | 2 |
| 3 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 5 | 0.763 | - | - | 0.926 | 0.927 | 0.356 | 1.23x | 27.4/30.0% | 5.5% | 5 |
| 8 | 0.762 | - | - | 0.927 | 0.927 | 0.377 | 1.26x | 28.0/30.6% | 5.6% | 8 |

> servers=8: misdecodes 1

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 0.761 | - | - | 0.911 | 0.913 | 0.371 | 1.20x | 26.5/29.1% | 5.3% | 3 |
| local | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| time | 0.755 | - | - | 0.908 | 0.909 | 0.372 | 1.22x | 27.0/29.8% | 5.5% | 3 |
| window | 0.765 | - | - | 0.916 | 0.918 | 0.379 | 1.19x | 26.3/29.0% | 5.3% | 3 |

> bucket-mode=global: misdecodes 42

> bucket-mode=time: misdecodes 44

> bucket-mode=window: misdecodes 20

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 0.755 | - | - | 0.913 | 0.916 | 0.378 | 1.31x | 29.4/32.1% | 6.1% | 3 |
| 1800 | 0.755 | - | - | 0.908 | 0.909 | 0.372 | 1.22x | 27.0/29.8% | 5.5% | 3 |
| 3600 | 0.752 | - | - | 0.912 | 0.914 | 0.373 | 1.19x | 26.3/28.9% | 5.3% | 3 |

> time-bucket-s=600: misdecodes 106

> time-bucket-s=1800: misdecodes 44

> time-bucket-s=3600: misdecodes 11

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.758 | - | - | 0.889 | 0.907 | 0.369 | 1.18x | 25.7/28.5% | 5.1% | 3 |
| 16 | 0.766 | - | - | 0.919 | 0.923 | 0.378 | 1.19x | 26.1/28.9% | 5.2% | 3 |
| 32 | 0.765 | - | - | 0.916 | 0.918 | 0.379 | 1.19x | 26.3/29.0% | 5.3% | 3 |

> capacity=8: misdecodes 18

> capacity=8: decode_failures 21

> capacity=16: misdecodes 24

> capacity=16: decode_failures 1

> capacity=32: misdecodes 20

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.749 | - | - | 0.905 | 0.905 | 0.366 | 1.29x | 28.7/31.4% | 5.7% | 3 |
| 16 | 0.758 | - | - | 0.909 | 0.909 | 0.367 | 1.22x | 26.8/29.6% | 5.4% | 3 |
| 32 | 0.765 | - | - | 0.916 | 0.918 | 0.379 | 1.19x | 26.3/29.0% | 5.3% | 3 |

> window-size=8: misdecodes 149

> window-size=16: misdecodes 72

> window-size=32: misdecodes 20

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.378 | - | - | 0.489 | 0.492 | 0.083 | 0.84x | 22.7/25.4% | 5.1% | 3 |
| 60 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 90 | 0.915 | - | - | 0.995 | 0.997 | 0.592 | 1.54x | 28.8/34.6% | 5.0% | 3 |
| 120 | 0.959 | - | - | 0.999 | 0.999 | 0.809 | 1.95x | 34.3/41.3% | 5.0% | 3 |
| 150 | 0.944 | - | - | 0.999 | 0.999 | 0.828 | 2.43x | 43.2/50.0% | 5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.574 | - | - | 0.748 | 0.748 | 0.187 | 0.94x | 21.4/24.1% | 4.5% | 3 |
| 5 | 0.737 | - | - | 0.871 | 0.873 | 0.324 | 1.15x | 25.0/27.8% | 5.0% | 3 |
| 7 | 0.808 | - | - | 0.908 | 0.908 | 0.470 | 1.25x | 26.3/29.1% | 5.2% | 3 |

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.808 | - | - | 0.943 | 0.946 | 0.488 | 1.34x | 35.7/37.8% | 7.5% | 3 |
| 60 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 90 | 0.772 | - | - | 0.940 | 0.942 | 0.470 | 1.57x | 23.7/26.7% | 4.7% | 3 |
| 120 | 0.755 | - | - | 0.865 | 0.935 | 0.409 | 2.19x | 26.0/32.9% | 5.2% | 3 |
| 150 | 0.714 | - | - | 0.908 | 0.915 | 0.339 | 2.64x | 25.3/30.0% | 5.7% | 3 |

> nodes=120: decode_failures 68

> nodes=150: decode_failures 9

> slower: 8.61 s per simulated hour against 3.4 over 4 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.574 | - | - | 0.748 | 0.748 | 0.187 | 0.94x | 21.4/24.1% | 4.5% | 3 |
| True | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| dm | 0.751 | - | - | 0.909 | 0.909 | 0.368 | 1.18x | 26.1/28.8% | 5.4% | 3 |

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| broadcast | 0.784 | - | - | 0.904 | 0.905 | 0.385 | 1.25x | 27.7/30.4% | 5.5% | 3 |

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.753 | - | - | 0.909 | 0.915 | 0.359 | 1.20x | 26.6/29.4% | 5.4% | 3 |
| 8 | 0.757 | - | - | 0.908 | 0.911 | 0.371 | 1.20x | 26.5/29.2% | 5.4% | 3 |
| 16 | 0.751 | - | - | 0.903 | 0.904 | 0.364 | 1.19x | 26.1/28.9% | 5.2% | 3 |
| 32 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 50 | 0.760 | - | - | 0.914 | 0.916 | 0.374 | 1.20x | 26.4/29.2% | 5.3% | 3 |

> capacity=4: decode_failures 78

> capacity=8: decode_failures 55

> capacity=16: decode_failures 3

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.784 | - | - | 0.904 | 0.905 | 0.385 | 1.25x | 27.7/30.4% | 5.5% | 3 |
| heard | 0.787 | - | - | 0.904 | 0.906 | 0.389 | 1.24x | 27.3/29.9% | 5.4% | 3 |

> replay-ordering=heard: misdecodes 14

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.759 | - | - | 0.912 | 0.913 | 0.379 | 1.20x | 26.6/29.3% | 5.3% | 3 |
| 30 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 120 | 0.760 | - | - | 0.916 | 0.918 | 0.381 | 1.21x | 26.6/29.4% | 5.3% | 3 |
| 600 | 0.765 | - | - | 0.920 | 0.921 | 0.366 | 1.21x | 26.5/29.3% | 5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| heard | 0.764 | - | - | 0.913 | 0.916 | 0.380 | 1.20x | 26.3/29.1% | 5.3% | 3 |

> replay-ordering=heard: misdecodes 21

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.749 | - | - | 0.874 | 0.874 | 0.362 | 1.20x | 26.2/29.0% | 5.3% | 3 |
| 2 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 3 | 0.805 | - | - | 0.936 | 0.951 | 0.379 | 1.22x | 27.0/29.7% | 5.4% | 3 |
| 4 | 0.768 | - | - | 0.791 | 0.948 | 0.377 | 1.21x | 26.0/28.9% | 5.2% | 3 |
| 5 | 0.791 | - | - | 0.746 | 0.982 | 0.375 | 1.20x | 26.6/29.2% | 5.4% | 3 |

> hops-apart=3: decode_failures 11

> hops-apart=4: decode_failures 20

> hops-apart=5: decode_failures 19

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.799 | - | - | 0.864 | 0.938 | 0.391 | 1.23x | 27.0/29.6% | 5.4% | 3 |
| routers | 0.749 | - | - | 0.874 | 0.874 | 0.362 | 1.20x | 26.2/29.0% | 5.3% | 3 |
| alternate-routers | 0.746 | - | - | 0.876 | 0.877 | 0.384 | 1.20x | 26.3/29.0% | 5.4% | 3 |
| beside-router | 0.750 | - | - | 0.875 | 0.875 | 0.375 | 1.20x | 26.3/29.2% | 5.2% | 3 |
| random-clients | 0.777 | - | - | 0.792 | 0.948 | 0.417 | 1.20x | 26.2/29.2% | 5.3% | 3 |
| hops-apart | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

> place=spread: decode_failures 34

> place=random-clients: decode_failures 34

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.754 | - | - | 0.898 | 0.902 | 0.392 | 1.20x | 26.1/29.0% | 5.2% | 2 |
| 3 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 5 | 0.763 | - | - | 0.926 | 0.927 | 0.356 | 1.23x | 27.4/30.0% | 5.5% | 5 |
| 8 | 0.762 | - | - | 0.927 | 0.927 | 0.377 | 1.26x | 28.0/30.6% | 5.6% | 8 |

> servers=8: misdecodes 1

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 0.200 | - | - | 0.444 | 0.445 | 0.000 | 0.05x | 0.8/1.2% | 0.3% | 3 |
| MEDIUM_TURBO | 0.372 | - | - | 0.625 | 0.635 | 0.000 | 0.25x | 5.1/6.6% | 1.2% | 3 |
| LONG_TURBO | 0.632 | - | - | 0.821 | 0.827 | 0.253 | 1.10x | 20.7/25.7% | 4.9% | 3 |

> preset=MEDIUM_TURBO: decode_failures 13

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 0.732 | - | - | 0.888 | 0.890 | 0.370 | 1.61x | 39.1/41.2% | 8.7% | 3 |
| 02-06 | 0.755 | - | - | 0.895 | 0.918 | 0.362 | 1.21x | 26.8/29.4% | 5.3% | 3 |
| 00-08 | 0.750 | - | - | 0.890 | 0.919 | 0.371 | 1.26x | 28.3/31.1% | 5.8% | 3 |

> catch-up-hours=: misdecodes 32

> catch-up-hours=02-06: decode_failures 5

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 5

> faster: 4.79 s per simulated hour against 10.1 over 4 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.959 | - | - | 0.999 | 0.999 | 0.809 | 1.95x | 34.3/41.3% | 5.0% | 3 |
| True | 0.762 | - | - | 0.902 | 0.931 | 0.613 | 5.50x | 72.5/78.9% | 12.4% | 3 |

> no-congestion-scaling=True: queue drops 11.5% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 83

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 0.785 | - | - | 0.941 | 0.942 | 0.375 | 1.12x | 24.8/27.4% | 5.0% | 3 |
| sinusoid | 0.780 | - | - | 0.929 | 0.929 | 0.410 | 1.08x | 23.6/26.1% | 4.7% | 3 |
| commuter | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.269 | - | - | 0.431 | 0.554 | 0.000 | 0.12x | 2.0/3.7% | 0.7% | 3 |
| LONG_FAST | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| LITE_FAST | 0.644 | - | - | 0.855 | 0.861 | 0.264 | 0.91x | 20.8/24.2% | 3.9% | 3 |
| NARROW_SLOW | 0.695 | - | - | 0.869 | 0.870 | 0.325 | 1.22x | 29.2/33.1% | 5.0% | 3 |

> preset=SHORT_FAST: decode_failures 14

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.269 | - | - | 0.431 | 0.554 | 0.000 | 0.12x | 2.0/3.7% | 0.7% | 3 |
| LONG_FAST | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| LONG_MODERATE | 0.728 | - | - | 0.868 | 0.875 | 0.502 | 3.24x | 70.8/73.7% | 11.3% | 3 |

> preset=SHORT_FAST: decode_failures 14

> preset=LONG_MODERATE: decode_failures 3

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.742 | - | - | 0 | 0.000 | 0.369 | 1.17x | 25.7/28.4% | 5.1% | 3 |
| sr | 0.805 | - | - | 0.936 | 0.951 | 0.379 | 1.22x | 27.0/29.7% | 5.4% | 3 |

> protocol=sr: decode_failures 11

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| random | 0.750 | - | - | 0.876 | 0.878 | 0.297 | 1.18x | 25.3/28.1% | 5.0% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 0.701 | - | - | 0.871 | 0.871 | 0.333 | 1.82x | 39.9/43.8% | 7.9% | 3 |
| 3600 | 0.791 | - | - | 0.944 | 0.945 | 0.383 | 0.81x | 17.5/19.4% | 3.5% | 3 |
| 10800 | 0.817 | - | - | 0.961 | 0.962 | 0.407 | 0.53x | 11.5/12.7% | 2.4% | 3 |
| 43200 | 0.830 | - | - | 0.974 | 0.975 | 0.423 | 0.37x | 8.3/9.2% | 1.7% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.742 | - | - | 0 | 0.000 | 0.369 | 1.17x | 25.7/28.4% | 5.1% | 3 |
| chain | 0.738 | - | - | 0.868 | 0.905 | 0.358 | 1.35x | 30.2/33.1% | 6.0% | 3 |
| sr | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| clustered | 0.953 | - | - | 0.996 | 0.996 | 0.715 | 1.19x | 35.1/36.4% | 5.6% | 3 |
| corridor | 0.456 | - | - | 0.627 | 0.634 | 0.227 | 1.69x | 36.2/41.3% | 7.4% | 3 |
| hub | 0.956 | - | - | 0.998 | 0.998 | 0.833 | 1.16x | 35.0/36.9% | 5.5% | 3 |

> topology=clustered: misdecodes 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.959 | - | - | 0.999 | 0.999 | 0.809 | 1.95x | 34.3/41.3% | 5.0% | 3 |
| True | 0.954 | - | - | 1.000 | 1.000 | 0.796 | 2.33x | 40.7/47.3% | 5.8% | 3 |

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 0.500 | - | - | 0.641 | 0.643 | 0.228 | 4.42x | 28.8/40.4% | 5.0% | 3 |
| truesize | 0.536 | - | - | 0.687 | 0.689 | 0.233 | 3.24x | 22.6/32.2% | 4.1% | 3 |

> faster: 9.11 s per simulated hour against 18.5 over 4 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 0.959 | - | - | 1.000 | 1.000 | 0.793 | 1.91x | 34.2/40.6% | 4.9% | 3 |
| adaptive | 0.959 | - | - | 0.999 | 0.999 | 0.809 | 1.95x | 34.3/41.3% | 5.0% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.722 | - | - | 0.887 | 0.889 | 0.369 | 1.39x | 31.3/34.4% | 6.2% | 3 |
| True | 0.711 | - | - | 0.885 | 0.890 | 0.361 | 1.41x | 31.7/34.7% | 6.4% | 3 |

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 0.697 | - | - | 0.876 | 0.879 | 0.342 | 1.51x | 33.8/37.0% | 6.7% | 3 |
| directed-with-late-flood | 0.722 | - | - | 0.887 | 0.889 | 0.369 | 1.39x | 31.3/34.4% | 6.2% | 3 |
| m4-early-flood | 0.720 | - | - | 0.878 | 0.880 | 0.364 | 1.40x | 31.5/34.6% | 6.2% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 0.711 | - | - | 0.885 | 0.890 | 0.361 | 1.41x | 31.7/34.7% | 6.4% | 3 |
| m4-early-flood | 0.714 | - | - | 0.887 | 0.891 | 0.352 | 1.41x | 31.6/34.7% | 6.3% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.751 | - | - | 0.897 | 0.899 | 0.382 | 1.35x | 34.3/36.8% | 5.4% | 3 |
| True | 0.760 | - | - | 0.893 | 0.895 | 0.375 | 1.36x | 34.2/36.6% | 5.3% | 3 |

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 0.815 | - | - | 0.948 | 0.952 | 0.553 | 0.64x | 11.0/13.8% | 1.8% | 3 |
| 2.8 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 120 | 0.755 | - | - | 0.865 | 0.935 | 0.409 | 2.19x | 26.0/32.9% | 5.2% | 3 |
| 250 | 0.505 | - | - | 0.656 | 0.656 | 0.223 | 4.69x | 30.5/42.7% | 5.3% | 3 |
| 500 | 0.312 | - | - | 0.394 | 0.398 | 0.000 | 9.91x | 35.1/50.1% | 5.7% | 3 |

> nodes=120: decode_failures 68

> nodes=500: decode_failures 55

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.645 | - | - | 0.784 | 0.786 | 0.345 | 2.68x | 64.1/68.1% | 8.8% | 3 |
| 100 | 0.773 | - | - | 0.893 | 0.894 | 0.409 | 1.48x | 38.2/40.8% | 5.1% | 3 |
| 120 | 0.773 | - | - | 0.893 | 0.894 | 0.409 | 1.48x | 38.2/40.8% | 5.1% | 3 |
| 250 | 0.773 | - | - | 0.893 | 0.894 | 0.409 | 1.48x | 38.2/40.8% | 5.1% | 3 |

> max-num-nodes=10: decode_failures 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.308 | - | - | 0.409 | 0.412 | 0.154 | 11.18x | 61.0/74.0% | 10.7% | 3 |
| 120 | 0.500 | - | - | 0.641 | 0.643 | 0.228 | 4.42x | 28.8/40.4% | 5.0% | 3 |
| 250 | 0.506 | - | - | 0.660 | 0.660 | 0.223 | 4.31x | 27.5/39.1% | 4.7% | 3 |

> max-num-nodes=10: decode_failures 3

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.25 | 0.750 | - | - | 0.938 | 0.941 | 0.300 | 1.05x | 25.0/27.0% | 4.5% | 3 |
| 0.5 | 0.822 | - | - | 0.981 | 0.987 | 0.537 | 0.91x | 16.7/19.5% | 3.8% | 3 |
| 0.75 | 0.767 | - | - | 0.936 | 0.939 | 0.322 | 0.81x | 15.2/16.8% | 2.4% | 3 |

> legacy-fraction=0.75: misdecodes 1

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.25 | 0.757 | - | - | 0.947 | 0.952 | 0.287 | 1.05x | 24.8/26.6% | 4.4% | 3 |
| 0.5 | 0.817 | - | - | 0.985 | 0.986 | 0.561 | 0.90x | 16.9/20.1% | 3.9% | 3 |
| 0.75 | 0.773 | - | - | 0.948 | 0.951 | 0.294 | 0.79x | 15.5/16.9% | 2.3% | 3 |

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 0.756 | - | - | 0.860 | 0.947 | 0.421 | 2.08x | 25.1/31.9% | 4.9% | 3 |
| 250 | 0.500 | - | - | 0.641 | 0.643 | 0.228 | 4.42x | 28.8/40.4% | 5.0% | 3 |
| 500 | 0.316 | - | - | 0.400 | 0.402 | 0.000 | 9.41x | 33.3/48.8% | 5.2% | 3 |

> nodes=120: decode_failures 34

> nodes=500: decode_failures 76

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.773 | - | - | 0.893 | 0.894 | 0.409 | 1.48x | 38.2/40.8% | 5.1% | 3 |
| baymesh-2026-08 | 0.773 | - | - | 0.893 | 0.894 | 0.409 | 1.48x | 38.2/40.8% | 5.1% | 3 |
| constrained | 0.649 | - | - | 0.788 | 0.790 | 0.343 | 2.69x | 64.1/68.1% | 8.8% | 3 |

> platform-mix=constrained: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| KNOWN_ONLY | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| CORE_PORTNUMS_ONLY | 0.749 | - | - | 0.857 | 0.919 | 0.365 | 1.18x | 25.7/28.5% | 5.1% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| True | 0.764 | - | - | 0.920 | 0.921 | 0.395 | 1.23x | 26.6/29.4% | 5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.959 | - | - | 0.999 | 0.999 | 0.809 | 1.95x | 34.3/41.3% | 5.0% | 3 |
| True | 0.959 | - | - | 0.998 | 0.999 | 0.799 | 2.00x | 34.8/42.0% | 5.0% | 3 |

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.763 | - | - | 0.931 | 0.932 | 0.253 | 1.18x | 26.2/28.9% | 5.2% | 3 |
| baymesh-2026-08 | 0.692 | - | - | 0.928 | 0.929 | 0.122 | 1.05x | 24.0/26.8% | 5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.772 | - | - | 0.923 | 0.927 | 0.271 | 1.21x | 26.3/29.1% | 5.2% | 3 |
| baymesh-2026-08 | 0.715 | - | - | 0.908 | 0.909 | 0.142 | 1.22x | 29.8/33.4% | 5.0% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.05 | 0.745 | - | - | 0.893 | 0.893 | 0.365 | 1.33x | 34.6/37.8% | 5.2% | 3 |
| 0.1 | 0.735 | - | - | 0.877 | 0.879 | 0.370 | 1.41x | 38.5/43.2% | 4.9% | 3 |
| 0.2 | 0.798 | - | - | 0.918 | 0.918 | 0.406 | 1.66x | 44.6/51.1% | 5.1% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| BALANCED | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| STRICT | 0.604 | - | - | 0.770 | 0.770 | 0.280 | 1.33x | 28.5/31.6% | 5.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 0.803 | - | - | 0.959 | 0.959 | 0.386 | 0.66x | 15.4/17.2% | 3.1% | 3 |
| signing=true | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| local-typical | 0.554 | - | - | 0.772 | 0.779 | 0.000 | 1.35x | 25.3/29.5% | 5.1% | 3 |
| event | 0.135 | - | - | 0.245 | 0.376 | 0.000 | 0.92x | 13.0/18.9% | 4.7% | 3 |
| backbone | 0.960 | - | - | 0.996 | 0.997 | 0.750 | 1.05x | 34.6/36.7% | 5.5% | 3 |

> siting-mix=backbone: misdecodes 1

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.758 | - | - | 0.924 | 0.926 | 0.395 | 1.11x | 24.8/27.2% | 4.9% | 3 |
| 1 | 0.748 | - | - | 0.892 | 0.897 | 0.387 | 1.11x | 24.5/27.1% | 4.8% | 3 |
| 2 | 0.748 | - | - | 0.892 | 0.897 | 0.387 | 1.11x | 24.5/27.1% | 4.8% | 3 |
| 4 | 0.748 | - | - | 0.892 | 0.897 | 0.387 | 1.11x | 24.5/27.1% | 4.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.25 | 0.759 | - | - | 0.911 | 0.912 | 0.378 | 1.23x | 27.4/30.1% | 5.4% | 3 |
| 1.0 | 0.751 | - | - | 0.908 | 0.910 | 0.360 | 1.36x | 30.2/33.2% | 6.0% | 3 |
| 4.0 | 0.708 | - | - | 0.876 | 0.876 | 0.351 | 1.65x | 37.4/41.4% | 7.4% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.746 | - | - | 0.867 | 0.919 | 0.598 | 5.58x | 72.9/79.1% | 12.6% | 3 |
| 1.0 | 0.673 | - | - | 0.819 | 0.875 | 0.528 | 6.17x | 75.7/80.6% | 13.9% | 3 |

> traceroute-per-hour=0.0: queue drops 12.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 111

> traceroute-per-hour=1.0: queue drops 20.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 85

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 0.804 | - | - | 0.941 | 0.943 | 0.550 | 0.65x | 12.2/15.6% | 2.1% | 3 |
| 2.5 | 0.812 | - | - | 0.950 | 0.952 | 0.554 | 0.67x | 12.5/15.7% | 2.1% | 3 |
| 2.6 | 0.811 | - | - | 0.950 | 0.959 | 0.532 | 0.64x | 12.2/15.7% | 2.1% | 3 |
| 2.7 | 0.803 | - | - | 0.927 | 0.931 | 0.514 | 0.66x | 14.9/17.9% | 2.8% | 3 |
| 2.8 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.746 | - | - | 0.867 | 0.919 | 0.598 | 5.58x | 72.9/79.1% | 12.6% | 3 |
| 25 | 0.746 | - | - | 0.867 | 0.919 | 0.598 | 5.58x | 72.9/79.1% | 12.6% | 3 |
| 100 | 0.746 | - | - | 0.867 | 0.919 | 0.598 | 5.58x | 72.9/79.1% | 12.6% | 3 |
| 2000 | 0.746 | - | - | 0.867 | 0.919 | 0.598 | 5.58x | 72.9/79.1% | 12.6% | 3 |

> warm-num-nodes=0: queue drops 12.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 111

> warm-num-nodes=25: queue drops 12.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 111

> warm-num-nodes=100: queue drops 12.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 111

> warm-num-nodes=2000: queue drops 12.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 111

### `AD-amplifiers` - amplifier-mix  `--scenario rolling`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| sprinkled | 0.909 | - | - | 0.963 | 0.964 | 0.726 | 1.09x | 25.6/27.9% | 5.0% | 3 |
| arms-race | 0.966 | - | - | 0.997 | 0.997 | 0.878 | 0.95x | 25.8/27.4% | 5.4% | 3 |

> amplifier-mix=sprinkled: misdecodes 1

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.1 | 0.863 | - | - | 0.890 | 0.895 | 0.619 | 1.10x | 26.0/28.9% | 5.4% | 3 |
| 0.3 | 0.930 | - | - | 0.993 | 0.997 | 0.811 | 1.10x | 26.3/31.1% | 5.0% | 3 |

> amplify-worst=0.1: decode_failures 3

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.692 | - | - | 0.928 | 0.929 | 0.122 | 1.05x | 24.0/26.8% | 5.1% | 3 |
| inverse | 0.611 | - | - | 0.904 | 0.912 | 0.101 | 0.95x | 19.4/21.5% | 3.4% | 3 |
| random | 0.690 | - | - | 0.899 | 0.905 | 0.248 | 1.09x | 21.4/24.1% | 4.8% | 3 |

> role-placement=inverse: decode_failures 5

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.791 | - | - | 0.944 | 0.945 | 0.383 | 0.81x | 17.5/19.4% | 3.5% | 3 |
| 900 | 0.701 | - | - | 0.871 | 0.871 | 0.333 | 1.82x | 39.9/43.8% | 7.9% | 3 |
| 300 | 0.481 | - | - | 0.675 | 0.703 | 0.249 | 3.98x | 73.2/78.0% | 15.2% | 3 |

> broadcast-interval-s=300: decode_failures 13

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.829 | - | - | 0.925 | 0.926 | 0.511 | 0.85x | 17.4/19.5% | 3.5% | 3 |
| 900 | 0.759 | - | - | 0.875 | 0.876 | 0.419 | 1.99x | 40.7/44.9% | 8.0% | 3 |
| 300 | 0.502 | - | - | 0.624 | 0.650 | 0.295 | 4.28x | 73.9/79.0% | 16.0% | 3 |

> broadcast-interval-s=300: decode_failures 4

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 0.25 | 0.821 | - | - | 0.942 | 0.943 | 0.517 | 1.01x | 26.6/28.9% | 5.0% | 3 |
| 1.0 | 0.891 | - | - | 0.971 | 0.972 | 0.697 | 0.87x | 29.8/31.4% | 5.1% | 3 |

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| temporal | 0.650 | - | - | 0.840 | 0.841 | 0.218 | 1.22x | 26.5/28.8% | 5.1% | 3 |
| transient | 0.751 | - | - | 0.908 | 0.909 | 0.363 | 1.20x | 26.3/29.0% | 5.3% | 3 |
| periodic | 0.598 | - | - | 0.749 | 0.757 | 0.271 | 1.11x | 24.0/26.6% | 4.5% | 3 |

> noise-profile=transient: misdecodes 1

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.692 | - | - | 0.928 | 0.929 | 0.122 | 1.05x | 24.0/26.8% | 5.1% | 3 |
| no-mute | 0.736 | - | - | 0.951 | 0.951 | 0.260 | 1.10x | 22.3/25.8% | 5.2% | 3 |
| all-routers | 0.862 | - | - | 0.967 | 0.969 | 0.547 | 2.63x | 48.5/51.8% | 5.4% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 0.708 | - | - | 0.861 | 0.861 | 0.349 | 1.17x | 25.7/28.4% | 5.0% | 3 |
| 10000 | 0.598 | - | - | 0.749 | 0.757 | 0.271 | 1.11x | 24.0/26.6% | 4.5% | 3 |
| 4000 | 0.360 | - | - | 0.458 | 0.513 | 0.137 | 0.98x | 21.1/23.6% | 3.5% | 3 |
| 2000 | 0.095 | - | - | 0.104 | 0.167 | 0.035 | 0.68x | 15.4/17.7% | 2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 2

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.692 | - | - | 0.928 | 0.929 | 0.122 | 1.05x | 24.0/26.8% | 5.1% | 3 |
| local-typical | 0.514 | - | - | 0.755 | 0.768 | 0.000 | 1.31x | 28.9/33.5% | 5.8% | 3 |
| basement-heavy | 0.113 | - | - | 0.151 | 0.234 | 0.000 | 0.62x | 8.9/13.2% | 3.2% | 3 |

> siting-mix=local-typical: decode_failures 13

> slower: 2.72 s per simulated hour against 1.3 over 4 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 0.760 | - | - | 0.915 | 0.917 | 0.369 | 1.20x | 26.4/29.1% | 5.3% | 3 |
| 1.25 | 0.526 | - | - | 0.708 | 0.744 | 0.208 | 1.35x | 26.3/31.4% | 5.5% | 3 |
| 1.5 | 0.334 | - | - | 0.526 | 0.600 | 0.000 | 1.30x | 18.6/23.6% | 4.8% | 3 |
| 2.0 | 0.139 | - | - | 0.320 | 0.352 | 0.000 | 1.03x | 12.5/15.6% | 3.9% | 3 |

> stretch=1.25: decode_failures 40

> stretch=1.5: decode_failures 8

> stretch=2.0: decode_failures 1

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.334 | - | - | 0.526 | 0.600 | 0.000 | 1.30x | 18.6/23.6% | 4.8% | 3 |
| 1.0 | 0.658 | - | - | 0.805 | 0.812 | 0.374 | 0.94x | 22.6/25.2% | 4.6% | 3 |

> duct-per-hour=0.0: decode_failures 8

> duct-per-hour=1.0: decode_failures 1

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.847 | - | - | 0.957 | 0.958 | 0.103 | 2.35x | 26.7/34.4% | 5.5% | 3 |
| inverse | 0.819 | - | - | 0.955 | 0.958 | 0.187 | 2.30x | 24.9/33.7% | 3.4% | 3 |

> role-placement=inverse: decode_failures 3

> faster: 4.84 s per simulated hour against 10.7 over 4 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

