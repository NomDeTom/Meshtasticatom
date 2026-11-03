# Sweep blocks-2026-11-03-8629140

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 8629140 · seeds 8629140
- **blocks** 87 run
- **compute** 9.0 h of simulator time across every cell
- **generated** 2026-11-03T10:59:08+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>65 warnings</summary>

- AD-amplifiers: amplifier-mix=sprinkled: misdecodes 1
- AD-siting: siting-mix=local-typical: decode_failures 44
- AD-siting: slower: 5.24 s per simulated hour against 1.49 over 74 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=degree: misdecodes 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 15
- DB-warm: warm-num-nodes=0: queue drops 17.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 104
- DB-warm: warm-num-nodes=25: queue drops 17.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 104
- DB-warm: warm-num-nodes=100: queue drops 17.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 104
- DB-warm: warm-num-nodes=2000: queue drops 17.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 104
- DG-burst: burst-loss=0.2: decode_failures 1
- DG-burst: burst-loss=0.3: decode_failures 29
- DG-outage: burst-loss=0.1: decode_failures 11
- DG-outage: burst-loss=0.2: decode_failures 28
- DG-outage: burst-loss=0.3: decode_failures 31
- LD-chatty-hops: broadcast-interval-s=3600: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: queue drops 15.6% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 2
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 17.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 104
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 26.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 102
- MS-density: nodes=40: decode_failures 12
- MS-hopscale: nodes=500: decode_failures 147
- MS-oversubscribed: nodes=500: decode_failures 33
- MS-roles-fav: role-mix=legacy-default: misdecodes 1
- MS-size: nodes=150: decode_failures 1
- MS-stretch: stretch=2.0: 3 archives requested, 2 placed - group on the placed count
- MS-stretch: faster: 1 s per simulated hour against 2.1 over 74 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-preset: preset=LONG_MODERATE: decode_failures 1
- RF-txpower: tx-power=17: decode_failures 4
- SF-bucket-mode: bucket-mode=global: misdecodes 17
- SF-bucket-mode: bucket-mode=time: misdecodes 43
- SF-bucket-mode: bucket-mode=window: misdecodes 31
- SF-bucket-time: time-bucket-s=600: misdecodes 93
- SF-bucket-time: time-bucket-s=1800: misdecodes 43
- SF-bucket-time: time-bucket-s=3600: misdecodes 14
- SF-cadence: trigger=interval: misdecodes 14
- SF-cadence: trigger=aimd: misdecodes 10
- SF-cadence: trigger=bucket+interval: misdecodes 13
- SF-cadence: faster: 1.35 s per simulated hour against 3.61 over 74 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-capacity-local: capacity=4: decode_failures 14
- SF-capacity: capacity=4: decode_failures 14
- SF-capacity-window: capacity=8: misdecodes 34
- SF-capacity-window: capacity=16: misdecodes 35
- SF-capacity-window: capacity=32: misdecodes 31
- SF-catchup: catch-up-hours=: misdecodes 13
- SF-catchup: faster: 1.11 s per simulated hour against 8.76 over 74 prior run(s) - 7.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: hops-apart=4: decode_failures 14
- SF-hops-spread: hops-apart=4: decode_failures 14
- SF-hops-spread: hops-apart=5: decode_failures 14
- SF-place-flat: place=spread: decode_failures 16
- SF-place-spread: place=spread: decode_failures 16
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 19
- SF-replay-order: replay-ordering=heard: misdecodes 17
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-spread: faster: 0.942 s per simulated hour against 2.19 over 74 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-window-size: window-size=8: misdecodes 88
- SF-window-size: window-size=16: misdecodes 64
- SF-window-size: window-size=32: misdecodes 31
- TH-congestion: no-congestion-scaling=True: queue drops 16.4% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 83

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-siting` | 5.24 | 1.49 | 3.52x | 74 |
| `PR-crladder` | 1.85 | 2.77 | 0.67x | 74 |
| `RF-stretch-duct` | 1.2 | 1.81 | 0.66x | 74 |
| `PR-repeats` | 1.01 | 1.57 | 0.64x | 74 |
| `AD-badrouters` | 1.14 | 1.78 | 0.64x | 74 |
| `RF-preset` | 1.78 | 2.78 | 0.64x | 74 |
| `SF-jitter-global` | 1.1 | 1.76 | 0.62x | 74 |
| `MS-oversubscribed` | 11.6 | 18.8 | 0.62x | 74 |
| `SF-hops-flat` | 2.34 | 3.98 | 0.59x | 74 |
| `RF-bw500` | 1.1 | 1.89 | 0.58x | 74 |
| `SF-resolve` | 0.854 | 1.51 | 0.57x | 74 |
| `RF-pulse` | 0.879 | 1.59 | 0.55x | 74 |
| `SF-capacity` | 0.931 | 1.7 | 0.55x | 74 |
| `LD-chatty` | 2.52 | 4.61 | 0.55x | 74 |
| `LD-traceroute` | 1.1 | 2.08 | 0.53x | 74 |
| `FW-signing-cost` | 0.797 | 1.51 | 0.53x | 74 |
| `SF-capacity-window` | 0.838 | 1.59 | 0.53x | 74 |
| `DM-mode` | 1.52 | 2.89 | 0.53x | 74 |
| `SF-place-spread` | 1.45 | 2.77 | 0.52x | 74 |
| `SF-servers-allrouters` | 0.956 | 1.83 | 0.52x | 74 |
| `RT-hopassign` | 0.893 | 1.75 | 0.51x | 74 |
| `SF-provide-transport` | 0.883 | 1.75 | 0.50x | 74 |
| `MS-stretch` | 1 | 2.1 | 0.48x | 74 |
| `SF-servers-spread` | 0.942 | 2.19 | 0.43x | 74 |
| `SF-cadence` | 1.35 | 3.61 | 0.37x | 74 |
| `SF-catchup` | 1.11 | 8.76 | 0.13x | 74 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.987 | 0.987 | 0.910 → 0.919 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.984 | 0.984 | 0.910 → 0.918 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.054 → 0.987 | 0.933 | 0.048 → 0.919 | 44x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.084 → 0.987 | 0.903 | 0.088 → 0.919 | 47x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.153 → 0.938 | 0.785 | 0.130 → 0.863 | 78x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.231 → 0.987 | 0.756 | 0.205 → 0.919 | 20x sr_bytes | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.149 → 0.888 | 0.739 | 0.145 → 0.881 | 3.9x sr_bytes | down | 3 |
| `MS-hopscale` | nodes | **text** | 0.305 → 0.920 | 0.616 | 0.298 → 0.919 | 18x sr_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.289 → 0.873 | 0.584 | 0.284 → 0.863 | 1.8x sr_airtime | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.452 → 0.978 | 0.526 | 0.445 → 0.978 | 2x sr_airtime | up | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.479 → 0.949 | 0.470 | 0.298 → 0.757 | 5x sr_bytes | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.488 → 0.920 | 0.432 | 0.485 → 0.919 | 2.2x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.488 → 0.920 | 0.432 | 0.485 → 0.919 | 3.4x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.595 → 0.948 | 0.353 | 0.586 → 0.947 | 2x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.604 → 0.920 | 0.316 | 0.578 → 0.919 | 3.3x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.660 → 0.956 | 0.296 | 0.645 → 0.955 | 9x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.629 → 0.920 | 0.291 | 0.594 → 0.919 | 3.9x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.654 → 0.929 | 0.274 | 0.638 → 0.928 | 6.9x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.396 → 0.641 | 0.245 | 0.329 → 0.521 | 5.5x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.588 → 0.829 | 0.241 | 0.576 → 0.814 | 1.7x sr_bytes | up | 2 |
| `MS-density` | nodes | **text** | 0.730 → 0.965 | 0.235 | 0.720 → 0.963 | 5.2x sr_airtime | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.736 → 0.965 | 0.229 | 0.728 → 0.963 | 5.4x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.732 → 0.920 | 0.189 | 0.719 → 0.919 | 8.1x sr_bytes | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.773 → 0.954 | 0.181 | 0.747 → 0.954 | 2.2x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.773 → 0.947 | 0.174 | 0.747 → 0.947 | 2.1x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.752 → 0.920 | 0.168 | 0.749 → 0.919 | 1.3x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.773 → 0.920 | 0.147 | 0.747 → 0.919 | 2.6x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.775 → 0.920 | 0.146 | 0.775 → 0.919 | 1.3x sr_airtime | down | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.854 → 0.949 | 0.095 | 0.848 → 0.947 | 2x bytes_on_air | up | 4 |
| `DG-loss` | extra-loss | **text** | 0.829 → 0.920 | 0.091 | 0.821 → 0.919 | 1.6x sr_bytes | down | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.754 → 0.838 | 0.084 | 0.638 → 0.720 | 1.4x sr_airtime | down | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.867 → 0.943 | 0.076 | 0.862 → 0.941 | 2x bytes_on_air | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.888 → 0.958 | 0.070 | 0.881 → 0.958 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.888 → 0.958 | 0.070 | 0.881 → 0.958 | 2.6x bytes_on_air | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.875 → 0.942 | 0.067 | 0.872 → 0.942 | 2.2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.876 → 0.942 | 0.066 | 0.873 → 0.942 | 2.2x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.882 → 0.943 | 0.060 | 0.878 → 0.942 | 5.2x sr_airtime | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.872 → 0.920 | 0.049 | 0.863 → 0.919 | 1.6x sr_bytes | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.908 → 0.953 | 0.045 | 0.904 → 0.952 | 1.4x sr_airtime | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.920 → 0.963 | 0.043 | 0.919 → 0.961 | 1.8x sr_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.622 → 0.659 | 0.038 | 0.516 → 0.551 | 1.5x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.883 → 0.920 | 0.037 | 0.880 → 0.919 | 1.5x sr_airtime | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.920 → 0.956 | 0.036 | 0.919 → 0.954 | 1.4x bytes_on_air | up | 3 |
| `SF-hops-flat` | hops-apart | **text** | 0.911 → 0.941 | 0.030 | 0.910 → 0.919 | 3.3x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.911 → 0.941 | 0.030 | 0.910 → 0.919 | 3.3x sr_bytes | up | 5 |
| `AD-worst` | role-placement | **text** | 0.737 → 0.766 | 0.029 | 0.726 → 0.762 | 1.3x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **text** | 0.888 → 0.913 | 0.025 | 0.881 → 0.911 | 1.2x sr_bytes | down | 2 |
| `SF-place-flat` | place | **text** | 0.916 → 0.940 | 0.025 | 0.914 → 0.919 | 3.8x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.916 → 0.940 | 0.025 | 0.914 → 0.919 | 3.8x sr_bytes | down | 6 |
| `AD-badrouters` | role-placement | **text** | 0.866 → 0.888 | 0.022 | 0.858 → 0.881 | 1.1x sr_airtime | down | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.918 → 0.940 | 0.022 | 0.917 → 0.939 | 1.1x sr_airtime | up | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.913 → 0.931 | 0.018 | 0.909 → 0.930 | 1.2x sr_airtime | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.920 → 0.938 | 0.018 | 0.919 → 0.937 | 3.4x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **text** | 0.905 → 0.920 | 0.015 | 0.901 → 0.919 | 13x advert_bytes | down | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.905 → 0.917 | 0.012 | 0.901 → 0.916 | 9.6x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.977 → 0.987 | 0.010 | 0.919 → 0.925 | 1.4x bytes_on_air | down | 4 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.910 → 0.920 | 0.010 | 0.909 → 0.919 | 2.6x sr_bytes | down | 4 |
| `SF-window-size` | window-size | **held** | 0.979 → 0.989 | 0.010 | 0.909 → 0.916 | 4.5x advert_bytes | down | 3 |
| `FW-versions` | profile | **held** | 0.987 → 0.996 | 0.010 | 0.919 → 0.926 | 3.1x bytes_on_air | down | 5 |
| `SF-capacity` | capacity | **text** | 0.915 → 0.924 | 0.009 | 0.912 → 0.922 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.915 → 0.924 | 0.009 | 0.912 → 0.922 | 5.3x advert_bytes | down | 5 |
| `SF-sr-retries` | sr-retries | **text** | 0.914 → 0.923 | 0.009 | 0.912 → 0.921 | 1.1x sr_airtime | up | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.977 → 0.984 | 0.007 | 0.902 → 0.908 | 1.1x sr_bytes | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.980 → 0.987 | 0.007 | 0.919 → 0.923 | 18x sr_airtime | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.899 → 0.905 | 0.006 | 0.899 → 0.905 | 1.1x sr_airtime | up | 3 |
| `SF-servers-flat` | servers | **text** | 0.914 → 0.920 | 0.006 | 0.908 → 0.919 | 6.6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **text** | 0.914 → 0.920 | 0.006 | 0.908 → 0.919 | 6.6x sr_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.914 → 0.920 | 0.006 | 0.913 → 0.919 | 1.2x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.914 → 0.920 | 0.006 | 0.913 → 0.919 | 1.2x sr_airtime | down | 4 |
| `SF-width` | short-id-bits | **text** | 0.915 → 0.921 | 0.006 | 0.913 → 0.919 | 3.1x advert_bytes | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.979 → 0.984 | 0.005 | 0.909 → 0.913 | 2.6x advert_bytes | down | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.982 → 0.987 | 0.005 | 0.914 → 0.919 | 1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.960 → 0.965 | 0.005 | 0.958 → 0.963 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.920 → 0.925 | 0.005 | 0.919 → 0.923 | 3.1x sr_airtime | up | 2 |
| `LD-diurnal` | diurnal | **held** | 0.982 → 0.987 | 0.004 | 0.916 → 0.920 | 1.3x sr_bytes | up | 3 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.902 → 0.905 | 0.004 | 0.902 → 0.905 | 1x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.916 → 0.920 | 0.004 | 0.912 → 0.918 | 2.2x sr_bytes | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.915 → 0.918 | 0.003 | 0.912 → 0.916 | 5.3x advert_bytes | up | 3 |
| `FW-firmware` | profile | **text** | 0.917 → 0.920 | 0.003 | 0.916 → 0.919 | 3x bytes_on_air | up | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.984 → 0.987 | 0.003 | 0.916 → 0.919 | 1.3x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.917 → 0.920 | 0.003 | 0.916 → 0.919 | 1.2x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.965 → 0.968 | 0.003 | 0.963 → 0.965 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.996 → 0.998 | 0.002 | 0.963 → 0.964 | 1x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.984 → 0.985 | 0.002 | 0.915 → 0.916 | 1.2x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **text** | 0.919 → 0.920 | 0.001 | 0.917 → 0.919 | 5.7x advert_bytes | = | 3 |

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
| none | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| sprinkled | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.961 | 0.961 | 0.782 | 1.28x | 18.9/27.2/30.0% | 1.9/5.3% | 3 |
| arms-race | 1 | 0.953 | 0.952 | 0.001 | - | - | 0.973 | 0.973 | 0.910 | 1.04x | 23.3/28.7/31.5% | 1.3/5.4% | 3 |

> amplifier-mix=sprinkled: misdecodes 1

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.1 | 1 | 0.927 | 0.923 | 0.004 | - | - | 0.981 | 0.984 | 0.739 | 1.20x | 19.6/26.2/29.3% | 1.8/5.0% | 3 |
| 0.3 | 1 | 0.963 | 0.961 | 0.002 | - | - | 0.997 | 0.997 | 0.894 | 0.93x | 20.9/26.8/28.7% | 1.1/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.888 | 0.881 | 0.007 | - | - | 0.987 | 0.990 | 0.496 | 1.14x | 17.2/24.3/28.7% | 1.9/5.1% | 3 |
| inverse | 1 | 0.866 | 0.858 | 0.008 | - | - | 0.979 | 0.980 | 0.630 | 1.09x | 15.0/20.3/24.1% | 2.0/4.1% | 3 |
| random | 1 | 0.868 | 0.860 | 0.008 | - | - | 0.966 | 0.971 | 0.673 | 1.16x | 16.2/22.2/25.7% | 1.9/5.3% | 3 |

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.888 | 0.881 | 0.007 | - | - | 0.987 | 0.990 | 0.496 | 1.14x | 17.2/24.3/28.7% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.958 | 0.958 | 0.001 | - | - | 0.995 | 0.995 | 0.824 | 2.92x | 38.1/47.6/49.8% | 4.8/5.4% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.888 | 0.881 | 0.007 | - | - | 0.987 | 0.990 | 0.496 | 1.14x | 17.2/24.3/28.7% | 1.9/5.1% | 3 |
| no-mute | 1 | 0.912 | 0.908 | 0.004 | - | - | 0.997 | 0.998 | 0.674 | 1.22x | 16.9/23.6/26.8% | 1.8/4.9% | 3 |
| all-routers | 1 | 0.958 | 0.958 | 0.001 | - | - | 0.995 | 0.995 | 0.824 | 2.92x | 38.1/47.6/49.8% | 4.8/5.4% | 3 |

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.888 | 0.881 | 0.007 | - | - | 0.987 | 0.990 | 0.496 | 1.14x | 17.2/24.3/28.7% | 1.9/5.1% | 3 |
| local-typical | 1 | 0.752 | 0.744 | 0.008 | - | - | 0.841 | 0.888 | 0.000 | 1.38x | 14.9/26.2/32.6% | 2.3/5.5% | 3 |
| basement-heavy | 1 | 0.149 | 0.145 | 0.004 | - | - | 0.392 | 0.393 | 0.000 | 0.78x | 2.1/11.7/17.7% | 0.7/4.3% | 3 |

> siting-mix=local-typical: decode_failures 44

> slower: 5.24 s per simulated hour against 1.49 over 74 prior run(s) - 3.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.766 | 0.762 | 0.004 | - | - | 0.908 | 0.908 | 0.000 | 2.33x | 16.5/29.1/37.0% | 1.7/5.3% | 3 |
| inverse | 1 | 0.737 | 0.726 | 0.010 | - | - | 0.906 | 0.906 | 0.000 | 2.23x | 14.3/24.4/30.7% | 1.7/3.3% | 3 |

> role-placement=degree: misdecodes 1

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.918 | 0.918 | 0.000 | - | - | 0 | 0.000 | 0.698 | 1.23x | 18.0/25.2/27.9% | 1.7/5.3% | 3 |
| sr | 1 | 0.922 | 0.910 | 0.012 | - | - | 0.984 | 0.988 | 0.692 | 1.26x | 18.4/25.7/28.4% | 1.7/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.875 | 0.872 | 0.003 | - | - | 0.942 | 0.942 | 0.685 | 3.23x | 42.5/60.9/66.0% | 4.2/10.8% | 3 |
| 100 | 1 | 0.942 | 0.942 | 0.000 | - | - | 0.980 | 0.980 | 0.794 | 1.57x | 21.8/32.6/36.1% | 1.9/5.5% | 3 |
| 120 | 1 | 0.942 | 0.942 | 0.000 | - | - | 0.980 | 0.980 | 0.794 | 1.57x | 21.8/32.6/36.1% | 1.9/5.5% | 3 |
| 250 | 1 | 0.942 | 0.942 | 0.000 | - | - | 0.980 | 0.980 | 0.794 | 1.57x | 21.8/32.6/36.1% | 1.9/5.5% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.333 | 0.329 | 0.004 | - | - | 0.396 | 0.399 | 0.173 | 11.16x | 39.1/58.5/73.8% | 3.9/11.2% | 3 |
| 120 | 1 | 0.522 | 0.516 | 0.006 | - | - | 0.622 | 0.622 | 0.226 | 4.41x | 15.6/26.0/37.1% | 1.5/4.8% | 3 |
| 250 | 1 | 0.529 | 0.521 | 0.007 | - | - | 0.641 | 0.643 | 0.229 | 4.28x | 15.2/25.1/35.8% | 1.4/4.7% | 3 |

> max-num-nodes=10: decode_failures 15

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.942 | 0.942 | 0.000 | - | - | 0.980 | 0.980 | 0.794 | 1.57x | 21.8/32.6/36.1% | 1.9/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.942 | 0.942 | 0.000 | - | - | 0.980 | 0.980 | 0.794 | 1.57x | 21.8/32.6/36.1% | 1.9/5.5% | 3 |
| constrained | 1 | 0.876 | 0.873 | 0.003 | - | - | 0.939 | 0.940 | 0.667 | 3.22x | 42.3/60.8/65.9% | 4.2/10.8% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.838 | 0.893 | 0.523 | 5.50x | 59.3/76.0/78.9% | 3.9/12.9% | 3 |
| 25 | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.838 | 0.893 | 0.523 | 5.50x | 59.3/76.0/78.9% | 3.9/12.9% | 3 |
| 100 | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.838 | 0.893 | 0.523 | 5.50x | 59.3/76.0/78.9% | 3.9/12.9% | 3 |
| 2000 | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.838 | 0.893 | 0.523 | 5.50x | 59.3/76.0/78.9% | 3.9/12.9% | 3 |

> warm-num-nodes=0: queue drops 17.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 104

> warm-num-nodes=25: queue drops 17.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 104

> warm-num-nodes=100: queue drops 17.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 104

> warm-num-nodes=2000: queue drops 17.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 104

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.1 | 1 | 0.820 | 0.809 | 0.011 | - | - | 0.975 | 0.975 | 0.577 | 1.23x | 17.7/25.1/27.9% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.725 | 0.699 | 0.026 | - | - | 0.936 | 0.943 | 0.482 | 1.11x | 16.3/23.3/25.7% | 1.6/4.3% | 3 |
| 0.3 | 1 | 0.629 | 0.594 | 0.036 | - | - | 0.887 | 0.918 | 0.340 | 1.06x | 15.7/22.7/25.0% | 1.6/3.9% | 3 |

> burst-loss=0.2: decode_failures 1

> burst-loss=0.3: decode_failures 29

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.1 | 1 | 0.899 | 0.896 | 0.003 | - | - | 0.983 | 0.984 | 0.650 | 1.36x | 19.8/27.6/29.9% | 1.9/5.3% | 3 |
| 0.2 | 1 | 0.865 | 0.860 | 0.006 | - | - | 0.980 | 0.980 | 0.573 | 1.44x | 20.6/29.0/31.1% | 2.1/5.2% | 3 |
| 0.3 | 1 | 0.829 | 0.821 | 0.008 | - | - | 0.966 | 0.968 | 0.501 | 1.44x | 20.6/29.2/31.5% | 2.1/4.9% | 3 |

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.1 | 1 | 0.821 | 0.811 | 0.010 | - | - | 0.970 | 0.979 | 0.599 | 1.21x | 17.6/24.9/27.7% | 1.7/5.0% | 3 |
| 0.2 | 1 | 0.712 | 0.693 | 0.018 | - | - | 0.917 | 0.969 | 0.481 | 1.14x | 16.6/23.8/26.3% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.604 | 0.578 | 0.026 | - | - | 0.792 | 0.881 | 0.394 | 1.11x | 16.1/23.4/26.0% | 1.6/4.5% | 3 |

> burst-loss=0.1: decode_failures 11

> burst-loss=0.2: decode_failures 28

> burst-loss=0.3: decode_failures 31

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.899 | 0.899 | 0.000 | - | - | 0.979 | 0.980 | 0.673 | 1.64x | 23.7/33.1/36.8% | 2.2/7.1% | 3 |
| directed-with-late-flood | 1 | 0.905 | 0.905 | 0.000 | - | - | 0.978 | 0.981 | 0.652 | 1.48x | 21.7/30.6/34.0% | 2.1/6.4% | 3 |
| m4-early-flood | 1 | 0.899 | 0.899 | 0.000 | - | - | 0.973 | 0.973 | 0.660 | 1.49x | 21.7/30.6/34.1% | 2.1/6.5% | 3 |

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.917 | 0.916 | 0.002 | - | - | 0.986 | 0.987 | 0.604 | 0.75x | 10.0/12.8/14.0% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.25 | 1 | 0.867 | 0.862 | 0.005 | - | - | 0.961 | 0.961 | 0.634 | 1.18x | 15.9/24.5/26.4% | 1.8/4.5% | 3 |
| 0.5 | 1 | 0.900 | 0.897 | 0.003 | - | - | 0.974 | 0.975 | 0.682 | 1.02x | 13.5/18.1/20.8% | 1.6/4.1% | 3 |
| 0.75 | 1 | 0.943 | 0.941 | 0.002 | - | - | 0.989 | 0.989 | 0.831 | 0.89x | 12.4/17.1/19.7% | 1.4/3.8% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.25 | 1 | 0.854 | 0.848 | 0.005 | - | - | 0.939 | 0.940 | 0.625 | 1.15x | 15.6/23.4/25.5% | 1.8/4.4% | 3 |
| 0.5 | 1 | 0.896 | 0.894 | 0.002 | - | - | 0.966 | 0.967 | 0.683 | 0.98x | 13.2/18.0/20.7% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.949 | 0.947 | 0.002 | - | - | 0.993 | 0.993 | 0.842 | 0.87x | 12.3/16.9/19.8% | 1.3/3.8% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.938 | 0.937 | 0.001 | - | - | 0.994 | 0.994 | 0.724 | 0.66x | 9.9/14.4/16.2% | 0.9/3.0% | 3 |
| signing=true | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.921 | 0.919 | 0.002 | - | - | 0.996 | 0.997 | 0.606 | 0.76x | 10.6/14.5/16.1% | 1.2/2.5% | 3 |
| 2.5 | 1 | 0.925 | 0.924 | 0.001 | - | - | 0.993 | 0.994 | 0.587 | 0.76x | 10.6/14.2/15.9% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.926 | 0.925 | 0.001 | - | - | 0.993 | 0.994 | 0.623 | 0.72x | 10.1/13.9/15.6% | 1.1/2.4% | 3 |
| 2.7 | 1 | 0.927 | 0.926 | 0.001 | - | - | 0.990 | 0.991 | 0.650 | 0.77x | 11.3/16.5/18.5% | 1.1/3.2% | 3 |
| 2.8 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.929 | 0.928 | 0.001 | - | - | 0.986 | 0.986 | 0.731 | 0.82x | 11.9/16.7/18.6% | 1.1/3.5% | 3 |
| 900 | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.969 | 0.969 | 0.638 | 2.02x | 29.1/40.6/44.9% | 2.8/8.6% | 3 |
| 300 | 1 | 0.654 | 0.638 | 0.016 | - | - | 0.843 | 0.859 | 0.375 | 4.36x | 58.1/73.4/76.6% | 6.2/16.0% | 3 |

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.993 | 0.993 | 0.851 | 0.89x | 12.6/17.4/19.0% | 1.2/3.5% | 3 |
| 900 | 1 | 0.927 | 0.925 | 0.002 | - | - | 0.981 | 0.982 | 0.789 | 2.32x | 32.7/44.2/47.4% | 3.3/8.9% | 3 |
| 300 | 1 | 0.660 | 0.645 | 0.015 | - | - | 0.825 | 0.831 | 0.459 | 4.85x | 61.8/75.5/78.4% | 7.2/16.9% | 3 |

> broadcast-interval-s=3600: misdecodes 1

> broadcast-interval-s=300: queue drops 15.6% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 2

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.982 | 0.982 | 0.700 | 1.16x | 16.7/23.6/26.2% | 1.6/5.0% | 3 |
| sinusoid | 1 | 0.922 | 0.920 | 0.001 | - | - | 0.984 | 0.984 | 0.697 | 1.15x | 16.7/23.4/25.8% | 1.6/4.9% | 3 |
| commuter | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.882 | 0.878 | 0.004 | - | - | 0.969 | 0.969 | 0.638 | 2.02x | 29.1/40.6/44.9% | 2.8/8.6% | 3 |
| 3600 | 1 | 0.929 | 0.928 | 0.001 | - | - | 0.986 | 0.986 | 0.731 | 0.82x | 11.9/16.7/18.6% | 1.1/3.5% | 3 |
| 10800 | 1 | 0.941 | 0.941 | 0.001 | - | - | 0.992 | 0.992 | 0.767 | 0.54x | 7.7/10.7/12.0% | 0.7/2.2% | 3 |
| 43200 | 1 | 0.943 | 0.942 | 0.001 | - | - | 0.991 | 0.991 | 0.773 | 0.39x | 5.5/7.8/8.6% | 0.5/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.25 | 1 | 0.916 | 0.914 | 0.002 | - | - | 0.985 | 0.986 | 0.677 | 1.31x | 19.1/26.9/30.0% | 1.8/5.7% | 3 |
| 1.0 | 1 | 0.910 | 0.907 | 0.003 | - | - | 0.984 | 0.984 | 0.680 | 1.46x | 21.3/30.0/33.3% | 2.0/6.4% | 3 |
| 4.0 | 1 | 0.883 | 0.880 | 0.003 | - | - | 0.973 | 0.973 | 0.626 | 1.85x | 27.2/38.7/43.3% | 2.6/8.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.838 | 0.893 | 0.523 | 5.50x | 59.3/76.0/78.9% | 3.9/12.9% | 3 |
| 1.0 | 1 | 0.643 | 0.638 | 0.005 | - | - | 0.754 | 0.835 | 0.461 | 6.04x | 63.7/77.8/80.1% | 4.5/14.7% | 3 |

> traceroute-per-hour=0.0: queue drops 17.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 104

> traceroute-per-hour=1.0: queue drops 26.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 102

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.730 | 0.720 | 0.011 | - | - | 0.783 | 0.895 | 0.338 | 1.36x | 22.2/33.3/34.9% | 3.2/7.0% | 3 |
| 60 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 90 | 1 | 0.950 | 0.947 | 0.003 | - | - | 0.997 | 0.998 | 0.743 | 1.53x | 18.6/26.9/31.4% | 1.4/4.9% | 3 |
| 120 | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.996 | 0.997 | 0.797 | 2.02x | 23.7/38.9/42.6% | 1.3/5.0% | 3 |
| 150 | 1 | 0.958 | 0.955 | 0.003 | - | - | 0.998 | 0.998 | 0.771 | 2.47x | 27.0/44.5/50.3% | 1.3/5.3% | 3 |

> nodes=40: decode_failures 12

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 120 | 1 | 0.764 | 0.757 | 0.007 | - | - | 0.943 | 0.944 | 0.444 | 2.25x | 14.9/29.2/34.7% | 1.6/5.1% | 3 |
| 250 | 1 | 0.521 | 0.515 | 0.007 | - | - | 0.621 | 0.621 | 0.240 | 4.71x | 16.7/27.9/38.5% | 1.6/5.3% | 3 |
| 500 | 1 | 0.305 | 0.298 | 0.006 | - | - | 0.487 | 0.493 | 0.115 | 9.85x | 18.2/26.6/48.6% | 1.7/6.8% | 3 |

> nodes=500: decode_failures 147

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.765 | 0.757 | 0.008 | - | - | 0.949 | 0.949 | 0.413 | 2.09x | 13.9/26.9/31.9% | 1.5/4.7% | 3 |
| 250 | 1 | 0.522 | 0.516 | 0.006 | - | - | 0.622 | 0.622 | 0.226 | 4.41x | 15.6/26.0/37.1% | 1.5/4.8% | 3 |
| 500 | 1 | 0.304 | 0.298 | 0.006 | - | - | 0.479 | 0.480 | 0.117 | 9.36x | 17.2/25.9/45.7% | 1.6/6.1% | 3 |

> nodes=500: decode_failures 33

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.913 | 0.911 | 0.002 | - | - | 0.998 | 0.998 | 0.638 | 1.28x | 18.5/26.0/29.0% | 1.8/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.888 | 0.881 | 0.007 | - | - | 0.987 | 0.990 | 0.496 | 1.14x | 17.2/24.3/28.7% | 1.9/5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.931 | 0.930 | 0.002 | - | - | 0.997 | 0.998 | 0.684 | 1.32x | 19.2/26.7/29.1% | 1.8/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.913 | 0.909 | 0.004 | - | - | 0.986 | 0.989 | 0.573 | 1.36x | 19.6/28.9/34.1% | 2.5/5.4% | 3 |

> role-mix=legacy-default: misdecodes 1

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.05 | 1 | 0.923 | 0.922 | 0.001 | - | - | 0.987 | 0.987 | 0.680 | 1.39x | 19.3/31.5/34.7% | 1.8/5.5% | 3 |
| 0.1 | 1 | 0.924 | 0.923 | 0.001 | - | - | 0.977 | 0.977 | 0.755 | 1.53x | 21.7/34.0/38.9% | 1.9/5.5% | 3 |
| 0.2 | 1 | 0.926 | 0.925 | 0.001 | - | - | 0.977 | 0.977 | 0.746 | 1.71x | 24.3/38.4/45.1% | 2.1/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| local-typical | 1 | 0.776 | 0.772 | 0.004 | - | - | 0.878 | 0.878 | 0.000 | 1.65x | 16.1/27.4/34.2% | 2.5/5.6% | 3 |
| event | 1 | 0.452 | 0.445 | 0.007 | - | - | 0.665 | 0.665 | 0.000 | 1.62x | 9.5/19.9/28.1% | 2.4/5.4% | 3 |
| backbone | 1 | 0.978 | 0.978 | 0.000 | - | - | 0.998 | 0.998 | 0.929 | 1.07x | 29.1/36.5/37.9% | 1.2/5.7% | 3 |

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.863 | 0.851 | 0.012 | - | - | 0.945 | 0.948 | 0.639 | 1.44x | 29.3/39.6/42.9% | 3.3/7.8% | 3 |
| 60 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 90 | 1 | 0.855 | 0.849 | 0.006 | - | - | 0.966 | 0.967 | 0.661 | 1.71x | 15.6/26.0/31.1% | 1.6/4.7% | 3 |
| 120 | 1 | 0.764 | 0.757 | 0.007 | - | - | 0.943 | 0.944 | 0.444 | 2.25x | 14.9/29.2/34.7% | 1.6/5.1% | 3 |
| 150 | 1 | 0.732 | 0.719 | 0.013 | - | - | 0.959 | 0.961 | 0.410 | 2.81x | 15.3/29.2/37.9% | 1.6/5.0% | 3 |

> nodes=150: decode_failures 1

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 1.25 | 1 | 0.742 | 0.740 | 0.002 | - | - | 0.912 | 0.913 | 0.258 | 1.37x | 15.4/21.4/25.7% | 2.0/5.5% | 3 |
| 1.5 | 1 | 0.588 | 0.576 | 0.012 | - | - | 0.874 | 0.876 | 0.099 | 1.43x | 11.8/20.3/25.6% | 2.0/6.1% | 3 |
| 2.0 | 1 | 0.205 | 0.205 | 0.000 | - | - | 0.231 | 0.461 | 0.000 | 1.32x | 6.5/13.4/20.3% | 2.1/5.3% | 2 |

> stretch=2.0: 3 archives requested, 2 placed - group on the placed count

> faster: 1 s per simulated hour against 2.1 over 74 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| clustered | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.963 | 0.966 | 0.503 | 1.01x | 33.2/37.4/38.8% | 0.9/5.6% | 3 |
| corridor | 1 | 0.595 | 0.586 | 0.009 | - | - | 0.806 | 0.811 | 0.208 | 1.25x | 12.7/28.8/32.5% | 1.7/5.3% | 3 |
| hub | 1 | 0.948 | 0.947 | 0.001 | - | - | 0.977 | 0.977 | 0.868 | 1.26x | 29.0/38.6/40.1% | 1.6/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.905 | 0.905 | 0.000 | - | - | 0.978 | 0.981 | 0.652 | 1.48x | 21.7/30.6/34.0% | 2.1/6.4% | 3 |
| True | 1 | 0.902 | 0.902 | 0.000 | - | - | 0.977 | 0.977 | 0.669 | 1.48x | 21.6/30.4/33.8% | 2.1/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.902 | 0.902 | 0.000 | - | - | 0.977 | 0.977 | 0.669 | 1.48x | 21.6/30.4/33.8% | 2.1/6.5% | 3 |
| m4-early-flood | 1 | 0.908 | 0.908 | 0.000 | - | - | 0.984 | 0.984 | 0.668 | 1.49x | 21.8/30.7/34.0% | 2.1/6.5% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.918 | 0.918 | 0.000 | - | - | 0 | 0.000 | 0.698 | 1.23x | 18.0/25.2/27.9% | 1.7/5.3% | 3 |
| chain | 1 | 0.912 | 0.910 | 0.001 | - | - | 0.971 | 0.984 | 0.695 | 1.43x | 20.5/29.0/32.6% | 1.9/6.2% | 3 |
| sr | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| True | 1 | 0.916 | 0.914 | 0.002 | - | - | 0.982 | 0.982 | 0.686 | 1.26x | 18.3/25.7/28.6% | 1.8/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.996 | 0.997 | 0.797 | 2.02x | 23.7/38.9/42.6% | 1.3/5.0% | 3 |
| True | 1 | 0.967 | 0.964 | 0.002 | - | - | 0.998 | 0.998 | 0.786 | 2.05x | 24.0/39.1/42.9% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.289 | 0.284 | 0.005 | - | - | 0.594 | 0.605 | 0.000 | 0.07x | 0.4/0.9/1.2% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.628 | 0.624 | 0.004 | - | - | 0.903 | 0.905 | 0.138 | 0.32x | 2.8/5.5/6.2% | 0.4/1.4% | 3 |
| LONG_TURBO | 1 | 0.873 | 0.863 | 0.009 | - | - | 0.977 | 0.977 | 0.595 | 1.34x | 14.8/23.4/27.8% | 2.1/5.2% | 3 |

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 0.25 | 1 | 0.926 | 0.925 | 0.001 | - | - | 0.986 | 0.986 | 0.734 | 1.22x | 20.0/27.0/29.9% | 1.6/5.5% | 3 |
| 1.0 | 1 | 0.956 | 0.954 | 0.003 | - | - | 0.994 | 0.994 | 0.864 | 0.91x | 25.6/31.4/33.0% | 1.0/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.488 | 0.485 | 0.003 | - | - | 0.664 | 0.669 | 0.054 | 0.18x | 1.3/2.8/4.0% | 0.2/0.8% | 3 |
| LONG_FAST | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| LITE_FAST | 1 | 0.868 | 0.867 | 0.002 | - | - | 0.967 | 0.968 | 0.560 | 0.98x | 12.4/18.6/23.3% | 1.4/4.2% | 3 |
| NARROW_SLOW | 1 | 0.896 | 0.893 | 0.002 | - | - | 0.980 | 0.980 | 0.689 | 1.31x | 17.1/25.5/30.1% | 1.9/5.4% | 3 |

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| temporal | 1 | 0.851 | 0.847 | 0.005 | - | - | 0.965 | 0.966 | 0.566 | 1.30x | 18.7/25.8/28.3% | 1.9/5.3% | 3 |
| transient | 1 | 0.916 | 0.915 | 0.001 | - | - | 0.982 | 0.982 | 0.695 | 1.27x | 18.3/25.6/28.5% | 1.7/5.4% | 3 |
| periodic | 1 | 0.752 | 0.749 | 0.003 | - | - | 0.826 | 0.827 | 0.513 | 1.17x | 17.2/24.0/26.0% | 1.6/4.6% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.488 | 0.485 | 0.003 | - | - | 0.664 | 0.669 | 0.054 | 0.18x | 1.3/2.8/4.0% | 0.2/0.8% | 3 |
| LONG_FAST | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| LONG_MODERATE | 1 | 0.876 | 0.868 | 0.008 | - | - | 0.944 | 0.948 | 0.732 | 3.44x | 53.8/68.2/69.8% | 4.9/12.9% | 3 |

> preset=LONG_MODERATE: decode_failures 1

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.048 | 0.048 | 0.000 | - | - | 0.054 | 0.162 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.289 | 0.284 | 0.005 | - | - | 0.594 | 0.605 | 0.000 | 0.07x | 0.4/0.9/1.2% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| LONG_TURBO | 1 | 0.873 | 0.863 | 0.009 | - | - | 0.977 | 0.977 | 0.595 | 1.34x | 14.8/23.4/27.8% | 2.1/5.2% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.898 | 0.895 | 0.003 | - | - | 0.976 | 0.977 | 0.666 | 1.76x | 23.2/33.7/38.4% | 2.5/7.4% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.866 | 0.863 | 0.002 | - | - | 0.938 | 0.939 | 0.635 | 1.24x | 18.2/25.5/28.1% | 1.8/5.2% | 3 |
| 10000 | 1 | 0.752 | 0.749 | 0.003 | - | - | 0.826 | 0.827 | 0.513 | 1.17x | 17.2/24.0/26.0% | 1.6/4.6% | 3 |
| 4000 | 1 | 0.521 | 0.516 | 0.004 | - | - | 0.599 | 0.610 | 0.312 | 1.08x | 15.5/22.2/23.8% | 1.6/3.8% | 3 |
| 2000 | 1 | 0.130 | 0.130 | 0.000 | - | - | 0.153 | 0.215 | 0.058 | 0.75x | 11.0/16.0/18.0% | 1.1/2.2% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.588 | 0.576 | 0.012 | - | - | 0.874 | 0.876 | 0.099 | 1.43x | 11.8/20.3/25.6% | 2.0/6.1% | 3 |
| 1.0 | 1 | 0.829 | 0.814 | 0.015 | - | - | 0.951 | 0.954 | 0.592 | 1.07x | 17.4/22.2/26.6% | 1.4/5.2% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 22 | 1 | 0.587 | 0.577 | 0.009 | - | - | 0.866 | 0.867 | 0.138 | 1.42x | 12.2/21.4/26.4% | 2.0/5.7% | 3 |
| 17 | 1 | 0.253 | 0.247 | 0.007 | - | - | 0.512 | 0.529 | 0.000 | 1.35x | 7.1/15.4/20.0% | 2.1/5.5% | 3 |
| 14 | 1 | 0.088 | 0.088 | 0.000 | - | - | 0.084 | 0.244 | 0.000 | 0.89x | 3.6/8.3/13.7% | 1.4/4.1% | 3 |

> tx-power=17: decode_failures 4

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.996 | 0.997 | 0.797 | 2.02x | 23.7/38.9/42.6% | 1.3/5.0% | 3 |
| True | 1 | 0.960 | 0.958 | 0.003 | - | - | 0.996 | 0.997 | 0.794 | 2.35x | 26.9/43.3/47.0% | 1.5/5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.918 | 0.917 | 0.001 | - | - | 0.982 | 0.982 | 0.727 | 1.37x | 18.9/29.1/32.6% | 1.7/5.5% | 3 |
| True | 1 | 0.940 | 0.939 | 0.001 | - | - | 0.986 | 0.986 | 0.801 | 1.43x | 19.5/29.7/32.8% | 1.8/5.5% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| random | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.966 | 0.967 | 0.635 | 1.22x | 17.7/25.0/27.9% | 1.7/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.773 | 0.747 | 0.026 | - | - | 0.968 | 0.973 | 0.443 | 0.93x | 14.3/20.6/24.0% | 1.3/4.5% | 3 |
| 7 | 1 | 0.947 | 0.947 | 0.000 | - | - | 0.989 | 0.990 | 0.802 | 1.37x | 19.5/26.8/29.4% | 1.9/5.5% | 3 |
| 15 | 1 | 0.954 | 0.954 | 0.001 | - | - | 0.986 | 0.987 | 0.850 | 1.41x | 20.1/27.6/29.9% | 2.0/5.5% | 3 |
| 32 | 1 | 0.954 | 0.954 | 0.001 | - | - | 0.986 | 0.987 | 0.850 | 1.41x | 20.1/27.6/29.9% | 2.0/5.5% | 3 |

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.773 | 0.747 | 0.026 | - | - | 0.968 | 0.973 | 0.443 | 0.93x | 14.3/20.6/24.0% | 1.3/4.5% | 3 |
| 5 | 1 | 0.901 | 0.897 | 0.004 | - | - | 0.984 | 0.984 | 0.663 | 1.27x | 18.5/25.8/28.5% | 1.8/5.3% | 3 |
| 7 | 1 | 0.947 | 0.947 | 0.000 | - | - | 0.989 | 0.990 | 0.802 | 1.37x | 19.5/26.8/29.4% | 1.9/5.5% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.923 | 0.923 | 0.000 | - | - | 0.980 | 0.991 | 0.705 | 1.25x | 18.2/25.5/28.1% | 1.7/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.773 | 0.747 | 0.026 | - | - | 0.968 | 0.973 | 0.443 | 0.93x | 14.3/20.6/24.0% | 1.3/4.5% | 3 |
| True | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| BALANCED | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| STRICT | 1 | 0.775 | 0.775 | 0.000 | - | - | 0.845 | 0.845 | 0.537 | 1.35x | 19.3/27.2/29.9% | 1.9/5.6% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| dm | 1 | 0.925 | 0.923 | 0.001 | - | - | 0.991 | 0.992 | 0.717 | 1.25x | 18.2/25.5/28.5% | 1.8/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.916 | 0.915 | 0.001 | - | - | 0.985 | 0.986 | 0.690 | 1.26x | 18.4/25.7/28.5% | 1.7/5.4% | 3 |
| local | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| time | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.984 | 0.984 | 0.700 | 1.32x | 19.0/26.7/29.7% | 1.9/5.6% | 3 |
| window | 1 | 0.910 | 0.909 | 0.001 | - | - | 0.979 | 0.979 | 0.687 | 1.27x | 18.4/25.8/28.5% | 1.8/5.4% | 3 |

> bucket-mode=global: misdecodes 17

> bucket-mode=time: misdecodes 43

> bucket-mode=window: misdecodes 31

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.915 | 0.912 | 0.002 | - | - | 0.985 | 0.985 | 0.687 | 1.38x | 19.6/27.8/31.2% | 1.9/5.9% | 3 |
| 1800 | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.984 | 0.984 | 0.700 | 1.32x | 19.0/26.7/29.7% | 1.9/5.6% | 3 |
| 3600 | 1 | 0.917 | 0.915 | 0.002 | - | - | 0.986 | 0.986 | 0.705 | 1.28x | 18.6/25.9/28.8% | 1.7/5.5% | 3 |

> time-bucket-s=600: misdecodes 93

> time-bucket-s=1800: misdecodes 43

> time-bucket-s=3600: misdecodes 14

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| interval | 1 | 0.910 | 0.908 | 0.002 | - | - | 0.984 | 0.985 | 0.675 | 1.59x | 22.9/33.0/36.6% | 2.2/6.9% | 3 |
| aimd | 1 | 0.917 | 0.917 | 0.000 | - | - | 0.977 | 0.987 | 0.715 | 1.27x | 18.5/25.8/28.6% | 1.7/5.4% | 3 |
| bucket+interval | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.984 | 0.984 | 0.673 | 1.61x | 23.3/33.7/37.1% | 2.2/7.1% | 3 |

> trigger=interval: misdecodes 14

> trigger=aimd: misdecodes 10

> trigger=bucket+interval: misdecodes 13

> faster: 1.35 s per simulated hour against 3.61 over 74 prior run(s) - 2.7x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.985 | 0.985 | 0.700 | 1.27x | 18.5/25.8/28.6% | 1.8/5.4% | 3 |
| 8 | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.986 | 0.986 | 0.703 | 1.27x | 18.4/25.9/28.6% | 1.7/5.4% | 3 |
| 16 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.990 | 0.990 | 0.713 | 1.26x | 18.2/25.6/28.4% | 1.7/5.4% | 3 |
| 32 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 50 | 1 | 0.915 | 0.912 | 0.002 | - | - | 0.983 | 0.983 | 0.690 | 1.28x | 18.6/26.0/28.9% | 1.8/5.5% | 3 |

> capacity=4: decode_failures 14

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.985 | 0.985 | 0.700 | 1.27x | 18.5/25.8/28.6% | 1.8/5.4% | 3 |
| 8 | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.986 | 0.986 | 0.703 | 1.27x | 18.4/25.9/28.6% | 1.7/5.4% | 3 |
| 16 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.990 | 0.990 | 0.713 | 1.26x | 18.2/25.6/28.4% | 1.7/5.4% | 3 |
| 32 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 50 | 1 | 0.915 | 0.912 | 0.002 | - | - | 0.983 | 0.983 | 0.690 | 1.28x | 18.6/26.0/28.9% | 1.8/5.5% | 3 |

> capacity=4: decode_failures 14

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.914 | 0.913 | 0.002 | - | - | 0.984 | 0.984 | 0.691 | 1.25x | 18.3/25.7/28.5% | 1.7/5.4% | 3 |
| 16 | 1 | 0.914 | 0.913 | 0.002 | - | - | 0.983 | 0.983 | 0.700 | 1.24x | 18.1/25.5/28.1% | 1.7/5.3% | 3 |
| 32 | 1 | 0.910 | 0.909 | 0.001 | - | - | 0.979 | 0.979 | 0.687 | 1.27x | 18.4/25.8/28.5% | 1.8/5.4% | 3 |

> capacity=8: misdecodes 34

> capacity=16: misdecodes 35

> capacity=32: misdecodes 31

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.984 | 0.984 | 0.673 | 1.61x | 23.3/33.7/37.1% | 2.2/7.1% | 3 |
| 02-06 | 1 | 0.915 | 0.915 | 0.001 | - | - | 0.975 | 0.982 | 0.692 | 1.26x | 18.3/25.8/28.8% | 1.8/5.5% | 3 |
| 00-08 | 1 | 0.917 | 0.916 | 0.001 | - | - | 0.978 | 0.983 | 0.696 | 1.30x | 18.8/26.5/29.7% | 1.8/5.6% | 3 |

> catch-up-hours=: misdecodes 13

> faster: 1.11 s per simulated hour against 8.76 over 74 prior run(s) - 7.9x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.911 | 0.910 | 0.001 | - | - | 0.979 | 0.979 | 0.686 | 1.26x | 18.3/25.8/28.5% | 1.7/5.4% | 3 |
| 2 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 3 | 1 | 0.922 | 0.910 | 0.012 | - | - | 0.984 | 0.988 | 0.692 | 1.26x | 18.4/25.7/28.4% | 1.7/5.3% | 3 |
| 4 | 1 | 0.941 | 0.919 | 0.022 | - | - | 0.964 | 0.993 | 0.682 | 1.30x | 18.9/26.4/29.3% | 1.8/5.4% | 3 |

> hops-apart=4: decode_failures 14

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.911 | 0.910 | 0.001 | - | - | 0.979 | 0.979 | 0.686 | 1.26x | 18.3/25.8/28.5% | 1.7/5.4% | 3 |
| 2 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 3 | 1 | 0.922 | 0.910 | 0.012 | - | - | 0.984 | 0.988 | 0.692 | 1.26x | 18.4/25.7/28.4% | 1.7/5.3% | 3 |
| 4 | 1 | 0.941 | 0.919 | 0.022 | - | - | 0.964 | 0.993 | 0.682 | 1.30x | 18.9/26.4/29.3% | 1.8/5.4% | 3 |
| 5 | 1 | 0.941 | 0.919 | 0.022 | - | - | 0.964 | 0.993 | 0.682 | 1.30x | 18.9/26.4/29.3% | 1.8/5.4% | 3 |

> hops-apart=4: decode_failures 14

> hops-apart=5: decode_failures 14

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.917 | 0.915 | 0.001 | - | - | 0.984 | 0.984 | 0.700 | 1.27x | 18.5/25.9/28.6% | 1.7/5.4% | 3 |
| 30 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 120 | 1 | 0.917 | 0.915 | 0.002 | - | - | 0.982 | 0.982 | 0.705 | 1.26x | 18.3/25.7/28.6% | 1.8/5.4% | 3 |
| 600 | 1 | 0.914 | 0.913 | 0.001 | - | - | 0.981 | 0.981 | 0.681 | 1.28x | 18.6/26.1/28.9% | 1.8/5.5% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.917 | 0.915 | 0.001 | - | - | 0.984 | 0.984 | 0.700 | 1.27x | 18.5/25.9/28.6% | 1.7/5.4% | 3 |
| 30 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 120 | 1 | 0.917 | 0.915 | 0.002 | - | - | 0.982 | 0.982 | 0.705 | 1.26x | 18.3/25.7/28.6% | 1.8/5.4% | 3 |
| 600 | 1 | 0.914 | 0.913 | 0.001 | - | - | 0.981 | 0.981 | 0.681 | 1.28x | 18.6/26.1/28.9% | 1.8/5.5% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.940 | 0.914 | 0.026 | - | - | 0.969 | 0.985 | 0.713 | 1.31x | 18.8/26.3/29.2% | 1.8/5.5% | 3 |
| routers | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.985 | 0.987 | 0.710 | 1.28x | 18.6/26.2/28.9% | 1.8/5.4% | 3 |
| alternate-routers | 1 | 0.916 | 0.915 | 0.001 | - | - | 0.982 | 0.982 | 0.692 | 1.29x | 18.7/26.2/29.1% | 1.8/5.5% | 3 |
| beside-router | 1 | 0.916 | 0.914 | 0.001 | - | - | 0.982 | 0.982 | 0.695 | 1.27x | 18.4/25.9/28.8% | 1.8/5.4% | 3 |
| random-clients | 1 | 0.919 | 0.918 | 0.002 | - | - | 0.984 | 0.984 | 0.703 | 1.28x | 18.6/26.2/29.0% | 1.8/5.5% | 3 |
| hops-apart | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

> place=spread: decode_failures 16

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.940 | 0.914 | 0.026 | - | - | 0.969 | 0.985 | 0.713 | 1.31x | 18.8/26.3/29.2% | 1.8/5.5% | 3 |
| routers | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.985 | 0.987 | 0.710 | 1.28x | 18.6/26.2/28.9% | 1.8/5.4% | 3 |
| alternate-routers | 1 | 0.916 | 0.915 | 0.001 | - | - | 0.982 | 0.982 | 0.692 | 1.29x | 18.7/26.2/29.1% | 1.8/5.5% | 3 |
| beside-router | 1 | 0.916 | 0.914 | 0.001 | - | - | 0.982 | 0.982 | 0.695 | 1.27x | 18.4/25.9/28.8% | 1.8/5.4% | 3 |
| random-clients | 1 | 0.919 | 0.918 | 0.002 | - | - | 0.984 | 0.984 | 0.703 | 1.28x | 18.6/26.2/29.0% | 1.8/5.5% | 3 |
| hops-apart | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

> place=spread: decode_failures 16

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| broadcast | 1 | 0.922 | 0.916 | 0.006 | - | - | 0.984 | 0.984 | 0.713 | 1.30x | 18.7/26.3/29.3% | 1.8/5.5% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| heard | 1 | 0.917 | 0.916 | 0.001 | - | - | 0.984 | 0.984 | 0.694 | 1.26x | 18.2/25.6/28.4% | 1.8/5.4% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.922 | 0.916 | 0.006 | - | - | 0.984 | 0.984 | 0.713 | 1.30x | 18.7/26.3/29.3% | 1.8/5.5% | 3 |
| heard | 1 | 0.923 | 0.915 | 0.007 | - | - | 0.985 | 0.986 | 0.729 | 1.29x | 18.7/26.2/29.0% | 1.8/5.5% | 3 |

> replay-ordering=heard: misdecodes 19

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| enum | 1 | 0.919 | 0.917 | 0.002 | - | - | 0.987 | 0.987 | 0.697 | 1.28x | 18.5/25.9/28.9% | 1.8/5.4% | 3 |
| hybrid | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.985 | 0.987 | 0.710 | 1.28x | 18.6/26.2/28.9% | 1.8/5.4% | 3 |
| 6 | 1 | 0.916 | 0.912 | 0.004 | - | - | 0.983 | 0.983 | 0.689 | 1.31x | 19.2/26.9/29.6% | 1.8/5.7% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.914 | 0.913 | 0.000 | - | - | 0.982 | 0.982 | 0.681 | 1.25x | 18.1/25.5/28.2% | 1.7/5.4% | 2 |
| 3 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 5 | 1 | 0.916 | 0.912 | 0.003 | - | - | 0.986 | 0.987 | 0.679 | 1.31x | 18.8/26.5/29.4% | 1.8/5.6% | 5 |
| 8 | 1 | 0.918 | 0.908 | 0.010 | - | - | 0.984 | 0.985 | 0.687 | 1.32x | 18.9/26.7/29.5% | 1.8/5.6% | 8 |

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.914 | 0.913 | 0.000 | - | - | 0.982 | 0.982 | 0.681 | 1.25x | 18.1/25.5/28.2% | 1.7/5.4% | 2 |
| 3 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 5 | 1 | 0.916 | 0.912 | 0.003 | - | - | 0.986 | 0.987 | 0.679 | 1.31x | 18.8/26.5/29.4% | 1.8/5.6% | 5 |
| 8 | 1 | 0.918 | 0.908 | 0.010 | - | - | 0.984 | 0.985 | 0.687 | 1.32x | 18.9/26.7/29.5% | 1.8/5.6% | 8 |

> faster: 0.942 s per simulated hour against 2.19 over 74 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| True | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.914 | 0.912 | 0.002 | - | - | 0.982 | 0.983 | 0.688 | 1.17x | 17.0/23.8/26.4% | 1.6/4.9% | 3 |
| 1 | 1 | 0.923 | 0.921 | 0.002 | - | - | 0.987 | 0.988 | 0.731 | 1.18x | 17.1/24.1/26.7% | 1.6/5.0% | 3 |
| 2 | 1 | 0.917 | 0.915 | 0.002 | - | - | 0.982 | 0.983 | 0.727 | 1.18x | 17.1/24.1/26.7% | 1.6/5.0% | 3 |
| 4 | 1 | 0.921 | 0.919 | 0.001 | - | - | 0.986 | 0.986 | 0.725 | 1.17x | 16.9/23.9/26.4% | 1.6/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.915 | 0.914 | 0.002 | - | - | 0.982 | 0.982 | 0.715 | 1.27x | 18.4/25.8/28.7% | 1.8/5.4% | 3 |
| 24 | 1 | 0.921 | 0.919 | 0.001 | - | - | 0.988 | 0.988 | 0.711 | 1.26x | 18.4/25.7/28.4% | 1.7/5.4% | 3 |
| 32 | 1 | 0.920 | 0.919 | 0.002 | - | - | 0.987 | 0.987 | 0.698 | 1.26x | 18.3/25.8/28.6% | 1.7/5.4% | 3 |
| 64 | 1 | 0.915 | 0.913 | 0.002 | - | - | 0.985 | 0.985 | 0.691 | 1.27x | 18.5/26.0/28.7% | 1.8/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.916 | 0.913 | 0.003 | - | - | 0.985 | 0.986 | 0.697 | 1.35x | 19.3/27.4/30.6% | 1.9/5.8% | 3 |
| 16 | 1 | 0.918 | 0.916 | 0.003 | - | - | 0.989 | 0.989 | 0.699 | 1.27x | 18.6/26.1/28.9% | 1.8/5.5% | 3 |
| 32 | 1 | 0.910 | 0.909 | 0.001 | - | - | 0.979 | 0.979 | 0.687 | 1.27x | 18.4/25.8/28.5% | 1.8/5.4% | 3 |

> window-size=8: misdecodes 88

> window-size=16: misdecodes 64

> window-size=32: misdecodes 31

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.996 | 0.997 | 0.797 | 2.02x | 23.7/38.9/42.6% | 1.3/5.0% | 3 |
| True | 1 | 0.736 | 0.728 | 0.008 | - | - | 0.849 | 0.898 | 0.558 | 5.50x | 59.5/75.9/78.7% | 3.9/12.7% | 3 |

> no-congestion-scaling=True: queue drops 16.4% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 83

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.522 | 0.516 | 0.006 | - | - | 0.622 | 0.622 | 0.226 | 4.41x | 15.6/26.0/37.1% | 1.5/4.8% | 3 |
| truesize | 1 | 0.558 | 0.551 | 0.007 | - | - | 0.659 | 0.660 | 0.250 | 3.24x | 11.8/19.8/27.4% | 1.1/3.8% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.968 | 0.965 | 0.002 | - | - | 0.999 | 0.999 | 0.789 | 1.90x | 22.1/36.3/39.9% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.996 | 0.997 | 0.797 | 2.02x | 23.7/38.9/42.6% | 1.3/5.0% | 3 |

