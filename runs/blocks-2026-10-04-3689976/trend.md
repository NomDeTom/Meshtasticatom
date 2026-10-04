# Sweep blocks-2026-10-04-3689976

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 3689976 · seeds 3689976
- **blocks** 87 run
- **compute** 9.4 h of simulator time across every cell
- **generated** 2026-10-04T09:33:01+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>77 warnings</summary>

- AD-amplifiers: faster: 0.799 s per simulated hour against 1.62 over 44 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-siting: siting-mix=basement-heavy: decode_failures 5
- AD-worst: role-placement=degree: misdecodes 1
- BL-control: protocol=sr: decode_failures 26
- BL-control: slower: 4.76 s per simulated hour against 1.98 over 44 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 66
- DB-warm: warm-num-nodes=0: queue drops 14.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 121
- DB-warm: warm-num-nodes=25: queue drops 14.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 121
- DB-warm: warm-num-nodes=100: queue drops 14.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 121
- DB-warm: warm-num-nodes=2000: queue drops 14.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 121
- DG-burst: burst-loss=0.2: decode_failures 2
- DG-burst: burst-loss=0.3: decode_failures 36
- DG-outage: burst-loss=0.1: decode_failures 13
- DG-outage: burst-loss=0.2: decode_failures 39
- DG-outage: burst-loss=0.3: decode_failures 34
- LD-chatty: broadcast-interval-s=300: decode_failures 10
- LD-interval: faster: 0.615 s per simulated hour against 1.29 over 44 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 14.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 121
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 21.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 114
- MS-hopscale: nodes=250: decode_failures 1
- MS-hopscale: nodes=500: decode_failures 65
- MS-oversubscribed: nodes=500: decode_failures 33
- MS-router-late: router-late-fraction=0.2: misdecodes 1
- MS-siting: faster: 0.896 s per simulated hour against 1.93 over 43 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-size: nodes=150: decode_failures 76
- MS-stretch: stretch=1.25: decode_failures 2
- MS-stretch: stretch=1.5: decode_failures 18
- MS-topology: topology=corridor: decode_failures 4
- PR-crladder: faster: 1.36 s per simulated hour against 2.79 over 44 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-bw500: preset=SHORT_TURBO: decode_failures 12
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 12
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 5
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 18
- RF-stretch-duct: slower: 4.36 s per simulated hour against 1.83 over 44 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=17: decode_failures 3
- SF-bucket-mode: bucket-mode=global: misdecodes 47
- SF-bucket-mode: bucket-mode=time: misdecodes 40
- SF-bucket-mode: bucket-mode=window: misdecodes 35
- SF-bucket-time: time-bucket-s=600: misdecodes 159
- SF-bucket-time: time-bucket-s=1800: misdecodes 40
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 9
- SF-cadence: trigger=bucket+interval: misdecodes 16
- SF-capacity-local: capacity=4: decode_failures 58
- SF-capacity-local: capacity=8: decode_failures 4
- SF-capacity: capacity=4: decode_failures 58
- SF-capacity: capacity=8: decode_failures 4
- SF-capacity-window: capacity=8: misdecodes 25
- SF-capacity-window: capacity=8: decode_failures 40
- SF-capacity-window: capacity=16: misdecodes 23
- SF-capacity-window: capacity=32: misdecodes 35
- SF-catchup: catch-up-hours=: misdecodes 16
- SF-catchup: catch-up-hours=02-06: decode_failures 36
- SF-catchup: catch-up-hours=00-08: misdecodes 3
- SF-catchup: catch-up-hours=00-08: decode_failures 37
- SF-hops-flat: hops-apart=3: decode_failures 26
- SF-hops-flat: hops-apart=4: decode_failures 40
- SF-hops-spread: hops-apart=3: decode_failures 26
- SF-hops-spread: hops-apart=4: decode_failures 40
- SF-hops-spread: hops-apart=5: decode_failures 17
- SF-place-flat: place=spread: decode_failures 6
- SF-place-spread: place=spread: decode_failures 6
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 18
- SF-replay-order: replay-ordering=heard: misdecodes 17
- SF-window-size: window-size=8: misdecodes 152
- SF-window-size: window-size=16: misdecodes 80
- SF-window-size: window-size=32: misdecodes 35
- TH-congestion: no-congestion-scaling=True: queue drops 13.9% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 83

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 4.76 | 1.98 | 2.40x | 44 |
| `RF-stretch-duct` | 4.36 | 1.82 | 2.39x | 44 |
| `MS-size` | 5.66 | 3.38 | 1.67x | 44 |
| `SF-hops-flat` | 6.09 | 3.92 | 1.56x | 44 |
| `MS-density` | 2.3 | 3.43 | 0.67x | 44 |
| `SF-window-size` | 0.942 | 1.41 | 0.67x | 44 |
| `AD-siting` | 0.986 | 1.49 | 0.66x | 44 |
| `RF-pulse` | 1.1 | 1.67 | 0.66x | 44 |
| `SF-replay-order` | 1.09 | 1.67 | 0.66x | 44 |
| `SF-servers-flat` | 1.56 | 2.4 | 0.65x | 44 |
| `TH-congestion-mode` | 2.15 | 3.34 | 0.64x | 44 |
| `RT-spread` | 1.45 | 2.33 | 0.62x | 44 |
| `SF-place-spread` | 1.73 | 2.8 | 0.62x | 44 |
| `RT-hoplimit` | 1.08 | 1.77 | 0.61x | 44 |
| `FW-mixed-26` | 1.02 | 1.71 | 0.59x | 44 |
| `RF-preset` | 1.63 | 2.91 | 0.56x | 44 |
| `DM-mode` | 1.77 | 3.29 | 0.54x | 44 |
| `SF-servers-spread` | 1.23 | 2.32 | 0.53x | 44 |
| `SF-place-flat` | 1.52 | 2.86 | 0.53x | 44 |
| `SF-cadence` | 1.85 | 3.61 | 0.51x | 44 |
| `FW-signing-cost` | 0.821 | 1.6 | 0.51x | 44 |
| `AD-amplifiers` | 0.799 | 1.62 | 0.49x | 44 |
| `PR-crladder` | 1.36 | 2.79 | 0.49x | 44 |
| `LD-interval` | 0.615 | 1.29 | 0.48x | 44 |
| `MS-siting` | 0.896 | 1.93 | 0.47x | 43 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.919 | 0.919 | 0.756 → 0.761 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.084 → 0.919 | 0.836 | 0.066 → 0.758 | 12x advert_bytes | up | 5 |
| `BL-control` | protocol | **held** | 0 → 0.823 | 0.823 | 0.757 → 0.761 | 1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.148 → 0.919 | 0.772 | 0.089 → 0.758 | 6.9x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.162 → 0.913 | 0.751 | 0.059 → 0.710 | 6.2x advert_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.120 → 0.861 | 0.742 | 0.103 → 0.705 | 80x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.219 → 0.911 | 0.693 | 0.212 → 0.911 | 2.4x sr_airtime | up | 4 |
| `SF-place-flat` | place | **held** | 0.285 → 0.941 | 0.656 | 0.751 → 0.763 | 3.4x advert_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.285 → 0.941 | 0.656 | 0.751 → 0.763 | 3.4x advert_bytes | up | 6 |
| `MS-stretch` | stretch | **held** | 0.270 → 0.919 | 0.650 | 0.172 → 0.758 | 4.8x sr_airtime | down | 4 |
| `MS-hopscale` | nodes | **held** | 0.301 → 0.919 | 0.619 | 0.331 → 0.758 | 8.2x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.303 → 0.920 | 0.617 | 0.335 → 0.737 | 4.7x bytes_on_air | down | 3 |
| `RF-bw500` | preset | **text** | 0.207 → 0.672 | 0.465 | 0.203 → 0.664 | 1.9x advert_bytes | up | 3 |
| `MS-density` | nodes | **text** | 0.572 → 0.957 | 0.385 | 0.568 → 0.955 | 5.1x advert_bytes | up | 5 |
| `RF-preset` | preset | **text** | 0.422 → 0.783 | 0.361 | 0.410 → 0.769 | 2.3x sr_airtime | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.519 → 0.868 | 0.349 | 0.510 → 0.865 | 14x sr_airtime | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.422 → 0.762 | 0.340 | 0.410 → 0.758 | 1.7x sr_airtime | up | 4 |
| `MS-topology` | topology | **text** | 0.662 → 0.969 | 0.306 | 0.650 → 0.967 | 2.9x sr_bytes | up | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.440 → 0.739 | 0.299 | 0.431 → 0.731 | 1.6x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.482 → 0.762 | 0.280 | 0.462 → 0.758 | 2.7x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.525 → 0.789 | 0.265 | 0.508 → 0.784 | 8.9x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.502 → 0.762 | 0.261 | 0.467 → 0.758 | 3.2x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.667 → 0.921 | 0.254 | 0.757 → 0.759 | 5.8x sr_bytes | down | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.531 → 0.777 | 0.246 | 0.321 → 0.516 | 4.9x sr_airtime | up | 3 |
| `MS-size` | nodes | **held** | 0.738 → 0.978 | 0.240 | 0.686 → 0.796 | 5.5x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.717 → 0.953 | 0.236 | 0.713 → 0.953 | 4.6x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.635 → 0.858 | 0.223 | 0.613 → 0.857 | 1.8x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.635 → 0.835 | 0.200 | 0.613 → 0.830 | 1.5x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.762 → 0.930 | 0.167 | 0.758 → 0.928 | 1.3x bytes_on_air | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.775 → 0.925 | 0.150 | 0.613 → 0.758 | 1.5x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.635 → 0.762 | 0.128 | 0.613 → 0.758 | 1.5x sr_bytes | up | 2 |
| `FW-versions` | profile | **text** | 0.762 → 0.888 | 0.126 | 0.758 → 0.887 | 3.3x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.762 → 0.884 | 0.121 | 0.758 → 0.880 | 3.2x bytes_on_air | down | 2 |
| `SC-signing` | signature-policy | **text** | 0.648 → 0.762 | 0.114 | 0.648 → 0.758 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.658 → 0.762 | 0.104 | 0.646 → 0.758 | 1.5x sr_bytes | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.817 → 0.921 | 0.104 | 0.757 → 0.758 | 5.8x sr_bytes | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.762 → 0.864 | 0.102 | 0.758 → 0.860 | 1.3x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.762 → 0.863 | 0.100 | 0.758 → 0.857 | 1.5x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.721 → 0.821 | 0.100 | 0.710 → 0.816 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.721 → 0.821 | 0.100 | 0.710 → 0.816 | 2.2x bytes_on_air | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.762 → 0.862 | 0.100 | 0.758 → 0.856 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.762 → 0.855 | 0.093 | 0.758 → 0.849 | 2.1x bytes_on_air | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.704 → 0.791 | 0.086 | 0.694 → 0.786 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.715 → 0.791 | 0.076 | 0.706 → 0.786 | 2x sr_airtime | up | 4 |
| `AD-badrouters` | role-placement | **text** | 0.648 → 0.721 | 0.073 | 0.633 → 0.710 | 1.3x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.734 → 0.805 | 0.071 | 0.727 → 0.802 | 5.8x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.658 → 0.723 | 0.065 | 0.654 → 0.719 | 1.4x sr_airtime | down | 2 |
| `MS-roles` | role-mix | **text** | 0.721 → 0.779 | 0.058 | 0.710 → 0.772 | 1.2x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.769 → 0.815 | 0.046 | 0.511 → 0.550 | 1.4x sr_airtime | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.877 → 0.919 | 0.043 | 0.758 → 0.762 | 25x sr_airtime | down | 3 |
| `RT-hopassign` | hop-assign | **held** | 0.885 → 0.919 | 0.034 | 0.751 → 0.758 | 1.1x sr_bytes | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.762 → 0.796 | 0.034 | 0.758 → 0.794 | 3.4x bytes_on_air | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.740 → 0.770 | 0.030 | 0.732 → 0.763 | 1.4x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.895 → 0.919 | 0.024 | 0.741 → 0.758 | 14x advert_bytes | down | 4 |
| `AD-worst` | role-placement | **text** | 0.819 → 0.840 | 0.021 | 0.812 → 0.836 | 1.2x sr_bytes | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.915 → 0.936 | 0.021 | 0.751 → 0.762 | 8.2x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.915 → 0.936 | 0.021 | 0.751 → 0.762 | 8.2x sr_bytes | up | 4 |
| `LD-diurnal` | diurnal | **held** | 0.919 → 0.940 | 0.020 | 0.758 → 0.775 | 1.2x sr_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.762 → 0.783 | 0.020 | 0.758 → 0.764 | 2.3x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **held** | 0.909 → 0.926 | 0.017 | 0.756 → 0.760 | 4.3x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **held** | 0.903 → 0.920 | 0.016 | 0.732 → 0.747 | 1.3x sr_airtime | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.769 → 0.785 | 0.016 | 0.763 → 0.781 | 1.1x sr_bytes | up | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.769 → 0.785 | 0.016 | 0.760 → 0.780 | 1.2x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.905 → 0.920 | 0.015 | 0.739 → 0.747 | 1.1x sr_airtime | down | 2 |
| `SF-width` | short-id-bits | **held** | 0.919 → 0.933 | 0.014 | 0.757 → 0.764 | 3.2x advert_bytes | up | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.917 → 0.929 | 0.012 | 0.750 → 0.754 | 1.2x sr_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.919 → 0.931 | 0.012 | 0.758 → 0.762 | 2.8x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.905 → 0.917 | 0.012 | 0.747 → 0.762 | 9.4x advert_bytes | down | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.910 → 0.921 | 0.011 | 0.758 → 0.767 | 1.3x bytes_on_air | down | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.755 → 0.766 | 0.010 | 0.749 → 0.760 | 5.2x advert_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.909 → 0.919 | 0.010 | 0.753 → 0.762 | 2.5x advert_bytes | up | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.905 → 0.915 | 0.010 | 0.739 → 0.744 | 1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.944 → 0.953 | 0.009 | 0.942 → 0.953 | 1.2x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.762 → 0.772 | 0.009 | 0.758 → 0.767 | 1.1x sr_bytes | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.921 → 0.930 | 0.009 | 0.751 → 0.756 | 3x sr_bytes | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.919 → 0.926 | 0.006 | 0.758 → 0.762 | 2.5x advert_bytes | down | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.776 → 0.783 | 0.006 | 0.757 → 0.764 | 1.1x sr_bytes | down | 2 |
| `SF-capacity` | capacity | **held** | 0.918 → 0.923 | 0.006 | 0.756 → 0.760 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.918 → 0.923 | 0.006 | 0.756 → 0.760 | 5.3x advert_bytes | up | 5 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.919 → 0.925 | 0.006 | 0.758 → 0.760 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.919 → 0.925 | 0.006 | 0.758 → 0.760 | 1.1x sr_bytes | up | 4 |
| `SF-resolve` | resolve | **held** | 0.919 → 0.922 | 0.003 | 0.755 → 0.758 | 5.7x advert_bytes | = | 3 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.996 → 0.998 | 0.002 | 0.953 → 0.953 | 1x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.762 → 0.764 | 0.001 | 0.758 → 0.759 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.996 → 0.997 | 0.001 | 0.952 → 0.953 | 1.1x sr_airtime | down | 2 |

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
| none | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| sprinkled | 1 | 0.853 | 0.846 | 0.007 | - | - | 0.958 | 0.960 | 0.000 | 1.31x | 17.1/26.5/30.8% | 1.8/5.3% | 3 |
| arms-race | 1 | 0.930 | 0.928 | 0.002 | - | - | 0.985 | 0.986 | 0.324 | 1.06x | 17.2/25.7/28.7% | 1.5/5.4% | 3 |

> faster: 0.799 s per simulated hour against 1.62 over 44 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.802 | 0.795 | 0.007 | - | - | 0.943 | 0.945 | 0.000 | 1.37x | 17.9/27.4/30.0% | 2.1/5.5% | 3 |
| 0.3 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.951 | 0.952 | 0.000 | 1.11x | 19.6/26.5/28.4% | 1.5/5.3% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.721 | 0.710 | 0.011 | - | - | 0.913 | 0.913 | 0.000 | 1.14x | 14.8/23.9/28.2% | 1.8/5.1% | 3 |
| inverse | 1 | 0.648 | 0.633 | 0.015 | - | - | 0.842 | 0.843 | 0.000 | 1.08x | 13.6/18.5/21.0% | 2.0/3.8% | 3 |
| random | 1 | 0.660 | 0.641 | 0.019 | - | - | 0.865 | 0.867 | 0.000 | 1.18x | 14.2/20.2/26.3% | 1.9/5.0% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.721 | 0.710 | 0.011 | - | - | 0.913 | 0.913 | 0.000 | 1.14x | 14.8/23.9/28.2% | 1.8/5.1% | 3 |
| all-routers | 1 | 0.821 | 0.816 | 0.005 | - | - | 0.940 | 0.941 | 0.000 | 2.55x | 28.3/39.4/42.5% | 4.3/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.721 | 0.710 | 0.011 | - | - | 0.913 | 0.913 | 0.000 | 1.14x | 14.8/23.9/28.2% | 1.8/5.1% | 3 |
| no-mute | 1 | 0.768 | 0.757 | 0.010 | - | - | 0.945 | 0.946 | 0.000 | 1.33x | 15.6/23.6/26.6% | 2.1/5.2% | 3 |
| all-routers | 1 | 0.821 | 0.816 | 0.005 | - | - | 0.940 | 0.941 | 0.000 | 2.55x | 28.3/39.4/42.5% | 4.3/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.721 | 0.710 | 0.011 | - | - | 0.913 | 0.913 | 0.000 | 1.14x | 14.8/23.9/28.2% | 1.8/5.1% | 3 |
| local-typical | 1 | 0.580 | 0.574 | 0.006 | - | - | 0.829 | 0.830 | 0.000 | 1.36x | 13.7/24.1/29.4% | 2.2/5.8% | 3 |
| basement-heavy | 1 | 0.060 | 0.059 | 0.001 | - | - | 0.162 | 0.199 | 0.000 | 0.49x | 1.5/4.8/10.2% | 0.3/2.9% | 3 |

> siting-mix=basement-heavy: decode_failures 5

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.840 | 0.836 | 0.004 | - | - | 0.960 | 0.960 | 0.139 | 2.33x | 19.4/28.7/37.7% | 1.6/5.8% | 3 |
| inverse | 1 | 0.819 | 0.812 | 0.007 | - | - | 0.964 | 0.965 | 0.124 | 2.24x | 16.3/25.7/35.2% | 1.8/3.5% | 3 |

> role-placement=degree: misdecodes 1

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.761 | 0.761 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.34x | 16.4/25.8/28.7% | 1.9/5.1% | 3 |
| sr | 1 | 0.775 | 0.757 | 0.018 | - | - | 0.823 | 0.947 | 0.000 | 1.37x | 16.8/26.3/29.3% | 2.0/5.2% | 3 |

> protocol=sr: decode_failures 26

> slower: 4.76 s per simulated hour against 1.98 over 44 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.715 | 0.706 | 0.009 | - | - | 0.851 | 0.851 | 0.000 | 2.88x | 35.0/55.8/60.6% | 3.9/9.4% | 3 |
| 100 | 1 | 0.791 | 0.786 | 0.004 | - | - | 0.909 | 0.910 | 0.000 | 1.54x | 18.8/32.0/34.9% | 2.1/5.0% | 3 |
| 120 | 1 | 0.791 | 0.786 | 0.004 | - | - | 0.909 | 0.910 | 0.000 | 1.54x | 18.8/32.0/34.9% | 2.1/5.0% | 3 |
| 250 | 1 | 0.791 | 0.786 | 0.004 | - | - | 0.909 | 0.910 | 0.000 | 1.54x | 18.8/32.0/34.9% | 2.1/5.0% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.326 | 0.321 | 0.005 | - | - | 0.531 | 0.583 | 0.052 | 11.49x | 37.7/63.0/75.8% | 4.0/11.4% | 3 |
| 120 | 1 | 0.518 | 0.511 | 0.008 | - | - | 0.769 | 0.771 | 0.070 | 4.73x | 15.3/31.0/43.9% | 1.6/6.0% | 3 |
| 250 | 1 | 0.523 | 0.516 | 0.008 | - | - | 0.777 | 0.779 | 0.070 | 4.64x | 15.1/30.0/42.5% | 1.6/5.8% | 3 |

> max-num-nodes=10: decode_failures 66

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.791 | 0.786 | 0.004 | - | - | 0.909 | 0.910 | 0.000 | 1.54x | 18.8/32.0/34.9% | 2.1/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.791 | 0.786 | 0.004 | - | - | 0.909 | 0.910 | 0.000 | 1.54x | 18.8/32.0/34.9% | 2.1/5.0% | 3 |
| constrained | 1 | 0.704 | 0.694 | 0.011 | - | - | 0.834 | 0.835 | 0.000 | 2.89x | 35.0/56.0/60.8% | 3.9/9.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.723 | 0.719 | 0.004 | - | - | 0.888 | 0.911 | 0.505 | 5.84x | 57.8/73.4/77.3% | 4.3/13.3% | 3 |
| 25 | 1 | 0.723 | 0.719 | 0.004 | - | - | 0.888 | 0.911 | 0.505 | 5.84x | 57.8/73.4/77.3% | 4.3/13.3% | 3 |
| 100 | 1 | 0.723 | 0.719 | 0.004 | - | - | 0.888 | 0.911 | 0.505 | 5.84x | 57.8/73.4/77.3% | 4.3/13.3% | 3 |
| 2000 | 1 | 0.723 | 0.719 | 0.004 | - | - | 0.888 | 0.911 | 0.505 | 5.84x | 57.8/73.4/77.3% | 4.3/13.3% | 3 |

> warm-num-nodes=0: queue drops 14.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 121

> warm-num-nodes=25: queue drops 14.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 121

> warm-num-nodes=100: queue drops 14.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 121

> warm-num-nodes=2000: queue drops 14.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 121

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.681 | 0.667 | 0.014 | - | - | 0.907 | 0.909 | 0.000 | 1.29x | 16.2/25.5/28.2% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.591 | 0.566 | 0.025 | - | - | 0.869 | 0.876 | 0.000 | 1.19x | 15.1/24.2/26.5% | 1.8/4.4% | 3 |
| 0.3 | 1 | 0.502 | 0.467 | 0.035 | - | - | 0.800 | 0.829 | 0.000 | 1.10x | 14.0/22.5/24.8% | 1.7/3.9% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 36

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.732 | 0.725 | 0.007 | - | - | 0.913 | 0.915 | 0.000 | 1.41x | 17.6/27.5/30.2% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.692 | 0.683 | 0.009 | - | - | 0.884 | 0.887 | 0.000 | 1.43x | 17.9/27.8/30.6% | 2.2/5.0% | 3 |
| 0.3 | 1 | 0.658 | 0.646 | 0.012 | - | - | 0.878 | 0.880 | 0.000 | 1.44x | 18.3/28.3/31.0% | 2.3/4.8% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.668 | 0.654 | 0.014 | - | - | 0.895 | 0.903 | 0.000 | 1.31x | 16.3/25.7/28.3% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.577 | 0.560 | 0.016 | - | - | 0.820 | 0.886 | 0.000 | 1.17x | 15.2/23.2/25.8% | 1.8/4.2% | 3 |
| 0.3 | 1 | 0.482 | 0.462 | 0.020 | - | - | 0.715 | 0.815 | 0.000 | 1.12x | 14.3/23.7/25.7% | 1.7/4.3% | 3 |

> burst-loss=0.1: decode_failures 13

> burst-loss=0.2: decode_failures 39

> burst-loss=0.3: decode_failures 34

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.732 | 0.732 | 0.000 | - | - | 0.903 | 0.903 | 0.000 | 1.78x | 21.7/34.6/38.7% | 2.6/6.9% | 3 |
| directed-with-late-flood | 1 | 0.747 | 0.747 | 0.000 | - | - | 0.920 | 0.923 | 0.000 | 1.62x | 19.8/31.6/35.3% | 2.3/6.2% | 3 |
| m4-early-flood | 1 | 0.739 | 0.739 | 0.000 | - | - | 0.911 | 0.914 | 0.000 | 1.61x | 19.7/31.3/35.1% | 2.3/6.2% | 3 |

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.884 | 0.880 | 0.004 | - | - | 0.987 | 0.987 | 0.000 | 0.76x | 9.3/11.7/13.5% | 1.2/2.1% | 3 |
| 2.8 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.862 | 0.856 | 0.006 | - | - | 0.954 | 0.956 | 0.000 | 1.27x | 14.9/25.0/28.0% | 1.9/4.4% | 3 |
| 0.5 | 1 | 0.853 | 0.844 | 0.009 | - | - | 0.980 | 0.982 | 0.000 | 1.07x | 13.5/20.5/23.7% | 1.7/4.2% | 3 |
| 0.75 | 1 | 0.847 | 0.841 | 0.006 | - | - | 0.964 | 0.966 | 0.000 | 0.89x | 11.1/15.0/16.1% | 1.5/2.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.855 | 0.849 | 0.006 | - | - | 0.957 | 0.957 | 0.000 | 1.30x | 15.6/26.1/29.1% | 2.0/4.6% | 3 |
| 0.5 | 1 | 0.844 | 0.834 | 0.011 | - | - | 0.987 | 0.991 | 0.000 | 1.01x | 12.9/19.5/23.3% | 1.6/4.1% | 3 |
| 0.75 | 1 | 0.851 | 0.844 | 0.007 | - | - | 0.964 | 0.964 | 0.000 | 0.91x | 11.6/15.6/16.9% | 1.5/2.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.796 | 0.794 | 0.003 | - | - | 0.939 | 0.940 | 0.000 | 0.73x | 9.2/14.9/16.7% | 1.1/3.0% | 3 |
| signing=true | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.873 | 0.870 | 0.003 | - | - | 0.982 | 0.984 | 0.000 | 0.76x | 9.8/12.9/15.1% | 1.1/2.4% | 3 |
| 2.5 | 1 | 0.869 | 0.867 | 0.003 | - | - | 0.981 | 0.981 | 0.000 | 0.80x | 10.2/13.2/15.4% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.868 | 0.865 | 0.003 | - | - | 0.979 | 0.980 | 0.000 | 0.75x | 10.0/13.1/15.4% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.888 | 0.887 | 0.002 | - | - | 0.982 | 0.984 | 0.000 | 0.78x | 10.4/15.2/18.6% | 1.1/3.3% | 3 |
| 2.8 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.789 | 0.784 | 0.005 | - | - | 0.943 | 0.944 | 0.000 | 0.94x | 11.5/18.5/20.4% | 1.3/3.7% | 3 |
| 900 | 1 | 0.734 | 0.727 | 0.007 | - | - | 0.902 | 0.905 | 0.000 | 2.19x | 26.7/41.5/46.0% | 3.2/8.2% | 3 |
| 300 | 1 | 0.525 | 0.508 | 0.017 | - | - | 0.751 | 0.770 | 0.000 | 4.78x | 53.7/74.0/78.4% | 7.5/15.7% | 3 |

> broadcast-interval-s=300: decode_failures 10

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.868 | 0.865 | 0.003 | - | - | 0.970 | 0.970 | 0.000 | 1.00x | 12.2/18.3/20.4% | 1.5/3.6% | 3 |
| 900 | 1 | 0.791 | 0.785 | 0.007 | - | - | 0.902 | 0.903 | 0.000 | 2.43x | 29.0/43.1/47.7% | 3.4/8.4% | 3 |
| 300 | 1 | 0.519 | 0.510 | 0.009 | - | - | 0.664 | 0.669 | 0.000 | 5.17x | 57.8/75.4/79.3% | 8.4/16.6% | 3 |

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.781 | 0.775 | 0.006 | - | - | 0.940 | 0.941 | 0.000 | 1.29x | 15.9/25.4/28.3% | 1.9/5.0% | 3 |
| sinusoid | 1 | 0.773 | 0.768 | 0.006 | - | - | 0.936 | 0.937 | 0.000 | 1.25x | 15.4/24.6/27.4% | 1.8/4.8% | 3 |
| commuter | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.734 | 0.727 | 0.007 | - | - | 0.902 | 0.905 | 0.000 | 2.19x | 26.7/41.5/46.0% | 3.2/8.2% | 3 |
| 3600 | 1 | 0.789 | 0.784 | 0.005 | - | - | 0.943 | 0.944 | 0.000 | 0.94x | 11.5/18.5/20.4% | 1.3/3.7% | 3 |
| 10800 | 1 | 0.805 | 0.802 | 0.003 | - | - | 0.954 | 0.954 | 0.000 | 0.60x | 7.3/11.9/13.1% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.799 | 0.796 | 0.003 | - | - | 0.944 | 0.945 | 0.000 | 0.42x | 5.0/8.5/9.4% | 0.6/1.7% | 3 |

> faster: 0.615 s per simulated hour against 1.29 over 44 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.770 | 0.763 | 0.007 | - | - | 0.933 | 0.933 | 0.000 | 1.44x | 17.7/28.2/31.2% | 2.1/5.5% | 3 |
| 1.0 | 1 | 0.755 | 0.748 | 0.006 | - | - | 0.915 | 0.916 | 0.000 | 1.57x | 19.4/30.7/34.1% | 2.2/6.0% | 3 |
| 4.0 | 1 | 0.740 | 0.732 | 0.008 | - | - | 0.914 | 0.915 | 0.000 | 1.91x | 23.6/37.6/41.7% | 2.8/7.7% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.719 | 0.004 | - | - | 0.888 | 0.911 | 0.505 | 5.84x | 57.8/73.4/77.3% | 4.3/13.3% | 3 |
| 1.0 | 1 | 0.658 | 0.654 | 0.004 | - | - | 0.831 | 0.879 | 0.457 | 6.41x | 61.3/75.7/79.3% | 4.8/14.6% | 3 |

> traceroute-per-hour=0.0: queue drops 14.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 121

> traceroute-per-hour=1.0: queue drops 21.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 114

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.572 | 0.568 | 0.004 | - | - | 0.723 | 0.725 | 0.057 | 1.21x | 18.1/27.5/33.4% | 2.7/6.1% | 3 |
| 60 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 90 | 1 | 0.912 | 0.909 | 0.003 | - | - | 0.985 | 0.985 | 0.643 | 1.72x | 18.9/30.5/36.1% | 1.6/5.1% | 3 |
| 120 | 1 | 0.953 | 0.953 | 0.001 | - | - | 0.996 | 0.996 | 0.816 | 2.04x | 22.1/34.7/38.8% | 1.4/5.4% | 3 |
| 150 | 1 | 0.957 | 0.955 | 0.002 | - | - | 0.999 | 1.000 | 0.739 | 2.61x | 27.3/37.9/44.8% | 1.3/5.6% | 3 |

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 120 | 1 | 0.738 | 0.733 | 0.005 | - | - | 0.917 | 0.918 | 0.189 | 2.19x | 15.6/23.2/30.1% | 1.5/5.2% | 3 |
| 250 | 1 | 0.522 | 0.514 | 0.008 | - | - | 0.779 | 0.780 | 0.075 | 5.05x | 16.1/32.9/46.6% | 1.7/6.4% | 3 |
| 500 | 1 | 0.332 | 0.331 | 0.001 | - | - | 0.301 | 0.308 | 0.107 | 10.15x | 18.7/32.9/42.9% | 1.7/5.6% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 65

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.742 | 0.737 | 0.005 | - | - | 0.920 | 0.921 | 0.180 | 2.01x | 14.2/21.2/27.6% | 1.4/4.7% | 3 |
| 250 | 1 | 0.518 | 0.511 | 0.008 | - | - | 0.769 | 0.771 | 0.070 | 4.73x | 15.3/31.0/43.9% | 1.6/6.0% | 3 |
| 500 | 1 | 0.337 | 0.335 | 0.001 | - | - | 0.303 | 0.310 | 0.109 | 9.34x | 17.5/30.3/39.6% | 1.6/5.2% | 3 |

> nodes=500: decode_failures 33

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.779 | 0.772 | 0.007 | - | - | 0.915 | 0.916 | 0.000 | 1.37x | 16.8/26.7/29.6% | 1.9/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.721 | 0.710 | 0.011 | - | - | 0.913 | 0.913 | 0.000 | 1.14x | 14.8/23.9/28.2% | 1.8/5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.785 | 0.780 | 0.004 | - | - | 0.908 | 0.909 | 0.000 | 1.40x | 17.2/26.9/29.7% | 2.1/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.769 | 0.760 | 0.009 | - | - | 0.900 | 0.902 | 0.000 | 1.30x | 16.7/27.2/32.3% | 2.1/5.0% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.05 | 1 | 0.767 | 0.761 | 0.006 | - | - | 0.921 | 0.923 | 0.000 | 1.46x | 18.3/30.6/34.4% | 2.1/5.1% | 3 |
| 0.1 | 1 | 0.769 | 0.763 | 0.006 | - | - | 0.910 | 0.911 | 0.000 | 1.54x | 19.2/32.8/36.2% | 2.2/5.0% | 3 |
| 0.2 | 1 | 0.773 | 0.767 | 0.006 | - | - | 0.915 | 0.915 | 0.000 | 1.78x | 22.5/36.5/42.1% | 2.6/5.2% | 3 |

> router-late-fraction=0.2: misdecodes 1

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| local-typical | 1 | 0.646 | 0.641 | 0.005 | - | - | 0.869 | 0.871 | 0.000 | 1.52x | 16.3/23.5/26.8% | 2.4/5.7% | 3 |
| event | 1 | 0.219 | 0.212 | 0.007 | - | - | 0.508 | 0.511 | 0.000 | 1.17x | 3.7/18.3/25.7% | 1.0/5.2% | 3 |
| backbone | 1 | 0.911 | 0.911 | 0.000 | - | - | 0.956 | 0.956 | 0.000 | 1.14x | 26.7/32.0/36.6% | 1.3/5.3% | 3 |

> faster: 0.896 s per simulated hour against 1.93 over 43 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.829 | 0.796 | 0.033 | - | - | 0.978 | 0.982 | 0.387 | 1.39x | 25.0/35.5/40.7% | 3.1/7.3% | 3 |
| 60 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 90 | 1 | 0.764 | 0.749 | 0.016 | - | - | 0.934 | 0.935 | 0.222 | 1.77x | 16.0/23.4/27.5% | 1.8/5.1% | 3 |
| 120 | 1 | 0.738 | 0.733 | 0.005 | - | - | 0.917 | 0.918 | 0.189 | 2.19x | 15.6/23.2/30.1% | 1.5/5.2% | 3 |
| 150 | 1 | 0.698 | 0.686 | 0.012 | - | - | 0.738 | 0.786 | 0.321 | 2.76x | 16.6/26.0/30.4% | 1.6/5.5% | 3 |

> nodes=150: decode_failures 76

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 1.25 | 1 | 0.581 | 0.569 | 0.012 | - | - | 0.842 | 0.846 | 0.000 | 1.40x | 14.0/20.5/25.6% | 2.3/5.1% | 3 |
| 1.5 | 1 | 0.440 | 0.431 | 0.009 | - | - | 0.784 | 0.802 | 0.000 | 1.44x | 10.8/18.8/22.2% | 2.4/5.7% | 3 |
| 2.0 | 1 | 0.173 | 0.172 | 0.001 | - | - | 0.270 | 0.272 | 0.000 | 1.05x | 4.7/10.8/14.4% | 1.6/4.1% | 3 |

> stretch=1.25: decode_failures 2

> stretch=1.5: decode_failures 18

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| clustered | 1 | 0.969 | 0.967 | 0.002 | - | - | 0.998 | 0.998 | 0.820 | 1.18x | 24.7/33.2/36.4% | 1.6/5.5% | 3 |
| corridor | 1 | 0.662 | 0.650 | 0.011 | - | - | 0.894 | 0.901 | 0.121 | 1.15x | 17.2/21.5/25.3% | 1.6/5.8% | 3 |
| hub | 1 | 0.952 | 0.944 | 0.007 | - | - | 0.997 | 0.997 | 0.831 | 1.27x | 25.9/37.5/40.2% | 1.9/5.5% | 3 |

> topology=corridor: decode_failures 4

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.747 | 0.747 | 0.000 | - | - | 0.920 | 0.923 | 0.000 | 1.62x | 19.8/31.6/35.3% | 2.3/6.2% | 3 |
| True | 1 | 0.739 | 0.739 | 0.000 | - | - | 0.905 | 0.905 | 0.000 | 1.61x | 19.7/31.4/35.0% | 2.3/6.2% | 3 |

> faster: 1.36 s per simulated hour against 2.79 over 44 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.739 | 0.739 | 0.000 | - | - | 0.905 | 0.905 | 0.000 | 1.61x | 19.7/31.4/35.0% | 2.3/6.2% | 3 |
| m4-early-flood | 1 | 0.744 | 0.744 | 0.000 | - | - | 0.915 | 0.915 | 0.000 | 1.62x | 19.8/31.7/35.5% | 2.3/6.3% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.761 | 0.761 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.34x | 16.4/25.8/28.7% | 1.9/5.1% | 3 |
| chain | 1 | 0.759 | 0.756 | 0.002 | - | - | 0.889 | 0.925 | 0.000 | 1.56x | 19.3/30.8/34.1% | 2.2/6.0% | 3 |
| sr | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| True | 1 | 0.772 | 0.767 | 0.005 | - | - | 0.927 | 0.929 | 0.000 | 1.38x | 16.9/26.6/29.5% | 1.9/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.953 | 0.953 | 0.001 | - | - | 0.996 | 0.996 | 0.816 | 2.04x | 22.1/34.7/38.8% | 1.4/5.4% | 3 |
| True | 1 | 0.954 | 0.953 | 0.001 | - | - | 0.998 | 0.998 | 0.814 | 2.08x | 22.4/34.7/38.7% | 1.4/5.4% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.207 | 0.203 | 0.004 | - | - | 0.488 | 0.557 | 0.000 | 0.05x | 0.2/0.6/0.9% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.500 | 0.495 | 0.005 | - | - | 0.825 | 0.826 | 0.000 | 0.28x | 2.5/4.0/5.4% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.672 | 0.664 | 0.008 | - | - | 0.904 | 0.904 | 0.000 | 1.28x | 13.3/22.2/25.4% | 2.1/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 12

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.780 | 0.774 | 0.006 | - | - | 0.930 | 0.930 | 0.026 | 1.31x | 17.3/26.7/29.7% | 1.8/5.2% | 3 |
| 1.0 | 1 | 0.864 | 0.860 | 0.004 | - | - | 0.946 | 0.947 | 0.089 | 1.04x | 21.2/28.9/31.6% | 1.3/5.2% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.422 | 0.410 | 0.012 | - | - | 0.721 | 0.723 | 0.000 | 0.15x | 1.1/2.2/2.9% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| LITE_FAST | 1 | 0.691 | 0.684 | 0.006 | - | - | 0.909 | 0.910 | 0.000 | 0.97x | 11.9/18.6/21.2% | 1.4/4.0% | 3 |
| NARROW_SLOW | 1 | 0.703 | 0.695 | 0.008 | - | - | 0.918 | 0.921 | 0.000 | 1.29x | 16.1/24.7/28.3% | 1.9/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| temporal | 1 | 0.677 | 0.668 | 0.009 | - | - | 0.891 | 0.894 | 0.000 | 1.37x | 17.1/25.7/29.5% | 2.1/5.2% | 3 |
| transient | 1 | 0.760 | 0.753 | 0.007 | - | - | 0.925 | 0.927 | 0.000 | 1.38x | 16.8/26.6/29.5% | 1.9/5.2% | 3 |
| periodic | 1 | 0.620 | 0.613 | 0.006 | - | - | 0.775 | 0.778 | 0.000 | 1.27x | 15.9/24.8/27.4% | 1.9/4.6% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.422 | 0.410 | 0.012 | - | - | 0.721 | 0.723 | 0.000 | 0.15x | 1.1/2.2/2.9% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| LONG_MODERATE | 1 | 0.783 | 0.769 | 0.013 | - | - | 0.894 | 0.897 | 0.000 | 3.52x | 45.2/62.7/66.5% | 5.3/12.3% | 3 |

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.066 | 0.066 | 0.000 | - | - | 0.084 | 0.095 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.207 | 0.203 | 0.004 | - | - | 0.488 | 0.557 | 0.000 | 0.05x | 0.2/0.6/0.9% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| LONG_TURBO | 1 | 0.672 | 0.664 | 0.008 | - | - | 0.904 | 0.904 | 0.000 | 1.28x | 13.3/22.2/25.4% | 2.1/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.748 | 0.743 | 0.005 | - | - | 0.903 | 0.903 | 0.000 | 1.93x | 21.7/34.6/38.7% | 2.9/6.9% | 3 |

> preset=SHORT_TURBO: decode_failures 12

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.709 | 0.705 | 0.004 | - | - | 0.861 | 0.863 | 0.000 | 1.34x | 16.7/26.3/29.1% | 1.9/5.0% | 3 |
| 10000 | 1 | 0.620 | 0.613 | 0.006 | - | - | 0.775 | 0.778 | 0.000 | 1.27x | 15.9/24.8/27.4% | 1.9/4.6% | 3 |
| 4000 | 1 | 0.384 | 0.381 | 0.003 | - | - | 0.515 | 0.532 | 0.000 | 1.05x | 13.5/20.9/22.8% | 1.7/3.5% | 3 |
| 2000 | 1 | 0.103 | 0.103 | 0.000 | - | - | 0.120 | 0.171 | 0.000 | 0.73x | 9.3/15.3/16.7% | 1.2/2.2% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 5

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.440 | 0.431 | 0.009 | - | - | 0.784 | 0.802 | 0.000 | 1.44x | 10.8/18.8/22.2% | 2.4/5.7% | 3 |
| 1.0 | 1 | 0.739 | 0.731 | 0.008 | - | - | 0.926 | 0.929 | 0.468 | 1.09x | 14.1/21.2/23.5% | 1.5/4.7% | 3 |

> duct-per-hour=0.0: decode_failures 18

> slower: 4.36 s per simulated hour against 1.83 over 44 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 22 | 1 | 0.457 | 0.451 | 0.006 | - | - | 0.757 | 0.759 | 0.000 | 1.46x | 11.9/18.6/25.8% | 2.3/5.2% | 3 |
| 17 | 1 | 0.195 | 0.190 | 0.004 | - | - | 0.434 | 0.523 | 0.000 | 1.06x | 5.4/11.7/16.0% | 1.6/4.5% | 3 |
| 14 | 1 | 0.089 | 0.089 | 0.000 | - | - | 0.148 | 0.149 | 0.000 | 0.69x | 2.7/6.2/7.7% | 1.1/2.5% | 3 |

> tx-power=17: decode_failures 3

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.953 | 0.953 | 0.001 | - | - | 0.996 | 0.996 | 0.816 | 2.04x | 22.1/34.7/38.8% | 1.4/5.4% | 3 |
| True | 1 | 0.944 | 0.942 | 0.002 | - | - | 0.996 | 0.996 | 0.792 | 2.46x | 26.1/39.4/43.7% | 1.6/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.769 | 0.763 | 0.006 | - | - | 0.918 | 0.919 | 0.000 | 1.45x | 18.3/29.7/33.4% | 2.0/5.1% | 3 |
| True | 1 | 0.785 | 0.781 | 0.005 | - | - | 0.916 | 0.917 | 0.000 | 1.50x | 18.7/30.5/34.1% | 2.0/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| random | 1 | 0.759 | 0.751 | 0.007 | - | - | 0.885 | 0.887 | 0.000 | 1.37x | 16.6/26.3/29.0% | 1.9/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.635 | 0.613 | 0.021 | - | - | 0.829 | 0.831 | 0.000 | 1.09x | 13.6/22.6/25.4% | 1.5/4.6% | 3 |
| 7 | 1 | 0.835 | 0.830 | 0.004 | - | - | 0.939 | 0.939 | 0.000 | 1.48x | 17.8/26.8/29.7% | 2.1/5.2% | 3 |
| 15 | 1 | 0.858 | 0.857 | 0.001 | - | - | 0.948 | 0.948 | 0.000 | 1.53x | 18.6/27.9/31.1% | 2.2/5.4% | 3 |
| 32 | 1 | 0.858 | 0.857 | 0.001 | - | - | 0.948 | 0.948 | 0.000 | 1.53x | 18.6/27.9/31.1% | 2.2/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.635 | 0.613 | 0.021 | - | - | 0.829 | 0.831 | 0.000 | 1.09x | 13.6/22.6/25.4% | 1.5/4.6% | 3 |
| 5 | 1 | 0.776 | 0.767 | 0.009 | - | - | 0.906 | 0.906 | 0.000 | 1.35x | 16.6/25.8/28.6% | 1.9/5.0% | 3 |
| 7 | 1 | 0.835 | 0.830 | 0.004 | - | - | 0.939 | 0.939 | 0.000 | 1.48x | 17.8/26.8/29.7% | 2.1/5.2% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.762 | 0.762 | 0.000 | - | - | 0.877 | 0.929 | 0.000 | 1.33x | 16.3/25.7/28.7% | 1.8/5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.635 | 0.613 | 0.021 | - | - | 0.829 | 0.831 | 0.000 | 1.09x | 13.6/22.6/25.4% | 1.5/4.6% | 3 |
| True | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| BALANCED | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| STRICT | 1 | 0.648 | 0.648 | 0.000 | - | - | 0.808 | 0.810 | 0.000 | 1.45x | 17.9/28.3/31.5% | 2.1/5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| dm | 1 | 0.769 | 0.762 | 0.007 | - | - | 0.931 | 0.932 | 0.000 | 1.35x | 16.6/26.5/29.3% | 1.9/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.767 | 0.762 | 0.005 | - | - | 0.926 | 0.927 | 0.000 | 1.39x | 17.1/27.1/30.1% | 2.0/5.3% | 3 |
| local | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| time | 1 | 0.766 | 0.760 | 0.005 | - | - | 0.921 | 0.921 | 0.000 | 1.41x | 17.3/27.3/30.2% | 1.9/5.3% | 3 |
| window | 1 | 0.764 | 0.760 | 0.004 | - | - | 0.919 | 0.921 | 0.000 | 1.36x | 16.8/26.7/29.6% | 1.9/5.2% | 3 |

> bucket-mode=global: misdecodes 47

> bucket-mode=time: misdecodes 40

> bucket-mode=window: misdecodes 35

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.755 | 0.749 | 0.006 | - | - | 0.912 | 0.912 | 0.000 | 1.52x | 18.3/29.6/32.7% | 2.1/5.9% | 3 |
| 1800 | 1 | 0.766 | 0.760 | 0.005 | - | - | 0.921 | 0.921 | 0.000 | 1.41x | 17.3/27.3/30.2% | 1.9/5.3% | 3 |
| 3600 | 1 | 0.764 | 0.759 | 0.005 | - | - | 0.915 | 0.915 | 0.000 | 1.39x | 17.0/27.0/29.9% | 1.9/5.2% | 3 |

> time-bucket-s=600: misdecodes 159

> time-bucket-s=1800: misdecodes 40

> time-bucket-s=3600: misdecodes 11

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| interval | 1 | 0.750 | 0.741 | 0.009 | - | - | 0.911 | 0.912 | 0.000 | 1.78x | 21.4/35.8/38.7% | 2.5/7.3% | 3 |
| aimd | 1 | 0.761 | 0.758 | 0.002 | - | - | 0.895 | 0.930 | 0.000 | 1.40x | 17.3/27.2/30.1% | 2.0/5.3% | 3 |
| bucket+interval | 1 | 0.754 | 0.747 | 0.007 | - | - | 0.917 | 0.919 | 0.000 | 1.81x | 21.9/36.5/39.6% | 2.6/7.5% | 3 |

> trigger=interval: misdecodes 15

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 9

> trigger=bucket+interval: misdecodes 16

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.763 | 0.757 | 0.006 | - | - | 0.919 | 0.921 | 0.000 | 1.37x | 16.8/27.0/29.7% | 1.9/5.3% | 3 |
| 8 | 1 | 0.762 | 0.756 | 0.005 | - | - | 0.918 | 0.919 | 0.000 | 1.37x | 16.8/26.7/29.6% | 1.9/5.2% | 3 |
| 16 | 1 | 0.765 | 0.760 | 0.005 | - | - | 0.923 | 0.925 | 0.000 | 1.38x | 16.8/26.7/29.7% | 1.9/5.3% | 3 |
| 32 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 50 | 1 | 0.764 | 0.758 | 0.005 | - | - | 0.923 | 0.926 | 0.000 | 1.36x | 16.7/26.5/29.5% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 58

> capacity=8: decode_failures 4

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.763 | 0.757 | 0.006 | - | - | 0.919 | 0.921 | 0.000 | 1.37x | 16.8/27.0/29.7% | 1.9/5.3% | 3 |
| 8 | 1 | 0.762 | 0.756 | 0.005 | - | - | 0.918 | 0.919 | 0.000 | 1.37x | 16.8/26.7/29.6% | 1.9/5.2% | 3 |
| 16 | 1 | 0.765 | 0.760 | 0.005 | - | - | 0.923 | 0.925 | 0.000 | 1.38x | 16.8/26.7/29.7% | 1.9/5.3% | 3 |
| 32 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 50 | 1 | 0.764 | 0.758 | 0.005 | - | - | 0.923 | 0.926 | 0.000 | 1.36x | 16.7/26.5/29.5% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 58

> capacity=8: decode_failures 4

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.757 | 0.753 | 0.005 | - | - | 0.909 | 0.921 | 0.000 | 1.36x | 16.8/26.6/29.6% | 1.9/5.1% | 3 |
| 16 | 1 | 0.766 | 0.762 | 0.004 | - | - | 0.917 | 0.920 | 0.000 | 1.35x | 16.5/26.3/29.2% | 1.9/5.1% | 3 |
| 32 | 1 | 0.764 | 0.760 | 0.004 | - | - | 0.919 | 0.921 | 0.000 | 1.36x | 16.8/26.7/29.6% | 1.9/5.2% | 3 |

> capacity=8: misdecodes 25

> capacity=8: decode_failures 40

> capacity=16: misdecodes 23

> capacity=32: misdecodes 35

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.754 | 0.747 | 0.007 | - | - | 0.917 | 0.919 | 0.000 | 1.81x | 21.9/36.5/39.6% | 2.6/7.5% | 3 |
| 02-06 | 1 | 0.764 | 0.761 | 0.003 | - | - | 0.905 | 0.930 | 0.000 | 1.41x | 17.3/27.9/30.8% | 2.0/5.4% | 3 |
| 00-08 | 1 | 0.765 | 0.762 | 0.003 | - | - | 0.911 | 0.932 | 0.000 | 1.47x | 17.8/29.2/32.2% | 2.0/5.8% | 3 |

> catch-up-hours=: misdecodes 16

> catch-up-hours=02-06: decode_failures 36

> catch-up-hours=00-08: misdecodes 3

> catch-up-hours=00-08: decode_failures 37

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.759 | 0.758 | 0.001 | - | - | 0.921 | 0.922 | 0.000 | 1.38x | 16.9/26.6/29.8% | 1.9/5.2% | 3 |
| 2 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 3 | 1 | 0.775 | 0.757 | 0.018 | - | - | 0.823 | 0.947 | 0.000 | 1.37x | 16.8/26.3/29.3% | 2.0/5.2% | 3 |
| 4 | 1 | 0.785 | 0.757 | 0.028 | - | - | 0.817 | 0.944 | 0.000 | 1.41x | 17.1/27.1/30.1% | 2.0/5.5% | 3 |

> hops-apart=3: decode_failures 26

> hops-apart=4: decode_failures 40

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.759 | 0.758 | 0.001 | - | - | 0.921 | 0.922 | 0.000 | 1.38x | 16.9/26.6/29.8% | 1.9/5.2% | 3 |
| 2 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 3 | 1 | 0.775 | 0.757 | 0.018 | - | - | 0.823 | 0.947 | 0.000 | 1.37x | 16.8/26.3/29.3% | 2.0/5.2% | 3 |
| 4 | 1 | 0.785 | 0.757 | 0.028 | - | - | 0.817 | 0.944 | 0.000 | 1.41x | 17.1/27.1/30.1% | 2.0/5.5% | 3 |
| 5 | 1 | 0.776 | 0.759 | 0.017 | - | - | 0.667 | 0.948 | 0.000 | 1.38x | 16.9/26.6/29.4% | 2.0/5.2% | 3 |

> hops-apart=3: decode_failures 26

> hops-apart=4: decode_failures 40

> hops-apart=5: decode_failures 17

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.765 | 0.759 | 0.006 | - | - | 0.922 | 0.923 | 0.000 | 1.38x | 16.8/26.9/29.9% | 1.9/5.3% | 3 |
| 30 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 120 | 1 | 0.765 | 0.760 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.35x | 16.6/26.3/29.2% | 1.9/5.1% | 3 |
| 600 | 1 | 0.763 | 0.758 | 0.005 | - | - | 0.925 | 0.927 | 0.000 | 1.40x | 17.2/27.2/30.1% | 2.0/5.3% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.765 | 0.759 | 0.006 | - | - | 0.922 | 0.923 | 0.000 | 1.38x | 16.8/26.9/29.9% | 1.9/5.3% | 3 |
| 30 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 120 | 1 | 0.765 | 0.760 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.35x | 16.6/26.3/29.2% | 1.9/5.1% | 3 |
| 600 | 1 | 0.763 | 0.758 | 0.005 | - | - | 0.925 | 0.927 | 0.000 | 1.40x | 17.2/27.2/30.1% | 2.0/5.3% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.767 | 0.762 | 0.005 | - | - | 0.285 | 0.589 | 0.000 | 1.37x | 16.7/26.3/29.3% | 2.0/5.1% | 3 |
| routers | 1 | 0.753 | 0.751 | 0.002 | - | - | 0.921 | 0.922 | 0.000 | 1.38x | 16.8/26.8/29.9% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.766 | 0.763 | 0.003 | - | - | 0.936 | 0.937 | 0.000 | 1.39x | 17.0/27.0/30.0% | 2.0/5.3% | 3 |
| beside-router | 1 | 0.766 | 0.762 | 0.004 | - | - | 0.927 | 0.930 | 0.000 | 1.35x | 16.7/26.2/29.4% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.765 | 0.754 | 0.011 | - | - | 0.941 | 0.949 | 0.000 | 1.37x | 16.6/26.3/29.8% | 1.9/5.2% | 3 |
| hops-apart | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

> place=spread: decode_failures 6

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.767 | 0.762 | 0.005 | - | - | 0.285 | 0.589 | 0.000 | 1.37x | 16.7/26.3/29.3% | 2.0/5.1% | 3 |
| routers | 1 | 0.753 | 0.751 | 0.002 | - | - | 0.921 | 0.922 | 0.000 | 1.38x | 16.8/26.8/29.9% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.766 | 0.763 | 0.003 | - | - | 0.936 | 0.937 | 0.000 | 1.39x | 17.0/27.0/30.0% | 2.0/5.3% | 3 |
| beside-router | 1 | 0.766 | 0.762 | 0.004 | - | - | 0.927 | 0.930 | 0.000 | 1.35x | 16.7/26.2/29.4% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.765 | 0.754 | 0.011 | - | - | 0.941 | 0.949 | 0.000 | 1.37x | 16.6/26.3/29.8% | 1.9/5.2% | 3 |
| hops-apart | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

> place=spread: decode_failures 6

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| broadcast | 1 | 0.783 | 0.764 | 0.019 | - | - | 0.924 | 0.927 | 0.000 | 1.41x | 17.3/27.3/30.4% | 2.0/5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| heard | 1 | 0.764 | 0.759 | 0.004 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.7/29.7% | 1.9/5.2% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.783 | 0.764 | 0.019 | - | - | 0.924 | 0.927 | 0.000 | 1.41x | 17.3/27.3/30.4% | 2.0/5.3% | 3 |
| heard | 1 | 0.776 | 0.757 | 0.019 | - | - | 0.921 | 0.923 | 0.000 | 1.42x | 17.4/27.7/30.8% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 18

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| enum | 1 | 0.761 | 0.755 | 0.007 | - | - | 0.922 | 0.924 | 0.000 | 1.36x | 16.8/26.7/29.6% | 1.9/5.3% | 3 |
| hybrid | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.753 | 0.751 | 0.002 | - | - | 0.921 | 0.922 | 0.000 | 1.38x | 16.8/26.8/29.9% | 1.9/5.3% | 3 |
| 6 | 1 | 0.760 | 0.756 | 0.004 | - | - | 0.930 | 0.930 | 0.000 | 1.40x | 17.1/27.3/30.4% | 2.0/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.761 | 0.757 | 0.003 | - | - | 0.915 | 0.916 | 0.000 | 1.36x | 16.6/26.3/29.3% | 2.0/5.1% | 2 |
| 3 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 5 | 1 | 0.771 | 0.762 | 0.008 | - | - | 0.936 | 0.937 | 0.000 | 1.40x | 17.1/27.1/30.3% | 2.0/5.4% | 5 |
| 8 | 1 | 0.763 | 0.751 | 0.013 | - | - | 0.935 | 0.935 | 0.000 | 1.44x | 17.5/28.1/31.2% | 2.1/5.5% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.761 | 0.757 | 0.003 | - | - | 0.915 | 0.916 | 0.000 | 1.36x | 16.6/26.3/29.3% | 2.0/5.1% | 2 |
| 3 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 5 | 1 | 0.771 | 0.762 | 0.008 | - | - | 0.936 | 0.937 | 0.000 | 1.40x | 17.1/27.1/30.3% | 2.0/5.4% | 5 |
| 8 | 1 | 0.763 | 0.751 | 0.013 | - | - | 0.935 | 0.935 | 0.000 | 1.44x | 17.5/28.1/31.2% | 2.1/5.5% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| True | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.760 | 0.754 | 0.006 | - | - | 0.929 | 0.931 | 0.000 | 1.29x | 16.1/25.2/28.0% | 1.9/4.9% | 3 |
| 1 | 1 | 0.758 | 0.751 | 0.007 | - | - | 0.917 | 0.917 | 0.000 | 1.32x | 16.3/25.7/28.3% | 1.9/5.0% | 3 |
| 2 | 1 | 0.757 | 0.750 | 0.007 | - | - | 0.919 | 0.919 | 0.000 | 1.28x | 15.8/24.8/27.4% | 1.8/4.8% | 3 |
| 4 | 1 | 0.759 | 0.751 | 0.007 | - | - | 0.925 | 0.925 | 0.000 | 1.28x | 15.9/25.2/27.6% | 1.8/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.763 | 0.759 | 0.005 | - | - | 0.924 | 0.926 | 0.000 | 1.37x | 16.9/26.9/29.8% | 2.0/5.3% | 3 |
| 24 | 1 | 0.763 | 0.757 | 0.006 | - | - | 0.925 | 0.927 | 0.000 | 1.38x | 17.1/26.9/29.9% | 2.0/5.3% | 3 |
| 32 | 1 | 0.762 | 0.758 | 0.005 | - | - | 0.919 | 0.921 | 0.000 | 1.38x | 16.8/26.8/29.6% | 1.9/5.2% | 3 |
| 64 | 1 | 0.770 | 0.764 | 0.006 | - | - | 0.933 | 0.933 | 0.000 | 1.39x | 17.0/27.0/30.1% | 2.0/5.3% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.761 | 0.756 | 0.006 | - | - | 0.909 | 0.909 | 0.000 | 1.48x | 18.0/28.5/31.7% | 2.1/5.5% | 3 |
| 16 | 1 | 0.764 | 0.759 | 0.005 | - | - | 0.926 | 0.927 | 0.000 | 1.42x | 17.5/27.7/30.7% | 2.0/5.3% | 3 |
| 32 | 1 | 0.764 | 0.760 | 0.004 | - | - | 0.919 | 0.921 | 0.000 | 1.36x | 16.8/26.7/29.6% | 1.9/5.2% | 3 |

> window-size=8: misdecodes 152

> window-size=16: misdecodes 80

> window-size=32: misdecodes 35

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.953 | 0.953 | 0.001 | - | - | 0.996 | 0.996 | 0.816 | 2.04x | 22.1/34.7/38.8% | 1.4/5.4% | 3 |
| True | 1 | 0.717 | 0.713 | 0.004 | - | - | 0.883 | 0.903 | 0.500 | 5.83x | 57.8/73.6/77.3% | 4.2/13.1% | 3 |

> no-congestion-scaling=True: queue drops 13.9% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 83

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.518 | 0.511 | 0.008 | - | - | 0.769 | 0.771 | 0.070 | 4.73x | 15.3/31.0/43.9% | 1.6/6.0% | 3 |
| truesize | 1 | 0.557 | 0.550 | 0.007 | - | - | 0.815 | 0.818 | 0.077 | 3.48x | 11.0/24.1/35.1% | 1.1/5.1% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.953 | 0.952 | 0.001 | - | - | 0.997 | 0.997 | 0.816 | 1.94x | 21.1/32.8/36.6% | 1.3/5.0% | 3 |
| adaptive | 1 | 0.953 | 0.953 | 0.001 | - | - | 0.996 | 0.996 | 0.816 | 2.04x | 22.1/34.7/38.8% | 1.4/5.4% | 3 |

